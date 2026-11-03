# Vendored xterm.js for standalone terminal apps

Use this when a standalone browser-terminal/dashboard app needs Hermes-like terminal feel but Docker build/container package installs are unreliable.

## Pattern

Keep the runtime simple and avoid npm build chains:

1. Fetch xterm assets from the host, not from Docker build:
   - `@xterm/xterm/lib/xterm.js`
   - `@xterm/xterm/css/xterm.css`
2. Store them under the app's served static tree, e.g.:
   - `backend/static/vendor/xterm/xterm.js`
   - `backend/static/vendor/xterm/xterm.css`
3. Reference them directly in the single HTML app:
   - `<link rel="stylesheet" href="/vendor/xterm/xterm.css">`
   - `<script src="/vendor/xterm/xterm.js"></script>`
4. Initialize `new Terminal({...})` in each pane after the pane DOM exists.
5. Wire `term.onData(...)` to the existing PTY WebSocket stream.
6. Keep HTTP write/read polling as fallback when WebSocket is not open.
7. Track printable current-line input separately so Enter can update shared command history.
8. Run a syntax check on extracted inline JS before rebuilding:
   - extract between `<script>` and `</script>` into `/tmp/...js`
   - run `node --check /tmp/...js`
9. Rebuild/restart the one-container app and verify served assets, browser xterm rendering, WebSocket state, command execution, history update, and console errors.

## Implementation notes

- In UMD builds, xterm exposes `window.Terminal` / global `Terminal`; no bundler needed.
- Dispose old terminal instances before remounting panes to avoid duplicate event handlers.
- Do not call a React/xterm parity migration complete from asset load alone. Verify actual keyboard input through xterm reaches the backend PTY and command output renders in the terminal.
- For stage-from-history behavior, send shell line-kill (`Ctrl+U`, `\u0015`) before writing the staged command into the PTY so the active prompt line is replaced cleanly.
- Keep a visible reconnect control that closes existing WebSockets and reattaches active pane sessions.

## Verification checklist

- `GET /vendor/xterm/xterm.js` returns 200 and JavaScript content type.
- `GET /vendor/xterm/xterm.css` returns 200 and CSS content type.
- Browser snapshot shows xterm's hidden `Terminal input` textarea or xterm DOM.
- Pane status shows `ws open` or an equivalent live stream state.
- Typing into the terminal and pressing Enter runs a real command, e.g. `echo xterm-ok`.
- Output contains the command result.
- Shared history contains that command.
- Browser console has zero JS errors.

## Honest clone-status language

After this pattern, the app is much closer to Hermes terminal parity because it has xterm-style rendering and WebSocket PTY streaming. It is still not exact Hermes dashboard terminal parity unless it also matches Hermes' React component behavior, auth/session model, durable backend session model, file rail behavior, and layout polish.
