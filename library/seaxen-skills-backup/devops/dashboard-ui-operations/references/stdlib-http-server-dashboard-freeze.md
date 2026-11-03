# stdlib HTTP server + slow dashboard endpoint freeze pattern

Symptom: dashboard SPA sits on its `Loading…` overlay indefinitely,
even though the server is up and the SQLite DB is fine. `curl` to
the homepage also hangs past its own timeout. The process shows
`Threads: 1` and `R (running)`.

Two compounding root causes. Patch both, not just one.

---

## 1. stdlib `HTTPServer` is single-threaded

`http.server.HTTPServer` accepts one connection at a time. Any slow
endpoint queues every other request, including the SPA shell at `/`.

```python
# BEFORE — one thread, every slow request freezes the SPA
from http.server import HTTPServer, SimpleHTTPRequestHandler
server = HTTPServer((host, port), Handler)

# AFTER — thread-per-request, zero new deps
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
server = ThreadingHTTPServer((host, port), Handler)
```

Always use `ThreadingHTTPServer` for a dashboard that:
- serves an SPA shell at `/`
- has any endpoint that may run a slow query
- has header auto-refresh or parallel tab fetches

If you write dashboards as a single-file `serve.py` over stdlib,
this is the default you want.

---

## 2. Heavy SQLite aggregate inside an auto-refreshed endpoint

A heavy aggregate in an endpoint that the home page polls will
block the UI even after threading is fixed. Typical offenders:

- correlated subquery joining 3+ tables once per outer row
  (e.g. `tool_calls ⨝ runs ⨝ llm_calls` per model group → 23M rows)
- full-scan `GROUP BY` over the whole `llm_calls` table when no
  time filter is applied
- missing index on a join / filter column

Verify with `EXPLAIN QUERY PLAN` and watch for `SCAN` markers without
an `INDEX` covering the WHERE.

Common fix shapes:
- replace the correlated subquery with a non-correlated aggregate
  joined to the outer query, or aggregate in Python over a small
  secondary query
- add an index on the join / filter column
- clamp the default `window_hours` (default to 24 instead of 0)
- cache results on a short TTL

---

## Verification recipe

When a dashboard appears stuck:

1. From the host, hit `/` and one slow-looking endpoint with `curl`:
   ```
   curl -sS -m 4 -o /dev/null -w '%{http_code} %{time_total}\n' URL
   ```
   - both hang past `time_total` 4s and never return → threading issue
   - only the heavy endpoint hangs → SQL is the issue

2. Inspect the live process:
   ```
   ps -o pid,pcpu,pmem,etime,stat,cmd -p <pid>
   ```
   - `Threads: 1` + `R (running)` + high CPU = busy single loop
   - many threads + low CPU = waiting on a slow query

3. Query the SQLite file directly with python:
   ```
   python3 -c "import sqlite3, time
   con = sqlite3.connect('/path/to/db', timeout=5)
   con.execute('PRAGMA query_only=ON')
   t0 = time.perf_counter()
   print(con.execute('SELECT ...').fetchall())
   print(round(time.perf_counter()-t0, 3), 's')"
   ```

4. If the dashboard is a plugin (`dashboard/plugin_api.py`), confirm
   the host service was restarted after the plugin was last updated.
   Plugin routes are mounted at boot; an API change on disk is
   invisible until the dashboard process restarts. Verify with
   `gh pr check <pr>` or `gh pr view <pr> --json state`.

---

## Companion fixes that look unrelated

These present as the same freeze and are easy to miss:

- **Plugin API routes return 404 even though the plugin shows in
  the sidebar.** The plugin was discovered (manifest scan is
  reactive) but its `plugin_api.py` was not mounted (mount only
  happens at boot). Restart the host service.

- **One slow request plus auto-refresh queues work forever.**
  Even with `ThreadingHTTPServer`, a 30s endpoint polled every 30s
  piles up. Verify each auto-refreshed endpoint independently with
  `curl -m 4` before shipping.

- **The browser reports `Loading telemetry dashboard…` but the
  page never advances.** That is the SPA's own load-state string,
  not a real load failure. Use `curl` to confirm whether requests
  are still in flight or have actually hung.