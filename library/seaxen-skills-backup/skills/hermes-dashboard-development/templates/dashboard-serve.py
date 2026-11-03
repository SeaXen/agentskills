#!/usr/bin/env python3
"""Starter dashboard server for a new Hermes plugin.

Copy to your plugin's dashboard/serve.py and adapt:
- DB_PATH to point to your plugin's SQLite file
- API handlers (api_summary, api_*) to query your tables
- Static file serving from same directory
"""

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
# DB path — CHANGE THIS to your plugin's telemetry directory
# ---------------------------------------------------------------------------
DB_PATH = (
    Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes")) / "my_plugin" / "telemetry.db"
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
# Time window helper — COPY AS-IS
# ---------------------------------------------------------------------------
def _since_clause(window_hours, col="started_at"):
    wh = int(window_hours)
    if wh == 0:
        return "1=1"
    return f"{col} >= datetime('now', '-{wh} hours')"

# ---------------------------------------------------------------------------
# API handlers — ADAPT THESE to your schema
# ---------------------------------------------------------------------------
def api_summary(window_hours=24):
    since = _since_clause(window_hours, "started_at")
    since_ts = _since_clause(window_hours, "ts")

    runs = _one(f"""
        SELECT COUNT(*) AS total_runs, ... FROM runs WHERE {since}
    """)
    # ... adapt columns to your runs table

    return {"window_hours": int(window_hours), "runs": runs, ...}

def api_my_data(window_hours=24):
    since_ts = _since_clause(window_hours, "ts")
    return _rows(f"SELECT * FROM my_table WHERE {since_ts}")

# ... add more endpoints as needed

# ---------------------------------------------------------------------------
# HTTP Handler — COPY AS-IS, add your endpoints
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).parent

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path == "/api/summary":
            qs = parse_qs(parsed.query)
            return self._json(api_summary(qs.get("hours", [24])[0]))

        if path == "/api/my-data":
            qs = parse_qs(parsed.query)
            return self._json(api_my_data(int(qs.get("hours", [24])[0])))

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

        if path == "/api/my-config":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                payload = json.loads(body) if body else {}
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            result = my_config_update(payload)  # implement this
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
        pass

# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def _parse_args(argv=None):
    parser = argparse.ArgumentParser(prog="serve.py", description="Plugin dashboard server.")
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Bind interface (default: {DEFAULT_HOST})")
    parser.add_argument("--port", type=int, default=None, help=f"Port (default: {DEFAULT_PORT})")
    parser.add_argument("port_positional", nargs="?", type=int, default=None, metavar="PORT")
    args = parser.parse_args(argv)
    port = args.port if args.port is not None else args.port_positional or DEFAULT_PORT
    return args.host, port

def main(argv=None):
    host, port = _parse_args(argv)
    if not DB_PATH.exists():
        print(f"ERROR: DB not found at {DB_PATH}")
        sys.exit(1)
    server = HTTPServer((host, port), Handler)
    print(f"Dashboard at http://{host if host not in ('127.0.0.1','localhost') else 'localhost'}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()