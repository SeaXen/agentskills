---
name: hermes-dashboard-development
description: "Patterns and workflows for building dashboards for Hermes Agent plugins — serve.py, index.html, API endpoints, hot-reload, file watchers"
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [hermes, dashboard, plugin, serve, hot-reload, watchdog]
    related_skills: [hermes-agent, github-operations]
---

# Hermes Dashboard Development

## Overview

Class-level skill for building and extending web dashboards for Hermes Agent plugins. Covers the `serve.py`/`index.html` pattern used by `hermes-telemetry` and similar plugins.

## When to use

- Building a new dashboard for a Hermes plugin
- Extending an existing plugin dashboard (adding endpoints, UI, charts)
- Adding hot-reload/file-watcher capabilities
- Implementing time-range filtering across API endpoints

## Core patterns

### 1. Dashboard server (`serve.py`)

- **Stdlib-only HTTP server** (`http.server`) — no external deps
- **Per-thread SQLite connections** via `threading.local()` + WAL mode
- **Time window helper** — single `_since_clause(window_hours, col)` handles all endpoints:
  - `window_hours=0` → "all time" (returns `"1=1"` no filter)
  - `window_hours>0` → `"col >= datetime('now', '-N hours')"`
- **API endpoints** return JSON, CORS-enabled (`Access-Control-Allow-Origin: *`)
- **Static file serving** from same directory (index.html, assets)
- **Auto-refresh** via client-side `setInterval(loadAll, 30000)`

### 2. Time range selector (frontend)

```html
<select id="windowSelect" onchange="loadAll()">
  <option value="24">Last 24h</option>
  <option value="168">Last 7 days</option>
  <option value="720">Last 30 days</option>
  <option value="2160">Last 90 days</option>
  <option value="0" selected>All time</option>  <!-- default = all time -->
</select>
```

**All API endpoints** must accept `?hours=` param and pass to their handler.

### 3. Modal form pattern (for config editing)

- Hidden modal overlay (`.modal-overlay` + `.modal`)
- Form fields with validation
- `fetch('/api/endpoint', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify(payload)})`
- Error display in modal (`.modal-error.show`)
- On success: `closeModal(); loadAll()` to refresh

### 4. File watcher for hot-reload (plugin side)

Add to plugin's budget/config module:

```python
# budget.py
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileModifiedEvent

_budget_observer = None
_budget_watcher_started = False

def start_budget_watcher():
    global _budget_observer, _budget_watcher_started
    if _budget_watcher_started:
        return
    try:
        class ConfigHandler(FileSystemEventHandler):
            def on_modified(self, event):
                if not event.is_directory and event.src_path.endswith("budget.yaml"):
                    logger.info("budget.yaml modified — hot-reloading")
                    reload_config()
        path = _budget_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        _budget_observer = Observer()
        _budget_observer.schedule(ConfigHandler(), str(path.parent), recursive=False)
        _budget_observer.daemon = True
        _budget_observer.start()
        _budget_watcher_started = True
    except Exception as exc:
        logger.debug("watcher unavailable: %s", exc)

def stop_budget_watcher():
    global _budget_observer, _budget_watcher_started
    if _budget_observer:
        _budget_observer.stop()
        _budget_observer.join(timeout=2)
    _budget_watcher_started = False
```

Call `start_budget_watcher()` in plugin's `register(ctx)` function.

**Dependency:** `watchdog>=3.0` in `pyproject.toml`

### 5. Token breakdown API

```python
def api_token_breakdown(window_hours=24):
    return _one(f"""
        SELECT SUM(tokens_in) AS tokens_in,
               SUM(tokens_out) AS tokens_out,
               SUM(cache_read_tokens) AS cache_read_tokens,
               SUM(cache_write_tokens) AS cache_write_tokens,
               SUM(reasoning_tokens) AS reasoning_tokens,
               COALESCE(SUM(tokens_in) + SUM(tokens_out) + SUM(cache_read_tokens) + SUM(cache_write_tokens) + SUM(reasoning_tokens), 0) AS total_tokens
        FROM llm_calls WHERE {_since_clause(window_hours, "ts")}
    """)
```

Frontend renders as table with colored indicators and percentages.

### 6. Per-model and per-day token usage tables

Use when the user wants deeper token accounting beyond the top summary.

### 7. Provider cost + token breakdown

Use when call-count-only provider charts stop being useful.

**Add `GET /api/providers?hours=` that returns more than calls:**
- `provider`
- `total_calls`
- `real_calls`
- `estimated_calls`
- `tokens_in`
- `tokens_out`
- `cache_read_tokens`
- `cache_write_tokens`
- `reasoning_tokens`
- `total_tokens`
- `cost_usd`
- `avg_cost_per_call`

**SQL shape**
- query from `llm_calls`
- `COALESCE(SUM(...), 0)` every token/cost field individually
- sort by `cost_usd DESC, total_tokens DESC, total_calls DESC`

**Frontend pattern**
- render as a table, not just doughnut legend data
- make provider rows clickable for drill-down (`setDrilldown({provider: ...})`)
- keep the lightweight provider doughnut on Home, move the detailed provider table to Breakdown

### 8. Cache efficiency stats

Use when cache-read totals exist but the user wants operational meaning.

**Add `GET /api/cache-efficiency?hours=`**
- overall fields:
  - `api_calls`
  - `sessions`
  - `tokens_in`
  - `cache_read_tokens`
  - `calls_with_cache`
  - `sessions_with_cache`
  - `cache_hit_share_pct`
  - `cache_calls_pct`
  - `estimated_cache_saved_tokens`
- per-model rows:
  - `model`
  - `api_calls`
  - `sessions`
  - `tokens_in`
  - `cache_read_tokens`
  - `calls_with_cache`
  - `cache_hit_share_pct`
  - `cache_calls_pct`
  - `cost_usd`

**Interpretation convention used in this dashboard**
- `cache_hit_share_pct = cache_read_tokens / (tokens_in + cache_read_tokens)`
- `estimated_cache_saved_tokens = cache_read_tokens`

This is deliberately simple and stable — useful for dashboard ops even if it is not a perfect semantic cache-hit metric.

### 9. Drill-down investigation flow

Use when aggregate tables/charts are no longer enough and the user needs to know which exact sessions caused a spike.

**State pattern**
- keep a small frontend object like `currentDrilldown = {day, model, provider, platform, status}`
- expose helpers:
  - `setDrilldown(filter)`
  - `clearDrilldown()`
  - `hasDrilldown()`
  - `drilldownLabel()`
  - `buildRunsQuery(hours, limit)`

