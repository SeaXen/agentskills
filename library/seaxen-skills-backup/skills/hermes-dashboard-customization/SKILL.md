---
name: hermes-dashboard-customization
description: "Use when customizing Hermes dashboard surfaces: Mission Control, Config-page UX, or feature-porting from third-party dashboards into built-in operator workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, dashboard, mission-control, config, ui, feature-porting, operators]
    related_skills: [hermes-agent, hermes-third-party-plugin-operations]
---

# Hermes Dashboard Customization

## Overview

This is the class-level umbrella for changing Hermes dashboard UX. Use it when the user wants to improve built-in dashboard surfaces, reorganize operator workflow, add dedicated config management UI, or port useful ideas from third-party dashboards without pretending the upstream plugin was installed unchanged.

## When to use
- Mission Control needs layout, workflow, or visual polish changes.
- The Config page exposes a raw config field but needs a safer purpose-built panel.
- A third-party dashboard has useful ideas worth porting into Hermes.
- The user wants operator-facing dashboard improvements with live verification.

## Core rules
1. Prefer improving **existing built-in dashboard surfaces** over creating redundant top-level pages.
2. Distinguish **generic schema/raw config exposure** from **dedicated management UI**.
3. If third-party code is stale or collides with Hermes identity/routing, switch to **feature-porting**, not fake installation claims.
4. Verify dashboard changes in the live running UI, not just source files.

## Subsections

### 1. Mission Control workflow customization
Use this branch when the main operator complaint is about Mission Control being cluttered, haphazard, or poorly sequenced.

Durable lessons:
- keep one Mission Control route unless the user explicitly asks for more
- prefer internal sub-tabs over a giant scroll wall
- default to sessions-first operator flow
- CSS/layout polish matters when the complaint is visual quality, not missing data
- **COMPACT DENSITY FIRST**: When user says "compact, edge to edge, less space use", they want minimal padding (p-2/p-3), tight gaps (gap-1.5/gap-2), small text (text-[10px]/text-[11px]), and data-dense tables — not "premium" visual fluff, gradients, or large shadows. Hero areas should be one row. Cards should use DenseCard pattern (rounded-xl, border-border/40, bg-card/80, p-2.5).
- **PRE-COMPUTE PANEL CONTENT**: Avoid inline ternary `panel === "x" && React.createElement(...)` inside the main return — it causes esbuild parsing errors with `:` tokens. Instead, compute `const continuityContent = panel === "continuity" && React.createElement(...)` before the return, then render `{continuityContent}` in the JSX children array.
- **INLINE UTILITIES WHEN SDK EXPORTS ARE LIMITED**: The Hermes SDK bridge (`../lib/sdk.js`) only exports React, hooks, api, fetchJSON, and a fixed component set. Formatters (formatNumber, formatCost, formatDate, timeAgoMs, trimText, prettySource) and storage helpers (safeLocalStorageGet/Set) are NOT exported — define them locally in the component.
- **ANALYTICS OVER DECORATION**: User wants rich data density: 8-stat pill rows, model deep stats (total in/out tokens, tools, sessions, by-provider breakdown), session deep stats (messages, tools, active, time span, by-source/model tables), top models table with sticky headers, provider health board with errors, skills table. Decorative gradients/shadows are noise.
- **MISSION CONTROL ↔ TELEMETRY MERGE PATTERN**: When the user wants Mission Control to "look like Hermes Telemetry" without losing Mission Control features, do not replace the page. Keep the session-first Continuity workflow, add a separate dense `Ops + Telemetry` view, and feed it from a plugin API endpoint that reads `~/.hermes/telemetry/telemetry.db` directly. Good payload sections: summary, token breakdown, top tools, provider distribution, budgets, recent runs, cron stats, and daily cost. Compact them into dense cards/mini-bars instead of large charts when the user asked for edge-to-edge density.
- **PERFORMANCE DEFAULT FOR MERGED MISSION CONTROL**: After adding telemetry-style features, do not keep the old "load everything at startup" pattern. Default to tab-scoped lazy loading: Continuity/base data first, `Ops + Telemetry` loads model analytics + telemetry only when opened, and `Config` loads skills/toolsets/cron/profiles/model info only when opened. Reduce the initial session payload to roughly 20–30 rows and fetch heavy detail only on selection. Small plugin-API caches (for example ~5s for status and ~10s for telemetry) are a good default to cut repeat cost without making the dashboard feel stale.
- **REMOVE HERO COPY ENTIRELY WHEN ASKED FOR ONE-LINE HEADER**: If the user says to remove explanatory text and make the header one line, do not merely shrink the hero. Delete the descriptive title/subtitle block and collapse the header to a compact metadata/actions row. For this user, a true one-line operational header is preferable to a smaller version of marketing copy.
- **VERIFY HYDRATION, NOT JUST FIRST PAINT**: Mission Control can briefly render zeros / `Loading Mission Control…` after navigation even when the APIs are healthy. On live verification, wait several seconds and re-check the DOM before calling the page broken. Distinguish initial shell paint from settled hydrated state.
- **BACKGROUND-HYDRATE DEFERRED KPI SOURCES IF NEEDED**: Lazy loading can improve first paint but leave top KPI tiles at zero until a secondary tab opens. If those zeros become visually misleading, keep the fast first paint and backfill deferred KPI inputs shortly after render in the background instead of returning to a blocking all-at-once load.
- **LOADING SHELL, NOT FAKE ZEROES**: When Mission Control has several concurrent data sources and first paint may take seconds, do not show a wall of zero-valued KPI cards as the main loading experience. Replace that with an explicit loading shell: a visible status line (`loading live sessions, telemetry, cron, and config…`), optional small spinner, and skeleton KPI placeholders. Keep the hero/status bar visible so the page feels alive instead of broken.
- **PARALLELIZE MISSION LOADS EARLY**: For Mission Control hydration, start the mission-status request and the rest of the dashboard/telemetry requests together rather than serializing mission first and everything else second. This materially shortens the misleading zero-state window.
- **ULTRA-DENSE KPI RULE**: When the user asks for "small box/card", "1/2 line", or "fit more info", interpret that literally. KPI cards should be compressed toward a two-line desktop pattern: label/hint on one side, value on the other, with smaller padding/radius and tighter outer gaps. Avoid tall three-line hero-card proportions.
- **CONTINUITY SHOULD TURN TABLE-LIKE ON DESKTOP**: For Mission Control Continuity, compactness means the session queue should become a table/grid on desktop (title/source/model/age/ops columns) while keeping a stacked mobile fallback. Do not waste vertical space on multi-line previews when the user is asking for density.
- **RECENT TELEMETRY SESSIONS SHOULD BE SINGLE-ROW ON DESKTOP**: In `Ops + Telemetry`, recent runs should collapse into one dense desktop row (time/platform/model/token counts/cost/status/id) with only a mobile stacked fallback. This is closer to telemetry semantics than card-per-run layouts.
- **TINY SPARKLINES ARE THE RIGHT CHART DEFAULT**: When the user wants visuals but also wants compactness, prefer tiny inline SVG sparklines in card headers (daily cost, provider distribution, top tools) rather than full charts. Verify their existence via DOM/`svg` checks if vision does not clearly surface them.
- **UNIX-SECONDS TIMESTAMP PITFALL**: Hermes session/provider timestamps may arrive as Unix seconds rather than milliseconds. In compact Mission Control lists, normalize second-based numbers to ms before `Date` / time-ago formatting, or you get absurd ages like `20595d ago`.

