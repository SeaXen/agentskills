# Hermes dashboard terminal: restore badge and history accounting

Use this when the dashboard terminal already supports persistent backend `screen` sessions and the next operator asks for better recovery affordances or cleaner shared-history accounting.

## What changed well

### 1) Restore-all toolbar affordance
For manual backend-session recovery, a plain `Restore all` button is functional but weak. Better operator shape:
- show `Restore all · N` when `N` backend sessions are recoverable but not present in tabs
- disable + dim the button when `N = 0`
- use a more honest tooltip when nothing is pending, e.g. `No backend sessions are waiting to be restored`
- after restore, remove restored sessions from `Previous` so the UI state self-clears

Practical count rule:
- derive `N` from live backend sessions minus current local/stored tab ids
- do not count sessions already visible in tabs

## 2) ArrowUp / ArrowDown shared-history pitfall
A subtle bug can survive even when command chips, counts, and shell history all mostly work:
- user presses `ArrowUp` / `ArrowDown` inside the shell
- shell recalls a prior command visibly in the prompt
- user presses `Enter`
- command executes
- but the browser-side input tracker is empty, so the shared history POST writes nothing and the count does not increase

### Durable fix
On terminal Enter handling:
1. try the tracked browser-side input buffer first
2. if it is empty, inspect the current visible prompt line from xterm buffer
3. strip ANSI/control sequences
4. extract the text after the prompt marker (`#`, `$`, `>`) as the executed command
5. send that value through the same shared-history write path

This is a better fix than trying to mirror every shell-history navigation event in JS.

## 3) Command-history rail polish
Show the total unique command count in the header itself, for example:
- `server`
- `6 cmds`

Why it matters:
- gives immediate confirmation that delete/clear operations changed the server-side history
- makes small QA checks faster without opening APIs or logs

## Verification pattern

### Recoverable-count UI
1. create a disposable backend-only session, e.g. `hermes-dashboard-badge-test`
2. force local tab storage to omit that session
3. reload `/terminal`
4. expect `Restore all · 1`
5. activate restore
6. expect the button to return to plain `Restore all`
7. clean up the disposable backend session and restore default local tab state

### ArrowUp count accounting
1. run a disposable command, e.g. `echo HERMES_ARROW_QA`
2. confirm it appears in shared history as `×1`
3. press `ArrowUp` inside the shell
4. press `Enter`
5. confirm the same history row becomes `×2`
6. delete the disposable history row afterward so shared history stays clean

## Operator-facing reasoning to preserve
When the user reports "history works but count does not change" or "restored command did not add to history", distinguish:
- shell execution worked
- shell recall worked
- shared-history accounting failed

That is a browser/xterm input-tracking bug, not a shell persistence bug.
