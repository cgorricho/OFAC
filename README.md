# OFAC Sanctions Screening Tools

**Project Status**: Planning & Research Phase  
**Last Updated**: December 6, 2025

## Project Overview

This project develops two complementary tools for screening project beneficiaries against OFAC (Office of Foreign Assets Control) sanctions lists, specifically designed for humanitarian NGO operations evaluating grant applications and project approvals.

### Tools

1. **Streamlit Web Application**: Bulk screening tool with file upload, visual results, and exportable reports
2. **Excel Custom Function**: In-cell screening via `=OFAC_CHECK()` formula for spreadsheet-based workflows

### Use Case

Screening organizations (primarily religious and humanitarian institutions) against OFAC sanctions lists before approving funding, with special considerations for:
- Fuzzy name matching (handling spelling variations, transliterations, diacritics)
- Country/geographic context
- Humanitarian aid exemptions (e.g., Syria General License 21)
- Clear, actionable results for non-technical users

## Project Goals

### Primary Objectives

1. **Accurate Screening**: Minimize false negatives while managing false positives through intelligent fuzzy matching
2. **Context-Aware Results**: 
   - Classify matches as OK, NOK (blocked), or REVIEW (requires manual assessment)
   - Flag humanitarian aid contexts where general licenses may apply
   - Provide detailed match information (entity ID, programs, countries, match score)
3. **User-Friendly**: Simple interfaces suitable for compliance staff without technical backgrounds
4. **Compliant**: Meet regulatory expectations for sanctions screening programs
5. **Up-to-Date**: Automated mechanisms to keep sanctions data current

### Key Features

- **Fuzzy matching** using rapidfuzz library (token sort ratio)
- **Country-aware scoring** to boost/de-boost matches based on geographic alignment
- **Multiple list support**: SDN (blocked entities) and Consolidated (restricted entities) with different severity classifications
- **Humanitarian context detection**: Special handling for Syria and other sanctioned regions with aid exemptions
- **Automatic updates**: Daily checks for new OFAC data with user-triggered downloads
- **Shared data layer**: Both tools use the same local OFAC data cache and matching engine

## Project Structure

```
/home/cgorricho/apps/OFAC/
├── README.md                          # This file
├── docs/                              # Planning and research documentation
│   ├── 20251205_OFAC_Sanctions_Screening_Tools_Plan.md
│   ├── 20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md
│   ├── 20251206_OFAC_List_Update_Policies_and_Strategy.md
│   ├── SLS-data-schemas/             # OFAC data format specifications
│   ├── ofac sanctions list service - api documentation.docx
│   └── Round 2 2025-Project to Fund Response ACN INTL - 20250812 - RAW DATA.csv (sample data)
├── data/                              # OFAC data cache (to be created)
│   ├── sdn/
│   │   ├── SDN.CSV
│   │   ├── ALT.CSV
│   │   └── ADD.CSV
│   ├── cons/
│   │   ├── CONS_PRIM.CSV
│   │   ├── CONS_ALT.CSV
│   │   └── CONS_ADD.CSV
│   └── version.json
├── streamlit_app/                     # Web application (to be created)
│   ├── app.py
│   ├── ofac_matcher.py
│   ├── ofac_updater.py
│   ├── requirements.txt
│   └── README.md
└── excel_addin/                       # Excel custom function (to be created)
    ├── ofac_excel_functions.py
    ├── ofac_matcher.py (shared)
    ├── requirements.txt
    ├── OFAC_Checker.xlsm
    └── install_instructions.md
```

## Current Progress

### ✅ Completed: Research & Planning Phase

#### 1. Initial Planning Document (Dec 5, 2025)
**File**: `docs/20251205_OFAC_Sanctions_Screening_Tools_Plan.md`

**Contents**:
- Problem statement and requirements analysis
- OFAC API research and capabilities assessment
- Input data structure analysis
- Proposed solution architecture for both tools
- Matching logic design (fuzzy matching with country awareness)
- Technical considerations (performance, privacy, cross-platform)
- Implementation phases and success criteria

**Key Decisions**:
- Use Streamlit for web application (simple, fast development)
- Use xlwings for Excel integration (Python + Excel compatibility)
- Implement shared matching engine for code reuse
- Focus on humanitarian NGO use case (medium-risk profile)

#### 2. Data Schemas Deep Dive (Dec 6, 2025)
**File**: `docs/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md`

**Contents**:
- Comprehensive analysis of OFAC data formats (CSV, XML variants)
- SDN vs Consolidated lists comparison
- File structure specifications and size metrics
- Data quality observations (18,422 SDN records, 443 CONS records as of Dec 2024)
- Matching strategy with classification logic
- Performance estimates and optimization approaches

