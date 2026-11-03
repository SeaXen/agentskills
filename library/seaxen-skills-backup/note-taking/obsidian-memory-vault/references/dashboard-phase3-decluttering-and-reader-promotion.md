# Dashboard phase 3 decluttering and reader promotion

Use this after the first visual cleanup pass when the Obsidian dashboard is still functional but feels too busy.

## When this pass is needed

Typical signs:
- graph labels are readable but still noisy
- too many graph overlays compete with the canvas
- sidebar note cards feel heavy and repetitive
- reader works but still feels metadata-first instead of content-first

## Durable pattern that worked

### 1) Pull graph chrome out of the canvas
Do not keep preset pills, legend, minimap, and graph-meta badges floating over the graph if the page still feels crowded.

A good next step is:
- wrap the graph area in a `graphShell`
- split it into:
  - main canvas area
  - narrow side rail for graph utilities
- move these out of the canvas and into the side rail:
  - preset bar
  - graph meta pills
  - minimap
  - legend

This reduces overlay competition without removing capability.

### 2) Tighten label density aggressively
If the graph is still busy, reduce labels by default instead of trying to style around the clutter.

Known-good direction from this session:
- reduce `labelLimit`
- require higher zoom / degree thresholds for non-important labels
- keep labels easiest to show only for:
  - selected
  - hovered
  - pinned
  - connected
  - matched

Session result:
- prior label rule was still too permissive
- lowering the label cap and raising the threshold made the graph materially calmer

### 3) Make the sidebar compact by default
For note-heavy dashboards, non-selected notes do not need full preview + tags + health rows all the time.

A good default pattern:
- compact non-active, low-risk notes into 2-line cards
- keep visible:
  - title
  - folder badge
  - short meta line
- hide by default on compact rows:
  - preview
  - tags
  - health pills
- keep full detail for:
  - active note
  - searched / special states
  - broken/orphan notes when relevant

This preserves scan speed and lowers sidebar visual mass.

### 4) Promote the reader to content-first
If the reader still feels like a metadata tray, add useful content before the chip pile.

Known-good move:
- insert a `noteExcerpt` block below path and above facts
- populate it from `note.preview`
- hide it when empty
- give the reader more vertical share than the graph on normal desktop sizes

This made the lower pane feel more like an actual reading surface instead of a control annex.

## Concrete implementation notes

### HTML changes
- add `<div class="noteExcerpt" id="noteExcerpt" style="display:none"></div>` below `#notePath`
- replace the single graph area block with:
  - `.graphShell`
  - `.graphArea`
  - `.graphAside`

### CSS changes
Useful overrides from this pass:
- `.graphShell { display:grid; grid-template-columns:minmax(0,1fr) 220px; }`
- `.graphAside` as a scrollable rail with stacked utility cards
- reduce graph row share and increase reader row share
- reduce sidebar tools max-height
- add `.item.compact` style for non-active notes
- style `.noteExcerpt` as a lightweight content card

### JS changes
Patch these areas, not the backend:
- `renderGraphStats()` → fewer default status badges
- `renderGraphMetaBar()` → fewer pills; keep only useful state
- `renderList()` → add `compact` logic for normal notes
- `openNote()` → populate `#noteExcerpt`
- graph draw loop → lower `labelLimit` and tougher `showLabel` thresholds

## Verification pattern

After edits, verify more than syntax:
- `py_compile` passes
- extracted JS passes `node --check`
- dashboard service restarts cleanly
- root URL returns HTTP 200
- `/api/graph`, `/api/memory-health`, `/api/recall-eval`, `/api/memory-candidates` still work

Browser checks that mattered in this pass:
- `getComputedStyle(document.querySelector('.graphShell')).gridTemplateColumns`
- compact note count via `document.querySelectorAll('#notes .item.compact').length`
- graph meta child count via `#graphMetaBar`
- reader excerpt visibility via `#noteExcerpt`
- reader scroll height vs client height to confirm the panel still carries real content

## Honest success criteria

Do not call this pass complete just because the graph looks nicer.

A real phase-3 success looks like:
- graph center has materially less overlay competition
- label density is visibly lower
- most sidebar notes are compact by default
- reader excerpt is visible for normal notes
- APIs and graph integrity still verify cleanly

## Remaining limitation after this pass

Even after the phase-3 improvements, the dashboard can still feel tool-heavy if:
- graph edges/hulls remain visually loud
- sidebar cards are still over-decorated
- reader header/status language remains too system-ish

If that happens, the next pass should be polish, not more structural churn.