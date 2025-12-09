---
project_name: 'OFAC Screening Tool'
user_name: 'Carlos'
date: '2025-12-09'
epics_count: 6
stories_count: 41
fr_coverage: 79
status: 'complete'
---

# OFAC Screening Tool - Epic Breakdown

**Author:** Carlos
**Date:** 2025-12-09
**Project Level:** High Complexity (GovTech/Compliance)
**Target Scale:** 250-500 screenings/year, 3-5 grant rounds

---

## Overview

This document provides the complete epic and story breakdown for the OFAC Screening Tool, decomposing the requirements from the [PRD](./prd.md) into implementable stories with full technical context from [Architecture](./architecture.md) and [UX Design](./ux-design-specification.md).

### Epic Summary

| Epic | User Value | Stories | Key FRs |
|------|------------|---------|---------|
| 1. Foundation & Data Layer | Core matching engine works | 8 | FR1-4, FR13-16, FR20-22 |
| 2. Batch Screening Workflow | Upload Excel → Get results | 10 | FR2, FR5-12, FR50-52, FR61-67 |
| 3. Classification & Humanitarian | Smart OK/REVIEW/NOK classification | 6 | FR8, FR24-30 |
| 4. Audit-Ready Reporting | Board-ready Excel reports | 7 | FR31-42, FR72-74 |
| 5. OFAC Data Freshness | Keep data current | 5 | FR17-19, FR23, FR75-77 |
| 6. Exception Review Workflow | Review flagged cases | 5 | FR43-49, FR78-79 |

**Total:** 6 Epics, 41 Stories, 79 FRs covered

---

## Functional Requirements Inventory

### Organization Screening & Matching (FR1-FR12)
- **FR1:** Screen single organization against OFAC lists
- **FR2:** Screen multiple organizations in batch
- **FR3:** Detect exact name matches
- **FR4:** Detect fuzzy name matches with configurable thresholds
- **FR5:** Detect alias variations
- **FR6:** Incorporate country for score boost/de-boost
- **FR7:** Incorporate project description for humanitarian context
- **FR8:** Classify results as OK/REVIEW/NOK
- **FR9:** Provide confidence scores (percentage)
- **FR10:** Identify SDN vs Consolidated list source
- **FR11:** Screen 100 orgs in <5 minutes
- **FR12:** Screen single org in <2 seconds

### OFAC Data Management & Freshness (FR13-FR23)
- **FR13:** Download SDN list files (SDN.CSV, ALT.CSV, ADD.CSV)
- **FR14:** Download Consolidated list files
- **FR15:** Store OFAC data in local cache
- **FR16:** Track version/date of OFAC files
- **FR17:** Detect stale data (7/14/30 day thresholds)
- **FR18:** Check for updates without downloading
- **FR19:** Update OFAC data on user command
- **FR20:** Validate downloads before replacing (atomic swap)
- **FR21:** Rollback on failed update
- **FR22:** Prevent data corruption during updates
- **FR23:** Display freshness status to users

### Humanitarian Context Intelligence (FR24-FR30)
- **FR24:** Maintain sanctioned countries registry
- **FR25:** Detect organizations in sanctioned countries
- **FR26:** Detect humanitarian keywords
- **FR27:** Combine country + keywords for GL detection
- **FR28:** Map countries to General Licenses
- **FR29:** Flag humanitarian matches as REVIEW with GL notes
- **FR30:** Flag non-humanitarian sanctioned country as NOK

### Reporting & Audit Trail (FR31-FR42)
- **FR31:** Generate multi-sheet Excel reports
- **FR32:** Include summary statistics
- **FR33:** Include detailed results for all orgs
- **FR34:** Include exception-only view
- **FR35:** Include audit trail fields
- **FR36:** Provide analyst notes fields
- **FR37:** Meet 10-year retention requirements
- **FR38:** Embed OFAC version timestamps
- **FR39:** Color-code results
- **FR40:** Sort exceptions by risk level
- **FR41:** Display match transparency
- **FR42:** Provide downloadable Excel

### Exception Management (FR43-FR49)
- **FR43:** Display complete match details
- **FR44:** Classify risk levels
- **FR45:** Provide General License notes
- **FR46:** Support re-screening
- **FR47:** Display country alignment
- **FR48:** Preserve analyst notes
- **FR49:** Support version control

### API Service Layer (FR50-FR60)
- **FR50:** Batch screening endpoint (file upload)
- **FR51:** Single org screening endpoint (JSON)
- **FR52:** OFAC version check endpoint
- **FR53:** OFAC update trigger endpoint
- **FR54:** Auto-generate API docs
- **FR55:** Return structured JSON
- **FR56:** Return appropriate HTTP codes
- **FR57:** Validate request inputs
- **FR58:** Provide detailed error messages
- **FR59:** Handle multipart/form-data
- **FR60:** Handle JSON payloads

### User Interface (FR61-FR71)
- **FR61:** Accept Excel uploads (.xlsx)
- **FR62:** Accept CSV uploads
- **FR63:** Auto-detect column names
- **FR64:** Manual column mapping
- **FR65:** Progress indicators
- **FR66:** Drag-and-drop upload
- **FR67:** Color-coded results display
- **FR68:** Summary dashboard
- **FR69:** OFAC version display
- **FR70:** OFAC update controls
- **FR71:** One-click report download

### Traceability (FR72-FR79)
- **FR72:** Unique screening IDs
- **FR73:** Timestamp all operations
- **FR74:** Link results to OFAC version
- **FR75:** Track data age in days
- **FR76:** Maintain version history
- **FR77:** Enable spot-check validation
- **FR78:** Complete decision traceability
- **FR79:** Support audit validation

---

## Epic 1: Foundation & Data Layer

**Goal:** Establish the core infrastructure and matching engine that powers all screening operations.

**User Value:** The fundamental screening engine works with real OFAC data—a developer can run `python -m ofac` and match entities against current sanctions lists.

**FRs Covered:** FR1-FR4, FR13-FR16, FR20-FR22

---

### Story 1.1: Project Initialization

As a **developer**,
I want the project structure and dependencies set up,
So that I can start implementing features.

**Acceptance Criteria:**

