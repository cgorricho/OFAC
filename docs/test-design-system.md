# System-Level Test Design

**Project:** OFAC Sanctions Screening Tool
**Date:** 2025-12-09
**Author:** Carlos
**Workflow:** Test Design (System-Level Mode)
**Phase:** Solutioning (Phase 2)

---

## Executive Summary

This document provides the system-level testability assessment for the OFAC Screening Tool architecture, evaluating controllability, observability, and reliability before implementation begins. It defines the test levels strategy, NFR testing approach, and identifies any testability concerns that could impact implementation.

**Assessment Result:** ✅ PASS (Architecture supports testability)

---

## Testability Assessment

### Controllability: ✅ PASS

**Can we control system state for testing?**

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **API Seeding** | ✅ Good | FastAPI dependency injection (`api/deps.py`) enables mock data injection |
| **Data Factories** | ✅ Good | Pydantic models (`core/models.py`) support easy test data creation |
| **OFAC Data Mocking** | ✅ Good | `data/loader.py` can load from `tests/fixtures/mock_ofac_data/` |
| **Configuration Override** | ✅ Good | Pydantic Settings supports env var override for tests |
| **Database Reset** | ✅ N/A | No database in Phase 1 (file-based, easy to reset) |

**Controllability Implementation:**

```python
# Example: Dependency override for testing
@pytest.fixture
def mock_ofac_loader():
    """Override OFAC data with test fixtures."""
    loader = OFACDataLoader(path=Path("tests/fixtures/mock_ofac_data"))
    return loader.load()

def test_screening_with_mock_data(mock_ofac_loader, client):
    app.dependency_overrides[get_ofac_data] = lambda: mock_ofac_loader
    response = client.post("/screenings/single", json={"entity_name": "Test"})
    assert response.status_code == 200
```

---

### Observability: ✅ PASS

**Can we inspect system state?**

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Structured Logging** | ✅ Good | Architecture specifies JSON logging with screening_id, duration_ms |
| **Error Codes** | ✅ Good | Custom exception hierarchy with prefixed codes (FILE_*, OFAC_*, SCREEN_*) |
| **Match Details** | ✅ Good | MatchResult includes score, match_type, algorithm, entity_id |
| **Version Tracking** | ✅ Good | Every screening response includes ofac_version |
| **Performance Metrics** | ✅ Good | API responses include duration_ms in meta object |

**Logging Structure (per Architecture):**

```json
{
  "timestamp": "2025-12-09T10:30:00Z",
  "level": "INFO",
  "event": "screening_complete",
  "screening_id": "scr_abc123",
  "ofac_version": "2025-12-08",
  "entities_processed": 150,
  "matches": {"ok": 140, "review": 8, "nok": 2},
  "duration_ms": 2340
}
```

**Test Validation Approach:**
- Unit tests can assert log output using log capture
- Integration tests verify JSON response structure
- Performance tests measure and assert timing metrics

---

### Reliability: ✅ PASS

**Are tests isolated and reproducible?**

| Aspect | Assessment | Evidence |
|--------|------------|----------|
| **Test Isolation** | ✅ Good | No shared database, session state scoped to test |
| **Deterministic Matching** | ✅ Good | RapidFuzz algorithm is deterministic |
| **Parallel-Safe** | ✅ Good | Each test can use isolated data fixtures |
| **Cleanup Discipline** | ✅ Good | pytest fixtures with yield for teardown |
| **No Race Conditions** | ✅ Good | Single-user Phase 1, no concurrency concerns |

**Test Isolation Patterns:**

```python
# Fixture with automatic cleanup
@pytest.fixture
def temp_ofac_cache(tmp_path):
    """Isolated OFAC cache for each test."""
    cache_dir = tmp_path / "ofac"
    cache_dir.mkdir()
    yield cache_dir
    # Cleanup automatic via tmp_path
```

---

## Architecturally Significant Requirements (ASRs)

These quality requirements drive architecture and pose testability challenges.

