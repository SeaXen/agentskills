# AGENTS.md — Antigravity Agent Skills Vault & Skill.Sea

> **Universal Operational Manual & System Runbook for AI Agents**
> Supported Agents: Antigravity, Claude Code, Cursor, Windsurf, Codex, and autonomous CLI subagents.

---

## 1. Executive Summary & Ground Truth Metrics

This repository (`D:/Repo/.agents` / `https://github.com/SeaXen/agentskills.git`) is the master archive and operational engine for **Antigravity Agent Skills** and its companion public web application, **[Skill.Sea](https://skill-sea.pages.dev)**.

### Verified Production Metrics
* **Total Catalog Skills:** `17,145` validated skills
* **Total Upstream Repositories:** `339` indexed libraries
* **Taxonomy Categories:** `38` engineering & domain disciplines
* **Active Hot-Set Skills:** `130` curated skills pre-linked into `.agents/skills/`
* **Live Web Endpoint:** [https://skill-sea.pages.dev](https://skill-sea.pages.dev)
* **Cloudflare R2 Storage Bucket:** `skill-sea-vault`
* **Cloudflare Account ID:** `dd110134ac07f1ddaf0ca47023e7c831` (`02. drsea@drhrs`)

---

## 2. Architecture & File Anatomy

```
D:/Repo/.agents/
├── AGENTS.md                          # 📍 THIS FILE: Master Agent Manual & Incident Runbook
├── ARCHITECTURE.md                    # System architecture documentation
├── PRODUCT.md                         # Product specification & UX constraints
├── SKILLS_PROVENANCE.md               # Upstream source tracking and attribution table
├── skills-lock.json                   # Resolved dependencies & lockfile for workspace skills
│
├── skills/                            # 🔥 ACTIVE HOT-SET (130 skills immediately accessible to agents)
│   ├── clean-code/                    # Example: coding standards skill
│   ├── frontend-design/               # Example: web design principles
│   └── ...                            # (Each skill contains a required SKILL.md)
│
├── library/                           # 📚 FULL REPOSITORY ARCHIVE (339 open-source repositories)
│   ├── upstreams.json                 # Registry mapping 339 repo slugs to GitHub URLs & commit hashes
│   ├── skills_index.json              # Aggregated master skill index
│   ├── addyosmani-agent-skills/       # Complete upstream repo files intact (zero auto-deletion)
│   ├── vercel-labs-skills/            # Upstream repo files intact
│   └── ...
│
├── category/                          # 🏷️ 38 DOMAIN CATEGORIES (Auto-generated taxonomy)
│   ├── categories_index.json          # Master category index with counts and skill ID arrays
│   ├── frontend-ui-components/        # Category folder containing README.md & skill links
│   ├── backend-api-design/
│   └── ...
│
├── skillssh/                          # 🌐 SKILLS.SH INTEGRATION (>=100K install tracker)
│   ├── skillssh.py                    # Audit, sync, and update engine for skills.sh repositories
│   └── .cache_skills_sh.json          # Cached metadata from skills.sh
│
├── skillleaderboard/                  # 🏆 SKILL LEADERBOARD TRACKER (skillleaderboard.com)
│   └── skillleaderboard.py            # Audit, sync, and update engine for trending/starred skills
│
├── Skill.Sea/                         # 🚢 PRODUCTION WEB APPLICATION (Zero-runtime deps)
│   ├── index.html                     # Semantic HTML5 SPA markup (desktop, tablet, mobile)
│   ├── server.js                      # Zero-dependency Node.js HTTP server (port 8080)
│   ├── _headers                       # Cloudflare Pages production caching headers
│   ├── _routes.json                   # Cloudflare Pages function routing
│   ├── manifest.json & sw.js          # PWA offline installation & cache engine
│   ├── styles/
│   │   ├── design-tokens.css          # CSS Variables (Teal #1d9e75, warm paper #f9f9f7, dark #0b0b0b)
│   │   └── main.css                   # Responsive layouts, mobile drawers, comparator, prompt simulator
│   ├── src/
│   │   └── app.js                     # Vanilla ES6 state, fuzzy search, hash routing, telemetry
│   ├── functions/data/[[path]].js     # ⚡ Cloudflare Pages Function (streams /data/* from R2)
│   ├── data/                          # 📦 MASTER JSON DATASETS (Rebuilt automatically)
│   │   ├── catalog.json               # 20.30 MB master catalog (17,145 items)
│   │   ├── categories.json            # 38 category records
│   │   ├── repositories.json          # 339 repository cards
│   │   └── stats.json                 # Real-time metrics
│   ├── scripts/
│   │   ├── build-catalog.js           # Rebuilds data/*.json from filesystem & library/
│   │   ├── sync-r2.js                 # Uploads data/*.json to Cloudflare R2 (skill-sea-vault)
│   │   └── verify.js                  # 63-point automated verification test suite
│   └── tests/
│       └── test_webapp.py             # Playwright E2E browser tests (Desktop & Mobile)
│
├── scripts/                           # ⚙️ WORKSPACE SCRIPTS
│   └── setup_hooks.py                 # Installs git pre-commit & pre-push hooks
├── .git/hooks/
│   ├── pre-commit                     # Auto-rebuilds catalog.json on git commit
│   └── pre-push                       # Auto-syncs catalog to Cloudflare R2 on git push
├── update.py                          # 🚀 UNIFIED MAINTENANCE & UPSTREAM ENGINE
└── update.ps1 / update.sh             # Cross-platform CLI runners
```

---

## 3. The "Auto-Everything" Automation Pipeline

The repository utilizes a 4-tier zero-friction automation pipeline. When you or any agent add, update, or remove skills, synchronization happens automatically without manual uploads:

```
┌────────────────────────────────────────────────────────┐
│ 1. File Modification                                  │
│    Skill added, updated, or removed in library/ or     │
│    skills/ (via manual edit, skillssh, or update.py)   │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. Git pre-commit Hook (.git/hooks/pre-commit)         │
│    Detects staged changes in skills/, library/, or     │
│    category/. Automatically runs:                      │
│    `node Skill.Sea/scripts/build-catalog.js`           │
│    and stages Skill.Sea/data/*.json into the commit    │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. Git pre-push Hook (.git/hooks/pre-push)             │
│    Detects outgoing skill or catalog modifications.    │
│    Executes:                                           │
│    `node Skill.Sea/scripts/sync-r2.js --allow-offline` │
│    Uploads 4 datasets directly to Cloudflare R2 bucket │
│    `skill-sea-vault` via active local Wrangler OAuth.  │
│    (Gracefully continues push if offline).             │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. Cloudflare Pages Function (functions/data/[[path]]) │
│    Live site https://skill-sea.pages.dev intercepts    │
│    requests to /data/*. Streams object from R2 with    │
│    HTTP ETags (304 support). Live visitors see updates │
│    instantly with ZERO build time or frontend redeploy!│
└────────────────────────────────────────────────────────┘
```

---

## 4. Standard Operating Procedures (How To Do Anything)

### A. How to Add a New Skill
1. Create a dedicated directory:
   - For an active workspace skill: `.agents/skills/<skill-name>/`
   - For a library skill: `.agents/library/<repo-slug>/skills/<skill-name>/`
2. Create a `SKILL.md` file inside that directory with valid YAML frontmatter:
   ```markdown
   ---
   name: <skill-name>
   description: <Clear, concise single or multi-line description>
   ---

   # Skill Name

   ## When to Use
   ...
   ```
3. Commit and push:
   ```bash
   git add -A
   git commit -m "feat(skills): add <skill-name>"
   git push origin main
   ```
   *The pre-commit and pre-push hooks will handle catalog rebuilding and R2 syncing automatically.*

### B. How to Update or Remove a Skill
1. Update or delete the corresponding folder in `.agents/skills/` or `.agents/library/`.
2. Commit and push:
   ```bash
   git add -A
   git commit -m "chore(skills): remove <skill-name>"
   git push origin main
   ```

### C. How to Pull Upstream Updates for All 339 Repositories
Run the master update engine:
```powershell
python update.py
# Or on Linux/macOS:
./update.sh
```
This updates all upstreams, rebuilds taxonomy categories, updates `catalog.json`, syncs to R2, and commits/pushes to GitHub.

### D. How to Audit & Ingest Repositories from skills.sh
* **Audit coverage:** `python skillssh/skillssh.py --check`
* **Ingest missing repos:** `python skillssh/skillssh.py --sync --push`
* **Update existing repos:** `python skillssh/skillssh.py --update --push`
* **Target single repo:** `python skillssh/skillssh.py --repo owner/repo --sync --push`

### E. How to Audit & Ingest from skillleaderboard.com
* **Audit trending:** `python skillleaderboard/skillleaderboard.py --trending 50`
* **Audit top starred:** `python skillleaderboard/skillleaderboard.py --starred 150`
* **Ingest missing:** `python skillleaderboard/skillleaderboard.py --starred 150 --ingest --push`
* **Update existing:** `python skillleaderboard/skillleaderboard.py --update --push`

### F. How to Force an Immediate Re-Index & Web Catalog Rebuild
```powershell
python update.py --reindex --push
# Or inside Skill.Sea:
npm run sync
```

---

## 5. Architectural Invariants (NEVER VIOLATE)

1. **Zero External Runtime Dependencies in Skill.Sea**:
   - The web app must run purely on native HTML5, CSS3 tokens, and ES6 JavaScript.
   - Do NOT introduce React, Vue, Tailwind, Webpack, Vite, or external bundling frameworks.
   - The local dev server (`server.js`) must remain pure Node.js standard library (`http`, `fs`, `path`, `url`, `zlib`).
2. **Full Upstream File Retention Policy**:
   - When pulling from upstreams, **NEVER auto-delete non-skill files**. Keep all READMEs, examples, scripts, and documentation intact within `.agents/library/<repo>/`. Files may only be deleted when the user explicitly instructs.
3. **Design System & Color Tokens**:
   - Primary: `#1d9e75` (Teal), Strong: `#0f6e56`
   - Dark Surface: `#0b0b0b`, Panel: `#141414`, Border: `#262626`
   - Light Surface: `#f9f9f7`, Panel: `#ffffff`, Border: `#e5e5e0`
   - Tabular numerals (`font-variant-numeric: tabular-nums`) must be preserved on all counts and table columns.
4. **Mobile Touch & Scroll Safety**:
   - `overscroll-behavior-y: none` MUST ONLY be placed on modal drawer bodies (`.drawer-body`, `.comparator-body`), NEVER on global `html, body`.
   - `body` must always specify `touch-action: pan-y` to prevent touch-freeze on mobile viewports.
   - Floating trays (`.agent-stack-tray`) must use `pointer-events: none` on outer wrapper with `pointer-events: auto` on interactive child buttons.

---

## 6. Incident Handling & Troubleshooting ("If Anything Happens, Handle It")

### Incident 1: Live Website Shows Outdated Counts or Missing Skills
* **Cause:** Catalog was built locally but R2 was not updated, or browser CDN cache is stale.
* **Resolution:**
  1. Rebuild catalog locally:
     ```powershell
     node Skill.Sea/scripts/build-catalog.js
     ```
  2. Sync directly to Cloudflare R2:
     ```powershell
     node Skill.Sea/scripts/sync-r2.js
     ```
  3. Verify live stats:
     ```powershell
     node -e "fetch('https://skill-sea.pages.dev/data/stats.json').then(r=>r.json()).then(console.log)"
     ```
  4. If Cloudflare Pages static files were also modified, deploy static assets:
     ```powershell
     cd Skill.Sea
     npx wrangler pages deploy . --project-name=skill-sea
     ```

### Incident 2: Cloudflare R2 Upload Fails (`wrangler` Auth / Network Error)
* **Cause:** Expired OAuth session or offline terminal.
* **Resolution:**
  1. Check auth status:
     ```powershell
     npx wrangler whoami
     ```
  2. If expired, refresh token:
     ```powershell
     npx wrangler login
     ```
  3. If offline or in an automated environment without browser login, pass `--allow-offline` to continue without crashing:
     ```powershell
     node Skill.Sea/scripts/sync-r2.js --allow-offline
     ```
  4. In GitHub Actions, ensure repository secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` are configured.

### Incident 3: `build-catalog.js` Fails or Generates Corrupted JSON
* **Cause:** A newly pulled upstream repo contains malformed frontmatter in `SKILL.md` (e.g. unquoted colons, invalid YAML).
* **Resolution:**
  1. `build-catalog.js` has a resilient fallback regex parser that extracts descriptions even if YAML parsing fails.
  2. Find the offending file by running:
     ```powershell
     node Skill.Sea/scripts/build-catalog.js
     ```
  3. Correct the frontmatter in the reported skill or check `library/skills_index.json`.

### Incident 4: Mobile Touch / Scroll Freezes
* **Cause:** A style rule applied `pointer-events: auto` over the entire screen or `overscroll-behavior: none` to `body`.
* **Resolution:**
  1. Check `Skill.Sea/styles/main.css`.
  2. Ensure `body` has `touch-action: pan-y;`.
  3. Verify `.agent-stack-tray` container has `pointer-events: none;` and its `.stack-dock-btn` has `pointer-events: auto;`.
  4. Run Playwright mobile test suite:
     ```powershell
     python Skill.Sea/tests/test_webapp.py
     ```

### Incident 5: Git Hook Blocks or Fails During Push
* **Cause:** Missing executable permissions or Node not in PATH.
* **Resolution:**
  1. Re-install hooks:
     ```powershell
     python scripts/setup_hooks.py
     ```
  2. The hooks are written in POSIX shell (`#!/bin/sh`) compatible with Git for Windows `sh.exe`, Linux, and macOS.
  3. Both hooks exit with code `0` even on warnings so normal git operations are never blocked.

---

## 7. Verification & Testing Protocol

Before completing any task or claiming work is complete, execute the full verification suite:

```powershell
# 1. Run 63-point Core Project Audit & Schema Validator
node Skill.Sea/scripts/verify.js

# 2. Run Local Development Server Test
python Skill.Sea/tests/test_webapp.py

# 3. Verify Git Status
git status
```

**Quality Bar:** All 63 verification checks must pass. Zero regressions allowed.
