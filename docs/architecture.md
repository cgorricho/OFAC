---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]
inputDocuments:
  - '/home/cgorricho/apps/OFAC/docs/prd.md'
  - '/home/cgorricho/apps/OFAC/docs/ux-design-specification.md'
  - '/home/cgorricho/apps/OFAC/docs/analysis/product-brief-OFAC-20251206.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251205_OFAC_Sanctions_Screening_Tools_Plan.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_List_Update_Policies_and_Strategy.md'
workflowType: 'architecture'
lastStep: 8
status: 'complete'
completedAt: '2025-12-09'
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

## Core Architectural Decisions

### Decision Priority Analysis

**Critical Decisions (Block Implementation):**
- Data loading strategy (eager load)
- In-memory data structure (Pandas DataFrame)
- Error response format (structured with codes)
- Configuration management (Pydantic Settings)

**Important Decisions (Shape Architecture):**
- Input validation strategy (permissive + auto-healing)
- Logging strategy (comprehensive JSON)
- Session state management (full workflow)
- Deployment entry point (single command)

**Deferred Decisions (Post-MVP):**
- Authentication & authorization (Phase 2)
- Database selection (Phase 2, if needed)
- Cloud deployment strategy (Phase 2)
- Horizontal scaling (Phase 2)

### Data Architecture

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Data Loading** | Eager Load on App Start | Predictable performance; 2-3 second startup acceptable for "instant" first screening |
| **Data Structure** | Pandas DataFrame | Works efficiently with RapidFuzz vectorized operations; simple to maintain |
| **Result Caching** | No Caching | Audit-friendly; always uses current OFAC data; simpler architecture |
| **OFAC Data Location** | Configurable (default: `./data/`) | Explicit path; easy to backup; configurable via Pydantic Settings |

**Data Flow:**
```
App Start → Load OFAC CSVs → Parse to DataFrame → Hold in Memory
                                                         ↓
User Upload → Validate/Clean → Extract Entities → Match Against DataFrame
                                                         ↓
                                              Generate Results → Export
```

### Security & Validation

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Input Validation** | Permissive + Auto-healing | Accept valid rows, auto-fix common issues (whitespace, encoding), warn on skipped rows |
| **OFAC Data Integrity** | Basic Validation | File exists, non-empty, expected columns; HTTPS downloads are trustworthy |
| **Authentication** | None (Phase 1) | Single-user local deployment; deferred to Phase 2 |

**Auto-healing Operations:**
- Trim leading/trailing whitespace from entity names
- Normalize Unicode characters (NFD → NFC)
- Handle common encoding issues (Latin-1 → UTF-8)
- Remove empty rows silently
- Flag malformed rows with clear warnings

### API & Communication Patterns

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **API Style** | REST (FastAPI) | Simple, well-understood; adequate for screening operations |
| **Documentation** | Enhanced OpenAPI with Examples | Pydantic schemas with example values; zero extra effort |
| **Error Format** | Structured with Code | `{"error": {"code": "...", "message": "...", "details": {...}}}` |
| **Logging** | Comprehensive JSON | Structured logs for 10-year audit trail requirement |

**Error Code Categories:**
```python
# Error code prefixes for consistent handling
FILE_*      # File upload/processing errors (FILE_TOO_LARGE, FILE_INVALID_FORMAT)
DATA_*      # Data validation errors (DATA_MISSING_COLUMN, DATA_INVALID_ROW)
OFAC_*      # OFAC data errors (OFAC_DATA_STALE, OFAC_DOWNLOAD_FAILED)
SCREEN_*    # Screening errors (SCREEN_TIMEOUT, SCREEN_PARTIAL_RESULTS)
```

**Logging Structure:**
```json
{
  "timestamp": "2025-12-09T10:30:00Z",
  "level": "INFO",
  "event": "screening_complete",
  "screening_id": "scr_abc123",
  "ofac_version": "2025-12-08",
  "entities_processed": 150,
  "matches": {"ok": 140, "review": 8, "nok": 2},
  "duration_ms": 2340
}
```

### Frontend Architecture

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Framework** | Streamlit ≥1.28.0 | PRD requirement; Python-native; rapid development |
| **Enhancements** | streamlit-extras + minimal CSS | "Tasteful Enhancement" per UX spec |
| **State Management** | Full Workflow State | Tracks upload → mapping → screening → review flow |
| **Multi-page** | Optional (single page adequate for Phase 1) | May add pages for settings/history in Phase 2 |

