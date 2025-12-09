---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
inputDocuments:
  - '/home/cgorricho/apps/OFAC/docs/analysis/product-brief-OFAC-20251206.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251205_OFAC_Sanctions_Screening_Tools_Plan.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_List_Update_Policies_and_Strategy.md'
workflowType: 'prd'
lastStep: 11
completed: true
completionDate: '2025-12-08'
project_name: 'OFAC'
user_name: 'Carlos'
date: '2025-12-07'
---

# Product Requirements Document - OFAC

**Author:** Carlos
**Date:** 2025-12-07

## Executive Summary

**OFAC Sanctions Screening Tools for Humanitarian NGOs** solves the critical compliance gap created when the U.S. Treasury removed free bulk screening capabilities. Built for small-to-medium humanitarian organizations conducting **low-frequency, high-stakes screening** (3-5 grant rounds per year, 50-100 organizations per batch), this API-first screening service eliminates the pricing mismatch where commercial tools charge $2,000-$10,000/year regardless of whether you screen 500 or 50,000 entities annually.

**The Core Problem:** Manual screening of grant beneficiaries takes 30-60 seconds per organization, turning what should be a 15-minute compliance task into 2-8 hours of mind-numbing, error-prone work. Compliance officers must choose between paying enterprise prices designed for banks and exporters, or accepting compliance risk through manual processes that miss name variations and lack proper audit trails.

**The Solution:** FastAPI-based screening service with Streamlit web application for batch processing. Upload Excel files with project beneficiaries, receive comprehensive screening reports with full 10-year audit trails in minutes. **Humanitarian context intelligence** automatically detects when organizations operate in sanctioned countries (Syria, Iran, Venezuela, etc.) for legitimate humanitarian aid purposes, flagging applicable General Licenses rather than blocking outright—a critical nuance that generic compliance tools miss.

**The Impact:** Compliance officers screen entire grant rounds in under 1 hour (vs. 6-8 hours manual), eliminate $2,000-$10,000/year subscription costs, and gain audit-ready documentation that passes external review without modification. Most critically: **compliance risk avoidance**—fuzzy matching catches name variations that manual screening misses, preventing the existential risk of OFAC violations.

### What Makes This Special

**1. Built for the Underserved Segment**

Every existing compliance tool is designed for high-volume daily users (banks, exporters, payment processors). This is purpose-built for **low-frequency, high-compliance** organizations: humanitarian NGOs screening 250-500 entities annually across 3-5 grant rounds. The workflow, pricing, and features match actual usage patterns rather than forcing square-peg enterprise solutions into round humanitarian holes.

**2. Compliance Risk Avoidance + Audit-Ready Confidence**

This isn't primarily about time savings—it's about **sleeping at night**. The #1 value driver is confidence that you won't miss a sanctioned entity due to:
- Fuzzy matching catching spelling variations (Archdiocèse vs Archdiocese)
- Country-aware scoring reducing false negatives
- Comprehensive audit trails with OFAC data version timestamps
- Reports that pass board and external auditor review without modification

For compliance officers, false negatives are career-ending. This tool provides the trust and documentation that manual screening cannot.

**3. Humanitarian Context Intelligence (Universal Pattern)**

Generic compliance tools treat all sanctioned country matches as automatic blocks. This tool understands that **humanitarian NGOs legitimately operate in sanctioned countries** (Syria, Iran, Venezuela, Cuba, etc.) under specific General Licenses.

**Universal detection pattern:**
- ANY sanctioned country match + humanitarian aid keywords detected → **REVIEW** status with applicable General License flagged
- Sanctioned country match WITHOUT humanitarian context → **NOK** (block)
- Dynamic General License mapping (GL-21 for Syria, GL D-1 for Iran, GL-41 for Venezuela, etc.)

**Built by practitioners for practitioners**—this nuance is invisible to generic tools but critical for humanitarian operations.

**4. Transparency Over "Black Box" Trust**

Challenges the assumption that "expensive = trustworthy." This tool earns trust through:
- **Visible data sources:** OFAC.gov official lists, version timestamps on every report
- **Explainable matching:** Match scores, country alignment, alias detection all documented
- **Open architecture:** API-first design, no vendor lock-in
- **Audit transparency:** Every decision traceable and defensible

Compliance officers can explain and defend results to boards, auditors, and legal counsel—unlike proprietary "black box" algorithms.

**5. API-First Architecture Enables Evolution**

Single screening API service supports:
- **Phase 1:** Streamlit web app for batch processing (internal MVP)
- **Phase 1.5:** Excel custom function for ad-hoc checks (if validated)
- **Phase 2:** Commercial SaaS for peer NGOs (if market validates)
- **Future:** Mobile apps, grant management integrations, CLI tools

Backend remains stable while frontend evolves based on user needs. No costly rewrites when scaling from internal tool → commercial product.

**6. Build-First, Commercialize-Later Validation**

Prove internally with 3-5 real grant rounds before considering commercial expansion. Validate:
- Time savings (≥70% reduction target)
- Accuracy (zero false negatives)
- Audit acceptance (external auditor approval)
- Trust projection (peer interest at NGO conferences)

Only pursue Phase 2 commercial SaaS if internal success demonstrates genuine product-market fit. Risk-managed approach that doesn't over-invest before validation.

## Project Classification

**Technical Type:** API Backend (primary) + Web Application (frontend)
**Domain:** GovTech (Government/Regulatory Compliance)
**Complexity:** High

**Classification Rationale:**

This is fundamentally an **API backend** project—the core value lives in the screening service with its fuzzy matching engine, OFAC data management, and classification logic. The Streamlit web app is the initial UI layer, but the API-first architecture enables multiple future clients (Excel UDF, commercial dashboard, mobile apps, integrations).

**GovTech domain** classification reflects the regulatory compliance context:
- **Federal government regulations:** U.S. Treasury OFAC sanctions lists
- **Compliance requirements:** 10-year audit trails, version tracking, transparency
- **Public sector operations:** Humanitarian NGOs serving international communities
- **Accuracy criticality:** False negatives = OFAC violations with severe penalties

**High complexity designation** drives these requirements:

1. **Regulatory Accuracy:** False negatives expose organizations to federal violations, fines, and reputational damage. Matching algorithm must be conservative yet intelligent enough to reduce false positives.

2. **Audit & Transparency:** Must satisfy external auditors, board oversight, and potential federal review. Every screening decision must be traceable, explainable, and defensible.

3. **Security & Data Handling:** While screening uses public OFAC data, organizational screening results contain sensitive grant decision information requiring proper handling.

4. **Compliance Standards:** If commercializing to organizations with federal funding, may need to address:
   - Section 508 accessibility standards
   - Security frameworks (FISMA considerations for federal grantees)
   - Data retention and privacy requirements

5. **General License Interpretation:** Humanitarian aid exception detection requires understanding complex, evolving regulatory frameworks across multiple sanctioned jurisdictions.

**Domain-Specific Considerations for High Complexity GovTech:**

- **Procurement compliance:** If selling to federally-funded NGOs, understand government procurement rules
- **Regulatory tracking:** OFAC policies and General Licenses evolve; tool must accommodate regulatory changes
- **Transparency requirements:** Match scoring, data versioning, and decision logic must be visible and explainable
- **Documentation standards:** Reports must meet federal audit and compliance documentation requirements

## Success Criteria

### User Success

**The "Sleep at Night" Confidence Factor**

Success means Carlos (and peer compliance officers) can **defend this tool to the board with complete confidence**. This requires:

1. **Match Score Transparency**
   - Every screening result shows percentage match (e.g., "88% match with Archdiocese of Bangui")
   - Country alignment clearly indicated (Match/Mismatch/N/A)
   - Match type documented (Exact/Fuzzy/Alias)
   - Able to explain WHY the tool flagged or cleared an organization

2. **OFAC Version Tracking**
   - Every report timestamps which OFAC data version was used
   - Screening date + data version = defensible audit trail
   - Can prove "we screened using current data as of [date]"
   - 10-year retention requirements built into report design

3. **Spot-Check Validation Capability**
   - Carlos can manually verify results against OFAC website
   - Match details provide enough context to validate accuracy
   - Suspicious results can be independently confirmed
   - Trust but verify approach supported

4. **Board-Ready Documentation**
   - Reports require zero modification before board presentation
   - Summary statistics answer standard board questions
   - Exception cases clearly explained with context
   - Professional format comparable to commercial tools

**User Success = Defendable Confidence:** Carlos can stand before the board, auditors, or legal counsel and explain every screening decision with supporting evidence.

### Business Success

**Phase 1: Internal Validation (Months 1-6)**

**Critical Success Factors:**

1. **Cost Avoidance Achievement**
   - **Target:** Zero subscription costs for OFAC screening
   - **Measurement:** Tool eliminates need for $2,000-$10,000/year commercial subscriptions
   - **Success:** Internal tool handles 100% of screening needs without external services

2. **Time Efficiency Transformation**
   - **Baseline:** 6-8 hours per grant round (manual screening)
   - **Target:** ≤1 hour per grant round (upload, review, document)
   - **Success Threshold:** Minimum 70% time savings (≤2.4 hours)
   - **Annual Impact:** 25-35 hours reclaimed for higher-value work

3. **Zero False Negatives (Compliance Risk Avoidance)**
   - **Target:** 100% accuracy - no sanctioned entities missed
   - **Measurement:** Spot-check screenings against manual OFAC searches quarterly
   - **Success:** Zero OFAC violations from missed matches over 6 months

4. **Audit & Report Acceptance**
   - **Target:** 100% acceptance by board/exec/auditors without modification
   - **Measurement:** Screening reports pass external audit review on first submission
   - **Success:** Zero audit findings related to OFAC compliance documentation

5. **Exception Detection Validation**
   - **Target:** Fuzzy matching catches name variations manual screening would miss
   - **Success Threshold:** At least 1 variant name match caught in 6 months
   - **Proof of Value:** Demonstrates matching engine superiority over manual process

**Month 6 Validation Gate Requirements:**
- ✅ 3 real grant rounds completed successfully with tool
- ✅ 70%+ time savings achieved and sustained
- ✅ Reports accepted by board and external auditor without revisions
- ✅ Zero compliance violations or audit findings
- ✅ At least 1 fuzzy match caught that manual screening would have missed

**Phase 2: Commercial Viability Decision (Month 12)**

**Commercial "Go/No-Go" Decision Criteria:**

1. **Peer Interest Validation (Primary Signal)**
   - **Minimum:** 2-3 peer compliance officers at other NGOs express genuine interest
   - **Strong Signal:** Interest expressed after live demo (not just concept)
   - **Gold Standard:** At least 1 peer NGO states explicit willingness to pay $200-500/year
   - **Validation Method:** Informal demos at NGO conferences, peer network conversations

2. **Trust & Professionalism Projection**
   - **Target:** Tool perceived as credible alternative to "big name" brands (LexisNexis, sanctions.io)
   - **Measurement:** Peer organizations trust screening results without external validation
   - **Success:** Professional UI/UX comparable to commercial tools, not "homemade" appearance
   - **Brand Positioning:** "Fair, transparent, auditable" vs. "expensive black box"

