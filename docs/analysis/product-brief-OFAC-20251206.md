---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments:
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251205_OFAC_Sanctions_Screening_Tools_Plan.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_List_Update_Policies_and_Strategy.md'
workflowType: 'product-brief'
lastStep: 5
project_name: 'OFAC'
user_name: 'Carlos'
date: '2025-12-06'
---

# Product Brief: OFAC

**Date:** 2025-12-06
**Author:** Carlos

---

## Executive Summary

OFAC sanctions screening tools for small-to-medium humanitarian NGOs, solving the bulk screening gap left when the U.S. Treasury removed free batch screening capabilities. Purpose-built for **low-frequency, high-stakes screening** (3-5 grant rounds per year, 50-100 organizations per batch), eliminating the pricing mismatch where commercial tools charge $2,000-$10,000/year regardless of volume.

**The Problem**: Manual one-by-one screening of organizations on the OFAC website takes 30-60 seconds per entry, creating hours of tedious work prone to transcription errors and documentation gaps. OFAC removed their bulk screening feature, forcing compliance officers to either pay enterprise prices for low-volume needs or accept compliance risk through manual processes.

**The Solution**: API-first screening service with Streamlit web application for batch processing. Upload Excel files with project beneficiaries, receive comprehensive screening reports with full 10-year audit trails. Built for internal use first, with commercial SaaS potential for other similarly-sized NGOs.

**The Impact**: Compliance officers screen entire grant rounds in minutes instead of hours, maintain audit compliance, and avoid $2,000-$10,000/year subscriptions designed for high-volume enterprise users. For low-frequency users (250-500 screenings/year), this represents 100% cost savings while improving accuracy and documentation quality.

---

## Core Vision

### Problem Statement

Small-to-medium humanitarian NGOs face a critical compliance bottleneck: screening project beneficiaries against OFAC sanctions lists. The U.S. Treasury's official website previously offered bulk screening but **removed this capability**, forcing compliance officers to manually screen each organization one-by-one.

**For low-frequency, high-stakes screening use cases (typical small-to-medium NGO):**
- **3-5 grant rounds per year** with 50-100 potential beneficiaries each
- **Total annual volume**: 250-500 screenings
- **Manual screening time**: 30-60 seconds per organization
- **Total time burden**: 2-8 hours per grant round, 10-40 hours annually

This creates multiple pain points:
- **Tedious manual data entry** copying organization names into OFAC website
- **High risk of transcription errors** with complex names and diacritics
- **Visual fatigue** scanning dense search results pages
- **Incomplete audit trails** relying on manual notes
- **Delayed grant approvals** while compliance bottlenecks clear

### Problem Impact

**For Compliance Officers**: Manual screening is mind-numbing, error-prone, and creates documentation challenges. The lack of batch processing turns what should be a 15-minute task into hours of repetitive work several times per year.

**For Grant Programs**: Screening delays cascade into delayed project approvals, frustrated field partners waiting for funding decisions, and pressure to "skip" thorough screening when facing urgent humanitarian crises.

**For the Organization**: Commercial compliance platforms are priced for high-volume enterprise users. At 250-500 screenings/year, paying $2,000-$10,000 annually means spending **$4-40 per screening** - economically unsustainable for small-to-medium NGOs.

**For Beneficiaries**: Delays in grant approvals mean slower humanitarian response when communities need help most urgently.

### Why Existing Solutions Fall Short

**OFAC Official Website**:
- Removed bulk screening capability (previously available, now gone)
- Only supports one-by-one manual searches
- No export or audit trail features
- Requires manual documentation of every search

**Commercial Compliance Platforms**:
- **sanctions.io** ($2,000/year minimum): Priced for high-volume daily users, not 3-5 batches/year
- **LexisNexis** ($10,000+/year): Enterprise pricing with unnecessary features
- **Pricing mismatch**: All charge flat annual fees regardless of volume - $2K-$10K for 250-500 screenings/year = $4-40 per screening
- **No humanitarian context awareness**: Don't flag Syria General License 21 applicability
- **Over-engineered for small NGOs**: Features designed for banks and exporters, not grant-making organizations

**Manual Excel + Copy-Paste**:
- Transcription errors copying names between systems
- No fuzzy matching for spelling variations
- Can't track OFAC data version for audit compliance
- Time-intensive and unscalable

### Proposed Solution

**Phase 1 (Internal MVP)**: API-first screening service with Streamlit web application for batch processing.

**Core Architecture**:
- **OFAC Screening API Service** (FastAPI/Flask)
  - RESTful endpoints for single and batch screening
  - Shared matching engine and data cache
  - Version tracking and update management
  - Localhost deployment for internal use

- **Streamlit Web Application**
  - Upload Excel/CSV files with project beneficiaries
  - Batch screen all organizations against SDN + Consolidated lists
  - Download comprehensive screening reports with:
    - Full audit trail (screening date, OFAC data version, match scores)
    - Color-coded results (OK/REVIEW/NOK)
    - Syria humanitarian context detection (General License 21)
    - Summary statistics and exceptions-only views
  - Excel export with multiple sheets for 10-year compliance documentation

