# Story 2.4: File Parsing & Column Detection

Status: done

## Story

As a **developer**,
I want to parse uploaded files and detect relevant columns,
So that organization names are correctly extracted.

## Acceptance Criteria

```gherkin
Given an Excel file with column "Organization Name"
When it's parsed
Then the column is auto-detected as the entity name column
And a mapping suggestion is returned

Given a file with non-standard column names
When auto-detection fails
Then column names are returned for manual selection
And no error is raised
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create core/file_parser.py utility
  - [x] parse_file() function
  - [x] detect_columns() function
  - [x] get_column_suggestions() function
  - [x] ColumnMapping NamedTuple
- [x] Task 2: Extract parsing logic from screening.py
  - [x] Refactored batch endpoint to use file_parser
  - [x] Removed duplicate parsing code
- [x] Task 3: Enhanced column detection
  - [x] Multiple name patterns (name, organization, entity, partner, etc.)
  - [x] Country and description detection
  - [x] Priority-based matching
- [x] Task 4: Error handling
  - [x] ColumnMappingError when name column not found
  - [x] get_column_suggestions() for manual selection (no error)
- [x] Task 5: Write unit tests (13 tests)
  - [x] File parsing tests (5)
  - [x] Column detection tests (5)
  - [x] Column suggestions tests (2)
  - [x] ColumnMapping tests (1)
- [x] Task 6: Run review and commit

## File Parser API

```python
from ofac.core.file_parser import parse_file, detect_columns, get_column_suggestions

# Parse file
df = parse_file(file_content, "test.xlsx")

# Auto-detect columns (raises if name column not found)
mapping = detect_columns(df)
# Returns: ColumnMapping(
#   entity_name_column="Organization Name",
#   country_column="Country",
#   description_column="Description",
#   all_columns=[...]
# )

# Get suggestions without errors
suggestions = get_column_suggestions(df)
# Returns: {
#   "name_candidates": [...],
#   "country_candidates": [...],
#   "description_candidates": [...],
#   "all_columns": [...]
# }
```

## Dev Notes

### Column Detection Patterns
- **Name patterns**: name, organization, entity, partner, beneficiary, org, company, institution
- **Country patterns**: country, nation, location, region
- **Description patterns**: description, project, notes, remarks, comment

### File Format Support
- Excel: .xlsx, .xls (openpyxl)
- CSV: .csv (pandas, UTF-8 with Latin-1 fallback)

### References
- [Source: docs/epics.md#Story 2.4]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created core/file_parser.py utility module
- ✅ Extracted parsing logic from screening.py
- ✅ Enhanced column detection with multiple patterns
- ✅ Added get_column_suggestions() for manual selection
- ✅ 13 file parser tests pass
- ✅ Batch endpoint still works with refactored code
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/core/file_parser.py
- tests/unit/test_file_parser.py

**Modified Files:**
- src/ofac/api/routes/screening.py (refactored to use file_parser)

## Change Log
- 2025-12-12: Story 2.4 implemented with full dev → review → commit cycle
