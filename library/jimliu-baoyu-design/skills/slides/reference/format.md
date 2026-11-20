# Slide HTML: the whole subset

A slide file, `project/slides/<id>.html`, holds exactly one `<section id="<id>">` on a fixed
1920×1080 px canvas (1440×1080 in a deck whose index has `"size":"4:3"`). Every style is inline in
`style="…"`. This page is the inline format, for a deck whose `project/deck.json` has no `format` key; a
deck with one shares `project/deck.css` and is written as ordinary HTML with classes
(`source-decks.md`). The page reads the file, lets people edit
it, and writes it back in the same format, normalized (canonical values, its own attribute order and
whitespace).

The subset is closed: the tags below and exactly the CSS in the table. What `open-artifact check` reports, and
what each level means:

| Level | When | What happens |
|---|---|---|
| `error` | Structure the page cannot represent: malformed markup, an unknown or misplaced tag, a limit passed, an image that is not an upload. | The slide is **held**: shown as far as it could be read, never edited or saved, until you fix the file. `open-artifact check` exits 1. |
| `warning` | A repair that changes what people see: a negative offset clamped to 0, an undeclared font dropped, a duplicate id dropped, a build on the wrong element dropped. | Applied when the slide is read; the next save writes the repaired form. Fix the file. |
| `info` … `dropped` | A property, value or attribute outside the subset (`unsupported`). | Dropped; the slide still opens. It did not apply: rewrite it in the subset. |
| `info` | An equivalent rewrite (a note): `pt` → `px`, `<strong>` → `<b>`, `class=` ignored, `font` shorthand expanded. | Nothing to do. |
| `info` `layout: …` | An estimate (a lint): low contrast, a box narrower than its longest word, overlapping pinned text, a long block arrow, a tiny icon, a ruled cell with no side padding. | Treat each as probably real and fix it. |

Lints are estimates from your styles: `open-artifact check` does not render the slide.

## Supported CSS

One line per property: the values it takes · the elements it applies to. `text` = `h1`, `h2`, `h3`,
`p`, `ul`, `ol` and `<div data-text>`; `box` = `section` and `div`; `flow child` = a child that is not
`position:absolute`; `pinned` = `position:absolute`. Anything else (`margin`, `z-index`, `float`,
`em`, `rem`, `vw`, `%` padding, `var()`, `calc()` outside `left`/`top`, …) is dropped.

