# Story 2.1: FastAPI Application Setup

Status: done

## Story

As a **developer**,
I want the FastAPI application skeleton running,
So that API endpoints can be added.

## Acceptance Criteria

```gherkin
Given I run `uvicorn ofac.api.main:app --reload`
When I access http://localhost:8000/health
Then I receive {"status": "healthy"}
And the response status is 200

When I access http://localhost:8000/docs
Then I see the auto-generated OpenAPI documentation
```

**✅ All acceptance criteria verified and passing**

## Tasks / Subtasks

- [x] Task 1: Create api/main.py with FastAPI app factory
  - [x] create_app() factory function
  - [x] app instance for uvicorn
  - [x] get_ofac_loader() helper function
- [x] Task 2: Add lifespan events for OFAC data loading
  - [x] @asynccontextmanager lifespan function
  - [x] Load OFAC data on startup
  - [x] Store in app.state for dependency injection
  - [x] Error handling (app still serves if data load fails)
- [x] Task 3: Add CORS middleware and basic configuration
  - [x] CORSMiddleware with configurable origins
  - [x] Added cors_origins to Settings (default: localhost:8501)
  - [x] Allow all methods and headers for development
- [x] Task 4: Create health endpoint
  - [x] GET /health returns {"status": "healthy"}
  - [x] GET /health/ready checks OFAC data loaded status
  - [x] Router registered with /health prefix
- [x] Task 5: Write integration tests (5 tests)
  - [x] Health endpoint test
  - [x] Readiness endpoint test
  - [x] OpenAPI docs test
  - [x] OpenAPI JSON test
  - [x] App metadata test
- [x] Task 6: Run review and commit

## FastAPI Application Structure

```python
from ofac.api.main import create_app, app

# App factory
app = create_app()

# Lifespan events:
# - Startup: Load OFAC data
# - Shutdown: Cleanup (if needed)

# Endpoints:
# - GET /health - Health check
# - GET /health/ready - Readiness check
# - GET /docs - OpenAPI documentation
# - GET /openapi.json - OpenAPI schema
```

## Dev Notes

### Lifespan Events
- OFAC data loads on application startup
- Stored in `app.state.ofac_data` and `app.state.ofac_loader`
- If load fails, app still serves (health endpoint works)
- Error stored in `app.state.ofac_load_error`

### CORS Configuration
- Default origins: `["http://localhost:8501", "http://127.0.0.1:8501"]`
- Configurable via `OFAC_CORS_ORIGINS` environment variable
- Allows all methods and headers for development

### References
- [Source: docs/architecture.md#API & Communication Patterns]
- [Source: docs/epics.md#Story 2.1]

## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created src/ofac/api/main.py with FastAPI app factory
- ✅ Lifespan events for OFAC data loading on startup
- ✅ CORS middleware configured
- ✅ Health and readiness endpoints
- ✅ OpenAPI documentation enabled
- ✅ 5 integration tests pass
- ✅ Total 216 tests pass (211 unit + 5 integration)
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓

### File List
**New Files:**
- src/ofac/api/main.py
- src/ofac/api/routes/health.py
- tests/integration/test_api_health.py

**Modified Files:**
- src/ofac/core/config.py (added cors_origins)
- src/ofac/api/routes/__init__.py (exports health router)
- docs/sprint-artifacts/sprint-status.yaml

## Change Log
- 2025-12-12: Story 2.1 implemented with full dev → review → commit cycle