3. **Internal Success Demonstration**
   - **Requirement:** All Phase 1 success criteria met convincingly
   - **Proof Point:** Carlos confidently recommends tool to peers
   - **Board Endorsement:** Executive leadership supports commercial exploration
   - **Risk Management:** Internal use continues regardless of commercial decision

4. **Market Validation Indicators**
   - **Target Customer Profile:** Small-to-medium NGOs ($5-15M budget) with 250-1,000 screenings/year
   - **Willingness to Pay:** Validated at $200-500/year price point (vs. $2K-$10K alternatives)
   - **Revenue Feasibility:** 5-10 customers Year 1 = $1,000-$5,000 covers hosting + maintenance
   - **Value Proposition Resonance:** Peers immediately understand "low-frequency compliance" problem

**Decision Matrix:**

| Condition | Decision |
|-----------|----------|
| All Phase 1 criteria met + 2+ peers interested + 1+ willing to pay | **PROCEED to Phase 2 (Commercial SaaS)** |
| All Phase 1 criteria met + peer interest unclear | **Continue internal use, defer commercialization 6 months** |
| Phase 1 criteria partially met | **Focus on internal improvement, no commercialization yet** |
| Internal tool works but no peer interest | **Keep as internal tool indefinitely (still major success)** |

### Technical Success

**Performance Requirements:**

1. **Screening Speed**
   - **Target:** <2 seconds per organization screening (matching + classification)
   - **Batch Processing:** <5 minutes for 100 organizations
   - **User Experience:** Progress indicator, no perceived lag

2. **OFAC Data Freshness**
   - **Target:** ≤7 days old at time of screening
   - **Automated Checks:** Daily version checking via HTTP Last-Modified headers
   - **Warning System:** Visual indicators at 7/14/30 days old
   - **Update Mechanism:** Manual "Update Now" button, atomic download/swap

3. **Matching Accuracy**
   - **Zero False Negatives:** No sanctioned entities missed (critical requirement)
   - **Acceptable False Positive Rate:** 10-30% of REVIEW/NOK flags are false matches upon manual review
   - **Rationale:** Conservative threshold preferred over aggressive (better safe than sorry)

4. **System Reliability**
   - **Local Deployment:** Runs on localhost without cloud dependencies (Phase 1)
   - **Data Persistence:** Local cache survives restarts, no data loss
   - **Error Handling:** Network failures don't corrupt OFAC data cache
   - **Graceful Degradation:** Clear error messages, recovery instructions

5. **Audit Trail Completeness**
   - **10-Year Retention:** Reports contain all fields needed for compliance documentation
   - **Version Tracking:** Every screening linked to specific OFAC data version
   - **Traceability:** Screening ID, timestamp, match details, analyst notes
   - **Exportability:** Excel multi-sheet format for archival storage

### Measurable Outcomes

**Quantitative Metrics (6-Month Validation):**

| Metric | Baseline (Manual) | Target (Tool) | Success Threshold |
|--------|------------------|---------------|-------------------|
| **Time per grant round** | 6-8 hours | ≤1 hour | ≤2.4 hours (70% savings) |
| **Annual cost** | $2,000-$10,000 | $0 | $0 (100% cost avoidance) |
| **False negatives** | Unknown risk | 0 | 0 (zero tolerance) |
| **Report acceptance** | Manual notes, often revised | 100% accepted | 100% first-time acceptance |
| **Audit findings** | Variable | 0 | 0 (zero compliance deficiencies) |
| **Exception detection** | Misses variants | ≥1 caught | ≥1 variant match in 6 months |
| **Data freshness** | Unknown | ≤7 days | ≤7 days average |
| **Processing speed** | 30-60 sec/org | <2 sec/org | <5 min for 100 orgs |

**Qualitative Outcomes:**

- **Confidence:** Carlos can defend tool to board with supporting evidence
- **Trust:** External auditors approve documentation quality
- **Professionalism:** Reports look comparable to commercial tools
- **Usability:** No IT support required after initial setup
- **Stress Reduction:** Compliance anxiety replaced with "sleep at night" confidence

**False Positive Rate (Phase 1 Learning Metric):**

- **Cannot be measured until tool is operational**
- **Acceptable Range (Expected):** 10-30% of REVIEW/NOK flags turn out to be false matches
- **Tracking Method:** Carlos documents false positive determinations in review notes
- **Adjustment Strategy:** If >50% false positives, consider raising similarity threshold (80% → 85%)
- **Learning Goal:** Establish baseline during first 3 grant rounds, optimize in months 4-6

## Product Scope

### MVP - Minimum Viable Product (Phase 1: Months 1-3)

**Core Functionality (Non-Negotiable for Launch):**

1. **OFAC Data Management**
   - Download SDN + Consolidated lists (CSV triplets: SDN.CSV, ALT.CSV, ADD.CSV, CONS_PRIM.CSV, CONS_ALT.CSV, CONS_ADD.CSV)
   - Local data cache with version tracking (version.json)
   - Manual update controls ("Check for Updates", "Update Now" buttons)
   - Data freshness display with warning indicators (7/14/30 days)

2. **Screening API Service (FastAPI)**
   - Batch screening endpoint (`POST /api/v1/screen/batch`)
   - Single screening endpoint (`POST /api/v1/screen/single`)
   - Data version endpoint (`GET /api/v1/data/version`)
   - Update trigger endpoint (`POST /api/v1/data/update`)
   - Fuzzy matching engine (rapidfuzz, 80% threshold)
   - Country-aware scoring (boost/de-boost based on address matching)
   - **Universal humanitarian context detection** (ANY sanctioned country + aid keywords)
   - Classification logic (OK/REVIEW/NOK)
   - Localhost deployment only

3. **Streamlit Web Application**
   - File upload (Excel/CSV)
   - Column mapping UI (auto-detect + manual selection)
   - Batch screening workflow with progress indicator
   - Results display (color-coded, sortable, filterable)
   - Summary statistics
   - Excel report download

4. **Comprehensive Screening Reports (Excel Multi-Sheet)**
   - **Sheet 1:** Summary statistics (metadata, counts, data freshness warning)
   - **Sheet 2:** Detailed results (all organizations with full audit trail)
   - **Sheet 3:** Exceptions only (REVIEW + NOK cases, sorted by risk)
   - All required fields for 10-year audit retention

5. **Universal Humanitarian Aid Exception Detection**
   - **Sanctioned country registry** (maintained list from OFAC programs)
   - **Humanitarian keyword detection** (humanitarian, aid, relief, medical, emergency, assistance)
   - **General License mapping** (Syria→GL-21, Iran→GL D-1, Venezuela→GL-41, etc.)
   - **Classification rule:** Sanctioned country match WITHOUT humanitarian keywords = NOK (block)
   - **Classification rule:** Sanctioned country match WITH humanitarian keywords = REVIEW + applicable GL note

6. **Local Deployment Package**
   - Docker container OR Python installer script
   - Single command startup (API + Streamlit)
   - Data persistence (local `data/` directory)
   - No authentication (single-user Phase 1)

**MVP Success Definition:** Carlos can screen 50-100 organizations in <1 hour, download audit-ready report, present to board without modification.

### Growth Features (Phase 1.5: Months 4-6)

**Proceed ONLY if Phase 1 validation successful AND usage validates need:**

1. **Excel Custom Function (UDF via xlwings)**
   - Function: `=OFAC_CHECK(organization_name, [country], [purpose])`
   - Returns: "OK" (green) | "NOK: [details]" (red) | "REVIEW: [context]" (yellow)
   - Calls existing API service (zero code duplication)
   - Local caching per Excel session
   - Excel ribbon with API controls and status indicator

**Decision Gate:** Proceed with Phase 1.5 ONLY if:
- ✅ Phase 1 validation successful (3 grant rounds completed)
- ✅ Carlos identifies need for ad-hoc screening between grant rounds
- ✅ Program officers request quick pre-screening capability
- ✅ Workflow analysis shows value in in-spreadsheet screening

**If usage doesn't validate need → Skip Phase 1.5, focus on Phase 2 commercial validation**

### Vision (Phase 2+: Months 9-12 if commercialized)

**Commercial SaaS Features (Only if Month 12 decision = "Go Commercial"):**

1. **React Frontend Rebuild**
   - Modern, professional UI comparable to enterprise tools
   - Custom branding, responsive design
   - White-label capabilities for NGO partners

2. **Cloud Deployment & SaaS Infrastructure**
   - Hosted API service (AWS/Railway/Heroku)
   - Authentication and API key management
   - Multi-tenant data isolation
   - Usage metering and billing (Stripe integration)

3. **Pricing Tiers**
   - **Tier 1:** $200-300/year (<500 screenings/year)
   - **Tier 2:** $400-600/year (500-1,500 screenings/year)
   - **Pay-per-use:** $0.50-$1.00 per screening
   - **Free tier:** 25 screenings/month for trials

4. **Customer Success**
   - Onboarding tutorials
   - Email support
   - Quarterly compliance webinars
   - Peer knowledge-sharing community

**Future Platform Expansion (Year 2-3 if commercial success proven):**

- Mobile app (iOS/Android) for field officers
- Automated workflows (email notifications, scheduled re-screening)
- Integration with grant management systems (Salesforce, Fluxx)
- Enhanced matching (ML-based, entity resolution)
- Additional compliance lists (UN, EU, UK OFSI)
- Historical screening tracking (flag previously cleared partners now sanctioned)

**Phase 2+ Trigger:** Only pursue if internal validation + peer interest + willingness to pay all confirmed at Month 12 decision gate.

## User Journeys

### Journey 1: Carlos Martinez - Grant Round Screening (Core Happy Path)

**The Scene:** It's Monday morning, and Carlos just received an Excel file from the Africa Program team with 87 organizations applying for Q1 humanitarian grants. In the past, this meant clearing his calendar for an entire afternoon of mind-numbing copy-paste screening on the OFAC website. Coffee in hand, he opens his laptop with a different plan.

**The Process Begins:** Carlos opens his browser to `localhost:8501` where the OFAC screening tool lives. The interface is clean, simple—no intimidating command lines. He clicks "Upload File" and selects the program team's Excel spreadsheet. The tool auto-detects the columns: "Institution" for organization name, "Country" for location, "Project Description" for context. Perfect—no manual mapping needed.

He clicks "Screen Against OFAC Lists" and watches the progress bar: *"Processing 87 organizations... 23 of 87 complete..."* Two minutes later, it's done.

**The Results:** The summary dashboard shows:
- **84 OK** (green) - Clear to proceed
- **2 REVIEW** (yellow) - Manual review needed
- **1 NOK** (red) - Blocked

Carlos clicks "Download Excel Report" and opens the three-sheet workbook. Sheet 1 gives him the summary statistics with the OFAC data version timestamp (updated 4 days ago—well within the 7-day freshness target). Sheet 2 shows all 87 organizations with their screening details. Sheet 3 shows just the 3 exceptions he needs to investigate.

