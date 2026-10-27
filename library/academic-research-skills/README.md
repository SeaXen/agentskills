# Academic Research & Literature Screening Pipeline

> **Category**: 📚 Deep Discovery, Citation Screening & Paper Synthesis  
> **Source / Upstream URL**: [https://github.com/imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)  
> **Total Skills in Reserve**: 5 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate academic-paper
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/academic-research-skills/skills/academic-paper" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/academic-research-skills/skills/academic-paper .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link academic-paper
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\academic-paper" ".agents\library\academic-research-skills\skills\academic-paper"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/academic-research-skills/skills/academic-paper" ".agents/skills/academic-paper"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add imbad0202/academic-research-skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove academic-paper
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/academic-paper"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move academic-paper --to hot
python .agents/library/activate_skill.py move academic-paper --to reserve
```

---

## 📑 Included Skills Catalog (5 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`academic-paper`** | "12-agent academic paper writing pipeline. 11 modes (full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/discl... |
| **`academic-paper-reviewer`** | "Multi-perspective academic paper review with dynamic reviewer personas. Runs a 5-seat, role-separated review panel (Journal-Fit Reviewer + 3 peer-rev... |
| **`academic-pipeline`** | "Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review -> re-revise -> final int... |
| **`deep-research`** | "Universal deep research agent team. 13-agent pipeline for rigorous academic research on any topic. 8 modes: full research, quick brief, paper review,... |
| **`sr-screener`** | "Protocol-driven study screening for systematic, scoping and rapid reviews. Turns a proposal or PROSPERO protocol into confirmed eligibility rules, th... |
