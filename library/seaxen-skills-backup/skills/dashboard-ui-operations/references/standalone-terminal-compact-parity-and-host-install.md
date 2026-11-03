# Standalone terminal compact parity + host install

Use when a standalone terminal app works technically but the user says it still does not look like the Hermes dashboard terminal, or asks whether it can run without Docker.

## Key lesson
Functional terminal features are not enough for a clone request. If the user asked for "same as Hermes dashboard terminal", treat visual density and layout hierarchy as correctness requirements.

## Compact parity pass
Do a live browser visual check, then tighten the surface before adding more features:

- one-line header; small title plus status chips only
- no subtitle/marketing/explanatory copy in the terminal chrome
- toolbar in a single nowrap row; horizontal overflow is acceptable
- compact session tabs below toolbar
- terminal/xterm area should dominate the page
- right rail should be subordinate: tighter rows, smaller cards, smaller controls
- remove redundant operator-rule text from always-visible chrome; keep semantics in labels/actions
- keep practical actions: `Stage`, `Copy`, `Run`, `Reconnect`, `Clear`, `Kill`
- verify with browser screenshot/vision, not only DOM text

Good CSS defaults for single-file terminal apps:

```css
.page { width: calc(100vw - 16px); margin: 6px auto; gap: 6px; }
.hero { min-height: 38px; padding: 6px 10px; flex-wrap: nowrap; }
.hero-sub { display: none; }
.toolbar { padding: 6px; gap: 5px; flex-wrap: nowrap; overflow-x: auto; }
.main { grid-template-columns: minmax(0, 1fr) 300px; gap: 6px; }
.pane-card, .rail-card { min-height: calc(100vh - 178px); }
.cmd-row { padding: 6px; gap: 4px; }
```

## Honest clone language
Say plainly:

- standalone reimplementation can get close
- exact same-to-same requires source-level cloning/reuse of the real Hermes terminal React route and backend contracts
- if React/Vite/npm build is blocked, continue vendored/static parity passes, but do not claim exact clone

## Host-PC install without Docker
If the app is stdlib Python plus vendored static assets, offer host mode.

`run-host.sh` shape for current Rexterm-style single-root apps:

```bash
#!/usr/bin/env bash
set -euo pipefail
APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CLI_REXTERM_BACKEND_PORT="${REXTERM_BACKEND_PORT:-}"
if [[ -f "$APP_DIR/.env" ]]; then
  set -a
  source "$APP_DIR/.env"
  set +a
fi
if [[ -n "$CLI_REXTERM_BACKEND_PORT" ]]; then
  export REXTERM_BACKEND_PORT="$CLI_REXTERM_BACKEND_PORT"
else
  # Docker often uses REXTERM_BACKEND_PORT=8080 internally; host mode should use public port.
  export REXTERM_BACKEND_PORT="${REXTERM_HOST_PORT:-${REXTERM_PORT:-${REXTERM_BACKEND_PORT:-2344}}}"
fi
export REXTERM_DATA_DIR="${REXTERM_DATA_DIR:-$APP_DIR/data}"
export REXTERM_STATIC_DIR="${REXTERM_STATIC_DIR:-$APP_DIR/static}"
export REXTERM_SHARED_TOKEN="${REXTERM_SHARED_TOKEN:-change-me}"
export REXTERM_HISTORY_LIMIT="${REXTERM_HISTORY_LIMIT:-300}"
if ! command -v tmux >/dev/null 2>&1 && [[ -x "$APP_DIR/vendor-rootfs-tmux/usr/bin/tmux" ]]; then
  export PATH="$APP_DIR/vendor-rootfs-tmux/usr/bin:$PATH"
  export LD_LIBRARY_PATH="$APP_DIR/vendor-rootfs-tmux/usr/lib/x86_64-linux-gnu:${LD_LIBRARY_PATH:-}"
fi
mkdir -p "$REXTERM_DATA_DIR"
exec python3 "$APP_DIR/app/server.py"
```

Important host-mode pitfalls:
- if `.env` has `REXTERM_BACKEND_PORT=8080` for Docker, host mode must prefer `REXTERM_HOST_PORT` or `REXTERM_PORT` so the public port remains `2344`
- if host `tmux` is not installed, add the vendored tmux path and `LD_LIBRARY_PATH` before starting Python
- for public-repo readiness, keep `.env` and `data/` gitignored; only `.env.example` and install scripts should be committed

Systemd installer shape:

```ini
[Unit]
Description=Standalone terminal app
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/app
ExecStart=/path/to/app/scripts/run-host.sh
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
```

Verification:

- if Docker owns the public port, test host mode on an alternate port
- `GET /` returns HTML
- `GET /api/health` returns JSON with the alternate port/data dir
- then stop the temporary host process
