---
stepsCompleted: [1, 2, 3]
inputDocuments:
  - '/home/cgorricho/apps/OFAC/docs/prd.md'
  - '/home/cgorricho/apps/OFAC/docs/ux-design-specification.md'
  - '/home/cgorricho/apps/OFAC/docs/analysis/product-brief-OFAC-20251206.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251205_OFAC_Sanctions_Screening_Tools_Plan.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_List_Update_Policies_and_Strategy.md'
workflowType: 'architecture'
lastStep: 3
project_name: 'OFAC'
user_name: 'Carlos'
date: '2025-12-09'
---

# Architecture Decision Document

**Project:** OFAC Sanctions Screening Tools
**Author:** Carlos
**Date:** 2025-12-09

---

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

## Project Context Analysis

### Requirements Overview

**Functional Requirements Summary:**

The PRD defines 79 functional requirements organized into these core capability areas:

| Area | FR Count | Key Capabilities |
|------|----------|------------------|
| File Processing | 12 | Upload, column detection, validation, batch processing |
| Matching Engine | 18 | Fuzzy matching, country-aware scoring, alias handling |
| Classification Logic | 10 | OK/REVIEW/NOK status, humanitarian context, General License detection |
| OFAC Data Management | 8 | Download, caching, version tracking, atomic updates |
| Reporting & Export | 15 | Excel generation, audit trails, summary statistics |
| User Interface | 16 | Streamlit webapp, status display, match details |

**Non-Functional Requirements Summary:**

53 NFRs drive architectural decisions:

| Category | Critical NFRs | Architectural Impact |
|----------|--------------|---------------------|
| Performance | <30 seconds for 100 entities | In-memory data structures, efficient algorithms |
| Accuracy | Zero false negatives | Conservative matching thresholds, comprehensive alias checking |
| Compliance | 10-year audit trail retention | Structured logging, report archival design |
| Security | Local processing, no cloud data transmission | Standalone deployment, data locality |
| Reliability | Graceful degradation, partial results on error | Error handling strategy, atomic operations |
| Maintainability | Shared matching engine across clients | Modular architecture, API-first design |

**Scale & Complexity:**

- **Primary domain:** API Backend + Web Application (FastAPI + Streamlit)
- **Complexity level:** Medium-High (compliance domain with focused scope)
- **Estimated architectural components:** 6 core modules
- **Data scale:** ~60,000 OFAC records (18K SDN + 20K aliases + 24K addresses)
- **User concurrency:** Single-user (Phase 1), potential multi-tenant (Phase 2)

### Technical Constraints & Dependencies

**Hard Constraints:**

| Constraint | Source | Rationale |
|------------|--------|-----------|
| Python-only stack | PRD, Team Skills | FastAPI, Streamlit, xlwings all Python-based |
| Local processing (Phase 1) | PRD | No cloud dependency for internal MVP |
| OFAC CSV format | Data Analysis | CSV triplets simpler than XML, adequate for needs |
| Streamlit for Phase 1 UI | PRD | Rapid development, Python-native |
| xlwings for Excel UDF | Conceptual Design | Requires Python on user machine |

**Key Dependencies:**

| Dependency | Version | Purpose |
|------------|---------|---------|
| FastAPI | Latest stable | API backend framework |
| Streamlit | ≥1.28.0 | Web application framework |
| RapidFuzz | Latest | Fuzzy string matching |
| Pandas | Latest | Data manipulation, CSV handling |
| xlwings | Latest | Excel custom function integration |
| Pydantic | v2 | Request/response validation |

### Cross-Cutting Concerns Identified

**1. Audit Trail & Compliance**
- Every screening operation must be traceable
- Affects: Matching engine, API layer, reporting, storage
- Implementation: Structured logging with screening_id, timestamp, OFAC version

**2. OFAC Data Lifecycle**
- Consistent data access across all clients
- Affects: Backend API, Streamlit frontend, Excel UDF
- Implementation: Shared data layer with version tracking and atomic updates

**3. Error Handling & Recovery**
- Graceful degradation preserves user work
- Affects: File processing, matching engine, API responses
- Implementation: Partial results on error, clear error messages, retry paths

**4. Configuration Management**
- Centralized settings for thresholds, paths, behavior
- Affects: All components
- Implementation: Environment variables + config file with sensible defaults

**5. Performance Monitoring**
- Identify bottlenecks in matching operations
- Affects: Matching engine primarily
- Implementation: Timing metrics, optional profiling hooks

### UX-Driven Architectural Requirements

From the UX Design Specification:

| UX Requirement | Architectural Implication |
|----------------|--------------------------|
| "Calm Confidence" aesthetic | API responses include all context for transparent display |
| Inline match explanation | Match results include reasoning, not just scores |
| Progressive disclosure | API supports summary and detail endpoints |
| One-click export | Report generation must be fast and complete |
| OFAC data freshness display | Version metadata always available |
| Status-first communication | API returns structured status (OK/REVIEW/NOK) with details |

### Phase-Aware Architecture Considerations

| Phase | Scope | Architectural Focus |
|-------|-------|---------------------|
| Phase 1 (MVP) | Single-user Streamlit app | Simplicity, correctness, local deployment |
| Phase 1.5 | Excel UDF addition | Shared matching engine, consistent behavior |
| Phase 2 | Commercial SaaS | Multi-tenancy, authentication, cloud deployment |

