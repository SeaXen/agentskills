---
name: feature-building
description: Build polished full-stack web app features one at a time, with live verification between each, then ship incrementally via single commits. Use when adding new features to an existing web app — especially dashboards, data-driven UIs, or tools where each feature has a backend API + frontend page + nav integration.
---

# Feature Building

The user expects every feature to land polished — design, performance, and integration breadth in one pass. **MVP-then-add iteration is explicitly NOT the desired pattern.** Each feature must be production-ready, verified live against the running app, and pushed before moving to the next.

## The loop (apply to every feature)

1. **Scope check first** — `search_files` / `grep` the codebase for existing implementations. Re-discovering wired features wastes the session and surprises the user.
2. **Build** — backend API + frontend page + types + nav integration + cross-links from related pages. Touch everything that needs touching in one pass; don't defer "polish" to a follow-up.
3. **Verify live** — `tsc --noEmit`, `npm test`, `npm run build`, `curl` the endpoints, check rendered pages. See standards below.
4. **Treat fresh-verification warnings as hard gates** — if Hermes or the workspace warns that changed files lack fresh passing evidence, rerun the relevant verification commands in the current turn before claiming completion, even if you already ran them earlier in the session.
5. **Clean up test artifacts** — delete any test bots / trades / wallets / exchanges created during verification BEFORE the commit. Polluting the live DB is a trust violation.
6. **Commit + push** — single commit per feature (or one bundle for a related batch), descriptive message with verification numbers. Before commit: unstage ephemeral dirs (`git reset -- test-results/` after Playwright); never commit `.env`.
7. **Report** — terse table with live numbers (HTTP code, size, time, content-type) plus the fresh verification commands that passed. No narrative.

## Live verification standards

**"Claimed done" is not done.** Every endpoint must be hit with curl, every page must be curl'd and its size/time reported, every destructive action must be exercised against a confirm-protected path. The user has stated this preference multiple times — it is the single biggest behavioral signal in the memory.

### Per-feature verification checklist

- `npx tsc --noEmit` returns 0 errors
- `npm test` passes (typically 60+ tests; show the count)
- `npm run build` produces clean output (show the new page sizes)
- New pages compile to reasonable size (target: <5KB page-specific JS)
- New API endpoints return 200 (or expected error code with valid body)
- New UI elements actually appear in the rendered page (curl the page, grep for the new text)
- Test data created during verification is cleaned up before commit
- If the commit path runs pre-commit hooks (`lint-staged`, prettier, eslint --fix, etc.), rerun the relevant test/build commands **after the commit or after staging hooks mutate files**. Do not assume pre-hook verification still applies to the post-hook tree.
- For frontend test files that depend on `localStorage` / `sessionStorage`, verify the test harness itself before blaming app logic. If the runtime-provided storage object is incomplete, add a minimal in-memory storage shim in the test/setup layer so `getItem`, `setItem`, `removeItem`, `key`, `length`, and `clear` all exist, then rerun the targeted test file.

### Monorepo verification pitfall

When verifying a package inside a monorepo, do not assume package-local tests/builds are self-sufficient.

Required order when the package imports a sibling workspace package:
1. Build the dependency workspace first (for example `packages/shared`) if the package expects built `dist/` artifacts.
2. Run tests from the package directory using the package-local relative path to the test file — do not pass a repo-root path from inside the workspace.
3. If the test fails before assertions run (for example storage/window setup dies in `beforeEach`), report it explicitly as a **test-harness/environment failure**, not as a feature regression.
4. Keep build/lint evidence separate from test evidence; a passing build does not erase a broken harness.

This avoids false negatives like "module not built" or malformed Vitest target paths, and it keeps PR verification honest when the feature builds but a test harness is independently broken.

### Container deploy pattern

`docker compose restart <service>` does NOT pick up a new image. The correct sequence:

```bash
docker build -t <service>:test .              # foreground
docker tag <service>:test <service>:latest     # foreground
docker compose up -d --force-recreate --no-deps <service>  # background=true
sleep 5 && curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:PORT/
```

Then verify each new endpoint with curl. If a 404 comes back, the container is still on the old image — rebuild + recreate again.

