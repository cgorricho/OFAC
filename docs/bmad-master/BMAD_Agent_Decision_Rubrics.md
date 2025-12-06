# BMAD Agent Decision Rubrics - When to Choose What

**Purpose**: Decision-making frameworks for selecting agents and workflows
**Audience**: Carlos (building judgment for future projects)
**Created**: December 6, 2025
**Author**: BMad Master Agent

---

## How to Use This Document

This is your "cheat sheet" for BMAD decisions. When you ask "Which agent?" or "Which workflow?", consult the relevant rubric below.

**Structure**:
1. Agent Selection Rubrics
2. Workflow Selection Rubrics
3. Track Selection Rubric
4. Timing & Sequencing Rubrics
5. Party Mode Decision Rubric

---

## 1. Agent Selection Rubrics

### Rubric 1.1: Which Agent for Planning?

| Situation | Choose | Don't Choose | Why |
|-----------|--------|--------------|-----|
| **Need requirements doc (complex project)** | PM (John) | Principal Engineer | PM specializes in PRDs for Track 2-3 projects |
| **Need quick tech-spec (simple feature)** | Principal Engineer (Jordan) OR PM | Architect | Principal Engineer optimized for Quick Flow; PM can also do tech-specs |
| **Need market/competitive research** | Analyst (Mary) | PM | Analyst is research specialist |
| **Need to brainstorm ideas** | Analyst (Mary) | PM | Analyst has brainstorming workflow |
| **Need UI/UX design** | UX Designer (Sally) | PM | UX Designer is design thinking expert |

**Key Insight**: PM for comprehensive planning (Track 2-3), Principal Engineer for rapid planning (Track 1), Analyst for discovery/research.

---

### Rubric 1.2: Which Agent for Architecture?

| Situation | Choose | Don't Choose | Why |
|-----------|--------|--------------|-----|
| **Need system architecture (Level 3-4)** | Architect (Winston) | PM or DEV | Architect is system design expert |
| **Game architecture** | Game Architect (Cloud) | Regular Architect | Game-specific expertise |
| **Quick feature (no architecture)** | Skip architecture phase | Architect | Track 1 doesn't need architecture |
| **Validate readiness for implementation** | Architect (Winston) | SM or PM | Architect validates PRD+Arch alignment |

**Key Insight**: Use Architect for Level 3-4 projects ONLY. Track 1-2 (simple) skip architecture.

---

### Rubric 1.3: Which Agent for Implementation?

| Situation | Choose | Don't Choose | Why |
|-----------|--------|--------------|-----|
| **Prepare stories for development** | SM (Bob) | DEV | SM creates stories and assembles context |
| **Implement story** | DEV (Amelia) | PM or Architect | DEV is implementation expert |
| **Implement game story** | Game Developer (Link) | Regular DEV | Game-specific expertise |
| **Code review** | DEV (Amelia) OR Principal Engineer | TEA | DEV/Principal Engineer are code quality experts; TEA is testing expert |
| **Mark story complete** | DEV (Amelia) | SM | DEV owns implementation lifecycle |

**Key Insight**: SM prepares work, DEV executes work, DEV reviews work, DEV marks complete.

---

### Rubric 1.4: Which Agent for Testing?

| Situation | Choose | Don't Choose | Why |
|-----------|--------|--------------|-----|
| **Setup test framework** | TEA (Murat) | DEV | TEA is testing strategy expert |
| **Write tests before implementation (ATDD)** | TEA (Murat) | DEV | TEA drives test-first approach |
| **Comprehensive test suite** | TEA (Murat) | DEV | TEA knows testing patterns deeply |
| **Setup CI/CD pipeline** | TEA (Murat) | Architect or DEV | TEA owns quality infrastructure |
| **Validate NFRs (performance, security)** | TEA (Murat) | Architect | TEA benchmarks and validates |
| **Requirements traceability** | TEA (Murat) | PM | TEA maps requirements → tests |

**Key Insight**: TEA for ALL testing strategy and quality assurance. DEV writes tests during implementation, but TEA sets standards.

