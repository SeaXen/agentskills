# AceRoute Skills page — pagination + preset filters + related drawer

Use when extending a Hermes-backed Skills explorer after the first usage-aware and maintenance-aware passes.

## What changed cleanly

### 1. Maintenance summary chips became real filters
The quick row under the result meta should be actionable, not decorative.

Good chips:
- no refs
- no tags
- no summary
- unused

Important rule:
- do not fake these by writing search text like `refs` into the free-text input
- keep a dedicated `skillsState.preset` and apply explicit predicates in `renderSkillFilteredView()`

Useful behavior:
- preset chips clear unrelated structured filters first
- structured filters (category/tag/search/page size) clear preset state when changed manually
- show the active preset as a result chip, e.g. `preset: no-refs`

## 2. Skills table needed real pagination
The old `slice(0, 80)` ceiling is fine for a prototype, but it hides rows and gives no navigation.

Working pattern:
- `skillsState.currentPage`
- page size selector: `20 / 40 / 80`
- footer summary:
  - `Showing 21–40 of 187 matching skills • page 2 / 10`
- Prev/Next buttons with disabled state at boundaries

Reset semantics that mattered:
- changing page size -> page 1
- changing category/state/tag/search -> page 1
- resetting all filters -> page size back to 40, page back to 1, preset cleared
- chart-click filters and tag/category clicks -> page 1

## 3. Related Skills panel in drawer
The drawer benefits from one more layer beyond metadata.

Cheap scoring heuristic that worked:
- same category: +3
- each shared tag: +2
- same creator: +1
- sort by score desc, then use_count desc, then name
- top 6 only

Render each related item as:
- skill name
- category
- use count
- score
- shared-tag badges
- clickable row to open the related skill drawer

Label this as a suggestion surface, not semantic truth.

## 4. Verification checks that mattered
Verify live in browser console after rebuild:
- quick-health chips exist and are buttons
- clicking first quick-health chip produces `preset: no-refs`
- page size change updates footer range text
- Next page updates footer page number
- opening a skill drawer populates `#skillDrawerRelated .stack-item`
- sticky header still reports `position: sticky`

## Files touched in AceRoute
- `static/index.html`
  - table footer controls
  - related-skills drawer card
- `static/js/dashboard.js`
  - `skillsState.currentPage`
  - `skillsState.preset`
  - `setSkillPresetFilter()`
  - `clearSkillPresetFilter()`
  - `changeSkillsPage()`
  - `relatedSkillsFor()`
  - pagination-aware `renderSkillFilteredView()`

## User-specific preference reinforced
When the user says 'upgrade next features', keep adding operational features, not cosmetic filler. Prefer controls that change workflow quality:
- actionable chips
- chart-as-filter behavior
- pagination
- better drawer context
