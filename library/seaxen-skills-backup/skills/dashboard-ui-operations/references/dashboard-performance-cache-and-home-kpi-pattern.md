# Dashboard performance + KPI correctness pattern

Use this when a self-hosted dashboard feels slow because the browser waits on historical aggregations, or when homepage KPI cards are derived from the wrong source.

## What worked

### 1) Scope fetches to the active page only
Do not fetch Breakdown / Request / Tool / Error page data while rendering Home.

Pattern:
- Home: fetch only summary, cron, providers, recent runs, budget
- Breakdown: fetch token/model breakdown endpoints only when the Breakdown tab is active
- Requests: fetch provider-health and request-forensics only when that tab is active
- Tools / Errors: same idea

This cut first-paint time because the browser was no longer waiting on irrelevant APIs.

### 2) Defer heavy Home charts
If Home has a metric strip plus a slow historical chart:
- render the metric strip immediately from a lightweight summary endpoint
- render the heavy trend chart after first paint
- replace a loading placeholder once the chart payload arrives

Good fit for:
- daily token history
- daily model breakdown
- any all-time grouped chart

### 3) Cache heavy historical aggregations in SQLite
For endpoints like `/api/daily-token-chart`, `/api/providers`, `/api/provider-health`, and `/api/daily-model-chart`:
- cache the full JSON payload in SQLite
- key by the actual query dimensions
- on cache miss, compute live once and seed the cache
- warm common keys in a background thread on startup

Useful cache key dimensions:
- `window_hours`
- `limit_days`
- `include_deleted`
- `granularity`
- viewer timezone when the payload is timezone-shaped

Warm the exact combinations used by the Home dashboard first.

### 4) Keep homepage KPI cards on a lightweight summary path
Do not derive the visible KPI numbers from the deferred chart payload.

Instead return a dedicated `home_metrics` block from the summary API so Home can show honest numbers immediately while the chart loads later.

## KPI correctness rules that mattered

### Messages
If the product meaning is real chat messages, count them from `state.db` / message storage:
- `role in ('user', 'assistant')`
- ignore empty content
- expose `user_messages`, `assistant_messages`, and combined `message_runs`

Do not fake this from run counts or chart rows.

### Cron runs
If users expect all scheduled executions, count from Hermes scheduler history / cron output history, not only telemetry-backed LLM runs.

Reason:
- script-only cron jobs may produce no token telemetry
- scheduler repeat/completed history is the user-visible source of truth

### Tool calls
Use actual `tool_calls` event rows, not per-run aggregate columns if those can drift.

### Token usage / savings
Use `llm_calls` aggregates for token counts and savings math.

## Restart + verification sequence
After patching performance paths:
1. run lint/tests
2. restart the systemd unit cleanly
3. verify live endpoint timings with repeated requests
4. verify browser first-paint separately from heavy chart load
5. verify the KPI numbers against the real backing stores

## Example impact from this pattern
- Home no longer blocked on `/api/daily-token-chart`
- providers and daily-token-chart endpoints dropped to ~1-2 ms on repeated requests after cache warm-up
- metric cards stayed correct because they came from `summary.home_metrics`, not the deferred chart

## Related: AceRoute (`:8866`, `/mnt/tb/1Apps/AceRoute`)

- **Global duration / true all-time:** `references/aceroute-global-duration-and-all-time.md` — single Settings duration, `ALL_TIME_DAYS=36500`, FastAPI `le=36500`, Docker rebuild for Python (static-only mount). Half-empty KPI/charts → curl `?days=36500` before Chart.js.
- **Tools:** `ToolsAnalyticsCache`, `aceroute.db` from `state.db` — `references/aceroute-hermes-tools-analytics.md`. Toolbar + stats = **two sibling rows** (`dashboard-ui-polish` → `references/two-row-toolbar-and-stats-strip.md`).
- **Skills/Journey:** KPI strip **one row** (`repeat(8)` / `repeat(5)`) — `references/stats-inline-row-one-line.md`.
- **Search:** compact Web Extract one-liner; `setAnalyticsCompact()` for empty Hermes debug sections.
- **SearXNG panel:** empty `/stats` → `/config` fallback — `searxng` → `references/aceroute-engine-stats-fallback.md`.
- **JS:** bump `dashboard.js?v=` after edits; `immutable` cache on static assets.