# Engineering Craft & Observability (Addy Osmani)

> **Category**: 🔍 Doubt-Driven Development & Software Craft  
> **Source / Upstream URL**: [https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)  
> **Total Skills in Reserve**: 4 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate doubt-driven-development
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/addyosmani-agent-skills/skills/doubt-driven-development" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/addyosmani-agent-skills/skills/doubt-driven-development .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link doubt-driven-development
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\doubt-driven-development" ".agents\library\addyosmani-agent-skills\skills\doubt-driven-development"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/addyosmani-agent-skills/skills/doubt-driven-development" ".agents/skills/doubt-driven-development"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add addyosmani/agent-skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove doubt-driven-development
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/doubt-driven-development"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move doubt-driven-development --to hot
python .agents/library/activate_skill.py move doubt-driven-development --to reserve
```

---

## 📑 Included Skills Catalog (4 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`doubt-driven-development`** | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before p... |
| **`git-workflow-and-versioning`** | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in... |
| **`incremental-implementation`** | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when pickin... |
| **`observability-and-instrumentation`** | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feat... |
