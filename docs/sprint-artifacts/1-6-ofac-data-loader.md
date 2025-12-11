# Story 1.6: OFAC Data Loader

Status: done

## Story

As a **developer**,
I want to load OFAC CSV triplets into memory,
So that the matching engine can query them efficiently.

## Acceptance Criteria

```gherkin
Given valid OFAC CSV files exist at the configured path
When I call OFACDataLoader().load()
Then a DataFrame is returned with all SDN entries
And aliases are merged by ent_num
And the load completes in under 3 seconds

Given OFAC files don't exist
When I call OFACDataLoader().load()
Then OFACDataError is raised with code "OFAC_DATA_NOT_FOUND"
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create data/loader.py with OFACDataLoader class
  - [x] OFACData NamedTuple for returned data
  - [x] OFACDataLoader with configurable data_path
  - [x] is_loaded property and clear_cache() method
- [x] Task 2: Implement load() method for CSV triplets
  - [x] Parse SDN.CSV, ALT.CSV, ADD.CSV
  - [x] Handle UTF-8 with Latin-1 fallback
  - [x] Convert ent_num to integers
  - [x] Handle OFAC null markers (-0-)
- [x] Task 3: Build lookup structures
  - [x] aliases_by_ent: Dict[int, List[str]]
  - [x] addresses_by_ent: Dict[int, List[str]]
  - [x] get_aliases(ent_num) and get_countries(ent_num) methods
- [x] Task 4: Add error handling
  - [x] OFACParseError with OFAC_DATA_NOT_FOUND code
  - [x] OFACNotLoadedError when accessing data before load
- [x] Task 5: Write unit tests (28 tests)
  - [x] Created mock OFAC data files
  - [x] Loader initialization tests (6)
  - [x] Load method tests (10)
  - [x] Missing file tests (2)
  - [x] Alias lookup tests (3)
  - [x] Country lookup tests (3)
  - [x] Data content tests (3)
  - [x] Import tests (1)

## OFACDataLoader API

```python
from ofac.data.loader import OFACDataLoader

# Initialize with default path from settings
loader = OFACDataLoader()

# Or custom path
loader = OFACDataLoader(data_path=Path("./custom/path"))

# Load data (cached after first call)
data = loader.load()
data = loader.load(force_reload=True)  # Force reload

# Access DataFrames
data.sdn_df      # SDN entries
data.alt_df      # Alternate names
data.add_df      # Addresses
data.version     # OFACDataVersion metadata

# Lookup helpers
aliases = loader.get_aliases(306)    # ["NATIONAL BANK OF CUBA", ...]
countries = loader.get_countries(306) # ["Switzerland", "Cuba"]

# Cache management
loader.is_loaded   # True/False
loader.clear_cache()
```

## Dev Notes

### Mock OFAC Data Files
Created in `tests/fixtures/mock_ofac_data/`:
- sdn.csv: 4 entries (BANCO NACIONAL, AL-QAIDA, IRGC, TEST VESSEL)
- alt.csv: 6 aliases
- add.csv: 5 addresses

### References
- [Source: docs/architecture.md#Data Architecture]
- [Source: docs/epics.md#Story 1.6]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/data/loader.py with OFACDataLoader
- ✅ OFACData NamedTuple with all DataFrames and lookups
- ✅ UTF-8/Latin-1 encoding fallback
- ✅ Automatic ent_num type conversion
- ✅ Built alias and country lookup dictionaries
- ✅ Created mock OFAC test data files
- ✅ 28 loader tests pass
- ✅ Total 173 unit tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/data/loader.py
- tests/unit/test_loader.py
- tests/fixtures/mock_ofac_data/sdn.csv
- tests/fixtures/mock_ofac_data/alt.csv
- tests/fixtures/mock_ofac_data/add.csv

**Modified Files:**
- src/ofac/data/__init__.py (exports OFACDataLoader)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.6 implemented with full dev → review → commit cycle