**The Exceptions:**
- **REVIEW Case 1:** "Syrian Development Foundation" - 83% fuzzy match with a Consolidated List entry, but the project description contains "humanitarian medical supplies" and "emergency relief." The tool flagged it: *"Syria + humanitarian context detected. General License 21 may apply - legal review required."* Carlos marks this for Robert (legal counsel).

- **REVIEW Case 2:** "Archdiocèse de Bangui" - 88% match with "Archdiocese of Bangui" (spelling variation). Country matches (CAR), but the tool correctly flags it as REVIEW because it's below the 90% auto-clear threshold. Carlos does a quick spot-check on the OFAC website—confirms it's the same entity and it's NOT on the sanctions list. False positive. He adds a note in the Analyst Notes column: *"Verified via OFAC.gov - same entity, clear. Diacritic spelling variation."*

- **NOK Case:** "Al-Noor Trading Company, Yemen" - 94% match with SDN entity #18422, country matches, program: Yemen-related sanctions. The tool correctly blocked it. Carlos immediately escalates this to Jennifer (Executive Director) and Robert (legal) with the full screening report attached.

**The Resolution:** By 11:30 AM—less than 90 minutes after receiving the file—Carlos has:
- Cleared 84 organizations for grant consideration
- Flagged 2 cases for legal review with full context
- Blocked 1 sanctioned entity from consideration
- Generated a board-ready report with complete audit trail

He saves the Excel report to the compliance shared drive with filename: `Q1_2025_Grant_Screening_20250107_OFAC_v20250103.xlsx` (including the OFAC data version date for audit purposes). He emails the program team: *"Screening complete. 84 organizations cleared, 2 pending legal review, 1 blocked. Report attached. Legal review should take 2-3 days."*

**The Breakthrough Moment:** As Carlos closes his laptop for lunch, he realizes he just saved 5 hours of tedious work. More importantly, the fuzzy matching caught the "Archdiocèse" spelling variation he might have missed manually—exactly the kind of subtle detail that could have become a false negative. He sleeps better knowing the tool has his back.

**What This Journey Reveals - Required Capabilities:**
- File upload with auto-column detection
- Batch screening API with progress indication
- Fuzzy matching engine with configurable thresholds
- Universal humanitarian context detection (Syria, Iran, Venezuela, etc.)
- Country-aware scoring and classification
- Multi-sheet Excel report generation with audit trail fields
- OFAC data version tracking and freshness warnings
- Color-coded results (OK/REVIEW/NOK)
- Analyst notes field for manual annotations
- Summary dashboard with statistics

---

### Journey 2: Carlos Martinez - Exception Management (REVIEW & NOK Cases)

**The Scene:** Three days after the initial screening, Carlos receives a response from Robert (legal counsel) about the two REVIEW cases. One is cleared (Syria humanitarian project qualifies under GL-21), but the other needs deeper investigation. Meanwhile, the NOK case has triggered an urgent board discussion. Carlos needs to manage these exceptions systematically.

**REVIEW Case Deep Dive:**

Robert's email says: *"The Syrian Development Foundation case is interesting. GL-21 should apply for humanitarian medical supplies, but I need to verify their project scope doesn't include any dual-use items. Can you send me the full OFAC match details?"*

Carlos opens the screening report Excel file and navigates to Sheet 3 (Exceptions Only). He finds the Syrian Development Foundation row and sees the full context:
- **Matched Entity Name:** "Syrian Development Agency"
- **Match Score:** 83%
- **Match Type:** Fuzzy
- **OFAC List:** Consolidated List
- **Country Alignment:** Match (Syria)
- **General License Applicable:** Yes - GL-21 (Humanitarian)
- **Risk Level:** Medium
- **OFAC Entity ID:** CONS-8742
- **Program:** Syria Sanctions Program

Carlos copies this information into an email to Robert along with the project description from the original grant application. Robert responds within an hour: *"Verified - this is a false positive. The Consolidated List entity is a government agency, but this applicant is a private NGO with different legal structure. GL-21 applies regardless. Clear to proceed with grant."*

Carlos updates the screening report:
- Changes status from REVIEW → OK
- Adds Analyst Notes: *"Legal review completed 2025-01-10. Robert Thompson confirmed false positive - applicant is private NGO, distinct from CONS-8742 government agency. GL-21 applies. CLEARED."*
- Saves updated report with new filename: `Q1_2025_Grant_Screening_20250107_UPDATED_20250110.xlsx`

**NOK Case Board Escalation:**

The Al-Noor Trading Company case has escalated to an emergency board call. Jennifer (Executive Director) needs Carlos to present the screening evidence to the board and explain why this grant cannot proceed.

Carlos joins the Zoom call with the screening report open. He shares his screen and walks through the evidence:

*"Board members, let me show you why we blocked this application. Our screening tool matched 'Al-Noor Trading Company, Yemen' with SDN entity #18422 at 94% similarity. Here's what makes this a definitive block:*

1. *High match score (94%) - well above our 80% threshold*
2. *Country alignment - both Yemen*
3. *SDN List - not just Consolidated List - which means active sanctions*
4. *OFAC Program: Yemen-related sanctions (Executive Order 13611)*
5. *Entity Type: Commercial/Trading (not humanitarian NGO)*

*I verified this manually on OFAC.gov to confirm - same entity, same location, same business type. Our OFAC data was updated 4 days before screening, so this is current. Proceeding with this grant would expose us to direct OFAC violations."*

Board member asks: *"Could this be a false positive like the Syrian case?"*

Carlos responds: *"Unlikely. The Syrian case was 83% match + different entity types (government vs NGO). This is 94% match + same entity type + same sanctioned program. The risk profile is completely different. I recommend we decline this application immediately and document our due diligence."*

The board votes unanimously to decline the application. Jennifer asks Carlos to draft the rejection letter with compliance reasoning.

**The Documentation Loop:**

Carlos creates a separate compliance memo for the board records:

**To:** Board of Directors, Executive Leadership
**From:** Carlos Martinez, Compliance Officer
**Re:** Q1 2025 Grant Round - OFAC Screening Results & Exception Resolution
**Date:** January 10, 2025

**Summary:**
- Total applications screened: 87 organizations
- Cleared: 85 organizations (97.7%)
- Blocked: 1 organization (Al-Noor Trading Company - SDN match)
- False positives resolved: 1 organization (Syrian Development Foundation - legal review confirmed clear)

**Exception Details:**
[Attaches full screening report with analyst notes]

**Actions Taken:**
- SDN match escalated to board - application declined
- REVIEW cases escalated to legal counsel - 1 cleared, 1 confirmed false positive
- All screening documentation retained for 10-year audit compliance
- OFAC data version: January 3, 2025 (4 days old at time of screening)

**Audit Trail:**
- Original screening report: `Q1_2025_Grant_Screening_20250107_OFAC_v20250103.xlsx`
- Updated report with legal notes: `Q1_2025_Grant_Screening_20250107_UPDATED_20250110.xlsx`
- Legal counsel correspondence: Attached
- Board meeting minutes: January 10, 2025

Carlos saves this memo to the compliance folder and breathes a sigh of relief. When the external auditor reviews this next year, everything is documented, defensible, and traceable.

**The Stress Test Moment:**

Two weeks later, the program team asks: *"Carlos, can you re-screen that Syrian Development Foundation org? We want to make sure nothing has changed before we finalize the grant."*

Carlos opens the screening tool, types "Syrian Development Foundation" into a quick single-organization check (using the `/api/v1/screen/single` endpoint). Results come back in 2 seconds: Still 83% match with same Consolidated List entity, still REVIEW status with GL-21 note. No changes since original screening.

He takes 30 seconds to add a note to the compliance file: *"Re-screened 2025-01-24 - no status change. OFAC data version: January 22, 2025. Original legal review decision stands."*

**What This Journey Reveals - Required Capabilities:**
- Exception-focused view (Sheet 3: REVIEW + NOK only)
- Complete match details for legal/board escalation (entity ID, program, match type, scores)
- Analyst notes field for tracking resolution steps
- Version control / audit trail for updated reports
- Single organization re-screening capability (spot checks)
- OFAC data version timestamps on every report
- Risk level classification (Low/Medium/High)
- General License flagging with specific GL numbers
- Country alignment visibility (Match/Mismatch)
- Ability to explain WHY the tool flagged or cleared an entity
- Documentation-ready format for board presentations
- Traceability: every decision backed by evidence

---

### Journey Requirements Summary

**These two journeys reveal the following core capability areas:**

**1. Batch Screening Workflow**
- File upload (Excel/CSV) with drag-and-drop
- Auto-column detection and manual mapping fallback
- Progress indication for batch processing
- Screening speed: <5 minutes for 100 organizations

**2. Fuzzy Matching & Classification Engine**
- Configurable similarity thresholds (80% default)
- Country-aware scoring (boost/de-boost)
- Match type detection (Exact/Fuzzy/Alias)
- Classification logic (OK/REVIEW/NOK)
- Universal humanitarian context detection (all sanctioned countries)
- General License mapping and flagging

**3. Comprehensive Reporting**
- Multi-sheet Excel reports (Summary, Detailed, Exceptions)
- Audit trail fields: screening date, OFAC version, match scores, entity IDs
- Analyst notes for manual annotations
- Color-coded results visualization
- Summary statistics dashboard
- Exception-only filtering

**4. Exception Management**
- REVIEW and NOK case visibility
- Complete match details for escalation (legal/board)
- Risk level classification
- General License context and notes
- Documentation-ready format for presentations

**5. OFAC Data Management**
- Version tracking with timestamps
- Data freshness warnings (7/14/30 days)
- Manual update controls
- Atomic download/swap to prevent corruption

**6. Audit & Compliance**
- 10-year retention-ready report format
- Version control for updated reports
- Traceability: every decision backed by evidence
- Spot-check validation capability
- Legal review workflow support

**7. Trust & Transparency**
- Match score visibility (percentage)
- Country alignment indicators
- Explainable flagging logic
- Manual verification support (spot-checks against OFAC.gov)
- Professional formatting comparable to commercial tools

## Domain-Specific Requirements

### GovTech Compliance & Regulatory Overview

The OFAC Sanctions Screening Tool operates in the **Government/Regulatory Compliance (GovTech)** domain, serving humanitarian NGOs that must comply with U.S. Treasury OFAC regulations. While the tool itself is internal to ACN-USA (Aid to the Church in Need - U.S. office), it processes screening data for projects that flow through an international organizational structure with 22 national offices worldwide, coordinated by the parent organization in Germany.

**Domain Complexity Factors:**