---

### Rubric 1.5: Which Agent for Documentation?

| Situation | Choose | Don't Choose | Why |
|-----------|--------|--------------|-----|
| **Document existing codebase (brownfield)** | Analyst (Mary) OR Technical Writer (Paige) | PM | Both have `document-project` workflow |
| **Create diagrams (Mermaid)** | Technical Writer (Paige) | Any agent | Paige generates diagrams as action |
| **Improve README** | Technical Writer (Paige) | DEV | Paige specializes in documentation quality |
| **Explain technical concepts** | Technical Writer (Paige) | Architect | Paige makes complex topics accessible |

**Key Insight**: Analyst for brownfield analysis, Technical Writer for documentation artifacts and diagrams.

---

### Rubric 1.6: Which Agent for Orchestration?

| Situation | Choose | Don't Choose | Why |
|-----------|--------|--------------|-----|
| **Multi-agent discussion** | BMad Master (party mode) | Any single agent | Master orchestrates 2-3 agents simultaneously |
| **List all available workflows** | BMad Master | Any agent | Master has `list-workflows` action |
| **List all available tasks** | BMad Master | Any agent | Master has `list-tasks` action |
| **Don't know what to do next** | ANY agent → `*workflow-status` | BMad Master | Every agent can run workflow-status |

**Key Insight**: Use BMad Master for party mode and meta-tasks. Use ANY agent's `workflow-status` for navigation.

---

## 2. Workflow Selection Rubrics

### Rubric 2.1: First Workflow to Run

| Project State | Run This Workflow | Agent | Why |
|---------------|-------------------|-------|-----|
| **New project (greenfield)** | `*workflow-init` | PM, Analyst, or Game Designer | Classify project and set track |
| **Existing code (brownfield)** | `*document-project` | Analyst or Technical Writer | Document before planning |
| **Already have planning docs** | `*workflow-init` (reference docs) | PM | Initialize tracking, reference existing research |
| **Lost / don't know state** | `*workflow-status` | ANY agent | Agent analyzes state and recommends next step |

**Key Insight**: Brownfield MUST start with `document-project`. Greenfield starts with `workflow-init`.

---

### Rubric 2.2: Planning Workflows (Phase 1-2)

| Goal | Workflow | Agent | When to Use | When to Skip |
|------|----------|-------|-------------|--------------|
| **Brainstorm ideas** | `*brainstorm-project` | Analyst | Uncertain scope, exploring solutions | Requirements already clear |
| **Strategic planning** | `*product-brief` | Analyst | Need product vision and strategy | Moving fast, skip Phase 1 |
| **Market research** | `*research` | Analyst | Need market/competitive/technical data | Already researched externally |
| **Create requirements** | `*create-prd` | PM | Track 2-3 projects (complex) | Track 1 (use tech-spec instead) |
| **Create quick spec** | `*create-tech-spec` | Principal Engineer or PM | Track 1 (simple features) | Track 2-3 (use PRD instead) |
| **Create UX design** | `*create-ux-design` | UX Designer | UI-heavy projects | Backend-only or CLI tools |
| **Validate PRD** | `*validate-prd` | PM | Learning mode, critical projects | Confident in quality, time-pressed |

**Key Insight**: Track determines doc type (PRD for Track 2-3, tech-spec for Track 1). Validation optional but recommended during learning.

---

### Rubric 2.3: Architecture Workflows (Phase 3)

| Goal | Workflow | Agent | When to Use | When to Skip |
|------|----------|-------|-------------|--------------|
| **Create architecture** | `*create-architecture` | Architect or Game Architect | Level 3-4 projects ONLY | Level 0-2 (no architecture needed) |
| **Validate architecture** | `*validate-architecture` | Architect | Learning mode, critical projects | Confident in quality |
| **Create epics/stories** | `*create-epics-and-stories` | PM | After PRD (and Architecture if Level 3-4) | Before requirements or architecture |
| **Validate readiness** | `*implementation-readiness` | Architect | Before starting implementation (quality gate) | Skip at your peril (not recommended) |

