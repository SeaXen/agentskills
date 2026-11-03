# AceRoute Skills usage explorer

Concrete pattern for upgrading AceRoute's Hermes Skills page from a static inventory into a usage-aware explorer.

## Backend enrichment

Primary inventory source stays:
- `~/.hermes/skills/**/SKILL.md`

Usage source:
- `collect_hermes_journey()`

Merge rule that worked:
- build a lookup from Journey skill nodes keyed by lowercase `id` and `label`
- match those against skill `slug` and frontmatter title
- enrich each skill with:
  - `use_count`
  - `last_used`
  - `state`
  - `pinned`
  - `created_by`
  - `stale`

Stale heuristic used here:
- stale if `last_used` is 30+ days old
- also stale if `use_count == 0`

Useful aggregate summary fields:
- `used_skills`
- `zero_use_skills`
- `pinned_skills`
- `active_skills`
- `stale_skills`
- `hot_skills`
- `total_uses`

Useful category fields:
- `count`
- `total_uses`
- `used_skills`
- `pinned_skills`

Useful convenience lists:
- `top_used`
- `stale_skills`
- `unused_skills`

## Frontend layout that worked

### Summary row
Use 5 compact mini-stats:
- `Total Skills`
- `Used`
- `Hot`
- `Stale`
- `Total Uses`

### Explorer controls
Use one compact toolbar with:
- text search
- category filter
- state filter
- usage filter:
  - all
  - hot / pinned
  - used
  - unused
  - stale
- sort options:
  - most used
  - recently used
  - most refs
  - label A–Z
  - category A–Z
- reset button

### Main table columns
- `Skill`
- `Category`
- `Uses`
- `Last Used`
- `Refs`
- `Status`

### Side panels
- `Top Used Skills`
- `Stale + Unused Skills`

### Detail cards
For the filtered detail stack, include:
- category
- refs
- uses
- relative last-used time
- status badges
- tags
- linked file badges

## Status badge convention

- `pinned` when pinned
- `hot` when `use_count >= 5` or state is `active`
- `stale` when last use is old or use count is zero
- `unused` when `use_count == 0`

## Visual/layout lessons

1. If the user says the two side-by-side Skills panels should be the "same size", that usually means **same outer card height**.
2. Matching outer card height does **not** guarantee the same visible count because table rows are shorter than stacked category cards.
3. For visual parity:
   - set a shared outer card height
   - make both inner regions scroll
   - verify both outer height and visible-item counts in the browser
4. Do not interpret "full size" as "remove scroll and let the panel grow to full dataset height". That creates giant columns and obvious empty/imbalanced space.

## Verification recipe

Use browser DOM checks, not just screenshots:

- outer card heights for both columns
- visible row count inside `#skillsTable`
- visible item count inside `#skillCategoryList`
- header labels in `#skillsTable thead th`
- summary mini-stat count
- explorer control count
- `#skillTopUsed`, `#skillStaleList`, `#skillHighlights` item counts

Example live checks that proved the feature landed:
- summary cards present: `5`
- controls present: `5`
- table headers present: `Skill / Category / Uses / Last Used / Refs / Status`
- top-used panel populated
- stale/unused panel populated
- detail cards populated

## Caveat

When usage is merged from Journey, not every skill will have a usage entry. Treat missing usage as:
- `use_count = 0`
- `last_used = null`
- `state = unknown`
- `pinned = false`

This keeps the explorer stable and makes filtering deterministic.