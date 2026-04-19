# UK PSC (People with Significant Control) sample data from Companies House
UK_PSC_ORIGINAL = {
    "company_number": "12345678",
    "data": {
        "company_name": "GREENFIELD ENERGY HOLDINGS LTD",
        "company_number": "12345678",
        "registered_office_address": {
            "address_line_1": "71-75 Shelton Street",
            "address_line_2": "Covent Garden",
            "locality": "London",
            "postal_code": "WC2H 9JQ",
            "country": "United Kingdom",
        },
        "sic_codes": ["35110"],
        "date_of_creation": "2019-03-12",
        "type": "ltd",
        "jurisdiction": "england-wales",
        "persons_with_significant_control": [
            {
                "kind": "individual-person-with-significant-control",
                "name": "Mrs Sarah Elizabeth Turner",
                "name_elements": {
                    "title": "Mrs",
                    "forename": "Sarah",
                    "middle_name": "Elizabeth",
                    "surname": "Turner",
                },
                "nationality": "British",
                "country_of_residence": "England",
                "address": {
                    "premises": "71-75",
                    "address_line_1": "Shelton Street",
                    "locality": "London",
                    "postal_code": "WC2H 9JQ",
                    "country": "United Kingdom",
                },
                "date_of_birth": {"month": 6, "year": 1982},
                "notified_on": "2019-03-12",
                "natures_of_control": [
                    "ownership-of-shares-75-to-100-percent",
                    "voting-rights-75-to-100-percent",
                    "right-to-appoint-and-remove-directors",
                ],
            },
            {
                "kind": "corporate-entity-person-with-significant-control",
                "name": "GREENFIELD VENTURES LLP",
                "address": {
                    "premises": "20",
                    "address_line_1": "Fenchurch Street",
                    "locality": "London",
                    "postal_code": "EC3M 3BY",
                    "country": "United Kingdom",
                },
                "identification": {
                    "legal_authority": "Companies Act 2006",
                    "legal_form": "Limited Liability Partnership",
                    "place_registered": "England And Wales",
                    "registration_number": "OC456789",
                    "country_registered": "United Kingdom",
                },
                "notified_on": "2020-06-15",
                "natures_of_control": [
                    "significant-influence-or-control",
                ],
            },
        ],
    },
}

# UK PSC data mapped to BODS 0.4
UK_BODS = [
    {
        "statementId": "f1a2b3c4-d5e6-7890-abcd-ef0123456001",
        "declarationSubject": "uk-entity-greenfield-energy",
        "recordId": "uk-entity-greenfield-energy",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "GREENFIELD ENERGY HOLDINGS LTD",
            "jurisdiction": {"name": "United Kingdom", "code": "GB"},
            "identifiers": [
                {
                    "id": "12345678",
                    "scheme": "GB-COH",
                    "schemeName": "Companies House",
                }
            ],
            "addresses": [
                {
                    "type": "registered",
                    "address": "71-75 Shelton Street, Covent Garden, London",
                    "postCode": "WC2H 9JQ",
                    "country": {"name": "United Kingdom", "code": "GB"},
                }
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — UK PSC mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from UK Companies House People with Significant Control (PSC) register",
            "url": "https://find-and-update.company-information.service.gov.uk/",
        },
    },
    {
        "statementId": "f1a2b3c4-d5e6-7890-abcd-ef0123456002",
        "declarationSubject": "uk-entity-greenfield-energy",
        "recordId": "uk-person-sarah-turner",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "Mrs Sarah Elizabeth Turner",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "British", "code": "GB"}],
            "birthDate": "1982-06",
            "addresses": [
                {
                    "type": "service",
                    "address": "71-75 Shelton Street, London",
                    "postCode": "WC2H 9JQ",
                    "country": {"name": "United Kingdom", "code": "GB"},
                }
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — UK PSC mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from UK Companies House PSC register",
            "url": "https://find-and-update.company-information.service.gov.uk/",
        },
    },
    {
        "statementId": "f1a2b3c4-d5e6-7890-abcd-ef0123456003",
        "declarationSubject": "uk-entity-greenfield-energy",
        "recordId": "uk-entity-greenfield-ventures",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "GREENFIELD VENTURES LLP",
            "jurisdiction": {"name": "United Kingdom", "code": "GB"},
            "identifiers": [
                {
                    "id": "OC456789",
                    "scheme": "GB-COH",
                    "schemeName": "Companies House",
                }
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — UK PSC mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from UK Companies House PSC register",
            "url": "https://find-and-update.company-information.service.gov.uk/",
        },
    },
    {
        "statementId": "f1a2b3c4-d5e6-7890-abcd-ef0123456004",
        "declarationSubject": "uk-entity-greenfield-energy",
        "recordId": "uk-rel-sarah-greenfield",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "uk-entity-greenfield-energy",
            "interestedParty": "uk-person-sarah-turner",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"minimum": 75, "maximum": 100},
                    "startDate": "2019-03-12",
                },
                {
                    "type": "votingRights",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"minimum": 75, "maximum": 100},
                    "startDate": "2019-03-12",
                },
                {
                    "type": "appointmentOfBoard",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "startDate": "2019-03-12",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — UK PSC mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from UK Companies House PSC register",
            "url": "https://find-and-update.company-information.service.gov.uk/",
        },
    },
    {
        "statementId": "f1a2b3c4-d5e6-7890-abcd-ef0123456005",
        "declarationSubject": "uk-entity-greenfield-energy",
        "recordId": "uk-rel-ventures-greenfield",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "uk-entity-greenfield-energy",
            "interestedParty": "uk-entity-greenfield-ventures",
            "interests": [
                {
                    "type": "otherInfluenceOrControl",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "startDate": "2020-06-15",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — UK PSC mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from UK Companies House PSC register",
            "url": "https://find-and-update.company-information.service.gov.uk/",
        },
    },
]

