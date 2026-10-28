# AI CAD Review

> **AI-Powered CAD Design, Manufacturing, Weldment & 2D Drawing Review Platform**  
> *Automated multi-agent engineering review of 3D CAD assemblies and 2D mechanical drawings against industry standards (ASME, AWS, ISO, DIN).*

---

## 📌 Overview

**AI CAD Review** is an enterprise-grade engineering inspection and automated review workspace. It combines interactive 3D WebGL visualization, high-precision 2D vector drawing inspection, multi-agent AI review pipelines, and standards-based RAG (Retrieval-Augmented Generation) knowledge bases to identify manufacturability, assembly, welding, and consistency defects before production release.

```
       ┌────────────────────────┐      ┌─────────────────────────┐
       │ 3D CAD Viewer Inputs   │      │   2D Engineering DWGs   │
       │ STEP/STL/OBJ/GLTF/GLB  │      │ (.pdf, .dxf, .dwg, .zip)│
       └───────────┬────────────┘      └────────────┬────────────┘
                   │                                │
                   ▼                                ▼
       ┌─────────────────────────────────────────────────────────┐
       │              CAD Adapter & Normalization Layer           │
       │    (PTC Creo, SolidWorks, Siemens NX, Neutral B-Rep)     │
       └───────────────────────────┬─────────────────────────────┘
                                   │
                   ┌───────────────┴───────────────┐
                   ▼                               ▼
       ┌────────────────────────┐      ┌─────────────────────────┐
       │   14 CAD Review Agents │      │ 11 Drawing & DFM Agents │
       │  • Interference & Clash│      │  • Structure & Metadata │
       │  • Weld Sizing (AWS)   │      │  • Title Block & Notes  │
       │  • Fastener Engagement │      │  • CAD/Drawing Sync     │
       │  • Sheet Metal Bends   │      │  • DFM Process Rules    │
       └───────────┬────────────┘      └────────────┬────────────┘
                   │                                │
                   └───────────────┬────────────────┘
                                   ▼
       ┌─────────────────────────────────────────────────────────┐
       │               Standards RAG Knowledge Base              │
       │    ASME Y14.5 • AWS D1.1 • ISO 2768 • DIN 6935 • AWS A2.4│
       └───────────────────────────┬─────────────────────────────┘
                                   │
                                   ▼
       ┌─────────────────────────────────────────────────────────┐
       │     Interactive CAD Desktop UI & Human Sign-Off         │
       │     HTML / Excel / JSON Engineering Audit Reports       │
       └─────────────────────────────────────────────────────────┘
```

---

## ✨ Key Features

### 1. Interactive 3D CAD Viewer
- **Open and inspect supported 3D files**: STEP/STP, STL, OBJ, GLTF, and GLB files can be opened from the file picker or by drag-and-drop.
- **Native CAD limitation**: Proprietary CAD files generally require export to STEP or a supported mesh format. Adapter classes for Creo, SolidWorks, CATIA, NX, and Inventor currently provide stubs/demo data, not native CAD runtime integrations. The `.prt` extension is ambiguous between Creo and NX, and filename-only detection currently defaults it to Creo.
- **Interactive Three.js viewer**: Orbit, pan, zoom, and select individual imported parts and meshes.
- **Dynamic Sectioning**: Live orthogonal cutting planes (X, Y, Z axes) with slider offset adjustment.
- **3D Measurement Caliper**: Point-to-point distance measurement with $\Delta X, \Delta Y, \Delta Z$ readouts.
- **Interactive View Cube & Triad**: Instant isometric, top, front, right, and oblique orthographic views.
- **Visual Defect Highlighting**: Pinpoint critical clashes, undersized welds, and clearance violations directly in 3D space.

### 2. Multi-Sheet 2D Vector Drawing Viewer
- **Vector Canvas**: Smooth pan and zoom rendering of engineering drawing sheets.
- **Multi-Sheet Navigation**: Instant toggling between assembly arrangements, detail sheets, and title blocks.
- **Interactive Finding Pins**: Direct visual pinpoints linked to specific issues (weld callout errors, missing drain holes, BOM count mismatches).

### 3. Drawings Input & Ingestion Pipeline
- **Dedicated Drawings Input Button**: Easily accessible from:
  - **Classic Engineering Toolbar**: `📥 Drawings Input` button in the primary File Actions group.
  - **Top Menubar**: `File` > `📥 Drawings Input...` (`Ctrl+D`).
  - **Left Model Tree**: Quick `📥 Input` button directly on the `Drawings` tree node.
  - **Bottom Inspection Dock**: `📥 Drawings Input...` action in the 2D Drawing tab sidebar.
  - **Drag-and-Drop Modal Dropzone**: Interactive upload supporting direct drag-and-drop.
