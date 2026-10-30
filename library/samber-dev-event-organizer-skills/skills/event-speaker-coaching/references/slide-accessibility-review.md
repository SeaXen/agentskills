# Slide accessibility review

Load at workflow step 9. Run on every deck, not only the decks you worry about. Sources: W3C WAI "How to Make Your Presentations Accessible to All", WCAG 2.2, WebAIM, the SIGACCESS accessible conference guide.

## Blocking

A failing item here is a Blocking note. Fix before the slide deadline.

- **Text contrast** at least 4.5:1, or 3:1 for large text (18pt, or 14pt bold) - WCAG 2.2 SC 1.4.3. Check with a contrast tool on the actual colour values; a description ("dark grey on black") is enough to suspect a failure, not to confirm one, so ask for the file. Dark themes are fine when the ratio passes. Never round up (4.49:1 fails). Projectors wash out colour, so treat the ratio as a floor.
- **No flashing** more than three times in any one second - WCAG 2.2 SC 2.3.1. Check animated GIFs, video clips and terminal recordings.
- **No meaning carried by colour alone** - WCAG 2.2 SC 1.4.1: a red/green diff, a status chart, a heat map gets a label, a symbol or a pattern too.

## Change

- **Readable from the back row**, code included: show the deck on the real projector from the last row, or on a laptop from proportionally as far away. No authoritative minimum font size exists; this test replaces one, which is why it is a Change and not a Blocking item.
- Every slide has a title, so a shared PDF is navigable by screen reader.
- Images that carry information have alt text in the shared deck.
- Video clips carry captions.
- Acronyms and jargon defined on first use, on the slide or aloud.
- Code slides show only the lines discussed, highlighted.
- Links come as short readable URLs, not only a QR code.

Sending slides to captioners and interpreters on time is a calendar deadline, not a deck property; it sits in the coaching calendar.

## Room-specific checks (Interview Q8)

- **Multilingual or second-language audience**: key terms written on the slide, fewer idioms and jokes that depend on wordplay, a steadier pace for interpreters and captioners, a glossary sent to interpreters with the slides.
- **Mixed room**: every term defined on first use; one concrete example before the abstraction; open where nearly everyone follows and end on material most of the room cannot, so the depth climbs instead of starting high.
- **Remote or hybrid**: code and text legible on a shared screen at laptop size; nothing pointed at physically that the camera cannot see; questions from the chat repeated aloud.

## Delivery, rehearsed in the dry run

- Say what each slide shows, including charts and the result of a demo step. A slide only seen is lost to part of the room and to the recording.
- Use the microphone even when the room seems small.
- Repeat every audience question into the mic before answering.
- Leave a few seconds after asking for questions; some people need longer to form one.
- Inclusive language: no "you guys", no ableist metaphors, no jokes at a group's expense.

## Who checks

A volunteer with this list and a contrast tool can review a deck in about ten minutes. The event-wide provisions (captioning, interpreters, hearing loops) are decided in `samber/dev-event-organizer-skills@event-accessibility-inclusion`; this review only checks the speaker's deck against them.
