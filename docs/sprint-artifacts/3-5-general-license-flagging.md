# Story 3.5: General License Flagging

Status: done

## Story

As a **developer**,
I want matches with humanitarian context flagged for GL review,
So that legitimate aid operations aren't automatically blocked.

## Acceptance Criteria

```gherkin
Given a match in Syria with humanitarian keywords
When classification runs
Then status is REVIEW (not NOK)
And general_license is "GL-21"
And notes include "Potential Syria Humanitarian License applicability"

Given a match in Syria WITHOUT humanitarian keywords
When classification runs
Then status is NOK
And general_license is null
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Enhance classifier with GL detection logic
  - [x] classify_with_gl_context() function
- [x] Task 2: Combine sanctioned_country + humanitarian_keywords
  - [x] GL detection logic
- [x] Task 3: Update screening workflow
  - [x] Single entity endpoint
  - [x] Batch endpoint
- [x] Task 4: Write unit tests (8 tests)
  - [x] Syria with humanitarian keywords → REVIEW with GL-21
  - [x] Syria without humanitarian keywords → NOK
  - [x] Iran with humanitarian keywords → REVIEW with GL D-1
  - [x] Venezuela with humanitarian keywords → REVIEW with GL-41
  - [x] Non-sanctioned country → NOK (no GL)
  - [x] Edge cases
- [x] Task 5: Run review and commit

## General License Flagging Logic

```python
from ofac.core.classifier import classify_with_gl_context

status, is_humanitarian, gl_note = classify_with_gl_context(
    highest_score=95,
    matches=matches,
    entity_country="SY",
    description="Emergency medical supplies for Syria"
)
# Returns: (MatchStatus.REVIEW, True, "GL-21: ...")
```

**Classification Rules:**
- High score (>=NOK) + Sanctioned country + Humanitarian keywords → REVIEW with GL
- High score (>=NOK) + Sanctioned country + NO humanitarian keywords → NOK
- High score (>=NOK) + Non-sanctioned country → NOK (no GL)
- Medium score (REVIEW threshold) → REVIEW
- Low score → OK

## Dev Notes

### GL Detection
- Combines sanctioned country check + humanitarian keyword detection
- Returns GL note with code, description, and detected keywords
- Only applies to high-score matches in sanctioned countries

### Integration
- Single entity endpoint uses classify_with_gl_context()
- Batch endpoint uses classify_with_gl_context()
- ScreeningResult model already has humanitarian_flag and general_license_note fields

### References
- [Source: docs/epics.md#Story 3.5]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Added classify_with_gl_context() to classifier.py
- ✅ GL detection logic (sanctioned country + humanitarian keywords)
- ✅ Integrated into single and batch screening endpoints
- ✅ 8 unit tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/core/classifier.py (added GL detection)
- src/ofac/api/routes/screening.py (integrated GL detection)
- src/ofac/core/__init__.py (export classify_with_gl_context)

**New Files:**
- tests/unit/test_gl_flagging.py

## Change Log
- 2025-12-12: Story 3.5 implemented with full dev → review → commit cycle
