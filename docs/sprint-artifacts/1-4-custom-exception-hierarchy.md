# Story 1.4: Custom Exception Hierarchy

Status: done

## Story

As a **developer**,
I want a structured exception hierarchy,
So that errors are handled consistently across the application.

## Acceptance Criteria

```gherkin
Given an OFACDataError is raised
When it is caught in an API route
Then it has a code attribute for structured error responses
And the error message is human-readable

Given I import from ofac.core.exceptions
When I use FileValidationError
Then it inherits from OFACError
And has code = "FILE_VALIDATION_ERROR"
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create exceptions.py with base OFACError
  - [x] OFACError base class with code, message, details
  - [x] to_dict() method for API responses
  - [x] Informative __repr__ for debugging
- [x] Task 2: Add specific exception classes with error codes
  - [x] FileValidationError hierarchy (FILE_*)
  - [x] OFACDataError hierarchy (OFAC_*)
  - [x] ScreeningError hierarchy (SCREEN_*)
  - [x] ConfigurationError hierarchy (CONFIG_*)
- [x] Task 3: Write unit tests (33 tests)
  - [x] Base OFACError tests (7)
  - [x] File validation error tests (7)
  - [x] OFAC data error tests (7)
  - [x] Screening error tests (5)
  - [x] Configuration error tests (2)
  - [x] Import tests (2)
  - [x] Usage pattern tests (3)
- [x] Task 4: Run review and fix issues
  - [x] ruff check passes
  - [x] mypy passes
- [x] Task 5: Commit changes

## Exception Hierarchy

```
OFACError (base)
├── FileValidationError (FILE_*)
│   ├── FileFormatError (FILE_INVALID_FORMAT)
│   ├── FileEmptyError (FILE_EMPTY)
│   ├── FileTooLargeError (FILE_TOO_LARGE)
│   ├── FileParseError (FILE_PARSE_ERROR)
│   └── ColumnMappingError (FILE_COLUMN_MAPPING_ERROR)
├── OFACDataError (OFAC_*)
│   ├── OFACDownloadError (OFAC_DOWNLOAD_ERROR)
│   ├── OFACParseError (OFAC_PARSE_ERROR)
│   ├── OFACIntegrityError (OFAC_INTEGRITY_ERROR)
│   ├── OFACNotLoadedError (OFAC_NOT_LOADED)
│   └── OFACStaleDataError (OFAC_STALE_DATA)
├── ScreeningError (SCREEN_*)
│   ├── ScreeningInputError (SCREEN_INVALID_INPUT)
│   ├── ScreeningTimeoutError (SCREEN_TIMEOUT)
│   └── BatchTooLargeError (SCREEN_BATCH_TOO_LARGE)
└── ConfigurationError (CONFIG_*)
    └── InvalidThresholdError (CONFIG_INVALID_THRESHOLD)
```

## Dev Notes

### References
- [Source: docs/architecture.md#Error Handling Pattern]
- [Source: docs/project_context.md#Error Codes]
- [Source: docs/epics.md#Story 1.4]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/core/exceptions.py with full hierarchy
- ✅ 16 exception classes covering all error categories
- ✅ to_dict() method for easy API response generation
- ✅ Exported all exceptions from ofac.core
- ✅ 33 exception tests pass
- ✅ Total 108 unit tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/core/exceptions.py
- tests/unit/test_exceptions.py

**Modified Files:**
- src/ofac/core/__init__.py (exports exceptions)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.4 implemented with full dev → review → commit cycle
