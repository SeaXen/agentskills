# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Zero-runtime external dependencies. Pure vanilla HTML5, custom design tokens in CSS3, vanilla ES Modules in JavaScript, and a zero-dependency Node HTTP static server. Compatible with static edge deployment (Cloudflare Pages, Vercel, Netlify, GitHub Pages) and local execution via `node server.js` or `npm run dev`. Edge data streaming powered by Cloudflare Pages Function binding to Cloudflare R2 bucket `skill-sea-vault`.

## Users

1. **AI Systems & Autonomous Agents**: Autonomous coding agents running in Google Antigravity, Claude Code, Cursor, Windsurf, and Codex that need targeted, on-demand skill activation without inflating LLM context windows or incurring token bloat.
2. **AI Engineers & Developers**: Builders configuring local agent environments who need to discover, evaluate, compare, and 1-click activate production-tested skills across 38 technical domains.
3. **Open-Source Community**: Visitors browsing the catalog online at [https://skill-sea.pages.dev](https://skill-sea.pages.dev) to explore agent capabilities, compare upstream implementations, and clone curated skill libraries.

## Product Purpose

Skill.Sea is an ultra-fast, zero-dependency directory, leaderboard, and 1-click activation suite for curated AI Agent Skills. It indexes 17,145 skills discovered across 339 open GitHub repositories and organizes them into 38 distinct engineering disciplines. Success means zero-friction discovery, instant evaluation, and offline-capable workspace activation with zero token bloat.

## Positioning

Unlike bloated registries or monolithic skill packs that force thousands of instructions into agent prompts, Skill.Sea operates as an on-demand virtual warehouse:
- **Zero Token Overhead**: Skills remain indexed in the master library and are linked into `.agents/skills/` only when needed for a specific task.
- **Hot-Set Tier (130 Skills)**: A pre-linked, curated core tier of high-impact skills immediately available for zero-latency execution.
- **Dual Operating Topology**: Operates as a local workbench inside the developer's filesystem and deploys statically to the web without requiring a backend database.
- **Live Edge Streaming**: Uses Cloudflare Pages Functions to stream catalog data directly from Cloudflare R2 (`skill-sea-vault`) with ETags (304 Not Modified), eliminating frontend redeployment delays when skills update.

## Operating Context

- **Local Development Workbench**: Served on `http://127.0.0.1:8080` inside `D:/Repo/.agents/Skill.Sea`, mounted directly alongside the `.agents/library/` master repository and active `.agents/skills/` directory.
- **Live Production URL**: [https://skill-sea.pages.dev](https://skill-sea.pages.dev)
- **Git Hook Automation**: Automatically synchronized via Git hooks (`.git/hooks/pre-commit` and `.git/hooks/pre-push`), ensuring datasets (`catalog.json`, `categories.json`, `repositories.json`, `stats.json`) stay synchronized on every commit and push.
- **Dual Display Modes**: Seamless switching between light (warm paper `#f9f9f7`) and dark (deep graphite `#0b0b0b`) themes.
- **Responsive Environments**: Full desktop multi-column data views, tablet grid views, and mobile-native bottom sheet drawer views with notch/Dynamic Island safe-area accommodation.

## Capabilities and Constraints

- **Confirmed Functionality**:
  - Full-text instant search across names, descriptions, categories, and command snippets with keyboard shortcut (`/`).
  - Edge-to-edge telemetry metrics cards showing real-time synchronized counts (17,145 Skills, 38 Categories, 339 Repositories, 130 Hot-Set).
  - Horizontal scrolling category rail with colored badges and item counts.
  - 1-Click install mode switcher supporting:
    1. Universal NPX (`npx skills add <url>`)
    2. Local CLI & Symlink activation (`python .agents/library/activate_skill.py activate <name>`)
    3. My Repo Vault installation (`git clone https://github.com/SeaXen/agentskills.git .agents`)
  - Detail slide-over drawer showing full markdown documentation, parameter lists, example prompts, and source repository links.
  - Tab navigation across Skill Hub, Hot-Set, 38 Categories, 339 Git Repositories, and Install Guide.
  - **URL Hash State Engine & Deep-Linking**: Full browser back/forward support and shareable URL routes (`#/hub`, `#/hotset`, `#/categories`, `#/library`, `#/guide`, `#/skill/:id`, and `#/stack=:ids`).
  - **Vanilla Typo-Tolerant Fuzzy Search**: Zero-dependency bounded Levenshtein matcher with 120ms debouncing, allowing fuzzy hits for misspellings like "dokcer" -> "docker-expert" or "palywright" -> "playwright".
  - **Agent Stack Builder & Cart Exporter**: Persistent skill collection dock with 1-click batch activation command export (Zero-Disk Symlink `python .agents/library/activate_skill.py link ...`, JSON bundle, and shareable hash URL).
  - **Interactive Prompt & Trigger Simulator**: Detail drawer tab simulating agent system prompt rules (`You are equipped with the '{name}' skill...`), user trigger keywords, and live goal input customization.
  - **Side-by-Side Skill Comparator**: Interactive matrix modal comparing 2-3 skills across category, token overhead, runtime scripts, dependencies, and install commands.
  - **Category Quick Actions**: 1-click batch operations on all 38 category cards (`⚡ Link All`, `📋 Names`, `📦 + Stack`).
  - **Live Workspace Telemetry**: Non-blocking 6s background polling watcher detecting changes to `/data/stats.json` with visual badge notifications and automatic counter synchronization.
- **Constraints**:
  - Absolute zero external runtime JavaScript or CSS dependencies (no React, no Vue, no Tailwind, no external CDN trackers). Only Tabler icons are pulled via CDN with local SVG fallbacks.
  - Strict preservation of offline capability for all local development and activation workflows.
  - **Full Repository File Retention Policy**: When skills or repositories are downloaded or updated from upstreams, all files of that repo (docs, scripts, examples, assets) stay intact in the files. Files are never deleted automatically; they are deleted only when the user explicitly instructs to delete them.

## Brand Commitments

- **Name**: Skill.Sea (AgentSkills Vault & Leaderboard).
- **Tone**: Technical, precise, restrained, and modern. No generic AI SaaS clichés or marketing fluff.
- **Identity Colors**: Primary deep teal (`#1d9e75`), dark teal (`#0f6e56`), warm paper surface (`#f9f9f7`), deep dark surface (`#0b0b0b`), and domain-specific category pill accents.

## Evidence on Hand

- **Master Catalog Data**: `Skill.Sea/data/catalog.json` (20.30 MB, 17,145 validated items).
- **Taxonomy Categories**: `Skill.Sea/data/categories.json` (38 domain definitions).
- **Origin Repositories**: `Skill.Sea/data/repositories.json` (1.54 MB, 339 indexed repositories).
- **Telemetry Statistics**: `Skill.Sea/data/stats.json` (17,145 skills, 38 categories, 339 repos, 130 hot-set).
- **Physical Skill Files**: Canonical source directories under `.agents/skills/` and `.agents/library/`.
- **Cloudflare Edge Configuration**: `functions/data/[[path]].js`, `_headers`, and `_routes.json`.

## Product Principles

1. **Precision & Restraint**: Information density and scanability outrank decorative fluff. Tabular numerals, tight groups, and clear hierarchies allow instant decision-making.
2. **Zero-Latency Execution**: Local agent workflows must never wait on network requests. Symlinks and local indices provide immediate workspace availability.
3. **Truth in Telemetry**: Numbers on screen must match physical files in the filesystem. Desynchronization or hardcoded stale counts are treated as defects.
4. **Resilient Portability**: The web app runs anywhere a static web server or browser can run, with zero external database dependencies.
5. **Zero-Friction Edge Sync**: Datasets stream from Cloudflare R2 with HTTP 304 ETags, delivering instant global catalog updates without redeploying static assets.

## Accessibility & Inclusion

- Adherence to WCAG 2.1 AA standards: minimum 4.5:1 text contrast on all functional states.
- Strict 11px font-size floor for all functional badges, buttons, timecodes, and labels.
- Keyboard navigation: skip-to-content link, `/` for search focus, `Escape` to dismiss drawers, `T` to toggle theme.
- Accessible ARIA landmarks, dialog roles, and screen-reader status live-regions.
