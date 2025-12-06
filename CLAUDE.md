# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains tools for screening project beneficiaries against OFAC (Office of Foreign Assets Control) sanctions lists, designed for humanitarian NGO operations. The project implements:

1. **Streamlit Web Application**: Bulk screening tool with file upload and exportable reports
2. **Excel Custom Function**: In-cell screening via `=OFAC_CHECK()` formula for spreadsheet workflows

Both tools share a common matching engine and OFAC data layer.

**Current Status**: Planning & Research Phase (no code implementation yet)

## Key Architecture Decisions

### Data Format: CSV Triplets
- **SDN List**: SDN.CSV (18,422 entities), ALT.CSV (20,104 aliases), ADD.CSV (24,170 addresses)
- **Consolidated List**: CONS_PRIM.CSV (443 entities), CONS_ALT.CSV, CONS_ADD.CSV
- **Rationale**: Simpler than XML, faster parsing, adequate for fuzzy matching with country context
- **Storage**: Local cache in `data/` directory with version tracking via `version.json`

### Matching Algorithm
- **Fuzzy matching** using rapidfuzz library with `token_sort_ratio` method
- **Default threshold**: 80% similarity (configurable)
- **Country-aware scoring**: Boost/de-boost matches based on geographic alignment
- **Text normalization**: Lowercase, diacritics removal, punctuation stripping, common suffix removal

### Classification Logic
| Condition | Result | Meaning |
|-----------|--------|---------|
| SDN match >90% | NOK | High confidence block |
| SDN match 80-90% + country match | NOK | Medium confidence with country support |
| SDN match 80-90% + country mismatch | REVIEW | Possible false positive |
| Only CONS match >80% | REVIEW | Non-SDN restricted entity |
| Syria + humanitarian keywords | REVIEW + Note | General License 21 context |
| No match >80% | OK | Clear to proceed |

### Update Strategy
- **Frequency**: Daily automated checks using HTTP Last-Modified headers
- **Download**: User-triggered (no automatic downloads without confirmation)
- **Warning thresholds**: 7 days (yellow), 14 days (orange), 30 days (red/block)
- **Process**: Atomic download and swap to prevent corruption
- **Audit**: Version history maintained in `version.json` for compliance

## Planned Project Structure

```
OFAC/
├── data/                           # OFAC data cache (to be created)
│   ├── sdn/
│   │   ├── SDN.CSV
│   │   ├── ALT.CSV
│   │   └── ADD.CSV
│   ├── cons/
│   │   ├── CONS_PRIM.CSV
│   │   ├── CONS_ALT.CSV
│   │   └── CONS_ADD.CSV
│   └── version.json
├── streamlit_app/                  # Web application (to be created)
│   ├── app.py
│   ├── ofac_matcher.py
│   ├── ofac_updater.py
│   └── requirements.txt
└── excel_addin/                    # Excel custom function (to be created)
    ├── ofac_excel_functions.py
    ├── ofac_matcher.py (shared)
    ├── requirements.txt
    └── OFAC_Checker.xlsm
```

## Core Dependencies

```
pandas                  # Data loading and manipulation
rapidfuzz              # High-performance fuzzy string matching
requests               # HTTP downloads and version checking
streamlit              # Web application framework
xlwings                # Excel integration
python-dateutil        # Date/time parsing
```

**Python Version**: 3.9+ recommended, 3.8+ minimum

## Development Commands

Since implementation hasn't started, there are no build/test commands yet. When development begins:

### Streamlit App
```bash
# Navigate to streamlit app directory
cd streamlit_app

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### Excel Add-in
```bash
# Navigate to excel add-in directory
cd excel_addin

# Install dependencies
pip install -r requirements.txt

# Setup xlwings
python -m xlwings quickstart OFAC_Checker
```

## OFAC Data Sources

**Primary API Endpoint**: `https://sanctionslistservice.ofac.treas.gov/api/download/`

**Available Files**:
- SDN.CSV, ALT.CSV, ADD.CSV, SDN_COMMENTS.CSV
- CONS_PRIM.CSV, CONS_ALT.CSV, CONS_ADD.CSV
- Version detection via Last-Modified HTTP header

**Update Patterns**:
- OFAC updates 2-3 times per week on average (166 updates in 2024, 113 in 2025 through Dec)
- 32% of days had updates in 2024
- No advance notice of updates
- Must check programmatically

## Humanitarian Context Detection

### Syria General License 21
The tool must detect humanitarian aid contexts for Syria and flag them appropriately:
- **Country**: SYRIA (or variants)
- **Purpose keywords**: humanitarian, aid, relief, medical, emergency, assistance
- **Result**: REVIEW status with contextual note about General License 21
- **Important**: Does NOT override NOK classification if entity is on SDN list

