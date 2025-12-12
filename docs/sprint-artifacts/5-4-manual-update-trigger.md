# Story 5.4: Manual Update Trigger

Status: done

## Story

As a **compliance officer**,
I want to update OFAC data on demand,
So that I can ensure freshness before screening.

## Acceptance Criteria

```gherkin
Given I click "Update OFAC Data"
When the update runs
Then I see a progress indicator
And I see "Downloading..." then "Validating..." then "Complete"
And the freshness indicator updates

Given an update fails
When the error is handled
Then I see an error message
And existing data is preserved
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/components/update.py
- [x] Task 2: Implement trigger_update() function
- [x] Task 3: Add update button to freshness indicator
- [x] Task 4: Show progress with st.spinner
- [x] Task 5: Handle success/failure feedback
- [x] Task 6: Error handling for API unavailable
- [x] Task 7: Run review and commit

## Manual Update Trigger

**Implementation:**
- Update button in freshness indicator
- Calls POST /data/refresh API
- Progress spinner during update
- Success/error feedback
- Auto-refresh after success

**User Experience:**
- One-click update
- Visual progress feedback
- Clear success/error messages

## Dev Notes

### Implementation
- Uses requests library to call API
- Progress spinner with timeout handling
- Error handling for connection/timeout errors
- Auto-refresh after successful update

### References
- [Source: docs/epics.md#Story 5.4]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/components/update.py
- ✅ Implemented trigger_update() function
- ✅ Added update button to freshness indicator
- ✅ Progress spinner and error handling
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/streamlit/components/update.py

**Modified Files:**
- src/ofac/streamlit/components/freshness.py (added update button)

## Change Log
- 2025-12-12: Story 5.4 implemented with full dev → review → commit cycle

