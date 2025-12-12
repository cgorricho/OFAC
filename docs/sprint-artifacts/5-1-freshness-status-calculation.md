# Story 5.1: Freshness Status Calculation

Status: done

## Story

As a **developer**,
I want to calculate OFAC data freshness,
So that staleness can be detected and displayed.

## Acceptance Criteria

```gherkin
Given OFAC data was last updated 5 days ago
When freshness is calculated
Then status is "CURRENT" (green)

Given OFAC data is 10 days old
When freshness is calculated
Then status is "STALE" (yellow warning)

Given OFAC data is 30+ days old
When freshness is calculated
Then status is "CRITICAL" (red)
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create data/status.py module
- [x] Task 2: Implement FreshnessStatus enum
- [x] Task 3: Implement calculate_freshness() function
- [x] Task 4: Read version.json for last update date (via OFACDataVersion)
- [x] Task 5: Thresholds: <7 days = CURRENT, 7-14 = STALE, >14 = CRITICAL
- [x] Task 6: Return FreshnessStatus with age_days
- [x] Task 7: Write unit tests (10 tests)
- [x] Task 8: Run review and commit

## Freshness Status Calculation

**Thresholds:**
- CURRENT: < 7 days old
- STALE: 7-14 days old
- CRITICAL: > 14 days old

**Implementation:**
- Uses OFACDataVersion.loaded_at timestamp
- Calculates age in days
- Returns (FreshnessStatus, age_days) tuple
- Handles missing timestamp (returns CRITICAL)

## Dev Notes

### Implementation
- FreshnessStatus enum with CURRENT, STALE, CRITICAL
- calculate_freshness() function takes OFACDataVersion
- Age calculation using datetime delta
- Edge cases handled (no timestamp, zero days)

### References
- [Source: docs/epics.md#Story 5.1]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created data/status.py module
- ✅ FreshnessStatus enum with 3 statuses
- ✅ calculate_freshness() function with thresholds
- ✅ Age calculation in days
- ✅ 10 unit tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/data/status.py
- tests/unit/test_status.py

**Modified Files:**
- src/ofac/data/__init__.py (export FreshnessStatus, calculate_freshness)

## Change Log
- 2025-12-12: Story 5.1 implemented with full dev → review → commit cycle
