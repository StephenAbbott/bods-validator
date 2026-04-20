import { useState } from "react";
import type { ValidationResult } from "../types";

interface Props {
  results: ValidationResult;
}

type Tab = "advice" | "errors" | "checks" | "statistics" | "fields";

export default function ResultsPanel({ results }: Props) {
  const [tab, setTab] = useState<Tab>("advice");

  const errorCount = results.schema_errors.length;
  const checkCount = results.additional_checks.length;
  const fieldCount = results.additional_fields.length;

  const statusColor = results.valid
    ? "bg-green-50"
    : "bg-red-50";
  const statusIcon = results.valid ? "\u2705" : "\u274C";
  const statusText = results.valid
    ? "Valid BODS data"
    : `${errorCount + checkCount} issue${errorCount + checkCount !== 1 ? "s" : ""} found`;

  const tabClass = (t: Tab) =>
    `px-3 py-2 text-sm font-medium rounded-t-lg transition-colors ${
      tab === t
        ? "bg-white border border-b-0"
        : "hover:bg-gray-50"
    }`;

  const badge = (count: number, color: string) =>
    count > 0 ? (
      <span
        className={`ml-1.5 px-1.5 py-0.5 text-xs rounded-full ${color}`}
      >
        {count}
      </span>
    ) : null;

  return (
    <div
      className="bg-white shadow-sm"
      style={{ borderRadius: 10, border: "1px solid var(--oo-rule)" }}
    >
      {/* Summary */}
      <div
        className={`p-4 ${statusColor}`}
        style={{ borderRadius: "10px 10px 0 0", borderBottom: "1px solid var(--oo-rule)" }}
      >
        <div className="flex items-center gap-3">
          <span className="text-2xl">{statusIcon}</span>
          <div>
            <h3 className="font-bold" style={{ color: "var(--oo-navy)" }}>{statusText}</h3>
            <p className="text-sm" style={{ color: "var(--oo-muted)" }}>
              {results.schema_version && `BODS version: ${results.schema_version}`}
              {results.sample_mode && " (sample mode)"}
            </p>
          </div>
        </div>
        {results.error && (
          <p className="mt-2 text-sm text-red-700 bg-red-100 p-2 rounded">
            {results.error}
          </p>
        )}
      </div>

      {/* Tabs */}
      <div className="flex gap-1 px-4 pt-3 overflow-x-auto" style={{ borderBottom: "1px solid var(--oo-rule)" }}>
        <button
          className={tabClass("advice")}
          style={tab === "advice" ? { color: "var(--oo-blue)", borderColor: "var(--oo-rule)" } : { color: "var(--oo-muted)" }}
          onClick={() => setTab("advice")}
        >
          Advice{badge(results.advice.length, "bg-blue-100 text-blue-700")}
        </button>
        <button
          className={tabClass("errors")}
          style={tab === "errors" ? { color: "var(--oo-blue)", borderColor: "var(--oo-rule)" } : { color: "var(--oo-muted)" }}
          onClick={() => setTab("errors")}
        >
          Schema Errors{badge(errorCount, "bg-red-100 text-red-700")}
        </button>
        <button
          className={tabClass("checks")}
          style={tab === "checks" ? { color: "var(--oo-blue)", borderColor: "var(--oo-rule)" } : { color: "var(--oo-muted)" }}
          onClick={() => setTab("checks")}
        >
          Additional Checks{badge(checkCount, "bg-amber-100 text-amber-700")}
        </button>
        <button
          className={tabClass("statistics")}
          style={tab === "statistics" ? { color: "var(--oo-blue)", borderColor: "var(--oo-rule)" } : { color: "var(--oo-muted)" }}
          onClick={() => setTab("statistics")}
        >
          Statistics
        </button>
        {fieldCount > 0 && (
          <button
            className={tabClass("fields")}
            style={tab === "fields" ? { color: "var(--oo-blue)", borderColor: "var(--oo-rule)" } : { color: "var(--oo-muted)" }}
            onClick={() => setTab("fields")}
          >
            Extra Fields{badge(fieldCount, "bg-gray-100 text-gray-700")}
          </button>
        )}
      </div>

      {/* Tab content */}
      <div className="p-4 max-h-[600px] overflow-y-auto">
        {tab === "advice" && <AdviceTab advice={results.advice} />}
        {tab === "errors" && <ErrorsTab errors={results.schema_errors} />}
        {tab === "checks" && <ChecksTab checks={results.additional_checks} />}
        {tab === "statistics" && <StatisticsTab statistics={results.statistics} />}
        {tab === "fields" && <FieldsTab fields={results.additional_fields} />}
      </div>
    </div>
  );
}