```
LEN    = Npx or bare N (px); Npt converts at 1pt = 4/3 px — no em rem vw vh
PCT    = N%
N, INT = number, whole number
COLOR  = #hex | rgb[a]() | hsl[a]() | named | transparent — no currentcolor, var()
ANGLE  = Ndeg | Nturn | Nrad
ALIGN  = start | center | end | stretch | baseline (flex-start, flex-end, self-* and normal heal)
FAMILY = a deck.json face, a basic face, then serif | sans-serif | monospace | cursive | system-ui

position: absolute | relative · any element but section, span, cells; relative only matters on a div
left top right bottom: LEN | PCT | auto; left/top also calc(PCT ± LEN) · pinned only (negative → 0, a warning)
width height: LEN | PCT | auto · any but section, span, tr, x-connector; td/th: width only; table: no height
min-width: LEN | min-content | max-content · flow child
min-height max-width max-height: LEN · flow child
aspect-ratio: N | N / N · any but section
display: flex | grid | none (no display = column; inline-flex → flex) · box
flex-direction: row | column | row-reverse | column-reverse · flex box (row with no display → flex)
flex-wrap: wrap | nowrap · row box
gap: LEN [LEN] 0–512 · box
align-items: ALIGN · box
justify-content: start | center | end | space-between | space-around | space-evenly · flex box
justify-items: start | center | end | stretch · grid box
align-self: ALIGN | auto · flow child
justify-self: start | center | end | stretch | auto · grid child
flex: none | auto | N [N] [LEN | 0% | auto] · flow child (flex:1 = an equal share; an empty div + flex:1 = a spacer)
flex-grow flex-shrink: N · flow child
flex-basis: LEN | auto · flow child
grid-template-columns grid-template-rows: (LEN | Nfr | auto | repeat(INT, …))+, ≤24 tracks — no minmax, auto-fill, names, areas · grid box
grid-column grid-row: span INT (cells fill in source order) · grid child
padding: LEN ×1–4, 0–256 (no %) · box, text, table; td/th: 0–64, one value per table
overflow: hidden | visible · div
background: COLOR | [repeating-]linear-gradient(ANGLE | to SIDE, COLOR [PCT [PCT]], … 2–8 stops) | radial-gradient([circle|ellipse] [at X% Y%], …); one gradient[, COLOR under it] · box, text, img, table, x-icon; tr: COLOR; x-shape and hr: a flat fill (a gradient heals to one color)
background-clip: text (+ -webkit-text-fill-color:transparent): the glyphs show the gradient; url(IMG) center / cover|contain is allowed only here · text
color: COLOR · text, box, span, td/th, table, x-icon, x-connector, hr
font-family: FAMILY · text, box, table (inherits)
font-size: LEN 8–400 (clamped) · text, box, table; inherits into p and li, not h1–h3
font-weight: 100–900 (rounded to hundreds) | normal | bold · text, box, table, th; span: ≥600 = bold
font-style: normal | italic · text, box, span
font: [italic] [weight] SIZE[/LINE] FAMILY · expands to the longhands
line-height: N | PCT | LEN | normal (0.5–4× the size) · text, box, table
letter-spacing: LEN (−24–32) | Nem (−0.5–1) | normal · text, box, table
text-align: left | center | right | justify · text, box; td/th: no justify
text-transform: none | uppercase | lowercase | capitalize · text, box
white-space: normal | nowrap · text
text-decoration: none | underline | line-through [solid|double|dotted|dashed|wavy] [COLOR] · text; span: underline only
font-variant-numeric: normal | tabular-nums · text, table
-webkit-text-stroke: LEN 0–8 COLOR · text
text-shadow: LEN LEN [LEN] COLOR, … ≤8 (x y ±64, blur ≤64) · text, table
border: [LEN 0–16, else 1] solid | dashed | dotted | double | none [COLOR] — the style word is required · div, text, img, table, x-icon; the stroke of x-shape, hr, x-connector (≤32)
border-top -right -bottom -left: as border · div, text, img, table, x-icon; hr: border-top = its stroke
border-width, border-style: alone on x-connector only (elsewhere write border)
border-radius: LEN | PCT (≤50%) ×1–4 (TL TR BR BL; no / form) · div, text, img, table; x-shape rect/rounded
box-shadow: [inset] LEN LEN [LEN [LEN]] COLOR, … ≤8 (x y ±64, blur ≤160, spread ±32) · div, text, img, table, x-icon, x-shape
opacity: N 0–1 | PCT · any but span, cells, tr
transform: translate(LEN[, LEN]) | translateX|Y(LEN | -50%), rotate(ANGLE), scale(N 0.5–2), skew[X|Y](ANGLE ±60) — any subset, in that order, each once · any but section, span, cells, tr, x-connector; x-shape: rotate only
filter backdrop-filter: blur(LEN ≤20) brightness|contrast(N 0–2) saturate(N 0–3) grayscale|sepia|invert(N 0–1) hue-rotate(ANGLE) — any subset, each once · div, text, img, x-shape
mix-blend-mode: normal | multiply | screen | overlay | darken | lighten · div, text, img, x-shape
object-fit: cover | contain · img
accepted as no-ops: margin:0, box-sizing:border-box, grid-template:none, position:static, display:block
```

Spellings folded into the table (an `info` note): `padding-top|right|bottom|left|inline|block` →
`padding`; `row-gap`, `column-gap`, `grid-gap` → `gap`; `inset` → the four offsets; `flex-flow`;
`place-items`, `place-self`; `overflow-x|y`; `text-decoration-line|style|color`;
`-webkit-text-stroke-width|color`; `background-image` and `background-color` → `background`;
`-webkit-background-clip`; `-webkit-backdrop-filter`; `border-width|style|color` together → `border`;
`rotate` and `translate` → `transform`. `!important` is ignored.

Inherited text properties: `font-family`, `font-size`, `font-weight`, `font-style`, `line-height`,
`letter-spacing`, `color`, `text-align`, `text-transform`, set on the section or a `div`, flow down to
the text inside, except that `font-size` and `font-weight` never reach `h1`–`h3` (their tag defaults
hold until set on them).

## The slide

`<section id="<id>" data-transition="fade|push|magic" hidden style="…">`

- `id` equals the file name (`plan.html` → `id="plan"`; an error otherwise). Ids are
  `[A-Za-z0-9_-]{1,64}`.
