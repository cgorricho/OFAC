# Story 5.2: OFAC Status API Endpoint

Status: done

## Story

As a **developer**,
I want an API endpoint for OFAC data status,
So that clients can query data freshness.

## Acceptance Criteria

```gherkin
Given I call GET /data/status
When the request succeeds
Then I receive current OFAC version info
And response includes age_days
And response includes freshness_status
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create api/routes/data.py
- [x] Task 2: Implement GET /data/status endpoint
- [x] Task 3: Return version, last_updated, age_days, freshness_status, record_count
- [x] Task 4: Integrate into FastAPI app
- [x] Task 5: Write integration tests (3 tests)
- [x] Task 6: Run review and commit

## OFAC Status API Endpoint

**Endpoint:** GET /data/status

**Response:**
```json
{
  "version": "2025-12-01",
  "last_updated": "2025-12-12T10:00:00Z",
  "age_days": 5,
  "freshness_status": "CURRENT",
  "record_count": 1000
}
```

**Error Handling:**
- 503 if OFAC data not loaded

## Dev Notes

### Implementation
- Uses get_matcher dependency for OFAC data access
- Calculates freshness using calculate_freshness()
- Returns comprehensive status information

### References
- [Source: docs/epics.md#Story 5.2]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created api/routes/data.py
- ✅ Implemented GET /data/status endpoint
- ✅ Returns version, last_updated, age_days, freshness_status, record_count
- ✅ Integrated into FastAPI app
- ✅ 3 integration tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/api/routes/data.py
- tests/integration/test_data_status.py

**Modified Files:**
- src/ofac/api/app.py (include data router)

## Change Log
- 2025-12-12: Story 5.2 implemented with full dev → review → commit cycle

