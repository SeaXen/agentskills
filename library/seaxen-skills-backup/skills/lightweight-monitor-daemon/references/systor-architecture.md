# systor — reference implementation walkthrough

Concrete file-by-file walkthrough of the systor project at `/mnt/tb/1Apps/systor`. Use this as a template when building the next lightweight monitor.

## Directory structure (what each piece does)

```
/mnt/tb/1Apps/systor/
├── systor/                          # python package (pip-installable)
│   ├── __init__.py                   # __version__ = "0.1.0", __app_name__ = "systor"
│   ├── __main__.py                   # enables `python -m systor` → cli.main()
│   ├── config.py                     # YAML + env loader, DEFAULT_CONFIG
│   ├── metrics.py                    # reads /proc, /sys, df
│   ├── storage.py                    # SQLite (samples, alerts, notifications, rollups)
│   ├── notifier.py                   # send_telegram + send_discord + Notifier class
│   ├── collector.py                  # the daemon: poll → eval → store → notify
│   ├── web.py                        # Flask dashboard on 127.0.0.1:6677
│   ├── cli.py                        # systor command: status, setup X, test, serve, config show
│   ├── templates/
│   │   ├── base.html                 # sidebar + content area, shared shell
│   │   ├── dashboard.html            # live KPIs + 4 charts + alerts table
│   │   ├── alerts.html               # alert history + notification delivery log
│   │   ├── logs.html                 # tail of log file
│   │   └── settings.html             # edit thresholds, telegram, discord, send test
│   └── static/
│       ├── css/style.css             # 6.7 KB, dark theme, CSS variables, no framework
│       └── js/app.js                 # 3.5 KB, fetch + tiny canvas chart, no deps
├── systemd/
│   ├── systor-collector.service      # poll every 30s
│   └── systor-web.service            # Flask on 6677
├── install.sh                        # sudo ./install.sh → fully installed
├── uninstall.sh                      # clean removal (keeps config + DB)
├── setup.py                          # pip install . → provides `systor` command
├── requirements.txt                  # Flask + waitress
├── README.md
├── LICENSE                           # MIT
└── .gitignore                        # python + secrets + db + logs excluded
```

## Module-by-module

### config.py — 130 lines

**What it does:** Load config from YAML files, merge with defaults, apply env var overrides, save back.

**Key trick — minimal YAML parser (no PyYAML dep):**
- 50 lines of `_yaml_to_dict()` handles `key: value` and 2-space indent
- 15 lines of `_deep_merge()` recursively merges overlay into base
- 30 lines of `_apply_env()` maps `SYSTOR_X_Y` env vars to `cfg[x][y]`

**Resolution order (later wins):**
1. Built-in defaults (`DEFAULT_CONFIG`)
2. `/etc/systor/config.yaml` (production)
3. `~/.config/systor/config.yaml` (user override)
4. `./systor.yaml` (cwd, dev)
5. `SYSTOR_*` environment variables (CI/Docker)

**Lesson:** Don't pull in PyYAML just to read 30 lines of config. A 50-line line-oriented parser handles 90% of use cases and saves a dependency.

### metrics.py — 150 lines

**What it does:** Pure functions that read /proc, /sys, df and return numbers or None.

**Each function is independent and best-effort:**
- `read_loadavg()` → first field of /proc/loadavg
- `read_cpu_percent(sample_interval=0.5)` → delta of /proc/stat
- `read_cpu_temp_c()` → max across /sys/class/thermal/thermal_zone*/temp
- `read_meminfo()` → parses /proc/meminfo into a dict
- `read_disk_usage()` → calls `df -PB G`, filters pseudo-filesystems
- `read_network_stats()` → sums rx/tx from /proc/net/dev (excludes lo)
- `collect_snapshot()` → one dict with everything, single point of failure

**Lesson:** Every reader returns `None` on error. Never crash the daemon because `/sys/class/thermal` doesn't exist on this kernel. Degrade gracefully.

### storage.py — 130 lines

**What it does:** SQLite wrapper with WAL mode + retention.

