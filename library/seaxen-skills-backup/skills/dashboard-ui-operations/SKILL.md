---
name: dashboard-ui-operations
description: Use when building, extending, rescuing, or operating self-hosted dashboards and web UIs, especially when the work spans reverse proxies, websocket/chat plumbing, monolithic single-file apps, or dist-only frontend bundles.
version: 1.2.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [dashboard, ui, web, proxy, websocket, dist-only, monolith, operations, verification]
    related_skills: [systematic-debugging, hermes-agent]
---

## Support files

- `references/static-mount-vs-baked-python.md` — when `./static` is live-mounted but Python is image-baked, backend fixes appear stuck; bind-mount modules or rebuild.
- `references/security-review-live-state-safety.md` — live-safe security audits.
- `references/stdlib-http-server-threading-pitfall.md` — server freeze pitfall.
- `references/static-web-root-and-privileged-api-audit.md` — mandatory public-dashboard audit for repository-root static exposure, auth bypass, privileged APIs, rating caps, and remediation order.
- `references/lightweight-admin-dashboard-production-hardening.md` — end-to-end hardening runbook for static allowlists, public fail-closed auth, safe persistence/restore, SSRF controls, rootless systemd, allocator tuning, tests, and release verification.
- `references/dashboard-performance-cache-and-home-kpi-pattern.md` — fetch/cache/KPI rules.
- `references/public-readonly-dashboard-and-storage-mount-pitfalls.md`.
- `references/data-page-auto-refresh-pattern.md` — polling hook + audit bugs.
- `references/self-hosted-terminal-professional-readiness-audit.md` — evidence-based audit checklist for browser terminals/operator UIs: root-service risk, secret-file permissions, password KDFs, brute-force controls, malformed-input probes, mobile workspace QA, accessibility labels, concurrency, CI, and release drift.

# Dashboard UI Operations

## Overview

This is the class-level umbrella skill for self-hosted dashboard and operator-UI work.

## Performance pitfall: slow inventory sources must not block the dashboard

When a dashboard endpoint combines cheap host stats with slow inventory/probe sources like Docker, LAN scans, public-route checks, or HTTP probes, do **not** leave the main UI request blocked on every refresh. Use a stale-while-revalidate pattern: cache the slow source, warm it on startup, refresh it

## Static-content pitfall: raw Mermaid blocks in shipped HTML can surface browser parse errors

If a self-hosted site ships study notes / docs / dashboards as static HTML and embeds raw Mermaid blocks like `<pre class="mermaid">...</pre>`, do **not** assume the browser-side Mermaid runtime will tolerate dense medical or technical labels. In practice, labels containing combinations like `LR+`, `LR-`, `/`, parentheses, braces, or colon-heavy text can render as visible `Syntax error in text` boxes.

Safer pattern:
- render Mermaid-like content server-side into static HTML when you already have a renderer/helper available
- for this class of site, prefer converting `flowchart` / `graph` / `mindmap` blocks into owned HTML components during build rather than shipping raw Mermaid to the browser
- after patching, verify the live HTML no longer contains `<pre class="mermaid">` for the affected page and that the visible `Syntax error in text` string is absent from a fresh fetch

Verification rule:
- check the built file on disk
- check the live file/container copy actually serving traffic
- then fetch the live URL with a cache-busting query string (for example `?v=2`) before trusting browser observations
 in one guarded background thread, return cached/stale data immediately with `cached`, `stale`, `refreshing`, and timing metadata, and show the state in the UI instead of freezing.

Always measure and report real numbers for this class of work: service RAM/CPU, app/container counts, cold vs warm `/api/dashboard`, serial and concurrent endpoint benchmarks, and top Docker CPU/RAM consumers. See `references/stale-while-revalidate-dashboard-performance.md` for the implementation/verification recipe and Python `http.server` BrokenPipe suppression pattern.

Use it when a request is really about **keeping a dashboard product working in the real world**: source may be missing, the page may be a single-file monolith, reverse proxies may break websocket/chat flows, and visual success may not mean the runtime behavior is actually correct.

This umbrella replaces narrower product/session-shaped skills by keeping the shared workflow in

SeaDash-specific references:
- `references/seadash-compact-full-rewrite.md` — single-file vanilla rewrite pattern for SeaDash: scope lock, MedSea-style compact UI, backend API shape pitfalls, service-worker cache busting, and live verification checklist.
- `references/seadash-10x-optimization-layer.md` — post-rewrite “10/10” layer: command palette, layout snapshots, safe hidden/scanner semantics, dashboard perf timing/cache, and live verification.
 one place and moving product-specific detail into support files under `references/`.

## When to use

Use this skill when the user asks to:
- build or extend a self-hosted dashboard or control panel
- repair a dashboard whose HTML shell loads but runtime behavior is broken
- troubleshoot reverse-proxy, auth, websocket, or embedded-chat failures
- patch a dist-only frontend bundle or plugin where editable source is absent
- maintain a monolithic single-file dashboard with inline HTML/CSS/JS
- improve operator UX for cards, tables, alerts, layout editors, or public/local routing

Do **not** use this for:
- generic backend/API debugging with no meaningful UI surface
- pure design mockups with no operational runtime
- normal source-based frontend work where a more specific framework skill exists

## Core principle

Treat dashboard work as a full-stack runtime problem, not a screenshot problem.

Always verify four layers:
1. **render surface** — what the browser loads
2. **frontend runtime** — whether the JS actually initializes and registers features
3. **backend/API contract** — whether reads and mutations exist and behave correctly
4. **deployment path** — whether the live served bundle/process/proxy is really the one you edited

## Class-level workflow

### 1) Discover the real maintenance surface
Before editing anything, determine which class of UI you are dealing with:

- **source-first app** — editable `src/` exists; patch source and rebuild
- **dist-only bundle** — only built assets exist; patch minimally and verify aggressively
- **single-file monolith** — one `index.html` or equivalent inline-script app; treat init/runtime ordering as fragile
- **proxy/chat path** — page renders, but embedded PTY/chat/events/websockets fail through proxy/auth

Do not start patching until you know which class you are in.

### 2) Add a safety net before editing
- back up the shipped asset or single-file app
- prefer targeted edits over broad rewrites unless the file is already corrupted
- add or extend smoke tests when the environment supports them
- for runtime-only fixes, define concrete browser/API checks before touching code

### 3) Verify the whole interaction path
For any requested feature or fix, inspect all involved layers:
- frontend render path
- active JS/runtime registration path
- API client/helper functions
- backend endpoint/model support
- persistence/config storage
- process/proxy/deployment route

Do not ship fake controls, dead links, or purely visual toggles when the user asked for real operations.

### 3.25) Clone-first dashboard work: lock parity scope before building
When the user asks for a **same-to-same** dashboard or terminal clone as a separate app, do not assume "similar" is good enough.

Before coding:
- name the exact source surface being cloned
- state whether V1 is **parity-first** or only "inspired by"
- lock required public port/path expectations early
- say plainly if the current plan is not yet true parity

This avoids a common failure mode: building a functional cousin while the user expected a near-copy of layout, density, and behavior.

### 3.5) Distinguish intended port from live listener

Check both facts separately:
- **intended/configured port** — service unit, launcher flags, docs, local conventions
- **live listener** — `ss -ltnp`, HTTP probe, owning process

Correct reporting shape:

This prevents a common operator-facing mistake: confusing `connection refused` with an incorrect service convention.

### 3.6) Reboot persistence and launcher-flag drift
When the user asks whether a dashboard will start after reboot, verify the systemd state and the live port together:

- `systemctl is-enabled <unit>` / `systemctl --user is-enabled <unit>` proves reboot intent
- `systemctl is-active <unit>` proves current state
- `systemctl status` + journal prove whether it is crash-looping
- `ss -ltnp` plus HTTP probe proves the service actually bound and serves the UI

Do not treat `enabled` as enough. An enabled dashboard unit can still fail after every reboot if its `ExecStart` contains a stale CLI flag. Before preserving or adding dashboard flags in a service unit, compare them against `hermes dashboard --help`. If the journal says `unrecognized arguments`, patch the service command, reload systemd, restart, then verify listener and HTTP 200.

See `references/hermes-dashboard-reboot-and-theme-inversion.md`.

### 4) Use the right repair mode

#### A. Dist-only maintenance
Use this mode when editable source is unavailable.
- prove source is absent first
- patch built assets minimally
- check syntax after every edit
- verify using the served JS/CSS bundle, not just HTML shell text
- compare live asset filenames/markers after deploy

#### B. Single-file monolith recovery
Use this mode when the UI lives mostly in one HTML file.
- test backend endpoints first so you know whether the break is frontend-only
- extract/syntax-check inline scripts independently
- distinguish cold-load failure from manual-refresh recovery
- when adding loading/refresh state to shared chrome, avoid generic state class names like `.loading` on small header/status elements if the page already has broad `.loading` CSS; prefer scoped modifiers such as `.is-loading` / `.is-error` so the header does not unexpectedly inherit large-body loading styles during refresh
- for slow all-time dashboards, keep existing content visible during manual/auto refresh when possible instead of blanking the whole app; use a lightweight status indicator or skeleton only for first paint, then verify in the live browser that header height and key controls stay stable while data reloads
- if multiple async refreshes can overlap (auto-refresh, manual refresh, filter changes, row-detail drawer fetches), add request-version guards so stale responses cannot overwrite newer UI state
- when adding charts for newly collected metrics, verify the full persistence path before blaming the frontend: live snapshot may show the value while historical `/api/series` fails because the existing SQLite table predates the new columns. Add lightweight additive migrations (`PRAGMA table_info` + `ALTER TABLE ... ADD COLUMN`) and verify both collector insert logs and series endpoints.
- for dependency-free canvas charts, do not draw overlay series by calling a single-series renderer twice if that renderer clears the canvas. Use a multi-series renderer that clears once, computes shared bounds, then draws every line; otherwise the first line silently disappears.
- compact dashboard chrome when the user complains about vertical waste: remove redundant page-title/subtitle text, combine host/uptime/sample/update state with refresh/range/manual-refresh/pause controls into one nowrap operator bar, and cache-bust static CSS/templates before judging the live browser result.
- do not keep stacking rescue timers/hooks after repeated failures; restore from backup and reapply cleanly if needed