**Core Features**:
- **Fuzzy matching** with country context (catches spelling variations)
- **Humanitarian aid detection** for Syria General License 21 awareness
- **Daily OFAC data checks** with version tracking
- **Local data storage** (no data leaves your machine)
- **CSV triplet format** (SDN + Consolidated lists with aliases and addresses)
- **Comprehensive reporting** with all fields needed for audit compliance

**Phase 1.5 (Optional)**: Excel Custom Function
- `=OFAC_CHECK(organization_name, country, purpose)` calling same API
- For ad-hoc screening between grant rounds
- Validate actual usage need before building

**Phase 2 (Future Commercial SaaS)**:
- Add authentication and API keys
- Deploy to cloud infrastructure
- Offer to other small-to-medium NGOs at volume-appropriate pricing ($200-500/year or pay-per-use)
- Same API architecture scales without rewrite

### Key Differentiators

**1. Built for Low-Frequency, High-Compliance Users**
- Designed for 3-5 grant rounds/year (not daily transaction screening)
- Batch-first workflow (not real-time integration)
- Perfect fit for small-to-medium NGO compliance needs

**2. Cost: Free (Internal) → Affordable (Commercial)**
- **Phase 1**: Zero cost for internal use
- **Phase 2**: Volume-appropriate pricing ($200-500/year vs. $2K-$10K)
- **ROI**: 75-95% cost savings vs. commercial alternatives
- No vendor lock-in, open architecture

**3. Humanitarian Context Awareness**
- Detects Syria + humanitarian aid keywords
- Flags General License 21 applicability automatically
- Built by practitioners for practitioners (not generic compliance tool)

**4. API-First Architecture**
- Single API service supports multiple clients
- Streamlit web app (primary)
- Future: Excel UDF, mobile app, CLI tools
- Commercial SaaS-ready without rewrite

**5. Solves the Bulk Screening Gap**
- Direct replacement for removed OFAC bulk screening feature
- Purpose-built for "screen 50-100 organizations per grant round" use case
- Fast, accurate, documented

**6. Compliance-First Design**
- 10-year audit trail requirements built-in
- OFAC data version tracking for every screening
- Comprehensive reporting for regulatory documentation
- Meets FFIEC guidance standards

**7. Build-First, Commercialize-Later Strategy**
- Prove internally with real grant rounds (3-5 batches)
- Validate accuracy and time savings
- Refine UX based on actual compliance officer workflow
- Only commercialize if internal success demonstrates product-market fit

---

## Target Users

### Primary Users

**Persona: Carlos Martinez - Compliance Officer at Mid-Sized NGO**

**Background & Role:**
- Wears multiple hats: Finance Director + Compliance Officer + occasional Grant Reviewer
- Background in accounting/finance, NOT legal or technology
- Technical comfort: Mid-to-low (comfortable with Excel, intimidated by command-line tools)
- Works at organization with $5-15M annual budget, 20-50 staff
- Handles OFAC compliance along with financial reporting, audit prep, and budget management

**Problem Experience:**
Carlos reviews 3-5 grant rounds per year, each with 50-100 potential beneficiary organizations. Currently screens each one manually on the OFAC website:
- Opens OFAC search page
- Copies organization name from Excel spreadsheet
- Pastes into search box
- Scans results visually for matches
- Makes notes in Word document or spreadsheet comments
- Repeats 50-100 times per grant round

**Pain Points:**
- **Time burden**: 2-8 hours per grant round doing mind-numbing copy-paste work
- **Transcription errors**: Complex organization names with diacritics frequently mistyped
- **Visual fatigue**: Scanning dense search results leads to missed details
- **Documentation gaps**: Manual notes don't meet audit trail requirements
- **Compliance anxiety**: Constant worry about false negatives exposing organization to violations
- **Opportunity cost**: Time spent on manual screening = time NOT spent on financial analysis or strategic work

**Success Vision:**
- Upload Excel file, get comprehensive report in 5 minutes
- Confidence in accuracy (fuzzy matching catches variations he might miss)
- Audit-ready reports with timestamps, OFAC version tracking, match scores
- Simple process that doesn't require IT support
- Reports he can share with board, legal counsel, and auditors without explanation
- Sleep better knowing he didn't miss a sanctioned entity

**Motivations:**
- Protect organization from OFAC violations (existential risk)
- Meet audit requirements without expensive subscriptions
- Reclaim time for higher-value financial work
- Look competent to board and executive leadership

---

### Secondary Users

**1. Program Officers (Grant Application Reviewers)**

**Persona: Maria Chen - Africa Regional Program Officer**

**Role:** Reviews grant applications from field partners, needs to flag potential compliance issues before forwarding to compliance review.

**Use Case:** Pre-screens organizations during initial application review to catch obvious red flags early (e.g., Syria-based organizations, entities in high-risk countries).

**Value:** Saves Carlos time by filtering out problematic applications before formal compliance review. Prevents awkward situations where program team advocates for a partner only to have compliance block it later.

**Interaction:** Might use the tool for quick ad-hoc checks ("Is this organization safe to recommend?") rather than batch processing.

---

**2. Executive Director (Board Reporting)**

**Persona: Jennifer Williams - Executive Director**

**Role:** Presents compliance posture to board of directors quarterly.