**Schema (4 tables):**
- `samples` — one row per poll, columns for each metric
- `rollups_5m` — averaged buckets (for long-term storage)
- `alerts` — every alert + recovery event
- `notification_log` — every send attempt + success/failure

**Thread safety:** single `threading.Lock` around all writes. SQLite itself is fine for concurrent reads but writes serialize.

**Retention:** `apply_retention()` deletes old data once per hour + runs VACUUM. Default 7 days raw + 90 days rollups.

**Lesson:** WAL + `synchronous=NORMAL` is the sweet spot for write-heavy monitoring. You lose ~1 second of durability on power loss, but the daemon polls every 30s so a lost sample is fine.

### notifier.py — 80 lines

**What it does:** `send_telegram()`, `send_discord()`, and a `Notifier` class that wraps both.

**Two functions, ~25 lines each:**
```python
def send_telegram(token, chat_id, text, timeout=10) -> tuple[bool, str|None]:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = urllib.parse.urlencode({...}).encode()
    # POST, return (ok, err)

def send_discord(webhook, text, timeout=10) -> tuple[bool, str|None]:
    payload = json.dumps({"content": text}).encode()
    # POST, return (ok, err)
```

**Both fail soft:** returns `(False, "error message")` on any failure. The Notifier class sends to all enabled channels and returns a list of results.

**Lesson:** Truncate Discord messages to 1900 chars (limit is 2000, leave margin for safety). Telegram doesn't need truncation (4096 limit).

### collector.py — 130 lines

**What it does:** The daemon loop. Polls every N seconds, evaluates thresholds, stores samples, sends alerts.

**The eval loop (canonical):**
```python
def _eval_metric(name, value, threshold, sustained_needed, higher_is_worse, cooldown_sec):
    s = _metric_state.setdefault(name, {"count": 0, "in_alert": False, "last_alert_ts": 0.0})
    is_bad = (value > threshold) if higher_is_worse else (value < threshold)
    s["count"] = s["count"] + 1 if is_bad else 0
    if s["count"] >= sustained_needed:
        if not s["in_alert"] or (now - s["last_alert_ts"]) > cooldown_sec:
            s["in_alert"] = True
            s["last_alert_ts"] = now
            return ("alert", value, threshold)
    elif s["in_alert"]:
        s["in_alert"] = False
        return ("recover", value, threshold)
    return None
```

5 metrics evaluated per cycle. Returns `("alert"|"recover", value, threshold)` or `None`.

**Signal handlers (canonical):**
```python
_running = True
def handle_term(signum, frame):
    global _running
    log.info("collector: received signal %d, shutting down", signum)
    _running = False
signal.signal(signal.SIGTERM, handle_term)
signal.signal(signal.SIGINT, handle_term)
```

Must be in `__main__` (not in worker threads — `signal.signal()` only works in main thread).

**The sleep loop:**
```python
while _running:
    try:
        snap = collect_snapshot()
        storage.insert_sample(snap)
        for metric, value, msg in evaluate(snap, cfg):
            ...
    except Exception:
        log.exception("loop error")
    for _ in range(poll):
        if not _running: break
        time.sleep(1)
```

The `for _ in range: time.sleep(1)` lets SIGTERM interrupt within 1s instead of waiting the full poll interval.

### web.py — 200 lines

**What it does:** Flask app with JSON API + Jinja2 templates.

**API endpoints:**
- `GET /api/snapshot` — current metrics JSON
- `GET /api/series?metric=X&hours=6` — historical time-series, downsampled to ≤600 points
- `GET /api/alerts?limit=50` — alert history
- `GET /api/notifications?limit=50` — notification delivery log
- `GET /api/system` — full snapshot + config + DB stats
- `GET /health` — `{"ok": true, "ts": ...}`

**HTML pages:**
- `/` — dashboard (KPIs + 4 charts + alerts table, auto-refresh 5s)
- `/alerts` — alert history + notification log
- `/logs` — tail of log file (read last 200 lines)
- `/settings` — edit thresholds, toggle channels, send test alerts (saves to /etc/systor/config.yaml)

**Production serving:** `waitress` (not Flask dev server):
```python
from waitress import serve
serve(app, host=host, port=port, threads=2, ident="systor")
```

