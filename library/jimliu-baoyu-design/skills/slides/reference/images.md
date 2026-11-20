# Pictures, video and SVG

How pictures and clips get into a deck, how to show them, and the rules for drawings. Fonts:
`fonts.md`.

## How pictures travel

Every picture FILE is uploaded: `open-artifact upload <root> <file>…` (with the Artifact tool, `call` `upload`
with `{file: "<absolute path>"}`) prints one line per file, the url first:

```
/_blob/3f9c0b7e2a4d4c1e9b8a7f6e5d4c3b2a	image/jpeg	482113	reef.jpg
```

The slide keeps only that url, written exactly as printed in `src`. The same bytes always get the same
url, so uploading a file twice is harmless. The one exception is a design system's picture copied in
with its install (`deck-files.md`): it is not uploaded, and its `src` is its path in the deck,
`project/ds/<folder>/<path>`, with no leading `/`.

The picture's bytes never go into a slide: never write a `data:` URI, an http(s) URL, a bare file name
or base64 (all errors). Nothing fetches URLs: save the image as a file and upload it.

- `png`, `jpg`, `gif`, `webp` and `avif` upload as they are. A photo much bigger than it will show is
  worth shrinking first to about 2× its box (the page itself downscales pictures people add to a
  2560px edge). One file is 25 MB at most.
- An `svg` file uploads too and shows through `<img>`, as a static image: scripts never run and external
  references never load. A small drawing (52 KB or less) can go into the slide as `<svg>` code instead
  (SVG, below).
- Any other format (`bmp`, `tiff`, `heic`, a PDF page): convert it to png or webp first.
- Cannot upload? Never write the picture into the slide another way. Leave an empty frame where it
  belongs, `<img alt="what goes here" style="width:…;height:…">` with no `src`: it keeps its box and
  people can fill it on the page. Tell the person which pictures are missing.

When you read a slide, its `src` values are uploads (`/_blob/<id>`) or a design system's files
(`project/ds/<folder>/…`). Keep every `src` exactly as it is when you edit the slide, and keep
`data-crop` (a person's crop, `ZOOM X% Y%`) unless the `src` changes.

## Video

A slide can hold a short clip: an `.mp4` (H.264) or `.webm` file of 20 MB or less. Upload the clip and
a still frame of it (a picture), then write the picture as an `<img>` and name the clip on it:

```html
<img src="/_blob/<still>" data-video="/_blob/<clip>" alt="what it shows" style="width:960px;height:540px;object-fit:cover">
```

The clip plays, looping, while its slide is presented, and on the page while its frame is selected
(a click selects it, and pauses or plays it). Everywhere else (thumbnails, the overview, exports) the
picture shows, so always give it one; without a still the frame is dark. `<video src="/_blob/<clip>"
poster="/_blob/<still>" aria-label="what it shows">` is read as the same thing and saved as the
`<img>`. `data-video` takes only an uploaded `/_blob/<id>` (anything else is dropped; the picture
stays).

Options on an uploaded clip:

- `data-video-sound="on"`: plays its sound (muted without it).
- `data-video-loop="off"`: plays once (it loops by default).
- `data-video-start="click"`: when presenting, the picture stays up until the frame is clicked
  (default: it starts with the slide).
- `data-video-delay="1.5"`: seconds (0–60) a clip that starts by itself waits.

At most four clips play at once on one slide.

**A hosted video** (YouTube, Vimeo, Loom, Google Drive) is named by its id, never its URL, on an `<img>`
with a size. Its `src`, an uploaded still, is optional: without one the page shows YouTube's own
thumbnail, and a placeholder for the others. Give it a still when you have one.

| Attribute | The id |
|---|---|
| `data-video-youtube` | the 11 characters after `v=` or `youtu.be/` |
| `data-video-vimeo` | the number in the link, then `/` and the hash after it (or after `h=`) if the link has one |
| `data-video-loom` | the last 32 characters of the link, before any `?` |
| `data-video-drive` | the characters between `/file/d/` and the next `/`, then `/` and the `resourcekey` value if the link has one |

`data-video-at="90"` starts it at that second (not for Google Drive). A hosted video plays in the
provider's own player, so it needs a network connection when presenting; one `<img>` holds at most one
video. Keep `data-video-still` as you find it: the page sets it.

If you edit a slide, keep its `data-video…` attributes as they are.

## SVG

Use SVG when crisp vector art matters: logos, charts, a diagram's curved lines. Either upload the file
and show it with `<img>`, or put the `<svg>…</svg>` code in the slide (`format.md`, Drawings). Either
way the page treats it as a sandboxed image: scripts never run and external references never load.

- SMIL animation (`<animate>`, `<animateTransform>`, `<animateMotion>`, `<set>`) plays only in `<svg>`
  code on the slide, only when presenting, and only if it changes at most three times a second with one
  `begin` and a readable `dur` (`format.md`, Motion). An uploaded file shown with `<img>` never plays
  it. The editor, thumbnails, PDF, PNG, PowerPoint and Reduce Motion show the drawing at its own
  attributes, so give each element the look it should have there (no `fill="freeze"` to rely on).
- A drawing holding `<foreignObject>` is refused in the slide (an error), so it never reaches an
  export; plain SVG is drawn as a picture in PowerPoint.

Code in the slide is checked: no `<script>`, `on*=` handlers, `<foreignObject>` or external `href` or
`url()` (errors), 52 KB at most. The markup inside is kept as you wrote it (only an `xmlns` is added if
missing). An `aria-label` on the `<svg>` is its description: set one when the drawing carries meaning (a
chart, a plan, a map) and leave it off pure decoration.

The drawing is read as XML: write a character as itself (`—`), as its number (`&#8212;`) or as one of
XML's five names (`&amp;` `&lt;` `&gt;` `&quot;` `&apos;`).

Fonts never load inside a drawing: `<text>` renders in a fallback font and gets clipped (a warning for
each). Keep labels OUT of the svg and paint them as real text over it (`layout.md`, Labels over a
picture).

## Display treatment

Look at each picture and decide how it is best shown. Photos fill their box (`object-fit:cover`).
Screenshots and diagrams fit inside it, keeping their shape (`object-fit:contain`), on a contrasting
background, and rarely carry anything on top (diagram labels are the exception).

Text over a picture is protected the way the deck's direction says, the same way every time: a card, a
scrim (`background:rgba(20,20,19,.6)`) or a `backdrop-filter:blur()` panel.

Use only the pictures the person gave you, a design system's pictures, photos found with a photo search
your harness provides (`photo-library.md`, licensed for reuse and uploaded), or an `<x-icon>`
(sparingly). No stock-photo URLs, no emoji, no decorative art you draw yourself unless asked. With no pictures, a
deck with good structure and no images is a fine deliverable. Never make up a picture or point at a file
you do not have.

## Borders and shadows

`border`, `border-radius`, `box-shadow`, `filter` and `opacity` work on an `<img>` as anywhere else
(`layout.md`, Paint and effects); the page's properties panel writes the same properties.

In a PowerPoint download, a picture's border and shadow become a picture outline and an outer shadow,
by PowerPoint's own approximations: `dashed` and `dotted` map to its dash styles; hex, `rgb()`,
`rgba()` and named colors convert. What an office shape cannot hold is drawn without it and noted in
the notes shown with the download: a `double` border (drawn single), a shadow's spread, an `inset` or layered
shadow, a blend mode, a `filter`.

## On the page

The Insert menu's **Image or video…** and dropping a file onto a slide both upload the file and place
it, pictures and clips (mp4, webm, mov) alike; **Video link…** takes a hosted video's link and writes
its id. You do not need to place every picture yourself.