#### C. Proxy / websocket / embedded-chat troubleshooting
Use this mode when the page loads but live interactivity fails.
- compare raw app port versus reverse-proxy path
- inspect browser console for websocket/auth failures
- verify the exact runtime endpoints, not just `/`
- treat PTY bridges, JSON-RPC sidecars, event feeds, and auth/token injection as separate moving parts
- for browser terminals exposed through Cloudflare Tunnel or another reverse proxy, distinguish three separate states: **HTML shell loads**, **websocket opens**, and **backend command actually renders usable PTY output**. A blank terminal with successful websocket logs is often an origin-command problem, not a tunnel problem.
- if the terminal page is blank, prove whether ttyd/gotty itself is healthy by launching a minimal alternate command (for example `bash -lc 'echo READY_FROM_TEST; exec bash -l'`) on a temporary port and comparing the rendered output. If the alternate command renders correctly through the same browser/proxy path, the tunnel/proxy is fine and the original command (for example `login`) is the real fault.

#### D. Network-constrained bootstrap / no-package-install path
Use this mode when the **host has internet access but Docker builds or app containers cannot reliably reach apt/pip/npm registries**.

#### E. Single-container terminal/dashboard app simplification
For small standalone terminal/dashboard apps, prefer one Docker service/container when ease of install and operation matters more than framework separation. A Python/stdlib server can serve both `/` static UI and `/api/*` terminal/session/history APIs. This avoids unnecessary nginx/frontend sidecars, makes port/volume management simpler, and is a good follow-up once a bootstrap prototype proves the UI/API contract.

When migrating from split containers to one container:
- copy the active static UI into the backend build context, e.g. `backend/static/index.html`
- add safe static serving to the API server for non-`/api/` GETs
- update compose to one service with one public port mapping
- run `docker compose up -d --build --remove-orphans` to remove old sidecars
- verify `GET /`, `/api/health`, live browser UI, and a real terminal command through the same public port

For the next parity step under the same no-package-install constraint, add a minimal stdlib WebSocket PTY stream before attempting xterm.js/vendor work:
- implement `/api/terminal/ws` with a direct RFC6455 handshake and frame handling
- accept browser websocket auth through a query token when custom headers are not possible
- send commands over WebSocket when open and retain HTTP polling/write as fallback
- verify with both a raw websocket command probe and browser command execution
- still report clone status honestly: WebSocket streaming is closer to Hermes behavior, but not exact Hermes terminal parity without xterm.js/rendering/session-model parity

After WebSocket streaming is verified, the next best clone-parity step is usually **vendored xterm.js**, not a full npm/React rebuild, when Docker build/package networking is unreliable:
- fetch xterm.js and xterm.css from the host into the app's static vendor directory
- reference those assets directly from the single-file app; no npm build required
- initialize `new Terminal(...)` per pane after the pane DOM exists
- wire `term.onData(...)` to the PTY WebSocket and keep HTTP fallback
- track printable current-line input separately so xterm Enter updates shared command history
- add a visible reconnect control that closes/reopens active WebSocket streams
- verify served assets, xterm DOM/input, real command output, history persistence, and browser console errors

For standalone terminal clones, do not assume browser-to-PTY **input** should use the same transport as browser **output**. If output streaming over WebSocket is healthy but browser command injection is flaky or timing-sensitive, keep WebSocket for live output and make authenticated HTTP `/write` the authoritative input path. That pattern is often more robust for static/single-file terminals while still preserving live-stream behavior.

After visual/xterm parity is working, the best next reliability upgrade is often **tmux-backed durable sessions**: map one app session id to one tmux session, persist metadata separately, attach browser/backend clients to tmux, and verify by killing the attach client while the tmux session survives and can be reattached. If Docker build package installs are blocked but the host can download packages, vendor the required tmux rootfs rather than repeatedly retrying apt inside the build. See `references/rexterm-compact-rail-and-tmux-durability.md`.

### Secure first-run + recovery auth for standalone terminals

When building or hardening a standalone browser terminal (Rexterm, ttydBridge-style, single-container dashboard terminal, etc.):

- **First boot only**: allow unauthenticated account creation via `/api/auth/setup` when no account file exists. This is the only time the endpoint should succeed without a session.
- **After first account**: `/api/auth/setup` must require a valid login session + verification of the current password before allowing username/password change. Never allow unauthenticated replacement.
- For normal day-to-day account management, prefer an **in-app Settings dropdown on the terminal page**, not a separate login-page-style account editor. Keep the login page for login and first-account creation.
- Split account actions by intent: **username change** and **password change** should be separate flows/forms, not one combined "change account" submission. A compact one-line username row (`new username` + `Save`) is often the cleanest operator UX; password change should keep explicit current-password verification.
- If auth controls move into the terminal header, verify more than the icons: one missing DOM binding in a monolithic `index.html` can abort page init and make the whole terminal look broken. After any header/auth refactor, verify page boot, settings dropdown behavior, logout, and actual terminal session creation.
- **Forgot-password recovery**: provide a root-only CLI script (`scripts/reset-auth.sh`) that writes a one-time recovery code to a `0600` file (`data/auth_recovery_code`). Expose `POST /api/auth/recover` that consumes the code and allows setting new credentials. Delete the code file after successful use.
- Never expose a public "reset account" button that works without either a session+current-password or a one-time CLI code. Unauthenticated reset from the login page is a remote takeover vector.

This pattern matches the security model of ttydBridge (system login), Nexterm, and other production self-hosted terminal/management tools. The dangerous "anyone can reset" state must be rejected even when the user initially requests convenience.

Add the recovery script and the hardened `/api/auth/setup` + `/api/auth/recover` logic before declaring the auth surface complete. Verify with explicit unauthenticated vs authenticated probes after changes.

For true terminal parity, cosmetic resize is not enough. Add real PTY resize propagation end to end:
- browser resize observer or fit logic computes `cols`/`rows`
- frontend sends a resize control frame and/or explicit resize API call
- backend applies `TIOCSWINSZ` and sends `SIGWINCH`
- verification includes a shell-level probe such as `stty size`, not only visual fit

If the user says the result still does **not look like the Hermes dashboard terminal**, treat that as a parity failure, not a cosmetic nit. Do a browser visual comparison and then reduce app/dashboard chrome before adding more features:
- compress the header to a single line with small status chips
- remove explanatory subtitles and operator-rule text from the main chrome
- make toolbar/tabs one-line, nowrap, horizontally scrollable if needed
- darken the xterm host and make it visually dominant/full-bleed
- tighten right rail rows/cards and keep it subordinate to the terminal
- add small practical controls such as `Copy` beside `Stage`/`Run`, but avoid growing the chrome
- report honestly when the standalone app is still a reimplementation rather than exact React/source parity

For stdlib/static standalone terminal apps, also offer a **host-PC install path without Docker** when the user asks. A minimal `scripts/run-host.sh` can set `REXTERM_BACKEND_PORT`, `REXTERM_DATA_DIR`, `REXTERM_STATIC_DIR`, create the data dir, and exec `python3 backend/app/server.py`; a user-systemd installer can write `~/.config/systemd/user/<app>.service`. Verify host mode on an alternate port if Docker already owns the public port. When the user asks whether it now runs on host, prove the public listener is owned by the host service/process rather than Docker/container mode; do not infer this from UI behavior alone.
- for small single-container calculator/trading dashboards, if the user asks for **compact / edge-to-edge / mobile** and dislikes oversized intros, strip the hero section instead of merely shrinking it. Prefer a dense top bar with title + core utilities, keep the main surface as tight cards/grids, and push explanatory text down to one compact notes area or remove it entirely when it is just filler.
- for these compact dashboard passes, verify two separate things: (1) the oversized section is actually gone in the live browser, not just visually reduced in code, and (2) the mobile path has real single-column breakpoints with touch-sized controls rather than a desktop grid that merely wraps badly.
- if a Dockerized standalone dashboard needs **public non-secret market data** and the container cannot reach the internet but the browser can, prefer browser-side fetches to a public API for optional UI enrichment like live coin prices. Keep the core calculator/server logic local, but move the live-price helper client-side so the feature works in practice instead of exposing a dead backend endpoint.
- after frontend fixes on self-hosted dashboards, explicitly consider **stale browser assets** before declaring the current build still broken. If browser automation shows the feature works live but the user still sees old behavior, add no-cache headers for static assets/JSON, then tell the user to hard-refresh or reopen the page. For button complaints, verify the real post-click state change in the DOM (not only absence of console errors).
- for compact calculator/trading dashboards that show a live price chip, be explicit about data semantics: a CoinGecko/browser-fetched value is a **current public spot reference**, not necessarily the exchange-specific mark/last price. Do not silently overwrite the user's current mark field unless the UX explicitly asks for that behavior.
- when the user wants both convenience and control on price ingestion, support both paths explicitly: a **Price** action that can auto-fill Mark when requested, and a separate **Use as Mark** action for manual re-application after switching sources. Good default sources are CoinGecko spot, Binance last, and Bybit mark, with the chip labeling the source so the operator can see what kind of price they are using.
- for compact trading calculators, derived metrics should be visible on the main result cards rather than buried in notes. High-value defaults: **liq distance %**, **PnL/ROI at current mark**, **target exit**, and **PnL/ROI at target**. If the user is modelling DCA adds, add a compact ladder table for common increments (`+$5 / +$10 / +$20 / +$50`) instead of forcing repeated manual what-if runs.
- when the user asks for one-click reusable scenarios, separate **last snapshot** from **named saved positions**. Last snapshot can stay browser-local for convenience, but the UI must label that persistence honestly; named saves should preserve the full form plus add/remove-margin steps and expose simple one-click load, update, and delete actions.
- once the user asks for durability beyond one browser, promote named saves to a **server-side JSON or DB-backed store** and add explicit import/export actions. Good minimum set: list saves, create/update/delete one save, export all saves as JSON, and import a JSON object of named saves with overwrite-on-name semantics documented.
- when those saved positions become the main reusable data model, extend that same payload with operator metadata instead of inventing side tables: coin logo/source icon, exchange badge, folders, and tags should live on the saved-position object, feed the portfolio view, and flow through CSV export and backup/restore.
- if you add backup/restore to a standalone calculator, prefer simple timestamped on-disk archives first. Good minimum behavior: create a timestamped archive under the app data directory, list available archives, download/export them, and restore one archive back into the live saved-position store.
- for trading calculators that support frequent symbol changes, add a dedicated **Reset for new coin** action instead of leaving the old entry/fill/target values in place. The reset should clear coin-specific numeric fields, keep stable preferences like side/mode/source, and optionally reseed Mark/fill/target from the newest fetched price so the next what-if starts cleanly.
- if the user wants a portfolio view, build it from the same saved-position payloads rather than inventing a second position model. Aggregate totals like **positions**, **collateral**, **entry notional**, **PnL/ROI at mark**, **PnL/ROI at target**, and **liq distance %**, then render the per-position rows from those same saved states.
- for the next high-ROI pass on a compact trading/risk dashboard, prefer a coherent phase-1 bundle over isolated tweaks: **risk badges**, **portfolio summary cards**, **always-visible search/filter/sort**, **compact CTA-driven empty states**, and **primary-vs-secondary metric hierarchy with projected delta chips**. This is the fastest route from “useful calculator” to “decision-support dashboard.”
- when shipping that bundle, verify both states of the backup surface: the empty CTA state and the non-empty restore/download state after creating a real archive. Do not stop after checking only one of them.
- if a summary/KPI card uses compressed notation like `0/0`, judge it as a UX risk even when the data is technically correct; operator summary cards should read clearly at a glance.
- for Dockerized standalone calculators, do not call saves/backups durable until you verify the app data path is bind-mounted or backed by a named volume. Rebuild/recreate can wipe container-local JSON archives even when the feature itself works. Warn clearly and add a host volume before claiming persistence is solved.
- if you use a second port for live verification during a dashboard pass, keep it explicitly temporary, kill it after testing, and restate the configured primary port in the final report so the user does not think the app was migrated.
- for browser-fetched exchange/spot helpers on trading dashboards, maintain an explicit symbol-mapping table for known mismatches and memecoins (`WIF`, `1000PEPE`, `1000BONK`, etc.) instead of assuming `SYMBOLUSDT` works everywhere. Verify the chosen source and mapping in the live chip text.

