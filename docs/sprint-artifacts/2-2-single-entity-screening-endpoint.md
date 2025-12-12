# Story 2.2: Single Entity Screening Endpoint

Status: done

## Story

As a **developer**,
I want an API endpoint to screen a single entity,
So that quick ad-hoc checks are possible.

## Acceptance Criteria

```gherkin
Given the API is running
When I POST to /screenings/single with {"entity_name": "Test Org"}
Then I receive a JSON response with screening results
And the response includes screening_id and timestamp
And the response status is 200

Given I POST with invalid JSON
When the request is processed
Then I receive status 400
And the error includes code and message
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create api/schemas.py with request/response models
  - [x] SingleScreeningRequest
  - [x] SingleScreeningResponse with data/meta wrapper
- [x] Task 2: Create api/deps.py for dependency injection
  - [x] get_ofac_data() dependency
  - [x] get_matcher() dependency
- [x] Task 3: Create api/routes/screening.py
  - [x] POST /screenings/single endpoint
  - [x] Integration with EntityMatcher
  - [x] Classification using classify_screening_result
- [x] Task 4: Create core/classifier.py
  - [x] classify_screening_result() function
  - [x] Uses settings thresholds
- [x] Task 5: Write integration tests (5 tests)
  - [x] Successful screening test
  - [x] Screening with country test
  - [x] Invalid JSON test
  - [x] Missing entity_name test
  - [x] No OFAC data test
- [x] Task 6: Run review and commit

## API Endpoint

```
POST /screenings/single
Content-Type: application/json

Request:
{
  "entity_name": "ACME Corporation",
  "country": "US",  // optional
  "description": "..."  // optional
}

Response:
{
  "data": {
    "screening_id": "uuid",
    "entity_input": {...},
    "match_status": "OK|REVIEW|NOK",
    "matches": [...],
    "highest_score": 85,
    "ofac_version": "...",
    "timestamp": "..."
  },
  "meta": {
    "ofac_version": "...",
    "duration_ms": 45
  }
}
```

## Dev Notes

### Classification Logic
- NOK: score >= match_threshold_nok (default: 95)
- REVIEW: score >= match_threshold_review (default: 80)
- OK: score < match_threshold_review

### References
- [Source: docs/epics.md#Story 2.2]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created api/schemas.py with request/response models
- ✅ Created api/deps.py for dependency injection
- ✅ Created api/routes/screening.py with POST /screenings/single
- ✅ Created core/classifier.py for OK/REVIEW/NOK classification
- ✅ 5 integration tests pass
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/api/schemas.py
- src/ofac/api/deps.py
- src/ofac/api/routes/screening.py
- src/ofac/core/classifier.py
- tests/integration/test_api_screening.py

**Modified Files:**
- src/ofac/api/main.py (register screening router)
- src/ofac/api/routes/__init__.py
- src/ofac/core/__init__.py (export classifier)

## Change Log
- 2025-12-12: Story 2.2 implemented with full dev → review → commit cycle
