# Story 6.1: Match Details Expansion

Status: done

## Story

As a **compliance officer**,
I want to expand match details for flagged cases,
So that I can understand why a match occurred.

## Acceptance Criteria

```gherkin
Given I see a REVIEW or NOK result
When I click to expand details
Then I see: matched SDN name, SDN type, match score, match algorithm, country alignment
And I see OFAC entity ID and programs
And I see General License notes if applicable
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Enhance expandable match details in results.py
- [x] Task 2: Display SDN name, SDN type, match score, match algorithm
- [x] Task 3: Display country alignment (already implemented)
- [x] Task 4: Display OFAC entity ID (ent_num)
- [x] Task 5: Display programs list
- [x] Task 6: Display General License notes if applicable
- [x] Task 7: Format for readability
- [x] Task 8: Run review and commit

## Match Details Expansion

**Enhancements:**
- Added SDN Type display
- Added Match Algorithm (match_type)
- Added OFAC Entity ID (ent_num)
- Enhanced Programs display
- Added General License notes display
- Improved formatting for readability

**Display Fields:**
- SDN Name
- SDN Type
- Match Type
- Match Score
- Match Algorithm
- Input Country
- OFAC Entry Country
- Country Alignment
- OFAC Entity ID
- Programs
- General License Notes

## Dev Notes

### Implementation
- Enhanced existing st.expander in results.py
- Added all required fields from MatchResult
- Improved formatting and readability
- Handles missing fields gracefully

### References
- [Source: docs/epics.md#Story 6.1]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Enhanced expandable match details
- ✅ Added SDN Type, Match Algorithm, Entity ID, Programs, GL Notes
- ✅ Improved formatting for readability
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/streamlit/components/results.py (enhanced match details)

## Change Log
- 2025-12-12: Story 6.1 implemented with full dev → review → commit cycle

