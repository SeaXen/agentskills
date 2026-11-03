# Rexterm standalone terminal parity repair

Use this when a standalone Docker terminal app on a fixed port loads shell chrome but the terminal box is missing, stuck, visually unlike Hermes, or shows the wrong prompt.

## Diagnostic sequence

1. Identify the live container and source directory:
   - `docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Ports}}\t{{.Status}}'`
   - `docker inspect <container> --format '{{range $k,$v := .Config.Labels}}{{if eq $k "com.docker.compose.project.working_dir"}}{{$v}}{{end}}{{end}}'`
2. Probe the app directly before patching:
   - `GET /` should return the static HTML.
   - Auth-protected API routes may return `401`; use the configured shared token for real health/session probes.
3. Browser-load the page and inspect console/DOM.
   - If the shell renders but pane stays `Loading sessions…` or the terminal is absent, suspect frontend boot failure, not PTY failure.
   - A single undefined constant in inline JS can stop the whole app before sessions and xterm mount.

## Root causes seen

- Frontend boot crash from naming drift: `RIGHT_RAIL_TAB_KEY` was defined, but state read `RAIL_TAB_KEY`.
- Shell prompt showed container identity because bash was launched as login shell and inherited container defaults.
- A large banner/workbench grid made the terminal look absent/hollow even after xterm worked.
- WebSocket attach notices were written into the terminal output stream, polluting the shell buffer and history-like output.
- Stale browser `localStorage` terminal-output buffers can make a fixed backend look blank, duplicated, or visually broken after reload.
- Quick-command success banners and websocket success banners add non-Hermes chrome; successful command output should be the confirmation.
- Killed/dead sessions remained in the sessions list, making stale UI tabs appear active.

## Repair pattern

### 1. Fix frontend boot first

Patch exact JS naming/initialization mismatches before styling. Verify after reload:
- status chip changes from `checking/down` to `ok:<port>`
- session count becomes nonzero
- one `.xterm` exists in DOM
- the terminal pane accepts focus/input

### 2. Force a DietPi-like/Hermes-like prompt for clone parity

For a stdlib Python PTY server launching bash, set prompt env and avoid profile files. If the user wants the cwd hidden like the Hermes-style dashboard terminal, use a short prompt while still starting shells in `/data`:

```python
env = os.environ.copy()
env["TERM"] = "xterm-256color"
env["HOSTNAME"] = "DietPi"
env["PROMPT_COMMAND"] = ""
env["PS1"] = "root@DietPi: "
proc = subprocess.Popen(
    [SHELL, "--noprofile", "--norc", "-i"],
    stdin=slave_fd,
    stdout=slave_fd,
    stderr=slave_fd,
    close_fds=True,
    env=env,
    cwd=DATA_DIR,
    start_new_session=True,
)
```

Expected visible prompt for this user:

```text
root@DietPi:
```

The working directory is still `/data`; `pwd` should print `/data`, but the prompt must not show `root@DietPi:/data#` when the user asks to hide cwd.

### 3. Keep websocket/status success noise out of the workbench

Do not send connection banners like `[rexterm websocket attached: main]` into the xterm stream. Show connection state in compact page chrome (`WS OPEN`, status chip), not inside the shell buffer.

For Hermes-like parity, successful attach and successful quick-run should not leave a banner either. Reserve banner strips for warnings, errors, and recovery notices:

```js
function setBanner(text) {
  const value = String(text || '');
  if (!value || value.startsWith('WebSocket attached:')) {
    bannerEl.textContent = '';
    bannerEl.classList.add('hidden');
    return;
  }
  bannerEl.textContent = value;
  bannerEl.classList.remove('hidden');
}

async function runQuickCommand() {
  // ... send command ...
  quickCommandEl.value = '';
  setBanner('');
}
```

If legacy output was cached in browser storage, strip it during frontend hydration or stop restoring terminal output from browser storage entirely. For a Hermes-like clean open, prefer backend stream/state over stale local browser buffers:

```js
state.outputs = {};                 // do not hydrate stale terminal text
localStorage.removeItem(OUTPUT_KEY); // do not persist xterm output cache
```

On websocket open, force a clean prompt redraw so a fresh load does not start as an empty xterm:

```js
ws.onopen = () => {
  setBanner(`WebSocket attached: ${sessionId}`); // hidden by setBanner
  try { ws.send('\u0015\f'); } catch {}
  renderPanes();
};
```