**Use Case:** Needs to report "All grant recipients screened against OFAC lists using current data" with evidence of systematic process.

**Value:** Carlos's screening reports provide board-ready documentation showing due diligence, version tracking, and audit trail.

**Interaction:** Doesn't use tool directly, but receives summary statistics from Carlos (e.g., "Screened 87 organizations in Q4, zero matches, all data current within 7 days").

---

**3. Internal/External Auditors**

**Persona: David Kim - External Auditor (CPA firm)**

**Role:** Annual audit includes compliance review, needs evidence of OFAC screening processes.

**Use Case:** Reviews Carlos's screening reports to validate:
- All grant recipients were screened
- Screening used current OFAC data
- Documentation meets 10-year retention requirements
- Process is systematic and repeatable

**Value:** Comprehensive reports with timestamps, OFAC version dates, and match details satisfy audit requirements without additional work from Carlos.

**Interaction:** Read-only access to screening reports, no direct tool usage.

---

**4. Legal Counsel (Risk Assessment)**

**Persona: Robert Thompson - External Legal Counsel**

**Role:** Advises on OFAC compliance, reviews flagged cases.

**Use Case:** When screening shows REVIEW status (fuzzy match, Syria humanitarian context), Carlos escalates to legal for interpretation.

**Value:** Detailed match information (scores, entity IDs, programs, remarks) helps legal counsel make informed determinations about General Licenses or false positives.

**Interaction:** Receives screening reports from Carlos, focuses on REVIEW/NOK cases requiring legal interpretation.

---

### User Journey

**Phase 1: Discovery (Internal Launch)**

**Trigger:** Carlos (compliance officer) builds tool for internal use

**Initial Users:** Just Carlos, testing with upcoming grant round

**Onboarding:**
- Carlos installs API service locally (one-time Docker setup or Python installer)
- Opens Streamlit app in browser (localhost)
- Uploads sample CSV to test matching accuracy
- Reviews screening report format, validates results against manual spot-checks

---

**Phase 2: Core Usage (Grant Round Workflow)**

**Typical Grant Round Scenario:**

1. **Preparation** (Day 1):
   - Carlos receives Excel file from program officers with 75 organizations for Q1 grants
   - Opens OFAC screening tool, checks data version (last updated 3 days ago - acceptable)

2. **Batch Screening** (Day 1, 10 minutes):
   - Uploads Excel file to Streamlit app
   - Selects columns: "Institution" (org name), "Country", "Project Description"
   - Clicks "Screen Against OFAC Lists"
   - Tool processes 75 organizations in ~2 minutes

3. **Results Review** (Day 1, 30-60 minutes):
   - Downloads comprehensive Excel report with 3 sheets:
     - Summary: 72 OK, 2 REVIEW, 1 NOK
     - Detailed Results: All 75 organizations with scores and context
     - Exceptions Only: Just the 3 flagged cases
   - Reviews REVIEW cases:
     - Syria organization with humanitarian aid keywords → Flags for legal counsel (General License 21 potential)
     - Fuzzy match (82% similarity, country mismatch) → Likely false positive, documents reasoning
   - Reviews NOK case:
     - 95% match with SDN entity, country match → Escalates to Executive Director and legal counsel immediately

4. **Documentation** (Day 1, 15 minutes):
   - Saves screening report to shared compliance folder
   - Adds summary to grant round memo for board
   - Forwards exception cases to legal counsel with context

5. **Board Presentation** (Day 7):
   - Presents to board: "75 organizations screened, 72 approved, 3 flagged for review, screening completed using OFAC data current as of [date]"
   - Board appreciates systematic process and documentation

---

**Phase 3: Success Moment**

**"Aha!" Moment #1:** First grant round takes 1 hour total (vs. 6-8 hours manual screening). Carlos realizes he just saved an entire workday.

**"Aha!" Moment #2:** External auditor reviews screening reports, says "This is exactly what we need - comprehensive audit trail, version tracking, systematic process. Well done."

**"Aha!" Moment #3:** Fuzzy matching catches a name variation Carlos would have missed manually (organization listed as "Archdiocèse de Bangui" in grant application, alias "Archdiocese of Bangui" in OFAC database with different spelling). Tool flags 88% match. Carlos thinks: "This just prevented a potential violation."

---

**Phase 4: Long-term Integration**

**Routine Adoption (Months 3-12):**
- Carlos uses tool for every grant round (5 times/year)
- Program officers ask Carlos to pre-screen questionable cases ad-hoc
- Tool becomes part of documented compliance procedures
- Executive Director cites systematic screening process in annual report

**Potential Phase 2 (Commercial Expansion):**
- Carlos mentions tool to peer compliance officers at NGO conferences
- Other small-to-medium NGOs express interest ("We're paying $2K/year for this - you built it yourself?!")
- Carlos considers offering as low-cost SaaS ($200-500/year) to peer organizations
- Tool becomes revenue-generating service for NGO sector

---

## Success Metrics

### Phase 1 Success Criteria (Internal MVP - Months 1-6)

**Critical Success Factors:**

1. **Cost Avoidance Achievement**
   - **Target**: Zero subscription costs for OFAC screening
   - **Measurement**: Tool eliminates need for $2,000-$10,000/year commercial subscriptions
   - **Success**: Internal tool handles 100% of screening needs without external services