**Key Insight**: Architecture phase ONLY for Level 3-4. Always run `implementation-readiness` before Phase 4.

---

### Rubric 2.4: Implementation Workflows (Phase 4)

| Goal | Workflow | Agent | When to Use | Frequency |
|------|----------|-------|-------------|-----------|
| **Initialize sprint tracking** | `*sprint-planning` | SM | After epics created | Once per project |
| **Setup test framework** | `*framework` | TEA | Before implementation begins | Once per project |
| **Create full story** | `*create-story` | SM | When ready to start next story | Per story (19x for OFAC) |
| **Assemble story context** | `*story-context` | SM | After creating story | Per story |
| **Implement story** | `*develop-story` | DEV or Game Developer | After story context ready | Per story (multiple runs if needed) |
| **Review code** | `*code-review` | DEV or Principal Engineer | After implementation | Per story |
| **Mark story complete** | `*story-done` | DEV | After review approved | Per story |

**Key Insight**: Story loop = create → context → implement → review → done. Repeat for all stories.

---

### Rubric 2.5: Testing Workflows (Parallel)

| Goal | Workflow | Agent | When to Use | Frequency |
|------|----------|-------|-------------|-----------|
| **Test-first (before code)** | `*atdd` | TEA | Critical features, TDD approach | Before implementing features |
| **Comprehensive test suite** | `*automate` | TEA | After features implemented | Every 3-4 stories or per epic |
| **Requirements traceability** | `*trace` | TEA | After all stories done (or per epic) | Once per epic or end of project |
| **Setup CI pipeline** | `*ci` | TEA | After test suite complete | Once per project |
| **Validate NFRs** | `*nfr-assess` | TEA | After implementation complete | Once at end of project |

**Key Insight**: TEA works in parallel to DEV. Framework early, ATDD optional, automate periodically, trace/ci/nfr at end.

---

### Rubric 2.6: Change Management Workflows

| Situation | Workflow | Agent | When to Use |
|-----------|----------|-------|-------------|
| **Requirements changed mid-sprint** | `*correct-course` | PM, Architect, SM, or Game Architect | Priorities shift, new requirements emerge |
| **Epic completed, reflect** | `*epic-retrospective` | SM or BMad Master (party mode) | After each epic or end of project |
| **Strategic discussion needed** | `*party-mode` | BMad Master | Multi-perspective problem, brainstorming, course correction |

**Key Insight**: Use `correct-course` for changes, `epic-retrospective` for reflection, `party-mode` for complex decisions.

---

## 3. Track Selection Rubric

### Rubric 3.1: Quick Flow vs BMad Method vs Enterprise

| Indicator | Track 1 (Quick Flow) | Track 2 (BMad Method) | Track 3 (Enterprise) |
|-----------|---------------------|---------------------|---------------------|
| **Scope** | Single feature, clear | Multiple features, interconnected | Enterprise needs, multi-tenant |
| **Architecture needed?** | No | Yes (Level 3-4) | Yes + extended artifacts |
| **Story count** | 1-15 | 10-50+ | 50+ |
| **Keywords in description** | "fix", "add", "simple", "bug" | "product", "platform", "system", "complex" | "enterprise", "compliance", "multi-tenant", "security" |
| **Rework cost** | Low | Medium-High | Very High |
| **Planning docs** | Tech-spec only | PRD + Architecture (+ optional UX) | PRD + Arch + Security + DevOps + Compliance |
| **Planning time** | Hours | 1-3 days | 3-5 days |
| **Agent support** | Basic | Exceptional | Maximum |

**Decision Tree**:
```
Is it a bug fix or simple feature?
├─ YES → Is scope crystal clear?
│         ├─ YES → Track 1 (Quick Flow)
│         └─ NO → Track 2 (BMad Method)
└─ NO → Does it have enterprise/compliance needs?
          ├─ YES → Track 3 (Enterprise Method)
          └─ NO → Is it a product/platform or complex feature?
                    ├─ YES → Track 2 (BMad Method)
                    └─ NO → Track 1 (Quick Flow)
```