```gherkin
Given I have Python 3.11+ and uv installed
When I clone the repository and run `uv venv && uv pip install -e ".[dev]"`
Then the virtual environment is created
And all dependencies are installed
And I can run `python -c "import ofac"` without errors
```

**Technical Implementation:**
- Create `pyproject.toml` per Architecture section "pyproject.toml Structure"
- Create `src/ofac/__init__.py` with `__version__ = "0.1.0"`
- Create `src/ofac/__main__.py` as entry point
- Create directory structure per Architecture "Project Structure"
- Configure Ruff in pyproject.toml (`line-length = 88`, `target-version = "py311"`)
- Configure mypy strict mode
- Create `.pre-commit-config.yaml`

**Prerequisites:** None (first story)

---

### Story 1.2: Configuration System

As a **developer**,
I want centralized configuration with environment variable support,
So that settings are consistent across all components.

**Acceptance Criteria:**

```gherkin
Given the application starts
When settings are loaded
Then all configuration values have sensible defaults
And environment variables prefixed with OFAC_ override defaults
And invalid configuration values raise ValidationError on startup

Given I set OFAC_MATCH_THRESHOLD_NOK=90
When the application loads configuration
Then settings.match_threshold_nok equals 90
```

**Technical Implementation:**
- Create `src/ofac/core/config.py` with Pydantic Settings v2 pattern
- Implement Settings class per Architecture "Configuration Schema"
- Fields: `match_threshold_nok` (95), `match_threshold_review` (80), `ofac_data_path`, `log_level`
- Use `model_config = ConfigDict(env_prefix="OFAC_", env_file=".env")`
- Create `.env.example` template
- Export singleton: `settings = Settings()`

**Prerequisites:** Story 1.1

---

### Story 1.3: Core Data Models

As a **developer**,
I want Pydantic models for all core data structures,
So that data validation is consistent throughout the application.

**Acceptance Criteria:**

```gherkin
Given I create an EntityInput with name="Test Org" and country="US"
When I access entity.entity_name
Then it returns "Test Org"

Given I create a ScreeningResult
When I serialize it to JSON
Then all fields use snake_case naming
And the model validates all required fields
```

**Technical Implementation:**
- Create `src/ofac/core/models.py`
- Define `EntityInput(BaseModel)`: entity_name (str), country (str | None), description (str | None)
- Define `MatchResult(BaseModel)`: sdn_name, sdn_type, match_score, match_type, ofac_list, programs
- Define `ScreeningResult(BaseModel)`: entity_input, match_status (OK|REVIEW|NOK), matches list, screening_id, timestamp
- All models use `model_config = ConfigDict(populate_by_name=True)`
- Add validators for score ranges (0-100)

**Prerequisites:** Story 1.2

---

### Story 1.4: Custom Exception Hierarchy

As a **developer**,
I want a structured exception hierarchy,
So that errors are handled consistently across the application.

**Acceptance Criteria:**

```gherkin
Given an OFACDataError is raised
When it is caught in an API route
Then it has a code attribute for structured error responses
And the error message is human-readable

Given I import from ofac.core.exceptions
When I use FileValidationError
Then it inherits from OFACError
And has code = "FILE_VALIDATION_ERROR"
```

**Technical Implementation:**
- Create `src/ofac/core/exceptions.py`
- Define base `OFACError(Exception)` with `code: str` attribute
- Define `FileValidationError(OFACError)` with code "FILE_*"
- Define `OFACDataError(OFACError)` with code "OFAC_*"
- Define `ScreeningError(OFACError)` with code "SCREEN_*"
- Pattern per Architecture "Error Handling Pattern"

**Prerequisites:** Story 1.1

---

### Story 1.5: OFAC Data Schemas

As a **developer**,
I want Pydantic models representing OFAC data structures,
So that CSV parsing is validated and typed.

**Acceptance Criteria:**

```gherkin
Given I parse a row from SDN.CSV
When I create an SDNEntry from the row data
Then all OFAC fields are properly typed
And ent_num is an integer
And sdn_name is a string

Given I have SDN, Alt, and Address entries
When I link them by ent_num
Then I can retrieve all aliases for an entity
And I can retrieve all addresses for an entity
```

**Technical Implementation:**
- Create `src/ofac/data/schemas.py`
- Define `SDNEntry(BaseModel)`: ent_num, sdn_name, sdn_type, programs, remarks, etc.
- Define `AltEntry(BaseModel)`: ent_num, alt_num, alt_name, alt_type
- Define `AddressEntry(BaseModel)`: ent_num, add_num, address, city, country, etc.
- Field names match OFAC CSV column headers
- Use Optional[] for nullable fields

**Prerequisites:** Story 1.3

---

### Story 1.6: OFAC Data Loader

As a **developer**,
I want to load OFAC CSV triplets into memory,
So that the matching engine can query them efficiently.

**Acceptance Criteria:**

```gherkin
Given valid OFAC CSV files exist at the configured path
When I call OFACDataLoader().load()
Then a DataFrame is returned with all SDN entries
And aliases are merged by ent_num
And the load completes in under 3 seconds

Given OFAC files don't exist
When I call OFACDataLoader().load()
Then OFACDataError is raised with code "OFAC_DATA_NOT_FOUND"
```

**Technical Implementation:**
- Create `src/ofac/data/loader.py`
- Implement `OFACDataLoader` class
- Method `load() -> pd.DataFrame` that reads CSV triplets
- Merge SDN.CSV + ALT.CSV + ADD.CSV by ent_num
- Handle encoding issues (UTF-8 with Latin-1 fallback)
- Cache loaded data in class instance
- Validate expected columns exist per FR20

**Prerequisites:** Story 1.5, Story 1.2 (for data path config)

**Architecture Reference:** "Data Architecture" - Eager Load, Pandas DataFrame

---

### Story 1.7: OFAC Data Downloader

As a **developer**,
I want to download OFAC files from Treasury.gov,
So that the local cache can be populated and updated.

**Acceptance Criteria:**

```gherkin
Given I call OFACUpdater().download_sdn_files()
When the download completes successfully
Then SDN.CSV, ALT.CSV, ADD.CSV are saved to a temp directory
And a version.json with download timestamp is created

Given a download fails mid-way
When the error is caught
Then existing cached files are not corrupted
And OFACDataError is raised with details
```