### 4. Compact the chrome before claiming Hermes-like parity

If the user says it does not look like Hermes terminal, make the terminal dominant:
- one-line header/status chips
- one-line toolbar, no explanatory operator-rule text
- small banner/status line only
- workbench as `flex column`; terminal card gets remaining height
- dark full-bleed terminal pane; side rail subordinate

If the header wraps into 2-3 lines, do not keep expanding it with full labels plus inline command input. The run/quick-command box is optional chrome and can be removed/hidden from the header; terminal input plus History/Presets already provide command entry. Keep only always-needed controls visible (`Active terminal`, New/Refresh/Rename, Hide tab, Pin, Previous/Restore, Remove, Tools, cwd pills) and move secondary actions (`Clear`, `Copy`, `Save`, `Restart`, `Reconnect`, `Split`, `Focus`, `Profiles`, `Settings`) under a compact `Tools` dropdown. Verify by measuring `.toolbar` height and `flex-wrap`; target one line around 44px.

Useful CSS shape:

```css
.toolbar { height: 44px; min-height: 44px; flex-wrap: nowrap; overflow: visible; }
.quickbar { display: none !important; } /* if it causes wrapping */
.workbench { display: flex; flex-direction: column; gap: 4px; min-height: calc(100vh - 178px); }
.banner { flex: 0 0 auto; padding: 4px 8px; }
.pane-card { flex: 1 1 auto; min-height: 0; }
```
Useful CSS shape:

```css
.toolbar { height: 44px; min-height: 44px; flex-wrap: nowrap; overflow: visible; }
.quickbar { display: none !important; }
.tabs { flex: 0 0 auto; max-width: none; min-width: 0; }
.workbench { display: flex; flex-direction: column; gap: 4px; min-height: calc(100vh - 178px); }
.banner { flex: 0 0 auto; padding: 4px 8px; }
.pane-card { flex: 1 1 auto; min-height: 0; }
```

### 5. Hide dead sessions from default session list

For in-memory PTY session managers, filter dead sessions in `list_sessions()` so killed verification sessions do not keep appearing as active tabs:

```python
sessions = [s for s in self.sessions.values() if s.process.poll() is None and s.alive]
```

For tmux-backed Rexterm, verify durable persistence explicitly instead of trusting UI state:

```bash
docker exec rexterm sh -lc '
  command -v tmux
  test -S /data/tmux/rexterm.sock && echo SOCKET_OK
  find /data/sessions -maxdepth 1 -type f -name "*.json" | sort
  tmux -S /data/tmux/rexterm.sock ls 2>/dev/null || true
'
```

Expected durable pieces:
- tmux binary available in the container
- socket under `/data/tmux/rexterm.sock`
- session metadata under `/data/sessions/<session>.json`
- `tmux -S /data/tmux/rexterm.sock ls` shows live sessions after rebuild/restart
- `Remove`/kill action kills the tmux session and removes it from the header; `Hide tab` is local UI only and must not kill the backend shell

### 5b. Keep Rexterm project organization low-clutter

When the user asks for “like many app, one root for all,” prefer a single-root layout, not separate frontend/backend wrapper folders:

```text
Rexterm/
├── app/
├── static/
├── data/
├── tests/
├── vendor-rootfs-tmux/
├── _archive/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── .dockerignore
```

Rules:
- Create a timestamped full backup outside the app before reorganizing.
- Do not delete old frontend/docs/scripts/plans/vendor caches; move unused/support material under `_archive/`.
- Update compose to `build.context: .` and `./data:/data`.
- Add `.dockerignore` excluding `data/` and `_archive/` so sockets/runtime state do not enter Docker build context.
- Rebuild and verify browser + tmux persistence after moving paths.

### 6. Implement real resize, not just resize-heartbeat frames

Hermes-style terminal parity needs the real shell PTY to receive dimensions. Do not only consume `\x1b[RESIZE:...]` as a harmless keepalive.

Backend stdlib pattern:

```python
import fcntl, struct, termios, signal

def parse_resize_frame(data: str):
    if not data.startswith("\x1b[RESIZE:") or not data.endswith("]"):
        return None
    cols_s, rows_s = data[len("\x1b[RESIZE:"):-1].split(";", 1)
    return max(20, min(int(cols_s), 300)), max(5, min(int(rows_s), 120))

def resize_pty(session, cols: int, rows: int) -> bool:
    packed = struct.pack("HHHH", rows, cols, 0, 0)
    fcntl.ioctl(session.master_fd, termios.TIOCSWINSZ, packed)
    os.killpg(session.process.pid, signal.SIGWINCH)
    session.cols, session.rows = cols, rows
    return True
```

