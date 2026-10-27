# Antigravity Colosseum & Telemetry Protocols

> **Category**: ⚔️ Colosseum Battle, Telemetry & Decoupled Learning  
> **Source / Upstream URL**: [Native Workspace Elite Protocols](Native Workspace Elite Protocols)  
> **Total Skills in Reserve**: 4 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate battle
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/antigravity-elite-protocols/skills/battle" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/antigravity-elite-protocols/skills/battle .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link battle
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\battle" ".agents\library\antigravity-elite-protocols\skills\battle"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/antigravity-elite-protocols/skills/battle" ".agents/skills/battle"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
Built-in workspace protocols
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove battle
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/battle"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move battle --to hot
python .agents/library/activate_skill.py move battle --to reserve
```

---

## 📑 Included Skills Catalog (4 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`battle`** | Activates Antigravity's Colosseum Battle Mode. Pits two rival subagents in isolated branched workspaces against each other, stress-tests competing imp... |
| **`benchmark`** | Replaces guesswork with empirical hardware telemetry: synthesizes ad-hoc stress-test harnesses on the fly, executes them headlessly, and proves perfor... |
| **`compaction`** | Triggers on-demand context compaction: persists critical state into durable artifacts, flushes obsolete transient turn history, and signals the runtim... |
| **`owl`** | Activates the OWL (Optimized Workforce Learning) decoupled multi-agent pipeline: uses DeepInvestigator for root-cause analysis and edge-case attacks, ... |