**Technical Implementation:**
- Create `src/ofac/data/updater.py`
- Implement `OFACUpdater` class
- Download URLs: `https://www.treasury.gov/ofac/downloads/sdn.csv`, etc.
- Use httpx for async downloads
- Implement atomic swap: download to temp → validate → move to cache
- Create `version.json` with `download_date`, `last_modified` (from HTTP header)
- Per FR20, FR21, FR22

**Prerequisites:** Story 1.6, Story 1.2

---

### Story 1.8: Basic Matching Engine

As a **developer**,
I want fuzzy string matching against OFAC entities,
So that I can identify potential sanctions matches.

**Acceptance Criteria:**

```gherkin
Given OFAC data is loaded
When I call matcher.match("ACME Corporation")
Then a list of MatchResult is returned
And each result has a match_score (0-100)
And results are sorted by score descending

Given I match "Archdiocèse de Bangui" against "Archdiocese of Bangui"
When using token_sort_ratio algorithm
Then the match score is >= 85

Given I match an entity with no close matches
When the highest score is < 80
Then an empty list is returned (or list with low scores)
```

**Technical Implementation:**
- Create `src/ofac/core/matcher.py`
- Implement `EntityMatcher` class
- Use `rapidfuzz.fuzz.token_sort_ratio` as primary algorithm
- Match against sdn_name AND alt_name columns
- Return top N matches above minimum threshold (configurable)
- Per FR1, FR3, FR4, FR5, FR9

**Prerequisites:** Story 1.6, Story 1.3

**Architecture Reference:** "RapidFuzz Matching Rules" in project_context.md

---

## Epic 1 Complete

**Stories:** 8
**FRs Covered:** FR1, FR3, FR4, FR5, FR9, FR13, FR14, FR15, FR16, FR20, FR21, FR22

**Technical Context Used:**
- Architecture: Project Structure, Configuration Schema, Data Architecture
- Project Context: Pydantic v2 patterns, import conventions

**Foundation Deliverables:**
- ✅ Project structure with all directories
- ✅ Configuration system (Pydantic Settings)
- ✅ Core data models
- ✅ Exception hierarchy
- ✅ OFAC data loading and caching
- ✅ Basic fuzzy matching engine

---

## Epic 2: Batch Screening Workflow

**Goal:** Enable the core user journey: upload a file of organizations, screen them against OFAC, and view results.

**User Value:** Carlos can upload his grant beneficiary Excel file and see which organizations are OK, need REVIEW, or are blocked (NOK)—the primary workflow that saves 6+ hours per grant round.

**FRs Covered:** FR2, FR5-12, FR50-52, FR61-67

**Dependencies:** Epic 1 (matching engine working)

---

### Story 2.1: FastAPI Application Setup

As a **developer**,
I want the FastAPI application skeleton running,
So that API endpoints can be added.

**Acceptance Criteria:**

```gherkin
Given I run `uvicorn ofac.api.main:app --reload`
When I access http://localhost:8000/health
Then I receive {"status": "healthy"}
And the response status is 200

When I access http://localhost:8000/docs
Then I see the auto-generated OpenAPI documentation
```

**Technical Implementation:**
- Create `src/ofac/api/main.py` with FastAPI app factory
- Create `src/ofac/api/routes/health.py` with health endpoint
- Use lifespan context manager to load OFAC data on startup
- Register routers from routes/ directory
- Configure CORS for local development

**Prerequisites:** Epic 1 complete

---

### Story 2.2: Single Entity Screening Endpoint

As a **developer**,
I want an API endpoint to screen a single entity,
So that quick ad-hoc checks are possible.

**Acceptance Criteria:**

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

**Technical Implementation:**
- Create `src/ofac/api/routes/screening.py`
- Create `src/ofac/api/schemas.py` with request/response models
- Implement `POST /screenings/single` endpoint
- Request body: `SingleScreeningRequest(entity_name, country?, description?)`
- Response: `{"data": {...}, "meta": {"ofac_version": ..., "duration_ms": ...}}`
- Per FR51, FR55, FR56

**Prerequisites:** Story 2.1

---

### Story 2.3: Batch Screening Endpoint

As a **developer**,
I want an API endpoint that accepts file uploads for batch screening,
So that multiple organizations can be screened at once.

**Acceptance Criteria:**

```gherkin
Given I have an Excel file with organization names
When I POST to /screenings/batch with the file
Then screening runs for all rows
And I receive results for each organization
And screening_id is the same for all results in batch

Given I upload a file larger than max size
When the request is processed
Then I receive status 413
And the error message indicates file too large
```

**Technical Implementation:**
- Extend `src/ofac/api/routes/screening.py`
- Implement `POST /screenings/batch` endpoint
- Accept `multipart/form-data` with UploadFile
- Parse Excel/CSV using pandas (openpyxl for xlsx)
- Process each row through matching engine
- Generate unique screening_id (UUID) for batch
- Per FR50, FR57, FR59

**Prerequisites:** Story 2.2

---

### Story 2.4: File Parsing & Column Detection

As a **developer**,
I want to parse uploaded files and detect relevant columns,
So that organization names are correctly extracted.

**Acceptance Criteria:**

```gherkin
Given an Excel file with column "Organization Name"
When it's parsed
Then the column is auto-detected as the entity name column
And a mapping suggestion is returned

Given a file with non-standard column names
When auto-detection fails
Then column names are returned for manual selection
And no error is raised
```

**Technical Implementation:**
- Create file parsing utility in `src/ofac/core/file_parser.py`
- Support .xlsx (openpyxl) and .csv (pandas)
- Auto-detect columns by common patterns: "name", "organization", "entity", "partner"
- Also detect "country", "project", "description" columns
- Return `ColumnMapping` with detected or suggested mappings
- Per FR61, FR62, FR63, FR64

**Prerequisites:** Story 2.3

---

### Story 2.5: Streamlit App Shell

As a **developer**,
I want the basic Streamlit application running,
So that the UI can be developed.

**Acceptance Criteria:**