2. **Report Quality & Trustworthiness**
   - **Target**: Screening reports accepted by Executive Director and Board without modification
   - **Measurement**: 100% of screening reports presented to board without requests for additional documentation
   - **Success**: External auditors approve screening documentation on first review
   - **Trustworthiness indicators**:
     - OFAC data version timestamp on every report
     - Match scores with confidence levels clearly displayed
     - Audit trail with screening date, data version, match details
     - Professional, clean report format (Excel multi-sheet output)

3. **Time Efficiency**
   - **Baseline**: 6-8 hours per grant round (manual screening)
   - **Target**: ≤1 hour per grant round (upload, review, document)
   - **Measurement**: Time from receiving organization list to completed screening report
   - **Success threshold**: Minimum 70% time savings (≤2.4 hours)

4. **Exception Detection (Catch What Manual Process Misses)**
   - **Target**: Fuzzy matching catches name variations that manual screening would miss
   - **Measurement**: Number of matches flagged by fuzzy matching (80-90% similarity) that wouldn't appear in exact search
   - **Success threshold**: At least 1 variant name match caught per year (validates matching engine value)
   - **Critical success**: Zero false negatives (no sanctioned entities missed)

5. **Ease of Use**
   - **Target**: No IT support required for regular use
   - **Measurement**: Carlos can complete screening workflow independently
   - **Success**: Simple 3-step process (upload → screen → download) with clear UI
   - **User experience**: Mid-to-low technical users can operate without training after first use

---

### Phase 2 Success Criteria (Commercial SaaS - Year 1 if launched)

**Market Validation Objectives:**

1. **Product-Market Fit Validation**
   - **Target**: Positive feedback from 3+ peer compliance officers at other NGOs
   - **Measurement**: Informal demos at NGO conferences, peer reviews
   - **Success**: At least 2 peer NGOs express willingness to pay $200-500/year

2. **Trust & Confidence Projection**
   - **Target**: Tool perceived as credible alternative to "big name" brands (LexisNexis, sanctions.io)
   - **Measurement qualitative indicators**:
     - Professional UI/UX comparable to commercial tools
     - Clear data source transparency (OFAC.gov official lists)
     - Visible version tracking and update mechanisms
     - Comprehensive audit trail documentation
   - **Success**: Peer organizations trust screening results without external validation
   - **Brand positioning**: "Fair, transparent, auditable" vs. "expensive black box"

3. **Customer Acquisition (if commercializing)**
   - **Year 1 Target**: 5-10 small-to-medium NGO customers
   - **Revenue Target**: $1,000-$5,000 annual revenue (validates business model viability)
   - **Success threshold**: Covers hosting/maintenance costs + Carlos's time investment

---

### Key Performance Indicators (Ongoing Tracking)

**Operational KPIs:**

1. **Screening Accuracy**
   - **Metric**: Percentage of screenings with zero false negatives (missed sanctioned entities)
   - **Target**: 100% (no violations from missed matches)
   - **Tracking**: Spot-check screenings against manual OFAC searches quarterly

2. **OFAC Data Freshness**
   - **Metric**: Average age of OFAC data at time of screening
   - **Target**: ≤7 days old (daily update checks)
   - **Tracking**: Automated version tracking in screening reports

3. **Exception Rate**
   - **Metric**: Percentage of organizations flagged as REVIEW or NOK
   - **Baseline expectation**: 2-5% (based on typical NGO grant recipient profiles)
   - **Tracking**: Monitor for anomalies (sudden spike indicates data issue or program change)

4. **Audit Compliance Rate**
   - **Metric**: Percentage of audits where screening documentation passes without deficiencies
   - **Target**: 100% (no audit findings related to OFAC compliance)
   - **Tracking**: Annual external audit results

**Efficiency KPIs:**

5. **Time Savings per Grant Round**
   - **Metric**: Hours saved vs. manual screening baseline (6-8 hours)
   - **Target**: 5-7 hours saved per grant round
   - **Annual target**: 25-35 hours saved per year (5 grant rounds × 5-7 hours)

6. **Report Generation Speed**
   - **Metric**: Time from file upload to downloadable report
   - **Target**: <5 minutes for batches of 50-100 organizations
   - **Technical benchmark**: <2 seconds per organization screening

**Quality KPIs:**

7. **Report Acceptance Rate**
   - **Metric**: Percentage of screening reports accepted by board/exec without revisions
   - **Target**: 100% (indicates report format meets stakeholder needs)

8. **False Positive Rate**
   - **Metric**: Percentage of REVIEW/NOK flags that are determined to be false matches upon manual review
   - **Acceptable range**: 10-30% (indicates conservative matching threshold)
   - **Tracking**: Carlos documents false positive determinations in review notes

---

### Business Objectives Alignment

**Phase 1 (Internal):**

- **Primary objective**: Eliminate $2,000-$10,000/year subscription costs while maintaining compliance
- **Secondary objective**: Reduce compliance officer time burden by 70%+ to enable higher-value work
- **Tertiary objective**: Improve audit trail quality to zero-deficiency standard

**Phase 2 (Commercial - if pursued):**

