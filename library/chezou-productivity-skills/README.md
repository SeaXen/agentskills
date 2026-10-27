# 💼 Chezou Enterprise Research & Career Skills

> **Upstream Repository**: [https://github.com/chezou/skills](https://github.com/chezou/skills)  
> **Total Skills**: 3 modular skills  
> **Status**: Offline Reserve (0 prompt tokens until activated)  

Deep company intelligence research, resume tailoring, and agent session mailbox utilities.

---

## 📦 Included Modular Skills (3)

| Skill Name | Purpose | Quick Activate |
| :--- | :--- | :--- |
| `company-research` | Modular agent intelligence skill | `python .agents/library/activate_skill.py activate company-research` |
| `resume-tailor` | Modular agent intelligence skill | `python .agents/library/activate_skill.py activate resume-tailor` |
| `session-mailbox` | Modular agent intelligence skill | `python .agents/library/activate_skill.py activate session-mailbox` |

---

## 🛠️ How to Use

### 1. 📥 Activate a Skill into Workspace
```powershell
python .agents/library/activate_skill.py activate <skill-name>
```

### 2. 🔗 Link (Symlink without copying)
```powershell
python .agents/library/activate_skill.py link <skill-name>
```

### 3. 🗑️ Deactivate / Remove
```powershell
python .agents/library/activate_skill.py remove <skill-name>
```
