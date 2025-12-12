# Story 5.3: Freshness Display in UI

Status: done

## Story

As a **compliance officer**,
I want to see OFAC data freshness at a glance,
So that I know if my data is current.

## Acceptance Criteria

```gherkin
Given I open the Streamlit app
When the header loads
Then I see "OFAC Data: Current (2 days old)" in green
OR I see "OFAC Data: Stale (10 days old)" in yellow
OR I see "OFAC Data: Critical (32 days old)" in red

Given data is stale
When I hover over the indicator
Then I see "Last updated: 2025-11-29"
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/components/freshness.py
- [x] Task 2: Implement render_freshness_indicator() function
- [x] Task 3: Fetch freshness from /data/status API
- [x] Task 4: Color-coded display (green/yellow/red)
- [x] Task 5: Show age in days and last updated date
- [x] Task 6: Integrate into app header
- [x] Task 7: Error handling for API unavailable
- [x] Task 8: Run review and commit

## Freshness Display

**Display:**
- Color-coded status: 🟢 CURRENT, 🟡 STALE, 🔴 CRITICAL
- Age in days
- Last updated date

**Integration:**
- Displayed in app header
- Fetches from /data/status API
- Graceful error handling

## Dev Notes

### Implementation
- Uses requests library to call API
- Color coding with emoji and HTML
- Shows last updated date (extracted from ISO timestamp)
- Handles API unavailability gracefully

### References
- [Source: docs/epics.md#Story 5.3]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/components/freshness.py
- ✅ Implemented render_freshness_indicator() function
- ✅ Color-coded display (green/yellow/red)
- ✅ Age in days and last updated date
- ✅ Integrated into app header
- ✅ Error handling for API unavailable
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/streamlit/components/freshness.py

**Modified Files:**
- src/ofac/streamlit/app.py (added freshness indicator)

## Change Log
- 2025-12-12: Story 5.3 implemented with full dev → review → commit cycle