```gherkin
Given I run `streamlit run src/ofac/streamlit/app.py`
When I access http://localhost:8501
Then I see the OFAC Screening Tool landing page
And the OFAC data version is displayed in the header
And the page has professional styling

Given the app starts
When session state is initialized
Then workflow_step is "upload"
And other state variables are initialized
```

**Technical Implementation:**
- Create `src/ofac/streamlit/app.py` as main entry
- Create `src/ofac/streamlit/state.py` for session state management
- Create `src/ofac/streamlit/styles.py` with CSS injection
- Initialize session state per Architecture "Session State Schema"
- Display app title and OFAC version
- Per FR68, FR69

**UX Reference:** "Calm Professional" design direction, "Sage Forest" color palette

**Prerequisites:** Story 2.1 (API running for OFAC version)

---

### Story 2.6: File Upload Component

As a **compliance officer (Carlos)**,
I want to upload my Excel file via drag-and-drop,
So that I can start the screening process easily.

**Acceptance Criteria:**

```gherkin
Given I am on the upload step
When I drag an Excel file onto the upload area
Then the file is accepted
And I see a preview of the first few rows
And file name and size are displayed

Given I upload a PDF file
When validation runs
Then I see an error message "Unsupported file format"
And the workflow does not advance
```

**Technical Implementation:**
- Create `src/ofac/streamlit/components/upload.py`
- Use `st.file_uploader` with accept=[".xlsx", ".csv"]
- Display file metadata after upload
- Show data preview with `st.dataframe` (first 5 rows)
- Validate file format and size (<10MB)
- Per FR61, FR62, FR66

**UX Reference:** Upload step in user flow, file feedback patterns

**Prerequisites:** Story 2.5

---

### Story 2.7: Column Mapping Component

As a **compliance officer**,
I want to confirm or correct column mappings,
So that the right data is used for screening.

**Acceptance Criteria:**

```gherkin
Given a file is uploaded
When column detection suggests "Organization Name" for entity
Then I see the suggestion highlighted
And I can confirm or change it via dropdown

Given I select columns and click "Confirm Mapping"
When validation passes
Then workflow advances to screening step
And column mapping is stored in session state
```

**Technical Implementation:**
- Create `src/ofac/streamlit/components/mapping.py`
- Display column suggestions with confidence indicators
- Use `st.selectbox` for each mapping (name, country, description)
- Mark required (name) vs optional (country, description) fields
- Store mapping in `st.session_state.column_mapping`
- Per FR63, FR64

**Prerequisites:** Story 2.6, Story 2.4 (auto-detection)

---

### Story 2.8: Screening Execution with Progress

As a **compliance officer**,
I want to see progress while screening runs,
So that I know the system is working.

**Acceptance Criteria:**

```gherkin
Given I have confirmed column mapping
When I click "Start Screening"
Then a progress bar appears
And it updates as entities are processed
And processing time is displayed

Given screening is running
When an entity is processed
Then the progress percentage updates
And estimated time remaining is shown (optional)
```

**Technical Implementation:**
- Implement screening orchestration in `src/ofac/streamlit/app.py`
- Call API endpoint with file data
- Use `st.progress()` and `st.spinner()` for feedback
- Update progress as results stream in (or poll)
- Store results in `st.session_state.screening_results`
- Per FR2, FR11, FR65

**Prerequisites:** Story 2.7, Story 2.3 (batch endpoint)

---

### Story 2.9: Results Display Component

As a **compliance officer**,
I want to see screening results with clear status indicators,
So that I can quickly identify issues.

**Acceptance Criteria:**

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

**Technical Implementation:**
- Create `src/ofac/streamlit/components/results.py`
- Display results with `st.dataframe` or custom component
- Apply status CSS classes (.status-ok, .status-review, .status-nok)
- Add filter controls for status
- Show summary counts above table
- Per FR67, FR39, FR8

**UX Reference:** Status indicator patterns, data table design

**Prerequisites:** Story 2.8

---

### Story 2.10: Summary Dashboard

As a **compliance officer**,
I want to see summary statistics,
So that I have an overview of screening results.

**Acceptance Criteria:**

```gherkin
Given screening is complete
When I view the summary
Then I see total screened count
And I see OK/REVIEW/NOK counts with percentages
And I see OFAC data version used
And I see screening timestamp

Given 5 out of 100 orgs are flagged
When summary is displayed
Then I see "5 exceptions require review (5%)"
```

**Technical Implementation:**
- Create `src/ofac/streamlit/components/summary.py`
- Use `st.metric` for key statistics
- Consider `streamlit_extras.metric_cards` for enhanced display
- Calculate percentages for each status
- Display screening metadata (ID, timestamp, OFAC version)
- Per FR32, FR68

**Prerequisites:** Story 2.9

---

## Epic 2 Complete

**Stories:** 10
**FRs Covered:** FR2, FR5, FR6, FR7, FR8, FR10, FR11, FR50, FR51, FR55, FR56, FR57, FR59, FR61, FR62, FR63, FR64, FR65, FR66, FR67, FR68

**Deliverables:**
- ✅ FastAPI running with screening endpoints
- ✅ Streamlit app with complete upload → screen → results flow
- ✅ File parsing with column detection
- ✅ Progress feedback during screening
- ✅ Results display with status badges
- ✅ Summary dashboard

---

## Epic 3: Classification & Humanitarian Intelligence

**Goal:** Implement smart classification that understands humanitarian context and General Licenses.

**User Value:** Carlos gets intelligent classification that doesn't automatically block humanitarian operations in sanctioned countries—the nuance that generic tools miss.

**FRs Covered:** FR8, FR24-FR30

**Dependencies:** Epic 2 (screening workflow working)

---

### Story 3.1: OK/REVIEW/NOK Classification Logic

As a **developer**,
I want threshold-based classification,
So that match scores are converted to actionable statuses.

**Acceptance Criteria:**

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

**Technical Implementation:**
- Create `src/ofac/core/classifier.py`
- Implement `ScreeningClassifier` class
- Use thresholds from `settings.match_threshold_nok` (95) and `settings.match_threshold_review` (80)
- Method `classify(score: int) -> Literal["OK", "REVIEW", "NOK"]`
- Per FR8