**Backend pattern**
- extend `GET /api/runs` so it accepts optional filters:
  - `hours`
  - `day`
  - `model`
  - `provider`
  - `platform`
  - `status`
  - `session_id`
- return structured payload, not a bare row array:
  - `filters`
  - `total_runs`
  - `rows`

**Frontend pattern**
- provider row click → `setDrilldown({provider: ...})`
- model row click → `setDrilldown({model: ...})`
- day row click → `setDrilldown({day: ...})`
- chart segment click should use the same state path, not a parallel code path
- render a dedicated `Session Investigation` table on Breakdown with:
  - current filter chip
  - clear filter button
  - clickable session rows for opening session detail

### 10. Session detail drawer / page

Use when a session row needs second-level inspection without leaving the dashboard.

**Add `GET /api/session-detail?session_id=`** returning at least:
- `run`
- `llm_summary`
- `llm_calls`
- `provider_models`
- `tool_summary`
- `tool_calls`

**Drawer UI pattern**
- right-side overlay (`.drawer-overlay` / `.drawer`)
- open synchronously with loading state first
- then fetch detail async
- sections that worked well here:
  - Run totals
  - LLM call summary
  - Provider / model mix
  - Recent LLM calls
  - Tool calls

**Important UX rule**
- session rows on both Home (`Recent Sessions`) and Breakdown (`Session Investigation`) should open the same drawer
- keep the drawer read-only; it is for diagnosis, not mutation

**Per-model token usage**
- Add `GET /api/model-tokens?hours=&limit=`
- Query from `llm_calls`, grouped by `COALESCE(model, '—')`
- Return: `api_calls`, `tokens_in`, `tokens_out`, `cache_read_tokens`, `cache_write_tokens`, `reasoning_tokens`, `total_tokens`
- Sort by `total_tokens DESC, api_calls DESC`
- Good default limit: `100`

**Daily token usage with pagination**
- Add `GET /api/daily-tokens?hours=&page=&per_page=`
- Group by `DATE(ts)` from `llm_calls`
- Clamp `per_page` to a safe UI maximum (user wanted 10–15 days per page; 15 is a good ceiling)
- Return paging metadata: `page`, `per_page`, `total_days`, `total_pages`, `rows`
- Reset the frontend page back to `1` whenever the selected time window changes
- Render pager controls below the table (`Prev` / `Next`)

**Frontend placement**
- For telemetry dashboards, placing these below `Recent Sessions` works well:
  1. `Model Token Usage`
  2. `Daily Token Usage`
- Columns that matched the user's request:
  - Model/Day
  - Calls
  - Token In
  - Token Out
  - Cache Read
  - Cache Write
  - Reasoning
  - Total

### 10.5. Advanced filterable secondary views inside a monolithic dashboard

Use when a dashboard grows beyond a single summary page and needs a richer subview like a Skills or Journey explorer without becoming a separate app.

**Good pattern used here:**
- `Analytics` / `Search`
- `Skills`
- `Journey`
- `Tools` (optional: Hermes tool + token analytics from `state.db` via app-owned cache)
- `Sessions` (message timeline + token stats from live `state.db`; complements Tools — see `references/aceroute-sessions-tab-state-db.md` and **v2** `references/aceroute-sessions-page-v2.md`)
- `Requests`, `Messages`, `Models` (conversation grains from `state.db` — assistant turns, all messages, per-model aggregates; see `references/aceroute-requests-messages-models-tabs.md`; **Requests v2** `references/aceroute-requests-page-v2.md`)
- keep one shared JS runtime, but store per-view state in a dedicated object (for example `journeyState = { data, filtersBound, searchTimer }`)
- fetch the full dataset once from the backend, then do client-side filtering/sorting for the interactive explorer
- expose a compact control bar with:
  - text search
  - kind/category/state filters
  - sort mode (`recent`, `used`, `label`, `category`)
  - reset button
- render three layers:
  1. top summary cards
  2. focus panels (`Top Used`, `Pinned + Hot Status`)
  3. filtered timeline + filtered category breakdown

**Backend payload shape that worked well for Journey:**
- `summary`
- `latest_timestamp`
- `items` (full normalized list for client-side filtering)
- `recent`
- `pinned_items`
- `top_used`
- `timeline`
- `categories`
- `kinds`

**Frontend helpers that are worth standardizing:**
- `bindJourneyControls()` once on DOMContentLoaded
- `fillSelectOptions()` for dynamic dropdowns
- `getJourneyFilters()` and `resetJourneyFilters()`
- `applyJourneyFilters()` for all filter + sort logic in one place
- `render<Thing>FocusPanels()` for top-used / pinned blocks
- `render<Thing>FilteredView()` for counts, chips, filtered list, and filtered category summary

**Hermes desktop Journey/Starmap parity rule:**
- use the **real Hermes learning graph structure** (`nodes` + `edges` + `clusters` + `stats`) when trying to match desktop Journey/Starmap
- do **not** combine a real node set with invented synthetic connections or a second decorative graph logic; users will read that as a duplicate/haphazard graph immediately
- if exact desktop parity is too heavy for the web surface, prefer a **single clean simplified graph** over a flashy approximation
- on dense graphs, remove always-on labels before removing real graph structure
- add hover tooltip + neighbor highlighting by default; a clickable graph without hover detail feels incomplete next to Hermes desktop
- when users complain that the graph looks overlapped or chaotic, first fix **layout discipline** before adding more chrome: smaller nodes, larger ring gaps, ring-level anti-overlap spacing, and direct-edge-only hover emphasis beat decorative labels or extra panels
- for radial Journey graphs, prefer a two-stage density strategy:
  1. place nodes by time bucket / ring
  2. run a ring-local relaxation pass to enforce minimum angular spacing based on node size
- once the graph is usable, the next high-value Journey pass is to make it an operator surface, not just a viewer. The bundle that worked here was:
  - graph toolbar controls (`zoom`, `reset`, density mode, label mode, edge mode, scope mode)
  - quick filters (`hot`, `stale`, `pinned`, `orphaned`, `neighbors`)
  - node focus state that feeds the rest of the page
  - drawer navigation (`Prev/Next node`, `Prev/Next neighbor`, `Focus Neighborhood`)
  - path tracing between two nodes
  - saved presets in `localStorage`
  - filtered JSON export
  - category-health and orphan heatmap panels
