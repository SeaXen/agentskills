---
description: Search, inspect, and activate any of the 2,031 skills from the 36 offline reserve repositories into your active workspace.
---

# /library Workflow - Skill Library Manager

Manage and activate skills from the local 2,031 skills repository catalog across 36 offline repositories (`.agents/library/`).

## How to Use

### 1. Search Skills
Search the 2,031 skills across all 36 repositories by topic, tool, or framework:
```bash
python .agent/library/activate_skill.py search <keyword>
```
*Examples:*
- `python .agent/library/activate_skill.py search zustand`
- `python .agent/library/activate_skill.py search voice`
- `python .agent/library/activate_skill.py search stripe`

### 2. Activate a Skill
Instantly copy a skill from the library into `.agent/skills/` so your agents can use it:
```bash
python .agent/library/activate_skill.py activate <skill-name>
```

### 3. Inspect a Skill
View a skill's instructions before activating it:
```bash
python .agent/library/activate_skill.py info <skill-name>
```
