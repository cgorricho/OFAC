# Story 2.6: File Upload Component

Status: done

## Story

As a **compliance officer (Carlos)**,
I want to upload my Excel file via drag-and-drop,
So that I can start the screening process easily.

## Acceptance Criteria

```gherkin
Given I am on the upload step
When I drag an Excel file onto the upload area
Then the file is accepted
And I see a preview of the first few rows
And file name and size are displayed

Given I upload a PDF file
When validation runs
Then I see an error message "Unsupported file format"
And the workflow does not advance
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/components/upload.py
  - [x] render_file_upload() function
  - [x] st.file_uploader with type restrictions
- [x] Task 2: Implement file validation
  - [x] File format validation
  - [x] File size validation
  - [x] Error messages for invalid files
- [x] Task 3: Add file preview
  - [x] Display first 10 rows with st.dataframe
  - [x] Show file metadata (name, rows, columns)
- [x] Task 4: Add column detection display
  - [x] Show detected columns
  - [x] Auto-set column mapping
  - [x] Handle cases where detection fails
- [x] Task 5: Integrate with app.py
  - [x] Route to upload component when workflow_step == "upload"
  - [x] Advance to "map" step on successful upload
- [x] Task 6: Run review and commit

## Upload Component Features

- Drag-and-drop file upload
- File format validation (.xlsx, .xls, .csv)
- File size validation (10MB limit)
- File preview (first 10 rows)
- Auto column detection display
- Error handling with user-friendly messages

## Dev Notes

### File Validation
- Uses file_parser.parse_file() for validation
- Catches FileFormatError, FileTooLargeError, FileParseError
- Displays user-friendly error messages

### Column Detection
- Uses file_parser.get_column_suggestions()
- Auto-sets column_mapping in session state
- Shows detected columns to user

### References
- [Source: docs/epics.md#Story 2.6]
- [Source: docs/ux-design-specification.md#Upload step]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/components/upload.py
- ✅ File upload with drag-and-drop support
- ✅ File validation and error handling
- ✅ File preview with st.dataframe
- ✅ Column detection and auto-mapping
- ✅ Integration with app.py workflow routing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/streamlit/components/upload.py

**Modified Files:**
- src/ofac/streamlit/app.py (workflow routing)
- src/ofac/streamlit/components/__init__.py

## Change Log
- 2025-12-12: Story 2.6 implemented with full dev → review → commit cycle