- ring labels should be **real filters**, not cosmetic highlights. Clicking a ring should narrow the filtered timeline/list to that ring bucket and emit an active chip with the ring label, so the user can understand what slice of time they are inspecting.
- for Journey saved views, store only compact UI state (`search`, structured filters, sort, graph controls, preset) in browser `localStorage`; do not persist volatile graph data itself.
- path tracing on a Journey graph does not need backend support first. A frontend BFS over the existing `edges` payload is enough for a strong first version; render the returned node chain as clickable rows and defer graph-overlay rendering to a later pass.
- if you add category health, keep the score intentionally heuristic and operational, not faux-precise. A practical first pass is: reward `hot`, reward non-orphaned nodes, lightly reward use volume, penalize orphaned nodes.
- orphan heatmaps should be actionable: clicking a category bar should set the category filter **and** the `orphaned` preset in one move.
- when highlighting on hover, brighten only the hovered node, its **direct neighbors**, and the **actual connecting edges**; dim unrelated nodes harder. Broad category-wide highlighting reads as noise.
- for Journey drawers with raw buffers, expose three distinct copy actions: identifier copy, human-facing content/title copy, and full raw-buffer copy. Users often need all three for different downstream uses.
- avoid a hardcoded `Loading graph…` label in static markup. Use a neutral placeholder (`—`) and let render code set live counts/status; otherwise stale text can persist visually even after the graph loaded.
- if a radial graph renders while its page/tab is hidden, expect bad geometry from fallback widths/heights. Re-render after the section becomes visible (immediate call + `requestAnimationFrame`, and if needed a short delayed pass) so rings and nodes share the same center.
- if a browser keeps running old dashboard JS after a frontend fix, bump the script query version in `index.html` (`dashboard.js?v=N`). Live verification can otherwise be misleading because the DOM still reflects stale code.
- when a two-column dashboard grid contains one long scroll/table card and one short summary card, add `align-items:start` on the grid. Default stretch can make the short card look like a broken/half-rendered box because it inherits the taller column height.
- important disambiguation for user wording like **"make skill card full size of category card/box"**: they usually mean **same visible card height**, not "expand the table to its full dataset height". Do **not** remove scroll caps and let the whole left column grow to thousands of pixels. Keep scrolling inside the panel.
- for compact twin-panel explorers (like **Skills** vs **Top Categories**), cap both panels to a target visible-count window and scroll the rest. Practical AceRoute rule: tune `max-height` so the skills table shows about **10 visible rows** and the category stack shows about **10 visible items**; verify in-browser by counting fully visible rows/items from DOM rects instead of guessing from CSS alone.
- when the user says two side-by-side panels should be the **same size**, distinguish between (a) same outer card height and (b) same visible row count. Matching card heights alone can still look wrong if one side uses compact table rows and the other uses taller stacked cards. If the user cares about visual parity, set a shared card height and make both inner regions scroll, then verify both the outer card heights and the visible item counts separately.
- important disambiguation for user wording like **"make skill card full size of category card/box"**: they usually mean **same visible card height**, not "expand the table to its full dataset height". Do **not** remove scroll caps and let the whole left column grow to thousands of pixels. Keep scrolling inside the panel.
- when the user says header explainer text is clutter, remove it from the **DOM**, not just via CSS `display:none`. Then null-guard any JS that previously wrote into those nodes (`if ($(...) ) ...`) so the dashboard stays clean without runtime errors.
- for compact secondary pages like Skills/Journey, put summary mini-stats on a single row when space allows (`repeat(N, minmax(0,1fr))`) and shrink card padding/label size before adding more header copy or status chrome.
- when a user asks whether a secondary dashboard page can show **how many times** items are used, treat that as a first-class upgrade path. For Hermes Skills specifically, enrich the inventory endpoint with usage metadata merged from Journey (`use_count`, `last_used`, `state`, `pinned`, `created_by`, `stale`) and expose both aggregate summary stats and convenience lists for the frontend (`top_used`, `stale_skills`, `unused_skills`).
- for a usage-aware Skills page, prefer a real explorer/table over a static list. The AceRoute pattern that worked: summary cards (`Total Skills`, `Used`, `Hot`, `Stale`, `Total Uses`), an explorer toolbar (search, category/state/usage filters, sort), a table with `Skill / Category / Uses / Last Used / Refs / Status`, plus side panels for `Top Used Skills` and `Stale + Unused Skills`.
- add a one-line pointer to `references/aceroute-skills-usage-explorer.md` when maintaining the AceRoute Skills page so future agents know the concrete payload/UI mapping exists.
- for the next pass beyond the usage explorer, see `references/aceroute-skills-explorer-next-features.md` for the working pattern: tag filter, activity chart, clickable table rows, result chips/meta, and skill detail drawer.
- for the pass after that, the AceRoute Skills page scaled well with a second analytics tier: `Category Usage` chart, `Maintenance Queue`, and `Possible Overlaps`. Backend fields that supported it cleanly were `category_usage`, `maintenance_queue`, `similar_skills`, plus maintenance summary counts like `untagged_skills`, `refless_skills`, and `descriptionless_skills`.
- maintenance queue scoring that worked in practice: sort first by missing refs, then missing tags, then missing summary, then low/zero use count. Render explicit badges (`no refs`, `no tags`, `no summary`, `unused`) so cleanup is actionable without opening the drawer.
- cheap overlap detection that is acceptable for dashboard surfacing: normalize slug/name into lowercase alnum word stubs, group identical stubs, and show them as `Possible Overlaps`. Keep the label intentionally weak — it is a triage hint, not semantic deduplication.
- for the AceRoute Skills page specifically, do not render overlap members as one dense pill-row. Users will read that as a broken/blank card. Render a compact group header plus one readable row per candidate (`name`, `category/use-count`, explicit `Open` button).
- when adding more Skills-page panels, do not reuse one global fixed-height rule for every row. Split the page into row-specific layout classes and give each tier its own height policy: compact charts, medium operational lists, tall inventory panels, auto-height overlap card, then details last.
- if the user says cards `look overlapped`, check structure before z-index. In this session the visible problem was bad row grouping + inherited heights, not actual CSS stacking. Moving `Category Usage` beside `Skill Activity` and separating `Top Tags` from the chart row fixed the visual confusion.
- after that layout pass, the next high-value polish on this page was operational legibility rather than another new panel: add a compact maintenance-summary chip row under the results meta, make the main skills table header sticky inside the scroll region, and constrain `Skill Details` with an internal scroll so the page does not end in an oversized wall of cards.
- treat dashboard analytics charts as controls when the page is already filter-driven. On the AceRoute Skills page, `Category Usage` became materially better once bar clicks set the category filter rather than acting as decoration only.
- quick-health chips should summarize maintenance counts the user can act on immediately. The practical set here was `no refs`, `no tags`, `no summary`, and `unused`. Put them directly under the result-count line, above the main table.
- when you add a preset/quick-health filter affordance, do not fake it with free-text search terms like `refs`. Drive the real structured filter state or a dedicated predicate instead.
- when verifying new Chart.js panels in browser automation, `window.charts.<name>` can report false even when the chart rendered. Use `!!Chart.getChart(document.getElementById('<canvasId>'))` as the authoritative live check.
- see `references/aceroute-skills-maintenance-overlap.md` for the concrete field mapping and UI pattern of the maintenance/overlap upgrade.
- see `references/aceroute-skills-layout-polish.md` for the follow-up layout pass: moving `Category Usage` beside `Skill Activity`, scoping row-specific card heights, and rendering `Possible Overlaps` as readable rows instead of cramped pills.
- see `references/aceroute-skills-legibility-and-chart-actions.md` for the later Skills-page pass: sticky table header, quick-health chips, constrained detail panel, and clickable `Category Usage` bars.
- see `references/aceroute-skills-maintenance-assistant-and-fuzzy-overlap.md` for the next pass: broken-ref assistant, maintenance sub-tabs, chart dataset actions, drawer prev/next navigation, and weighted fuzzy overlap scoring.
- see `references/aceroute-search-analytics-empty-state-polish.md` for Search: tab title, **one-line Web Extract** (`#extractInlineMeta` + Log toggle), `setAnalyticsCompact()` for empty Hermes debug cards, `.results-chip` filter spacing.
- see `references/aceroute-tools-tab-feature-bundle.md` for Tools features after `state.db` sync; layout is always two-row per `dashboard-ui-polish` → `two-row-toolbar-and-stats-strip.md`.
- see `references/aceroute-hermes-only-search-tab.md` for Hermes-only Search (`ACEROUTE_SEARCH_SOURCE=hermes`, `aceroute_search.py`, Dockerfile `COPY`, optional `ACEROUTE_SHOW_SEARXNG=1`).
- see `references/aceroute-dependency-and-tab-sources.md` when the user asks which AceRoute tabs survive removing OmniRoute/SearXNG/plugins.
- see `references/aceroute-sessions-tab-state-db.md` for the Sessions tab APIs, drawer, and `COPY aceroute_sessions.py` Dockerfile pitfall.
- see `references/aceroute-sessions-page-v2.md` for Sessions v2 operator surface (podium, 5-chart grid, sort/export, drawer charts, `session_id` Messages filter).
- see `references/aceroute-requests-messages-models-tabs.md` for Requests, Messages, Models tabs when the user asks for per-model stats, message breakdown, or LLM request analytics.
- see `references/aceroute-requests-page-v2.md` when extending the **Requests** tab (podium, finish/source/tools filters, 5-chart grid, export). If the user says "session page" but the nav is **Requests**, extend Requests — confirm tab if ambiguous.
- see `references/aceroute-models-page-v2.md` when extending the **Models** tab (provider rollup, export, pins, cross-tab filters, drawer charts); v3 adds compare, sparklines, token-mix chart (`2c79b16`).
- for Search/analytics pages, do not stop at static metrics once the user wants investigation. The next high-value upgrade is a compact drill-down layer: provider filter chip row, clickable provider tables/charts, clickable recent/error/zero-result/extract rows, and a right-side detail drawer with summary, signals, related activity, and quick actions (`Filter Provider`, `Search Query`, `Copy Primary`).
- when the top overview card says `Searches` and also mentions extracts in the sublabel, split it into two first-class cards instead (`Searches`, `Extracts`). Users read that separation faster than mixed text.
- if you add provider drill-down on a Search page, keep one shared filter state (`searchState.provider`) and route every entry point through it: provider table rows, cost pie clicks, provider-comparison bar clicks, and drawer `Filter Provider`. Do not create separate ad-hoc filter paths.
- make query-like lists genuinely actionable. `Top Queries`, `Recent Queries`, `Zero-Result Queries`, error tables, and extract logs should open the same detail drawer instead of acting as passive text.
- for detail drawers on dashboard investigation pages, include at least four sections: `Summary`, `Signals`, `Primary Content`, and `Related Activity`. Reusing the existing right-side drawer pattern keeps the app visually consistent and avoids inventing a second modal system.
- on Search pages with provider filtering, empty states must stay specific to the current filter (`No recent queries for current filter`, `No extract calls for current provider filter`) rather than generic `No data yet` text.
- for browser verification of clickable Chart.js drill-downs, call the chart's `options.onClick` handler directly against `Chart.getChart(canvas)` rather than relying only on synthetic DOM clicks; this is a more reliable proof that the filter wiring is live.
- see `references/aceroute-search-drilldown-and-provider-filter.md` for the concrete AceRoute Search-page pass adding provider chips, clickable charts/rows, and the unified detail drawer.
- in the next Skills-page pass, make quick-health maintenance chips (`no refs`, `no tags`, `no summary`, `unused`) real controls, not decorative counts. Drive them with a dedicated preset state/predicate; do **not** fake maintenance filtering by stuffing words like `refs` into the free-text search box.
- once the skills inventory grows, replace the old hard cap (`slice(0, 80)`) with real table pagination: explicit page size selector, Prev/Next controls, footer text showing the visible range and total pages, and page reset on filter/search/preset changes.
- if multiple filter-entry paths exist (toolbar dropdowns, chart clicks, top-tag clicks, maintenance chips), centralize the reset semantics: structured filters should clear transient preset state; preset chips should clear unrelated structured filters that would otherwise create confusing intersections.
- for Skills drawers, add a `Related Skills` panel once the inventory becomes rich enough. A cheap but useful scoring heuristic is: same category (+3), each shared tag (+2), same creator (+1), then sort by score and usage count. Label it as a suggestion surface, not ground truth.
- when adding page-size selectors or pagination to a dashboard table, bind them into the same control lifecycle as the other filters. Changing page size should reset to page 1; Next/Prev should only mutate page state and re-render.
- on dashboards where Search is the default landing page, do not keep large secondary views like Skills and Journey in the global background heavy-refresh loop. Lazy-load them on first tab open and refresh them only when their tab is active; this reduces idle CPU churn and avoids paying multi-hundred-KB JSON parse costs on every background refresh.
- if a Skills inventory endpoint is cold-slow but warm-fast, prefer a daemonized background singleton cache over repeated request-time recomputation. For AceRoute this meant splitting `_compute_hermes_skills()` from `collect_hermes_skills()`, warming a `SkillsInventoryCache` on startup, and refreshing every ~300s. In this session the measured effect moved Skills from prior cold-ish multi-second samples (~5–6s) to ~0.046–0.084s after warmup.
- if a Journey drawer is slow because raw content shells out to `hermes journey edit`, prefetch raw buffers for the top-used/recent nodes in a small background cache and seed the normal per-node TTL cache from it. Pair that with an optimistic drawer header (title/subtitle from already-loaded page data before raw content lands) to remove the visible `Loading…` pause. In this session a `JourneyItemCache` prefetching ~12 top/recent nodes brought tested drawer raw-buffer fetches down from ~1.7–2.9s to ~0.005–0.039s.
- if the Skills filesystem walk itself is cheap but the endpoint is still cold-slow, treat the expensive part as payload assembly / merge / serialization, not directory scanning. Do not optimize the wrong layer first.
- for a **Tools / token / session analytics** page on AceRoute (or similar Hermes SPA), do **not** bind the feature to `hermes-telemetry` / `telemetry.db`. Hermes core `~/.hermes/state.db` already has `sessions` token totals + `messages.tool_name`. Sync into an app-owned SQLite (`aceroute.db`) on a daemon thread so analytics survive plugin removal and stay fast. Optional: merge plugin `latency_ms` / `ok` later if the DB exists.
- Tools tab pattern: lazy-load on first nav open; `GET /api/tools?days=` + session drawer hitting `state.db` for message drill-down; Docker named volume for `aceroute.db`, read-only mount for `state.db`. See `references/aceroute-tools-page-state-db-sync.md`.

