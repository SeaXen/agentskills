# canvas.json, pages, notes and design systems

`project/canvas.json` is the canvas: which artboards exist, where they sit,
on which page, plus notes and installed design systems. The page edits it
too (people drag, resize, add pages and notes), so read it again before
each change and change only what you mean to.

```json
{
  "v": 3,
  "createdOnFiles": { "v": 1, "at": "2026-11-14T10:00:00Z" },
  "title": "Checkout",
  "launch": { "view": "canvas", "page": "flow" },
  "pages": [
    { "id": "flow", "name": "Flow" },
    { "id": "parts", "name": "Components" }
  ],
  "boards": {
    "Cart.dc.html": { "x": 0, "y": 120, "w": 390, "h": 844, "title": "Cart", "page": "flow" },
    "Pay.dc.html": { "x": 490, "y": 120, "w": 390, "h": 844, "title": "Payment", "page": "flow", "is_interactive": true },
    "parts/Card.dc.html": { "x": 0, "y": 0, "w": 360, "h": 220, "page": "parts" }
  },
  "order": ["Cart.dc.html", "Pay.dc.html", "parts/Card.dc.html"],
  "notes": {
    "t1": { "kind": "title1", "x": 0, "y": 0, "text": "Checkout flow", "maxW": 880 },
    "n1": { "x": 980, "y": 120, "text": "Apple Pay only on iOS.", "color": "orange" }
  },
  "designSystems": []
}
```

## Top level

- `v` is 3. `createdOnFiles` marks a canvas made on files; `open-artifact open` writes
  it for a new folder.
- `title` names the design.
- `launch` is what opens first: `{"view": "canvas", "page": "<id>"}` or
  `{"view": "focused", "file": "<board path>"}` (one artboard full size,
  for a prototype).
- `pages`: at most 40, `id` matching `[A-Za-z0-9_-]{1,40}`. With no pages,
  everything is on one canvas. A board or note without `page` is on the
  first page.
- `order` lists every board exactly once: the reading order (arrow keys in
  the focused view, export order).

## Boards

The key is the artboard path under `project/`. Fields:

| Field | Meaning |
|---|---|
| `x`, `y` | Top-left on the canvas, px. |
| `w`, `h` | Size, 40–8000 px. Match the artboard's `$preview`. |
| `title` | Label above the frame; defaults to the file's `<title>`. |
| `page` | Page id. |
| `is_interactive` | It has working controls: the frame gets a Play button that hands clicks to the artboard. |
| `expand: "fill"` | The artboard fills the window in the focused view instead of keeping its size. |
| `print: "flow"`, `paper: "letter" \| "a4"` | Marks a document-like artboard for paginated printing. Share → Export → PDF in the frame shell paginates the artboard at the chosen paper width. |
| `frameless` | Drawn without a frame. Set by the page; leave it. |
| `radius` | Corner radius of the frame, px: a phone or tablet screen (about 40 for a phone). Leave it off a PAGE, print or poster. |
| `guides` | Up to 6 layout guides: `{ "kind": "columns" \| "rows" \| "grid", "count": 12, "gutter": 24, "margin": 32 }`. |

Boards on one page must not overlap. Lay them out on a grid with 80–120 px
gaps; leave at least 223 px above a row that has a title note.

## Notes

Keyed by id (`[A-Za-z0-9_-]{1,40}`), fewer than 1000. Every note has `x` and `y`. Stickies and titles also have `text`.

- `kind: "title1"` is a title over SEVERAL artboards, never over one (a frame's name strip already
  shows its `title` or file name): one bold 72 px line. Set `maxW` to its row's width (`maxH` if it is
  tight): longer text shrinks to fit. Put it at least 223 px above its row, clear of the name strips,
  with nothing over it.
- No `kind` is a sticky: set `w`; it grows to 4/3 of `w` tall (keep that space clear), taller on empty
  canvas, then scrolls.
- Both take `size` (px, or `s m l xl xxl`), `bold`, `italic`, `page`, and `color` (sticky: `fill`)
  from `gray red orange green teal blue purple pink`.
- `rect`, `oval`, `pen`, `line`, `arrow` and `image` are what people draw on the canvas: leave them.
- `groups` lists the groups a note belongs to, innermost first (ids like `g1`, at most 8 levels): people
  group notes with ⌘G and selecting one then selects its whole group. Keep the list when you move or
  restyle a note; drop an id from it only to take the note out of that group. Two or more notes make a
  group; a lone id means nothing.
- `kind: "link"` is a card that opens another artifact: `{"kind":"link","x":0,"y":680,"href":"<its link>","title":"Spring menu deck"}`,
  640 × 112 px; `title` is its name (left out, the card shows the bare link). When you make something else (a deck, a document) from
  artboards, add one under what it was made from: 120 px below that artboard, left edges level, on bare
  canvas, never right of the rightmost artboard; one per artifact. No link to give: no card; say in
  your reply where it is.

Use notes sparingly: a title per group, a sticky for a decision the person should see. Rationale and
options go in your reply, never on the canvas.

## Pages

Put alternatives or separate flows on their own pages, components the
screens import on a "Components" page. When you add a page, add boards with
its `page` id; when someone asks for "a new page", they usually mean a
canvas page, not a new artboard.

## Using a design system

Installing a system (its files under `project/ds/<folder>/`, its record in `designSystems`) and mounting
its components: `design-systems.md`.

## Checking

`open-artifact check <dir>` reports: a missing or invalid `canvas.json`, a wrong `v`,
bad page or note ids, boards whose file is missing, sizes out of range,
unknown pages, boards missing from `order` (or listed twice), artboard files
not on the canvas, overlapping boards, a `launch` that names nothing, and
installed systems without `tokens.json`.
