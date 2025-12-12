# Story 5.5: Update Trigger API

Status: done

## Story

As a **developer**,
I want an API endpoint to trigger OFAC updates,
So that clients can initiate updates.

## Acceptance Criteria

```gherkin
Given I call POST /data/refresh
When the update succeeds
Then I receive new version info
And status 200 is returned

Given an update fails
When the error is caught
Then status 503 is returned
And error message is included
And existing data is not corrupted
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Implement POST /data/refresh in data.py
- [x] Task 2: Call OFACUpdater.download_sdn_files()
- [x] Task 3: Reload data after successful update
- [x] Task 4: Return new version info on success
- [x] Task 5: Error handling with 503 status
- [x] Task 6: Ensure existing data preserved on failure
- [x] Task 7: Run review and commit

## Update Trigger API

**Endpoint:** POST /data/refresh

**Response (Success):**
```json
{
  "version": "2025-12-12",
  "last_updated": "2025-12-12T10:00:00Z",
  "age_days": 0,
  "freshness_status": "CURRENT",
  "record_count": 1000,
  "status": "success"
}
```

**Error Handling:**
- 503 if update fails
- Existing data preserved on failure

## Dev Notes

### Implementation
- Uses OFACUpdater.download_sdn_files()
- Reloads data after successful update
- Returns comprehensive status information
- Error handling preserves existing data

### References
- [Source: docs/epics.md#Story 5.5]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Implemented POST /data/refresh endpoint
- ✅ Calls OFACUpdater.download_sdn_files()
- ✅ Reloads data after successful update
- ✅ Returns new version info on success
- ✅ Error handling with 503 status
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/api/routes/data.py (added POST /data/refresh)

## Change Log
- 2025-12-12: Story 5.5 implemented with full dev → review → commit cycle

