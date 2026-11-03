---
name: lightweight-monitor-daemon
description: "Architecture template for building a small, standalone (no-Hermes, no-Docker, no-cron) system monitor + web dashboard + Telegram/Discord alerter. Python daemon + Flask + SQLite + systemd. Pattern distilled from the systor project (/mnt/tb/1Apps/systor)."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [monitoring, daemon, systemd, flask, sqlite, telegram, discord]
    related_skills: [devops/sagar-hermes-ops, mcp/native-mcp]
---

# Lightweight Monitor Daemon

A reusable architecture pattern for **"build me a small standalone tool that watches my machine and tells me when something is wrong, without dragging in Prometheus / Grafana / Docker"**.

Distilled from the systor project (`/mnt/tb/1Apps/systor`, GitHub `SeaXen/systor`). When the user asks for something in this class, scaffold from here instead of starting from scratch.

## When to use this pattern

Trigger when the user says any of:
- "build me a lightweight system monitor"
- "I want a small daemon + web dashboard"
- "something like Prometheus but lighter"
- "monitor X and notify me when Y"
- "standalone / not part of Hermes"
- "low CPU and memory budget"
- "runs as systemd service, no cron"
- "dashboard on a specific port"

Don't use when:
- The user wants HA / multi-host / federated monitoring (use Prometheus + Grafana)
- They want deep application tracing (use OpenTelemetry)
- They want a one-off script, not a long-lived daemon

## The architecture (canonical)

```
   /etc/<app>/
   ├── config.yaml          ← main config (thresholds, ports, channels)
   └── <app>.env           ← secrets (bot tokens, webhooks)

   /opt/<app>/             ← python package installed here
   └── <app>/              ← source

   /var/lib/<app>/
   └── <app>.db            ← SQLite (samples, rollups, alerts, log)

   /var/log/<app>/         ← log files

   systemd user services (or system services):
   ├── <app>-collector.service   ← polls every N seconds
   └── <app>-web.service         ← web UI on a port
```

Two long-lived processes, two service files, one SQLite DB. Same dir layout, just different names. This pattern works for: system monitor (systor), file watcher / indexer, backup orchestrator, log aggregator, cron replacement, any "read state, decide, notify, log" loop.

## Decision framework (defaults that work)

| Decision | Default | Why |
|---|---|---|
| Language | Python 3.9+ | stdlib covers 90% of needs, no compile step, ships everywhere |
| Web framework | Flask + waitress | small, fast WSGI server, pure-Python, no gunicorn workers needed |
| Database | SQLite (WAL mode) | zero-config, fast for time-series, easy backup |
| Frontend | vanilla HTML + CSS + JS | no SPA, no build step, no node_modules |
| Charts | canvas 2D in plain JS | no Chart.js, no D3, ~3 KB JS |
| Polling loop | `time.sleep(1)` in a `for _ in range(interval)` so SIGTERM breaks within 1s | responsiveness vs simplicity |
| Notifications | Telegram bot API + Discord webhook | both have free tiers, both bypass email spam filters |
| State (alert hysteresis) | in-process dict + JSON dump on each transition | survives restart, no extra DB table |
| Process management | systemd user service (not cron, not screen) | auto-restart on crash, log to journald, runs at boot |
| Config format | YAML + env var overrides | humans edit YAML, automation sets env |
| CLI | argparse subcommands (`status`, `setup X`, `test`, `serve`) | standard, no click/typer dep |
| Logging | stdlib `logging` + FileHandler | rotation via logrotate, not Python |
| Resource budget | <50 MB RSS total, <1% CPU at idle | small enough to run alongside anything |

## Code layout