1. **U.S. Federal Regulatory Compliance:** OFAC sanctions screening is mandatory for U.S.-based organizations making international grants
2. **International Data Handling:** Screening data relates to projects from global partners flowing through German headquarters
3. **Audit & Transparency Requirements:** 10-year documentation retention, external auditor review, board oversight
4. **Potential EU Privacy Considerations:** Parent organization based in Germany may trigger GDPR considerations for shared data
5. **Commercial Expansion Implications:** Phase 2 commercialization introduces procurement, accessibility, and multi-jurisdictional compliance

### Key Domain Concerns

**1. Procurement Compliance (Phase 2 Concern)**

**Current Status:** Not applicable for Phase 1 internal use.

**Phase 2 Consideration:** If commercializing to NGOs with federal funding, customers may need to comply with federal procurement rules when purchasing software/services. This is a research concern for Month 12 commercial decision gate.

**Action:** Defer until commercial viability validated. Research federal procurement requirements (FAR/DFAR basics, GSA Schedule considerations) only if 2+ peer NGOs express purchase interest.

**2. Security & Data Handling**

**Data Classification:**

The tool processes two data categories:

1. **Public Data (No Security Concerns):**
   - OFAC SDN and Consolidated Lists (public domain from OFAC.gov)
   - OFAC entity details, addresses, aliases, programs

2. **Sensitive Organizational Data (Confidentiality Required):**
   - Project applicant organization names and locations
   - Project descriptions and purposes (humanitarian aid context)
   - Grant allocation decisions (which organizations cleared/flagged/blocked)
   - Internal compliance notes and legal review correspondence
   - Information flows through ACN International (Germany) to 22 national offices

**Privacy Considerations:**

- **U.S. Requirements:** No PII of individuals; organizational data only. Standard confidentiality practices sufficient.
- **EU Privacy (GDPR) - Potential Concern:** Parent organization in Germany processes project data that U.S. office screens. While ACN-USA and ACN International are separate legal entities, shared project pipeline data may have GDPR implications.

**Phase 1 Mitigation (Local Deployment):**
- Data never leaves local machine (localhost deployment)
- No cloud storage, no data transmission
- No external database, no backups to external servers
- Screening reports saved to local/network drives only
- **GDPR Impact: Minimized** - local processing, no cross-border data transfer, data minimization principle satisfied

**Phase 2 Cloud Deployment (If Commercializing):**
- Cloud hosting = potential GDPR applicability if European NGOs use the tool
- Multi-tenant architecture requires strong data isolation
- Cross-border data transfers (U.S. cloud hosting EU customers) = GDPR considerations
- **Action Required:** Legal review of GDPR applicability, potential Privacy Shield/Standard Contractual Clauses

**Data Retention Policy:**

