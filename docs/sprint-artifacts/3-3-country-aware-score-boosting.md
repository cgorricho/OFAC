# Story 3.3: Country-Aware Score Boosting

Status: done

## Story

As a **developer**,
I want to boost scores when entity country matches OFAC entry country,
So that geographic alignment increases match confidence.

## Acceptance Criteria

```gherkin
Given an entity from Syria matching an OFAC entry in Syria
When scoring runs
Then the score is boosted by 10 points

Given an entity from France matching an OFAC entry in Syria
When scoring runs
Then the score is NOT boosted

Given a boosted score exceeds 100
When normalization runs
Then the score is capped at 100
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Enhance matcher to use countries registry
  - [x] Import is_sanctioned_country from countries module
  - [x] Enhanced _check_country_match() method
- [x] Task 2: Make boost configurable via settings
  - [x] Added country_match_boost to Settings (default: 10)
  - [x] Use settings.country_match_boost in matcher
- [x] Task 3: Ensure score capping at 100
  - [x] min(100, score + boost) ensures capping
- [x] Task 4: Enhanced country matching logic
  - [x] Direct match, substring match, country code matching
- [x] Task 5: Run review and commit

## Country-Aware Boosting

```python
from ofac.core.matcher import EntityMatcher

matcher = EntityMatcher(ofac_data)
matches = matcher.match("Entity Name", country="Syria")

# If entity country matches OFAC entry country:
# - Score is boosted by country_match_boost (default: 10)
# - Score is capped at 100
# - country_match flag is set to True
```

**Country Matching Logic:**
- Direct match: "Syria" == "Syria"
- Substring match: "Syria" in "Syrian Arab Republic"
- Country code matching: "SY" matches "Syria" (for sanctioned countries)

## Dev Notes

### Configuration
- `country_match_boost` in Settings (default: 10, range: 0-50)
- Configurable via `OFAC_COUNTRY_MATCH_BOOST` environment variable

### Enhanced Matching
- Uses countries registry for better country code matching
- Handles country name variations
- Case-insensitive matching

### References
- [Source: docs/epics.md#Story 3.3]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Enhanced matcher with countries registry integration
- ✅ Added country_match_boost to Settings
- ✅ Enhanced _check_country_match() method
- ✅ Configurable boost amount
- ✅ Score capping at 100
- ✅ Existing tests verify functionality
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/core/matcher.py (enhanced country matching)
- src/ofac/core/config.py (added country_match_boost)

## Change Log
- 2025-12-12: Story 3.3 implemented with full dev → review → commit cycle
