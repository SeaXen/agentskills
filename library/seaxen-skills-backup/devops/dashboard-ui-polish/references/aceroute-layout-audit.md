# AceRoute layout audit — stat grids, chip rows, and chart-card stretch

Session-specific lessons from fixing AceRoute's dashboard-wide visual regressions.

## Trigger
Use this reference when a dashboard has multiple pages/tabs and the user complains that:
- stats bars are "correct" in data but visually broken
- some cards are huge while others are tiny
- empty space dominates the page
- newly added pages look much worse than old ones
- screenshot feedback says the whole page feels like a disaster, not just one component

## Root causes seen in this session
1. New pages reused old markup patterns but were **not included in the shared CSS selectors** for compact toolbar rows and summary stat grids.
2. New chip rows existed in HTML but **had no layout CSS**, so every chip became a full-width block.
3. New list rows existed in JS/HTML but **had no `.stack-row` styling**, so text looked jammed and alignment was inconsistent.
4. Grid containers used for mixed content let short cards **stretch to the height of tall chart cards**, creating giant empty rectangles.
5. Mobile/tablet overrides handled old pages only; new pages were missing from the responsive selectors.

## Durable fix pattern
### 1. Audit globally, not page-by-page first
When several new tabs all look wrong, inspect the shared layout system before tweaking individual pages.

Check these classes/selectors first:
- summary/stat grid wrappers
- chip rows / insights rows
- stack/list row styling
- chart-grid alignment behavior
- toolbar / top-row compaction selectors
- mobile/tablet selector coverage

### 2. Make new-page stat bars use a real grid
For new dashboard pages, define an explicit grid for the page summary wrapper.
Pattern:
- `display:grid`
- `grid-template-columns: repeat(auto-fit, minmax(150px, 1fr))`
- `align-items:stretch`
- stat cards with fixed compact min-height and centered content

Symptom if missing:
- one stat per row
- giant full-width cards
- lots of wasted vertical space

### 3. Give chips and quick actions a shared grid/flex system
For insight chips / quick-jump buttons, define a real row layout.
Good default:
- `display:grid`
- `grid-template-columns: repeat(auto-fit, minmax(150px, 1fr))`
- `gap: 8px`

Symptom if missing:
- each chip spans full width
- dashboard looks like a stack of unrelated slabs

### 4. Define `.stack-row` explicitly
If JS renders rows like `<div class="stack-row">...`, make sure CSS exists for:
- left/right alignment
- gap
- padding
- border/background
- hover state for clickable rows
- truncation/overflow rules for the left text column

Symptom if missing:
- titles and metadata run together
- rows look like plain text instead of structured cards

### 5. Prevent grid item stretch on mixed chart/list layouts
Add `align-items:start` on chart grids containing both charts and short list cards.
Optionally override wide-span cards per page if needed.

Symptom if missing:
- short cards stretch to the chart height
- giant empty boxes under small lists

### 6. Extend responsive selectors whenever adding new pages
If mobile/tablet rules target page-specific IDs, every new page must be added deliberately.
Typical misses:
- stat grids not horizontal-scrollable on tablet/mobile
- top bar meta not hidden on small screens
- chip rows not collapsing cleanly
- chart grids not dropping to one column

## Verification checklist
Before saying a dashboard polish pass is done:
- check **every tab/page affected**, not just the one the user first mentioned
- visually confirm stat rows are multi-column, equal-height, compact
- confirm no chip row has become a vertical stack of full-width blocks
- confirm short cards do not stretch to tall chart height
- compare at least one desktop screenshot and one mobile/tablet rule path
- if screenshots were provided, verify against those literally

## Good phrasing to remember
If the user says the pages are a disaster, do not answer with a feature summary. Treat it as a layout-system bug hunt first.