**OFAC Example**: Multiple features (2 tools) + Architecture needed + Compliance context = **Track 2**

---

### Rubric 3.2: Level Selection (Within Track 2)

| Level | Characteristics | Architecture? | Example |
|-------|----------------|---------------|---------|
| **Level 0** | Single file, trivial change | No | Fix typo in README |
| **Level 1** | Single feature, no architecture decisions | No | Add logging to existing function |
| **Level 2** | Multiple features, no complex architecture | Optional | Add search feature to existing UI |
| **Level 3** | Architectural decisions required | Yes | Multi-tool system with shared layer (OFAC) |
| **Level 4** | Complex distributed system | Yes | Microservices platform, multi-region deployment |

**OFAC is Level 3**: 2 tools + shared core + architecture decisions (CSV format, update strategy, shared modules)

---

## 4. Timing & Sequencing Rubrics

### Rubric 4.1: When to Run Validation Workflows

| Validation | Timing | Always? | Skip When |
|------------|--------|---------|-----------|
| `*validate-prd` | After `*create-prd` | **Recommended during learning** | Confident, time-pressed |
| `*validate-tech-spec` | After `*create-tech-spec` | **Recommended during learning** | Confident, time-pressed |
| `*validate-architecture` | After `*create-architecture` | **Recommended during learning** | Confident, time-pressed |
| `*validate-design` | After `*create-ux-design` | **Recommended for UX-heavy** | Simple UI, time-pressed |
| `*validate-create-story` | After `*create-story` | **Optional** | Stories straightforward |
| `*validate-story-context` | After `*story-context` | **Optional** | Context assembly confident |
| `*implementation-readiness` | After epics/stories created | **MANDATORY** | Never skip (quality gate) |

**Pattern**: Validate more during learning (first 3-5 projects), validate less as you gain confidence.

---

### Rubric 4.2: Sequential vs Parallel Workflow Execution

| Workflows | Relationship | Execute | Why |
|-----------|-------------|---------|-----|
| `*document-project` → `*workflow-init` | Sequential | Document FIRST | Need codebase understanding before planning |
| `*create-prd` → `*create-architecture` | Sequential | PRD FIRST | Architecture needs requirements as input |
| `*create-architecture` → `*create-epics-and-stories` | Sequential | Architecture FIRST | Epic breakdown needs technical approach |
| `*sprint-planning` + `*framework` | **PARALLEL** | Run simultaneously | Independent - SM tracks stories, TEA sets up tests |
| `*create-story` → `*story-context` | Sequential | Story FIRST | Context needs story content |
| `*develop-story` → `*code-review` | Sequential | Implement FIRST | Review needs code |
| Epic 2 + Epic 3 (OFAC) | **PARALLEL** (if multi-dev) | After Epic 1 | Both depend only on Epic 1 |

**Key Insight**: Respect dependencies (sequential), parallelize independents (faster delivery).

---

### Rubric 4.3: When to Re-run Workflows (Multi-Run)

| Workflow | Re-run Scenario | Typical Runs | Why |
|----------|-----------------|--------------|-----|
| `*develop-story` | Code review found issues | 1-3 | Fix issues from review |
| `*code-review` | After fixes applied | 2 (implementation + fixes) | Validate fixes |
| `*create-prd` | Requirements changed | 1 (rarely 2 if major changes) | Update PRD mid-project |
| `*create-architecture` | Architecture pivot | 1 (rarely 2 if major redesign) | Rare, indicates early mistake |
| `*automate` (TEA) | Every 3-4 stories | 3-5 times per project | Periodic test suite expansion |

**Pattern**: DEV workflows multi-run (iterative refinement). Planning workflows single-run (changes indicate process failure).

---

## 5. Party Mode Decision Rubric

### Rubric 5.1: When to Use Party Mode