See `references/single-container-standalone-terminal-app.md`, `references/stdlib-websocket-terminal-streaming.md`, `references/vendored-xterm-standalone-terminal.md`, `references/standalone-terminal-compact-parity-and-host-install.md`, and `references/standalone-calculator-live-price-and-cache-busting.md`.

Do not keep burning time on repeated package-manager retries if the product goal is still reachable.

Practical fallback:
- verify the split explicitly: host can fetch, container/build cannot
- avoid `apt-get`, `pip install`, and frontend build chains for the first milestone
- pivot to the narrowest dependency-free stack that can still prove the feature works
- for terminal/dashboard prototypes, a strong fallback is:
  - stdlib-only Python backend
  - static nginx frontend
  - PTY/session handling via stdlib
  - HTTP polling before websocket streaming
- get a **real working milestone** first (health, create session, send command, read output, browser smoke test)
- only then decide whether the environment problem is worth solving for richer dependencies

This is not the final architecture preference; it is a delivery tactic for constrained environments.

Why it matters:
- keeps progress moving when package registries are unreachable inside builds
- produces a verifiable artifact instead of a blocked scaffold
- reduces the risk of claiming parity/features that were never exercised live

### 5) Optimize for operator truth
A dashboard should tell the operator what is really happening.

Prefer:
- grouped/deduped alert summaries over noisy repeated strings
- consistent card/table parity
- one canonical open-target helper for local/public routing
- explicit edit/draft state for inline editing
- dense but honest cards instead of hollow visual space

### 5.5) For read-heavy operator trackers, prefer static JSON over a fragile plugin API
When the surface is mainly an inventory / update tracker and the dashboard only needs to **display generated state**, a script-written static JSON file can be the cleanest runtime contract.

Use this pattern when:
- the data is refreshed by a scheduled script anyway
- the dashboard mostly reads, not mutates
- direct plugin API fetches are awkward, auth-coupled, or route through the SPA shell unexpectedly
- you want low-risk deployment in a dist-only dashboard plugin

Recommended shape:
- generator script writes the normal report file(s)
- the same script also writes `dashboard/dist/data.json`
- plugin frontend fetches that static JSON with a cache-busting query string
- browser button does a simple reload of the JSON-backed view

Why this is a good default:
- avoids inventing backend state for read-only tracker tabs
- avoids auth/header friction for lightweight internal dashboards
- keeps cron/inventory generation and dashboard rendering tied to the same ground-truth payload
- easier to verify live: check file exists, check browser fetch succeeds, check rendered cards match JSON

This is especially good for Hermes operator tabs like third-party inventories, update boards, and other scheduled-status pages.

### 5.6) Compact-pass pattern for dense operator tracker tabs
When the user says a tracker tab or operator panel "looks big", "looks oversized", "empty and haphazard", or asks for a compact/beautiful pass, do not stop at color/theme tweaks. Tighten the information architecture directly.

For dist-only tracker tabs where the JS behavior already works, prefer a **CSS-only override pass** before touching the bundle logic: back up the stylesheet, append a marked override block, preserve all DOM/classes/actions, then verify served CSS, console, DOM dimensions, and every tracker mode. See `references/dist-only-tracker-css-redesign-and-symlink-source.md`.

Good defaults for a compact pass:
- reduce hero/title height first: smaller title, smaller subtitle/meta text, tighter top gap
- shrink KPI/stat cards aggressively: less padding, smaller hint text, tighter line height
- tighten row density in list items: smaller border radius, less padding, smaller metadata text, smaller gaps between rows
- add **section counters** beside subsection labels so the user can scan without reading the body
- collapse low-value plumbing sections into a **tiny footer line** instead of a full card (for example inventory paths or static data source hints)
- if the page is primarily for actionability, default to an **Updates only** view and keep `Show all` as a secondary toggle
- in updates-only mode, hide weak-signal sections like manual/local inventories that add noise but no action
- if the user wants the KPI row "all in one line", keep that row single-line and prefer horizontal overflow as fallback instead of wrapping into multiple rows
- after a first declutter pass, do a **final compact pass** on the three most visible density offenders: the selected/active card, the top KPI chips, and the graph/control side rail
- for the selected/active note card, prefer a quieter selected state: slimmer padding, timestamp-only or otherwise shorter metadata, at most one tag by default, and a shorter preview line than ordinary expanded cards
- for top KPI chips, soften them rather than deleting them: lower-contrast background/border, slightly smaller value text, and more muted label text so they stop competing with the main surface
- for graph/control side rails, shorten labels aggressively (`Map` over `Mini-map`, `Key` over `Legend`, shorter pill copy like `Match`, `Orph`, `Hull`) and trim redundant explanatory wording before changing layout again
- when graph labels still feel noisy after broader layout cleanup, reduce label thresholds/limits directly: show fewer labels at low and medium zoom, and make cluster labels appear later and smaller instead of leaving the graph text density untouched

Practical rule:
- compactness is not only smaller fonts; it is also removing whole containers when their content can fit in one line
- if one side of a two-column card is often empty, note that remaining bloat honestly after the pass instead of pretending it is perfect
- verify with browser vision/DOM after the CSS change; density that looks tighter in code may still leave obvious empty body space live

### 5.7) Operator update controls for tracker-style dashboard tabs
When a dashboard tab is primarily an **update board** rather than a generic report, the highest-value next step is usually **exact update-command affordances**, not more analytics.

Good default progression:
1. show the exact command on each actionable row
2. add a **Copy** button
3. add a **Run** button only for clearly safe items
4. keep unknown/manual items visible but non-runnable
5. add **Dry run / Preview safe updates** before any bulk update action
6. enable **Run all / Apply N safe** only after a safe plan is generated
7. surface scan health, generated timestamp, and cron/scheduler status near the controls
8. add clickable KPI chips for common operator filters: updates, manual review, weak sources
9. add local-only `Mark known` / `Unmark known` state for manual/local review triage when backend persistence is not needed

Safe defaults:
- the literal shell command should stay visible in the row; do not hide it behind icons only
- `Copy` is the safest default action and should be available whenever a command exists
- `Run` should only be enabled for clearly safe item classes: core app updates, hub skills, git-tracked plugins, and clean tracked git repos
- block automatic updates for weak-provenance items such as manual/local copied plugins
- refuse automatic updates on dirty repos; require a clean worktree first
- use `git pull --ff-only` for repo-style updates instead of unconstrained pulls
- bulk mode should first return a plan/count, then execute exactly that safe set when the user chooses `Run all`

Plugin/runtime notes:
- for read-heavy state, static `dist/data.json` remains a strong default; use plugin API routes for mutations like `run-update` or `run-update-all`
- Hermes dashboard plugin mutation routes are session-token protected; browser-side fetches should send `X-Hermes-Session-Token` from the dashboard page context
- after layout/CSS changes, verify the actual controls, not just the rendered page: intercept clipboard writes and assert exact copied commands; click mode toggles; run dry-run endpoints; wait long enough for scan buttons that shell out to git/network checks; see `references/third-party-tracker-button-verification.md`
- for richer tracker/operator enhancements — clickable KPI filters, scan/cron health strips, manual review cards, weak-source review, and local-only known state — see `references/third-party-tracker-operator-enhancements.md`
- for pushing a third-party tracker toward a trusted “10/10” operator surface — persisted known/ignore state, custom external git repo registry, future-install discovery rules, audit logs, and backend route verification — see `references/third-party-tracker-10-operator-registry.md`
- for repo-visibility UX, persisted-vs-local state labeling, and the practical "dashboard restart vs gateway restart" check, see `references/third-party-tracker-persistence-and-registry.md`
- for the final operator-polish tier after the tracker is already functionally complete — export buttons, `Copy cd` helpers, manual collapse/expand, audit color coding, and the rule to stop before feature bloat — see `references/third-party-tracker-final-polish-pass.md`
- if `Copy visible` or runnable counts are built from fallback inventory rows, ensure every view filters out non-updating items; a displayed inventory row like Hermes core should not leak `hermes update -y` into the command pool when core has zero updates
- for browser-console click tests against React UIs, add a short async delay after `element.click()` before reading the DOM/state; immediate reads can capture the pre-update state and falsely suggest the control did nothing
- if a newly added plugin API route returns missing/old behavior from the live dashboard while the code looks correct, restart the dashboard so the route table is re-mounted before assuming the implementation is wrong
- for Hermes dashboard plugin API changes, the required bounce is the **dashboard service**, not the gateway; if frontend assets are live but plugin routes still return SPA HTML, 405, or stale payloads, restart `hermes-dashboard.service` and then re-check the route
- if a plugin ships both a standalone dashboard server and an embedded Hermes dashboard tab (for example `hermes-telemetry`), verify those as separate runtime surfaces. A healthy standalone port (for example `:8009`) does not prove `/api/plugins/<name>/*` is mounted in the Hermes dashboard process. If the sidebar/tab appears but authenticated `/api/plugins/<name>/health` or `/summary` returns `404`, treat it as plugin-backend route divergence and restart the dashboard service. See `references/hermes-telemetry-standalone-vs-dashboard-route-divergence.md`.

Safe-item default set:

- hub skill updates (`hermes skills update <name>`)
- git-tracked plugin updates (`hermes plugins update <name>`)
- known git repos via `git -C <path> pull --ff-only`

