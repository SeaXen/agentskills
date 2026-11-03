# Hermes dashboard terminal session manager

Use this when the user wants the built-in Hermes Terminal page to behave like a real persistent session manager rather than a disposable tab strip.

## Durable expectations
- Backend shell sessions are the source of truth for persistence.
- Browser-local tab state may shape presentation, but reloads must not make backend sessions appear lost.
- UI-only tab removal must be clearly distinct from permanent backend session kill/delete.
- Recovery affordances should be explicit and operator-friendly (`Previous`, `Restore all`, clear labels).
- Do not claim terminal persistence is fixed from code review alone; verify live.

## Live implementation pattern
1. Patch the live frontend source under `/usr/local/lib/hermes-agent/web/src/pages/TerminalPage.tsx`.
2. Persist UI tab state and recently-closed state in localStorage.
3. Reconcile browser state with backend session inventory from `/api/terminal/sessions`.
4. If local state falls back to defaults but backend has extra sessions, auto-restore those sessions into tabs instead of hiding them only in recovery lists.
5. Keep overflow tabs visible through a `More` lane and recoverable/closed sessions in a `Previous` lane.
6. Add a manual one-click recovery path near session-scan controls (`Restore all`) even if auto-recovery exists.
7. Make dropdowns mutually exclusive and render them above the terminal surface (`overflow-visible`, correct z-index, controlled open state).
8. Avoid stale duplicates: restoring/adding a session should remove the same id from recently-closed state.

## Verification sequence
1. `npm run build` from `/usr/local/lib/hermes-agent/web`.
2. Open the live dashboard at `/terminal`.
3. Confirm the toolbar shows `Scan` and `Restore all`.
4. Inspect localStorage keys:
   - `hermes-dashboard-terminal-sessions`
   - `hermes-dashboard-terminal-recently-closed`
5. Verify backend truth separately with `screen -ls | sed -n '/hermes-dashboard-/p'`.
6. Simulate a mismatch by removing a backend session from local tab storage, reload, and verify either auto-recovery or `Restore all` returns it.
7. Test a real terminal command and confirm output renders and command history still lands server-side.
8. Clean disposable QA sessions and test commands from both backend and history before finishing.

## Common pitfalls
- Treating browser-local default tabs as the source of truth.
- Hiding backend sessions in `Previous` only, so users interpret reloads as data loss.
- Letting dropdown menus clip behind the terminal pane.
- Leaving both `More` and `Previous` open so they overlap and steal clicks.
- Forgetting to explain the difference between local tab removal and backend screen kill.
- Reporting success without a real backend-only recovery test.