### 2. Config-page dedicated panels
Use this branch when a setting already exists in `config.yaml` or the generic Config page but the operator experience is confusing or misleading.

Durable lessons:
- say clearly whether the raw field already exists
- preserve storage format unless migration is truly necessary
- group mixed semantics visibly (for example, exact strings vs approval-generated category keys)
- auth-gated config APIs should be verified in-browser with the real dashboard session

### 3. Feature-porting from third-party dashboards
Use this branch when the upstream dashboard/plugin is broken, stale, colliding, or only partially compatible, but its ideas are still valuable.

Durable lessons:
- audit the upstream repo before claiming installability
- prefer incremental ports of the highest-value operator features
- back up and patch dist bundles carefully when source is unavailable
- report what was ported versus what remains unported

### 4. Terminal/workbench surfaces inside the dashboard
Use this branch when the user wants a terminal tab, command-history UX, session controls, uploads/downloads, or other operator workbench features inside the Hermes dashboard.

Durable lessons:
- prefer adding terminal/workbench capability inside the existing dashboard route rather than creating a separate dashboard
- when the user says remove **only** a standalone terminal tab/page, do not rip out shared Chat TUI pieces blindly; separate (a) sidebar nav/route removal from (b) embedded chat runtime support
- for Hermes specifically, inspect both frontend routing (`web/src/App.tsx`) and backend embedded-chat startup before claiming a terminal cleanup is safe
- when a feature spans xterm UI and runtime/session state, patch frontend and backend together
- command history that should survive browser reloads and multiple clients belongs on the server side, not only in browser `localStorage`
- terminal UI should not blindly restore stale browser tab/session state on reload if the operator expects a clean default layout
- keep action chrome compact on dense operator surfaces; icon-only buttons with clear tooltips are often better than text labels
- for flex layouts around xterm, use `flex-col` plus `flex-1 min-h-0` patterns; naive `h-full` containers often clip the last row or overflow below headers
- bind command recall only to actual keyboard arrow events; do not let wheel/scroll behavior trigger history recall
- if terminal input suddenly "stops working", inspect shell state before blaming transport; a shell left in a multiline continuation prompt (`>`) may need `Ctrl+C` or a clean session reset
- verify with live browser interaction, not just API responses
- see `references/terminal-tab-notes.md` for terminal-specific implementation notes and pitfalls