# French RNE (Registre National des Entreprises) beneficial ownership data
# Based on the INPI API: https://entreprise.api.gouv.fr/catalogue/inpi/rne/beneficiaires_effectifs
FRANCE_ORIGINAL = {
    "data": [
        {
            "uuid": "21120ee0-d42b-44f6-a462-d3724cf6aeaf",
            "nom": "Dupont",
            "nom_usage": None,
            "prenoms": ["Marie", "Claire"],
            "date_naissance": {"annee": 1975, "mois": 3},
            "nationalite": "Française",
            "pays_residence": "France",
            "modalites_de_controle": {
                "detention_de_capital": {
                    "parts_directes": {
                        "pourcentage": 51.0,
                        "modalites": {
                            "pleine_propriete": True,
                            "nue_propriete": False,
                        },
                    },
                    "parts_indirectes": {
                        "pourcentage": 10.0,
                        "modalites": {
                            "pleine_propriete": False,
                            "nue_propriete": True,
                        },
                        "details_parts_indirectes": {
                            "via_indivision": False,
                            "via_personne_morale": True,
                            "details_en_personne_morale": [
                                {
                                    "denomination": "SCI DUPONT PATRIMOINE",
                                    "siren": "987654321",
                                }
                            ],
                        },
                    },
                },
                "detention_de_droits_de_vote": {
                    "parts_directes": {
                        "pourcentage": 51.0,
                        "modalites": {
                            "pleine_propriete": True,
                            "nue_propriete": False,
                        },
                    },
                    "parts_indirectes": {
                        "pourcentage": 10.0,
                        "modalites": {
                            "pleine_propriete": False,
                            "nue_propriete": True,
                        },
                    },
                },
                "pouvoirs_de_controle": {
                    "decision_ag": True,
                    "nomination_membres_conseil_administration": False,
                },
                "representant_legal": False,
            },
        },
        {
            "uuid": "c8f3a912-7b5e-4d1a-9c6f-e82b4a1f5d3e",
            "nom": "Martin",
            "nom_usage": None,
            "prenoms": ["Jean", "Pierre"],
            "date_naissance": {"annee": 1968, "mois": 11},
            "nationalite": "Française",
            "pays_residence": "France",
            "modalites_de_controle": {
                "detention_de_capital": {
                    "parts_directes": {
                        "pourcentage": 30.0,
                        "modalites": {
                            "pleine_propriete": True,
                            "nue_propriete": False,
                        },
                    },
                    "parts_indirectes": None,
                },
                "detention_de_droits_de_vote": {
                    "parts_directes": {
                        "pourcentage": 30.0,
                        "modalites": {
                            "pleine_propriete": True,
                            "nue_propriete": False,
                        },
                    },
                    "parts_indirectes": None,
                },
                "pouvoirs_de_controle": {
                    "decision_ag": False,
                    "nomination_membres_conseil_administration": False,
                },
                "representant_legal": True,
            },
        },
    ],
    "meta": {
        "nombre_beneficiaires": 2,
        "uuids_beneficiaires_sans_modalites": [],
    },
    "links": {
        "unite_legale": "https://entreprise.api.gouv.fr/v3/inpi/rne/unites_legales/123456789",
    },
}

