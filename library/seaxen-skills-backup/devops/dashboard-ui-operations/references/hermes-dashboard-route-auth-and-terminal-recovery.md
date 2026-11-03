# Hermes dashboard route/auth split and terminal recovery

Use this when the Hermes dashboard appears to have a missing page, a vanished terminal tab, or confusing auth behavior across public and internal ports.

## Route/auth split to verify first

Typical split:
- public/auth-gated dashboard port (for example `9119`) served by nginx
- raw app/runtime port (for example `9120`) served by Hermes directly

Verification pattern:
1. Probe `/` and page routes like `/chat` on the public port.
2. Probe websocket/event/PTY endpoints separately.
3. Distinguish **proxy auth** from **Hermes app auth**.

Observed pattern to recognize:
- `/` or `/chat` on the public port returns `401` with `WWW-Authenticate: Basic ...` => nginx/browser Basic Auth layer is working.
- `/api/ws`, `/api/events`, `/api/pty`, or similar returns JSON `401 Unauthorized` => Hermes app/session auth layer is distinct and still required after proxy auth.

Operational meaning:
- HTML/page auth can be correct while websocket/API auth still fails.
- Do not describe that as one generic "auth is broken" problem.

## Ghost-route detection

A dashboard page can appear to exist server-side while being absent in the SPA.

Check for this pattern:
- direct visit to `/terminal` initially renders an HTML shell or heading
- after SPA boot, `location.pathname` changes or the UI falls back to another route such as `/sessions`

If that happens:
- the server/router may serve the shell for `/terminal`
- but the frontend app does not own that route anymore
- confirm by checking the active route table in `App.tsx` (or equivalent) and the fallback/redirect logic

Do not call the page "hidden" until you verify whether the route is actually registered.

## Missing-terminal recovery pattern

When a previously working dashboard terminal vanishes, verify all three layers:
1. frontend page file exists (`TerminalPage.tsx` or equivalent)
2. frontend route/nav wiring still exists in `App.tsx` / sidebar config
3. backend `/api/terminal/*` endpoints or equivalent helpers still exist

If frontend route and backend endpoints are both gone, the feature was removed/lost, not merely disabled.

## Durable recovery rule

Do **not** treat a rebuilt `web_dist/` alone as the durable fix.

Durable recovery path:
1. restore source-level frontend files
2. restore source-level route wiring
3. restore backend endpoint/helpers
4. rebuild from source when possible
5. keep an external patch/reapply overlay outside the installed package tree so future upgrades can reapply the customization

Why:
- package reinstalls or upstream updates often replace `web_dist/`
- source+backend features disappear again if only built assets were patched

## Recovery artifacts

If the live repo no longer contains the lost customization, check Hermes session artifacts before assuming the work is unrecoverable.

High-value artifacts:
- `~/.hermes/sessions/request_dump_*.json`
- prior session transcripts containing `read_file` output, diffs, or bundle filenames

Useful signals inside dumps:
- old route names
- old endpoint names like `/api/terminal/history`
- built bundle filenames proving a prior successful deploy
- copied source snippets or diffs large enough to reconstruct the feature

Treat session dumps as recovery evidence, not canonical source control.
