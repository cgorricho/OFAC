# OFAC Data Schemas Analysis and Recommendations

## Executive Summary
This document provides a comprehensive analysis of OFAC sanctions list data formats and structures, with specific recommendations for implementing the data layer for both the Streamlit web application and Excel custom function for screening project beneficiaries.

**Key Recommendation**: Use CSV triplet format (SDN + ALT + ADD, plus optional CONS variants) for both tools due to simplicity, performance, and adequacy for fuzzy name matching with country context.

## Data Source Analysis

### Available Data Formats
OFAC provides sanctions data in three primary format families:

1. **Flat Files (CSV/Fixed-Field)**
   - Simple, fast to parse
   - Multiple related files (triplet structure)
   - Direct pandas compatibility

2. **XML (3 schema levels)**
   - Classic XML (xml.xsd)
   - Enhanced XML (enhanced_xml.xsd)
   - Advanced XML (advanced_xml.xsd)

3. **DAT Specification (Fixed-Field)**
   - Legacy format
   - Not recommended for new implementations

## List Families

### 1. SDN List (Specially Designated Nationals)
The primary OFAC sanctions list. Entities on this list are **blocked** - U.S. persons must generally block their property and interests.

#### SDN Triplet Files

**SDN.CSV (Primary Entities)**
- **Size**: 18,422 records (as of December 2024)
- **Structure**: `entity_id, name, type, program, title, call_sign, vess_type, tonnage, grt, vess_flag, vess_owner, remarks`
- **Entity Types**:
  - Individual: 7,313 records
  - Organizations: ~10,000 records
  - Vessels: 1,380 records
  - Aircraft: 342 records
- **Key Programs** (Top 10):
  - RUSSIA-EO14024: 4,070 entities
  - SDGT (Specially Designated Global Terrorist): 779 entities
  - IRAN: 447 entities
  - GLOMAG (Global Magnitsky): 446 entities
  - SDNTK (Narcotics): 418 entities
  - UKRAINE-EO13662: 487 entities
  - IRAN-EO13902: 407 entities
  - NPWMD (Non-Proliferation of WMD): 338 entities

**Example SDN.CSV Record**:
```csv
306,"BANCO NACIONAL DE CUBA",-0- ,"CUBA",-0- ,-0- ,-0- ,-0- ,-0- ,-0- ,-0- ,"a.k.a. 'BNC'."
```

**ALT.CSV (Alternate Names/Aliases)**
- **Size**: 20,104 records
- **Structure**: `entity_id, alt_id, alt_type, alt_name, alt_remarks`
- **Purpose**: Critical for fuzzy matching - captures spelling variations, transliterations, a.k.a., f.k.a.
- **Alt Types**: "aka" (also known as), "fka" (formerly known as), "nka" (now known as)

**Example ALT.CSV Record**:
```csv
306,220,"aka","NATIONAL BANK OF CUBA",-0-
```

**ADD.CSV (Addresses)**
- **Size**: 24,170 records
- **Structure**: `entity_id, address_id, address, city_state_postal, country, address_remarks`
- **Purpose**: Geographic context for matching, can boost/de-boost scores based on country alignment

**Example ADD.CSV Record**:
```csv
306,199,"Zweierstrasse 35","Zurich CH-8022","Switzerland",-0-
```

**SDN_COMMENTS.CSV (Remarks Overflow)**
- **Purpose**: Contains full remarks when they exceed 1,000 character limit in SDN.CSV
- **Use Case**: Rich context for UI display, not needed for matching logic

### 2. Consolidated Non-SDN Lists (CONS)
Entities on these lists face **targeted restrictions** but are not fully blocked like SDN entities.

#### CONS Triplet Files

**CONS_PRIM.CSV (Consolidated Primary)**
- **Size**: 443 records (significantly smaller than SDN)
- **Includes**:
  - Non-SDN Palestinian Legislative Council (NS-PLC)
  - Foreign Sanctions Evaders (FSE)
  - Sectoral Sanctions Identifications (SSI)
  - Non-SDN Menu-Based Sanctions List (NS-MBS)
  - Non-SDN Chinese Military-Industrial Complex (CMIC)
  - CAPTA List

**Example CONS_PRIM.CSV Record**:
```csv
9639,"HANIYA, Ismail Abdul Salah","individual","NS-PLC",-0- ,-0- ,-0- ,-0- ,-0- ,-0- ,-0- ,"DOB 1962; POB Shati."
```