# French RNE data mapped to BODS 0.4
FRANCE_BODS = [
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd01",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-entity-sarl-dupont",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "SARL DUPONT TECHNOLOGIES",
            "jurisdiction": {"name": "France", "code": "FR"},
            "identifiers": [
                {
                    "id": "123456789",
                    "scheme": "FR-RCS",
                    "schemeName": "Registre du Commerce et des Sociétés (SIREN)",
                }
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE (Registre National des Entreprises) via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd02",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-entity-sci-dupont",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "SCI DUPONT PATRIMOINE",
            "jurisdiction": {"name": "France", "code": "FR"},
            "identifiers": [
                {
                    "id": "987654321",
                    "scheme": "FR-RCS",
                    "schemeName": "Registre du Commerce et des Sociétés (SIREN)",
                }
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd03",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-person-marie-dupont",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "Marie Claire Dupont",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "French", "code": "FR"}],
            "birthDate": "1975-03",
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd04",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-person-jean-martin",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "Jean Pierre Martin",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "French", "code": "FR"}],
            "birthDate": "1968-11",
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd05",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-rel-dupont-direct",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "fr-entity-sarl-dupont",
            "interestedParty": "fr-person-marie-dupont",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 51},
                    "startDate": "2024-01-01",
                },
                {
                    "type": "shareholding",
                    "directOrIndirect": "indirect",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 10},
                    "startDate": "2024-01-01",
                },
                {
                    "type": "votingRights",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 51},
                    "startDate": "2024-01-01",
                },
                {
                    "type": "votingRights",
                    "directOrIndirect": "indirect",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 10},
                    "startDate": "2024-01-01",
                },
                {
                    "type": "otherInfluenceOrControl",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "startDate": "2024-01-01",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd06",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-rel-sci-sarl",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "fr-entity-sarl-dupont",
            "interestedParty": "fr-entity-sci-dupont",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "share": {"exact": 10},
                    "startDate": "2024-01-01",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-1234-567890abcd07",
        "declarationSubject": "fr-entity-sarl-dupont",
        "recordId": "fr-rel-martin-direct",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "fr-entity-sarl-dupont",
            "interestedParty": "fr-person-jean-martin",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 30},
                    "startDate": "2024-01-01",
                },
                {
                    "type": "votingRights",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 30},
                    "startDate": "2024-01-01",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — France RNE mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from French RNE via INPI API",
            "url": "https://data.inpi.fr/",
        },
    },
]

# Indonesian sample data in original AHU API format
INDONESIA_ORIGINAL = {
    "status": 200,
    "message": "Berhasil mendapatkan data",
    "data": {
        "nama_perseroan": "PT MAJU BERSAMA SEJAHTERA",
        "no_sk": "AHU-0012345.AH.01.01.TAHUN 2020",
        "tgl_sk": "2020-03-15",
        "alamat": "Jl. Sudirman No. 45, RT 001/RW 005, Kel. Senayan, Kec. Kebayoran Baru",
        "kota": "Jakarta Selatan",
        "propinsi": "DKI Jakarta",
        "kode_pos": "12190",
        "npwp": "01.234.567.8-012.000",
        "status_bo": "Sudah Lapor",
        "beneficiary_owner": [
            {
                "nama_bo": "Budi Santoso",
                "nik": "3171012345670001",
                "tempat_lahir": "Jakarta",
                "tgl_lahir": "1975-08-20",
                "alamat_bo": "Jl. Gatot Subroto No. 12, Jakarta Selatan",
                "kewarganegaraan": "Indonesia",
                "npwp_bo": "09.876.543.2-012.000",
                "kriteria_bo": "memiliki saham lebih dari 25%",
                "persentase_saham": 60,
                "persentase_hak_suara": 60,
                "persentase_dividen": 60,
            },
            {
                "nama_bo": "Siti Rahayu",
                "nik": "3171012345670002",
                "tempat_lahir": "Bandung",
                "tgl_lahir": "1980-12-05",
                "alamat_bo": "Jl. Thamrin No. 88, Jakarta Pusat",
                "kewarganegaraan": "Indonesia",
                "npwp_bo": "08.765.432.1-012.000",
                "kriteria_bo": "memiliki saham lebih dari 25%",
                "persentase_saham": 40,
                "persentase_hak_suara": 40,
                "persentase_dividen": 40,
            },
        ],
    },
}