- Always set `background` (a color or a gradient), the text defaults (`font-family`, `color`), and the
  layout: `display:flex; flex-direction:column` or `display:grid`, `padding` (the margins, normally
  128px), `gap`, `align-items`, `justify-content`.
- Children flow in it; `position:absolute` pins a child to the slide instead
  (`left`/`right`/`top`/`bottom`/`width`/`height`; `left` AND `right` = stretch; `left:50%` +
  `transform:translateX(-50%)` centers). Keep pinned boxes on the canvas and, normally, inside the
  128px margins (left + width ≤ 1792, top + height ≤ 952). A negative offset is clamped to 0 with a
  warning, so give an overhanging sticker room in its parent's padding.
- Paint order: later children paint on top, and all flow content paints as ONE layer where the first
  flow child sits. A pinned backdrop (picture, stripe, scrim) listed after the first flow child hides
  the flow text: list backdrops first.
- `<aside>`: the speaker notes, plain text (`<p>` and `<br>` keep line breaks; other markup is
  dropped), the section's last child, at most 4,000 characters. It takes no space on the slide. A second
  `<aside>` is joined to the first (a warning).
- `hidden`: the slide is skipped when presenting. `data-transition`: how this slide arrives (`magic`:
  see Motion).
- Nothing outside the section: no `<!doctype>`, `<html>`, `<head>`, `<body>`, `<title>`, `<meta>`,
  `<link>` or `<style>` (errors). The deck's title, outline and fonts live in `project/deck.json`.

## Text

- `<h1>` `<h2>` `<h3>` `<p>` (tag defaults 96/64/44/32px, weights 600/600/600/400, line-heights
  1.1/1.15/1.2/1.4; text with no `font-family` anywhere uses the system UI font). Set `font-size`
  yourself: 24px and up everywhere, labels, cells and footers too (not checked). `<h4>`–`<h6>` are
  errors: use `<h3>` or `<p>`.
- `<ul>`/`<ol>` of plain `<li>`; style the list, not the items. An item may end with a `<ul>` or `<ol>`
  of sub-items one level further in, up to 9 levels; markers change by level (bullets: disc, circle,
  square; numbers: 1, a, i) and each level indents 1.25em. `data-indent="N"` on an `<li>` puts it N
  levels further in than where it sits (an outline that skips a level). The page's Tab / Shift+Tab nest
  and un-nest the line being typed.
- `<div data-text>` (`data-text="N"`: the list indent in px, 0–256) of unstyled `<p>`, `<h1>`–`<h3>`,
  `<ul>`, `<ol>` = ONE text box: style the div; styles on its children are dropped.
- Inline, inside text only: `<b>` `<i>` `<u>` `<a href="https://…">` `<span style="color:…">` and
  `<br>`. `<strong>` → `<b>`, `<em>` → `<i>` (notes); `<code>`, `<s>`, `<mark>`, `<sup>`, `<sub>` and
  the like keep their text and lose the tag. A `<span>` takes `color`, `font-weight` (→ `<b>`),
  `font-style:italic` (→ `<i>`), `text-decoration:underline` (→ `<u>`) and nothing else: no sizes or
  fonts on spans (use two blocks). Links are http(s) only.
- Text written straight into a `div` or the section is wrapped in a `<p>` (a warning).
- At most 20,000 characters and 100 inline marks in one text element.
- A pill is a `<p>` with `background` + `padding` + `border-radius`.
- Give pinned text a `width` so it wraps. Text wraps only at spaces; a word wider than its box breaks
  mid-word (a lint), so size every box to its longest word: about 0.6 × `font-size` per character
  (more for bold or capitals) plus padding. At 44px, five cards across 1664px hold about 11 characters
  each.