- **Primary objective**: Generate $1,000-$5,000 Year 1 revenue to validate business model
- **Secondary objective**: Establish brand reputation as "trustworthy, transparent, affordable" alternative to enterprise tools
- **Tertiary objective**: Build peer network of 5-10 small-to-medium NGO customers for product feedback and iteration

---

### Success Milestones & Validation Gates

**Month 1-2: Initial Build & Testing**
- ✅ API service + Streamlit app functional
- ✅ Fuzzy matching engine tested against sample data
- ✅ Report format approved by Carlos (internal user)

**Month 3: First Production Use**
- ✅ First real grant round screened (50-100 organizations)
- ✅ Time saved ≥70% vs. manual screening
- ✅ Report accepted by Executive Director/Board

**Month 6: Internal Validation**
- ✅ 3 grant rounds completed successfully
- ✅ External auditor reviews and approves screening documentation
- ✅ Zero compliance violations or audit findings
- ✅ At least 1 fuzzy match caught that manual screening would have missed

**Month 12: Commercial Decision Gate**
- ✅ If all Phase 1 metrics met → Evaluate commercial viability
- ✅ If peer interest validated → Develop Phase 2 SaaS architecture
- ✅ If internal success only → Continue as internal tool, no commercialization

---

## MVP Scope

### Core Features (Phase 1 - Months 1-3)

**1. OFAC Data Management**
- Download SDN + Consolidated lists from OFAC API (CSV triplets: SDN.CSV, ALT.CSV, ADD.CSV, CONS_PRIM.CSV, CONS_ALT.CSV, CONS_ADD.CSV)
- Local data cache in `data/` directory with version tracking (`version.json`)
- Version checking via HTTP Last-Modified headers
- Manual update controls: "Check for Updates" and "Update Now" buttons in UI
- Data freshness display (last updated timestamp, age in days, warning indicators at 7/14/30 days)

**2. OFAC Screening API Service (FastAPI)**
- **RESTful Endpoints**:
  - `POST /api/v1/screen/batch` - Batch screening (CSV/Excel upload)
  - `POST /api/v1/screen/single` - Single organization screening
  - `GET /api/v1/data/version` - Check OFAC data version and freshness
  - `POST /api/v1/data/update` - Trigger OFAC list download/update
- **Matching Engine**:
  - Fuzzy string matching using rapidfuzz library (token_sort_ratio method)
  - Default threshold: 80% similarity (configurable)
  - Text normalization (lowercase, diacritics removal, punctuation stripping)
  - Search against both SDN and Consolidated lists with aliases (ALT.CSV)
- **Country-Aware Scoring**:
  - Boost match confidence when organization country matches OFAC entity addresses (ADD.CSV)
  - De-boost scores for country mismatches
  - Handle regional designations (e.g., "Africa II" → country list mapping)
- **Syria Humanitarian Context Detection**:
  - Detect: Country = Syria/Syrian Arab Republic + Purpose keywords (humanitarian, aid, relief, medical, emergency, assistance)
  - Action: Flag REVIEW status with note "General License 21 may apply - manual review required"
  - Does NOT override NOK classification for SDN matches
- **Classification Logic**:
  - **OK**: No match >80% similarity
  - **REVIEW**: Fuzzy match 80-90% with country mismatch, OR Consolidated list match >80%, OR Syria humanitarian context
  - **NOK**: SDN match >90%, OR SDN match 80-90% with country alignment
- **Local Deployment**: Runs on localhost (no cloud hosting for Phase 1)

**3. Streamlit Web Application (Frontend)**
- **Technology Choice**: Streamlit (Python-based)
  - **Rationale**: Fast development (2-3 weeks), simple deployment, good enough for internal use and early commercial validation
  - **Future**: Rebuild in React if Phase 2 commercial traction validates investment (API remains unchanged)
- **File Upload Widget**: Accept Excel (.xlsx) or CSV files
- **Column Mapping UI**:
  - Auto-detect common column names ("Institution", "Organization", "Country", "Project Description")
  - Manual column selection dropdowns for Organization Name (required), Country (optional), Purpose (optional)
- **Batch Screening Workflow**:
  - Upload file → Map columns → Click "Screen Against OFAC Lists"
  - Progress indicator during screening (processing X of Y organizations)
  - Processing time: ~2 seconds per organization, <5 minutes for 100 organizations
- **Results Display**:
  - Interactive table with color coding (green = OK, yellow = REVIEW, red = NOK)
  - Sortable/filterable columns
  - Summary statistics at top (Total screened, OK/REVIEW/NOK counts)
- **Report Download**: Export to Excel button

**4. Comprehensive Screening Reports (Excel Multi-Sheet)**
- **Sheet 1: Summary Statistics**
  - Report metadata (generated date/time, OFAC data version, user who generated, batch ID)
  - Total organizations screened
  - Results breakdown (count and percentage for OK/REVIEW/NOK)
  - Exception summary (REVIEW + NOK cases)
  - Data freshness warning if >7 days old

