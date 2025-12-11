# Story 1.8: Basic Matching Engine

Status: done

## Story

As a **developer**,
I want fuzzy string matching against OFAC entities,
So that I can identify potential sanctions matches.

## Acceptance Criteria

```gherkin
Given OFAC data is loaded
When I call matcher.match("ACME Corporation")
Then a list of MatchResult is returned
And each result has a match_score (0-100)
And results are sorted by score descending

Given I match "Archdiocèse de Bangui" against "Archdiocese of Bangui"
When using token_sort_ratio algorithm
Then the match score is >= 85

Given I match an entity with no close matches
When the highest score is < 80
Then an empty list is returned (or list with low scores)
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create core/matcher.py with EntityMatcher class
  - [x] EntityMatcher with OFACData input
  - [x] min_score parameter for threshold filtering
- [x] Task 2: Implement fuzzy matching with RapidFuzz
  - [x] Uses rapidfuzz.fuzz.token_sort_ratio
  - [x] Matches against sdn_name (primary names)
  - [x] Returns MatchResult objects with scores 0-100
- [x] Task 3: Add country-aware scoring
  - [x] +10 point boost if entity country matches OFAC country
  - [x] Score capped at 100
  - [x] country_match flag set correctly
- [x] Task 4: Add alias matching support
  - [x] Matches against aliases_by_ent dictionary
  - [x] MatchType.ALIAS for alias matches
  - [x] Country boost applied to alias matches
- [x] Task 5: Write unit tests (22 tests)
  - [x] Matcher initialization tests (4)
  - [x] Match method tests (8)
  - [x] Country-aware scoring tests (4)
  - [x] MatchResult structure tests (3)
  - [x] match_entity alias test (1)
  - [x] Import tests (1)
- [x] Task 6: Run review and commit

## EntityMatcher API

```python
from ofac.core.matcher import EntityMatcher
from ofac.data.loader import OFACDataLoader

# Load OFAC data
loader = OFACDataLoader()
data = loader.load()

# Create matcher
matcher = EntityMatcher(data, min_score=80)

# Match entity
matches = matcher.match("ACME Corporation", country="US", max_results=10)

# Results sorted by score descending
for match in matches:
    print(f"{match.sdn_name}: {match.match_score}% ({match.match_type})")
```

## Matching Algorithm

1. **Primary Name Matching**: Uses `token_sort_ratio` against sdn_name
2. **Alias Matching**: Also matches against all aliases for each entity
3. **Country Boost**: +10 points if entity country matches OFAC country
4. **Score Capping**: Scores never exceed 100
5. **Sorting**: Results sorted by score (descending)
6. **Filtering**: Only returns matches >= min_score threshold

## Match Types

- **EXACT**: score == 100 (perfect match)
- **FUZZY**: score < 100 (similarity match)
- **ALIAS**: Match found via alternate name

## Dev Notes

### RapidFuzz token_sort_ratio
- Tokenizes strings, sorts tokens, then compares
- Handles word order variations well
- Case-insensitive comparison
- Good for "Banco Nacional" vs "Nacional Banco"

### References
- [Source: docs/project_context.md#RapidFuzz Matching Rules]
- [Source: docs/epics.md#Story 1.8]
- [Source: docs/architecture.md#Matching Engine]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/core/matcher.py with EntityMatcher
- ✅ Uses rapidfuzz.fuzz.token_sort_ratio for fuzzy matching
- ✅ Matches against sdn_name and aliases
- ✅ Country-aware scoring (+10 boost, capped at 100)
- ✅ Returns MatchResult objects sorted by score
- ✅ 22 matcher tests pass
- ✅ Total 211 unit tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/core/matcher.py
- tests/unit/test_matcher.py

**Modified Files:**
- src/ofac/core/__init__.py (exports EntityMatcher)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-11: Story 1.8 implemented with full dev → review → commit cycle