See `references/aceroute-journey-starmap-parity.md` for the AceRoute-specific parity lessons and fallback hierarchy.
See `references/aceroute-journey-hover-spacing.md` for the overlap/neighbor-highlight cleanup pass.

**Verification pattern:**
- verify API shape first by hitting the JSON endpoint directly
- then verify browser-rendered counts and filter behavior from the live DOM, not just static HTML source
- for browser-tool verification, `browser_console(expression=...)` is often the most reliable way to assert:
  - active page id
  - dropdown option counts
  - rendered row/card counts
  - filtered result counts after programmatically changing controls
- use `browser_snapshot` for visible structure, but use DOM inspection for exact counts and state because snapshots can lag or truncate

See `references/aceroute-hermes-skill-journey-pattern.md` for the concrete AceRoute pattern.

### 11. Slow-endpoint performance: background cache + frontend defer

Use when a dashboard's first-paint load time grows because one or two endpoints
are slow (5–30s) while the rest are fast (<100ms). Browser fires all endpoints
in parallel via `Promise.all`, so the slowest one dominates first-paint.

**Two-step fix:**

**Step A: cache the slow query in SQLite, refresh in a background thread.**

The endpoint must read from a small cache table instead of recomputing every
request. Run a daemon thread inside `serve.py` that pre-computes the result for
the common window presets and writes the JSON to a cache table.

