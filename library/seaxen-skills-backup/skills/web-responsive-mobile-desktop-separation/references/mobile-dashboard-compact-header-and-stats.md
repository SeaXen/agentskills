# Mobile dashboard compactness pattern — AceRoute case

Use this when the user says mobile still feels too big even after a normal responsive pass.

## Trigger phrases
- "mobile not fit properly"
- "header take half of screen"
- "still not fit to mobile screen"
- "make change only for mobile"
- "remove from to box"
- "make icon so that header only one line"
- "make search in two line"
- "stats and monthly summary card look big"

## Correct pattern

### 1. Keep desktop untouched
Load a separate mobile stylesheet:

```html
<link rel="stylesheet" href="/static/css/mobile.css" media="(max-width:1024px)">
```

Do not keep piling mobile fixes into desktop inline CSS.

### 2. One-line mobile header
For dense dashboards, the user may prefer a true one-line mobile header:
- keep only logo + a few compact actions
- hide large filter controls like `FROM/TO` on mobile
- convert CSV / Refresh / theme controls into compact icon-style buttons or very short controls
- shrink logo/image/text sizes aggressively

### 3. Two-line action/test area
Do not stack each input/button pair into 4 vertical blocks. Use a 2-row grid:
- row 1 = search input + search button
- row 2 = extract input + extract button

### 4. Horizontal stat rows on mobile
If overview and monthly summary cards still feel too large, switch from wrapped grids to horizontally scrollable single rows:
- `grid-auto-flow: column`
- fixed `grid-auto-columns` (e.g. 120–132px)
- `overflow-x: auto`
- smaller value/label/subtext sizing

This preserves density without making cards huge.

### 5. Tighten recent-query tables
The mobile pain point is often the query column. Fix by:
- capping query column width
- shrinking time / latency columns
- reducing font/padding
- keeping horizontal scrolling available

### 6. Extract/Hermes stat cards need explicit mobile classes
If stat rows are rendered from JS with inline `display:grid`, move them to named classes like:
- `.extract-stats-grid`
- `.hermes-stats-grid`

Then style those classes in the mobile stylesheet. Otherwise mobile CSS cannot reliably control the layout.

## Why this matters
The user repeatedly rejected generic responsive stacking because it still wasted vertical space. The winning pattern was **aggressive mobile compactness**: hide non-essential controls, keep header to one line, use 2-line action areas, and move stats into horizontal scroll rows.