### Future General Licenses
Consider adding detection for:
- Iran humanitarian aid (GL D-1)
- Venezuela humanitarian aid (GL 41)
- Other jurisdiction-specific exemptions

## Compliance Requirements

### Risk Profile
**Classification**: Medium-risk organization (humanitarian NGO with global operations)

### Update Requirements
- **Minimum**: Weekly updates
- **Recommended**: Daily automated checks
- **Before critical actions**: Update before high-value or sensitive project approvals

### Documentation for Audits
Maintain 5-year retention of:
1. Update log with timestamps
2. Version history for all OFAC files
3. Screening results with data version used
4. Evidence of update attempts and failures
5. User training records

## Sample Data

- **Location**: `sample-data/Round 2 2025-Project to Fund Response ACN INTL - 20250812 - RAW DATA.csv`
- **Key columns**: Institution (organization name), Country, Project Description, Fund Description
- **Use**: Test data for validating matching logic and UI

## Documentation

All planning and research documents are in `docs/`:

1. **20251205_OFAC_Sanctions_Screening_Tools_Plan.md**
   - Problem statement and requirements
   - OFAC API research and capabilities
   - Solution architecture for both tools
   - Matching logic design
   - Implementation phases

2. **20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md**
   - OFAC data formats (CSV vs XML)
   - SDN vs Consolidated lists comparison
   - File structure specifications
   - Data quality metrics (18,422 SDN records, 443 CONS records)
   - Matching strategy and classification logic

3. **20251206_OFAC_List_Update_Policies_and_Strategy.md**
   - OFAC update frequency analysis
   - Industry compliance requirements
   - Version detection methods
   - Implementation architecture for update service
   - Compliance recommendations

## Known Limitations

1. **Not Legal Advice**: Tool assists compliance but does not make legal determinations
2. **Manual Review Required**: REVIEW classifications require human assessment
3. **English Names Only**: Primarily designed for romanized/English organization names
4. **No Entity Resolution**: Cannot determine if two names refer to same organization
5. **Static Country Mapping**: Regional designations require manual mapping
6. **Windows/Mac Excel Only**: xlwings requires Excel on Windows or Mac (not LibreOffice on Linux)

## BMAD Framework Integration

This project uses the BMAD (Balanced Multi-Agent Development) framework for AI-assisted development workflows. BMAD provides specialized agents, tasks, and workflows.

**Available via**: `.cursor/rules/bmad/` and `.bmad/` directories

**Key agents**:
- @bmad/bmm/agents/dev - Development agent
- @bmad/bmm/agents/architect - Architecture planning
- @bmad/bmm/agents/analyst - Requirements analysis
- @bmad/bmm/agents/quick-flow-solo-dev - Rapid development workflow

**When to use**: Reference BMAD agents for complex development tasks, architecture decisions, or sprint planning

## Implementation Notes

### Shared Code Pattern
Both Streamlit and Excel tools should share:
- `ofac_matcher.py` - Core matching engine (should be identical or symlinked)
- `ofac_updater.py` - Update service (should be identical or symlinked)
- OFAC data cache in `data/` directory

### Performance Considerations
- SDN + ALT combined: ~38,500 names to match against
- Expected screening time: <1 second per organization name
- Batch processing: Use progress bars for files with >100 entries
- Memory usage: ~50-100 MB for full OFAC data in pandas DataFrames

### Security Considerations
- No authentication required for OFAC API (public data)
- Do NOT cache user input data (privacy consideration)
- Validate CSV downloads before swapping (prevent corruption)
- Log all downloads for compliance audit trail

### Error Handling
- Network failures: Retry with exponential backoff
- Partial downloads: Rollback entire update
- Corrupted files: Validate before swap
- Keep last 3 versions as emergency backup

## Testing Strategy

### Unit Tests (to be created)
- Test exact matches
- Test fuzzy matches at various thresholds (75%, 80%, 85%, 90%)
- Test country matching logic
- Test humanitarian context detection
- Test text normalization functions

### Integration Tests (to be created)
- Test Streamlit app end-to-end with sample data
- Test Excel function in real workbook
- Test update mechanisms (mock HTTP responses)
- Test edge cases: special characters, regional names, Syria humanitarian context

### Validation Data
Use sample data in `sample-data/` for testing:
- Known organizations to verify matching
- Edge cases with diacritics and special characters
- Regional country designations (Africa II, Oceania)
- Syria humanitarian aid projects
