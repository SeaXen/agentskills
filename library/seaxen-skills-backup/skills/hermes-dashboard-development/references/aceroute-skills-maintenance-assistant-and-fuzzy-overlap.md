# AceRoute Skills page — maintenance assistant, drawer navigation, and fuzzy overlap pass

Use when extending the AceRoute Skills page beyond usage metrics into cleanup workflows and richer navigation.

## What worked in this pass
- Treat **broken refs** as a first-class maintenance dimension, not just a status badge.
- Give users **bulk maintenance views** with explicit tabs instead of one mixed queue.
- Treat the **Category Usage** chart as an action surface with dataset-specific behavior.
- Once the table becomes the main exploration surface, the skill drawer needs **prev/next navigation** tied to the current filtered result set.
- Simple exact-stub overlap detection is not enough after the skill library grows; a lightweight weighted similarity score is better.

## Backend payload additions that worked
From `collect_hermes_skills()` expose:

### Per-skill
- `broken_linked_files`
- `broken_linked_file_count`

### Summary
- `broken_ref_skills`

### Collections
- `maintenance_groups` with:
  - `broken-refs`
  - `no-refs`
  - `no-tags`
  - `unused`
- `broken_ref_report[]` with:
  - `id`
  - `name`
  - `category`
  - `path`
  - `missing_paths[]`
- `category_usage[]` should also carry:
  - `broken_ref_skills`
  - `pinned_skills`

## Broken-ref detection pattern
A practical SKILL.md pass used this heuristic:
- scan skill content for paths beginning with `references/`, `templates/`, `scripts/`, or `assets/`
- if referenced path is not in discovered `linked_files` and does not exist under the skill dir, count it as broken
- dedupe and sort before returning

This is good enough for dashboard triage even if it is not a full markdown-link parser.

## Maintenance queue UI pattern
### Toolbar
Add above the queue:
- maintenance tabs container
- `Copy Missing Paths` bulk action

### Tabs
Use explicit tabs for:
- `broken refs`
- `no refs`
- `no tags`
- `unused`

Render the active group from `maintenance_groups[activeTab]`.

### Row UX
For broken-ref rows:
- show exact missing paths inline
- add `copy list` button on the row
- keep row clickable to open drawer

## Drawer upgrades that worked
Add drawer actions:
- `Copy Missing Paths`
- `Prev Skill`
- `Next Skill`
- existing `Jump Category` / `Jump Tag`

### Navigation rule
Drawer prev/next must walk the **currently filtered skill list**, not the raw inventory.

Useful implementation pattern:
- during `renderSkillFilteredView()`, store ordered filtered ids in state
- on drawer open, compute current index from that filtered id list
- show position in subtitle, e.g. `2 / 29`

## Category chart multi-action pattern
`Category Usage` got materially better when each dataset meant something different:
- dataset 0 `Total uses` → set category filter
- dataset 1 `Used skills` → set category filter + used filter
- dataset 2 `Broken refs` → set category filter + broken-refs preset

Also highlight the active category by changing bar colors for the selected label.

## Fuzzy overlap detection that worked
Replace exact stub grouping with weighted pairwise similarity.

Inputs that worked:
- `SequenceMatcher` name ratio
- `SequenceMatcher` slug ratio
- token overlap on normalized slug/name tokens
- shared-tag count bonus
- same-category bonus

Practical threshold that worked here:
- keep pairs with overall score around `>= 0.58`
- if there are no shared tokens, require stronger direct name/slug similarity

Return overlap groups with:
- `score`
- `summary` like `name 0.81 • slug 0.76 • token 0.50`
- `shared_tokens[]`
- `shared_tag_count`
- the two candidate skills

## Verification checklist
After rebuild, verify in browser console:
- maintenance tabs render (`#skillMaintenanceTabs .maintenance-tab-btn`)
- maintenance rows include `copy list` for broken refs
- drawer actions include `Prev Skill`, `Next Skill`, and `Copy Missing Paths`
- opening a drawer shows filtered-position text like `1 / N`
- `charts.skillsCategory.data.datasets` includes `Broken refs`
- programmatic click on dataset 2 applies category + broken-refs state
- overlap panel text contains `weighted similarity`

## Important implementation caveat
When verifying Chart.js in browser automation, do not rely on a stale local variable if the chart may not be ready on the first tick. Read from `window.charts.skillsCategory` or `Chart.getChart(canvas)` after render and then call `chart.options.onClick(...)` with a synthetic element payload.