For dashboards that add a **local analytics SQLite** (e.g. AceRoute `aceroute.db` synced from Hermes `state.db`):

- Add a **named Docker volume** for the writable DB path (`aceroute-data:/app/data`), not only bind-mounts for read-only upstream data.
- Mount Hermes home **read-only** when the collector reads `state.db`.
- Copy any new Python module into the image in `Dockerfile` (`COPY ... aceroute_tools.py`).
- Do not commit the live DB file; keep `data/.gitkeep` only.
- Lazy-load heavy secondary nav tabs (Tools/Skills/Journey) on first open so the default Search landing page does not pay sync/parse cost on every refresh.
- Mount **`./static:/app/static:ro`** when static is not bind-mounted — otherwise UI edits on host do not appear until image rebuild; verify with `curl` on served `/`.
- If you add a new backend Python module, update the Dockerfile `COPY ...` list in the same pass. A missing module will only surface after container recreate as `ModuleNotFoundError`, even when local `py_compile` succeeded.
- Hermes `state.db` analytics tabs: `references/hermes-state-analytics-dashboard.md`.
- Alert/incident workflow reference: `references/alert-center-workflow.md`.

### When browser automation stalls

If `browser_navigate` returns a page snapshot with empty DOM or the `evaluate` expression returns null, fall back to `curl` + `grep` on the rendered HTML. The browser layer can be stale (stale service worker, cached headless browser, etc.) and curl is the source of truth.

## Crypto risk analytics feature pattern

When adding a trader-facing crypto risk feature (portfolio heat, concentration, leverage-stacking, liquidation proximity), avoid burying the logic inside a page or route.

Preferred structure:
1. Put the scoring/math in a pure helper under `lib/crypto/`.
2. Add a read-only API route that aggregates live positions + balance and returns both raw metrics and human-readable insights.
3. Add a dedicated page with posture/KPI summary, breakdown table, and a concise risk-read panel.
4. Wire it into nav in the same pass so it is discoverable immediately.
5. Add `?demo=1` support for safe verification when live exchange state is empty or too risky to manipulate.
6. Add unit tests for the pure helper, not just page/route smoke coverage.

Verification pitfall:
- For thresholded risk metrics like `nearLiqCount`, do not guess expected test values from memory. Run the real helper logic, inspect the returned counts, then set assertions to match the implemented liquidation-distance rule. In this class of feature, wrong test expectations are more likely than broken math.

## TypeScript patterns

### Type widening when adding a variant

When adding a new variant to an existing union (e.g., `"dark" | "light"` → `"dark" | "light" | "system"`):

1. Widen the type in the central types file (`lib/types.ts`, `lib/settings.ts`, etc.)
2. Add the variant to all consumers in one pass (Settings UI, applicator, topbar, etc.)
3. Existing persisted values default to the existing default (no migration needed — string settings store handles it)
4. Don't introduce back-compat shims; the union widening is the API change

### Discriminated union narrowing in JSX

For shared fields across union variants, use `as any` for read-only display:

```tsx
{(t.config as any).side ?? (t.config as any).mode}
```

For variant-specific fields, use explicit `kind` checks. Avoid complex narrowing functions for read-only display code — the `as any` cost is paid once at the JSX boundary, and the union is the actual safety guarantee at the API boundary.

### Rate-limited bulk operations

For destructive bulk actions (close-all, cancel-all, delete-all):

- Require a **typed confirm string**, not a boolean. `confirm: "CLOSE_ALL_POSITIONS"`, not `confirm: true`. The string is unguessable in casual use.
- Rate limit to 5/min via `withRateLimit({ max: 5, windowMs: 60_000 })`
- Audit log every call (`actor`, `action`, `target`, `details`, `ip`)
- UI button only appears when there are items to act on
- UI confirm step (typed string in a `prompt()`) before the API call

## Cross-link pattern

When adding a new page that complements existing ones, link from the existing pages — don't just add a nav entry. Example: a `/strategy-templates` marketplace should be linked from `/dca` and `/grid` with a "From Templates" button. This makes the feature discoverable from where the user is already working, without adding nav clutter or requiring the user to remember a new tab.

## One-pass polish expectations

For every feature, ALSO do:

### UI/theme/dashboard tasks — reference-first rule