```
<app>/
├── __init__.py             # __version__, __app_name__
├── __main__.py             # `python -m <app>` entry → cli.main()
├── config.py               # YAML + env, DEFAULT_CONFIG, load_config(), save_config()
├── metrics.py              # all readers (CPU, mem, disk, temp, net) — return None on error
├── storage.py              # SQLite schema + retention + log_alert + log_notification
├── notifier.py             # send_telegram() + send_discord() + Notifier class
├── collector.py            # the daemon loop: poll → eval → store → notify
├── web.py                  # Flask app: /api/snapshot, /api/series, /alerts, /settings, /logs
├── cli.py                  # argparse CLI: status / setup telegram / setup discord / test / serve / config show
├── templates/              # Jinja2: base.html, dashboard.html, alerts.html, logs.html, settings.html
│   └── base.html           # shared shell (sidebar + auto-refresh JS)
├── static/
│   ├── css/style.css       # dark theme, CSS variables, no framework
│   └── js/app.js           # fetch + tiny canvas line chart, ~3.5 KB total
├── systemd/
│   ├── <app>-collector.service
│   └── <app>-web.service
├── install.sh              # copies to /opt, creates dirs, writes config, enables services
├── uninstall.sh            # stops services, removes files, keeps data + config
├── setup.py                # pip-installable, entry_points → console_scripts
├── requirements.txt        # minimal: Flask + waitress
├── README.md
├── LICENSE
└── .gitignore              # python + secrets + db + logs excluded
```

**Why each module:**
- `config.py` is the only thing that touches the filesystem on startup
- `metrics.py` is the only thing that touches `/proc` and `/sys`
- `storage.py` is the only thing that touches SQLite
- `notifier.py` is the only thing that touches the network
- `web.py` is the only thing that exposes an HTTP port
- `collector.py` is the only thing that runs forever
- All can be unit-tested in isolation

## The polling loop (canonical)

```python
_running = True
def handle_term(signum, frame):
    global _running
    log.info("received signal %d, shutting down", signum)
    _running = False
signal.signal(signal.SIGTERM, handle_term)
signal.signal(signal.SIGINT, handle_term)

def run():
    cfg = load_config()
    storage = Storage(...)
    notifier = Notifier(cfg)
    while _running:
        try:
            snap = collect_snapshot()        # metrics.py
            storage.insert_sample(snap)        # storage.py
            for metric, value, msg in evaluate(snap, cfg):  # collector.py
                results = notifier.notify(metric, msg)       # notifier.py
                for ch, ok, err in results:
                    storage.log_notification(ch, ok, err)
        except Exception:
            log.exception("loop error")
        # sleep with frequent interrupt checks
        for _ in range(poll_interval):
            if not _running: break
            time.sleep(1)
```

The `for _ in range: time.sleep(1)` pattern lets SIGTERM interrupt within 1 second instead of waiting up to the full poll interval.

## Sustained-threshold alerts (canonical pattern)

Single-sample alerts are noisy. Instead, track per-metric state:

```python
state[metric] = {"count": 0, "in_alert": False, "last_alert_ts": 0.0}

def eval_metric(name, value, threshold, sustained_needed, higher_is_worse, cooldown_sec):
    s = state[name]
    is_bad = (value > threshold) if higher_is_worse else (value < threshold)
    s["count"] = s["count"] + 1 if is_bad else 0
    if s["count"] >= sustained_needed:
        if not s["in_alert"] or (now - s["last_alert_ts"]) > cooldown_sec:
            s["in_alert"] = True; s["last_alert_ts"] = now
            return "alert"
    elif s["in_alert"]:
        s["in_alert"] = False
        return "recover"
    return None
```

Defaults that work for system monitoring:
- `sustained_needed`: 4 samples × 30s = 2 min (CPU/mem/swap)
- `sustained_needed`: 1 sample (disk fills slowly, no need to debounce)
- `cooldown_sec`: 600 (10 min between repeats)

### UX: expose threshold + duration in **minutes**, not samples

The user thinks in minutes, not in "samples × poll interval". The settings page
should literally show "alert when > 85 °C for 3 minutes" — never
"sustained_samples_temp: 6". Convert internally:

```python
def samples_for(duration_min: int, poll_sec: int) -> int:
    return max(1, (duration_min * 60) // max(poll_sec, 1))
```

Schema shape:

```yaml
thresholds:
  cpu_temp_c: { enabled: true, value: 85.0, duration_min: 3 }
  mem_free_mb: { enabled: true, value: 500, duration_min: 2 }
```

If your config started as flat scalars (`cpu_temp_c: 85.0`, `sustained_samples_temp: 6`),
auto-migrate on load by detecting any non-dict threshold and converting with
`samples_for(th[dur_key] * 30 / 60)`. See `references/schema-migration-old-flat-thresholds.md`.

## Hot-reload config without restarting the daemon

For "save in UI, see effect in <30s" UX, the collector must pick up config
changes without a systemd restart. The pattern that works:

1. Write a pidfile at startup (`/tmp/<app>-collector.pid`).
2. Inside the main loop, before each tick, check the config file's mtime
   (cheap — one `stat()` call). If it's newer than the last seen mtime, reload.
3. Also install a `SIGHUP` handler that sets a `_reload_requested = True` flag.
   The web UI's "Apply now" button writes the config, bumps its mtime, and
   `kill -HUP $(cat pidfile)`s the collector.
4. On reload, reset `_metric_state` (so old sustained counters don't bleed).

```python
import signal
_reload_requested = False

def _handle_hup(*_):
    global _reload_requested
    _reload_requested = True

signal.signal(signal.SIGHUP, _handle_hup)

last_cfg_mtime = _config_mtime()
while _running:
    cur_mtime = _config_mtime()
    if _reload_requested or (cur_mtime and cur_mtime > last_cfg_mtime):
        new_cfg = load_config()
        if new_cfg != cfg:
            _metric_state.clear()
            log.info("config reloaded from disk")
        cfg = new_cfg
        _reload_requested = False
        last_cfg_mtime = cur_mtime
    # ... rest of tick ...
```

The web "Apply" endpoint just needs `os.utime(path, None)` to bump mtime,
plus `os.kill(pid, signal.SIGHUP)` to nudge the daemon. No restart.

If `new_cfg == cfg` after the reload (no actual change), skip the log line —
otherwise operators spam the log with reload entries every time the UI polls
or autosaves.

## Notifications — both channels, fail soft

```python
class Notifier:
    def notify(self, subject, body):
        results = []
        if self.cfg["telegram"]["enabled"]:
            ok, err = send_telegram(...)
            results.append(("telegram", ok, err))
        if self.cfg["discord"]["enabled"]:
            ok, err = send_discord(...)
            results.append(("discord", ok, err))
        return results
```

Always log notification success/failure to the DB so you can debug "why didn't I get the alert" later.

## systemd unit (canonical)

```ini
[Unit]
Description=...
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 -m <app> serve collector
WorkingDirectory=/opt/<app>
Restart=always
RestartSec=10
StartLimitBurst=5
StartLimitIntervalSec=120
StandardOutput=append:/var/log/<app>/collector.log
StandardError=append:/var/log/<app>/collector.log
EnvironmentFile=-/etc/<app>/<app>.env   # - means optional

[Install]
WantedBy=default.target
```

For fresh-device installs where the user expects `sudo ./install.sh` to be enough, prefer **system services enabled in the installer by default** over user services that require extra `loginctl enable-linger` / `systemctl --user enable` steps. User-service installs are acceptable only when the user explicitly wants per-user isolation and understands the linger requirement. Verification after install must include `systemctl is-enabled <app>-web <app>-collector`, `systemctl is-active ...`, and a live listener / health check.

If you do support user services as an alternate mode, document them as an explicit opt-in path instead of the default quick-start path.

## Web UI (canonical)

Pages:
- `/` — live dashboard (auto-refresh every 5s with `setInterval`)
- `/alerts` — recent alert table
- `/logs` — tail of log file (read last 200 lines)
- `/settings` — edit thresholds (with per-metric duration in minutes), toggle channels, send test alerts
- `/api/snapshot` — current metrics JSON
- `/api/series?metric=X&hours=6` — historical time-series for a metric
- `/api/alerts`, `/api/notifications` — audit trail
- `/api/config` — current config (with secrets masked)
- `/api/apply` (POST) — bump mtime + SIGHUP collector so settings changes take effect immediately
- `/api/restart-collector` (POST) — SIGTERM the collector; systemd restarts it
- `/health` — `{"ok":true}` for liveness probes

Use `waitress` for production serving (not Flask dev server):

```python
from waitress import serve
serve(app, host=host, port=port, threads=2, ident="<app>")
```

### Visual style: GitHub-dark with top tabs (no sidebar)

When the user asks for "dashboard like X", a known-good reference is the
local `hermes-telemetry` on port 8009 (GitHub-dark palette: `#0f1117` bg,
`#161b22` elev, `#30363d` border, `#58a6ff` accent blue, `#3fb950` green,
`#f85149` red, `#d29922` yellow). Replicate that look:

- **Top header, no sidebar.** App title on the left, pill-shaped nav tabs
  (`Dashboard` / `Alerts` / `Logs` / `Settings`) on the right, refresh
  button at the far right.
- **Stat cards** with a 3px colored side-bar (`::before` pseudo) for status:
  green / yellow / red / cyan / purple.
- **Chart rows** of 2 cards each (1fr 1fr grid), with small canvas elements.
  Plain JS line chart, no Chart.js. ~3 KB.
- **Tables** as `.table-card` containers with a header bar.
- Inline JS per page; no shared `app.js` — easier to keep template-only.
- See `references/github-dark-palette-and-top-tabs.md` for the full CSS
  palette + the exact structure that shipped in systor v0.2.

When the user gives a literal visual reference ("dashboard is like hermes
telemetry port 8009"), `curl http://127.0.0.1:8009/` first to extract the
palette and class names — don't guess the look from the description.

## README template

Every project in this class should ship with:

```markdown
# <app>

**One-line description.**

Built for <use case> where Prometheus + Grafana is overkill.

## Features

- <bullet>
- <bullet>

## Quick start

\`\`\`bash
git clone <url>
cd <app>
sudo ./install.sh
\`\`\`

Open <http://127.0.0.1:PORT>.

## Configure notifications

\`\`\`bash
sudo -u $USER <app> setup telegram --token "..." --chat-id "..." --test
\`\`\`

## Resource cost

| Component | RSS at idle | CPU at idle |
|---|---|---|
| <app>-collector | ~10 MB | <0.5% |
| <app>-web | ~20 MB peak | <0.5% |
| **Total** | **~30-50 MB** | **<1%** |

## Tested on

- Debian 12/13
- Ubuntu 22.04/24.04
- DietPi
- Raspberry Pi OS (Bookworm)

## License

MIT.
```

### Optional: GitHub Pages marketing landing

Ship a static landing in `docs/` (`index.html`, self-contained CSS, screenshots already used by README) so the repo has a public site separate from the app on `:6677`. Enable via GitHub **Pages → `/docs`** or `gh api` (see `github/github-operations` → `references/github-pages-product-landing.md`). Reference implementation: `SeaXen/systor` at `/mnt/tb/1Apps/systor`.

## Pitfalls (learned the hard way)

- **Match the user's request literally; do not pre-add security/complexity.** A request like "give me a settings page to set CPU temp threshold and minutes" wants a settings page, threshold field, and minute field. It does **not** want auth tokens, `lan_only` gates, JWT-style masked secret placeholders, or `web_auth_token` regeneration buttons. When the user says "Revert back if you do anything wrong", treat that as a stop signal. Build the literal request first; ask before adding extras. (See `sagar-hermes-ops` for the full user-feedback pattern.)
- **`pkill -f "pattern"` will kill your own bash** if your command line contains "pattern". Use `pgrep -x <exact_name> | xargs kill` or `pgrep -x chromium` etc. Hit this multiple times debugging chromium leaks — `pkill -9 chromium` kept killing my own terminal.
- **TCP `CLOSE-WAIT` socket** can hide a stalled upload — local buffer accepts data but server already sent FIN. Check `ss -tnp` for actual state, not just the progress bar.
- **`shutil.disk_usage()` hangs forever on FUSE/autofs mounts.** `statvfs()` on a hung `fuse.rclone` / `sshfs` / untriggered `autofs` mount can block indefinitely while the user-space driver waits. Any endpoint that calls `shutil.disk_usage()` over a non-fixed mount list can lock the request for 60s+ and freeze the browser tab. Wrap every disk_usage call in a thread with a hard timeout (`_disk_usage_bounded(path, timeout=2.0)`), and hardcode the candidate mount list instead of enumerating via `findmnt`. See `references/common-pitfalls.md`.
- **Expensive cold-cache endpoints need a background refresher thread.** When `/api/something` runs psutil+docker+findmnt synchronously, a 2s cache TTL means any pause >2s re-triggers the cold path and the page feels slow. Fix is two parts together: a daemon thread that pre-warms the cache every ~4s, AND a slightly-larger TTL (~6s) so requests always hit cache. Either alone leaves a window where the request blocks. See `references/common-pitfalls.md`.
- **Recursive size walks inside file-manager listings kill browse perf.** Computing a directory's recursive size for every entry in a listing turns `/api/storage/browse` into 2s of stat calls. Listings must be O(1)-per-entry (immediate children via `os.scandir`); reserve recursive walks for an explicit on-demand Deep Scan action. Same rule applies to file counts, search results, anything shown "as you browse". See `references/common-pitfalls.md`.
- **MCP servers with browser pools leak** unless they `atexit.register(cleanup)` + `signal.signal(SIGTERM, handler)` + track `user-data-dir` for cleanup. Without this, each restart orphans ~250 MiB. (See `references/mcp-server-browser-pool-hygiene.md` in the mcp/native-mcp skill.)
- **`hermes config set mcp_servers.X.enabled false`** writes to user config only. Running Hermes doesn't reload — must restart to take effect. Same pattern applies to any config that's read at startup.
- **Don't run heavy work inside `for _ in range(poll): time.sleep(1)`** — keep sleep granular so SIGTERM interrupts within 1s.
- **sqlite3 WAL mode** + `PRAGMA synchronous=NORMAL` is the sweet spot for write-heavy monitoring workloads. WAL survives crashes; NORMAL is faster than FULL with minimal durability loss.
- **stdout-flushing matters** when you pipe to `tee` and then to file. Either use `python3 -u` or write logs directly with `logging.FileHandler` so the log is durable independent of stdout buffering.
- **Don't use `signal.signal()` in threads** — it only works in main thread. The collector's signal handlers must be installed in `run()`, called from `__main__`, not in a worker thread.
- **Hot-reload log spam trap**: if you log "config reloaded" every time mtime changes, the loop will spam that line on every UI autosave even when nothing changed. Only log when `new_cfg != cfg`. Same for SIGHUP — log the *intent* ("will reload on next tick") at SIGHUP time, log the *outcome* (skipped because no change / reloaded with N changes) at the actual reload.
- **Do not build multi-metric app dashboards by firing several parallel requests into a delta-based source.** If host CPU comes from `/proc` deltas or any sampler with mutable module-level baseline state, parallel `/api/apps?sort=cpu`, `/api/apps?sort=mem`, `/api/apps?sort=disk` calls can corrupt the CPU view and produce absurd numbers. Fetch one raw app snapshot per refresh, then sort/slice client-side (or server-side from the same snapshot object) into CPU / RAM / disk / network tables.
- **Autostart claims must be verified with the real service manager, not inferred from unit files.** After install/reinstall, check `systemctl is-enabled`, `systemctl is-active`, and the actual bound port / `/health`. A unit file containing `Restart=always` and `[Install] WantedBy=...` is not proof that the installer actually enabled it.
- **Auto-migration in `load_config()` is cheaper than asking users to run a converter.** When the schema shape changes between releases, detect the old shape on load (e.g. any non-dict value under `thresholds` means old flat schema), convert in-memory, and let `save_config()` write the new shape next time someone saves. See `references/schema-migration-old-flat-thresholds.md`.

## Anti-patterns to avoid

- ❌ Using a SPA framework (React/Vue/Svelte) for a 5-page admin dashboard
- ❌ Using Chart.js / D3 / Plotly for a 4-line time-series chart
- ❌ Running the collector and web in the same process (they have different lifecycle + resource profiles)
- ❌ Using cron jobs for periodic polling (no auto-restart, no clean shutdown, hard to debug)
- ❌ Sending alerts on a single sample (false positives everywhere — every GC pause triggers)
- ❌ Using a real database (Postgres, MySQL) when SQLite suffices
- ❌ Bundling a secrets manager when `/etc/<app>/<app>.env` (mode 600) is fine
- ❌ Using Prometheus + Grafana for one host

## Files in this skill

- `SKILL.md` (this file) — architecture template
- `references/systor-architecture.md` — concrete reference implementation walkthrough
- `references/common-pitfalls.md` — daemon + web + systemd + notifier pitfalls
- `references/schema-migration-old-flat-thresholds.md` — auto-migrate flat scalars to nested `{enabled, value, duration_min}` on load
- `references/github-dark-palette-and-top-tabs.md` — CSS palette + structural pattern matching hermes-telemetry on port 8009
- Cross-skill: `github/github-operations` → `references/github-pages-product-landing.md` — static `docs/` landing for public repos (systor pattern)
- `references/proc-based-metrics.md` — CPU%, disk I/O, and top processes read directly from `/proc` + `/sys`, no psutil dep. Delta-based metrics pattern with module-level state.
- `templates/service-unit.ini` — copy-paste systemd unit template
- `templates/config.yaml` — copy-paste config template
- `scripts/health-check.sh` — check service is up and DB is recent
