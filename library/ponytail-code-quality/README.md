# 🧹 Ponytail Code Quality & Tech Debt Suite

> **Upstream Repository**: [https://github.com/DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)  
> **Total Skills**: 6 modular skills  
> **Status**: Offline Reserve (0 prompt tokens until activated)  

Automated code health audits, tech debt analysis, refactoring gain metrics, and clean code inspection.

---

## 📦 Included Modular Skills (6)

| Skill Name | Purpose | Quick Activate |
| :--- | :--- | :--- |
| `ponytail` | Modular intelligence skill | `python .agents/library/activate_skill.py activate ponytail` |
| `ponytail-audit` | Modular intelligence skill | `python .agents/library/activate_skill.py activate ponytail-audit` |
| `ponytail-debt` | Modular intelligence skill | `python .agents/library/activate_skill.py activate ponytail-debt` |
| `ponytail-gain` | Modular intelligence skill | `python .agents/library/activate_skill.py activate ponytail-gain` |
| `ponytail-help` | Modular intelligence skill | `python .agents/library/activate_skill.py activate ponytail-help` |
| `ponytail-review` | Modular intelligence skill | `python .agents/library/activate_skill.py activate ponytail-review` |

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

### 4. 🔄 Rebuild Index
```powershell
python .agents/update.py --index
```