### ASR-1: Screening Performance

| Attribute | Details |
|-----------|---------|
| **Requirement** | Screen 100 entities in <5 minutes (NFR1), single entity in <2 seconds (NFR2) |
| **Probability** | 2 (Possible - depends on implementation) |
| **Impact** | 2 (Degraded - slow screening frustrates workflow) |
| **Risk Score** | 4 (Medium) |
| **Test Approach** | Integration tests with timing assertions; benchmark tests for regression |

**Test Strategy:**
```python
def test_batch_screening_performance(client, sample_100_entities):
    start = time.time()
    response = client.post("/screenings/batch", files={"file": sample_100_entities})
    duration = time.time() - start
    assert duration < 300  # 5 minutes
    assert response.status_code == 200
```

---

### ASR-2: Matching Accuracy

| Attribute | Details |
|-----------|---------|
| **Requirement** | Zero false negatives (NFR22), 10-30% false positive rate acceptable (NFR23) |
| **Probability** | 2 (Possible - threshold tuning critical) |
| **Impact** | 3 (Critical - false negative = compliance violation) |
| **Risk Score** | 6 (High - immediate mitigation required) |
| **Test Approach** | Golden test set with known matches; alias detection tests; boundary threshold tests |

**Test Strategy:**
```python
# Golden test set - must never fail
KNOWN_MATCHES = [
    ("Archdiocese of Bangui", "ARCHDIOCESE OF BANGUI", True),  # Exact
    ("Archdiocèse de Bangui", "ARCHDIOCESE OF BANGUI", True),  # Fuzzy
    ("Al-Noor Trading", "AL-NOOR TRADING CO", True),           # Partial
]

@pytest.mark.parametrize("input,expected_match,should_match", KNOWN_MATCHES)
def test_golden_matches(matcher, input, expected_match, should_match):
    result = matcher.match(input)
    found = any(r.sdn_name == expected_match for r in result)
    assert found == should_match, f"False negative detected: {input}"
```

---

### ASR-3: Audit Trail Completeness

| Attribute | Details |
|-----------|---------|
| **Requirement** | 10-year retention-ready reports (NFR47), complete traceability (NFR50) |
| **Probability** | 1 (Unlikely to fail if implemented correctly) |
| **Impact** | 3 (Critical - audit failure = compliance violation) |
| **Risk Score** | 3 (Medium) |
| **Test Approach** | Schema validation tests; report field completeness assertions |

**Test Strategy:**
```python
def test_report_audit_fields(report_generator, screening_results):
    report = report_generator.generate(screening_results)
    # Every report MUST have these fields
    assert "screening_id" in report.summary
    assert "timestamp" in report.summary
    assert "ofac_version" in report.summary
    for row in report.details:
        assert row["match_score"] is not None
        assert row["ofac_entity_id"] is not None
```

---

### ASR-4: Data Integrity

| Attribute | Details |
|-----------|---------|
| **Requirement** | Atomic swap for OFAC updates (NFR24), rollback on failure (NFR25) |
| **Probability** | 2 (Possible - network failures happen) |
| **Impact** | 3 (Critical - corrupt data = wrong screening results) |
| **Risk Score** | 6 (High - immediate mitigation required) |
| **Test Approach** | Failure injection tests; atomic operation verification |

**Test Strategy:**
```python
def test_failed_download_preserves_existing_data(updater, monkeypatch):
    """Simulate download failure and verify rollback."""
    original_version = updater.get_current_version()
    
    # Inject failure
    monkeypatch.setattr(httpx, "get", lambda *args: raise_connection_error())
    
    with pytest.raises(OFACDataError):
        updater.download_and_update()
    
    # Verify rollback
    assert updater.get_current_version() == original_version
```

---

### ASR-5: Humanitarian Context Detection

