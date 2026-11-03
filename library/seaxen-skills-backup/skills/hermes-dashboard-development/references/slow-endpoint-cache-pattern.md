# Slow-Endpoint Cache + Frontend Defer — Annotated Reference

A working recipe for taking a dashboard endpoint that takes 5-30s and making
the first-paint load time bound by the fastest endpoints instead. The
`hermes-telemetry` API used this pattern on `api_model_efficiency` to take
home-page first-paint from 21.2s to 6.7s.

## When to use this pattern

Symptoms that say "use it":

- One or two endpoints take >=1s (often 5-30s)
- The rest of the home-page endpoints are <100ms
- The dashboard's `Loaded 5.0s` turns into `Loaded 20s+` once telemetry grows
- Browser shows `Loading…` for seconds even though most data is in memory
- The slow query joins two large tables (`tool_calls ⨝ llm_calls` etc.)

If the whole page is uniformly slow, you have a different problem (likely
SQLite index missing, or a query without time-window filter).

## Step 1: confirm `ThreadingHTTPServer` is in use

`http.server.HTTPServer` is single-threaded. One slow request queues every
other request including the homepage HTML.

Check:
```bash
grep -n "ThreadingHTTPServer\|HTTPServer(" dashboard/serve.py
```

Expected:
```
33:from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
2872:    server = ThreadingHTTPServer((host, port), Handler)
```

If you see `HTTPServer(` (no `Threading`), change the import and the boot:

```python
# before
from http.server import HTTPServer, SimpleHTTPRequestHandler
...
server = HTTPServer((host, port), Handler)

# after
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
...
server = ThreadingHTTPServer((host, port), Handler)
```

## Step 2: build the cache class

Pattern: a singleton class with a daemon thread that pre-computes the
slow query for the common window presets and writes JSON to a SQLite cache
table. Request handlers read the cache; cold reads compute + seed.

### Backend: `SlowEndpointCache` (drop-in for any endpoint)

```python
import time
import threading
from datetime import datetime, timezone
import sqlite3
import json

class SlowEndpointCache:
    _instance = None
    _lock = threading.Lock()

    DEFAULT_REFRESH_SECONDS = 300
    DEFAULT_WINDOWS = (24, 168, 720, 0)  # 1d, 1w, 30d, all
    DEFAULT_LIMITS = (50,)

    def __init__(self, db_path):
        self._conn = sqlite3.connect(
            str(db_path), isolation_level=None, check_same_thread=False
        )
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA busy_timeout=5000")
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS slow_endpoint_cache (
                cache_key TEXT PRIMARY KEY,
                window_hours INTEGER NOT NULL,
                include_deleted INTEGER NOT NULL,
                limit_n INTEGER NOT NULL,
                payload_json TEXT NOT NULL,
                rows_count INTEGER NOT NULL,
                built_at TEXT NOT NULL
            )
        """)
        self._cond = threading.Condition(threading.Lock())
        self._stop = threading.Event()
        self._refreshing = False
        self._last_refresh_at = None
        self._last_refresh_seconds = 0.0
        self._thread = threading.Thread(
            target=self._run, name="slow-endpoint-cache", daemon=True
        )

    @classmethod
    def instance(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls(DB_PATH)
                cls._instance.start()
            return cls._instance

    def start(self):
        if not self._thread.is_alive():
            self._thread.start()

    def _run(self):
        try:
            self._refresh_all()
        except Exception:
            logger.exception("initial slow-endpoint cache refresh failed")
        while not self._stop.is_set():
            with self._cond:
                self._cond.wait(timeout=self.DEFAULT_REFRESH_SECONDS)
            if self._stop.is_set():
                break
            try:
                self._refresh_all()
            except Exception:
                logger.exception("scheduled slow-endpoint cache refresh failed")

    def _key(self, window_hours, include_deleted, limit):
        return f"{int(window_hours)}|{int(bool(include_deleted))}|{int(limit)}"

    def _cache_rows(self, window_hours, include_deleted, limit):
        row = self._conn.execute(
            "SELECT payload_json, built_at FROM slow_endpoint_cache WHERE cache_key = ?",
            (self._key(window_hours, include_deleted, limit),),
        ).fetchone()
        if not row:
            return None
        return json.loads(row["payload_json"])

    def _write_cache(self, window_hours, include_deleted, limit, payload):
        with self._cond:  # serialize concurrent writes
            self._conn.execute(
                """
                INSERT INTO slow_endpoint_cache
                    (cache_key, window_hours, include_deleted, limit_n,
                     payload_json, rows_count, built_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(cache_key) DO UPDATE SET
                    payload_json = excluded.payload_json,
                    rows_count = excluded.rows_count,
                    built_at = excluded.built_at
                """,
                (
                    self._key(window_hours, include_deleted, limit),
                    int(window_hours),
                    int(bool(include_deleted)),
                    int(limit),
                    json.dumps(payload, default=str),
                    len(payload),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )

    def get_rows(self, window_hours, include_deleted, limit):
        cached = self._cache_rows(window_hours, include_deleted, limit)
        if cached is not None:
            return cached
        rows = self._compute_live(window_hours, include_deleted, limit)
        try:
            self._write_cache(window_hours, include_deleted, limit, rows)
        except Exception:
            logger.exception("failed to seed slow_endpoint_cache")
        return rows

    def status(self):
        rows = self._conn.execute(
            "SELECT cache_key, window_hours, include_deleted, limit_n, rows_count, built_at "
            "FROM slow_endpoint_cache ORDER BY window_hours, include_deleted, limit_n"
        ).fetchall()
        return {
            "refresh_interval_seconds": self.DEFAULT_REFRESH_SECONDS,
            "last_refresh_at": self._last_refresh_at,
            "last_refresh_seconds": (
                round(self._last_refresh_seconds, 3) if self._last_refresh_seconds else None
            ),
            "entries": [dict(r) for r in rows],
        }

    def _refresh_all(self):
        if self._refreshing:
            return
        self._refreshing = True
        started = time.monotonic()
        try:
            for wh in self.DEFAULT_WINDOWS:
                for include_deleted in (False, True):
                    for limit in self.DEFAULT_LIMITS:
                        try:
                            rows = self._compute_live(wh, include_deleted, limit)
                            self._write_cache(wh, include_deleted, limit, rows)
                        except Exception:
                            logger.exception(
                                "refresh failed (window=%s include_deleted=%s)",
                                wh, include_deleted,
                            )
            with self._cond:
                self._last_refresh_seconds = time.monotonic() - started
                self._last_refresh_at = datetime.now(timezone.utc).isoformat()
        finally:
            self._refreshing = False

    def _compute_live(self, window_hours, include_deleted, limit):
        # Replace this with the actual heavy query.
        # Return a list of dicts.
        raise NotImplementedError
```

