# Problem Statement
Create two tools to screen project beneficiaries against the OFAC sanctions list:
1. A Streamlit web application for bulk screening with file upload
2. An Excel custom function/add-in for in-spreadsheet screening

Both tools need to handle fuzzy matching of organization names, consider country context, account for humanitarian aid general licenses (especially for Syria), and provide detailed match results.

# Current State Analysis
## OFAC API Understanding
### Available Data
* **Primary endpoint**: `https://sanctionslistservice.ofac.treas.gov/api/download/SDN.CSV`
* **SDN.CSV structure**: `entity_id, name, -0-, country, [other fields], remarks`
    * Example: `306,"BANCO NACIONAL DE CUBA",-0- ,"CUBA",-0- ,-0- ,-0- ,-0- ,-0- ,-0- ,-0- ,"a.k.a. 'BNC'."`
* **ADD.CSV structure**: Contains addresses with entity_id references for geographic matching
* **Consolidated list**: Multiple OFAC lists combined (SDN, FSE, Sectoral Sanctions, etc.)
* **Last-Modified header**: Available for version checking (seen: `Wed, 22 Oct 2025 21:34:50 GMT`)
* **No authentication required**: Direct public access via GET requests

### API Limitations
* No direct name search API endpoint - must download full list and search locally
* Redirects to S3 for actual file download
* Files are relatively large (SDN list has thousands of entries)
* Updates are periodic, not real-time

### Sanctions Programs Context
* Syria is heavily sanctioned but has **General License 21** (humanitarian aid exemption)
* Matching logic must consider:
    * Organization name (fuzzy match required due to spelling variations, diacritics)
    * Country/region information
    * Purpose/project type (humanitarian aid vs other activities)
    * Not just binary match - need to provide context for decision-making

## Input Data Structure
Based on `Round 2 2025-Project to Fund Response ACN INTL - 20250812 - RAW DATA.csv`:
* **Key column**: "Institution" (organization name)
* **Supporting columns**: "Country", "Project Description", "Fund Description"
* Countries may be specific ("SYRIA", "TANZANIA") or regional ("Africa II", "Oceania")
* Project descriptions indicate purpose ("Humanitarian Aid", "Construction", "Theological Formation", etc.)

# Proposed Solution
## Project 1: Streamlit Web Application
### Architecture
* **Backend**: Python with Streamlit framework
* **Data management**: 
    * Local cache of OFAC SDN.CSV and ADD.CSV
    * Automatic version checking on app startup
    * Download mechanism with Last-Modified header tracking
* **Matching engine**:
    * FuzzyWuzzy or RapidFuzz library for fuzzy string matching
    * Configurable threshold (suggest 85% as default)
    * Country-aware matching (boost scores for country matches)
    * Humanitarian aid flag detection from project descriptions
* **Output**: 
    * Interactive web table showing results
    * Downloadable CSV/Excel with new "OFAC" column
    * Match details: entity ID, matched name, match score, country, program, remarks

### Key Features
1. **File upload widget**: Accept CSV or Excel files
2. **Column mapping**: Auto-detect or let user specify Institution/Country/Purpose columns
3. **List version display**: Show current OFAC list date and update button
4. **Results table**: Color-coded (green=OK, red=NOK, yellow=humanitarian aid context)
5. **Match details panel**: Expandable rows showing why entity matched
6. **Export functionality**: Download results with all original columns plus OFAC findings

### File Structure
```
/home/cgorricho/apps/OFAC/
├── streamlit_app/
│   ├── app.py (main Streamlit application)
│   ├── ofac_matcher.py (matching logic)
│   ├── ofac_updater.py (download and version management)
│   ├── requirements.txt
│   ├── data/
│   │   ├── SDN.CSV (cached)
│   │   ├── ADD.CSV (cached)
│   │   └── version.json (metadata)
│   └── README.md
```

## Project 2: Excel Custom Function Add-in
### Architecture
* **Technology**: Python with xlwings for Excel integration
* **Alternative**: VBA with Python backend service (for cross-platform compatibility)
* **Deployment**: 
    * Local Python script that Excel calls via xlwings
    * Package as Excel add-in (.xlam for VBA or xlwings-based)
    * Shared data cache with Streamlit app

### Custom Function Signature
```excel
=OFAC_CHECK(organization_name, [country], [purpose])
```
* **Returns**: Status text ("OK", "NOK: [match details]", "REVIEW: humanitarian aid context")
* **Parameters**:
    * `organization_name` (required): String to check
    * `country` (optional): Country or region for contextual matching
    * `purpose` (optional): Project purpose to detect humanitarian aid