**CONS_ALT.CSV**
- **Size**: 1,073 records
- Same structure as ALT.CSV, for consolidated list entities

**CONS_ADD.CSV**
- **Size**: 575 records
- Same structure as ADD.CSV, for consolidated list entities

**CONS_COMMENTS.CSV**
- Remarks overflow for consolidated lists

### 3. XML Schema Variants

#### xml.xsd (Classic SDN XML)
**Structure**:
- Root: `<sdnList>` with publication info
- Entry: `<sdnEntry>` containing:
  - `uid`, `firstName`, `lastName`, `title`, `sdnType`
  - `<programList>` - sanctions programs
  - `<akaList>` - alternate names
  - `<addressList>` - addresses
  - `<idList>` - identity documents
  - `<nationalityList>` - citizenships

**Pros**:
- Clean, structured format
- Direct equivalent to CSV triplets
- Well-documented

**Cons**:
- Larger file size
- Slower parsing than CSV
- More complex to integrate with Excel

#### enhanced_xml.xsd (Enhanced SDN XML)
**Additional Features**:
- `<referenceValues>` - Normalized reference data (countries, programs, lists)
- `<featureTypes>` - Structured feature taxonomy
- `<sanctionsData>` with `<publicationInfo>`
- Richer entity metadata (livingStatus, isUsCitizen, isUsPerson)

**Use Cases**:
- Need normalized codes across all lists
- Want consistent taxonomy
- Building multi-list analytics

**Trade-offs**:
- More complex parsing
- Heavier processing
- Overkill for simple name/country matching

#### advanced_xml.xsd (Advanced Normalized XML)
**Structure**:
- Graph-like normalized model
- `<DistinctParties>` - Unique party definitions
- `<ProfileRelationships>` - Entity relationships
- `<SanctionsEntries>` - Linked to parties
- `<ReferenceValueSets>` - Complete reference data
- `<IDRegDocuments>` - Identity documents
- `<Locations>` - Normalized locations

**Use Cases**:
- Complex relationship analysis
- Cross-list entity resolution
- Advanced analytics and reporting
- Building comprehensive sanctions graph

**Trade-offs**:
- Most complex to parse
- Highest processing overhead
- Requires significant development effort
- Unnecessary for current scope

## Data Update Mechanism

### Version Tracking Options

**Option 1: HTTP Last-Modified Header (Recommended)**
- Download endpoint returns `Last-Modified` header
- Example: `Last-Modified: Wed, 22 Oct 2025 21:34:50 GMT`
- Store in local `version.json`
- Check on app startup or manual trigger

**Option 2: Content Hash**
- Compute SHA-256 of downloaded file
- Compare with stored hash
- More reliable but slower

**Option 3: Publication ID (API-based)**
- Use `/changes/latest` endpoint
- Returns publication ID and timestamp
- Requires separate API call

### Update Strategy
1. Check version on app startup (Streamlit) or manual trigger (Excel)
2. Display warning if data is >7 days old
3. Provide "Update Lists" button in both interfaces
4. Download process:
   - Fetch all required CSV files
   - Validate structure
   - Atomic swap (rename temp → production)
   - Update version.json

## Recommendations for Implementation

### Data Layer Architecture

#### Recommended: CSV Triplets
**For Both Streamlit and Excel Function**

**Core Files (Required)**:
1. `SDN.CSV` - Base list, canonical names, programs
2. `ALT.CSV` - Aliases for fuzzy matching
3. `ADD.CSV` - Geographic context

**Extended Files (Strongly Recommended)**:
4. `CONS_PRIM.CSV` - Non-SDN lists
5. `CONS_ALT.CSV` - Non-SDN aliases
6. `CONS_ADD.CSV` - Non-SDN addresses

**Optional Files**:
7. `SDN_COMMENTS.CSV` - Full remarks for display
8. `CONS_COMMENTS.CSV` - Non-SDN full remarks

#### Why CSV Over XML?

**Advantages**:
1. **Performance**: Fast loading with pandas
2. **Simplicity**: Easy to parse, no complex schema handling
3. **Excel Compatibility**: xlwings works seamlessly with CSV/pandas
4. **Adequacy**: Contains all needed fields for fuzzy matching
5. **Size**: Smaller memory footprint
6. **Updates**: Simpler to download and swap

**When to Consider XML**:
- Need normalized codes and reference values
- Building relationship analysis
- Require structured identity documents
- Implementing advanced analytics