**Key Findings**:
- **SDN List**: 18,422 entities (primary blocking list)
  - ALT.CSV: 20,104 aliases (critical for fuzzy matching)
  - ADD.CSV: 24,170 addresses (geographic context)
- **Consolidated Lists**: 443 entities (targeted restrictions, not full blocks)
- **Total download size**: ~7.7 MB uncompressed

**Key Decisions**:
- **Use CSV triplets** (SDN + ALT + ADD, plus CONS variants) instead of XML
- Rationale: Simpler, faster, adequate for fuzzy matching needs, Excel-friendly
- Load both SDN and CONS into separate indices with different severity classifications
- Entity distribution: 39.7% individuals, 54.3% organizations, 7.5% vessels

#### 3. Update Policies & Strategy (Dec 6, 2025)
**File**: `docs/20251206_OFAC_List_Update_Policies_and_Strategy.md`

**Contents**:
- OFAC update frequency analysis (historical patterns from 2024-2025)
- Industry compliance requirements and best practices
- Consequences of using outdated lists (enforcement cases, penalties)
- Version detection methods comparison
- Detailed implementation architecture for update service
- Compliance recommendations by organization risk profile

**Key Findings**:
- OFAC updates **2-3 times per week** on average (166 updates in 2024, 113 through Dec 2025)
- 32% of days had updates in 2024
- Updates occur without advance notice
- Monthly checks are "gold standard" for most organizations
- High-risk operations require daily or real-time updates

