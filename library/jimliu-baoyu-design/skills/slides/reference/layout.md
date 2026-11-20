# Layout: flow, pinning, paint and how the page renders

SKILL.md shows the common slide. Read this page when a layout needs more than a column of blocks and a
card row, or a slide needs more than color and a card border. `format.md` has the exact grammar; this
page is how to use it.

## Two ways to place anything

A `<section>` is a 1920×1080 canvas. Its style is both its paint (`background`) and its layout:

- `padding` is the slide margin; 128px is the standard.
- `display:flex; flex-direction:column; gap` stacks the children top to bottom with space between.
- `justify-content:center` centers them vertically; `justify-content:end` sinks them to the bottom.
- A section with no `display` is a plain column with no gap.

Children are placed one of two ways:

- **Flow.** Flow children sit one after another in the section's layout, sized to their content
  unless you give them `width`, `height` or `flex`. Open space appears where the flow leaves it; open
  space LOW on a slide is correct. Do not reach for `justify-content:center` on every slide.
- **Pinned.** `position:absolute` children leave the flow and sit where `left`, `right`, `top` and
  `bottom` say, measured from the section's edge (`left:0` is the slide's edge, not the margin). Give
  them a `width` (text needs one to wrap), or pin both sides. Use pinning only for what flow cannot do:
  - a source line or page number at the bottom edge (the footer band, below);
  - a badge over a corner;
  - a full-bleed photo behind everything: `position:absolute; left:0; top:0; width:1920px;
    height:1080px; object-fit:cover`, listed FIRST so everything else paints over it;
  - an element that builds in or out, or a magic-move element.

Everything else goes in the flow.

Paint order is source order; there is no `z-index` (the page's bring-forward and send-backward
commands reorder the HTML). All flow content paints as one layer, where the first flow child sits, so
pinned backdrops go first. Inside a `position:relative` `<div>`, its pinned children paint over its flow
content.

At most 24 pinned children in one host, the section included. A slide that needs more (a big diagram,
a wall of labels) groups them into pinned layer `<div>`s with their own pinned children (each layer
holds up to 24 more), or splits into two slides.

## Flex idioms

- **Card row.** `<div style="display:flex; gap:32px">` with `flex:1` on each child makes equal columns;
  the default `align-items:stretch` makes every card as tall as the tallest. A card is a `<div>` with
  `display:flex; flex-direction:column; gap:12px` plus its paint (background, border, radius, padding).
- **Two unequal columns.** `flex:2` and `flex:1`, or `width:800px` on one and `flex:1` on the other.
- **Push apart.** An empty `<div style="flex:1"></div>` between siblings, or
  `justify-content:space-between` on the parent.
- **Bottom-anchored block.** A column section with `margin-top:auto` on the block (a deck with
  `format`), or an empty `flex:1` spacer above it (an inline deck has no `margin`).
- **Centered block**, for a one-off slide (a statement, a quote, a closing line):
  `justify-content:center` on the section's column. Without it a short column hangs from the top, which
  is what a slide with a heading wants (next idiom).
- **A run of slides with one layout** (the content slides of a deck; one slide per region, step or
  option): the heading sits at the top margin on every one, at the same height, so it stays put as the
  viewer flips through. Leave the section's column top-aligned and spread or anchor the BODY below
  the heading: `justify-content:space-between`, or a `flex:1` spacer above the block you want low.
  Centering the whole column makes the heading's height depend on how much the slide holds, so it hops
  20–60px between neighbouring slides, a common flaw in generated decks. A slide of a different kind
  (a centered statement with no heading) is free to differ.
- **Align a row's items.** `align-items:center` centers them vertically; `baseline` lines up text of
  different sizes on one line; `end` sinks them.
- **Big number + caption.** A column with `gap:8px`; the number 160–200px with `line-height:1`; the
  caption 28–32px in the softened tone.
