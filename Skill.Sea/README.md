# 🌊 Skill.Sea — Autonomous Agent Skills Vault & Leaderboard

<div align="center">

[![Skill.Sea Version](https://img.shields.io/badge/Version-v2.1_Production-0f6e56?style=for-the-badge&logo=waves)](https://github.com/SeaXen/agentskills)
[![Skills Tracked](https://img.shields.io/badge/Skills-7,401_Tracked-1d9e75?style=for-the-badge)](./data/catalog.json)
[![Categories](https://img.shields.io/badge/Categories-38_Disciplines-1d9e75?style=for-the-badge)](./data/categories.json)
[![Repositories](https://img.shields.io/badge/Origin_Repos-212_Upstreams-2563EB?style=for-the-badge)](./data/repositories.json)
[![Active Hot-Set](https://img.shields.io/badge/Active_HotSet-130_Skills-D97706?style=for-the-badge)](../skills)
[![License](https://img.shields.io/badge/License-MIT-gray?style=for-the-badge)](./LICENSE)

<br/>

**An ultra-fast, zero-dependency directory, leaderboard, and 1-click activation suite for 7,400+ AI Agent Skills across 38 functional disciplines.**  
*Inspired by [skillleaderboard.com](https://www.skillleaderboard.com/) • Engineered with the **ExamForge Design System** • 100% Zero Runtime Dependencies.*

[Live Demo (Localhost)](#-quick-start) • [Multi-Cloud Deployment](#-multi-platform-deployment-guides) • [Cloudflare R2 Sync](#-cloudflare-r2-remote-storage-sync) • [CLI Workflows](#-cli-activation-workflows) • [38-Domain Taxonomy](#-38-domain-category-taxonomy) • [Architecture](#-system-architecture)

</div>

---

## 🌟 Executive Overview

Modern autonomous AI agents (Google Antigravity, Claude Code, Cursor, Windsurf, Cline) face a critical architectural dilemma: **tool fatigue and context exhaustion**. Loading thousands of tool definitions directly into an agent's active system prompt exhausts token budgets, degrades reasoning quality, and induces tool hallucination.

**Skill.Sea** addresses this by providing an independent, high-performance visual interface, search index, and activation engine for the **SeaXen AgentSkills Vault**:

- **⚡ 7,401 Ingested Skills**: Discovered and cataloged from 212 official and community GitHub repositories.
- **🏛️ 38 Functional Disciplines**: Structured classification from backend systems, databases, and Docker/DevOps to web security, web3, and machine learning.
- **🔥 130 Hot-Set Skills**: Lean, pre-linked daily-driver skills available in the local session with zero token latency.
- **🖱️ 1-Click Activation**: Instant copy commands for Python CLI, symbolic linking, or cURL installation into any workspace.
- **🎨 ExamForge Design System**: Warm-gray surfaces (`#f9f9f7` / `#0b0b0b`), deep teal accents (`#1d9e75` / `#0f6e56`), 0.5px hairline borders, and full dark/light theme switching.
- **📱 Responsive Edge-to-Edge & Mobile Perfection**: Full 100% viewport width desktop interface and native mobile bottom tab bar navigation matching mobile touch conventions.
- **🚢 8-Platform Zero-Lockin Deployment**: Deployable to Localhost, Docker, Cloudflare Pages/Workers (Free Plan), Vercel, Netlify, Railway, Render, or Fly.io.

---

## 📐 System Architecture

Skill.Sea operates as a decoupled presentation and catalog layer built directly on top of the `.agents` vault filesystem:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   🌊 SKILL.SEA WEB APPLICATION                          │
│                                                                        │
│   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   │
│   │   📊 Skill Hub   │   │  🔥 Hot-Set (130)│   │  🗂️ 38 Categories│   │
│   └─────────┬────────┘   └─────────┬────────┘   └─────────┬────────┘   │
│             │                      │                      │            │
│             └──────────────────────┼──────────────────────┘            │
│                                    ▼                                   │
│                        Client Router & Filter Engine                   │
│               (Sub-millisecond Search, Multi-Facet Faceting)           │
└────────────────────────────────────┬───────────────────────────────────┘
                                     │ JSON Manifests
                                     ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        DATA & CATALOG ENGINE                           │
│                                                                        │
│   catalog.json (6,063)   categories.json (38)   repositories.json (225)│
│                                    ▲                                   │
│                                    │ scripts/build-catalog.js          │
└────────────────────────────────────┼───────────────────────────────────┘
                                     │ File System Ingestion
                                     ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   🏛️ .AGENTS MASTER SKILLS VAULT                       │
│                                                                        │
│   📁 .agents/skills/      Lean Active Tier (130 Hot-Set Skills)        │
│   📁 .agents/library/     Master Warehouse (6,063 Skills, 225 Repos)   │
│   📁 .agents/category/    38 Curated Functional Discipline Trees       │
│   📄 update.py            Parallel Multi-Threaded Upstream Sync Engine │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

Skill.Sea requires **zero third-party npm packages** at runtime. It runs natively using pure Node.js (or any static HTTP server).

### 1. Launch via Node.js Server
```bash
# Navigate to the Skill.Sea directory
cd .agents/Skill.Sea

# Start the native HTTP server (with Gzip compression & SPA routing)
node server.js
```

### 2. Launch via Python
```bash
cd .agents/Skill.Sea
python -m http.server 8080
```

Open your browser at **[http://localhost:8080](http://localhost:8080)**.

### Rebuilding the Local Catalog
Whenever new skills or upstream repositories are pulled into `.agents/library/`, refresh the web catalog in seconds:
```bash
node scripts/build-catalog.js
```

---

## 🚢 Multi-Platform Deployment Guides

Skill.Sea is engineered with zero server lock-in. Native deployment configurations for all 8 target hosting environments are included out of the box:

### 1. Docker & Docker Compose
```bash
# Build standalone Docker image
docker build -t skill-sea .

# Run container
docker run -d -p 8080:8080 --name skill-sea skill-sea

# Or launch with Docker Compose
docker compose up -d
```
Access at `http://localhost:8080`.

---

### 2. Cloudflare Pages & Workers (100% Free Plan)
Skill.Sea is 100% static-asset compliant with Cloudflare's worldwide edge CDN:
```bash
# Deploy instantly with Wrangler
npx wrangler pages deploy . --project-name=skill-sea
```
*Pre-configured with `wrangler.toml`, `_headers` (cache optimization), and `_redirects` (SPA fallback).*

---

### 3. Vercel
Deploy in one command using the included `vercel.json`:
```bash
npx vercel deploy --prod
```

---

### 4. Netlify
Deploy using the included `netlify.toml`:
```bash
npx netlify deploy --prod --dir=.
```

---

### 5. Railway
- Link your GitHub repository to Railway.
- Railway automatically detects the included `railway.json` and `Dockerfile`.
- Set environment variable `PORT=8080`.

---

### 6. Render
- Link your GitHub repository to Render.
- Create a **New Blueprint Instance** and select the bundled `render.yaml`.
- Render automatically provisions the static web service with zero manual configuration.

---

### 7. Fly.io
Deploy to Fly's global edge MicroVM network using `fly.toml`:
```bash
fly launch
fly deploy
```

---

## ☁️ Cloudflare R2 Remote Storage Sync

Cloudflare R2 provides S3-compatible object storage with **zero egress bandwidth fees**, allowing you to back up and host the complete skill catalog remotely.

### Configuration
Set your Cloudflare credentials in your environment:

```powershell
# Windows PowerShell
$env:R2_ACCOUNT_ID="your_cloudflare_account_id"
$env:R2_ACCESS_KEY_ID="your_r2_access_key_id"
$env:R2_SECRET_ACCESS_KEY="your_r2_secret_access_key"
$env:R2_BUCKET_NAME="skill-sea-vault"

# Run automated SigV4 sync script
npm run sync:r2
```

```bash
# Linux / macOS Bash
export R2_ACCOUNT_ID="your_cloudflare_account_id"
export R2_ACCESS_KEY_ID="your_r2_access_key_id"
export R2_SECRET_ACCESS_KEY="your_r2_secret_access_key"
export R2_BUCKET_NAME="skill-sea-vault"

npm run sync:r2
```

---

## 💻 CLI Activation Workflows

Every skill in Skill.Sea has a dedicated 1-click activation command. Once copied, run it from your project root:

### Method 1: Permanent Copy Activation
Copies the skill into `.agents/skills/<skill-name>/` so it is always available locally:
```bash
python .agents/library/activate_skill.py activate <skill-name>
```
*Example:*
```bash
python .agents/library/activate_skill.py activate clean-code
python .agents/library/activate_skill.py activate systematic-debugging
```

### Method 2: Zero-Disk Symlink / Junction
Creates an instant filesystem junction without duplicating disk storage:
```bash
python .agents/library/activate_skill.py link <skill-name>
```

### Method 3: Remote Activation via cURL (Linux / macOS / Codespaces)
```bash
curl -sSL https://raw.githubusercontent.com/SeaXen/agentskills/main/install.sh | bash -s -- activate <skill-name>
```

---

## 🗂️ 38-Domain Category Taxonomy

The 7,401 cataloged skills are classified into 38 functional disciplines:

| Domain Category | Skills | Focus Areas |
|:---|:---:|:---|
| **SQL Databases, ORMs & Indexing** | 786 | PostgreSQL, Prisma, Drizzle, query optimization, migrations |
| **Code Quality, Refactoring & Clean Code** | 546 | Clean code standards, anti-slop patterns, static analysis |
| **Backend Systems, REST & Microservices** | 181 | Express, NestJS, FastAPI, resilient service design |
| **Scientific Bio-Informatics & Laboratory** | 180 | Computational genomics, sequence alignment, molecular analysis |
| **NousResearch Hermes Agent Skills** | 179 | Advanced reasoning, tool calling, autonomous agent loops |
| **Fullstack Web Frameworks** | 175 | Next.js 15/16, React 19, Remix, Vite, Astro, Vue |
| **Frontend UI Components & Design Systems**| 168 | Radix UI, Tailwind CSS, accessible components, micro-interactions |
| **Cloudflare Edge, Workers & Serverless** | 134 | Cloudflare Workers, Pages, D1 SQL, R2 Object Storage, Vectorize |
| **DevOps, Docker, Kubernetes & CI/CD** | 128 | Multi-stage Dockerfiles, Helm charts, GitHub Actions, monitoring |
| **Security Audit, Hardening & Exploits** | 122 | OWASP 2025, threat modeling (STRIDE), API security, pentesting |
| **Agentic IDE & Tool Integration** | 118 | Antigravity IDE plugins, Claude Code hooks, Cursor rules |
| **Testing, Quality Assurance & TDD** | 115 | Playwright E2E, Vitest, contract testing, mutation testing |
| **AI Prompt Engineering & Reasoning** | 110 | Chain-of-thought, Socratic protocols, meta-prompting |
| **Machine Learning, PyTorch & Data Science**| 104 | PyTorch pipelines, feature engineering, model evaluation |
| **Web3, Solidity & Smart Contract Security**| 96 | Smart contract audits, reentrancy prevention, EVM internals |
| **Mobile App Development (React Native / Flutter)**| 92 | Native mobile UX, touch ergonomics, offline storage |
| **API Integration & Webhooks** | 88 | Stripe, GitHub API, Slack webhooks, OpenAPI validation |
| **Linux System Administration & Bash** | 85 | Shell automation, systemd services, terminal performance |
| **Documentation & Technical Writing** | 82 | ADR generation, interactive docs, markdown architecture |
| ...and 19 additional domains | 2,134 | 3D graphics, game dev, search algorithms, audio processing |

---

## 🎨 Design System & ExamForge Tokens

Skill.Sea adheres strictly to the tokens defined in `styles/design-tokens.css`:

```css
/* Color Palette */
--surface-0: #f9f9f7;            /* Light page background */
--surface-1: #fcfcfb;            /* Headers, rails, table headers */
--surface-2: #ffffff;            /* Cards, modals, drawers */
--text-primary: #0b0b0b;         /* Crisp neutral dark text */
--text-secondary: #52514e;       /* Readable secondary labels */

--teal: #1d9e75;                 /* Accent color, status indicators */
--teal-strong: #0f6e56;          /* Brand badge & primary actions */
--teal-nav-active: rgba(29, 158, 117, 0.16); /* Selected navigation pills */

/* Dark Mode Overrides */
[data-theme="dark"] {
  --surface-0: #0b0b0b;          /* Pure neutral deep background */
  --surface-1: #151515;          /* Elevated surface */
  --surface-2: #1a1a19;          /* Card & panel surface */
  --text-primary: #f0efec;       /* Off-white text */
  --text-secondary: #c3c2b7;     /* High-contrast subtext */
}
```

### Visual Standards
- **Hairline Borders**: `0.5px solid var(--border)` throughout all cards, rows, and divider lines.
- **Refined Typography**: Strict adherence to font-weights `400` and `500` (no heavy un-styled bold fonts).
- **Tabular Figures**: `font-variant-numeric: tabular-nums` for seamless rank and metric alignment.
- **Micro-Animations**: 150ms ease transitions on interactive chips, hover states, and drawers.

---

## 🧪 Automated Verification Suite

Skill.Sea contains a built-in automated verification script that validates catalog integrity, tokens, server status, and file assets:

```bash
# Run the test suite
npm test
# Or directly with Node
node scripts/verify.js
```

### Verification Checks (29/29 Passing):
- [x] All 19 core web application, data, and deployment files verified.
- [x] Catalog JSON contains 6,063 valid items with proper activation commands.
- [x] ExamForge teal tokens (`#1d9e75`, `#0f6e56`) and neutral surfaces verified.
- [x] Local HTTP server responds with HTTP 200 and valid JSON endpoints.

---

## 📄 Repository Provenance & Attribution

- Built as the official presentation directory for the **[SeaXen/agentskills](https://github.com/SeaXen/agentskills)** repository.
- Web Application Code released under the **MIT License**.
- Upstream skill definitions, tool specifications, and code remain the intellectual property of their respective repository authors.
