# Cline System Tools & Browser Automation

> **Category**: 🛠️ Tooling, Automation & Terminal Integrations  
> **Source / Upstream URL**: [https://github.com/cline/skills](https://github.com/cline/skills)  
> **Total Skills in Reserve**: 17 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate building-pydantic-ai-agents
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/cline-skills/skills/building-pydantic-ai-agents" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/cline-skills/skills/building-pydantic-ai-agents .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link building-pydantic-ai-agents
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\building-pydantic-ai-agents" ".agents\library\cline-skills\skills\building-pydantic-ai-agents"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/cline-skills/skills/building-pydantic-ai-agents" ".agents/skills/building-pydantic-ai-agents"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add cline/skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove building-pydantic-ai-agents
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/building-pydantic-ai-agents"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move building-pydantic-ai-agents --to hot
python .agents/library/activate_skill.py move building-pydantic-ai-agents --to reserve
```

---

## 📑 Included Skills Catalog (17 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`building-pydantic-ai-agents`** | Build AI agents with Pydantic AI — tools, capabilities (including on-demand loading), structured output, streaming, testing, and multi-agent patterns.... |
| **`convex-design`** | "Design and build reactive, type-safe, production-grade backends on Convex. Covers schema, queries/mutations/actions, indexes, auth, file storage, sch... |
| **`cosmosdb-best-practices`** | Azure Cosmos DB performance optimization and best practices guidelines for NoSQL, partitioning, queries, SDK usage, and vector search. Use when writin... |
| **`data-analyst`** | Act as an interactive data analyst for ClickHouse-backed analytics. Use when the user asks questions about internal data, metrics, dashboards, telemet... |
| **`dataproc-skills`** | Skills to interact with your Dataproc clusters and jobs. |
| **`desktop-commander-overview`** | Use for Desktop Commander MCP capabilities — persistent shells and REPLs, long-running processes, filesystem beyond the workspace, structured files (.... |
| **`endor-setup`** | "Use when user asks to setup endorctl, install endorctl, run endorctl scan, scan for vulnerabilities, run endor scan or run Endor Labs scan or when an... |
| **`exa-search`** | "Deep research powered by Exa. Use for lead generation, literature reviews, deep dives, competitive analysis, or any query where one search falls shor... |
| **`knowledge-catalog-discovery`** | Use these skills when you need to discover and explore data assets in the Knowledge Catalog. It allows you to search for entries, lookup specific meta... |
| **`math-olympiad`** | "Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates ... |
| **`playground`** | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live p... |
| **`review-team`** | Use when the user asks for a code review by a fleet of specialized reviewer agents, wants multiple independent reviewer perspectives, or asks to run r... |
| **`searching-sourcegraph`** | Use when the user needs to search or navigate code with Sourcegraph MCP tools. Provides disciplined search workflows for finding implementations, unde... |
| **`sentry-cli`** | Guide for using the Sentry CLI to interact with Sentry from the command line. Use when the user asks about viewing issues, events, projects, organizat... |
| **`session-report`** | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcri... |
| **`site-specification`** | Extract comprehensive site specifications from simple descriptions. Use when analyzing a user's theme request to determine site type, audience, tone, ... |
| **`vibe-prospecting`** | "Find company & contact data. Turn your agent into a prospecting platform. Get contact information, roles, tech stack, business events, website change... |
