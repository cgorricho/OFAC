# Story 1.3: Core Data Models

Status: done

## Story

As a **developer**,
I want Pydantic models for all core data structures,
So that data validation is consistent throughout the application.

## Acceptance Criteria

```gherkin
Given I create an EntityInput with name="Test Org" and country="US"
When I access entity.entity_name
Then it returns "Test Org"

Given I create a ScreeningResult
When I serialize it to JSON
Then all fields use snake_case naming
And the model validates all required fields
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create models.py with core Pydantic models
  - [x] EntityInput model (entity_name, country, description)
  - [x] MatchResult model (sdn_name, sdn_type, match_score, match_type, ofac_list, programs)
  - [x] ScreeningResult model (entity_input, match_status, matches, screening_id, timestamp)
  - [x] BatchScreeningRequest and BatchScreeningResponse models
- [x] Task 2: Add enums for status types
  - [x] MatchStatus enum (OK, REVIEW, NOK)
  - [x] MatchType enum (EXACT, FUZZY, ALIAS)
  - [x] OFACList enum (SDN, CONSOLIDATED)
- [x] Task 3: Add validation
  - [x] Score ranges (0-100) using Annotated type
  - [x] Required fields validation
  - [x] snake_case JSON serialization (ConfigDict)
  - [x] Whitespace stripping for entity_name
- [x] Task 4: Write unit tests (35 tests)
  - [x] Test model creation
  - [x] Test JSON serialization
  - [x] Test validation errors
  - [x] Test default values
  - [x] Test imports from ofac.core
- [x] Task 5: Verify all checks pass
  - [x] ruff check passes
  - [x] mypy passes
  - [x] pytest passes (75 total tests)

## Dev Notes

### Models Implemented

| Model | Purpose | Key Fields |
|-------|---------|------------|
| `EntityInput` | Input entity for screening | entity_name, country, description |
| `MatchResult` | Single OFAC match | sdn_name, match_score, match_type, ofac_list |
| `ScreeningResult` | Complete screening result | entity_input, match_status, matches, screening_id |
| `BatchScreeningRequest` | Batch screening input | entities list |
| `BatchScreeningResponse` | Batch screening output | results, counts, processing_time |

### Enums Implemented

| Enum | Values |
|------|--------|
| `MatchStatus` | OK, REVIEW, NOK |
| `MatchType` | EXACT, FUZZY, ALIAS |
| `OFACList` | SDN, CONSOLIDATED |

### References
- [Source: docs/architecture.md#Core Data Models]
- [Source: docs/project_context.md#Pydantic Patterns]
- [Source: docs/epics.md#Story 1.3]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/core/models.py with all models and enums
- ✅ Implemented Score type alias with validation (0-100)
- ✅ Added auto-generated screening_id (UUID) and timestamp (UTC)
- ✅ Fixed deprecation warning: datetime.utcnow() → datetime.now(UTC)
- ✅ Created 35 model tests in tests/unit/test_models.py
- ✅ All 75 unit tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### Code Review Fixes Applied
- ✅ Fixed datetime.utcnow() deprecation (MEDIUM)
- ✅ Fixed all ruff whitespace errors (8 W293)
- ✅ Formatted all files with ruff format

### File List
**New Files:**
- src/ofac/core/models.py
- tests/unit/test_models.py

**Modified Files:**
- src/ofac/core/__init__.py (exports models)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.3 implemented with full dev → review → fix cycle
