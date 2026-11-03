# Terminal tab notes

Condensed implementation notes for Hermes dashboard terminal/workbench work.

## Scope this reference covers
- Adding or extending a terminal tab on the built-in Hermes dashboard
- Command history UX
- Session recovery and layout pitfalls
- Live verification expectations

## Durable patterns
- Treat the server as the source of truth for shared command history when the same operator may use multiple browsers or devices.
- If browser-only state causes confusing reopen behavior, remove terminal tab/session restore from `localStorage` and start from clean default tabs.
- Dense terminal toolbars benefit from icon-only controls with tooltip titles.
- Xterm containers inside dashboard cards need flex layouts that explicitly allow shrinking: `flex`, `flex-col`, `flex-1`, `min-h-0`, and `overflow-hidden` at the right levels.
- Only keyboard `ArrowUp`/`ArrowDown` should recall command history. Wheel/scroll should stay bound to terminal buffer scrolling.

## Backend/frontend pairing
Typical terminal-history changes span both sides:
- backend: persistence helpers + `/api/terminal/history` endpoints
- frontend: fetch/update/delete history state and render controls

If per-command delete is needed, prefer extending the existing delete route with an optional command selector instead of creating a separate endpoint.

## Failure mode worth checking early
If commands stop executing or the UI looks connected but input behaves oddly, inspect the shell itself:
- a bare `>` prompt usually means bash is waiting for the rest of a multiline command
- recover with `Ctrl+C`
- if the terminal session is polluted beyond easy recovery, recreating clean `screen` sessions is safer than chasing phantom websocket bugs

## Verification standard
Do not stop at a source patch.
Verify all of these:
1. frontend build succeeds
2. dashboard restarts cleanly on the intended route/port
3. browser shows the expected controls
4. live interaction proves the feature works (for example: history recall, per-command delete, scroll behavior, normal prompt state)

## Example durable UX decisions from this class of work
- keep old backend sessions discoverable under a "Previous" area instead of auto-remounting them as active tabs after reload
- store terminal history in a shared JSON file on the server when cross-browser persistence matters
- compact top actions to preserve horizontal room for session labels