**Session State Schema:**
```python
st.session_state = {
    "workflow_step": "upload" | "map" | "screen" | "review",
    "uploaded_file": UploadedFile | None,
    "column_mapping": {"name": str, "country": str | None},
    "screening_results": DataFrame | None,
    "ofac_version": str,
    "screening_id": str,
}
```

### Infrastructure & Deployment

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Configuration** | Pydantic Settings | Type-safe; validates on startup; supports env vars + defaults |
| **Deployment** | Single Entry Point | `python -m ofac` starts both API and Streamlit |
| **Data Storage** | Configurable path (default `./data/`) | Explicit; easy to backup; follows config |
| **Containerization** | Deferred to Phase 2 | Local Python install adequate for internal use |

**Configuration Schema:**
```python
class Settings(BaseSettings):
    # Matching thresholds
    match_threshold_nok: int = 95      # Score >= this → NOK
    match_threshold_review: int = 80   # Score >= this → REVIEW
    
    # OFAC data
    ofac_data_path: Path = Path("./data/ofac")
    ofac_auto_update: bool = True
    ofac_update_check_hours: int = 24
    
    # Performance
    batch_size: int = 100
    max_file_rows: int = 10000
    
    # Logging
    log_level: str = "INFO"
    log_path: Path = Path("./logs")
    
    class Config:
        env_prefix = "OFAC_"
        env_file = ".env"
```

### Decision Impact Analysis

**Implementation Sequence:**
1. Configuration system (Pydantic Settings) - foundation for all components
2. OFAC data layer (loader, storage) - required for matching
3. Matching engine (RapidFuzz + DataFrame) - core functionality
4. FastAPI endpoints - expose matching capability
5. Streamlit frontend - user interface
6. Logging infrastructure - audit trail

**Cross-Component Dependencies:**
```
Settings ──────────────────────────────────────────────┐
    │                                                  │
    ▼                                                  ▼
OFAC Data Layer ──────────────────────────────────► Logging
    │                                                  ▲
    ▼                                                  │
Matching Engine ───────────────────────────────────────┤
    │                                                  │
    ▼                                                  │
FastAPI Routes ────────────────────────────────────────┤
    │                                                  │
    ▼                                                  │
Streamlit App ─────────────────────────────────────────┘
```

## Implementation Patterns & Consistency Rules

### Pattern Categories Defined

**Critical Conflict Points Identified:** 6 areas where AI agents could make different choices, all addressed below.

### Naming Patterns

#### Python Naming (PEP 8 Standard)

| Element | Convention | Example |
|---------|------------|---------|
| Functions | snake_case | `screen_entities()`, `load_ofac_data()` |
| Variables | snake_case | `entity_name`, `match_score` |
| Classes | PascalCase | `ScreeningResult`, `OFACLoader` |
| Constants | UPPER_SNAKE | `DEFAULT_THRESHOLD`, `MAX_FILE_SIZE` |
| Modules/Files | snake_case | `matcher.py`, `ofac_loader.py` |
| Private members | leading underscore | `_internal_helper()`, `_cached_data` |
| Type variables | PascalCase | `EntityT`, `ResultT` |

**Examples:**
```python
# Good
class ScreeningResult:
    entity_name: str
    match_score: int
    
def calculate_match_score(entity: str, target: str) -> int:
    MAX_SCORE = 100
    _normalized = _normalize_string(entity)
    return _compute_similarity(_normalized, target)

# Bad - Don't do this
class screeningResult:  # Wrong: should be PascalCase
    entityName: str     # Wrong: should be snake_case
```

#### API Naming Conventions

| Pattern | Convention | Example |
|---------|------------|---------|
| Resources | Plural nouns, lowercase | `/screenings`, `/entities` |
| Actions | Noun + verb path | `/screenings/batch`, `/data/refresh` |
| Path params | snake_case | `/screenings/{screening_id}` |
| Query params | snake_case | `?threshold=80&include_aliases=true` |
| Versioning | URL prefix (future) | `/api/v1/screenings` |

**API Endpoint Reference:**
```
POST   /screenings/batch     # Submit batch screening
POST   /screenings/single    # Single entity check
GET    /screenings/{id}      # Get screening result
GET    /data/status          # OFAC data status
POST   /data/refresh         # Trigger data update
GET    /health               # Health check
```

#### JSON Field Naming

