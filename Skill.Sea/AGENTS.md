# AGENTS.md — Skill.Sea Web Application

> **Frontend Architecture, Maintenance & Runbook for AI Agents**
> Companion to Master Agent Manual at [../AGENTS.md](file:///d:/Repo/.agents/AGENTS.md).

---

## 1. Overview & Live Endpoints

`Skill.Sea` is the zero-dependency web interface, leaderboard, and interactive exploration portal for the **17,145 Antigravity Agent Skills** indexed across 339 open-source repositories in 38 categories.

* **Live Production URL:** [https://skill-sea.pages.dev](https://skill-sea.pages.dev)
* **Local Development Server:** `http://127.0.0.1:8080`
* **Edge Storage:** Cloudflare R2 bucket `skill-sea-vault`
* **Cloudflare Binding:** `env.SKILLS_BUCKET` inside `functions/data/[[path]].js`

---

## 2. Directory Structure

```
Skill.Sea/
├── index.html                 # Semantic HTML5 SPA markup (Skip link, dialog drawers, comparator, simulator)
├── server.js                  # Zero-dependency Node.js HTTP static server (port 8080, mime types, security headers)
├── manifest.json              # Progressive Web App (PWA) manifest
├── sw.js                      # Service Worker with offline caching & dynamic catalog stale-while-revalidate
├── _headers                   # Cloudflare Pages HTTP security & Cache-Control headers
├── _routes.json               # Cloudflare Pages function route configuration
│
├── styles/
│   ├── design-tokens.css      # CSS variables (Teal #1d9e75, warm light #f9f9f7, dark graphite #0b0b0b)
│   └── main.css               # Mobile bottom sheet, comparator, prompt simulator, accessible focus rings
│
├── src/
│   └── app.js                 # Vanilla ES6 state engine, fuzzy search, hash routing, agent stack tray
│
├── functions/
│   └── data/[[path]].js       # ⚡ Cloudflare Pages Function (streams /data/* directly from R2 bucket)
│
├── data/                      # 📦 PRE-AGGREGATED MASTER DATASETS (Rebuilt automatically)
│   ├── catalog.json           # 20.30 MB master catalog (17,145 items)
│   ├── categories.json        # 38 domain category records
│   ├── repositories.json      # 339 repository cards
│   └── stats.json             # Real-time telemetry counts
│
├── scripts/
│   ├── build-catalog.js       # Rebuilds data/*.json from filesystem & library/
│   ├── sync-r2.js             # Uploads data/*.json to Cloudflare R2 bucket `skill-sea-vault`
│   └── verify.js              # 63-point automated verification test suite
│
└── tests/
    └── test_webapp.py         # Playwright E2E browser test suite (Desktop and Mobile)
```

---

## 3. Core Operating Commands

All commands are run from `D:\Repo\.agents\Skill.Sea`:

```powershell
# 1. Start local dev server (port 8080)
npm run dev
# or: node server.js

# 2. Rebuild catalog from physical filesystem & library/
npm run build:catalog

# 3. Synchronize catalog datasets to Cloudflare R2 (skill-sea-vault)
npm run sync:r2

# 4. Rebuild catalog AND upload to R2 in one command
npm run sync

# 5. Run full verification test suite (63 checks)
npm run verify

# 6. Run Playwright E2E browser tests (Desktop & Mobile)
npm run test:e2e

# 7. Deploy static frontend assets to Cloudflare Pages
npm run deploy
```

---

## 4. Frontend Invariants (Strict Quality Rules)

1. **Zero External Runtime Dependencies**:
   - Absolutely NO React, Vue, Svelte, Tailwind CSS, or Webpack/Vite build steps.
   - Pure HTML5 + CSS3 Variables + Vanilla ES6 JavaScript only.
2. **Mobile-First Touch & Scroll Safety**:
   - `body` MUST have `touch-action: pan-y;` at all times.
   - Do NOT apply `overscroll-behavior-y: none;` to `html` or `body`. Confine it strictly to modal scrolling containers (`.drawer-body`, `.comparator-body`, `.stack-items-list`).
   - Floating containers (like `.agent-stack-tray`) must use `pointer-events: none;` on the outer fixed wrapper, and `pointer-events: auto;` on interactive child elements (`.stack-dock-btn`, `.stack-panel`).
3. **Design Tokens & Theme Consistency**:
   - Primary Accent: `var(--teal-primary)` (`#1d9e75`)
   - Accent Strong: `var(--teal-strong)` (`#0f6e56`)
   - Surface Light: `var(--surface-0)` (`#f9f9f7`)
   - Surface Dark: `var(--surface-0)` (`#0b0b0b`)
   - Always use tabular numerals (`font-variant-numeric: tabular-nums`) on counts, dates, and metric badges.

---

## 5. Live R2 Edge Data Flow

Requests from live visitors to `https://skill-sea.pages.dev/data/<fileName>` are intercepted by `functions/data/[[path]].js`:
1. It queries Cloudflare R2 bucket `skill-sea-vault` (`SKILLS_BUCKET.get('data/<fileName>')`).
2. If found, it streams the object with `ETag` and HTTP 304 conditional request support.
3. If R2 is offline or missing, it falls back seamlessly to the static CDN copy in `Skill.Sea/data/`.

To update the live data for all visitors worldwide without redeploying frontend code:
```powershell
npm run sync
```
This updates R2 instantly, and live visitors receive the latest data on their next page view or refresh.