Guardrails that matter in practice:
- do **not** auto-run updates for manual/local plugins with weak provenance
- do **not** auto-run updates for dirty repos
- use `git pull --ff-only` for repo rows to avoid surprise merge commits
- prefer explicit per-row actions over a blind `update all` button
- if you later add bulk update, start with a **dry-run / plan** surface first

### 5.8) Dashboard plugin backend route activation nuance
For Hermes dashboard plugins, changes to `dashboard/plugin_api.py` are not reliably live just because the file changed on disk.

Operational rule:
- if a new plugin backend endpoint returns `405`, old behavior, or the SPA shell instead of the expected JSON, suspect that the dashboard process is still serving the old mounted router
- after changing `manifest.json` or `plugin_api.py`, do a **full dashboard restart**, not just a browser refresh or plugin rescan
- then verify the route with an authenticated browser fetch using the dashboard session token

Practical verification shape:
- direct browser-side fetch to `/api/plugins/<name>/...` with `X-Hermes-Session-Token`
- confirm status code, content type, and a small JSON body sample
- if the dashboard process was restarted, reload the page before trusting an old browser token; pre-restart `window.__HERMES_SESSION_TOKEN__` values can yield fresh `401` responses until the page bootstraps a new session token
- only after backend verification, test the visible UI buttons that depend on that route
- for browser-console click tests against React UIs, add a short async delay after `element.click()` before reading the DOM/state; immediate reads can capture the pre-update state and falsely suggest the control did nothing

Critical stale-process pitfall:
- if browser-authenticated API fetches still show the old payload after you edited the file correctly, compare **served behavior** versus **on-disk behavior** instead of assuming your patch failed
- run the backend helper directly from disk (for example import the plugin module and call the payload function) and compare its result to the browser fetch result
- if they differ, check for a **stray manual dashboard process** still bound to the dashboard port while `hermes-dashboard.service` crash-loops with `address already in use`
- in that state, a browser refresh keeps talking to the stale manual process, so plugin route changes never appear even though the file and direct Python checks are correct
- fix by identifying the PID listening on the dashboard port, stopping the stray process, starting the managed systemd service, and then repeating the authenticated fetch

### 5.9) Custom dashboard theme inversion check
If a custom Hermes dashboard theme looks light when it should be dark, inspect the theme palette before rewriting CSS. The dashboard has a foreground difference/inversion layer; `foreground.alpha: 1` can invert a dark theme into a pale/light-looking UI. For normal dark themes, `foreground.alpha` should usually be `0` while `background` and `midground` carry the dark surface and light text values.

Verify live CSS variables in the browser, not only the YAML:
- `localStorage['hermes-dashboard-theme']` is the expected theme
- `--foreground-alpha` is `0` for non-inverted dark themes
- `--background-base` is the intended dark canvas
- browser vision/screenshot confirms dark surfaces

See `references/hermes-dashboard-reboot-and-theme-inversion.md`.

### 6) Verify like an operator, not a static analyzer
Use a mixed verification pass:
- syntax/build/test checks
- live API probes
- process/service checks
- live browser inspection of rendered cards, rows, badges, and DOM dimensions
- served-bundle verification when dist deployment is involved
- for mutation controls, verify both the backend dry-run response and the visible post-click UI state (for example the generated command list and enabled/disabled state of `Run all`)
- when the work is mainly visual polish, do **not** trust text snapshots alone; use a visual/browser QA pass to judge whether the page still looks cheap, cramped, or under-spaced after the code change
- if the first polish pass still reads as "functional admin panel" instead of premium UI, keep going: widen the hero action area, increase internal card height/padding, separate metadata into clearer chips, and reduce dense one-line status packing inside KPI cards

## Subsections preserved from absorbed skills

### Dist-only UI maintenance patterns
Preserve these durable lessons:
- successful HTML load does not prove the shipped JS bundle changed
- add failing tests/smoke markers before patching fragile built assets
- prefer explicit backend wiring over fake UI affordances
- live DOM checks matter after dense CSS/grid changes
- when dashboard plugin code on disk disagrees with the live route, compare direct on-disk helper output against an authenticated browser fetch before re-patching; a stray manual process may still own the port
- for small self-hosted monitor/admin dashboards, if the user says settings/notification pages "take too much space" or there is "no save button", treat that as an information-architecture failure, not a color/theme nit: compress the surface into a sticky action bar plus dense cards/tables, make the primary save/apply actions always visible, and keep live status chips/access info in the same top control band instead of scattered explanatory blocks
- for read-only SQLite-backed dashboard tabs, inspect the real schema/counts first and keep empty states and summary cards honest
- for compact operator Settings pages, do not stop at rearranging cards if the form controls themselves still look bright or browser-default. On dark dashboards, explicitly restyle `input`, `select`, and `textarea` backgrounds/borders/placeholders so the form fields do not read as ugly whitish boxes against the dark surface.
- for notification Settings pages, separate three truths clearly: (1) UI wiring/save/test flow, (2) backend delivery path, and (3) external credential validity. If Telegram still returns `HTTP 404 ... Not Found` after a direct backend test, report it as an invalid bot token problem rather than continuing to treat it as a dashboard bug.
- for restart buttons that target a daemon from the web UI, do not rely on pidfiles alone. If the pidfile is missing, fall back to process discovery; but do not use loose `pgrep -f` matching that can also catch your own probe shell command. Prefer exact `ps ... args` matching for the true daemon command, wait for the old PID to exit, then start a detached replacement only if nothing came back.
- if a dashboard filters SQLite rows by time and the DB stores timestamps as ISO-8601 text (`2026-06-13T07:12:09+00:00` style), do not compare them to SQLite `datetime('now', ...)` strings. Generate the cutoff in the same UTC ISO format as the stored values or the window math can silently overcount/undercount.
- when a dashboard surface reports budget or quota usage, make the display window match the enforcement window exactly. If enforcement resets at local day/month boundaries, do not show rolling 24h/30d math in the dashboard or operators will see contradictory spend numbers.
- for compact analytics additions on read-only memory dashboards, give time-window growth visual priority, keep graph/extracted summaries secondary, and avoid fake time filtering where timestamp semantics are weak
- when that dashboard is already functionally correct and the user asks for a tiny polish pass, prefer a final CSS-only spacing/balance pass plus live browser-vision verification over inventing more features
- for Mnemosyne-style conversation memory rows, treat `veracity: unknown` and low assistant auto-importance (for example `0.20`) as values to verify/explain before "fixing" them in the UI
- for Hermes dashboard plugins, verify served `dist/` assets and protected plugin API routes separately; browser-side API checks should use `X-Hermes-Session-Token` from `window.__HERMES_SESSION_TOKEN__`
- for copy buttons in dashboard contexts, verify the visible success/failure feedback path separately from actual clipboard permission success

