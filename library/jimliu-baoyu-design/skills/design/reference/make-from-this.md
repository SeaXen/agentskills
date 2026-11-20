# Making something from this canvas

Read this FIRST when asked for a deck, an animation, a document, a page in another tool, or another width of a
page made from artboards on this canvas.

## A deck, an animation or a doc made from artboards

Read `project/canvas.json` and the artboards it is to be made from: the ones named or selected (`open-artifact
context <root>`), else all on the page in view, in reading order (rows top to bottom, each left to right;
`boards` gives each one's `x`, `y`). An artboard is one part: its `title` (or file name) names it, its copy is the
content, its look is the brief. Make the thing in its own type, never a picture of the canvas: one slide or section
per artboard unless the content asks otherwise, the text retyped as text, the images uploaded into the new artifact
(`open-artifact upload` there, from this canvas's `_blobs/`); an installed design system goes along, installed in
the new artifact the same way from its source folder. Leave the artboards as they are: never move, resize or edit
one for this.

Then hand it over on the canvas: add one entry to `notes` in `project/canvas.json`, under a key not already there,
`"deck1":{"kind":"link","x":0,"y":680,"href":"<the new artifact's link>","title":"Spring menu deck"}`: `href` is the
new artifact's link verbatim (its page's url, or its folder path when it has none), `title` its name (without it the
card shows the bare link). It draws a card 640 × 112 px that opens the artifact. Put it on bare canvas under what it
was made from: 120 px under that artboard, left edges level (made from a whole row: under the row's first
artboard). If something stands there or a row below leaves it no room, go down its column to the first bare
ground, 120 px under the last artboard there. Never right of the rightmost artboard: that is where the next
artboard goes. It covers nothing: no artboard, name strip, title or note. On a canvas with pages give it that
artboard's `page`. One card for each artifact; none for an artifact that already has one, none for one that has
nothing to do with this canvas. No link to give: no card; say in your reply where the new artifact is. Change only
the index (Revising: read it again right before you write it, change only your key). This is part of delivering
what was asked, so do it without being asked.

## Another design tool

Open **Share › Export** in the global frame shell to choose the file format and artboards.

- For **Figma**, select an artboard and choose its **HTML** option for Figma's capture extension. Open the exported HTML in Chrome,
  choose **Capture design** in the Figma extension, then paste onto a Figma Design page. A loopback HTTP
  preview also works for capture. The import contains editable text and visual layers. Component logic and
  props stay in the source project. [Figma Chrome extension](https://help.figma.com/hc/en-us/articles/9067379354135-Figma-Chrome-extension)
- **Canva and other tools that import files**: **PDF** (or every artboard of the page) or **PNG** for a
  picture. Canva imports a PDF as pages it can edit, swapping fonts it lacks. Never hand an import tool the
  canvas's local url: it is on this machine only.
- An artboard's HTML (**HTML (.zip)** or **single file**) is what to give a developer or another page.

## A page at another width

A fluid PAGE (`expand: "fill"`) shows at its board's `w`. To show it at another width too, keep one source:
add an artboard that imports it, such as `project/Home-phone.dc.html` with a fixed 390 px root holding
`<dc-import name="Home" hint-size="390px,1600px"></dc-import>`, its `$preview` and `boards` entry 390 wide and as
tall as the page runs at that width (taller beats clipped). Place it beside the original on the same row. Edits
to `Home.dc.html` show in both. Never copy the page's markup into a second file: the two drift apart.