**Standard: snake_case** (consistent with Python internals)

```json
{
  "screening_id": "scr_abc123",
  "entity_name": "Example Organization",
  "match_score": 85,
  "match_status": "REVIEW",
  "ofac_version": "2025-12-08",
  "matched_entries": [
    {
      "sdn_name": "EXAMPLE ORG",
      "sdn_type": "Entity",
      "match_reason": "token_sort_ratio: 92%"
    }
  ]
}
```

### Structure Patterns

#### Test Organization

```
tests/
├── __init__.py
├── conftest.py           # Shared fixtures, pytest configuration
├── unit/                 # Fast, isolated tests (mock external deps)
│   ├── __init__.py
│   ├── test_matcher.py       # Matching engine unit tests
│   ├── test_classifier.py    # Classification logic tests
│   ├── test_models.py        # Pydantic model tests
│   └── test_config.py        # Configuration validation tests
├── integration/          # Tests with real component interactions
│   ├── __init__.py
│   ├── test_api_screening.py # Full API endpoint tests
│   ├── test_data_loader.py   # OFAC data loading tests
│   └── test_pipeline.py      # End-to-end screening pipeline
└── fixtures/             # Test data files
    ├── sample_entities.csv
    ├── sample_entities.xlsx
    └── mock_ofac_data/
        ├── sdn.csv
        ├── add.csv
        └── alt.csv
```

**Test Naming Convention:**
- Files: `test_<module_name>.py`
- Functions: `test_<behavior_description>()`
- Classes (optional): `TestMatcherFuzzyScoring`

```python
# Example test structure
def test_fuzzy_match_returns_score_above_threshold():
    """Exact match should return score >= 95."""
    result = match_entity("ACME Corp", "ACME Corp")
    assert result.score >= 95

def test_fuzzy_match_handles_unicode_characters():
    """Unicode normalization should not affect matching."""
    result = match_entity("Café Organization", "Cafe Organization")
    assert result.score >= 80
```

#### Import Conventions

**Standard: Absolute imports from package root**

```python
# CORRECT - Absolute imports
from ofac.core.matcher import screen_entity, MatchResult
from ofac.core.models import ScreeningResult, EntityInput
from ofac.core.config import settings
from ofac.data.loader import OFACDataLoader
from ofac.api.schemas import ScreeningRequest, ScreeningResponse

# AVOID - Relative imports
from ..core.matcher import screen_entity  # Don't use
from .models import ScreeningResult       # Avoid except in __init__.py
```

**Import Order (enforced by Ruff):**
1. Standard library imports
2. Third-party imports
3. Local application imports

```python
# Example properly ordered imports
import json
from datetime import datetime
from pathlib import Path

import pandas as pd
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ofac.core.matcher import screen_entity
from ofac.core.models import ScreeningResult
```

### Format Patterns

#### API Response Structure

**Success Response:**
```json
{
  "data": {
    "screening_id": "scr_abc123",
    "status": "completed",
    "results": [...]
  },
  "meta": {
    "ofac_version": "2025-12-08",
    "processed_at": "2025-12-09T10:30:00Z",
    "duration_ms": 2340
  }
}
```

**Error Response:**
```json
{
  "error": {
    "code": "FILE_INVALID_FORMAT",
    "message": "Uploaded file must be .xlsx or .csv format",
    "details": {
      "received_type": "application/pdf",
      "allowed_types": ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "text/csv"]
    }
  }
}
```

#### Date/Time Formats

| Context | Format | Example |
|---------|--------|---------|
| API responses | ISO 8601 with timezone | `2025-12-09T10:30:00Z` |
| Logging | ISO 8601 with timezone | `2025-12-09T10:30:00Z` |
| File names | Date only, hyphenated | `screening-2025-12-09.xlsx` |
| Display (UI) | Localized | `December 9, 2025 at 10:30 AM` |

### Process Patterns

#### Error Handling Pattern

```python
# Define custom exceptions in ofac/core/exceptions.py
class OFACError(Exception):
    """Base exception for OFAC screening errors."""
    code: str = "OFAC_ERROR"
    
class FileValidationError(OFACError):
    """Raised when uploaded file fails validation."""
    code: str = "FILE_VALIDATION_ERROR"
    
class OFACDataError(OFACError):
    """Raised when OFAC data is unavailable or corrupt."""
    code: str = "OFAC_DATA_ERROR"

# Usage pattern in API routes
@router.post("/screenings/batch")
async def batch_screening(file: UploadFile):
    try:
        result = await process_screening(file)
        return {"data": result}
    except FileValidationError as e:
        raise HTTPException(status_code=400, detail={"error": {"code": e.code, "message": str(e)}})
    except OFACDataError as e:
        raise HTTPException(status_code=503, detail={"error": {"code": e.code, "message": str(e)}})
```

