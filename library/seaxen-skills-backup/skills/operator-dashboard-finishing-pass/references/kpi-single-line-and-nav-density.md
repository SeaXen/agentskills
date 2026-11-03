# KPI single-line + nav density (operator dashboards)

Session class: multi-page Hermes/ops analytics UIs (AceRoute-style) where the user complains cards/KPIs look unprofessional and wrap badly — then wants a full multi-sector upgrade toward 10/10.

## User signals
- “stats cards show like this arrange and give in 1 line like home page”
- “complete as much as phase possible and make it 10/10 in all sector”
- Orphan last KPI on row 2 is a hard fail, even if data is correct

## Root causes seen
1. Mixed grid rules: some pages `repeat(8, …)`, others `auto-fit minmax(150px,1fr)` → inconsistent wrap
2. Mobile CSS (`max-width:1024px`) rewrote KPI containers with wrapping grids and fought desktop rules
3. Hand-rolled per-page KPI HTML instead of one `statCards()` builder
4. 16 peer top-nav pills wrapping to 2 rows
5. Insight/filter chips wrapping into multi-line soup
6. Session titles leaking `<think>…</think>` into chips/tables
7. Default duration = all-time (`36500`) → nonsense +100% deltas
8. Header `Loading...` only updated on one page
9. Long Search analytics as infinite card stack (no subtabs)
10. Day windows in UTC while host TZ is local (Asia/Dhaka) — wrong “Today”
11. Docker: `./static` mounted live but Python baked into image → CSS/JS fixed, backend TZ/meta unchanged until mount/rebuild

## Fix order

### Pass A — layout (user-visible first)
1. Global KPI CSS — flex nowrap + equal flex children + overflow-x (see SKILL.md)
2. Mobile override — same one-line flex; never reintroduce wrap grids for KPI ids
3. Unify builders — every page calls `statCards`
4. Nav — primary 6–8 + More ▾
5. Insight + filter chips — nowrap scroll rows
6. cleanTitle / clean_title — client + server
7. Default 7d — bump localStorage duration key version
8. markUpdated(ts) — every page paint
9. Cache-bust static assets (`?v=N`)

### Pass B — data trust + security
1. Local midnight windows — `_since_ts` from local midnight; SQL `date(col, 'unixepoch', 'localtime')`; compose `TZ` + `ACEROUTE_TZ`
2. Optional write auth — `ACEROUTE_API_KEY` on POSTs; UI Settings stores key; writes use `X-AceRoute-Key` via shared `apiFetch`
3. Env for search backend URL — no hardcoded LAN IPs
4. `/api/meta` — timezone, auth_required, version (no secrets)

### Pass C — Search / long pages
1. Split dump into subtabs: Overview · Providers · Errors · Hermes · Test
2. Hide inactive panels with `.search-tab-panel` / `.active`
3. Persist selected tab in localStorage

### Pass D — deploy correctness
1. If only `./static` is bind-mounted, Python changes do not go live until image rebuild **or** bind-mount each `*.py`
2. After backend change: recreate container, wait healthz, then smoke
3. Keep a short smoke script (no long network tests): healthz, meta, 2–3 dashboards, static assets, timezone field

## Local day window (Python sketch)
```python
now = datetime.now(ZoneInfo(ACEROUTE_TZ))
start = now.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=N-1)
since_ts = start.timestamp()
# SQLite: date(started_at, 'unixepoch', 'localtime')
# Compose: TZ=Asia/Dhaka, ACEROUTE_TZ=Asia/Dhaka
```

## Verify
- Hard refresh after asset bumps
- Screenshot Sessions (+ one other 8-KPI page): one row only
- Search subtabs switch without showing entire dump
- `days=1` payload includes timezone + Today-like label; timeline days match local calendar
- Smoke script green; no JS console errors
- If meta/TZ still old after “fix”: container is on baked Python — check mounts (`dashboard-ui-operations` → `references/static-mount-vs-baked-python.md`)

## Related
- Parent skill: `operator-dashboard-finishing-pass`
- Deploy ops: `dashboard-ui-operations`
- Design lens: `impeccable`
