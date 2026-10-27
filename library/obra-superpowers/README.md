# Obra Developer Superpowers

> **Category**: 🔮 Developer Diagnostics & Workspace Execution  
> **Source / Upstream URL**: [https://github.com/obra/superpowers](https://github.com/obra/superpowers)  
> **Total Skills in Reserve**: 15 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate brainstorming
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/obra-superpowers/skills/brainstorming" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/obra-superpowers/skills/brainstorming .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link brainstorming
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\brainstorming" ".agents\library\obra-superpowers\skills\brainstorming"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/obra-superpowers/skills/brainstorming" ".agents/skills/brainstorming"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add obra/superpowers
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove brainstorming
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/brainstorming"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move brainstorming --to hot
python .agents/library/activate_skill.py move brainstorming --to reserve
```

---

## 📑 Included Skills Catalog (15 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`brainstorming`** | "You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planning anything n... |
| **`diagnosing-superpowers`** | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill tha... |
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| **`executing-plans`** | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subage... |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires ... |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session |
| **`systematic-debugging`** | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| **`test-driven-development`** | Use when implementing any feature or bugfix, before writing implementation code |
| **`using-git-worktrees`** | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace ex... |
| **`using-superpowers`** | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying quest... |
| **`verification-before-completion`** | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming... |
| **`writing-plans`** | Use when you have a spec or requirements for a multi-step task, before touching code |
| **`writing-skills`** | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