- **Sheet 2: Detailed Results** (All Organizations)
  - Screening ID (unique identifier for audit trail)
  - Screening Date/Time
  - Organization Name (input)
  - Country (input)
  - Project Description (input)
  - Screening Status (OK/REVIEW/NOK)
  - Match Found (Yes/No)
  - Confidence Level (match score percentage, only if match)
  - OFAC List Hit (SDN / Consolidated / None)
  - Matched Entity Name (from OFAC list, if applicable)
  - Match Type (Exact / Fuzzy / Alias)
  - Country Alignment (Match / Mismatch / N/A)
  - General License Applicable (Yes - Humanitarian / No)
  - Risk Level (Low / Medium / High)
  - Analyst Notes (free-form field for manual annotations)
  - OFAC Data Version (date when OFAC lists were last updated)

- **Sheet 3: Exceptions Only** (REVIEW + NOK Cases)
  - Same columns as Detailed Results
  - Filtered to show only organizations requiring manual review or blocking
  - Sorted by Risk Level (High → Medium → Low)

**5. Local Deployment Package**
- **Deployment Method**: Docker container (preferred) OR Python installer script
- **Startup**: Single command launches API service + Streamlit app
- **Access**: Open browser to http://localhost:8501 (Streamlit default port)
- **Data Persistence**: Local `data/` directory stores OFAC lists and version.json
- **No Authentication**: Single-user local deployment (Phase 1 only)

---

### Phase 1.5: Excel UDF Addition (Months 4-6)

**Timeline**: After 3 successful grant rounds with Phase 1 Streamlit app

**Decision Gate**: Proceed with Phase 1.5 ONLY if:
- ✅ Phase 1 validation successful (3 grant rounds completed)
- ✅ Carlos identifies need for ad-hoc screening between grant rounds
- ✅ Program officers request quick pre-screening capability
- ✅ Workflow analysis shows value in in-spreadsheet screening

---

**Phase 1.5 Core Features:**

**1. Excel Custom Function (UDF via xlwings)**

**Function Signature:**
```excel
=OFAC_CHECK(organization_name, [country], [purpose])
```

**Parameters:**
- `organization_name` (required): Organization/entity name to screen
- `country` (optional): Country for context-aware matching
- `purpose` (optional): Project purpose for Syria GL-21 detection

**Return Values:**
- **"OK"** - No match found (green cell formatting)
- **"NOK: [details]"** - SDN match found (red cell formatting)
  - Example: `"NOK: Match 'BANCO NACIONAL DE CUBA' (SDN #306, 95% match)"`
- **"REVIEW: [context]"** - Requires manual review (yellow cell formatting)
  - Example: `"REVIEW: Fuzzy match 82%, country mismatch - likely false positive"`
  - Example: `"REVIEW: Syria humanitarian context - General License 21 may apply"`

**2. Architecture Integration**

**API Communication:**
- Excel UDF calls existing API service via HTTP
- Endpoint: `POST http://localhost:8000/api/v1/screen/single`
- Request payload: `{"organization": "...", "country": "...", "purpose": "..."}`
- Response: JSON with screening result, match details, classification

**Benefits of API Architecture:**
- ✅ Zero code duplication (UDF and Streamlit use same matching engine)
- ✅ Same OFAC data cache (single source of truth)
- ✅ Consistent results across both tools
- ✅ API service must be running for UDF to work (acceptable trade-off)

**3. Caching Strategy**

**Local Cache (Per Excel Session):**
- Cache results per unique `(organization, country, purpose)` tuple
- Prevents redundant API calls when dragging formula down identical names
- Cache invalidates on Excel workbook close or manual refresh
- Cache stored in memory (not persisted to disk)

**Cache Performance:**
- First call for "Archdiocese of Bangui, CAR, Construction": ~2 seconds (API call + matching)
- Subsequent calls for same org: <50ms (cache hit)
- Dragging formula down 100 identical organizations: ~50ms total (after first call)

**4. User Interface Elements**

**Excel Ribbon Tab: "OFAC Screening"**

