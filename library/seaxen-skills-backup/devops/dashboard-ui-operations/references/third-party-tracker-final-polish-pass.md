# Third-party tracker final polish pass

Session pattern: after the tracker already had safe update controls, registry management, persisted manual review state, and live cron/status metadata, the remaining high-value work was **operator polish without product bloat**.

## Durable additions that were worth keeping

### 1) Export the operator state directly from the UI
For tracker-style dashboard tabs, lightweight export actions are useful when the state already exists client-side or via a simple plugin API.

Good defaults:
- `Export registry` — current custom repo registry JSON
- `Export state` — persisted known/ignored/notes state JSON
- `Export audit` — recent audit rows JSON

Implementation shape:
- generate a `Blob` from `JSON.stringify(data, null, 2)`
- create a temporary object URL
- click a temporary `<a download>` element
- revoke the object URL shortly after
- show a short notice/toast so the operator knows the export fired

Why this is worth it:
- gives the operator a fast backup/debug artifact
- avoids inventing backend file-download endpoints when the data already exists in the browser
- keeps the tracker self-serve for review and migration work

## 2) Add `Copy cd` helpers for repo-backed rows
When rows represent local repos or filesystem-backed installs, `Copy path` is weaker than `Copy cd`.

Useful surfaces:
- tracked external repos
- dashboard registry entries
- normal repo/update rows
- manual plugin rows when a local path exists

Recommended helper text:
- `cd /absolute/path`

This is better than only copying the raw path because it is immediately pasteable into a shell.

## 3) Let manual-review cards collapse
If the tracker has many manual/local items, the page becomes noisy even when the data is good.

Good defaults:
- per-item `Collapse` / `Expand`
- global `Collapse all` / `Expand all`
- persist collapse state locally in `localStorage`
- when collapsed, still show minimal identity: path and note preview if present

Design rule:
- collapsed state should reduce noise, not hide the item entirely
- keep primary actions visible in the header row even when collapsed

## 4) Color-code audit rows by event class
Audit sections become much easier to scan if event type is visible before reading the body.

Useful event tones:
- add-repo → green
- remove-repo → amber
- state-save → cyan/blue
- run-update / run-update-all-item → violet
- failed events → red

Keep the event chip text explicit too (`ADD-REPO`, `STATE-SAVE`, etc.). Color alone is not enough.

## 5) Verification pattern for this polish tier
Do not stop at syntax checks.

Verify all of these:
- `node --check` for dist JS
- Python compile for plugin/generator backends if touched
- browser text or DOM contains new controls (`Export registry`, `Export state`, `Export audit`, `Copy cd`, `Expand all`, `Collapse all`)
- browser-driven interaction changes DOM state, not just renders buttons
  - collapse-all increases `.tp-item-collapsed`
  - expand-all clears collapsed count
  - export button triggers a notice/toast
- browser console remains at zero JS errors after interaction

## Product judgment rule
Once a tracker already has:
- actionable update controls
- safe dry-run/apply split
- visible command lists
- registry management
- persisted manual review state
- live scan freshness and cron status
- audit visibility

then the next step is usually **stop adding features** unless a real operator pain appears.

Prefer:
- compact polish
- better scanning
- safer exports/helpers

over new heavyweight panels or clever abstractions.
