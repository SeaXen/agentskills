# Hermes telemetry forensic/operator upgrade

Use this when extending a SQLite-backed telemetry dashboard with forensic/operator surfaces rather than just summary KPIs.

## Good feature bundle
For Hermes telemetry-style dashboards, a high-ROI forensic/operator batch is:
- request forensics table
- request detail drawer
- tool analytics table
- error center
- provider health / anomaly signals
- shared drill-down filters across all of them

This works better than isolated widgets because the operator can move from aggregate view -> exact request -> surrounding session -> related tool failures.

If the page starts feeling dense, split the forensic surfaces into internal tabs/pages instead of stacking everything on Breakdown:
- **Request** → provider health / anomaly signals + LLM request forensics
- **Tool** → tool analytics
- **Error** → error center, status groups, failed tools, incident feed
- **Breakdown** should stay focused on token/provider/model/cache/day/session-investigation analytics

For this user, when they ask to remove noisy columns, do it literally and verify the table headers live. Good defaults found in practice:
- remove `Cron Job` from Home **Recent Sessions** when it makes the feed too wide/noisy
- remove `Reasoning` from **LLM Request Forensics** when request triage needs a narrower table; keep reasoning visible in detail drawers or deeper model/token surfaces

## Backend pattern
When the data already lives in SQLite and the dashboard is a monolithic `serve.py` + `index.html` app:

### 1) Extend the existing run/session drill-down model instead of inventing a second filter system
Add the new dimensions to the existing filter builder and query-string contract.

Useful extra filter:
- `tool_name`

Practical pattern:
- keep run/session filters in one helper
- add request-level filters in a second helper that joins `llm_calls` to `runs`
- make tool filters work through `EXISTS (...)` on `tool_calls` rather than denormalizing everything into `runs`

### 2) Add forensic APIs
Recommended minimal endpoints:
- `/api/requests`
- `/api/request-detail`
- `/api/tool-analytics`
- `/api/error-center`
- `/api/provider-health`

Recommended shapes:

#### `/api/requests`
Return recent LLM-call rows joined to run/session metadata:
- `id`, `ts`, `session_id`
- `provider`, `model`
- token fields (`tokens_in`, `tokens_out`, `cache_read_tokens`, `cache_write_tokens`, `reasoning_tokens`)
- `cost_usd`, `latency_ms`, `estimated`
- run-side fields like `platform`, `cron_job_id`, `status`
- counts and hidden-deleted metadata

#### `/api/request-detail`
Return one request plus surrounding session context:
- the request row itself
- session-level totals for all LLM calls in that session
- sibling LLM calls from the same session
- tool activity from the same session

This is the fastest path from “one odd request” to “what was happening around it?”

#### `/api/tool-analytics`
Aggregate `tool_calls` by tool:
- total calls
- sessions
- ok / failed counts
- failure %
- avg/max latency
- last seen
- top-level summary block for cards

#### `/api/error-center`
Combine two error surfaces:
- non-`ok` run statuses from `runs`
- failed tool calls from `tool_calls`

Good response shape:
- summary cards
- grouped run statuses
- grouped failed tools
- a recent incident feed that merges run-status failures and tool failures

#### `/api/provider-health`
Compare provider behavior in the current window against the previous equal window.

Good fields:
- provider
- current call count and previous call count
- traffic delta %
- estimated-call %
- failed-run %
- current/previous average latency and latency delta %
- current cost
- health state: `ok`, `warn`, `error`
- anomaly labels such as `estimated-heavy`, `run-failures`, `latency-spike`, `traffic-spike`, `traffic-drop`

For an `All time` dashboard selector, use a bounded operational comparison window such as last 24h vs previous 24h; all-time anomaly comparison is not meaningful.

## SQL/querying notes

### Request filtering
For request tables, join `llm_calls lc` to `runs r` and filter by request timestamp (`lc.ts`), not only run start time.

### Tool-aware drill-down
For run/request surfaces, tool filtering is cleanest as:
- `EXISTS (SELECT 1 FROM tool_calls tc WHERE tc.session_id = ... AND tc.tool_name = ?)`

### Deleted-session soft-hide
If the dashboard already soft-hides deleted Hermes sessions in `/api/runs`, carry the same semantics into `/api/requests`, `/api/tool-analytics`, and `/api/error-center`.
Do not let new forensic tables quietly re-expose deleted session rows.

## Frontend pattern

### 1) Partition dense forensic surfaces into internal pages
Avoid making one Breakdown page carry every operator surface. Keep one dashboard route, but add internal tabs/pages when the forensic widgets become dense.

Recommended tab split:
- **Home**: top KPIs, budgets, high-level cost/tool/provider charts, recent sessions
- **Breakdown**: token breakdown, provider cost/token breakdown, cache efficiency, model tokens, daily tokens, combined daily token/model chart, session investigation
- **Request**: provider health/anomaly signals + LLM request forensics
- **Tool**: tool analytics
- **Error**: error center, run status groups, failed tools, recent incidents

When moving sections, remove them from the old page entirely; do not leave duplicates lower down.

### 2) Reuse the existing right-drawer pattern
If session detail already exists, create a parallel request drawer instead of inventing a totally different modal.

Good request drawer sections:
- request metrics
- session totals
- sibling session LLM calls
- session tool activity