#### Loading State Pattern (Streamlit)

```python
# Standard loading state pattern for Streamlit
def process_with_loading(label: str, operation: Callable):
    """Wrap long operations with consistent loading UI."""
    with st.spinner(label):
        try:
            result = operation()
            return result
        except Exception as e:
            st.error(f"Operation failed: {str(e)}")
            return None

# Usage
results = process_with_loading(
    "Screening 150 entities against OFAC database...",
    lambda: screen_batch(entities)
)
```

### Enforcement Guidelines

**All AI Agents MUST:**

1. Run `ruff check .` and `ruff format .` before committing code
2. Follow the naming conventions exactly as specified above
3. Use absolute imports from the `ofac` package root
4. Structure API responses using the defined wrapper format
5. Write tests in the `tests/` directory following the organization pattern
6. Use snake_case for all JSON fields in API contracts

**Pattern Enforcement:**

| Tool | Purpose | When |
|------|---------|------|
| Ruff | Linting + formatting | Pre-commit hook, CI |
| mypy | Type checking | Pre-commit hook, CI |
| pytest | Test execution | Pre-commit hook, CI |

**Pre-commit Configuration:**
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.0.0
    hooks:
      - id: mypy
        additional_dependencies: [pydantic>=2.0]
```

### Anti-Patterns to Avoid

| Anti-Pattern | Why It's Bad | Correct Approach |
|--------------|--------------|------------------|
| `getUserData()` | Breaks Python convention | `get_user_data()` |
| `/user/{userId}` | Mixed casing in API | `/users/{user_id}` |
| `{"entityName": "..."}` | Inconsistent with Python | `{"entity_name": "..."}` |
| `from ..core import x` | Fragile relative imports | `from ofac.core import x` |
| Tests in `src/` | Pollutes package | Tests in `tests/` |
| Bare `except:` | Hides errors | `except SpecificError:` |

## Project Structure & Boundaries

### Complete Project Directory Structure

```
OFAC/
├── pyproject.toml                    # Project metadata, dependencies, tool config
├── uv.lock                           # Lock file for reproducible installs
├── .env.example                      # Environment variable template
├── .gitignore                        # Git ignore patterns
├── .pre-commit-config.yaml           # Pre-commit hooks config
├── README.md                         # Project overview
├── CLAUDE.md                         # AI agent guidance
│
├── src/
│   └── ofac/
│       ├── __init__.py               # Package init, version
│       ├── __main__.py               # Entry point: python -m ofac
│       │
│       ├── core/                     # Shared business logic
│       │   ├── __init__.py
│       │   ├── config.py             # Pydantic Settings (all configuration)
│       │   ├── models.py             # Pydantic models (ScreeningResult, EntityInput, etc.)
│       │   ├── exceptions.py         # Custom exceptions (OFACError hierarchy)
│       │   ├── matcher.py            # Fuzzy matching engine (RapidFuzz)
│       │   ├── classifier.py         # OK/REVIEW/NOK classification logic
│       │   └── reporter.py           # Report generation (Excel, audit trail)
│       │
│       ├── data/                     # OFAC data management
│       │   ├── __init__.py
│       │   ├── loader.py             # CSV triplet parsing, DataFrame construction
│       │   ├── updater.py            # Download, version tracking, atomic swap
│       │   ├── schemas.py            # OFAC data schemas (SDN, Address, Alias)
│       │   └── cache/                # Downloaded OFAC files (gitignored)
│       │       └── .gitkeep
│       │
│       ├── api/                      # FastAPI backend
│       │   ├── __init__.py
│       │   ├── main.py               # FastAPI app factory, lifespan events
│       │   ├── deps.py               # Dependency injection (get_ofac_data, etc.)
│       │   ├── schemas.py            # API request/response Pydantic models
│       │   └── routes/
│       │       ├── __init__.py       # Router aggregation
│       │       ├── screening.py      # POST /screenings/batch, /screenings/single
│       │       ├── data.py           # GET /data/status, POST /data/refresh
│       │       └── health.py         # GET /health
│       │
│       └── streamlit/                # Streamlit frontend
│           ├── __init__.py
│           ├── app.py                # Main Streamlit application
│           ├── state.py              # Session state management
│           ├── styles.py             # Custom CSS injection
│           └── components/
│               ├── __init__.py
│               ├── upload.py         # File upload component
│               ├── mapping.py        # Column mapping UI
│               ├── results.py        # Results table with status badges
│               ├── summary.py        # Metrics and summary cards
│               └── export.py         # Download buttons, report generation
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                   # Shared fixtures, pytest config
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_matcher.py           # Matching engine tests
│   │   ├── test_classifier.py        # Classification logic tests
│   │   ├── test_models.py            # Pydantic model validation tests
│   │   ├── test_config.py            # Configuration tests
│   │   └── test_reporter.py          # Report generation tests
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_api_screening.py     # API endpoint tests
│   │   ├── test_api_data.py          # Data management API tests
│   │   ├── test_data_loader.py       # OFAC data loading tests
│   │   └── test_pipeline.py          # End-to-end screening pipeline
│   └── fixtures/
│       ├── sample_entities.csv       # Test input file
│       ├── sample_entities.xlsx      # Test input file (Excel)
│       └── mock_ofac_data/
│           ├── sdn.csv               # Mock SDN list
│           ├── add.csv               # Mock addresses
│           └── alt.csv               # Mock aliases
│
├── scripts/
│   ├── update_ofac.py                # Manual OFAC data update script
│   └── generate_test_data.py         # Generate test fixtures
│
├── data/                             # Runtime data directory (gitignored)
│   ├── ofac/                         # Downloaded OFAC CSV files
│   │   └── .gitkeep
│   └── logs/                         # Application logs
│       └── .gitkeep
│
└── docs/
    ├── development/
    │   └── uv-guide.md               # uv usage instructions
    ├── prd.md                        # Product Requirements Document
    ├── ux-design-specification.md    # UX Design Specification
    ├── architecture.md               # This document
    └── bmm-workflow-status.yaml      # BMAD workflow tracking