**Prerequisites:** Story 1.8 (matcher returns scores)

---

### Story 3.2: Sanctioned Countries Registry

As a **developer**,
I want a maintained list of OFAC-sanctioned countries,
So that country-based detection works correctly.

**Acceptance Criteria:**

```gherkin
Given I query is_sanctioned_country("SY")
When the check runs
Then True is returned (Syria is sanctioned)

Given I query is_sanctioned_country("US")
When the check runs
Then False is returned

Given I query get_general_license("SY")
When lookup runs
Then "GL-21" is returned with description
```

**Technical Implementation:**
- Add sanctioned countries data to `src/ofac/core/classifier.py` or separate file
- Countries: Syria (SY), Iran (IR), Cuba (CU), North Korea (KP), Venezuela (VE), etc.
- Map to General Licenses: SY→GL-21, IR→GL D-1, VE→GL-41
- Use ISO country codes
- Per FR24, FR28

**Prerequisites:** Story 3.1

---

### Story 3.3: Country-Aware Score Boosting

As a **developer**,
I want to boost scores when entity country matches OFAC entry country,
So that geographic alignment increases match confidence.

**Acceptance Criteria:**

```gherkin
Given an entity from Syria matching an OFAC entry in Syria
When scoring runs
Then the score is boosted by 10 points

Given an entity from France matching an OFAC entry in Syria
When scoring runs
Then the score is NOT boosted

Given a boosted score exceeds 100
When normalization runs
Then the score is capped at 100
```

**Technical Implementation:**
- Extend `EntityMatcher` in `src/ofac/core/matcher.py`
- Extract country from OFAC address data
- Compare input entity country with OFAC entry country
- Apply configurable boost (default +10 points)
- Cap at 100
- Per FR6

**Prerequisites:** Story 3.2, Story 1.6 (address data loaded)

---

### Story 3.4: Humanitarian Keyword Detection

As a **developer**,
I want to detect humanitarian context in project descriptions,
So that humanitarian aid operations are handled appropriately.

**Acceptance Criteria:**

```gherkin
Given a project description "Emergency medical supplies for Syria"
When humanitarian detection runs
Then is_humanitarian returns True
And detected_keywords includes ["emergency", "medical"]

Given a description "Banking services in Damascus"
When humanitarian detection runs
Then is_humanitarian returns False
```

**Technical Implementation:**
- Add humanitarian detection to `src/ofac/core/classifier.py`
- Keyword list: "humanitarian", "aid", "relief", "medical", "emergency", "food", "water", "shelter", "assistance", "refugee"
- Case-insensitive matching
- Return detected keywords for transparency
- Per FR26

**Prerequisites:** Story 3.1

---

### Story 3.5: General License Flagging

As a **developer**,
I want matches with humanitarian context flagged for GL review,
So that legitimate aid operations aren't automatically blocked.

**Acceptance Criteria:**

```gherkin
Given a match in Syria with humanitarian keywords
When classification runs
Then status is REVIEW (not NOK)
And general_license is "GL-21"
And notes include "Potential Syria Humanitarian License applicability"

Given a match in Syria WITHOUT humanitarian keywords
When classification runs
Then status is NOK
And general_license is null
```

**Technical Implementation:**
- Extend `ScreeningClassifier` with GL detection logic
- Combine: sanctioned_country + humanitarian_keywords → REVIEW with GL
- Combine: sanctioned_country + NO humanitarian_keywords → NOK
- Add `general_license` and `humanitarian_context` fields to `ScreeningResult`
- Per FR27, FR29, FR30

**Prerequisites:** Story 3.3, Story 3.4

---

### Story 3.6: Country Alignment Display

As a **compliance officer**,
I want to see country alignment in match details,
So that I understand geographic context of matches.

**Acceptance Criteria:**

```gherkin
Given a match result
When I view details
Then I see country alignment: "Match" / "Mismatch" / "N/A"
And the input country is displayed
And the OFAC entry country is displayed

Given country data is missing
When alignment is calculated
Then "N/A" is displayed gracefully
```

**Technical Implementation:**
- Add country alignment to `MatchResult` model
- Enum: `CountryAlignment(Enum)` with MATCH, MISMATCH, NOT_AVAILABLE
- Display in results table and match details
- Per FR47

**Prerequisites:** Story 3.3

---

## Epic 3 Complete

**Stories:** 6
**FRs Covered:** FR8, FR24, FR25, FR26, FR27, FR28, FR29, FR30, FR6, FR47

**Deliverables:**
- ✅ Threshold-based OK/REVIEW/NOK classification
- ✅ Sanctioned countries registry with GL mapping
- ✅ Country-aware score boosting
- ✅ Humanitarian keyword detection
- ✅ General License flagging for humanitarian context
- ✅ Country alignment display

---

## Epic 4: Audit-Ready Reporting

**Goal:** Generate Excel reports that pass board and auditor review without modification.

**User Value:** Carlos downloads a professional, multi-sheet Excel report that he can present to the board and archive for the required 10 years—zero manual cleanup needed.

**FRs Covered:** FR31-FR42, FR72-FR74

**Dependencies:** Epic 3 (classification complete)

---

### Story 4.1: Report Generator Service

As a **developer**,
I want a report generation service,
So that screening results can be exported to Excel.

**Acceptance Criteria:**

```gherkin
Given I have screening results
When I call ReportGenerator.generate(results)
Then an Excel workbook is created in memory
And it has multiple sheets
And it can be saved to file or returned as bytes

Given results contain 100 organizations
When the report generates
Then generation completes in under 10 seconds
```

**Technical Implementation:**
- Create `src/ofac/core/reporter.py`
- Implement `ReportGenerator` class
- Use openpyxl for Excel generation
- Return `io.BytesIO` for streaming downloads
- Per FR31, FR42

**Prerequisites:** Epic 3 complete (full screening results)

---

### Story 4.2: Summary Sheet

As a **compliance officer**,
I want a summary sheet with key statistics,
So that I can present high-level results to the board.

**Acceptance Criteria:**

```gherkin
Given a report is generated
When I open the Summary sheet
Then I see screening date and time
And I see OFAC data version used
And I see total screened count
And I see OK/REVIEW/NOK breakdown with counts and percentages
And I see screening ID for traceability
```

