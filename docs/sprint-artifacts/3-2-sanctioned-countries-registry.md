# Story 3.2: Sanctioned Countries Registry

Status: done

## Story

As a **developer**,
I want a maintained list of OFAC-sanctioned countries,
So that country-based detection works correctly.

## Acceptance Criteria

```gherkin
Given I query is_sanctioned_country("SY")
When the check runs
Then True is returned (Syria is sanctioned)

Given I query is_sanctioned_country("US")
When the check runs
Then False is returned

Given I query get_general_license("SY")
When lookup runs
Then "GL-21" is returned with description
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create countries registry module
  - [x] src/ofac/core/countries.py
- [x] Task 2: Add sanctioned countries list
  - [x] 10 sanctioned countries (SY, IR, CU, KP, VE, BY, RU, MM, SD, LY)
- [x] Task 3: Add General License mappings
  - [x] GL-21 for Syria and Cuba
  - [x] GL D-1 for Iran
  - [x] GL-41 for Venezuela
- [x] Task 4: Implement is_sanctioned_country()
  - [x] Case-insensitive lookup
- [x] Task 5: Implement get_general_license()
  - [x] Returns GeneralLicense NamedTuple
- [x] Task 6: Write unit tests (19 tests)
  - [x] Sanctioned country tests
  - [x] General License tests
  - [x] Helper function tests
- [x] Task 7: Run review and commit

## Countries Registry

```python
from ofac.core.countries import is_sanctioned_country, get_general_license

# Check if country is sanctioned
is_sanctioned_country("SY")  # Returns True
is_sanctioned_country("US")  # Returns False

# Get General License
gl = get_general_license("SY")  # Returns GL-21 info
```

**Sanctioned Countries:**
- SY (Syria) → GL-21
- IR (Iran) → GL D-1
- CU (Cuba) → GL-21
- KP (North Korea) → No GL
- VE (Venezuela) → GL-41
- BY (Belarus), RU (Russia), MM (Myanmar), SD (Sudan), LY (Libya)

## Dev Notes

### General License Structure
- GeneralLicense NamedTuple with code, description, applicable_countries
- Maps country codes to their applicable General Licenses

### References
- [Source: docs/epics.md#Story 3.2]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created core/countries.py with sanctioned countries registry
- ✅ 10 sanctioned countries with ISO codes
- ✅ General License mappings (GL-21, GL D-1, GL-41)
- ✅ is_sanctioned_country() and get_general_license() functions
- ✅ 19 unit tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/core/countries.py
- tests/unit/test_countries.py

**Modified Files:**
- src/ofac/core/__init__.py (export countries functions)

## Change Log
- 2025-12-12: Story 3.2 implemented with full dev → review → commit cycle