For current use case (fuzzy name + country + purpose matching), CSV is optimal.

### Data Storage Structure

```
/home/cgorricho/apps/OFAC/
├── data/
│   ├── sdn/
│   │   ├── SDN.CSV
│   │   ├── ALT.CSV
│   │   ├── ADD.CSV
│   │   └── SDN_COMMENTS.CSV (optional)
│   ├── cons/
│   │   ├── CONS_PRIM.CSV
│   │   ├── CONS_ALT.CSV
│   │   ├── CONS_ADD.CSV
│   │   └── CONS_COMMENTS.CSV (optional)
│   └── version.json
├── streamlit_app/
└── excel_addin/
```

**version.json Structure**:
```json
{
  "sdn": {
    "last_modified": "2025-12-02T12:00:00Z",
    "last_checked": "2025-12-06T17:30:00Z",
    "file_hashes": {
      "SDN.CSV": "sha256:abc123...",
      "ALT.CSV": "sha256:def456...",
      "ADD.CSV": "sha256:ghi789..."
    }
  },
  "cons": {
    "last_modified": "2025-12-02T12:00:00Z",
    "last_checked": "2025-12-06T17:30:00Z",
    "file_hashes": {
      "CONS_PRIM.CSV": "sha256:jkl012...",
      "CONS_ALT.CSV": "sha256:mno345...",
      "CONS_ADD.CSV": "sha256:pqr678..."
    }
  }
}
```

### Matching Strategy

#### Index Building

**SDN Index**:
```python
{
  'entities': [
    {
      'id': 306,
      'canonical_name': 'BANCO NACIONAL DE CUBA',
      'normalized_names': ['banco nacional de cuba', 'national bank of cuba', 'bnc'],
      'type': 'entity',
      'programs': ['CUBA'],
      'countries': ['Switzerland', 'Spain', 'Japan', 'Panama'],
      'remarks': "a.k.a. 'BNC'."
    },
    ...
  ],
  'name_corpus': [...],  # All normalized names for fuzzy search
}
```

**CONS Index**:
- Same structure, separate index
- Different severity classification

#### Matching Logic

**Step 1: Fuzzy Match Against Name Corpus**
- Use `rapidfuzz` library (token_sort_ratio)
- Normalize input: lowercase, remove punctuation, handle diacritics
- Strip common suffixes: S.A., Ltd., Inc., LLC, etc.

**Step 2: Country-Aware Scoring**
- If input country provided:
  - Boost score if entity has matching country in ADD.CSV
  - De-boost if entity has conflicting country
  - Handle regional mappings (e.g., "Africa II" → list of countries)

**Step 3: Classification**

| Condition | Classification | Details |
|-----------|---------------|----------|
| SDN match >90% | NOK | High confidence block |
| SDN match 80-90% + country match | NOK | Medium confidence with country support |
| SDN match 80-90% + country mismatch | REVIEW | Possible false positive |
| Only CONS match >80% | REVIEW | Non-SDN restricted entity |
| Syria + humanitarian keywords | REVIEW + Note | General License context |
| No match >80% | OK | Clear |

**Step 4: Humanitarian Context Detection**
- Input country: SYRIA (or synonyms: Syrian Arab Republic)
- Purpose keywords: humanitarian, aid, relief, medical, emergency, assistance
- Action: Add note "Potential General License 21 (Syria Humanitarian) applicability - requires manual compliance review"
- Does NOT override NOK, only adds context

#### Output Format

**For Streamlit (Excel-compatible)**:
```csv
Fund ID,Institution,Country,OFAC_Status,OFAC_Match_Score,OFAC_Entity_ID,OFAC_Entity_Name,OFAC_Programs,OFAC_Countries,OFAC_Notes
29,"Archidiocèse de Bangui","CENTRAL AFRICAN REPUBLIC","OK",0,,,,,
59,"Archidiocèse Grec-Melkite","SYRIA","REVIEW",0,,,"","","Humanitarian aid context - General License 21 may apply"
```

**For Excel Function**:
```
=OFAC_CHECK("Archidiocèse de Bangui", "CENTRAL AFRICAN REPUBLIC", "Construction")
→ "OK"

=OFAC_CHECK("BANCO NACIONAL DE CUBA", "Cuba", "")
→ "NOK: Match 'BANCO NACIONAL DE CUBA' (SDN #306, Program: CUBA, Score: 100%)"

=OFAC_CHECK("Archidiocèse Grec-Melkite", "Syria", "Humanitarian Aid")
→ "REVIEW: Humanitarian context (Syria General License 21) - manual review required"
```