```python
import time, threading
from http.server import ThreadingHTTPServer  # see Pitfalls

_CACHE_SCHEMA = """
CREATE TABLE IF NOT EXISTS slow_endpoint_cache (
    cache_key TEXT PRIMARY KEY,
    window_hours INTEGER NOT NULL,
    include_deleted INTEGER NOT NULL,
    limit_n INTEGER NOT NULL,
    payload_json TEXT NOT NULL,
    rows_count INTEGER NOT NULL,
    built_at TEXT NOT NULL
)
"""

class SlowEndpointCache:
    DEFAULT_REFRESH_SECONDS = 300
    DEFAULT_WINDOWS = (24, 168, 720, 0)  # 1d, 1w, 30d, all-time

    def __init__(self, db_path):
        # check_same_thread=False: connection is touched from BOTH the
        # background refresh thread AND request handlers. Serialize writes
        # through the condition variable; SQLite WAL + busy_timeout handle reads.
        self._conn = sqlite3.connect(str(db_path), isolation_level=None, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA busy_timeout=5000")
        self._conn.execute(_CACHE_SCHEMA)
        self._cond = threading.Condition(threading.Lock())
        self._stop = threading.Event()
        self._last_refresh_at = None
        self._thread = threading.Thread(target=self._run, name="slow-endpoint-cache", daemon=True)

    def _run(self):
        try:
            self._refresh_all()
        except Exception:
            logger.exception("initial slow-endpoint cache refresh failed")
        while not self._stop.is_set():
            with self._cond:
                self._cond.wait(timeout=self.DEFAULT_REFRESH_SECONDS)
            if self._stop.is_set(): break
            try: self._refresh_all()
            except Exception: logger.exception("scheduled refresh failed")

    def get_rows(self, window_hours, include_deleted, limit):
        key = self._key(window_hours, include_deleted, limit)
        row = self._conn.execute(
            "SELECT payload_json, built_at FROM slow_endpoint_cache WHERE cache_key = ?", (key,)
        ).fetchone()
        if row:
            return json.loads(row["payload_json"])
        rows = self._compute_live(window_hours, include_deleted, limit)
        with self._cond:
            self._conn.execute(
                """INSERT INTO slow_endpoint_cache(cache_key, window_hours, include_deleted, limit_n, payload_json, rows_count, built_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?)
                   ON CONFLICT(cache_key) DO UPDATE SET payload_json=excluded.payload_json, built_at=excluded.built_at""",
                (key, window_hours, int(include_deleted), limit, json.dumps(rows, default=str), len(rows),
                 datetime.now(timezone.utc).isoformat()))
        return rows
```

Start the cache singleton in `main()`:

```python
def main(argv=None):
    ...
    SlowEndpointCache.instance()  # daemon thread primes cache before serve
    server = ThreadingHTTPServer((host, port), Handler)
```

**Step B: defer the slow endpoint from initial `Promise.all` on the home page.**

Move the slow endpoint out of the initial fetch batch. For pages that need
the data, render a placeholder card first, then lazy-fetch and swap in real
data after first-paint:

