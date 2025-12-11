# Story 1.1: Project Initialization

Status: done

## Story

As a **developer**,
I want the project structure and dependencies set up,
So that I can start implementing features.

## Acceptance Criteria

```gherkin
Given I have Python 3.11+ and uv installed
When I clone the repository and run `uv venv && uv pip install -e ".[dev]"`
Then the virtual environment is created
And all dependencies are installed
And I can run `python -c "import ofac"` without errors
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create pyproject.toml (AC: Complete project metadata and dependencies)
  - [x] Define project metadata (name, version, description, python version)
  - [x] Add core dependencies (fastapi, uvicorn, streamlit, pandas, rapidfuzz, pydantic, httpx, python-multipart, openpyxl)
  - [x] Add dev dependencies (pytest, pytest-cov, ruff, mypy, pre-commit)
  - [x] Add optional excel dependencies (xlwings)
  - [x] Configure tool sections (ruff, pytest, mypy)
- [x] Task 2: Create src/ofac package structure (AC: Package can be imported)
  - [x] Create src/ofac/__init__.py with version
  - [x] Create src/ofac/__main__.py as entry point
  - [x] Create core/ subdirectory with __init__.py
  - [x] Create data/ subdirectory with __init__.py
  - [x] Create api/ subdirectory with __init__.py
  - [x] Create streamlit/ subdirectory with __init__.py
- [x] Task 3: Create tests directory structure (AC: Test framework ready)
  - [x] Create tests/__init__.py
  - [x] Create tests/conftest.py with basic fixtures
  - [x] Create tests/unit/ directory with __init__.py
  - [x] Create tests/integration/ directory with __init__.py
  - [x] Create tests/fixtures/ directory
- [x] Task 4: Create configuration files (AC: Dev tooling configured)
  - [x] Create .env.example template
  - [x] Create .pre-commit-config.yaml
  - [x] Verify .gitignore includes Python patterns
- [x] Task 5: Verify installation works (AC: Acceptance criteria pass)
  - [x] Run uv venv and uv pip install -e ".[dev]"
  - [x] Verify import ofac works
  - [x] Run initial test to verify pytest works

## Dev Notes

### Architecture Reference
- Follow project structure from `docs/architecture.md` section "Project Structure"
- Use `src/ofac/` layout (importable package)
- Python 3.11+ required per architecture spec

### Project Structure Notes
- Root: `pyproject.toml` as single source of truth
- Package location: `src/ofac/`
- Test location: `tests/` (mirroring src structure)
- Data location: `data/` (gitignored runtime data)
- Config: `.env.example`, `.pre-commit-config.yaml`

### Dependencies (from architecture.md)
```
Core:
- fastapi>=0.109.0
- uvicorn[standard]>=0.27.0
- streamlit>=1.28.0
- pandas>=2.0.0
- rapidfuzz>=3.0.0
- pydantic>=2.0.0
- httpx>=0.26.0
- python-multipart>=0.0.6
- openpyxl>=3.1.0

Dev:
- pytest>=7.0.0
- pytest-cov>=4.0.0
- ruff>=0.1.0
- mypy>=1.0.0
- pre-commit>=3.0.0

Optional (Excel):
- xlwings>=0.30.0
```

### Tool Configuration (from architecture.md)
- Ruff: line-length=88, target-version="py311"
- Pytest: testpaths=["tests"], addopts="-v --tb=short"
- Mypy: python_version="3.11", strict=true

### References
- [Source: docs/architecture.md#Project Structure]
- [Source: docs/architecture.md#pyproject.toml Structure]
- [Source: docs/architecture.md#Development Tooling]
- [Source: docs/epics.md#Story 1.1]

## Dev Agent Record

### Context Reference
<!-- Story context from epics.md and architecture.md -->

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Debug Log References
- uv installed via pip
- Virtual environment created with uv venv
- 83 packages installed including ofac-screening

### Completion Notes List
- ✅ Created pyproject.toml with full project configuration
- ✅ Created src/ofac/ package with all submodules (core, data, api, streamlit)
- ✅ Created tests/ directory with unit, integration, and fixtures subdirectories
- ✅ Created .env.example with environment variable documentation
- ✅ Created .pre-commit-config.yaml with ruff, mypy, and standard hooks
- ✅ Verified installation: `python -c "import ofac"` returns version 0.1.0
- ✅ All 5 package import tests pass

### Code Review Fixes Applied (2025-12-11)
- ✅ Fixed conftest.py: Changed `from typing import Generator` to `from collections.abc import Generator`
- ✅ Fixed __main__.py: Version now imports from `ofac.__version__` (single source of truth)
- ✅ Added `[tool.bandit]` section to pyproject.toml for pre-commit bandit hook
- ✅ Ran `ruff check --fix` to fix import ordering
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- pyproject.toml
- src/ofac/__init__.py
- src/ofac/__main__.py
- src/ofac/core/__init__.py
- src/ofac/data/__init__.py
- src/ofac/api/__init__.py
- src/ofac/api/routes/__init__.py
- src/ofac/streamlit/__init__.py
- src/ofac/streamlit/components/__init__.py
- tests/__init__.py
- tests/conftest.py
- tests/unit/__init__.py
- tests/unit/test_package.py
- tests/integration/__init__.py
- tests/fixtures/.gitkeep
- tests/fixtures/mock_ofac_data/.gitkeep
- data/ofac/.gitkeep
- data/logs/.gitkeep
- .env.example
- .pre-commit-config.yaml

**Modified Files (Review Fixes):**
- tests/conftest.py (import fix)
- src/ofac/__main__.py (version import fix)
- pyproject.toml (bandit config added)

## Change Log
- 2025-12-11: Story 1.1 implemented - Project initialization complete with all dependencies and structure
- 2025-12-11: Code review fixes applied - Linting issues fixed, version duplication resolved, bandit config added
