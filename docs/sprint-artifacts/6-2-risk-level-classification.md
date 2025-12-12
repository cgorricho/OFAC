# Story 6.2: Risk Level Classification

Status: done

## Story

As a **compliance officer**,
I want to see risk levels for matches,
So that I can prioritize review.

## Acceptance Criteria

```gherkin
Given a NOK match with score 98%
When risk level is calculated
Then risk is "High"

Given a REVIEW match with score 75%
When risk level is calculated
Then risk is "Medium"

Given a REVIEW match with score 60%
When risk level is calculated
Then risk is "Low"
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create core/risk.py module
- [x] Task 2: Implement RiskLevel enum (HIGH, MEDIUM, LOW)
- [x] Task 3: Implement classify_risk_level() function
- [x] Task 4: Risk rules: EXACT=HIGH, score>=90+country=HIGH, score>=70=MEDIUM, else=LOW
- [x] Task 5: Write unit tests (10 tests)
- [x] Task 6: Integrate into results component
- [x] Task 7: Display risk level with color coding
- [x] Task 8: Run review and commit

## Risk Level Classification

**Risk Rules:**
- HIGH: Exact match OR (score >= 90 AND country_match)
- MEDIUM: Score >= 70 AND (fuzzy match OR country mismatch)
- LOW: Score < 70 OR (fuzzy match AND country mismatch)

**Display:**
- Color-coded risk badges (red/orange/yellow)
- Shown in match details expansion

## Dev Notes

### Implementation
- RiskLevel enum with HIGH, MEDIUM, LOW
- classify_risk_level() function with clear rules
- Integrated into results component
- Color-coded display for visual prioritization

### References
- [Source: docs/epics.md#Story 6.2]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created core/risk.py module
- ✅ RiskLevel enum and classify_risk_level() function
- ✅ 10 unit tests, all passing
- ✅ Integrated into results component
- ✅ Color-coded risk display
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/core/risk.py
- tests/unit/test_risk.py

**Modified Files:**
- src/ofac/core/__init__.py (export RiskLevel, classify_risk_level)
- src/ofac/streamlit/components/results.py (display risk level)

## Change Log
- 2025-12-12: Story 6.2 implemented with full dev → review → commit cycle