### Key Features
1. **Async loading**: Function shows "Checking..." while processing
2. **Caching**: Results cached to avoid repeated API/file checks
3. **Cell formatting**: Conditional formatting applied based on result
4. **Bulk recalculation**: Button to refresh all OFAC checks
5. **Settings panel**: Configure match threshold, update OFAC list

### Implementation Options
**Option A - xlwings (Recommended)**
* Pros: Full Python capabilities, shared code with Streamlit
* Cons: Requires Python installation on user machine
* Distribution: Share Python script + Excel file with xlwings configuration

**Option B - VBA + Web Service**
* Pros: No Python required on user machine, native Excel
* Cons: Need to run local web service, more complex architecture
* Distribution: Excel .xlam file + Python service installer

### File Structure
```
/home/cgorricho/apps/OFAC/
├── excel_addin/
│   ├── ofac_excel_functions.py (xlwings UDFs)
│   ├── ofac_matcher.py (shared with streamlit)
│   ├── install_instructions.md
│   ├── requirements.txt
│   ├── OFAC_Checker.xlsm (Excel file with xlwings setup)
│   └── setup.py (installation script)
```

## Shared Components
### OFAC Matcher Module (ofac_matcher.py)
* `download_ofac_lists()`: Fetch latest SDN and ADD CSVs
* `check_version()`: Compare local vs remote Last-Modified dates
* `parse_ofac_data()`: Load CSVs into searchable format (pandas DataFrame)
* `fuzzy_match(query, threshold)`: Find potential matches with scores
* `check_humanitarian_context()`: Detect if project qualifies for general licenses
* `format_result()`: Generate human-readable match details

### Matching Logic Priorities
1. Exact name match (case-insensitive) → NOK
2. Fuzzy match > 90% → NOK with match details
3. Fuzzy match 80-90% + country match → NOK with match details
4. Fuzzy match 80-90% + country mismatch → REVIEW (possible false positive)
5. Syria + humanitarian aid flag → REVIEW (General License context)
6. No match > 80% → OK

### Version Management
* Store Last-Modified header in local `version.json`
* Check on every app startup (Streamlit) or manual trigger (Excel)
* Display warning if list is > 7 days old
* One-click update button in both interfaces

## Implementation Approach
### Phase 1: Core Matching Engine (Shared)
1. Create `ofac_matcher.py` with download and parsing logic
2. Implement fuzzy matching with configurable thresholds
3. Add humanitarian aid detection logic
4. Create unit tests with sample data

### Phase 2: Streamlit Web App
1. Build basic Streamlit UI with file upload
2. Integrate matcher module
3. Create results display with filtering/sorting
4. Add export functionality
5. Implement version checking UI

### Phase 3: Excel Add-in
1. Set up xlwings environment
2. Create UDF functions
3. Add caching layer
4. Build settings/update interface
5. Write installation documentation

### Phase 4: Testing & Documentation
1. Test with provided sample CSV
2. Test edge cases (special characters, regional names)
3. Create user guides for both tools
4. Document installation procedures

## Technical Considerations
### Fuzzy Matching Strategy
* Use `rapidfuzz` library (faster than FuzzyWuzzy)
* Token sort ratio for handling word order differences
* Normalize: lowercase, remove punctuation, handle diacritics
* Consider splitting on common organization suffixes (S.A., Ltd., Inc.)

### Performance Optimization
* Load OFAC lists once into memory (pandas DataFrame)
* Pre-compute normalized versions for faster matching
* For Excel: cache results per unique organization name
* For Streamlit: batch process with progress bar

### Data Privacy
* All processing happens locally
* No data sent to external services (except OFAC .gov download)
* User data never leaves their machine

### Cross-Platform Compatibility
* Streamlit: Works on Linux/Windows/Mac (current: Linux/Ubuntu)
* Excel add-in: xlwings requires Windows or Mac with Excel installed
* Consider LibreOffice Calc compatibility for Linux users

## Deployment & Distribution
### Streamlit App
* Can run locally: `streamlit run app.py`
* Optional: Deploy to Streamlit Cloud for web access
* Package requirements in virtual environment

### Excel Add-in Distribution
1. **Via xlwings**: 
    * User installs Python + xlwings
    * Runs `xlwings addin install`
    * Opens provided Excel file
2. **Standalone installer**: Create with PyInstaller
3. **Documentation**: Step-by-step guide with screenshots

## Success Criteria
1. Both tools successfully match known OFAC entities
2. Fuzzy matching catches spelling variations
3. No false negatives on exact matches
4. Humanitarian aid context properly flagged for review
5. Version checking works and alerts on outdated data
6. Clear, actionable output for non-technical users
7. Processing time < 30 seconds for 100 entries
