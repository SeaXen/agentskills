# 🧠 Graphify Codebase Knowledge Graph

> **Upstream Repository**: [https://github.com/Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)  
> **Total Skills**: 1 modular skills  
> **Status**: Offline Reserve (0 prompt tokens until activated)  

Turns any input (code, docs, PRs, issues) into a persistent queryable knowledge graph with clustered communities.

---

## 📦 Included Modular Skills (1)

| Skill Name | Purpose | Quick Activate |
| :--- | :--- | :--- |
| `graphify` | Modular intelligence skill | `python .agents/library/activate_skill.py activate graphify` |

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
