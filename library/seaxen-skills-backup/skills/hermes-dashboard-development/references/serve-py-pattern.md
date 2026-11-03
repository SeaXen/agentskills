# serve.py Pattern (Annotated)

This is a working template from `hermes-telemetry` dashboard. Copy and adapt for new plugin dashboards.

```python
#!/usr/bin/env python3
"""Plugin dashboard server — stdlib only."""

import argparse
import json
import logging
import os
import sqlite3
import sys
import threading
from datetime import datetime, timedelta, timezone
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import parse_qs, urlparse

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765

logger = logging.getLogger("my_plugin.dashboard")

# ---------------------------------------------------------------------------
# DB path
# ---------------------------------------------------------------------------
DB_PATH = (
    Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")) / "telemetry" / "telemetry.db"
)

_local = threading.local()

def _conn():
    if not getattr(_local, "c", None):
        _local.c = sqlite3.connect(str(DB_PATH), isolation_level=None)
        _local.c.row_factory = sqlite3.Row
        _local.c.execute("PRAGMA busy_timeout=5000")
    return _local.c

def _rows(sql, params=()):
    return [dict(r) for r in _conn().execute(sql, params).fetchall()]

def _one(sql, params=()):
    r = _conn().execute(sql, params).fetchone()
    return dict(r) if r else {}

# ---------------------------------------------------------------------------
# Time window helper — single source of truth for all endpoints
# ---------------------------------------------------------------------------
def _since_clause(window_hours, col="started_at"):
    """Return SQL WHERE clause for time window. 0 = all time (no filter)."""
    wh = int(window_hours)
    if wh == 0:
        return "1=1"
    return f"{col} >= datetime('now', '-{wh} hours')"

# ---------------------------------------------------------------------------
# API handlers
# ---------------------------------------------------------------------------
def api_summary(window_hours=24):
    since_clause = _since_clause(window_hours, "started_at")
    since_clause_ts = _since_clause(window_hours, "ts")

    runs = _one(f"""
        SELECT
            COUNT(*) AS total_runs,
            SUM(CASE WHEN status='ok' THEN 1 ELSE 0 END) AS ok_runs,
            SUM(CASE WHEN status NOT IN ('ok','running') THEN 1 ELSE 0 END) AS failed_runs,
            SUM(tokens_in) AS tokens_in,
            SUM(tokens_out) AS tokens_out,
            ROUND(SUM(cost_usd), 6) AS cost_usd,
            AVG(duration_ms) AS avg_duration_ms,
            SUM(tool_calls) AS tool_calls,
            SUM(estimated_llm_calls) AS estimated_llm_calls
        FROM runs WHERE {since_clause}
    """)

    llm = _one(f"""
        SELECT COUNT(*) AS api_calls, AVG(latency_ms) AS avg_latency_ms
        FROM llm_calls WHERE {since_clause_ts}
    """)

    top_tools = _rows(f"""
        SELECT tool_name, COUNT(*) AS calls,
               SUM(CASE WHEN ok=0 THEN 1 ELSE 0 END) AS failures,
               AVG(latency_ms) AS avg_ms
        FROM tool_calls tc
        JOIN runs r ON tc.session_id = r.session_id
        WHERE {_since_clause(window_hours, "r.started_at")}
        GROUP BY tool_name ORDER BY calls DESC LIMIT 10
    """)

    # Daily cost chart — unbounded for all-time
    daily_window = int(window_hours)
    if daily_window == 0:
        daily_cost = _rows("""
            SELECT DATE(started_at) AS day,
                   ROUND(SUM(cost_usd), 4) AS cost,
                   COUNT(*) AS runs
            FROM runs
            GROUP BY DATE(started_at)
            ORDER BY day
        """)
    else:
        daily_cost = _rows(f"""
            SELECT DATE(started_at) AS day,
                   ROUND(SUM(cost_usd), 4) AS cost,
                   COUNT(*) AS runs
            FROM runs
            WHERE started_at >= datetime('now', '-{daily_window // 24} days')
            GROUP BY DATE(started_at)
            ORDER BY day
        """)

    return {
        "window_hours": int(window_hours),
        "runs": runs,
        "llm": llm,
        "top_tools": top_tools,
        "daily_cost": daily_cost,
    }

def api_token_breakdown(window_hours=24):
    since_clause_ts = _since_clause(window_hours, "ts")
    # COALESCE each SUM individually: SUM() returns NULL when ALL rows are NULL
    # (e.g., reasoning_tokens for models that don't emit it).
    # Outer COALESCE alone doesn't fix: NULL + 0 = NULL.
    return _one(f"""
        SELECT
            COALESCE(SUM(tokens_in), 0) AS tokens_in,
            COALESCE(SUM(tokens_out), 0) AS tokens_out,
            COALESCE(SUM(cache_read_tokens), 0) AS cache_read_tokens,
            COALESCE(SUM(cache_write_tokens), 0) AS cache_write_tokens,
            COALESCE(SUM(reasoning_tokens), 0) AS reasoning_tokens,
            COALESCE(SUM(tokens_in), 0) + COALESCE(SUM(tokens_out), 0)
                + COALESCE(SUM(cache_read_tokens), 0) + COALESCE(SUM(cache_write_tokens), 0)
                + COALESCE(SUM(reasoning_tokens), 0) AS total_tokens
        FROM llm_calls WHERE {since_clause_ts}
    """)

# ... other endpoints (api_cron, api_providers, api_runs, api_budget, api_budget_update)

# ---------------------------------------------------------------------------
# HTTP Handler
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path == "/api/summary":
            qs = parse qs(parsed.query)
            return self._json(api_summary(qs.get("hours", [24])[0]))

        if path == "/api/cron":
            qs = parse_qs(parsed.query)
            return self._json(api_cron(qs.get("hours", [168])[0]))

        if path == "/api/providers":
            qs = parse_qs(parsed.query)
            return self._json(api_providers(int(qs.get("hours", [24])[0])))

        if path == "/api/runs":
            qs = parse_qs(parsed.query)
            return self._json(api_runs(qs.get("limit", [50])[0]))

        if path == "/api/budget":
            return self._json(api_budget())

        if path == "/api/token-breakdown":
            qs = parse_qs(parsed.query)
            return self._json(api_token_breakdown(int(qs.get("hours", [24])[0])))

        if path == "/" or path == "/index.html":
            html = (SCRIPT_DIR / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html)
            return

        fpath = SCRIPT_DIR / path.lstrip("/")
        if fpath.is_file():
            super().do_GET()
            return

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not Found")

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path == "/api/budget":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                payload = json.loads(body) if body else {}
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            result = api_budget_update(payload)
            return self._json(result)

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not Found")

    def _json(self, data):
        body = json.dumps(data, default=str).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass  # quiet
```

## Key patterns to copy

1. **`_since_clause(window_hours, col="started_at")`** — single helper for all time filtering
2. **All endpoints parse `hours` param** — `qs.get("hours", [default])[0]`
3. **All-time chart unbounded** — `if daily_window == 0: no WHERE clause`
4. **Integer division** — `daily_window // 24` not `int(daily_window/24)`
5. **POST handler** — reads body, validates JSON, calls update function
6. **CORS header** — `Access-Control-Allow-Origin: *` for LAN access