```

### Architectural Boundaries

#### Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     External Clients                         │
│              (Streamlit App, Future Excel UDF)              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    FastAPI Routes Layer                      │
│   /screenings/batch  │  /screenings/single  │  /data/*      │
│                                                              │
│   Responsibilities:                                          │
│   - Request validation (Pydantic schemas)                    │
│   - Response formatting                                      │
│   - Error handling → HTTP status codes                       │
│   - Logging (screening_id, duration, status)                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Core Business Logic                     │
│       matcher.py  │  classifier.py  │  reporter.py          │
│                                                              │
│   Responsibilities:                                          │
│   - Fuzzy matching algorithms                                │
│   - Score calculation and normalization                      │
│   - OK/REVIEW/NOK classification                             │
│   - Report generation                                        │
│   - NO HTTP concepts (pure Python)                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      Data Access Layer                       │
│            loader.py  │  updater.py  │  schemas.py           │
│                                                              │
│   Responsibilities:                                          │
│   - OFAC CSV parsing and loading                             │
│   - DataFrame construction and caching                       │
│   - Download management and atomic updates                   │
│   - Version tracking                                         │
└─────────────────────────────────────────────────────────────┘
```

#### API Boundary Contracts

| Endpoint | Method | Request | Response | Errors |
|----------|--------|---------|----------|--------|
| `/screenings/batch` | POST | Multipart file upload | `{data: {screening_id, results[]}, meta: {...}}` | 400, 413, 503 |
| `/screenings/single` | POST | `{entity_name, country?}` | `{data: {match_status, matches[]}, meta: {...}}` | 400, 503 |
| `/screenings/{id}` | GET | - | `{data: {screening_id, status, results[]}}` | 404 |
| `/data/status` | GET | - | `{data: {version, last_updated, record_count}}` | 503 |
| `/data/refresh` | POST | - | `{data: {status, new_version}}` | 503 |
| `/health` | GET | - | `{status: "healthy"}` | - |

#### Component Communication

| From | To | Method | Data Format |
|------|----|----|-------------|
| Streamlit App | FastAPI | HTTP POST/GET | JSON (Pydantic schemas) |
| FastAPI Routes | Core Logic | Direct function calls | Python objects (models.py) |
| Core Logic | Data Layer | Direct function calls | Pandas DataFrames |
| Any Component | Logging | structlog calls | JSON to file |

