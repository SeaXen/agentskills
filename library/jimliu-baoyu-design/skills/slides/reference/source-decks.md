# Source decks: shared CSS

Every new deck is written the way a web page is: ordinary HTML with classes, and one shared
stylesheet, `project/deck.css`, that holds the rules and `--variables` every slide uses. The page reads each slide
by browser rules, works it out to plain values, and edits it like any other slide. This page is what
differs from the inline format (`format.md`); everything it does not name (tags, `x-*` elements,
pictures, tables, limits) is the same.

## The deck

- `project/deck.json` carries `"v":5` and `"format":{"v":1,"shared":["project/deck.css"]}`, after
  `lists`:
  `{"v":5,"createdOnFiles":{"v":1,"at":"<now>"},"lists":"css","format":{"v":1,"shared":["project/deck.css"]},"title":"Q3 Review",…}`.
- `project/deck.css` is sent in the same step as the index. **Never write `format` without
  `project/deck.css`**: `open-artifact check` errors and every slide reads unstyled. If you cannot send both,
  write the deck inline, with `"v":4` and no `format`.
- `open-artifact open` on an empty folder writes such an index and a starter `project/deck.css` (plain defaults
  on `section`): replace the stylesheet with the deck's look before the first slide.
- A deck with slides and no `format` key is an inline deck, even with an empty `order`: revise it
  inline. Never add `format` to it, and never write classes, `var()` or fragments into its slides:
  `open-artifact check` warns that such a slide needs `project/deck.css`, and adding the key would change how the
  inline slides look. A `format` the page does not know (another `v`, another shared file) is an error.
- `project/deck.css` in a deck without `format` does nothing (`open-artifact check` says so).

## A slide

One `<section id="<id>">` per file, as in the inline format, with classes and inline styles as you
like. Write normal CSS. How it is read:

- **The cascade** is the browser's: the sheet, then the element's `style=""`, `!important`, selector
  specificity, source order, and inheritance of the text properties (font, size, weight, style,
  line-height, letter-spacing, colour, alignment, transform). A `body` or `section` rule sets the deck's
  defaults.
- **Values.** `var(--x, fallback)`, `em`, `rem`, `vw` / `vh` (of the slide), `pt`, `in`, `cm`, `mm`,
  and `calc()`, `min()`, `max()`, `clamp()` of those are worked out to px; `%` stays where the inline
  format takes it. Tag defaults:
  `h1` 96px, `h2` 64px, `h3` 44px, text 32px, `line-height:normal` 1.2, no default margins.
- **Box sizing.** `width` and `height` are the content box unless `box-sizing:border-box`, as in a
  browser; the page adds padding and border itself. Margins are kept and add up rather than collapse.
- **Generated content.** `::before` / `::after` with `content` becomes a line people cannot retype. A
  counter the `<section>` increments is its place in the deck:
  `section{counter-increment:page}` and `.folio::after{content:counter(page)}` make a page number.
- **Tags.** Other HTML tags become what the subset has: `header`, `footer`, `figure`, `blockquote`,
  `article`, `nav` and similar are boxes; `h4`–`h6`, `figcaption`, `dt`, `dd`, `pre`, `label` are lines;
  `strong` / `em` are bold / italic; `code`, `mark`, `small`, `sup`, `sub` and other phrases keep their
  text, not their look. A list with `list-style:none` becomes plain lines (a screen reader hears no
  list). Nested lists nest (`format.md`, Text).
- **Skipping.** `hidden` or `data-deck-skip` on the `<section>` skips the slide when presenting and
  downloading; `data-deck-skip="false"` does not.

## The stylesheet

- `@media` is read at the slide's size (1920×1080, or 1440×1080 in a 4:3 deck): `screen`, `all`,
  `only`, `not`, `orientation` and px `min-`/`max-` `width`/`height` apply;
  `prefers-reduced-motion:no-preference` applies, `reduce` does not; any other feature never matches.
- Selectors: type, class, id, `*`, the four combinators, `:first-child`, `:last-child`,
  `:nth-child()`, `:nth-of-type()` and their kin, `:only-child`, `:not()`, `:root`, `:empty`,
  `::before`, `::after`. Attribute selectors, `:is()`, `:where()`, `:has()`, `:hover`, `::marker`,
  `::first-line` and nested rules drop their rule, each with a warning on `project/deck.css`.
- `@import`, `@supports`, `@container`, `@layer` blocks and `@scope` are dropped with a warning: write
  the rules plainly. `@keyframes`, `@property` and `@starting-style` are kept for presenting (see
  Motion); `@font-face` and `@page` are skipped quietly; fonts come from deck.json `faces`
  (`fonts.md`).
- A `<style>` inside a slide holds that slide read-only: put the rules in `project/deck.css`.

## What does not carry over

What the inline format lacks is dropped from a source slide too, with an `info … dropped` line naming
the property (the table in `format.md` is what survives). Motion is kept apart from the still
slide: the editor, thumbnails and exports draw every slide at rest (fragments shown, animations at
their own style), and it plays only when presenting (below).

