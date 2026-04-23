# BODS Validator & Visualiser

An online tool for validating beneficial ownership data against the [Beneficial Ownership Data Standard (BODS)](https://standard.openownership.org/en/0.4.0/) v0.4 schema, providing actionable guidance and ownership visualisations.

![BODS Validator](https://img.shields.io/badge/BODS-0.4.0-652eb1) ![Python](https://img.shields.io/badge/Python-3.9+-blue) ![React](https://img.shields.io/badge/React-18-61dafb) ![License](https://img.shields.io/badge/License-MIT-green)

**Live demo:** [bods-validator.onrender.com](https://bods-validator.onrender.com/)

Part of the [BODS Interoperability Toolkit](https://github.com/StephenAbbott/bods-interoperability-toolkit).

## Features

- **Schema Validation** — Validate JSON data against the BODS 0.4 schema using [lib-cove-bods](https://pypi.org/project/libcovebods/), which performs JSON schema validation plus 26 additional compliance checks
- **Actionable Advice** — Get clear guidance on each issue with links to the relevant BODS documentation
- **Ownership Visualisation** — Render interactive ownership diagrams using the [@openownership/bods-dagre](https://github.com/openownership/visualisation-tool) library with [BOVS](https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/) icons and conventions
- **Country Examples** — Real-world examples showing how national beneficial ownership data maps to BODS:
  - 🇬🇧 **UK** — Companies House PSC (People with Significant Control)
  - 🇫🇷 **France** — RNE / INPI (Registre National des Entreprises)
  - 🇮🇩 **Indonesia** — AHU (Administrasi Hukum Umum)
  - 🇳🇴 **Norway** — Brønnøysund Register Centre (Reelle Rettighetshavere)
- **Data Comparison** — Side-by-side views showing original national data formats alongside their BODS 0.4 mappings
- **Multiple Input Methods** — Paste JSON, upload a file, or fetch from a URL

## Quick Start

### Prerequisites

- Python 3.9+
- Node.js 18+

### Setup

```bash
# Clone the repository
git clone https://github.com/StephenAbbott/bods-validator.git
cd bods-validator

# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# Frontend setup
cd frontend
npm install
cd ..
```

### Run

```bash
# Option 1: Use the start script
bash start.sh

# Option 2: Start manually
# Terminal 1 - Backend (port 8000)
cd backend && source venv/bin/activate && uvicorn app.main:app --host 0.0.0.0 --port 8000

# Terminal 2 - Frontend (port 5173)
cd frontend && npm run dev
```

Open **http://localhost:5173** in your browser.

## Architecture

```
bods-validator/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI endpoints
│   │   ├── validator.py     # lib-cove-bods wrapper with advice engine
│   │   └── examples.py      # Country example datasets
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.tsx           # Main application
│   │   ├── api.ts            # API client
│   │   ├── types.ts          # TypeScript interfaces
│   │   └── components/
│   │       ├── InputPanel.tsx          # JSON paste, file upload, URL fetch
│   │       ├── ResultsPanel.tsx        # Validation results with tabs
│   │       ├── ExamplesPanel.tsx       # Country example selector
│   │       ├── VisualisationPanel.tsx  # BOVS ownership diagrams
│   │       └── DataComparisonPanel.tsx # Side-by-side data mapping
│   └── public/
│       └── bods-images/      # BOVS icons (person, organisation, etc.)
└── start.sh
```

**Backend**: FastAPI (Python) — validates BODS data using lib-cove-bods, serves example datasets

**Frontend**: React + Vite + TypeScript + Tailwind CSS v4 — responsive UI with BOVS design system

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/examples` | GET | List available examples |
| `/api/examples/{id}` | GET | Get example data by ID |
| `/api/validate` | POST | Validate JSON data |
| `/api/validate/file` | POST | Validate uploaded file |
| `/api/validate/url` | POST | Validate from URL |

## Design System

The UI follows the [Beneficial Ownership Visualisation System (BOVS)](https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/):

- **Purple** (`#652eb1`) — Ownership relationships
- **Cyan** (`#349aee`) — Control relationships
- BOVS iconography for persons, organisations, arrangements, and states

## Resources

- [BODS 0.4 Standard](https://standard.openownership.org/en/0.4.0/)
- [lib-cove-bods](https://pypi.org/project/libcovebods/) — Python validation library
- [BODS Visualisation Library](https://github.com/openownership/visualisation-tool)
- [BOVS Design System](https://www.openownership.org/en/publications/beneficial-ownership-visualisation-system/)
- [Open Ownership](https://www.openownership.org/)
- [BODS Data](https://bods-data.openownership.org/) — Published BODS datasets

## Acknowledgements

Built using open-source tools from [Open Ownership](https://www.openownership.org/). Country data examples are based on public register formats from the UK (Companies House), France (INPI), Indonesia (AHU/Kemenkumham), and Norway (Brønnøysund Register Centre).

## License

MIT
