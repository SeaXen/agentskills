# 📚 AgentSkills Offline Reserve Library

> **Total Offline Skills**: 1,476 total skills (594 repository skills + 882 awesome skills)  
> **Offline Repositories**: 17 standardized repository bundles  
> **Context Cost**: **0 Active Tokens** (Never loaded into system prompt until activated)  
> **Purpose**: Serves as your on-disk warehouse for all agent skills across all upstream repositories.

---

## 📑 Complete Repository Directory

Every repository is self-contained with its own `skills/` folder and individual operational guide:

| Repository Folder | Category | Skills | Individual Guide |
| :--- | :--- | :---: | :--- |
| **[`antigravity-awesome-skills`](./antigravity-awesome-skills)** | 🌟 Curated Open-Source Skills Ecosystem | 882 | [Guide](./antigravity-awesome-skills/README.md) |
| **[`anthropics-knowledge-work`](./anthropics-knowledge-work)** | 💼 Operations, Finance, Marketing & Sales | 217 | [Guide](./anthropics-knowledge-work/README.md) |
| **[`core-antigravity-library`](./core-antigravity-library)** | 🏛️ Core Standards, Architecture & Engineering | 162 | [Guide](./core-antigravity-library/README.md) |
| **[`magentosh-superpowers`](./magentosh-superpowers)** | ⚡ Multi-Agent Workflows & Orchestration | 86 | [Guide](./magentosh-superpowers/README.md) |
| **[`anthropics-official-skills`](./anthropics-official-skills)**| 🤖 Official Anthropic Skills & Docs | 20 | [Guide](./anthropics-official-skills/README.md) |
| **[`specialized-community-skills`](./specialized-community-skills)**| 🧩 Integrations (Playwright, Supabase, Neon) | 20 | [Guide](./specialized-community-skills/README.md) |
| **[`cline-skills`](./cline-skills)** | 🛠️ System Tools & Terminal Automation | 17 | [Guide](./cline-skills/README.md) |
| **[`emilkowalski-skills`](./emilkowalski-skills)** | ✨ Micro-interactions, Motion & Polish | 15 | [Guide](./emilkowalski-skills/README.md) |
| **[`obra-superpowers`](./obra-superpowers)** | 🔮 Developer Diagnostics & Tooling | 15 | [Guide](./obra-superpowers/README.md) |
| **[`vercel-agent-skills`](./vercel-agent-skills)** | ▲ Vercel React 19, Next.js & Server Actions | 9 | [Guide](./vercel-agent-skills/README.md) |
| **[`ui-ux-pro-max-skill`](./ui-ux-pro-max-skill)** | 🎨 UI/UX Design System Reasoning | 6 | [Guide](./ui-ux-pro-max-skill/README.md) |
| **[`crypto-skills`](./crypto-skills)** | 🪙 Smart Contract Security & DeFi Protocols | 6 | [Guide](./crypto-skills/README.md) |
| **[`academic-research-skills`](./academic-research-skills)** | 📚 Academic Research & Literature Pipeline | 5 | [Guide](./academic-research-skills/README.md) |
| **[`wshobson-agents`](./wshobson-agents)** | 🛡️ Multi-Agent Teams & Session Guards | 5 | [Guide](./wshobson-agents/README.md) |
| **[`antigravity-elite-protocols`](./antigravity-elite-protocols)** | ⚔️ Colosseum Battle, Telemetry & OWL | 4 | [Guide](./antigravity-elite-protocols/README.md) |
| **[`cloudflare-skills`](./cloudflare-skills)** | ☁️ Cloudflare Workers, Wrangler & Edge | 4 | [Guide](./cloudflare-skills/README.md) |
| **[`addyosmani-agent-skills`](./addyosmani-agent-skills)** | 🔍 Software Craft & Observability (Addy Osmani) | 4 | [Guide](./addyosmani-agent-skills/README.md) |

---

## 🛠️ Master Operational Guide

### 1. 📥 Install / Activate a Skill
To activate any skill into your active AI workspace:
```powershell
python .agents/library/activate_skill.py activate <skill-name>
```

### 2. 🔗 Link (Symlink / Junction)
To make a skill available in `.agents/skills/` without copying or duplicating disk space:
```powershell
python .agents/library/activate_skill.py link <skill-name>
```

### 3. 🔄 Update Both Library & Skills
To synchronize the latest updates from all upstream repositories into both `library/` and `skills/`:
```powershell
python .agents/update.py
```

### 4. 🗑️ Remove / Deactivate a Skill
To deactivate a skill from `.agents/skills/`:
```powershell
python .agents/library/activate_skill.py remove <skill-name>
```

### 5. 🚚 Move Between Tiers
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move <skill-name> --to hot
python .agents/library/activate_skill.py move <skill-name> --to reserve
```

### 6. 🔎 Search All 1,476 Skills
```powershell
python .agents/library/activate_skill.py search <keyword>
```