| Attribute | Details |
|-----------|---------|
| **Requirement** | General License flagging (FR27-29), sanctioned country registry (FR24) |
| **Probability** | 2 (Possible - keyword detection may miss edge cases) |
| **Impact** | 2 (Degraded - blocks legitimate humanitarian aid) |
| **Risk Score** | 4 (Medium) |
| **Test Approach** | Comprehensive keyword coverage tests; country registry validation |

**Test Strategy:**
```python
HUMANITARIAN_SCENARIOS = [
    ("Syria medical aid", "SY", True, "GL-21"),
    ("Iran food assistance", "IR", True, "GL D-1"),
    ("Syria banking", "SY", False, None),  # Not humanitarian
]

@pytest.mark.parametrize("desc,country,is_humanitarian,expected_gl", HUMANITARIAN_SCENARIOS)
def test_humanitarian_detection(classifier, desc, country, is_humanitarian, expected_gl):
    result = classifier.classify_with_context(entity_country=country, description=desc)
    assert result.is_humanitarian == is_humanitarian
    assert result.general_license == expected_gl
```

---

## Test Levels Strategy

### Recommended Split

Based on the OFAC architecture (API-heavy, Streamlit frontend, compliance domain):

| Level | Percentage | Rationale |
|-------|------------|-----------|
| **Unit Tests** | 50% | Core matching logic, classification rules, data parsing |
| **Integration Tests** | 35% | API endpoints, data loader, OFAC update flow |
| **E2E Tests** | 15% | Critical user journeys (upload → screen → download) |

### Test Level Definitions

#### Unit Tests (50%)

**Target Modules:**
- `core/matcher.py` - Fuzzy matching algorithm
- `core/classifier.py` - OK/REVIEW/NOK classification, humanitarian detection
- `core/models.py` - Pydantic validation
- `core/reporter.py` - Excel generation logic
- `data/schemas.py` - OFAC data parsing

**Characteristics:**
- Fast (<100ms per test)
- No external dependencies
- Mock all I/O operations
- Test edge cases and boundary conditions

**Example Coverage:**
```
tests/unit/
├── test_matcher.py          # ~20 tests (fuzzy matching algorithms)
├── test_classifier.py       # ~15 tests (thresholds, humanitarian)
├── test_models.py           # ~10 tests (Pydantic validation)
├── test_reporter.py         # ~10 tests (Excel generation)
└── test_config.py           # ~5 tests (configuration loading)
```

#### Integration Tests (35%)

**Target Modules:**
- `api/routes/screening.py` - Batch and single screening endpoints
- `api/routes/data.py` - OFAC status and update endpoints
- `data/loader.py` - CSV triplet parsing with real test data
- `data/updater.py` - Download and atomic swap (with mocked network)

**Characteristics:**
- Medium speed (<5s per test)
- Test component interactions
- Use real test fixtures
- Verify API contracts

**Example Coverage:**
```
tests/integration/
├── test_api_screening.py    # ~15 tests (POST /screenings/*)
├── test_api_data.py         # ~10 tests (GET/POST /data/*)
├── test_data_loader.py      # ~10 tests (CSV parsing)
└── test_pipeline.py         # ~8 tests (end-to-end pipeline)
```

#### E2E Tests (15%)

**Target Scenarios:**
- Complete screening workflow (upload → map → screen → download)
- OFAC update workflow (check → update → verify)
- Error recovery scenarios

**Characteristics:**
- Slower (<30s per test)
- Test through Streamlit UI or API
- Verify complete user journeys
- Minimal (critical paths only)

**Example Coverage:**
```
tests/e2e/
├── test_screening_workflow.py   # ~5 tests (complete journey)
├── test_ofac_update.py          # ~3 tests (data refresh)
└── test_error_recovery.py       # ~3 tests (graceful degradation)
```

---

## NFR Testing Approach

### Security Testing

| NFR | Test Approach | Tools |
|-----|--------------|-------|
| NFR9: Localhost only | Integration test verifying no external network calls | pytest + network mocking |
| NFR10: No external transmission | Code review + test assertions | Static analysis |
| NFR19: Input validation | Fuzz testing on file uploads | pytest + hypothesis |
| NFR20: Generic error messages | API error response tests | pytest |