```js
// BEFORE: blocks first-paint
const [..., modelEfficiency, ...] = await Promise.all([
  ...,
  fetchJSON(`/api/model-efficiency?hours=${hours}&limit=50`),  // slow
  ...
]);

// AFTER: first-paint not blocked
const [...] = await Promise.all([
  ...,
  // fetchJSON(`/api/model-efficiency?hours=${hours}&limit=50`),  // removed
  ...
]);

// Render placeholder on the page that needs it
html += renderTableCard('modelEfficiencyTable', 'Model Efficiency Score',
  `<div id="modelEfficiencyMount" class="loading-shell" style="min-height:120px">Loading…</div>`);

// After first-paint: lazy-fetch and swap
fetchJSON(`/api/model-efficiency?hours=${hours}&limit=50`)
  .then((rows) => {
    if (requestId !== latestLoadRequestId) return;  // stale guard
    const mount = document.getElementById('modelEfficiencyMount');
    if (!mount) return;
    const card = mount.closest('.table-card');
    const tmp = document.createElement('div');
    tmp.innerHTML = renderTableCard('modelEfficiencyTable', 'Model Efficiency Score', renderModelEfficiency(rows));
    card.replaceWith(tmp.firstElementChild);
  })
  .catch((err) => {
    const mount = document.getElementById('modelEfficiencyMount');
    if (mount) mount.innerHTML = `<div class="text-muted">Unavailable: ${err.message}</div>`;
  });
```

**Result on `hermes-telemetry`:** `Loaded 21.2s → 6.7s`; slow endpoint `13s → 0.001s`.

**Expose admin endpoints for ops visibility:**

- `GET  /api/<slow-endpoint>/cache/status` — entries, last refresh, is_refreshing
- `POST /api/<slow-endpoint>/refresh?hours=24&include_deleted=0` — force refresh

**Test recipe:**

- Pin `db._utcnow()` to current time and record LLM calls with `now = db._utcnow()` so window filters pass.
- First call: live compute + seed cache; assert row present.
- Second call: must hit cache in <500ms.
- `status` endpoint reports the entry.
- `refresh` endpoint rebuilds without error.

**Why this works:** background thread does the heavy lifting off the request
path; request path reads JSON from a single-row `SELECT`; frontend stops
waiting for the slow endpoint on initial paint.

## Pitfalls & fixes