When the user provides a reference site, screenshot set, or raw HTML/CSS mockup, treat that artifact as the visual source of truth instead of freehand styling.

Required workflow for this class of task:
- Extract the exact palette, background layering, panel colors, border colors, text hierarchy, and chrome behaviors from the provided reference.
- If the user says "match this" and then complains about dullness or mismatch, assume the problem is not just tokens — audit structure too: sidebar width, collapse affordances, search placement, ticker strips, utility rails, widget chrome, and nav rhythm.
- Prefer additive theme variants and shared chrome components over one-off page hacks.
- Verify actual behavior live, not just code presence: collapse/expand must change width/state, search must return results, ticker strip must show live symbols, nav groups must open/close, and the intended theme must be active in computed styles.
- If a live check shows one shell element still using an old color (for example sidebar shell/background), patch that exact shell/container explicitly rather than assuming global CSS vars propagated everywhere.

See also `references/admin-dashboard-chrome.md` for the distilled admin-dashboard matching checklist from the TradingX session.

- **Nav integration** — add to `TOPBAR_NAV` (or equivalent) if it's a primary destination
- **Cross-links** from related pages (see above)
- **Settings integration** if the feature has user-configurable behavior
- **Empty / loading / error states** — every new page needs three-state handling
- **Rate limits** on every POST/PUT/DELETE endpoint
- **Audit log** on every destructive action
- **Security** — URL scheme whitelisting at render boundary, AES-256 for secrets, withdrawal block by default

## Reference-driven UI/theme work (important)

When the user provides screenshots, a live site, or source HTML/CSS as the target look, treat that as the spec — not loose inspiration.

Required loop:
1. Extract concrete tokens from the reference first: background, panel/card, border, primary text, muted text, accent, radii, spacing, and sidebar/header structure.
2. Compare the live app against the reference visually and by computed styles. Do not stop at "theme variables changed" if the rendered UI still looks off.
3. Fix root causes, not only one page: hardcoded colors, missing utility variants, stale compatibility classes, wrong defaults, missing controls.
4. Verify live with both DOM + rendered checks. Minimum for theme/layout work: computed `body`/card/sidebar colors, sidebar widths, default mode, collapse/expand behavior, search-result visibility, and ticker/nav-group interaction if those controls were added.
5. If the user asks for a reference layout feature (e.g. sidebar default, slimmer width, collapse/expand), ship the actual control — not just colors.
6. When the user likes an older visual direction, prefer adding a separate theme variant (for example a restored legacy dark-green palette) instead of silently overwriting the current dark/admin themes. Preserve the newer variants and expose the legacy look as an explicit option.

User preference lesson: this user wants close visual matching and clear contrast, not approximate "inspired by" styling. If the result is dull, low-contrast, or missing obvious controls from the reference, it is not done.

## WebSocket-first live market upgrade pattern

When a user asks for trader-grade "real-time" behavior, do not substitute webhook or 1s REST polling. The correct path is a **narrow first-wave WebSocket rollout** with REST fallback.

Recommended rollout order:
1. top ticker strip
2. trade page selected-symbol live ticker
3. watchlist live prices
4. open-position mark price + unrealized PnL overlay
5. orders page live price + distance-to-market
6. mini order book / spread awareness / stale timer / reconnect indicators

Architecture rules:
- **WebSocket** = live price, ticker, spread, mini order-book, mark-price overlays.
- **API** = control plane, orders, balances, history, positions snapshot, analytics, exports, health, fallback bootstrap.
- **Webhook** = signals/notifications/callback events only; never use it as the main continuous price transport.
- Start narrow. Do not try to stream the entire app in one pass.
- Keep existing API/polling pages unless a concrete latency benefit exists.

Implementation pattern that worked:
- Build one shared browser-side stream helper instead of many page-local sockets.
- Seed each symbol from `/api/market?symbol=...` first, then overlay stream updates.
- Merge Bybit `delta` frames into the last `snapshot`; treating deltas as full rows corrupts fields like `last/high/low/volume`.
- Add a stream-status surface (`LIVE / FALLBACK`) driven by `lastMessageAt`, socket readyState, and reconnect attempts.
- Expose `last tick Xs ago` on the trade-critical surface so stale data is visible, not implicit.
- For positions, recompute unrealized PnL from streamed mark price in the UI while keeping API snapshots as the base state.
- For open orders, show current live price and simple distance-to-market (% away from the resting order).
- For trade entry, a lightweight level-1 mini order book is enough for a first pass; avoid heavy depth visualizations unless explicitly requested.