**Phase 1 Security Focus:**
- Input validation (file size, format, column limits)
- Error message sanitization
- No secrets in logs

### Performance Testing

| NFR | Test Approach | Tools |
|-----|--------------|-------|
| NFR1: Batch <5 min | Benchmark tests with 100 entities | pytest-benchmark |
| NFR2: Single <2 sec | Unit tests with timing assertions | time.time() |
| NFR7: Report <10 sec | Integration tests | pytest |
| NFR8: Update <2 min | Integration tests with mocked network | pytest + httpx mock |

**Performance Test Strategy:**
```python
# Benchmark in CI
@pytest.mark.benchmark
def test_batch_screening_benchmark(benchmark, client, sample_entities):
    result = benchmark(client.post, "/screenings/batch", files={"file": sample_entities})
    assert benchmark.stats["mean"] < 0.1  # 100ms per entity
```

### Reliability Testing

| NFR | Test Approach | Tools |
|-----|--------------|-------|
| NFR22: Zero false negatives | Golden test set | pytest |
| NFR24: Atomic swap | Failure injection | monkeypatch |
| NFR28: Network failure handling | Mock failures | httpx mock |
| NFR29: Clear error messages | Error scenario tests | pytest |

### Maintainability Testing

| NFR | Test Approach | Tools |
|-----|--------------|-------|
| NFR30: Externalized GL mapping | Config-driven tests | pytest |
| NFR33: Adjustable thresholds | Config override tests | pytest |
| NFR35: Auto-generated docs | OpenAPI validation | pytest + openapi-spec-validator |

---

## Test Environment Requirements

### Local Development

```yaml
Environment: Development
Requirements:
  - Python 3.11+
  - uv for dependency management
  - pytest with plugins (pytest-cov, pytest-asyncio, pytest-mock)
  - Mock OFAC data (tests/fixtures/mock_ofac_data/)
  
Setup:
  - uv pip install -e ".[dev]"
  - pre-commit install
  - pytest runs all unit and integration tests
```

### CI Pipeline

```yaml
Environment: GitHub Actions / CI
Requirements:
  - Python 3.11 matrix
  - Isolated virtual environment per run
  - No network access to treasury.gov (use mocks)
  - Coverage reporting (≥80% target)

Stages:
  1. lint: ruff check + ruff format --check
  2. type-check: mypy --strict
  3. unit-tests: pytest tests/unit/ --cov
  4. integration-tests: pytest tests/integration/
  5. coverage-report: fail if <80%
```

### Test Data Requirements

```
tests/fixtures/
├── sample_entities.csv          # 20 test entities
├── sample_entities.xlsx         # Excel version
├── sample_100_entities.xlsx     # Performance testing
├── invalid_format.pdf           # Error handling
├── invalid_encoding.csv         # Encoding edge cases
└── mock_ofac_data/
    ├── sdn.csv                  # 50 mock SDN entries
    ├── add.csv                  # 50 mock addresses
    └── alt.csv                  # 30 mock aliases
```

---

## Testability Concerns

### Concern 1: Streamlit Testing Complexity

| Attribute | Details |
|-----------|---------|
| **Concern** | Streamlit UI testing is non-trivial; no standard E2E framework |
| **Severity** | Low (workaround exists) |
| **Mitigation** | Focus E2E tests on API layer; use Streamlit only for manual smoke tests |
| **Recommendation** | Test Streamlit components as Python functions where possible |

**Approach:**
```python
# Test component logic, not Streamlit rendering
def test_upload_validation():
    """Test upload logic without Streamlit."""
    from ofac.streamlit.components.upload import validate_file
    
    valid_file = create_mock_xlsx()
    assert validate_file(valid_file) == True
    
    invalid_file = create_mock_pdf()
    assert validate_file(invalid_file) == False
```

