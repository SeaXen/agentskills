# Diagrams: flowcharts, swimlanes, org charts, trees, timelines, system maps

Read this before any slide that shows boxes joined by lines. **Boxes first, in the file; lines
second.** Pick the layout (below), take its row and column numbers, and write the slide with only the
boxes (and lanes), keeping a node list (id, left, top, width, height) beside you, in your notes or as
an HTML comment above the host (`<!-- A 0,0,320,120  B 448,0,320,120 … -->`; the page drops comments
when it saves). Run `open-artifact check`. Only then add connectors and labels, reading every coordinate off that
list. If you notice you are computing connector coordinates before the boxes are written, stop and
write the boxes.

**Source order is paint order and reading order.** A screen reader or a PDF's text layer gets only the
text, in source order (boxes first, so each edge label comes after every box), and none of the lines.
Put the structure in the words: number sequential steps in their box text, carry an edge's word into
the step it leads to ("No → escalate to legal"), keep edge labels in the boxes' order, and let the
slide's title or the line under it say what the diagram shows ("Four stages; legal gates the last
two").

## Which layout

1. **A straight chain, or a small tree (two levels of branching, four leaves at most): flow.** Stack
   the boxes in a column (`display:flex; flex-direction:column; gap:24px`) with a down arrow between
   steps, `<x-shape kind="arrow-down" style="width:32px;height:24px;align-self:center;background:#…">`,
   and center the boxes with `align-self:center`. For a left-to-right chain use a row, with a bare
   `<x-connector>` (a 96px straight arrow) or `<x-shape kind="arrow-right" style="width:48px;height:24px">`
   between steps. Branches are columns inside a row. Nothing can overlap. The leaf boxes are painted
   `<p>`s (background, border, padding). Never a stretched block arrow for a long gap.
2. **A bigger tree, an org chart, a decision tree with more than four outcomes, or a bracket: the pinned
   Rows recipe** (below). In flow, the branches would not be joined by lines and the tree would crowd
   the top of the slide.
3. **Anything else** (loops, crossing lines, swimlanes, boxes with two parents, a map): **pin the boxes
   inside one host**, `<div style="position:relative; width:1664px; height:700px">`, with exact
   `left`/`top`/`width`/`height`: boxes first, then connectors, then labels (that order is the paint
   order). A host holds at most 24 pinned children, connectors included. Count boxes + connectors +
   labels before you start; past 24 (a bracket, a metro map, most swimlanes), use layers (More than 24
   pinned elements, below).

## Pinned diagrams

- **Boxes on a grid.** One pitch between columns and one between rows: for example 320px boxes at left
  0, 448, 896, 1344; 120px boxes at top 0, 290, 580. At least 32px between boxes. Boxes for the same
  kind of node share a size.
- **No box narrower than its longest word.** At 24px a node box is at least 200px wide, which holds a
  10-letter word with room to spare; add 16px per letter beyond 10 ("documentation", 13 letters →
  248px). At 28px: at least 232px, plus 18px per letter beyond 10. Bold or capitals: another 10%. Two
  lines of 24px text need a box about 100px tall; of 28px, about 112px. A pinned box's `width` is yours
  to set: `min-width:min-content` does not apply to a pinned box, and `white-space:nowrap` keeps one
  line without widening the box.
