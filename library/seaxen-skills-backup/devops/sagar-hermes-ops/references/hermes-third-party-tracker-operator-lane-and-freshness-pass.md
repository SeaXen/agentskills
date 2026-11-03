# Hermes third-party tracker — operator lane and freshness pass

Use after the tracker already has live-first refresh, manual-source confidence, and operator actions, but still feels summary-heavy or slightly ambiguous.

## Trigger
- User says the tab is good and then asks to "make it best"
- Visual audit says the page is polished but still underfilled
- Controls read like labels instead of explicit actions
- Safe-update area exists but does not clearly show scope/trust

## What to add

### 1) Operator lane near the top
Add 3-4 compact trust/action tiles above the deeper cards.

Recommended set:
- **Runnable actions** — count of safe visible actions/commands
- **Manual review** — count of copied/local items needing judgment
- **Weak source confidence** — count of `unknown` + `related_links`
- **Freshness** — short age label like `34m old` / `Fresh`

Rule: this lane should answer *what needs attention right now* faster than the deeper cards.

### 2) Explicit action labels
Rename terse labels to verbs/noun phrases.

Prefer:
- `View updates`
- `View inventory`
- `Run live scan`

Avoid:
- `Updates`
- `Inventory`
- `Scan live`

Reason: operators should not have to infer whether a control is a tab, filter, or action.

### 3) Persist view state
Store current mode and manual-visibility preference in `localStorage`.

Recommended keys:
- `tp-view-mode`
- `tp-show-manual`

Reason: update triage is repetitive work; reopening in the last-used mode reduces friction.

### 4) Freshness signaling
Do not rely only on a timestamp.

Add:
- hero freshness badge (e.g. `34m old`, `Fresh`)
- dedicated `Data freshness` tile in the health strip
- semantic freshness tones:
  - `ok` < 60m
  - `warn` < 6h
  - `bad` >= 6h

Simple JS helpers are enough:
- parse timestamp
- compute age in minutes
- map to label + tone

### 5) Bulk/safe-update scope card
The safe-update card should explain scope before execution.

Recommended stats:
- **Safe runnable**
- **Manual blocked**
- **Visible commands**
- **Current view**

Recommended copy:
- manual/copied installs stay out
- review generated commands before running all

Reason: `Run all` without visible scope feels unsafe even when the backend behavior is correct.

## Verification pattern
After the patch:
1. JS syntax check the dist bundle
2. Browser render check on the live route
3. DOM marker check for the new labels
4. Visual inspection for density/clarity
5. Console check for runtime errors

Useful DOM markers:
- top buttons: `View updates`, `View inventory`, `Run live scan`
- operator lane: `Runnable actions`, `Manual review`, `Weak source confidence`, `Freshness`
- bulk stats: `Safe runnable`, `Manual blocked`, `Visible commands`, `Current view`

## Session-specific note
A visual QA pass found the earlier tracker already solid but slightly underfilled. The winning move was not more charts or decorative metrics. It was:
- clearer control language
- a small operator lane
- visible freshness
- explicit safe-update scope

That made the page feel more operational without broad redesign.