## Shared workflow
1. Inspect the current built-in surface and actual backend behavior.
2. Determine whether the problem is workflow, semantics, visual polish, upstream compatibility, or terminal/runtime interaction.
3. Choose the branch above.
4. Patch backend and frontend together when the feature spans both.
5. Build/restart as needed.
6. Verify through the live dashboard and browser.

## Common pitfalls
- **Blaming missing manifests when the tab is gated off.** User plugins with a valid `dashboard/manifest.json` still disappear from the sidebar if the name is absent from `plugins.enabled` (Hermes #46435). Symptom: `/api/dashboard/plugins` lists only a subset while `mission-control`, `third-party-tracker`, etc. remain on disk. Recovery: `hermes plugins enable <name>`, optional `/api/dashboard/plugins/rescan`, hard-refresh. See `sagar-hermes-ops` → `references/dashboard-user-plugins-enabled-gate.md`.
- Saying "the dashboard has nothing for this" when a raw config field already exists.
- Pretending a broken third-party dashboard was installed successfully when only ideas were ported.
- Treating source edits as sufficient without browser verification.
- Letting analytics walls dominate primary operator workflows.
- Storing shared terminal history only in the browser when the operator uses multiple browsers/devices.
- Restoring stale terminal tabs/sessions from browser storage and presenting them as live state.
- Misdiagnosing a shell continuation prompt as a websocket or PTY transport failure.
- **Rebuilding the whole dashboard surface when a new landing route + sidebar polish is enough.** When the user asks for a "complete" custom look, ship a single new route plus selective chrome, not a rewrite of every page.
- **Replacing the bootstrap script with one branch only.** The script is duplicated for gated (no `_SESSION_TOKEN`) and non-gated paths. Adding a new `window.__HERMES_*__` global in only one branch will silently fail in the other.
- **Forgetting to escape Tailwind v4 group slashes in CSS selectors.** `.group/nav { ... }` is a parse error in modern Vite; the rule is `.group\/nav { ... }`. JS selectors need the same escape: `'.group\\/nav[aria-current="page"]'`.
- **Borrowing features from a visual reference.** "Make it look like X" is a layout/typography/palette instruction, not a feature-import instruction. If the user adds "do not add anything from it", enforce that strictly.
- **Building a "whole design" hero with marketing copy.** Dense operator surfaces want a one-row title + big-number + actions bar, not a hero with subtitle paragraphs. Empty hero real estate is the loudest density complaint.

## Verification checklist
- [ ] Correct dashboard surface chosen (Mission Control, Config page, or feature-port)
- [ ] Backend semantics checked against real stored values
- [ ] Frontend built successfully
- [ ] Live dashboard route loads
- [ ] Browser verification confirms the intended operator experience
- [ ] Final report distinguishes real install/port status and tested behavior
- [ ] Static assets: `npm run build` outputs to `hermes_cli/web_dist/`, no server restart needed for frontend changes
- [ ] Tailwind v4 selectors: `group/action`, `group/nav` etc. escaped as `group\/action`, `group\/nav` in CSS and JS
- [ ] Trading-style KPI numbers: `font-variant-numeric: tabular-nums` on cells, `font-feature-settings: "tnum" 1`
- [ ] Sidebar section headers hidden when `isDesktopCollapsed` is true
- [ ] Active sidebar item styled via `aria-current="page"` selector, not a custom class

## Support files
- `references/terminal-tab-notes.md` — terminal-specific implementation notes and pitfalls
- `references/terminal-tab-overlay-permanence.md` — terminal overlay persistence
- `references/mission-control-plugin-structure.md` — Complete Mission Control plugin skeleton discovered during rescue
- `references/plugin-dashboard-deployment.md` — Deploying & customizing third-party plugin dashboards (systemd, time ranges, LAN access)
- See also `sagar-hermes-ops` → `references/dashboard-user-plugins-enabled-gate.md` when custom plugin tabs disappear from the sidebar.
