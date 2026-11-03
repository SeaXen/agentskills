# AceRoute Skills explorer — next-feature lessons

Use when extending AceRoute's Hermes Skills page beyond a simple inventory.

## What the user actually wanted
- A **real table view**, not a short static list.
- **Usage-aware** skill analytics: how many times each skill was called, last used, hot/stale/unused state.
- More features added proactively once the direction is clear.
- Visual fixes must be literal: if the user says remove text, remove it from the DOM; if they say two boxes should be the same size, verify visible parity, not just CSS height.

## Backend payload additions that worked
Starting from `collect_hermes_skills()`, merge Journey skill items by slug/title and expose:
- per-skill:
  - `use_count`
  - `last_used`
  - `state`
  - `pinned`
  - `created_by`
  - `stale`
  - normalized `tags`
- summary:
  - `used_skills`
  - `zero_use_skills`
  - `pinned_skills`
  - `active_skills`
  - `stale_skills`
  - `hot_skills`
  - `total_uses`
  - `tagged_skills`
- collections:
  - `categories[]` with `count`, `total_uses`, `used_skills`, `pinned_skills`
  - `top_used[]`
  - `stale_skills[]`
  - `unused_skills[]`
  - `top_tags[]`
  - `activity_timeline[]` with daily `skills`, `used`, `uses`, `stale`

## Frontend pattern that worked
### Explorer toolbar
Controls:
- search
- category filter
- state filter
- tag filter
- usage filter
- sort selector
- reset button

### Main table
Columns:
- Skill
- Category
- Uses
- Last Used
- Refs
- Status

Make rows clickable and keyboard-activatable. Use `row-clickable` styling and open a drawer on row click.

### Extra panels
Add these below/around the table:
- `Skill Activity` line chart
- `Top Tags` clickable stack list
- `Top Used Skills`
- `Stale + Unused Skills`
- `Skill Details`

### Filter state UX
Render a compact meta line plus active chips, e.g.:
- `3 / 187 skills • 3 used • 0 stale • 0 pinned`
- chips like `tag: docker`

### Skill detail drawer
Reuse the Journey drawer visual system for consistency.
Show:
- slug
- category
- path
- use count
- last used
- refs
- creator
- state
- description
- tags
- linked files

Useful interaction:
- clicking a tag in drawer sets the tag filter
- copy slug button

## Follow-on upgrades that proved valuable
### Filter chips and active-state polish
- When rendering active chips, join chip HTML with a literal spacer (`' '`) rather than `''` so adjacent badges do not visually merge (e.g. avoid `category: devopspreset: broken-refs`).
- When maintenance or category metric buttons represent the current filter, add an `.active` state so the selected view is obvious without reading the table.

### Maintenance queue evolution
Turn the maintenance panel into a real workbench, not a static list.
Add:
- sub-tabs for `broken refs`, `no refs`, `no tags`, `unused`
- per-row missing-path preview when broken refs exist
- row-level `copy list` action for missing paths
- toolbar actions for `Copy Missing Paths`, `Export TXT`, `Export JSON`, and `Open Next Broken`

Backend payload additions that helped:
- `maintenance_groups` keyed by maintenance class
- `broken_ref_report[]` with `id`, `name`, `category`, `path`, `missing_paths[]`

### Broken-ref fix assistant pattern
For broken linked-file diagnostics, do not stop at a count.
Expose exact missing paths grouped by skill, then provide three user actions:
- copy current skill's missing paths from drawer
- copy the full grouped report from the maintenance toolbar
- export the report as TXT and JSON for offline cleanup

### Drawer navigation pattern
When the table is filtered, the drawer should behave like a navigator over the filtered result set.
Add:
- `Prev Skill`
- `Next Skill`
- `Next Broken`
- subtitle position indicator like `2 / 29`

Important UX rule:
- disable prev/next buttons at edges
- disable `Next Broken` when there are no broken skills, or when only the current broken skill exists
- reset button disabled state when drawer closes

### Category chart multi-action
The category chart should support dataset-specific actions, not one generic click.
Useful mapping:
- `Total uses` bar click -> set category filter
- `Used skills` bar click -> set category filter + usage=`used`
- `Broken refs` bar click -> set category filter + preset=`broken-refs`

Also tint bars for the currently selected category so chart state matches right-side metric buttons.

### Fuzzy overlap detection
The simple shared-stub approach was too weak.
A better overlap heuristic used:
- `difflib.SequenceMatcher` on name
- `SequenceMatcher` on slug
- token overlap ratio
- shared tag count bonus
- same-category bonus

Only surface pairs above a threshold, and show a compact explanation like:
- weighted similarity score
- name ratio
- slug ratio
- token overlap
- shared tokens
- shared tag count

## Verification checklist
After rebuild, verify in browser console:
- Skills page is active
- control IDs include `skillsTagFilter`
- `#skillTagList .stack-item` count > 0
- `window.charts.skillsActivity` exists after render
- clicking a top-tag card changes `skillsTagFilter` and result meta count
- clicking first table row opens drawer (`#skillDrawerOverlay.active`)
- drawer title matches selected skill
- active chips render with visible separation between badges
- maintenance tabs render for `broken refs / no refs / no tags / unused`
- toolbar shows `Copy Missing Paths`, `Export TXT`, `Export JSON`, `Open Next Broken`
- `window.charts.skillsCategory.data.datasets` includes `Broken refs`
- clicking category chart dataset index 2 applies category + broken-ref preset
- drawer subtitle includes filtered position like `1 / 29`
- `Prev Skill` is disabled on the first filtered item
- `Next Skill` advances the drawer title on non-terminal items
- overlap panel includes `weighted similarity` copy

## Exact user-preference lessons
- If user says **same size**, check both outer card height and visible row/item count.
- If user says **remove this text**, remove it from DOM, not just with CSS.
- When user asks for more features, continue adding the next obvious high-value explorer features instead of stopping at one metric.