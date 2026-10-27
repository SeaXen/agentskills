# Official Anthropic Agent Skills

> **Category**: 🤖 Official Anthropic Skills & Document Automation  
> **Source / Upstream URL**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)  
> **Total Skills in Reserve**: 20 skills  
> **Storage Mode**: Offline Reserve on Disk Only (0 Active Context Tokens)

---

## 📖 Operational Playbook

### 1. 📥 How to Install / Activate into Active Workspace
To activate any skill from this offline reserve into your active AI workspace (`.agents/skills/`):

#### Via Central Activator CLI (Recommended):
```powershell
python .agents/library/activate_skill.py activate academy-guide
```

#### Via Direct Copy (PowerShell):
```powershell
Copy-Item -Recurse -Force ".agents/library/anthropics-official-skills/skills/academy-guide" ".agents/skills/"
```

#### Via Direct Copy (Bash):
```bash
cp -r .agents/library/anthropics-official-skills/skills/academy-guide .agents/skills/
```

---

### 2. 🔗 How to Link (Symlink / Junction)
If you want to use the skill without duplicating disk space, create a Directory Junction (Windows) or Symbolic Link (Linux/macOS):

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py link academy-guide
```

#### Manual Windows Junction:
```powershell
cmd /c mklink /J ".agents\skills\academy-guide" ".agents\library\anthropics-official-skills\skills\academy-guide"
```

#### Manual Linux / macOS Symlink:
```bash
ln -s "$(pwd)/.agents/library/anthropics-official-skills/skills/academy-guide" ".agents/skills/academy-guide"
```

---

### 3. 🔄 How to Update
To update this skill collection from its upstream source:
```powershell
# Update via master vault updater:
python .agents/update.py

# Or update this repository directly via npx skills:
npx skills add anthropics/skills
```

---

### 4. 🗑️ How to Remove / Deactivate
To remove an activated skill from your active workspace and return it to offline reserve:

#### Via Central Activator CLI:
```powershell
python .agents/library/activate_skill.py remove academy-guide
```

#### Manual PowerShell:
```powershell
Remove-Item -Recurse -Force ".agents/skills/academy-guide"
```

---

### 5. 🚚 How to Move (Migrate Between Tiers)
To move a skill between the **Active Hot Set** (`.agent/skills`), **Workspace Store** (`.agents/skills`), or **Offline Reserve** (`.agents/library`):
```powershell
python .agents/library/activate_skill.py move academy-guide --to hot
python .agents/library/activate_skill.py move academy-guide --to reserve
```

---

## 📑 Included Skills Catalog (20 Skills)

| Skill Name | Description |
| :--- | :--- |
| **`academy-guide`** | > Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tut... |
| **`algorithmic-art`** | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code... |
| **`brand-guidelines`** | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when b... |
| **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece... |
| **`claude-api`** | - Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migratio... |
| **`discernment-nudge`** | > After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, ... |
| **`doc-coauthoring`** | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, deci... |
| **`docx`** | "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers in... |
| **`frontend-design`** | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps with aesthetic direction, typography, and... |
| **`internal-comms`** | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill... |
| **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. ... |
| **`pdf`** | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging ... |
| **`pptx`** | "Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, o... |
| **`skill-creator`** | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or opt... |
| **`slack-gif-creator`** | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users... |
| **`template-skill`** | Replace with description of the skill and when Claude should use it. |
| **`theme-factory`** | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with... |
| **`web-artifacts-builder`** | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui... |
| **`webapp-testing`** | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, ca... |
| **`xlsx`** | "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an e... |
