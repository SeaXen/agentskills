# 📚 Antigravity 889+ Skill Library

This directory contains the full, offline clone of [`benjaminasterA/antigravity-awesome-skills`](https://github.com/benjaminasterA/antigravity-awesome-skills) containing **889 modular skills**.

## 💡 Why a Local Library?

Keeping 889 skills active in `.agent/skills/` simultaneously would inject **~75,000 tokens** into every single agent prompt, causing massive latency and model confusion. 

With this **Local Library pattern**:
- **You own all 889 skills on your machine permanently** (3,199 files, full documentation, templates, and scripts).
- Your active workspace (`.agent/skills/`) remains blazing fast with only the core skills active.
- You can activate any skill into your active workspace in 1 second.

---

## 🔍 Commands

### Search the Library
```bash
python .agent/library/activate_skill.py search <keyword>
```

### Activate a Skill
```bash
python .agent/library/activate_skill.py activate <skill-name>
```

### Inspect Skill Instructions
```bash
python .agent/library/activate_skill.py info <skill-name>
```

### Check Library Count
```bash
python .agent/library/activate_skill.py count
```