- **Audit Requirement:** 10-year retention for compliance documentation
- **Retention Scope:** Screening reports with full audit trail (dates, versions, match scores, analyst notes)
- **Storage Location (Phase 1):** Local compliance shared drive (organization's existing retention infrastructure)
- **Storage Location (Phase 2):** Cloud storage with appropriate retention policies and legal holds

**Security Measures (Phase 1):**

- Local deployment = physical security of user's machine
- No authentication required (single-user localhost)
- OFAC data integrity: atomic download/swap prevents corruption
- No network exposure (localhost only, not accessible remotely)

**Security Measures (Phase 2 - If Commercializing):**

- Authentication and authorization (API keys, user accounts)
- Multi-tenant data isolation (each NGO's data separate)
- Encryption in transit (HTTPS) and at rest
- Audit logging of all screening activities
- Backup and disaster recovery
- Security incident response procedures

**3. Accessibility Standards (Section 508)**

**Phase 1 Decision:** Keep It Simple (KIS).

**Current Status:** No accessibility requirements identified for internal MVP.

**Phase 2 Consideration:** If commercializing to NGOs with federal funding, customers may require Section 508 compliance (WCAG 2.1 AA standard).

**Action:**
- Phase 1: Defer accessibility enhancements
- Streamlit default accessibility is basic but functional
- Phase 2 React rebuild: Design for WCAG 2.1 AA compliance from the start if commercial validation succeeds

**4. Transparency & Audit Requirements**

**Status:** ✅ Core product differentiator - already extensively addressed.

**Requirements Satisfied:**

- **Match Score Transparency:** Every result shows percentage match, match type, country alignment
- **OFAC Version Tracking:** Every report timestamps which OFAC data version used
- **Explainable Decisions:** Clear logic for OK/REVIEW/NOK classifications
- **Audit Trail Completeness:** Screening ID, timestamp, match details, analyst notes, 10-year retention format
- **Traceability:** Every decision backed by evidence and reproducible
- **Board/Auditor Ready:** Professional format, no modification needed for presentation

**No additional requirements needed beyond what's documented in Success Criteria and User Journeys.**

**5. Privacy & Confidential Data Handling**

**Sensitivity Context:**

Screening reports contain confidential information:
- **Pre-Award Confidentiality:** Which organizations are under consideration for grants (not public until awarded)
- **Rejection Reasoning:** Why organizations were flagged or blocked (sensitive, potentially reputational)
- **Internal Deliberations:** Legal review notes, compliance officer annotations, board discussions

**Access Control:**

**Phase 1 (Internal Use):**
- **Primary Access:** Carlos (Compliance Officer / Fractional CFO)
- **Shared With:**
  - Jennifer Williams (Executive Director) - summary and exception cases
  - Robert Thompson (Legal Counsel) - REVIEW and NOK cases requiring interpretation
  - Board of Directors - summary statistics and compliance reports
  - External Auditors - annual review of screening documentation

**Phase 1 Access Management:**
- No technical access controls in tool (localhost, single-user)
- Access managed through organizational file sharing permissions (compliance shared drive)
- Standard organizational confidentiality policies apply

**Phase 2 (If Commercializing):**
- Role-based access control (RBAC): Compliance Officer, Executive, Auditor roles
- Multi-tenant data isolation: Each NGO sees only their screening data
- Audit logging: Track who accessed what screening reports and when
- Data portability: Customers can export their screening history if they leave service

**Privacy Risk Assessment:**

**Phase 1 Risk Level: LOW**
- Local deployment, no network exposure
- Organizational data (not individual PII)
- Standard organizational confidentiality practices sufficient
- Existing file-sharing security infrastructure used

**Phase 2 Risk Level: MEDIUM**
- Cloud hosting introduces data breach risk
- Multi-tenant architecture requires technical isolation controls
- GDPR applicability if European NGOs use service
- Compliance with U.S. privacy expectations (confidentiality, breach notification)

**Mitigation Strategy:**

**Phase 1:**
- Document confidentiality expectations in user training
- Leverage existing organizational data handling policies
- No additional technical controls needed

**Phase 2 (If Commercializing):**
- Legal review of privacy obligations (U.S. + potential GDPR)
- Implement encryption, access controls, audit logging
- Privacy policy and terms of service
- Data processing agreements for European customers (if applicable)
- Breach notification procedures

### Industry Standards & Best Practices

**OFAC Compliance Industry Standards:**

1. **FFIEC BSA/AML Examination Manual:**
   - Financial institution guidance on OFAC compliance programs
   - While ACN-USA is not a financial institution, manual provides best practices for screening frequency, documentation, and audit trails
   - **Application:** 10-year retention, screening all transactions, maintaining current OFAC data

2. **OFAC Best Practices for Sanctions Compliance:**
   - Official guidance from U.S. Treasury
   - Recommends risk-based approach, regular list updates, comprehensive audit trails
   - **Application:** Daily data freshness checks, fuzzy matching for name variations, escalation procedures for matches

3. **NGO Sector Compliance Norms:**
   - Pre-award screening of all grant recipients
   - Documentation of due diligence for board and auditors
   - Legal review of ambiguous cases
   - **Application:** Systematic screening workflow, exception management, legal escalation

**Audit & Compliance Documentation Standards:**

1. **External Audit Requirements:**
   - CPA firms conducting annual audits expect systematic compliance processes
   - Documentation must be complete, contemporaneous, and defensible
   - **Application:** Timestamped reports, version tracking, analyst notes, legal correspondence

2. **Board Oversight Standards:**
   - Nonprofit boards require evidence of risk management and compliance
   - Reports must be understandable to non-technical board members
   - **Application:** Summary statistics, professional formatting, clear explanations

### Required Expertise & Validation

**Domain Expertise Needed:**

1. **OFAC Regulatory Knowledge:**
   - Understanding of SDN vs. Consolidated Lists
   - General License framework and applicability
   - Sanctions program structures and jurisdictional scope
   - **Source:** U.S. Treasury OFAC website, compliance training, legal counsel consultation

2. **Humanitarian Aid Context:**
   - General License 21 (Syria humanitarian aid)
   - General License D-1 (Iran humanitarian aid)
   - General License 41 (Venezuela humanitarian aid)
   - Evolving regulatory landscape for NGO operations in sanctioned countries
   - **Source:** ACN International legal team, sector peer networks, OFAC guidance updates

3. **NGO Compliance Practices:**
   - Grant-making due diligence workflows
   - Audit trail requirements for nonprofit accountability
   - Board reporting expectations
   - **Source:** Carlos's direct experience, external auditor feedback, peer NGO practices

4. **Fuzzy Matching & Data Science (Technical):**
   - String similarity algorithms (rapidfuzz, token_sort_ratio)
   - Threshold calibration for false positive/negative balance
   - Country-aware scoring and entity resolution
   - **Source:** Technical research, testing with real grant data, iterative refinement

**Validation Requirements:**

**Phase 1 (Months 1-6):**

1. **Functional Validation:**
   - Test fuzzy matching with real organization names from past grant rounds
   - Validate classification logic against known OFAC matches
   - Spot-check tool results against manual OFAC.gov searches
   - **Success Criteria:** Zero false negatives, 10-30% acceptable false positive rate

2. **Accuracy Validation:**
   - Quarterly spot-checks: Manually verify sample of screenings
   - Compare tool classifications against legal counsel interpretations
   - Track false positive rate and adjust threshold if >50%
   - **Success Criteria:** 100% alignment with legal counsel on NOK cases

3. **Audit Validation:**
   - External auditor review of screening documentation (Month 6+)
   - Verify reports meet 10-year retention standards
   - Confirm audit trail completeness and traceability
   - **Success Criteria:** Zero audit findings, unconditional approval

4. **User Validation:**
   - Carlos completes 3 real grant rounds using tool
   - Board accepts reports without modification
   - Time savings validated (≥70% reduction)
   - **Success Criteria:** Internal user confidently recommends to peers

**Phase 2 (If Commercializing):**

1. **Peer Validation:**
   - Demo to 2-3 peer compliance officers at other NGOs
   - Solicit feedback on trustworthiness and professionalism
   - Validate willingness to pay $200-500/year
   - **Success Criteria:** At least 1 peer NGO commits to pilot

2. **Legal/Privacy Validation:**
   - Legal review of GDPR applicability for European customers
   - Privacy policy and terms of service review
   - Procurement compliance research (if federal-funded customers)
   - **Success Criteria:** Legal clearance for commercial launch

### Implementation Considerations

**Domain-Driven Design Implications:**

**1. Data Versioning is Non-Negotiable:**

Every screening must be traceable to specific OFAC data version used. This is not a "nice to have" - it's **mandatory for defensibility**.

**Implementation:**
- `version.json` tracks OFAC list update timestamps
- Every screening report embeds OFAC data version
- Atomic download/swap prevents corrupted data states
- Version history retained for 10+ years

**2. Conservative Matching Threshold (Better Safe Than Sorry):**

False negatives are career-ending for compliance officers. False positives are manageable (manual review).

**Implementation:**
- Default 80% similarity threshold (conservative)
- Adjustable if false positive rate >50% after Phase 1 learning
- Country-aware scoring reduces false positives while maintaining safety
- Human-in-the-loop for all REVIEW cases

**3. Explainability Over Black-Box Algorithms:**

Trust comes from transparency, not proprietary "magic."

**Implementation:**
- Match scores visible (percentage)
- Match type documented (Exact/Fuzzy/Alias)
- Country alignment shown (Match/Mismatch)
- Classification logic explainable to board and auditors
- No ML "black boxes" in Phase 1 (keep it simple and defensible)

**4. Humanitarian Context Detection is Domain-Specific:**

Generic compliance tools don't understand that **humanitarian NGOs legitimately operate in sanctioned countries under General Licenses**.

**Implementation:**
- Universal sanctioned country registry (not just Syria)
- Humanitarian keyword detection (not just project titles)
- General License mapping (dynamic, not hardcoded)
- **Differentiator:** This is what makes it "built by practitioners for practitioners"

**5. Privacy by Design (Phase 1: Local, Phase 2: Cloud):**

**Phase 1:**
- Local deployment = minimal privacy risk
- No technical controls needed beyond organizational policies
- Standard confidentiality practices sufficient

**Phase 2:**
- Privacy must be architected from the start (not bolted on later)
- Multi-tenant data isolation
- Encryption, access controls, audit logging
- Legal review before launch (GDPR, procurement, accessibility)

**6. Compliance Drives Release Sequencing:**

**MVP Non-Negotiables (Must work perfectly for Phase 1):**
- OFAC data version tracking
- Fuzzy matching with conservative threshold
- Universal humanitarian context detection
- Audit trail completeness
- Excel report generation

**Can Wait for Phase 2:**
- Advanced UI/UX polish (Streamlit is "good enough")
- Authentication/authorization (single-user Phase 1)
- Automated update scheduling (manual updates acceptable)
- PDF reports (Excel meets requirements)
- Accessibility enhancements (no users requiring it in Phase 1)

**Must Research Before Phase 2:**
- GDPR applicability for European NGO customers
- Federal procurement compliance (if selling to federally-funded NGOs)
- Section 508 accessibility (if target market includes federal grantees)

## API Backend Specific Requirements

### Project-Type Overview

The OFAC Sanctions Screening Tool is fundamentally an **API-first architecture** with a web frontend (Streamlit for Phase 1, potentially React for Phase 2). The core value lives in the API service - the screening engine, fuzzy matching algorithm, OFAC data management, and classification logic. This design enables multiple client applications (Streamlit web app, future Excel UDF, potential commercial integrations) to share a single, consistent backend.

**Architectural Philosophy:**

- **Backend remains stable while frontend evolves** - Can swap Streamlit for React without touching API
- **Single source of truth** - All clients use same matching engine, same OFAC data cache, same version tracking
- **Multiple client support** - Streamlit (primary), Excel UDF (Phase 1.5), commercial dashboard (Phase 2), mobile/CLI (future)
- **Local-first design** - Phase 1 runs entirely on localhost (no cloud dependencies, maximum privacy)
- **Cloud-ready architecture** - API structure prepared for Phase 2 cloud deployment without major refactoring

### Technical Architecture Considerations

**Phase 1: Localhost Deployment**

- **API Service:** FastAPI framework running on `localhost:8000`
- **Web Frontend:** Streamlit application on `localhost:8501`
- **Data Storage:** Local file system (`data/` directory for OFAC lists, `version.json` for tracking)
- **Communication:** HTTP between Streamlit and API (both localhost, no network exposure)
- **Security Model:** Physical machine security only (no auth required for single-user local deployment)

**Phase 2: Cloud Deployment (If Commercializing)**

- **API Service:** Hosted FastAPI on cloud platform (AWS/Railway/Heroku)
- **Frontend:** React rebuild or Streamlit cloud deployment
- **Data Storage:** Cloud database (PostgreSQL/MongoDB) for screening history, S3 for OFAC cache
- **Communication:** HTTPS with authentication (API keys)
- **Security Model:** Multi-tenant data isolation, encryption at rest and in transit, role-based access control

### API Endpoint Specification

**Phase 1 MVP Endpoints:**

**1. Batch Screening Endpoint**
```
POST /api/v1/screen/batch
```

**Purpose:** Screen multiple organizations in a single request (primary workflow)

**Request:**
- **Content-Type:** `multipart/form-data`
- **Body:** File upload (Excel `.xlsx` or CSV `.csv`)
- **Required fields in file:**
  - Organization name (column: "Institution", "Organization", or similar)
  - Country (optional, column: "Country" or similar)
  - Project description (optional, column: "Project Description", "Purpose", or similar)

**Response:**
- **Content-Type:** `application/json`
- **Status codes:**
  - `200 OK` - Screening completed successfully
  - `400 Bad Request` - Invalid file format or missing required columns
  - `500 Internal Server Error` - OFAC data unavailable or processing error
- **Body structure:**
```json
{
  "screening_id": "uuid",
  "screening_date": "2025-01-07T10:30:00Z",
  "ofac_version": "2025-01-03",
  "data_age_days": 4,
  "total_screened": 87,
  "summary": {
    "ok": 84,
    "review": 2,
    "nok": 1
  },
  "results": [
    {
      "row_number": 1,
      "organization": "Example Org",
      "country": "Syria",
      "purpose": "Humanitarian medical supplies",
      "status": "REVIEW",
      "match_found": true,
      "confidence_score": 83,
      "match_type": "Fuzzy",
      "matched_entity": "Example Agency",
      "ofac_list": "Consolidated",
      "country_alignment": "Match",
      "general_license": "GL-21",
      "risk_level": "Medium",
      "ofac_entity_id": "CONS-8742",
      "program": "Syria Sanctions"
    }
  ]
}
```

**Processing:**
- Auto-detect column names ("Institution", "Country", etc.)
- Screen each organization against SDN + Consolidated lists
- Apply fuzzy matching (80% threshold), country-aware scoring, humanitarian context detection
- Return complete results with audit trail fields

---

**2. Single Organization Screening Endpoint**
```
POST /api/v1/screen/single
```

**Purpose:** Screen one organization (for ad-hoc checks, Excel UDF, spot-checking)

**Request:**
- **Content-Type:** `application/json`
- **Body:**
```json
{
  "organization": "Syrian Development Foundation",
  "country": "Syria",
  "purpose": "Humanitarian medical supplies"
}
```

**Response:**
- **Content-Type:** `application/json`
- **Status codes:**
  - `200 OK` - Screening completed
  - `400 Bad Request` - Missing organization name
  - `500 Internal Server Error` - OFAC data unavailable
- **Body structure:** Single result object (same structure as batch results array)

**Processing:**
- Same matching logic as batch endpoint
- Returns immediately (<2 seconds)
- Used by Excel UDF, quick spot-checks, re-screening

---

**3. OFAC Data Version Endpoint**
```
GET /api/v1/data/version
```

**Purpose:** Check OFAC data freshness and version information

**Request:**
- No body required

**Response:**
- **Content-Type:** `application/json`
- **Status codes:**
  - `200 OK` - Version info retrieved
  - `500 Internal Server Error` - Version file corrupted or missing
- **Body structure:**
```json
{
  "sdn_version": "2025-01-03T14:22:00Z",
  "consolidated_version": "2025-01-03T14:22:00Z",
  "age_days": 4,
  "freshness_status": "current",
  "warning_threshold_days": 7,
  "last_check": "2025-01-07T08:00:00Z"
}
```

**Freshness Status:**
- `current`: ≤7 days old (green)
- `warning`: 8-14 days old (yellow)
- `stale`: 15-29 days old (orange)
- `critical`: ≥30 days old (red/block screenings)

---

**4. OFAC Data Update Endpoint**
```
POST /api/v1/data/update
```

**Purpose:** Trigger download and update of OFAC lists

**Request:**
- No body required (or optional `{"force": true}` to bypass freshness check)

**Response:**
- **Content-Type:** `application/json`
- **Status codes:**
  - `200 OK` - Update completed successfully
  - `304 Not Modified` - Data already current, no update needed
  - `500 Internal Server Error` - Download failed, data corrupted
- **Body structure:**
```json
{
  "status": "updated",
  "previous_version": "2024-12-30T10:15:00Z",
  "new_version": "2025-01-03T14:22:00Z",
  "files_updated": ["SDN.CSV", "ALT.CSV", "ADD.CSV", "CONS_PRIM.CSV", "CONS_ALT.CSV", "CONS_ADD.CSV"],
  "download_time_seconds": 12.4
}
```

**Processing:**
- Check HTTP Last-Modified headers from OFAC.gov
- Download all 6 CSV files if new version available
- Atomic swap (download to temp, validate, swap, delete old)
- Update version.json with new timestamps
- Rollback if any file fails validation

---

**Future Endpoints (Deferred to Phase 2 or Phase 3):**

- `GET /api/v1/health` - Health check for monitoring
- `GET /api/v1/screen/history` - Retrieve past screening results (requires database)
- `GET /api/v1/config` - Get API configuration and capabilities
- `POST /api/v1/screen/batch/async` - Asynchronous batch processing with job ID polling

### Authentication & Authorization Model

**Phase 1 (Localhost):**

**No authentication required** for Phase 1 MVP:
- Single-user deployment (Carlos only)
- Localhost-only access (no network exposure)
- Physical machine security sufficient
- API endpoints accessible without credentials

**Rationale:**
- Minimal complexity for internal MVP
- No cloud security concerns (data never leaves machine)
- Standard organizational confidentiality policies apply to screening reports

---

**Phase 2 (Cloud Deployment - If Commercializing):**

**Recommendation: API Key Authentication**

**Why API Keys (not OAuth):**
- **Simpler for NGO users** - No complex OAuth flows, no identity provider setup
- **Adequate security** - Sufficient for organizational API access (not end-user authentication)
- **Industry standard** - Familiar pattern for API services
- **Programmatic access-friendly** - Easy for integrations and SDKs

**API Key Implementation:**

**Generation:**
- Each NGO customer gets one or more API keys on account creation
- Keys are UUID-based, cryptographically secure
- Display once on creation, then hash and store (like passwords)

**Usage:**
- Include in request header: `Authorization: Bearer <api_key>`
- Or query parameter for simple integrations: `?api_key=<key>` (less secure, discourage)

**Rotation:**
- Support multiple active keys per account (for zero-downtime rotation)
- Customer can generate new key, update integrations, then revoke old key
- Automatic expiration optional (e.g., 1-year expiration with renewal reminders)

**Permissions:**
- Per-key permissions for fine-grained access control
- Example: "screening_read_write", "data_version_read", "admin_full_access"
- Enables service accounts (e.g., Excel UDF gets read-only key, admin dashboard gets full access)

**Multi-Tenant Data Isolation:**

- Each API key associated with a specific NGO tenant
- Database queries scoped by tenant ID
- No cross-tenant data access possible
- Screening results, history, configuration all isolated per tenant

**Rate Limiting (tied to authentication):**

- Rate limits enforced per API key
- Tiered based on subscription (Tier 1: 500/year, Tier 2: 1,500/year)
- Monthly or annual quota tracking
- Burst allowances for batch operations (e.g., screen 100 at once within quota)

**High Safety Standards - Security Best Practices:**

1. **Encryption in Transit:** HTTPS only, TLS 1.2+ (no plain HTTP)
2. **Encryption at Rest:** Database encryption for screening history
3. **Key Storage:** Hash API keys with bcrypt/argon2 before storage
4. **Audit Logging:** Log all API calls (tenant, endpoint, timestamp, result code)
5. **Breach Response:** Immediate key revocation capability, customer notification
6. **DDoS Protection:** Cloudflare or similar in front of API
7. **Input Validation:** Strict validation on all inputs (file size limits, column count, organization name length)
8. **Error Handling:** Generic error messages to external users (detailed logs internally only)

### SDK & Programmatic Access

**Phase 1: No SDK Needed**

**Current Clients:**
- Streamlit web app (calls API internally)
- No external integrations

**Confirmed:** SDK deferred for Phase 1.

---

**Phase 2: API Service Model Opportunity**

**Strategic Opportunity:** Offering API access in Phase 2 creates a new revenue stream and competitive advantage.

**API Service Model = Three Product Offerings:**

1. **Streamlit UI Subscription** (primary offering)
   - $200-500/year for web-based screening
   - Target: Non-technical compliance officers

2. **API Access Subscription** (new offering - programmatic integration)
   - Same pricing tiers, but customers use API directly
   - Target: NGOs with existing grant management systems
   - Value prop: "Integrate OFAC screening into your Salesforce/Fluxx workflow"

3. **Hybrid Subscription** (best value)
   - UI + API access combined
   - Slightly higher price ($300-700/year)
   - Target: NGOs wanting both manual screening AND automated integration

**Phase 2 API Access Benefits:**

**For Customers:**
- Integrate screening into grant management platforms (Salesforce, Fluxx, custom systems)
- Automate screening workflows (trigger on grant submission, not manual batch)
- Build custom dashboards and reporting on top of screening API
- Re-screen existing partners automatically on schedule

**For You (Competitive Advantage):**
- **Differentiate from commercial tools** that only offer UI access
- **Higher perceived value** - "Not just a tool, it's an API service"
- **Stickier customers** - API integrations create switching costs
- **Developer-friendly brand** - Appeal to technically sophisticated NGOs

**Phase 2 SDK Considerations:**

If offering API access, SDKs significantly improve developer experience:

**Python SDK** (Priority 1 - Most NGOs use Python for data work)
```python
from ofac_screening import OFACClient

client = OFACClient(api_key="...")
results = client.screen_batch(file="grants_q1.xlsx")
print(results.summary)
```

**JavaScript SDK** (Priority 2 - For web integrations)
```javascript
import { OFACClient } from '@ofac-screening/sdk';
const client = new OFACClient({ apiKey: '...' });
const results = await client.screenBatch(file);
```

**SDK Benefits:**
- Simpler for customers (vs. raw HTTP requests)
- Built-in authentication, error handling, retries
- Type safety (TypeScript definitions, Python type hints)
- Examples and documentation

**SDK Effort:**
- Python SDK: ~2-3 weeks development
- JavaScript SDK: ~2-3 weeks development
- Worth it if 2+ customers request programmatic access

---

**Recommendation:**

**Phase 2 Plan:**
1. Launch with API access as optional add-on to UI subscription
2. Provide API documentation (no SDK initially)
3. **If 2+ customers request programmatic access** → Build Python SDK
4. **If SDK validates demand** → Expand to JavaScript SDK
5. **Phase 3:** Consider open-sourcing SDKs for community growth

**Decision Point:** Revisit SDK priority at Month 12 commercial decision gate based on customer feedback.

### Implementation Considerations

**Technology Stack Decisions:**

**API Framework: FastAPI (Python)**
- **Pros:** Modern, async-friendly, auto-generates OpenAPI docs, type hints
- **Cons:** Slightly more complex than Flask, newer ecosystem
- **Verdict:** Recommended for Phase 1 and Phase 2 (excellent for API-first design)

**Alternative: Flask + Flask-RESTful**
- **Pros:** Mature, simpler, huge ecosystem
- **Cons:** Less modern, manual API documentation
- **Verdict:** Acceptable fallback if FastAPI learning curve is issue

**Data Processing: Pandas + rapidfuzz**
- **Pandas:** Load OFAC CSV files, Excel/CSV uploads
- **rapidfuzz:** Fuzzy string matching (token_sort_ratio method)
- **Confirmed:** No changes needed from conceptual design

**Deployment (Phase 1):**
- **Local Python environment** or **Docker container**
- Single command startup: `docker-compose up` or `python run_api.py`
- No cloud dependencies

**Deployment (Phase 2):**
- **Cloud platform:** Railway (simplest), AWS ECS (enterprise-grade), Heroku (legacy but easy)
- **Database:** PostgreSQL for screening history, user management
- **File storage:** S3 for OFAC data cache
- **CDN/DDoS:** Cloudflare for API protection

**API Documentation:**

**Phase 1:**
- Auto-generated OpenAPI/Swagger docs from FastAPI
- Accessible at `http://localhost:8000/docs`
- Interactive API testing via Swagger UI

**Phase 2:**
- Hosted API documentation (ReadTheDocs or similar)
- Interactive examples with "Try It Out" functionality
- Code snippets for Python, JavaScript, cURL
- Authentication guide with API key setup instructions

**Testing Strategy:**

**Unit Tests:**
- Test matching engine (exact, fuzzy, alias detection)
- Test classification logic (OK/REVIEW/NOK rules)
- Test humanitarian context detection
- Test country-aware scoring

**Integration Tests:**
- Test API endpoints end-to-end
- Test file upload and processing
- Test error scenarios (invalid files, missing data)
- Test OFAC data update mechanism

**Load Testing (Phase 2):**
- Batch screening performance (100 orgs in <5 minutes)
- Concurrent user testing (10 users screening simultaneously)
- Rate limiting enforcement under load

## Project Scoping & Phased Development

### MVP Strategy & Philosophy

**MVP Approach: Problem-Solving MVP**

The OFAC Sanctions Screening Tool follows a **Problem-Solving MVP** strategy focused on solving the core bulk screening problem with minimal features. Phase 1 validates the solution internally through real grant rounds before considering commercial expansion.

**Strategic Rationale:**

- **Fast path to validated learning** - 3 grant rounds (3-6 months) proves or disproves the concept
- **Minimal upfront investment** - Localhost deployment, no cloud costs, single-user simplicity
- **De-risk before commercialization** - Prove internal value before investing in Phase 2 cloud infrastructure
- **Flexibility to pivot** - API-first architecture enables future expansion (Excel UDF, commercial SaaS) without backend rewrite

**Phase 1 Success = Internal validation complete, regardless of commercial decision**

Even if Phase 2 commercialization doesn't happen, the internal tool delivers:
- $2,000-$10,000/year cost avoidance
- 25-35 hours/year time savings
- Zero false negatives (compliance risk mitigation)
- Audit-ready documentation

**Resource Requirements (Phase 1):**

- **Developer:** 1 person (Carlos or contractor)
- **Technical Skills:** Python (FastAPI, Pandas, rapidfuzz), Streamlit basics
- **Time Estimate:** 6-10 weeks development + 3-6 months validation
- **Infrastructure:** Local machine only (no cloud services)

### MVP Feature Set (Phase 1: Months 1-3)

**Core User Journeys Supported:**

1. **Grant Round Screening (Primary Journey)**
   - Upload Excel/CSV file with grant applicant organizations
   - Screen 50-100 organizations in <5 minutes
   - Download comprehensive 3-sheet Excel report
   - Save to compliance shared drive with OFAC version in filename

2. **Exception Management (Secondary Journey)**
   - Review REVIEW/NOK cases in Sheet 3 (Exceptions Only)
   - Escalate to legal counsel with full match details
   - Add analyst notes documenting resolution
   - Re-screen individual organizations for status changes

**Must-Have Capabilities:**

**1. Batch Screening Workflow**
- File upload (Excel `.xlsx` or CSV `.csv`)
- Auto-column detection ("Institution", "Country", "Project Description")
- Manual column mapping fallback (Streamlit UI)
- Progress indicator during processing
- Screening speed: <5 minutes for 100 organizations

**2. Fuzzy Matching & Classification Engine**
- Fuzzy matching with rapidfuzz (token_sort_ratio, 80% threshold)
- Country-aware scoring (boost match if country aligns, de-boost if mismatch)
- Match type detection (Exact/Fuzzy/Alias)
- Classification logic (OK/REVIEW/NOK)
- **Universal humanitarian context detection** (ALL sanctioned countries, not Syria-only)
- General License mapping (GL-21 Syria, GL D-1 Iran, GL-41 Venezuela, etc.)

**3. OFAC Data Management**
- Download SDN + Consolidated lists (6 CSV files total)
- Local cache in `data/` directory
- Version tracking via `version.json`
- Manual update controls ("Check for Updates", "Update Now" buttons)
- Data freshness display with warnings (7/14/30 days thresholds)
- Atomic download/swap (prevent corrupted data states)

**4. Comprehensive Excel Reporting**
- **Sheet 1:** Summary statistics (metadata, counts, data freshness)
- **Sheet 2:** Detailed results (all organizations with full audit trail)
- **Sheet 3:** Exceptions only (REVIEW + NOK, sorted by risk level)
- Audit trail fields: screening ID, date, OFAC version, match scores, entity IDs, programs, General Licenses
- Analyst notes field for manual annotations
- 10-year retention-ready format

**5. API Endpoints (FastAPI Service)**
- `POST /api/v1/screen/batch` - Batch screening (primary workflow)
- `POST /api/v1/screen/single` - Single organization screening (spot checks, re-screening)
- `GET /api/v1/data/version` - Check OFAC data freshness
- `POST /api/v1/data/update` - Trigger OFAC data update

**6. Streamlit Web Application**
- Clean, simple UI (no intimidating command lines)
- File upload with drag-and-drop
- Column mapping interface
- Results display (color-coded: green OK, yellow REVIEW, red NOK)
- Summary statistics dashboard
- Excel report download button
- OFAC data version display with freshness indicator

**7. Local Deployment Package**
- Docker container OR Python installer script
- Single command startup: `docker-compose up` or `python run.py`
- Localhost only (`localhost:8000` API, `localhost:8501` Streamlit)
- No authentication (single-user Phase 1)
- Data persistence via local file system

**MVP Success Definition:**

Carlos can screen an entire grant round (50-100 organizations) in <1 hour, download audit-ready report, present to board without modification, and pass external auditor review.

### Post-MVP Features

**Phase 1.5 (Months 4-6): Conditional Enhancements**

**Proceed ONLY if Phase 1 validation successful AND usage validates need:**

**Excel Custom Function (UDF via xlwings)**
- Function: `=OFAC_CHECK(organization_name, [country], [purpose])`
- Returns: "OK" (green) | "NOK: [details]" (red) | "REVIEW: [context]" (yellow)
- Calls existing API service (zero backend code duplication)
- Excel ribbon with API controls and status

**Decision Gate:** Add Excel UDF ONLY if:
- ✅ Phase 1 validation successful (3 grant rounds completed)
- ✅ Carlos identifies need for ad-hoc screening between grant rounds
- ✅ Program officers request quick pre-screening capability
- ✅ Workflow analysis shows value in in-spreadsheet screening

**If usage doesn't validate need → Skip Phase 1.5, focus on Phase 2 commercial validation**

---

**Phase 2 (Months 9-12+): Commercial SaaS (If Commercializing)**

**Proceed ONLY if Month 12 decision = "Go Commercial"**

**Commercial decision criteria:**
- ✅ All Phase 1 success criteria met convincingly
- ✅ 2-3 peer NGOs express genuine interest after live demo
- ✅ At least 1 peer NGO states explicit willingness to pay $200-500/year
- ✅ Board endorses commercial exploration

**Phase 2 Features:**

**1. Cloud Infrastructure**
- Hosted FastAPI on cloud platform (Railway/AWS/Heroku)
- PostgreSQL database for screening history, user management
- S3 for OFAC data cache
- HTTPS with TLS 1.2+ encryption

**2. Authentication & Multi-Tenancy**
- API key authentication (Bearer token)
- Multi-tenant data isolation (each NGO sees only their data)
- Role-based access control (Compliance Officer, Executive, Auditor roles)
- API key rotation and management

**3. Rate Limiting & Quotas**
- Tiered quotas (Tier 1: 500/year, Tier 2: 1,500/year)
- Monthly/annual tracking
- Overage handling ($0.50/screening or upgrade prompts)

**4. Enhanced Frontend**
- React rebuild (modern, professional UI)
- Custom branding
- Responsive design (tablet/mobile support)
- White-label capabilities for NGO partners

**5. API Service Model (Strategic Opportunity)**
- **Three product offerings:**
  1. Streamlit UI Subscription ($200-500/year)
  2. API Access Subscription (programmatic integration for grant management systems)
  3. Hybrid Subscription (UI + API, $300-700/year)
- API documentation (ReadTheDocs)
- Python SDK (if 2+ customers request programmatic access)
- JavaScript SDK (if SDK demand validates)

**6. Compliance & Security**
- GDPR legal review (if European NGO customers)
- Audit logging (all API calls tracked)
- Encryption at rest and in transit
- Breach response procedures
- Data processing agreements for EU customers

**7. Customer Success**
- Onboarding tutorials
- Email support
- Quarterly compliance webinars
- Peer knowledge-sharing community

---

**Phase 3 (Year 2-3+): Platform Expansion (If Phase 2 Succeeds)**

**Future vision if commercial success proven:**

**1. Additional Integrations**
- Salesforce integration (automated screening on grant submission)
- Fluxx integration (grant management platform)
- Zapier connectors (workflow automation)
- CLI tool (command-line power users)

**2. Enhanced Matching**
- ML-based entity resolution
- Historical screening tracking (flag previously cleared partners now sanctioned)
- Anomaly detection (unusual patterns in screening results)

**3. Multi-List Support**
- UN sanctions lists
- EU sanctions lists
- UK OFSI lists
- Comprehensive global sanctions coverage

**4. Advanced Features**
- Mobile app (iOS/Android) for field officers
- Automated workflows (scheduled re-screening, email notifications)
- Custom reporting templates
- Bulk historical re-screening

**5. Open Source Community**
- Open-source SDKs on GitHub
- Community contributions welcome
- Integration marketplace
- Public roadmap and feature voting

### Deferred or Not Needed

**Features Explicitly Deferred (Not in Phase 1 MVP):**

- ❌ **Automated OFAC data updates** - Manual "Update Now" is sufficient Phase 1 (automation Phase 2)
- ❌ **Screening history database** - Excel reports to file system Phase 1 (database Phase 2)
- ❌ **JSON API input** - File upload only Phase 1 (JSON payloads Phase 2)
- ❌ **Advanced error recovery** - Basic error messages Phase 1 (detailed recovery Phase 2)
- ❌ **PDF reports** - Excel meets requirements (PDF Phase 2+)
- ❌ **Async batch processing** - Synchronous fine for <100 orgs (async Phase 2+)
- ❌ **Accessibility enhancements** - Streamlit defaults Phase 1 (WCAG 2.1 AA Phase 2)

**Features Not Needed (Ever):**

- ❌ **Mobile app** - Not relevant for grant screening workflow (desktop-centric)
- ❌ **Real-time collaboration** - Single-user workflow, no concurrent editing
- ❌ **Advanced ML matching** - Fuzzy matching sufficient and more explainable/trustworthy
- ❌ **Blockchain/immutable audit** - Overkill for compliance documentation

### Risk Mitigation Strategy

**Technical Risks & Mitigation:**

**Risk 1: Universal Humanitarian Context Detection Complexity**
- **Risk:** Implementing General License detection for ALL sanctioned countries (not just Syria) is more complex than Syria-only
- **Mitigation:** Full universal pattern implemented in Phase 1 (confirmed as critical requirement)
- **Fallback:** If implementation proves too complex, start with top 3 countries (Syria, Iran, Venezuela) and add others incrementally
- **Validation:** Test with real grant data from December 2025 round (Syria, Iraq, Lebanon, Sudan, Pakistan visible in screenshots)

**Risk 2: Fuzzy Matching False Positive Rate**
- **Risk:** Too many false positives (>50%) creates "review fatigue" and undermines trust
- **Mitigation:** 
  - Conservative 80% threshold (adjustable based on Phase 1 learning)
  - Country-aware scoring reduces false positives
  - Human-in-the-loop for all REVIEW cases (no auto-clearing)
- **Validation:** Track false positive rate during first 3 grant rounds, adjust threshold if needed
- **Acceptance Criteria:** 10-30% false positive rate acceptable (per success criteria)

**Risk 3: OFAC Data Corruption**
- **Risk:** Partial download or network failure corrupts local OFAC cache
- **Mitigation:**
  - Atomic download/swap (download to temp, validate, then swap)
  - Rollback if any file fails validation
  - Keep last 3 versions as emergency backup
- **Validation:** Test network failure scenarios during development

**Risk 4: Excel Report Compatibility**
- **Risk:** Excel format compatibility issues across different Excel versions or LibreOffice
- **Mitigation:**
  - Use `.xlsx` format (OpenXML standard, widely compatible)
  - Pandas ExcelWriter with openpyxl engine
  - Test on Windows Excel, Mac Excel, LibreOffice Calc
- **Validation:** Validate with Carlos's actual Excel version during development

---

**Market Risks & Validation:**

**Risk 1: Commercial Demand Uncertainty**
- **Risk:** Peer NGOs express polite interest but don't actually subscribe
- **Mitigation:**
  - Build-first, commercialize-later approach (Phase 1 proves internal value first)
  - Month 12 decision gate requires explicit willingness to pay (not just "sounds interesting")
  - Internal tool success = win regardless of commercial outcome
- **Validation:** Live demos at NGO conferences, informal peer conversations, explicit pricing discussions
- **Contingency:** If commercial interest weak, keep as internal tool indefinitely (still $2K-$10K/year value)

**Risk 2: Competitive Response**
- **Risk:** Commercial vendors lower prices or add low-frequency tiers in response
- **Mitigation:**
  - Humanitarian context intelligence differentiator (hard for generic tools to replicate)
  - Transparency/explainability vs. black-box trust
  - API service model (not just UI access)
  - Already validated internal use case (commercial is upside, not necessity)
- **Validation:** Monitor commercial tool pricing during Phase 1 validation period
- **Contingency:** Adjust Phase 2 pricing ($200-500/year has significant margin below commercial $2K-$10K)

**Risk 3: OFAC Policy Changes**
- **Risk:** OFAC changes data formats, API endpoints, or regulatory framework
- **Mitigation:**
  - Design for change: CSV parsing flexible, OFAC endpoint configurable
  - General License mapping externalized (easy to update as regulations evolve)
  - Version tracking enables "screening valid as of [date]" defensibility
- **Validation:** Monitor OFAC website for policy announcements
- **Contingency:** OFAC data format changes require code updates (acceptable maintenance cost)

---

**Resource Risks & Contingency:**

**Risk 1: Development Time Overruns**
- **Risk:** Phase 1 takes longer than 6-10 weeks (learning curve, unexpected complexity)
- **Mitigation:**
  - Start with absolute minimum (4 endpoints + basic Streamlit UI)
  - Skip "nice-to-have" features (analyst notes, data freshness warnings can be added later)
  - Leverage existing Python libraries (Pandas, rapidfuzz, FastAPI, Streamlit)
- **Contingency - Ultra-Lean MVP:** Remove single org re-screening, simplify UI, skip analyst notes field
- **Acceptance:** Even 3-month development still delivers value within single grant round cycle

**Risk 2: Carlos's Limited Availability**
- **Risk:** Carlos wears multiple hats (CFO + Compliance + Grant Review), limited time for tool development/testing
- **Mitigation:**
  - Problem-Solving MVP keeps scope minimal
  - Contractor option if internal capacity insufficient
  - Validation can happen gradually (1 grant round at a time, not urgent deadline)
- **Contingency:** Extend Phase 1 timeline to 6-12 months instead of 3-6 months (still acceptable)

**Risk 3: Technical Skill Gaps**
- **Risk:** Python/FastAPI/Streamlit learning curve slows development
- **Mitigation:**
  - Comprehensive PRD reduces ambiguity (clear requirements)
  - FastAPI auto-generates API docs (reduces documentation burden)
  - Streamlit is beginner-friendly (rapid UI development)
  - Existing conceptual design documents provide technical roadmap
- **Contingency:** Hire contractor for initial implementation, Carlos maintains/operates

**Risk 4: Insufficient Testing Before Launch**
- **Risk:** Bugs or data quality issues discovered during first real grant round
- **Mitigation:**
  - Test with sample data before real grant round (use December 2025 screenshots as test data)
  - Parallel run: Use tool + manual screening for first grant round (validate results match)
  - Spot-check random sample against OFAC.gov manually
- **Contingency:** If serious bugs discovered, revert to manual screening for that round, fix issues before next round

## Functional Requirements

### Organization Screening & Matching

**FR1:** The system can screen a single organization name against OFAC SDN and Consolidated sanctions lists

**FR2:** The system can screen multiple organizations in a single batch operation

**FR3:** The system can detect exact name matches between input organizations and OFAC entities

**FR4:** The system can detect fuzzy name matches using configurable similarity thresholds

**FR5:** The system can detect alias variations of sanctioned entities (organization known by multiple names)

**FR6:** The system can incorporate country information to boost or de-boost match confidence scores

**FR7:** The system can incorporate project purpose/description to inform humanitarian context detection

**FR8:** The system can classify screening results into three categories: OK (clear), REVIEW (manual review needed), or NOK (blocked)

**FR9:** The system can provide confidence scores for all matches (percentage similarity)

**FR10:** The system can identify whether a match comes from SDN List or Consolidated List

**FR11:** The system can screen 100 organizations in less than 5 minutes

**FR12:** The system can screen a single organization in less than 2 seconds

### OFAC Data Management & Freshness

**FR13:** The system can download OFAC SDN list files (SDN.CSV, ALT.CSV, ADD.CSV) from official government sources

**FR14:** The system can download OFAC Consolidated list files (CONS_PRIM.CSV, CONS_ALT.CSV, CONS_ADD.CSV) from official government sources

**FR15:** The system can store OFAC list data in a local cache for offline screening

**FR16:** The system can track the version/date of all OFAC data files currently in use

**FR17:** The system can detect when OFAC data is stale (older than configurable thresholds: 7/14/30 days)

**FR18:** The system can check for OFAC data updates without automatically downloading

**FR19:** The system can update OFAC data on user command

**FR20:** The system can validate downloaded OFAC files before replacing existing data (atomic swap)

**FR21:** The system can rollback to previous OFAC data version if update fails

**FR22:** The system can prevent data corruption during download or update processes

**FR23:** The system can display OFAC data freshness status to users (current/warning/stale/critical)

### Humanitarian Context Intelligence

**FR24:** The system can maintain a registry of sanctioned countries from OFAC programs

**FR25:** The system can detect when an organization operates in a sanctioned country

**FR26:** The system can detect humanitarian aid keywords in project descriptions (humanitarian, aid, relief, medical, emergency, assistance)

**FR27:** The system can combine sanctioned country + humanitarian keywords to identify potential General License applicability

**FR28:** The system can map sanctioned countries to applicable General Licenses (GL-21 for Syria, GL D-1 for Iran, GL-41 for Venezuela, etc.)

**FR29:** The system can flag matches with humanitarian context as REVIEW (not automatic NOK) with General License notes

**FR30:** The system can flag sanctioned country matches WITHOUT humanitarian context as NOK (block)

### Reporting & Audit Trail

**FR31:** The system can generate multi-sheet Excel reports with screening results

**FR32:** The system can include summary statistics in reports (total screened, OK/REVIEW/NOK counts, OFAC data version, screening date)

**FR33:** The system can include detailed results for all screened organizations in reports

**FR34:** The system can include exception-only view (REVIEW + NOK cases only) in reports

**FR35:** The system can include all audit trail fields in reports (screening ID, timestamp, OFAC version, match scores, entity IDs, programs, General Licenses)

**FR36:** The system can provide analyst notes fields for manual annotations and resolution tracking

**FR37:** The system can generate reports that meet 10-year retention compliance requirements

**FR38:** The system can embed OFAC data version timestamps in every report

**FR39:** The system can color-code screening results (green=OK, yellow=REVIEW, red=NOK)

**FR40:** The system can sort exception cases by risk level

**FR41:** The system can display match scores with transparency (percentage, match type, country alignment)

**FR42:** The system can provide downloadable reports in Excel format

### Exception Management & Review Workflow

**FR43:** The system can display complete match details for REVIEW and NOK cases (entity name, match score, match type, OFAC list, country alignment, entity ID, program, risk level)

**FR44:** The system can classify risk levels for matches (Low/Medium/High)

**FR45:** The system can provide General License applicability notes for humanitarian cases

**FR46:** The system can support re-screening of individual organizations for status changes

**FR47:** The system can display country alignment status (Match/Mismatch/N/A)

**FR48:** The system can preserve analyst notes and resolution tracking in updated reports

**FR49:** The system can support version control for updated screening reports

### API Service Layer

**FR50:** The system can expose a batch screening API endpoint that accepts file uploads

**FR51:** The system can expose a single organization screening API endpoint that accepts JSON requests

**FR52:** The system can expose an OFAC data version check API endpoint

**FR53:** The system can expose an OFAC data update trigger API endpoint

**FR54:** The system can auto-generate API documentation from code

**FR55:** The system can return structured JSON responses with screening results

**FR56:** The system can return appropriate HTTP status codes for success/error conditions

**FR57:** The system can validate API request inputs (file format, required fields, data types)

**FR58:** The system can provide detailed error messages for invalid requests

**FR59:** The system can handle file uploads via multipart/form-data

**FR60:** The system can handle JSON payloads for single organization screening

### User Interface & File Processing

**FR61:** The system can accept Excel file uploads (.xlsx format)

**FR62:** The system can accept CSV file uploads (.csv format)

**FR63:** The system can auto-detect column names for organization, country, and project description

**FR64:** The system can provide manual column mapping when auto-detection fails

**FR65:** The system can display progress indicators during batch screening operations

**FR66:** The system can provide file upload via drag-and-drop interface

**FR67:** The system can display screening results with color-coding and filtering

**FR68:** The system can display summary statistics dashboard

**FR69:** The system can provide OFAC data version display with freshness indicators

**FR70:** The system can provide manual controls for checking and updating OFAC data

**FR71:** The system can enable report download via single-click action

### Data Version Control & Traceability

**FR72:** The system can assign unique screening IDs to each screening operation

**FR73:** The system can timestamp all screening operations

**FR74:** The system can link every screening result to the specific OFAC data version used

**FR75:** The system can track OFAC data age in days

**FR76:** The system can maintain version history for OFAC data updates

**FR77:** The system can enable spot-check validation against official OFAC sources

**FR78:** The system can provide complete traceability for all screening decisions

**FR79:** The system can support audit validation of screening methodology and results

## Non-Functional Requirements

### Performance

**NFR1:** Batch screening operations must complete in less than 5 minutes for 100 organizations

**NFR2:** Single organization screening operations must return results in less than 2 seconds

**NFR3:** The system must display progress indicators for operations expected to take more than 3 seconds

**NFR4:** OFAC data version checks must complete in less than 1 second

**NFR5:** File upload and column detection must provide feedback within 2 seconds of user action

**NFR6:** The Streamlit web application must be responsive to user interactions with no perceived lag (<500ms for UI updates)

**NFR7:** Excel report generation and download must complete within 10 seconds for reports containing up to 200 organizations

**NFR8:** OFAC data update downloads must complete within 2 minutes under normal network conditions

### Security & Privacy

**Phase 1 (Local Deployment):**

**NFR9:** The system must run exclusively on localhost with no network exposure beyond the local machine

**NFR10:** The system must not transmit screening data or results to external services

**NFR11:** The system must store all OFAC data and screening reports on the local file system only

**NFR12:** The system must validate all OFAC data downloads for integrity before replacing cached data

**Phase 2 (Cloud Deployment - If Commercializing):**

**NFR13:** All API communications must use HTTPS with TLS 1.2 or higher encryption

**NFR14:** All API keys must be hashed using bcrypt or argon2 before storage

**NFR15:** All screening history data must be encrypted at rest in the database

**NFR16:** The system must enforce multi-tenant data isolation with no possibility of cross-tenant data access

**NFR17:** The system must log all API requests with tenant ID, endpoint, timestamp, and result code for audit purposes

**NFR18:** The system must implement rate limiting per API key to prevent abuse

**NFR19:** The system must validate all user inputs with strict limits (file size ≤10MB, column count ≤50, organization name length ≤500 characters)

**NFR20:** The system must provide generic error messages to external users while logging detailed errors internally only

**NFR21:** The system must support immediate API key revocation in case of security incidents

### Reliability & Accuracy

**NFR22:** The system must achieve zero false negatives (100% recall) for sanctioned entity detection

**NFR23:** The system must maintain acceptable false positive rate (10-30% of REVIEW/NOK flags may be false matches)

**NFR24:** OFAC data updates must use atomic download/swap operations to prevent data corruption

**NFR25:** The system must rollback to previous OFAC data version if any file fails validation during update

**NFR26:** The system must maintain last 3 OFAC data versions as emergency backup

**NFR27:** The system must preserve data integrity across application restarts (local cache survives)

**NFR28:** The system must handle network failures gracefully without corrupting OFAC data cache

**NFR29:** The system must provide clear error messages and recovery instructions for failure scenarios

### Maintainability & Adaptability

**NFR30:** The system must externalize General License mappings to enable updates without code changes

**NFR31:** The system must externalize sanctioned country registry to accommodate regulatory changes

**NFR32:** The system must configure OFAC data source URLs to enable endpoint changes without code modification

**NFR33:** The system must support adjustable fuzzy matching thresholds without requiring redeployment

**NFR34:** The system must use structured logging for debugging and troubleshooting

**NFR35:** The API must auto-generate OpenAPI/Swagger documentation from code

**NFR36:** The system must separate business logic from data access layers to enable technology changes

**NFR37:** The system must use configuration files for environment-specific settings (localhost vs. cloud)

### Usability & Trust

**NFR38:** The system must display match transparency information (percentage scores, match types, country alignment) for all screening results

**NFR39:** The system must embed OFAC data version timestamps in all reports and API responses

**NFR40:** The system must provide data freshness warnings at configurable thresholds (7/14/30 days)

**NFR41:** The system must use color-coding conventions consistently (green=OK, yellow=REVIEW, red=NOK)

**NFR42:** The system must generate reports in widely compatible Excel format (.xlsx) without requiring proprietary software

**NFR43:** The system must enable manual spot-check validation against official OFAC sources

**NFR44:** The system must provide complete audit trails linking every screening decision to supporting evidence

**NFR45:** The Streamlit UI must be intuitive for non-technical compliance officers without requiring training beyond initial setup

**NFR46:** Error messages must be actionable and non-technical (e.g., "Could not connect to OFAC website" vs. "HTTP 503 error")

### Compliance & Audit

**NFR47:** The system must generate reports that meet 10-year retention compliance requirements

**NFR48:** The system must include all required audit trail fields in reports (screening ID, timestamp, OFAC version, match scores, entity IDs, programs, General Licenses, analyst notes)

**NFR49:** The system must maintain version history for OFAC data updates for audit purposes

**NFR50:** The system must provide traceability for every screening decision (what data was used, when, what was the result)

**NFR51:** The system must support contemporaneous documentation (timestamp all operations at time of execution)

**NFR52:** Reports must be formatted for professional presentation to boards and external auditors without modification

**NFR53:** The system must enable verification of screening accuracy through reproducible results
