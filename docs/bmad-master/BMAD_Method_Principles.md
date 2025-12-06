# BMAD Method Principles - Theoretical Foundation

**Purpose**: Comprehensive theoretical foundation for mastering the BMAD (Balanced Multi-Agent Development) Method
**Audience**: Carlos (learning BMAD as human expert)
**Created**: December 6, 2025
**Author**: BMad Master Agent

---

## Table of Contents

1. [What is BMAD?](#what-is-bmad)
2. [Core Philosophy](#core-philosophy)
3. [Fundamental Concepts](#fundamental-concepts)
4. [Agents vs Workflows](#agents-vs-workflows)
5. [Scale-Adaptive System](#scale-adaptive-system)
6. [The Three Tracks](#the-three-tracks)
7. [Agent Orchestration Patterns](#agent-orchestration-patterns)
8. [Story-Centric Implementation](#story-centric-implementation)
9. [BMAD Principles in Practice](#bmad-principles-in-practice)
10. [When to Use What](#when-to-use-what)

---

## What is BMAD?

### Definition

**BMAD (Balanced Multi-Agent Development)** is a comprehensive AI-assisted software development methodology that orchestrates specialized AI agents through structured workflows to guide projects from conception through implementation.

### Key Characteristics

1. **Multi-Agent System**: 13+ specialized AI agents, each with unique expertise, personality, and decision-making principles
2. **Workflow-Driven**: 34+ structured workflows across 4 phases + testing
3. **Scale-Adaptive**: Automatically adjusts planning depth based on project complexity (3 tracks)
4. **Story-Centric**: Implementation organized around user stories with just-in-time context
5. **Human-AI Partnership**: AI agents are expert collaborators, not code generators

### What BMAD is NOT

- ❌ **Not a code generator**: BMAD guides strategic decisions and executes with expertise
- ❌ **Not autopilot**: You make decisions, agents provide expert perspectives
- ❌ **Not one-size-fits-all**: Adapts to project complexity (bug fix to enterprise system)
- ❌ **Not just for greenfield**: Comprehensive brownfield (existing code) support

---

## Core Philosophy

### 1. AI Agents as Expert Collaborators

**Principle**: AI agents embody decades of simulated experience in their specialized roles.

**Implications**:
- **Trust their expertise**: Recommendations are data-informed, questions uncover critical issues
- **Answer their questions**: Incomplete answers lead to assumptions and suboptimal outcomes
- **Respect their boundaries**: Each agent has specific expertise; don't ask PM to write code
- **Leverage their memory**: Agents maintain context across the project lifecycle

**Example**: When PM asks "Have you validated these requirements with stakeholders?", it's not bureaucracy—it's preventing costly rework from misunderstood needs.

### 2. Right Planning Depth for Right Complexity

**Principle**: Not all projects need the same planning depth.

**The Problem BMAD Solves**:
- Traditional methodologies: Bug fix requires full design docs (over-planning)
- Or: Enterprise system built with minimal planning (under-planning)
- Result: Wasted time or costly rework

**BMAD Solution**: Scale-Adaptive System with 3 tracks
- **Quick Flow**: Tech-spec only for simple features (hours)
- **BMad Method**: PRD + Architecture for products (1-3 days)
- **Enterprise Method**: Extended planning for compliance/security needs (3-5 days)

**Key Insight**: Complexity drives planning depth, not story count or arbitrary rules.

### 3. Just-in-Time Context, Not Upfront Everything

**Principle**: Provide exactly the information needed, exactly when needed.

**Traditional Approach**:
- Write massive spec upfront
- Developers read 100+ pages
- Most context forgotten by implementation time
- Spec becomes outdated

**BMAD Approach**:
- **Epic-level context**: Optional high-level technical guidance (reusable across stories)
- **Story-level context**: Dynamic XML assembled when developer starts work
- **Repository docs**: Persisted patterns, conventions, architectural decisions
- **Agent memory**: Workflow tracking maintains state

**Benefits**:
- Reduced cognitive load (developer sees only what they need)
- Always current (assembled at implementation time)
- Better code quality (AI has complete, relevant context)

### 4. Story-Centric Implementation

**Principle**: User stories are the atomic unit of development.

**Story Lifecycle**:
```
backlog → drafted → ready → in-progress → review → done
```

**Each State Means**:
- **backlog**: Epic exists, story not yet created
- **drafted**: SM created story, not yet validated
- **ready**: Story validated, has context, approved for development
- **in-progress**: DEV implementing
- **review**: Implementation complete, under code review
- **done**: All acceptance criteria met, tests passing, merged

**Critical Rules**:
- DEV never starts until story Status == ready
- Story Context XML is single source of truth during implementation
- All acceptance criteria must be satisfied before marking done
- Tests must pass 100% before completion

### 5. Multi-Agent Collaboration via Party Mode

**Principle**: Complex problems benefit from multiple expert perspectives simultaneously.

**When Single Agent Insufficient**:
- Strategic decisions with trade-offs (performance vs maintainability)
- Creative brainstorming (multiple solution approaches)
- Cross-functional alignment (PM + Architect + UX must agree)
- Complex problem-solving (debugging architectural issues)

**Party Mode Mechanics**:
1. BMad Master loads agent manifest
2. User poses problem/question
3. Master orchestrates 2-3 relevant agents per message
4. Agents discuss, debate, propose solutions
5. Master summarizes when circular or consensus reached

**Example Use Cases**:
- Sprint retrospectives (all agents reflect on what worked)
- Architecture decisions (Architect + DEV + TEA collaborate)
- Creative ideation (Analyst + PM + Designer brainstorm)
- Course correction (PM + SM + Architect handle mid-sprint changes)

---

## Fundamental Concepts

### Agents

**Definition**: Specialized AI personas with unique expertise, communication style, and decision-making principles.

**Core Agent Roster** (13 total):
1. **Analyst** (Mary) - Requirements elicitation, research, brownfield analysis
2. **PM** (John) - PRD creation, epic/story breakdown, validation
3. **Architect** (Winston) - System design, technical decisions, implementation readiness
4. **SM** (Bob) - Sprint planning, story preparation, context assembly
5. **DEV** (Amelia) - Implementation, code review, story completion
6. **TEA** (Murat) - Test strategy, framework setup, quality gates
7. **UX Designer** (Sally) - User research, design thinking, UI/UX specifications
8. **Technical Writer** (Paige) - Documentation, diagrams, brownfield docs
9. **Principal Engineer** (Jordan) - Quick Flow solo dev, tech specs, rapid prototyping
10. **Game Designer** (Samus) - Game design, GDD, narrative
11. **Game Developer** (Link) - Game implementation
12. **Game Architect** (Cloud) - Game systems architecture
13. **BMad Master** - Meta-orchestration, party mode, task/workflow listing

**Key Characteristics**:
- Each has unique personality and communication style
- Domain expertise spans planning → architecture → implementation → testing
- Some are phase-specific (PM in Phase 2), others cross-cutting (TEA all phases)
- Can be customized per-project without modifying core files

### Workflows

**Definition**: Structured multi-step processes that guide specific tasks through completion.

**Workflow Structure**:
- **Entry point**: Trigger (e.g., `*create-prd`)
- **Steps**: Sequential or conditional instructions
- **Prompts**: Questions to gather necessary information
- **Templates**: Structured output formats
- **Validation**: Quality gates and completeness checks
- **Exit point**: Deliverable produced, next step recommended

**Workflow Categories**:
- **Phase 0**: Documentation (brownfield only) - 1 workflow
- **Phase 1**: Analysis (optional) - 5 workflows
- **Phase 2**: Planning (required) - 6 workflows
- **Phase 3**: Solutioning (Level 3-4 only) - 2 workflows
- **Phase 4**: Implementation (iterative) - 10 workflows
- **Testing**: Quality assurance (parallel) - 9 workflows

**Total**: 34+ workflows across BMM module

### Workflow vs Agent Relationship

**Mental Model**: Workflows are "scripts" that agents "perform"

- **Agent** = Actor with expertise and personality
- **Workflow** = Script with steps and deliverables
- **Relationship** = One workflow can be accessible to multiple agents

**Examples**:
- `workflow-status`: Available to ALL agents (universal)
- `create-prd`: Only PM agent
- `develop-story`: DEV and Game Developer agents
- `document-project`: Analyst and Technical Writer agents
- `correct-course`: PM, Architect, SM, Game Architect (cross-functional)

**Why This Matters**:
- You invoke workflows THROUGH agents (load agent, then run workflow)
- Same workflow may behave slightly differently based on agent's personality
- Multi-agent access indicates cross-functional nature of task

### Phases

**BMAD Development Lifecycle**:

**Phase 0: Documentation** (Brownfield Only)
- **Purpose**: Understand existing codebase before planning changes
- **Key Workflow**: `document-project`
- **Agent**: Analyst or Technical Writer
- **Output**: Comprehensive project documentation
- **When**: Always first step for brownfield projects

**Phase 1: Analysis** (Optional)
- **Purpose**: Brainstorming, research, strategic planning
- **Key Workflows**: `brainstorm-project`, `product-brief`, `research`
- **Agent**: Analyst, Game Designer
- **Output**: Product brief, research findings, strategic direction
- **When**: Uncertain scope, need market research, exploring solutions

**Phase 2: Planning** (Required)
- **Purpose**: Define requirements and user experience
- **Key Workflows**: `create-prd`, `tech-spec`, `create-ux-design`, `create-epics-and-stories`
- **Agents**: PM, UX Designer, Game Designer
- **Output**: PRD (or tech-spec), UX Design (if UI-heavy), Epics (NOT stories yet)
- **When**: Every project (track determines doc depth)

**Phase 3: Solutioning** (Level 3-4 Only)
- **Purpose**: Design system architecture
- **Key Workflows**: `create-architecture`, `implementation-readiness`
- **Agents**: Architect, Game Architect
- **Output**: Architecture.md with technical decisions
- **When**: Complex projects requiring architectural planning

**Phase 4: Implementation** (Iterative)
- **Purpose**: Build the system story-by-story
- **Key Workflows**: `sprint-planning`, `create-story`, `story-context`, `develop-story`, `code-review`, `story-done`
- **Agents**: SM, DEV, Game Developer
- **Output**: Working software, passing tests, completed stories
- **When**: After planning (and architecture if Level 3-4)

**Testing & QA** (Parallel to All Phases)
- **Purpose**: Quality assurance throughout lifecycle
- **Key Workflows**: `framework`, `atdd`, `automate`, `trace`, `ci`
- **Agent**: TEA
- **Output**: Test framework, automated tests, CI pipeline, traceability matrix
- **When**: Can start as early as Phase 1, continues through Phase 4

---

## Agents vs Workflows

### When to Think "Agent"

**Use Agent Mental Model When**:
- Choosing WHO to collaborate with
- Understanding communication styles
- Customizing personalities for your domain
- Organizing party mode discussions

**Questions to Ask**:
- "Who is the expert for this type of task?"
- "Which agent has the right perspective?"
- "What personality/style do I need right now?"

**Example**: "I need to design system architecture. Winston (Architect agent) is the expert."

### When to Think "Workflow"

**Use Workflow Mental Model When**:
- Executing specific tasks
- Following structured processes
- Understanding what deliverables are produced
- Checking what information is needed

**Questions to Ask**:
- "What process do I follow to create X?"
- "What steps are involved in Y?"
- "What outputs will I get from Z?"

**Example**: "I need to create architecture. I'll run the `create-architecture` workflow, which will ask questions, guide design decisions, and produce Architecture.md."

### The Synthesis

**How They Work Together**:

1. **You identify the task**: "I need to create a PRD"
2. **You choose the agent**: "PM (John) is the expert"
3. **You invoke the workflow**: `*create-prd`
4. **Agent performs workflow**: PM's expertise + workflow's structure = high-quality PRD
5. **You get deliverable**: PRD.md with FRs and NFRs

**Key Insight**: Agent provides expertise and personality; workflow provides structure and steps.

---

## Scale-Adaptive System

### The Problem

**Traditional Methodologies**:
- Bug fix → Full design docs required (wasteful over-planning)
- Enterprise system → Minimal planning (dangerous under-planning)
- One-size-fits-none approach

### BMAD Solution: Three Tracks

**Track Selection Based On**:
- Project complexity (not story count)
- Scope clarity (clear vs uncertain)
- Risk profile (simple vs enterprise)

### Track 1: Quick Flow

**Characteristics**:
- Planning: Tech-spec only (implementation-focused)
- Time: Hours to 1 day
- Story Count Guidance: 1-15 stories typically
- Agent: Principal Engineer (Quick Flow Solo Dev)
- Path: `Tech-Spec → Implement`

**Use For**:
- Bug fixes
- Simple features with clear scope
- Enhancements to existing systems
- Rapid prototyping

**AI Support Level**: Basic (minimal context)

**Trade-off**: Less planning = higher rework risk if complexity emerges

**Example**: "Fix authentication token expiration bug"

### Track 2: BMad Method (RECOMMENDED)

**Characteristics**:
- Planning: PRD + Architecture + UX (if UI)
- Time: 1-3 days of planning
- Story Count Guidance: 10-50+ stories typically
- Agents: PM, Architect, UX Designer, SM, DEV, TEA
- Path: `(Optional Analysis) → PRD → (Optional UX) → Architecture → Epics & Stories → Implement`

**Use For**:
- Products and platforms
- Multi-feature initiatives
- Complex additions to existing systems
- Major refactors or new modules

**AI Support Level**: Exceptional (complete context)

**Trade-off**: More upfront time for significantly reduced rework

**Examples**:
- "User dashboard with analytics and preferences"
- "Payment integration system"
- "Real-time collaboration features"

### Track 3: Enterprise Method

**Characteristics**:
- Planning: BMad Method + Security + DevOps + Compliance
- Time: 3-5 days of planning
- Story Count Guidance: 50+ stories typically
- Agents: All core agents + enterprise specialists
- Path: `BMad Method + Extended Planning Artifacts`

**Use For**:
- Enterprise systems
- Multi-tenant SaaS
- Compliance-heavy domains (healthcare, finance)
- Security-critical applications

**AI Support Level**: Maximum (enterprise-grade context)

**Trade-off**: Significant upfront investment for enterprise requirements

**Example**: "HIPAA-compliant patient portal with SSO and audit logging"

### How Track Selection Works

**Process** (via `workflow-init`):

1. **Description Analysis**: You describe your project
2. **AI Recommendation**: Based on complexity keywords, AI suggests track
3. **Educational Presentation**: All three tracks shown with examples
4. **User Choice**: You select the track that fits
5. **Workflow Path Set**: System routes you to appropriate workflows

**Key Principle**: System guides, user decides.

**Example Interaction**:
```
You: "Add user dashboard with analytics"
workflow-init: "Based on 'multiple features + system design', I recommend BMad Method (Track 2)"
You: "Sounds right"
workflow-init: "Great! Next: Create PRD with PM agent"
```

---

## The Three Tracks

### Quick Flow Track - Deep Dive

**Philosophy**: Ship fast, iterate quickly, minimal overhead

**When Perfect**:
- Scope is crystal clear
- Low technical risk
- Small surface area
- Fast feedback loop needed

**When Risky**:
- Scope ambiguous ("make it better")
- High technical complexity
- Many integration points
- Low tolerance for rework

**Workflow Sequence**:
```
1. (Brownfield: *document-project if needed)
2. Principal Engineer: *create-tech-spec
3. Principal Engineer: *quick-dev
4. Principal Engineer: *code-review
5. Done
```

**What You Get**:
- Tech-Spec.md (implementation-focused, no fluff)
- Working code with tests
- Fast delivery (hours to days)

**What You Don't Get**:
- Comprehensive requirements analysis
- Architectural design documents
- UX specifications
- Epic-level technical context

**Best Practice**: Use for ~80% of tasks (small features, bug fixes, quick adds)

### BMad Method Track - Deep Dive

**Philosophy**: Strategic planning enables autonomous AI execution

**When Perfect**:
- Building products or platforms
- Multiple interconnected features
- Architecture decisions needed
- High rework cost

**When Overkill**:
- Simple, isolated changes
- Proof-of-concept code
- Throwaway prototypes

**Workflow Sequence**:
```
1. (Brownfield: *document-project if needed)
2. (Optional) Analyst: *brainstorm-project or *product-brief
3. PM: *workflow-init
4. PM: *create-prd
5. (Optional) UX Designer: *create-ux-design
6. Architect: *create-architecture
7. PM: *create-epics-and-stories (AFTER architecture)
8. Architect: *implementation-readiness (validate)
9. SM: *sprint-planning
10. [Story Loop: *create-story → *story-context → *develop-story → *code-review → *story-done]
11. SM: *epic-retrospective
```

**What You Get**:
- PRD.md with FRs and NFRs
- Architecture.md with technical decisions
- UX Design (if UI components)
- Epic files (high-level grouping)
- Story files (implementation-ready)
- Complete context for AI agents

**What You Don't Get**:
- Extended enterprise artifacts (security models, compliance docs)
- Faster delivery than planning (upfront investment)

**Best Practice**: Use for ~15% of tasks (products, complex features, new systems)

### Enterprise Method Track - Deep Dive

**Philosophy**: Comprehensive planning for high-stakes systems

**When Perfect**:
- Enterprise customers
- Compliance requirements (HIPAA, SOC2, GDPR)
- Multi-tenant SaaS
- Security-critical systems

**When Overkill**:
- Internal tools
- MVPs and prototypes
- Startups without enterprise needs

**Workflow Sequence**:
```
BMad Method workflows +
- Security model documentation
- DevOps and deployment strategy
- Compliance checklist
- Multi-tenant architecture
- Audit logging requirements
- Performance and scale planning
```

**What You Get**:
- Everything from BMad Method
- Security architecture
- Compliance documentation
- Enterprise-grade planning artifacts

**What You Don't Get**:
- Fast delivery (significant upfront investment)
- Agile flexibility (more waterfall-like)

**Best Practice**: Use for ~5% of tasks (enterprise systems, compliance-heavy domains)

---

## Agent Orchestration Patterns

### Pattern 1: Sequential Hand-offs

**Definition**: Agent A completes work, explicitly hands off to Agent B.

**Example**: PM creates PRD → Hands off to Architect for system design

**Workflow**:
```
1. PM: *create-prd → Produces PRD.md
2. PM: "Winston, ready for architecture design"
3. Architect: *create-architecture → Produces Architecture.md
4. Architect: "John, ready to break into epics/stories"
5. PM: *create-epics-and-stories → Produces epic files
```

**When to Use**:
- Clear dependencies (B needs A's output)
- Phase transitions
- Quality gates (validation before next phase)

**Characteristics**:
- Explicit communication
- Clear deliverables
- Audit trail

### Pattern 2: Parallel Collaboration

**Definition**: Multiple agents work simultaneously on independent tasks.

**Example**: UX Designer creates mockups WHILE Architect designs backend

**Workflow**:
```
Concurrent:
- UX Designer: *create-ux-design → UI specifications
- Architect: *create-architecture → Backend design
Then:
- PM: *create-epics-and-stories (using BOTH outputs)
```

**When to Use**:
- Independent work streams
- Time-sensitive projects
- Specialized expertise needed simultaneously

**Characteristics**:
- Faster delivery
- Requires coordination
- Integration point at convergence

### Pattern 3: Iterative Refinement

**Definition**: Agent produces draft, another agent reviews/refines, repeat.

**Example**: DEV implements story → Code review finds issues → DEV fixes → Review again

**Workflow**:
```
1. DEV: *develop-story → Implementation (Run 1)
2. DEV: *code-review → Identifies 5 issues
3. DEV: *develop-story (Run 2, fix mode) → Fixes issues
4. DEV: *code-review → Clean, approved
5. DEV: *story-done
```

**When to Use**:
- Quality-critical deliverables
- Learning mode (review teaches patterns)
- Complex implementation

**Characteristics**:
- Multiple passes
- Quality improvement each iteration
- Higher time investment

### Pattern 4: Party Mode (Multi-Agent Simultaneous)

**Definition**: Multiple agents discuss problem simultaneously, moderated by BMad Master.

**Example**: Sprint retrospective with all agents reflecting

**Workflow**:
```
1. User or Agent: *party-mode
2. BMad Master: Loads 2-3 relevant agents
3. Agents discuss, debate, propose
4. Master summarizes or escalates more agents
5. Consensus or action plan emerges
```

**When to Use**:
- Strategic decisions (multiple perspectives needed)
- Brainstorming (creative solutions)
- Retrospectives (cross-functional reflection)
- Course correction (complex problems)

**Characteristics**:
- Rich discussion
- Multiple viewpoints
- Master moderation
- Circular detection and summarization

---

## Story-Centric Implementation

### Why Stories?

**Traditional Approach Problems**:
- Massive feature branches (merge hell)
- "Big bang" integration (high risk)
- Developer context overload (read entire spec)
- Stale documentation (out of sync with code)

**Story-Centric Benefits**:
- Small, mergeable increments
- Continuous integration
- Just-in-time context (only what's needed)
- Living documentation (story status tracks reality)

### Story Lifecycle

**States**:
```
backlog → drafted → ready → in-progress → review → done
```

**State Definitions**:

**backlog**:
- Epic exists
- Story not yet created
- Next candidate for SM to draft

**drafted**:
- SM created story file
- Has title, description, tasks, acceptance criteria
- NOT yet validated or approved
- No context XML yet

**ready**:
- Story validated (optional `validate-create-story`)
- Story context XML assembled (via `story-context`)
- Approved for development
- DEV can start work

**in-progress**:
- DEV actively implementing
- Tasks being completed
- Tests being written
- Code being committed

**review**:
- Implementation complete per DEV
- Code review in progress
- May return to in-progress if issues found

**done**:
- All acceptance criteria met
- Tests passing 100%
- Code review approved
- Merged to main branch
- Sprint status updated

### Story Context XML

**Purpose**: Provide AI agents with complete, relevant context at implementation time.

**Contents**:
```xml
<story-context>
  <story>
    <!-- Story title, description, tasks, acceptance criteria -->
  </story>
  <epic-context>
    <!-- Optional: Epic-level technical guidance (reusable) -->
  </epic-context>
  <repository-docs>
    <!-- Patterns, conventions, architectural decisions (persisted) -->
  </repository-docs>
  <dynamic-context>
    <!-- Files, functions, patterns relevant to THIS story (assembled just-in-time) -->
  </dynamic-context>
</story-context>
```

**Key Principles**:
- **Single source of truth**: DEV reads ONLY story context XML
- **Just-in-time assembly**: Created when DEV starts work (always current)
- **Right-sized**: Only information needed for THIS story
- **Reusable**: Epic context shared across stories in same epic
- **Persisted**: Repository docs survive across epics

**Workflow**:
1. SM: `*create-story` → Produces story-XXX.md file
2. SM: `*story-context` → Produces story-XXX-context.xml
3. DEV loads story context XML (automatically or manually)
4. DEV: `*develop-story` → Uses context to implement
5. Story context ensures AI has perfect information

---

## BMAD Principles in Practice

### Principle 1: Load Resources at Runtime, Never Pre-Load

**What It Means**: Agents don't pre-load all project files. They load exactly what's needed when needed.

**Why It Matters**:
- **Performance**: Faster agent loading (no massive context upfront)
- **Relevance**: Only relevant information considered
- **Accuracy**: No outdated cached information

**Example**:
- ❌ **Wrong**: SM loads all 50 stories to create next story
- ✅ **Right**: SM loads epic file, finds next story in backlog, loads only that story

### Principle 2: Present Numbered Lists for User Choices

**What It Means**: When user has choices, always present numbered list.

**Why It Matters**:
- **Clarity**: Unambiguous selection
- **Efficiency**: User can say "3" instead of typing full option
- **Discoverability**: User sees all options

**Example**:
```
BMad Master presents:
1. List Available Tasks
2. List Workflows
3. Group chat with all agents
4. Dismiss Agent

User: 3
(Party mode activated)
```

### Principle 3: Validation is Optional, But Recommended

**What It Means**: Most workflows have optional validation workflows. You decide when to use them.

**When to Validate**:
- **Learning BMAD**: Understand what "good" looks like
- **Critical documents**: PRD before architecture, architecture before implementation
- **Phase transitions**: Before advancing to next phase
- **High-stakes projects**: When mistakes are costly

**When to Skip**:
- **Time pressure**: Validation takes extra time
- **Confident**: You've done this many times
- **Low risk**: Mistakes are cheap to fix

**Example**:
```
PM: *create-prd → Produces PRD.md
(Optional) PM: *validate-prd → Reviews PRD for completeness
Architect: *create-architecture → Uses PRD as input
```

### Principle 4: Agents Ask Questions for Good Reasons

**What It Means**: When an agent asks a question, it's to prevent a real problem.

**Why They Ask**:
- **Uncover hidden requirements**: PM asks "Who are the users?" to ensure you've thought about personas
- **Prevent rework**: Architect asks "What's your scale target?" to avoid over/under-engineering
- **Ensure quality**: TEA asks "What's your risk tolerance?" to calibrate test depth

**How to Respond**:
- **Answer honestly**: "I don't know" is valid (prompts research)
- **Provide context**: Why you're asking for this feature
- **Ask clarifying questions**: "Why does that matter?" helps you learn

**Example**:
```
PM: "Have you validated these requirements with stakeholders?"
You (honest): "Not yet, but I'm the stakeholder"
PM: "Got it. For a company-wide tool, I'd recommend validation. For a personal tool, we can proceed."
```

### Principle 5: Tests Are Not Overhead, They Are Feature Work

**What It Means**: Writing tests is part of implementing the feature, not a separate burden.

**Why It Matters**:
- **Quality**: Untested code is not "done"
- **Confidence**: Tests prove acceptance criteria met
- **Regression prevention**: Tests catch future breaks
- **Documentation**: Tests show how code should work

**How BMAD Enforces**:
- DEV cannot mark story done until tests pass 100%
- Story context includes testing requirements
- Code review checks test coverage
- No cheating or lying about test results

**Example**:
```
Story: "Add password reset via email"
Acceptance Criteria:
- AC1: User receives email with reset link
- AC2: Link expires after 1 hour
- AC3: Invalid link shows error message

Tests Required:
- Test AC1: Assert email sent with correct link
- Test AC2: Assert link invalid after 61 minutes
- Test AC3: Assert error shown when link invalid
```

---

## When to Use What

### Decision Matrix: Agent Selection

| Situation | Agent to Use | Rationale |
|-----------|--------------|-----------|
| **Need to brainstorm project ideas** | Analyst (Mary) | Brainstorming expert, creative exploration |
| **Need market/competitive research** | Analyst (Mary) | Research specialist |
| **Have existing code, need docs** | Analyst or Technical Writer | Brownfield documentation experts |
| **Need to create PRD** | PM (John) | Requirements specialist |
| **Need to create tech-spec (quick)** | Principal Engineer (Jordan) or PM | Quick Flow experts |
| **Need to break PRD into epics/stories** | PM (John) | Epic/story breakdown specialist |
| **Need system architecture** | Architect (Winston) | System design expert |
| **Need UX design** | UX Designer (Sally) | User experience specialist |
| **Need to prepare stories for dev** | SM (Bob) | Story context assembly expert |
| **Need to implement story** | DEV (Amelia) | Implementation expert |
| **Need code review** | DEV (Amelia) or Principal Engineer | Code quality experts |
| **Need test strategy** | TEA (Murat) | Testing expert |
| **Need diagrams/docs** | Technical Writer (Paige) | Documentation and visualization expert |
| **Need multi-perspective discussion** | BMad Master (party mode) | Orchestrates multiple agents |
| **Lost, don't know what to do** | ANY agent → `*workflow-status` | Analyzes state, recommends next step |

### Decision Matrix: Workflow Selection

| Goal | Workflow to Use | Agent | Rationale |
|------|-----------------|-------|-----------|
| **Initialize project tracking** | `*workflow-init` | PM, Analyst, Game Designer | Sets up workflow path |
| **Document existing codebase** | `*document-project` | Analyst, Technical Writer | Brownfield prerequisite |
| **Create requirements doc** | `*create-prd` | PM | Level 2-4 planning |
| **Create quick tech-spec** | `*create-tech-spec` | Principal Engineer or PM | Level 0-1 planning |
| **Design system architecture** | `*create-architecture` | Architect | Level 3-4 only |
| **Create UX design** | `*create-ux-design` | UX Designer | UI-heavy projects |
| **Break PRD into epics/stories** | `*create-epics-and-stories` | PM | After architecture |
| **Validate ready for implementation** | `*implementation-readiness` | Architect | Phase 3 → 4 gate |
| **Initialize sprint tracking** | `*sprint-planning` | SM | Once per project |
| **Create next story** | `*create-story` | SM | Per-story basis |
| **Assemble story context** | `*story-context` | SM | Before dev starts |
| **Implement story** | `*develop-story` | DEV | Per-story basis |
| **Review story code** | `*code-review` | DEV | After implementation |
| **Mark story complete** | `*story-done` | DEV | After review passes |
| **Initialize test framework** | `*framework` | TEA | Once per project, early |
| **Write tests before implementation** | `*atdd` | TEA | Test-first approach |
| **Create comprehensive test suite** | `*automate` | TEA | After features implemented |
| **Validate requirements → tests mapping** | `*trace` | TEA | Quality gate |
| **Setup CI/CD pipeline** | `*ci` | TEA | DevOps integration |
| **Handle mid-sprint changes** | `*correct-course` | PM, Architect, SM | Change management |
| **Reflect on completed epic** | `*epic-retrospective` | SM | After epic done |
| **Multi-agent discussion** | `*party-mode` | BMad Master | Strategic decisions |

### Decision Tree: Which Track?

```
START: Describe your project
  ↓
Is it a bug fix or simple feature?
  ├─ YES → Is scope crystal clear?
  │         ├─ YES → Quick Flow (Tech-spec only)
  │         └─ NO → BMad Method (PRD + Architecture)
  └─ NO → Does it have enterprise/compliance needs?
            ├─ YES → Enterprise Method (Extended planning)
            └─ NO → Is it a product/platform or complex feature?
                      ├─ YES → BMad Method (PRD + Architecture)
                      └─ NO → Quick Flow (Tech-spec only)
```

### Common Patterns by Project Type

**Bug Fix**:
```
1. (Optional) Analyst: *document-project (if unfamiliar codebase)
2. Principal Engineer: *create-tech-spec
3. Principal Engineer: *quick-dev
4. Principal Engineer: *code-review
```

**Simple Feature (Clear Scope)**:
```
1. Principal Engineer: *create-tech-spec
2. Principal Engineer: *quick-dev
3. TEA: *atdd (optional, for critical features)
4. Principal Engineer: *code-review
```

**Product/Platform (Greenfield)**:
```
1. Analyst: *brainstorm-project (optional)
2. PM: *workflow-init
3. PM: *create-prd
4. UX Designer: *create-ux-design (if UI-heavy)
5. Architect: *create-architecture
6. PM: *create-epics-and-stories
7. Architect: *implementation-readiness
8. TEA: *framework
9. SM: *sprint-planning
10. [Story loop: SM creates → DEV implements → TEA tests]
```

**Complex Addition (Brownfield)**:
```
1. Analyst: *document-project
2. PM: *workflow-init
3. PM: *create-prd
4. Architect: *create-architecture
5. PM: *create-epics-and-stories
6. SM: *sprint-planning
7. [Story loop]
```

---

## Summary: Key Takeaways

### The Essence of BMAD

1. **Multi-Agent Collaboration**: 13+ specialized AI experts, each with unique expertise
2. **Workflow-Driven**: 34+ structured processes guide tasks to completion
3. **Scale-Adaptive**: 3 tracks (Quick Flow, BMad Method, Enterprise) adapt to complexity
4. **Story-Centric**: Just-in-time context enables autonomous AI execution
5. **Human-AI Partnership**: You decide strategy, AI executes with expertise

### When BMAD Shines

- ✅ **Products and platforms** requiring comprehensive planning
- ✅ **Complex features** with architectural implications
- ✅ **Brownfield codebases** needing documentation before changes
- ✅ **Quality-critical systems** requiring thorough testing
- ✅ **Multi-phase projects** benefiting from structured approach

### When BMAD May Be Overkill

- ❌ **Trivial changes** (1-line fixes)
- ❌ **Throw-away prototypes** (POC code)
- ❌ **Experimental code** (learning/exploration)
- ❌ **Non-software projects** (BMAD is software-focused)

### How to Master BMAD

1. **Understand principles** (this document)
2. **Follow roadmap** (next document: OFAC_BMAD_Roadmap.md)
3. **Use decision rubrics** (document 3: BMAD_Agent_Decision_Rubrics.md)
4. **Document observations** (document 4: BMAD_Learning_Journal.md)
5. **Extract patterns** (document 5: BMAD_Project_Retrospective.md)

---

**Next**: Proceed to `OFAC_BMAD_Roadmap.md` for the phase-by-phase implementation plan with Level 3 rationale.

---

**Document Metadata**

- **Created**: 2025-12-06
- **Author**: BMad Master Agent
- **Purpose**: Theoretical foundation for BMAD mastery
- **Audience**: Carlos (human expert learner)
- **Part**: 1 of 5 (BMAD Learning Journey)
