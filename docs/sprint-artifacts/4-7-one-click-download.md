# Story 4.7: One-Click Download

Status: done

## Story

As a **compliance officer**,
I want to download the report with one click,
So that exporting is effortless.

## Acceptance Criteria

```gherkin
Given I am viewing screening results
When I click "Download Report"
Then an Excel file downloads immediately
And the filename includes date (screening-2025-12-09.xlsx)
And no additional dialog or configuration is needed
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/components/export.py
- [x] Task 2: Implement render_export_button() function
- [x] Task 3: Use st.download_button with report bytes
- [x] Task 4: Generate filename with date
- [x] Task 5: Integrate into results component
- [x] Task 6: Error handling for missing results
- [x] Task 7: Run review and commit

## One-Click Download

**Implementation:**
- Export button in results view
- Generates Excel report on demand
- Filename format: `screening-YYYY-MM-DD.xlsx`
- No configuration needed

**User Experience:**
- Single click to download
- Immediate file download
- Professional filename with date

## Dev Notes

### Implementation
- Uses Streamlit's st.download_button
- Generates report bytes on demand
- Filename includes current date
- Error handling for missing results

### References
- [Source: docs/epics.md#Story 4.7]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/components/export.py
- ✅ Implemented render_export_button() function
- ✅ Integrated into results component
- ✅ Date-based filename generation
- ✅ Error handling for missing results
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/streamlit/components/export.py

**Modified Files:**
- src/ofac/streamlit/components/results.py (added export button)

## Change Log
- 2025-12-12: Story 4.7 implemented with full dev → review → commit cycle

