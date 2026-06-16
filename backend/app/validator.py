import functools
import json
import tempfile
import os
import libcovebods.schema as _cove_schema
import libcovebods.schema_dir as _cove_schema_dir
from libcovebods.data_reader import DataReader
from libcovebods.config import LibCoveBODSConfig
from libcovebods.schema import SchemaBODS
from libcovebods.jsonschemavalidate import JSONSchemaValidator
from libcovebods.run_tasks import process_additional_checks, TASK_CLASSES, TASK_CLASSES_IN_SAMPLE_MODE
from libcovebods.additionalfields import AdditionalFields

SAMPLE_MODE_THRESHOLD = 1000


def _install_schema_caches():
    """Memoise the BODS schema loaders so the schema is parsed once, not per request.

    For BODS 0.4, ``SchemaBODS._pkg_schema_obj`` is a plain property that calls
    ``schema_registry()`` — reading every schema file from disk and rebuilding
    the jsonschema registry — on *every* access, and it is accessed several
    times per validation. The packaged schema files never change at runtime, so
    we wrap the two loader functions in an ``lru_cache`` keyed on the schema
    directory/component. The cached objects (a ``referencing.Registry`` and
    plain dicts) are only read by lib-cove-bods, so sharing them across requests
    and worker threads is safe. The patch is applied to both the origin module
    and the ``schema`` module that imported the names by value.
    """
    if getattr(_cove_schema_dir, "_bods_schema_cache_installed", False):
        return
    cached_registry = functools.lru_cache(maxsize=16)(_cove_schema_dir.schema_registry)
    cached_file_data = functools.lru_cache(maxsize=64)(
        _cove_schema_dir.get_scheme_file_data
    )
    for _mod in (_cove_schema_dir, _cove_schema):
        _mod.schema_registry = cached_registry
        _mod.get_scheme_file_data = cached_file_data
    _cove_schema_dir._bods_schema_cache_installed = True


_install_schema_caches()

# Build the lib-cove-bods config once and reuse it (it is read-only).
_CONFIG = LibCoveBODSConfig()

