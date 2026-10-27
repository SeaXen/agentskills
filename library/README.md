# 📚 AgentSkills Offline Reserve Library

> **Total Offline Skills**: 1,470 total skills across 17 upstream repositories  
> **Offline Repositories**: 17 standardized repository bundles  
> **Master Index**: [`library/skills_index.json`](./skills_index.json) (1,470 skills cataloged)  
> **Individual Repo Indexes**: Every single repository includes its own local `skills_index.json`  
> **Context Cost**: **0 Active Tokens** (Never loaded into system prompt until activated)  
> **Purpose**: Serves as your on-disk warehouse for all agent skills across all upstream repositories.

---

## 📑 Complete Repository Directory & Indexes

Every repository is self-contained with its own `skills/` folder, local `skills_index.json`, and individual operational guide:

| Repository Folder | Category | Skills | Index | Individual Guide |
| :--- | :--- | :---: | :---: | :--- |
| **[`antigravity-awesome-skills`](./antigravity-awesome-skills)** | 🌟 Curated Open-Source Skills Ecosystem | 876 | [`JSON`](./antigravity-awesome-skills/skills_index.json) | [Guide](./antigravity-awesome-skills/README.md) |
| **[`anthropics-knowledge-work`](./anthropics-knowledge-work)** | 💼 Operations, Finance, Marketing & Sales | 216 | [`JSON`](./anthropics-knowledge-work/skills_index.json) | [Guide](./anthropics-knowledge-work/README.md) |
| **[`core-antigravity-library`](./core-antigravity-library)** | 🏛️ Core Standards, Architecture & Engineering | 162 | [`JSON`](./core-antigravity-library/skills_index.json) | [Guide](./core-antigravity-library/README.md) |
| **[`magentosh-superpowers`](./magentosh-superpowers)** | ⚡ Multi-Agent Workflows & Orchestration | 86 | [`JSON`](./magentosh-superpowers/skills_index.json) | [Guide](./magentosh-superpowers/README.md) |
| **[`anthropics-official-skills`](./anthropics-official-skills)**| 🤖 Official Anthropic Skills & Docs | 20 | [`JSON`](./anthropics-official-skills/skills_index.json) | [Guide](./anthropics-official-skills/README.md) |
| **[`specialized-community-skills`](./specialized-community-skills)**| 🧩 Integrations (Playwright, Supabase, Neon) | 20 | [`JSON`](./specialized-community-skills/skills_index.json) | [Guide](./specialized-community-skills/README.md) |
| **[`cline-skills`](./cline-skills)** | 🛠️ System Tools & Terminal Automation | 17 | [`JSON`](./cline-skills/skills_index.json) | [Guide](./cline-skills/README.md) |
| **[`emilkowalski-skills`](./emilkowalski-skills)** | ✨ Micro-interactions, Motion & Polish | 15 | [`JSON`](./emilkowalski-skills/skills_index.json) | [Guide](./emilkowalski-skills/README.md) |
| **[`obra-superpowers`](./obra-superpowers)** | 🔮 Developer Diagnostics & Tooling | 15 | [`JSON`](./obra-superpowers/skills_index.json) | [Guide](./obra-superpowers/README.md) |
| **[`vercel-agent-skills`](./vercel-agent-skills)** | ▲ Vercel React 19, Next.js & Server Actions | 9 | [`JSON`](./vercel-agent-skills/skills_index.json) | [Guide](./vercel-agent-skills/README.md) |
| **[`ui-ux-pro-max-skill`](./ui-ux-pro-max-skill)** | 🎨 UI/UX Design System Reasoning | 6 | [`JSON`](./ui-ux-pro-max-skill/skills_index.json) | [Guide](./ui-ux-pro-max-skill/README.md) |
| **[`crypto-skills`](./crypto-skills)** | 🪙 Smart Contract Security & DeFi Protocols | 6 | [`JSON`](./crypto-skills/skills_index.json) | [Guide](./crypto-skills/README.md) |
| **[`academic-research-skills`](./academic-research-skills)** | 📚 Academic Research & Literature Pipeline | 5 | [`JSON`](./academic-research-skills/skills_index.json) | [Guide](./academic-research-skills/README.md) |
| **[`wshobson-agents`](./wshobson-agents)** | 🛡️ Multi-Agent Teams & Session Guards | 5 | [`JSON`](./wshobson-agents/skills_index.json) | [Guide](./wshobson-agents/README.md) |
| **[`antigravity-elite-protocols`](./antigravity-elite-protocols)** | ⚔️ Colosseum Battle, Telemetry & OWL | 4 | [`JSON`](./antigravity-elite-protocols/skills_index.json) | [Guide](./antigravity-elite-protocols/README.md) |
| **[`cloudflare-skills`](./cloudflare-skills)** | ☁️ Cloudflare Workers, Wrangler & Edge | 4 | [`JSON`](./cloudflare-skills/skills_index.json) | [Guide](./cloudflare-skills/README.md) |
| **[`addyosmani-agent-skills`](./addyosmani-agent-skills)** | 🔍 Software Craft & Observability (Addy Osmani) | 4 | [`JSON`](./addyosmani-agent-skills/skills_index.json) | [Guide](./addyosmani-agent-skills/README.md) |

---

## 🗂️ The `skills_index.json` Architecture

Each repository as well as the library root contains a structured `skills_index.json` designed for programmatic exploration, agent tools, and fast scriptable indexing.

### Master Index vs. Repository Indexes
1. **Master Index ([`library/skills_index.json`](./skills_index.json))**: Single JSON array indexing all **1,470 skills** across all 17 library repos.
2. **Individual Repo Indexes (`<repo>/skills_index.json`)**: Scoped to each repository bundle (e.g. `emilkowalski-skills/skills_index.json`).

### Standard JSON Schema
```json
{
  "id": "animate",
  "name": "animate",
  "repository": "emilkowalski-skills",
  "category": "frontend",
  "description": "Build an animation from scratch, making the decisions in the order that determines whether it feels right...",
  "path": "library/emilkowalski-skills/skills/animate",
  "activation_cmd": "python .agents/library/activate_skill.py activate animate",
  "link_cmd": "python .agents/library/activate_skill.py link animate"
}
```

### Auto-Rebuild Indexes
Whenever you run an update or want to refresh the indexes, simply run:
```powershell
python .agents/update.py --index
```
This automatically parses all `SKILL.md` frontmatter, extracts descriptions and tool lists, categorizes skills into domain tags, and regenerates all 17 repo indexes + the master index.

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
To synchronize the latest updates from all upstream repositories into both `library/` and `skills/` and rebuild indexes:
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

### 6. 🔎 Search All 1,470 Skills
```powershell
python .agents/library/activate_skill.py search <keyword>
# or using update.py
python .agents/update.py --find <keyword>
```
