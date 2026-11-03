# Hermes dashboard Terminal tab pattern

Use when adding or repairing a browser shell terminal in the built-in Hermes dashboard.

## Durable pattern

The dashboard already has a POSIX PTY-over-WebSocket bridge for `/chat`:

- frontend: xterm.js in `web/src/pages/ChatPage.tsx`
- backend: `/api/pty` in `hermes_cli/web_server.py`
- route/nav shell: `web/src/App.tsx`

For a separate shell terminal tab, do not invent a second PTY server. Reuse `/api/pty` and add a mode switch:

- default `mode=chat` preserves existing Chat behavior
- `mode=shell` spawns a normal interactive shell
- frontend route `/terminal` connects to `/api/pty?mode=shell&token=...` or ticket auth via `buildWsAuthParam()`
- terminal page can reuse xterm addons: `FitAddon`, `Unicode11Addon`, `WebLinksAddon`, optional `WebglAddon`

## Backend shape

Add a helper near `_resolve_chat_argv()`:

```python
def _resolve_shell_argv() -> tuple[list[str], Optional[str], Optional[dict]]:
    import shutil
    shell = os.environ.get("SHELL") or shutil.which("bash") or "/bin/sh"
    argv = [shell]
    if os.path.basename(shell) in {"bash", "zsh", "fish"}:
        argv.append("-l")
    env = os.environ.copy()
    env.setdefault("TERM", "xterm-256color")
    env.setdefault("COLORTERM", "truecolor")
    env.setdefault("HERMES_DASHBOARD_TERMINAL", "1")
    cwd = os.environ.get("HERMES_TERMINAL_CWD") or str(get_hermes_home())
    return argv, cwd, env
```

Then in `pty_ws`, before spawning:

```python
mode = (ws.query_params.get("mode") or "chat").strip().lower()
if mode not in {"chat", "shell"}: close/refuse
sidecar_url = _build_sidecar_url(channel) if channel and mode == "chat" else None
argv, cwd, env = _resolve_shell_argv() if mode == "shell" else _resolve_chat_argv(...)
```

Keep websocket auth, loopback/public admission, resize handling, PTY read/write loop, and POSIX availability checks shared.

## Frontend shape

- Add `web/src/pages/TerminalPage.tsx`.
- Add `TerminalPage` to `BUILTIN_ROUTES_CORE` under `/terminal`.
- Add a sidebar nav item near Chat, but only expose it when embedded dashboard TUI is enabled if it depends on `/api/pty`.
- Give the page a clear warning: commands run as the dashboard process user; do not expose the dashboard publicly without auth.

## Verification checklist

1. Compile backend:
   ```bash
   /usr/local/lib/hermes-agent/venv/bin/python -m py_compile hermes_cli/web_server.py
   ```
2. Build served frontend bundle. If `npm run build` is blocked by unrelated pre-existing TypeScript errors, use Vite-only build to ship the route while reporting the TS blocker honestly:
   ```bash
   ./node_modules/.bin/vite build
   ```
3. Restart the actual dashboard process bound to the intended port.
4. Probe HTTP:
   ```bash
   ss -ltnp | grep ':9120'
   curl -I http://127.0.0.1:9120/terminal
   ```
5. Probe WebSocket directly by extracting `window.__HERMES_SESSION_TOKEN__` from `/` and connecting to:
   ```text
   ws://127.0.0.1:9120/api/pty?token=<token>&mode=shell
   ```
   Send bytes with `\r` for Enter in raw WebSocket tests; browser/xterm `Enter` handles this normally.
6. Browser-verify the visible tab, `OPEN` state, shell prompt, and command output.

## Pitfalls

- A successful HTML shell at `/terminal` does not prove the PTY works. Verify the websocket and command echo/output.
- Do not route shell mode through chat sidecar event publishing; only chat mode needs `/api/pub` sidecar wiring.
- Do not claim full TypeScript build success if `tsc -b` fails from unrelated existing errors. Report the distinction: backend compile OK, Vite bundle OK, full TS check blocked elsewhere.
- In raw websocket tests, sending `\n` may only echo the command without execution depending on PTY/shell line discipline; send `\r` for Enter.
- If `Unicode11Addon` is loaded, set `allowProposedApi: true` on the xterm `Terminal` constructor or the pane can crash with `You must set the allowProposedApi option to true`.
- Avoid effect-dependency reconnect loops in `TerminalPane`: do not include inline parent callbacks or active-pane state in the websocket/xterm initialization effect. Stable `useCallback` handlers plus session/cwd/reconnect deps prevent constant close/reopen cycles that look like "websocket not connecting" and can make navigation feel stuck.
- For operator usability, put Command History at the top of the right rail, above safety/cwd/upload/download controls, and make the terminal panel tall enough (`min-h` around 600px+) so the shell feels primary.
- Restart the process actually listening on the dashboard port; stale manual dashboard processes can keep serving old bundles/routes.
