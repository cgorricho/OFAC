# Story 3.4: Humanitarian Keyword Detection

Status: done

## Story

As a **developer**,
I want to detect humanitarian context in project descriptions,
So that humanitarian aid operations are handled appropriately.

## Acceptance Criteria

```gherkin
Given a project description "Emergency medical supplies for Syria"
When humanitarian detection runs
Then is_humanitarian returns True
And detected_keywords includes ["emergency", "medical"]

Given a description "Banking services in Damascus"
When humanitarian detection runs
Then is_humanitarian returns False
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Add humanitarian detection to classifier.py
  - [x] detect_humanitarian_keywords() function
- [x] Task 2: Implement keyword list
  - [x] 20 humanitarian keywords
- [x] Task 3: Implement detection logic
  - [x] Case-insensitive matching
  - [x] Word boundary matching (avoid partial matches)
  - [x] Returns (is_humanitarian, detected_keywords)
- [x] Task 4: Write unit tests (9 tests)
  - [x] Keyword detection tests
  - [x] Case-insensitive tests
  - [x] Word boundary tests
  - [x] Edge case tests
- [x] Task 5: Update exports
- [x] Task 6: Run review and commit

## Humanitarian Keyword Detection

```python
from ofac.core.classifier import detect_humanitarian_keywords

is_humanitarian, keywords = detect_humanitarian_keywords(
    "Emergency medical supplies for Syria"
)
# Returns: (True, ["emergency", "medical"])
```

**Keywords List (20):**
humanitarian, aid, relief, medical, emergency, food, water, shelter,
assistance, refugee, disaster, crisis, healthcare, medicine, nutrition,
sanitation, education, protection, vulnerable, displaced

## Dev Notes

### Word Boundary Matching
- Uses regex word boundaries (\b) to avoid partial matches
- "aid" matches "aid" but not "paid" or "maid"

### Case Insensitive
- All matching is case-insensitive
- Keywords returned in lowercase

### References
- [Source: docs/epics.md#Story 3.4]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Added detect_humanitarian_keywords() to classifier.py
- ✅ 20 humanitarian keywords
- ✅ Case-insensitive word boundary matching
- ✅ Returns (is_humanitarian, detected_keywords) tuple
- ✅ 9 unit tests, all passing
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**Modified Files:**
- src/ofac/core/classifier.py (added humanitarian detection)
- src/ofac/core/__init__.py (export functions)

**New Files:**
- tests/unit/test_humanitarian_detection.py

## Change Log
- 2025-12-12: Story 3.4 implemented with full dev → review → commit cycle