Verification pattern for this class of work:
- Verify the upstream exchange socket directly from terminal/Node, not just the browser DOM.
- Confirm you receive both `snapshot` and ongoing `delta` frames.
- Verify the live page text changes over time from the same open page, not just initial load.
- If a browser resource API does not show `wss://` entries, do not treat that as a blocker; use direct socket probes plus live DOM checks.
- When there are no open orders or positions in the live environment, report that structural/live UI verification passed but row-level dynamic behavior could not be visually proven because the dataset is empty.
- If the user asks for large multi-phase trader upgrades in one go, do NOT promise to 'complete everything at once' when the remaining work spans exchange-private account streams, risk math, alerts, simulator, and mobile polish. Push back and collapse the work into 1-3 larger verified waves instead. For this user, the right first remaining wave after public-market WebSocket rollout is a DB-backed in-app execution event center (fills, position changes, milestones, signals, alerts) built on top of the existing `notify(...)` pipeline before attempting adapter-specific private account WebSockets.
- For trading UX with empty live datasets, add a safe page-scoped `demo verify` mode via explicit API query flags (`?demo=1`) so orders/positions UIs can be proven without touching real exchange state. Label it clearly as simulation-only and keep it isolated from real writes.
- When shell-side token interpolation is unreliable during API checks, prefer browser-authenticated fetches for `/api/*` verification instead of claiming the route is broken.

Pitfalls:
- Browser snapshots may truncate below-the-fold content; extract `document.body.innerText` or targeted DOM state to verify live markers like `Spread`, `Signal`, `last tick`, `Mini order book`, and new table headers.
- Do not claim the live stream path is done if field mapping is wrong even when build/tests pass; a live parser mismatch is a failed rollout until fixed.
- Do not store or repeat any runtime token/cookie values while verifying the live app.

Support file:
- See `references/tradingx-websocket-phase-rollout.md` for the concrete TradingX rollout lessons, verification examples, and phase sequencing.

## Live-market chrome polling guidance

For dashboard chrome features like a top ticker strip, 1-second polling is usually the wrong implementation even if the user says crypto speed matters.

Rules:
- 10–30s polling is a reasonable compromise for a non-trading-critical header ticker.
- 1s polling across multiple symbols multiplies browser work, server hits, and upstream API churn quickly; call this out plainly instead of pretending it is free.
- If the user truly needs near-real-time behavior, prefer a websocket/streaming path over 1s REST polling.
- When discussing the trade-off, report actual live container CPU/RAM numbers first, then explain the relative request multiplier (for example 60s → 10s → 1s).

## WebSocket-first trader UI upgrades

When the user wants a crypto trading surface to feel faster or more profitable, the right improvement path is transport + execution awareness, not just cosmetic refreshes.

Rules:
- For real-time price updates, use WebSocket, not webhook, and do not frame webhook as a substitute for API or stream transport.
- Keep API routes for control-plane and snapshot work: orders, balances, history, positions snapshots, settings, analytics, sync jobs, exports, health.
- Keep webhook usage limited to true event callbacks: inbound signals, outbound notifications, external integrations.
- Start narrow on the first WebSocket rollout: migrate the highest-value surfaces first (ticker strip, selected-symbol trade ticket, watchlist rows, open-position mark prices) before touching the whole app.
- Treat exchange stream payloads as incremental state, not guaranteed full snapshots. If the upstream sends `snapshot` then `delta`, merge deltas into cached rows before computing derived fields like last/high/low/volume.
- Shared browser stream client is preferred over per-component socket sprawl. Fan out to multiple UI consumers from one connection when possible.
- Add explicit stream-state UI, not silent failure: `LIVE / FALLBACK`, reconnect/stale notice, and ideally a `last tick Xs ago` counter.
- For trader-facing phase upgrades, the most valuable order is usually:
  1. live ticker + spread
  2. live watchlist prices
  3. live mark price + unrealized PnL on positions
  4. mini order book / spread-quality hints
  5. live open-order distance to market
  6. stale/reconnect alerts
  7. liquidation-distance visibility