- **The columns do not allow that width? Use fewer columns, never narrower boxes or smaller text.** In
  order: (1) consecutive steps in different lanes or rows go in the SAME column, one above the other;
  step to a new column only when the next box is in the same lane; (2) wrap a long chain into two rows
  (left to right, then right to left below, joined by a `vh` at the turn); (3) merge boxes ("Validate &
  register"). Shorter labels are fine too. A 1664px host holds at most 7 columns of 200px boxes with
  44px gaps (lefts 0, 244, 488, 732, 976, 1220, 1464).
- **Connectors run from edge point to edge point.**
  - Edge points: the middle of the right edge is `(left + width, top + height/2)`; of the bottom edge,
    `(left + width/2, top + height)`. If an edge's midpoint is taken, use another point on that edge.
  - **Straight** when the two points share a row or a column.
  - **`vh`** (down, then across) from a top or bottom edge into a side edge; **`hv`** (across, then
    down) from a side edge into a top or bottom edge.
  - **One parent to several children, or several boxes into one**: the bus and join recipes in Rows (or
    the spine in Org chart). Never join a top or bottom edge to another top or bottom edge (a parent's
    bottom to a child's top) with `elbow`, `hv` or `vh`: one leg lies along a box's own border and the
    head lands sideways. (`vh` from a top or bottom edge into a SIDE edge, as in a swimlane hand-off, is
    fine.)
  - **`elbow`** only between boxes in different rows AND columns, side edge to side edge, when the
    points are at least as far apart sideways as up and down and the column gap is at least 96px: the
    middle leg then runs down that gap. Otherwise its first leg runs down the box's own side: use
    `hv`/`vh` from another edge, or three straight segments. Unsure: do not use `elbow`.
  - **Where legs run.** A horizontal leg runs in the gap between two rows, never at a y where a box sits
    unless it ends at that box. A vertical leg runs in the gap between two columns, or at a column's
    center when it enters a box from above or below. If a leg would pass a box at the box's own y (or
    x), move it into the gap: add a segment.
  - **Loop-back** (the last box back to the first): around the outside, down from the last box, along a
    clear strip below the boxes, up into the first box: three straight connectors with `head="none"`,
    `"none"`, `"end"`. Never run a connector through a box.
- **Labels are `<p>`s pinned beside their line**, never on it: at least 8px clear of the stroke and of
  every box (an angled label's first letter beside its dot is the one exception), with a `width`. Along
  a rail, path or timeline: period names (months, quarters) go inside or directly under the track; a
  milestone label sits only at the far end of its own leader line, and neighbouring leaders alternate
  two lengths (40px and 100px) or two sides so labels cannot touch; flags, ticks and "today" markers
  never share a label's strip; phase names go in a gutter, not on the track.
- **Angled labels (45°) on maps and dense timelines: use this recipe, not your eye.** `rotate` turns a
  box about its center, so a rotated label with its corner at the dot swings back across the line. For a
  dot centered at (X, Y), a label that starts beside the dot and runs up and to the right is:

  ```html
  <p style="position:absolute;left:{X−23}px;top:{Y−114}px;width:240px;height:34px;line-height:34px;font-size:24px;white-space:nowrap;transform:rotate(-45deg)">Station name</p>
  ```

  Down and to the right: the same with `top:{Y+80}px` and `rotate(45deg)`. Always `width:240px;
  height:34px`, whatever the text: it starts about 16px from the dot's center. Names of 13 characters at
  most (abbreviate); a 13-character label climbs about 160px, so parallel lines sit at least 170px apart
  (in a 700px host, four lines at y = 160, 330, 500, 670, every label above its line) and stations at
  least 56px apart along a line. `open-artifact check` cannot see rotated text: the recipe is the check.
- **Keep the slide within budget.** A title of about 70px, a 40px gap and a 700px host use 810px of the
  824px. With a pinned legend or source line at the bottom (a footer band, `layout.md`), give the slide
  `padding:128px 128px 160px` and a 16px gap: 786px of 792px. **Use the whole host**: the lowest row of
  boxes ends below y = 600 (the Rows tables do this); a diagram squeezed into the top half above an empty
  band reads as unfinished. If the brief allows two slides, split at about 12 nodes; if it must be one,
  keep 24px text and use Rows and the fewer-columns rule.
- **Before you finish, check the source: the geometry is the check.** `open-artifact check` cannot see where
  connector legs run, svg lines, angled labels or diamond text, so go down your node list once: (1)
  every connector's `x1,y1` and `x2,y2` is an edge midpoint of a listed box, or a bus or junction point
  from a recipe, none "about there"; (2) every horizontal leg's y is in a gap between rows, every
  vertical leg's x in a gap between columns or at a column center where it enters a box; (3) every label
  `<p>` is at least 8px from every line and box; (4) boxes are at least 32px apart (except boxes that
  touch on purpose and share one stroke) and inside the host; (5) `open-artifact check` prints no `layout:` lines
  for the slide. Built from the recipes, (1) and (2) hold by construction: check the connectors you
  improvised. No screenshots, no rendering.

## The connector element

```html
<x-connector x1="320" y1="60" x2="448" y2="60"></x-connector>
<x-connector x1="608" y1="160" x2="896" y2="320" route="vh" style="color:#2b7a78;border-width:3px"></x-connector>
<x-connector x1="1504" y1="160" x2="1504" y2="260" head="none" style="color:#8a9199;border-style:dashed"></x-connector>
```

- In a `<section>`, `x1 y1 x2 y2` are slide coordinates; in a `position:relative` `<div>` (or a pinned
  `<div>`), they are measured from that div's top-left, in px or `%` of it. They may fall outside the
  host, negative included: the line draws past its edges.
- With coordinates it takes no `left`, `top`, `width` or `height` (dropped), and holds no content. It is
  a pinned layer of its host and counts toward the host's 24.
- `head="end"` (the default) puts a filled head at `x2,y2`; `head="both"` at both ends; `head="none"` at
  neither. `head-start` / `head-end` (`none|open|filled`) set one end alone. A head is a constant size,
  about 4 stroke widths, at any length or angle.
- `route`: `straight` (default), `hv` (across, then down), `vh` (down, then across), `elbow` (three
  segments, bending at the middle of the longer run).
- Style: `color`, `border-width` (the stroke, 2px by default, 32px at most), `border-style:dashed` or
  `dotted`, `opacity`. No fill, shadow or radius. Lines have round caps and joins.
- **Without coordinates** it is a flow child whose line runs corner to corner of its own box from
  `from="tl|tr|bl|br"` (default `tl`). Its box is flat, so the line is horizontal: a 96px arrow pointing
  right (`from="tr"` points it left); `style="flex:1"` stretches it across the space in a row. `width`
  and `height` on it are dropped today, so it cannot run down a column: there use `<x-shape
  kind="arrow-down">` at about 32×24.

When `hv`, `vh` or `elbow` cannot make the path, chain straight connectors with `head="none"`:

- only the last segment carries a head;
- the `x2,y2` of one segment is EXACTLY the `x1,y1` of the next (the same numbers);
- the same width and color on all segments; never overlap or offset the ends to fill a corner;
- a dashed line's pattern restarts at each joint;
- a 45° segment has |dx| = |dy|.

A many-bend line nobody will edit piece by piece may be one `<svg>` `<path>` with round joins, in a box
that contains it.

`<x-shape kind="arrow-*">` is a block-arrow glyph: its head is the last 40% of its length and stretches
with it. Keep it near 2:1 (64×32) as a glyph; past about 3:1 `open-artifact check` flags it.

## Curves: `<svg>` paths

Use an `<svg>` only when a line must be curved: a `<path>` with a fixed-size `<marker>` for the head.
Make the svg cover the whole host, listed FIRST in the host, before the boxes (it is one picture the
size of the host; listed later it would sit over the boxes and take their clicks):

```html
<!-- A 0,0,320,120  B 896,0,320,120: an arc from A's right-edge midpoint (320,60) to B's left-edge midpoint (896,60), ending 8px short -->
<svg aria-label="A feeds B" width="1664" height="700" viewBox="0 0 1664 700" style="position:absolute;left:0;top:0;width:1664px;height:700px">
<defs><marker id="h" orient="auto" markerWidth="5" markerHeight="5" refX="2" refY="2" overflow="visible"><path d="M0 0 L4 2 L0 4 Z" fill="#2b7a78" stroke="none"/></marker></defs>
<path d="M 320 60 Q 608 180 888 60" fill="none" stroke="#2b7a78" stroke-width="4" marker-end="url(#h)"/>
</svg>
```

- Path coordinates are then the same numbers as your boxes' edges. Every path starts at one box's edge
  midpoint and ends at another's, copied from your node list (`M x1 y1 Q cx cy x2 y2`: only the control
  point is free; put it 80–160px to the outside of the straight line between the ends, or to the inside
  when the outside would leave the host).
- End the path 2 stroke widths short of the target point (8px at a 4px stroke): the marker's tip sits 2
  stroke widths past the path's end, so it then touches the edge. Never estimate an endpoint: if you
  cannot name the box edge a path ends on, it is wrong.
- `width`/`height` equal the `viewBox`; the marker's fill is the path's stroke color; keep the path at
  least 2 stroke widths inside the `viewBox`. `markerUnits` defaults to `strokeWidth`, so the head scales
  with the stroke; `orient="auto"` turns it with the line; `stroke-dasharray="12 10"` dashes it.
- No `<text>` inside. When the curves carry meaning the labels do not (direction, polarity), give the
  svg an `aria-label` saying it ("more listings → lower rents").
- On the page the svg is one picture: its arrows cannot be edited one by one.

## Building in two passes

Pass 1: write the slide with the title, the host, the lanes or rows and the boxes (no connectors, no
labels), with your node list, and run `open-artifact check`. Pass 2: add the connectors and labels from that list,
run `open-artifact check`, and fix until no `layout:` lines remain. Decide the rows and columns in a few lines, then
write: connector coordinates are worked out in pass 2 from boxes already in the file, never beforehand in
your head.

## Rows: trees, org charts, decision trees

Each level of the tree is one row of boxes in the 700px host. Work from the leaves up.

- **Count the leaves: they set the columns.** Up to 6 leaves fit in one row at 24px (six: 240px boxes
  at lefts 0, 285, 570, 854, 1139, 1424; five: 300px at 0, 341, 682, 1023, 1364; four: 380px at 0, 428,
  856, 1284). With 7–10 leaves, do NOT narrow the boxes: fold the last yes/no question into the leaf
  (one leaf card holds both answers: "NORMAL → Welch's t-test" above "NOT NORMAL → Mann–Whitney U"),
  which halves the leaf count. Still too many: the last row may hold two lines of leaves.
- **Rows fill the host.** 3 rows: box height 120, tops 0 / 290 / 580. 4 rows: height 96, tops 0 / 200 /
  400 / 600. 5 rows: height 80, tops 0 / 155 / 310 / 465 / 620. 6 rows: height 64 (one line of text;
  org charts and brackets only), tops 0 / 127 / 254 / 381 / 508 / 636. Leaf cards with two answers are
  taller: let the last row run down to 700.
- **Center each parent over its children**: parent `left` = (first child's left + last child's left +
  last child's width − parent width) / 2. Or make the parent exactly as wide as its children's span
  (left = first child's left; width = last child's right − first child's left): centered with no
  arithmetic, and wide parents read well as category bands.
- **Join a parent to its children with a bus, never `elbow`.** All segments straight. With the parent's
  bottom at y = P, its center at x = PC, the children's tops at y = C and their centers at x = C1 … Cn,
  the bus runs at y = B = C − 24:

  ```html
  <x-connector x1="PC" y1="P" x2="PC" y2="B" head="none"></x-connector>  <!-- drop from the parent -->
  <x-connector x1="C1" y1="B" x2="Cn" y2="B" head="none"></x-connector>  <!-- bar from first to last child center -->
  <x-connector x1="C1" y1="B" x2="C1" y2="C"></x-connector>              <!-- one stub per child; the head lands on it -->
  <x-connector x1="C2" y1="B" x2="C2" y2="C"></x-connector>
  ```

  If the parent's center is left of C1 or right of Cn, run the bar from PC. An org chart's stubs take
  `head="none"` too. A single child is one straight connector from (PC, P) to (PC, C). Keep at least
  48px between a parent's bottom and its children's tops.
- **Questions go in rounded boxes by default; a diamond is optional and holds one short line.** A
  `<x-shape kind="diamond">` of 320×120 holds a 24px question of 12 characters at most; 480×140 holds a
  28px question of 16 at most ("Two groups?", "Paired?"). Pin the question `<p>` at the diamond's
  `left`, `top + 43` (320×120) or `top + 52` (480×140), the diamond's full width, `text-align:center`,
  `white-space:nowrap`. A diamond is only as wide as its middle line: two lines or a longer question
  poke through the outline (shorten it or use a rounded box). Diamonds fit only the 3- and 4-row tables.
- **YES / NO** go inside the top of the child box as a small first line (`<p
  style="font-size:24px;font-weight:600;letter-spacing:1px">YES</p>` above its text): nothing to place,
  nothing for a line to cross. Beside the stubs instead: lower the bus to B = C − 56 and pin each label
  at `left` = stub x + 12, `top` = B + 10 (needs at least 72px between parent and children: the 3-, 4-
  and 5-row tables).
- **Dotted or secondary relationships** route exactly like solid ones (a bus, or `hv`/`vh` through the
  gaps), `border-style:dashed` and `head="none"`. Never a straight diagonal from box to box: it crosses
  the boxes in between.

**Brackets (knock-out tournaments)** turn the same idea on its side: each round is a column, two boxes
feed one box in the next column.

- 16 teams do not fit one column at 24px. Split: 8 teams down the left playing rightwards, 8 down the
  right playing leftwards, the final in the middle: seven columns of 200px boxes with 44px gaps (lefts 0,
  244, 488, 732 for the final, 976, 1220, 1464) and team boxes 48px tall. The two teams of one match may
  touch and share one stroke; keep 32px between matches.
- Each next-round box's center sits exactly half-way between the centers of its two feeders.
- **The join.** Feeder right edges at x = R, centers at y = T (upper) and L (lower); the next box's left
  edge at x = N, its center at M = (T + L) / 2; the junction at J = (R + N) / 2. Three connectors, no
  heads:

  ```html
  <x-connector x1="R" y1="T" x2="J" y2="L" route="hv" head="none"></x-connector>  <!-- upper arm and the upright -->
  <x-connector x1="R" y1="L" x2="J" y2="L" head="none"></x-connector>             <!-- lower arm -->
  <x-connector x1="J" y1="M" x2="N" y2="M" head="none"></x-connector>             <!-- stub into the next round -->
  ```

  With the columns above, J = R + 22. Mirror it for the right half. Never `elbow` here.
- Scores go inside the team box on the name's line (a flex row: the name `flex:1`, the score
  `white-space:nowrap`), not in a separate narrow box.
- A simpler alternative that reads well: each match as ONE card holding both teams, the column order
  carrying the progression, no connectors at all.

## More than 24 pinned elements

The 24 cap holds for every host, **the section included**, so pinning everything to the section is not
a way around it. Decide before you write:

- **Layers.** Split the pinned elements into a few layer `<div>`s, each one region of the diagram (a
  lane, a row band, the left and right halves of a bracket), each pinned in the host (or the section)
  with `position:absolute` and its own `left`/`top`/`width`/`height`, and each holding up to 24 pinned
  children. Coordinates inside a layer are measured from the layer's top-left: subtract its `left` and
  `top` from the host numbers in the recipes. Keep the layers side by side or stacked, not on top of one
  another. A connector between two regions goes in the layer it starts from, with coordinates past that
  layer's edges where it needs them (negative included). Paint order is the layers' source order, then
  their children's.
- **Or split the slide** (about 12 nodes per slide reads best).

About 200 elements per slide (nested ones count; a 16-team bracket with name and score `<p>`s is about
150). Keep lanes, boxes, connectors, labels in that order within each layer.

## Idioms

- **Swimlane.** The host is the pool; each lane is a full-width pinned painted `<div>` in it. Lanes are
  natural layers: pin a lane's boxes inside the lane (their `top` measured from the lane's top), so each
  lane holds up to 24 and the pool holds only the lanes. Leave a 60px strip under the last lane for
  loop-backs: 3 lanes 200px tall (tops 0 / 215 / 430), 4 lanes 150px (0 / 160 / 320 / 480), 5 lanes
  120px (0 / 128 / 256 / 384 / 512; one line of text per box). The same column `left`s in every lane.
  **A hand-off to another lane stays in the same column**: the next box directly below or above, joined
  by one straight vertical connector (in the lane it leaves, its `y2` past the lane's bottom edge); step
  one column right only when the next box is in the same lane. Merge trivial consecutive steps. Then
  count the columns and pick ONE plan: **up to 6 columns**: lane names in a 200px gutter, 200px boxes at
  lefts 232, 476, 720, 964, 1208, 1452; **7 or 8 columns**: the pool pinned to the section at
  `left:64px; width:1792px` (a dense process map is a reason for 64px side margins), lane names as one
  or two short words in a 128px gutter, 176px boxes at lefts 136, 347, 558, 769, 980, 1191, 1402, 1613
  in the pool (35px gaps); a 176px box holds a 10-letter word at 24px. More than 8 columns after sharing
  and merging: the process is too long for one legible slide; say so, and if it must be one slide, use
  20px step text in 150px boxes (lefts 136 + 186 per column, up to 9 columns), the only place text goes
  under 24px. Decisions are 240×120 diamonds holding one word and a question mark ("Disputed?", 10
  characters at most) or rounded boxes; YES continues along the row, NO leaves from the bottom tip. A
  loop back to an earlier step goes around: a straight drop into the strip below the lanes (or the band
  above the boxes in the top lane), a straight run along it, a straight rise into the target box's edge,
  heads `none` / `none` / `end`; each loop on its own line in the strip, 16px apart.
- **Org chart.** The Rows recipe (flow only for at most four leaves and no dotted lines). Reporting lines
  are buses with `head="none"`; dotted-line relationships are dashed buses or `hv`/`vh` routes through
  the gaps, never diagonals. More than about 6 reports under one head: a **spine** instead of a row:
  stack the reports in one column under the head, indented 40px, 24px apart; from one point on the
  head's bottom edge (x = head's left + 20) draw one `vh` connector with `head="none"` into the middle
  of each report's left edge.
- **Decision tree.** Up to four outcomes: flow (a diamond is a sized `position:relative` `<div>` centered
  with `align-self:center`, holding an `<x-shape kind="diamond">` and a pinned one-line `<p>`). Five or
  more: Rows, rounded question boxes by default. Either way a diamond holds ONE short line, and YES / NO
  go inside the top of the child box or beside the stub, never on a line.
- **Timeline / roadmap.** A flow row over a 4px painted rail, or pinned milestones at one regular pitch.
  Save width for the LAST label. Period names inside or directly under the track; milestone labels on
  the other side, on short leader lines of two alternating lengths. A multi-row "snake" is rows at one
  pitch (3 rows: tops 40 / 270 / 500, the track 60px tall) joined at alternate ends by a half-circle
  `<svg>` arc whose radius is half the row pitch (115 here) and whose ends are exactly the two track
  ends (end both tracks at least the radius plus 8px inside the host on the turning side), or by a
  straight vertical track segment; a two-leg connector cannot make a U-turn. Phase names in a 160px
  gutter on the left, not on the track.
- **Causal loop / architecture.** Nodes on a ring (up to 8, at the corners and edge midpoints of a
  1200×480 rectangle centered in the host, leaving 110px above and below for arcs) or in tiers. A causal
  loop's arrows are arcs in ONE `<svg>` covering the host, listed before the boxes, exactly as in Curves:
  every arc starts and ends at a box edge midpoint from your node list. If you cannot name the edge
  point an arc ends on, use a straight `<x-connector>` between the two edge midpoints instead (side
  edges when the other box is more beside than above or below), and keep straight links to ring
  neighbours so they do not cut across the middle. Architecture in tiers: buses and straight
  connectors; dashed lines for optional or delayed links. `+` / `−` signs in 28px bold `<p>`s 16px
  outside the arrowhead, on the outside of the ring; loop names (R1, B1) in the empty middle of each
  loop, at least 24px from any line. On a floor plan, flow arrows run along aisles, 24px from every
  table and seat, around furniture with `hv`/`vh`, never across it.
