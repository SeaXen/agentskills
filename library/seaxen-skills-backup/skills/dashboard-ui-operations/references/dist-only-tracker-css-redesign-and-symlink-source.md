# Dist-only tracker CSS redesign + symlinked source detection

Use this reference when improving a dist-only dashboard tracker tab while preserving all existing behavior.

## Context

A Hermes 3rd Party tracker tab existed only as built dashboard assets under `dashboard/dist/`. The user wanted it compact and polished without losing update/inventory/manual-source operations.

## Low-risk redesign pattern

1. Prove the maintenance surface.
   - Read the shipped `dist/index.js` and `dist/style.css`.
   - Confirm whether editable source exists before touching built assets.
   - Inspect the live DOM classes and actual dimensions before patching.

2. Preserve behavior with a CSS-only override when JS is already correct.
   - Back up the stylesheet first.
   - Append a clearly marked override block instead of rewriting the bundle.
   - Keep existing class names, buttons, routes, and data flow unchanged.

3. Compact tracker UI by hierarchy, not decoration.
   - Reduce hero/title/meta/card padding.
   - Group top-right actions into an explicit cluster.
   - Shrink KPI/operator tiles so the page becomes denser without hiding controls.
   - Keep update actions, inventory/manual sections, copy/run/dry-run affordances visible.

4. Verify the served asset, not just the file on disk.
   - Fetch the served CSS with a cache-busting query and check for the redesign marker.
   - Check brace counts or equivalent syntax sanity for hand-edited CSS.
   - Run JS syntax check on the shipped bundle if touched/read as part of the verification.

5. Verify behavior across tracker modes.
   - Updates-only view still shows actionable update rows.
   - Full inventory view still shows manual/local items.
   - Manual visibility toggle still works.
   - Live scan / dry run / run all / copy visible / per-row copy/run controls are still present.
   - Browser console has no JS errors.
   - Browser visual pass confirms no overlaps, clipped controls, or haphazard empty space.

## Symlinked plugin source detection pattern

Copied or symlinked plugins can appear manual-only even when their real source lives inside a git repo.

Before leaving such a plugin as `unknown`:
- resolve the plugin path with `Path.resolve()` / `realpath`
- walk upward from the resolved target looking for a git worktree
- inspect its remote URL and branch/commit
- if the resolved plugin target is inside that repo, surface the upstream repo URL with explicit confidence/reason
- keep update automation cautious if the installed plugin directory itself is a symlink or weak-provenance item

Good operator wording:
- `source_confidence: exact_repo`
- `linked_repo_path: <resolved git repo>`
- manual reason like: `Installed as symlink into a git-managed source repo; plugin dir itself has no git remote`

Do not claim a symlinked plugin is safely auto-updatable just because the source repo was detected. Source attribution and update safety are separate decisions.