function AdviceTab({ advice }: { advice: ValidationResult["advice"] }) {
  if (advice.length === 0)
    return <p style={{ color: "var(--oo-muted)" }} className="text-sm">No advice to show.</p>;
  return (
    <div className="space-y-3">
      {advice.map((a, i) => {
        const colors = {
          error: "border-red-200 bg-red-50",
          warning: "border-amber-200 bg-amber-50",
          success: "border-green-200 bg-green-50",
        };
        const icons = { error: "\u274C", warning: "\u26A0\uFE0F", success: "\u2705" };
        return (
          <div key={i} className={`p-3 border ${colors[a.level]}`} style={{ borderRadius: 8 }}>
            <div className="flex items-start gap-2">
              <span>{icons[a.level]}</span>
              <div className="flex-1">
                <p className="font-medium" style={{ color: "var(--oo-ink)" }}>
                  {a.message}
                  {a.count > 1 && (
                    <span
                      className="ml-2 text-xs px-1.5 py-0.5 rounded-full"
                      style={{ background: "var(--oo-rule)", color: "var(--oo-muted)" }}
                    >
                      x{a.count}
                    </span>
                  )}
                </p>
                <p className="text-sm mt-1" style={{ color: "var(--oo-muted)" }}>{a.guidance}</p>
                <a
                  href={a.docs_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-sm hover:underline mt-1 inline-block font-mono"
                  style={{ color: "var(--oo-blue)", fontSize: 12 }}
                >
                  View BODS documentation &rarr;
                </a>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}

function ErrorsTab({ errors }: { errors: ValidationResult["schema_errors"] }) {
  const [expanded, setExpanded] = useState<Set<number>>(new Set());
  if (errors.length === 0)
    return <p style={{ color: "var(--oo-muted)" }} className="text-sm">No schema errors.</p>;

  const toggle = (i: number) => {
    const next = new Set(expanded);
    next.has(i) ? next.delete(i) : next.add(i);
    setExpanded(next);
  };

  return (
    <div className="space-y-2">
      {errors.map((err, i) => (
        <div key={i} className="border border-red-100" style={{ borderRadius: 8 }}>
          <button
            onClick={() => toggle(i)}
            className="w-full p-3 text-left flex items-start gap-2 hover:bg-red-50 transition-colors"
          >
            <span className="text-red-500 mt-0.5">{expanded.has(i) ? "\u25BC" : "\u25B6"}</span>
            <div className="flex-1 min-w-0">
              <p className="text-sm" style={{ color: "var(--oo-ink)" }}>{err.message}</p>
              <p className="text-xs font-mono mt-0.5 truncate" style={{ color: "var(--oo-muted)" }}>
                Path: /{err.path.join("/")}
              </p>
            </div>
            <span className="text-xs bg-red-100 text-red-700 px-2 py-0.5 rounded-full whitespace-nowrap">
              {err.validator}
            </span>
          </button>
          {expanded.has(i) && (
            <div className="px-3 pb-3 text-sm border-t border-red-100">
              <div className="mt-2 space-y-1">
                <p>
                  <span style={{ color: "var(--oo-muted)" }}>Validator:</span>{" "}
                  <code className="text-xs px-1 py-0.5 rounded" style={{ background: "var(--oo-bg)" }}>{err.validator}</code>
                </p>
                <p>
                  <span style={{ color: "var(--oo-muted)" }}>Schema path:</span>{" "}
                  <code className="text-xs px-1 py-0.5 rounded" style={{ background: "var(--oo-bg)" }}>
                    /{err.schema_path.join("/")}
                  </code>
                </p>
                {err.extra?.required_key_which_is_missing && (
                  <p>
                    <span style={{ color: "var(--oo-muted)" }}>Missing field:</span>{" "}
                    <code className="text-xs bg-red-100 px-1 py-0.5 rounded text-red-800">
                      {err.extra.required_key_which_is_missing}
                    </code>
                  </p>
                )}
                {err.instance !== undefined && (
                  <div>
                    <span style={{ color: "var(--oo-muted)" }}>Value:</span>
                    <pre className="text-xs p-2 rounded mt-1 overflow-x-auto" style={{ background: "var(--oo-bg)" }}>
                      {JSON.stringify(err.instance, null, 2)}
                    </pre>
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}

function ChecksTab({ checks }: { checks: ValidationResult["additional_checks"] }) {
  if (checks.length === 0)
    return <p style={{ color: "var(--oo-muted)" }} className="text-sm">All additional checks passed.</p>;
  return (
    <div className="space-y-2">
      {checks.map((check, i) => (
        <div key={i} className="p-3 border border-amber-100 bg-amber-50" style={{ borderRadius: 8 }}>
          <p className="font-medium text-sm" style={{ color: "var(--oo-ink)" }}>
            {check.type.replace(/_/g, " ")}
          </p>
          <pre className="text-xs mt-1 overflow-x-auto" style={{ color: "var(--oo-muted)" }}>
            {JSON.stringify(
              Object.fromEntries(
                Object.entries(check).filter(([k]) => k !== "type")
              ),
              null,
              2
            )}
          </pre>
        </div>
      ))}
    </div>
  );
}

function StatisticsTab({ statistics }: { statistics: Record<string, any> }) {
  if (!statistics || Object.keys(statistics).length === 0)
    return <p style={{ color: "var(--oo-muted)" }} className="text-sm">No statistics available.</p>;

  const renderValue = (val: any): string => {
    if (typeof val === "object" && val !== null) return JSON.stringify(val, null, 2);
    return String(val);
  };

  return (
    <div className="space-y-1">
      {Object.entries(statistics).map(([key, value]) => (
        <div key={key} className="flex justify-between py-2" style={{ borderBottom: "1px solid var(--oo-bg)" }}>
          <span className="text-sm" style={{ color: "var(--oo-muted)" }}>{key.replace(/_/g, " ")}</span>
          <span className="text-sm font-mono" style={{ color: "var(--oo-ink)" }}>
            {typeof value === "object" ? (
              <pre className="text-xs text-right">{renderValue(value)}</pre>
            ) : (
              renderValue(value)
            )}
          </span>
        </div>
      ))}
    </div>
  );
}

function FieldsTab({ fields }: { fields: ValidationResult["additional_fields"] }) {
  if (fields.length === 0)
    return <p style={{ color: "var(--oo-muted)" }} className="text-sm">No additional fields found.</p>;
  return (
    <div className="space-y-2">
      {fields.map((field, i) => (
        <div key={i} className="p-2 rounded" style={{ background: "var(--oo-bg)", border: "1px solid var(--oo-rule)" }}>
          <pre className="text-xs overflow-x-auto">
            {JSON.stringify(field, null, 2)}
          </pre>
        </div>
      ))}
    </div>
  );
}