**Technical Implementation:**
- Add "Summary" sheet to report workbook
- Include: screening_id, timestamp, ofac_version, entity_count, status_breakdown
- Format as professional table
- Per FR32, FR38, FR72, FR73, FR74

**Prerequisites:** Story 4.1

---

### Story 4.3: Detailed Results Sheet

As a **compliance officer**,
I want all results in a detailed sheet,
So that I have complete documentation.

**Acceptance Criteria:**

```gherkin
Given a report is generated
When I open the Details sheet
Then I see one row per screened organization
And columns include: organization name, status, match score, matched entity, country alignment
And rows are sorted by status (NOK first, then REVIEW, then OK)
```

**Technical Implementation:**
- Add "All Results" sheet to report
- Columns: Row#, Organization, Country, Status, Match Score, Matched SDN, Match Type, Country Alignment
- Sort by status severity
- Per FR33, FR41

**Prerequisites:** Story 4.2

---

### Story 4.4: Exceptions Sheet

As a **compliance officer**,
I want an exceptions-only sheet,
So that I can focus on cases requiring review.

**Acceptance Criteria:**

```gherkin
Given a report with 100 results including 5 REVIEW and 2 NOK
When I open the Exceptions sheet
Then I see only 7 rows (REVIEW + NOK cases)
And they are sorted by risk level (NOK first)
And each has complete match details
```

**Technical Implementation:**
- Add "Exceptions" sheet to report
- Filter to only REVIEW and NOK statuses
- Include all match details: score, SDN name, entity ID, programs
- Sort by status then score descending
- Per FR34, FR40, FR43

**Prerequisites:** Story 4.3

---

### Story 4.5: Color Coding & Formatting

As a **compliance officer**,
I want color-coded results,
So that I can visually scan for issues.

**Acceptance Criteria:**

```gherkin
Given I open the Details sheet
When I look at the Status column
Then OK cells have green background
And REVIEW cells have yellow background
And NOK cells have red background

Given the report is printed
When color-blind users view it
Then text labels are readable independent of color
```

**Technical Implementation:**
- Apply cell fills using openpyxl styles
- Colors per UX spec: OK=#C6F6D5, REVIEW=#FEFCBF, NOK=#FED7D7
- Also bold NOK text for accessibility
- Apply consistent font and sizing
- Per FR39

**Prerequisites:** Story 4.4

---

### Story 4.6: Audit Trail Fields

As a **compliance officer**,
I want complete audit trail fields,
So that the report meets 10-year retention requirements.

**Acceptance Criteria:**

```gherkin
Given a report is generated
When I review audit fields
Then I see screening_id, timestamp, ofac_version
And I see OFAC entity IDs for each match
And I see OFAC program names
And I see General License notes where applicable
```

**Technical Implementation:**
- Add audit columns: Screening ID, Timestamp, OFAC Version, SDN Entity ID, Programs, GL Notes
- Include in both Details and Exceptions sheets
- Per FR35, FR37, FR38, FR72, FR74

**Prerequisites:** Story 4.5

---

### Story 4.7: One-Click Download

As a **compliance officer**,
I want to download the report with one click,
So that exporting is effortless.

**Acceptance Criteria:**

```gherkin
Given I am viewing screening results
When I click "Download Report"
Then an Excel file downloads immediately
And the filename includes date (screening-2025-12-09.xlsx)
And no additional dialog or configuration is needed
```

**Technical Implementation:**
- Create `src/ofac/streamlit/components/export.py`
- Use `st.download_button` with report bytes
- Generate filename with date
- Call ReportGenerator to create report
- Per FR42, FR71

**Prerequisites:** Story 4.6, Story 2.9 (results view)

---

## Epic 4 Complete

**Stories:** 7
**FRs Covered:** FR31, FR32, FR33, FR34, FR35, FR37, FR38, FR39, FR40, FR41, FR42, FR43, FR72, FR73, FR74, FR71

**Deliverables:**
- ✅ Report generator service
- ✅ Summary sheet with statistics
- ✅ Detailed results sheet
- ✅ Exceptions-only sheet
- ✅ Color coding (green/yellow/red)
- ✅ Complete audit trail fields
- ✅ One-click download

---

## Epic 5: OFAC Data Freshness & Updates

**Goal:** Keep OFAC data current and inform users about data age.

**User Value:** Carlos knows exactly how old his OFAC data is and can update it when needed—critical for audit defensibility.

**FRs Covered:** FR17-FR19, FR23, FR75-FR77

**Dependencies:** Epic 1 (data layer)

---

### Story 5.1: Freshness Status Calculation

As a **developer**,
I want to calculate OFAC data freshness,
So that staleness can be detected and displayed.

**Acceptance Criteria:**

```gherkin
Given OFAC data was last updated 5 days ago
When freshness is calculated
Then status is "CURRENT" (green)

Given OFAC data is 10 days old
When freshness is calculated
Then status is "STALE" (yellow warning)

Given OFAC data is 30+ days old
When freshness is calculated
Then status is "CRITICAL" (red)
```

**Technical Implementation:**
- Add freshness calculation to `src/ofac/data/loader.py` or new `status.py`
- Read `version.json` for last update date
- Thresholds: <7 days = CURRENT, 7-14 = STALE, >14 = CRITICAL
- Return `FreshnessStatus` enum with age_days
- Per FR17, FR75

**Prerequisites:** Story 1.7 (version.json created)

---

### Story 5.2: OFAC Status API Endpoint

As a **developer**,
I want an API endpoint for OFAC data status,
So that clients can query data freshness.

**Acceptance Criteria:**

```gherkin
Given I call GET /data/status
When the request succeeds
Then I receive current OFAC version info
And response includes age_days
And response includes freshness_status
```

**Technical Implementation:**
- Create `src/ofac/api/routes/data.py`
- Implement `GET /data/status` endpoint
- Return: version, last_updated, age_days, freshness_status, record_count
- Per FR52

**Prerequisites:** Story 5.1, Story 2.1

---

### Story 5.3: Freshness Display in UI