# The same Indonesian data mapped to BODS 0.4
INDONESIA_BODS = [
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-ef0123456789",
        "declarationSubject": "idn-entity-pt-maju-bersama-sejahtera",
        "recordId": "idn-entity-pt-maju-bersama-sejahtera",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "PT MAJU BERSAMA SEJAHTERA",
            "jurisdiction": {"name": "Indonesia", "code": "ID"},
            "identifiers": [
                {
                    "id": "AHU-0012345.AH.01.01.TAHUN 2020",
                    "schemeName": "Keputusan Menteri Hukum dan HAM (SK Kemenkumham)",
                },
                {
                    "id": "01.234.567.8-012.000",
                    "schemeName": "Nomor Pokok Wajib Pajak (NPWP)",
                },
            ],
            "addresses": [
                {
                    "type": "registered",
                    "address": "Jl. Sudirman No. 45, RT 001/RW 005, Kel. Senayan, Kec. Kebayoran Baru",
                    "postCode": "12190",
                    "country": {"name": "Indonesia", "code": "ID"},
                }
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Indonesia mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from AHU (Administrasi Hukum Umum) beneficial ownership register, Ministry of Law and Human Rights, Republic of Indonesia",
            "url": "https://ahu.go.id",
        },
    },
    {
        "statementId": "b2c3d4e5-f6a1-7890-abcd-ef1234567890",
        "declarationSubject": "idn-entity-pt-maju-bersama-sejahtera",
        "recordId": "idn-person-budi-santoso",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "Budi Santoso",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "Indonesia", "code": "ID"}],
            "birthDate": "1975-08-20",
            "addresses": [
                {
                    "type": "residence",
                    "address": "Jl. Gatot Subroto No. 12, Jakarta Selatan",
                    "country": {"name": "Indonesia", "code": "ID"},
                }
            ],
            "identifiers": [
                {
                    "id": "3171012345670001",
                    "scheme": "IDN-NIK",
                    "schemeName": "Nomor Induk Kependudukan (NIK)",
                },
                {
                    "id": "09.876.543.2-012.000",
                    "scheme": "IDN-NPWP",
                    "schemeName": "Nomor Pokok Wajib Pajak (NPWP)",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Indonesia mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from AHU beneficial ownership register",
            "url": "https://ahu.go.id",
        },
    },
    {
        "statementId": "c3d4e5f6-a1b2-7890-abcd-ef2345678901",
        "declarationSubject": "idn-entity-pt-maju-bersama-sejahtera",
        "recordId": "idn-person-siti-rahayu",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "Siti Rahayu",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "Indonesia", "code": "ID"}],
            "birthDate": "1980-12-05",
            "addresses": [
                {
                    "type": "residence",
                    "address": "Jl. Thamrin No. 88, Jakarta Pusat",
                    "country": {"name": "Indonesia", "code": "ID"},
                }
            ],
            "identifiers": [
                {
                    "id": "3171012345670002",
                    "scheme": "IDN-NIK",
                    "schemeName": "Nomor Induk Kependudukan (NIK)",
                },
                {
                    "id": "08.765.432.1-012.000",
                    "scheme": "IDN-NPWP",
                    "schemeName": "Nomor Pokok Wajib Pajak (NPWP)",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Indonesia mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from AHU beneficial ownership register",
            "url": "https://ahu.go.id",
        },
    },
    {
        "statementId": "d4e5f6a1-b2c3-7890-abcd-ef3456789012",
        "declarationSubject": "idn-entity-pt-maju-bersama-sejahtera",
        "recordId": "idn-rel-budi-ptmaju",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "idn-entity-pt-maju-bersama-sejahtera",
            "interestedParty": "idn-person-budi-santoso",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 60},
                    "startDate": "2020-03-15",
                },
                {
                    "type": "votingRights",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 60},
                    "startDate": "2020-03-15",
                },
                {
                    "type": "rightsToProfitOrIncome",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 60},
                    "startDate": "2020-03-15",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Indonesia mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from AHU beneficial ownership register",
            "url": "https://ahu.go.id",
        },
    },
    {
        "statementId": "e5f6a1b2-c3d4-7890-abcd-ef4567890123",
        "declarationSubject": "idn-entity-pt-maju-bersama-sejahtera",
        "recordId": "idn-rel-siti-ptmaju",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "idn-entity-pt-maju-bersama-sejahtera",
            "interestedParty": "idn-person-siti-rahayu",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 40},
                    "startDate": "2020-03-15",
                },
                {
                    "type": "votingRights",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 40},
                    "startDate": "2020-03-15",
                },
                {
                    "type": "rightsToProfitOrIncome",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 40},
                    "startDate": "2020-03-15",
                },
            ],
        },
        "statementDate": "2024-06-01",
        "publicationDetails": {
            "publicationDate": "2024-06-01T00:00:00Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Indonesia mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from AHU beneficial ownership register",
            "url": "https://ahu.go.id",
        },
    },
]

