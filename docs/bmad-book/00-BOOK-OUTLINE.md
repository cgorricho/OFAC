# BMAD Method: AI-Assisted Agile Development
## From Theory to Practice - A Comprehensive Guide

**Author:** Carlos Gorricho  
**Working Title:** BMAD Method: AI-Assisted Agile Development in Practice  
**Subtitle:** Building Production Software with Specialized AI Agents

---

## Research Summary

### Publication Status (December 2025)
**✅ CONFIRMED: No existing BMAD Method books**
- GitHub repository (19 agents, 50+ workflows, MIT license)
- Medium articles and blog posts (Courtlin Holt-Nguyen, Steve Kaplan, Lakshmi Narayana)
- Community adoption (Discord, multiple implementations)
- **NO published books** - first-mover opportunity

### Target Publishers & Platforms

#### Tier 1: Traditional Technical Publishers
1. **Pragmatic Bookshelf** ⭐ (BEST FIT)
   - Founded by Andy Hunt & Dave Thomas (Agile Manifesto co-authors)
   - Focus: "Books by developers for developers"
   - DRM-free, beta book model
   - 50% profit split (vs 7-15% revenue elsewhere)
   - Perfect alignment: Agile methodology book from practitioners
   - Contact: Submit through pragprog.com

2. **O'Reilly Media**
   - Industry leader, highest credibility
   - Best-case royalties: ~$100-200K lifetime for successful titles
   - Strict editorial process, high bar
   - Strong distribution network

3. **Manning Publications**
   - Technical depth focus
   - MEAP (Manning Early Access Program) beta readers
   - Historical figures on covers
   - Strong community engagement

#### Tier 2: Self-Publishing (Faster to Market)
1. **Leanpub** ⭐ (RECOMMENDED FOR MVP)
   - Write-in-progress model (publish chapters as you write)
   - 80% royalties (author keeps most revenue)
   - Markdown-based workflow
   - Built-in reader feedback loop
   - Perfect for validating market interest before pitching to traditional publishers

2. **Gumroad**
   - Direct sales to audience
   - 90% royalties
   - Full pricing control

### Successful Methodology Book Patterns

Based on analysis of "Agile Manifesto," "The Pragmatic Programmer," and modern AI development books:

#### Structure Pattern: "Theory → Practice → Case Study"
1. **Part 1: Foundations** (30% of book)
   - Problem statement (why existing approaches fail)
   - Philosophical principles
   - Core concepts and terminology
   - Mental models

2. **Part 2: The Method** (40% of book)
   - Detailed workflows
   - Agent roles and responsibilities
   - Decision frameworks
   - Practical patterns

3. **Part 3: Real-World Application** (30% of book)
   - Complete project walkthrough
   - Challenges and solutions
   - Lessons learned
   - Templates and tools

#### Key Success Factors
- **Actionable immediately**: Readers can apply principles same day
- **Real examples**: Not hypothetical - actual production code
- **Visual workflows**: Diagrams explain 90% of confusion
- **Progressive disclosure**: Simple → Complex
- **Defensible claims**: Back assertions with evidence

---

## Book Outline

### Front Matter
- Title Page
- Copyright Notice & Legal
  * Book Copyright: © Carlos Gorricho, [Year]
  * BMAD Method Framework: MIT License (open source)
  * Trademarks: BMAD™ and BMAD-METHOD™ are trademarks of BMad Code, LLC (used with permission/fair use for educational purposes)
  * Acknowledgment: "This book documents the BMAD Method framework (https://github.com/bmad-code-org/BMAD-METHOD), released under MIT License. The framework is free and open source. BMAD™ and BMAD-METHOD™ are trademarks of BMad Code, LLC."
- Dedication
- Foreword (invite BMad Code founder if possible)
- Preface: Why This Book Exists
- About the Author
- How to Read This Book
- Acknowledgments

---

## PART 1: THE BMAD METHOD - Foundations

**Goal**: Establish theoretical foundation, philosophy, and core concepts

### Chapter 1: The AI Development Crisis
**Purpose**: Problem statement - why traditional AI-assisted development fails

- **1.1 The Promise vs Reality of AI Coding**
  - Ad-hoc prompting chaos ("jazz improvisation vs symphony orchestra")
  - Context loss between sessions
  - Inconsistent planning and documentation
  - Lack of structured handoffs

- **1.2 What Doesn't Work**
  - Treating AI as "fancy autocomplete"
  - Generic task runners without domain expertise
  - One-size-fits-all planning (bug fix = same docs as enterprise system)
  - Autopilot mentality (over-reliance without human judgment)

