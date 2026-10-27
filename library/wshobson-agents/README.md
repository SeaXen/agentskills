# Multi-Agent Collaboration & Production Safeguards

> **Category**: 🛡️ Parallel Debugging, Session Guards & Coordination  
> **Source / Upstream URL**: [https://github.com/wshobson/agents](https://github.com/wshobson/agents)  
> **Total Skills in Reserve**: 5 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate ai-debt-detector
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/wshobson-agents/skills/ai-debt-detector" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/wshobson-agents/skills/ai-debt-detector .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link ai-debt-detector
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\ai-debt-detector" ".agents\library\wshobson-agents\skills\ai-debt-detector"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/wshobson-agents/skills/ai-debt-detector" ".agents/skills/ai-debt-detector"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add wshobson/agents
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove ai-debt-detector
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/ai-debt-detector"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move ai-debt-detector --to hot
python .agents/library/activate_skill.py move ai-debt-detector --to reserve
```

---

## 📑 Included Skills Catalog (5 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`ai-debt-detector`** | Use after generating code, after accepting AI suggestions, or when reviewing AI-written modules. Also use when code works but feels brittle, when erro... |
| **`parallel-debugging`** | Debug complex issues using competing hypotheses with parallel investigation, evidence collection, and root cause arbitration. Use this skill when debu... |
| **`parallel-feature-development`** | Coordinate parallel feature development with file ownership strategies, conflict avoidance rules, and integration patterns for multi-agent implementat... |
| **`session-guard`** | Use when working on complex multi-step tasks, when a session is getting long (40+ tool calls), when the agent starts ignoring rules it followed earlie... |
| **`task-coordination-strategies`** | Decompose complex tasks, design dependency graphs, and coordinate multi-agent work with proper task descriptions and workload balancing. Use this skil... |