- **Bar charts.** Every bar stands on ONE baseline: a track of fixed height that bottom-aligns its bars,
  `<div style="height:360px; display:flex; align-items:end; gap:12px">` holding the bar `<div>`s (each
  bar's `height` = its value × one scale for the whole slide), the value above each bar, the category
  label and any note BELOW the track. With several groups side by side (plan vs actual per team, one
  small chart per region), every group uses the same track height and scale, so all bars share one
  floor and the labels sit on one line. Never build a group as a top-aligned column with the bars
  first: short bars hang from the top at different heights. A waterfall (bridge) chart is the one
  exception: its middle bars float on purpose, each starting where the previous one ended; its first
  and last bars still stand on the floor.
- **Tree or linear flowchart.** Flow for a straight chain or a small tree (two levels, four leaves at
  most); pin anything bigger, a bracket, or lines that join or cross. `diagrams.md` has both.
- **Widths.** Every column, card, pill and legend item at least as wide as its longest word, or the word
  breaks in the middle (`format.md`, Text).

A `<div>` is invisible unless it has a `background`, `border` or `box-shadow`, so group freely: a plain
grouping `<div>` costs nothing visually. Fifteen levels is the limit; past three, the slide wants
splitting.

## Grid idioms

`display:grid; grid-template-columns:repeat(3, 1fr); gap:32px` fills children into cells in row-major
order; `grid-column:span 2` widens one. That is the whole grid vocabulary: tracks of px, `fr`, `auto` or
`repeat(N, …)`, and `gap` (row gap, column gap). No `minmax()`, `auto-fill`, named areas or line
numbers.

Use a grid for KPI tiles, photo grids, feature matrices and anything a flex row cannot keep square
(`aspect-ratio:1` or `4 / 3` on the tiles). Row heights follow the content unless you set
`grid-template-rows`. When the content is tabular, a table is usually better than a grid of text.

**A matrix is ONE grid, not many columns.** Three columns each holding a chip, a blurb and a card look
like three stacks, but they are one grid, `grid-template-columns:repeat(3, 1fr)`, with the nine
children in row-major order (chip, chip, chip, blurb, blurb, blurb, …). Grid rows line up across
columns; separate stacks drift apart as their heights differ. Parallel content (a bilingual table, a
before/after pair) shares rows the same way: one table with both as column groups, or one flex row per
row. Put a `gap` or a divider between side-by-side tables so their rules do not read as one.

## Footer band

A footer (page number, source line, logo) is ONE pinned 24px row (text, or a logo no taller) at
`bottom:64px`, in the same spot on every slide that has one. It sits at y ≈ 982–1016, nearer the edge
than content ever does; backdrops aside, it is the one pinned element allowed past the 952 line.
Nothing else enters its band: give that slide `padding:128px 128px 160px` so flow stops at y 920 (a
792px budget, not 824), and keep pinned content at `top + height ≤ 920`.

## Labels over a picture (and anything pinned to a box)

Wrap the `<img>` in a `<div>` with `position:relative` and a `width` and `height`; its
`position:absolute` children then pin to that box instead of the slide: badges, callouts, a caption bar
(`left:0; right:0; bottom:0; padding:24px 32px; background:rgba(0,0,0,.55); color:#fff`). Diagram
labels go here as real text, `<p>`s over the picture, never inside an `<svg>`: fonts do not load in a
drawing and exports cannot reach the words. The artwork is the picture; the words are `<p>`s over it.

## Paint and effects

- A gradient background is a deliberate choice, not a default. Flat, toned backgrounds are the norm;
  one gradient slide (a statement or the cover) is plenty.
- `border:1px solid #e3e6e4` draws a hairline one step off a light background (on a dark one,
  `rgba(255,255,255,.12)`). `border-top`, `-bottom`, `-left`, `-right` draw it only where you choose: a
  line above a card, under a header row, an accent bar down a quote. Sides may differ in width, never in
  style or color; for that, use a painted 4px div. Boxes that touch (stacked rows, tiles with no gap)
  share ONE stroke: `border-top:none` (or `border-left:none`) after the `border` on each box after the
  first, or keep the gap. Two adjacent strokes read as one double line.
- A circle is `border-radius:50%` on a square box: avatars, dots, markers.
- An `<x-icon>` draws its glyph at about half its box: at least 32px (48px beside 24px body text), in a
  color that stands off what is behind it. For a pale or accent icon, sit it on a filled chip (a small
  dark circle or square).
- Shadows are seasoning: one soft shadow, large blur, low opacity (`0 4px 24px rgba(0,0,0,.06)` on a
  white card over an off-white slide). Never dark, hard shadows; never shadows on text or on everything.
- `opacity` fades an element and everything inside it.
- Effects: a small `rotate(-2deg)` on one polaroid-style photo is playful, on three it is noise;
  `filter:blur(8px) brightness(.9)` on a full-bleed photo behind a statement; `backdrop-filter:
  blur(16px)` on a partly transparent div over a picture makes a frosted panel; `mix-blend-mode:
  multiply` on a colored div over a photo makes a duotone. Most decks need none; good ones use one
  effect idea consistently.

## Text

- Display text: `line-height` 1.05–1.15 and a slightly negative `letter-spacing`. Body text: 1.3–1.45.
- A small uppercase eyebrow: `letter-spacing` 2–4px and `text-transform:uppercase`.
- Keep `font-weight` within what the typeface has (`fonts.md`).
- Emphasis inside a sentence: `<b>`, `<i>`, `<span style="color:…">`, or `text-decoration:underline` in
  the accent color. A bigger word or a second typeface goes in a separate block.
- `text-shadow:0 2px 8px rgba(0,0,0,.4)` only for light text on a photo with no scrim.
- Gradient or picture text, when asked for: `background:linear-gradient(…)` (or `url(/_blob/<id>)
  center / cover`) with `background-clip:text; -webkit-text-fill-color:transparent` on the heading,
  `color` kept as its fallback, no box background on that element.

## How the page renders

The page, the presenter, thumbnails and exports use one layout engine: the browser's own flex and grid,
limited to the subset.

- **Nothing scrolls; a squeezed box shrinks its text.** When a slide holds more than fits, its column
  squeezes its boxes, and each squeezed text box, list or table (or a pinned text box given a height
  smaller than its text) scales its own text down until it fits, never below 60% of its size or 8px,
  and past that clips. Box by box: neighbours can land on different sizes, a one-line title at the floor
  can lose its descenders. A box in a row or a grid cell is as tall as its row or track and does not
  shrink. Treat a shrunken slide as a mistake to fix by splitting it. Per element, `data-fit="none"`
  keeps the authored size (text paints past its box) and `data-fit="grow"` keeps a column from
  squeezing that box at all; the default is `shrink`. Content inside a div with `overflow:hidden`
  clips; otherwise text too long for its box paints outside it.
- **Estimating heights.** One line ≈ `font-size × line-height`: a 96px heading at 1.15 takes about
  220px for two lines; a table row at 32px about 70px. Inside the 128px margins a slide has 824px of
  height (792px with a footer band).
- **Inheritance is CSS inheritance**, with one exception. The section's style sets the slide's
  defaults and an element's own style overrides them. Font family, size, weight and style,
  `line-height`, `letter-spacing`, `color`, `text-align` and `text-transform` inherit down; but
  `font-size` and `font-weight` reach `<p>` and `<li>`, never `<h1>`–`<h3>`, which keep their tag
  defaults until set on them. Paint (background, border, shadow) never inherits. Table text uses the
  table's `font-size`.
- **Flex and grid are real CSS flex and grid**, within the subset. `align-items` defaults to `stretch`:
  cards in a row take the height of the tallest, and text in a column spans the column's width (so
  `text-align` works across it). Children size to their content unless `flex` or `width` says
  otherwise. `justify-content` only acts when the parent is bigger than its content.
