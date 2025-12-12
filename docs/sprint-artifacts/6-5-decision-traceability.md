# Story 6.5: Decision Traceability

Status: done

## Story

As a **compliance officer**,
I want to record my review decisions with timestamps,
So that I have an audit trail for compliance.

## Acceptance Criteria

```gherkin
Given I review a flagged case
When I select a decision (Approved/Rejected/Requires Further Review)
Then the decision is recorded
And a timestamp is stored
And the timestamp is displayed
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Add decision radio buttons to match details
- [x] Task 2: Store decision in session state
- [x] Task 3: Record timestamp when decision changes
- [x] Task 4: Display decision timestamp
- [x] Task 5: Options: Pending, Approved, Rejected, Requires Further Review
- [x] Task 6: Run review and commit

## Decision Traceability

**Implementation:**
- Decision radio buttons in match details expansion
- Options: Pending, Approved, Rejected, Requires Further Review
- Timestamp recorded when decision changes
- Timestamp displayed to user

**Audit Trail:**
- Decision stored in session state
- Timestamp in ISO format
- Clear display of decision and timestamp

## Dev Notes

### Implementation
- Uses st.radio for decision selection
- Session state for decision and timestamp
- Timestamp recorded on decision change
- ISO format timestamp for audit trail

### References
- [Source: docs/epics.md#Story 6.5]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Added decision radio buttons
- ✅ Session state for decision and timestamp
- ✅ Timestamp recorded on decision change
- ✅ Clear display of decision and timestamp
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/streamlit/components/results.py (added decision traceability)

## Change Log
- 2025-12-12: Story 6.5 implemented with full dev → review → commit cycle