- **Accepted Drawing Inputs**: PDF, common raster images, DXF/DWG, native drawing extensions, and ZIP packages are accepted by the validation pipeline. Extraction depth depends on the available parser; the current pipeline has specific PDF text extraction and deterministic demo/model-based handling, not full CAD drawing parsing for every listed format.

### 4. 11-Agent Mechanical Drawing & DFM Review Pipeline
- **Structure Agent**: Extracts title blocks, drawing metadata, and views.
- **Extraction Agent**: Parses dimensions, tolerances, surface finishes, weld symbols, and notes.
- **Consistency Agent**: Cross-verifies 3D CAD dimensions against 2D drawing callouts.
- **DFM Checking Agent**: Evaluates process-specific constraints (laser cutting, CNC milling, sheet metal bending, injection molding).
- **Inspection Agent**: Verifies completeness of inspection criteria and balloon callouts.
- **Rules Engine**: Deterministic compliance checking against engineering standards.
- **Report Generator**: Produces formal evidence-based audit reports.

### 5. Standards RAG Engine
- Built-in retrieval knowledge base covering:
  - **ASME Y14.5-2018**: Engineering Drawing Practices & Tolerancing Conventions.
  - **AWS D1.1:2020**: Structural Welding Code – Minimum Fillet Throat Criteria.
  - **AWS A2.4**: Standard Symbols for Welding, Brazing, and Nondestructive Examination.
  - **ISO 2768-mK**: General Tolerances for Linear & Angular Dimensions.
  - **DIN 6935**: Cold Bending Tangent Distances for Sheet Metal.

### 6. Strict Scope Policy & GD&T Exclusion
- **Deterministic Scope Boundary**: In accordance with system policy, full geometric tolerance verification (datum reference frames, position/profile feature control frames, bonus tolerance stacks) is explicitly flagged as **NOT REVIEWED**, eliminating false positives and maintaining strict evidence traceability.

### 7. Human-in-the-Loop Sign-Off & Disposition
- Formally record engineer dispositions (`Accepted`, `Rejected`, `Requires Correction`, `Requires Further Investigation`) with reviewer name, PE credentials, and timestamped remarks.

---

## 📁 Repository Structure

```
AI Cad Review/
├── app/
│   ├── adapters/            # CAD platform connectors (Creo, SolidWorks, NX, Neutral)
│   ├── agents/              # Multi-agent orchestrators & specialized inspection agents
│   ├── cad_service/         # CAD model normalizer and sample assemblies
│   ├── drawing_review/      # 11-agent mechanical drawing & DFM review pipeline
│   │   ├── consistency_agent.py
│   │   ├── dfm_agent.py
│   │   ├── extraction_agent.py
│   │   ├── inspection_agent.py
│   │   ├── report_generator.py
│   │   ├── review_orchestrator.py
│   │   ├── rules.py
│   │   ├── schemas.py
│   │   └── structure_agent.py
│   ├── models/              # Pydantic schemas (CAD, Findings, Audit, Projects)
│   ├── rag/                 # Standards RAG knowledge base & search index
│   ├── reports/             # HTML, Excel (.xlsx), and JSON report generators
│   ├── routes/              # FastAPI API routes (api.py, chat_api.py, drawing_api.py)
│   ├── services/            # Shared application state and service coordination
│   ├── rules/               # Rule engine & deterministic engineering rule definitions
│   ├── config.py            # Global configuration, thresholds, and scope policies
│   └── main.py              # FastAPI application initialization & static mount
├── static/
│   ├── css/
│   │   └── styles.css       # Enterprise CAD workstation styling system
│   ├── js/
│   │   ├── app.js           # UI logic, state management, upload triggers
│   │   ├── chat.js          # Engineering AI copilot drawer
│   │   ├── viewer2d.js      # Vector 2D drawing canvas renderer & pinpoints
│   │   └── viewer3d.js      # Interactive 3D CAD viewer & HUD controls
│   ├── index.html           # Main CAD Desktop application interface
│   └── presentation.html    # Interactive engineering presentation deck
├── tests/
│   ├── test_acrylic_panel.py   # Test suite for single-part drawing review
│   ├── test_drawing_review.py  # Test suite for 11-agent drawing pipeline
│   └── test_pipeline.py        # Core CAD review pipeline & GD&T exclusion tests
├── requirements.txt         # Python package dependencies
├── run.py                   # Server startup script
├── .gitignore               # Python caches, local secrets, and generated output
└── README.md                # Project documentation
```

### Frontend and backend responsibilities