# Official BODS 0.4 mixed direct/indirect ownership example from the standard
MIXED_OWNERSHIP = [
    {
        "statementId": "4fa965df-63a5-48c7-9a2f-7b058981fe60",
        "declarationSubject": "9bfe59b6a869",
        "statementDate": "2018-12-17",
        "publicationDetails": {
            "publicationDate": "2017-12-01",
            "bodsVersion": "0.4",
            "publisher": {"name": "Companies House"},
        },
        "recordId": "9bfe59b6a869",
        "recordStatus": "new",
        "recordType": "entity",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "Company A",
            "identifiers": [{"scheme": "GB-COH", "id": "XE-08-A"}],
        },
    },
    {
        "statementId": "9f188b1a-cb45-4e6b-abe5-252378d6a0f5",
        "declarationSubject": "9bfe59b6a869",
        "statementDate": "2018-12-17",
        "publicationDetails": {
            "publicationDate": "2017-12-01",
            "bodsVersion": "0.4",
            "publisher": {"name": "Companies House"},
        },
        "recordId": "ec61aeda7141",
        "recordStatus": "new",
        "recordType": "entity",
        "recordDetails": {
            "isComponent": True,
            "entityType": {"type": "registeredEntity"},
            "name": "Company B",
            "identifiers": [{"scheme": "GB-COH", "id": "XE-08-B"}],
        },
    },
    {
        "statementId": "6eea4b19-de06-46f2-aa3d-4e346ed3a7c2",
        "declarationSubject": "9bfe59b6a869",
        "statementDate": "2018-12-17",
        "publicationDetails": {
            "publicationDate": "2017-12-01",
            "bodsVersion": "0.4",
            "publisher": {"name": "Companies House"},
        },
        "recordId": "53508b65253f",
        "recordStatus": "new",
        "recordType": "person",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [{"type": "legal", "fullName": "Person 1"}],
            "nationalities": [{"name": "British", "code": "GB"}],
            "birthDate": "1978-08",
        },
    },
    {
        "statementId": "30f1cb63-d849-4550-b6cd-2a6b7268d0cb",
        "source": {"assertedBy": [{"name": "Company A"}]},
        "declarationSubject": "9bfe59b6a869",
        "statementDate": "2018-12-17",
        "publicationDetails": {
            "publicationDate": "2017-12-01",
            "bodsVersion": "0.4",
            "publisher": {"name": "Companies House"},
        },
        "recordId": "07f0f7024a92",
        "recordStatus": "new",
        "recordType": "relationship",
        "recordDetails": {
            "isComponent": True,
            "subject": "9bfe59b6a869",
            "interestedParty": "ec61aeda7141",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "share": {"exact": 50},
                    "startDate": "2017-11-01",
                }
            ],
        },
    },
    {
        "statementId": "f500210d-c8b0-4f74-9bbd-ca762724d0e8",
        "source": {"assertedBy": [{"name": "Company A"}]},
        "declarationSubject": "9bfe59b6a869",
        "statementDate": "2018-12-17",
        "publicationDetails": {
            "publicationDate": "2017-12-01",
            "bodsVersion": "0.4",
            "publisher": {"name": "Companies House"},
        },
        "recordId": "acdf30ece808",
        "recordStatus": "new",
        "recordType": "relationship",
        "recordDetails": {
            "isComponent": True,
            "subject": "ec61aeda7141",
            "interestedParty": "53508b65253f",
            "interests": [
                {"directOrIndirect": "unknown", "beneficialOwnershipOrControl": True}
            ],
        },
    },
    {
        "statementId": "fffad4d7-8263-4dbc-a300-8976bed7790c",
        "source": {"assertedBy": [{"name": "Company A"}]},
        "declarationSubject": "9bfe59b6a869",
        "statementDate": "2018-12-17",
        "publicationDetails": {
            "publicationDate": "2017-12-01",
            "bodsVersion": "0.4",
            "publisher": {"name": "Companies House"},
        },
        "recordId": "f5a45a6daf31",
        "recordStatus": "new",
        "recordType": "relationship",
        "recordDetails": {
            "isComponent": False,
            "subject": "9bfe59b6a869",
            "interestedParty": "53508b65253f",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "indirect",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 50},
                    "startDate": "2017-11-01",
                },
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"exact": 50},
                    "startDate": "2019-05-01",
                },
            ],
            "componentRecords": ["ec61aeda7141", "acdf30ece808", "07f0f7024a92"],
        },
    },
]

