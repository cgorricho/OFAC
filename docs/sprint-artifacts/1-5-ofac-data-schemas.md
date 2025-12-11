# Story 1.5: OFAC Data Schemas

Status: done

## Story

As a **developer**,
I want Pydantic models representing OFAC data structures,
So that CSV parsing is validated and typed.

## Acceptance Criteria

```gherkin
Given I parse a row from SDN.CSV
When I create an SDNEntry from the row data
Then all OFAC fields are properly typed
And ent_num is an integer
And sdn_name is a string

Given I have SDN, Alt, and Address entries
When I link them by ent_num
Then I can retrieve all aliases for an entity
And I can retrieve all addresses for an entity
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create data/schemas.py with OFAC models
  - [x] SDNType enum (individual, entity, vessel, aircraft)
  - [x] AltType enum (aka, fka, nka)
- [x] Task 2: Add SDNEntry, AltEntry, AddressEntry models
  - [x] SDNEntry with 12 fields matching SDN.CSV
  - [x] AltEntry with 5 fields matching ALT.CSV
  - [x] AddressEntry with 6 fields matching ADD.CSV
  - [x] OFACDataVersion for metadata tracking
- [x] Task 3: Add validation and conversion
  - [x] Convert OFAC null marker '-0-' to None
  - [x] Coerce string IDs to integers
  - [x] Strip whitespace from strings
  - [x] programs_list property for parsing
- [x] Task 4: Write unit tests (37 tests)
  - [x] Enum tests (7)
  - [x] SDNEntry tests (11)
  - [x] AltEntry tests (5)
  - [x] AddressEntry tests (4)
  - [x] OFACDataVersion tests (3)
  - [x] CSV column tests (3)
  - [x] Import tests (2)
  - [x] Real-world example tests (3)
- [x] Task 5: Commit changes

## OFAC Schema Models

| Model | Purpose | Key Fields |
|-------|---------|------------|
| `SDNEntry` | SDN.CSV parsing | ent_num, sdn_name, programs, remarks |
| `AltEntry` | ALT.CSV parsing | ent_num, alt_num, alt_name, alt_type |
| `AddressEntry` | ADD.CSV parsing | ent_num, add_num, country |
| `OFACDataVersion` | Metadata tracking | publish_date, counts, source |

## Dev Notes

### OFAC Null Handling
- OFAC uses `-0-` to represent null/empty values
- All schemas convert `-0-` to Python `None` via field_validator

### CSV Column Mappings
```python
SDN_CSV_COLUMNS = ["ent_num", "sdn_name", "sdn_type", "programs", ...]
ALT_CSV_COLUMNS = ["ent_num", "alt_num", "alt_type", "alt_name", ...]
ADD_CSV_COLUMNS = ["ent_num", "add_num", "address", "city_state_zip", "country", ...]
```

### References
- [Source: docs/conceptual-design/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md]
- [Source: docs/epics.md#Story 1.5]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/data/schemas.py with 4 models + 2 enums
- ✅ Handles OFAC null marker '-0-' conversion
- ✅ Type coercion for ID fields (string → int)
- ✅ Exported from ofac.data module
- ✅ 37 schema tests pass
- ✅ Total 145 unit tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/data/schemas.py
- tests/unit/test_ofac_schemas.py

**Modified Files:**
- src/ofac/data/__init__.py (exports schemas)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.5 implemented with full dev → review → commit cycle