Frontend static/xterm pattern:
- add a `ResizeObserver` on each terminal host
- estimate cols/rows from host client size and xterm render dimensions/cell size
- call `term.resize(cols, rows)`
- send `\x1b[RESIZE:${cols};${rows}]` over websocket or POST `/api/terminal/resize`

Verify with the shell, not the UI:

```bash
stty size; echo RESIZE_OK
```

Expected output shape after a browser resize/split/focus change:

```text
<rows> <cols>
RESIZE_OK
```

### 7. Prefer reliable input path if browser websocket sends are flaky

If the UI shows `WS OPEN` but typed/quickbar commands do not reach the shell, do not treat the terminal as fixed merely because output streams. Use websocket for output and authenticated HTTP `/api/terminal/write` for command input. This keeps the low-latency stream while avoiding silent browser/proxy client-frame loss.

## Follow-up feature pass for Hermes-like parity

After the base terminal works, the highest-value next features are still low-dependency and can live in the same static/stdlib app:

- top quick-command input: `Enter` runs, `Ctrl+Enter` stages into the active xterm
- cwd chips for common paths (`/data`, `/root`, `/mnt/tb`) that stage `cd <path> && pwd`
- focus mode that hides the right rail and expands the terminal
- Hermes-like compact toolbar labels (`New`, `Scan`, `Stop`, `Copy`, `Restart`, `WS`) so controls do not feel like a separate admin panel
- `Copy screen`, `Stop`, `Restart`, `Reconnect WS`, and soft `Clear` controls in the one-line toolbar
- WebSocket keepalive frames that the backend consumes instead of writing into the shell, reducing idle disconnects without polluting terminal output
- real PTY resize propagation: frontend measures xterm geometry, sends Hermes-style `\x1b[RESIZE:<cols>;<rows>]`, backend applies `TIOCSWINSZ` and sends `SIGWINCH`; verify with `stty size`
- robust input path: keep WebSocket as low-latency output, but prefer authenticated HTTP `/api/terminal/write` for browser command input if client WebSocket frames can silently fail while `WS OPEN` still displays
- richer preset commands covering system, Docker, disk, network, logs, and app-local checks
- editable grouped preset sections with `Edit`, `Defaults`, section accordions, and `Pin/Unpin` actions; persist `preset_sections` and `pinned_commands` through `/api/terminal/preferences`
- a real Files rail backed by authenticated `/api/files/*` routes: list `/data`, write text files, upload files, download files through query-token URL, mkdir, delete empty dirs/files, and stage `cd here`
- per-session dropdown actions beyond open/kill: rename, local remove, and stop, with wording that distinguishes local tab removal from backend process termination
- small server-side `/api/terminal/preferences` GET/POST backed by `terminal_preferences.json` for `history_view`, `command_click_mode`, `focus_mode`, default cwd, pinned commands, and preset sections

Keep test pollution out of the operator surface after browser/API smoke tests: kill temporary sessions and remove obvious `echo *_OK` smoke commands from shared history if you inserted them.

### 8. Keep Rexterm project organization flat at root without deleting state

For this user's Rexterm app, root should stay low-clutter. Prefer only the important project entry points at root:

```text
Rexterm/
├── backend/
├── frontend/
├── docker-compose.yml
├── README.md
├── .env.example
└── .gitignore
```

Do **not** delete data, docs, scripts, plans, or old backups during cleanup. First create a timestamped full backup outside the project root, then move clutter under an existing umbrella folder:

```bash
TS=$(date +%Y%m%d-%H%M%S)
mkdir -p /mnt/tb/1Apps/Rexterm-backups
tar -C /mnt/tb/1Apps -czf /mnt/tb/1Apps/Rexterm-backups/Rexterm-pre-org-$TS.tgz Rexterm
sha256sum /mnt/tb/1Apps/Rexterm-backups/Rexterm-pre-org-$TS.tgz > /mnt/tb/1Apps/Rexterm-backups/Rexterm-pre-org-$TS.tgz.sha256
```