- Verification must include both upstream and UI evidence when feasible:
  - direct terminal subscription to the upstream WebSocket to inspect real payload shape
  - browser/DOM proof that the on-page value changes over time, not just on first render
  - fresh `tsc`, tests, build, redeploy
- If the live app has no open orders or no open positions, say that plainly. Verify structure and wiring, but do not overclaim row-level live behavior you could not visually observe.
- Build warning pattern to remember: Next.js build may print `ESLint must be installed...` while still completing successfully. Report it as a non-blocking build note, not as a failed build.

See also `references/websocket-trader-ui-rollout.md` for the concrete rollout pattern and verification checklist from the TradingX session.

## WebSocket-first phase rollout for trader UIs

When the user wants a crypto app to feel more trader-grade, do not jump straight from polling to a full app-wide streaming rewrite. Use a narrow, high-value rollout first, then verify live before expanding.

Recommended sequence:
1. Migrate the highest-latency-sensitivity surfaces first:
   - header / top ticker strip
   - trade ticket selected-symbol live ticker
2. Keep the existing REST endpoint as bootstrap + fallback instead of deleting it.
3. Add explicit UI stream-state signalling early (`LIVE` / `FALLBACK`) so stale data is visible.
4. For phase 2, extend streaming to:
   - watchlist rows
   - open-position mark price
   - open-position unrealized PnL
   - trade-page spread / spread-quality hint
5. Leave slower-changing or snapshot-oriented surfaces on API polling unless there is a clear trading benefit:
   - balances
   - orders history
   - portfolios
   - analytics
   - sync jobs

Implementation pitfalls:
- Bybit ticker streams send one full `snapshot` followed by partial `delta` frames. Do NOT treat every delta as a full row; merge delta fields into the last snapshot or you will zero/mix fields like `last/high/low/volume`.
- Verify live movement, not just initial render. A page showing one correct value is insufficient; sample the same live DOM twice with a delay and confirm `Last` changes over time.
- Browser performance APIs may not expose `wss://` entries reliably. If you need proof of the live socket, verify it from the terminal against the upstream WebSocket endpoint and separately verify changing values in the page DOM.
- For positions streaming, if there are no open positions live, state that the path is structurally deployed but not visually proven against a real row yet. Do not overclaim.
- Reference: `references/websocket-market-rollout.md` for the concrete phase-by-phase pattern and verification checklist.

## User preferences (terse style)

- **One-pass polish** — "10/10 across features + design + performance" is the **direction**, never the **claim**. Build to that bar; never self-grade it.
- **Terse responses** — table of verification numbers, not narrative
- **Live verification required** — every claim must be backed by measurements
- **No MVP iteration** — features ship polished, not "first cut, then improve"
- **Casual chat fragments OK** — lowercase, short, no formality
- **Explicit constraints are absolute** — "no need tax features" means don't try to sneak them back later
- **Pair with shippable artifacts** — private GitHub repo + pro README for new users
- **Honest self-assessment is non-negotiable** — see the section below; this is the most common place sessions damage trust

## Honest self-rating (do not skip this)

When the user asks "is it 10/10?" or "so my app is perfect now?", treat the question as a calibration test, not a compliment fishing for confirmation. The correct response is **always a sober scorecard with named gaps**, never "yes, it's 10/10".

Hard rules:

- **Never declare 10/10**, not after a wave of fixes, not when tests are green, not when the user seems to want a confident answer. 10/10 is a structural claim over features + security + perf + reliability + tests + accessibility + ops + docs, and almost nothing in a single coding session covers all of that.
- **"Make it 10/10" is a direction, not an achievable one-shot.** Acknowledge it, plan the next wave, execute, then re-score honestly. Do not announce "done — it's 10/10" at any point.
- **Round down, not up.** If you're tempted to claim 9.5 because the user seems frustrated, claim 8.8 with a gap list instead. A verified 8.8 + gap list is more useful than a claimed 9.5 the next wave will reveal as 8.
- **Avoid:** "It's now 10/10" · "All sectors perfect" · "Production-ready perfection" · "Nothing left to fix".
- **Prefer:** "Better. Honest score: X. Gaps remaining: A, B, C." · "Not 10/10 yet. What I fixed: …. What still blocks it: …" · "Stronger, but I won't claim perfect — here's the real scorecard."

