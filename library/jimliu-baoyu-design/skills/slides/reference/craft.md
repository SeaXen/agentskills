# Designing a good deck: the long form

SKILL.md has the checklist; this page is the reasoning behind it. Read it when the person argues with a
design choice, asks for a kind of deck the checklist does not cover (a keynote, a training deck), or
asks for speaker notes. The content rules every artifact type shares are at the end.

There is no house look beyond the default typefaces. The fonts are the faces you declare
(`fonts.md`); the palette is the hex colors you choose for the brief.

## The rules, with their numbers

- **One idea per slide.** One big statement beats three bullet-ish slides; several short slides beat
  one crowded slide.
- **128px edge margins** are the standard: `padding:128px` on the section, and pinned elements 128px
  from an edge unless you have a reason.
- **Respect your type scale.** Four or five sizes, reused: eyebrows 24–28px (uppercase, extra letter
  spacing, accent color) for labels; headings for statements; 40–48px for agenda-level points;
  28–32px for sentences. Never under 24px.
- **Change backgrounds on purpose.** The palette's dark color for the opening and closing slides, the
  light color for the main content, the accent for one statement slide: the single number or sentence
  people should remember. Always set `background` on every section.
- **Width discipline.** Flow text inside the margins is 1664px wide, too wide for body text. Put
  sentences in a column 800–1000px wide (`width:960px`, or a `flex:1` column beside something else).
  Display lines work best at about 1400px. The other limit is the longest word (`format.md`, Text):
  count characters before you choose how many columns to use.
- **Vertical space budget.** The slide is 1080px tall and nothing scrolls; an over-full slide squeezes
  its boxes and shrinks their text, which reads as a mistake. Inside the 128px margins there are 824px:
  - a two-line heading at 96px, line-height 1.1 ≈ 210px;
  - a gap: 48px;
  - a table row ≈ 2.1 × the font size per line of text in its tallest cell: at 32px one row ≈ 70px, so
    9 rows ≈ 630px, which does not fit under that heading; a two-line cell counts twice;
  - a card = lines × font-size × line-height + padding.

  Never give a text box a fixed `height` smaller than that total: leave the height out. Too tall: 24–28px
  for tables, or split the slide.
- Keep decks under about 50 slides. The markup is tiny; a deck's weight is its pictures. Reuse one
  upload rather than several crops of it.

## You are a presentation designer

Think like a consultant or an executive preparing boardroom material: clarity, narrative flow,
back-of-the-room readability. The subset is deliberately not the web: each slide is a fixed 1920×1080
page, designed like a poster, and makes sense on its own.

Ask only what you cannot work out yourself (the length and the audience, when the request does not hint
at them). A topic and an occasion are enough to start a draft.

A font size the person gives is in **points**: px = pt × 2 (a slide is 960pt wide, so "36pt" = 72px).
Convert it yourself and write px.

## Outline and titles first

Write the outline first: the slide titles alone should tell the story, like a table of contents. Write
the whole title sequence before any slide, in ONE grammatical style:

- short topic titles in title case ("Market Research", "Engagement Overview", "Team Structure"), or
- action titles, short phrases ("Asia is our largest market…", "…but Eastern Europe has the most room
  to grow").

Read just the titles: someone should follow the flow from them alone. Share the outline as a list of
titles before you start the slides (or while you make them); do not wait for approval unless the
request was unclear.

Avoid titles that sound machine-written: titles that deliver a verdict, that are overly dramatic, that
build fake tension ("It's not X. It's Y."), heavy reframing, faux insight ("The magic moment"). A title
INTRODUCES the slide; it is not the speaker's punchline.

## Less text, more structure

Avoid putting too much text on slides. Decide which parts are tables, diagrams, quotes, pictures, card
rows or big numbers. Mix the look: full-picture slides, different backgrounds, big numbers, quotes,
tables, some text. Avoid a short block of text hanging under the heading with nothing below: spread the
body down the slide (Compose, below); do not center the column.

Parallel design: section headers look alike; repeated elements sit in the same place, the heading at
the same height on every content slide; slides of one kind share their markup (padding, gap, sizes).

## Label diagrams in the deck's type, not inside them

The artwork is the picture or the `<svg>`; the labels are real text over it (`layout.md`, Labels over a
picture).

## Commit to the system up front

Say the system you will use: a layout for each kind of slide (title, section header, content, picture),
and variety and rhythm on purpose. On text-heavy slides, commit to the person's pictures or to
structure (a table, a card row, a big number).

No web density (14–16px body text). The smallest text is 24px. Nothing enforces it, but if the text only
fits at 20px, there is too much text.

## Speaker notes (`<aside>`)

Add speaker notes only when asked. Then the deck becomes visual-first and the notes carry the script:
write them as what the presenter will actually say, in full, conversationally, not as bullets. One
`<aside>` per slide, always the section's last child.

Because the notes carry the story, take text off the slides: large figures, quotes, full-bleed
pictures, diagrams, one-line headlines. No paragraphs on slides. A text-heavy slide means the script is
on the slide; move it to the notes.

## Compose like a slide designer, not a web designer

There is no review pass after `open-artifact check`, so decide each slide's composition as you write it.

A statement or title slide with open space below is correct. A CONTENT slide whose column stops at 60%
of the height reads as unfinished. Spread the column on purpose:

- Fill the height: `justify-content:space-between`, or a `flex:1` spacer before the last row. The
  heading stays at the top margin, at the same height as on the deck's other content slides, so it does
  not hop as the viewer flips through.
- Center the content only on a slide with no heading above its body (a statement, a quote):
  `justify-content:center`. Never center a column with a heading: the column's height then sets where the
  heading lands, differently on every slide.

Plan the `gap`s so the blocks span the 824px.

## Content rules every artifact type shares

These are about the content you write (the slides, their text, the notes), not the page around it.

- **No filler.** Never pad a deck with placeholder sections, dummy text or information just to fill
  space. Every element earns its place; an empty-feeling slide is a layout problem, solved with
  composition, not invented content. Avoid data slop: numbers, icons or stats that are not useful.
  Less is more.
- **Ask before adding material.** If more slides, sections or copy would help, ask first: the person
  knows their audience and goals better than you do.
- **Targeted changes stay targeted.** A small request (some text, a color, one element) changes ONLY
  that: every other layout, spacing, font, size, position, color and word stays exactly as it is. A
  redesign or a new direction is different. If a broader change would help, finish what was asked and
  SUGGEST the rest.
- **Follow an existing deck's visual vocabulary.** Adding to a deck: match its copywriting, palette,
  tone, card and layout patterns, density and motion.
- **Avoid generated-look tropes**: gratuitous gradient backgrounds, emoji (unless the brand or design
  system uses them), rounded containers with a colored left-border accent.
- **Recreate from source, not memory.** Asked to recreate a design whose source you can reach (files, a
  design system), read the source and copy its exact values and assets rather than rounding them or
  working from memory or screenshots.
- **Do not recreate copyrighted designs.** Do not reproduce another company's distinctive branded
  look or proprietary visual elements unless the person says they work there; help them make an
  original design instead.