Expected tar warning: live tmux sockets cannot be archived (`socket ignored`). That is OK as long as persisted session metadata/history/preferences are archived.

Recommended cleanup pattern:
- stop the container before moving runtime paths
- move `data/` → `backend/data/`
- move `docs/`, `scripts/`, `.hermes/`, old root backup files → `backend/project-meta/`
- update compose volume from `./data:/data` to `./backend/data:/data`
- add `backend/.dockerignore` so Docker build context excludes runtime sockets and metadata:

```text
data/
project-meta/
__pycache__/
app/__pycache__/
tests/__pycache__/
.pytest_cache/
*.pyc
*.bak.*
vendor-cache/
```

Rebuild after the move and verify all of the following:
- `docker ps` shows `rexterm` bound to `0.0.0.0:2344->8080`
- `backend/data/sessions/*.json`, `terminal_history.json`, and `terminal_preferences.json` still exist
- inside the container, `tmux -S /data/tmux/rexterm.sock ls` works or recreates a session on boot
- browser loads, `.xterm` exists, prompt is visible, and console has zero JS errors

## Session learnings: host-tool access, visual nesting, and history focus

For Dockerized Rexterm, `bash: hermes: command not found` does not mean the host lacks Hermes. It usually means the container cannot see the host install. To expose host Hermes into the Rexterm shell, mount all runtime pieces, not just `/usr/local/bin/hermes`:

```yaml
volumes:
  - /usr/local/bin/hermes:/usr/local/bin/hermes:ro
  - /usr/local/lib/hermes-agent:/usr/local/lib/hermes-agent:ro
  - /root/.local/share/uv/python:/root/.local/share/uv/python:ro
  - /root/.hermes:/root/.hermes
```

Why the uv Python path matters: `/usr/local/lib/hermes-agent/venv/bin/python` may be a symlink into `/root/.local/share/uv/python/...`; without that mount, the wrapper exists but fails with `cannot execute: required file not found`.

For temperature chips in a Docker terminal, mounting only `/sys/class/thermal` may leave `thermal_zone*` symlinks unresolved because they point into `/sys/devices/...`. Mount host `/sys` read-only and read via `/host-sys/class/thermal/thermal_zone*/temp` plus `/host-sys/class/hwmon/hwmon*/temp*_input`.

When the user says the terminal looks like “3 boxes inside,” flatten nested chrome:
- keep one outer `.pane-card` border
- remove `.terminal` border
- remove xterm screen/viewport radius
- keep xterm viewport and terminal background controlled by theme CSS variables
- verify computed styles: pane has one border, terminal has `0px none`, xterm screen/viewport radius is `0px`

If terminal typing also appears in the History search box, disable terminal-to-history mirroring. A previous “typing auto-searches history” feature can become a focus/legibility bug. Prefer explicit History search only unless the user asks for live mirroring.

## Verification checklist

- `docker compose build <service> && docker compose up -d --remove-orphans <service>` completes.
- `ss -ltnp | grep ':2344'` shows Docker proxy bound to the expected public port.
- Authenticated `GET /api/health` returns `200` and expected backend port/data dir.
- Authenticated session create/read/write proves the PTY works:
  - initial read is alive and can redraw to a prompt
  - writing `echo API_OK\n` returns `API_OK`
- Browser QA proves the real app works:
  - page loads at the public port
  - document title/identity matches the parity target, e.g. `Terminal`
  - status chip says `ALIVE`/expected backend state
  - websocket says `WS OPEN`
  - `.xterm` exists and the terminal pane is large/dark/full-bleed
  - no websocket-success, quick-run-success, or clear-success banner remains visible
  - browser-entered `echo FINAL_OK` prints `FINAL_OK`
  - resize is real, not cosmetic: browser/API run `stty size` after resize/split/focus and confirm the shell reports expected rows/cols
  - visible prompt is the requested short prompt, e.g. `root@DietPi:`
  - right rail tabs/history/presets/files still render after the visual pass
  - after `Clear`, the pane returns to a clean prompt instead of stale cached output
- Clean verification artifacts: kill temporary sessions, delete obvious `echo *_OK` history rows, and remove scratch files created during browser/file tests.

## Reporting rule

Be honest: this pattern can make a standalone terminal app visually/functionally close to Hermes dashboard terminal, but it is still a standalone reimplementation unless it literally reuses Hermes dashboard React/source and backend PTY routes.