- **1.3 The Cost of Chaos**
  - Time wasted: $50K-$200K burned before first product
  - Planning inconsistency leads to costly rework
  - Developer cognitive overload from 100+ page specs
  - Mission-critical errors from context gaps

- **1.4 Enter BMAD: A Different Approach**
  - AI agents as expert collaborators, not code generators
  - Workflow-driven, scale-adaptive methodology
  - Story-centric implementation with just-in-time context
  - Human-AI partnership model

### Chapter 2: Core Philosophy
**Purpose**: Establish foundational principles that drive all BMAD decisions

- **2.1 AI Agents as Expert Collaborators**
  - Decades of simulated experience in specialized roles
  - Trust expertise, answer questions fully
  - Respect boundaries (PM doesn't write code)
  - Leverage persistent memory across lifecycle

- **2.2 Right Planning Depth for Right Complexity**
  - The over-planning / under-planning problem
  - Scale-Adaptive System: 3 tracks (Quick Flow, BMad Method, Enterprise)
  - Complexity drives planning depth, not story count
  - Efficiency without sacrificing quality

- **2.3 Just-in-Time Context, Not Upfront Everything**
  - Traditional approach: Massive spec upfront, forgotten by implementation
  - BMAD approach: Dynamic context assembly when needed
  - Epic-level + story-level context + repository patterns
  - Reduced cognitive load, always current

- **2.4 Story-Centric Implementation**
  - User stories as atomic unit of development
  - Lifecycle: backlog → drafted → ready → in-progress → review → done
  - Story Context XML is single source of truth
  - All acceptance criteria must pass

- **2.5 Multi-Agent Collaboration (Party Mode)**
  - Complex problems need multiple perspectives
  - Orchestrated debates and brainstorming
  - When consensus reached, master summarizes
  - Cross-functional alignment

### Chapter 3: The Agent Roster
**Purpose**: Meet the 13+ specialized AI agents and their expertise

- **3.1 Planning Phase Agents**
  - **Analyst (Mary)**: Research, brownfield analysis, brainstorming
  - **PM (John)**: PRD creation, epic/story breakdown, validation
  - **UX Designer (Sally)**: User research, design thinking, UI/UX specs

- **3.2 Architecture Phase Agents**
  - **Architect (Winston)**: System design, technical decisions, readiness validation
  - **Game Architect (Cloud)**: Game-specific systems architecture

- **3.3 Implementation Phase Agents**
  - **SM (Bob)**: Sprint planning, story preparation, context assembly
  - **DEV (Amelia)**: Implementation, code review, story completion
  - **Principal Engineer (Jordan)**: Quick Flow solo dev, tech specs
  - **Game Developer (Link)**: Game implementation

- **3.4 Quality Assurance Agents**
  - **TEA (Murat)**: Test strategy, framework setup, NFR validation

- **3.5 Documentation & Orchestration**
  - **Technical Writer (Paige)**: Documentation, diagrams, brownfield docs
  - **Game Designer (Samus)**: Game design, GDD, narrative
  - **BMad Master**: Meta-orchestration, party mode, workflow listing

- **3.6 Agent Customization**
  - Personality and communication style
  - Domain expertise boundaries
  - Project-specific customization without modifying core

### Chapter 4: The Three Tracks
**Purpose**: Explain scale-adaptive system - different projects need different planning

- **4.1 Understanding Project Complexity**
  - Complexity levels 0-4
  - Why one-size-fits-all fails
  - Matching track to project characteristics

- **4.2 Track 1: Quick Flow (Hours)**
  - Simple features, clear scope
  - Tech-spec only (no PRD or architecture)
  - Principal Engineer or PM solo
  - When to use: Bug fixes, simple features, prototypes

- **4.3 Track 2: BMad Method (1-3 Days)**
  - Complex projects, interconnected features
  - PRD + optional architecture (Level 3-4 only)
  - Full agent team collaboration
  - When to use: Products, platforms, SaaS applications

- **4.4 Track 3: Enterprise Method (3-5 Days)**
  - Enterprise needs, compliance, security
  - Extended planning artifacts
  - Architecture mandatory
  - When to use: Multi-tenant systems, regulated industries

- **4.5 Decision Framework: Which Track?**
  - Use `*workflow-init` to analyze project
  - Complexity indicators and triggers
  - Trade-offs between speed and thoroughness

### Chapter 5: Workflows - The Orchestrated Process
**Purpose**: Introduce workflow system - structured multi-step processes

- **5.1 What is a Workflow?**
  - Entry point triggers (e.g., `*create-prd`)
  - Sequential or conditional steps
  - Prompts to gather information
  - Templates for structured output
  - Validation and quality gates
  - Exit point with deliverable

- **5.2 Workflow Categories**
  - Phase 0: Documentation (brownfield) - 1 workflow
  - Phase 1: Analysis (optional) - 5 workflows
  - Phase 2: Planning (required) - 6 workflows
  - Phase 3: Solutioning (Level 3-4 only) - 2 workflows
  - Phase 4: Implementation (iterative) - 10 workflows
  - Testing: Quality assurance (parallel) - 9 workflows
  - **Total**: 34+ workflows

- **5.3 Workflow vs Agent Relationship**
  - Mental model: Workflows are "scripts" that agents "perform"
  - Agent = Actor with expertise and personality
  - Workflow = Role-specific process with steps
  - Same workflow run by different agents (e.g., `*create-tech-spec`)

- **5.4 Key Workflows Deep Dive**
  - `*workflow-init`: Project classification and track selection
  - `*create-prd`: Requirements documentation
  - `*create-architecture`: System design
  - `*create-story`: Story preparation
  - `*develop-story`: Implementation
  - `*workflow-status`: "Where am I?" navigation

### Chapter 6: The Development Lifecycle
**Purpose**: Walk through complete BMAD development cycle end-to-end

- **6.1 Phase 0: Brownfield Documentation (If Existing Code)**
  - `*document-project` workflow
  - Analyst or Technical Writer
  - Generate codebase context for AI understanding

- **6.2 Phase 1: Analysis (Optional Discovery)**
  - `*brainstorm-project`: Idea generation
  - `*product-brief`: Strategic planning
  - `*research`: Market/competitive/technical analysis
  - When to skip vs invest time

- **6.3 Phase 2: Planning (Required)**
  - Track 1: `*create-tech-spec` (Principal Engineer/PM)
  - Track 2-3: `*create-prd` (PM)
  - `*create-ux-design` (UX Designer for UI projects)
  - `*validate-prd` (optional quality check)

- **6.4 Phase 3: Solutioning (Level 3-4 Only)**
  - `*create-architecture` (Architect)
  - `*validate-architecture` (optional)
  - `*create-epics-and-stories` (PM)
  - `*implementation-readiness` (quality gate)

- **6.5 Phase 4: Implementation (Iterative)**
  - `*sprint-planning` (SM - once per project)
  - `*framework` (TEA - setup test infrastructure)
  - **Story Loop** (repeat for all stories):
    1. `*create-story` (SM)
    2. `*story-context` (SM - assemble dynamic context)
    3. `*develop-story` (DEV - implement)
    4. `*code-review` (DEV/Principal Engineer)
    5. `*story-done` (DEV - mark complete)
  
- **6.6 Testing (Parallel to Implementation)**
  - `*atdd`: Test-first before code (optional)
  - `*automate`: Comprehensive test suite (every 3-4 stories)
  - `*trace`: Requirements traceability (per epic or end)
  - `*ci`: Continuous integration pipeline (once)
  - `*nfr-assess`: Non-functional requirements validation (end)

- **6.7 Change Management**
  - `*correct-course`: Mid-sprint requirement changes
  - `*epic-retrospective`: Reflect after each epic
  - `*party-mode`: Multi-agent strategic discussions

---

## PART 2: THE OFAC PROJECT - Real-World Application

**Goal**: Complete case study demonstrating BMAD Method in production

### Chapter 7: Project Context - OFAC Sanctions Screening
**Purpose**: Introduce the real-world problem and requirements

- **7.1 The Problem**
  - Humanitarian NGOs need OFAC sanctions screening for grant beneficiaries
  - U.S. Treasury removed free bulk screening capability
  - Commercial tools cost $2K-$10K/year for low-volume use (250-500 screenings/year)
  - Manual screening: 30-60 seconds per organization, 6-8 hours per grant round

- **7.2 The Solution Vision**
  - Phase 1: API-first screening service + Streamlit web app (internal MVP)
  - Phase 1.5: Optional Excel custom function
  - Phase 2: Commercial SaaS for peer NGOs (if validated)
  - Fuzzy matching, humanitarian context intelligence, audit trails

- **7.3 Technical Scope**
  - FastAPI screening service (RESTful API)
  - Streamlit batch processing web app
  - OFAC CSV triplets (SDN + ALT + ADD: 18,422 entities, 20,104 aliases)
  - RapidFuzz matching engine (85% threshold, country-aware)
  - Daily OFAC update checks (2-3x/week update frequency)
  - Syria General License 21 humanitarian context detection

- **7.4 Success Criteria**
  - Cost avoidance: $2K-$10K/year eliminated
  - Time savings: 70% reduction (6-8 hours → <2 hours)
  - Zero false negatives (compliance risk avoidance)
  - Audit acceptance: Reports pass external review first submission
  - Fuzzy matching value: At least 1 variant name caught in 6 months

### Chapter 8: Phase 0 & 1 - Discovery and Planning
**Purpose**: Demonstrate Analysis and Planning workflows with real artifacts

- **8.1 Initial Brainstorming**
  - User request: "Create simple web app for OFAC screening"
  - Clarifying questions from Analyst
  - Decision to build two tools: Streamlit + Excel UDF

- **8.2 Product Brief Creation**
  - `*product-brief` workflow execution
  - Strategic vision document (954 lines)
  - Problem statement: Treasury removed bulk screening, commercial tools too expensive
  - Target user persona: Carlos Martinez - multi-hat compliance officer at mid-sized NGO
  - Key differentiators: Humanitarian context awareness, cost savings, compliance-first design

- **8.3 PRD Development**
  - `*create-prd` workflow with PM agent
  - Comprehensive Product Requirements Document (610 lines)
  - Project classification: High-complexity GovTech/API Backend
  - User success criteria: "Sleep at night" confidence factor
    - Match score transparency
    - OFAC version tracking
    - Spot-check validation capability
    - Board-ready documentation
  - Business success: Phase 1 validation gate (Month 6), Phase 2 commercial decision (Month 12)
  - Technical architecture: FastAPI + Streamlit + shared ofac_matcher.py module

- **8.4 Workflow Status Tracking**
  - `bmm-workflow-status.yaml` creation (135 lines)
  - BMAD methodology workflow tracking
  - Selected track: "method" (greenfield project)
  - Project constraints documented: Sample data format, reference docs, technical requirements

- **8.5 Lessons from Planning Phase**
  - Importance of user persona development
  - Balancing internal MVP vs commercial vision
  - Capturing compliance/audit requirements upfront
  - Humanitarian context as competitive differentiator

### Chapter 9: Phase 2 - Conceptual Design & Research
**Purpose**: Show how BMAD handles deep technical research and analysis

- **9.1 Data Schema Analysis**
  - Workflow: Deep dive into OFAC data structures
  - `20251206_OFAC_Data_Schemas_Analysis_and_Recommendations.md` (482 lines)
  - Decision: CSV triplets over XML for simplicity
  - Key findings:
    - SDN.CSV: 18,422 entities
    - ALT.CSV: 20,104 alternate names
    - ADD.CSV: 24,170 addresses
  - Matching strategy: RapidFuzz with token_sort_ratio, country-aware scoring

- **9.2 OFAC Update Policies Research**
  - Workflow: Regulatory compliance analysis
  - `20251206_OFAC_List_Update_Policies_and_Strategy.md` (712 lines)
  - Findings: OFAC updates 2-3x per week, 166 updates in 2024
  - Strategy: Daily automated checks, atomic download/swap, warn if >7 days old

- **9.3 Initial Technical Plan**
  - `20251205_OFAC_Sanctions_Screening_Tools_Plan.md` (224 lines)
  - Architecture decisions:
    - Shared ofac_matcher.py module for both Streamlit and Excel
    - Local cache in data/ directory (excluded from git)
    - Humanitarian aid detection: Syria General License 21
    - Performance target: <30 seconds for 100 entries

- **9.4 Documentation Reorganization**
  - Created `docs/analysis/` for strategic planning
  - Created `docs/conceptual-design/` for technical planning
  - Version control: Git commits with extensive documentation
  - GitHub repository creation: https://github.com/cgorricho/OFAC

- **9.5 Lessons from Research Phase**
  - Don't skip deep dives on critical decisions (CSV vs XML)
  - Regulatory compliance research prevents costly rework
  - Document decisions for future reference
  - Git history as project narrative

### Chapter 10: Phase 3 - Architecture & Solutioning
**Purpose**: Demonstrate solutioning workflows for complex projects (Level 3-4)

- **10.1 System Architecture**
  - `*create-architecture` workflow
  - [TO BE CREATED DURING OFAC PROJECT]
  - Component breakdown:
    - Core: ofac_matcher.py (fuzzy matching engine)
    - Data layer: OFAC list management, version tracking
    - API service: FastAPI endpoints (single, batch screening)
    - Frontend: Streamlit web app
    - Optional: Excel UDF
  - Integration patterns
  - Security and compliance considerations

- **10.2 Epic and Story Breakdown**
  - `*create-epics-and-stories` workflow with PM
  - [TO BE CREATED DURING OFAC PROJECT]
  - Epic structure:
    - Epic 1: Core Matching Engine
    - Epic 2: OFAC Data Management
    - Epic 3: API Service Layer
    - Epic 4: Streamlit Web Application
    - Epic 5: Humanitarian Context Detection
    - Epic 6: Reporting and Audit Trail
    - Epic 7: Testing and Quality Assurance
  - Story sizing and prioritization
  - Acceptance criteria templates

- **10.3 Implementation Readiness Validation**
  - `*implementation-readiness` workflow with Architect
  - Quality gate before Phase 4
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - Checklist:
    - PRD complete and validated
    - Architecture documented
    - All epics and stories defined
    - Technical dependencies identified
    - Test strategy in place

- **10.4 Lessons from Solutioning Phase**
  - Value of architecture for complex projects
  - Story breakdown prevents "analysis paralysis"
  - Implementation readiness as quality gate
  - Balance between planning and action

### Chapter 11: Phase 4 - Implementation (Part 1: Sprint Setup)
**Purpose**: Show sprint planning and test framework setup

- **11.1 Sprint Planning**
  - `*sprint-planning` workflow with SM
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - Sprint structure and cadence
  - Story prioritization
  - Sprint tracking mechanisms

- **11.2 Test Framework Setup**
  - `*framework` workflow with TEA
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - pytest configuration
  - Test data fixtures
  - Mocking OFAC data for tests
  - CI/CD pipeline design

- **11.3 Repository Structure**
  - Directory organization
  - Configuration management
  - Documentation standards
  - Git workflow and branching strategy

### Chapter 12: Phase 4 - Implementation (Part 2: Story Loop)
**Purpose**: Demonstrate complete story lifecycle multiple times

- **12.1 Story Example 1: Core Fuzzy Matching**
  - `*create-story`: SM prepares story
  - `*story-context`: Dynamic context assembly
  - `*develop-story`: DEV implements
  - `*code-review`: Senior review
  - `*story-done`: Mark complete
  - [ACTUAL CODE AND ARTIFACTS FROM OFAC PROJECT]

- **12.2 Story Example 2: OFAC Data Download**
  - Full lifecycle with different challenges
  - Handling network failures
  - Atomic swap mechanism
  - [ACTUAL CODE AND ARTIFACTS FROM OFAC PROJECT]

- **12.3 Story Example 3: Humanitarian Context Detection**
  - Business logic complexity
  - Syria General License 21 detection
  - Edge cases and testing
  - [ACTUAL CODE AND ARTIFACTS FROM OFAC PROJECT]

- **12.4 Story Example 4: Streamlit UI - Upload Widget**
  - Frontend development
  - User experience considerations
  - File validation
  - [ACTUAL CODE AND ARTIFACTS FROM OFAC PROJECT]

- **12.5 Common Patterns in Story Implementation**
  - Context assembly reduces developer cognitive load
  - Code review catches issues early
  - Acceptance criteria as definition of done
  - Iterative refinement through feedback

### Chapter 13: Testing and Quality Assurance
**Purpose**: Show parallel testing workflows in action

- **13.1 Test-Driven Development with ATDD**
  - `*atdd` workflow with TEA
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - Writing tests before implementation
  - Example: Fuzzy matching thresholds
  - Benefits and trade-offs

- **13.2 Comprehensive Test Automation**
  - `*automate` workflow (every 3-4 stories)
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - Unit tests, integration tests, end-to-end tests
  - Coverage metrics
  - Example test suites from OFAC project

- **13.3 Requirements Traceability**
  - `*trace` workflow with TEA
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - Mapping requirements to tests
  - Ensuring all acceptance criteria have tests
  - Audit trail for compliance

- **13.4 Non-Functional Requirements Validation**
  - `*nfr-assess` workflow
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - Performance benchmarking: <30 seconds for 100 entries
  - Security: Data handling, API authentication
  - Usability: Streamlit UI testing
  - Compliance: OFAC version tracking, audit trails

### Chapter 14: Course Correction and Retrospectives
**Purpose**: Handle mid-project changes and reflect on lessons

- **14.1 When Requirements Change**
  - `*correct-course` workflow
  - [IF APPLICABLE DURING OFAC PROJECT]
  - Example: Discovering need for consolidated lists (CONS.CSV)
  - Impact assessment
  - Story re-prioritization
  - Communication with stakeholders

- **14.2 Epic Retrospective**
  - `*epic-retrospective` workflow after each epic
  - [TO BE EXECUTED DURING OFAC PROJECT]
  - What went well
  - What could improve
  - Action items for next epic
  - Team (agent) feedback

- **14.3 Party Mode for Strategic Decisions**
  - `*party-mode` workflow with BMad Master
  - [IF APPLICABLE DURING OFAC PROJECT]
  - Example: Deciding between local vs cloud deployment
  - Multi-agent perspectives: PM + Architect + DEV
  - Consensus building
  - Final decision and rationale

### Chapter 15: Project Completion and Validation
**Purpose**: Wrap up OFAC project and assess success against criteria

- **15.1 Final Deliverables**
  - Codebase walkthrough
  - Documentation artifacts
  - Test coverage report
  - Deployment guide

- **15.2 Success Criteria Assessment**
  - **Cost avoidance**: ✅ Zero subscription costs
  - **Time savings**: ✅ [ACTUAL METRICS FROM USAGE]
  - **Compliance**: ✅ Zero false negatives (spot-check validation)
  - **Audit acceptance**: ✅ [EXTERNAL AUDITOR FEEDBACK]
  - **Fuzzy matching value**: ✅ [EXAMPLES OF VARIANT NAMES CAUGHT]

- **15.3 Lessons Learned**
  - What worked exceptionally well
  - Challenges and how BMAD helped overcome them
  - Where BMAD constraints felt limiting (if any)
  - Advice for next project using BMAD

- **15.4 Path to Phase 2 (Commercial SaaS)**
  - Month 6 validation gate: PASSED / IN PROGRESS
  - Peer NGO interest and feedback
  - Commercial viability decision framework
  - Next steps if proceeding to commercialization

---

## PART 3: MASTERING BMAD

**Goal**: Advanced topics, decision frameworks, and customization

### Chapter 16: Decision Rubrics - When to Choose What
**Purpose**: Equip readers with judgment for future projects

- **16.1 Agent Selection Rubrics**
  - Which agent for planning? (PM vs Principal Engineer vs Analyst)
  - Which agent for architecture? (Architect vs skip)
  - Which agent for implementation? (SM vs DEV lifecycle)
  - Which agent for testing? (TEA vs DEV)
  - Which agent for documentation? (Analyst vs Technical Writer)
  - Which agent for orchestration? (BMad Master party mode)

- **16.2 Workflow Selection Rubrics**
  - First workflow to run (greenfield vs brownfield)
  - Planning workflows (when to brainstorm, research, create PRD)
  - Architecture workflows (when Level 3-4 required)
  - Implementation workflows (story loop mechanics)
  - Testing workflows (ATDD vs automate vs trace timing)
  - Change management workflows (correct-course, retrospective, party-mode)

- **16.3 Track Selection Rubric**
  - Quick Flow vs BMad Method vs Enterprise
  - Complexity indicators and triggers
  - Trade-offs between tracks
  - Decision tree / flowchart

- **16.4 Timing & Sequencing Rubrics**
  - When to validate (PRD, architecture, implementation readiness)
  - Parallel vs sequential workflows
  - Critical path dependencies

### Chapter 17: Customizing BMAD for Your Team
**Purpose**: Teach customization without breaking methodology

- **17.1 Agent Personality Customization**
  - Adjusting communication style
  - Domain-specific expertise injection
  - Project-specific agent configurations
  - Example: DuckTales Agent Customizations (OFAC project)

- **17.2 Workflow Adaptation**
  - Modifying existing workflows
  - Creating custom workflows
  - Workflow versioning and maintenance
  - When to customize vs use as-is

- **17.3 Template and Checklist Customization**
  - PRD templates for different domains
  - Architecture document structures
  - Story templates and acceptance criteria
  - Quality gates and validation checklists

- **17.4 Integration with Existing Tools**
  - IDEs: Claude Code, Cursor, Windsurf, VS Code
  - Project management: Jira, Linear, GitHub Projects
  - CI/CD: GitHub Actions, GitLab CI, Jenkins
  - Documentation: Confluence, Notion, Markdown repos

### Chapter 18: Common Pitfalls and How to Avoid Them
**Purpose**: Learn from others' mistakes

- **18.1 Planning Phase Pitfalls**
  - Skipping brownfield documentation (starting blind)
  - Over-planning simple projects (Track mismatch)
  - Under-planning complex projects (premature implementation)
  - Incomplete PRDs (vague requirements)
  - Ignoring validation warnings

- **18.2 Implementation Phase Pitfalls**
  - Starting before implementation readiness
  - Incomplete story context (developer confusion)
  - Skipping code review (technical debt accumulation)
  - Marking stories done without passing tests
  - Ignoring failing tests to "ship faster"

- **18.3 Testing Phase Pitfalls**
  - No test framework setup (scrambling later)
  - Writing tests after all code (missing coverage)
  - Ignoring NFRs until end (performance surprises)
  - No requirements traceability (audit failures)

- **18.4 Change Management Pitfalls**
  - Not using correct-course for mid-sprint changes
  - Skipping retrospectives (no learning)
  - Overusing party mode (slows decision-making)
  - Ignoring agent questions (incomplete answers → assumptions)

### Chapter 19: Scaling BMAD
**Purpose**: Apply BMAD to larger teams and projects

- **19.1 From Solo Developer to Team**
  - Multiple developers using same BMAD project
  - Coordinating story assignments
  - Shared repository patterns
  - Communication protocols

- **19.2 Multi-Epic Projects**
  - Epic prioritization and sequencing
  - Inter-epic dependencies
  - Managing scope creep
  - Long-term roadmap alignment

- **19.3 BMAD for Non-Software Domains**
  - Creative writing (existing expansion pack)
  - Business strategy
  - Education and wellness
  - Game development (Game Designer, Game Developer, Game Architect agents)

- **19.4 Building Custom BMAD Modules**
  - BMad Builder introduction
  - Creating domain-specific modules (legal, medical, finance)
  - Community marketplace (future)
  - Sharing and collaboration

### Chapter 20: The Future of AI-Assisted Development
**Purpose**: Vision for where BMAD and AI development are heading

- **20.1 Evolution from v4 to v6**
  - BMad Core framework (Collaboration Optimized Reflection Engine)
  - Modular architecture enabling custom domains
  - Scale-adaptive intelligence improvements
  - Visual workflows and diagrams

- **20.2 Emerging Trends**
  - Agentic reasoning and multi-agent systems
  - Context engineering as discipline
  - Shift from "writing code" to "orchestrating intelligence"
  - Human-AI partnership models

- **20.3 Open Questions**
  - Limits of AI agents in planning and design
  - Balancing autonomy vs human oversight
  - Ethics of AI-generated code
  - Impact on developer skills and careers

- **20.4 Call to Action**
  - Try BMAD on your next project
  - Contribute to BMAD community
  - Share your experiences and customizations
  - Help shape the future of agile AI development

---

## Back Matter

### Appendices

#### Appendix A: BMAD Quick Reference
- Agent roster with specializations
- Workflow categories and triggers
- Track selection decision tree
- Common commands and shortcuts

#### Appendix B: OFAC Project Repository Guide
- GitHub repository: https://github.com/cgorricho/OFAC
- Directory structure explained
- Key files and their purpose
- How to run and deploy

#### Appendix C: BMAD Installation and Setup
- Prerequisites (Node.js, npm, IDEs)
- Installing BMAD Method v6 (or stable v4)
- Configuration files
- First project setup

#### Appendix D: Additional Resources
- BMAD GitHub: https://github.com/bmad-code-org/BMAD-METHOD
- Discord community
- BMad Codes website: https://bmadcodes.com
- BMad Builder documentation
- Related blog posts and articles

#### Appendix E: Templates and Checklists
- PRD template (from BMAD Method)
- Architecture document template
- Story template with acceptance criteria
- Epic retrospective checklist
- Implementation readiness validation checklist

### Glossary
- BMAD terminology (agent, workflow, epic, story, track, phase)
- Agile terms (sprint, backlog, scrum master)
- Technical terms (fuzzy matching, API, REST, CI/CD)

### Index
- Comprehensive alphabetical index

### Bibliography
- References to Agile Manifesto, Pragmatic Programmer
- BMAD Method GitHub and documentation
- Related AI development frameworks
- Technical references (RapidFuzz, FastAPI, Streamlit)

---

## Writing Style Guidelines

### Tone
- **Conversational but authoritative**: Like a senior developer explaining to a colleague
- **Practical over theoretical**: Show, don't just tell
- **Honest about trade-offs**: No silver bullets, acknowledge limitations
- **Encouraging**: Readers can master this

### Voice
- First-person plural "we" for inclusive collaboration
- Active voice
- Direct address "you" for reader engagement
- Story-driven (OFAC project as narrative thread)

### Technical Depth
- Code examples: Real, production-ready snippets from OFAC project
- Diagrams: Visual workflows for 90% of concepts
- Progressive complexity: Simple examples → Complex patterns
- Actionable: Every chapter ends with "Try This" exercises

### Length Target
- Total: 300-400 pages
- Part 1: ~100-120 pages (theory)
- Part 2: ~150-180 pages (OFAC case study)
- Part 3: ~50-70 pages (advanced topics)
- Back matter: ~30-50 pages

---

## Publication Strategy

### Phase 1: Leanpub MVP (Recommended)
**Goal**: Validate market interest, build audience, gather feedback

1. **Chapters 1-6** (Part 1 - Foundations): Write first, publish as "In Progress"
2. **Early adopter pricing**: $19.99 during writing, $39.99 at completion
3. **Reader feedback loop**: Incorporate comments into later chapters
4. **Build email list**: Engage readers, gauge interest
5. **Timeline**: 3-4 months to Part 1 completion

### Phase 2: Complete OFAC Project
**Goal**: Generate real Part 2 content

1. Continue OFAC project implementation using BMAD Method
2. Document every workflow execution with screenshots, code snippets, lessons
3. Capture challenges and solutions in real-time
4. **Chapters 7-15** written as project progresses
5. **Timeline**: 4-6 months (concurrent with OFAC development)

### Phase 3: Self-Publish Complete Book (Leanpub)
**Goal**: Full book release, establish credibility

1. **Chapters 16-20** (Part 3 - Advanced topics): 1-2 months
2. Final editing and proofreading pass
3. Professional cover design
4. Launch price: $49.99 (industry standard for technical books)
5. Marketing: BMAD Discord, Medium articles, Twitter/LinkedIn
6. **Timeline**: 9-12 months total from start to complete book

### Phase 4: Pitch to Traditional Publishers (Optional)
**Goal**: Wider distribution, credibility boost, advance payment

1. Proven market success on Leanpub (e.g., 500+ copies sold)
2. Reader testimonials and reviews
3. Pitch to Pragmatic Bookshelf (best fit), O'Reilly, Manning
4. Pitch document:
   - Market validation (Leanpub sales data)
   - No existing BMAD Method books (first-mover)
   - Target audience: Developers using AI-assisted development (massive and growing market)
   - Comparable titles: "The Pragmatic Programmer," Agile methodology books
   - Competitive advantage: Only book with complete real-world case study
5. **Timeline**: 12-18 months post-Leanpub launch

### Marketing and Promotion

#### Content Marketing
- Medium articles: "How I Built an OFAC Screening Tool with BMAD Method" (link to book)
- Dev.to posts: BMAD tutorials and tips
- YouTube: Video walkthrough of OFAC project using BMAD
- GitHub: OFAC project README links to book

#### Community Engagement
- BMAD Discord: Share excerpts, gather feedback, answer questions
- Reddit: r/programming, r/learnprogramming, r/MachineLearning
- Hacker News: "Show HN: I wrote a book about BMAD Method"

#### Partnerships
- BMad Code, LLC: Potential foreword, cross-promotion, official endorsement
- Technical influencers: Early review copies, testimonials

---

## Next Steps

1. **Create Part 1 outline chapter files** (Chapters 1-6)
2. **Begin writing Chapter 1** (draft, no perfection needed)
3. **Set up Leanpub account** and create book project
4. **Continue OFAC project implementation** (generates Part 2 content)
5. **Establish writing cadence**: 2-3 chapters per month target

---

## Success Metrics

### Leanpub MVP (Phase 1)
- 100+ early adopter purchases
- 50+ email subscribers
- 80%+ positive reader reviews

### Complete Book (Phase 3)
- 500+ total copies sold (self-published)
- 4.5+ stars average rating
- 10+ detailed reader reviews
- Featured in BMAD Discord community

### Traditional Publishing (Phase 4 - Optional)
- Contract with Pragmatic Bookshelf, O'Reilly, or Manning
- $5K-$15K advance payment
- Wider distribution through publisher network

---

## Contact Information for Publishers

**Pragmatic Bookshelf**
- Website: https://pragprog.com
- Submission: Contact through website (editor inquiries)
- Executive Editor: Susannah Davidson

**O'Reilly Media**
- Website: https://www.oreilly.com
- Authors page: https://www.oreilly.com/authors
- Submission: Author proposal form

**Manning Publications**
- Website: https://www.manning.com
- MEAP (Manning Early Access Program)
- Submission: Author proposal form

**Leanpub**
- Website: https://leanpub.com
- Self-service: Create account, start writing immediately
- 80% royalties to author

---

**END OF OUTLINE**

---

## Document Metadata

- **Author**: Carlos Gorricho
- **Date Created**: December 9, 2025
- **Version**: 1.0
- **Status**: Complete research-based outline
- **Next Action**: Create chapter files for Part 1 (Chapters 1-6)
- **Estimated Timeline to MVP**: 3-4 months (Part 1 + Chapters 7-8)
