# Single-file frontend recovery for SeaDash

Use when `/mnt/tb/1Apps/SeaDash/index.html` has grown into a large monolithic HTML+JS file and UI regressions appear after repeated live patching.

## Symptom pattern
- Page chrome/header loads, but cards stay at `0`
- Stats bar stays on loading text
- Bell/settings/theme/edit controls are missing or dead
- Browser reports empty exceptions
- Backend endpoints still return valid data
- Manual `window.refreshAll()` repopulates the UI

## Strong diagnosis signal
If manual refresh/render works but cold page load does not, suspect **frontend boot/init/export ordering** or **syntax corruption in the main inline script**, not the API.

## Recovery order
1. Back up current `index.html`
2. Verify backend endpoints first (`/api/dashboard`, `/api/monitor`, `/api/docker`, `/api/stats` as applicable)
3. Extract inline script blocks and run `node --check` on each one separately
4. If parse failure appears in script 0/1, inspect surrounding template literals and recent patch boundaries
5. If multiple repair attempts are already layered into the file, stop adding more hooks
6. Restore from the newest known-good backup and re-apply only the requested features cleanly
7. Re-verify on **fresh page load** before accepting the fix

## Anti-patterns
- Adding more `setTimeout(window.refreshAll...)` calls after several failed attempts
- Leaving duplicate runtime repair layers active after the dashboard becomes usable
- Verifying only the manual refresh path and calling the job done
- Trusting shell HTML delivery as proof that the frontend JS executed fully

## Operator checks to keep
- grouped alert banner still renders concise summaries
- dead/offline apps sort to top where requested
- modal outside-click close still works
- rescan action remains subtle/small if user asked for low-visual-noise controls
- bell/settings/theme controls work from normal click path on first load