- `static/` contains the browser application: `index.html`, stylesheets, JavaScript, and browser-side CAD libraries.
- `app/routes/` defines the `/api` endpoints. Route handlers call the application services and review pipelines.
- `app/services/review_state.py` owns one shared `ReviewState` object containing the active CAD model, findings, rule engine, and standards index. Routes read and update its fields so chat, drawing review, and reports see the same active project.
- The dashboard's **DFM Review** toolbar action opens a process selector for sheet metal, CNC machining/turning, or injection molding. It calls `POST /api/dfm/review`, reports model feature evidence, and lists unavailable checks explicitly.
- `app/agents/`, `app/drawing_review/`, `app/rules/`, `app/adapters/`, and `app/reports/` contain backend review logic, integrations, and report generation.
- `run.py` starts the FastAPI application in `app/main.py`, which serves the frontend at `/` and assets under `/static/`.

Generated Python bytecode and test caches are local artifacts and are excluded by `.gitignore`.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (Python 3.10 or 3.11 recommended)
- A modern WebGL-compatible browser (Chrome, Edge, Firefox, or Safari)

### Installation

1. **Clone or navigate to the repository directory:**
   ```bash
   cd "AI Cad Review"
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux / macOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables (optional):**
   Create a `.env` file from `.env.example`:
   ```bash
   copy .env.example .env
   ```
Configure optional keys (e.g. `GEMINI_API_KEY` for Gemini-assisted drawing extraction and standards embeddings). Without a key, the application uses its local fallback paths. `HOST`, `PORT`, and `APP_ENV` control server startup; reload is enabled when `APP_ENV=development`.

---

## 🖥️ Running the Application

Start the local server using `run.py`:

```bash
python run.py
```

Or run via Uvicorn directly:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Once started:
- **CAD Desktop Application**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Interactive Presentation Deck**: [http://127.0.0.1:8000/static/presentation.html](http://127.0.0.1:8000/static/presentation.html)
- **Interactive API Documentation (Swagger UI)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative API Documentation (ReDoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Tests

Run the comprehensive pytest suite:

```bash
# Windows Command Prompt
set PYTHONPATH=. && pytest -v

# Windows PowerShell
$env:PYTHONPATH="."; pytest -v

# Linux / macOS
PYTHONPATH=. pytest -v
```

The test suite validates:
1. CAD assembly normalization and component loading.
2. Strict **Zero GD&T Findings** exclusion verification.
3. Realistic engineering findings across interference, machining, fasteners, and welding.
4. Acrylic panel single-part drawing review validation.
5. Multi-agent drawing review pipeline and report exports.

The PDF text extraction path requires the `pypdf` dependency from `requirements.txt`. Some upload tests use small fixture bytes and validate deterministic metadata handling rather than real PDF parsing.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|:---|:---|
| **`Ctrl + D`** | **Drawings Input** (Open drawing upload selector) |
| **`Ctrl + O`** | Open 3D CAD Model |
| **`Ctrl + S`** | Save Review Session to PLM |
| **`F5`** | Run Full AI Engineering Review |
| **`F`** | Fit Model in 3D Viewport |
| **`Ctrl + I`** | Set Isometric View |
| **`X`** | Toggle Section Cut Plane |
| **`M`** | Toggle 3D Distance Measurement Caliper |
| **`Esc`** | Clear 3D Highlights & Selections |

---

## 🔌 API Endpoints Summary

| Method | Endpoint | Description |
|:---|:---|:---|
| `GET` | `/api/scope` | Returns application scope & strict GD&T policy statements |
| `GET` | `/api/cad/model` | Fetches normalized CAD assembly model for 3D/2D viewers |
| `POST` | `/api/cad/upload` | Ingests native CAD files via adapter factory |
| `POST` | `/api/reviews/run` | Triggers multi-agent engineering review on active CAD assembly |
| `POST` | `/api/dfm/review` | Reviews active model feature data for a selected DFM process |
| `POST` | `/api/drawing/review` | Uploads and reviews mechanical drawing through 11-agent pipeline |
| `POST` | `/api/drawing/run-active` | Executes drawing review on current active project drawing |
| `GET` | `/api/drawing/report` | Retrieves latest structured drawing review findings & summary |
| `POST` | `/api/drawing/signoff` | Submits engineer disposition sign-off record |
| `GET` | `/api/reports/html` | Downloads formal HTML engineering review report |
| `GET` | `/api/reports/excel` | Exports findings audit sheet to Excel (`.xlsx`) |
| `GET` | `/api/reports/json` | Exports structured JSON review report |
| `GET` | `/api/drawing/export/{fmt}` | Exports drawing review report as HTML or Markdown |
| `POST` | `/api/chat` | AI Engineering Assistant conversation endpoint |

---

## 🛡️ Engineering Disclaimer

> **Notice**: AI CAD Review is an advanced engineering assistance and pre-check tool. All AI-generated findings, dimensional checks, weld sizing alerts, and DFM recommendations must be reviewed and dispositioned by a qualified Professional Engineer (PE) or designated CAD Checker prior to formal design release or manufacturing commitment.
