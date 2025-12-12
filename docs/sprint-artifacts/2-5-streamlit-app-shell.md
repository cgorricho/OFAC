# Story 2.5: Streamlit App Shell

Status: done

## Story

As a **developer**,
I want the basic Streamlit application running,
So that the UI can be developed.

## Acceptance Criteria

```gherkin
Given I run `streamlit run src/ofac/streamlit/app.py`
When I access http://localhost:8501
Then I see the OFAC Screening Tool landing page
And the OFAC data version is displayed in the header
And the page has professional styling

Given the app starts
When session state is initialized
Then workflow_step is "upload"
And other state variables are initialized
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/app.py main application
  - [x] Page configuration
  - [x] Header with title and OFAC version
  - [x] Welcome message
- [x] Task 2: Create streamlit/state.py for session state
  - [x] init_session_state() function
  - [x] get_workflow_step() and set_workflow_step()
  - [x] reset_session_state() function
  - [x] WorkflowStep type
- [x] Task 3: Create streamlit/styles.py for custom CSS
  - [x] inject_custom_css() function
  - [x] Status badge classes (.status-ok, .status-review, .status-nok)
  - [x] Header styling
- [x] Task 4: Add OFAC data version display
  - [x] Load OFAC data on app start
  - [x] Display version in header
  - [x] Store in session state
- [x] Task 5: Update __main__.py
  - [x] Support --streamlit flag
  - [x] Launch Streamlit with correct port
- [x] Task 6: Run review and commit

## Streamlit Application Structure

```python
# Main app
streamlit run src/ofac/streamlit/app.py

# Or via module
python -m ofac --streamlit

# Session state schema:
{
    "workflow_step": "upload" | "map" | "screen" | "review",
    "uploaded_file": UploadedFile | None,
    "column_mapping": {"name": str, "country": str | None, "description": str | None},
    "screening_results": DataFrame | None,
    "ofac_version": str,
    "screening_id": str | None
}
```

## Dev Notes

### CSS Classes (Tasteful Minimum)
- `.status-ok` - Green badge for OK results
- `.status-review` - Yellow badge for REVIEW results
- `.status-nok` - Red badge for NOK results
- `.main-header` - Professional header styling
- `.ofac-version` - Version display styling

### References
- [Source: docs/ux-design-specification.md#Design System Foundation]
- [Source: docs/architecture.md#Session State Schema]
- [Source: docs/epics.md#Story 2.5]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/app.py with main application
- ✅ Created streamlit/state.py for session state management
- ✅ Created streamlit/styles.py with custom CSS (3 status classes)
- ✅ OFAC data version loading and display
- ✅ Updated __main__.py to support Streamlit
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/streamlit/app.py
- src/ofac/streamlit/state.py
- src/ofac/streamlit/styles.py

**Modified Files:**
- src/ofac/__main__.py (added Streamlit support)

## Change Log
- 2025-12-12: Story 2.5 implemented with full dev → review → commit cycle
