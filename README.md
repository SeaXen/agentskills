# ⚡ AgentSkills Vault (`SeaXen/agentskills`)

<div align="center">

[![Skills](https://img.shields.io/badge/Skills-87_Active_HotSet-2563EB?style=for-the-badge&logo=anthropic)](./skills)
[![Specialist Agents](https://img.shields.io/badge/Specialist_Agents-20-7C3AED?style=for-the-badge)](./agents)
[![Workflows](https://img.shields.io/badge/Autonomous_Workflows-17-059669?style=for-the-badge)](./workflows)
[![Categories](https://img.shields.io/badge/Categories-16_Functional_Domains-10B981?style=for-the-badge)](./category)
[![Repositories](https://img.shields.io/badge/Upstream_Origins-36_Sources-D97706?style=for-the-badge)](./SKILLS_PROVENANCE.md)
[![Offline Reserve Library](https://img.shields.io/badge/Offline_Reserve_Library-2,031_Skills-DC2626?style=for-the-badge)](./library)

**The complete, production-grade intelligence suite for AI agents (Antigravity IDE, Claude Code, Cursor, Windsurf, Cline).**  
87 curated active hot-set skills, 16 functional category directories (1,878+ cataloged skills), 20 domain-specialist personas, 17 automated slash workflows, and 2,031 offline reserve library skills across 36 repositories.

[Quick Start](#-quick-start--installation) • [Upstream Repositories](#-upstream-repositories-breakdown) • [How to Update](#-how-to-update) • [Architecture](#-directory-architecture) • [Provenance Registry](./SKILLS_PROVENANCE.md)

</div>


---

## 🗂️ Functional Categories Taxonomy (`.agents/category/`)

All 1,878+ skills across active workspace and offline library repositories are classified into **16 functional category folders** in [`.agents/category/`](./category). Every folder contains **Windows directory junctions** for seamless in-editor browsing and a complete Markdown catalog:

| Category Folder | Domain | Description |
| :--- | :--- | :--- |
| **[`core-antigravity`](./category/core-antigravity)** | ⚔️ Core Kit Protocols | Colosseum battle, telemetry, benchmark, OWL, compaction, and prompt engineering. |
| **[`software-engineering`](./category/software-engineering)** | 🏛️ Code Craft & Architecture | Clean code standards, refactoring, code review, git worktrees, and architecture. |
| **[`frontend-ui`](./category/frontend-ui)** | 🎨 Frontend & UI Motion | React 19, Next.js, Tailwind CSS, Emil animations, Radix UI, and Shadcn components. |
| **[`backend-api`](./category/backend-api)** | ⚡ Backend & Microservices | API design, Node.js, Python, NestJS, microservices, and hardened REST endpoints. |
| **[`database-storage`](./category/database-storage)** | 🗄️ Database & Query Tuning | PostgreSQL, Supabase, Neon serverless, SQLite, Drizzle ORM, and Prisma. |
| **[`devops-cloud`](./category/devops-cloud)** | ☁️ Cloud & Infrastructure | Vercel, Cloudflare Pages/Workers, Docker, Kubernetes, CI/CD, and deployment. |
| **[`security-audit`](./category/security-audit)** | 🛡️ Security & Pentesting | Vulnerability scanning, threat modeling, red teaming, OWASP, and smart contracts. |
| **[`testing-qa`](./category/testing-qa)** | 🧪 Automated Testing & QA | Playwright headless testing, E2E automation, TDD workflows, and mutation tests. |
| **[`ai-agents`](./category/ai-agents)** | 🤖 Autonomous AI Agents | Hermes skills, LobeHub capabilities, multi-agent orchestration, and prompt design. |
| **[`data-ml`](./category/data-ml)** | 📊 Data Engineering & ML | BigQuery SQL optimization, Dataproc, Apache Spark, Dataflow, and notebooks. |
| **[`mobile-development`](./category/mobile-development)** | 📱 Mobile Apps (iOS/Android) | React Native, Flutter, Swift, Kotlin, Expo, and Apple HIG guidelines. |
| **[`web3-crypto`](./category/web3-crypto)** | 🪙 Web3 & Blockchain | Solidity smart contracts, EVM security, DeFi protocol templates, and tokens. |
| **[`design-creative`](./category/design-creative)** | 🎬 Creative Design & Video | HeyGen Hyperframes, Lemo Opuscar video, Remotion React, and 3D Three.js. |
| **[`business-operations`](./category/business-operations)** | 💼 Enterprise & Operations | Accounting, invoices, AP processing, financial models, CRM, and sales outreach. |
| **[`productivity-workflow`](./category/productivity-workflow)** | 🚀 Productivity & Team Ops | Notion integrations, Slack search & messaging, Linear tracking, and standups. |
| **academic-research** | 🔬 Academic & Bio-Research | K-Dense scientific skills, paper writing pipeline, literature review, and RNA-QC. |

> 💡 **Tip**: Browse any category in your file explorer at `D:\Repo\.agents\category\<domain>` to see and open skills directly!

---

## 📖 Table of Contents
1. [Overview](#-overview)
2. [Functional Categories Taxonomy (`category/`)](#-functional-categories-taxonomy)
2. [Quick Start & Installation](#-quick-start--installation)
   - [Clone Full Vault](#1-install-full-vault-together-recommended)
   - [Install Individual Repositories](#2-install-individual-repositories-via-npx-skills)
   - [Copy Specific Skills](#3-copy-specific-skills-manually)
3. [How to Update](#-how-to-update)
   - [Update Full Vault](#1-update-the-full-vault)
   - [Update from Upstream Source](#2-update-from-upstream-repositories)
   - [Update a Single Skill](#3-update-a-single-skill)
4. [Token Budgeting & Hot-Set Activation](#-token-budgeting--active-hot-set)
5. [Upstream Repositories Breakdown (Interactive)](#-upstream-repositories-breakdown)
6. [Specialist Agents (20 Personas)](#-specialist-agents-20-personas)
7. [Autonomous Workflows (17 Slash Commands)](#-autonomous-workflows-17-commands)
8. [Directory Architecture](#-directory-architecture)
9. [License & Attribution](#-license--attribution)

---

## 🌟 Overview

Modern AI coding agents become dramatically more capable when augmented with targeted domain instructions (**skills**), strict execution personas (**agents**), and verified lifecycle rules (**workflows**).

This vault consolidates the highest-quality open-source and proprietary agent skills into a single, standardized, and version-controlled repository:
- **594 Verified Skills**: Covering React 19, Cloudflare, Next.js, Postgres, smart contract security, UI animation, literature research, and enterprise operations.
- **Zero Prompt Bloat**: Configured to work seamlessly with Antigravity context budgeting (87 active hot-set engineering skills in `.agents/skills`, 16 organized domain categories in `.agents/category`, and 2,031 skills in offline reserve library across 36 repositories).
- **100% Traceable Provenance**: Every skill is locked to its upstream author, source URL, and git hash in `skills-lock.json`.

---


---

## 🚦 Beginner's Cheat Sheet (The Only 3 Commands You Need!)

If all the different commands and tools feel overwhelming, don't worry! **You only need 3 simple actions for your daily work:**

### 1️⃣ Find any skill in your vault
```powershell
python update.py --find <name>
# Example: python update.py --find animation
```

### 2️⃣ Turn ON a skill from your offline warehouse
```powershell
python library/activate_skill.py link <skill-name>
# Example: python library/activate_skill.py link hyperframes
```
*(This makes the skill instantly available to your AI assistant without duplicating disk space!)*

### 3️⃣ Update everything & backup to your GitHub
```powershell
python update.py
```
*(Or simply double-click `update.bat` in Windows File Explorer!)*

---

### ❓ NPX vs. Python — Made Super Simple:
* **Why does everyone talk about `npx`?**  
  `npx` is for **downloading skills from the internet** into a project. Any person anywhere can install skills from your GitHub by running:  
  `npx -y skills add SeaXen/agentskills --skill <name>`
* **Why do we use `python` locally?**  
  Python is your **private local manager**. It manages your on-disk storage room of **1763 reserve skills** so they don't slow down your AI's brain with unnecessary prompt tokens.
* **Prefer npm instead of python?**  
  You can also type `npm run find <name>`, `npm run link <name>`, or `npm run update`!

---

## ⚡ 1-Click Instant Install

You can install the entire AgentSkills vault (594 skills, 20 agents, 17 workflows) into **any project workspace** with a single command:

#### 🪟 Windows (PowerShell):
```powershell
irm https://raw.githubusercontent.com/SeaXen/agentskills/main/install.ps1 | iex
```

#### 🍎 macOS & 🐧 Linux (Bash):
```bash
curl -fsSL https://raw.githubusercontent.com/SeaXen/agentskills/main/install.sh | bash
```

---

## 🔄 1-Click Regular Updates

To keep your installed skills updated with the latest improvements from upstream repositories:

#### 1-Line Terminal Command:
```powershell
# In your project root:
git -C .agents pull
```

#### Automated Full Vault Updater (With automatic git commit & push):
```powershell
# Run the interactive updater:
.\.agents\update.ps1
```

---

## 🚀 Quick Start & Installation

### 1. Install Full Vault Together (Recommended)

To give any project or workspace access to the entire vault, clone directly into your project's `.agents` directory:

```bash
# In your project root:
git clone https://github.com/SeaXen/agentskills.git .agents
```

If you prefer using Git Submodules:
```bash
git submodule add https://github.com/SeaXen/agentskills.git .agents
```

*(Optional)* To also give the active Antigravity engine immediate access to the curated hot-set:
```powershell
# Copy the 89 curated hot skills into .agent/skills
robocopy .agents/skills .agent/skills clean-code architecture vercel-react-best-practices /E
```

---

### 2. Install Individual Repositories via `npx skills`

If you only need specific components from this vault, you can install individual upstream repositories directly using the `npx skills` CLI:

```bash
# Emil Kowalski UI Motion & Micro-interactions (15 skills)
npx skills add emilkowalski/skills

# Vercel React & Next.js Best Practices (9 skills)
npx skills add vercel-labs/agent-skills

# Cloudflare Workers, Wrangler & Edge (4 skills)
npx skills add cloudflare/skills

# Multi-Agent Team Orchestration (86 skills)
npx skills add magentosh/superpowers

# Academic Research & Paper Pipeline (5 skills)
npx skills add imbad0202/academic-research-skills

# UI/UX Pro Max Design Intelligence (6 skills)
npx skills add nextlevelbuilder/ui-ux-pro-max-skill

# Official Anthropic Core Skills (20 skills)
npx skills add anthropics/skills
```

---

### 3. Copy Specific Skills Manually

All skills are completely self-contained in `.agents/skills/<skill-name>/` with a standard `SKILL.md` instruction file:

```powershell
# Windows PowerShell example:
Copy-Item -Recurse -Force ".agents/skills/clean-code" "my-project/.agents/skills/"
Copy-Item -Recurse -Force ".agents/skills/emil-design-eng" "my-project/.agents/skills/"
```

```bash
# macOS / Linux Bash example:
cp -r .agents/skills/clean-code my-project/.agents/skills/
cp -r .agents/skills/emil-design-eng my-project/.agents/skills/
```

---

## 🔄 How to Update

### 1. Update the Full Vault
Pull all new skills, improvements, and agent updates with standard git:
```bash
cd .agents
git pull origin main
```

### 2. Update from Upstream Repositories
To fetch upstream changes from original authors:
```bash
# Update an entire repo suite:
npx skills add emilkowalski/skills
npx skills add cloudflare/skills
npx skills add vercel-labs/agent-skills
```

### 3. Update a Single Skill
```bash
npx skills add addyosmani/agent-skills --skill doubt-driven-development
npx skills add juliusbrussee/caveman --skill caveman-review
```

---

## 🎯 Token Budgeting & Active Hot Set

Antigravity IDE limits active system prompt skills to **~100 skills** to prevent context exhaustion and token warnings. This repository solves that using a **2-Tier Architecture**:

1. **Full Store (`.agents/skills/`)**: All **594 skills** remain permanently saved and searchable on disk.
2. **Active Hot Set (`.agent/skills/`)**: **89 curated high-signal skills** are loaded into active AI context for instant zero-latency reasoning.
3. **On-Demand Activation**: Need a skill that isn't currently active? Activate it in one command:
   ```powershell
   python .agents/library/activate_skill.py <skill-name>
   ```

---

## 📦 Upstream Repositories Breakdown

Below is the complete interactive inventory of all 32 upstream repositories and their included skills. **Click any repository to expand or collapse its skill list.**

| Source Repository / Origin | Skills | Category | Quick Update Command |
| :--- | :---: | :--- | :--- |
| **`anthropics/knowledge-work-plugins`** | 216 | 💼 Business, Marketing, Finance & Enterprise Operations | `npx skills add anthropics/knowledge-work-plugins` |
| **`local-library`** | 162 | 🏛️ Core Engineering, Design Systems & Agent Infrastructure | `python library/activate_skill.py <skill-name>` |
| **`magentosh/superpowers`** | 86 | ⚡ Multi-Agent Orchestration, Planning & Execution | `npx skills add magentosh/superpowers` |
| **`anthropics/skills`** | 20 | 🤖 Official Anthropic Skills Suite | `npx skills add anthropics/skills` |
| **`cline/skills`** | 17 | 🛠️ Tooling, Automation & Browser Execution | `npx skills add cline/skills` |
| **`emilkowalski/skills`** | 15 | ✨ UI Craft, Animations & Motion Engineering (Emil Kowalski) | `npx skills add emilkowalski/skills` |
| **`obra/superpowers`** | 15 | 🔮 Developer Superpowers & Diagnostics | `npx skills add obra/superpowers` |
| **`vercel-labs/agent-skills`** | 9 | ▲ Vercel, Next.js & React 19 Best Practices | `npx skills add vercel-labs/agent-skills` |
| **`nextlevelbuilder/ui-ux-pro-max-skill`** | 6 | 🎨 UI/UX Pro Max Design Intelligence | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill` |
| **`kukapay/crypto-skills`** | 6 | 🪙 Web3, EVM & DeFi Protocol Architecture | `npx skills add kukapay/crypto-skills` |
| **`imbad0202/academic-research-skills`** | 5 | 📚 Academic Research, Paper Writing & Literature Screening | `npx skills add imbad0202/academic-research-skills` |
| **`wshobson/agents`** | 5 | 🛡️ Agent Teams & Session Guardrails | `npx skills add wshobson/agents` |
| **`Antigravity Kit (Local Workspace)`** | 4 | ⚔️ Elite Adversarial & Telemetry Protocols | `Directly maintained in .agents/workflows and .agents/skills` |
| **`cloudflare/skills`** | 4 | ☁️ Cloudflare Edge, Workers & D1 Architecture | `npx skills add cloudflare/skills` |
| **`addyosmani/agent-skills`** | 4 | 🔍 Engineering Craft & Observability (Addy Osmani) | `npx skills add addyosmani/agent-skills` |
| **`microsoft/playwright-cli`** | 2 | 🎭 Real-Browser Automation & Headless Testing | `npx skills add microsoft/playwright-cli` |
| **`uizze.sh`** | 2 | 📱 iOS Design & Aesthetics Taste System | `npx skills add https://uizze.sh/` |
| **`supabase/agent-skills`** | 2 | ⚡ Supabase & Postgres Best Practices | `npx skills add supabase/agent-skills` |
| **`SeaXen/app-production-readiness`** | 1 | 🚀 21-Gate Adaptive Deploy & QA Review | `npx skills add SeaXen/app-production-readiness` |
| **`juliusbrussee/caveman`** | 1 | 🔍 High-Density Compressed Code Review | `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-review` |
| **`buzzbysolcex/buzz-bd-agent`** | 1 | 🤝 Web3 BD & Ecosystem Growth | `npx skills add https://github.com/buzzbysolcex/buzz-bd-agent` |
| **`designed-by-ai/skills`** | 1 | 🍎 Apple HIG & Premium Ecosystem Design | `npx skills add designed-by-ai/skills` |
| **`Leonxlnx/taste-skill`** | 1 | 👁️ Modern Frontend Visual Taste | `npx skills add Leonxlnx/taste-skill` |
| **`getsentry/skills`** | 1 | 🐛 Sentry Bug Finding & Vulnerability Audit | `npx skills add getsentry/skills` |
| **`vercel-labs/skills`** | 1 | ▲ Vercel One-Click Deploy Tooling | `npx skills add vercel-labs/skills` |
| **`udaysharmadev/Gravitas`** | 1 | 🧠 Cognitive Focus & High-Impact Work | `npx skills add udaysharmadev/Gravitas` |
| **`pbakaus/impeccable`** | 1 | 🎯 Impeccable Design Critique (Paul Bakaus) | `npx skills add pbakaus/impeccable` |
| **`neondatabase/agent-skills`** | 1 | 🐘 Serverless Postgres Architecture (Neon) | `npx skills add neondatabase/agent-skills` |
| **`SeaXen/app-production-readiness (Legacy alias)`** | 1 | 🔄 Backward Compatibility Alias | `npx skills add SeaXen/app-production-readiness` |
| **`humanlayer/skills`** | 1 | 🐙 GitHub Pull Request Formatting | `npx skills add humanlayer/skills` |
| **`Shpigford/skills`** | 1 | 📸 Automated Marketing Screenshots | `npx skills add Shpigford/skills` |
| **`shadcn-ui/ui`** | 1 | 🧱 shadcn/ui Component Registry | `npx skills add shadcn-ui/ui` |

---

### 📂 Detailed Interactive Skill Manifest

<details>
<summary><b>💼 Business, Marketing, Finance & Enterprise Operations — <code>anthropics/knowledge-work-plugins</code> (216 skills)</b></summary>

> **Repository Source**: [https://github.com/anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)  
> **Description**: Enterprise workflow suite by Anthropic covering strategic finance, marketing campaigns, customer success, sales outreach, operations, and product analytics.  
> **Update Command**: `npx skills add anthropics/knowledge-work-plugins`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`accessibility-review`** | Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design f... | `design/skills/accessibility-review/SKILL.md` |
| **`account-context`** | 360-degree view of an account - CRM data, recent email threads, docs, transcripts, and internal chat chatter, synthesized into one brief. Use when the user asks... | `sales/skills/account-context/SKILL.md` |
| **`account-plan`** | Build or refresh a strategic account plan - current state, goals, stakeholder coverage, opportunity map, risks, and the action plan - written to a doc and key f... | `sales/skills/account-plan/SKILL.md` |
| **`account-research`** | Research a target company and optionally a specific contact - company overview, recent news, likely priorities, and fit against your ICP. Cross-references exist... | `sales/skills/account-research/SKILL.md` |
| **`account-tiering`** | Score and tier a list of accounts (or your full book) against ICP fit and engagement signals to prioritize where to spend time. Use when the user asks to "tier ... | `sales/skills/account-tiering/SKILL.md` |
| **`ad-manager`** | > The ads consultant that becomes an ads agent. Reads paid-ad performance natively through the TikTok Ads connector, or via a build-connector Zapier connection ... | `small-business/skills/ad-manager/SKILL.md` |
| **`analyze`** | Answer data questions -- from quick lookups to full analyses. Use when looking up a single metric, investigating what's driving a trend or drop, comparing segme... | `data/skills/analyze/SKILL.md` |
| **`ap-processor`** | > Works the bill pile end to end: reads bills and vendor statements out of the AP inbox or from uploaded PDFs and phone photos, pulls out vendor, amount, due da... | `small-business/skills/ap-processor/SKILL.md` |
| **`architecture`** | Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-... | `engineering/skills/architecture/SKILL.md` |
| **`audit-support`** | Support SOX 404 compliance with control testing methodology, sample selection, and documentation standards. Use when generating testing workpapers, selecting au... | `finance/skills/audit-support/SKILL.md` |
| **`brand-review`** | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. Use when checking... | `marketing/skills/brand-review/SKILL.md` |
| **`brand-style`** | > Sets and updates the owner's brand look and output preferences, which every page and document the plugin produces then follows automatically. Captures the bra... | `small-business/skills/brand-style/SKILL.md` |
| **`brand-voice-enforcement`** | > This skill applies brand guidelines to content creation. It should be used when the user asks to "write an email", "draft a proposal", "create a pitch deck", ... | `partner-built/brand-voice/skills/brand-voice-enforcement/SKILL.md` |
| **`brief`** | Generate contextual briefings for legal work — daily summary, topic research, or incident response. Use when starting your day and need a scan of legal-relevant... | `legal/skills/brief/SKILL.md` |
| **`build-agent`** | > Turns a task the owner keeps doing by hand into a named, reusable skill they can trigger by name or put on a schedule. Watches them do it once or listens to t... | `small-business/skills/build-agent/SKILL.md` |
| **`build-connector`** | > Gets Claude talking to a tool nobody built an official connector for. Works out what the system is, checks the Claude connector directory for an existing conn... | `small-business/skills/build-connector/SKILL.md` |
| **`build-dashboard`** | Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a share... | `data/skills/build-dashboard/SKILL.md` |
| **`build-zoom-bot`** | Build a Zoom meeting bot, recorder, or real-time media workflow. Use when joining meetings programmatically, processing live media or transcripts, or combining ... | `partner-built/zoom-plugin/skills/build-zoom-bot/SKILL.md` |
| **`build-zoom-contact-center-app`** | "Reference skill for Zoom Contact Center. Use after routing to a contact-center workflow when implementing app, web, or native integrations; engagement context ... | `partner-built/zoom-plugin/skills/contact-center/SKILL.md` |
| **`build-zoom-meeting-app`** | Build or embed a Zoom meeting flow. Use when implementing Meeting SDK joins, web or mobile meeting embeds, meeting lifecycle flows, or when deciding between Mee... | `partner-built/zoom-plugin/skills/build-zoom-meeting-app/SKILL.md` |
| **`build-zoom-meeting-sdk-app`** | Reference skill for Zoom Meeting SDK. Use after routing to a meeting-embed workflow when implementing real Zoom meeting joins, platform-specific SDK behavior, a... | `partner-built/zoom-plugin/skills/meeting-sdk/SKILL.md` |
| **`build-zoom-phone-integration`** | "Reference skill for Zoom Phone. Use after routing to a phone workflow when implementing OAuth, Phone APIs, webhooks, Smart Embed events, URI schemes, CRM or CT... | `partner-built/zoom-plugin/skills/phone/SKILL.md` |
| **`build-zoom-rest-api-app`** | "Reference skill for Zoom REST API. Use after choosing an API-based workflow when you need endpoint selection, resource-management patterns, OAuth requirements,... | `partner-built/zoom-plugin/skills/rest-api/SKILL.md` |
| **`build-zoom-team-chat-app`** | "Reference skill for Zoom Team Chat. Use after routing to a chat workflow when building user-scoped messaging integrations, chatbot experiences, rich cards, but... | `partner-built/zoom-plugin/skills/team-chat/SKILL.md` |
| **`build-zoom-video-sdk-app`** | Reference skill for Zoom Video SDK. Use after routing to a custom-session workflow when the user needs full control over the video experience rather than an act... | `partner-built/zoom-plugin/skills/video-sdk/SKILL.md` |
| **`build-zoom-virtual-agent`** | "Reference skill for Zoom Virtual Agent. Use after routing to a virtual-agent workflow when implementing web embeds, Android or iOS wrapper integrations, knowle... | `partner-built/zoom-plugin/skills/virtual-agent/SKILL.md` |
| **`business-pulse`** | > Produces a one-page cross-functional business snapshot for SMB owners — cash position (the ledger: MYOB, NetSuite, QuickBooks, Xero, or Zoho Books), sales tre... | `small-business/skills/business-pulse/SKILL.md` |
| **`call-list`** | Builds today's call list. Runs lead-triage to rank the top-5 leads most worth calling, supplies talking points from email history, blocks time on the calendar, ... | `small-business/skills/call-list/SKILL.md` |
| **`call-prep`** | Pre-call brief for an upcoming meeting - attendees, account history, prior call context from transcripts, open opportunity status, and suggested discovery quest... | `sales/skills/call-prep/SKILL.md` |
| **`call-summary`** | Turn a call transcript or call notes into a customer follow-up email draft, an internal chat summary, and proposed CRM updates. Use when the user says "call sum... | `sales/skills/call-summary/SKILL.md` |
| **`campaign-plan`** | Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. Use when planning a product launch... | `marketing/skills/campaign-plan/SKILL.md` |
| **`canva-creator`** | > Takes an approved content brief and executes a campaign end-to-end: builds the posting calendar, generates Canva designs for social posts, drafts caption and ... | `small-business/skills/canva-creator/SKILL.md` |
| **`capacity-plan`** | Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you need the ... | `operations/skills/capacity-plan/SKILL.md` |
| **`cash-flow-snapshot`** | > Reads AR/AP, historical cash timing, and known fixed costs from the ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) or from PayPal, Square, or Stripe... | `small-business/skills/cash-flow-snapshot/SKILL.md` |
| **`change-request`** | Create a change management request with impact analysis and rollback plan. Use when proposing a system or process change that needs approval, preparing a change... | `operations/skills/change-request/SKILL.md` |
| **`choose-zoom-approach`** | Choose the right Zoom architecture for a use case. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, Video SDK, Zoom Apps SDK, Zoom MCP, Ph... | `partner-built/zoom-plugin/skills/choose-zoom-approach/SKILL.md` |
| **`close-management`** | Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, ident... | `finance/skills/close-management/SKILL.md` |
| **`close-month`** | Closes the books and turns them into a decision as a three-link chain — month-end-prep reconciles the ledger against every connected payment processor and write... | `small-business/skills/close-month/SKILL.md` |
| **`close-plan`** | Build the business case and mutual action plan for a deal - the why-buy/why-now story, the ROI framing, and the dated step-by-step path to signature shared with... | `sales/skills/close-plan/SKILL.md` |
| **`code-review`** | Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when check... | `engineering/skills/code-review/SKILL.md` |
| **`comp-analysis`** | Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this e... | `human-resources/skills/comp-analysis/SKILL.md` |
| **`competitive-brief`** | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. Use when building sales battlecards, whe... | `marketing/skills/competitive-brief/SKILL.md` |
| **`competitive-intelligence`** | Competitive analysis two ways - the in-deal play against a named competitor, and win/loss patterns, competitor mentions, and battlecards across the book. Use wh... | `sales/skills/competitive-intelligence/SKILL.md` |
| **`compliance-check`** | Run a compliance check on a proposed action, product feature, or business initiative, surfacing applicable regulations, required approvals, and risk areas. Use ... | `legal/skills/compliance-check/SKILL.md` |
| **`compliance-tracking`** | Track compliance requirements and audit readiness. Trigger with "compliance", "audit prep", "SOC 2", "ISO 27001", "GDPR", "regulatory requirement", or when the ... | `operations/skills/compliance-tracking/SKILL.md` |
| **`compose-outreach`** | "Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message for... | `partner-built/common-room/skills/compose-outreach/SKILL.md` |
| **`contact-research`** | "Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any contac... | `partner-built/common-room/skills/contact-research/SKILL.md` |
| **`content-creation`** | Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. Use when writing any mar... | `marketing/skills/content-creation/SKILL.md` |
| **`content-strategy`** | > Analyzes sales data from PayPal and QuickBooks to find top performers and slow movers, layers in seasonality, and produces a prioritized 30-day content brief:... | `small-business/skills/content-strategy/SKILL.md` |
| **`contract-review`** | > Lightweight NDA, MSA, and vendor contract review for SMBs without legal on staff. Reads contracts from local files, mail attachments (Gmail or M365), a connec... | `small-business/skills/contract-review/SKILL.md` |
| **`cowork-plugin-customizer`** | > Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, set up plugin, configure plugin, tailor plugin, ... | `cowork-plugin-management/skills/cowork-plugin-customizer/SKILL.md` |
| **`create-an-asset`** | Build a customer deck, one-pager or leave-behind from your account data, call notes and approved materials, with no made-up numbers. Use when the user asks for ... | `sales/skills/create-an-asset/SKILL.md` |
| **`create-cowork-plugin`** | > Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop... | `cowork-plugin-management/skills/create-cowork-plugin/SKILL.md` |
| **`create-viz`** | Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a chart, selecting the right chart type for a trend or... | `data/skills/create-viz/SKILL.md` |
| **`crm-autopilot`** | > Keeps the CRM current without the owner ever opening it. Creates and updates contacts and deals from email, calendar, and call transcripts; logs activity auto... | `small-business/skills/crm-autopilot/SKILL.md` |
| **`crm-hygiene-check`** | Read-only audit of your CRM opportunities for missing fields, stale dates, and stage mismatches - outputs a fix checklist to apply by hand or through update-opp... | `sales/skills/crm-hygiene-check/SKILL.md` |
| **`customer-escalation`** | Package an escalation for engineering, product, or leadership with full context. Use when a bug needs engineering attention beyond normal support, multiple cust... | `customer-support/skills/customer-escalation/SKILL.md` |
| **`customer-health`** | Health check on a customer account and QBR-ready prep - relationship strength, engagement trend, risk signals, value delivered, and the agenda that makes the re... | `sales/skills/customer-health/SKILL.md` |
| **`customer-research`** | Multi-source research on a customer question or topic with source attribution. Use when a customer asks something you need to look up, investigating whether a b... | `customer-support/skills/customer-research/SKILL.md` |
| **`customer-voice`** | Surface what customers are actually saying - direct attributed quotes on a topic across call transcripts and email, across your accounts. Use when the user asks... | `sales/skills/customer-voice/SKILL.md` |
| **`daily-briefing`** | Morning rundown - today's meetings with account context, opps closing soon with stale flags, waiting customer emails, and the day's top actions. Use when the us... | `sales/skills/daily-briefing/SKILL.md` |
| **`data-context-extractor`** | > Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts. BOOTSTRAP MODE - Triggers: "Create a data context ski... | `data/skills/data-context-extractor/SKILL.md` |
| **`deal-advance-gap`** | Forward-looking gap check on one opportunity - exactly what is missing to advance it to the next stage and to close, with who does what by when. Use when the us... | `sales/skills/deal-advance-gap/SKILL.md` |
| **`deal-review`** | Deep-dive on a single opportunity - signal-adjusted health score, risks, gaps in qualification, and recommended next actions. Use when the user asks "review the... | `sales/skills/deal-review/SKILL.md` |
| **`deal-signals`** | Proactive watch over your book - deals gone quiet, close dates slipping into view, champion changes, renewal windows opening, competitor mentions - surfaced as ... | `sales/skills/deal-signals/SKILL.md` |
| **`deal-slip-scenario`** | Model what happens to your number if a deal slips, shrinks, or dies - quota impact, coverage ratio change, and the substitute pipeline needed to stay on plan. U... | `sales/skills/deal-slip-scenario/SKILL.md` |
| **`debug`** | Structured debugging session — reproduce, isolate, diagnose, and fix. Trigger with an error message or stack trace, "this works in staging but not prod", "somet... | `engineering/skills/debug/SKILL.md` |
| **`debug-zoom`** | Debug a broken Zoom integration by isolating the failure point and routing into the right Zoom references. Use when auth, API, webhook, SDK, or MCP behavior is ... | `partner-built/zoom-plugin/skills/debug-zoom/SKILL.md` |
| **`debug-zoom-integration`** | Debug broken Zoom implementations quickly. Use when auth, webhooks, SDK joins, MCP transport, or real-time media workflows are failing and you need to isolate t... | `partner-built/zoom-plugin/skills/debug-zoom-integration/SKILL.md` |
| **`deploy-checklist`** | Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and a... | `engineering/skills/deploy-checklist/SKILL.md` |
| **`design-critique`** | Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of this s... | `design/skills/design-critique/SKILL.md` |
| **`design-handoff`** | Generate developer handoff specs from a design. Use when a design is ready for engineering and needs a spec sheet covering layout, design tokens, component prop... | `design/skills/design-handoff/SKILL.md` |
| **`design-mcp-workflow`** | Design a Zoom MCP workflow for Claude. Use when deciding whether Zoom MCP fits a task, when planning tool-based AI workflows, or when separating MCP responsibil... | `partner-built/zoom-plugin/skills/design-mcp-workflow/SKILL.md` |
| **`design-system`** | Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a c... | `design/skills/design-system/SKILL.md` |
| **`digest`** | Generate a daily or weekly digest of activity across all connected sources. Use when catching up after time away, starting the day and wanting a summary of ment... | `enterprise-search/skills/digest/SKILL.md` |
| **`discover-brand`** | > This skill orchestrates autonomous discovery of brand materials across enterprise platforms (Notion, Confluence, Google Drive, Box, SharePoint, Figma, Gong, G... | `partner-built/brand-voice/skills/discover-brand/SKILL.md` |
| **`documentation`** | Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when th... | `engineering/skills/documentation/SKILL.md` |
| **`draft-content`** | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations. Use... | `marketing/skills/draft-content/SKILL.md` |
| **`draft-offer`** | Draft an offer letter with comp details and terms. Use when a candidate is ready for an offer, assembling a total comp package (base, equity, signing bonus), wr... | `human-resources/skills/draft-offer/SKILL.md` |
| **`draft-outreach`** | Draft a personalized outreach email or multi-touch sequence to a prospect, create it as an email draft for review, and add the contact to a sequence in your sal... | `sales/skills/draft-outreach/SKILL.md` |
| **`draft-response`** | Draft a professional customer-facing response tailored to the situation and relationship. Use when answering a product question, responding to an escalation or ... | `customer-support/skills/draft-response/SKILL.md` |
| **`email-sequence`** | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. Use when building onboarding, lead ... | `marketing/skills/email-sequence/SKILL.md` |
| **`end-of-day`** | The closing beat of the day - every call processed or explicitly skipped, the CRM brought current, commitments captured, and tomorrow's top three teed up. Use w... | `sales/skills/end-of-day/SKILL.md` |
| **`enrich-lead`** | "Instant lead enrichment. Drop a name, company, LinkedIn URL, or email and get the full contact card with email, phone, title, company intel, and next actions." | `partner-built/apollo/skills/enrich-lead/SKILL.md` |
| **`expansion-whitespace`** | Find the expansion whitespace in an account or a book - what they own vs. what they could own, the evidence for each play, and the open opps to create. Use when... | `sales/skills/expansion-whitespace/SKILL.md` |
| **`explore-data`** | Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distribu... | `data/skills/explore-data/SKILL.md` |
| **`financial-statements`** | Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis. Use when preparing a monthl... | `finance/skills/financial-statements/SKILL.md` |
| **`forecast`** | Generate the commit / best-case / pipeline narrative for a forecast call or a 1:1 with your manager - what's closing, what's at risk, what changed since last ti... | `sales/skills/forecast/SKILL.md` |
| **`grant-rfp-writer`** | > Finds grant and solicitation opportunities the organization actually qualifies for, runs a hard go/no-go before anyone starts writing, drafts the application ... | `small-business/skills/grant-rfp-writer/SKILL.md` |
| **`grow-pipeline`** | Fills the funnel end to end without the owner babysitting it — reads the market and the competition for context, builds a ranked list of named prospects with a ... | `small-business/skills/grow-pipeline/SKILL.md` |
| **`growth-pulse`** | > Answers one question for an SMB owner — is the growth engine actually working? Pulls sales trend by channel, funnel conversion, campaign return, best and wors... | `small-business/skills/growth-pulse/SKILL.md` |
| **`guideline-generation`** | > This skill generates, creates, or builds brand voice guidelines from source materials. It should be used when the user asks to "generate brand guidelines", "c... | `partner-built/brand-voice/skills/guideline-generation/SKILL.md` |
| **`handle-objection`** | Work through a live objection or competitive threat - what's really being said, the response that has worked before, and the proof points to use, grounded in yo... | `sales/skills/handle-objection/SKILL.md` |
| **`hiring-screener`** | > Takes a pile of applications and turns it into a ranked shortlist, scored only against the job's stated rubric, with drafted replies to every candidate, sched... | `small-business/skills/hiring-screener/SKILL.md` |
| **`inbox-manager`** | > Turns a full inbox into a short, ranked list of what actually needs the owner. Reads the mail, sorts it into needs-you, drafted-and-waiting, and handled, writ... | `small-business/skills/inbox-manager/SKILL.md` |
| **`inbox-sweep`** | Batch-process unread customer emails - classify, prioritize, and draft replies. Use when the user asks "sweep my inbox", "what customer emails need a reply", "d... | `sales/skills/inbox-sweep/SKILL.md` |
| **`incident-response`** | Run an incident response workflow — triage, communicate, and write postmortem. Trigger with "we have an incident", "production is down", an alert that needs sev... | `engineering/skills/incident-response/SKILL.md` |
| **`instrument-data-to-allotrope`** | Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientist... | `bio-research/skills/instrument-data-to-allotrope/SKILL.md` |
| **`interview-prep`** | Create structured interview plans with competency-based questions and scorecards. Trigger with "interview plan for", "interview questions for", "how should we i... | `human-resources/skills/interview-prep/SKILL.md` |
| **`inventory-planner`** | > Works out what to reorder and when, from what is actually selling: pulls sales history and stock on hand from Shopify, Square, NetSuite, or an uploaded CSV, c... | `small-business/skills/inventory-planner/SKILL.md` |
| **`invoice-chase`** | > Drafts overdue-invoice reminder emails from the ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) plus PayPal, Stripe, and Airwallex data, matched to e... | `small-business/skills/invoice-chase/SKILL.md` |
| **`job-post-builder`** | > Builds end-to-end hiring packets — job post, structured interview guide with scoring rubric, and offer letter template — from a hiring brief. Triggers on: "he... | `small-business/skills/job-post-builder/SKILL.md` |
| **`journal-entry`** | Prepare journal entries with proper debits, credits, and supporting detail. Use when booking month-end accruals (AP, payroll, prepaid), recording depreciation o... | `finance/skills/journal-entry/SKILL.md` |
| **`journal-entry-prep`** | Prepare journal entries with proper debits, credits, and supporting documentation for month-end close. Use when booking accruals, prepaid amortization, fixed as... | `finance/skills/journal-entry-prep/SKILL.md` |
| **`kb-article`** | Draft a knowledge base article from a resolved issue or common question. Use when a ticket resolution is worth documenting for self-service, the same question k... | `customer-support/skills/kb-article/SKILL.md` |
| **`knowledge-synthesis`** | Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based on freshness and aut... | `enterprise-search/skills/knowledge-synthesis/SKILL.md` |
| **`lead-finder`** | > Builds a ranked list of prospects worth contacting. Works out the owner's ideal customer profile from the customers they already have, finds look-alike compan... | `small-business/skills/lead-finder/SKILL.md` |
| **`lead-triage`** | Score and route an inbound lead, or rank a backlog of leads, against your ICP and qualification framework, then recommend a priority and next action. Use when t... | `sales/skills/lead-triage/SKILL.md` |
| **`legal-response`** | Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply. U... | `legal/skills/legal-response/SKILL.md` |
| **`legal-risk-assessment`** | Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria. Use when evaluating contract risk, assessing deal exposure, c... | `legal/skills/legal-risk-assessment/SKILL.md` |
| **`log-activity`** | Log a call, meeting, or email exchange to the CRM after the fact as a completed activity on the right account, opportunity, and contact - drafted from your desc... | `sales/skills/log-activity/SKILL.md` |
| **`marketing-monday`** | Delivers the weekly growth briefing as one merged read — whether the growth engine is working, what customers are saying in public and private, what competitors... | `small-business/skills/marketing-monday/SKILL.md` |
| **`meeting-briefing`** | Prepare structured briefings for meetings with legal relevance and track resulting action items. Use when preparing for contract negotiations, board meetings, c... | `legal/skills/meeting-briefing/SKILL.md` |
| **`memory-management`** | Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames, and internal language so Claude understands requ... | `productivity/skills/memory-management/SKILL.md` |
| **`metrics-review`** | Review and analyze product metrics with trend analysis and actionable insights. Use when running a weekly, monthly, or quarterly metrics review, investigating a... | `product-management/skills/metrics-review/SKILL.md` |
| **`monday-brief`** | Runs the owner's Monday morning briefing as a two-link chain — business-pulse for the cross-connector snapshot of cash, sales, and pipeline, and report-builder ... | `small-business/skills/monday-brief/SKILL.md` |
| **`month-end-prep`** | > Reconciles the accounting ledger (MYOB, NetSuite, QuickBooks, Xero, or Zoho Books) against PayPal, Shopify, Square, and Stripe settlements, flags transactions... | `small-business/skills/month-end-prep/SKILL.md` |
| **`nextflow-development`** | Run nf-core bioinformatics pipelines (rnaseq, sarek, atacseq) on sequencing data. Use when analyzing RNA-seq, WGS/WES, or ATAC-seq data—either local FASTQs or p... | `bio-research/skills/nextflow-development/SKILL.md` |
| **`onboarding`** | Generate an onboarding checklist and first-week plan for a new hire. Use when someone has a start date coming up, building the pre-start task list (accounts, eq... | `human-resources/skills/onboarding/SKILL.md` |
| **`org-planning`** | Headcount planning, org design, and team structure optimization. Trigger with "org planning", "headcount plan", "team structure", "reorg", "who should we hire n... | `human-resources/skills/org-planning/SKILL.md` |
| **`outreach-composer`** | > Writes prospect outreach and follow-up sequences that sound like the owner wrote them, not like an AI did. Learns a voice profile from the owner's own sent ma... | `small-business/skills/outreach-composer/SKILL.md` |
| **`pay-the-bills`** | Works the bill pile from the AP inbox all the way to a staged payment run — reads and codes every bill, then checks the cash position before a dollar is committ... | `small-business/skills/pay-the-bills/SKILL.md` |
| **`payroll-prep`** | > Gets payroll ready to run without anyone getting shorted: pulls timesheets from Gusto, QuickBooks Payroll, or an uploaded spreadsheet, totals regular, overtim... | `small-business/skills/payroll-prep/SKILL.md` |
| **`people-report`** | Generate headcount, attrition, diversity, or org health reports. Use when pulling a headcount snapshot for leadership, analyzing turnover trends by team, prepar... | `human-resources/skills/people-report/SKILL.md` |
| **`performance-report`** | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. Use when wrapping a campai... | `marketing/skills/performance-report/SKILL.md` |
| **`performance-review`** | Structure a performance review with self-assessment, manager template, and calibration prep. Use when review season kicks off and you need a self-assessment tem... | `human-resources/skills/performance-review/SKILL.md` |
| **`pipeline-review`** | Stage-by-stage pipeline health check - coverage, aging, conversion, and at-risk deals - from CRM opportunity data. Use when the user asks "review my pipeline", ... | `sales/skills/pipeline-review/SKILL.md` |
| **`plan-payroll`** | Runs the payroll-confidence chain end to end — forecasts cash across the payroll window with cash-flow-snapshot, ranks and drafts overdue-invoice reminders with... | `small-business/skills/plan-payroll/SKILL.md` |
| **`plan-zoom-integration`** | Turn a Zoom integration idea into an implementation plan with architecture, auth, and delivery milestones. Use when you need a practical build plan, phased deli... | `partner-built/zoom-plugin/skills/plan-zoom-integration/SKILL.md` |
| **`plan-zoom-product`** | Choose the right Zoom building surface for a use case and explain the tradeoffs clearly. Use when deciding between REST API, Webhooks, WebSockets, Meeting SDK, ... | `partner-built/zoom-plugin/skills/plan-zoom-product/SKILL.md` |
| **`policy-lookup`** | Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expenses work", o... | `human-resources/skills/policy-lookup/SKILL.md` |
| **`probe-sdk`** | "Reference skill for Zoom Probe SDK. Use after routing to a preflight workflow when testing browser compatibility, media permissions, audio or video diagnostics... | `partner-built/zoom-plugin/skills/probe-sdk/SKILL.md` |
| **`process-doc`** | Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what,... | `operations/skills/process-doc/SKILL.md` |
| **`process-optimization`** | Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", o... | `operations/skills/process-optimization/SKILL.md` |
| **`product-brainstorming`** | Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner. Use when exploring a new opportunity, generating solutions to... | `product-management/skills/product-brainstorming/SKILL.md` |
| **`proposal-builder`** | > Turns whatever came out of a discovery conversation — a call transcript, a voice memo, jobsite photos, an RFP document, a set of drawings, or scrappy notes — ... | `small-business/skills/proposal-builder/SKILL.md` |
| **`prospect`** | "Full ICP-to-leads pipeline. Describe your ideal customer in plain English and get a ranked table of enriched decision-maker leads with emails and phone numbers... | `partner-built/apollo/skills/prospect/SKILL.md` |
| **`reactivate`** | Wins back customers who have quietly stopped buying — finds the ones whose gap has stretched past their own normal rhythm or who are showing churn signals, rank... | `small-business/skills/reactivate/SKILL.md` |
| **`reconciliation`** | Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data. Use when performing bank reconciliations, GL-to-subledger recs,... | `finance/skills/reconciliation/SKILL.md` |
| **`recruiting-pipeline`** | Track and manage recruiting pipeline stages. Trigger with "recruiting update", "candidate pipeline", "how many candidates", "hiring status", or when the user di... | `human-resources/skills/recruiting-pipeline/SKILL.md` |
| **`renewal-radar`** | Upcoming renewals with timing, risk, and uplift potential - and the renewal opportunity records to keep them honest. Use when the user asks "what renewals are c... | `sales/skills/renewal-radar/SKILL.md` |
| **`rep-context`** | Leader's prep on a single rep before a 1:1 - their pipeline, recent activity, what they've been working on per chat and calendar, and where they might need help... | `sales/skills/rep-context/SKILL.md` |
| **`report-builder`** | > Turns a plain-English description of a recurring report into a real, repeatable report — defines the metrics, pulls them from whatever data sources are connec... | `small-business/skills/report-builder/SKILL.md` |
| **`report-pack`** | Delivers the owner's custom recurring report pack on a set cadence — runs the saved report definition from report-builder, wraps it in a business-pulse snapshot... | `small-business/skills/report-pack/SKILL.md` |
| **`research-synthesis`** | Synthesize user research into themes, insights, and recommendations. Use when you have interview transcripts, survey results, usability test notes, support tick... | `design/skills/research-synthesis/SKILL.md` |
| **`restock`** | Turns what is actually selling into a reorder decision and gets it all the way into the books — computes sales velocity and conservative stockout dates per item... | `small-business/skills/restock/SKILL.md` |
| **`review-contract`** | Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provide business impact analysis. Use when reviewing ve... | `legal/skills/review-contract/SKILL.md` |
| **`review-reputation`** | > Watches what customers are saying in public and in private, then does something about it. Aggregates Google, Yelp, and Facebook reviews alongside disputes, ti... | `small-business/skills/review-reputation/SKILL.md` |
| **`risk-assessment`** | Identify, assess, and mitigate operational risks. Trigger with "what are the risks", "risk assessment", "risk register", "what could go wrong", or when the user... | `operations/skills/risk-assessment/SKILL.md` |
| **`rivet-sdk`** | "Reference skill for Zoom Rivet SDK. Use after routing to a Rivet-based server workflow when implementing auth handling, webhook consumers, API wrappers, multi-... | `partner-built/zoom-plugin/skills/rivet-sdk/SKILL.md` |
| **`roadmap-update`** | Update, create, or reprioritize your product roadmap. Use when adding a new initiative and deciding what moves to make room, shifting priorities after new infor... | `product-management/skills/roadmap-update/SKILL.md` |
| **`route-lead`** | Decide who owns an unrouted lead or opportunity and manage the handoff - deterministic routing by the org's own rules, a routing card the human router accepts o... | `sales/skills/route-lead/SKILL.md` |
| **`runbook`** | Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning trib... | `operations/skills/runbook/SKILL.md` |
| **`schedule-meeting`** | Find a time, draft the invite, and book the meeting on Google Calendar or Outlook - then log it to the CRM as an event on the right account and opportunity. Use... | `sales/skills/schedule-meeting/SKILL.md` |
| **`scientific-problem-selection`** | This skill should be used when scientists need help with research problem selection, project ideation, troubleshooting stuck projects, or strategic scientific d... | `bio-research/skills/scientific-problem-selection/SKILL.md` |
| **`scribe`** | "Reference skill for Zoom AI Services Scribe. Use after routing to a transcription workflow when handling uploaded or stored media, Build-platform JWT auth, fas... | `partner-built/zoom-plugin/skills/scribe/SKILL.md` |
| **`scvi-tools`** | Deep learning for single-cell analysis using scvi-tools. This skill should be used when users need (1) data integration and batch correction with scVI/scANVI, (... | `bio-research/skills/scvi-tools/SKILL.md` |
| **`search`** | Search across all connected sources in one query. Trigger with "find that doc about...", "what did we decide on...", "where was the conversation about...", or w... | `enterprise-search/skills/search/SKILL.md` |
| **`search-strategy`** | Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates queries into source-s... | `enterprise-search/skills/search-strategy/SKILL.md` |
| **`seo-ai-visibility`** | > Audits and fixes both halves of being found — classic search and AI answers. Search side: rankings, site structure, page speed, titles and descriptions, and c... | `small-business/skills/seo-ai-visibility/SKILL.md` |
| **`seo-audit`** | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. Use when assessing a site's SEO h... | `marketing/skills/seo-audit/SKILL.md` |
| **`sequence-load`** | "Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and enrollment in one flow.... | `partner-built/apollo/skills/sequence-load/SKILL.md` |
| **`setup`** | First-run setup - checks which tools are connected, shows what's connected and what each one unlocks, learns how you write from your sent email, and renders a s... | `sales/skills/setup/SKILL.md` |
| **`setup-zoom-mcp`** | Decide when Zoom MCP is the right fit and produce a safe setup plan for Claude. Use when planning AI workflows over Zoom data, deciding between MCP and REST, or... | `partner-built/zoom-plugin/skills/setup-zoom-mcp/SKILL.md` |
| **`setup-zoom-oauth`** | Implement Zoom authentication correctly. Use when setting up app credentials, choosing an OAuth grant, requesting scopes, handling token refresh, or debugging a... | `partner-built/zoom-plugin/skills/setup-zoom-oauth/SKILL.md` |
| **`setup-zoom-webhooks`** | Reference skill for Zoom webhooks. Use after routing to an event-driven workflow when implementing subscriptions, signature verification, delivery handling, ret... | `partner-built/zoom-plugin/skills/webhooks/SKILL.md` |
| **`setup-zoom-websockets`** | Reference skill for Zoom WebSockets. Use after routing to a low-latency event workflow when persistent connections, faster event delivery, or security constrain... | `partner-built/zoom-plugin/skills/websockets/SKILL.md` |
| **`signature-request`** | Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized ... | `legal/skills/signature-request/SKILL.md` |
| **`single-cell-rna-qc`** | Performs quality control on single-cell RNA-seq data (.h5ad or .h5 files) using scverse best practices with MAD-based filtering and comprehensive visualizations... | `bio-research/skills/single-cell-rna-qc/SKILL.md` |
| **`slack-messaging`** | Guidance for composing well-formatted, effective Slack messages using mrkdwn syntax | `partner-built/slack/skills/slack-messaging/SKILL.md` |
| **`slack-search`** | Guidance for effectively searching Slack to find messages, files, channels, and people | `partner-built/slack/skills/slack-search/SKILL.md` |
| **`smb-onboard`** | > Claude as the trainer. Walks an SMB owner through connecting their first two tools, runs one recipe to prove immediate value, interviews them about their busi... | `small-business/skills/smb-onboard/SKILL.md` |
| **`smb-router`** | > The front door to the Small Business plugin. Listens to what the owner needs right now — vague or specific — and routes them to the best skill or slash comman... | `small-business/skills/smb-router/SKILL.md` |
| **`social-content-engine`** | > Runs the owner's content operation as a standing thing rather than a one-off: keeps a rolling posting calendar, learns the owner's voice, generates on-brand C... | `small-business/skills/social-content-engine/SKILL.md` |
| **`source-management`** | Manages connected MCP sources for enterprise search. Detects available sources, guides users to connect new ones, handles source priority ordering, and manages ... | `enterprise-search/skills/source-management/SKILL.md` |
| **`sox-testing`** | Generate SOX sample selections, testing workpapers, and control assessments. Use when planning quarterly or annual SOX 404 testing, pulling a sample for a contr... | `finance/skills/sox-testing/SKILL.md` |
| **`speed-to-lead`** | > Makes sure no inbound lead goes unanswered. Watches web forms, the shared inbox, and the CRM for new inquiries, qualifies each one against the owner's criteri... | `small-business/skills/speed-to-lead/SKILL.md` |
| **`sprint-planning`** | Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan. Use when kicking off a new sprint, sizing a backlog against team availability... | `product-management/skills/sprint-planning/SKILL.md` |
| **`sql-queries`** | Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing... | `data/skills/sql-queries/SKILL.md` |
| **`stakeholder-map`** | Map the people in a deal or account - roles, influence, sentiment, who's missing, and your best access path to the people you haven't reached. Use when the user... | `sales/skills/stakeholder-map/SKILL.md` |
| **`stakeholder-update`** | Generate a stakeholder update tailored to audience and cadence. Use when writing a weekly or monthly status for leadership, announcing a launch, escalating a ri... | `product-management/skills/stakeholder-update/SKILL.md` |
| **`standup`** | Generate a standup update from recent activity. Use when preparing for daily standup, summarizing yesterday's commits and PRs and ticket moves, formatting work ... | `engineering/skills/standup/SKILL.md` |
| **`start`** | Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, bootstrapping working memory from your existing ta... | `productivity/skills/start/SKILL.md` |
| **`statistical-analysis`** | Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing. Use when analyzing distributions, testing for ... | `data/skills/statistical-analysis/SKILL.md` |
| **`status-report`** | Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/y... | `operations/skills/status-report/SKILL.md` |
| **`synthesize-research`** | Synthesize user research from interviews, surveys, and feedback into structured insights. Use when you have a pile of interview notes, survey responses, or supp... | `product-management/skills/synthesize-research/SKILL.md` |
| **`system-design`** | Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture ... | `engineering/skills/system-design/SKILL.md` |
| **`task-management`** | Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, wants to add/complete tasks, or needs help tracking co... | `productivity/skills/task-management/SKILL.md` |
| **`tax-prep`** | Prepares tax materials as a two-link chain — month-end-prep confirms the books are closed and reconciled first, then tax-season-organizer calculates the quarter... | `small-business/skills/tax-prep/SKILL.md` |
| **`tax-season-organizer`** | > Prepares tax-season materials for the owner's accountant, not tax advice. US federal tax; a non-US business gets its closed-books packet instead. Two modes: (... | `small-business/skills/tax-season-organizer/SKILL.md` |
| **`team-pipeline`** | Leader view - roll up a team's pipeline by rep and stage, flag at-risk deals, and surface coaching moments. Use when the user asks "show my team's pipeline", "t... | `sales/skills/team-pipeline/SKILL.md` |
| **`tech-debt`** | Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the use... | `engineering/skills/tech-debt/SKILL.md` |
| **`testing-strategy`** | Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when ... | `engineering/skills/testing-strategy/SKILL.md` |
| **`ticket-deflector`** | > Reads a forwarded customer email or ticket, pulls order and refund status from a payments connector (PayPal, Square, or Stripe) or Shopify, account history fr... | `small-business/skills/ticket-deflector/SKILL.md` |
| **`ticket-triage`** | Triage and prioritize a support ticket or customer issue. Use when a new ticket comes in and needs categorization, assigning P1-P4 priority, deciding which team... | `customer-support/skills/ticket-triage/SKILL.md` |
| **`triage-nda`** | Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review). Use when a new NDA arrives fro... | `legal/skills/triage-nda/SKILL.md` |
| **`update`** | Sync tasks and refresh memory from your current activity. Use when pulling new assignments from your project tracker into TASKS.md, triaging stale or overdue ta... | `productivity/skills/update/SKILL.md` |
| **`update-opportunity`** | Guided updates to an opportunity - push the stage, move the close date, set next steps, fix amount or forecast category. Shows the before/after, writes what you... | `sales/skills/update-opportunity/SKILL.md` |
| **`user-research`** | Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability test", "survey design", "research questions", or w... | `design/skills/user-research/SKILL.md` |
| **`ux-copy`** | Write or review UX copy — microcopy, error messages, empty states, CTAs. Trigger with "write copy for", "what should this button say?", "review this error messa... | `design/skills/ux-copy/SKILL.md` |
| **`validate-data`** | QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calcula... | `data/skills/validate-data/SKILL.md` |
| **`variance-analysis`** | Decompose financial variances into drivers with narrative explanations and waterfall analysis. Use when analyzing budget vs. actual, period-over-period changes,... | `finance/skills/variance-analysis/SKILL.md` |
| **`vendor-check`** | Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upcoming dead... | `legal/skills/vendor-check/SKILL.md` |
| **`vendor-review`** | Evaluate a vendor — cost analysis, risk assessment, and recommendation. Use when reviewing a new vendor proposal, deciding whether to renew or replace a contrac... | `operations/skills/vendor-review/SKILL.md` |
| **`view-pdf`** | Interactive PDF viewer. Use when the user wants to open, show, or view a PDF and collaborate on it visually — annotate, highlight, stamp, fill form fields, plac... | `pdf-viewer/skills/view-pdf/SKILL.md` |
| **`weekly-prep-brief`** | "Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I have t... | `partner-built/common-room/skills/weekly-prep-brief/SKILL.md` |
| **`weekly-wrap`** | End-of-week summary for a rep or leader - what closed, what moved, what slipped, and what's on deck Monday. Optionally drafts a chat post to the team channel. U... | `sales/skills/weekly-wrap/SKILL.md` |
| **`win-loss-review`** | Analyze recently closed opportunities to find patterns in what wins and what loses - stage of loss, common objections from transcripts, deal characteristics. Le... | `sales/skills/win-loss-review/SKILL.md` |
| **`write-query`** | Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and ... | `data/skills/write-query/SKILL.md` |
| **`write-spec`** | Write a feature spec or PRD from a problem statement or feature idea. Use when turning a vague idea or user request into a structured document, scoping a featur... | `product-management/skills/write-spec/SKILL.md` |
| **`zoom-apps-sdk`** | Reference skill for Zoom Apps SDK. Use after routing to an in-client app workflow when building web apps that run inside Zoom meetings, webinars, the main clien... | `partner-built/zoom-plugin/skills/zoom-apps-sdk/SKILL.md` |
| **`zoom-cobrowse-sdk`** | "Reference skill for Zoom Cobrowse SDK. Use after routing to a collaborative-support workflow when implementing browser co-browsing, annotation tools, privacy m... | `partner-built/zoom-plugin/skills/cobrowse-sdk/SKILL.md` |
| **`zoom-general`** | Cross-product Zoom reference skill. Use after the workflow is clear when you need shared platform guidance, app-model comparisons, authentication context, scope... | `partner-built/zoom-plugin/skills/general/SKILL.md` |
| **`zoom-mcp`** | Guidance for the bundled Zoom MCP connectors. Use after routing to an MCP workflow when planning or troubleshooting tool-based access to meetings, recordings, m... | `partner-built/zoom-plugin/skills/zoom-mcp/SKILL.md` |
| **`zoom-oauth`** | Reference skill for Zoom authentication. Use after routing to an auth workflow when choosing app credentials, grant types, scopes, token refresh behavior, or de... | `partner-built/zoom-plugin/skills/oauth/SKILL.md` |
| **`zoom-rtms`** | Reference skill for Zoom RTMS. Use after routing to a live-media workflow when processing real-time audio, video, chat, transcripts, screen share, or contact-ce... | `partner-built/zoom-plugin/skills/rtms/SKILL.md` |

</details>

<details>
<summary><b>🏛️ Core Engineering, Design Systems & Agent Infrastructure — <code>local-library</code> (162 skills)</b></summary>

> **Repository Source**: Local Antigravity Kit Core Store  
> **Description**: Foundational engineering skills including clean-code, system architecture, API design, testing patterns, and core development practices.  
> **Update Command**: `python library/activate_skill.py <skill-name>`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`3d-web-experience`** | "Expert in building 3D experiences for the web - Three.js, React Three Fiber, Spline, WebGL, and interactive 3D scenes. Covers product configurators, 3D portfol... | `SKILL.md` |
| **`antigravity-expert`** | Complete mastery of Google Antigravity platform architecture. Use when authoring or debugging Antigravity skills, hierarchical rules (GEMINI.md, AGENTS.md), sla... | `SKILL.md` |
| **`api-contract-testing`** | API contract testing, OpenAPI schema validation, and Consumer-Driven Contracts (Pact). Use when testing inter-service communication, preventing breaking API cha... | `SKILL.md` |
| **`api-patterns`** | API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination. | `SKILL.md` |
| **`app-builder`** | Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects tech stack, coordinates... | `SKILL.md` |
| **`architect-review`** | Master software architect specializing in modern architecture patterns, clean architecture, microservices, event-driven systems, and DDD. Reviews system designs... | `SKILL.md` |
| **`ask-matt`** | Ask which skill or flow fits your situation. A router over the skills in this repo. | `SKILL.md` |
| **`aspnet-core`** | Build, review, refactor, or architect ASP.NET Core web applications using current official guidance for .NET web development. Use when working on Blazor Web App... | `SKILL.md` |
| **`auto`** | Auto-generated project-specific knowledge repository containing learned conventions, project gotchas, bug fixes, and configuration patterns for the Managment wo... | `SKILL.md` |
| **`aws-cloud-patterns`** | AWS Cloud Architecture and serverless design patterns. Use when architecting AWS solutions, writing Lambda functions, configuring S3 buckets, designing DynamoDB... | `SKILL.md` |
| **`backtesting-frameworks`** | "Build robust backtesting systems for trading strategies with proper handling of look-ahead bias, survivorship bias, and transaction costs. Use when developing ... | `SKILL.md` |
| **`bash-linux`** | Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems. | `SKILL.md` |
| **`behavioral-modes`** | AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type. | `SKILL.md` |
| **`browser-extension-builder`** | "Expert in building browser extensions that solve real problems - Chrome, Firefox, and cross-browser extensions. Covers extension architecture, manifest v3, con... | `SKILL.md` |
| **`chatgpt-apps`** | Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, regist... | `SKILL.md` |
| **`chief-of-staff`** | Pursue a long-running goal in a single session by co-ordinating subagents. | `SKILL.md` |
| **`claude-d3js-skill`** | "Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geographic visualisation... | `SKILL.md` |
| **`claude-handoff`** | Hand the current conversation off to a fresh background agent that picks up the work immediately. | `SKILL.md` |
| **`clean-code`** | Pragmatic coding standards - concise, direct, no over-engineering, no unnecessary comments | `SKILL.md` |
| **`cli-creator`** | Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user ... | `SKILL.md` |
| **`cloudflare-deploy`** | Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or se... | `SKILL.md` |
| **`code-review-checklist`** | Code review guidelines covering code quality, security, and best practices. | `SKILL.md` |
| **`codebase-design`** | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportunities, decide where a se... | `SKILL.md` |
| **`database-design`** | Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases. | `SKILL.md` |
| **`database-query-optimizer`** | Advanced database query optimization, EXPLAIN ANALYZE interpretation, indexing strategies, and deadlock prevention. Use when debugging slow SQL queries, analyzi... | `SKILL.md` |
| **`defi-protocol-templates`** | "Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and lending systems. Use when building decentralized finance applicatio... | `SKILL.md` |
| **`define-goal`** | Help the user define a concrete, measurable goal before starting work, especially when they ask to use the goal tool, create a goal, set an objective, clarify s... | `SKILL.md` |
| **`dependency-management-deps-audit`** | "You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze project dependencies for kn... | `SKILL.md` |
| **`deployment-procedures`** | Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking, not scripts. | `SKILL.md` |
| **`diagnosing-bugs`** | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/throwing/failing/slow. | `SKILL.md` |
| **`docker-expert`** | Docker containerization and Compose architecture. Use when creating Dockerfiles, optimizing multi-stage builds, managing docker-compose stacks, configuring netw... | `SKILL.md` |
| **`documentation-templates`** | Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. | `SKILL.md` |
| **`domain-modeling`** | Build and sharpen a project's domain model. Use when discussing codebase terminology, writing or editing a GLOSSARY.md, or recording or editing an ADR. | `SKILL.md` |
| **`dr-bedrock`** | Troubleshoot local AWS Bedrock authentication and region configuration for the Cline CLI as Dr. Bedrock. Use when users report Bedrock CLI errors, AWS profile/d... | `SKILL.md` |
| **`dsql`** | "Build with Aurora DSQL — manage schemas, execute queries, handle migrations, diagnose query plans, load data, and develop applications with a serverless, distr... | `SKILL.md` |
| **`figma`** | Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to translate Figma nodes into production code. Trigger when... | `SKILL.md` |
| **`figma-code-connect-components`** | Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code connect", "connect this component to code", "map ... | `SKILL.md` |
| **`figma-create-design-system-rules`** | Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design r... | `SKILL.md` |
| **`figma-create-new-file`** | Create a new blank Figma file. Use when the user wants to create a new Figma design or FigJam file, or when you need a new file before calling use_figma. Handle... | `SKILL.md` |
| **`figma-generate-design`** | "Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Triggers: 'write to Figma'... | `SKILL.md` |
| **`figma-generate-library`** | "Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build component libraries, set... | `SKILL.md` |
| **`figma-implement-design`** | Translates Figma designs into production-ready application code with 1:1 visual fidelity. Use when implementing UI code from Figma files, when user mentions "im... | `SKILL.md` |
| **`figma-use`** | "**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without loading this skill first. S... | `SKILL.md` |
| **`firestore-data`** | Handles NoSQL document operations and collection hierarchy exploration. Use for CRUD tasks and data retrieval. Provides flexible document manipulation and struc... | `SKILL.md` |
| **`frontend-ui-dark-ts`** | "Build dark-themed React applications using Tailwind CSS with custom theming, glassmorphism effects, and Framer Motion animations. Use when creating dashboards,... | `SKILL.md` |
| **`game-audio`** | "Game audio principles. Sound design, music integration, adaptive audio systems." | `SKILL.md` |
| **`game-development`** | Game development orchestrator. Routes to platform-specific skills based on project needs. | `SKILL.md` |
| **`gcp-to-aws`** | "Migrate workloads from Google Cloud Platform to AWS — including AI and agentic workloads regardless of cloud provider. Triggers on: migrate from GCP, GCP to AW... | `SKILL.md` |
| **`geo-fundamentals`** | Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity). | `SKILL.md` |
| **`gh-address-comments`** | Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not lo... | `SKILL.md` |
| **`gh-fix-ci`** | "Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft... | `SKILL.md` |
| **`git-guardrails-claude-code`** | Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destru... | `SKILL.md` |
| **`git-workflow-pro`** | Advanced Git operations, conventional commits, interactive rebase, bisect, worktrees, and release branch management. Use when restructuring messy commit history... | `SKILL.md` |
| **`graphify`** | "any input (code, docs, papers, images) - knowledge graph - clustered communities - HTML + JSON + audit report" | `SKILL.md` |
| **`grill-me`** | A relentless interview to sharpen a plan or design. | `SKILL.md` |
| **`grill-with-docs`** | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. | `SKILL.md` |
| **`grilling`** | Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases. | `SKILL.md` |
| **`handoff`** | Compact the current conversation into a handoff document for another agent to pick up. | `SKILL.md` |
| **`hatch-pet`** | Create, repair, validate, visually QA, and package Codex-compatible animated pets and pet spritesheets from character art, generated images, company or prospect... | `SKILL.md` |
| **`i18n-localization`** | Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support. | `SKILL.md` |
| **`imagegen`** | "Generate or edit raster images when the task benefits from AI-created bitmap visuals such as photos, illustrations, textures, sprites, mockups, or transparent-... | `SKILL.md` |
| **`implement`** | "Implement a piece of work based on a spec or set of tickets." | `SKILL.md` |
| **`implement-spec`** | "Implement the result of /to-spec and /to-tickets in code." | `SKILL.md` |
| **`improve-codebase-architecture`** | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. | `SKILL.md` |
| **`incident-postmortem`** | Site Reliability Engineering (SRE) incident postmortem authoring, root-cause analysis (5 Whys), and timeline reconstruction. Use when documenting production out... | `SKILL.md` |
| **`intelligent-routing`** | Automatic agent selection and intelligent task routing. Analyzes user requests and automatically selects the best specialist agent(s) without requiring explicit... | `SKILL.md` |
| **`jupyter-notebook`** | "Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and ... | `SKILL.md` |
| **`kubernetes-operator`** | Kubernetes orchestration, Helm chart authoring, production manifest design, and cluster debugging. Use when writing k8s manifests, configuring Helm charts, trou... | `SKILL.md` |
| **`linear`** | Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear. | `SKILL.md` |
| **`linear-sdk-scripting`** | Perform actions in Linear (read, create, update, search issues, projects, comments, teams, cycles, labels, etc.) by writing and running small Node scripts again... | `SKILL.md` |
| **`lint-and-validate`** | "Automatic quality control, linting, and static analysis procedures. Use after every code modification to ensure syntax correctness and project standards. Trigg... | `SKILL.md` |
| **`loop-me`** | Grill me about specs for the workflows I want to build, within this workspace. | `SKILL.md` |
| **`microservices-resilience`** | Distributed systems resilience patterns, circuit breakers, bulkheads, rate limiting, and exponential backoff with jitter. Use when designing fault-tolerant micr... | `SKILL.md` |
| **`migrate-to-codex`** | Migrate supported instruction files, skills, agents, and MCP config into Codex project and global files. | `SKILL.md` |
| **`migrate-to-shoehorn`** | Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial te... | `SKILL.md` |
| **`mintlify`** | Comprehensive reference for building Mintlify documentation sites. Use when creating pages, configuring docs.json, adding components, setting up navigation, or ... | `SKILL.md` |
| **`mobile-design`** | Mobile-first design thinking and decision-making for iOS and Android apps. Touch interaction, performance patterns, platform conventions. Teaches principles, no... | `SKILL.md` |
| **`mutation-testing`** | Mutation testing methodologies and frameworks (Stryker, Mutmut). Use when evaluating test suite effectiveness, identifying false-positive tests, killing survivi... | `SKILL.md` |
| **`nestjs-expert`** | Enterprise NestJS backend architecture, dependency injection, modular systems, guards, interceptors, pipes, microservices, and testing. Use when building scalab... | `SKILL.md` |
| **`netlify-deploy`** | Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including... | `SKILL.md` |
| **`nextjs-react-expert`** | React and Next.js performance optimization from Vercel Engineering. Use when building React components, optimizing performance, eliminating waterfalls, reducing... | `SKILL.md` |
| **`nodejs-best-practices`** | Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, not copying. | `SKILL.md` |
| **`notion-knowledge-capture`** | Capture conversations and decisions into structured Notion pages; use when turning chats/notes into wiki entries, how-tos, decisions, or FAQs with proper linkin... | `SKILL.md` |
| **`notion-meeting-intelligence`** | Prepare meeting materials with Notion context and Codex research; use when gathering context, drafting agendas/pre-reads, and tailoring materials to attendees. | `SKILL.md` |
| **`notion-research-documentation`** | Research across Notion and synthesize into structured documentation; use when gathering info from multiple Notion sources to produce briefs, comparisons, or rep... | `SKILL.md` |
| **`notion-spec-to-implementation`** | Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature specs and creating Notion plans + tasks from them. | `SKILL.md` |
| **`openai-docs`** | "Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex surfaces, needs up-to-date official documentation w... | `SKILL.md` |
| **`oracledb`** | Use these skills to manage and monitor Oracle databases by executing SQL statements, exploring schema metadata, analyzing query performance, monitoring active s... | `SKILL.md` |
| **`parallel-agents`** | Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive analysis requires multiple... | `SKILL.md` |
| **`performance-profiling`** | Performance profiling principles. Measurement, analysis, and optimization techniques. | `SKILL.md` |
| **`plaid-fintech`** | "Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance checks, webhook handling,... | `SKILL.md` |
| **`plan-writing`** | Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or any multi-step work. | `SKILL.md` |
| **`playwright`** | "Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) v... | `SKILL.md` |
| **`playwright-interactive`** | "Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging." | `SKILL.md` |
| **`plugin-creator`** | Create and scaffold plugin directories for Codex with a required `.codex-plugin/plugin.json`, optional plugin folders/files, and baseline placeholders you can e... | `SKILL.md` |
| **`powershell-windows`** | PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling. | `SKILL.md` |
| **`pr-review-specialist`** | High-impact Pull Request (PR) reviews, automated diff analysis, severity calibration, and security flagging. Use when reviewing PRs, analyzing diffs, providing ... | `SKILL.md` |
| **`prisma-expert`** | Prisma ORM architecture, schema design, and query optimization. Use when designing Prisma data models, handling zero-downtime migrations, optimizing relation qu... | `SKILL.md` |
| **`production-code-audit`** | "Autonomously deep-scan entire codebase line-by-line, understand architecture and patterns, then systematically transform it to production-grade, corporate-leve... | `SKILL.md` |
| **`property-based-testing`** | Property-based and generative testing patterns (fast-check, Hypothesis). Use when testing complex business invariants, mathematical algorithms, data serializati... | `SKILL.md` |
| **`python-patterns`** | Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking, not copying. | `SKILL.md` |
| **`quant-analyst`** | "Build financial models, backtest trading strategies, and analyze" market data. Implements risk metrics, portfolio optimization, and statistical arbitrage. Use ... | `SKILL.md` |
| **`radix-ui-design-system`** | "Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component patterns for production-... | `SKILL.md` |
| **`react-flow-node-ts`** | "Create React Flow node components with TypeScript types, handles, and Zustand integration. Use when building custom nodes for React Flow canvas, creating visua... | `SKILL.md` |
| **`react-state-management`** | "Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing server state, or choosing ... | `SKILL.md` |
| **`red-team-tactics`** | Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting. | `SKILL.md` |
| **`remotion-best-practices`** | "Best practices for Remotion - Video creation in React" | `SKILL.md` |
| **`render-deploy`** | Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, h... | `SKILL.md` |
| **`research`** | Investigate a question against high-trust primary sources and capture the findings as a Markdown file in the repo. Use when the user wants a topic researched, d... | `SKILL.md` |
| **`retro`** | "Conduct a retrospective on a coding session." | `SKILL.md` |
| **`risk-metrics-calculation`** | "Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or b... | `SKILL.md` |
| **`rust-pro`** | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. Expert in the latest Rust ecosystem inclu... | `SKILL.md` |
| **`sap-fiori-add-visual-filter`** | Add visual filters (chart-based) to SAP Fiori Elements filter bar/value help using CAP or ABAP RAP. | `SKILL.md` |
| **`save-to-spotify`** | Create polished audio content and save to Spotify. Produces episodes with TTS narration, a rich timeline (chapters plus in-player images, external links, and Sp... | `SKILL.md` |
| **`scaffold-exercises`** | Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exe... | `SKILL.md` |
| **`screenshot`** | "Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture ca... | `SKILL.md` |
| **`scroll-experience`** | "Expert in building immersive scroll-driven experiences - parallax storytelling, scroll animations, interactive narratives, and cinematic web experiences. Like ... | `SKILL.md` |
| **`security-audit`** | Security guidance and vulnerability review for codebases, APIs, services, CLI tools, libraries, and daemons. Use for security questions, focused reviews, vulner... | `SKILL.md` |
| **`security-best-practices`** | "Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best p... | `SKILL.md` |
| **`security-hardened-api`** | OWASP API Security Top 10 hardening, rate limiting, JWT validation, and input sanitization. Use when securing API endpoints, implementing authentication/authori... | `SKILL.md` |
| **`security-ownership-map`** | "Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensitive-code ownership, and export CSV/JSON for grap... | `SKILL.md` |
| **`security-threat-model`** | "Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdow... | `SKILL.md` |
| **`sentry`** | "Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry CLI; perform rea... | `SKILL.md` |
| **`seo-fundamentals`** | SEO fundamentals, E-E-A-T, Core Web Vitals, and Google algorithm principles. | `SKILL.md` |
| **`server-management`** | Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. | `SKILL.md` |
| **`setup-matt-pocock-skills`** | "Configure this repo for the engineering skills: set up its issue tracker, triage label vocabulary, and domain doc layout. Run once before first use of the othe... | `SKILL.md` |
| **`setup-pre-commit`** | Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Hus... | `SKILL.md` |
| **`setup-ts-deep-modules`** | Wire dependency-cruiser into a TypeScript repo so each package is a deep module, with implementation hidden in subfolders and reachable only through its entry-p... | `SKILL.md` |
| **`skill-installer`** | Install Codex skills into $CODEX_HOME/skills from a curated list or a GitHub repo path. Use when a user asks to list installable skills, install a curated skill... | `SKILL.md` |
| **`solidity-security`** | "Master smart contract security best practices to prevent common vulnerabilities and implement secure Solidity patterns. Use when writing smart contracts, audit... | `SKILL.md` |
| **`spanner-data`** | Use these skills when you need to explore the database structure, discover schema objects like tables and graphs, and execute custom SQL queries to interact wit... | `SKILL.md` |
| **`speech`** | "Use when the user asks for text-to-speech narration or voiceover, accessibility reads, audio prompts, or batch speech generation via the OpenAI Audio API; run ... | `SKILL.md` |
| **`tailwind-patterns`** | Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture. | `SKILL.md` |
| **`tdd`** | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integration tests. | `SKILL.md` |
| **`tdd-workflow`** | Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle. | `SKILL.md` |
| **`teach`** | Teach the user a new skill or concept, within this workspace. | `SKILL.md` |
| **`teamcity-cli`** | Use when working with TeamCity CI/CD or when a user provides a TeamCity build URL — drives the `teamcity` CLI for builds, logs, jobs, queues, agents, pools, pro... | `SKILL.md` |
| **`terraform-architect`** | Terraform Infrastructure as Code (IaC) architecture, state management, module design, and security linting. Use when authoring Terraform configurations, managin... | `SKILL.md` |
| **`testing-patterns`** | Testing patterns and principles. Unit, integration, mocking strategies. | `SKILL.md` |
| **`threat-modeling-expert`** | "Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and security requirement extra... | `SKILL.md` |
| **`to-questionnaire`** | Turn a decision you can't fully answer into a questionnaire for someone else to fill in. | `SKILL.md` |
| **`to-spec`** | "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed." | `SKILL.md` |
| **`to-tickets`** | Break a plan, spec, or the current conversation into a set of tracer-bullet tickets, each declaring its blocking edges, published to the configured tracker (edg... | `SKILL.md` |
| **`transcribe`** | "Transcribe audio files to text with optional diarization and known-speaker hints. Use when a user asks to transcribe speech from audio/video, extract text from... | `SKILL.md` |
| **`triage`** | Move issues and external PRs through a state machine of triage roles, categorise, verify, grill if needed, and write agent-ready briefs. | `SKILL.md` |
| **`typescript-expert`** | Modern TypeScript 5+ type system architecture, strict mode standards, type-level programming, generics, and performance optimization. Use when authoring complex... | `SKILL.md` |
| **`ui-toolkit-web`** | "Reference skill for Zoom Video SDK UI Toolkit. Use after routing to a web video workflow when you want prebuilt React UI instead of building a fully custom Vid... | `SKILL.md` |
| **`ui5-typescript-conversion`** | A skill for converting UI5 (SAPUI5/OpenUI5) projects to TypeScript. | `SKILL.md` |
| **`use-railway`** | > Operate Railway infrastructure: sign up for or sign in to a Railway account, create projects, provision services and databases, manage object storage buckets,... | `SKILL.md` |
| **`vercel-deploy`** | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live",... | `SKILL.md` |
| **`vulnerability-scanner`** | Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization. | `SKILL.md` |
| **`wait-what`** | "Stop. That last message did not land: re-pitch it." | `SKILL.md` |
| **`wayfinder`** | Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on your issue tracker, and resolve them one at a time until... | `SKILL.md` |
| **`wcag-audit-patterns`** | "Conduct WCAG 2.2 accessibility audits with automated testing, manual verification, and remediation guidance. Use when auditing websites for accessibility, fixi... | `SKILL.md` |
| **`windsor-ai-business-data`** | Query Windsor.ai business data across marketing, sales, CRM, ecommerce, finance, and analytics connectors. Use when users need dashboards, reports, data visuali... | `SKILL.md` |
| **`winui-app`** | Bootstrap, develop, and design modern WinUI 3 desktop applications with C# and the Windows App SDK using official Microsoft guidance, WinUI Gallery patterns, Wi... | `SKILL.md` |
| **`wizard`** | Generate an interactive bash wizard that walks a human through steps only they can perform. Use when provisioning infrastructure, setting up credentials or CI s... | `SKILL.md` |
| **`writing-beats`** | Writing, exploit; assemble raw material into a journey of beats, grounding each term before a beat leans on it. | `SKILL.md` |
| **`writing-for-agents`** | Writing documents for agents. Use when creating or editing skills, or modifying AGENTS.md or CLAUDE.md. | `SKILL.md` |
| **`writing-fragments`** | "Writing, explore: mine raw fragments, no structure yet." | `SKILL.md` |
| **`writing-shape`** | "Writing, exploit: shape raw material into an article, paragraph by paragraph." | `SKILL.md` |
| **`yeet`** | "Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`)." | `SKILL.md` |

</details>

<details>
<summary><b>⚡ Multi-Agent Orchestration, Planning & Execution — <code>magentosh/superpowers</code> (86 skills)</b></summary>

> **Repository Source**: [https://github.com/magentosh/superpowers](https://github.com/magentosh/superpowers)  
> **Description**: Agent automation superpowers enabling multi-agent delegation, parallel worktrees, systematic debugging, test-driven development, and plan verification.  
> **Update Command**: `npx skills add magentosh/superpowers`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`affirmations`** | "Reset your own trajectory when you're stuck, looping, or demoralized — read these affirmations, then re-ground and take one clean step. Use when: you've tried ... | `guides/agent/affirmations/SKILL.md` |
| **`agent-browser`** | "Browser automation for AI agents via inference.sh. Navigate web pages, interact with elements using @e refs, take screenshots, record video. Capabilities: web ... | `tools/utilities/agent-browser/SKILL.md` |
| **`agent-tools`** | "Run AI apps via inference.sh CLI - image generation, video creation, LLMs, search, 3D, Twitter automation. Models: FLUX, Veo, Gemini, Grok, Claude, Seedance, O... | `tools/agent-tools/SKILL.md` |
| **`agent-ui`** | "Batteries-included agent component for React/Next.js from ui.inference.sh. One component with runtime, tools, streaming, approvals, and widgets built in. Capab... | `ui/agent-ui/SKILL.md` |
| **`ai-automation-workflows`** | "Build automated AI workflows combining multiple models and services. Patterns: batch processing, scheduled tasks, event-driven pipelines, agent loops. Tools: i... | `guides/content/ai-automation-workflows/SKILL.md` |
| **`ai-avatar-video`** | "Create AI avatar and talking head videos via inference.sh CLI. Recommended: P-Video-Avatar (fastest, cheapest, built-in TTS). Also: OmniHuman, Fabric, PixVerse... | `tools/video/ai-avatar-video/SKILL.md` |
| **`ai-content-pipeline`** | "Build multi-step AI content creation pipelines combining image, video, audio, and text. Workflow examples: generate image -> animate -> add voiceover -> merge ... | `guides/content/ai-content-pipeline/SKILL.md` |
| **`ai-image-generation`** | "Generate AI images with GPT-Image-2, FLUX, Gemini, Grok, Seedream, Reve and 50+ models via inference.sh CLI. Models: GPT-Image-2, FLUX Dev LoRA, FLUX.2 Klein L... | `tools/image/ai-image-generation/SKILL.md` |
| **`ai-marketing-videos`** | "Create AI marketing videos for ads, promos, product launches, and brand content. Models: Veo, Seedance, Wan, FLUX for visuals, Kokoro for voiceover. Types: pro... | `guides/video/ai-marketing-videos/SKILL.md` |
| **`ai-music-generation`** | "Generate AI music and songs with ElevenLabs, Diffrythm, Tencent Song Generation via inference.sh CLI. Models: ElevenLabs Music (up to 10 min, commercial licens... | `tools/audio/ai-music-generation/SKILL.md` |
| **`ai-podcast`** | "Generate multi-person talking head podcast videos from scratch using AI — character creation, TTS, avatar animation, and video stitching. Use when the user wan... | `guides/content/ai-podcast/SKILL.md` |
| **`ai-podcast-creation`** | "Create AI-powered podcasts with text-to-speech, music, and audio editing. Tools: Kokoro TTS, DIA TTS, Chatterbox, AI music generation, media merger. Capabiliti... | `guides/content/ai-podcast-creation/SKILL.md` |
| **`ai-product-photography`** | "Generate professional AI product photography and commercial images. Models: FLUX, Imagen 3, Grok, Seedream for product shots, lifestyle images, mockups. Capabi... | `guides/photo/ai-product-photography/SKILL.md` |
| **`ai-rag-pipeline`** | "Build RAG (Retrieval Augmented Generation) pipelines with web search and LLMs. Tools: Tavily Search, Exa Search, Exa Answer, Claude, GPT-4, Gemini via OpenRout... | `tools/llm/ai-rag-pipeline/SKILL.md` |
| **`ai-social-media-content`** | "Create AI-powered social media content for TikTok, Instagram, YouTube, Twitter/X. Generate: images, videos, reels, shorts, thumbnails, captions, hashtags. Tool... | `guides/social/ai-social-media-content/SKILL.md` |
| **`ai-video-generation`** | "Generate AI videos with Google Veo, Seedance 2.0, HappyHorse, Wan, Grok and 40+ models via inference.sh CLI. Models: Veo 3.1, Veo 3, Seedance 2.0, HappyHorse 1... | `tools/video/ai-video-generation/SKILL.md` |
| **`ai-voice-cloning`** | "AI voice generation, text-to-speech, and voice synthesis via inference.sh CLI. Models: Inworld TTS-2 (100+ languages, emotion/non-verbal steering), Inworld TTS... | `tools/audio/ai-voice-cloning/SKILL.md` |
| **`app-store-screenshots`** | "App Store and Google Play screenshot creation with exact platform specs. Covers iOS/Android dimensions, gallery ordering, device mockups, and preview videos. U... | `guides/design/app-store-screenshots/SKILL.md` |
| **`background-removal`** | "Remove backgrounds from images with BiRefNet via inference.sh CLI. Model: BiRefNet (high accuracy background removal). Use for: product photos, portraits, e-co... | `tools/image/background-removal/SKILL.md` |
| **`book-cover-design`** | "Book cover design with genre-specific conventions, typography rules, and AI image generation. Covers fiction and non-fiction genres, sizing, thumbnail testing,... | `guides/design/book-cover-design/SKILL.md` |
| **`building-inferencesh-apps`** | "Build and deploy applications on inference.sh. Use when getting started, understanding the platform, creating apps, configuring resources, or needing an overvi... | `sdk/building-apps/SKILL.md` |
| **`case-study-writing`** | "B2B case study writing with STAR framework, data visualization, and research. Covers structure, customer quotes, metrics presentation, and distribution formats... | `guides/writing/case-study-writing/SKILL.md` |
| **`character-design-sheet`** | "Character consistency across AI-generated images with reference sheets and LoRA techniques. Covers turnaround views, expression sheets, color palettes, and sty... | `guides/design/character-design-sheet/SKILL.md` |
| **`chat-ui`** | "Chat UI building blocks for React/Next.js from ui.inference.sh. Components: container, messages, input, typing indicators, avatars. Capabilities: chat interfac... | `ui/chat-ui/SKILL.md` |
| **`competitor-teardown`** | "Structured competitive analysis with feature matrices, SWOT, positioning maps, and UX review. Covers research frameworks, pricing comparison, review mining, an... | `guides/product/competitor-teardown/SKILL.md` |
| **`content-repurposing`** | "Content atomization — turn one piece of content into many formats. Covers blog-to-thread, blog-to-carousel, podcast-to-blog, video-to-quotes, and more. Use for... | `guides/content/content-repurposing/SKILL.md` |
| **`customer-persona`** | "Research-backed customer persona creation with market data and avatar generation. Covers demographics, psychographics, jobs-to-be-done, journey mapping, and an... | `guides/product/customer-persona/SKILL.md` |
| **`data-visualization`** | "Data visualization with chart selection, color theory, and annotation best practices. Covers chart types (bar, line, scatter, heatmap), axes rules, and storyte... | `guides/design/data-visualization/SKILL.md` |
| **`dialogue-audio`** | "Multi-speaker dialogue audio creation with ElevenLabs and Dia TTS. Covers speaker tags, emotion control, pacing, conversation flow, and post-production. Use fo... | `tools/audio/dialogue-audio/SKILL.md` |
| **`elevenlabs-dialogue`** | "ElevenLabs multi-speaker dialogue generation - create conversations with different voices in a single audio file via inference.sh CLI. Capabilities: multi-voic... | `tools/audio/elevenlabs-dialogue/SKILL.md` |
| **`elevenlabs-dubbing`** | "ElevenLabs automatic dubbing - translate and dub audio/video into 29 languages while preserving speaker voice via inference.sh CLI. Capabilities: auto speaker ... | `tools/audio/elevenlabs-dubbing/SKILL.md` |
| **`elevenlabs-music`** | "ElevenLabs AI music generation - create original music from text prompts via inference.sh CLI. Capabilities: text-to-music, custom duration up to 10 minutes, g... | `tools/audio/elevenlabs-music/SKILL.md` |
| **`elevenlabs-sound-effects`** | "Generate AI sound effects from text descriptions with ElevenLabs via inference.sh CLI. Capabilities: text-to-sound-effect, custom duration, royalty-free audio.... | `tools/audio/elevenlabs-sound-effects/SKILL.md` |
| **`elevenlabs-stt`** | "ElevenLabs speech-to-text with Scribe models and forced alignment via inference.sh CLI. Models: Scribe v1/v2 (98%+ accuracy, 90+ languages). Capabilities: tran... | `tools/audio/elevenlabs-stt/SKILL.md` |
| **`elevenlabs-tts`** | "ElevenLabs text-to-speech with 22+ premium voices, multilingual support, and voice tuning via inference.sh CLI. Models: eleven_multilingual_v2 (highest quality... | `tools/audio/elevenlabs-tts/SKILL.md` |
| **`elevenlabs-voice-changer`** | "ElevenLabs voice changer - transform any voice to a different voice while preserving speech content and emotion via inference.sh CLI. Models: eleven_multilingu... | `tools/audio/elevenlabs-voice-changer/SKILL.md` |
| **`elevenlabs-voice-isolator`** | "ElevenLabs voice isolator - remove background noise and isolate vocals from audio via inference.sh CLI. Capabilities: noise removal, voice extraction, audio cl... | `tools/audio/elevenlabs-voice-isolator/SKILL.md` |
| **`email-design`** | "Email marketing design with layout patterns, subject line formulas, and deliverability rules. Covers welcome sequences, promotional emails, transactional templ... | `guides/design/email-design/SKILL.md` |
| **`explainer-video-guide`** | "Explainer video production guide: scripting, voiceover, visuals, and assembly. Covers script formulas, pacing rules, scene planning, and multi-tool pipelines. ... | `guides/video/explainer-video-guide/SKILL.md` |
| **`flux-image`** | "Generate images with FLUX models (Black Forest Labs) via inference.sh CLI. Models: FLUX Dev LoRA, FLUX.2 Klein LoRA with custom style adaptation. Capabilities:... | `tools/image/flux-image/SKILL.md` |
| **`google-veo`** | "Generate videos with Google Veo models via inference.sh CLI. Models: Veo 3.1, Veo 3.1 Fast, Veo 3, Veo 3 Fast, Veo 2. Capabilities: text-to-video, cinematic ou... | `tools/video/google-veo/SKILL.md` |
| **`gpt-image`** | "Generate and edit images with OpenAI GPT-Image-2 via inference.sh CLI. Models: GPT-Image-2. Capabilities: text-to-image, image editing, inpainting, mask-based ... | `tools/image/gpt-image/SKILL.md` |
| **`happyhorse`** | "Generate and edit videos with Alibaba HappyHorse 1.0 models via inference.sh CLI. Models: HappyHorse T2V, I2V, R2V, Video Edit. Capabilities: text-to-video, im... | `tools/video/happyhorse/SKILL.md` |
| **`image-to-video`** | "Still-to-video conversion guide: model selection, motion prompting, and camera movement. Covers Wan 2.5 i2v, Seedance, Fabric, Grok Video with when to use each... | `tools/video/image-to-video/SKILL.md` |
| **`image-upscaling`** | "Upscale and enhance images with Real-ESRGAN, Thera, Topaz, FLUX Upscaler via inference.sh CLI. Models: Real-ESRGAN, Thera (any size), FLUX Dev Upscaler, Topaz ... | `tools/image/image-upscaling/SKILL.md` |
| **`infsh-cli`** | "Run AI apps via inference.sh CLI - image generation, video creation, LLMs, search, 3D, Twitter automation. Models: FLUX, Veo, Gemini, Grok, Claude, Seedance, O... | `tools/infsh-cli/SKILL.md` |
| **`javascript-sdk`** | "JavaScript/TypeScript SDK for inference.sh - run AI apps, build agents, integrate with all models. Package: @inferencesh/sdk (npm install). Full TypeScript sup... | `sdk/javascript-sdk/SKILL.md` |
| **`landing-page-design`** | "Landing page conversion optimization with layout rules, hero section design, and CTA psychology. Covers above-the-fold formula, social proof placement, mobile ... | `guides/design/landing-page-design/SKILL.md` |
| **`linkedin-content`** | "LinkedIn post writing with hook formulas, formatting rules, and engagement patterns. Covers post types, algorithm signals, character limits, and content pillar... | `guides/social/linkedin-content/SKILL.md` |
| **`llm-models`** | "Access Claude, Gemini, Kimi, GLM and 100+ LLMs via inference.sh CLI using OpenRouter. Models: Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, Gemini 3 Pr... | `tools/llm/llm-models/SKILL.md` |
| **`logo-design-guide`** | "Logo design principles and AI image generation best practices for creating logos. Covers logo types, prompting techniques, scalability rules, and iteration wor... | `guides/design/logo-design-guide/SKILL.md` |
| **`nano-banana`** | "Generate images with Google Gemini native image models via inference.sh CLI. Models: Gemini 3 Pro Image, Gemini 2.5 Flash Image. Capabilities: text-to-image, i... | `tools/image/nano-banana/SKILL.md` |
| **`nano-banana-2`** | "Generate images with Google Gemini 3.1 Flash Image Preview (Nano Banana 2) via inference.sh CLI. Capabilities: text-to-image, image editing, multi-image input ... | `tools/image/nano-banana-2/SKILL.md` |
| **`newsletter-curation`** | "Newsletter curation with content sourcing, editorial structure, and subscriber growth strategies. Covers issue formatting, link roundups, commentary style, and... | `guides/writing/newsletter-curation/SKILL.md` |
| **`og-image-design`** | "Open Graph and social sharing image design with platform specs, text placement, and branding. Covers OG meta tags, Twitter cards, LinkedIn previews, and dynami... | `guides/design/og-image-design/SKILL.md` |
| **`p-image`** | "Generate images with Pruna P-Image models via inference.sh CLI. Models: P-Image, P-Image-LoRA, P-Image-Edit, P-Image-Edit-LoRA. Capabilities: text-to-image, im... | `tools/image/p-image/SKILL.md` |
| **`p-video`** | "Generate videos with Pruna P-Video and WAN models via inference.sh CLI. Models: P-Video, WAN-T2V, WAN-I2V. Capabilities: text-to-video, image-to-video, audio s... | `tools/video/p-video/SKILL.md` |
| **`p-video-avatar`** | "Generate talking head avatar videos with Pruna P-Video-Avatar via inference.sh CLI. Turn a portrait image into a realistic speaking video with built-in TTS. 18... | `tools/video/p-video-avatar/SKILL.md` |
| **`pitch-deck-visuals`** | "Investor pitch deck structure with slide-by-slide framework, visual design rules, and data presentation. Covers the 12-slide framework, chart types, team slide... | `guides/design/pitch-deck-visuals/SKILL.md` |
| **`press-release-writing`** | "Press release writing in AP style with inverted pyramid structure. Covers formatting, datelines, quotes, boilerplates, and fact-checking. Use for: product laun... | `guides/writing/press-release-writing/SKILL.md` |
| **`product-changelog`** | "Product changelog and release notes that users actually read. Covers categorization, user-facing language, visuals, and distribution. Use for: release notes, c... | `guides/product/product-changelog/SKILL.md` |
| **`product-hunt-launch`** | "Product Hunt launch optimization with specific specs, timing, and gallery strategy. Covers taglines, gallery images, maker comments, and launch day tactics. Us... | `guides/product/product-hunt-launch/SKILL.md` |
| **`product-photography`** | "AI product photography with studio lighting, lifestyle shots, and packshot conventions. Covers angles, backgrounds, shadow types, hero shots, and e-commerce im... | `guides/photo/product-photography/SKILL.md` |
| **`prompt-engineering`** | "Master prompt engineering for AI models: LLMs, image generators, video models. Techniques: chain-of-thought, few-shot, system prompts, negative prompts. Models... | `guides/prompting/prompt-engineering/SKILL.md` |
| **`python-executor`** | "Execute Python code in a safe sandboxed environment via [inference.sh](https://inference.sh). Pre-installed: NumPy, Pandas, Matplotlib, requests, BeautifulSoup... | `tools/utilities/python-executor/SKILL.md` |
| **`python-sdk`** | "Python SDK for inference.sh - run AI apps, build agents, and integrate with all models. Package: inferencesh (pip install inferencesh). Supports sync/async, st... | `sdk/python-sdk/SKILL.md` |
| **`qwen-image-2`** | "Generate and edit images with Alibaba Qwen-Image-2.0 models via inference.sh CLI. Models: Qwen-Image-2.0 (fast), Qwen-Image-2.0-Pro (professional text renderin... | `tools/image/qwen-image-2/SKILL.md` |
| **`qwen-image-2-pro`** | "Generate images with Alibaba Qwen-Image-2.0-Pro via inference.sh CLI. Professional text rendering, fine-grained realism, enhanced semantic adherence. Ideal for... | `tools/image/qwen-image-2-pro/SKILL.md` |
| **`related-skill`** | "Discover and install related skills from inference.sh skill registry. Helps find complementary skills for your AI workflow. Use for: skill discovery, workflow ... | `tools/utilities/related-skill/SKILL.md` |
| **`remotion-render`** | "Render videos from React/Remotion component code via inference.sh. Pass TSX code, get MP4. Supports all Remotion APIs: useCurrentFrame, useVideoConfig, spring,... | `tools/video/remotion-render/SKILL.md` |
| **`seedance`** | "Generate videos with ByteDance Seedance 2.0 via inference.sh CLI. Unified model for text-to-video, image-to-video, and reference-to-video with synchronized aud... | `tools/video/seedance/SKILL.md` |
| **`seo-content-brief`** | "SEO content brief creation with keyword research, search intent analysis, and content structure. Covers SERP analysis, heading hierarchy, word count targets, a... | `guides/writing/seo-content-brief/SKILL.md` |
| **`social-media-carousel`** | "Multi-slide carousel design for Instagram, LinkedIn, and Twitter/X with layout rules and hooks. Covers slide structure, text hierarchy, swipe psychology, and p... | `guides/social/social-media-carousel/SKILL.md` |
| **`speech-to-text`** | "Transcribe audio to text with ElevenLabs Scribe and Whisper models via inference.sh CLI. Models: ElevenLabs Scribe v2 (98%+ accuracy, diarization), Fast Whispe... | `tools/audio/speech-to-text/SKILL.md` |
| **`storyboard-creation`** | "Film and video storyboarding with shot vocabulary, continuity rules, and panel layout. Covers shot types, camera angles, movement, 180-degree rule, and annotat... | `guides/video/storyboard-creation/SKILL.md` |
| **`talking-head-production`** | "Talking head video production with AI avatars, lipsync, and voiceover. Recommended: P-Video-Avatar (fastest, cheapest, built-in TTS). Also covers OmniHuman, Pi... | `guides/video/talking-head-production/SKILL.md` |
| **`technical-blog-writing`** | "Technical blog post writing with structure, code examples, and developer audience conventions. Covers post types, code formatting, explanation depth, and devel... | `guides/writing/technical-blog-writing/SKILL.md` |
| **`text-to-speech`** | "Convert text to natural speech with Inworld TTS, ElevenLabs, DIA TTS, Kokoro, Chatterbox, and more via inference.sh CLI. Models: Inworld TTS-2 (100+ languages,... | `tools/audio/text-to-speech/SKILL.md` |
| **`tools-ui`** | "Tool lifecycle UI components for React/Next.js from ui.inference.sh. Display tool calls: pending, progress, approval required, results. Capabilities: tool stat... | `ui/tools-ui/SKILL.md` |
| **`twitter-automation`** | "Automate Twitter/X with posting, engagement, and user management via inference.sh CLI. Apps: x/post-tweet, x/post-create (with media), x/post-like, x/post-retw... | `tools/social/twitter-automation/SKILL.md` |
| **`twitter-thread-creation`** | "Twitter/X thread writing with hook tweets, thread structure, and engagement optimization. Covers tweet formatting, character limits, media attachments, and pos... | `guides/social/twitter-thread-creation/SKILL.md` |
| **`video-ad-specs`** | "Video ad creation with exact platform-specific specs for TikTok, Instagram, YouTube, Facebook, LinkedIn. Covers dimensions, duration limits, AIDA framework, an... | `guides/video/video-ad-specs/SKILL.md` |
| **`video-prompting-guide`** | "Best practices and techniques for writing effective AI video generation prompts. Covers: Veo, Seedance, Wan, Grok, Kling, Runway, Pika, Sora prompting strategi... | `guides/prompting/video-prompting-guide/SKILL.md` |
| **`web-search`** | "Web search and content extraction with Tavily and Exa via inference.sh CLI. Apps: Tavily Search, Tavily Extract, Exa Search, Exa Answer, Exa Extract. Capabilit... | `tools/llm/web-search/SKILL.md` |
| **`widgets-ui`** | "Declarative UI widgets from JSON for React/Next.js from ui.inference.sh. Render rich interactive UIs from structured agent responses. Capabilities: forms, butt... | `ui/widgets-ui/SKILL.md` |
| **`youtube-thumbnail-design`** | "YouTube thumbnail design with specific dimensions, contrast rules, and mobile preview optimization. Covers safe zones, text placement, face expression psycholo... | `guides/design/youtube-thumbnail-design/SKILL.md` |

</details>

<details>
<summary><b>🤖 Official Anthropic Skills Suite — <code>anthropics/skills</code> (20 skills)</b></summary>

> **Repository Source**: [https://github.com/anthropics/skills](https://github.com/anthropics/skills)  
> **Description**: Foundational Anthropic skills for creating new skills, inspecting web guidelines, and document automation (Word, PDF, Excel).  
> **Update Command**: `npx skills add anthropics/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`academy-guide`** | > Stop and check this skill before finishing any reply to a question about how to use Claude or a Claude product — it recommends matching courses, tutorials, an... | `skills/academy-guide/SKILL.md` |
| **`algorithmic-art`** | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generati... | `skills/algorithmic-art/SKILL.md` |
| **`brand-guidelines`** | Applies Anthropic's official brand colors and typography to any sort of artifact that may benefit from having Anthropic's look-and-feel. Use it when brand color... | `skills/brand-guidelines/SKILL.md` |
| **`canvas-design`** | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, d... | `skills/canvas-design/SKILL.md` |
| **`claude-api`** | - Reference for the Claude API / Anthropic SDK — model ids, pricing, params, streaming, tool use, MCP, agents, caching, token counting, model migration. TRIGGER... | `skills/claude-api/SKILL.md` |
| **`discernment-nudge`** | > After you give a substantive answer or draft that the user may act on — advice or recommendations, drafted artifacts such as goals, plans, pitches, proposals,... | `skills/discernment-nudge/SKILL.md` |
| **`doc-coauthoring`** | Guide users through a structured workflow for co-authoring documentation. Use when user wants to write documentation, proposals, technical specs, decision docs,... | `skills/doc-coauthoring/SKILL.md` |
| **`docx`** | "Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files) or Word templates (.dotx files). Triggers include: any... | `skills/docx/SKILL.md` |
| **`frontend-design`** | Design thinking and decision-making for web UI. Use when designing components, layouts, color schemes, typography, or creating aesthetic interfaces. Teaches pri... | `skills/frontend-design/SKILL.md` |
| **`internal-comms`** | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever ... | `skills/internal-comms/SKILL.md` |
| **`mcp-builder`** | Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when b... | `skills/mcp-builder/SKILL.md` |
| **`pdf`** | Use this skill whenever the user wants to do anything with PDF files. This includes reading or extracting text/tables from PDFs, combining or merging multiple P... | `skills/pdf/SKILL.md` |
| **`pptx`** | "Use this skill any time a .pptx or .potx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presenta... | `skills/pptx/SKILL.md` |
| **`skill-creator`** | Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an e... | `skills/skill-creator/SKILL.md` |
| **`slack-gif-creator`** | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request a... | `skills/slack-gif-creator/SKILL.md` |
| **`template-skill`** | Replace with description of the skill and when Claude should use it. | `template/SKILL.md` |
| **`theme-factory`** | Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fo... | `skills/theme-factory/SKILL.md` |
| **`web-artifacts-builder`** | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for... | `skills/web-artifacts-builder/SKILL.md` |
| **`webapp-testing`** | Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend functionality, debugging UI behavior, capturing br... | `skills/webapp-testing/SKILL.md` |
| **`xlsx`** | "Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user wants to: open, read, edit, or fix an existing .x... | `skills/xlsx/SKILL.md` |

</details>

<details>
<summary><b>🛠️ Tooling, Automation & Browser Execution — <code>cline/skills</code> (17 skills)</b></summary>

> **Repository Source**: [https://github.com/cline/skills](https://github.com/cline/skills)  
> **Description**: Developer terminal tools, browser automation, and integration adapters.  
> **Update Command**: `npx skills add cline/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`building-pydantic-ai-agents`** | Build AI agents with Pydantic AI — tools, capabilities (including on-demand loading), structured output, streaming, testing, and multi-agent patterns. Use when ... | `skills/building-pydantic-ai-agents/SKILL.md` |
| **`convex-design`** | "Design and build reactive, type-safe, production-grade backends on Convex. Covers schema, queries/mutations/actions, indexes, auth, file storage, scheduling, r... | `skills/convex-design/SKILL.md` |
| **`cosmosdb-best-practices`** | Azure Cosmos DB performance optimization and best practices guidelines for NoSQL, partitioning, queries, SDK usage, and vector search. Use when writing, reviewi... | `skills/cosmosdb-best-practices/SKILL.md` |
| **`data-analyst`** | Act as an interactive data analyst for ClickHouse-backed analytics. Use when the user asks questions about internal data, metrics, dashboards, telemetry, active... | `skills/data-analyst/SKILL.md` |
| **`dataproc-skills`** | Skills to interact with your Dataproc clusters and jobs. | `skills/dataproc-skills/SKILL.md` |
| **`desktop-commander-overview`** | Use for Desktop Commander MCP capabilities — persistent shells and REPLs, long-running processes, filesystem beyond the workspace, structured files (.xlsx, .doc... | `skills/desktop-commander-overview/SKILL.md` |
| **`endor-setup`** | "Use when user asks to setup endorctl, install endorctl, run endorctl scan, scan for vulnerabilities, run endor scan or run Endor Labs scan or when any endorctl... | `skills/endor-setup/SKILL.md` |
| **`exa-search`** | "Deep research powered by Exa. Use for lead generation, literature reviews, deep dives, competitive analysis, or any query where one search falls short, includi... | `skills/exa-search/SKILL.md` |
| **`knowledge-catalog-discovery`** | Use these skills when you need to discover and explore data assets in the Knowledge Catalog. It allows you to search for entries, lookup specific metadata, and ... | `skills/knowledge-catalog-discovery/SKILL.md` |
| **`math-olympiad`** | "Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked... | `skills/math-olympiad/SKILL.md` |
| **`playground`** | Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, an... | `skills/playground/SKILL.md` |
| **`review-team`** | Use when the user asks for a code review by a fleet of specialized reviewer agents, wants multiple independent reviewer perspectives, or asks to run reviewers i... | `skills/review-team/SKILL.md` |
| **`searching-sourcegraph`** | Use when the user needs to search or navigate code with Sourcegraph MCP tools. Provides disciplined search workflows for finding implementations, understanding ... | `skills/searching-sourcegraph/SKILL.md` |
| **`sentry-cli`** | Guide for using the Sentry CLI to interact with Sentry from the command line. Use when the user asks about viewing issues, events, projects, organizations, maki... | `skills/sentry-cli/SKILL.md` |
| **`session-report`** | Generate an explorable HTML report of Claude Code session usage (tokens, cache, subagents, skills, expensive prompts) from ~/.claude/projects transcripts. | `skills/session-report/SKILL.md` |
| **`site-specification`** | Extract comprehensive site specifications from simple descriptions. Use when analyzing a user's theme request to determine site type, audience, tone, layout req... | `skills/site-specification/SKILL.md` |
| **`vibe-prospecting`** | "Find company & contact data. Turn your agent into a prospecting platform. Get contact information, roles, tech stack, business events, website changes, intent ... | `skills/vibe-prospecting/SKILL.md` |

</details>

<details>
<summary><b>✨ UI Craft, Animations & Motion Engineering (Emil Kowalski) — <code>emilkowalski/skills</code> (15 skills)</b></summary>

> **Repository Source**: [https://github.com/emilkowalski/skills](https://github.com/emilkowalski/skills)  
> **Description**: World-class micro-interactions, animation craft, fluid physics, and design engineering principles encoded by Emil Kowalski.  
> **Update Command**: `npx skills add emilkowalski/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`animate`** | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, ... | `skills/animate/SKILL.md` |
| **`animate-expo`** | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs o... | `skills/animate-expo/SKILL.md` |
| **`animation-performance`** | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when ... | `skills/animation-performance/SKILL.md` |
| **`animation-vocabulary`** | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in... | `skills/animation-vocabulary/SKILL.md` |
| **`apple-design`** | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, dr... | `skills/apple-design/SKILL.md` |
| **`ask-sonner`** | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and pe... | `skills/ask-sonner/SKILL.md` |
| **`break-ui`** | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, long label... | `skills/break-ui/SKILL.md` |
| **`emil-design-eng`** | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | `skills/emil-design-eng/SKILL.md` |
| **`find-animation-opportunities`** | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does... | `skills/find-animation-opportunities/SKILL.md` |
| **`improve-animations`** | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other age... | `skills/improve-animations/SKILL.md` |
| **`mobile-native`** | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. Covers stic... | `skills/mobile-native/SKILL.md` |
| **`pick-ui-library`** | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, t... | `skills/pick-ui-library/SKILL.md` |
| **`prototype`** | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one th... | `skills/prototype/SKILL.md` |
| **`review-animations`** | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. | `skills/review-animations/SKILL.md` |
| **`write-swift`** | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, t... | `skills/write-swift/SKILL.md` |

</details>

<details>
<summary><b>🔮 Developer Superpowers & Diagnostics — <code>obra/superpowers</code> (15 skills)</b></summary>

> **Repository Source**: [https://github.com/obra/superpowers](https://github.com/obra/superpowers)  
> **Description**: Supercharged diagnostics, code execution patterns, and developer productivity modules.  
> **Update Command**: `npx skills add obra/superpowers`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`brainstorming`** | Socratic questioning protocol + user communication. MANDATORY for complex requests, new features, or unclear requirements. Includes progress reporting and error... | `skills/brainstorming/SKILL.md` |
| **`diagnosing-superpowers`** | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results, a skill that didn't f... | `skills/diagnosing-superpowers/SKILL.md` |
| **`dispatching-parallel-agents`** | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies | `skills/dispatching-parallel-agents/SKILL.md` |
| **`executing-plans`** | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution, or no subagent tool is... | `skills/executing-plans/SKILL.md` |
| **`finishing-a-development-branch`** | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work | `skills/finishing-a-development-branch/SKILL.md` |
| **`receiving-code-review`** | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionable - requires technical ... | `skills/receiving-code-review/SKILL.md` |
| **`requesting-code-review`** | Use when completing tasks, implementing major features, or before merging to verify work meets requirements | `skills/requesting-code-review/SKILL.md` |
| **`subagent-driven-development`** | Use when executing implementation plans with independent tasks in the current session | `skills/subagent-driven-development/SKILL.md` |
| **`systematic-debugging`** | 4-phase systematic debugging methodology with root cause analysis and evidence-based verification. Use when debugging complex issues. | `skills/systematic-debugging/SKILL.md` |
| **`test-driven-development`** | Use when implementing any feature or bugfix, before writing implementation code | `skills/test-driven-development/SKILL.md` |
| **`using-git-worktrees`** | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated workspace exists via n... | `skills/using-git-worktrees/SKILL.md` |
| **`using-superpowers`** | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions | `skills/using-superpowers/SKILL.md` |
| **`verification-before-completion`** | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output be... | `skills/verification-before-completion/SKILL.md` |
| **`writing-plans`** | Use when you have a spec or requirements for a multi-step task, before touching code | `skills/writing-plans/SKILL.md` |
| **`writing-skills`** | Use when creating new skills, editing existing skills, or verifying skills work before deployment | `skills/writing-skills/SKILL.md` |

</details>

<details>
<summary><b>▲ Vercel, Next.js & React 19 Best Practices — <code>vercel-labs/agent-skills</code> (9 skills)</b></summary>

> **Repository Source**: [https://github.com/vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)  
> **Description**: Vercel official React and Next.js design patterns, server actions, composition techniques, and transition primitives.  
> **Update Command**: `npx skills add vercel-labs/agent-skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`deploy-to-vercel`** | Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live",... | `skills/deploy-to-vercel/SKILL.md` |
| **`vercel-cli-with-tokens`** | Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g.... | `skills/vercel-cli-with-tokens/SKILL.md` |
| **`vercel-composition-patterns`** | React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reus... | `skills/composition-patterns/SKILL.md` |
| **`vercel-optimize`** | "Use for Vercel cost and performance optimization on deployed projects, especially Next.js, SvelteKit, Nuxt, and limited Astro apps. Collect Vercel metrics, usa... | `skills/vercel-optimize/SKILL.md` |
| **`vercel-react-best-practices`** | React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js c... | `skills/react-best-practices/SKILL.md` |
| **`vercel-react-native-skills`** | React Native and Expo best practices for building performant mobile apps. Use when building React Native components, optimizing list performance, implementing a... | `skills/react-native-skills/SKILL.md` |
| **`vercel-react-view-transitions`** | Guide for implementing smooth, native-feeling animations using React's View Transition API (`<ViewTransition>` component, `addTransitionType`, and CSS view tran... | `skills/react-view-transitions/SKILL.md` |
| **`web-design-guidelines`** | Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site ... | `skills/web-design-guidelines/SKILL.md` |
| **`writing-guidelines`** | Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style", "audit prose", "review docs voice and tone", or ... | `skills/writing-guidelines/SKILL.md` |

</details>

<details>
<summary><b>🎨 UI/UX Pro Max Design Intelligence — <code>nextlevelbuilder/ui-ux-pro-max-skill</code> (6 skills)</b></summary>

> **Repository Source**: [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)  
> **Description**: Design system reasoning, typography rules, color palettes, and stack-specific component guidelines.  
> **Update Command**: `npx skills add nextlevelbuilder/ui-ux-pro-max-skill`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`banner-design`** | "Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. A... | `.claude/skills/banner-design/SKILL.md` |
| **`brand`** | Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand co... | `.claude/skills/brand/SKILL.md` |
| **`design`** | "Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini, Atlas Cloud, or MuAPI AI), corporate identity progra... | `.claude/skills/design/SKILL.md` |
| **`slides`** | Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies. | `.claude/skills/slides/SKILL.md` |
| **`ui-styling`** | Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visu... | `.claude/skills/ui-styling/SKILL.md` |
| **`ui-ux-pro-max`** | "UI/UX design intelligence for web, mobile, and desktop. This skill should be used when designing, building, reviewing, or fixing interfaces, including pages, c... | `.claude/skills/ui-ux-pro-max/SKILL.md` |

</details>

<details>
<summary><b>🪙 Web3, EVM & DeFi Protocol Architecture — <code>kukapay/crypto-skills</code> (6 skills)</b></summary>

> **Repository Source**: [https://github.com/kukapay/crypto-skills](https://github.com/kukapay/crypto-skills)  
> **Description**: Solidity smart contract security, decentralized finance templates, staking pools, and tokenomics.  
> **Update Command**: `npx skills add kukapay/crypto-skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`evm-swiss-knife`** | Interact with EVM-compatible blockchains using Foundry's cast tool for querying balances, calling contracts, sending transactions, and blockchain exploration. U... | `skills/evm-swiss-knife/SKILL.md` |
| **`market-sentiment`** | Aggregate news from popular cryptocurrency RSS feeds, analyze sentiment of articles, and calculate an overall market sentiment score with detailed explanation. ... | `skills/market-sentiment/SKILL.md` |
| **`meme-scout`** | Comprehensive tool for scouting trending meme coins on DEX platforms like DexScreener. Use for discovering trending tokens, analyzing price movements, volume da... | `skills/meme-scout/SKILL.md` |
| **`token-minter`** | Generate, build, and deploy custom ERC20 tokens on EVM networks. Use when users want to create and deploy their own ERC20 tokens with custom parameters like nam... | `skills/token-minter/SKILL.md` |
| **`trading-strategist`** | Provides trading strategies for cryptocurrencies based on Binance market data, calculated technical analysis indicators, and aggregated market sentiment from cr... | `skills/trading-strategist/SKILL.md` |
| **`yield-opportunities`** | Comprehensive tool for finding and analyzing DeFi yield opportunities across protocols, chains, and asset types. Use when users want to earn yield on crypto ass... | `skills/yield-opportunities/SKILL.md` |

</details>

<details>
<summary><b>📚 Academic Research, Paper Writing & Literature Screening — <code>imbad0202/academic-research-skills</code> (5 skills)</b></summary>

> **Repository Source**: [https://github.com/imbad0202/academic-research-skills](https://github.com/imbad0202/academic-research-skills)  
> **Description**: Deep literature discovery, systematic review screening, academic writing pipeline, and paper review workflows.  
> **Update Command**: `npx skills add imbad0202/academic-research-skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`academic-paper`** | "12-agent academic paper writing pipeline. 11 modes (full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/disclosure/rebu... | `academic-paper/SKILL.md` |
| **`academic-paper-reviewer`** | "Multi-perspective academic paper review with dynamic reviewer personas. Runs a 5-seat, role-separated review panel (Journal-Fit Reviewer + 3 peer-review roles ... | `academic-paper-reviewer/SKILL.md` |
| **`academic-pipeline`** | "Orchestrator for the full academic research pipeline: research -> write -> integrity check -> review -> revise -> re-review -> re-revise -> final integrity che... | `academic-pipeline/SKILL.md` |
| **`deep-research`** | "Universal deep research agent team. 13-agent pipeline for rigorous academic research on any topic. 8 modes: full research, quick brief, paper review, lit-revie... | `deep-research/SKILL.md` |
| **`sr-screener`** | "Protocol-driven study screening for systematic, scoping and rapid reviews. Turns a proposal or PROSPERO protocol into confirmed eligibility rules, then screens... | `sr-screener/SKILL.md` |

</details>

<details>
<summary><b>🛡️ Agent Teams & Session Guardrails — <code>wshobson/agents</code> (5 skills)</b></summary>

> **Repository Source**: [https://github.com/wshobson/agents](https://github.com/wshobson/agents)  
> **Description**: Parallel debugging protocols, technical debt detection, session guardrails, and task coordination.  
> **Update Command**: `npx skills add wshobson/agents`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`ai-debt-detector`** | Use after generating code, after accepting AI suggestions, or when reviewing AI-written modules. Also use when code works but feels brittle, when error handling... | `plugins/skill-forge-essentials/skills/ai-debt-detector/SKILL.md` |
| **`parallel-debugging`** | Debug complex issues using competing hypotheses with parallel investigation, evidence collection, and root cause arbitration. Use this skill when debugging bugs... | `plugins/agent-teams/skills/parallel-debugging/SKILL.md` |
| **`parallel-feature-development`** | Coordinate parallel feature development with file ownership strategies, conflict avoidance rules, and integration patterns for multi-agent implementation. Use t... | `plugins/agent-teams/skills/parallel-feature-development/SKILL.md` |
| **`session-guard`** | Use when working on complex multi-step tasks, when a session is getting long (40+ tool calls), when the agent starts ignoring rules it followed earlier, when co... | `plugins/skill-forge-essentials/skills/session-guard/SKILL.md` |
| **`task-coordination-strategies`** | Decompose complex tasks, design dependency graphs, and coordinate multi-agent work with proper task descriptions and workload balancing. Use this skill when bre... | `plugins/agent-teams/skills/task-coordination-strategies/SKILL.md` |

</details>

<details>
<summary><b>⚔️ Elite Adversarial & Telemetry Protocols — <code>Antigravity Kit (Local Workspace)</code> (4 skills)</b></summary>

> **Repository Source**: Local Built-in Elite Protocols  
> **Description**: Colosseum Battle Mode (/battle), Hardware Telemetry Benchmarks (/benchmark), Context Compaction (/compaction), and Decoupled Multi-Agent Learning (/owl).  
> **Update Command**: `Directly maintained in .agents/workflows and .agents/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`battle`** | Activates Antigravity's Colosseum Battle Mode. Pits two rival subagents in isolated branched workspaces against each other, stress-tests competing implementatio... | `.agents/skills/battle/SKILL.md` |
| **`benchmark`** | Replaces guesswork with empirical hardware telemetry: synthesizes ad-hoc stress-test harnesses on the fly, executes them headlessly, and proves performance gain... | `.agents/skills/benchmark/SKILL.md` |
| **`compaction`** | Triggers on-demand context compaction: persists critical state into durable artifacts, flushes obsolete transient turn history, and signals the runtime to compa... | `.agents/skills/compaction/SKILL.md` |
| **`owl`** | Activates the OWL (Optimized Workforce Learning) decoupled multi-agent pipeline: uses DeepInvestigator for root-cause analysis and edge-case attacks, and DeepCo... | `.agents/skills/owl/SKILL.md` |

</details>

<details>
<summary><b>☁️ Cloudflare Edge, Workers & D1 Architecture — <code>cloudflare/skills</code> (4 skills)</b></summary>

> **Repository Source**: [https://github.com/cloudflare/skills](https://github.com/cloudflare/skills)  
> **Description**: Production Cloudflare deployment, Workers best practices, Wrangler CLI integration, and Next.js on Cloudflare.  
> **Update Command**: `npx skills add cloudflare/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`cloudflare`** | Discover and choose Cloudflare products for apps, APIs, AI agents, storage, networking, and security. Use for architecture and product selection, including when... | `skills/cloudflare/SKILL.md` |
| **`nextjs-on-cloudflare`** | Build, migrate, and deploy Next.js apps on Cloudflare Workers with vinext. Use when starting a Next.js project on Cloudflare, moving an existing app to Workers,... | `skills/nextjs-on-cloudflare/SKILL.md` |
| **`workers-best-practices`** | Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers. | `skills/workers-best-practices/SKILL.md` |
| **`wrangler`** | Run or troubleshoot Wrangler CLI commands in projects that have a wrangler.jsonc, wrangler.json, or wrangler.toml file, including local development, Previews, d... | `skills/wrangler/SKILL.md` |

</details>

<details>
<summary><b>🔍 Engineering Craft & Observability (Addy Osmani) — <code>addyosmani/agent-skills</code> (4 skills)</b></summary>

> **Repository Source**: [https://github.com/addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)  
> **Description**: Doubt-driven development, git versioning discipline, incremental implementation, and observability patterns by Addy Osmani.  
> **Update Command**: `npx skills add addyosmani/agent-skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`doubt-driven-development`** | Subjects every non-trivial decision to a fresh-context adversarial review before it stands. Use when you want every assumption cross-examined before proceeding,... | `skills/doubt-driven-development/SKILL.md` |
| **`git-workflow-and-versioning`** | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, splitting uncommitted work in a messy w... | `skills/git-workflow-and-versioning/SKILL.md` |
| **`incremental-implementation`** | Delivers changes incrementally in thin, verifiable slices. Use when implementing any feature or change that touches more than one file, or when picking up the n... | `skills/incremental-implementation/SKILL.md` |
| **`observability-and-instrumentation`** | Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that r... | `skills/observability-and-instrumentation/SKILL.md` |

</details>

<details>
<summary><b>🎭 Real-Browser Automation & Headless Testing — <code>microsoft/playwright-cli</code> (2 skills)</b></summary>

> **Repository Source**: [https://github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)  
> **Description**: Headless and interactive browser automation, screenshots, visual assertions, and web crawling with Playwright.  
> **Update Command**: `npx skills add microsoft/playwright-cli`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`dev`** | Development workflows for the playwright-cli repository. Use when the user asks about rolling dependencies, releasing, or other repo maintenance tasks. | `.claude/skills/dev/SKILL.md` |
| **`playwright-cli`** | Automate browser interactions, test web pages and work with Playwright tests. | `skills/playwright-cli/SKILL.md` |

</details>

<details>
<summary><b>📱 iOS Design & Aesthetics Taste System — <code>uizze.sh</code> (2 skills)</b></summary>

> **Repository Source**: [https://uizze.sh/](https://uizze.sh/)  
> **Description**: Native iOS HIG design guidelines and curated visual frontend taste parameters.  
> **Update Command**: `npx skills add https://uizze.sh/`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`ios-design`** | Design and review iOS UI/UX for iPhone apps in SwiftUI, UIKit, or React Native. Use for mobile app design, screen redesigns, navigation flows, typography, forms... | `skills/ios-design/SKILL.md` |
| **`ui-taste`** | Give your coding agent better UI taste. Build and polish web and iOS interfaces with Uizze's anti-ui-slop playbooks and optional real-product references. Use fo... | `skills/ui-taste/SKILL.md` |

</details>

<details>
<summary><b>⚡ Supabase & Postgres Best Practices — <code>supabase/agent-skills</code> (2 skills)</b></summary>

> **Repository Source**: [https://github.com/supabase/agent-skills](https://github.com/supabase/agent-skills)  
> **Description**: Postgres schema design, RLS security policies, real-time database subscriptions, and indexing optimization.  
> **Update Command**: `npx skills add supabase/agent-skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`supabase`** | "Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client libr... | `skills/supabase/SKILL.md` |
| **`supabase-postgres-best-practices`** | "Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing or changing anything that lives in a Postgres dat... | `skills/supabase-postgres-best-practices/SKILL.md` |

</details>

<details>
<summary><b>🚀 21-Gate Adaptive Deploy & QA Review — <code>SeaXen/app-production-readiness</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/SeaXen/app-production-readiness](https://github.com/SeaXen/app-production-readiness)  
> **Description**: 21-gate production readiness and deployment review suite supporting any stack.  
> **Update Command**: `npx skills add SeaXen/app-production-readiness`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`app-production-readiness`** | Build portable apps (any stack - TypeScript, Python, Go, Rust) for localhost, Docker, Vercel, Netlify, Railway, Render, Fly.io, Cloudflare Free plan, then run a... | `SKILL.md` |

</details>

<details>
<summary><b>🔍 High-Density Compressed Code Review — <code>juliusbrussee/caveman</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/juliusbrussee/caveman](https://github.com/juliusbrussee/caveman)  
> **Description**: High-density, one-line-per-finding code review eliminating conversational fluff.  
> **Update Command**: `npx skills add https://github.com/juliusbrussee/caveman --skill caveman-review`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`caveman-review`** | > Compressed code review - one line per finding with location, problem and fix. Use for /caveman-review, "review this PR", or "review the diff". | `skills/caveman-review/SKILL.md` |

</details>

<details>
<summary><b>🤝 Web3 BD & Ecosystem Growth — <code>buzzbysolcex/buzz-bd-agent</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/buzzbysolcex/buzz-bd-agent](https://github.com/buzzbysolcex/buzz-bd-agent)  
> **Description**: Crypto business development and ecosystem expansion workflows.  
> **Update Command**: `npx skills add https://github.com/buzzbysolcex/buzz-bd-agent`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`crypto-bd-agent`** | ">" Autonomous crypto business development patterns — multi-chain token discovery, 100-point scoring with wallet forensics, x402 micropayments, ERC-8004 on-chai... | `SKILL.md` |

</details>

<details>
<summary><b>🍎 Apple HIG & Premium Ecosystem Design — <code>designed-by-ai/skills</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/designed-by-ai/skills](https://github.com/designed-by-ai/skills)  
> **Description**: Apple design guidelines, typography hierarchy, and fluid tactile UI components.  
> **Update Command**: `npx skills add designed-by-ai/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`design-mobile-apps`** | Design mobile app screens with Sleek, edit Sleek projects, and implement their designs in React Native or HTML. | `skills/design-mobile-apps/SKILL.md` |

</details>

<details>
<summary><b>👁️ Modern Frontend Visual Taste — <code>Leonxlnx/taste-skill</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)  
> **Description**: Curated aesthetic principles preventing generic MVP looks and enforcing high-end craft.  
> **Update Command**: `npx skills add Leonxlnx/taste-skill`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`design-taste-frontend`** | tasteskill v2, the anti-slop frontend skill. Art direction for websites, distilled from a study of 247 curated gallery sites (One Page Love, Awwwards Sites of t... | `skills/taste-skill/SKILL.md` |

</details>

<details>
<summary><b>🐛 Sentry Bug Finding & Vulnerability Audit — <code>getsentry/skills</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/getsentry/skills](https://github.com/getsentry/skills)  
> **Description**: Codebase vulnerability analysis, memory leak isolation, and regression auditing.  
> **Update Command**: `npx skills add getsentry/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`find-bugs`** | "Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, security review, or audit co... | `skills/find-bugs/SKILL.md` |

</details>

<details>
<summary><b>▲ Vercel One-Click Deploy Tooling — <code>vercel-labs/skills</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/vercel-labs/skills](https://github.com/vercel-labs/skills)  
> **Description**: Automated preview and production deployments to Vercel.  
> **Update Command**: `npx skills add vercel-labs/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`find-skills`** | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express int... | `skills/find-skills/SKILL.md` |

</details>

<details>
<summary><b>🧠 Cognitive Focus & High-Impact Work — <code>udaysharmadev/Gravitas</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/udaysharmadev/Gravitas](https://github.com/udaysharmadev/Gravitas)  
> **Description**: Deep work prioritization, cognitive load reduction, and mission-critical task execution.  
> **Update Command**: `npx skills add udaysharmadev/Gravitas`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`gravitas`** | > Use for software implementation, debugging, refactoring, review, migration, and other repository-changing engineering work where correctness must be verified.... | `skills/gravitas/SKILL.md` |

</details>

<details>
<summary><b>🎯 Impeccable Design Critique (Paul Bakaus) — <code>pbakaus/impeccable</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)  
> **Description**: Systematic UI audit, typography typesetting, spacing critique, and visual hierarchy validation.  
> **Update Command**: `npx skills add pbakaus/impeccable`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`impeccable`** | "Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend interface: websites, la... | `.agents/skills/impeccable/SKILL.md` |

</details>

<details>
<summary><b>🐘 Serverless Postgres Architecture (Neon) — <code>neondatabase/agent-skills</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/neondatabase/agent-skills](https://github.com/neondatabase/agent-skills)  
> **Description**: Serverless database branching, connection pooling, and autoscaling Postgres techniques.  
> **Update Command**: `npx skills add neondatabase/agent-skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`neon`** | Overview of Neon, a complete set of cloud backend primitives around Lakebase Postgres: Auth, Object Storage, Functions, the AI Gateway, and Realtime. Start here... | `skills/neon/SKILL.md` |

</details>

<details>
<summary><b>🔄 Backward Compatibility Alias — <code>SeaXen/app-production-readiness (Legacy alias)</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/SeaXen/app-production-readiness](https://github.com/SeaXen/app-production-readiness)  
> **Description**: Legacy alias for portable-deploy-qa forwarding to app-production-readiness.  
> **Update Command**: `npx skills add SeaXen/app-production-readiness`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`portable-deploy-qa`** | (Legacy alias for app-production-readiness) Build portable apps (any stack - TypeScript, Python, Go, Rust) for localhost, Docker, Vercel, Netlify, Railway, Rend... | `.agents/skills/portable-deploy-qa/SKILL.md` |

</details>

<details>
<summary><b>🐙 GitHub Pull Request Formatting — <code>humanlayer/skills</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/humanlayer/skills](https://github.com/humanlayer/skills)  
> **Description**: Automated PR description generation, diff summarization, and review checklists.  
> **Update Command**: `npx skills add humanlayer/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`pr`** | "Use when writing a PR body." | `skills/pr/SKILL.md` |

</details>

<details>
<summary><b>📸 Automated Marketing Screenshots — <code>Shpigford/skills</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/Shpigford/skills](https://github.com/Shpigford/skills)  
> **Description**: Automated high-resolution marketing screenshots for Product Hunt, docs, and social cards.  
> **Update Command**: `npx skills add Shpigford/skills`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`screenshots`** | "Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social media, landing pages, or do... | `skills/screenshots/SKILL.md` |

</details>

<details>
<summary><b>🧱 shadcn/ui Component Registry — <code>shadcn-ui/ui</code> (1 skills)</b></summary>

> **Repository Source**: [https://github.com/shadcn-ui/ui](https://github.com/shadcn-ui/ui)  
> **Description**: Accessible headless UI component scaffolding and theme integration with Radix and Tailwind.  
> **Update Command**: `npx skills add shadcn-ui/ui`

| Skill Name | Description | Upstream Path |
| :--- | :--- | :--- |
| **`shadcn`** | Manages shadcn components and projects — adding, searching, fixing, debugging, styling, and composing UI, including chat interfaces. Provides project context, c... | `skills/shadcn/SKILL.md` |

</details>

---

## 🤖 Specialist Agents (20 Personas)

Located in [`.agents/agents/`](./agents):

<details>
<summary><b>Click to expand all 20 Specialized Personas</b></summary>

| Agent Name | Primary Specialty | Key Trigger |
| :--- | :--- | :--- |
| **`orchestrator`** | Master Coordinator & Socratic Task Routing | Complex multi-domain tasks & architectural workflows |
| **`frontend-specialist`** | Web UI, React/Next.js & Design Systems | Web interface design, animations, component engineering |
| **`backend-specialist`** | API Architecture, Databases & Server Performance | REST/GraphQL/tRPC APIs, Postgres schema, microservices |
| **`mobile-developer`** | iOS, Android, React Native & Flutter | Mobile interfaces, touch ergonomics, offline storage |
| **`security-auditor`** | Vulnerability Analysis & Hardening | Security scanning, OWASP compliance, auth defense |
| **`project-planner`** | 4-Phase System Plan Formulation | Implementation plans, dependency mapping, risk matrices |
| **`debugger`** | Systematic Root-Cause Debugging | Reproductions, regression diagnosis, fix verification |
| **`game-developer`** | Game Mechanics, Physics & Shaders | 2D/3D games, canvas rendering, game loop tuning |
| **`system-architect`** | High-Level System Architecture | Trade-off evaluations, ADRs, distributed topologies |
| **`database-expert`** | SQL Query Optimization & Data Modeling | Drizzle, Prisma, Neon, Supabase, migration safety |
| **`devops-engineer`** | Cloudflare, Docker, CI/CD & Deployments | Cloudflare Workers, Wrangler, container deployments |
| **`code-reviewer`** | Clean Code & Pull Request Auditing | High-density diff reviews, style enforcement |
| **`performance-engineer`** | Web Vitals & Runtime Profiling | Bundle analysis, memory leaks, latency profiling |
| **`seo-specialist`** | SEO Architecture, Core Web Vitals & GEO | Semantic HTML, metadata, generative search visibility |
| **`test-engineer`** | Unit, Integration & Playwright E2E | Test pyramid, red-green-refactor, mutation testing |
| **`accessibility-specialist`** | WCAG 2.2 AA Compliance & Screen Readers | Focus traps, ARIA attributes, semantic markup |
| **`api-designer`** | Contract-First API Specifications | OpenAPI, tRPC routes, error schemas, rate limits |
| **`researcher`** | Literature Review & Academic Synthesis | Deep discovery, citation screening, methodology synthesis |
| **`technical-writer`** | Comprehensive Documentation & Guides | READMEs, developer portals, architecture manuals |
| **`brand-strategist`** | Brand Voice & Tone Alignment | Marketing copy, typography guidelines, identity design |

</details>

---

## ⚡ Autonomous Workflows (17 Commands)

Located in [`.agents/workflows/`](./workflows):

<details>
<summary><b>Click to expand all 17 Slash Workflows</b></summary>

| Command | Workflow File | Description |
| :--- | :--- | :--- |
| **`/battle`** | [`battle.md`](./workflows/battle.md) | Activates Colosseum Battle Mode: forks rival subagents, pits them against each other, and merges the winner. |
| **`/benchmark`** | [`benchmark.md`](./workflows/benchmark.md) | Synthesizes ad-hoc test harnesses headlessly and proves performance gains with real hardware telemetry. |
| **`/compaction`** | [`compaction.md`](./workflows/compaction.md) | Compresses active conversation context into persistent durable artifacts to prevent memory exhaustion. |
| **`/owl`** | [`owl.md`](./workflows/owl.md) | Decoupled multi-agent engineering pipeline: DeepInvestigator for root causes + DeepCoder for verified code. |
| **`/create`** | [`create.md`](./workflows/create.md) | Interactive application builder wizard: discovers requirements, selects tech stack, and scaffolds projects. |
| **`/debug`** | [`debug.md`](./workflows/debug.md) | 4-phase systematic debugging loop: reproduce, isolate, verify hypothesis, and confirm resolution. |
| **`/deploy`** | [`deploy.md`](./workflows/deploy.md) | Pre-flight security scans, environment variable validation, and deployment execution to Vercel/Cloudflare. |
| **`/enhance`** | [`enhance.md`](./workflows/enhance.md) | Iterative feature addition workflow preserving existing architecture and automated regression tests. |
| **`/impeccable`** | [`impeccable.md`](./workflows/impeccable.md) | Paul Bakaus Impeccable design workflow: critique typography, micro-spacing, contrast, and visual rhythm. |
| **`/library`** | [`library.md`](./workflows/library.md) | Search, inspect, and activate any of the 2,031 offline reserve skills into your active workspace hot set. |
| **`/orchestrate`**| [`orchestrate.md`](./workflows/orchestrate.md) | Multi-agent coordination pipeline assigning domain tasks to specialized subagents in parallel. |
| **`/plan`** | [`plan.md`](./workflows/plan.md) | 4-phase project planning generating actionable plan markdown documents before writing code. |
| **`/preview`** | [`preview.md`](./workflows/preview.md) | Local development preview server management, port discovery, and visual readiness validation. |
| **`/status`** | [`status.md`](./workflows/status.md) | Interactive project status board tracking tasks, active subagents, and delivery milestones. |
| **`/test`** | [`test.md`](./workflows/test.md) | Automated unit, integration, and Playwright browser test generation and execution. |
| **`/ui-ux-pro-max`**| [`ui-ux-pro-max.md`](./workflows/ui-ux-pro-max.md) | Comprehensive UI/UX design intelligence planning: typography, color schemes, and component stacks. |
| **`/brainstorm`** | [`brainstorm.md`](./workflows/brainstorm.md) | Socratic discovery dialogue to explore edge cases, user personas, and architectural alternatives. |

</details>

---


---

## 🏷️ Skill Domain Tags & Filter Tool

You can filter, search, and inspect the 594 skills by category tags using the built-in `--tag` CLI:

| Domain Tag | Skills Count | Description |
| :--- | :---: | :--- |
| **`frontend`** | 113 | React 19, Next.js, Tailwind v4, Shadcn, design tokens |
| **`testing-qa`** | 43 | Unit, integration, Playwright E2E, mutation testing, PR reviews |
| **`agent-orchestration`** | 45 | Subagent delegation, /battle, /owl, /compaction, multi-agent teams |
| **`sales-marketing`** | 33 | Content strategy, outreach composition, lead discovery, SEO |
| **`devops-cloud`** | 23 | Cloudflare Workers, Wrangler, Docker, Vercel, Terraform |
| **`research-academic`** | 21 | Deep research, academic literature screening, paper review |
| **`backend-api`** | 13 | Node, Express, NestJS, Python, Rust, OpenAPI, tRPC |
| **`security`** | 13 | OWASP hardening, red-team tactics, smart contract audits |
| **`animation-craft`** | 12 | Emil Kowalski animations, micro-interactions, Apple HIG |
| **`finance-crypto`** | 11 | DeFi templates, smart contract security, invoicing |
| **`database-sql`** | 9 | Postgres, Drizzle, Prisma, Neon, Supabase, query optimizer |
| **`mobile`** | 6 | iOS HIG, Android Jetpack, React Native, Flutter |

### CLI Search & Tag Commands:
```powershell
# Display vault about info & metadata:
python .agents/update.py --about

# List all available domain tags:
python .agents/update.py --tags

# Filter skills by tag:
python .agents/update.py --tag animation-craft
python .agents/update.py --tag cloudflare
python .agents/update.py --tag security
python .agents/update.py --tag database-sql
```

## 🏛️ Directory Architecture

```text
.agents/
├── skills/                     # 594 Modular skills (flat structure for 100% tool compatibility)
│   ├── clean-code/             # Pragmatic coding standards & clean code rules
│   ├── emil-design-eng/        # Emil Kowalski UI polish and animation craft
│   ├── vercel-react-best-practices/ # Vercel React & Next.js production patterns
│   └── ... (594 total skills)
├── agents/                     # 20 Specialized agent personas (frontend, backend, security, etc.)
├── workflows/                  # 17 Autonomous slash command workflows (/battle, /owl, /debug, etc.)
├── rules/                      # Core behavioral rules (GEMINI.md, brainsyncory.md)
├── scripts/                    # Validation scripts (checklist.py, verify_all.py)
├── category/                   # 16 Functional Category Directories with in-editor browsing & indexes
├── library/                    # Offline reserve store (2,031 skills across 36 repositories)
│   └── activate_skill.py       # Instant 1-command hot-set activation utility
├── .shared/                    # Shared dataset matrices (ui-ux-pro-max palettes, typography, icons)
├── SKILLS_PROVENANCE.md        # Complete upstream repository origin registry
├── skills-lock.json            # Machine-readable hashes, upstream URLs & timestamps
└── ARCHITECTURE.md             # System map and token budget documentation
```

---

## 📜 License & Attribution

- Built and maintained with 💜 by **[SeaXen](https://github.com/SeaXen)**.
- Skills and plugins retain the open-source licenses of their respective upstream authors (Anthropic, Vercel Labs, Emil Kowalski, Addy Osmani, Microsoft, Cloudflare, Supabase, and the open-source agent community).
- See [`SKILLS_PROVENANCE.md`](./SKILLS_PROVENANCE.md) for full attribution and author repositories.