Wire it into `main()` so the daemon thread primes the cache before the
HTTP server starts accepting traffic:

```python
def main(argv=None):
    ...
    SlowEndpointCache.instance()  # daemon thread; non-blocking
    server = ThreadingHTTPServer((host, port), Handler)
    ...
```

### Handler changes

```python
def api_slow_endpoint(window_hours=0, limit=50, include_deleted=False):
    return SlowEndpointCache.instance().get_rows(
        window_hours=window_hours, include_deleted=include_deleted, limit=limit
    )

def api_slow_endpoint_cache_status():
    return SlowEndpointCache.instance().status()
```

### Admin endpoints (for ops visibility)

```python
# in Handler.do_GET:
if path == "/api/slow-endpoint/cache/status":
    return self._json(api_slow_endpoint_cache_status())

# in Handler.do_POST:
if path == "/api/slow-endpoint/refresh":
    parsed_qs = parse_qs(parsed.query)
    wh_raw = parsed_qs.get("hours", [None])[0]
    include_deleted = parsed_qs.get("include_deleted", ["0"])[0] in {"1", "true", "yes"}
    # ...refresh logic...
    return self._json(result)
```

## Step 3: defer the endpoint from initial `Promise.all`

The browser fires all endpoints in parallel. The slowest one dominates
first-paint. Move the slow one out of the initial batch.

```js
// BEFORE: blocks first-paint on /api/slow-endpoint
const [summary, ...otherFast, slowData] = await Promise.all([
  fetchJSON(`/api/summary?hours=${hours}`),
  // ...
  fetchJSON(`/api/slow-endpoint?hours=${hours}&limit=50`),  // 13s
  // ...
]);

// AFTER: first-paint is bounded by the fastest endpoints
const [summary, ...otherFast] = await Promise.all([
  fetchJSON(`/api/summary?hours=${hours}`),
  // fetchJSON(`/api/slow-endpoint?hours=${hours}&limit=50`),  // removed
  // ...
]);
```

For pages that need the data (e.g. a breakdown page), render a placeholder
card first, then lazy-fetch and swap the real card in after first-paint:

```js
// In the breakdown-page render branch:
const mountId = 'slowEndpointMount';
const placeholder = `<div id="${mountId}" class="loading-shell" style="min-height:120px">Loading…</div>`;
html += renderTableCard('slowEndpointTable', 'Slow Endpoint', placeholder);

// After app.innerHTML = html; the lazy fetch + swap:
fetchJSON(`/api/slow-endpoint?hours=${hours}&limit=50`)
  .then((rows) => {
    if (requestId !== latestLoadRequestId) return;  // stale guard
    const mount = document.getElementById(mountId);
    if (!mount) return;
    const card = mount.closest('.table-card');
    const tmp = document.createElement('div');
    tmp.innerHTML = renderTableCard('slowEndpointTable', 'Slow Endpoint',
      renderSlowEndpointRows(rows));
    card.replaceWith(tmp.firstElementChild);
  })
  .catch((err) => {
    const mount = document.getElementById(mountId);
    if (mount) mount.innerHTML = `<div class="text-muted">Unavailable: ${err.message}</div>`;
  });
```

## Step 4: test recipe

```python
def test_slow_endpoint_cache_hits_and_refresh(tmp_path, serve_module):
    import time
    now = db._utcnow()  # use real now, not a pinned time, so 24h filter passes
    db.start_run("sess-test", model="gpt-5.4", platform="cli")
    db.record_llm_call("sess-test", now, "gpt-5.4", "openai-codex", 1000, 200, 0.01, 120)
    db.end_run("sess-test", "ok")

    # First call: live compute + seed cache.
    first = serve_module.api_slow_endpoint(window_hours=24, include_deleted=True)
    assert any(row["model"] == "gpt-5.4" for row in first), first

    # Second call: must hit cache.
    started = time.monotonic()
    second = serve_module.api_slow_endpoint(window_hours=24, include_deleted=True)
    cache_elapsed = time.monotonic() - started
    assert second == first
    assert cache_elapsed < 0.5, f"cache hit too slow: {cache_elapsed:.3f}s"

    # Status endpoint reports the entry.
    status = serve_module.api_slow_endpoint_cache_status()
    assert any(e["window_hours"] == 24 and e["include_deleted"] is True
               for e in status["entries"])
    assert status["refresh_interval_seconds"] == 300

    # Force-refresh endpoint rebuilds the cache.
    refreshed = serve_module.api_slow_endpoint_refresh(window_hours=24,
                                                     include_deleted=True)
    assert refreshed["window_hours"] == 24
    assert refreshed["refreshed_at"]
```

**Critical:** use `now = db._utcnow()` for the recorded timestamp. Do **not**
pin a fake time — the `_since_clause(window_hours, "ts")` filter uses
`datetime.now(timezone.utc)` directly, so a hardcoded past timestamp will
be filtered out by the time window.

## Live verification commands

```bash
# Cache-hit timing
curl -s -o /dev/null -w "/api/slow-endpoint?hours=24 %{http_code} %{time_total}s\n" \
  "http://127.0.0.1:8009/api/slow-endpoint?hours=24&limit=50"
# Expected: <0.005s (was 13s before)

# Cache status
curl -s "http://127.0.0.1:8009/api/slow-endpoint/cache/status" | python3 -m json.tool
# Expected: 8 entries (4 windows x 2 include_deleted), last_refresh_at fresh

# Force refresh
curl -s -X POST "http://127.0.0.1:8009/api/slow-endpoint/refresh?hours=24"
# Expected: 200 with elapsed_seconds
```

## Numbers from `hermes-telemetry`

| Metric | Before | After |
|---|---|---|
| First-paint (live browser) | 21.2s | 6.7s |
| `/api/model-efficiency?hours=0` | 13s+ | 0.001s (cache hit) |
| `/api/model-efficiency?hours=24` | 5s | 0.001s (cache hit) |
| Initial daemon refresh (cold) | n/a | ~110s for 8 entries |
| Refresh interval | n/a | 300s |

## Why this is better than the alternatives

- **A. Defer only** — leaves the heavy query running on the user's first
  click. If the user opens the breakdown page they wait 13s.
- **B. Cache only** — first request still slow (cold cache), then fast.
  Acceptable but worse than A+B.
- **C. Shrink the default window** — band-aid. The metric is now wrong
  for "All time".
- **A + B (this recipe)** — first request is fast (deferred), every
  subsequent request is fast (cached), admin has visibility into cache
  state. The 5-min background refresh keeps data fresh enough for ops
  dashboards.