### Hermes dashboard / embedded chat and terminal patterns
Preserve these durable lessons:
- raw port vs proxy port comparison is mandatory
- on split-port deployments, distinguish **public/proxy auth** from **Hermes app/session auth**: page routes on the public port may 401 with `WWW-Authenticate: Basic ...` while `/api/ws`, `/api/events`, or `/api/pty` separately return JSON `401 Unauthorized`; that means nginx/page auth and Hermes runtime auth are different layers, not one generic failure
- `/`, `/chat`, `/terminal`, PTY websocket, metadata websocket, publish path, and events feed are distinct failure surfaces
- proxy auth and websocket upgrade behavior often explain `events feed disconnected`
- page-shell success is not chat-runtime or terminal-runtime success
- if a route like `/terminal` appears to load only briefly and then the SPA lands on `/sessions` or another default page, treat it as a **ghost route** until proven otherwise: verify `location.pathname`, inspect the frontend route table/fallback logic, and confirm the page is still registered in `App.tsx` before calling it hidden or auth-blocked
- when adding a browser shell Terminal tab, prefer reusing the existing `/api/pty` POSIX PTY bridge with a `mode=shell` query parameter rather than creating a second PTY server; keep `mode=chat` as the default to preserve Chat behavior
- if the app currently keeps `<ChatPage />` mounted-but-hidden off-route, do not reuse that pattern for `/terminal`: a hidden mounted chat page can still open `/api/pty` + `/api/ws` and silently create empty `source='tui'` session rows (`Untitled session`, 0 msgs). Render `ChatPage` only on the real `/chat` route.
- add a second guard so future dashboard terminal paths do not clutter history even if they touch the session DB: tag terminal-originated Hermes launches with a distinct hidden source such as `dashboard-terminal`, exclude hidden sources from default session/search surfaces, and keep an explicit `HERMES_SKIP_SESSION_DB=1` kill-switch honored by session-row creation for true non-conversation transports
- for persistent browser terminal sessions, use GNU `screen` when available: spawn `screen -xRR hermes-dashboard-<session>` from `mode=shell&session=<id>`, sanitize session names, and expose a small `/api/terminal/sessions` endpoint that lists recoverable `screen -ls` sessions
- terminal UI useful defaults: multiple named session chips, configurable visible session count, recover-deleted-local-tab chips from backend screen sessions, reconnect button, local command-history chips, and a visible backend/status badge
- for compact terminal layouts: keep session chips/new-session/visible/status/reconnect/scan in one top row; put overflow sessions in a `More` dropdown; put recoverable detached screen sessions in a `Previous` dropdown; keep command history as a slim searchable right rail with per-command usage counts; remove connection splash text so prompts start near the first terminal row
- when only the first few terminal tabs should stay visible, separate **stored sessions** from **visible tabs**. The visible limit is a display rule, not a storage rule: never trim the underlying session array to `maxSessions` or the 5th+ terminal will be destroyed instead of moving into `More`.
- for persistent dashboard terminals, make deletion semantics explicit: **remove/delete tab** should affect only the browser/local session entry, while **stop/kill/permanent delete** should terminate the backend `screen` session. Surface both paths in the UI so operators do not confuse local cleanup with backend termination.
- if the older terminal UI had actionable overflow/recovery menus, preserve that operator power. `More` and `Previous` dropdowns should not be passive lists; they should expose practical actions like open/restore, rename, pin/unpin, local remove, and permanent delete/backend kill where applicable.
- terminal dropdown layering pitfall: a toolbar with `overflow-x-auto` can still clip or block absolutely positioned vertical menus even if `overflow-y-visible` is present. For `More`/`Previous` menus, prefer a visible-overflow toolbar or a portal/popover layer, high z-index, and verify with `document.elementFromPoint()` inside the menu rectangle — not just screenshots — because the menu can look visible while clicks still hit the xterm/terminal section underneath.
- when the user wants parity with an older terminal tab, restore the old **visual hierarchy** before micro-tuning: darker xterm host, less top chrome, fewer text labels, and removal of redundant per-pane status lines like `current (primary): ...` when session state is already visible elsewhere. A full-bleed feel usually matters more than adding more controls.
- if the old screenshot shows the terminal toolbar spanning the whole tab, do not keep the session/control strip inside only the left terminal column; move it above the terminal/right-rail split so it reads as one full-width header across the page
- for browser-side `clear` parity, browser buffer clearing alone is insufficient when the shell still echoes `root@...# clear`; use a combined approach that clears xterm locally and sends shell line-kill + form-feed (`Ctrl+U` + `\f`) so the next prompt redraws cleanly at the top-left
- if a standalone xterm/tmux terminal shows the prompt in the middle or prints junk like `1;2c0;276;0c`, do not treat it as only CSS. Check stale restored output and browser terminal control replies being forwarded into bash/tmux. Filter device-status/OSC replies in `term.onData`, avoid restoring stale local terminal buffers on reload, and only write a synthetic fallback prompt after a short delay if xterm is still blank.
- if the prompt still starts too low on a fresh terminal open, do not stop at the manual `clear` path. Apply the same clean redraw idea on websocket/session open after any cwd bootstrap, and only then fit/resize the terminal; prompt-first-row parity is an initial-connect problem as much as a command problem.
- for polling-based browser terminals with split panes, do **not** rebuild the entire pane DOM on every poll tick just to append output. That wipes active input state, makes typing look broken, and can falsify browser QA. Keep per-pane draft input state explicitly (prefer browser-local persistence too), update the terminal/output node in place during poll cycles, and reserve full pane rerenders for structural changes like tab/split/session reassignment.
- for dashboard shell terminals, intercept mouse wheel explicitly with `attachCustomWheelEventHandler` and scroll xterm's buffer there; do not assume key-only history handlers are enough, because wheel events can still leak into shell input/history behavior without a dedicated wheel handler
- keep command-history recall keyboard-only. If `ArrowUp` / `ArrowDown` starts concatenating or stepping through history incorrectly, suspect custom local history-index bookkeeping first; a brittle `historyNavIndexRef`-style layer is often the thing breaking recall.
- if command-history chips or the current-line mirror show prompt/CSS/control-sequence junk, strip ANSI escape sequences aggressively before syncing/saving current input; otherwise the shared history UI becomes polluted even when shell execution itself is fine.
- for terminal pane geometry, do not put the xterm host at `h-full` inside a card that also has a header row above it; make the card `flex flex-col` and the terminal host `flex-1 min-h-0` or the last row/prompt gets clipped at the bottom
- if the user wants reload to open a fresh default terminal tab set rather than restoring old local UI tabs, clear/stop persisting the terminal's `localStorage` session keys and leave old backend `screen` sessions discoverable only under `Previous`
- if terminal commands suddenly look dead and the pane shows a bare `>` prompt, suspect a shell continuation state inside the persistent `screen` session before blaming the websocket bridge; inspect the live `screen` buffer/hardcopy, then either send `Ctrl+C` to clear the multiline state or kill and recreate the affected `hermes-dashboard-*` session
- terminal refresh-state pitfall: if `More` or `Previous` disappears after reload even though backend `screen` sessions still exist, the bug is usually browser-local UI persistence rather than backend session loss. Persist the local session list, active tab, split state, and recently-closed list in `localStorage`; then, after `/api/terminal/sessions` loads, repopulate `Previous` with detached backend sessions not already present in visible/local tabs. Distinguish three layers clearly in operator-facing reasoning: (1) shell sessions are server-side persistent `screen` sessions, (2) command-history chips are server-side shared history, and (3) tab/dropdown arrangement is browser-local UI state that must be explicitly restored on refresh.
- stronger recovery rule: if the browser tab list has fallen all the way back to the default local 4-session set (`main/work/logs/scratch`) but backend `screen` sessions still exist, do **not** only hide them under `Previous`; auto-restore those backend sessions directly into the active tab list and show a small recovery banner. Otherwise the operator experiences the session as "gone" even though the shell still exists server-side.
- when operator confidence matters, give the terminal toolbar both an explicit `Restore all` action and an at-a-glance recoverable count. Good default: label the button `Restore all · N` when `N>0`, disable/dim it when `N=0`, and make its action remove restored sessions from `Previous` so the recovery state is self-clearing.
- when this reload-loss report is hard to reproduce naturally, simulate the exact failure mode: create an extra backend terminal session, force `localStorage` back to the default 4-session set, reload `/terminal`, and verify that the remote session is restored into tabs instead of only appearing as recoverable history.
- command-history accounting pitfall: ArrowUp/ArrowDown shell recall can execute a prior command while the browser-side input tracker is empty, so Enter runs the command but shared history/counts fail to increment. On terminal Enter handling, if the tracked input buffer is empty, fall back to extracting the visible command from the current prompt line before calling the shared history write path.
- command-history operator polish: show the total unique command count directly in the history rail header (for example `6 cmds`) so the user can see whether deletes/clears actually changed server-side history.
- if the terminal page is meant to mirror the currently typed shell input into the command-history search/filter box, preserve that wiring explicitly during UI refactors. Keep the pane's current-line state live in the parent, derive the active pane's current line, and sync that value back into the history query; otherwise typing in xterm still works while the history rail silently stops auto-filtering.
- when changing terminal sidebar/header/preset UI, verify behavioral cross-links too — not only the visible layout. A chrome-only change can accidentally sever hidden couplings like terminal input -> history search mirroring even when build and screenshots look fine.
- if the right rail starts feeling cramped because command history, preset banks, and file tools compete vertically, prefer a tabbed rail (`History | Presets | Files`) over a taller stacked sidebar. History should get the full rail by default; presets and files should not permanently steal height from the primary workflow.
- for terminal-side rails, do not equate “prettier” with glossier. If the user wants the panel to match the terminal, keep the rail visually subordinate to the xterm surface: darker green/black background, muted borders, low-gloss chrome, smaller radii, tighter padding, and compact counts/icons. If a premium/glassy pass makes the rail feel bigger or visually detached from the terminal, roll it back rather than iterating on the same direction.
- when preset-bank UX evolves beyond a small static block, keep the header search-oriented: an always-visible preset search field plus `Add` is a better default than extra section-title chrome or a click-to-open search affordance.
- when a standalone terminal rail feels too big or the user points to a compact reference screenshot, make History and Presets share the same compact command-row language: icon tabs with count badges, short bar rows, one-line nowrap section headers, row-click for stage/run, small trailing pin/delete/run/count controls, and no full-width `Stage / Copy / Pin / Run` button groups. Default the history visibility selector to `All` when faster direct access is requested, but keep short `10/25/50` selector choices available. Verify both tabs visually and with DOM row/header heights; fixing History while Presets remain card-like is incomplete. For terminal header controls, remove redundant per-pane headers when the main toolbar already carries state, separate local tab hide from backend Kill/Remove, keep Previous dropdown clickable even when empty, avoid toolbar overflow clipping, and color-code active/warn/danger/disabled states. If the user says the header looks too short/icon-like or asks for edge-to-edge full names, first try full labels and an explicit `Active terminal: <name>`, but do not accept a 2-3 line header as a finished state. If full labels wrap, remove the quick-command box from the header and move secondary actions (`Clear`, `Copy`, `Save`, `Restart`, `Reconnect`, `Split`, `Focus`, `Profiles`, `Settings`) into a compact `Tools` dropdown while keeping primary actions visible: active tab, New, Refresh, Rename, Hide tab, Pin, More, Previous, Restore, Remove, cwd chips, and any compact system chips. `Remove` should remain the clear destructive terminal-delete/kill action; `Hide tab` is local-only. If adding CPU/RAM/temp header telemetry, use compact polling chips and show `n/a` for unavailable sensors rather than inventing temperatures. For small standalone terminal apps where the user rejects split frontend/backend wrappers, back up first and flatten to a single-root layout with old artifacts preserved under `_archive/`. Verify with DOM metrics that the toolbar is one line (`flex-wrap: nowrap`, fixed/compact height) and with browser vision that the command box is gone. See `references/rexterm-compact-rail-and-tmux-durability.md`.

### Secure first-run + recovery auth for standalone terminals

When building or hardening a standalone browser terminal (Rexterm, ttydBridge-style, single-container dashboard terminal, etc.):

- **First boot only**: allow unauthenticated account creation via `/api/auth/setup` when no account file exists. This is the only time the endpoint should succeed without a session.
- **After first account**: `/api/auth/setup` must require a valid login session + verification of the current password before allowing username/password change. Never allow unauthenticated replacement.
- **Forgot-password recovery**: provide a root-only CLI script (`scripts/reset-auth.sh`) that writes a one-time recovery code to a `0600` file (`data/auth_recovery_code`). Expose `POST /api/auth/recover` that consumes the code and allows setting new credentials. Delete the code file after successful use.
- Never expose a public "reset account" button that works without either a session+current-password or a one-time CLI code. Unauthenticated reset from the login page is a remote takeover vector.

This pattern matches the security model of ttydBridge (system login), Nexterm, and other production self-hosted terminal/management tools. The dangerous "anyone can reset" state must be rejected even when the user initially requests convenience.