| Situation | Use Party Mode? | Agents to Include | Why |
|-----------|----------------|-------------------|-----|
| **Strategic architecture decision** | ✅ YES | Architect + DEV + TEA | Multiple perspectives on trade-offs |
| **Sprint retrospective** | ✅ YES | All agents | Cross-functional reflection |
| **Creative brainstorming** | ✅ YES | Analyst + PM + Designer | Multiple creative angles |
| **Course correction** | ✅ YES | PM + Architect + SM | Cross-functional alignment |
| **Simple story creation** | ❌ NO | Just SM | Single-agent sufficient |
| **Straightforward implementation** | ❌ NO | Just DEV | Clear task, no debate needed |
| **Test framework setup** | ❌ NO | Just TEA | TEA has expertise |
| **Complex story (cross-cutting)** | ✅ MAYBE | SM + Architect + TEA | If story touches UI + backend + performance |

**Decision Rule**:
- Use party mode when: **Multiple expert perspectives** provide value
- Don't use party mode when: **Single expertise** sufficient or **time-sensitive**

---

### Rubric 5.2: How Many Agents in Party Mode

| Scenario | Agent Count | Why |
|----------|-------------|-----|
| **Simple discussion** | 2 agents | Debate between two perspectives (e.g., PM + Architect) |
| **Standard collaboration** | 2-3 agents | Sweet spot (e.g., Architect + DEV + TEA for architecture review) |
| **Complex multi-faceted** | 3-4 agents | Multiple dimensions (e.g., PM + Architect + UX + TEA for product decision) |
| **Full retrospective** | All available agents | Comprehensive reflection |

**Pattern**: Start with 2-3 agents. BMad Master can add more if discussion reveals need.

---

## 6. Common Decision Patterns

### Pattern 6.1: "I Don't Know What to Do Next"

