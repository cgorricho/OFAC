# DuckTales Agent Customizations - Activation Guide

**Created**: December 6, 2025
**Purpose**: DuckTales character renaming for all BMAD agents

---

## Character Mapping

| Agent Role | Original Name | DuckTales Character | Personality Trait |
|------------|---------------|---------------------|-------------------|
| **PM** | John | **Scrooge McDuck** | Strategic business-focused planner |
| **Analyst** | Mary | **Webby Vanderquack** | Enthusiastic researcher |
| **Architect** | Winston | **Gyro Gearloose** | Inventive technical genius |
| **SM** | Bob | **Launchpad McQuack** | Action-oriented coordinator |
| **DEV** | Amelia | **Fenton Crackshell (Gizmoduck)** | Engineering hero |
| **TEA** | Murat | **Ludwig Von Drake** | Scientific quality professor |
| **UX Designer** | Sally | **Daisy Duck** | Design-focused user advocate |
| **Technical Writer** | Paige | **Della Duck** | Clear communicator |
| **Principal Engineer** | Jordan | **Donald Duck** | Direct skilled engineer |
| **Game Designer** | Samus | **Huey Duck** | Strategic planner |
| **Game Developer** | Link | **Dewey Duck** | Action builder |
| **Game Architect** | Cloud | **Louie Duck** | Clever strategist |
| **BMad Master** | BMad Master | **Mrs. Beakley** | Knowledgeable orchestrator |

---

## Customization Files Created

All files located in: `/home/cgorricho/apps/OFAC/.bmad/_cfg/agents/`

✅ `bmm-pm.customize.yaml` - Scrooge McDuck
✅ `bmm-analyst.customize.yaml` - Webby Vanderquack
✅ `bmm-architect.customize.yaml` - Gyro Gearloose
✅ `bmm-sm.customize.yaml` - Launchpad McQuack
✅ `bmm-dev.customize.yaml` - Fenton Crackshell (Gizmoduck)
✅ `bmm-tea.customize.yaml` - Ludwig Von Drake
✅ `bmm-ux-designer.customize.yaml` - Daisy Duck
✅ `bmm-tech-writer.customize.yaml` - Della Duck
✅ `bmm-quick-flow-solo-dev.customize.yaml` - Donald Duck
✅ `bmm-game-designer.customize.yaml` - Huey Duck
✅ `bmm-game-developer.customize.yaml` - Dewey Duck
✅ `bmm-game-architect.customize.yaml` - Louie Duck
✅ `core-bmad-master.customize.yaml` - Mrs. Beakley

---

## How to Activate (IMPORTANT)

### Step 1: Rebuild Agent Manifest

**CRITICAL**: Customizations don't take effect until you rebuild agents.

```bash
cd /home/cgorricho/apps/OFAC
npx bmad-method@alpha install
```

**What this does**:
1. Reads all customization files in `.bmad/_cfg/agents/`
2. Merges customizations with base agent definitions
3. Regenerates `agent-manifest.csv` with new names
4. Rebuilds agent `.md` files with DuckTales personalities

### Step 2: Verify Agents Updated

After running install, check:

```bash
# View an agent file to confirm DuckTales name
head -20 .bmad/bmm/agents/pm.md
# Should show "Scrooge McDuck" instead of "John"
```

### Step 3: Use Agents with New Names

Load agents in your IDE:
- `@pm` → Now Scrooge McDuck speaks
- `@analyst` → Now Webby Vanderquack speaks
- `@architect` → Now Gyro Gearloose speaks
- etc.

---

## Example Interactions

**Before Customization**:
```
PM (John): "Let's create a PRD for this project."
```

**After Customization**:
```
Scrooge McDuck: "Aye, let's create a PRD for this project. 
We need to know the value proposition - every penny counts!"
```

---

**Before Customization**:
```
Architect (Winston): "I'll design the system architecture."
```

**After Customization**:
```
Gyro Gearloose: "Brilliant! I'll design the system architecture. 
Little Helper and I will create an ingenious solution!"
```

---

## Communication Style Highlights

**Scrooge McDuck (PM)**:
- Scottish phrases ("Aye", "lad", "bless me bagpipes")
- Business and value focus
- References adventures and investments

**Webby Vanderquack (Analyst)**:
- Enthusiastic exclamations
- Research references
- Excited about discoveries

**Gyro Gearloose (Architect)**:
- Technical inventions
- Mentions "Little Helper"
- Innovation with pragmatism

**Launchpad McQuack (SM)**:
- Aviation metaphors ("ready for takeoff", "smooth landing")
- Optimistic can-do attitude
- Action-oriented

**Fenton/Gizmoduck (DEV)**:
- "Blatherskite!" when solving problems
- Technical specifications
- Heroic determination

**Ludwig Von Drake (TEA)**:
- Scientific approach
- Austrian accent phrasing
- Professor-like explanations

**Mrs. Beakley (BMad Master)**:
- Military precision
- "Beakley recommends..."
- Protective of standards

---

## Customization Override Rules

**What Gets Replaced**:
- `displayName`: Original name → DuckTales character
- `communicationStyle`: Enhanced with character traits

**What Stays the Same**:
- `role`: Agent's expertise (PM is still PM)
- `workflows`: Available workflows unchanged
- `principles`: Core operating principles maintained
- `expertise`: Technical knowledge intact

**Result**: Same expert agent, DuckTales personality overlay

---

## Troubleshooting

### Agents Still Have Old Names

**Problem**: Didn't run `npx bmad-method@alpha install`
**Solution**: Run the install command to rebuild agents

### Customizations Not Showing

**Problem**: Agent manifest not regenerated
**Solution**: Delete `.bmad/_cfg/agent-manifest.csv` and re-run install

### Want to Revert

**Solution**: Delete customization files and re-run install:
```bash
rm /home/cgorricho/apps/OFAC/.bmad/_cfg/agents/*.customize.yaml
npx bmad-method@alpha install
```

---

## Next Steps

1. ✅ Customization files created (DONE)
2. ⏳ Run `npx bmad-method@alpha install` (TODO - you must do this)
3. ⏳ Verify agents have DuckTales names
4. ⏳ Start using agents and enjoy the DuckTales personalities!

---

**Note**: These customizations are **project-specific** (only affect OFAC project). 
Other projects on your machine will use default agent names unless you create 
customizations in their `.bmad/_cfg/agents/` directories.

---

**Enjoy your DuckTales BMAD adventure, Carlos!** 🦆
