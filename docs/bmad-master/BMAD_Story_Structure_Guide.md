# BMAD Story Structure Guide

**Author:** Carlos (with BMad Master guidance)
**Date:** 2025-12-11
**Purpose:** Learning guide for understanding and creating implementation-ready user stories
**Part of:** BMAD Method Learning Journey

---

## Table of Contents

1. [Introduction](#introduction)
2. [What is a Story in BMAD?](#what-is-a-story-in-bmad)
3. [Story Document Structure](#story-document-structure)
4. [Reading Strategy: The Funnel Pattern](#reading-strategy-the-funnel-pattern)
5. [Section-by-Section Deep Dive](#section-by-section-deep-dive)
6. [How to Read Stories for Different Purposes](#how-to-read-stories-for-different-purposes)
7. [Story Quality Criteria](#story-quality-criteria)
8. [Real Example: Story 1-1 Analysis](#real-example-story-1-1-analysis)
9. [Creating Your Own Stories](#creating-your-own-stories)
10. [Common Pitfalls & How to Avoid Them](#common-pitfalls--how-to-avoid-them)
11. [Quick Reference Cards](#quick-reference-cards)

---

## Introduction

### Why Story Documentation Matters

In the BMAD (Balanced Multi-Agent Development) methodology, **stories are the atomic unit of implementation**. Unlike traditional Agile where stories might be brief index cards, BMAD stories are **comprehensive, context-rich documents** designed for AI agent execution and human understanding.

**Key Principle:** A story should contain everything needed to implement it without searching through multiple documents.

### What You'll Learn

This guide teaches you:
- ✅ How to structure implementation-ready stories
- ✅ How to read and interpret story documents
- ✅ How to use stories as checklists, references, and audit trails
- ✅ How to document your implementation work
- ✅ How to maintain quality and consistency across stories

### Learning Journey Context

This document is part of your BMAD learning journey alongside:
- **BMAD_Method_Principles.md** - Core BMAD philosophy
- **BMAD_Agent_Decision_Rubrics.md** - When to use which agent
- **OFAC_BMAD_Roadmap.md** - Project-specific BMAD implementation
- **BMAD_Learning_Journal.md** - Your reflections and observations

---

## What is a Story in BMAD?

### Definition

**A BMAD story is a self-contained, implementation-ready document that:**
1. Describes **what** to build (user story)
2. Defines **success criteria** (acceptance criteria)
3. Breaks down **how** to build it (tasks/subtasks)
4. Provides **context** for decisions (dev notes, architecture refs)
5. Records **what actually happened** (dev agent record)
6. Maintains **audit trail** (file list, change log)

### Story vs Epic

| Aspect | Epic | Story |
|--------|------|-------|
| **Scope** | Large feature area | Single implementable unit |
| **Size** | Days to weeks | Hours to 1 day |
| **User Value** | High-level benefit | Specific functionality |
| **Example** | "Foundation & Data Layer" | "Project Initialization" |
| **Implementation** | Contains 5-10 stories | Single developer/agent session |

### Story Characteristics in BMAD

**1. Context-Rich**
- All necessary information included or referenced
- No need to search multiple documents
- Architecture decisions cited with document/section references

**2. Agent-Ready**
- AI agents can execute with minimal human intervention
- Clear acceptance criteria enable automated verification
- Task breakdown prevents agent confusion

**3. Audit-Complete**
- Complete file list of changes
- Code review fixes documented
- Change log maintained
- Traceability to PRD requirements

**4. Learning-Focused**
- Captures implementation decisions and rationale
- Documents problems encountered and solutions
- Serves as knowledge base for future work

---

## Story Document Structure

### Standard Template

Every BMAD story follows this 7-section structure:

```markdown
# Story X.Y: [Story Name]

Status: [backlog | drafted | ready-for-dev | in-progress | review | done]

## Story
As a [actor],
I want [capability],
So that [benefit].

## Acceptance Criteria
```gherkin
Given [context]
When [action]
Then [outcome]
And [additional outcome]
```

## Tasks / Subtasks
- [ ] Task 1: [Description] (AC: [relevant acceptance criterion])
  - [ ] Subtask 1.1
  - [ ] Subtask 1.2
- [ ] Task 2: [Description]
  ...

## Dev Notes
### Architecture Reference
### Key Decisions
### Dependencies
### References

## Dev Agent Record
### Context Reference
### Agent Model Used
### Debug Log References
### Completion Notes List
### Code Review Fixes Applied
### File List

## Change Log
- YYYY-MM-DD: [Change description]
```

### Section Purposes

| Section | Purpose | When to Read |
|---------|---------|--------------|
| **Story** | Understand the goal | Before implementation |
| **Acceptance Criteria** | Know when you're done | Before & after implementation |
| **Tasks/Subtasks** | Implementation roadmap | During implementation |
| **Dev Notes** | Context and guidance | When stuck or deciding |
| **Dev Agent Record** | What actually happened | After implementation, code review |
| **Change Log** | Historical timeline | Debugging, retrospectives |

---

## Reading Strategy: The Funnel Pattern

### Concept: Broad to Narrow

Think of a story as a **funnel** - broad understanding at the top, specific details at the bottom:

```
┌──────────────────────────────────────┐
│  1. STORY (WHAT & WHY)              │  ← Start here: 30 seconds
│     "What am I building?"            │
├──────────────────────────────────────┤
│  2. ACCEPTANCE CRITERIA (SUCCESS)    │  ← Next: 2 minutes
│     "How do I know I'm done?"        │
├──────────────────────────────────────┤
│  3. TASKS (HOW - High Level)        │  ← Then: 5 minutes
│     "What are the steps?"            │
├──────────────────────────────────────┤
│  4. DEV NOTES (CONTEXT)             │  ← Reference: 10 minutes
│     "What context do I need?"        │
├──────────────────────────────────────┤
│  5. DEV AGENT RECORD (ACTUAL WORK)  │  ← After work: document
│     "What did I do?"                 │
└──────────────────────────────────────┘
```

### Three-Phase Reading Approach

**Phase 1: Before Implementation (Planning)**
- Read: Story → Acceptance Criteria → Tasks → Dev Notes
- Time: 15-20 minutes
- Goal: Understand what to build and how

**Phase 2: During Implementation**
- Use: Tasks as checklist, Dev Notes as reference
- Time: Ongoing
- Goal: Stay on track, make informed decisions

**Phase 3: After Implementation (Documentation)**
- Update: Dev Agent Record, File List, Change Log
- Time: 10-15 minutes
- Goal: Complete audit trail, capture learnings

---

## Section-by-Section Deep Dive

### 1. Story Header

**Format:**
```markdown
# Story X.Y: [Story Name]

Status: [current status]
```

**Story Numbering:**
- `X` = Epic number (1-6 for OFAC project)
- `Y` = Story number within epic (1, 2, 3...)
- Example: `1.1` = Epic 1, Story 1 (first story in Foundation epic)

**Status Values:**
- `backlog` - Story exists in epic file, not yet detailed
- `drafted` - Story file created in sprint-artifacts folder
- `ready-for-dev` - Approved and ready for implementation
- `in-progress` - Developer actively working
- `review` - Under code review
- `done` - Completed and verified

### 2. Story (User Story Format)

**Format:**
```markdown
## Story
As a [actor],
I want [capability],
So that [benefit].
```

**Components:**

**Actor (Who):**
- Usually: developer, user, system, administrator
- Be specific: "backend developer" vs "frontend developer" if relevant
- OFAC Example: "As a **developer**..." (story 1-1 is infrastructure)

**Capability (What):**
- Concrete, specific action or feature
- Avoid vague language: "better" → "faster", "improved" → "automated"
- OFAC Example: "I want the project structure and dependencies set up"

**Benefit (Why):**
- Clear value statement
- Answers "why does this matter?"
- OFAC Example: "So that I can start implementing features"

**Quality Check:**
- ✅ Can you identify who benefits?
- ✅ Is the capability specific and measurable?
- ✅ Is the benefit clear and valuable?

### 3. Acceptance Criteria

**Format: Gherkin (BDD)**

```gherkin
Given [context/precondition]
When [action/trigger]
Then [expected outcome]
And [additional outcome]
And [additional outcome]
```

**Why Gherkin?**
- **Testable** - Each criterion maps to a test
- **Unambiguous** - Clear pass/fail conditions
- **Standard** - Industry-recognized format (Behavior-Driven Development)

**Example from Story 1-1:**
```gherkin
Given I have Python 3.11+ and uv installed
When I clone the repository and run `uv venv && uv pip install -e ".[dev]"`
Then the virtual environment is created
And all dependencies are installed
And I can run `python -c "import ofac"` without errors
```

**Writing Good Acceptance Criteria:**

**DO:**
- ✅ Use concrete, testable conditions
- ✅ Include verification steps (commands to run)
- ✅ Cover happy path and critical edge cases
- ✅ Make criteria objectively verifiable

**DON'T:**
- ❌ Use vague language ("should work well")
- ❌ Include implementation details (belongs in Tasks)
- ❌ Make criteria subjective ("looks good")
- ❌ Forget to mark as verified when done

**Verification Checkpoint:**

After implementation, add:
```markdown
**✅ All acceptance criteria verified and passing**
```

This signals story completion.

### 4. Tasks / Subtasks

**Format:**
```markdown
## Tasks / Subtasks

- [x] Task 1: [Description] (AC: [relevant acceptance criterion])
  - [x] Subtask 1.1: [Specific action]
  - [x] Subtask 1.2: [Specific action]
  - [x] Subtask 1.3: [Specific action]
- [x] Task 2: [Description] (AC: [relevant acceptance criterion])
  - [x] Subtask 2.1: [Specific action]
  ...
```

**Task Breakdown Principles:**

**1. Sequential Logic**
- Order tasks by dependency (foundation → features → verification)
- Example: Create structure → Add code → Write tests → Verify

**2. Acceptance Criteria Mapping**
- Each task references which AC it satisfies
- Example: `(AC: Complete project metadata and dependencies)`

**3. Subtask Granularity**
- Subtasks are concrete actions (create file, add function, run command)
- Each subtask takes 5-30 minutes
- Checkbox-friendly (clear done/not-done state)

**4. Verification Task**
- Last task should prove acceptance criteria
- Example: "Verify installation works"

**Quality Checklist:**
- ✅ Are tasks in logical sequence?
- ✅ Does each task map to an acceptance criterion?
- ✅ Are subtasks concrete and actionable?
- ✅ Can each subtask be checked off unambiguously?
- ✅ Is there a verification task at the end?

**Example Breakdown (Story 1-1):**

```
Task 1: Create pyproject.toml (AC: Complete project metadata)
  ├─ Define project metadata (name, version, description)
  ├─ Add core dependencies (fastapi, streamlit, pandas...)
  ├─ Add dev dependencies (pytest, ruff, mypy...)
  ├─ Add optional excel dependencies (xlwings)
  └─ Configure tool sections (ruff, pytest, mypy)

Task 2: Create src/ofac package structure (AC: Package can be imported)
  ├─ Create src/ofac/__init__.py with version
  ├─ Create src/ofac/__main__.py as entry point
  ├─ Create core/ subdirectory with __init__.py
  ├─ Create data/ subdirectory with __init__.py
  ├─ Create api/ subdirectory with __init__.py
  └─ Create streamlit/ subdirectory with __init__.py

...

Task 5: Verify installation works (AC: Acceptance criteria pass)
  ├─ Run uv venv and uv pip install -e ".[dev]"
  ├─ Verify import ofac works
  └─ Run initial test to verify pytest works
```

### 5. Dev Notes

**Purpose:** Provide all context needed without searching other documents.

**Standard Subsections:**

**5a. Architecture Reference**
```markdown
### Architecture Reference
- Follow project structure from `docs/architecture.md` section "Project Structure"
- Use `src/ofac/` layout (importable package)
- Python 3.11+ required per architecture spec
```

**Why:** Links story to architecture decisions, prevents drift.

**5b. Key Decisions / Context**
```markdown
### Project Structure Notes
- Root: `pyproject.toml` as single source of truth
- Package location: `src/ofac/`
- Test location: `tests/` (mirroring src structure)
```

**Why:** Captures important design decisions specific to this story.

**5c. Dependencies**
```markdown
### Dependencies (from architecture.md)
Core:
- fastapi>=0.109.0
- streamlit>=1.28.0
- pandas>=2.0.0
...
```

**Why:** Developers know exact versions to use without searching.

**5d. Tool Configuration**
```markdown
### Tool Configuration (from architecture.md)
- Ruff: line-length=88, target-version="py311"
- Pytest: testpaths=["tests"], addopts="-v --tb=short"
- Mypy: python_version="3.11", strict=true
```

**Why:** Ensures consistency across all stories.

**5e. References**
```markdown
### References
- [Source: docs/architecture.md#Project Structure]
- [Source: docs/architecture.md#pyproject.toml Structure]
- [Source: docs/epics.md#Story 1.1]
```

**Why:** Enables verification and deeper investigation if needed.

**Best Practices:**
- ✅ Include exact document sections (use # anchors)
- ✅ Copy-paste critical info (dependencies, config) directly
- ✅ Explain "why" for non-obvious decisions
- ✅ Keep it concise but complete

### 6. Dev Agent Record

**Purpose:** Document what actually happened during implementation.

This section is **CRITICAL** for BMAD - it captures the reality of implementation vs the plan.

**Standard Subsections:**

**6a. Context Reference**
```markdown
### Context Reference
<!-- Story context from epics.md and architecture.md -->
```

**Optional:** Can include brief summary of key context points.

**6b. Agent Model Used**
```markdown
### Agent Model Used
Claude Opus 4.5 (via Cursor)
```

**Why:** Different AI models have different capabilities. Documenting this helps:
- Reproduce results
- Debug unexpected behavior
- Compare model performance across stories

**6c. Debug Log References**
```markdown
### Debug Log References
- uv installed via pip
- Virtual environment created with uv venv
- 83 packages installed including ofac-screening
```

**Why:** Captures important runtime information, installation steps, versions.

**6d. Completion Notes List**
```markdown
### Completion Notes List
- ✅ Created pyproject.toml with full project configuration
- ✅ Created src/ofac/ package with all submodules (core, data, api, streamlit)
- ✅ Created tests/ directory with unit, integration, and fixtures subdirectories
- ✅ Verified installation: `python -c "import ofac"` returns version 0.1.0
- ✅ All 5 package import tests pass
```

**Why:**
- Proves acceptance criteria were met
- Shows what was actually delivered
- Serves as implementation summary

**Best Practice:** One checkbox per major deliverable, with verification details.

**6e. Code Review Fixes Applied**
```markdown
### Code Review Fixes Applied (YYYY-MM-DD)
- ✅ Fixed conftest.py: Changed `from typing import Generator` to `from collections.abc import Generator`
- ✅ Fixed __main__.py: Version now imports from `ofac.__version__` (single source of truth)
- ✅ Added `[tool.bandit]` section to pyproject.toml for pre-commit bandit hook
- ✅ Ran `ruff check --fix` to fix import ordering
- ✅ All linting passes: `ruff check` ✓, `mypy` ✓
```

**Why This is GOLD:**
- Shows iterative improvement (not "perfect first try")
- Documents lessons learned
- Prevents repeating mistakes in future stories
- Demonstrates professional discipline

**Best Practice:** Include:
- What was wrong (specific error or issue)
- How you fixed it (specific change)
- Verification (linting passes, tests pass)

**6f. File List**
```markdown
### File List

**New Files:**
- pyproject.toml
- src/ofac/__init__.py
- src/ofac/__main__.py
- tests/conftest.py
...

**Modified Files (Review Fixes):**
- tests/conftest.py (import fix)
- src/ofac/__main__.py (version import fix)
- pyproject.toml (bandit config added)
```

**Why:**
- Complete audit trail
- Code review knows what to examine
- Git commit messages can reference this
- Debugging knows what changed when

**Best Practice:** Separate new files from modified files for clarity.

### 7. Change Log

**Format:**
```markdown
## Change Log
- YYYY-MM-DD: [Description of change and context]
- YYYY-MM-DD: [Description of change and context]
```

**Example:**
```markdown
## Change Log
- 2025-12-11: Story 1.1 implemented - Project initialization complete with all dependencies and structure
- 2025-12-11: Code review fixes applied - Linting issues fixed, version duplication resolved, bandit config added
```

**Best Practices:**
- ✅ Always include date (ISO format: YYYY-MM-DD)
- ✅ Be specific about what changed
- ✅ Include context (why the change was made if not obvious)
- ✅ One entry per significant change or milestone
- ✅ Keep entries concise (1-2 lines each)

**When to Add Entries:**
- Story completed
- Code review fixes applied
- Bug fixes after initial completion
- Refactoring based on learnings from later stories

---

## How to Read Stories for Different Purposes

### Purpose 1: Implementing the Story (First Time)

**Reading Order:**

1. **Story (30 seconds)** → Understand the goal
2. **Acceptance Criteria (2 minutes)** → Know success criteria
3. **Tasks/Subtasks (5 minutes)** → Understand roadmap
4. **Dev Notes (10 minutes)** → Absorb context and architecture guidance

**Total Time:** ~17 minutes before writing any code

**Usage Pattern:**
- Print or keep story open in second window
- Use Tasks as checklist (check off as you go)
- Reference Dev Notes when making decisions
- Verify against Acceptance Criteria when done

### Purpose 2: Code Review

**Reading Order:**

1. **Story + Acceptance Criteria (2 minutes)** → Understand what was supposed to be built
2. **Completion Notes (3 minutes)** → See what was actually delivered
3. **File List (2 minutes)** → Know what to examine
4. **Code Review Fixes (if present)** → Understand iterations

**Total Time:** ~7 minutes

**Review Questions:**
- ✅ Do completion notes satisfy acceptance criteria?
- ✅ Are all files in file list necessary?
- ✅ Do changes align with architecture references?
- ✅ Are there any missing pieces from tasks list?

### Purpose 3: Understanding Pattern (Learning)

**Reading Order:**

1. **Story (30 seconds)** → See how user story is written
2. **Acceptance Criteria (1 minute)** → Study Gherkin format
3. **Tasks breakdown (3 minutes)** → Analyze task decomposition logic
4. **Dev Notes (5 minutes)** → See how context is provided
5. **Dev Agent Record (5 minutes)** → Understand documentation discipline

**Total Time:** ~15 minutes

**Learning Focus:**
- How are capabilities broken down into tasks?
- How are architecture decisions referenced?
- How is implementation documented?
- What patterns can I reuse in my next story?

### Purpose 4: Debugging (Something Broke)

**Reading Order:**

1. **File List** → Which files were changed?
2. **Completion Notes** → What was delivered?
3. **Debug Log References** → What environment details matter?
4. **Code Review Fixes** → Were there known issues?
5. **Change Log** → What changed over time?

**Debugging Questions:**
- What files did this story touch?
- What was the implementation approach?
- Were there any known issues or fixes?
- What dependencies or versions matter?

### Purpose 5: Retrospective (What Did We Learn?)

**Reading Order:**

1. **Story + Acceptance Criteria** → Original plan
2. **Tasks** → Planned approach
3. **Dev Agent Record** → What actually happened
4. **Code Review Fixes** → What we learned and fixed
5. **Change Log** → Timeline of changes

**Retrospective Questions:**
- Did we estimate tasks accurately?
- What surprised us during implementation?
- What would we do differently next time?
- What patterns worked well?

---

## Story Quality Criteria

### The 7 Quality Dimensions

Use this checklist to evaluate any story (yours or someone else's):

#### 1. User Story Quality

**Excellent:**
- ✅ Clear actor (who benefits)
- ✅ Specific capability (what to build)
- ✅ Valuable benefit (why it matters)
- ✅ Follows "As a... I want... So that..." format

**Poor:**
- ❌ Vague actor ("the system")
- ❌ Implementation detail instead of capability
- ❌ No clear benefit stated

#### 2. Acceptance Criteria Quality

**Excellent:**
- ✅ Gherkin format (Given/When/Then)
- ✅ Testable conditions (can be verified objectively)
- ✅ Complete coverage (happy path + critical cases)
- ✅ Marked as verified when complete

**Poor:**
- ❌ No format or inconsistent format
- ❌ Subjective criteria ("works well")
- ❌ Missing critical scenarios
- ❌ Never marked as verified

#### 3. Task Breakdown Quality

**Excellent:**
- ✅ Logical sequence (dependencies respected)
- ✅ Each task maps to acceptance criteria
- ✅ Subtasks are concrete and actionable
- ✅ Verification task at the end
- ✅ All checkboxes marked complete when done

**Poor:**
- ❌ Random order (no logic)
- ❌ Tasks don't connect to AC
- ❌ Vague subtasks
- ❌ No verification step
- ❌ Incomplete checkbox marking

#### 4. Context Quality (Dev Notes)

**Excellent:**
- ✅ Architecture references with document sections
- ✅ Key decisions explained
- ✅ Dependencies with versions
- ✅ Tool configuration specified
- ✅ Source citations provided

**Poor:**
- ❌ No architecture references
- ❌ No explanation of decisions
- ❌ Missing dependency info
- ❌ No references to source documents

#### 5. Documentation Quality (Dev Agent Record)

**Excellent:**
- ✅ Agent model documented
- ✅ Debug log captures important info
- ✅ Completion notes prove AC satisfied
- ✅ Code review fixes documented
- ✅ Complete file list (new + modified)

**Poor:**
- ❌ No agent model mentioned
- ❌ No debug information
- ❌ No completion notes
- ❌ Code review fixes not documented
- ❌ Incomplete or missing file list

#### 6. Traceability Quality

**Excellent:**
- ✅ References to PRD requirements
- ✅ References to architecture sections
- ✅ References to epic document
- ✅ Clear connection to project goals

**Poor:**
- ❌ No connection to requirements
- ❌ No architecture references
- ❌ Unclear why story exists

#### 7. Audit Trail Quality

**Excellent:**
- ✅ Complete file list
- ✅ Timestamped change log
- ✅ Code review fixes documented
- ✅ Can reconstruct what happened and when

**Poor:**
- ❌ Missing file list
- ❌ No change log or dates
- ❌ No record of fixes
- ❌ Cannot determine timeline

### Story Quality Scorecard Template

Use this to self-assess your stories:

```markdown
| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| User Story Format | ___ | |
| Acceptance Criteria | ___ | |
| Task Breakdown | ___ | |
| Context (Dev Notes) | ___ | |
| Documentation (Record) | ___ | |
| Traceability | ___ | |
| Audit Trail | ___ | |
| **Total** | **___/35** | |
```

**Scoring:**
- 5 = Exceptional (top 5%)
- 4 = Strong (professional quality)
- 3 = Adequate (meets minimum bar)
- 2 = Weak (needs improvement)
- 1 = Poor (missing critical elements)

**Targets:**
- **30-35**: Exceptional quality
- **25-29**: Strong quality, minor improvements possible
- **20-24**: Adequate, needs improvement in some areas
- **<20**: Significant gaps, revisit structure

---

## Real Example: Story 1-1 Analysis

### Story Overview

**Story:** 1-1 Project Initialization
**Epic:** 1 - Foundation & Data Layer
**Status:** Done
**Quality Score:** 35/35 (100%)

### Section-by-Section Quality Analysis

#### User Story (5/5)

```markdown
As a **developer**,
I want the project structure and dependencies set up,
So that I can start implementing features.
```

**Why Excellent:**
- ✅ Clear actor: developer (infrastructure work)
- ✅ Specific capability: project structure and dependencies setup
- ✅ Clear benefit: enables feature implementation
- ✅ Perfect format adherence

#### Acceptance Criteria (5/5)

```gherkin
Given I have Python 3.11+ and uv installed
When I clone the repository and run `uv venv && uv pip install -e ".[dev]"`
Then the virtual environment is created
And all dependencies are installed
And I can run `python -c "import ofac"` without errors
```

**Why Excellent:**
- ✅ Gherkin format (Given/When/Then/And)
- ✅ Testable: exact commands to verify
- ✅ Complete: covers setup through verification
- ✅ Marked as verified: "All acceptance criteria verified and passing"

#### Task Breakdown (5/5)

**5 Main Tasks, 19 Subtasks:**

1. Create pyproject.toml (5 subtasks)
2. Create src/ofac package structure (6 subtasks)
3. Create tests directory structure (5 subtasks)
4. Create configuration files (3 subtasks)
5. Verify installation works (3 subtasks)

**Why Excellent:**
- ✅ Logical sequence: config → structure → tests → verify
- ✅ Each task maps to AC (noted in parentheses)
- ✅ Subtasks concrete and actionable
- ✅ Verification task at end
- ✅ All checkboxes marked complete

#### Context/Dev Notes (5/5)

**Includes:**
- Architecture references with specific sections
- Complete dependency list with versions
- Tool configuration (Ruff, Pytest, Mypy)
- Source citations to architecture.md and epics.md

**Why Excellent:**
- ✅ No need to search other documents
- ✅ All critical info included
- ✅ Specific document sections referenced
- ✅ Rationale provided where needed

#### Dev Agent Record (5/5)

**Includes:**
- Agent model: Claude Opus 4.5 (via Cursor)
- Debug log: uv installation, 83 packages installed
- Completion notes: 7 items with verification
- Code review fixes: 4 fixes documented with verification
- File list: 19 new files, 3 modified files

**Why Excellent:**
- ✅ Complete documentation of implementation
- ✅ Code review fixes show iterative improvement
- ✅ All files accounted for
- ✅ Verification proves AC satisfied

#### Traceability (5/5)

**References:**
- docs/architecture.md#Project Structure
- docs/architecture.md#pyproject.toml Structure
- docs/architecture.md#Development Tooling
- docs/epics.md#Story 1.1

**Why Excellent:**
- ✅ Clear connection to architecture
- ✅ Epic reference provided
- ✅ Can verify against source documents
- ✅ Enables future maintenance

#### Audit Trail (5/5)

**Includes:**
- Complete file list (new + modified)
- Timestamped change log (2 entries)
- Code review fixes documented
- Can reconstruct implementation timeline

**Why Excellent:**
- ✅ Complete audit trail
- ✅ Changes documented with dates
- ✅ Review process visible
- ✅ Professional compliance standard

### Key Learning Points from Story 1-1

**What Made This Story Exceptional:**

1. **Code Review Fixes Documented**
   - Shows professional iterative development
   - Prevents repeating mistakes
   - Demonstrates learning mindset

2. **Architecture Citations**
   - Prevents architectural drift
   - Enables verification
   - Maintains consistency across stories

3. **Verification Documented**
   - Proves acceptance criteria met
   - Shows discipline (test before marking done)
   - Provides confidence for next stories

4. **Complete File List**
   - New files separated from modified files
   - Review process visible
   - Audit trail complete

**Patterns to Replicate:**

- ✅ Use same section structure
- ✅ Include architecture references with sections
- ✅ Document code review fixes
- ✅ Verify AC before marking done
- ✅ Maintain complete file list
- ✅ Update change log with dates

---

## Creating Your Own Stories

### Story Creation Workflow

**Step 1: Start from Epic Document**

Your epic document (`docs/epics.md`) contains story summaries. Example:

```markdown
**Story 1.2: Configuration System**
- Create Pydantic Settings configuration system
- Support environment variables and .env files
- Validate settings on application startup
```

**Step 2: Create Story File**

Create file: `docs/sprint-artifacts/1-2-configuration-system.md`

**Step 3: Fill in Sections (Recommended Order)**

**3a. Story Header + User Story (5 minutes)**
```markdown
# Story 1.2: Configuration System

Status: drafted

## Story
As a **developer**,
I want centralized configuration management,
So that all components use consistent settings.
```

**3b. Acceptance Criteria (10 minutes)**

Think: "How do I prove this works?"

```gherkin
Given I have created a Settings class
When I import and access settings.match_threshold_nok
Then I receive the configured value (default: 95)
And environment variables override defaults
And invalid settings raise validation errors on startup
```

**3c. Tasks/Subtasks (15 minutes)**

Think: "What are the implementation steps?"

```markdown
- [ ] Task 1: Create core/config.py with Pydantic BaseSettings (AC: Settings class exists)
  - [ ] Import pydantic-settings
  - [ ] Define Settings class inheriting from BaseSettings
  - [ ] Add matching threshold fields (match_threshold_nok, match_threshold_review)
  - [ ] Add OFAC data path fields
  - [ ] Add logging configuration fields
  - [ ] Configure env_prefix="OFAC_" and env_file=".env"
- [ ] Task 2: Add validation logic (AC: Invalid settings raise errors)
  - [ ] Add field validators (threshold ranges, path existence)
  - [ ] Test validation with invalid values
- [ ] Task 3: Create singleton instance (AC: Settings accessible everywhere)
  - [ ] Create settings instance at module level
  - [ ] Test import from different modules
- [ ] Task 4: Update .env.example (AC: Environment variables documented)
  - [ ] Add all OFAC_* variables with descriptions
  - [ ] Add example values
- [ ] Task 5: Verify configuration system works (AC: Acceptance criteria pass)
  - [ ] Test default values
  - [ ] Test environment variable override
  - [ ] Test validation errors
```

**3d. Dev Notes (10 minutes)**

Reference architecture document, include:
- Architecture section references
- Key design decisions (why Pydantic Settings?)
- Configuration specifications from architecture
- Dependencies and versions

**3e. Dev Agent Record (Leave blank initially)**

Fill this in as you implement.

**Step 4: Get Story Approved (Move to ready-for-dev)**

Update `docs/sprint-artifacts/sprint-status.yaml`:
```yaml
1-2-configuration-system: ready-for-dev
```

**Step 5: Implement Story**

Use story as your guide, checking off tasks as you go.

**Step 6: Document Implementation**

Fill in Dev Agent Record:
- Agent model used
- Debug log
- Completion notes
- File list

**Step 7: Code Review & Fixes**

If fixes needed, document in "Code Review Fixes Applied" section.

**Step 8: Mark Done**

- Verify all acceptance criteria
- Mark all checkboxes complete
- Update status to `done`
- Update change log

### Story Writing Checklist

Before moving story to `ready-for-dev`, verify:

**User Story:**
- [ ] Clear actor identified
- [ ] Specific capability described
- [ ] Valuable benefit stated
- [ ] Follows "As a... I want... So that..." format

**Acceptance Criteria:**
- [ ] Written in Gherkin format (Given/When/Then)
- [ ] All criteria are testable
- [ ] Happy path covered
- [ ] Critical edge cases covered

**Tasks/Subtasks:**
- [ ] Tasks in logical sequence
- [ ] Each task maps to AC (noted in parentheses)
- [ ] Subtasks are concrete actions
- [ ] Verification task included
- [ ] Estimated to complete in <1 day

**Dev Notes:**
- [ ] Architecture references included
- [ ] Key decisions explained
- [ ] Dependencies specified with versions
- [ ] Source citations provided

**Story Ready Checklist:**
- [ ] All sections completed
- [ ] Story can be implemented without searching other docs
- [ ] AC are verifiable
- [ ] Tasks are actionable
- [ ] Context is complete

---

## Common Pitfalls & How to Avoid Them

### Pitfall 1: Vague Acceptance Criteria

**Bad Example:**
```markdown
- The configuration system should work properly
- Settings should be easy to use
- Configuration should be flexible
```

**Why Bad:**
- Not testable
- Subjective ("properly", "easy", "flexible")
- No specific success criteria

**Good Example:**
```gherkin
Given I have a Settings class
When I access settings.match_threshold_nok
Then I receive the default value (95)
And when I set OFAC_MATCH_THRESHOLD_NOK=90 in .env
Then I receive the overridden value (90)
```

**How to Avoid:**
- ✅ Use Gherkin format
- ✅ Include specific commands/actions to verify
- ✅ Make criteria objectively testable

### Pitfall 2: Implementation in User Story

**Bad Example:**
```markdown
As a developer,
I want to create a Pydantic BaseSettings class in core/config.py,
So that configuration is centralized.
```

**Why Bad:**
- User story describes implementation (Pydantic BaseSettings)
- Too technical for user story level
- Locks in implementation before design discussion

**Good Example:**
```markdown
As a developer,
I want centralized configuration management,
So that all components use consistent settings.
```

**How to Avoid:**
- ✅ Focus on capability, not implementation
- ✅ Save implementation details for Tasks section
- ✅ Ask: "What capability do I need?" not "How will I build it?"

### Pitfall 3: Tasks Without AC Mapping

**Bad Example:**
```markdown
- [ ] Task 1: Create config.py
- [ ] Task 2: Add settings
- [ ] Task 3: Write tests
```

**Why Bad:**
- No connection to acceptance criteria
- Unclear which AC each task satisfies
- Hard to verify completeness

**Good Example:**
```markdown
- [ ] Task 1: Create core/config.py with Pydantic BaseSettings (AC: Settings class exists)
- [ ] Task 2: Add validation logic (AC: Invalid settings raise errors)
- [ ] Task 3: Verify configuration system works (AC: All acceptance criteria pass)
```

**How to Avoid:**
- ✅ Add (AC: ...) after each task description
- ✅ Ensure every AC has at least one task
- ✅ Ensure every task contributes to an AC

### Pitfall 4: Missing Architecture References

**Bad Example:**
```markdown
## Dev Notes

Create a configuration system using Pydantic.
```

**Why Bad:**
- No reference to architecture decisions
- Risk of implementation diverging from design
- No traceability

**Good Example:**
```markdown
## Dev Notes

### Architecture Reference
- Follow configuration pattern from `docs/architecture.md#Infrastructure & Deployment`
- Use Pydantic Settings per architecture spec (line 466)
- Configuration schema defined in architecture (lines 472-493)

### References
- [Source: docs/architecture.md#Infrastructure & Deployment]
- [Source: docs/architecture.md#Configuration Schema]
```

**How to Avoid:**
- ✅ Always include architecture references
- ✅ Cite specific document sections
- ✅ Copy key specs directly into Dev Notes

### Pitfall 5: Incomplete Dev Agent Record

**Bad Example:**
```markdown
## Dev Agent Record

Story completed.
```

**Why Bad:**
- No documentation of what happened
- No audit trail
- No learning captured
- No file list

**Good Example:**
```markdown
## Dev Agent Record

### Agent Model Used
Claude Opus 4.5 (via Cursor)

### Completion Notes List
- ✅ Created core/config.py with Settings class
- ✅ All 8 configuration fields added
- ✅ Environment variable override tested and verified
- ✅ Validation raises errors as expected

### Code Review Fixes Applied
- ✅ Fixed type hint: Path | None → Path | None = None
- ✅ All type checking passes: mypy ✓

### File List
**New Files:**
- src/ofac/core/config.py

**Modified Files:**
- .env.example (added OFAC_* variables)
```

**How to Avoid:**
- ✅ Fill in all Dev Agent Record subsections
- ✅ Document completion notes with verification
- ✅ List all files created or modified
- ✅ Document code review fixes if applicable

### Pitfall 6: Not Marking Checkboxes

**Bad Example:**
```markdown
- [ ] Task 1: Create config.py
  - [ ] Create file
  - [ ] Add Settings class
```

[Story marked as "done" but checkboxes still empty]

**Why Bad:**
- Visual signal missing
- Unclear what was actually completed
- Can't quickly scan completion status

**Good Example:**
```markdown
- [x] Task 1: Create config.py
  - [x] Create file
  - [x] Add Settings class
```

**How to Avoid:**
- ✅ Check off boxes as you complete subtasks
- ✅ Don't mark story "done" until all boxes checked
- ✅ Use checkboxes as your progress tracker

### Pitfall 7: Forgetting Code Review Documentation

**Bad Example:**
```markdown
[Story shows status: done, but no mention of code review fixes]
```

**Why Bad:**
- Lessons learned not captured
- Future stories may repeat mistakes
- No evidence of iterative improvement

**Good Example:**
```markdown
### Code Review Fixes Applied (2025-12-11)
- ✅ Fixed: Import statement used typing instead of collections.abc
- ✅ Fixed: Duplicate version definition removed
- ✅ Added: Bandit configuration for security scanning
- ✅ Verified: All linting passes (ruff ✓, mypy ✓, bandit ✓)
```

**How to Avoid:**
- ✅ Always add "Code Review Fixes Applied" section
- ✅ Document what was wrong, how you fixed it, verification
- ✅ Date the fixes
- ✅ Consider it part of "done" definition

---

## Quick Reference Cards

### Card 1: Story Reading Flow

```
┌────────────────────────────────────────────────┐
│ BEFORE IMPLEMENTATION (15-20 min)             │
├────────────────────────────────────────────────┤
│ 1. Story (30 sec)      → What am I building?  │
│ 2. AC (2 min)          → How do I know I'm done?│
│ 3. Tasks (5 min)       → What are the steps?  │
│ 4. Dev Notes (10 min)  → What context needed? │
├────────────────────────────────────────────────┤
│ DURING IMPLEMENTATION                          │
├────────────────────────────────────────────────┤
│ - Use Tasks as checklist                       │
│ - Check off subtasks as you go                │
│ - Reference Dev Notes when stuck              │
│ - Verify against AC when done                 │
├────────────────────────────────────────────────┤
│ AFTER IMPLEMENTATION (10-15 min)              │
├────────────────────────────────────────────────┤
│ 1. Fill Dev Agent Record                      │
│ 2. Document completion notes                  │
│ 3. List all files changed                     │
│ 4. Document code review fixes                 │
│ 5. Update change log                          │
│ 6. Verify AC one final time                   │
│ 7. Mark status: done                          │
└────────────────────────────────────────────────┘
```

### Card 2: Story Quality Self-Check

```
┌────────────────────────────────────────────────┐
│ QUICK QUALITY CHECK                            │
├────────────────────────────────────────────────┤
│ USER STORY:                                    │
│ ☐ Clear actor, capability, benefit            │
│ ☐ "As a... I want... So that..." format       │
│                                                │
│ ACCEPTANCE CRITERIA:                           │
│ ☐ Gherkin format (Given/When/Then)            │
│ ☐ Testable and specific                       │
│ ☐ Marked as verified when done                │
│                                                │
│ TASKS:                                         │
│ ☐ Logical sequence                            │
│ ☐ Each task maps to AC                        │
│ ☐ All checkboxes marked when done             │
│                                                │
│ DEV NOTES:                                     │
│ ☐ Architecture references included            │
│ ☐ Dependencies with versions                  │
│ ☐ Source citations provided                   │
│                                                │
│ DEV AGENT RECORD:                              │
│ ☐ Completion notes documented                 │
│ ☐ Code review fixes recorded                  │
│ ☐ Complete file list provided                 │
│                                                │
│ CHANGE LOG:                                    │
│ ☐ Dated entries for major changes             │
└────────────────────────────────────────────────┘
```

### Card 3: Gherkin Template

```
┌────────────────────────────────────────────────┐
│ ACCEPTANCE CRITERIA (GHERKIN FORMAT)           │
├────────────────────────────────────────────────┤
│ ```gherkin                                     │
│ Given [precondition/context]                   │
│ When [action/trigger]                          │
│ Then [expected outcome]                        │
│ And [additional outcome]                       │
│ And [additional outcome]                       │
│ ```                                            │
│                                                │
│ TIPS:                                          │
│ - Given: Setup/context                         │
│ - When: Action user takes                      │
│ - Then: Observable result                      │
│ - And: Additional results                      │
│                                                │
│ VERIFICATION:                                  │
│ After implementation, add:                     │
│ **✅ All acceptance criteria verified**        │
└────────────────────────────────────────────────┘
```

### Card 4: File List Template

```
┌────────────────────────────────────────────────┐
│ FILE LIST TEMPLATE                             │
├────────────────────────────────────────────────┤
│ ### File List                                  │
│                                                │
│ **New Files:**                                 │
│ - path/to/new/file1.py                        │
│ - path/to/new/file2.py                        │
│ - path/to/new/file3.yaml                      │
│                                                │
│ **Modified Files:**                            │
│ - path/to/existing/file1.py (reason)          │
│ - path/to/existing/file2.md (reason)          │
│                                                │
│ **Deleted Files:** (if any)                    │
│ - path/to/removed/file.py (reason)            │
└────────────────────────────────────────────────┘
```

---

## Conclusion

### Key Takeaways

**1. Stories Are Comprehensive Documents**
- Not just brief index cards
- Self-contained with all context needed
- Designed for AI agent execution and human understanding

**2. Structure Enables Quality**
- 7 standard sections prevent gaps
- Each section has specific purpose
- Consistency across stories aids understanding

**3. Documentation is Professional Discipline**
- Code review fixes show iterative improvement
- File lists provide complete audit trail
- Change logs maintain historical record

**4. Context Prevents Drift**
- Architecture references keep implementation aligned
- Source citations enable verification
- Dependencies with versions ensure consistency

**5. Verification Proves Completion**
- Gherkin format makes AC testable
- Completion notes demonstrate satisfaction
- "All acceptance criteria verified" signals done

### Your Learning Journey

As you create more stories:
- **Stories 1-3:** Focus on structure (get all sections right)
- **Stories 4-6:** Focus on quality (make AC testable, tasks specific)
- **Stories 7+:** Focus on efficiency (write faster while maintaining quality)

**Remember:** The goal is not perfection on the first story, but **continuous improvement** across all stories.

### Next Steps

**Immediate Actions:**
1. Review Story 1-1 with this guide
2. Use this guide when creating Story 1-2
3. Self-assess Story 1-2 using quality scorecard
4. Iterate and improve

**Ongoing Practices:**
1. Reference this guide before creating each new story
2. Use quality scorecard to self-assess
3. Document lessons learned in your BMAD Learning Journal
4. Share patterns that work well with your team

### Additional Resources

**Related BMAD Documents:**
- `BMAD_Method_Principles.md` - Core methodology
- `BMAD_Agent_Decision_Rubrics.md` - When to use which agent
- `OFAC_BMAD_Roadmap.md` - Project-specific implementation
- `BMAD_Learning_Journal.md` - Your reflections

**Architecture References:**
- `docs/architecture.md` - System architecture
- `docs/epics.md` - Epic and story breakdown
- `docs/prd.md` - Requirements

**Story Examples:**
- `docs/sprint-artifacts/1-1-project-initialization.md` - Exemplary first story
- `docs/sprint-artifacts/sprint-status.yaml` - Status tracking

---

## Appendix: Story Template

Copy this template when creating new stories:

```markdown
# Story X.Y: [Story Name]

Status: [backlog | drafted | ready-for-dev | in-progress | review | done]

## Story

As a [actor],
I want [capability],
So that [benefit].

## Acceptance Criteria

```gherkin
Given [context]
When [action]
Then [outcome]
And [additional outcome]
```

## Tasks / Subtasks

- [ ] Task 1: [Description] (AC: [relevant acceptance criterion])
  - [ ] Subtask 1.1: [Specific action]
  - [ ] Subtask 1.2: [Specific action]
- [ ] Task 2: [Description] (AC: [relevant acceptance criterion])
  - [ ] Subtask 2.1: [Specific action]
- [ ] Task 3: Verify [capability] works (AC: All acceptance criteria pass)
  - [ ] Test [specific aspect]
  - [ ] Verify [specific outcome]

## Dev Notes

### Architecture Reference
- Follow [pattern] from `docs/architecture.md` section "[Section Name]"
- [Key architectural decision]
- [Version/technology requirement]

### Key Decisions
- [Decision 1 with rationale]
- [Decision 2 with rationale]

### Dependencies
```
[Dependency 1]>=X.Y.Z
[Dependency 2]>=X.Y.Z
```

### References
- [Source: docs/architecture.md#Section]
- [Source: docs/epics.md#Story X.Y]

## Dev Agent Record

### Context Reference
<!-- Story context from epics.md and architecture.md -->

### Agent Model Used
[Model name and platform]

### Debug Log References
- [Key installation/setup detail]
- [Important runtime information]

### Completion Notes List
- ✅ [Major deliverable 1 with verification]
- ✅ [Major deliverable 2 with verification]

### Code Review Fixes Applied (YYYY-MM-DD)
- ✅ Fixed: [Issue description and solution]
- ✅ Verified: [Verification step]

### File List

**New Files:**
- path/to/file1
- path/to/file2

**Modified Files:**
- path/to/file3 (reason)

## Change Log
- YYYY-MM-DD: [Description of change]
```

---

**Document Version:** 1.0
**Last Updated:** 2025-12-11
**Author:** Carlos (with BMad Master guidance)
**Status:** Complete - Ready for Use

---

🧙 **May this guide serve you well in your BMAD learning journey, Carlos!**
