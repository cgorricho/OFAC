# Story 3.1: OK/REVIEW/NOK Classification Logic

Status: done

## Story

As a **developer**,
I want threshold-based classification,
So that match scores are converted to actionable statuses.

## Acceptance Criteria

```gherkin
Given a match score of 95
When classification runs
Then status is NOK

Given a match score of 85
When classification runs
Then status is REVIEW

Given a match score of 75
When classification runs
Then status is OK

Given thresholds are configured as 90/75
When a score of 88 is classified
Then status is REVIEW (between thresholds)
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Enhance classifier.py with ScreeningClassifier class
  - [x] ScreeningClassifier class with configurable thresholds
  - [x] classify() method
- [x] Task 2: Implement threshold validation
  - [x] Validate threshold_review < threshold_nok
- [x] Task 3: Maintain backward compatibility
  - [x] Keep classify_screening_result() function
- [x] Task 4: Write unit tests (9 tests)
  - [x] NOK classification tests
  - [x] REVIEW classification tests
  - [x] OK classification tests
  - [x] Custom thresholds tests
  - [x] Invalid thresholds tests
- [x] Task 5: Update exports
- [x] Task 6: Run review and commit

## Classification Logic

```python
from ofac.core.classifier import ScreeningClassifier

classifier = ScreeningClassifier()
status = classifier.classify(95)  # Returns MatchStatus.NOK
status = classifier.classify(85)  # Returns MatchStatus.REVIEW
status = classifier.classify(75)  # Returns MatchStatus.OK
```

**Classification Rules:**
- NOK: score >= threshold_nok (default: 95)
- REVIEW: threshold_review <= score < threshold_nok (default: 80-94)
- OK: score < threshold_review (default: <80)

## Dev Notes

### Backward Compatibility
- Maintained `classify_screening_result()` function for existing code
- New code should use `ScreeningClassifier` class

### References
- [Source: docs/epics.md#Story 3.1]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Enhanced classifier.py with ScreeningClassifier class
- ✅ Configurable thresholds with validation
- ✅ Backward compatibility maintained
- ✅ 9 unit tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/core/classifier.py (enhanced with class)
- src/ofac/core/__init__.py (export ScreeningClassifier)

**New Files:**
- tests/unit/test_classifier.py

## Change Log
- 2025-12-12: Story 3.1 implemented with full dev → review → commit cycle
