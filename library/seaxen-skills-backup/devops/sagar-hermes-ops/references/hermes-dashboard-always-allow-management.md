# Hermes dashboard Always Allow management

Use when the user wants the Hermes dashboard itself to expose persistent dangerous-command approval management.

## Goal shape
Add a Config-page panel for `command_allowlist` with:
- current pattern count
- list of current patterns
- add one new exact pattern
- delete one exact pattern
- clear all patterns
- destructive confirmation dialogs for delete/clear

## Backing state
Persistent approvals live in:
- `~/.hermes/config.yaml`
- key: `command_allowlist`

Approval meaning:
- `Allow Once` -> one command only
- `Allow Session` -> current process/session only
- `Always Allow` -> persistent `command_allowlist`

## Backend pattern
In `hermes_cli/web_server.py` add:
- `GET /api/config/command-allowlist`
- `POST /api/config/command-allowlist` with JSON body `{ "pattern": "..." }`
- `DELETE /api/config/command-allowlist` with JSON body `{ "pattern": "..." }`
- `POST /api/config/command-allowlist/clear`

Implementation notes:
- load with `load_config() or {}`
- normalize non-list values to `[]`
- trim the incoming pattern before mutation
- reject empty add requests with 400 instead of writing junk
- add by exact string equality only; keep the list unique
- a duplicate add should return success with `created: false`, not a hard error
- delete by exact string equality
- return updated `patterns` after mutation
- raise 404 if delete target is absent

## Frontend pattern
In `web/src/lib/api.ts` add API helpers for the four routes.

In `web/src/pages/ConfigPage.tsx` add:
- `allowlistPatterns`, `allowlistLoading`, `allowlistBusy`, `allowlistError`
- `allowlistDraft` for the add-pattern textbox
- `allowlistConfirm` union for delete vs clear
- `loadCommandAllowlist()` on page load + manual refresh
- Card UI near the top of Config page
- add-pattern textbox + `Add pattern` button
- Enter-key submit for the textbox
- per-entry trash buttons
- danger-zone clear-all block
- `ConfirmDialog` for delete and clear-all

UX notes:
- disable add while busy or when the trimmed draft is empty
- after successful add, clear the draft and refresh local state
- if the backend reports a duplicate (`created: false`), toast it as an informational success rather than surfacing it as a failure

## Verification pattern
### 1) Build real frontend
```bash
cd /usr/local/lib/hermes-agent/web
npm run build
```

### 2) Verify live dashboard route
Open `/config` and confirm the panel exists on the real dashboard.

### 3) Remember protected local API behavior
Even on localhost, direct API probes can return 401 unless you provide the dashboard session token.

Safe probe pattern:
1. fetch `/`
2. extract `window.__HERMES_SESSION_TOKEN__`
3. send header `X-Hermes-Session-Token: <token>`
4. call `/api/config/command-allowlist*`

## Isolated verification pattern
If the user's real allowlist is empty, do not mutate the main profile just to prove the UI.

Use a throwaway home:
1. create temp dir
2. copy or synthesize `config.yaml`
3. seed `command_allowlist` with sample patterns
4. run a second dashboard instance with `HERMES_HOME=/tmp/...` on another port
5. verify list/delete/clear there
6. kill the temp dashboard

This gives real end-to-end proof without touching the main profile.

## Browser QA checklist
- panel visible on Config page
- add textbox and button visible
- button enables only when a non-empty pattern is present
- add action inserts the pattern and updates the count/list
- count updates after refresh
- delete button opens destructive confirm
- delete confirm removes one pattern
- clear-all opens danger-zone confirm
- clear-all leaves empty-state UI

## Practical verification flow
1. Prove API CRUD on the live port with the session-token header:
   - POST add
   - GET list
   - DELETE one
   - POST clear
2. Then exercise at least one add and one delete from the real browser UI.
3. Restore the real allowlist to its original state when using the main profile for proof.

## Operational caveat
Removing entries from `command_allowlist` stops future persistent auto-approval, but already-running Hermes sessions/gateway processes may still hold in-memory approval state. For full revocation, start a fresh session or restart the relevant Hermes runtime.