**Key Decisions**:
- **Daily automated checks** using HTTP Last-Modified headers
- User-triggered manual updates (don't auto-download without confirmation)
- Warning thresholds: 7 days (yellow), 14 days (orange), 30 days (red/block)
- Shared update service (`ofac_updater.py`) used by both Streamlit and Excel
- Atomic download and swap to prevent corruption
- Audit trail with version history for compliance documentation

### 🎯 Next Steps: Implementation Phase

#### Phase 1: Core Matching Engine (Week 1)
**Priority**: High  
**Status**: Not Started

**Tasks**:
- [ ] Create `ofac_loader.py` module
  - [ ] Implement CSV download with Last-Modified version tracking
  - [ ] Build SDN and CONS indices in memory (pandas DataFrames)
  - [ ] Add text normalization functions (lowercase, diacritics, punctuation)
- [ ] Create `ofac_matcher.py` module
  - [ ] Implement fuzzy matching with rapidfuzz (token_sort_ratio)
  - [ ] Add country-aware scoring logic
  - [ ] Implement humanitarian context detection (Syria + keywords)
  - [ ] Format results for both Streamlit and Excel consumption
- [ ] Create `ofac_updater.py` module
  - [ ] Version checking via HTTP HEAD requests
  - [ ] Atomic download and swap mechanism
  - [ ] version.json metadata management
  - [ ] Error handling and rollback
- [ ] Unit tests with sample data
  - [ ] Test exact matches
  - [ ] Test fuzzy matches at various thresholds
  - [ ] Test country matching logic
  - [ ] Test humanitarian context detection

**Deliverables**:
- Working Python modules that can be imported by both applications
- Test suite with >90% code coverage
- Sample screening results for validation

#### Phase 2: Streamlit Web Application (Week 1-2)
**Priority**: High  
**Status**: Not Started

**Tasks**:
- [ ] Create `streamlit_app/app.py`
  - [ ] File upload widget (CSV/Excel)
  - [ ] Column mapping interface (auto-detect Institution, Country, Purpose)
  - [ ] Bulk screening with progress bar
  - [ ] Results table with color coding (green=OK, red=NOK, yellow=REVIEW)
  - [ ] Expandable match details panel
  - [ ] Export to CSV/Excel with OFAC columns added
- [ ] Integrate update UI
  - [ ] Status display (data age, last check time)
  - [ ] "Check for Updates" and "Update Now" buttons
  - [ ] Update notifications and warnings
- [ ] Settings panel
  - [ ] Update frequency configuration
  - [ ] Match threshold adjustment
  - [ ] Warning threshold settings
- [ ] Documentation
  - [ ] User guide
  - [ ] Deployment instructions (local and optional cloud)

**Deliverables**:
- Functional web application
- requirements.txt with dependencies
- README with usage instructions
- Test with provided sample data

#### Phase 3: Excel Custom Function (Week 2)
**Priority**: High  
**Status**: Not Started

**Tasks**:
- [ ] Create `excel_addin/ofac_excel_functions.py`
  - [ ] `OFAC_CHECK(org_name, [country], [purpose])` UDF
  - [ ] Result caching per unique input tuple
  - [ ] Error handling for Excel display
- [ ] Create VBA settings form
  - [ ] Update status display
  - [ ] "Check for Updates" and "Update Now" buttons
  - [ ] Settings (auto-check on open, frequency)
- [ ] Create `OFAC_Checker.xlsm` template
  - [ ] Sample usage worksheet
  - [ ] Settings ribbon/form
  - [ ] Conditional formatting for results
- [ ] xlwings setup and configuration
  - [ ] Installation script
  - [ ] Python environment setup
- [ ] Documentation
  - [ ] Installation guide (step-by-step with screenshots)
  - [ ] Usage examples
  - [ ] Troubleshooting guide

**Deliverables**:
- Working Excel add-in with UDF
- Installation package
- User guide with examples
- Test workbook

#### Phase 4: Testing & Documentation (Week 2-3)
**Priority**: Medium  
**Status**: Not Started

**Tasks**:
- [ ] Integration testing
  - [ ] Test Streamlit app end-to-end
  - [ ] Test Excel function in real workbook
  - [ ] Test update mechanisms
  - [ ] Test with edge cases (special characters, regional names, Syria humanitarian)
- [ ] User acceptance testing
  - [ ] Test with actual project data
  - [ ] Gather feedback on UX
  - [ ] Validate screening accuracy
- [ ] Create comprehensive documentation
  - [ ] Overall project documentation
  - [ ] Compliance best practices guide
  - [ ] Training materials
  - [ ] FAQ document
- [ ] Prepare for deployment
  - [ ] Package applications
  - [ ] Create installation guides
  - [ ] Set up monitoring/logging

**Deliverables**:
- Test reports with validation results
- Complete user documentation
- Training materials
- Deployment packages

## Technical Architecture

### Data Layer

**OFAC Data Sources**:
- **Primary**: SDN.CSV (Specially Designated Nationals - blocked entities)
- **Aliases**: ALT.CSV (alternate names, critical for fuzzy matching)
- **Addresses**: ADD.CSV (geographic information)
- **Consolidated**: CONS_PRIM.CSV, CONS_ALT.CSV, CONS_ADD.CSV (restricted but not blocked)

**Storage Structure**:
```
data/
├── sdn/
│   ├── SDN.CSV          (18,422 entities)
│   ├── ALT.CSV          (20,104 aliases)
│   └── ADD.CSV          (24,170 addresses)
├── cons/
│   ├── CONS_PRIM.CSV    (443 entities)
│   ├── CONS_ALT.CSV     (1,073 aliases)
│   └── CONS_ADD.CSV     (575 addresses)
└── version.json         (metadata and update history)
```

### Matching Engine

**Algorithm**:
1. **Text Normalization**:
   - Lowercase conversion
   - Diacritics removal (é → e, ñ → n)
   - Punctuation stripping
   - Common suffix removal (S.A., Ltd., Inc., LLC)

2. **Fuzzy Matching** (rapidfuzz library):
   - Method: `token_sort_ratio` (handles word order differences)
   - Threshold: 80% minimum (configurable)
   - Corpus: All canonical names + aliases from ALT files

3. **Country-Aware Scoring**:
   - Boost score if entity's ADD.CSV country matches input country
   - De-boost if countries conflict
   - Handle regional inputs (e.g., "Africa II" → country list)

4. **Classification Logic**:

| Condition | Classification | Action |
|-----------|---------------|---------|
| SDN match >90% | NOK | High confidence block |
| SDN match 80-90% + country match | NOK | Medium confidence with country support |
| SDN match 80-90% + country mismatch | REVIEW | Possible false positive |
| Only CONS match >80% | REVIEW | Non-SDN restricted entity |
| Syria + humanitarian keywords | REVIEW + Note | General License context |
| No match >80% | OK | Clear to proceed |

5. **Humanitarian Context Detection**:
   - Country: SYRIA (or variants)
   - Purpose keywords: humanitarian, aid, relief, medical, emergency, assistance
   - Result: Add contextual note about General License 21
   - Does NOT override NOK classification

### Update Mechanism

**Schedule**:
- **Automated**: Daily at 6:00 AM local time
- **Manual**: User-triggered via UI button
- **Method**: HTTP HEAD request to check Last-Modified header

**Process**:
1. Check remote Last-Modified vs local version
2. If newer, download to temporary directory
3. Validate CSV structure
4. Atomic swap (rename temp → production)
5. Update version.json metadata
6. Notify user of changes

**Error Handling**:
- Network failures: Retry with exponential backoff
- Partial downloads: Rollback entire update
- Corrupted files: Validate before swap
- Keep last 3 versions as emergency backup

## Dependencies

### Core Libraries
- **pandas**: Data loading and manipulation
- **rapidfuzz**: High-performance fuzzy string matching
- **requests**: HTTP downloads and version checking
- **streamlit**: Web application framework
- **xlwings**: Excel integration
- **python-dateutil**: Date/time parsing

### Python Version
- Python 3.9+ recommended
- Python 3.8+ minimum

## Compliance Considerations

### Risk Profile
**Classification**: Medium-risk organization
- **Reason**: Humanitarian NGO with global operations including sanctioned regions
- **Not**: Financial institution, exporter, or real-time payment processor

### Update Requirements
- **Minimum frequency**: Weekly updates
- **Recommended**: Daily automated checks
- **Before critical actions**: Update before high-value or sensitive project approvals

### Documentation Requirements
For compliance audits, maintain:
1. Update log with timestamps
2. Version history for all OFAC files  
3. Screening results with data version used
4. Evidence of update attempts and failures
5. User training records

**Retention**: 5 years (standard for sanctions compliance)

### Special Considerations

#### Syria Humanitarian Aid
- Syria is heavily sanctioned but **General License 21** permits humanitarian activities
- Tool flags Syria + humanitarian context as "REVIEW" not automatic "NOK"
- User must verify:
  - Counterparty is not SDN entity
  - Project qualifies under general license terms
  - No Syrian government involvement

#### Other General Licenses
Future enhancements may add detection for:
- Iran humanitarian aid (GL D-1)
- Venezuela humanitarian aid (GL 41)
- Other jurisdiction-specific exemptions

## Known Limitations

1. **Not Legal Advice**: Tool assists compliance, does not make legal determinations
2. **Manual Review Required**: REVIEW classifications require human assessment
3. **English Names Only**: Primarily designed for romanized/English organization names
4. **No Entity Resolution**: Cannot determine if two names refer to same organization
5. **Static Country Mapping**: Regional designations require manual mapping
6. **Windows/Mac Excel Only**: xlwings requires Excel on Windows or Mac (not LibreOffice on Linux)

## Future Enhancements

### Potential Features
- [ ] Multiple language support (Arabic, Cyrillic, Chinese characters)
- [ ] Entity relationship mapping (parent/subsidiary detection)
- [ ] Integration with other sanctions lists (UN, EU, UK)
- [ ] Risk scoring (beyond binary OK/NOK)
- [ ] Batch API for programmatic access
- [ ] Cloud deployment option (Streamlit Cloud)
- [ ] Mobile-friendly interface
- [ ] Real-time update notifications (webhook/push)
- [ ] LibreOffice Calc support for Linux users
- [ ] Advanced analytics and reporting dashboard

### API Integration Opportunities
- Direct OFAC API integration (when/if available)
- Integration with grants management systems
- Connection to CRM platforms (Salesforce, etc.)
- Webhook notifications to Slack/Teams

## Resources

### Official OFAC Resources
- **OFAC Website**: https://ofac.treasury.gov/
- **Sanctions List Search**: https://sanctionssearch.ofac.treas.gov/
- **API Base URL**: https://sanctionslistservice.ofac.treas.gov/
- **Compliance Guidance**: https://ofac.treasury.gov/compliance

### Industry Resources
- FFIEC BSA/AML Examination Manual - OFAC Section
- Financial Crime Academy - OFAC Guidance
- sanctions.io - Best Practices Guide

### Project Documentation
All detailed documentation is in the `docs/` folder:
1. `20251205_OFAC_Sanctions_Screening_Tools_Plan.md` - Initial planning and architecture
2. `20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md` - Data format analysis
3. `20251206_OFAC_List_Update_Policies_and_Strategy.md` - Update mechanism design

## Contributing

This is currently a private project for specific organizational use. 

If you're considering adapting this approach for your organization:
1. Review the planning documents in `docs/`
2. Ensure you understand OFAC compliance requirements for your risk profile
3. Consult with legal counsel on sanctions compliance obligations
4. Consider engaging compliance professionals for validation

## License

[To be determined - likely proprietary for organizational use]

## Contact

For questions about this project, contact the project maintainer through your organization's compliance or IT department.

---

**Disclaimer**: This tool is designed to assist with OFAC sanctions compliance but does not constitute legal advice. Organizations are responsible for their own compliance programs and should consult with legal counsel regarding sanctions obligations. The tool's output should be reviewed by qualified compliance personnel before making final decisions about transactions or relationships.
