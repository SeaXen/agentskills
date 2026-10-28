# Skill.Sea — Agent Skills Vault & Leaderboard
## Master Architecture & Implementation Plan

> **Gravitas Policy Record**
> ```json
> {
>   "planning": "deep",
>   "context_depth": "dependency",
>   "verification_depth": "impact",
>   "delegation": "none",
>   "reason_codes": ["new-app", "multi-platform-deploy", "design-system-integration", "large-catalog-indexing"]
> }
> ```

---

## 1. Executive Summary & Vision

**Skill.Sea** is a high-performance, aesthetically refined agent skills directory, leaderboard, and installer for the 3,558+ skills across 38 categories curated in the `.agents` ecosystem.

Inspired by [skillleaderboard.com](https://www.skillleaderboard.com/), **Skill.Sea** translates the ranking, discovery, and filtering workflows into a tailored experience adopting the exact **ExamForge Design System** (`d:\Repo\.agents\Skill.Sea\design\reference\design-tokens.css`):
- **Surfaces**: Warm-gray palettes (`--surface-0: #f9f9f7`, `--surface-1: #fcfcfb`, `--surface-2: #ffffff` in light mode; `#0b0b0b`, `#151515`, `#1a1a19` in dark mode).
- **Accents**: Deep teal tones (`#1d9e75`, `#0f6e56`, `rgba(29, 158, 117, 0.16)`).
- **Hairlines**: Subtle `0.5px` border dividers and crisp pill outlines.
- **Typography**: Refined tabular numerics, weights 400 and 500 exclusively (anti-cliché, no harsh bolds).
- **Multi-Platform Zero-Lockin**: Runs on Localhost, Docker, Vercel, Netlify, Railway, Render, Fly.io, and Cloudflare Pages/Workers (Free plan) with optional Cloudflare R2 storage sync.

---

## 2. Data Sources & Architecture

The app ingests and indexes data directly from the existing `.agents` repository:

| Data Source | Location | Volume | Usage |
|---|---|---|---|
| **Categories Index** | `d:\Repo\.agents\category\categories_index.json` | 38 categories, 3,558 skills | Taxonomy, categories, counts, descriptions |
| **Skills Index** | `d:\Repo\.agents\library\skills_index.json` | 2.67 MB | Commands (`activate_cmd`, `link_cmd`), paths, repositories |
| **Upstreams Index** | `d:\Repo\.agents\library\upstreams.json` | 200+ repos | GitHub URLs, upstream repository mappings |
| **Hot Set Skills** | `d:\Repo\.agents\skills/` | 87 curated skills | Active "Hot Set" badges and quick-launch links |
| **Skill Instructions** | `d:\Repo\.agents\library/*/skills/*/SKILL.md` | Thousands | README markdown documentation, triggers, parameters |

### Catalog Aggregator Engine
A pre-compilation script (`scripts/build-catalog.js`) merges and normalizes the datasets into an optimized, search-indexed, split JSON structure:
- `data/catalog-summary.json` (~450 KB): Top metadata, metrics, and searchable indices for instantaneous client-side searching.
- `data/categories.json`: Complete hierarchy with icons and counts.
- `data/skills-chunked/`: Paginated or on-demand skill detail manifests containing full SKILL.md instructions and installation snippets.

---

## 3. Core Features & UX Flow

### 1. Masthead & Real-time Metrics Row
- Masthead title: **Skill.Sea** with subtitle *"The Autonomous Agent Skills Vault & Leaderboard"*.
- Live telemetry tiles (`.mc`):
  - **3,558** Skills Tracked
  - **38** Functional Categories
  - **207** Curated Repositories
  - **87** Active Hot-Set Skills
- System controls: Theme toggle (Light / Dark with local persistence), Search shortcut (`/`), Sync indicator.

### 2. Category Rail & Filtering
- Horizontal scrolling category rail with mask fade edges.
- Categories include: `All`, `Code Quality`, `Frontend Design`, `Multi-Agent Orchestration`, `DevOps & Docker`, `Security & Audit`, `Testing & Playwright`, `Web3 Smart Contracts`, `Cloudflare Edge`, etc.
- Multi-faceted filter drawer: Filter by Repository, Tier (Hot-Set vs Vault), Compatibility (Antigravity, Claude Code, Hermes), and Star/Traction order.

### 3. Leaderboard & Catalog View
- Toggleable layout: **Table View** (dense leaderboard layout matching skillleaderboard) and **Card Grid View**.
- Table columns:
  - **Rank / Status**: Numerical rank + status dot (Active Hot-Set vs Reserve Vault).
  - **Skill & Repository**: Skill name, repository slug, avatar/icon, concise synopsis.
  - **Category**: Color-coded pill tag.
  - **Traction / Velocity**: Star badge or composite traction score.
  - **1-Click Install**: Copy command button with instant visual feedback tooltip (`python .agents/library/activate_skill.py activate <name>`).
  - **Action**: Details drawer launcher.

### 4. Interactive Skill Detail Slide-Over Drawer
Clicking any skill opens a slide-over panel displaying:
- Complete title, upstream GitHub link (`https://github.com/user/repo`), author, license.
- Interactive multi-tab installer:
  - **AgentSkills CLI**: `python .agents/library/activate_skill.py activate <name>`
  - **Zero-Disk Symlink**: `python .agents/library/activate_skill.py link <name>`
  - **One-Line cURL**: Ready-to-run curl snippet for remote workspaces.
- Full formatted Markdown instructions (`SKILL.md` parser and viewer with code syntax blocks).
- Parameter documentation, triggers, and companion skills in the same category.

---

## 4. Multi-Platform Deployment Architecture

To guarantee out-of-the-box deployment across all 8 required platforms without code modifications:

```
Skill.Sea/
├── index.html                   # Zero-dependency, ultra-fast semantic entrypoint
├── styles/
│   ├── design-tokens.css        # ExamForge tokens (Warm-Gray + Teal palette)
│   └── main.css                 # Clean CSS with responsive layouts & drawer
├── src/
│   ├── app.js                   # Client controller (state, router, search, filter)
│   ├── search.js                # Fuzzy indexing engine
│   └── ui.js                    # DOM renderers, animations, modal controller
├── data/
│   ├── catalog.json             # Pre-aggregated master index
│   └── categories.json          # Category breakdown
├── scripts/
│   ├── build-catalog.js         # Build script to generate catalog from .agents data
│   └── sync-r2.js               # Optional Cloudflare R2 bucket syncer
├── server.js                    # Minimal Node.js / Express static server
├── Dockerfile                   # Multi-stage Alpine container (static + server)
├── docker-compose.yml           # One-command local Docker test
├── vercel.json                  # Vercel zero-config static deployment
├── netlify.toml                 # Netlify redirects and header config
├── railway.json                 # Railway service deployment config
├── render.yaml                  # Render static site blueprint
├── fly.toml                     # Fly.io edge deployment config
├── wrangler.toml                # Cloudflare Pages / Workers Free Plan config
└── package.json                 # Standard scripts (build, dev, start, r2-sync)
```

### Platform Compatibility Matrix

| Platform | Deployment Type | Command / Config |
|---|---|---|
| **Localhost** | Node / Vite or HTTP server | `npm start` or `npx serve .` |
| **Docker** | Multi-stage Nginx/Node Alpine | `docker build -t skill-sea . && docker run -p 8080:8080 skill-sea` |
| **Vercel** | Static Edge CDN | `vercel.json` |
| **Netlify** | Static Edge CDN | `netlify.toml` |
| **Railway** | Docker / Node service | `railway.json` |
| **Render** | Web Service or Static Site | `render.yaml` |
| **Fly.io** | MicroVM with health checks | `fly.toml` |
| **Cloudflare Pages / Workers** | Cloudflare Free Plan | `wrangler.toml` (Pages output: `.`) |
| **Cloudflare R2** | Optional Remote Object Store | `scripts/sync-r2.js` using `@aws-sdk/client-s3` (R2 S3-compat API) |

---

## 5. Verification & Gravitas Quality Gates

1. **Token Invariant**: All colors and measurements match `design-tokens.css` exactly (no ad-hoc purple/blue gradients).
2. **Data Invariant**: All 3,558 skills correctly resolve with functional activation commands and valid upstream GitHub links.
3. **Execution Invariant**: Verify server runs locally on port 8080 or 3000, responds with HTTP 200, and passes automated syntax/lint audit.
4. **Build Invariant**: Test `npm run build` generates deterministic output ready for any CDN or container.