Add the recovery script and the hardened `/api/auth/setup` + `/api/auth/recover` logic before declaring the auth surface complete. Verify with explicit unauthenticated vs authenticated probes after changes.
- preset-bank persistence pitfall: updating frontend default preset arrays alone is insufficient. If `/api/terminal/preferences` POST merges only history keys and ignores `preset_sections`, browser-local preset edits/counts can look correct while server-side persistence stays stale. For any preset default/edit/save work, verify three layers explicitly: rendered section counts, browser `localStorage`, and authenticated `GET/POST /api/terminal/preferences` round-trip after a dashboard restart.
- when expanding built-in preset sections or commands, do not overwrite saved operator customizations. Normalize by merging stored `preset_sections` with the new defaults: preserve user/custom sections, append newly introduced default sections, and add missing default commands into known sections.
- when command history is large, separate **stored history** from **visible clickable rows**. Keep the total count honest, but let the operator choose how many clickable history chips/rows to render (`Top 6`, `Top 10`, `Top 25`, `Top 50`, `All`, `Custom`). `All` means render every stored command entry; presets/custom control only visible click targets, not retention.
- for right-rail terminal tooling, prefer **collapsible `<details>/<summary>` groups** for lower-frequency controls instead of permanently expanded blocks. This works well for file upload/download tools and for curated preset-command banks.
- a good default right-rail stack is: **command history first**, then a **Preset commands** card, then **Files**. Keep both Preset commands and Files collapsible so the rail stays compact while still exposing one-click actions when needed.
- preset command banks should be grouped by real operator workflows (for example `Daily Hermes`, `Daily Linux`, `Git`, `Docker`, `Network`, `Systemd`), show a small count badge in each header, and keep each row actionable: clicking the command injects it into the terminal, while secondary controls handle copy/pin actions.
- when the user wants preset rows to feel integrated with command history rather than like a separate widget family, restyle preset commands as the same compact bar language used by history rows: same dark row background, similar border/radius, tighter spacing, and compact trailing action buttons. This usually reads better than making presets look like cards.
- for compact right-rail terminal presets, prefer a `Presets` header with a **Search** toggle over permanently showing filter UI; keep the preset groups collapsed by default, auto-expand matching groups during search, and keep lower-frequency sections like **Files** collapsible below Presets.
- every preset row should support three operator actions with clear separation: **inject/run next** on primary click, **Copy** for the exact command text, and **Pin** to add it into shared quick-access history.
- if the user wants preset banks editable, use the simplest durable model: section-level textarea editing with **one command per line**, plus `Save`, `Defaults`, and `Cancel` actions.
- persist editable preset banks in two layers: browser-local `localStorage` for per-browser customization and a real server-side terminal preferences payload (for example `GET/POST /api/terminal/preferences`) for cross-device/server state. Hydration rule: prefer browser-local preset sections when present; otherwise fall back to the saved server-side preset sections.
- live-verify preset edits with both layers, not just UI chrome: confirm the edited section renders, inspect browser storage, and read back the authenticated preferences API payload so you do not mistake local-only success for true server persistence.
- persist the history-view selector in browser `localStorage` so the rail stays compact or expanded the way the operator last chose on that device/browser; live-verify by changing the selector, reloading `/terminal`, and confirming the chosen preset returns.
- if the user asks for that history-view preference to follow them across browsers/devices, keep the browser-side `localStorage` behavior and add a real server-side prefs surface (for example `GET/POST /api/terminal/preferences` backed by `~/.hermes/terminal-ui-preferences.json`). Hydration rule: prefer browser-local values when present; otherwise fall back to the saved server-side preference.
- for a compact terminal history rail, remove redundant section-title text when the rail is already visually obvious; keep the top row as a **single-line nowrap header** with horizontal overflow fallback rather than wrapping onto two lines.
- make the selector discoverable but short. Prefer a tiny chip like `clickable` over longer text once the location is learned, and keep the count chip separate from the visibility selector.
- if the operator asks for faster direct access, default the history visibility mode to `All` (while still preserving any saved browser/server preference that already exists).
- see `references/hermes-dashboard-terminal-persistence-vs-server-state.md` for the specific reload-loss diagnostic: separating persistent backend `screen` sessions, shared server-side command history, and browser-local tab/dropdown state, plus the pattern of repopulating `Previous` from detached remote sessions on load.
- see `references/hermes-dashboard-terminal-default-reset-recovery.md` for the stricter recovery rule when the browser resets to the default 4 tabs but backend sessions still exist.
- see `references/hermes-dashboard-terminal-restore-badge-and-history-accounting.md` for the concrete restore-count badge pattern and the ArrowUp/ArrowDown history-accounting fix.
- see `references/hermes-dashboard-terminal-history-visibility-selector.md` for the visible-vs-stored history pattern, selector semantics, and live verification shape.
- see `references/hermes-dashboard-terminal-history-selector-persistence-and-top-50.md` for the device-local-vs-server-side persistence distinction and the `Top 50` preset update.
- terminal wheel/history pitfall: binding command history only through `attachCustomKeyEventHandler` is not enough. The terminal tab should also install an explicit `attachCustomWheelEventHandler` that scrolls xterm scrollback and stops propagation, otherwise mouse-wheel events can still surface as shell/history navigation even while keyboard `ArrowUp/ArrowDown` handling looks correct.
- terminal fit/layout pitfall: do not give the xterm host `h-full` inside a panel that also has a header row above it. Make the terminal card `flex flex-col`, keep the host `flex-1 min-h-0`, and only then fit xterm. Otherwise the last row can be clipped because the host height ignores the header chrome.

- see `references/static-content-site-patterns.md` for knowledge-base / static-content-site patterns: auto-synthesized mindmaps from headings, universal search with pre-built JSON index, 3-column grid centered search header, Docker port alignment gotcha, missing-template-tag-after-refactor, and small-edge-gap + close-inner-items layout balance.
- reload behavior preference for Hermes dashboard terminal: do not restore prior local terminal tabs, active pane ids, or split state from browser `localStorage` when the operator expects a fresh page load. Start from the default local tabs and show persistent backend `screen` sessions under `Previous`; when migrating away from restored local tab state, clear the stale terminal localStorage keys so old sessions do not keep reappearing after reload.
- see `references/hermes-dashboard-terminal-wheel-fit-and-reload.md` for the concrete verification pattern and migration notes
- see `references/hermes-dashboard-terminal-parity-polish.md` for terminal-tab parity fixes: darker full-bleed styling, wheel-vs-keyboard history separation, ANSI-clean history sync, stale-session cleanup, and header-clipping checks
- terminal session controls should distinguish **local UI removal** from **backend process termination**: `delete` removes only the browser-side session chip/tab, while `stop`/`kill` should terminate the persistent backend `screen` session itself via a dedicated endpoint. Surface both actions explicitly so operators do not assume deleting a tab killed the shell.
- good next-step operator features for Hermes dashboard terminal: a top-bar `Stop` button for the active persistent session, kill controls in recoverable/detached-session dropdowns, and a `Clear` action for browser-shared command history. These are high-value because they reduce stale backend shells and stale suggestion noise without adding much UI weight.
- browser terminal websockets can be dropped by idle browser/proxy/network paths even when the underlying `screen` session survives; a harmless keepalive is to periodically send the existing consumed resize control frame (`\x1b[RESIZE:cols;rows]`) instead of shell input
- if an xterm.js pane crashes with `You must set the allowProposedApi option to true to use proposed API`, check addons first. `Unicode11Addon` can require `allowProposedApi: true` in the `new Terminal({...})` options even when WebGL/canvas addons have already been removed.
- if a dashboard terminal backend websocket probe succeeds but the visible pane stays `CONNECTING` or shows a stale websocket-error banner, inspect the React lifecycle before blaming `/api/pty`: unstable inline callback props (`onStatusChange`, `onCurrentLineChange`, etc.) can retrigger the terminal `useEffect` and reconnect loop. Stabilize parent callbacks with `useCallback`, update state only when values change, then rebuild/restart and browser-verify the pane.
- terminal tabs need an explicit operator warning: commands run as the dashboard process user, so public `--insecure` exposure is dangerous without external auth/proxy controls
- terminal tabs should still be treated operationally as privileged shells: commands run as the dashboard process user, so public `--insecure` exposure is dangerous without external auth/proxy controls. Prefer keeping a warning unless the user explicitly asks to remove it; if removed, preserve the security understanding in implementation notes rather than visible UI chrome.
- if a previously working dashboard terminal disappears after an update/reinstall, verify all three layers before attempting a cosmetic fix: the frontend page file, the route/sidebar wiring, and the backend `/api/terminal/*` helpers. If both route wiring and backend endpoints are gone, treat it as a lost feature that must be restored from source-level artifacts, not a hidden toggle.
- for durable restoration of custom Hermes dashboard features, do not patch `web_dist/` alone. Restore the source files and backend helpers, then keep an external patch/reapply overlay outside the installed package tree so future updates can reapply the customization after package replacement.
- when the live repo no longer contains a lost dashboard customization, mine Hermes session artifacts (`~/.hermes/sessions/request_dump_*.json`, prior transcript snippets, old bundle filenames) as recovery evidence. These dumps can preserve route names, endpoint names, and large code fragments sufficient for reconstruction even when git history is unavailable locally.
- on Hermes dashboard, a page that loads with model `closed` plus `events feed disconnected` can be a **backend websocket admission-policy bug**, not just nginx/auth misconfiguration
- explicit public bind (`--host 0.0.0.0 --insecure`) must be treated differently from loopback mode: if HTML loads over LAN but `/api/ws` and `/api/events` return `403`, inspect websocket peer-allow logic separately from token bootstrap and Host/Origin checks
- for ttyd/gotty/PTY bridges behind Cloudflare Tunnel, do not call the tunnel broken just because the browser shows a blank terminal. If Cloudflare serves the HTML and the browser console shows `websocket connection opened`, inspect the backend launch command and PTY program first. A command like `login` can produce a blank terminal even when the tunnel and websocket path are healthy; switching to `bash -l` or another direct shell can be the fix.

- See `references/cloudflare-tunnel-ttyd-blank-terminal.md`.

### 5.95) Better Auth single trusted origin — multi-network access
Many self-hosted apps (Manifest and others using Better Auth) hardcode a single trusted origin via `BETTER_AUTH_URL` and reject all others with `Invalid origin`. Do not promise "all three networks" (LAN + Tailscale + CF tunnel) with one instance — max coverage is 2 of 3 because Tailscale has no Host-header rewrite hook. Pick one of: tunnel-only (simplest), LAN + CF tunnel via `httpHostHeader` rewrite, or run N instances on different ports. See `references/better-auth-single-trusted-origin-multi-network.md`.

See `references/hermes-dashboard-*` support files, especially `references/hermes-dashboard-insecure-bind-ws-policy.md`.
See `references/hermes-dashboard-terminal-tab.md` for the concrete pattern to add `/terminal` via `/api/pty?mode=shell`, including frontend route wiring, backend mode switch, restart, and live websocket/browser verification.