As a **compliance officer**,
I want to see OFAC data freshness at a glance,
So that I know if my data is current.

**Acceptance Criteria:**

```gherkin
Given I open the Streamlit app
When the header loads
Then I see "OFAC Data: Current (2 days old)" in green
OR I see "OFAC Data: Stale (10 days old)" in yellow
OR I see "OFAC Data: Critical (32 days old)" in red

Given data is stale
When I hover over the indicator
Then I see "Last updated: 2025-11-29"
```

**Technical Implementation:**
- Add freshness indicator to app header in `app.py`
- Use colored badge per status
- Fetch from /data/status on app load
- Per FR23, FR69

**Prerequisites:** Story 5.2, Story 2.5

---

### Story 5.4: Manual Update Trigger

As a **compliance officer**,
I want to update OFAC data on demand,
So that I can ensure freshness before screening.

**Acceptance Criteria:**

```gherkin
Given I click "Update OFAC Data"
When the update runs
Then I see a progress indicator
And I see "Downloading..." then "Validating..." then "Complete"
And the freshness indicator updates

Given an update fails
When the error is handled
Then I see an error message
And existing data is preserved
```

**Technical Implementation:**
- Add update button in Streamlit header or sidebar
- Call `POST /data/refresh` endpoint
- Show progress with `st.spinner`
- Handle success/failure feedback
- Per FR19, FR70

**Prerequisites:** Story 5.3, Story 1.7 (downloader)

---

### Story 5.5: Update Trigger API

As a **developer**,
I want an API endpoint to trigger OFAC updates,
So that clients can initiate updates.

**Acceptance Criteria:**

```gherkin
Given I call POST /data/refresh
When the update succeeds
Then I receive new version info
And status 200 is returned

Given an update fails
When the error is caught
Then status 503 is returned
And error message is included
And existing data is not corrupted
```

**Technical Implementation:**
- Implement `POST /data/refresh` in `src/ofac/api/routes/data.py`
- Call OFACUpdater.download_and_update()
- Return new version info on success
- Per FR53

**Prerequisites:** Story 5.2, Story 1.7

---

## Epic 5 Complete

**Stories:** 5
**FRs Covered:** FR17, FR18, FR19, FR23, FR52, FR53, FR69, FR70, FR75

**Deliverables:**
- ✅ Freshness calculation with thresholds
- ✅ OFAC status API endpoint
- ✅ Visual freshness indicator in UI
- ✅ Manual update button
- ✅ Update trigger API

---

## Epic 6: Exception Review Workflow

**Goal:** Enable efficient review and resolution of flagged cases.

**User Value:** Carlos can drill into REVIEW and NOK cases, see complete match details, add analyst notes, and re-screen if needed—the workflow for resolving exceptions before finalizing reports.

**FRs Covered:** FR43-FR49, FR78-FR79

**Dependencies:** Epic 4 (reporting complete)

---

### Story 6.1: Match Details Expansion

As a **compliance officer**,
I want to expand match details for flagged cases,
So that I can understand why a match occurred.

**Acceptance Criteria:**

```gherkin
Given I see a REVIEW or NOK result
When I click to expand details
Then I see: matched SDN name, SDN type, match score, match algorithm, country alignment
And I see OFAC entity ID and programs
And I see General License notes if applicable
```

**Technical Implementation:**
- Use `st.expander` in results component
- Display all fields from MatchResult
- Format for readability
- Per FR43, FR41, FR45

**Prerequisites:** Story 2.9

---

### Story 6.2: Risk Level Classification

As a **compliance officer**,
I want to see risk levels for matches,
So that I can prioritize review.

**Acceptance Criteria:**

```gherkin
Given a NOK match with score 98%
When risk level is calculated
Then risk is "High"

Given a REVIEW match with score 82%
When risk level is calculated
Then risk is "Medium"

Given a REVIEW match with score 80% and humanitarian context
When risk level is calculated
Then risk is "Low"
```

**Technical Implementation:**
- Add risk level calculation to `classifier.py`
- Enum: `RiskLevel(Enum)` with HIGH, MEDIUM, LOW
- Rules: NOK = High, REVIEW >90 = Medium, REVIEW with GL = Low, REVIEW else = Medium
- Per FR44

**Prerequisites:** Story 6.1

---

### Story 6.3: Analyst Notes Field

As a **compliance officer**,
I want to add notes to screening results,
So that I can document my review decisions.

**Acceptance Criteria:**

```gherkin
Given I am viewing an exception case
When I enter notes in the text area
Then the notes are saved to session state
And notes appear in the downloaded report

Given I add notes "Verified - legitimate organization"
When I download the report
Then the notes column shows my text for that row
```

**Technical Implementation:**
- Add `st.text_area` for notes in expanded match details
- Store notes in session state keyed by entity name
- Include notes in report generation
- Per FR36, FR48

**Prerequisites:** Story 6.1

---

### Story 6.4: Single Entity Re-Screening

As a **compliance officer**,
I want to re-screen a single entity,
So that I can check for changes after OFAC updates.

**Acceptance Criteria:**

```gherkin
Given I am viewing an exception case
When I click "Re-Screen This Entity"
Then a new screening runs for just that entity
And results update in place
And I see whether status changed

Given OFAC data was updated
When I re-screen an entity
Then results reflect the new data
```

**Technical Implementation:**
- Add re-screen button in expanded details
- Call single screening API
- Update result in session state
- Show before/after comparison
- Per FR46

**Prerequisites:** Story 6.3, Story 2.2

---

### Story 6.5: Decision Traceability

As a **compliance officer**,
I want complete traceability for all decisions,
So that auditors can verify my review process.

**Acceptance Criteria:**

```gherkin
Given I review and document an exception
When the report is generated
Then it includes screening_id linking to original batch
And it includes analyst notes with timestamp
And it includes OFAC data version used
And the audit trail is complete for 10-year retention
```

**Technical Implementation:**
- Ensure all traceability fields flow through to report
- Add note_timestamp when analyst notes are added
- Include reviewer identification (if available)
- Per FR78, FR79, FR37

**Prerequisites:** Story 6.4, Story 4.6

---

## Epic 6 Complete

