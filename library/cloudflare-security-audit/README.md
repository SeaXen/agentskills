# 🛡️ Cloudflare Security & Attack Surface Audit

> **Upstream Repository**: [https://github.com/cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)  
> **Total Skills**: 1 modular skills  
> **Status**: Offline Reserve (0 prompt tokens until activated)  

Enterprise-grade red-team reconnaissance, LLM boundaries, memory safety, client-side vulnerabilities, and protocol auditing.

---

## 📦 Included Modular Skills (1)

| Skill Name | Purpose | Quick Activate |
| :--- | :--- | :--- |
| `security-audit` | Modular intelligence skill | `python .agents/library/activate_skill.py activate security-audit` |

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
