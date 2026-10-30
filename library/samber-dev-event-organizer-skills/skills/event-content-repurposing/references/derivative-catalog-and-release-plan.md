# Derivative catalog and release plan

What each derivative is made from, what it actually costs, a worked release plan against its negative counterpart, and the two handovers this skill owes downstream.

Contents: 1. The catalog - 2. A worked release plan - 3. The same plan done badly - 4. Handover to the channel - 5. Inventory handed up to the campaign.

## 1. The catalog

This table is this skill's own construction, not a measured benchmark. Effort is given as an order of magnitude, never as a figure. Everything in the "made from" column is an input somebody else produced.

| Derivative                   | Made from                                                | Effort                                            | What it buys                                                                                | What kills it                                                        |
| ---------------------------- | -------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Written write-up             | The programme, notes, slides, a transcript if one exists | An hour or two, once, most of it review           | The link that answers "what is this event" for a stranger, reusable across editions         | Written as a schedule recap rather than about what was said          |
| Short clips                  | The published master                                     | An hour per clip, dominated by finding the moment | Travel through other people's feeds - the only derivative that reaches strangers on its own | Cutting by running order instead of by what people asked about       |
| Social thread                | The photo archive and quotes already collected           | Near-zero                                         | A same-week reminder to an audience the event already has                                   | Treated as reach; it is mostly reminder                              |
| Transcript-derived text page | The master's audio, plus a human correction pass         | A standing job across a programme                 | Search finds it long after a feed has moved on; the only derivative that translates         | An uncorrected machine transcript published as if it were a document |
| Audio cut                    | The master's audio                                       | An hour per talk                                  | Nothing on its own - it needs a property that already has subscribers                       | Made because it is easy, published where nobody subscribes           |

Two notes on the short-clips row:

- Automatic clip tools can cut the "finding the moment" hour. Keep a human review before each publish, and run Menu 4's rights gate on the generated clip as on any other.
- The same organizers also clip key conference moments and behind-the-scenes footage of the organizing work. Both sources are made from the photo and video archive rather than the master, and both usually show identifiable attendees.

Two notes on the transcript row:

- Post-event subtitling of conference talks runs as a standing, tooled, crowdsourced volunteer project with its own repositories, separate from the live production pipeline (c3subtitles) - that is the honest measure of what a correct text pass costs at programme scale.
- A text derivative published after the event never substitutes for a live access provision in the room; that provision is decided elsewhere in the collection and this file does not touch it.

## 2. A worked release plan

Illustrative: the shape is this skill's own, and the dates come from the interview's deadline answer and the owner's real availability.

Named developer conferences differ sharply on how fast the master itself reaches publication. Treat any one of them as a data point rather than a convention to match:

- FOSDEM's automated review pipeline gets most talks public within hours to a few days of the room going quiet.
- NDC Conferences states its own turnaround as about a month.
- PyCon US's full catalog has historically taken closer to a quarter.

Each reflects a different owner and a different tooling investment behind it. That is exactly Q6's question, not an industry default to inherit.

- **Before anything is cut:**
  - Every session marked usable, restricted or off-limits against the consent record.
  - Sessions Q7 named written down.
  - Licence decided.
  - Owner named with an end date.
- **Wave one, the week the master is public.** The written write-up, published with its licence line, linking to the masters rather than re-hosting them. It is first because it exists without editing and it is the artifact everything later points at.
- **Wave two, once editing has actually happened.** Clips for the sessions people asked about, each cleared through the rights gate before it was cut rather than after. Each handed to the channel sibling with its date, not posted here.
- **Standing, only if an owner exists.** One further piece per fixed interval until the stated end date. If nobody owns this, it is not in the plan; a dump with a date is the honest floor.
- **Opportunistic, no schedule.** Re-surfacing an existing artifact when its subject becomes newly relevant. Nothing is produced for this; it re-uses what waves one and two already made.

Each line carries three things or it is not in the plan:

- What the artifact is.
- The date.
- The person.

## 3. The same plan done badly

- "We will publish the videos and then do some clips." No dates, no owner, no marked-up consent list. This is the failure `samber/dev-event-organizer-skills@event-production` names: the crew disperses and the artifacts never appear.
- Clips cut first, rights checked at upload time. The check fails on a slide nobody looked at, and the editing is already spent.
- A drip scheduled across many weeks by a team that has just finished an edition, with the owner named as "the organizers".
- A write-up that lists the schedule again. The programme page already did that; nobody reads it twice.
- An audio cut published because the audio was already separated, to a destination with no subscribers.
- A licence decided per artifact at publication time by whoever uploaded it, producing an archive with three different terms and no record of who chose which.

## 4. Handover to the channel

The publishing channel is owned by `samber/dev-event-organizer-skills@event-social-media`. Hand over one row per scheduled piece and stop. The five fields are this skill's own list, not a format that sibling specifies:

- The artifact and where the file is.
- The date it should go out.
- The licence line that must appear with it.
- Any restriction the rights gate produced - a speaker not to be tagged, a photo not to be used, a frame already cut.
- The speaker ask, if one was agreed, and whether the asset was already sent.

Do not write the caption, choose the platform, or set the hashtag. Those are that skill's, and a second version of them competes with the first.

## 5. Inventory handed up to the campaign

The marketing plan schedules content it knows exists. Hand it a list, not a folder. These four fields are this skill's own list, not a format that sibling specifies:

- Artifact type, count, and the date each becomes available.
- Which are evergreen (usable months later) and which are dated (only meaningful near the edition).
- Which carry an open licence and which do not, since that decides whether a partner may re-use them.
- What is missing and will not exist, so the calendar is not built on a hoped-for piece.

An edition that produced nothing repurposable has nothing to promote the next one with, and that absence belongs in the list too.