Pattern for the reply after a polish wave:

```
What I did this wave: …
Verified: typecheck ✅ · tests N/N ✅ · build ✅ · live N pages ✅
Honest rating now: ~8.9 overall. Not 10/10.
What still blocks 10/10: <real structural gap list>
Next wave I'd do: <ranked options>
```

If the user explicitly says "stop overclaiming" / "be honest" / "don't say 10/10" — they are correcting this exact behavior. Update mid-session and stay corrected for the rest of the conversation.
- **Never claim literal perfection without proof** — when the user says "make it 10/10" or "perfect app", treat that as a push for maximum quality, not permission to overclaim. Keep improving aggressively, but explicitly distinguish verified improvements from unresolved gaps.
- **Use direct yes/no on quality claims** — when asked "is it 10/10?" answer yes or no first, then justify. Do not soften it with marketing language.

## Quality-claim discipline

When a user asks for "10/10", "perfect", or "all sector" quality:

1. Treat it as a mandate to keep improving, not as a reporting shortcut.
2. Do the real work: verify build, tests, live behavior, and measurable performance paths.
3. Do **not** say the app is 10/10 unless the remaining gaps are genuinely closed and you have evidence for the claim.
4. If the app is materially better but still short of perfect, say so plainly: "better, verified, not 10/10 yet".
5. Name the exact blockers still preventing a 10/10 claim — warnings, missing audits, unresolved architecture debt, absent E2E/security/accessibility coverage.
6. Prefer an honest score range over fake certainty when some sectors were not fully audited.

This user explicitly prefers blunt honesty over hype. Saying "no" to an inflated quality claim is the correct behavior.
## Polish pass pattern (Wave C)

When the user asks for a "polish wave" or "wave C" after core features ship, treat it as a coordinated quality/observability/testing sweep — not piecemeal fixes. The pattern:

1. **Code quality tooling** — install ESLint/prettier if missing, fix all violations in one pass
2. **Observability surface** — add a `/diagnostics` or `/health` or `/debug` page exposing runtime state (WebSocket health, API counters, stale data age, etc.)
3. **Test coverage for fragile paths** — extract and unit-test pure functions that were previously only exercised via E2E (parsers, calculators, formatters)
4. **Demo/simulator mode** — add `?demo=1` query param support to key endpoints so the UI can be stress-tested without live data or API keys
5. **Mobile/responsive audit** — wrap tables in `overflow-x-auto`, check grid breakpoints, ensure nav scrolls horizontally on small screens
6. **Security/header pass** — add safe global headers (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, narrow `Permissions-Policy`) and harden every `target="_blank"` link with `rel="noopener noreferrer"`
7. **Accessibility semantics pass** — add missing dialog semantics (`role="dialog"`, `aria-modal`, `aria-labelledby`), explicit button types, and aria-labels for icon-only or terse action buttons
8. **Operator diagnostics surface** — for self-hosted dashboards with caching, background refresh, or multiple heavyweight tabs, add a dedicated diagnostics page plus a backend summary route (for example `/api/diagnostics`) that exposes health/uptime, cache state, warm coverage, per-endpoint timings, slowest paths, stale keys, and warning conditions. Include an explicit cache-warm/refresh control when the app has a materialized cache layer.
9. **Full verification sweep** — typecheck, tests, build, deploy, live verify, commit, push

### Diagnostics + alerts workflow pattern for dashboard apps

When the app is already functionally rich and the next best pass is quality/trust/perf visibility, do not keep piling on passive widgets. Add an operator-facing diagnostics page first, then a persisted alerts workflow page when the user wants actual incident handling.

Recommended diagnostics payload:
- health / uptime
- cache TTL / refresh interval / coalesce window / LRU size-capacity
- cache row count / stale keys / bad refresh statuses
- upstream state signature summary
- per-endpoint probe timings with payload size, row count, and cache mode
- slowest-path table