### SeaDash / single-file operator dashboard patterns
Preserve these durable lessons:
- monolithic inline-script apps need explicit cold-load verification
- backend health can be good while the frontend init path is broken
- when adding or moving header/toolbar controls in a single-file dashboard or terminal, verify the DOM element actually exists before binding events. A direct `$('missing-id').onclick = ...` can throw during init and silently abort the rest of the page boot. For non-critical controls, prefer null-safe listeners like `$('id')?.addEventListener(...)`, and live-verify that the whole page still initializes after the UI tweak.
- category/layout/editor features must be verified in both card and table views
- dedupe, route mapping, and public/local target logic should resolve to one canonical app record
- operator dashboards benefit from grouped alerts, compact cards, and explicit category curation
- when a dashboard feels haphazard because everything is on one screen, fix information architecture before styling: cap auxiliary control heights, collapse low-frequency controls, tab dense detail panes, and verify actual scroll containers in the browser DOM
- if the graph/center canvas remains the busiest area after decluttering, the next structural move is a focus mode or route-level split instead of piling on more inline controls
- if the user says the dashboard still overlaps or that a polish pass changed 'nothing', treat that as a structural-layout failure, not a theme failure. Verify live geometry in the browser DOM and change panel arrangement, not just colors/padding.
- for triage dashboards that try to show notes + graph + reader together, do **not** assume a vertical top-to-bottom stack is the cure for overlap. Test live geometry first. On shorter desktop viewports, a full vertical 3-stack often makes the graph too shallow, clips the reader, and feels more broken than the original squeeze.
- when the graph is the primary surface, prefer a **balanced 2-column workbench** as the default mixed mode: fixed notes rail on the left, graph top-right, reader bottom-right. Keep focused modes for Explore/Reader/Recall work instead of forcing every job into one layout.
- if the user explicitly rejects the "fit everything into one screen" behavior and asks for **whole-page scrolling**, switch from viewport-fit to **document-flow layout**: remove `height:100vh` and forced grid-fit assumptions, let `body` scroll vertically, make top cards intentionally tall, and place the graph in a lower section the user reaches by scrolling.
- in page-flow mode, avoid fake spaciousness from mismatched row heights and card caps. If the grid row is tall but the card has a lower `max-height`, you create dead vertical bands. Either let the card fill the row or reduce the row.
- if the user asks to reduce empty vertical gap after enabling full-page scroll, check live row height versus actual panel height in the browser DOM before tuning cosmetics. Most "mystery gap" cases are geometry mismatch, not spacing tokens.
- for read-heavy note dashboards, if the user says the root/reader upper part is not fully visible, tighten the **reader header stack** before touching the graph again: reduce padding, compress chip rows, tighten tab bars, shrink action rows, and consider hiding the duplicated first `h1` in the body when the same note title is already rendered in the reader header.
- widening a notes rail usually helps more than making note cards denser. Prefer a modest width increase first, then simplify metadata only if the wider rail still feels cramped.
- for graph-first premium dashboards, reduce default workbench overlay noise aggressively: hide or demote legend/minimap/meta/stats blocks in the mixed view, shorten toolbar copy, and keep instrumentation available in dedicated focus modes rather than always visible.

- for the 2-row graph-first layout, keep the graph controls in a slim top bar or a floating/collapsible dock. Do not permanently consume bottom-row height with a full-width control rail unless the viewport is tall enough to support it.
- after switching to the 2-row layout, verify actual viewport geometry in the browser: top-row panel heights, note-list scroll height vs client height, reader scroll height vs client height, and graph canvas client height. A visually "full-width" graph can still fail if its row height collapses under a short viewport.
- for graph-first premium dashboards, reduce default workbench overlay noise aggressively: hide or demote legend/minimap/meta/stats blocks in the mixed view, shorten toolbar copy, and keep instrumentation available in dedicated focus modes rather than always visible.

See `references/seadash-*` support files and `references/obsidian-dashboard-layout-decluttering.md`.

### Obsidian graph dashboard visual polish
For canvas-based graph rendering upgrades (dot-grid, glossy nodes, arrowheads, label collision, hull visibility, simulation stability):
See `references/obsidian-dashboard-visual-polish.md`.

### Force-graph visibility tuning (v3 — from obsmemory dashboard work)

When a force-directed graph looks "sparse and dim" or the user says "graph not showing", do not accept the rendered output at face value. Measure pixel coverage and color variety first with PIL:

```python
from PIL import Image
import numpy as np
img = Image.open('/path/to/screenshot.png').crop((20, 160, img.width-20, 600))
arr = np.array(img)
sat = arr.max(axis=2) - arr.min(axis=2)
bri = arr.mean(axis=2)
vivid = ((bri > 100) & (sat > 80)).sum()  # truly colored pixels
high_quality = ((bri > 100) & (sat > 80)).sum()
```

If `vivid / total < 1%`, the graph is essentially invisible regardless of "nodes are there". Apply these tuning defaults:

| Setting | Conservative (dim) | Polished (vivid) |
|---------|-------------------|------------------|
| Node radius min/max | 5–14 px | 8–24 px (scale with degree: `9 + degree*0.55`) |
| Default zoom | 1.0× | 1.35× |
| Edge opacity (normal) | 0.22 | 0.45 |
| Edge line width | 1.0 | 1.2 |
| Node shadow blur | 6 | 14 |
| Node shadow color (default) | `rgba(0,0,0,.45)` (flat black) | `rgba(56,189,248,.35)` (cyan glow) |
| Glass border opacity | 0.24 | 0.35 |
| Gradient stops | `0.28 → base → 1.0 → rgba(0,0,0,0.38)` | `0.32 → base → 0.85 → base → 1.0 → base@0.45` |

The most impactful single change is **shadow color** — `rgba(0,0,0,.45)` makes nodes look like flat holes punched in the background. Replace with the accent color at low opacity for a glowing-orb look.

Result on the obsmemory graph (62 nodes, 236 links):
- Vivid pixels: 1,788 (0.33%) → 205,701 (37.70%) — **115× more visible**
- Vertical spread: 15% → 82% (was concentrated in one horizontal band)
- Color buckets: 6 distinct hue families visible (was effectively blue-only)

### Orphan-canvas bug pattern (CRITICAL)

When a dashboard adds a new "graph page" alongside an existing "notes page with graph", do not create a second hardcoded `<canvas id="graph2">` in the new page's container. The default canvas size is 300×150 and will visually overwrite the real `#graph` canvas (which is moved into the new container via `appendChild`).

Symptoms:
- Graph page renders as a small dark square instead of the full canvas
- DOM inspection shows BOTH `#graph` (1228×341, real) AND `#graph2` (300×150, orphan) in the same parent with `display: block`

**Fix**: remove the orphan `<canvas id="graph2">` from the new page's HTML. The existing JS that moves `#graph` via `appendChild` is sufficient — and add an explicit `window._graphResize` helper so the page switcher can call `resizeGraph()` after the canvas moves to its new container.

```html
<!-- WRONG -->
<div class="graphArea" id="graphArea2">
  <canvas id="graph2"></canvas>   <!-- orphan, hides the real one -->
</div>

<!-- RIGHT -->
<div class="graphArea" id="graphArea2">
  <!-- no canvas; switchPage moves the existing #graph canvas in -->
</div>
```

### PIL pixel analysis fallback when vision is down

When `vision_analyze` / `browser_vision` returns `Unknown Model` (provider config drift, model retirement, etc.) and the user sends screenshots you cannot see, use PIL pixel sampling to characterize the rendered output quantitatively:

- **Coverage check**: how many pixels are vivid vs background-only
- **Spread check**: which x/y bands contain content (e.g. graph nodes in a narrow band vs well-distributed)
- **Color distribution**: hue buckets to confirm multiple colors render (not just the dominant blue)
- **Aspect match**: confirm the canvas fills the container, not just sits at default 300×150

```python
from PIL import Image
import numpy as np
img = Image.open('/path/to/screenshot.png')
arr = np.array(img.crop((20, 160, img.width-20, 600)))
sat = arr.max(axis=2) - arr.min(axis=2)
bri = arr.mean(axis=2)
mask = (bri > 100) & (sat > 80)
print(f'vivid: {mask.sum()}/{mask.size} ({100*mask.sum()/mask.size:.2f}%)')
# Bin into a 40x40 grid to find hot regions
bin_size = 40
bins = {}
for y in range(arr.shape[0]):
    for x in range(arr.shape[1]):
        if mask[y, x]:
            bx, by = x // bin_size, y // bin_size
            bins[(bx, by)] = bins.get((bx, by), 0) + 1
hot = sorted(bins.items(), key=lambda x: -x[1])[:10]
```

Useful both as a diagnostic ("the graph has only 134 hot bins in 240 possible") and as before/after comparison ("was 1788 vivid pixels, now 13323"). Save cropped screenshots to `/root/.hermes/cache/screenshots/<descriptive-name>.png` so future sessions can compare.

Apply the same pattern to verify dashboard polish passes even when vision works — pixel coverage and color variety give more reproducible evidence than "looks better".

## Other useful patterns captured here
- For Dr. Sagar's SeaDash on `:9090`, the retro CRT amber-phosphor retrofit pattern (full CSS swap on a 220 KB single-file dashboard, atomic `<style>.*?</style>` regex replacement, six-theme-as-phosphor-colors, scanline/vignette/flicker stack, ASCII decorations, bracketed-button universal selectors, boot sequence). See `references/seadash-retro-crt-theme.md`.
- The atomic CSS block swap recipe (use a callable replacement to avoid backreference interpretation errors, never patch a 800+ line CSS block with `patch`). See `references/seadash-retro-crt-theme.md` and `software-development/large-file-editing` for the general pattern.

## Common pitfalls

1. **Calling a dashboard fixed because the shell loads.**
   The live JS runtime, websocket path, or API mutation may still be broken.

2. **Editing dist files without proving source is absent.**
   If source exists, dist-patching is the wrong default.

3. **Believing proxy and raw-port behavior are interchangeable.**
   They often diverge precisely where websockets/auth are involved.

4. **Stopping at token/bootstrap inspection.**
   On Hermes dashboard, `window.__HERMES_SESSION_TOKEN__` and a healthy `/chat` shell do not prove websocket admission is correct. If LAN/public clients still get `403` on `/api/ws` or `/api/events`, inspect backend websocket peer policy separately from frontend auth injection.

5. **Letting card view and table view drift apart.**
   Operator usefulness depends on parity across both surfaces.

5. **Unsafe localhost telemetry APIs.**
   A no-auth dashboard bound to loopback is still sensitive. Do not add `Access-Control-Allow-Origin: *` to JSON telemetry endpoints unless cross-origin reads are explicitly required and intentionally secured; any website open in the operator's browser can otherwise read localhost data via JS.

6. **Keeping duplicate render sources alive.**
   In monoliths, patch the active later definition too, or consolidate duplicated helpers.

7. **Over-layering rescue hooks after repeated failures.**
   Restore and reapply cleanly instead of accumulating fragile boot hacks.

7. **Confusing a stale launcher with a wrong port.**

### Compact settings/admin surfaces for lightweight monitor dashboards
For small low-overhead monitor apps, settings/logs/alerts pages often become the ugliest and least usable surfaces because every control is stacked vertically.

Good default recovery pattern:
- move save/apply/restart actions into a sticky top bar
- keep status chips in that same bar: save state, channel state, access summary
- replace long threshold forms with a compact table
- collapse access/network information into short rows rather than prose blocks
- keep notification cards dense: enabled state, saved-secret state, last-send state, fields, test button
- if the primary `Save` button sits outside the `<form>`, bind it with the HTML `form="..."` attribute or equivalent explicit submit wiring, then verify it in the live browser
- if adding log maintenance, prefer a real `Clear file` action that truncates the configured log on disk and then verify both the UI state and the file size

