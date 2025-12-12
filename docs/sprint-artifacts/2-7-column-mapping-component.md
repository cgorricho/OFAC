# Story 2.7: Column Mapping Component

Status: done

## Story

As a **compliance officer**,
I want to confirm or correct column mappings,
So that the right data is used for screening.

## Acceptance Criteria

```gherkin
Given a file is uploaded
When column detection suggests "Organization Name" for entity
Then I see the suggestion highlighted
And I can confirm or change it via dropdown

Given I select columns and click "Confirm Mapping"
When validation passes
Then workflow advances to screening step
And column mapping is stored in session state
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/components/mapping.py
  - [x] render_column_mapping() function
- [x] Task 2: Implement column selection UI
  - [x] st.selectbox for name column (required)
  - [x] st.selectbox for country column (optional)
  - [x] st.selectbox for description column (optional)
- [x] Task 3: Add mapping confirmation
  - [x] Validation (name column required)
  - [x] Save to session state
  - [x] Preview of selected columns
- [x] Task 4: Integrate with app.py
  - [x] Route to mapping component when workflow_step == "map"
  - [x] Advance to "screen" step on confirmation
- [x] Task 5: Run review and commit

## Column Mapping Features

- Auto-detection with manual override
- Required field validation (entity name)
- Optional fields (country, description)
- Mapping preview
- Workflow progression

## Dev Notes

### Column Selection
- Uses st.selectbox for each column type
- Pre-selects auto-detected columns
- Allows manual selection if auto-detection fails
- Shows preview of selected columns

### References
- [Source: docs/epics.md#Story 2.7]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/components/mapping.py
- ✅ Column selection UI with st.selectbox
- ✅ Auto-detection integration
- ✅ Required/optional field handling
- ✅ Mapping preview
- ✅ Integration with workflow routing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/streamlit/components/mapping.py

**Modified Files:**
- src/ofac/streamlit/app.py (workflow routing)
- src/ofac/streamlit/components/__init__.py

## Change Log
- 2025-12-12: Story 2.7 implemented with full dev → review → commit cycle