| Issue | Fix |
|-------|-----|
| `/api/providers` ignored time window | Ensure handler parses `hours` param AND frontend passes `?hours=` |
| Fragile `.replace("started_at", "r.started_at")` in SQL | Use `_since_clause(window_hours, "r.started_at")` with column parameter |
| `int(daily_window/24)` truncates for non-24-multiples | Use integer division: `daily_window // 24` |
| Chart capped at 90 days for "All time" | Make chart query unconditional when `hours=0` (match summary cards) |
| Dashboard edits don't propagate to plugin | Add file watcher + `reload_config()` in plugin; call from `register()` |
| Edit button on separate line | Put button inside `.info` flex container with `margin-left: 12px; white-space: nowrap` |
| `JSON.stringify()` in onclick breaks HTML attribute (double quotes) | Use single quotes in onclick: `onclick="openBudgetModal('${safeScope}')"`, escape single quotes in value |
| Budget API expects separate scope/window but button passes "global/daily" | Parse in `openBudgetModal()`: `const [parsedScope, parsedWindow] = scope.split('/')` |
| Modal fails to open on tunnel/mixed-content (HTTPS→HTTP) | Open modal **synchronously first** (`classList.add('open')`), then fetch details async; works even if fetch fails |
| Modal invisible behind proxy/auth layers / mobile viewport | CSS: `z-index: 99999`, `display: flex !important`, `box-shadow: 0 8px 32px rgba(0,0,0,0.5)` |
| Upstream PR push denied (403) | Add fork remote: `git remote add fork https://github.com/<user>/<repo>.git`; push to fork |
| Rebase conflicts on dashboard files after fork sync | `git checkout --theirs dashboard/serve.py dashboard/index.html` to keep review fixes |
| PR already merged, pushing to same branch | Check `gh pr view --json state,mergedAt` before pushing; create new branch for new features |
| New columns not in existing DB | Add migration function (`_migrate_vN`) that runs on connection; call in `_ensure_schema` order |
| Budget hot-reload not working | `reload_config()` must clear both `_config_cache` AND `_verdict_cache`; watchdog runs in daemon thread |
| Token breakdown SUM returns NULL for missing reasoning_tokens | Use `COALESCE(SUM(column), 0)` on **each** column individually, not just outer COALESCE |
| Budget modal opens with defaults instead of current values | Add `/api/budget/detail?scope=&window=` endpoint; fetch on `openBudgetModal()` |
| Stale dropdown state bug in budget modal | Always fetch `window=daily` in `openBudgetModal()` — ignore `$('#budgetWindow').value` which may hold previous interaction's value |
| Unused state variable `currentBudgetWindow` | Remove; `openBudgetModal()` reads DOM directly for window dropdown |
| Modal race on slow connections (HTTPS→HTTP tunnel) | Open modal **synchronously first** (`classList.add('open')`), **then** fetch details async; user sees instant feedback |
| Threshold scope footgun — soft/hard pct look per-scope but are global | Add `(global)` label to soft/hard threshold fields in modal |
| Non-atomic YAML write → watchdog reads partial file | Write to temp file (`path.with_suffix('.yaml.tmp')`), then `os.replace(tmp, path)` (POSIX atomic); apply in both dashboard POST and slash command |
| Upstream PR push 403 (no write access) | Add fork remote; push to fork (`git push fork HEAD:feature-branch`); PR auto-updates |
| Rebase conflicts on dashboard files after fork sync | `git checkout --theirs dashboard/serve.py dashboard/index.html` to keep review fixes; `git add` + `git rebase --continue` |
| Pry output without tee loses evidence | Pipe long commands through `tee` or capture to file for debugging |
| User wants local dashboard work but has not asked for PR/push | Keep changes local; do **not** push commits or update PRs without explicit user instruction |
| Per-model / per-day token tables requested | Add `/api/model-tokens` and paginated `/api/daily-tokens`; place new tables below `Recent Sessions` |
| Daily token pagination should follow time-window selection | Reset page to 1 when `hours` filter changes so pager state does not drift across ranges |
| Token breakdown endpoint can crash older DBs | Return `None` on schema/query failure so frontend can hide the widget instead of 500ing the whole dashboard |
| **Full stylesheet replacement loses 189+ class definitions** | Use **additive CSS overlay**: add second `<style id="custom">` block AFTER original; new rules override via specificity, original classes untouched |
| **Header HTML replacement breaks structure** | Replace header block via exact string match on unique comment markers (`<!-- Header -->` to `</div>`), not line numbers |
| **renderStats() undefined after CSS changes** | Must be defined **before** `Object.assign(window, ...)` export in the **main app IIFE** (third script block); other script blocks have separate scopes |
| **Function exported but not defined** | Add function name to `Object.assign(window, { ..., renderStats })` export list |
| **Modal architecture broken (.modal vs .modal-overlay)** | `.modal-overlay` = backdrop (fixed, full-screen, hidden by default, `display:flex` when `.active`); `.modal` = inner panel (smaller, centered). Don't conflate with `[class*="modal"]` selectors |
| **Verify ALL modals before/after changes** | Test open/close/save for all modals (`modal-app`, `modal-sysinfo`, `modal-docker`, `modal-logs`, `modal-bookmark`, `modal-settings`, `modal-sysactions`, `modal-alerts`, `modal-layout`) programmatically |
| **Original renderStats() used innerHTML with `stat-pill` classes** | New version must target individual element IDs (`stat-load`, `stat-ram`, `stat-disk`, `stat-servers`, `stat-temp`, `stat-time`) with `metric-value` classes and `ok`/`warn`/`crit` color coding |
| **Multiple IIFEs in single HTML file** | Identify which script block is the main app (typically the third one, with `STATE` and `renderAll`); only that scope has access to `STATE.stats` |
| **Surgical HTML replacement via exact strings** | Use unique comment markers (`<!-- Header -->` to next `</div>`) for `str.replace(old, new, 1)` — avoid line numbers which drift |
| **Additive CSS preserves all 189 original class definitions** | Original classes like `.card-stat`, `.card-action-btn`, `.layout-toolbar`, `.settings-group`, `.sysinfo-grid`, `.section-icon` remain fully functional; new CSS only overrides visual properties via specificity |
| **stdlib `HTTPServer` is single-threaded** — one slow endpoint blocks every other request including `/` | Use `ThreadingHTTPServer` from `http.server` instead: `from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer` and `server = ThreadingHTTPServer((host, port), Handler)`. Symptom: dashboard stuck on `Loading…` even though 9 of 10 endpoints are fast, because the slow one queues every other request. Browser fires endpoints in parallel via `Promise.all`, so first-paint is bounded by the slowest endpoint. |
| **Daemon thread + sqlite3 connection → `ProgrammingError: SQLite objects created in a thread can only be used in that same thread`** | Open the connection with `check_same_thread=False` and serialize writes through a `threading.Condition`. Reads can use the same connection; rely on `PRAGMA busy_timeout=5000` for concurrent reads. Don't try to share connections between threads without `check_same_thread=False`. |
| **Forgot `import time` in `serve.py`** when adding a background cache that uses `time.monotonic()` for elapsed-time tracking | Add `import time` at top; the default stdlib `serve.py` template does not import it. |
| **Stale card data after lazy-fetch swap** | Use a `requestId !== latestLoadRequestId` guard before swapping the lazy-loaded card content. The user may have changed the time window or clicked Refresh between the placeholder render and the lazy fetch landing. |
| **Monolithic dashboard: note links from Home use title + encodeURIComponent** | Titles with spaces/`&` never match; use **vault paths** and `onclick="openNoteByPath(${JSON.stringify(path)})"`. Implement `openNoteByPath` → `switchPage('notes')` → wait for `openNote()` + `data.notes` — do not write HTML into a dead `#reader` id. See `obsidian-memory-vault` → `references/obsidian-dashboard-note-links.md` for Obsidian vault dashboard. |
| **Cache refresh blocks new request handlers** | Use `with self._cond:` around `_write_cache()` calls so the daemon thread and request-time cache misses don't interleave their writes. Reads can run without the lock; the lock is for write serialization. |
| **Dashboard/plugin collector is pointed at an old source name, not the live traffic source** | Before debugging cron wrappers or patching SQL, verify which system is actually receiving current traffic. In this session a `manifest-history` plugin was still reading a stale local Manifest Postgres, while Hermes had moved to cloud Manifest for inference and the live request archive was really in OmniRoute call logs. Check the live system first: compare the newest timestamps in the collector source, the active provider/gateway config, and any alternate local logs. If the named product DB is stale overall (not just one table), fix the collector source instead of trying to "repair" an inactive database. See `references/collector-source-drift-manifest-vs-omniroute.md`. |
| **Daemon thread reentrancy on startup** | Check `self._refreshing` flag at the top of `_refresh_all()` and return early if already refreshing. Otherwise a slow first refresh can be re-entered by a 300s tick before it finishes. |
| **Initial cache refresh takes 1-2 min for first load** | That is acceptable — it runs in the daemon thread; the first user request is served from cold-compute (slow), then warm on every subsequent call. Document the expected initial cold-start time in the skill. |
| **Tools analytics tied to telemetry plugin DB** | User may remove `hermes-telemetry`; use Hermes `state.db` as source and a dashboard-owned cache DB (`aceroute.db`). Rebuild `tool_daily`/`tool_totals` on each sync — never incremental-add daily tool counts. |
| **User wants Tools bar + stats on separate lines** | Two sibling blocks (`tools-bar-card` then `tools-stats-row`). Do **not** merge into one hero after they corrected you. See `dashboard-ui-polish` → `two-row-toolbar-and-stats-strip.md`. |
| **New Python module in AceRoute/FastAPI app but container crashes on import** | Add the `.py` file to Dockerfile `COPY` line. Symptom: `ModuleNotFoundError` (e.g. `aceroute_search`). |
| **User wants Search analytics without OmniRoute/SearXNG** | `ACEROUTE_SEARCH_SOURCE=hermes`; ingest `web_search`/`x_search`/`web_extract` from `state.db` (+ debug logs). See `references/aceroute-hermes-only-search-tab.md`. |
| **AceRoute UI unchanged after user refresh** | Container may serve old baked `static/`. Verify `curl -s http://host:8866/ \| grep dashboard.js` vs repo; rebuild and/or compose mount `./static:/app/static:ro`. User signal: "nothing changed even after refresh". |
| **Sessions bar should be one line** | Bar card: single `.sessions-bar-row` (`nowrap`) with chips scrolling inline; stats in separate 8-col `#sessionsSummary`. `dashboard-ui-polish` → `references/sessions-one-line-bar-and-stats.md`. |
| **Monolithic `dashboard.js` page rewrite** | Write fragment `static/js/<page>_v2.js`, Python-splice between `// ── Section ──` markers, `node --check`, bump `?v=`. See `references/aceroute-sessions-page-v2.md` and `references/aceroute-requests-page-v2.md`. |
| **Splice deleted an entire page block** | Broad `patch` on Requests/Sessions can remove `renderRequests` / `renderSessions`. After edit: `node --check` and confirm those functions exist; re-insert from `<page>_v2.js` if missing. |
| **Section marker glued to prior function** | `closeFoo(); }// ── Next` without newline breaks `dash.index('// ── Next')`. Add newline before the section comment. |
| **Ambiguous `conn.close()` in `aceroute_sessions.py`** | Anchor patches with surrounding SQL/return context (e.g. `recent_sessions` query tail), not bare `conn.close()` (multiple matches). |
| **Aggregate API cache feels stale** | Add `fresh=1` on dashboard endpoints; ↻ button calls `render*(true)`. |
| **Messages tab missing old session rows** | `GET /api/messages?session_id=` must not apply days window on `timestamp` when filtering one session. |
| **renderStats() undefined after CSS changes** | Must be defined **before** `Object.assign(window, ...)` export in the **main app IIFE** (third script block); other script blocks have separate scopes |
| **Function exported but not defined** | Add function name to `Object.assign(window, { ..., renderStats })` export list |
| **Modal architecture broken (.modal vs .modal-overlay)** | `.modal-overlay` = backdrop (fixed, full-screen, hidden by default, `display:flex` when `.active`); `.modal` = inner panel (smaller, centered). Don't conflate with `[class*="modal"]` selectors |
| **Verify ALL modals before/after changes** | Test open/close/save for all modals (`modal-app`, `modal-sysinfo`, `modal-docker`, `modal-logs`, `modal-bookmark`, `modal-settings`, `modal-sysactions`, `modal-alerts`, `modal-layout`) programmatically |
| **Original renderStats() used innerHTML with `stat-pill` classes** | New version must target individual element IDs (`stat-load`, `stat-ram`, `stat-disk`, `stat-servers`, `stat-temp`, `stat-time`) with `metric-value` classes and `ok`/`warn`/`crit` color coding |
| **Multiple IIFEs in single HTML file** | Identify which script block is the main app (typically the third one, with `STATE` and `renderAll`); only that scope has access to `STATE.stats` |
| **Surgical HTML replacement via exact strings** | Use unique comment markers (`<!-- Header -->` to next `</div>`) for `str.replace(old, new, 1)` — avoid line numbers which drift |
| **Additive CSS preserves all 189 original class definitions** | Original classes like `.card-stat`, `.card-action-btn`, `.layout-toolbar`, `.settings-group`, `.sysinfo-grid`, `.section-icon` remain fully functional; new CSS only overrides visual properties via specificity |