- `white-space:nowrap` keeps one line (a flow box grows; a pinned box's text runs past its edge).
  `flex-wrap:wrap` on a row lets its children wrap. `min-width:min-content` or `max-content` on a flow
  text element or column keeps it at least as wide as its longest word or line (siblings shrink).
- `data-fit="shrink|none|grow"` on a text element, list, text box or table: what happens when its box
  is smaller than its text. `shrink` (the default) scales all its text down by one factor, to 60% of
  its size at most (never under 8px), then clips; `none` keeps the size and overflows; `grow` is never
  squeezed by its flex parent. See `layout.md`.

## Containers

- `<div>`: a flex row or column, or a grid; no `display` = a column; at most 15 nested. An empty
  `<div style="flex:1">` is a spacer. A `<div>` is invisible unless it has a `background`, `border` or
  `box-shadow`.
- `position:relative` on a `<div>` makes it the host of its `position:absolute` children (offsets are
  then relative to it). Without `relative`, an absolute child of a flow `<div>` pins to the slide (a
  note). A pinned `<div>` is itself the containing block of its pinned children.
- At most 24 pinned children in one host, **the section included** (an error past that). With more,
  group them into pinned or `position:relative` layer `<div>`s, or split the slide.
- `data-group` on a `<div>` marks a group people made on the page (at most 24 members): keep it.
- At most about 200 elements per slide (a warning past that; 800 is an error), 4,000 table cells and
  100 builds.

## Pictures and video

`<img src alt style="width; height; object-fit:cover|contain; border-radius">`:

- `src` is an upload, `/_blob/<id>` exactly as `open-artifact upload` printed it, or an installed design-system
  file, `project/ds/<folder>/<path>`. A `data:` URI, an http(s) URL or a bare file name is an error.
- `alt` = what it shows (`alt=""` if decorative), at most 500 characters.
- `data-crop="ZOOM X% Y%"` (zoom 1–50) is a person's crop: keep it unless `src` changes.
- `width`/`height` attributes are ignored: size it in `style`.
- A clip: `data-video="/_blob/<id>"` on the `<img>` (the picture is its still); a hosted video:
  `data-video-youtube|vimeo|loom|drive="<id>"`. Options and limits: `images.md`. A `<video>` is read
  and saved as `<img data-video>`.

## Tables

- `<table>` of `<tr>` with `<th>`/`<td>` of plain inline text; at most 100 rows × 24 columns.
  `<thead>`/`<tbody>` are implied (notes); `<caption>`, `<col>`, `colspan` and `rowspan` are dropped.
  A short row is filled with empty cells (a warning).
- A first row of `<th>` is the header. Column widths: `width:N%` on EVERY cell of the first row (any
  missing = equal columns).
- `text-align` on a cell aligns its column; `color` works on a cell; set `font-family`, `font-size` or
  `color` on the `<table>`, or it inherits them. A `<tr>` may carry `background:COLOR`; cells take no
  background.
- Cells pad 0.35em 0.6em unless a cell sets `padding` (one value for the whole table); never
  `padding:… 0` on a text cell: cells are ruled and the text would sit on the line (a lint).
- Rows are as tall as their content and a table as tall as its rows (a `height` on it is ignored). A
  row ≈ 2.1 × the font size per line of text; every row must fit under the heading. If not, use
  24–28px or split the table.
- Columns never grow for one long word: make each at least as wide as its longest word (0.6 × font
  size per character). Five or more columns at 32px in a half-width table do not fit: 24–26px, or
  abbreviate.
- Merged group headers: a painted flex row above the table whose parts use the columns' `width:N%`,
  summing to 100. Rotated headers: `diagrams.md`.

## Drawings and live embeds

`<svg aria-label="…" viewBox …>…</svg>`: charts, illustrations and a diagram's curved lines. One
opaque graphic: paths, shapes, gradients, filters, local `#id` references only. At most 52 KB. No
`<script>`, `on*=` handlers, `<foreignObject>` or external `href`/`url()` (errors). `<text>` gets a
warning: fonts never load in an svg, so labels are `<p>`s over it. Use numeric entities (`&#160;`) or
the XML five (`&amp;` …); other characters literally (`—`). Size it with `style` (`width`, `height`)
matching the `viewBox`. An svg takes no background, border or shadow: put it in a painted `div`.

`<x-embed style="position:absolute; left; top; width; height">…HTML…</x-embed>`: a small live page in
a sandboxed frame. The content is the BODY of a page (inline `<style>` and `<script>` are fine; no
`<html>`/`<head>`): it runs with scripts allowed and no network at all (`img-src data: blob:`,
`font-src data:`), so it cannot load files, fonts or libraries. The deck's fonts and styles do NOT
reach it: use a system font stack. Its background is transparent until painted; people cannot click or
type into it. A DIRECT child of `<section>`, pinned, with a width and a height (inside a `<div>`, or in
the flow, is an error); at most 16 KB each and 8 per slide. Thumbnails, the overview and exports show a
placeholder, not the page. The check does not read its contents, so keep its text 24px and up. In an
embed, animate with CSS `@keyframes`, not SMIL (SMIL can stand still until its first loop ends), and
keep it light: one canvas, not a heavy page, or presenting on a phone can stall.

## Shapes, icons and connectors

None of these hold content (anything inside is dropped with a warning).

- A painted `<div>` IS a rectangle. `<hr>` is a line: `border-top` (or `border`) is its stroke and
  thickness, else `color`; `width` as usual.
- `<x-shape kind="rect|rounded|ellipse|diamond|arrow-right|arrow-left|arrow-up|arrow-down|line"
  style="background; border; box-shadow; opacity; width; height; transform:rotate(…)">`: each kind
  fills its box (`background` is a flat fill, `border` its stroke). A block arrow's head is the last
  40% of its length: keep it near 2:1 (a lint past 3:1). `border-radius` only on `rect`/`rounded`.
- `<x-icon name="…" style="color; width; height">`, one of these names, exactly:
  `Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe GraduationCap Home Key
  Lightbulb Lightning Link Lock PaperPlane Play Search Settings Star ThumbsUp Tool Trust Users
  Verified Warning Wrench`. Any other name is an error. The glyph draws at about half the box: give it
  at least 32px (a lint below).
- `<x-connector x1 y1 x2 y2 head="end|both|none" head-start="none|open|filled"
  head-end="none|open|filled" route="straight|hv|vh|elbow" style="color; border-width;
  border-style:solid|dashed|dotted; opacity">`: a line with constant-size heads (`hv` = across then
  down, `vh` = down then across, `elbow` = three segments). Coordinates are px or `%` of its host, the
  section or a `position:relative` `<div>`; all four are required once any is given. A connector with
  coordinates is a pinned layer (it counts toward the host's 24) and takes no `left`, `top`, `width`,
  `height` or fill. Without coordinates it is a flow child whose line runs corner to corner of its box
  from `from="tl|tr|bl|br"` (default `tl`); in a row it is a 96px straight arrow. `width` and `height`
  on a flow connector are dropped today: size it with `flex`, or see `diagrams.md`.

## Motion (when presenting)

- `data-build-in` / `data-build-out="fade|rise|drop|left|right|scale|pop [order 1–50] [auto]"` on the
  section's direct `position:absolute` children only (elsewhere dropped, a warning). Numbered builds
  play first, by number (one number = one step, played together); the rest follow in source order,
  one step each (an element's build-in before its build-out). `auto` plays that step on its own after
  the previous one, without a click.
- `data-transition` on the section: `fade`, `push` or `magic`. Magic move: `data-transition="magic"` on
  the slide that arrives, plus the same `id` on the matching pinned element of both slides.
- SMIL inside an `<svg>` (`<animate>`, `<animateTransform>`, `<animateMotion>`, `<set>`) plays only when
  presenting, and only when it changes at most three times a second with one `begin` and a readable
  `dur`; elsewhere the drawing stands still at its own attributes. Nothing plays with reduced motion.
- CSS animations, `@starting-style` entrances, count-ups and in-flow fragments: source decks only
  (`source-decks.md`, Motion).

## Not in this subset

Any CSS not in the table (dropped); `<style>`, `<link>`, `<script>`, `<iframe>`, `<canvas>` and
`<object>` outside `<x-embed>` (errors); `on*=` handlers (dropped, a warning); merged
cells; hover states; keyframes (a source deck plays them, `source-decks.md`); `class` (ignored); `margin` (use `gap`, `padding` or a spacer);
`z-index` (paint order is source order).

## Errors, in one list

Malformed or unclosed markup; anything outside the one `<section>`; a section id that differs from the
file name; an unknown or misplaced tag (`<style>`, `<link>`, `<script>`, `<iframe>` included), `x-shape`
kind or `x-icon` name; `<h4>`–`<h6>`;
more than 15 nested `<div>`s; more than 24 pinned children in one host (the section included); an image
`src` that is not `/_blob/<id>` or `project/ds/…`; an `<x-embed>` that is not a pinned direct child of the
section, over 16 KB or over 8 on a slide; an `<svg>` over 52 KB or holding a script, handler,
foreignObject or external reference; a text element over 20,000 characters or 100 inline marks; a table
over 100 × 24; more than 4,000 table cells, 800 elements or 100 builds on a slide; an `<x-connector>`
missing a coordinate; a slide file over 1 MB.
