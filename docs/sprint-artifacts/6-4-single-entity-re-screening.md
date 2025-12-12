# Story 6.4: Single Entity Re-Screening

Status: done

## Story

As a **compliance officer**,
I want to re-screen a single entity after making changes,
So that I can verify my updates resolved the issue.

## Acceptance Criteria

```gherkin
Given I see a REVIEW or NOK result
When I click "Re-screen"
Then I am taken to the screening page
And the entity name is pre-filled
And I can modify and re-screen
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Add re-screen button to match details expansion
- [x] Task 2: Store entity info in session state
- [x] Task 3: Navigate to screening page
- [x] Task 4: Pre-fill entity in screening component
- [x] Task 5: Show re-screen indicator
- [x] Task 6: Allow cancel re-screen
- [x] Task 7: Run review and commit

## Single Entity Re-Screening

**Implementation:**
- Re-screen button in match details expansion
- Stores entity info in session state
- Navigates to screening page
- Pre-fills entity name and country
- Shows re-screen indicator

**User Experience:**
- One-click re-screen from results
- Pre-filled entity information
- Clear re-screen indicator
- Cancel option available

## Dev Notes

### Implementation
- Re-screen button stores entity in session state
- Screening component checks for rescreen_from_results flag
- Pre-fills entity information
- Clear visual indicator for re-screen mode

### References
- [Source: docs/epics.md#Story 6.4]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Added re-screen button to match details
- ✅ Session state for re-screen entity
- ✅ Navigation to screening page
- ✅ Pre-fill entity information
- ✅ Re-screen indicator and cancel option
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/streamlit/components/results.py (added re-screen button)
- src/ofac/streamlit/components/screening.py (added re-screen handling)

## Change Log
- 2025-12-12: Story 6.4 implemented with full dev → review → commit cycle