Recommended diagnostics UI:
- compact KPI summary row
- insight chips for status / TTL / refresh cadence / cache rows
- stack lists for endpoint timings, cache health, warnings, runtime/security
- slowest-path table
- explicit warm button wired to the cache refresh endpoint

After diagnostics exists, the next operator-grade wave is a persisted alerts center:
- synthesize current alerts from existing APIs instead of adding fresh collectors first
- persist alert state/history in the app-local SQLite DB
- separate `alert_key` (instance) from `rule_key` (family/mute key)
- expose one center route plus `ack`, `mute`, and `unmute` mutation routes
- verify ack/mute/unmute with live round trips against the running app before claiming completion

Verification rule:
- verify the diagnostics route itself with curl
- verify the served HTML contains the new nav target, page container, and cache-busted asset
- verify response headers live with `curl -I`, not by code inspection alone
- if browser automation is flaky, treat curl/API/source checks as the source of truth and say the browser runtime failed rather than blaming the app

Do this in ONE session, ONE commit. Don't stop mid-wave and wait for user re-engagement; the user expects momentum through the entire checklist.

### Final polish verification detail

For the security/accessibility portion of a polish wave, do not stop at code inspection.

Required checks:
- Re-run `typecheck`, `build`, and browser/E2E smoke coverage after the polish edits.
- Verify security headers on a live response with a real request (`HEAD` or `GET`), not just by pointing at `next.config.*`.
- If you harden modal/button semantics, make sure existing smoke tests still pass on the routes that render those widgets.
- Prefer small, low-regression fixes in this phase; a polish wave is not the time for large architectural rewrites unless the user explicitly asks for them.

## Anti-patterns to avoid

- Re-discovering features that are already wired (always search the codebase first)
- Leaving test data in the database after verification
- Claiming "done" without curl/browser verification
- Ignoring a workspace/system warning that fresh verification evidence is missing for edited files
- "Iterative" approach: build small → ship → expand (the user wants one-pass 10/10)
- Verbose explanations of what was done (let the table speak)
- Using `docker compose restart` expecting it to pick up a new image
- Using `docker compose restart` expecting it to reload `.env` files — `restart` keeps original env; use `up -d --force-recreate` instead
- Using `docker compose up -d --force-recreate --build` expecting it to always pick up file changes — the `COPY . .` layer can still be cached; use `build --no-cache` if `docker exec` shows old code
- Adding HTTP Basic Auth to internal dashboards — browser native auth prompt re-asks on every refresh and is universally hated by users; use session-based login or skip auth for LAN-only tools
- Delegating feature work to subagents (do it inline; the user wants to see the loop, and the live verification per step wouldn't be visible across subagent boundaries)
- Re-running `tsc` / `npm test` / `npm run build` in a tight loop when one fresh run covers everything
- **Using `write_file()` with `read_file()` output that still has line numbers** — `read_file()` returns `"line_num|content"` format; if you feed that directly to `write_file()`, you corrupt the file with `123|const foo = ...` on every line. Always strip the line-number prefix first, or use `patch()` instead for surgical edits
- Stopping mid-polish-wave and waiting for user nudge — when the user says "continue complete build wave C", they expect you to finish the entire checklist autonomously, not pause after each item

## When to use this skill

- Adding a new page to an existing web app
- Adding a new backend API endpoint + its UI
- Bulk operations, templates, marketplaces, settings panels
- Anything that needs to be live-verified before commit

## When NOT to use this skill

- Greenfield app design (use `writing-plans` instead)
- Code cleanup / refactor of existing code (use `simplify-code` instead)
- Pre-commit review of staged changes (use `requesting-code-review` instead)
- Debugging an existing bug (use `systematic-debugging` instead)

## References

- `references/aceroute-diagnostics-page.md` — diagnostics page/API pattern for AceRoute-class self-hosted dashboards
- `references/hermes-state-analytics-dashboard.md` — Hermes `state.db` FastAPI analytics (AceRoute-class)
- `references/icalendar-export.md` — RFC 5545 .ics generation with ET→UTC + DST detection
- `references/canvas-candlestick-chart.md` — DPR-scaled time-series chart with overlay markers, designed for trade replay