**Buttons:**
- **"Start API Service"** - Launches localhost API if not already running (optional convenience)
- **"Check API Status"** - Verifies API service is reachable (displays "Connected" or "Offline")
- **"Update OFAC Lists"** - Triggers data update via API `/data/update` endpoint
- **"View Data Version"** - Shows last OFAC update timestamp and age
- **"Refresh All Checks"** - Forces recalculation of all `=OFAC_CHECK()` formulas in workbook (clears cache)
- **"Settings"** - Configure API endpoint URL (default: http://localhost:8000)

**Status Indicator:**
- Real-time display: "API: Connected | OFAC Data: 3 days old"
- Warning icon if data >7 days old
- Error icon if API unreachable

**5. Conditional Formatting (Auto-Applied)**

When `=OFAC_CHECK()` formula is used, automatically apply cell formatting:
- **Green fill** for "OK" results
- **Yellow fill** for "REVIEW" results
- **Red fill** for "NOK" results
- **Gray fill** for errors (API offline, invalid input)

**6. Error Handling**

**Error Messages:**
- `"#API_OFFLINE"` - API service not running (display message: "Start API service first")
- `"#INVALID_INPUT"` - Empty organization name or malformed data
- `"#TIMEOUT"` - API call exceeded 10-second timeout
- `"#ERROR: [details]"` - Generic error with details for troubleshooting

**Graceful Degradation:**
- If API offline, display error but don't crash Excel
- Provide clear instructions in error message
- Allow retry without closing workbook

**7. Installation & Setup**

**Prerequisites:**
- Python 3.9+ installed on user's machine
- xlwings library (`pip install xlwings`)
- API service running (same service as Streamlit app uses)

**Installation Steps:**
1. Install xlwings: `pip install xlwings`
2. Run xlwings addin install: `xlwings addin install`
3. Open `OFAC_Checker.xlsm` workbook
4. Enable macros when prompted
5. Start API service: `python api_service.py` (or use "Start API Service" button)
6. Test: Enter `=OFAC_CHECK("Test Org")` in any cell

**Distribution:**
- Provide `OFAC_Checker.xlsm` template workbook with pre-configured ribbon
- Include `ofac_excel_functions.py` (xlwings UDF Python module)
- Installation guide with screenshots for non-technical users

**8. Use Cases**

**Primary Use Cases:**
1. **Ad-hoc Screening Between Grant Rounds**
   - Quick check on single organization before preliminary discussion
   - Example: Program officer calls Carlos: "Can I talk to XYZ organization about partnership?"
   - Carlos opens Excel, types `=OFAC_CHECK("XYZ Org", "Syria")`, gets instant answer

2. **In-Spreadsheet Workflow**
   - Grant application tracking spreadsheet with OFAC column
   - Drag formula down to screen 20-30 organizations during initial review
   - Color-coded results help prioritize which applications to advance

3. **Spot-Checking Existing Partners**
   - Re-screen current partners periodically (e.g., quarterly)
   - Paste partner names in column, add formula, identify if any newly sanctioned

**Secondary Use Cases:**
- Program officers self-serve screening (reduces Carlos's interruptions)
- Quick validation before Carlos runs full Streamlit batch report
- Backup screening method if Streamlit has issues

---

**Phase 1.5 Success Criteria**

**Functional Success:**
- ✅ UDF returns accurate results matching Streamlit batch screening
- ✅ Response time <3 seconds per organization (acceptable for ad-hoc use)
- ✅ Conditional formatting applies correctly (green/yellow/red)
- ✅ Error handling provides clear guidance when API offline

**User Adoption Success:**
- ✅ Carlos uses UDF at least 2-3 times between grant rounds (validates need)
- ✅ Program officers successfully use UDF without Carlos's help (validates simplicity)
- ✅ UDF catches at least 1 case that would have required manual OFAC website lookup

**Decision Gates:**

**Proceed to Regular Use (Keep UDF):**
- Carlos uses UDF regularly (>5 times between grant rounds)
- Program officers adopt it for pre-screening
- Saves time compared to manual OFAC lookups

**Deprecate UDF (Remove from toolkit):**
- Carlos rarely uses it (<2 times in 3 months)
- Batch screening via Streamlit meets 95%+ of needs
- Maintenance burden not justified by usage

---

**Phase 1.5 Out of Scope**

**NOT Included in Phase 1.5:**

1. **Advanced Excel Features**
   - Bulk screening via Excel ribbon button (use Streamlit for batches)
   - Historical screening log within Excel
   - Automated re-screening on workbook open
   - Integration with Excel data validation rules

2. **Offline Mode**
   - UDF requires API service running (no standalone Excel-only mode)
   - No embedded OFAC data within Excel workbook
   - Rationale: Keeps data cache centralized, ensures consistency

3. **Cloud API Connection**
   - Phase 1.5 UDF connects to localhost API only
   - Cloud API connection deferred to Phase 2 (commercial SaaS)
   - Rationale: Focus on internal use validation first

4. **Cross-Platform Support**
   - xlwings requires Windows or Mac with Excel installed
   - No LibreOffice Calc support
   - No Google Sheets support
   - Rationale: Carlos uses Excel on Windows, optimize for primary use case

---

**Phase 1.5 Timeline & Effort**

**Development Timeline: 1-2 Weeks**

**Week 1: Core UDF Development**
- Day 1-2: xlwings UDF function (`ofac_check()` calling API)
- Day 3: Caching logic and error handling
- Day 4: Excel ribbon UI buttons (Start API, Check Status, Update Lists)
- Day 5: Conditional formatting automation

**Week 2: Testing & Documentation**
- Day 1-2: Testing with real organization names from past grant rounds
- Day 3: Installation guide with screenshots
- Day 4: Training Carlos on UDF usage
- Day 5: Buffer for bug fixes and refinements

**Effort: 40-60 hours total** (vs. 80-120 hours for Phase 1 Streamlit app)

**Dependencies:**
- ✅ Phase 1 API service must be complete and stable
- ✅ API `/screen/single` endpoint fully functional
- ✅ Carlos has successfully completed 3 grant rounds with Streamlit

---

### Out of Scope for MVP (Phase 1 & 1.5)

**Explicitly NOT Included:**

1. **Automated Daily OFAC Updates**
   - **Rationale**: Manual updates sufficient for low-frequency use (3-5 grant rounds/year)
   - **Phase 1 Approach**: Manual "Update Now" button with visual freshness indicators
   - **Timeline**: Add scheduled checks in Phase 2 if desired

2. **User Authentication & Multi-User Support**
   - **Rationale**: Local single-user deployment for Phase 1 (Carlos only)
   - **Timeline**: Required for Phase 2 commercial SaaS (authentication, API keys, multi-tenancy)

3. **Advanced UI Features**
   - Complex filtering/search within results (basic sort/filter sufficient for MVP)
   - Saved search queries or screening templates
   - Batch history tracking (only current session for Phase 1)
   - Dashboard analytics (beyond summary statistics)

4. **PDF Report Generation**
   - **Rationale**: Excel reports meet audit requirements; PDF is nice-to-have
   - **Timeline**: Add in Phase 2 if board/auditors request it

5. **Commercial SaaS Features**
   - Cloud hosting and deployment
   - Billing/payment integration
   - Usage metering and quota management
   - White-label branding customization
   - Multi-tenant data isolation
   - **Timeline**: Phase 2 (Months 9-12) if commercial validation succeeds

6. **React Frontend Rebuild**
   - **Rationale**: Streamlit adequate for internal use and early commercial pilots
   - **Timeline**: Phase 2 (Months 9-12) ONLY if 2-3 peer NGOs validate willingness to pay
   - **Architecture Protection**: API-first design means frontend swap doesn't touch backend code

---

### MVP Success Criteria

**Phase 1 is successful if (Month 6 validation gate):**

1. **Functional Completeness**
   - ✅ API service + Streamlit app deployed and operational
   - ✅ Fuzzy matching engine catches name variations with 80%+ threshold
   - ✅ All screening report fields populated correctly
   - ✅ Zero critical bugs blocking workflow

2. **User Validation (Internal)**
   - ✅ Carlos completes 3 real grant rounds using the tool (minimum validation dataset)
   - ✅ Time savings ≥70% (6-8 hours manual → ≤2.4 hours with tool)
   - ✅ Screening reports accepted by Executive Director and Board without modification
   - ✅ External auditor approves screening documentation (zero audit findings)

3. **Accuracy & Trust**
   - ✅ Zero false negatives (no sanctioned entities missed)
   - ✅ At least 1 fuzzy match caught that manual screening would have missed (validates matching engine value)
   - ✅ False positive rate 10-30% (indicates conservative threshold, not too aggressive)

4. **Commercial Viability Indicators** (Phase 2 Decision Gate)
   - ✅ 2-3 peer compliance officers at other NGOs express interest after informal demo
   - ✅ At least 1 peer NGO states willingness to pay $200-500/year
   - ✅ Carlos confident tool projects "trust and professionalism" comparable to commercial alternatives

**If all criteria met → Proceed to Phase 2 planning (React rebuild + commercial SaaS)**

**If only internal success → Continue as internal tool, no commercialization**

---

### Future Vision (Phase 2+ if commercialized)

**Phase 2: Commercial SaaS Launch (Year 1)**

**Target Market**: Small-to-medium U.S.-based NGOs with international operations
- **Market Size**: Estimated 500-1,000 NGOs with OFAC compliance needs
- **Target Segment**: Low-frequency screening (3-10 batches/year, 250-1,000 screenings annually)
- **Positioning**: "Affordable, transparent, auditable alternative to enterprise compliance tools"

**Key Enhancements**:
1. **React Frontend Rebuild**
   - Modern, professional UI comparable to LexisNexis/sanctions.io
   - Custom branding and white-label capabilities
   - Responsive design (mobile/tablet support)

2. **Cloud Deployment & SaaS Infrastructure**
   - Hosted API service (AWS, Railway, or Heroku)
   - Authentication and API key management
   - Multi-tenant data isolation (each NGO's screening data separate)
   - Usage metering and billing integration (Stripe)

3. **Pricing & Business Model**
   - **Tier 1**: $200-300/year for <500 screenings/year (small NGOs)
   - **Tier 2**: $400-600/year for 500-1,500 screenings/year (medium NGOs)
   - **Pay-per-use option**: $0.50-$1.00 per screening (no annual commitment)
   - **Free tier**: 25 screenings/month for trial/evaluation

4. **Customer Success Features**
   - Onboarding tutorials and documentation
   - Email support for technical issues
   - Quarterly compliance webinars (OFAC update briefings)
   - Community forum for peer knowledge sharing

**Phase 3: Platform Expansion (Year 2-3)**

**Advanced Features**:
1. **Excel Add-In (UDF)** - Production-ready version calling cloud API
2. **Mobile App** - iOS/Android for field officers to screen on-the-go
3. **Automated Workflows**
   - Email notifications when OFAC lists update
   - Scheduled re-screening of existing partner lists
   - Integration with grant management systems (Salesforce, Fluxx)
4. **Enhanced Matching**
   - Machine learning-based name matching
   - Entity resolution (detect when two names refer to same organization)
   - Historical screening tracking (flag if previously cleared partner now appears on OFAC list)

**Additional Compliance Lists** (if customer demand justifies):
- UN Security Council sanctions
- EU sanctions lists
- UK OFSI (Office of Financial Sanctions Implementation)
- Multi-list consolidated screening

**Market Expansion**:
- **Geographic**: International NGOs (EU, Canada, Australia with OFAC compliance needs)
- **Vertical**: Foundations, faith-based organizations, development banks
- **Partnership**: Integration with grant management software vendors

---