ADVICE_MAP = {
    "required": {
        "level": "error",
        "template": "Required field '{field}' is missing at {path}.",
        "guidance": "BODS requires this field to be present in every statement. See the schema reference for which fields are mandatory.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "enum": {
        "level": "error",
        "template": "Invalid value at {path}. Must be one of the allowed values.",
        "guidance": "Check the BODS codelists for valid enumerated values for this field.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "format": {
        "level": "error",
        "template": "Invalid format at {path}.",
        "guidance": "Check that dates use YYYY-MM-DD format and URIs are valid RFC 3986 URIs.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "type": {
        "level": "error",
        "template": "Wrong data type at {path}.",
        "guidance": "The field has an incorrect JSON type (e.g. string where number expected). Check the schema reference.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "minLength": {
        "level": "error",
        "template": "Value too short at {path}.",
        "guidance": "The field value does not meet the minimum length requirement. For statementId, the minimum is 32 characters.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "maxLength": {
        "level": "error",
        "template": "Value too long at {path}.",
        "guidance": "The field value exceeds the maximum length. For statementId, the maximum is 64 characters.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "additionalProperties": {
        "level": "warning",
        "template": "Unexpected property at {path}.",
        "guidance": "This field is not defined in the BODS schema and will be ignored by compliant tools.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "oneOf": {
        "level": "error",
        "template": "Data does not match any valid BODS record type at {path}.",
        "guidance": "Each statement must have a valid recordType ('entity', 'person', or 'relationship') with matching recordDetails.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "duplicate_statement_id": {
        "level": "error",
        "template": "Duplicate statementId found.",
        "guidance": "Each statement must have a globally unique statementId (32-64 characters).",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "statement_date_in_future": {
        "level": "warning",
        "template": "Statement date is in the future.",
        "guidance": "statementDate should represent when the statement was made, not a future date.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "unknown_schema_version_used": {
        "level": "error",
        "template": "Unknown or missing BODS schema version.",
        "guidance": "Include publicationDetails.bodsVersion in your statements. The current version is '0.4'.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "publication_date_in_future": {
        "level": "warning",
        "template": "Publication date is in the future.",
        "guidance": "publicationDate should not be in the future.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "interested_party_not_found": {
        "level": "error",
        "template": "Interested party reference not found in dataset.",
        "guidance": "The interestedParty recordId in a relationship must reference an existing person or entity record.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
    "subject_not_found": {
        "level": "error",
        "template": "Subject reference not found in dataset.",
        "guidance": "The subject recordId in a relationship must reference an existing entity record.",
        "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
    },
}


def _location_of(err):
    """Human-readable path to the data that triggered a schema error."""
    return "/".join(str(p) for p in err.get("path", [])) or "root"


# Cap the number of locations embedded per advice item so a file with
# thousands of identical errors doesn't bloat the response. The full count is
# always preserved separately.
MAX_LOCATIONS_PER_ADVICE = 50


def generate_advice(schema_errors, additional_checks, additional_fields):
    advice = []

    # Group schema errors by (validator, missing-field) so each distinct
    # problem becomes one advice item that lists every place it occurs,
    # rather than collapsing all errors of a type to a single first location.
    error_groups = {}
    for err in schema_errors:
        validator = err.get("validator", "unknown")
        field = err.get("extra", {}).get("required_key_which_is_missing", "")
        key = (validator, field)
        group = error_groups.setdefault(
            key, {"validator": validator, "field": field, "locations": []}
        )
        group["locations"].append(_location_of(err))

    for (validator, field), group in error_groups.items():
        mapping = ADVICE_MAP.get(validator, {
            "level": "error",
            "template": f"Schema validation error ({validator}).",
            "guidance": "Check the BODS schema reference for the correct data structure.",
            "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
        })
        locations = group["locations"]
        first_path = locations[0] if locations else "root"
        advice.append({
            "level": mapping["level"],
            "message": mapping["template"].format(field=field, path=first_path, id=""),
            "guidance": mapping["guidance"],
            "docs_url": mapping["docs_url"],
            "count": len(locations),
            "field": field,
            "locations": locations[:MAX_LOCATIONS_PER_ADVICE],
            "locations_truncated": len(locations) > MAX_LOCATIONS_PER_ADVICE,
        })

    check_counts = {}
    for check in additional_checks:
        check_type = check.get("type", "unknown")
        if check_type not in check_counts:
            check_counts[check_type] = 0
        check_counts[check_type] += 1

    for check_type, count in check_counts.items():
        mapping = ADVICE_MAP.get(check_type, {
            "level": "warning",
            "template": f"Additional check: {check_type.replace('_', ' ')}",
            "guidance": "See the BODS standard documentation for details on this requirement.",
            "docs_url": "https://standard.openownership.org/en/0.4.0/",
        })
        advice.append({
            "level": mapping["level"],
            "message": mapping["template"].format(field="", path="", id=""),
            "guidance": mapping["guidance"],
            "docs_url": mapping["docs_url"],
            "count": count,
        })

    if additional_fields:
        advice.append({
            "level": "warning",
            "message": f"Found {len(additional_fields)} field(s) not defined in the BODS schema.",
            "guidance": "Additional fields are not part of the standard and will be ignored by BODS-compliant tools. Consider mapping them to standard BODS fields.",
            "docs_url": "https://standard.openownership.org/en/0.4.0/schema/reference.html",
            "count": len(additional_fields),
        })

    if not advice:
        advice.append({
            "level": "success",
            "message": "Data is fully compliant with the BODS schema.",
            "guidance": "Your data meets all BODS requirements. Well done!",
            "docs_url": "https://standard.openownership.org/en/0.4.0/",
            "count": 0,
        })

    return advice


def validate_bods_data(data, sample_mode=False):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        temp_path = f.name

    try:
        if isinstance(data, list) and len(data) > SAMPLE_MODE_THRESHOLD:
            sample_mode = True

        data_reader = DataReader(temp_path, sample_mode=sample_mode)
        config = _CONFIG
        schema = SchemaBODS(data_reader, config)

        # 1. JSON Schema validation
        schema_validator = JSONSchemaValidator(schema)
        schema_errors_raw = schema_validator.validate(data_reader)
        schema_errors = [e.json() for e in schema_errors_raw]

        # 2. Additional checks + statistics
        task_classes = TASK_CLASSES_IN_SAMPLE_MODE if sample_mode else TASK_CLASSES
        checks_result = process_additional_checks(
            data_reader, config, schema, task_classes=task_classes
        )

        # 3. Additional fields
        af = AdditionalFields(schema)
        additional_fields = af.process(data_reader)

        valid = (
            len(schema_errors) == 0
            and len(checks_result.get("additional_checks", [])) == 0
        )
        schema_valid = len(schema_errors) == 0

        advice = generate_advice(
            schema_errors,
            checks_result.get("additional_checks", []),
            additional_fields,
        )

        return {
            "valid": valid,
            "schema_valid": schema_valid,
            "schema_version": getattr(schema, "schema_version", "unknown"),
            "sample_mode": sample_mode,
            "schema_errors": schema_errors,
            "additional_checks": checks_result.get("additional_checks", []),
            "additional_fields": additional_fields,
            "statistics": checks_result.get("statistics", {}),
            "advice": advice,
        }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e),
            "error_type": type(e).__name__,
            "schema_errors": [],
            "additional_checks": [],
            "additional_fields": [],
            "statistics": {},
            "advice": [
                {
                    "level": "error",
                    "message": f"Could not process data: {str(e)}",
                    "guidance": "Ensure your data is a valid JSON array of BODS statements.",
                    "docs_url": "https://standard.openownership.org/en/0.4.0/",
                    "count": 0,
                }
            ],
        }
    finally:
        os.unlink(temp_path)