# Norwegian Brønnøysund Register Centre (Reelle Rettighetshavere) sample data
# Source: FERD AS (org.nr. 930185930) — real data from Norwegian BO register API
NORWAY_ORIGINAL = {
    "organisasjonsnummer": "930185930",
    "foerstRegistrertIRegisterOverReelleRettighetshavere": "2024-09-26T10:22:02.634Z",
    "registreringer": [
        {
            "registreringsid": "0198c614-dfcc-4e65-bc96-4fdaf2c2c22b",
            "registreringsstatus": {
                "kode": "registreringsstatus.rettighetsinformasjonErRegistrert",
                "kodenavn": "Rettighetsinformasjon er registrert",
            },
            "registrert": "2024-10-08T13:11:28.956Z",
            "erGjeldendeRegistrering": False,
            "reelleRettighetshaverestatus": {
                "kode": "reellerettighetshaverestatus.harReelleRettighetshavere",
                "kodenavn": "Virksomheten har meldt at de har reelle rettighetshavere, og at alle reelle rettighetshavere er identifisert",
            },
            "reelleRettighetshavere": [
                {
                    "folkeregistrertPerson": {
                        "foedselsdato": "1961-07-25",
                        "foedselsaar": "1961",
                        "navn": {
                            "fornavn": "JOHAN HENRIK",
                            "etternavn": "ANDRESEN",
                        },
                        "erDoed": False,
                        "bostedsland": {"landkode": "NOR", "navn": "Norge"},
                        "statsborgerskap": [
                            {"landkode": "NOR", "navn": "Norge"}
                        ],
                    },
                    "erUnntattFraInnsyn": False,
                    "foerstRegistrert": "2024-10-08T13:11:28.657Z",
                    "endret": "2024-10-08T13:11:28.657Z",
                    "posisjoner": [
                        {
                            "posisjonstype": {
                                "kode": "posisjonstype.kontrollOverStemmerettigheter",
                                "kodenavn": "Kontroll over stemmerettigheter",
                            },
                            "stoerrelsesintervall": {
                                "kode": "stoerrelsesintervall.intervall2",
                                "kodenavn": "50% - 74,99%",
                            },
                            "grunnlagstyper": [
                                {
                                    "kode": "grunnlagstype.enighetEllerAvtale",
                                    "kodenavn": "Enighet eller avtale",
                                }
                            ],
                            "mellomliggendeVirksomheter": [],
                        }
                    ],
                },
                {
                    "folkeregistrertPerson": {
                        "foedselsdato": "1995-05-21",
                        "foedselsaar": "1995",
                        "navn": {
                            "fornavn": "KATHARINA",
                            "mellomnavn": "KVASNES",
                            "etternavn": "ANDRESEN",
                        },
                        "erDoed": False,
                        "bostedsland": {"landkode": "NOR", "navn": "Norge"},
                        "statsborgerskap": [
                            {"landkode": "NOR", "navn": "Norge"}
                        ],
                    },
                    "erUnntattFraInnsyn": False,
                    "foerstRegistrert": "2024-10-08T13:11:28.657Z",
                    "endret": "2024-10-08T13:11:28.657Z",
                    "posisjoner": [
                        {
                            "posisjonstype": {
                                "kode": "posisjonstype.eierskap",
                                "kodenavn": "Eierskap",
                            },
                            "stoerrelsesintervall": {
                                "kode": "stoerrelsesintervall.intervall1",
                                "kodenavn": "25,01% - 49,99%",
                            },
                            "grunnlagstyper": [
                                {
                                    "kode": "grunnlagstype.indirekte",
                                    "kodenavn": "Indirekte",
                                }
                            ],
                            "mellomliggendeVirksomheter": [
                                {
                                    "norskVirksomhet": {
                                        "organisasjonsnummer": "921903766"
                                    }
                                }
                            ],
                        }
                    ],
                },
                {
                    "folkeregistrertPerson": {
                        "foedselsdato": "1996-07-23",
                        "foedselsaar": "1996",
                        "navn": {
                            "fornavn": "ALEXANDRA",
                            "etternavn": "ANDRESEN-THOMPSON",
                        },
                        "erDoed": False,
                        "bostedsland": {"landkode": "NOR", "navn": "Norge"},
                        "statsborgerskap": [
                            {"landkode": "NOR", "navn": "Norge"}
                        ],
                    },
                    "erUnntattFraInnsyn": False,
                    "foerstRegistrert": "2024-10-08T13:11:28.657Z",
                    "endret": "2024-10-08T13:11:28.657Z",
                    "posisjoner": [
                        {
                            "posisjonstype": {
                                "kode": "posisjonstype.eierskap",
                                "kodenavn": "Eierskap",
                            },
                            "stoerrelsesintervall": {
                                "kode": "stoerrelsesintervall.intervall1",
                                "kodenavn": "25,01% - 49,99%",
                            },
                            "grunnlagstyper": [
                                {
                                    "kode": "grunnlagstype.indirekte",
                                    "kodenavn": "Indirekte",
                                }
                            ],
                            "mellomliggendeVirksomheter": [
                                {
                                    "norskVirksomhet": {
                                        "organisasjonsnummer": "921903553"
                                    }
                                }
                            ],
                        }
                    ],
                },
            ],
        }
    ],
}