What to write instead of what is dropped (`→` names the replacement; with no arrow, nothing replaces
it):

- Stacking: `z-index`, `order` → source order; later elements paint on top (`format.md`, The slide).
- Layout: `float`, `columns`, `display:table` or `inline-block` side by side → flex or grid.
  `vertical-align`, `align-content` → `align-items`. `position:fixed` or `sticky` → `absolute`.
  `width:fit-content` → `align-self:start` in a flex column.
- Grid: `grid-template-areas`, `grid-area`, `grid-auto-*`, named lines, line numbers, `minmax()`,
  `auto-fill` → tracks of px, `fr`, `auto` or `repeat(N, …)`, cells in source order, `span N` to widen
  one.
- Clipping: `clip-path`, `mask` → `border-radius` with `overflow:hidden`, or an `<svg>`. `overflow:auto`
  or `scroll` → `hidden`, on a `<div>`.
- Fills: `url()` backgrounds, `background-size`, `background-position` → an `<img>` (a `url()` fills
  only text, with `background-clip:text`). `conic-gradient` or a second gradient layer → one
  gradient, or an `<svg>`. `object-position`.
- Borders: `outline` → `border`. A `border` needs its style word (`solid`, `dashed`, …).
- Transforms: 3D functions; functions out of the order translate, rotate, scale, skew; `filter:
  drop-shadow()` → `box-shadow`.
- Text: `word-break`, `hyphens`, `text-wrap`, `text-overflow`, `-webkit-line-clamp` → size the box.
  `writing-mode` → a pinned `<p>` turned with `transform:rotate(…)`. `font-variant`,
  `font-feature-settings` → `font-variant-numeric:tabular-nums`. `white-space` other than `normal` or
  `nowrap` → `<br>`. `text-indent`.
- Inside a line: a phrase keeps only colour, bold, italic and underline. A size, face, padding or pill
  → a block of its own.
- Tables: cell borders, `border-collapse`, `border-spacing`: every cell is ruled already. Fills →
  `background` on a `<tr>`, not on cells or `<thead>`.
- Caps: the ranges in `format.md`'s table (a `font-size` of 8–400px, `gap` 512, `padding` 256, 24 grid
  tracks, 2–8 gradient stops, 8 shadow layers, …) hold here too: `open-artifact check` names a value
  past one and what became of it.

## Motion

When presenting, a source slide plays what `project/deck.css` gives it, as the slide appears:

- `animation` with the deck's `@keyframes` (rules that load anything, `url(…)`, are left out).
  Put motion inside `@media (prefers-reduced-motion: no-preference)`; with reduced motion on, nothing
  plays anyway.
- `@starting-style` plus `transition`: the element starts from its `@starting-style` and moves to its
  own style with the transition's duration, easing and delay, so a `transition-delay` (e.g.
  `calc(var(--i) * 80ms)`) staggers a list in. Without a transition it would only cut, so nothing plays.
- Count-up: an animation whose first keyframe sets a registered numeric `@property` counts the first
  number in the element's text up from that value, keeping its decimals and thousands commas:

  ```css
  @property --n { syntax: '<integer>'; inherits: false; initial-value: 0 }
  @keyframes count { from { --n: 0 } }
  .n { animation: count 1.2s ease-out both }   /* <p class="n">93%</p> counts 0 → 93% */
  ```
- Fragments: a `class="fragment"` that is pinned (`position:absolute`, a direct child of the section)
  becomes a build that fades in; one in the flow fades in at its own click. Both step in
  `data-fragment-index` order (index N steps with build N + 1); fragments without one follow in
  document order. HTML export shows flow fragments from the start.
- SVG SMIL (`<animate>`, `<animateTransform>`, `<animateMotion>`, `<set>`) plays only when presenting.
- Flash guard: nothing changes more than three times a second. A looping animation (or SMIL) faster
  than that stands still or is removed, a finite one is slowed down to it, a two-keyframe one-shot of
  100–333 ms takes 334 ms, and SMIL with several `begin` times or an unreadable `dur` / `calcMode` is
  removed. Animations on an element that also has `data-build-in`/`-out` give way to the build.
- Pure `transition` (no `@starting-style`), hover and state classes, `offset-*` and scroll-driven
  timelines do not play.

## People's edits

The page writes an edit back into the slide's own markup: new words in place, a changed style as an
inline `style` on that one tag beside its classes, an added or removed element in place. When that
would not read back as what the person sees (an edit to generated content, a change the cascade
would undo), the page saves the whole slide **flat**: `<section data-flat …>`, every style inline, no
classes, no longer following `project/deck.css`. A slide a person adds is flat too. Leave `data-flat`
where you find it, and write a flat slide in the inline format (`format.md`); to bring it back to the
sheet, rewrite it with classes and drop `data-flat`.
