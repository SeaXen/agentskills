# Digital layer: the event's own website, forms, schedule and stream

**Scope warning, and it is the whole point of this file.** Everything here transfers to the event's _digital_ surface only: the website, the registration and CFP forms, the published schedule, the livestream player, and program materials published as web pages or documents. None of it says anything about physical, sensory, dietary or economic provision on site.

Web accessibility and event accessibility are separate disciplines, and a conformant website is not an accessible conference. Never present a passing audit as accessibility coverage.

Web-accessibility skills already published in this field converge on WCAG 2.2 with level AA as the target, and it is recommended as a legal requirement in many jurisdictions. That is why AA is the target here rather than a number invented for this skill. Whether it is a duty for your event in your jurisdiction is a question for counsel.

## The four categories (POUR)

Structure any check this way, so nothing whole is missed:

- **Perceivable** - text alternatives for images, captions and transcripts for media, sufficient colour contrast, content that survives being resized.
- **Operable** - everything reachable and usable by keyboard alone, no keyboard traps, enough time to complete a form, visible focus.
- **Understandable** - predictable navigation, labelled inputs, errors identified in text rather than by colour alone, and clear instructions.
- **Robust** - valid markup and correct roles and names, so assistive technology can interpret the page.

## What to check, in the order that matters for an event

1. **The registration and ticket flow.** The highest-stakes path on the whole site: a person who cannot complete it does not attend, and no on-site provision can rescue that. Exercise it end to end with the keyboard only, including any date picker, any dropdown, and the payment step.
2. **The accommodation-request field.** Labelled in text, with its help text programmatically associated, and its errors described in words. A field that is only labelled by a placeholder disappears the moment someone starts typing.
3. **The CFP form.** Same rules. A speaker who cannot submit is a speaker you never hear from, and this is upstream of every diversity-of-lineup effort the CFP sibling runs.
4. **The schedule.** Usually the worst page on a conference site: a dense grid, colour-coded by track, at small text sizes. Check contrast (4.5:1 for normal text, 3:1 for large text and interface components at AA), check it is not conveying track or status by colour alone, and check it is usable at 200% zoom and on a narrow viewport.
5. **The accessibility page itself.** It fails more often than people expect, and failing on that page specifically undercuts the claim it is making.
6. **The livestream player.** Keyboard-operable controls, a caption track that can be turned on, and captions on the published recordings afterwards - required independently of whether live captioning was provided in the room. If the programme was captioned live, the transcript usually already exists; publishing it is cheap and frequently skipped.
7. **Published program documents.** A PDF schedule or a slide deck is a document accessibility problem of its own - tagged structure, reading order, real text rather than an image of text. If you cannot make the PDF work, publish the same content as a web page and treat the PDF as a convenience copy.

## Audit workflow

1. Run an automated audit tool against the key pages if your environment can.
2. Localize each failure to the element that caused it.
3. Inspect the accessibility tree for the components the tool flagged, since a passing automated check on a custom widget frequently hides a missing name or role.
4. Exercise each flow by keyboard alone, start to finish.
5. Fix, then re-audit.

**A perfect automated score is not conformance.** Automated tools catch a minority of WCAG failures.

They miss most of what matters in a registration flow: a form that is technically labelled but incomprehensible, a modal that traps focus, an error message that only appears in colour. The keyboard pass in step 4 is the one that finds those.

## Who does this

This is web work, not event-organizer work. Decide the target (AA), decide which surfaces are in scope, and hand the checklist to whoever maintains the site. Your job is that the target exists, that the registration and request flows are in scope, and that the result is stated on the accessibility page rather than assumed.
