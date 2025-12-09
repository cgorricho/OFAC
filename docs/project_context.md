---
project_name: 'OFAC Screening Tool'
user_name: 'Carlos'
date: '2025-12-09'
sections_completed: ['technology_stack', 'language_rules', 'framework_rules', 'testing_rules', 'code_quality', 'domain_rules', 'anti_patterns']
status: 'complete'
rule_count: 45
optimized_for_llm: true
---

# Project Context for AI Agents

_Critical rules and patterns that AI agents must follow when implementing code in the OFAC Screening Tool project. Focus on unobvious details that agents might otherwise miss._

---

## Technology Stack & Versions

| Technology | Version | Notes |
|------------|---------|-------|
| Python | 3.11+ | Required for latest typing features |
| FastAPI | ≥0.109.0 | API backend |
| Streamlit | ≥1.28.0 | Web frontend |
| Pydantic | v2+ | NOT v1 - use v2 patterns |
| RapidFuzz | ≥3.0.0 | For fuzzy matching |
| Pandas | ≥2.0.0 | Data processing |
| uv | Latest | Package management (NOT pip) |
| Ruff | ≥0.1.0 | Linting AND formatting |
| mypy | ≥1.0.0 | Strict mode enabled |

---

## Critical Implementation Rules

### Python-Specific Rules

- **Type hints required** on all functions and class attributes
- **Use Pydantic v2 patterns**: `model_validator` not `validator`, `ConfigDict` not `Config`
- **Strict mypy**: No implicit `Any`, no untyped defs
- **Absolute imports only**: `from ofac.core.matcher import ...` NOT `from ..core.matcher`
- **Constants are UPPER_SNAKE_CASE**: `DEFAULT_THRESHOLD = 80`

### Pydantic Settings Pattern

```python
# CORRECT - Pydantic v2 Settings
from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    match_threshold_nok: int = 95
    
    model_config = ConfigDict(
        env_prefix="OFAC_",
        env_file=".env",
    )
```

### FastAPI Patterns

- **Response wrapper required**: Always return `{"data": {...}, "meta": {...}}` or `{"error": {...}}`
- **Error codes use prefixes**: `FILE_*`, `DATA_*`, `OFAC_*`, `SCREEN_*`
- **Path params are snake_case**: `/screenings/{screening_id}` NOT `{screeningId}`
- **Use HTTPException with structured detail**: `{"error": {"code": "...", "message": "..."}}`

### Streamlit Patterns

- **Session state schema** - Always use these keys:
  - `workflow_step`: "upload" | "map" | "screen" | "review"
  - `screening_id`: str
  - `ofac_version`: str
- **Use spinners for all operations >1 second**
- **Status badges use 3 CSS classes only**: `.status-ok`, `.status-review`, `.status-nok`

### RapidFuzz Matching Rules

- **Algorithm**: Use `token_sort_ratio` as primary matcher
- **Thresholds**: score ≥95 = NOK, score ≥80 = REVIEW, score <80 = OK
- **Always check aliases**: Match against SDN names AND alt names
- **Country boost**: +10 points if entity country matches OFAC country

---

## Testing Rules

- **Unit tests go in** `tests/unit/test_<module>.py`
- **Integration tests go in** `tests/integration/test_<feature>.py`
- **Test fixtures go in** `tests/fixtures/`
- **Use pytest fixtures from** `tests/conftest.py`
- **Test function names**: `def test_<behavior_description>():`
- **Mock external services** (OFAC downloads) in unit tests

---

## Code Quality Rules

### Pre-Commit (MUST pass before commit)

```bash
ruff check --fix .
ruff format .
mypy .
pytest tests/unit/
```

### Import Order (Ruff enforced)

1. Standard library
2. Third-party
3. Local (`from ofac.core...`)

### JSON Field Naming

- **Always snake_case**: `entity_name`, `match_score`, `screening_id`
- **NEVER camelCase**: NO `entityName`, `matchScore`

---

## OFAC Domain Rules

### Classification Logic

```
score >= 95 → NOK (blocked, needs escalation)
score >= 80 → REVIEW (needs human review)
score < 80  → OK (cleared)
```

### Humanitarian Context Detection

- If project country is Syria AND description contains humanitarian keywords
- Flag for General License 21 (GL-21) review
- **Never auto-clear** Syria-related matches

### OFAC Data Structure

- **Three CSV files**: `sdn.csv` (entities), `add.csv` (addresses), `alt.csv` (aliases)
- **Primary key**: `ent_num` links all three files
- **Load at startup** into Pandas DataFrame, not on-demand

---

## Anti-Patterns (NEVER DO)

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| `from ..core import x` | `from ofac.core import x` |
| `{"entityName": "..."}` | `{"entity_name": "..."}` |
| `class Config:` in Pydantic | `model_config = ConfigDict(...)` |
| Bare `except:` | `except SpecificError:` |
| `pip install` | `uv pip install` |
| Tests in `src/` | Tests in `tests/` |
| `print()` for debugging | `logger.debug()` |

---

## File Locations Reference

| What | Where |
|------|-------|
| Configuration | `src/ofac/core/config.py` |
| Data models | `src/ofac/core/models.py` |
| Custom exceptions | `src/ofac/core/exceptions.py` |
| Matching engine | `src/ofac/core/matcher.py` |
| Classification | `src/ofac/core/classifier.py` |
| OFAC data loading | `src/ofac/data/loader.py` |
| API routes | `src/ofac/api/routes/*.py` |
| Streamlit app | `src/ofac/streamlit/app.py` |
| Tests | `tests/unit/`, `tests/integration/` |

---

## Quick Checks Before Commit

1. ✅ `ruff check --fix .` passes
2. ✅ `ruff format .` applied
3. ✅ `mypy .` passes with no errors
4. ✅ `pytest tests/unit/` passes
5. ✅ All imports are absolute (`from ofac.core...`)
6. ✅ All JSON fields are snake_case
7. ✅ Type hints on all functions

---

## Usage Guidelines

**For AI Agents:**

- Read this file before implementing any code
- Follow ALL rules exactly as documented
- When in doubt, prefer the more restrictive option
- Refer to `docs/architecture.md` for detailed decisions

**For Humans:**

- Keep this file lean and focused on agent needs
- Update when technology stack changes
- Review quarterly for outdated rules
- Remove rules that become obvious over time

---

_Last Updated: 2025-12-09_