### One listener can legitimately serve localhost + LAN + Tailscale
When a dashboard binds `0.0.0.0:<port>`, do not describe localhost/LAN/Tailscale as separate dashboard instances. They are usually the same listener reachable via different addresses.

Operator-facing UI can make this clearer with a tiny access panel or `/api/access` summary that reports:
- localhost URLs
- preferred LAN URL
- Tailscale URL(s)
- whether a `cloudflared` process is present

### Stale-process verification after restart
If a browser still shows old UI or new routes 404 after you already edited the files, suspect a stale survivor process before re-patching.

Verification pattern:
- check the listening PID on the port
- compare it to the PID of the process you just started
- if the new process exited with `address already in use`, the old one is still serving traffic
- kill the stale listener, restart once, then re-check the port and re-open the page

This matters especially for lightweight Python/waitress/Flask dashboards where an older manually started process can outlive your restart attempt.

## SeaDash section-control polish lessons

When adding or repairing section management UI, follow `references/seadash-section-controls-presets.md`.

Key rules from hard-earned SeaDash fixes:
- Do not use native color `<select>` controls for section colors in the dark UI; use a custom swatch button + dark popover so text stays readable.
- Section color must tint the full header/border, not only a small one-side stripe.
- If section mode cycles `grid -> compact -> table`, the table-mode section header must keep all controls visible: Select, Move all, Pin, color picker, mode, Hide all.
- Hidden apps need a clear recovery path: `Unhide` plus a distinct `Remove` hidden-state action. Keep destructive `Delete` limited to manual apps.
- Offer simple section presets: Default, Host + Docker, No sections, plus saved custom presets.
- Add new layout/config keys to backend `DEFAULT_CONFIG` and example config, not only frontend JSON handling.
- Bump the service worker cache name after substantial single-file UI changes to avoid stale browser shells.

## Performance-cache pattern for Docker-backed dashboards

When a self-hosted dashboard builds its main payload from slow Docker calls (`docker ps`, `docker stats`, container probes), do not let normal dashboard requests block on Docker after the first warmup.

Preferred pattern:
1. Keep a short-lived in-memory Docker cache with age metadata.
2. Start a daemon background refresher at service boot and refresh every ~10s (tune per host).
3. Request path returns cached data immediately. If cache is stale, mark payload as `stale/refreshing` and schedule one background refresh under a lock instead of making every request wait.
4. Expose timing fields in the API (`docker`, `monitor`, `stats`, `total`, plus cache flags) and surface a compact UI indicator such as `api · refresh` when data is stale.
5. Cache empty/failure states briefly too, and on Docker command failure return stale data with a `refresh_error` if available rather than blanking the dashboard.
6. Suppress expected client-abort noise (`BrokenPipeError`, `ConnectionResetError`, `ConnectionAbortedError`) at the HTTP server `handle_error`/write boundary. Verify with forced aborted requests; do not rely only on code inspection.
7. Benchmark both cold and warm paths after restart. A good lightweight target for SeaDash-class pages is: static page <5ms, health <5ms, warm dashboard ~40-100ms, concurrent dashboard p95 under a few hundred ms on low-power hosts.

## Verification checklist

After writing the new shell, verify live in the browser, not just by reading code:
- [ ] Backed up the shipped asset(s) before invasive edits
- [ ] Verified backend/API surfaces separately from frontend rendering
- [ ] Patched the active runtime path, not only a dead/duplicate code path
- [ ] Checked syntax/build/tests where applicable
- [ ] Verified the live served bundle/process/proxy actually reflects the change
- [ ] Confirmed browser-visible runtime behavior, not just static HTML
- [ ] Confirmed operator-facing parity for cards/tables/links/alerts when relevant

## Support files

This umbrella keeps narrower, session-specific detail in `references/` files copied from the absorbed skills.

New reference for this class of failure:
- `references/lightweight-monitor-dashboard-notifications-and-logs.md` — lightweight monitor dashboard patterns: SQLite additive migrations for new metrics, no-dependency multi-series canvas charts, masked secret settings with blank-means-keep semantics, Discord webhook User-Agent workaround for Cloudflare 1010, Telegram 404 token diagnosis, and operator-focused Logs/Alerts pages.
- `references/standalone-calculator-trading-ux-upgrades.md` — compact trading-calculator UX upgrades: explicit price-source semantics, auto-fill-vs-manual Mark controls, DCA ladder defaults, derived PnL/ROI/liq-distance metrics, and browser-local named position saves.
- `references/liquidrisk-phase1-decision-support-bundle.md` — high-ROI phase-1 bundle for compact trading/risk dashboards: risk badges, portfolio summary cards, always-visible search/filter/sort, CTA-driven empty states, metric hierarchy/delta chips, and the verification pattern for backup empty/non-empty states.
- `references/standalone-calculator-saved-state-portfolio.md` — server-side named saves, reset-for-new-coin behavior, JSON import/export, portfolio aggregation from saved positions, and live verification/cleanup shape.
- `references/standalone-calculator-docker-persistence-and-temp-port-verification.md` — keep the operator-facing primary port stable, treat alternate test ports as temporary only, verify the live listener explicitly, and do not call saves/backups durable until the app data path is mounted outside the container.
- `references/standalone-terminal-universal-host-auth.md` — standalone browser terminal pattern for true universal host-shell mode, public/non-popup login auth, first-run/account-change username-password flows, session-cookie WebSocket auth, and host-vs-Docker public-readiness verification.
- See `references/restyling-to-telemetry-design-language.md` — pattern for bringing an older Hermes dashboard (purple/blue glassmorphic theme) up to par with `hermes-telemetry` design language while preserving legacy JS via a CSS class-name compatibility shim. Covers atomic `<style>` regex replacement, page-tab system, stat-card hero, table-driven panels, hook-without-calling-original pattern, and `systemctl --user restart` after edits.
- See `references/obsidian-vault-v2-enrichment.md` — V2 lazy-tab enrichment pattern for an already-restyled dashboard: switchPage() interception for lazy-load, tier-classified tag cloud, GitHub-style 365-day activity heatmap, localStorage pinned notes, quick-capture POST endpoint, the timezone-naive datetime pitfall that silently breaks "last N days" endpoints, and the `browser_console` verification pattern for lazy-loaded tabs (since `browser_snapshot` does not capture fetched content).
- See `references/hermes-dashboard-reboot-and-theme-inversion.md` — systemd reboot persistence checks, stale dashboard CLI flag crash loops, and foreground-alpha theme inversion for dark custom themes.
- `references/hermes-dashboard-route-auth-and-terminal-recovery.md` — split-port auth interpretation, ghost-route detection, lost-terminal recovery, and why source-level overlays beat `web_dist`-only edits.
- `references/hermes-dashboard-terminal-session-overflow-and-delete-parity.md` — old-terminal parity rules for visible-vs-stored sessions, `More`/`Previous` action menus, delete-vs-kill semantics, and prompt-first-row verification.
- `references/network-constrained-terminal-bootstrap.md` — host-vs-container network split, dependency-free terminal bootstrap, stdlib PTY milestone sequencing, and honest parity reporting under Docker package-install constraints.
- `references/single-container-standalone-terminal-app.md` — one-container terminal/dashboard app pattern: serve static UI and `/api/*` from the same Python/stdlib service, migrate away from frontend/backend sidecars, and verify via one public port.
- `references/stdlib-websocket-terminal-streaming.md` — add a minimal no-dependency WebSocket PTY stream to a standalone terminal app, with HTTP fallback, raw WS probe, browser verification, and honest non-xterm clone-status language.
- `references/vendored-xterm-standalone-terminal.md` — vendor xterm.js/xterm.css into a single-container static terminal app without npm builds, wire it to WebSocket PTY, and verify real xterm command execution plus history accounting.
- `references/rexterm-standalone-terminal-parity-repair.md` — concrete repair pattern for Rexterm-style Docker terminal apps when the shell chrome loads but xterm does not mount, the prompt is wrong, websocket banners pollute output, or the layout still does not feel like the Hermes terminal tab.
- `references/rexterm-standalone-terminal-followthrough-upgrades.md` — post-parity upgrade path for standalone terminal clones: real PTY resize, authoritative HTTP write path with WebSocket output, transcript export, launch profiles, honest scope limits vs tmux/Termius/Nexterm, and live verification shape.
- `references/hermes-dashboard-terminal-parity-polish.md` — terminal-tab parity fixes: darker full-bleed styling, wheel-vs-keyboard history separation, ANSI-clean history sync, stale-session cleanup, and header-clipping checks.
- `references/rexterm-header-settings-and-vendored-tmux-runtime.md` — header Settings-dropdown auth pattern for standalone terminals, single-line username row UX, and the rule to verify real terminal session creation alongside vendored tmux runtime resolution.
- See `references/hermes-telemetry-forensics-operator-upgrade.md` — SQLite-backed telemetry dashboard forensic/operator expansion: request forensics table, request drawer, tool analytics, error center, shared `tool_name` drill-down, and live browser verification pattern.
- `references/seadash-refined-css-overlay.md` — safe CSS polish pattern for SeaDash: append a second `<style>` block instead of replacing the original 822-line block. Preserves the 189 original class definitions, fixes modal-architecture, restores `.auth-overlay` rules, and includes the end-to-end verification pattern (modal open/close + critical function check + visual confirmation).
- `references/seadash-compact-full-rewrite.md` — full SeaDash rewrite pattern when the current single-file app is too messy: keep dependency-free Python + vanilla UI, preserve host/Docker/manual-app controls, verify the live `/api/dashboard` schema, bump service-worker cache, and report non-git roots honestly before any requested push.
- `references/seadash-nested-layered-card-pattern.md` — Homarr-style "outer card + inner panel" technique via `::before` pseudo overlay with `pointer-events: none`, plus the `getComputedStyle(el, '::before')` browser-console check that confirms the pseudo-element actually rendered. The "make my dashboard beautiful, this looks ugly" pattern when the user shows a reference card screenshot.
- `references/seadash-card-cleanup-section-colors.md` — SeaDash cleanup semantics: one-click `Close` hides any app, `Delete` is manual-app-only with confirmation, section color strips/dropdowns, layout export support, and headless Chromium verification fallback when browser automation is blocked by a confirm dialog.
- `references/seadash-10x-operator-dashboard.md` — clean SeaDash 10x rewrite pattern: dependency-free frontend, section/tag/hidden/bulk/layout features, port scanner/import, safe Docker bulk API, logo/favicon asset generation, live verification, and private GitHub repo hygiene.
