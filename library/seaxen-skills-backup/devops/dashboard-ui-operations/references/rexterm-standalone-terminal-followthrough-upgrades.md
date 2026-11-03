# Rexterm standalone terminal: parity follow-through and pragmatic non-Hermes upgrades

Use this note when a standalone static-terminal app has already reached practical Hermes-terminal parity and the user asks for worthwhile upgrades from tmux / Termius / Nexterm **without** turning it into a full remote-host management platform.

## Good next upgrades in this class

Prefer low-risk, operator-useful additions that fit the existing architecture:

1. **Real PTY resize support**
   - Frontend computes `cols`/`rows` from the mounted xterm pane.
   - Send resize via control frame and/or `/api/terminal/resize`.
   - Backend applies `TIOCSWINSZ` and `SIGWINCH`.
   - Verify with `stty size` in a live shell.

2. **Authoritative HTTP write path**
   - Keep WebSocket for live output.
   - Use authenticated HTTP `/api/terminal/write` for command injection if browser-side WebSocket sending is inconsistent.
   - This is especially useful in static/single-file terminals where output streaming is solid but click-driven quick-run behavior is timing-sensitive.

3. **Transcript capture + export**
   - Keep a bounded rolling transcript buffer per session on the backend.
   - Expose `/api/terminal/transcript`.
   - Add a `Save log`/download action in the toolbar.
   - Verify by creating a short session, exporting, and confirming command/output presence.

4. **Launch profiles**
   - Add saved profiles that open named sessions and optionally run a startup command.
   - Good defaults: main shell, root shell, repo shell, data shell.
   - Persist via terminal preferences rather than hardcoding only in frontend state.
   - Verify by launching a profile and checking transcript or backend session state.

5. **Terminal settings panel**
   - Add a top-toolbar `Settings` dropdown for theme, font size, line height, scrollback, and cursor blink.
   - Persist settings server-side under terminal preferences, e.g. `terminal_settings`.
   - Normalize values on both frontend and backend so reloads cannot persist nonsense ranges.
   - Recreate xterm instances from the normalized settings object instead of scattering hardcoded `new Terminal(...)` values.
   - Good starter themes for this class: Hermes green, soft green, amber, mono.
   - Verify three things live: apply changes updates the active xterm, page reload keeps them, and reset returns to Hermes defaults.

## What not to overclaim

Do **not** call it "10/10 in all sectors" if it still lacks:
- tmux/screen-style durable sessions across backend/container restart
- SSH host inventory and key management
- SFTP / VNC / RDP / tunnels
- multi-host server-management workflows

That is a different product tier.

## Verification shape

Do not stop at build success.

Verify all of these live:
- page title / parity marker
- xterm mounted
- websocket open
- clean prompt with no stale success banner
- quickbar/browser-run command actually executes
- direct terminal input works
- PTY resize reflected by shell (`stty size`)
- transcript/export works
- new sessions/profiles show up in backend API state
- test history/session artifacts cleaned afterward

## Browser-testing nuance

If a visible button click appears flaky in browser automation, inspect DOM state and trigger the control from page context before concluding the feature is broken. For quick-run paths, a programmatic click plus post-click DOM/API verification can distinguish a tooling-timing issue from a real product bug.