**Solution**:
1. Load ANY agent (doesn't matter which)
2. Run `*workflow-status`
3. Agent analyzes current project state
4. Agent recommends next workflow and agent to use

**Example**:
```
You: *workflow-status
PM: Analyzing project state...
    - PRD.md exists ✅
    - Architecture.md exists ✅
    - Epic files exist ✅
    - sprint-status.yaml missing ❌

    Recommendation: Run `*sprint-planning` with SM (Bob) to initialize sprint tracking.
```

---

### Pattern 6.2: "Should I Validate This Document?"

**Decision Criteria**:

**Always Validate**:
- First 3-5 projects using BMAD (learning standards)
- Critical projects (high rework cost)
- Unfamiliar domain

**Sometimes Validate**:
- Projects 6-10 (calibrating judgment)
- Medium-risk projects
- When uncertain about quality

**Rarely Validate**:
- After 10+ projects (confident)
- Low-risk projects
- Time-constrained

**OFAC Recommendation**: **ALWAYS validate** (Carlos learning BMAD)

---

### Pattern 6.3: "Which Track for This Project?"

**Keywords to Track Mapping**:

**Track 1 Indicators**:
- "fix bug in..."
- "add simple feature..."
- "update existing..."
- "change color of..."
- Scope fits in 1 sentence clearly

**Track 2 Indicators**:
- "build product..."
- "create platform..."
- "integrate system..."
- "add dashboard with..."
- Multiple interconnected features

**Track 3 Indicators**:
- "enterprise-grade..."
- "multi-tenant SaaS..."
- "HIPAA-compliant..."
- "SOC2 certified..."
- Compliance/security requirements

**When in Doubt**: Choose **Track 2** (over-plan slightly better than under-plan significantly)

---

### Pattern 6.4: "Can I Skip Architecture?"

**Yes, Skip If**:
- Track 1 project (Quick Flow)
- Level 0-2 (simple features)
- No architectural decisions needed
- Adding to well-established architecture

**No, Don't Skip If**:
- Track 2-3 project (BMad Method, Enterprise)
- Level 3-4 (architectural decisions required)
- Multiple tools/components
- Performance/security critical
- **OFAC case**: Don't skip (Level 3)

**Cost of Skipping When Needed**:
- DEV makes ad-hoc decisions
- Inconsistent code structure
- Tech debt accumulates
- Rework required

---

### Pattern 6.5: "How Do I Know When Story is Ready?"

**Story Ready Checklist**:
- [ ] Story file exists with tasks and acceptance criteria
- [ ] Story-context.xml assembled
- [ ] Story status == "ready" (in sprint-status.yaml)
- [ ] Dependencies resolved (prior stories complete if needed)
- [ ] DEV agent confirms readiness (refuses if not ready)

**If ANY checkbox false**: Story NOT ready, DEV will refuse to start

---

### Pattern 6.6: "Should I Run ATDD (Test-First)?"

**Yes, Use ATDD When**:
- Critical features (high-risk)
- Well-defined acceptance criteria
- TDD culture in team
- Learning TDD approach

**No, Skip ATDD When**:
- Exploratory implementation (figuring out approach)
- Prototype/throwaway code
- Time-constrained
- Tests better written during/after (integration tests, complex setup)

**OFAC Recommendation**: **Yes for Epic 1 (core engine)** - critical, well-defined. **Optional for Epic 2-3** - UI/integration tests often better after implementation.

---

## 7. Anti-Patterns to Avoid

### Anti-Pattern 7.1: Premature Architecture

❌ **Wrong**: Create Architecture.md before PRD.md
✅ **Right**: PRD first, then Architecture

**Why**: Architecture answers "how" - can't answer without knowing "what" (requirements)

---

### Anti-Pattern 7.2: Skipping Implementation Readiness

❌ **Wrong**: Create epics/stories, immediately start implementing
✅ **Right**: Run `*implementation-readiness` quality gate first

**Why**: Catches misalignments BEFORE costly implementation

---

### Anti-Pattern 7.3: DEV Starts Without Story Context

❌ **Wrong**: DEV starts implementing with just story title
✅ **Right**: SM runs `*story-context`, then DEV starts

**Why**: DEV needs complete context (story + epic + repo docs + dynamic context) for quality code

---

### Anti-Pattern 7.4: Marking Story Done Without All ACs Met

❌ **Wrong**: "90% done, good enough, marking done"
✅ **Right**: ALL acceptance criteria met, tests pass, review approved, THEN done

**Why**: "Done" means truly done. Incomplete stories accumulate tech debt.

---

### Anti-Pattern 7.5: No Testing Strategy

❌ **Wrong**: Skip `*framework`, add tests at end "if time"
✅ **Right**: TEA runs `*framework` before implementation, tests written alongside code

**Why**: "Add tests later" rarely happens. Framework upfront enables TDD.

---

## Summary: Your Decision-Making Framework

### Quick Reference

**When to use WHAT**:
1. **Unknown state**: ANY agent → `*workflow-status`
2. **Brownfield**: Analyst/Technical Writer → `*document-project`
3. **Greenfield**: PM → `*workflow-init`
4. **Complex planning**: PM → `*create-prd` (Track 2-3)
5. **Quick planning**: Principal Engineer → `*create-tech-spec` (Track 1)
6. **Architecture**: Architect → `*create-architecture` (Level 3-4 only)
7. **Story prep**: SM → `*create-story` + `*story-context`
8. **Implementation**: DEV → `*develop-story` + `*code-review` + `*story-done`
9. **Testing**: TEA → `*framework` (early) + `*automate` (periodic) + `*trace` (end)
10. **Multi-perspective**: BMad Master → `*party-mode`

**When to VALIDATE**:
- **Learning mode**: Always
- **Confident**: Critical docs only
- **Expert**: Rarely (quality internalized)

**When to use PARTY MODE**:
- Strategic decisions
- Retrospectives
- Creative brainstorming
- Course correction
- Complex cross-cutting stories

---

**Next Document**: BMAD_Learning_Journal.md (template for your observations during OFAC implementation)

---

**Document Metadata**

- **Created**: 2025-12-06
- **Author**: BMad Master Agent
- **Purpose**: Decision rubrics for agent and workflow selection
- **Audience**: Carlos (building judgment)
- **Part**: 3 of 5 (BMAD Learning Journey)
