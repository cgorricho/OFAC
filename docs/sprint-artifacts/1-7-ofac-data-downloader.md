# Story 1.7: OFAC Data Downloader

Status: done

## Story

As a **developer**,
I want to download OFAC files from Treasury.gov,
So that the local cache can be populated and updated.

## Acceptance Criteria

```gherkin
Given I call OFACUpdater().download_sdn_files()
When the download completes successfully
Then SDN.CSV, ALT.CSV, ADD.CSV are saved to a temp directory
And a version.json with download timestamp is created

Given a download fails mid-way
When the error is caught
Then existing cached files are not corrupted
And OFACDataError is raised with details
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create data/updater.py with OFACUpdater class
  - [x] OFACUpdater with configurable data_path and timeout
  - [x] Treasury.gov URL constants (OFAC_BASE_URL, SDN_FILES)
- [x] Task 2: Implement download_sdn_files() method
  - [x] Download all 3 CSV files using httpx
  - [x] Extract Last-Modified headers
  - [x] Handle HTTP errors, timeouts, network errors
- [x] Task 3: Add atomic swap mechanism
  - [x] Download to temporary directory first
  - [x] Validate files before swap
  - [x] Move files atomically (all or nothing)
  - [x] Preserve existing files on failure
- [x] Task 4: Add version tracking
  - [x] Create version.json with download_date, last_modified
  - [x] Track file sizes
  - [x] get_current_version() method
  - [x] check_for_updates() method
- [x] Task 5: Write unit tests (16 tests)
  - [x] Updater initialization tests (3)
  - [x] Download success/failure tests (5)
  - [x] Version tracking tests (3)
  - [x] Update check tests (4)
  - [x] Import tests (1)
- [x] Task 6: Run review and commit

## OFACUpdater API

```python
from ofac.data.updater import OFACUpdater

# Initialize
updater = OFACUpdater(data_path=Path("./data/ofac"))

# Download SDN files
version_info = updater.download_sdn_files()
# Returns: {
#   "download_date": "2025-12-11T10:30:00Z",
#   "last_modified": "2025-12-10T15:00:00Z",
#   "files_downloaded": ["sdn.csv", "alt.csv", "add.csv"],
#   "file_sizes": {...}
# }

# Check current version
version = updater.get_current_version()

# Check if update needed
needs_update = updater.check_for_updates()
```

## Dev Notes

### Atomic Swap Mechanism
1. Download all files to temporary directory
2. Validate all files (non-empty, valid CSV)
3. Move files to data_path (atomic operation)
4. Create version.json
5. If any step fails, existing files remain untouched

### Error Handling
- HTTP errors → OFACDownloadError with status code
- Network timeouts → OFACDownloadError with timeout details
- Empty/corrupted files → OFACIntegrityError
- All errors preserve existing cached files

### References
- [Source: docs/architecture.md#Data Architecture]
- [Source: docs/epics.md#Story 1.7]
- [Source: docs/conceptual-design/20251206_OFAC_List_Update_Policies_and_Strategy.md]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/data/updater.py with OFACUpdater
- ✅ Atomic swap mechanism prevents data corruption
- ✅ Version tracking with version.json
- ✅ check_for_updates() compares Last-Modified headers
- ✅ Comprehensive error handling (HTTP, timeout, network)
- ✅ 16 updater tests pass
- ✅ Total 189 unit tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/data/updater.py
- tests/unit/test_updater.py

**Modified Files:**
- src/ofac/data/__init__.py (exports OFACUpdater)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.7 implemented with full dev → review → commit cycle
