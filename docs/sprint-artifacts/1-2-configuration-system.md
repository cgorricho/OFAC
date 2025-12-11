# Story 1.2: Configuration System

Status: done

## Story

As a **developer**,
I want centralized configuration with environment variable support,
So that settings are consistent across all components.

## Acceptance Criteria

```gherkin
Given the application starts
When settings are loaded
Then all configuration values have sensible defaults
And environment variables prefixed with OFAC_ override defaults
And invalid configuration values raise ValidationError on startup

Given I set OFAC_MATCH_THRESHOLD_NOK=90
When the application loads configuration
Then settings.match_threshold_nok equals 90
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create config.py with Pydantic Settings v2 pattern
  - [x] Import from pydantic_settings (NOT pydantic)
  - [x] Define Settings class with SettingsConfigDict
  - [x] Set env_prefix="OFAC_" and env_file=".env"
- [x] Task 2: Implement configuration fields
  - [x] match_threshold_nok: int = 95
  - [x] match_threshold_review: int = 80
  - [x] ofac_data_path: Path with default "./data/ofac"
  - [x] log_level: str = "INFO" (with Literal type)
  - [x] Add validation for threshold ranges (0-100)
  - [x] Add all other settings (batch_size, max_file_rows, api_host, api_port, etc.)
  - [x] Add model_validator to ensure review < nok thresholds
- [x] Task 3: Export singleton settings instance
  - [x] Create settings = Settings() at module level
  - [x] Export from core __init__.py
- [x] Task 4: Write unit tests for configuration
  - [x] Test default values (12 tests)
  - [x] Test environment variable override (7 tests)
  - [x] Test validation errors for invalid values (11 tests)
  - [x] Test import locations (3 tests)
  - [x] Test path conversion (2 tests)
- [x] Task 5: Verify configuration works
  - [x] All 35 unit tests pass
  - [x] mypy passes with no errors
  - [x] ruff check passes

## Dev Notes

### Architecture Reference
- Pattern from `docs/project_context.md` - Pydantic Settings section
- Use Pydantic v2 patterns: `SettingsConfigDict` NOT `ConfigDict`

### Configuration Fields Implemented
```python
# Matching thresholds
match_threshold_nok: int = 95      # Score >= this = NOK
match_threshold_review: int = 80   # Score >= this = REVIEW

# OFAC data settings
ofac_data_path: Path = Path("./data/ofac")
auto_update: bool = True
update_check_hours: int = 24

# Performance settings
batch_size: int = 100
max_file_rows: int = 10000

# Logging settings
log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
log_path: Path = Path("./data/logs")

# API settings
api_host: str = "127.0.0.1"
api_port: int = 8000

# Streamlit settings
streamlit_port: int = 8501
```

### References
- [Source: docs/architecture.md#Configuration Schema]
- [Source: docs/project_context.md#Pydantic Settings Pattern]
- [Source: docs/epics.md#Story 1.2]

## Dev Agent Record

### Context Reference
<!-- Story context from epics.md and architecture.md -->

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Debug Log References
- Used SettingsConfigDict from pydantic_settings (not ConfigDict from pydantic)
- Added field_validator for Path conversion
- Added model_validator for threshold relationship
- All 35 tests pass

### Completion Notes List
- ✅ Created src/ofac/core/config.py with Pydantic Settings v2 pattern
- ✅ Implemented all configuration fields with validation (ge/le constraints)
- ✅ Exported settings singleton from ofac.core module
- ✅ Created comprehensive test suite with 35 configuration tests
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓
- ✅ All 35 unit tests pass

### Code Review Fixes Applied (2025-12-11)
- ✅ Fixed ruff whitespace errors (8 W293 errors)
- ✅ Added model_validator to enforce review < nok threshold
- ✅ Added test for log_path default value
- ✅ Added tests for threshold relationship validation (2 tests)

### File List
**New Files:**
- src/ofac/core/config.py
- tests/unit/test_config.py

**Modified Files:**
- src/ofac/core/__init__.py (exports settings)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.2 implemented - Configuration system complete with all settings and tests
- 2025-12-11: Code review fixes applied - Added threshold validation, fixed whitespace, added tests