### Requirements to Structure Mapping

#### PRD Category Mapping

| PRD Category | FR Count | Primary Location | Secondary Location |
|--------------|----------|------------------|-------------------|
| File Processing | 12 | `streamlit/components/upload.py` | `api/routes/screening.py` |
| Matching Engine | 18 | `core/matcher.py` | `core/models.py` |
| Classification Logic | 10 | `core/classifier.py` | `core/models.py` |
| OFAC Data Management | 8 | `data/loader.py`, `data/updater.py` | `api/routes/data.py` |
| Reporting & Export | 15 | `core/reporter.py` | `streamlit/components/export.py` |
| User Interface | 16 | `streamlit/app.py` | `streamlit/components/*.py` |

#### Cross-Cutting Concerns Mapping

| Concern | Implementation Location | Used By |
|---------|------------------------|---------|
| Configuration | `core/config.py` | All modules |
| Error Handling | `core/exceptions.py` | All modules |
| Logging | `core/config.py` (structlog setup) | All modules |
| Data Models | `core/models.py` | core/*, api/*, streamlit/* |
| OFAC Data Access | `data/loader.py` | core/matcher.py, api/deps.py |

### Data Flow

```
User Upload (CSV/XLSX)
        │
        ▼
┌───────────────────┐
│   File Validation │  → Reject if invalid format/size
│   & Parsing       │     Location: streamlit/components/upload.py
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Column Mapping   │  → User confirms name/country columns
│  (Streamlit UI)   │     Location: streamlit/components/mapping.py
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Entity Extraction│  → List[EntityInput] 
│  & Normalization  │     Location: core/models.py, api/schemas.py
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Matching Engine  │  → Fuzzy match against OFAC DataFrame
│  (RapidFuzz)      │     Location: core/matcher.py
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Classification   │  → OK (< 80) / REVIEW (80-94) / NOK (≥ 95)
│  Logic            │     Location: core/classifier.py
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Results Display  │  → Streamlit dataframe with status badges
│  (Streamlit UI)   │     Location: streamlit/components/results.py
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Report Export    │  → Excel file with full audit trail
│  (reporter.py)    │     Location: core/reporter.py
└───────────────────┘
```

### Module Responsibilities (Single Responsibility Principle)

| Module | Single Responsibility | Key Dependencies |
|--------|----------------------|------------------|
| `core/config.py` | Load and validate all settings | pydantic-settings |
| `core/models.py` | Define shared data models | pydantic |
| `core/exceptions.py` | Define error hierarchy | None (stdlib only) |
| `core/matcher.py` | Execute fuzzy matching | rapidfuzz, pandas |
| `core/classifier.py` | Assign OK/REVIEW/NOK status | core/models |
| `core/reporter.py` | Generate Excel reports | openpyxl, pandas |
| `data/loader.py` | Parse and load OFAC CSVs | pandas |
| `data/updater.py` | Download and update OFAC data | httpx |
| `data/schemas.py` | Define OFAC data structures | pydantic |
| `api/main.py` | FastAPI app setup and lifespan | fastapi |
| `api/deps.py` | Dependency injection | data/loader |
| `api/schemas.py` | API request/response models | pydantic |
| `api/routes/*.py` | HTTP endpoint handlers | core/*, api/deps |
| `streamlit/app.py` | UI orchestration and workflow | streamlit |
| `streamlit/state.py` | Session state management | streamlit |
| `streamlit/styles.py` | CSS injection | None |
| `streamlit/components/*.py` | Reusable UI components | streamlit |

### Integration Points

#### Internal Integration

| Integration | Pattern | Location |
|-------------|---------|----------|
| API ↔ Core Logic | Dependency Injection | `api/deps.py` provides `get_ofac_data()` |
| Streamlit ↔ API | HTTP Client | `streamlit/app.py` calls FastAPI endpoints |
| Core ↔ Data | Direct Import | `core/matcher.py` imports `data/loader` |
| All ↔ Config | Singleton | `from ofac.core.config import settings` |

#### External Integration

| Integration | Protocol | Location |
|-------------|----------|----------|
| OFAC Data Download | HTTPS GET | `data/updater.py` → treasury.gov |
| User File Upload | HTTP Multipart | `api/routes/screening.py` |
| Report Download | HTTP Response | `streamlit/components/export.py` |

## Architecture Validation Results

### Coherence Validation ✅

**Decision Compatibility:**
All technology choices work together seamlessly. Python 3.11+ is compatible with FastAPI (latest), Streamlit (≥1.28.0), RapidFuzz, Pandas, and Pydantic v2. No version conflicts or incompatibilities identified.

**Pattern Consistency:**
Implementation patterns align with the Python ecosystem:
- PEP 8 naming conventions throughout
- Pydantic for all data validation (core models, API schemas)
- FastAPI patterns for REST API design
- Streamlit conventions for frontend components

**Structure Alignment:**
The `src/ofac/` structure supports all architectural decisions:
- `core/` enables shared business logic across clients
- `data/` provides isolated OFAC data management
- `api/` and `streamlit/` are parallel frontends sharing core logic
- `tests/` mirrors source structure for maintainability

### Requirements Coverage Validation ✅

**Functional Requirements Coverage (79 FRs):**

| Category | Count | Status | Implementation Location |
|----------|-------|--------|------------------------|
| File Processing | 12 | ✅ Covered | streamlit/, api/routes/ |
| Matching Engine | 18 | ✅ Covered | core/matcher.py |
| Classification Logic | 10 | ✅ Covered | core/classifier.py |
| OFAC Data Management | 8 | ✅ Covered | data/ |
| Reporting & Export | 15 | ✅ Covered | core/reporter.py |
| User Interface | 16 | ✅ Covered | streamlit/ |

**Non-Functional Requirements Coverage (53 NFRs):**

| Category | Status | Architectural Support |
|----------|--------|----------------------|
| Performance | ✅ | Eager load, in-memory DataFrame, RapidFuzz optimization |
| Accuracy | ✅ | Conservative thresholds (80/95), alias matching, country boost |
| Compliance | ✅ | Structured JSON logging, screening_id tracing, Excel audit reports |
| Security | ✅ | Local processing, no cloud transmission, input validation |
| Reliability | ✅ | Exception hierarchy, graceful degradation, partial results |
| Maintainability | ✅ | Modular core/, shared across API and future Excel UDF |

### Implementation Readiness Validation ✅

**Decision Completeness:**
- All critical architectural decisions documented with specific versions
- Technology rationale provided for each choice
- Phase-aware decisions clearly marked (Phase 1 vs Phase 2)

**Structure Completeness:**
- Complete project tree with 50+ files explicitly named
- Every module's responsibility documented
- Integration points specified with communication patterns

**Pattern Completeness:**
- 6 potential conflict points identified and resolved
- Comprehensive naming conventions (Python, API, JSON)
- Process patterns (error handling, loading states) with code examples
- Anti-patterns documented to prevent common mistakes

### Gap Analysis Results

**Critical Gaps:** None

**Important Gaps (Action Items):**
1. Create `docs/development/uv-guide.md` during Phase 1 setup
2. Generate `.env.example` during project scaffold
3. Update `CLAUDE.md` to reference new architecture

**Nice-to-Have (Post-MVP):**
- Detailed Streamlit ↔ API HTTP client patterns
- Performance profiling hooks documentation
- Additional test fixtures for edge cases

### Architecture Completeness Checklist

**✅ Requirements Analysis**
- [x] Project context thoroughly analyzed (PRD, UX Spec, Conceptual Design)
- [x] Scale and complexity assessed (60K OFAC records, <30s performance)
- [x] Technical constraints identified (Python-only, local deployment)
- [x] Cross-cutting concerns mapped (audit trail, error handling, config)

**✅ Technology Foundation**
- [x] Primary stack specified with versions
- [x] Dependency management selected (uv)
- [x] Development tooling defined (Ruff, pytest, mypy, pre-commit)
- [x] pyproject.toml structure documented

**✅ Architectural Decisions**
- [x] Data architecture decisions documented (eager load, DataFrame, no cache)
- [x] Security/validation approach defined (permissive + auto-healing)
- [x] API patterns established (REST, structured errors, comprehensive logging)
- [x] Frontend architecture documented (Streamlit + session state)
- [x] Infrastructure decisions made (Pydantic Settings, single entry point)

**✅ Implementation Patterns**
- [x] Python naming conventions (PEP 8)
- [x] API naming conventions (plural resources, snake_case)
- [x] JSON field naming (snake_case)
- [x] Test organization (tests/unit/, tests/integration/)
- [x] Import conventions (absolute imports)
- [x] Error handling patterns (exception hierarchy)
- [x] Pre-commit configuration

**✅ Project Structure**
- [x] Complete directory structure defined
- [x] Component boundaries established (layers diagram)
- [x] API boundary contracts specified
- [x] Integration points mapped (internal and external)
- [x] Requirements to structure mapping complete

### Architecture Readiness Assessment

**Overall Status:** ✅ READY FOR IMPLEMENTATION

**Confidence Level:** HIGH

**Key Strengths:**
1. **Clear separation of concerns** - Core logic is isolated and reusable
2. **Comprehensive patterns** - AI agents have unambiguous guidance
3. **Phase-aware design** - Phase 1 simplicity with Phase 2 extensibility
4. **Compliance-ready** - Audit trail and logging built into architecture
5. **Performance-conscious** - Eager load and in-memory processing for speed

**Areas for Future Enhancement:**
1. Multi-tenant architecture (Phase 2)
2. Cloud deployment patterns (Phase 2)
3. Horizontal scaling for matching engine (if needed)
4. Additional matching algorithms (Phase 2)

### Implementation Handoff

**AI Agent Guidelines:**
1. Follow all architectural decisions exactly as documented
2. Use implementation patterns consistently across all components
3. Respect project structure and layer boundaries
4. Run `ruff check` and `ruff format` before all commits
5. Write tests in `tests/unit/` and `tests/integration/` as specified
6. Use absolute imports from the `ofac` package root
7. Refer to this document for all architectural questions

**First Implementation Steps:**
1. Initialize project with `uv init` and configure `pyproject.toml`
2. Create directory structure as specified
3. Implement `core/config.py` (Pydantic Settings) first
4. Implement `data/loader.py` to parse OFAC CSVs
5. Implement `core/matcher.py` with RapidFuzz
6. Build FastAPI skeleton with health endpoint
7. Create Streamlit app shell with file upload

## Architecture Completion Summary

### Workflow Completion

**Architecture Decision Workflow:** COMPLETED ✅
**Total Steps Completed:** 8
**Date Completed:** 2025-12-09
**Document Location:** docs/architecture.md

### Final Architecture Deliverables

**📋 Complete Architecture Document**
- All architectural decisions documented with specific versions
- Implementation patterns ensuring AI agent consistency
- Complete project structure with all files and directories
- Requirements to architecture mapping
- Validation confirming coherence and completeness

**🏗️ Implementation Ready Foundation**
- 15+ architectural decisions made
- 6 implementation pattern categories defined
- 6 core architectural components specified
- 79 functional + 53 non-functional requirements fully supported

**📚 AI Agent Implementation Guide**
- Technology stack with verified versions
- Consistency rules that prevent implementation conflicts
- Project structure with clear boundaries
- Integration patterns and communication standards

### Development Sequence

1. Initialize project using `uv init`
2. Set up development environment per architecture
3. Implement core architectural foundations (`core/config.py`, `data/loader.py`)
4. Build matching engine (`core/matcher.py`, `core/classifier.py`)
5. Create API layer (`api/main.py`, routes)
6. Develop Streamlit frontend
7. Maintain consistency with documented rules

### Quality Assurance Checklist

**✅ Architecture Coherence**
- [x] All decisions work together without conflicts
- [x] Technology choices are compatible
- [x] Patterns support the architectural decisions
- [x] Structure aligns with all choices

**✅ Requirements Coverage**
- [x] All functional requirements are supported
- [x] All non-functional requirements are addressed
- [x] Cross-cutting concerns are handled
- [x] Integration points are defined

**✅ Implementation Readiness**
- [x] Decisions are specific and actionable
- [x] Patterns prevent agent conflicts
- [x] Structure is complete and unambiguous
- [x] Examples are provided for clarity

### Project Success Factors

**🎯 Clear Decision Framework**
Every technology choice was made collaboratively with clear rationale, ensuring all stakeholders understand the architectural direction.

**🔧 Consistency Guarantee**
Implementation patterns and rules ensure that multiple AI agents will produce compatible, consistent code that works together seamlessly.

**📋 Complete Coverage**
All project requirements are architecturally supported, with clear mapping from business needs to technical implementation.

**🏗️ Solid Foundation**
The Python project structure and architectural patterns provide a production-ready foundation following current best practices.

---

**Architecture Status:** READY FOR IMPLEMENTATION ✅

**Next Phase:** Begin implementation using the architectural decisions and patterns documented herein.

**Document Maintenance:** Update this architecture when major technical decisions are made during implementation.