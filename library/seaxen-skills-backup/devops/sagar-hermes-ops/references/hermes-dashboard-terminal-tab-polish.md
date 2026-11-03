# Hermes dashboard terminal tab polish

Use when refining the built-in Hermes dashboard Terminal tab on Dr. Sagar's setup.

## Durable facts
- The live editable frontend/backend sources for this Hermes install are under `/usr/local/lib/hermes-agent/`, not the chat cwd `~/.hermes`.
  - Frontend: `/usr/local/lib/hermes-agent/web/src/pages/TerminalPage.tsx`
  - Backend: `/usr/local/lib/hermes-agent/hermes_cli/web_server.py`
- The live dashboard in this setup runs on `:9120`.
- For terminal history, the server-side source of truth is `/root/.hermes/terminal-command-history.json`.

## Good terminal-tab polish targets
- Confirm before deleting a local terminal tab.
- Keep a `Recently closed` lane so accidental local tab closure is recoverable.
- Replace `window.prompt(...)` rename UX with a small in-app modal/dialog.
- If split pane exists, add an explicit width control rather than forcing a fixed 50/50 layout.
- Keep command-history deletion per-item and server-side, not browser-local only.

## Build / restart / verify pattern
1. Patch the real live source under `/usr/local/lib/hermes-agent/...`.
2. Build the frontend with direct Vite output into `hermes_cli/web_dist/`.
   - On this host, `./node_modules/.bin/vite build` may be misclassified by Hermes terminal foreground heuristics, so run it as a tracked background job and read the log file.
3. Stop the existing dashboard listener first, then start a fresh dashboard process separately.
   - Do **not** chain stop + start in one tracked background job.
4. Verify in layers:
   - build log shows success and the new bundle name
   - `ss -ltnp` shows the new dashboard listener on `:9120`
   - localhost HTTP probe returns `200`
   - browser snapshot confirms the actual UI affordances (rename modal, Recently closed, split-width slider, per-item history delete, etc.)

## Practical verification examples
- Rename modal should render as real dashboard UI, not browser `prompt()`.
- Deleting a local tab should show a recovery path in `Recently closed`.
- Restoring from `Recently closed` should bring the tab back into the active tab strip.
- Split mode should visibly expose a width control and persist the current ratio in browser storage.

## Pitfalls
- Editing `~/.hermes/.../TerminalPage.tsx` and thinking the live dashboard changed.
- Calling the terminal tab "perfect" from file presence alone; runtime/browser checks are still required.
- Treating backend screen-session kill as the same thing as closing a local tab. Recovery expectations differ.
- Leaving local tab delete without confirm or undo/reopen; Dr. Sagar notices this kind of rough edge fast.