### 3) Keep one shared drill-down state
The new surfaces should feed the same `currentDrilldown` object as the rest of the dashboard.
Useful shared keys:
- `provider`
- `model`
- `day`
- `platform`
- `status`
- `cron_job_id`
- `tool_name`
- `q`

### 4) Make tool names clickable everywhere
If the dashboard adds `tool_name` filtering, expose it in:
- tool analytics rows
- error center failed-tool rows
- session detail tool-call rows
- request drawer session-tool rows

That keeps the whole forensic workspace connected.

### Dense table legibility
For model/provider-heavy telemetry tables, do not let long IDs wrap into ugly multi-line chips.

Use single-line chip styling:
- `display: inline-flex`
- `white-space: nowrap`
- `overflow: hidden`
- `text-overflow: ellipsis`
- bounded `max-width`
- full value in `title`

Apply consistently in:
- Recent Sessions model cells
- Investigation Workspace provider/model cells
- LLM Request Forensics provider/model cells
- request/session drawers
- provider/model mix tables

## Verification pattern
Do not stop at API implementation.

### Required checks
- targeted pytest for dashboard helpers/APIs
- `py_compile` or equivalent syntax check
- lint on edited backend/tests
- dashboard service restart
- live browser verification on the real served page
- browser console check for JS errors

### Live browser checks that matter
- Breakdown renders the new section headings
- request table has real rows
- clicking a request row opens the request drawer
- request drawer shows all expected sections
- tool analytics rows drill down correctly
- error center shows grouped failures/incidents
- zero console errors after interactions

## Good test additions
For a `serve.py`-style dashboard test file, add helper-level tests for:
- request filtering by `status` + `tool_name`
- request-detail session context payload
- tool analytics failed-call aggregation
- error-center merged incidents / interrupted-or-error summaries

## Gap-analysis against the main Hermes dashboard
When the user asks what telemetry should add next, first inspect the main Hermes dashboard (often port 9120 on this host) and avoid duplicating built-in surfaces.

Main Hermes dashboard may already cover:
- Analytics: daily tokens, daily breakdown, per-model breakdown, top skills
- Models: current model controls, per-model sessions/tokens/cache/reasoning/API/tool counts
- Cron: schedule/last/next/status/errors
- Cronalytics: cron runs, cost/tokens/pace, jobs breakdown
- Logs: agent/gateway/error log filters
- System: CPU/memory/disk/load/gateway/memory/credential status

Telemetry should therefore specialize in cross-store forensic correlation and cost/request/tool operator truth. Good follow-up features:
- dashboard reconciliation panel: Hermes sessions/messages/models vs telemetry runs/API calls, including deleted-session mismatches and stale running telemetry rows
- model efficiency score: cost per 1M tokens, output/input ratio, cache hit %, tool calls/API call, latency, failure rate
- cron failure/waste center: timed out jobs, failed jobs, no-agent run noise, wasted cost/tokens, last-success age
- log-linked error center: correlate DB incidents with nearby `ERROR`, `Traceback`, `timeout`, rate-limit, auth log lines
- request latency anomaly chart: p50/p95/slowest requests and provider/model spikes
- tool failure heatmap: tool × model, tool × platform, tool × cron job
- skill cost/usefulness analytics: tokens/cost per loaded skill and expensive/low-signal skill loads
- budget forecast/runway: projected daily/monthly spend and contributors to future breach
- retry/duplicate request detector: repeated API calls in the same session that suggest provider retries or stuck loops
- session quality labels: normal, long-running, high-cache, high-cost, many-tools, failed-tools, interrupted, likely-stuck

Implemented follow-up bundle after Request/Tool/Error pages:

### Model efficiency score
Add `/api/model-efficiency` and render it on **Breakdown** near model/cache analytics. Good columns:
- score
- provider/model
- API calls and total tokens
- cost per 1M tokens
- output/input ratio
- cache hit share
- tool calls per API call
- failure %
- avg latency

Simple practical scoring: start at 100, penalize failure rate, high latency, and estimated-heavy usage; add a small cache-hit bonus. Label it clearly as an operator heuristic, not a scientific benchmark.

### Tool failure heatmap
Add `/api/tool-failure-heatmap` and render it on **Tool** below Tool Analytics. Group failures by:
- tool × model × platform × cron

Good columns:
- tool
- model
- platform
- cron job
- calls
- failed calls
- failure %
- avg latency
- last seen

Clicking a heatmap row should feed the shared drill-down state, usually `tool_name + model`.

### Cron failure / waste center
Add `/api/cron-failure-waste` and render it on **Error** above the generic Error Center. Good columns:
- cron job
- risk labels
- runs / failed / timeout
- failed tool calls
- wasted tokens and wasted cost from non-ok runs
- last success age
- avg duration

Risk labels that worked well: `timeout`, `failure-rate`, `tool-failures`, `never-success`, `stale-success`.

### Page-title cleanup from screenshot feedback
If internal tabs already show the active page and the content starts with a floating duplicate word like `Home` or `Breakdown`, remove the in-content `.page-title` entirely. Verify `document.querySelectorAll('.page-title')` is empty and that the cards move up cleanly.

Still useful future follow-ups:
1. log-linked error center
2. budget forecast/runway
3. retry/duplicate request detector
4. session quality labels
5. skill cost/usefulness analytics

## User-preference note
For this user, do not call the batch complete from code inspection alone.
The feature is only done after:
- tests pass
- service restarts
- browser interaction proves the new sections and drawers work live
- console is clean
