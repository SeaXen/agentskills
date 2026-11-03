# Hermes telemetry home first-paint and KPI correctness

Use this note when the home page is slow or when `Messages` / `Cron runs` / `Tool calls` look obviously wrong.

## Correct source split
Do not force one DB to answer all KPI questions.

- `Messages`:
  - source: `~/.hermes/state.db`
  - table: `messages`
  - count only non-empty `user` + non-empty `assistant`
  - ignore `tool`
  - ignore empty assistant placeholders
- `LLM calls`, token totals, cost, savings:
  - source: `~/.hermes/telemetry/telemetry.db`
  - table: `llm_calls`
- `Tool calls`:
  - source: `telemetry.db`
  - table: `tool_calls`
  - prefer real event rows, not `SUM(runs.tool_calls)`
- `Sessions`:
  - source: `telemetry.db`
  - table: `runs`
- `Cron runs`:
  - source of truth for count: Hermes scheduler history
  - files: `~/.hermes/cron/jobs.json` and `~/.hermes/cron/output/<job_id>/*.md`
  - reason: script-only / `no_agent` cron jobs may have no telemetry rows
  - token/cost columns can still stay telemetry-backed

## Fast inspection probes
Use these probes before changing semantics:

### Messages by role
```sql
select role, count(*) from messages group by role order by role;
```

### Real user+assistant message count
```sql
select
  sum(case when role='user' and trim(coalesce(content,''))!='' then 1 else 0 end)
+ sum(case when role='assistant' and trim(coalesce(content,''))!='' then 1 else 0 end)
as messages
from messages;
```

### Telemetry totals
```sql
select count(*) from llm_calls;
select count(*) from tool_calls;
select count(*) from runs;
select count(*) from runs where cron_job_id is not null and cron_job_id!='';
```

### Scheduler-backed cron run reality check
- sum `repeat.completed` across `jobs.json`
- count `*.md` files under each `~/.hermes/cron/output/<job_id>/`
- if all-time view is requested, use the larger trustworthy scheduler-history count per job

## Home first-paint performance pattern
If Home feels slow, the common mistake is fetching data for hidden tabs during the first render.

Bad pattern:
- one giant `Promise.all([...])` for Home + Breakdown + Request + Tool + Error payloads

Preferred pattern:
- Home fetches only:
  - summary
  - cron
  - providers
  - recent runs
  - budget
- Breakdown / Request / Tool / Error fetch only when that page is active

## Defer the trend chart if needed
If `/api/daily-token-chart` is slower than the rest of Home:
1. return a lightweight `summary.home_metrics`
2. render KPI strip immediately from `summary.home_metrics`
3. show a loading shell in the trend card
4. fetch `/api/daily-token-chart` after first paint
5. replace the shell with the real chart when ready

## Fields worth exposing in `summary.home_metrics`
Keep these aligned with the chart header so the KPI strip does not flash fake placeholders:
- `total_tokens`
- `api_calls`
- `request_runs`
- `tool_calls`
- `cron_job_runs`
- `user_messages`
- `assistant_messages`
- `message_runs`
- `cost_usd`
- `estimated_savings_usd`
- `savings_pct`

## Public-PR honesty rule
It is acceptable for one dashboard surface to use multiple sources when the semantics are genuinely different.
The problem is not "two sources" by itself.
The problem is mislabeled metrics.

If counts come from mixed sources, make the labels and explanations honest:
- `Messages` = actual conversation messages from state DB
- `Cron runs` = scheduler executions
- `Tool calls` = tool-call events
- `Sessions` = Hermes runs

Do not collapse them into one approximate source just to say everything came from the same DB.