### Concern 2: OFAC Data Mocking Fidelity

| Attribute | Details |
|-----------|---------|
| **Concern** | Mock OFAC data may not represent real-world complexity |
| **Severity** | Medium (could miss edge cases) |
| **Mitigation** | Create representative mock data; include known edge cases |
| **Recommendation** | Periodically validate against sample of real OFAC data |

**Mock Data Requirements:**
- Include Unicode characters (Archdiocèse, Москва)
- Include long names and aliases
- Include multiple countries per entity
- Include known sanctioned countries

### No Critical Concerns ✅

The architecture does not have any blocking testability issues. All identified concerns have viable mitigations.

---

## Recommendations for Sprint 0

### 1. Test Infrastructure Setup

| Priority | Task | Effort |
|----------|------|--------|
| P0 | Create `tests/conftest.py` with core fixtures | 2 hours |
| P0 | Create `tests/fixtures/mock_ofac_data/` | 2 hours |
| P0 | Configure pytest in `pyproject.toml` | 30 min |
| P0 | Add `pytest-cov` for coverage | 30 min |

### 2. Golden Test Set

| Priority | Task | Effort |
|----------|------|--------|
| P0 | Define 20+ known match/non-match pairs | 2 hours |
| P0 | Create fuzzy matching edge case tests | 2 hours |
| P1 | Create humanitarian context test scenarios | 1 hour |

### 3. CI Pipeline

| Priority | Task | Effort |
|----------|------|--------|
| P1 | Create `.github/workflows/ci.yml` | 1 hour |
| P1 | Configure lint + typecheck + test stages | 1 hour |
| P1 | Set up coverage threshold (80%) | 30 min |

---

## Quality Gate Criteria

### Pre-Implementation Gates

Before starting each epic:
- [ ] Unit test coverage target defined
- [ ] Integration test scenarios documented
- [ ] Mock data requirements identified

### Story Completion Gates

Each story is "done" when:
- [ ] Unit tests written and passing
- [ ] Integration tests written (if API/data changes)
- [ ] Coverage ≥80% for new code
- [ ] No regressions in existing tests

### Epic Completion Gates

Each epic is "done" when:
- [ ] All story tests passing
- [ ] End-to-end scenario passing
- [ ] Performance benchmarks met (if applicable)
- [ ] Golden test set passing (matching accuracy)

### Release Gates

Before Phase 1 release:
- [ ] 100% P0 tests passing
- [ ] ≥95% P1 tests passing
- [ ] Zero high-risk items unmitigated
- [ ] Zero false negatives in golden test set
- [ ] Performance requirements verified

---

## Summary

### Testability Assessment

| Criterion | Status | Score |
|-----------|--------|-------|
| Controllability | ✅ PASS | Good |
| Observability | ✅ PASS | Good |
| Reliability | ✅ PASS | Good |

### Risk Summary

| Risk Score | Count | Categories |
|------------|-------|------------|
| High (≥6) | 2 | Matching Accuracy (ASR-2), Data Integrity (ASR-4) |
| Medium (3-4) | 3 | Performance (ASR-1), Audit Trail (ASR-3), Humanitarian (ASR-5) |
| Low (1-2) | 0 | - |

### Test Effort Estimate

| Level | Tests | Effort |
|-------|-------|--------|
| Unit | ~60 | 20 hours |
| Integration | ~43 | 25 hours |
| E2E | ~11 | 10 hours |
| **Total** | ~114 | ~55 hours |

### Next Steps

1. **Create test infrastructure** during Epic 1, Story 1.1
2. **Define golden test set** before Epic 1, Story 1.8 (matcher)
3. **Set up CI pipeline** as part of Epic 1
4. **Run `test-design` again** per-epic during Phase 3 (Implementation)

---

**Test Design Status:** COMPLETE ✅
**Architecture Testability:** APPROVED ✅
**Implementation Readiness:** CONFIRMED ✅