- [ ] All API endpoints accept `?hours=` and respect it
- [ ] Time range selector includes "All time" (value=0) as default
- [ ] Chart titles dynamic per selection
- [ ] Modal forms validate required fields
- [ ] File watcher starts on plugin load, logs on config change
- [ ] `reload_config()` clears caches + verdict cache
- [ ] Dashboard refreshes after modal save (`loadAll()`)
- [ ] Token breakdown table shows all 5 types + total row
- [ ] `/api/budget/detail` returns current config for modal pre-fill
- [ ] POST `/api/budget` returns 400 for validation errors, 200 for success
- [ ] Content-Length > 1 MiB returns 413
- [ ] XSS-safe onclick handlers use single quotes (not JSON.stringify double quotes)
- [ ] Frontend parses floats with empty-string guard (`parseOptFloat`)
- [ ] `openBudgetModal()` parses "global/daily" format into separate scope/window
- [ ] Modal opens synchronously before async fetch (works on tunnel/mixed-content)
- [ ] Modal CSS has high z-index (99999), !important display, box-shadow
- [ ] `serve.py` uses `ThreadingHTTPServer` (not `HTTPServer`) — verify with `grep -n "ThreadingHTTPServer\|HTTPServer(" dashboard/serve.py`
- [ ] Any background-cache singleton uses `check_same_thread=False` and serializes writes through a `Condition`/`Lock`
- [ ] Slow endpoints (≥1s) are either cached or deferred from initial `Promise.all` on the home page
- [ ] Admin endpoints expose cache status (`/cache/status`) and force-refresh (`/refresh`) for ops visibility

## Related files

- `references/serve-py-pattern.md` — annotated serve.py template
- `references/index-html-pattern.md` — annotated index.html template
- `references/slow-endpoint-cache-pattern.md` — annotated background-cache class + frontend defer
- `references/aceroute-hermes-skill-journey-pattern.md` — adding live Hermes Skills/Journey tabs to an SPA dashboard, including DOM-level verification after browser rendering
- `references/journey-drawer-radial-graph-and-mutation-gating.md` — journey-node drawer/graph pattern, CLI capability probing, and read-only mutation gating.
- `references/aceroute-journey-starmap-parity.md` — AceRoute Journey graph parity rules for Hermes desktop starmap: use real edges, avoid duplicate graph logic, and prefer clean fallback over flashy approximation.
- `references/aceroute-skills-maintenance-overlap.md`
- `references/aceroute-tools-page-state-db-sync.md` — AceRoute Tools tab: `aceroute.db` sync from Hermes `state.db` (not telemetry plugin), API shape, Docker volume, verification.
- `references/aceroute-tools-tab-feature-bundle.md` — expanded Tools UI/API after sync (charts, export, drawers).
- `references/aceroute-hermes-only-search-tab.md` — Hermes-only Search tab from `state.db`.
- `references/aceroute-sessions-tab-state-db.md` — Sessions tab v1 (messages + tokens from `state.db`).
- `references/aceroute-sessions-page-v2.md` — Sessions tab v2 operator surface.
- `references/aceroute-requests-messages-models-tabs.md` — Requests, Messages, Models tabs and grain model.
- `references/aceroute-requests-page-v2.md` — Requests tab operator UI (v2 + JS splice pitfalls).
- `references/aceroute-models-page-v2.md` — Models page operator UI (v2 feature bundle + verification).
- `references/aceroute-dependency-and-tab-sources.md` — Hermes-only vs optional OmniRoute/SearXNG per tab.
- `references/collector-source-drift-manifest-vs-omniroute.md` — diagnosing stale dashboard archives when the plugin/job still points at an old product DB instead of the system that now receives live traffic.
- `templates/dashboard-serve.py` — starter serve.py
- `templates/dashboard-index.html` — starter index.html