**Phase 1 Simplifications:**
- No authentication required (single user)
- No database required (file-based storage adequate)
- No cloud infrastructure (local deployment)
- No real-time updates (batch processing focus)

**Phase 2 Considerations (Design-ahead but don't implement):**
- Multi-tenant data isolation
- User authentication and authorization
- Cloud-native deployment options
- Horizontal scaling for matching engine

## Technology Foundation

### Primary Technology Stack

| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| Language | Python | 3.11+ | Core runtime |
| Backend Framework | FastAPI | Latest | API server |
| Frontend Framework | Streamlit | ≥1.28.0 | Web application |
| Matching Library | RapidFuzz | Latest | Fuzzy string matching |
| Data Processing | Pandas | Latest | CSV handling, data manipulation |
| Validation | Pydantic | v2 | Request/response schemas |
| Excel Integration | xlwings | Latest | Excel UDF (Phase 1.5) |

### Dependency Management: uv

**Selected Tool:** `uv` - Rust-based Python package installer and resolver

**Rationale:**
- 10-100x faster than pip for installations
- Built-in virtual environment management
- Lock file support for reproducible builds
- Drop-in replacement for pip commands
- Active development by Astral (creators of Ruff)

**Basic Commands:**
```bash
# Create virtual environment
uv venv

# Install dependencies from pyproject.toml
uv pip install -e .

# Add a new dependency
uv pip install fastapi

# Sync from lock file
uv pip sync requirements.lock
```

**Note:** Detailed uv usage guide will be created at `docs/development/uv-guide.md`

### Project Structure

```
OFAC/
├── pyproject.toml           # Project metadata & dependencies
├── .env.example             # Environment variable template
├── .gitignore               # Python-appropriate ignores
│
├── src/
│   └── ofac/
│       ├── __init__.py
│       ├── core/            # Shared core logic
│       │   ├── __init__.py
│       │   ├── matcher.py   # Fuzzy matching engine
│       │   ├── classifier.py # OK/REVIEW/NOK classification
│       │   ├── models.py    # Pydantic data models
│       │   └── config.py    # Configuration management
│       │
│       ├── data/            # OFAC data layer
│       │   ├── __init__.py
│       │   ├── loader.py    # CSV triplet parsing
│       │   ├── updater.py   # Download & version management
│       │   └── cache/       # Cached OFAC CSV files
│       │       ├── sdn/     # SDN list files
│       │       └── version.json
│       │
│       ├── api/             # FastAPI backend
│       │   ├── __init__.py
│       │   ├── main.py      # FastAPI application entry
│       │   ├── routes/      # Endpoint definitions
│       │   │   ├── __init__.py
│       │   │   ├── screening.py  # Batch screening endpoints
│       │   │   ├── single.py     # Single entity check
│       │   │   └── data.py       # OFAC data management
│       │   └── schemas.py   # API request/response models
│       │
│       └── streamlit/       # Streamlit frontend
│           ├── __init__.py
│           ├── app.py       # Main Streamlit application
│           ├── pages/       # Multi-page app structure (if needed)
│           └── components/  # Reusable UI components
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   ├── test_matcher.py      # Matching engine tests
│   ├── test_classifier.py   # Classification logic tests
│   ├── test_api.py          # API endpoint tests
│   └── fixtures/            # Test data files
│
├── scripts/
│   ├── update_ofac.py       # Manual OFAC data update
│   └── generate_report.py   # Standalone report generation
│
└── docs/                    # Documentation (BMAD artifacts + guides)
    ├── development/
    │   └── uv-guide.md      # uv usage instructions
    └── ...
```

### Development Tooling

| Tool | Purpose | Configuration |
|------|---------|---------------|
| uv | Package management | `pyproject.toml` |
| Ruff | Linting + formatting | `pyproject.toml [tool.ruff]` |
| pytest | Testing | `pyproject.toml [tool.pytest]` |
| mypy | Type checking | `pyproject.toml [tool.mypy]` |
| pre-commit | Git hooks | `.pre-commit-config.yaml` |

### pyproject.toml Structure

```toml
[project]
name = "ofac-screening"
version = "0.1.0"
description = "OFAC Sanctions Screening Tools for Humanitarian NGOs"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "streamlit>=1.28.0",
    "pandas>=2.0.0",
    "rapidfuzz>=3.0.0",
    "pydantic>=2.0.0",
    "httpx>=0.26.0",
    "python-multipart>=0.0.6",
    "openpyxl>=3.1.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
    "pre-commit>=3.0.0",
]
excel = [
    "xlwings>=0.30.0",
]

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-v --tb=short"

[tool.mypy]
python_version = "3.11"
strict = true
```

### Development Workflow

**Initial Setup:**
```bash
# Clone repository
git clone <repo-url>
cd OFAC

# Create virtual environment with uv
uv venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Install all dependencies including dev
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

**Daily Development:**
```bash
# Run API server
uvicorn ofac.api.main:app --reload

# Run Streamlit app
streamlit run src/ofac/streamlit/app.py

# Run tests
pytest

# Format and lint
ruff check --fix .
ruff format .
```

### Documentation Deliverable

**Action Item:** Create `docs/development/uv-guide.md` with comprehensive uv instructions including:
- Installation on Linux/Windows/Mac
- Virtual environment management
- Adding/removing dependencies
- Lock file usage
- Troubleshooting common issues
