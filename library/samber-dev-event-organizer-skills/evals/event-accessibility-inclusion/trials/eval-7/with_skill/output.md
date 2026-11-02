# LoopState Conf: accessibility sign-off review

## Verdict

**Don't close the ticket, and don't ship "fully accessible" in the hero.** The 100/100 is real but covers only part of the site. The skill's own warning applies: "A perfect automated score is not conformance," and "a conformant website is not an accessible conference."

## Why the score doesn't support the claim

- **Scope of the score.** A scanner covers part of the digital layer, and the skill says it catches only a minority of WCAG failures. It says nothing about the venue, captioning, quiet space, food or cost of attending.
- **The claim reaches past the website.** "Fully accessible conference" is a promise about the event. Per the skill's wording rule, it is "a different promise" from a scoped statement. A deaf attendee, a wheelchair user or a parent will book travel on that sentence.
- **Absolute claims are the failure mode.** The skill's examples are "The conference is captioned" and "Accommodations available on request." The right form states scope inside the sentence.

## 1. The color-coded schedule grid (digital layer, check 4)

The skill calls the schedule "usually the worst page on a conference site." Scanners are weakest on exactly this. Check each item below.

| Check | Pass criterion | Why the scanner misses it |
|---|---|---|
| Track identified by color alone | Each session also shows the track name or an icon or pattern, in text | The scanner can't know a color carries meaning |
| Text contrast on colored cells | 4.5:1 for normal text, 3:1 for large text and UI components | Gradients, images and hover or active states are often skipped |
| Legend | Legend is text-labelled, not just swatches | Not detectable |
| Zoom and reflow | Usable at 200% zoom and on a narrow viewport, with no clipped or overlapping cells | Scanners test a fixed viewport |
| Keyboard | Reach and open every session, filter and tab by keyboard, with visible focus | A scanner can't judge usability |
| Screen reader | Grid is real table or list markup, with correct roles, names and reading order | A passing check on a custom widget often hides a missing name or role |
| Status | "Full", "moved" and "cancelled" are not shown by color only | Not detectable |

Pass test: view the grid in grayscale. If you can still tell tracks apart and read every cell, it passes.

## 2. Speaker slides posted as PDFs (check 7)

This is a gap the score almost certainly doesn't cover, for two reasons.

- **Slides are uploaded after the event, and the scanner scored the site before that.** Nothing currently posted has been audited, and nothing posted later will be.
- **A PDF deck is its own document-accessibility problem.** The skill names tagged structure, reading order and real text rather than images of text.

What to do:

1. **Decide the rule now.** Options are an accessible format required from speakers, or a web page or text version published alongside. The skill's fallback applies: "If you cannot make the PDF work, publish the same content as a web page and treat the PDF as a convenience copy."
2. **Put the requirement in the speaker brief**, handled through `event-speaker-experience`.
3. **Name an owner** for checking uploads, with a turnaround.
4. **Spot-check the first batch** before the pattern repeats. Check for real text, a heading structure, alt text on figures, and a sensible reading order.
5. **Don't publish an image-only deck** without a text alternative.

## 3. The rest of the digital layer the score doesn't settle

Check these in the skill's order of importance.

1. **Registration and ticket flow, by keyboard only.** Include the date picker, the dropdowns and the payment step. This is the highest-stakes path, because nobody who can't complete it attends.
2. **Accommodation-request field.** It needs a text label (not a placeholder), help text associated programmatically, and errors in words.
3. **CFP form.** The same rules apply.
4. **The accessibility page itself.** It "fails more often than people expect," and a failure there undercuts the claim.
5. **Livestream player.** Check keyboard controls and a caption track that can be turned on. Recordings need captions afterwards, whether or not the room had live captioning. If live captioning exists, publish the transcript, which is cheap and often skipped.
6. **Audit method.** Follow the skill's workflow: tool, then localize failures, then inspect the accessibility tree, then keyboard pass, then re-audit. Ask the agency which of these steps they did beyond the scanner.

Target: WCAG 2.2 AA on these surfaces. Whether it is a legal duty for you is a question for counsel.

## 4. Beyond the website: what the ticket must also cover

The hero claim is about the event, and the site score can't back it. Ask for evidence on each of these, or scope the claim without them.

- **Venue.** Step-free route, lifts, accessible and all-gender restrooms. Do you know the venue's real access facts? Is the venue signed? If so, some options are already fixed.
- **Captioning and interpretation.** Which rooms and days are covered? A capable A/V team is not a provision until someone "states, budgets and publishes it."
- **Spaces.** Quiet space, nursing room, reserved seating. Quiet-space sizing has no sourced standard, so state that yours is self-set.
- **Food.** Which dietary categories are covered, and what happens when a supplier can't cover one.
- **Cost of attending.** Need-gated ticket route, childcare or travel grants, each with its own limits.
- **Request channel.** A named owner, a lead time, and a retention rule stated on the form. If the channel collects disability data, decide where it lives and who reads it. If it has no owner, requests go unanswered.
- **A named person who owns accessibility through to the debrief.** Is there one?

## 5. Replacement for the hero line

Don't use an absolute claim. Use a scoped one that links to a page covering everything above. A template, with placeholders you can only fill from facts you hold:

> **Accessibility at LoopState.** [Provision, e.g. "Live captioning is provided in every session room on the main days. Tutorial days are not captioned."] [Venue fact, e.g. "The venue has step-free access to all session rooms. The upper gallery is not step-free."] To request anything else, write to [named owner] by [date]. We reply within [N] days.

For the website itself, the safe claim is narrower: "Our website meets WCAG 2.2 AA" holds only after the keyboard and screen-reader passes confirm it. State the result on the accessibility page, not in the hero.

## 6. Before closing the ticket

1. Run the schedule-grid checks (section 1) and the keyboard pass on registration, CFP and the request field.
2. Decide the slide-PDF rule, owner and speaker-brief wording (section 2).
3. Publish a single accessibility page with provision-by-provision scope and the request channel, with the owner and retention rule named.
4. Replace the hero line with the scoped version (section 5).
5. Re-title the ticket: "Website audit passed. Event accessibility open until the page, the request owner and the slide process are in place."
6. Record the provision set and requests in the debrief, and delete the request data on the schedule you published.

## Gaps I can't fill

- I haven't seen the site, the agency report or the venue contract. I'm working only from what you told me, so the checks above are for the agency or your web owner to run.
- I did not run the interview. These answers would change the provision recommendations: who funds accessibility, whether the venue is signed, what needs are already known, which jurisdiction, and how much staff time exists.
- Jurisdictional duties (premises, auxiliary aids, disability data) need counsel. This is not legal advice.