**Settings save:** POST /settings receives JSON, updates config dict, calls `save_config()`. On `PermissionError` (config owned by root), returns the error so the UI can show it.

### cli.py — 130 lines

**What it does:** argparse-based CLI with subcommands.

Subcommands:
- `systor status` — one-shot snapshot of system state
- `systor setup telegram --token X --chat-id Y --test`
- `systor setup discord --webhook X --test`
- `systor test --channel telegram|discord|all --message "..."`
- `systor serve collector` — run daemon in foreground (debug)
- `systor serve web` — run web in foreground (debug)
- `systor config show` — dump current config as JSON

Entry point: `systor.cli:main`. The `setup.py` entry_points wires `systor` → this.

## v0.3.0 additions

The user asked for "where is CPU use stat and graph", "disk usage stat + disk load", "manual refresh time + past time view setting", and "if it not make app heavy add most cpu/memory use apps". All four shipped without adding `psutil` — see `references/proc-based-metrics.md` for the recipes.

- **CPU usage %** stat card + chart: `/proc/stat` delta in `metrics._cpu_percent_delta()`, surfaced via `cpu.percent` in `/api/snapshot` and `cpu_pct` series.
- **Disk I/O load** stat card + chart (read in cyan, write overlaid in red): `/proc/diskstats` sector delta in `metrics.read_disk_io_mbps()`. Persisted as `disk_read_mbps` / `disk_write_mbps` columns.
- **Refresh / range / pause controls** in dashboard header: dropdowns for refresh (1s/2s/5s/10s/30s/1m) and range (1h/6h/24h/7d), all persisted in `localStorage`. Pause button freezes both.
- **Top processes by CPU and memory** (10 each): `/api/top-processes?by=cpu|mem&n=10`. Reads `/proc/<pid>/stat` for utime/stime/rss + `/proc/<pid>/cmdline` for the tooltip. Collector pre-warms the CPU baseline at startup so the first user request has data.

## What worked well

- **The two-process split (collector + web)** was the right call. They have different lifecycles (you might restart the web to pick up code changes without losing poll history).
- **SQLite + WAL** handled 7 days × 2880 samples/day = ~20k rows easily. Total DB size ~1 MB. No cleanup needed in the hot path.
- **Vanilla JS** for the dashboard — no build step, no `node_modules`, runs from `static/` directly. Total dashboard payload ~17 KB (HTML + CSS + JS).
- **`waitress`** as the WSGI server was the right pick — pure-Python, no gunicorn workers config, single-process keeps memory predictable.
- **`hermes config set` user override** pattern (`/root/.hermes/config.yaml` overrides project config) is reusable: write to user layer, document that restart is needed.
- **Delta-based `/proc` metrics** (CPU%, disk I/O, process CPU%) avoid the `psutil` dependency entirely. Module-level state holds the previous sample; each call computes a rate.

## What I'd do differently next time

- **Add a `record` mode** to the CLI that captures one sample and exits. Useful for shell scripting and cron (if you really need cron).
- **Per-metric JSON config schema validation** (use `pydantic` or `dataclass` instead of raw dict).
- **Smarter chart downsampling** — currently uses simple stride slicing, would prefer LTTB for visual fidelity.
- **TLS for the web** via self-signed cert + reverse proxy (currently binds to 127.0.0.1 only).
- **Token rotation** for Telegram bots (currently assumes long-lived token).
- **Health check endpoint** that returns HTTP 503 if DB writes have stalled for >5 minutes.

## Concrete numbers (systor v0.1.0 on DietPi, 7.8 GB RAM)

| Component | RSS | CPU at idle |
|---|---|---|
| systor-collector | 9.8 MB | <0.5% |
| systor-web (Flask + waitress) | 24 MB peak | <0.5% |
| SQLite (7 days data, ~20k rows) | 1 MB | — |
| **Total** | **~35 MB** | **<1%** |

Compared to the user's previous setup:
- tradingview-chart MCP leak: ~2.9 GB (now fixed)
- 13 other MCPs: ~4.7 GB (most now disabled)

**systor does more, uses 25× less memory.**
