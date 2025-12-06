# OFAC BMAD Roadmap - Phase-by-Phase Implementation Guide

**Purpose**: Complete BMAD agent/workflow roadmap for OFAC Sanctions Screening Tools project
**Audience**: Carlos (learning BMAD Method while implementing OFAC project)
**Depth**: Level 3 (Advanced) - Includes underlying principles, when to deviate, pattern recognition
**Created**: December 6, 2025
**Author**: BMad Master Agent

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Project Classification](#project-classification)
3. [Complete Roadmap Overview](#complete-roadmap-overview)
4. [Phase 0: Pre-Implementation](#phase-0-pre-implementation)
5. [Phase 1: Planning (Track 2: BMad Method)](#phase-1-planning-track-2-bmad-method)
6. [Phase 2: Architecture (Level 3)](#phase-2-architecture-level-3)
7. [Phase 3: Story Preparation](#phase-3-story-preparation)
8. [Phase 4: Implementation Loop](#phase-4-implementation-loop)
9. [Phase 5: Testing & Quality](#phase-5-testing--quality)
10. [Checkpoints & Learning Moments](#checkpoints--learning-moments)
11. [Alternative Paths & Deviations](#alternative-paths--deviations)

---

## Executive Summary

### Project: OFAC Sanctions Screening Tools

**Status**: Planning phase complete, ready for implementation

**BMAD Classification**:
- **Track**: BMad Method (Track 2)
- **Level**: 3 (PRD + Architecture required)
- **Type**: Greenfield (no existing code)
- **Complexity**: Medium-High (2 tools, shared code layer, compliance requirements)

**Recommended BMAD Path**:
```
PM: workflow-init (classify) →
PM: create-prd →
PM: validate-prd (optional) →
Architect: create-architecture →
Architect: validate-architecture (optional) →
PM: create-epics-and-stories →
Architect: implementation-readiness →
TEA: framework (parallel) →
SM: sprint-planning →
[Story Loop: SM → DEV → TEA → SM] →
SM: epic-retrospective
```

**Estimated Timeline**: 2-3 weeks implementation (agents accelerate delivery)

---

## Project Classification

### Why This Matters for BMAD Mastery

**BMAD Principle**: The first critical decision is track selection. Getting this wrong means either over-planning (waste) or under-planning (rework).

**Your Learning Goal**: Understand HOW to classify projects, not just this one project.

### OFAC Project Analysis

**Evidence for Track 2 (BMad Method)**:

| Indicator | Evidence from OFAC | Track Signal |
|-----------|-------------------|--------------|
| **Scope complexity** | 2 tools (Streamlit + Excel), shared code layer | Multi-feature = Track 2 |
| **Architecture needed** | Yes - shared modules, update mechanism, data layer | Level 3 = Track 2 required |
| **Clear requirements** | Yes - detailed planning docs exist | Not Track 1 (would be unclear) |
| **Compliance context** | Yes - OFAC regulations, audit trail, 5-year retention | Not Track 1 (too risky) |
| **User variety** | 2 different workflows (bulk vs in-cell) | Multi-persona = Track 2 |
| **Integration complexity** | xlwings, pandas, rapidfuzz, OFAC API | Medium = Track 2 |
| **Story count estimate** | 15-25 stories (3 epics) | Track 2 range (10-50) |

**Classification**: Track 2 (BMad Method), Level 3 (needs architecture)

**Alternative Consideration**: Could this be Quick Flow (Track 1)?
- ❌ **No** - Too many moving parts (2 tools, shared layer)
- ❌ **No** - Architecture decisions required (data format, update strategy, shared code)
- ❌ **No** - Compliance implications (mistakes costly)

**Key Learning**: When multiple interconnected features + architectural decisions + compliance needs = BMad Method (Track 2).

### Pattern Recognition for Future

**Track 1 (Quick Flow) Signals**:
- Keywords: "fix", "add", "update", "bug", "simple"
- Single feature, clear scope
- No architecture decisions
- Low rework cost

**Track 2 (BMad Method) Signals**:
- Keywords: "product", "platform", "system", "dashboard", "integrate"
- Multiple features, interconnected
- Architecture decisions needed
- Medium-High rework cost

**Track 3 (Enterprise) Signals**:
- Keywords: "enterprise", "multi-tenant", "compliance", "audit", "security"
- Enterprise requirements
- Regulatory constraints
- Very high rework cost

**OFAC hits Track 2 signals** (multiple features, architecture, compliance context).

---

## Complete Roadmap Overview

### Visual Roadmap

```
┌─────────────────────────────────────────────────────────────┐
│ PHASE 0: PRE-IMPLEMENTATION (Current State)                 │
│ Status: ✅ COMPLETE                                         │
│ • Planning docs exist (3 comprehensive documents)           │
│ • README.md, CLAUDE.md created                             │
│ • Sample data available                                     │
│ • No code exists (greenfield)                               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 1: PLANNING (Track 2: BMad Method)                    │
│ Agent: PM (John)                                            │
│ Duration: 1-2 days                                          │
│ • workflow-init (classify project)                          │
│ • create-prd (PRD.md with FRs/NFRs)                        │
│ • validate-prd (optional quality gate)                      │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 2: ARCHITECTURE (Level 3)                             │
│ Agent: Architect (Winston)                                  │
│ Duration: 1 day                                             │
│ • create-architecture (Architecture.md)                     │
│ • validate-architecture (optional quality gate)             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 2b: EPIC & STORY CREATION                             │
│ Agent: PM (John)                                            │
│ Duration: 0.5 days                                          │
│ • create-epics-and-stories (epic files + story stubs)      │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 2c: IMPLEMENTATION READINESS                          │
│ Agent: Architect (Winston)                                  │
│ Duration: 0.5 days                                          │
│ • implementation-readiness (validate PRD + Arch alignment)  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 3: STORY PREPARATION                                  │
│ Agent: SM (Bob) + TEA (Murat - parallel)                    │
│ Duration: 0.5 days                                          │
│ • SM: sprint-planning (initialize sprint-status.yaml)      │
│ • TEA: framework (setup test infrastructure) [PARALLEL]    │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 4: IMPLEMENTATION LOOP (Iterative)                    │
│ Agents: SM (Bob) + DEV (Amelia) + TEA (Murat)              │
│ Duration: 1.5-2 weeks (15-25 stories)                       │
│ Per Story:                                                  │
│ • SM: create-story → story-context                         │
│ • DEV: develop-story → code-review                         │
│ • DEV: story-done (updates sprint-status)                  │
│ • TEA: automate (parallel, periodic)                        │
│ Repeat until all stories done                               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 5: TESTING & QUALITY                                  │
│ Agent: TEA (Murat)                                          │
│ Duration: 0.5-1 days                                        │
│ • trace (requirements → tests traceability)                 │
│ • ci (setup CI/CD pipeline)                                 │
│ • nfr-assess (validate performance, security)               │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ PHASE 6: RETROSPECTIVE                                      │
│ Agent: SM (Bob) or BMad Master (party mode)                │
│ Duration: 0.5 days                                          │
│ • epic-retrospective (reflect on what worked)              │
│ • Extract BMAD patterns learned                             │
└─────────────────────────────────────────────────────────────┘
```

### Total Duration Estimate

- **Phase 1 (Planning)**: 1-2 days
- **Phase 2 (Architecture + Epics)**: 1.5 days
- **Phase 3 (Prep)**: 0.5 days
- **Phase 4 (Implementation)**: 1.5-2 weeks
- **Phase 5 (Testing)**: 0.5-1 days
- **Phase 6 (Retrospective)**: 0.5 days

**Total**: 2.5-3 weeks (agents accelerate vs manual)

---

## Phase 0: Pre-Implementation

### Current State Analysis

**What Exists** ✅:
- Planning documents (3 comprehensive files)
- README.md with implementation phases
- CLAUDE.md with technical guidance
- Sample data (Round 2 2025 CSV)
- OFAC schema specifications

**What Does NOT Exist** ❌:
- No code (greenfield project)
- No PRD.md in BMAD format
- No Architecture.md in BMAD format
- No epic files
- No story files

### BMAD Principle: Greenfield vs Brownfield

**Greenfield** (OFAC case):
- No existing code to document
- Skip `*document-project` workflow
- Start directly with planning

**Brownfield** (if OFAC had existing code):
- MUST run `*document-project` first (Analyst or Technical Writer)
- Creates comprehensive documentation before planning changes
- Then proceed to planning

**Why This Matters**:
- Brownfield without docs = AI agents lack context = poor code quality
- Greenfield with docs attempt = waste time documenting nothing

**Key Learning**: Always check "Does code exist?" before choosing first workflow.

### Pre-Implementation Checklist

Before starting BMAD workflows:

- [x] Project idea clear (OFAC screening tools)
- [x] Requirements researched (3 planning docs)
- [x] Sample data available (test cases exist)
- [x] Technical constraints understood (CSV format, OFAC API)
- [ ] BMAD installed (`npx bmad-method@alpha install`)
- [ ] Agents accessible in IDE (Claude Code, Cursor, or Windsurf)
- [ ] Learning journal ready (Document 4: BMAD_Learning_Journal.md)

**Next Step**: Proceed to Phase 1 (Planning)

---

## Phase 1: Planning (Track 2: BMad Method)

### Agent: PM (John) 📋

**Why PM for Planning**:
- **BMAD Role**: PM is the requirements expert, creates PRDs, breaks into epics/stories
- **Alternative**: Principal Engineer (Jordan) for Quick Flow tech-specs - NOT appropriate here (Track 2, not Track 1)
- **Pattern**: Track 2 projects always start with PM, never Principal Engineer

### Step 1.1: Workflow Initialization

**Workflow**: `*workflow-init`

**Agent**: PM (John)

**Purpose**: Classify project, set workflow path, create tracking file

**How to Execute**:
1. Load PM agent in your IDE (`@pm` in Claude Code)
2. Wait for PM's menu to appear
3. Type: `*workflow-init`
4. Follow PM's questions

**What PM Will Ask**:
- Project description (brief summary)
- Greenfield or brownfield? (Greenfield in OFAC case)
- Any existing planning docs? (Yes - you'll point to docs/)

**What PM Will Do**:
1. Analyze your description for complexity keywords
2. Recommend track (should recommend Track 2 for OFAC)
3. Explain all 3 tracks educationally
4. Ask you to confirm track selection
5. Create `.bmad/_cfg/workflow-status.yaml` tracking file
6. Recommend next workflow (`*create-prd`)

**Expected Output**:
```yaml
# workflow-status.yaml
workflow:
  track: "bmad-method"  # Track 2
  level: 3              # Requires architecture
  type: "greenfield"
  phase: "planning"
  next_workflow: "create-prd"
  next_agent: "pm"
```

**Learning Checkpoint #1**: Understanding Track Classification

**What to Observe**:
- How does PM analyze complexity keywords?
- What questions help distinguish Track 1 vs Track 2?
- Why does PM recommend Track 2 for OFAC?

**Document in Learning Journal**:
- PM's classification rationale
- Questions PM asked
- How you'd classify future projects

**Time Estimate**: 30 minutes

---

### Step 1.2: PRD Creation

**Workflow**: `*create-prd`

**Agent**: PM (John)

**Purpose**: Create Product Requirements Document with Functional Requirements (FRs) and Non-Functional Requirements (NFRs)

**How to Execute**:
1. PM agent already loaded
2. Type: `*create-prd`
3. Answer PM's elicitation questions

**What PM Will Ask**:
- **Vision**: What problem does this solve? (OFAC compliance for humanitarian NGOs)
- **Users**: Who uses this? (Compliance staff, program managers)
- **Use Cases**: How will they use it? (Bulk screening, in-spreadsheet checking)
- **Functional Requirements**: What features? (File upload, fuzzy matching, update mechanism, etc.)
- **Non-Functional Requirements**: Performance? Security? (Match speed, data privacy, update frequency)
- **Success Criteria**: How do we know it works? (Accuracy, speed, user adoption)

**Existing Material to Reference**:
- Point PM to `/docs/20251205_OFAC_Sanctions_Screening_Tools_Plan.md`
- Point PM to `/docs/20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md`
- Point PM to README.md

**What PM Will Do**:
1. Read your existing planning docs
2. Ask clarifying questions to fill gaps
3. Draft PRD.md with structure:
   - Vision & Goals
   - User Personas
   - Use Cases
   - Functional Requirements (FRs)
   - Non-Functional Requirements (NFRs)
   - Success Metrics
   - Out of Scope
4. Save to `/docs/PRD.md` (or similar location)
5. Update workflow-status.yaml

**Expected PRD Structure**:
```markdown
# PRD: OFAC Sanctions Screening Tools

## Vision
[Problem statement, solution overview]

## User Personas
- Compliance Officer (bulk screening)
- Program Manager (spreadsheet workflow)

## Use Cases
- UC1: Bulk screen 100 organizations from CSV
- UC2: Check single organization in Excel
- UC3: Update OFAC lists weekly

## Functional Requirements
- FR1: Upload CSV/Excel file for screening
- FR2: Fuzzy match organization names (80% threshold)
- FR3: Country-aware scoring
- FR4: Syria humanitarian context detection
- FR5: Daily automated update checks
- FR6: Export results with match details
- FR7: Excel UDF function =OFAC_CHECK()
- ... (15-20 FRs total)

## Non-Functional Requirements
- NFR1: Match speed <1 second per organization
- NFR2: Memory usage <100 MB
- NFR3: Update check <2 seconds
- NFR4: Data privacy (local processing only)
- NFR5: 5-year audit trail retention
- ... (8-12 NFRs total)

## Success Metrics
- Accuracy: 0% false negatives on known OFAC entities
- Performance: <1 second match time (95th percentile)
- Adoption: >80% of target users within 30 days

## Out of Scope
- Multi-language support (Phase 2)
- UN/EU sanctions lists (Phase 2)
- API for programmatic access (Phase 2)
```

**BMAD Principle Deep Dive**: Why PRD Before Architecture?

**The Pattern**:
- ❌ **Anti-pattern**: Start coding, figure out requirements later
- ❌ **Anti-pattern**: Create architecture before knowing requirements
- ✅ **BMAD pattern**: Requirements (PRD) → Architecture → Implementation

**Rationale**:
- Architecture answers "How do we build this?"
- Can't answer "how" without knowing "what" (requirements)
- PRD provides "what", Architecture provides "how"

**Real-World Example**:
- Imagine Architect designs data layer before PM defines requirements
- PM later adds: "Oh, we need to support Excel offline mode"
- Architect's design assumed always-online
- Result: Complete redesign (costly rework)

**Key Learning**: Sequential dependencies matter. Requirements unlock architecture, architecture unlocks implementation.

**Learning Checkpoint #2**: PRD as AI Agent Context

**What to Observe**:
- How does PM transform your existing docs into BMAD PRD format?
- What gaps does PM identify in your planning?
- How detailed are FRs and NFRs?

**Document in Learning Journal**:
- Differences between your docs and BMAD PRD format
- PM's elicitation questions (what you hadn't considered)
- How FRs/NFRs will help downstream agents

**Time Estimate**: 2-4 hours (with existing research, faster)

---

### Step 1.3: PRD Validation (OPTIONAL)

**Workflow**: `*validate-prd`

**Agent**: PM (John)

**Purpose**: Independent review of PRD for completeness and quality

**When to Use**:
- **Learning mode** ← **RECOMMENDED FOR CARLOS**
- Critical projects (high rework cost)
- Unfamiliar domain
- Before phase transition

**When to Skip**:
- Time pressure
- Confident in PRD quality
- Low-stakes project

**How to Execute**:
1. PM agent already loaded
2. Type: `*validate-prd`
3. PM performs independent review

**What PM Will Check**:
- ✅ All FRs have clear acceptance criteria
- ✅ NFRs are measurable (not vague)
- ✅ Success metrics defined
- ✅ User personas complete
- ✅ Out of scope explicit
- ✅ No contradictions between FRs
- ✅ Testability (can requirements be validated?)

**Expected Output**:
- Validation report with issues found (if any)
- Recommendations for improvement
- "Approved" or "Needs revision" verdict

**BMAD Principle**: Validation as Learning Accelerator

**Why Validate During Learning**:
- See what "good" looks like (PM shows quality standards)
- Calibrate your judgment (learn to self-validate later)
- Prevent downstream rework (Architecture uses PRD as input)

**Pattern for Mastery**:
1. **First 3 projects**: Always validate (learn standards)
2. **Next 5 projects**: Validate if uncertain (calibrate judgment)
3. **After 8 projects**: Validate only critical docs (confident)

**Key Learning**: Validation workflows are teaching tools, not bureaucracy.

**Learning Checkpoint #3**: What Makes a Quality PRD?

**What to Observe**:
- PM's validation criteria (completeness, clarity, testability)
- Issues PM identifies (gaps you missed)
- How PM explains quality standards

**Document in Learning Journal**:
- PM's quality checklist
- Common PRD mistakes to avoid
- Your calibrated quality bar for future PRDs

**Time Estimate**: 1 hour

---

## Phase 2: Architecture (Level 3)

### Agent: Architect (Winston) 🏗️

**Why Architect for Solutioning**:
- **BMAD Role**: Architect is the system design expert, creates technical architecture
- **Alternative**: Skip architecture (Level 0-2 only) - NOT appropriate here (OFAC is Level 3)
- **Pattern**: Level 3-4 projects always include architecture phase

### Step 2.1: Architecture Design

**Workflow**: `*create-architecture`

**Agent**: Architect (Winston)

**Purpose**: Design system architecture with technical decisions, component diagrams, data flow

**How to Execute**:
1. Load Architect agent in your IDE (`@architect`)
2. Type: `*create-architecture`
3. Point Architect to PRD.md created in Phase 1
4. Answer Architect's design questions

**What Architect Will Ask**:
- **Inputs**: Where is PRD.md? (provide path)
- **Scale targets**: Expected load? (100s of orgs per screening, not thousands)
- **Performance requirements**: Latency tolerance? (Referenced from NFRs: <1 second)
- **Data residency**: Where is data stored? (Local only, privacy requirement)
- **Integration points**: External systems? (OFAC API for downloads)
- **Technology constraints**: Mandated tech stack? (Python, Streamlit, xlwings from CLAUDE.md)
- **Deployment model**: How is it deployed? (Local Streamlit, Excel add-in distributed)

**What Architect Will Do**:
1. Read PRD.md (understand requirements)
2. Ask design questions (clarify technical constraints)
3. Propose architectural approach
4. Create Architecture.md with:
   - System Overview (high-level design)
   - Component Diagram (modules and relationships)
   - Data Flow Diagram (how data moves)
   - Technology Stack (libraries, frameworks)
   - Key Technical Decisions (with rationale)
   - API Contracts (if applicable)
   - Data Models (schemas, structures)
   - Deployment Architecture (how it runs)
   - Security Considerations
   - Performance Considerations
   - Risks and Mitigations
5. Save to `/docs/Architecture.md`
6. Update workflow-status.yaml

**Expected Architecture Content** (OFAC-specific):

**System Overview**:
- 2 user-facing applications (Streamlit, Excel)
- Shared core layer (ofac_loader, ofac_matcher, ofac_updater)
- Local data cache (CSV files)
- External dependency (OFAC API for updates)

**Component Diagram**:
```
┌─────────────────┐     ┌──────────────────┐
│ Streamlit App   │     │ Excel Add-in     │
│ (app.py)        │     │ (xlwings UDF)    │
└────────┬────────┘     └────────┬─────────┘
         │                       │
         └───────────┬───────────┘
                     ↓
         ┌───────────────────────┐
         │ Shared Core Layer     │
         │ • ofac_matcher.py     │
         │ • ofac_loader.py      │
         │ • ofac_updater.py     │
         └───────────┬───────────┘
                     ↓
         ┌───────────────────────┐
         │ Data Cache            │
         │ • SDN.CSV, ALT.CSV    │
         │ • CONS_PRIM.CSV, etc  │
         │ • version.json        │
         └───────────┬───────────┘
                     ↓
         ┌───────────────────────┐
         │ OFAC API              │
         │ (sanctionslistservice)│
         └───────────────────────┘
```

**Key Technical Decisions**:
- **Decision 1**: CSV over XML for data format
  - **Rationale**: Simpler parsing, faster, adequate for fuzzy matching (from existing research)
  - **Trade-offs**: Less structured than XML, but performance and simplicity win
- **Decision 2**: Shared Python module over duplication
  - **Rationale**: Single source of truth, easier maintenance, consistent behavior
  - **Trade-offs**: Both apps must use Python (acceptable - Streamlit is Python, xlwings supports Python)
- **Decision 3**: Local data cache over API calls
  - **Rationale**: Performance (no network latency per match), privacy (data stays local)
  - **Trade-offs**: Must manage updates, stale data risk (mitigated with daily checks)
- **Decision 4**: Atomic file swap for updates
  - **Rationale**: Prevent corruption if download fails mid-stream
  - **Trade-offs**: Requires temp directory and rename logic (low complexity)

**Data Models**:
```python
# Entity Index (in-memory)
{
  'entities': [
    {
      'id': 306,
      'canonical_name': 'BANCO NACIONAL DE CUBA',
      'normalized_names': ['banco nacional de cuba', 'national bank of cuba', 'bnc'],
      'type': 'entity',
      'programs': ['CUBA'],
      'countries': ['Switzerland', 'Spain'],
      'remarks': "a.k.a. 'BNC'."
    }
  ]
}

# Version Metadata (version.json)
{
  "last_checked": "2025-12-06T06:00:00Z",
  "files": {
    "SDN.CSV": {
      "last_modified": "2025-12-03T10:02:13Z",
      "size_bytes": 2621440,
      "hash_sha256": "abc123..."
    }
  }
}
```

**BMAD Principle Deep Dive**: Architecture as AI Agent Blueprint

**Why Architecture Matters for AI**:
- **Without Architecture**: DEV agent makes ad-hoc decisions per story
  - Story 1: DEV puts matching in streamlit_app/
  - Story 2: DEV realizes Excel needs same logic, duplicates code
  - Story 3: Bug found, must fix in 2 places
  - Result: Tech debt, inconsistency
- **With Architecture**: DEV agent follows blueprint
  - Architecture specifies: "Shared core layer in /shared/"
  - Story 1: DEV implements matcher in shared/ofac_matcher.py
  - Story 2: DEV imports shared module into Excel add-in
  - Story 3: Bug fix in one place
  - Result: Clean, maintainable code

**Key Learning**: Architecture is the AI's instruction manual. Without it, AI improvises (dangerous).

**Learning Checkpoint #4**: Architecture as Decision Documentation

**What to Observe**:
- How does Architect transform PRD requirements into technical decisions?
- What questions does Architect ask that PM didn't?
- How are trade-offs explicitly documented?

**Document in Learning Journal**:
- Architect's design questions
- Key technical decisions and rationale
- How Architecture.md will guide DEV agents

**Time Estimate**: 3-5 hours

---

### Step 2.2: Architecture Validation (OPTIONAL)

**Workflow**: `*validate-architecture`

**Agent**: Architect (Winston)

**Purpose**: Independent review of Architecture.md for completeness, soundness, and alignment with PRD

**When to Use**: Same criteria as PRD validation (learning mode ← **RECOMMENDED FOR CARLOS**)

**What Architect Will Check**:
- ✅ All PRD requirements have architectural support
- ✅ Technology choices justified
- ✅ Performance NFRs addressed
- ✅ Security NFRs addressed
- ✅ No contradictions with PRD
- ✅ Deployment model clear
- ✅ Data models complete
- ✅ Risks identified and mitigated

**Time Estimate**: 1 hour

---

### Step 2.3: Epic and Story Creation

**Workflow**: `*create-epics-and-stories`

**Agent**: PM (John)

**Purpose**: Break PRD into epics (high-level groupings) and story stubs (placeholders, NOT full stories yet)

**Timing**: AFTER Architecture.md complete

**Why After Architecture**:
- PM needs to know technical approach to properly group stories
- Example: "Should Streamlit and Excel be separate epics or one epic?"
  - If Architecture says "completely independent deployments" → Separate epics
  - If Architecture says "tightly coupled via shared code" → Consider single epic or sequenced epics

**How to Execute**:
1. Load PM agent
2. Type: `*create-epics-and-stories`
3. Point PM to PRD.md AND Architecture.md
4. PM creates epic breakdown

**Expected Epic Structure** (OFAC-specific):

**Epic 1: Shared Core Engine**
- **Description**: Build the shared matching engine, loader, and updater used by both tools
- **Stories** (stubs):
  - Story 1.1: Implement OFAC data loader (download and parse CSV)
  - Story 1.2: Implement fuzzy matching engine (rapidfuzz integration)
  - Story 1.3: Implement country-aware scoring logic
  - Story 1.4: Implement humanitarian context detection
  - Story 1.5: Implement OFAC updater (version checking, atomic swap)
  - Story 1.6: Unit tests for core engine
- **Dependencies**: None (foundational)
- **Estimated Stories**: 6

**Epic 2: Streamlit Web Application**
- **Description**: Build the bulk screening web interface
- **Stories** (stubs):
  - Story 2.1: File upload widget and column mapping
  - Story 2.2: Bulk screening with progress indicator
  - Story 2.3: Results table with color coding
  - Story 2.4: Export results to CSV/Excel
  - Story 2.5: Update UI (status display, update buttons)
  - Story 2.6: Settings panel (thresholds, warnings)
  - Story 2.7: Integration tests for Streamlit app
- **Dependencies**: Epic 1 (needs core engine)
- **Estimated Stories**: 7

**Epic 3: Excel Custom Function**
- **Description**: Build the in-cell screening add-in
- **Stories** (stubs):
  - Story 3.1: xlwings UDF implementation (=OFAC_CHECK())
  - Story 3.2: Result caching mechanism
  - Story 3.3: VBA settings form (update controls)
  - Story 3.4: Excel template workbook with examples
  - Story 3.5: Installation script and documentation
  - Story 3.6: Integration tests for Excel add-in
- **Dependencies**: Epic 1 (needs core engine)
- **Estimated Stories**: 6

**Total**: 3 epics, 19 story stubs

**BMAD Principle**: Story Stubs vs Full Stories

**At This Stage**:
- PM creates **stubs** (title, brief description, epic assignment)
- PM does NOT create full stories (tasks, acceptance criteria, context)
- Full stories created just-in-time by SM in Phase 4

**Why Stubs First**:
- Don't waste time detailing story 19 when story 1 might change approach
- Stubs provide roadmap, full stories provide execution detail
- Just-in-time story creation adapts to learnings from earlier stories

**File Structure Created**:
```
/docs/epics/
  epic-001-shared-core-engine.md
  epic-002-streamlit-web-app.md
  epic-003-excel-custom-function.md

/docs/stories/
  story-001.001.md  (stub)
  story-001.002.md  (stub)
  ...
  story-003.006.md  (stub)
```

**Learning Checkpoint #5**: Epic Breakdown Strategy

**What to Observe**:
- How does PM group requirements into epics?
- Why 3 epics, not 1 or 6?
- How are dependencies identified?

**Document in Learning Journal**:
- PM's epic breakdown logic
- Story stub format (what's included, what's not)
- How epic structure reflects architecture

**Time Estimate**: 2-3 hours

---

### Step 2.4: Implementation Readiness Check

**Workflow**: `*implementation-readiness`

**Agent**: Architect (Winston)

**Purpose**: Validate that PRD, Architecture, and Epics are aligned and complete before starting implementation

**This is a QUALITY GATE**: Do not proceed to Phase 4 if this fails.

**How to Execute**:
1. Load Architect agent
2. Type: `*implementation-readiness`
3. Architect reviews PRD.md, Architecture.md, epic files

**What Architect Will Check**:
- ✅ All PRD FRs covered by architecture
- ✅ All PRD NFRs addressed in architecture
- ✅ Epic breakdown complete (no missing areas)
- ✅ Epic dependencies logical
- ✅ No contradictions between docs
- ✅ Story stubs sufficient for starting implementation

**Expected Output**:
- **PASS**: "Ready for implementation. Proceed to sprint planning."
- **FAIL**: "Issues found: [list]. Resolve before implementation."

**BMAD Principle**: Quality Gates Prevent Rework

**Why This Matters**:
- Catch misalignments NOW (cheap to fix)
- vs. Discover mid-implementation (expensive to fix)

**Example**:
- **Scenario**: PRD has FR14: "Support regional country designations (Africa II, Oceania)"
- **Issue**: Architecture.md doesn't explain country mapping strategy
- **Readiness Check**: Architect flags missing design
- **Resolution**: Architect adds country mapping table to Architecture.md
- **Result**: DEV agent has clear guidance when implementing Story 1.3

**Without Readiness Check**:
- DEV agent reaches Story 1.3, no guidance on regional mapping
- DEV improvises (hardcodes list? API lookup? skip?)
- Result: Tech debt or rework

**Learning Checkpoint #6**: Alignment Validation

**What to Observe**:
- What gaps does Architect find (if any)?
- How does Architect verify completeness?
- What does "ready" mean in BMAD context?

**Document in Learning Journal**:
- Readiness checklist Architect uses
- Gaps found (if any) and resolutions
- Pattern: What to check before implementation

**Time Estimate**: 1-2 hours

---

## Phase 3: Story Preparation

### Step 3.1: Sprint Planning Initialization

**Workflow**: `*sprint-planning`

**Agent**: SM (Bob) 🏃

**Purpose**: Initialize sprint tracking file (sprint-status.yaml) with all story stubs

**How to Execute**:
1. Load SM agent (`@sm`)
2. Type: `*sprint-planning`
3. SM scans epic files and creates tracking

**What SM Will Do**:
1. Read all epic files
2. Extract all story stubs
3. Create `sprint-status.yaml` with structure:
```yaml
epics:
  - id: "epic-001"
    name: "Shared Core Engine"
    status: "in-progress"  # or backlog
    stories:
      - id: "story-001.001"
        title: "Implement OFAC data loader"
        status: "backlog"  # Initial state
      - id: "story-001.002"
        title: "Implement fuzzy matching engine"
        status: "backlog"
      # ... all stories
  - id: "epic-002"
    # ...
```
4. Recommend first story to work on (usually story-001.001)

**BMAD Principle**: Sprint Status as Single Source of Truth

**Why sprint-status.yaml**:
- **Centralized tracking**: One file shows entire project status
- **Workflow queries**: Agents read this to know "what's next?"
- **Audit trail**: History of progress (via git commits)
- **Human-readable**: YAML format easy to inspect

**Alternative** (without BMAD):
- Scattered tracking (Jira, GitHub issues, mental notes)
- Agents can't access external tools
- Result: Manual coordination overhead

**Learning Checkpoint #7**: Sprint Tracking Mechanics

**What to Observe**:
- How SM organizes stories in sprint-status.yaml
- Story states (backlog → drafted → ready → in-progress → review → done)
- How SM recommends prioritization

**Document in Learning Journal**:
- sprint-status.yaml structure
- Story state lifecycle
- How tracking enables workflow automation

**Time Estimate**: 30 minutes

---

### Step 3.2: Test Framework Setup (PARALLEL)

**Workflow**: `*framework`

**Agent**: TEA (Murat) 🧪

**Purpose**: Initialize test infrastructure before implementation begins

**Timing**: **PARALLEL** to sprint planning (can run simultaneously)

**How to Execute**:
1. Load TEA agent (`@tea`)
2. Type: `*framework`
3. TEA asks about testing requirements

**What TEA Will Ask**:
- **Testing level**: Unit, integration, E2E? (All three for OFAC)
- **Framework preference**: pytest for Python (standard)
- **E2E needs**: Streamlit testing (Selenium/Playwright), Excel testing (manual initially)
- **Coverage target**: >90% per PRD NFRs

**What TEA Will Do**:
1. Create test directory structure:
```
/tests/
  /unit/
    test_ofac_loader.py
    test_ofac_matcher.py
    test_ofac_updater.py
  /integration/
    test_streamlit_integration.py
    test_excel_integration.py
  /e2e/
    test_bulk_screening_workflow.py
  conftest.py (pytest fixtures)
  pytest.ini (configuration)
```
2. Install pytest and dependencies (requirements.txt)
3. Create sample test fixtures (mock OFAC data)
4. Document testing standards in `/docs/testing-strategy.md`

**BMAD Principle**: Test Framework Before Code

**Why Setup Tests First**:
- **TDD enablement**: DEV can write tests as they implement
- **No excuses**: Framework ready, no "I'll add tests later"
- **Standards set**: TEA defines patterns, DEV follows

**Pattern**:
- ❌ **Anti-pattern**: Implement features, add tests at end (often skipped)
- ✅ **BMAD pattern**: Framework ready, tests written alongside code

**Learning Checkpoint #8**: Testing as First-Class Citizen

**What to Observe**:
- How TEA structures test directories
- What fixtures TEA creates (mock data, test helpers)
- How testing standards are documented

**Document in Learning Journal**:
- Test framework structure
- TEA's testing philosophy
- How tests integrate with story workflow

**Time Estimate**: 2-3 hours

---

## Phase 4: Implementation Loop

### Overview

**Pattern**: Iterative story-by-story implementation

**Agents Involved**:
- **SM (Bob)**: Story creation and context assembly
- **DEV (Amelia)**: Implementation and code review
- **TEA (Murat)**: Periodic test automation (parallel)

**Sequence** (per story):
```
1. SM: *create-story → Full story file
2. SM: *story-context → Context XML
3. DEV: *develop-story → Implementation (Run 1)
4. DEV: *code-review → QA check
5. (If issues) DEV: *develop-story → Fixes (Run 2)
6. (If clean) DEV: *story-done → Mark complete
7. Repeat for next story
```

**Total Stories**: 19 (estimated)
**Estimated Duration**: 1.5-2 weeks

---

### Step 4.1: Create Story (Per-Story Basis)

**Workflow**: `*create-story`

**Agent**: SM (Bob)

**Purpose**: Transform story stub into full story with tasks, acceptance criteria, dependencies

**When**: At the start of each story cycle

**How to Execute**:
1. Load SM agent
2. Type: `*create-story`
3. SM asks which story (or auto-selects next in backlog)
4. SM creates full story

**Example: Story 001.001 - Implement OFAC Data Loader**

**Stub** (from epic):
```markdown
# Story 001.001: Implement OFAC Data Loader
Brief: Create module to download and parse OFAC CSV files
```

**Full Story** (after SM's create-story):
```markdown
# Story 001.001: Implement OFAC Data Loader

## Description
Implement the OFAC data loader module that downloads CSV files from OFAC API,
parses them into pandas DataFrames, and builds in-memory entity indices.

## Epic
Epic 001: Shared Core Engine

## Dependencies
- None (foundational story)

## Tasks
1. Create ofac_loader.py module structure
2. Implement download_ofac_file(file_name) function
   - HTTP GET to sanctionslistservice.ofac.treas.gov
   - Handle redirects (S3 redirect pattern)
   - Save to temp directory
   - Return file path
3. Implement parse_sdn_csv(file_path) function
   - Load CSV into pandas DataFrame
   - Validate column structure
   - Return DataFrame
4. Implement parse_alt_csv(file_path) function
5. Implement parse_add_csv(file_path) function
6. Implement build_entity_index(sdn_df, alt_df, add_df) function
   - Merge data from 3 DataFrames
   - Create normalized name list
   - Build searchable index structure
7. Write unit tests for each function (>90% coverage)
8. Handle error cases (network failure, invalid CSV)

## Acceptance Criteria
- AC1: download_ofac_file() successfully downloads SDN.CSV from OFAC API
- AC2: parse_sdn_csv() correctly parses all columns and rows
- AC3: build_entity_index() creates searchable index with 18,422 entities
- AC4: Unit tests cover all functions with >90% coverage
- AC5: Error handling validates CSV structure before parsing
- AC6: Network failures retry with exponential backoff (3 attempts)

## Definition of Done
- [ ] All tasks completed
- [ ] All acceptance criteria met
- [ ] Unit tests passing (100%)
- [ ] Code reviewed and approved
- [ ] Documentation strings (docstrings) complete
- [ ] No linting errors (flake8, black)

## Estimated Complexity
Medium (4-6 hours)
```

**BMAD Principle**: Tasks vs Acceptance Criteria

**Tasks**: HOW to implement (developer guidance)
**Acceptance Criteria**: WHAT must be true when done (validation)

**Example**:
- **Task 2**: "Implement download_ofac_file() function" ← HOW
- **AC1**: "download_ofac_file() successfully downloads SDN.CSV" ← WHAT

**Why Both**:
- Tasks guide DEV during implementation
- ACs validate completeness during review
- Tasks can change (approach evolves), ACs should not (requirements fixed)

**Learning Checkpoint #9**: Story Anatomy

**What to Observe**:
- How SM expands stub into full story
- Task granularity (how small?)
- Acceptance criteria specificity

**Document in Learning Journal**:
- Story structure SM uses
- Task vs AC distinction
- How SM estimates complexity

**Time Per Story**: 1-2 hours (SM's effort)

---

### Step 4.2: Assemble Story Context (Per-Story Basis)

**Workflow**: `*story-context`

**Agent**: SM (Bob)

**Purpose**: Create story-XXX-context.xml with all information DEV needs

**When**: Immediately after *create-story

**How to Execute**:
1. SM agent already loaded
2. Type: `*story-context`
3. SM asks which story (or auto-continues from create-story)
4. SM assembles context XML

**What SM Will Include**:
```xml
<story-context>
  <story>
    <!-- Full story content: description, tasks, ACs, DoD -->
  </story>

  <epic-context>
    <!-- Epic-level technical guidance (if exists) -->
    <!-- For Epic 001: "Use pandas for CSV parsing, rapidfuzz for matching" -->
  </epic-context>

  <repository-docs>
    <!-- Patterns, conventions from Architecture.md, PRD.md -->
    <!-- "Shared modules go in /shared/ directory" -->
    <!-- "Use Python 3.9+ type hints" -->
  </repository-docs>

  <dynamic-context>
    <!-- Files relevant to THIS story -->
    <!-- For Story 001.001: Sample OFAC CSV structure, pandas examples -->
  </dynamic-context>

  <testing-requirements>
    <!-- From testing-strategy.md -->
    <!-- "Unit tests required, >90% coverage" -->
  </testing-requirements>
</story-context>
```

**BMAD Principle**: Context XML as AI's Complete Blueprint

**Why XML Format**:
- **Structured**: Easy for AI to parse sections
- **Complete**: Everything in one file
- **Just-in-time**: Assembled when needed (always current)
- **Single source**: DEV reads ONLY this file (no hunting for info)

**Analogy**:
- **Without Context**: "Build this house" (no blueprints)
- **With Context**: "Build this house" + blueprints + materials list + building codes

**Learning Checkpoint #10**: Context Assembly Process

**What to Observe**:
- What sources SM pulls from (PRD, Architecture, epic, etc.)
- How SM decides what's relevant for THIS story
- XML structure and sections

**Document in Learning Journal**:
- Context XML format
- Sources SM queries
- How context enables autonomous DEV execution

**Time Per Story**: 30-60 minutes (SM's effort)

---

### Step 4.3: Implement Story (Per-Story Basis)

**Workflow**: `*develop-story`

**Agent**: DEV (Amelia) 💻

**Purpose**: Implement story tasks, write tests, satisfy acceptance criteria

**When**: After story context XML assembled

**How to Execute**:
1. Load DEV agent (`@dev`)
2. Type: `*develop-story`
3. Point DEV to story-XXX-context.xml (or DEV auto-finds it)
4. DEV implements

**What DEV Will Do** (Story 001.001 example):

**Run 1 - Implementation**:
1. Create `/shared/ofac_loader.py`
2. Implement functions per tasks:
   - `download_ofac_file(file_name)`
   - `parse_sdn_csv(file_path)`
   - `parse_alt_csv(file_path)`
   - `parse_add_csv(file_path)`
   - `build_entity_index(sdn_df, alt_df, add_df)`
3. Write unit tests in `/tests/unit/test_ofac_loader.py`:
   - `test_download_ofac_file_success()`
   - `test_download_ofac_file_network_failure()`
   - `test_parse_sdn_csv_valid_file()`
   - `test_parse_sdn_csv_invalid_structure()`
   - `test_build_entity_index_correct_count()`
   - ... (15-20 tests for >90% coverage)
4. Run tests: `pytest tests/unit/test_ofac_loader.py`
5. Fix any failures
6. Commit code: `git commit -m "feat: implement OFAC data loader (Story 001.001)"`
7. Update story file status: `status: in-progress → review`

**BMAD Principle**: DEV Never Starts Until Status == Ready

**Critical Rule**: DEV agent will REFUSE to start if:
- Story status != "ready"
- Story context XML missing
- Acceptance criteria unclear

**Why This Matters**:
- Ensures DEV has complete information
- Prevents half-baked implementations
- Enforces workflow discipline

**Learning Checkpoint #11**: TDD in Practice

**What to Observe**:
- Does DEV write tests before or during implementation?
- How does DEV use acceptance criteria to guide testing?
- What does ">90% coverage" mean in practice?

**Document in Learning Journal**:
- DEV's implementation approach
- Test-first vs test-during patterns
- How ACs map to tests

**Time Per Story**: 3-8 hours (varies by complexity)

---

### Step 4.4: Code Review (Per-Story Basis)

**Workflow**: `*code-review`

**Agent**: DEV (Amelia) or Principal Engineer (Jordan)

**Purpose**: Senior-level review of implementation quality, architecture alignment, test coverage

**When**: After DEV completes implementation (status = review)

**How to Execute**:
1. DEV agent already loaded (or load fresh)
2. Type: `*code-review`
3. Point DEV to story file
4. DEV reviews code

**What DEV Will Check**:
- ✅ All tasks completed
- ✅ All acceptance criteria satisfied
- ✅ Tests passing (100%)
- ✅ Test coverage >90% (per NFRs)
- ✅ Code follows architecture (shared module in /shared/)
- ✅ Code follows conventions (type hints, docstrings)
- ✅ No security issues (input validation, error handling)
- ✅ No performance issues (efficient algorithms)
- ✅ No code smells (duplication, complexity)

**Possible Outcomes**:

**APPROVED** (Clean):
```
Code Review: APPROVED
- All ACs satisfied
- Test coverage 94%
- Follows architecture
- No issues found
Recommendation: Mark story done
```

**CHANGES REQUESTED** (Issues Found):
```
Code Review: CHANGES REQUESTED
Issues:
1. AC6 not satisfied: Retry logic only attempts 1 time, not 3
2. Test coverage 82% (below 90% threshold): Missing error case tests
3. Function download_ofac_file() missing type hints
4. Docstring incomplete for build_entity_index()

Recommendation: Run *develop-story again (Run 2) to fix issues
```

**BMAD Principle**: Code Review as Teaching Moment

**Why AI Code Review Matters**:
- **Consistency**: Same standards every time
- **Thoroughness**: AI checks EVERYTHING (humans miss details)
- **Educational**: Review explains WHY issues matter
- **Non-personal**: No ego, just quality

**Pattern for Mastery**:
- **First 5 stories**: Expect issues found (calibrate to standards)
- **Next 10 stories**: Fewer issues (learned patterns)
- **After 15 stories**: Minimal issues (internalized quality bar)

**Learning Checkpoint #12**: Code Review Standards

**What to Observe**:
- What issues DEV finds (if any)
- How DEV explains quality standards
- Common mistakes to avoid

**Document in Learning Journal**:
- Code review checklist DEV uses
- Issues found in YOUR implementations
- Quality patterns to internalize

**Time Per Story**: 30-60 minutes (review time)

---

### Step 4.5: Fix Issues (If Needed)

**Workflow**: `*develop-story` (Run 2)

**Agent**: DEV (Amelia)

**Purpose**: Fix issues found during code review

**When**: If code review finds issues (status remains "review")

**How to Execute**:
1. DEV agent loaded
2. Type: `*develop-story` (Run 2)
3. DEV uses code review feedback to fix issues

**What DEV Will Do**:
1. Read code review feedback
2. Fix each issue:
   - Issue 1: Update retry logic (1 attempt → 3 attempts)
   - Issue 2: Add missing error case tests
   - Issue 3: Add type hints to download_ofac_file()
   - Issue 4: Complete docstring for build_entity_index()
3. Re-run tests
4. Commit fixes: `git commit -m "fix: address code review feedback (Story 001.001)"`
5. Request re-review

**Iterative Loop**:
```
*develop-story (Run 1) → *code-review (issues found)
  → *develop-story (Run 2) → *code-review (clean)
    → *story-done
```

**BMAD Principle**: Multi-Run Capability

**Why Multiple Runs**:
- First attempt rarely perfect (learning process)
- Code review identifies gaps
- Run 2 fixes gaps (improves quality)

**Pattern**:
- **New developers**: Often need Run 2-3
- **Experienced developers**: Usually Run 1 clean
- **Complex stories**: Even experts need Run 2

**Time Per Fix**: 1-3 hours

---

### Step 4.6: Mark Story Done

**Workflow**: `*story-done`

**Agent**: DEV (Amelia)

**Purpose**: Update story status, update sprint-status.yaml, trigger next story

**When**: After code review approves (all ACs met, tests pass, no issues)

**How to Execute**:
1. DEV agent loaded
2. Type: `*story-done`
3. DEV asks which story (or auto-detects from context)
4. DEV updates tracking

**What DEV Will Do**:
1. Update story file:
   - `status: review → done`
   - Add completion timestamp
2. Update sprint-status.yaml:
   - `story-001.001: status: done`
   - Increment epic progress
3. Recommend next story:
   - "Story 001.001 complete. Next: Story 001.002 (Implement fuzzy matching engine)"

**BMAD Principle**: Story Done != Code Written

**Definition of Done** (from story):
- [ ] All tasks completed ← Must be TRUE
- [ ] All acceptance criteria met ← Must be TRUE
- [ ] Unit tests passing (100%) ← Must be TRUE
- [ ] Code reviewed and approved ← Must be TRUE
- [ ] Documentation strings complete ← Must be TRUE
- [ ] No linting errors ← Must be TRUE

**If ANY checkbox false**: Story NOT done (status stays "review")

**Learning Checkpoint #13**: Definition of Done Discipline

**What to Observe**:
- How DEV validates DoD before marking done
- What happens if DoD not met (refuses to mark done)
- How sprint-status.yaml updates

**Document in Learning Journal**:
- DoD checklist enforcement
- Story completion pattern
- Sprint tracking mechanics

**Time Per Story**: 10 minutes (administrative)

---

### Step 4.7: Repeat for All Stories

**Pattern**: Repeat Steps 4.1 - 4.6 for each of the 19 stories

**Epic 1** (6 stories):
- Story 001.001: OFAC data loader
- Story 001.002: Fuzzy matching engine
- Story 001.003: Country-aware scoring
- Story 001.004: Humanitarian context detection
- Story 001.005: OFAC updater
- Story 001.006: Unit tests for core

**Epic 2** (7 stories):
- Story 002.001: Streamlit file upload
- Story 002.002: Bulk screening
- Story 002.003: Results table
- Story 002.004: Export functionality
- Story 002.005: Update UI
- Story 002.006: Settings panel
- Story 002.007: Integration tests

**Epic 3** (6 stories):
- Story 003.001: xlwings UDF
- Story 003.002: Result caching
- Story 003.003: VBA settings form
- Story 003.004: Excel template
- Story 003.005: Installation script
- Story 003.006: Integration tests

**Parallel TEA Activities**:
- Every 3-4 stories: TEA runs `*automate` to add comprehensive tests
- After Epic 1 complete: TEA can create integration tests for core engine

**Estimated Timeline**:
- **Epic 1**: 3-5 days (6 stories, foundational)
- **Epic 2**: 3-4 days (7 stories, depends on Epic 1)
- **Epic 3**: 2-3 days (6 stories, depends on Epic 1)
- **Total**: 8-12 days (1.5-2 weeks)

---

## Phase 5: Testing & Quality

### Step 5.1: Traceability Matrix

**Workflow**: `*trace`

**Agent**: TEA (Murat)

**Purpose**: Validate that every PRD requirement has corresponding tests

**When**: After all stories implemented (or per epic)

**How to Execute**:
1. Load TEA agent
2. Type: `*trace`
3. TEA analyzes PRD vs test coverage

**What TEA Will Check**:
- Map every FR to test(s)
- Map every NFR to validation
- Identify untested requirements (gaps)

**Expected Output**:
```markdown
# Requirements Traceability Matrix

## Functional Requirements
- FR1: Upload CSV/Excel → test_file_upload.py::test_csv_upload ✅
- FR2: Fuzzy match (80%) → test_ofac_matcher.py::test_fuzzy_match_80 ✅
- FR3: Country-aware scoring → test_ofac_matcher.py::test_country_boost ✅
- FR14: Regional mapping → ❌ NO TEST FOUND

## Non-Functional Requirements
- NFR1: Match <1 second → test_performance.py::test_match_speed ✅
- NFR2: Memory <100MB → test_performance.py::test_memory_usage ✅
- NFR3: Update check <2 sec → test_ofac_updater.py::test_version_check_speed ✅

## Gaps
- FR14 missing test coverage
- Recommendation: Add test_country_regional_mapping.py
```

**BMAD Principle**: Traceability as Quality Gate

**Why This Matters**:
- Ensures complete test coverage (no blind spots)
- Validates requirements satisfaction
- Catches implementation gaps

**Learning Checkpoint #14**: Test Traceability

**What to Observe**:
- How TEA maps requirements to tests
- Gaps TEA identifies
- What "complete coverage" means

**Document in Learning Journal**:
- Traceability matrix format
- Gap analysis process
- Quality gate criteria

**Time Estimate**: 2-3 hours

---

### Step 5.2: CI/CD Pipeline Setup

**Workflow**: `*ci`

**Agent**: TEA (Murat)

**Purpose**: Setup continuous integration pipeline for automated testing

**When**: After test suite complete

**How to Execute**:
1. Load TEA agent
2. Type: `*ci`
3. TEA creates CI configuration

**What TEA Will Create**:
```yaml
# .github/workflows/ci.yml (if using GitHub Actions)
name: OFAC CI Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - run: pip install -r requirements.txt
      - run: pytest tests/ --cov=shared --cov-report=xml
      - run: flake8 shared/ streamlit_app/ excel_addin/
      - run: black --check shared/ streamlit_app/ excel_addin/
```

**BMAD Principle**: Automation as Safety Net

**Why CI/CD**:
- Catches regressions automatically
- Enforces quality standards
- No manual "remember to run tests"

**Time Estimate**: 1-2 hours

---

### Step 5.3: NFR Assessment

**Workflow**: `*nfr-assess`

**Agent**: TEA (Murat)

**Purpose**: Validate non-functional requirements met (performance, security, etc.)

**When**: After implementation complete

**How to Execute**:
1. Load TEA agent
2. Type: `*nfr-assess`
3. TEA runs benchmarks and security checks

**What TEA Will Check**:
- NFR1: Match speed (run performance tests)
- NFR2: Memory usage (run profiling)
- NFR3: Update check speed (benchmark version check)
- NFR4: Data privacy (audit for external calls)
- NFR5: Audit trail (verify version logging)

**Expected Output**:
```markdown
# NFR Assessment Report

## Performance NFRs
- NFR1: Match speed <1 second
  - Result: 0.23s average (95th percentile 0.48s) ✅ PASS
- NFR2: Memory usage <100 MB
  - Result: 67 MB with full OFAC index ✅ PASS
- NFR3: Update check <2 seconds
  - Result: 1.1s average ✅ PASS

## Security NFRs
- NFR4: Data privacy (local processing)
  - Result: No external API calls except OFAC .gov ✅ PASS

## Compliance NFRs
- NFR5: 5-year audit trail
  - Result: version.json logs all updates ✅ PASS

## Overall: ALL NFRs SATISFIED
```

**Learning Checkpoint #15**: NFR Validation

**What to Observe**:
- How TEA benchmarks performance
- Security audit methodology
- Compliance verification

**Document in Learning Journal**:
- NFR assessment process
- Performance testing patterns
- Security checklist

**Time Estimate**: 2-4 hours

---

## Phase 6: Retrospective

### Step 6.1: Epic Retrospective

**Workflow**: `*epic-retrospective`

**Agent**: SM (Bob) or BMad Master (party mode)

**Purpose**: Reflect on what worked, what didn't, extract patterns learned

**When**: After all epics complete (or per epic)

**How to Execute**:
1. Load SM agent or invoke `*party-mode`
2. Type: `*epic-retrospective`
3. Reflect on process

**What to Discuss**:
- **What went well**: Shared code layer worked great
- **What didn't**: xlwings testing tricky (manual Excel needed)
- **Process improvements**: Could have done Epic 2 and 3 in parallel
- **Technical learnings**: rapidfuzz performs better than expected
- **BMAD learnings**: Story context XML made DEV autonomous

**Expected Output**:
```markdown
# Epic Retrospective: OFAC Sanctions Screening Tools

## Successes
- Shared code layer eliminated duplication
- Daily update checks caught OFAC list changes during development
- Test coverage >90% caught 3 bugs before production

## Challenges
- xlwings testing required manual Excel (no CI for Excel tests)
- Regional country mapping not in initial architecture (added mid-stream)

## BMAD Process Observations
- Story context XML worked perfectly (DEV had all info needed)
- Code review caught 15 issues across 19 stories (quality improved)
- Architecture.md prevented tech debt (shared module design clear)

## Future Improvements
- Add regional mapping to architecture phase next time
- Consider Streamlit + Excel as parallel epics (not sequential)
```

**Learning Checkpoint #16**: BMAD Patterns Extracted

**What to Observe**:
- Which BMAD workflows added most value?
- Where did BMAD process feel heavy? Light?
- What would you do differently next project?

**Document in Learning Journal**:
- Personal reflections on BMAD experience
- Workflow effectiveness ratings
- Customizations you'd make for future projects

**Time Estimate**: 1-2 hours

---

## Checkpoints & Learning Moments

### Summary of All Learning Checkpoints

1. **Track Classification** (workflow-init)
2. **PRD as AI Context** (create-prd)
3. **Quality PRD Standards** (validate-prd)
4. **Architecture as Decision Docs** (create-architecture)
5. **Epic Breakdown Strategy** (create-epics-and-stories)
6. **Alignment Validation** (implementation-readiness)
7. **Sprint Tracking Mechanics** (sprint-planning)
8. **Testing as First-Class** (framework)
9. **Story Anatomy** (create-story)
10. **Context Assembly** (story-context)
11. **TDD in Practice** (develop-story)
12. **Code Review Standards** (code-review)
13. **Definition of Done Discipline** (story-done)
14. **Test Traceability** (trace)
15. **NFR Validation** (nfr-assess)
16. **BMAD Patterns Extracted** (epic-retrospective)

**Use Learning Journal**: Document observations at each checkpoint

---

## Alternative Paths & Deviations

### When to Deviate from This Roadmap

**BMAD is Adaptive**: This roadmap is optimal for OFAC, but not rigid.

### Alternative: Skip Architecture (NOT RECOMMENDED for OFAC)

**If you chose Track 1 (Quick Flow)**:
- Skip create-architecture
- Use Principal Engineer: create-tech-spec instead
- Faster, but OFAC complexity makes this risky

### Alternative: Parallel Epic Development

**If you have multiple developers**:
- Epic 2 (Streamlit) and Epic 3 (Excel) can run in parallel after Epic 1
- Both depend only on Epic 1 (shared core)
- Reduces timeline by 3-4 days

### Alternative: Skip Validation Workflows

**If time-constrained**:
- Skip validate-prd, validate-architecture
- Risk: Lower quality, potential rework
- Recommendation: Don't skip during learning phase

### Alternative: Party Mode for Story Creation

**If stories complex**:
- Use `*party-mode` with PM + Architect + TEA
- Multi-agent discussion for complex story design
- Example: Story with both UI, backend, and testing implications

### Pattern: When to Use Party Mode

**Use Party Mode When**:
- Strategic decisions (architecture approach)
- Retrospectives (multi-perspective reflection)
- Complex story design (cross-cutting concerns)
- Course correction (priorities changed)

**Don't Use Party Mode When**:
- Straightforward tasks (create simple story)
- Single-agent expertise sufficient (testing framework)
- Time-sensitive (party mode takes longer)

---

## Summary: Your BMAD Journey

### What You'll Learn by Following This Roadmap

1. **Project Classification**: How to choose Track 1 vs 2 vs 3
2. **Requirements Engineering**: How PM transforms ideas into PRDs
3. **Architecture Design**: How Architect translates requirements into system design
4. **Story Breakdown**: How PM creates epics and stories from PRD
5. **Context Assembly**: How SM provides complete info to DEV
6. **TDD Workflow**: How DEV implements with tests alongside code
7. **Code Review**: How AI maintains quality standards
8. **Sprint Tracking**: How sprint-status.yaml orchestrates workflows
9. **Testing Strategy**: How TEA ensures comprehensive quality
10. **BMAD Patterns**: Reusable workflows for future projects

### Your Next Step

**Begin with**: PM agent → `*workflow-init`

**Then refer to**: This roadmap for each subsequent workflow

**Remember**: Use BMAD_Learning_Journal.md to document observations

---

**Next Documents**:
- **Document 3**: BMAD_Agent_Decision_Rubrics.md (when to choose what)
- **Document 4**: BMAD_Learning_Journal.md (template for your observations)
- **Document 5**: BMAD_Project_Retrospective.md (post-completion reflection)

---

**Document Metadata**

- **Created**: 2025-12-06
- **Author**: BMad Master Agent
- **Purpose**: Phase-by-phase BMAD roadmap for OFAC project
- **Depth**: Level 3 (Advanced - principles, deviations, patterns)
- **Audience**: Carlos (human expert learner)
- **Part**: 2 of 5 (BMAD Learning Journey)
