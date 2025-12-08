---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - '/home/cgorricho/apps/OFAC/docs/analysis/product-brief-OFAC-20251206.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251205_OFAC_Sanctions_Screening_Tools_Plan.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md'
  - '/home/cgorricho/apps/OFAC/docs/conceptual-design/20251206_OFAC_List_Update_Policies_and_Strategy.md'
workflowType: 'prd'
lastStep: 4
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
