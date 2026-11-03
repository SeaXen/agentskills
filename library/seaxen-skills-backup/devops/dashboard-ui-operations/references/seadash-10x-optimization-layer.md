# SeaDash 10x optimization and feature layer

Use after the compact SeaDash rewrite is already working and the user asks to make it “10/10”, add more features, or optimize.

## Priority order
1. **Optimize first** — add real timing and cache behavior before adding more UI.
2. Add high-leverage controls only: command palette, layout snapshots, health triage, scanner import safety.
3. Keep the app dependency-free unless explicitly asked otherwise: vanilla `index.html`, stdlib `server.py`, no build chain.
4. Live-verify browser behavior and API timings before committing/pushing.

## Backend optimization pattern
- Add `/api/dashboard` timing fields such as:
  - `docker`
  - `config`
  - `monitor`
  - `stats`
  - `total`
- Add short-lived caches:
  - Docker inventory cache around 5 seconds.
  - HTTP probe cache around 30 seconds.
  - Preserve existing monitor cache, but return explicit `cached: true/false` so the UI and tests can tell.
- Return `perf` in `/api/dashboard`:
  - `timing_ms`
  - `docker_cached`
  - `monitor_cached`
- Verify cold and warm calls. Warm dashboard calls should drop to tens of milliseconds if Docker/probe data is cached.

## Frontend feature layer
Add features as compact overlays, not a redesign:
- **Command palette** (`Ctrl/⌘+K` + header button): search actions and apps.
  - Open Health page
  - Open Scanner
  - Add manual app
  - Save layout snapshot
  - Switch section presets
  - Refresh dashboard
  - Open/favorite/hide/restart individual apps
- **Layout snapshots** in the existing Layout side panel.
  - Save named snapshots of layout-only keys.
  - Restore/delete snapshots.
  - Exclude routes/secrets from snapshots and layout export.
- **Health triage** should remain a filter/page showing only problems, not another giant dashboard.
- **Scanner import** must default unchecked/unselected and expose Select all / Clear selection.
- **Search** should be debounced to avoid full re-render on every keystroke.

## Safety semantics
- `Close` / `×` means hide app, not delete it.
- Hidden tab should visibly show `Unhide` and `Remove from hidden`.
- Destructive `Delete` remains for manual/custom apps only and should confirm.
- Safe Docker bulk action should skip healthy running containers unless the user explicitly chooses a destructive action.

## Verification checklist
Run all of these before reporting done:
- `python3 -m py_compile server.py`
- Extract inline JS from `index.html` and run `node --check`.
- Restart `seadash` and hit `/api/health`.
- Hit `/api/dashboard` twice and compare perf timings/cached flags.
- Browser-console verify:
  - command palette opens and filters commands
  - layout snapshot button/list exists
  - health filter switches and shows problem count
  - scanner checkboxes default unchecked
  - no console errors
- Review diff for secrets before commit.
- Commit and push only after live verification when the user asked for git push.

## Pitfalls
- Do not count this as “10/10” if warm API timing is still unmeasured.
- Do not add large charts, animations, or a framework just to look premium; this user values compact, fast, low-CPU operator UX.
- Do not store credentials or public route secrets in layout snapshots.
- Do not let service workers serve stale UI after changing frontend behavior; bump the SeaDash cache name.
