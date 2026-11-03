# Embedded chat flag vs standalone terminal tab

Use this note when `/chat` looks broken after dashboard terminal work.

## The important split
Two things can be true at once:
1. the standalone `/terminal` page/tab should be removed
2. the embedded Chat TUI must still work

Do not treat them as the same feature.

## Symptom pattern
If `/chat` renders but browser console shows disconnected PTY/events/ws behavior, check whether this is actually a missing embedded-chat startup flag rather than a frontend route problem.

High-signal checks:
- sidebar has no `TERMINAL` nav item
- `/terminal` falls back to another route like `/sessions`
- `/chat` still renders an `.xterm`
- `window.__HERMES_DASHBOARD_EMBEDDED_CHAT__` is `false`
- `/api/events`, `/api/ws`, or `/api/pty?mode=chat` return `404`

That means the frontend shell is present but backend embedded-chat routes were not enabled.

## Files to inspect
- `/usr/local/lib/hermes-agent/web/src/App.tsx`
  - standalone terminal nav/route removal belongs here
- `/usr/local/lib/hermes-agent/hermes_cli/main.py`
  - dashboard startup must pass `embedded_chat=True` when the built-in Chat TUI is intended to exist
- `/usr/local/lib/hermes-agent/hermes_cli/web_server.py`
  - route registration and embedded-chat guards live here
- `/usr/local/lib/hermes-agent/web/src/lib/dashboard-flags.ts`
  - frontend may assume embedded chat is always enabled

## Safe workflow
1. Remove only the standalone terminal nav item and route.
2. Rebuild the frontend and restart the dashboard.
3. Verify whether the served bundle is fresh before drawing conclusions from old browser state.
4. If `/chat` still disconnects, inspect backend startup and bootstrap flags before blaming the frontend edit.
5. Confirm `start_server(..., embedded_chat=True)` if Chat TUI is meant to exist.
6. Re-verify in browser:
   - `/chat` path stays `/chat`
   - `.xterm` exists
   - no disconnect banner
   - no reconnect warning
   - `/terminal` no longer resolves to a real terminal page

## Pitfall
The easiest wrong move is to remove `Terminal`-related code broadly from `App.tsx` and accidentally break Chat icon/runtime assumptions while the real runtime bug is backend startup. Treat standalone terminal removal and embedded chat repair as separate checks.
