# Antigravity Awesome Skills (882 Skills)

> **Category**: 🌟 Curated Open-Source Agent Skills Ecosystem  
> **Source / Upstream URL**: [https://github.com/benjaminasterA/antigravity-awesome-skills](https://github.com/benjaminasterA/antigravity-awesome-skills)  
> **Total Skills in Reserve**: 882 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate <skill-name>
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/antigravity-awesome-skills/skills/<skill-name>" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/antigravity-awesome-skills/skills/<skill-name> .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
To link without duplicating disk space:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link <skill-name>
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\<skill-name>" ".agents\library\antigravity-awesome-skills\skills\<skill-name>"
```

---

### 3. 🔄 How to Update
```powershell
# Sync latest skills from upstream:
python .agents/update.py --awesome
```

---

### 4. 🗑️ How to Remove / Deactivate
```powershell
python .agents/library/activate_skill.py remove <skill-name>
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
```powershell
python .agents/library/activate_skill.py move <skill-name> --to hot
python .agents/library/activate_skill.py move <skill-name> --to reserve
```
