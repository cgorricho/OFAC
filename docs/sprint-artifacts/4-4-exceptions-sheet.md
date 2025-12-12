# Story 4.4: Exceptions Sheet

Status: done

## Story

As a **compliance officer**,
I want an exceptions-only sheet,
So that I can focus on cases requiring review.

## Acceptance Criteria

```gherkin
Given a report with 100 results including 5 REVIEW and 2 NOK
When I open the Exceptions sheet
Then I see only 7 rows (REVIEW + NOK cases)
And they are sorted by risk level (NOK first)
And each has complete match details
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Implement _create_exceptions_sheet() method
- [x] Task 2: Filter to only REVIEW and NOK statuses
- [x] Task 3: Sort by status (NOK first) then score descending
- [x] Task 4: Include all match details
- [x] Task 5: Handle empty exceptions case
- [x] Task 6: Write unit tests (3 new tests)
- [x] Task 7: Run review and commit

## Exceptions Sheet

**Filtering:**
- Only REVIEW and NOK cases
- Excludes OK cases

**Sorting:**
- NOK first (highest risk)
- Then REVIEW
- Within each status, sorted by score descending

**Content:**
- Same columns as Details sheet
- Complete match information

## Dev Notes

### Implementation
- Filters results by match_status (REVIEW or NOK)
- Sorts by status priority then score
- Handles empty exceptions gracefully

### References
- [Source: docs/epics.md#Story 4.4]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Implemented _create_exceptions_sheet() method
- ✅ Filter to REVIEW and NOK only
- ✅ Sort by risk level (NOK first, then by score)
- ✅ Complete match details included
- ✅ 3 new unit tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/core/reporter.py (implemented exceptions sheet)
- tests/unit/test_reporter.py (added exceptions sheet tests)

## Change Log
- 2025-12-12: Story 4.4 implemented with full dev → review → commit cycle