- **Table cells wrap**: a long cell makes its row taller, until the slide is over-full; then the
  squeezed table shrinks its text and, past the floor, clips. Count wrapped lines and split the slide
  before that. Every cell is ruled on all four sides and pads 0.35em 0.6em by default; leave that on
  text cells. `width` on the first row's cells sets the columns; `text-align` on a cell aligns its
  column.

## What the page does with structure

People never see the HTML tree. When they work on a slide:

- **Select**: a click selects the leaf element; an unpainted grouping `<div>` is not selectable. A
  `<div data-group>` is a group people made: it selects and moves as one. Keep the attribute.
- **Drag an element out of the flow** (or resize it from an edge the flow holds): the page pins it
  (`position:absolute`) where it was drawn. On a drag its former siblings reflow; on a resize whatever
  would have shifted is pinned too, and the containers it sat in keep their size (`min-width`,
  `min-height`), so the rest of the slide stays put.
- **Drag a painted container**: it moves whole; its children keep flowing inside it.
- **Delete**: the element goes; its siblings reflow.

The page writes these changes into the same file, so a slide you read again may have pinned elements
where you wrote flow. Keep them; do not "fix" them. It also writes the file normalized (canonical
values, its own whitespace and attribute order, comments dropped): compare by meaning, never by bytes.

## Example: one slide, flow plus pin

```html
<section id="kpis" style="background:#fbfbf8;color:#1a1a1a;font-family:Inter, Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:40px">
<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#2b7a78">Q3 in numbers</p>
<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:32px">
<div style="background:#ffffff;border:1px solid #e3e6e4;border-radius:16px;padding:40px;display:flex;flex-direction:column;gap:8px">
<p style="font-size:120px;font-weight:600;line-height:1;color:#0f2a3d">41%</p>
<p style="font-size:28px;color:#4a5568">faster ramp</p>
</div>
<div style="background:#ffffff;border:1px solid #e3e6e4;border-radius:16px;padding:40px;display:flex;flex-direction:column;gap:8px">
<p style="font-size:120px;font-weight:600;line-height:1;color:#0f2a3d">6→1</p>
<p style="font-size:28px;color:#4a5568">onboarding paths</p>
</div>
<div style="background:#ffffff;border:1px solid #e3e6e4;border-radius:16px;padding:40px;display:flex;flex-direction:column;gap:8px">
<p style="font-size:120px;font-weight:600;line-height:1;color:#0f2a3d">[__]</p>
<p style="font-size:28px;color:#4a5568">[third result]</p>
</div>
</div>
<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#6a7179">Source: [team survey, n=__]</p>
</section>
```