## Performance Considerations

### CSV Loading Performance
- **SDN triplet**: ~62,700 total records
- **CONS triplet**: ~2,100 total records
- **Load time** (estimated): <2 seconds on modern hardware
- **Memory footprint**: ~50-100 MB in pandas DataFrames

### Fuzzy Matching Performance
- **rapidfuzz**: Highly optimized C++ implementation
- **Strategy**: Pre-compute normalized corpus, use process.extractOne()
- **Expected speed**: <100ms per query for full corpus search
- **Optimization**: Cache results per unique organization name

### Excel Considerations
- **Caching**: Store results per unique (org_name, country, purpose) tuple
- **Lazy loading**: Load data on first function call, keep in memory
- **Update trigger**: Manual refresh button, not automatic per-cell

## Syria Humanitarian Aid Context

### General License 21
OFAC provides General License 21 for humanitarian activities in Syria, but with conditions:

**Permitted**:
- Humanitarian projects by NGOs and international organizations
- Activities that benefit Syrian people

**Prohibited**:
- Transactions with Syrian government entities
- Transactions with SDN individuals/entities
- Transactions that support Syrian government programs

**Implementation in Screening Tool**:
1. Detect Syria context (country = Syria, or Syrian mentions in description)
2. Detect humanitarian keywords in purpose/description
3. If both present: Add "REVIEW" flag with General License note
4. User must still verify counterparty is not SDN and project qualifies
5. Tool aids decision, does not make compliance determination

## Data Quality Observations

### Entity Distribution
- **Individuals**: 39.7% of SDN list (7,313 records)
- **Organizations**: ~54.3% of SDN list
- **Vessels**: 7.5% (1,380 records)
- **Aircraft**: 1.9% (342 records)

### Geographic Distribution (Top Sanctioned Regions)
- Russia/Ukraine: ~4,500 entities
- Iran: ~1,100 entities
- North Korea (DPRK): ~240 entities
- Venezuela: 111 entities
- Belarus: 87 entities

### Program Complexity
- Many entities listed under multiple programs (e.g., "SDGT] [IFSR")
- Requires parsing program field carefully
- Use for display/context, not primary matching

## Next Steps

### Phase 1: Data Loader Implementation
1. Create `ofac_loader.py` module
2. Implement CSV download with version tracking
3. Build SDN and CONS indices in memory
4. Add normalization functions
5. Unit tests with sample data

### Phase 2: Matcher Implementation
1. Create `ofac_matcher.py` module
2. Implement fuzzy matching with rapidfuzz
3. Add country-aware scoring
4. Implement humanitarian context detection
5. Format results for Streamlit and Excel
6. Unit tests with edge cases

### Phase 3: Integration
1. Wire loader + matcher into Streamlit app
2. Create Excel UDF using xlwings
3. Shared data cache
4. Update mechanisms

## Appendix: Sample Data

### Sample SDN Entities (Syria-related)
```csv
3754,"ABU MARZOOK, Mousa Mohammed","individual","SDGT","Political Leader in Amman, Jordan and Damascus, Syria for HAMAS"
6947,"DARKAZANLI, Mamoun","individual","SDGT" (POB: Aleppo, Syria)
10725,"MAKHLUF, Rami","individual","PAARSSR-EO13894" (POB: Syria, Passport: Syria)
```

### Sample File Sizes
- SDN.CSV: ~2.5 MB
- ALT.CSV: ~1.8 MB
- ADD.CSV: ~3.2 MB
- CONS_PRIM.CSV: ~65 KB
- CONS_ALT.CSV: ~95 KB
- CONS_ADD.CSV: ~45 KB

**Total Download Size**: ~7.7 MB (uncompressed CSV)

## Conclusion

The CSV triplet approach (SDN + CONS) provides the optimal balance of:
- **Simplicity**: Easy to implement and maintain
- **Performance**: Fast loading and searching
- **Adequacy**: Contains all necessary data for fuzzy name matching with country context
- **Compatibility**: Works seamlessly with both Streamlit (pandas) and Excel (xlwings)

XML formats should be revisited only if future requirements demand:
- Relationship analysis between entities
- Normalized reference codes across all OFAC programs
- Identity document processing
- Complex multi-list analytics

For the current scope (screen organization names against OFAC with country/purpose context), CSV triplets are the clear choice.
