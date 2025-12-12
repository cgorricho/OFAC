# Story 2.3: Batch Screening Endpoint

Status: done

## Story

As a **developer**,
I want an API endpoint that accepts file uploads for batch screening,
So that multiple organizations can be screened at once.

## Acceptance Criteria

```gherkin
Given I have an Excel file with organization names
When I POST to /screenings/batch with the file
Then screening runs for all rows
And I receive results for each organization
And screening_id is the same for all results in batch

Given I upload a file larger than max size
When the request is processed
Then I receive status 413
And the error message indicates file too large
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Extend screening.py with batch endpoint
  - [x] POST /screenings/batch endpoint
  - [x] File upload handling (multipart/form-data)
- [x] Task 2: Add file parsing (Excel/CSV)
  - [x] _parse_uploaded_file() function
  - [x] Support .xlsx, .xls, .csv
  - [x] Uses pandas and openpyxl
- [x] Task 3: Add file size validation
  - [x] 10MB file size limit
  - [x] max_file_rows limit from settings
  - [x] Returns 413 for oversized files
- [x] Task 4: Implement batch processing logic
  - [x] Auto-detect name column (_detect_name_column)
  - [x] Process each row through matcher
  - [x] Generate unique screening_id per batch
  - [x] Count OK/REVIEW/NOK results
- [x] Task 5: Write integration tests (5 tests)
  - [x] CSV file test
  - [x] Excel file test
  - [x] File too large test
  - [x] Unsupported format test
  - [x] No name column test
- [x] Task 6: Run review and commit

## API Endpoint

```
POST /screenings/batch
Content-Type: multipart/form-data

Request:
file: (Excel or CSV file)

Response:
{
  "results": [...],
  "total_screened": 10,
  "ok_count": 8,
  "review_count": 1,
  "nok_count": 1,
  "ofac_version": "...",
  "processing_time_ms": 250
}
```

## Dev Notes

### File Parsing
- Supports .xlsx, .xls (openpyxl), .csv (pandas)
- Auto-detects entity name column by patterns
- Extracts optional country and description columns
- Skips empty rows

### Column Auto-Detection
- Name patterns: "name", "organization", "entity", "partner", "beneficiary"
- Country patterns: "country", "nation", "location"
- Description patterns: "description", "project", "notes", "remarks"

### References
- [Source: docs/epics.md#Story 2.3]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Extended screening.py with POST /screenings/batch
- ✅ File upload handling (multipart/form-data)
- ✅ Excel/CSV parsing with pandas/openpyxl
- ✅ File size validation (10MB, max_file_rows)
- ✅ Auto-column detection
- ✅ Batch processing with shared screening_id
- ✅ 5 batch tests, 10 total screening tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/api/routes/screening.py (added batch endpoint)
- src/ofac/api/schemas.py (export BatchScreeningResponse)
- tests/integration/test_api_screening.py (added batch tests)

## Change Log
- 2025-12-12: Story 2.3 implemented with full dev → review → commit cycle
