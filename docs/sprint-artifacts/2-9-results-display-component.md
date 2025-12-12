# Story 2.9: Results Display Component

Status: done

## Story

As a **compliance officer**,
I want to see screening results with clear status indicators,
So that I can quickly identify issues.

## Acceptance Criteria

```gherkin
Given screening is complete
When I view results
Then I see a table with all organizations
And each row has a status badge (OK/REVIEW/NOK)
And I can filter by status

Given a result is NOK
When I view the table
Then the row is highlighted in red
And the status badge shows "NOK" prominently
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create streamlit/components/results.py
  - [x] render_results() function
- [x] Task 2: Implement results table
  - [x] Convert results to DataFrame
  - [x] Display with st.markdown HTML table
- [x] Task 3: Add status badges
  - [x] _get_status_badge() function
  - [x] CSS classes for OK/REVIEW/NOK
- [x] Task 4: Add filtering
  - [x] st.selectbox for status filter
  - [x] Filter DataFrame by status
- [x] Task 5: Add expandable match details
  - [x] st.expander for each result
  - [x] Display match details (SDN name, score, programs)
- [x] Task 6: Add summary metrics
  - [x] st.metric for total, OK, REVIEW, NOK counts
- [x] Task 7: Integrate with app.py
- [x] Task 8: Run review and commit

## Results Display Features

- Summary metrics (total, OK, REVIEW, NOK)
- Results table with status badges
- Status filtering
- Expandable match details
- Match information display

## Dev Notes

### Status Badges
- Uses CSS classes: .status-ok, .status-review, .status-nok
- HTML badges rendered via st.markdown with unsafe_allow_html

### Match Details
- Expandable sections per entity
- Shows SDN name, match type, score, programs, country
- Only displayed for entities with matches

### References
- [Source: docs/epics.md#Story 2.9]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created streamlit/components/results.py
- ✅ Results table with status badges
- ✅ Status filtering
- ✅ Expandable match details
- ✅ Summary metrics
- ✅ Integration with workflow routing
- ✅ All linting passes: `ruff check` ✓

### File List
**New Files:**
- src/ofac/streamlit/components/results.py

**Modified Files:**
- src/ofac/streamlit/app.py (workflow routing)
- src/ofac/streamlit/components/__init__.py

## Change Log
- 2025-12-12: Story 2.9 implemented with full dev → review → commit cycle
