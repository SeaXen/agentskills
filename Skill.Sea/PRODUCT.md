# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Zero-runtime external dependencies. Pure vanilla HTML5, custom design tokens in CSS3, vanilla ES Modules in JavaScript, and a zero-dependency Node HTTP static server. Compatible with static edge deployment (Vercel, Cloudflare Pages, Netlify, GitHub Pages) and local execution via `node server.js` or `npm run dev`.

## Users

1. **AI Systems & Autonomous Agents**: Autonomous coding agents running in Google Antigravity, Claude Code, Cursor, and Windsurf that need targeted, on-demand skill activation without inflating LLM context windows or incurring token bloat.
2. **AI Engineers & Developers**: Builders configuring local agent environments who need to discover, evaluate, and 1-click activate production-tested skills across specific technical domains (backend, frontend, security, data, DevOps, web3).
3. **Open-Source Community**: Visitors browsing the catalog online to explore agent capabilities, compare upstream implementations, and clone curated skill libraries.

## Product Purpose

Skill.Sea is an ultra-fast, zero-dependency directory, leaderboard, and 1-click activation suite for curated AI Agent Skills. It indexes 7,400+ skills discovered across 212 open GitHub repositories and organizes them into 38 distinct engineering disciplines. Success means zero-friction discovery and instant, offline-capable workspace activation with zero token bloat.

## Positioning

Unlike bloated registries or monolithic skill packs that force thousands of instructions into agent prompts, Skill.Sea operates as an on-demand virtual warehouse:
- **Zero Token Overhead**: Skills remain indexed in the master library and are linked into `.agents/skills/` only when needed for a specific task.
- **Hot-Set Tier (130 Skills)**: A pre-linked, curated core tier of high-impact skills immediately available for zero-latency execution.
- **Dual Operating Topology**: Operates as a local workbench inside the developer's filesystem and deploys statically to the web without requiring a backend database.

## Operating Context

- **Local Development Workbench**: Served on `http://127.0.0.1:8080` inside `D:/Repo/.agents/Skill.Sea`, mounted directly alongside the `.agents/library/` master repository and active `.agents/skills/` directory.
- **Git Hook Automation**: Automatically synchronized via Git pre-commit hooks (`scripts/setup_hooks.py` and `category_system.py`), ensuring datasets (`catalog.json`, `categories.json`, `repositories.json`, `stats.json`) stay synchronized on every commit.
- **Dual Display Modes**: Seamless switching between light (warm paper `#f9f9f7`) and dark (deep graphite `#0b0b0b`) themes.
- **Responsive Environments**: Full desktop multi-column data views, tablet grid views, and mobile-native bottom sheet drawer views with notch/Dynamic Island safe-area accommodation.

## Capabilities and Constraints

- **Confirmed Functionality**:
  - Full-text instant search across names, descriptions, categories, and command snippets with keyboard shortcut (`/`).
  - Edge-to-edge telemetry metrics cards showing real-time synchronized counts (Skills, Categories, Repositories, Hot-Set).
  - Horizontal scrolling category rail with colored badges and item counts.
  - 1-Click install mode switcher supporting:
    1. Universal NPX (`npx skills add <url>`)
    2. Local CLI & Symlink activation (`python .agents/library/activate_skill.py activate <name>`)
    3. My Repo Vault installation (`git clone https://github.com/SeaXen/agentskills.git .agents`)
  - Detail slide-over drawer showing full markdown documentation, parameter lists, example prompts, and source repository links.
  - Tab navigation across Skill Hub, Hot-Set, 38 Categories, 212 Git Repositories, and Install Guide.
- **Constraints**:
  - Absolute zero external runtime JavaScript or CSS dependencies (no React, no Vue, no Tailwind, no external CDN trackers). Only Tabler icons are pulled via CDN with local SVG fallbacks.
  - Strict preservation of offline capability for all local development and activation workflows.
  - **Full Repository File Retention**: When skills or repositories are downloaded or updated from upstreams, all files of that repo (docs, scripts, examples, assets) stay intact in the files. Files are never deleted automatically; they are deleted only when the user explicitly instructs to delete them.

## Brand Commitments

- **Name**: Skill.Sea (AgentSkills Vault & Leaderboard).
- **Tone**: Technical, precise, restrained, and modern. No generic AI SaaS clichés or marketing fluff.
- **Identity Colors**: Primary deep teal (`#1d9e75`), dark teal (`#0f6e56`), warm paper surface (`#f9f9f7`), deep dark surface (`#0b0b0b`), and domain-specific category pill accents.

## Evidence on Hand

- **Master Catalog Data**: `Skill.Sea/data/catalog.json` (7,401 validated items).
- **Taxonomy Categories**: `Skill.Sea/data/categories.json` (38 domain definitions).
- **Origin Repositories**: `Skill.Sea/data/repositories.json` (212 indexed repositories).
- **Telemetry Statistics**: `Skill.Sea/data/stats.json` (7,401 skills, 38 categories, 212 repos, 130 hot-set).
- **Physical Skill Files**: Canonical source directories under `.agents/skills/` and `.agents/library/`.

## Product Principles

1. **Precision & Restraint**: Information density and scanability outrank decorative fluff. Tabular numerals, tight groups, and clear hierarchies allow instant decision-making.
2. **Zero-Latency Execution**: Local agent workflows must never wait on network requests. Symlinks and local indices provide immediate workspace availability.
3. **Truth in Telemetry**: Numbers on screen must match physical files in the filesystem. Desynchronization or hardcoded stale counts are treated as defects.
4. **Resilient Portability**: The web app runs anywhere a static web server or browser can run, with zero external database dependencies.

## Accessibility & Inclusion

- Adherence to WCAG 2.1 AA standards: minimum 4.5:1 text contrast on all functional states.
- Strict 11px font-size floor for all functional badges, buttons, timecodes, and labels.
- Keyboard navigation: skip-to-content link, `/` for search focus, `Escape` to dismiss drawers, `T` to toggle theme.
- Accessible ARIA landmarks, dialog roles, and screen-reader status live-regions.