**Stories:** 5
**FRs Covered:** FR43, FR44, FR45, FR46, FR48, FR78, FR79, FR36, FR41

**Deliverables:**
- ✅ Expandable match details
- ✅ Risk level classification
- ✅ Analyst notes field
- ✅ Single entity re-screening
- ✅ Complete decision traceability

---

## FR Coverage Matrix

| FR | Description | Epic | Story |
|----|-------------|------|-------|
| FR1 | Screen single org | 1 | 1.8 |
| FR2 | Screen batch | 2 | 2.3, 2.8 |
| FR3 | Exact matches | 1 | 1.8 |
| FR4 | Fuzzy matches | 1 | 1.8 |
| FR5 | Alias detection | 1, 2 | 1.8, 2.8 |
| FR6 | Country boost | 3 | 3.3 |
| FR7 | Project description | 3 | 3.4 |
| FR8 | OK/REVIEW/NOK | 3 | 3.1 |
| FR9 | Confidence scores | 1 | 1.8 |
| FR10 | SDN vs Consolidated | 2 | 2.8 |
| FR11 | 100 orgs in 5 min | 2 | 2.8 |
| FR12 | Single in 2 sec | 2 | 2.2 |
| FR13 | Download SDN | 1 | 1.7 |
| FR14 | Download Consolidated | 1 | 1.7 |
| FR15 | Local cache | 1 | 1.6 |
| FR16 | Version tracking | 1 | 1.7 |
| FR17 | Detect stale | 5 | 5.1 |
| FR18 | Check for updates | 5 | 5.2 |
| FR19 | Update on command | 5 | 5.4 |
| FR20 | Validate before replace | 1 | 1.7 |
| FR21 | Rollback on failure | 1 | 1.7 |
| FR22 | Prevent corruption | 1 | 1.7 |
| FR23 | Display freshness | 5 | 5.3 |
| FR24 | Sanctioned countries | 3 | 3.2 |
| FR25 | Detect sanctioned country | 3 | 3.2 |
| FR26 | Humanitarian keywords | 3 | 3.4 |
| FR27 | GL detection | 3 | 3.5 |
| FR28 | GL mapping | 3 | 3.2 |
| FR29 | Humanitarian = REVIEW | 3 | 3.5 |
| FR30 | Non-humanitarian = NOK | 3 | 3.5 |
| FR31 | Multi-sheet Excel | 4 | 4.1 |
| FR32 | Summary stats | 4 | 4.2 |
| FR33 | Detailed results | 4 | 4.3 |
| FR34 | Exception view | 4 | 4.4 |
| FR35 | Audit trail fields | 4 | 4.6 |
| FR36 | Analyst notes | 6 | 6.3 |
| FR37 | 10-year retention | 4 | 4.6 |
| FR38 | OFAC timestamps | 4 | 4.2 |
| FR39 | Color coding | 4 | 4.5 |
| FR40 | Sort by risk | 4 | 4.4 |
| FR41 | Match transparency | 4, 6 | 4.3, 6.1 |
| FR42 | Downloadable Excel | 4 | 4.7 |
| FR43 | Match details | 6 | 6.1 |
| FR44 | Risk levels | 6 | 6.2 |
| FR45 | GL notes | 6 | 6.1 |
| FR46 | Re-screening | 6 | 6.4 |
| FR47 | Country alignment | 3 | 3.6 |
| FR48 | Preserve notes | 6 | 6.3 |
| FR49 | Version control | 4 | 4.7 |
| FR50 | Batch API | 2 | 2.3 |
| FR51 | Single API | 2 | 2.2 |
| FR52 | Version check API | 5 | 5.2 |
| FR53 | Update trigger API | 5 | 5.5 |
| FR54 | Auto API docs | 2 | 2.1 |
| FR55 | Structured JSON | 2 | 2.2 |
| FR56 | HTTP status codes | 2 | 2.2 |
| FR57 | Input validation | 2 | 2.3 |
| FR58 | Error messages | 2 | 2.2 |
| FR59 | Multipart upload | 2 | 2.3 |
| FR60 | JSON payloads | 2 | 2.2 |
| FR61 | Excel upload | 2 | 2.6 |
| FR62 | CSV upload | 2 | 2.6 |
| FR63 | Auto-detect columns | 2 | 2.4 |
| FR64 | Manual mapping | 2 | 2.7 |
| FR65 | Progress indicators | 2 | 2.8 |
| FR66 | Drag-drop | 2 | 2.6 |
| FR67 | Color-coded display | 2 | 2.9 |
| FR68 | Summary dashboard | 2 | 2.10 |
| FR69 | OFAC version display | 5 | 5.3 |
| FR70 | Update controls | 5 | 5.4 |
| FR71 | One-click download | 4 | 4.7 |
| FR72 | Screening IDs | 4 | 4.2 |
| FR73 | Timestamps | 4 | 4.2 |
| FR74 | Link to OFAC version | 4 | 4.2 |
| FR75 | Track data age | 5 | 5.1 |
| FR76 | Version history | 5 | 5.1 |
| FR77 | Spot-check validation | 5 | 5.3 |
| FR78 | Decision traceability | 6 | 6.5 |
| FR79 | Audit validation | 6 | 6.5 |

**Coverage:** 79/79 FRs mapped (100%)

---

## Summary

| Metric | Value |
|--------|-------|
| **Total Epics** | 6 |
| **Total Stories** | 41 |
| **FRs Covered** | 79 (100%) |
| **NFRs Addressed** | Performance, Accuracy, Compliance, Security |

### Implementation Sequence

1. **Epic 1** (Foundation) → Core matching works
2. **Epic 2** (Batch Screening) → Upload → Results workflow
3. **Epic 3** (Classification) → Smart OK/REVIEW/NOK
4. **Epic 4** (Reporting) → Audit-ready Excel
5. **Epic 5** (Data Freshness) → Keep OFAC current
6. **Epic 6** (Exception Review) → Resolve flagged cases

### Next Steps

1. Run `implementation-readiness` workflow to validate completeness
2. Run `sprint-planning` workflow to create sprint-status.yaml
3. Begin implementation with Epic 1, Story 1.1

---

_For implementation: Use the `dev-story` workflow to implement individual stories from this breakdown._