# Norwegian data mapped to BODS 0.4
# FERD AS with 3 beneficial owners: Johan Henrik Andresen (direct voting control),
# Katharina Andresen (indirect ownership via org 921903766),
# Alexandra Andresen-Thompson (indirect ownership via org 921903553)
NORWAY_BODS = [
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor001entity01",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-entity-ferd-as",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "FERD AS",
            "jurisdiction": {"name": "Norway", "code": "NO"},
            "identifiers": [
                {
                    "id": "930185930",
                    "scheme": "NO-BRC",
                    "schemeName": "Brønnøysund Register Centre",
                }
            ],
            "addresses": [
                {
                    "type": "registered",
                    "address": "Strandveien 50, Lysaker",
                    "country": {"name": "Norway", "code": "NO"},
                }
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian Register of Beneficial Owners (Register over reelle rettighetshavere)",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor002entity02",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-entity-intermediary-766",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "Intermediary entity (org.nr. 921903766)",
            "jurisdiction": {"name": "Norway", "code": "NO"},
            "identifiers": [
                {
                    "id": "921903766",
                    "scheme": "NO-BRC",
                    "schemeName": "Brønnøysund Register Centre",
                }
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Intermediary company identified in Norwegian BO register",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor003entity03",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-entity-intermediary-553",
        "recordType": "entity",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "entityType": {"type": "registeredEntity"},
            "name": "Intermediary entity (org.nr. 921903553)",
            "jurisdiction": {"name": "Norway", "code": "NO"},
            "identifiers": [
                {
                    "id": "921903553",
                    "scheme": "NO-BRC",
                    "schemeName": "Brønnøysund Register Centre",
                }
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Intermediary company identified in Norwegian BO register",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor004person001",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-person-johan-andresen",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "JOHAN HENRIK ANDRESEN",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "Norwegian", "code": "NO"}],
            "birthDate": "1961-07-25",
            "addresses": [
                {
                    "type": "residence",
                    "country": {"name": "Norway", "code": "NO"},
                }
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian Register of Beneficial Owners",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor005person002",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-person-katharina-andresen",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "KATHARINA KVASNES ANDRESEN",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "Norwegian", "code": "NO"}],
            "birthDate": "1995-05-21",
            "addresses": [
                {
                    "type": "residence",
                    "country": {"name": "Norway", "code": "NO"},
                }
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian Register of Beneficial Owners",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor006person003",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-person-alexandra-andresen",
        "recordType": "person",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "personType": "knownPerson",
            "names": [
                {
                    "fullName": "ALEXANDRA ANDRESEN-THOMPSON",
                    "type": "legal",
                }
            ],
            "nationalities": [{"name": "Norwegian", "code": "NO"}],
            "birthDate": "1996-07-23",
            "addresses": [
                {
                    "type": "residence",
                    "country": {"name": "Norway", "code": "NO"},
                }
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian Register of Beneficial Owners",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: Johan Henrik Andresen -> FERD AS (direct voting control 50-74.99%)
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor007relat001",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-johan-ferd-voting",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-ferd-as",
            "interestedParty": "nor-person-johan-andresen",
            "interests": [
                {
                    "type": "votingRights",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": True,
                    "share": {"minimum": 50, "maximum": 75},
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian BO register: kontrollOverStemmerettigheter 50%-74.99%",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: Katharina Andresen -> intermediary 921903766 (indirect ownership)
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor008relat002",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-katharina-intermediary",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-intermediary-766",
            "interestedParty": "nor-person-katharina-andresen",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian BO register: indirect ownership via intermediary 921903766",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: intermediary 921903766 -> FERD AS
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor009relat003",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-intermediary766-ferd",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-ferd-as",
            "interestedParty": "nor-entity-intermediary-766",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "share": {"minimum": 25, "maximum": 50},
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Intermediary company ownership in FERD AS (25.01%-49.99%)",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: Katharina Andresen -> FERD AS (indirect ownership 25.01-49.99%)
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor010relat004",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-katharina-ferd-indirect",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-ferd-as",
            "interestedParty": "nor-person-katharina-andresen",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "indirect",
                    "beneficialOwnershipOrControl": True,
                    "share": {"minimum": 25, "maximum": 50},
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian BO register: indirect eierskap 25.01%-49.99%",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: Alexandra Andresen-Thompson -> intermediary 921903553 (indirect ownership)
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor011relat005",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-alexandra-intermediary",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-intermediary-553",
            "interestedParty": "nor-person-alexandra-andresen",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian BO register: indirect ownership via intermediary 921903553",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: intermediary 921903553 -> FERD AS
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor012relat006",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-intermediary553-ferd",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-ferd-as",
            "interestedParty": "nor-entity-intermediary-553",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "direct",
                    "beneficialOwnershipOrControl": False,
                    "share": {"minimum": 25, "maximum": 50},
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Intermediary company ownership in FERD AS (25.01%-49.99%)",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
    # Relationship: Alexandra Andresen-Thompson -> FERD AS (indirect ownership 25.01-49.99%)
    {
        "statementId": "a1b2c3d4-e5f6-7890-abcd-nor013relat007",
        "declarationSubject": "nor-entity-ferd-as",
        "recordId": "nor-rel-alexandra-ferd-indirect",
        "recordType": "relationship",
        "recordStatus": "new",
        "recordDetails": {
            "isComponent": False,
            "subject": "nor-entity-ferd-as",
            "interestedParty": "nor-person-alexandra-andresen",
            "interests": [
                {
                    "type": "shareholding",
                    "directOrIndirect": "indirect",
                    "beneficialOwnershipOrControl": True,
                    "share": {"minimum": 25, "maximum": 50},
                    "startDate": "2024-10-08",
                },
            ],
        },
        "statementDate": "2024-10-08",
        "publicationDetails": {
            "publicationDate": "2024-10-08T13:11:28Z",
            "bodsVersion": "0.4",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "publisher": {"name": "BODS Validator — Norwegian BO register mapping example"},
        },
        "source": {
            "type": ["officialRegister"],
            "description": "Mapped from Norwegian BO register: indirect eierskap 25.01%-49.99%",
            "url": "https://www.brreg.no/reelle-rettighetshavere/",
        },
    },
]

EXAMPLES = [
    {
        "id": "mixed-ownership",
        "title": "Mixed Direct & Indirect Ownership",
        "description": "Official BODS 0.4 example: Person 1 owns Company A both directly (50%) and indirectly via Company B (50%).",
        "valid": True,
        "country": "GB",
        "icon": "bovs-organisation",
        "data": MIXED_OWNERSHIP,
    },
    {
        "id": "uk-psc",
        "title": "UK — Companies House PSC",
        "description": "UK People with Significant Control data (Greenfield Energy Holdings Ltd) mapped from Companies House PSC format to BODS 0.4.",
        "valid": True,
        "country": "GB",
        "icon": "bovs-organisation",
        "has_original": True,
        "original_format": "Companies House PSC (UK)",
        "original_data": UK_PSC_ORIGINAL,
        "data": UK_BODS,
    },
    {
        "id": "france-rne",
        "title": "France — RNE / INPI",
        "description": "French beneficial ownership data (SARL Dupont Technologies) mapped from the RNE register (INPI API) to BODS 0.4, showing direct & indirect capital holdings.",
        "valid": True,
        "country": "FR",
        "icon": "bovs-person",
        "has_original": True,
        "original_format": "RNE / INPI API (France)",
        "original_data": FRANCE_ORIGINAL,
        "data": FRANCE_BODS,
    },
    {
        "id": "indonesia-bods",
        "title": "Indonesia — Mapped to BODS",
        "description": "Indonesian beneficial ownership data (PT Maju Bersama Sejahtera) mapped from the AHU register to BODS 0.4 format.",
        "valid": True,
        "country": "ID",
        "icon": "bovs-person",
        "has_original": True,
        "original_format": "AHU API (Indonesia)",
        "original_data": INDONESIA_ORIGINAL,
        "data": INDONESIA_BODS,
    },
    {
        "id": "norway-brreg",
        "title": "Norway — Brønnøysund Register",
        "description": "Norwegian beneficial ownership data (FERD AS) mapped from the Brønnøysund Register Centre (Reelle Rettighetshavere) to BODS 0.4. Shows direct voting control and indirect ownership via intermediary companies.",
        "valid": True,
        "country": "NO",
        "icon": "bovs-organisation",
        "has_original": True,
        "original_format": "Brønnøysund Register API (Norway)",
        "original_data": NORWAY_ORIGINAL,
        "data": NORWAY_BODS,
    },
    {
        "id": "errors-common",
        "title": "Common Errors Example",
        "description": "Intentionally invalid data to demonstrate validation: missing fields, future dates, and broken references.",
        "valid": False,
        "icon": "bovs-unknown",
        "data": [
            {
                "statementId": "short",
                "recordId": "entity-1",
                "recordType": "entity",
                "recordDetails": {
                    "entityType": {"type": "registeredEntity"},
                    "name": "Bad Data Corp",
                },
                "statementDate": "2030-12-01",
                "publicationDetails": {
                    "publicationDate": "2024-01-15T00:00:00Z",
                    "bodsVersion": "0.4",
                    "license": "https://creativecommons.org/publicdomain/zero/1.0/",
                    "publisher": {"name": "Test"},
                },
            },
            {
                "statementId": "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1",
                "declarationSubject": "entity-1",
                "recordId": "rel-1",
                "recordType": "relationship",
                "recordStatus": "new",
                "recordDetails": {
                    "isComponent": False,
                    "subject": "entity-nonexistent",
                    "interestedParty": "person-nonexistent",
                    "interests": [
                        {
                            "type": "shareholding",
                            "share": {"minimum": 80, "maximum": 20},
                        }
                    ],
                },
                "statementDate": "2024-01-15",
                "publicationDetails": {
                    "publicationDate": "2024-01-15T00:00:00Z",
                    "bodsVersion": "0.4",
                    "license": "https://creativecommons.org/publicdomain/zero/1.0/",
                    "publisher": {"name": "Test"},
                },
                "source": {"type": ["officialRegister"]},
            },
        ],
    },
]


def get_examples():
    return [
        {
            "id": ex["id"],
            "title": ex["title"],
            "description": ex["description"],
            "valid": ex["valid"],
            "country": ex.get("country"),
            "icon": ex.get("icon"),
            "has_original": ex.get("has_original", False),
            "original_format": ex.get("original_format"),
        }
        for ex in EXAMPLES
    ]


def get_example_by_id(example_id):
    for ex in EXAMPLES:
        if ex["id"] == example_id:
            return ex
    return None
