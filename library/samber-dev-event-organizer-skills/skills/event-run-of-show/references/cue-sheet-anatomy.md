# Cue sheet anatomy

What a run-of-show row actually carries, the sourced transition mechanics behind it, the two segments that carry the most weight, and a positive/negative pair.

## What each row carries

A cue sheet is not the published schedule with more rows. The grid answers _what happens when_; a cue sheet answers _who does what, and what gets said, at the moment one thing becomes another_. Give every segment and every transition its own row, with:

- **Clock** - the start time, and for a transition, the window rather than an instant.
- **Room or stage** - always, even at a single-room event, because the sheet outlives the assumption.
- **Owner, by name** - the person accountable for that row happening. "A volunteer" is not an owner; a named person who can be found in a corridor is.
- **Tech owner** - who is at the machine, which machine, and where the material for this row already lives.
- **What is said** - at the depth the skill's cue-sheet menu picked: a prompt, a scripted line, or nothing where nothing is spoken.
- **What physically moves** - the next presenter walking to the queue, a table coming out, a mic changing hands.
- **Escalation** - who this row's owner calls when it fails, which for most rows is the organizer on duty for that block.

The last column is what separates a cue sheet from a checklist: every row already knows what happens when it does not happen.

**Write the participant-facing and staff-facing rows as two interleaved tracks rather than one column**, and let the staff track run ahead of the participant one: a room-reset row starts while the current segment is still running, not after it ends, so the swap is invisible to the audience instead of a visible gap. Give room reconfiguration its own named, timed row - "reset the lobby into conference mode, 15 minutes, owner: Priya" - rather than leaving it to be assumed.

This row shape matches published stage-management and broadcast conventions rather than inventing a new one: professional cue sheets (also called rundowns, show-flow docs, or run sheets) are built the same way, with named departmental cue columns and a named owner per row, whether for a theatre production, a broadcast, or a corporate/conference event - the document scales across event types, only the row-level detail changes.

## The sourced transition mechanics

Source: DevOpsDays organizing guide, "Running Ignites" section (`devopsdays/devopsdays-web`, `content/page/organizing.md`). The source describes one rapid-fire talk format; the three mechanics generalize to any tight handover - lightning talks, sponsor slots, a demo queue - while the format's own timings do not and belong to the format, not here.

- **Physical queue position.** Presenters queue _next to the stage_, not in the audience. The organizer either starts the deck for them or lets it advance from a bio-slide interlude, so no part of the transition is spent watching somebody find their way to the front.
- **One machine, one operator.** All decks run from a single dedicated laptop, never the presenters' own - specifically to keep popups, sign-in prompts and format surprises out of the transition window. Material is collected in advance (the source uses PDFs in a shared folder), so the handover is a file switch rather than a laptop swap.
- **The spoken reminder, on the day.** Even after presenters were briefed in advance, the guide instructs giving the constraint verbally at the point of use: in its own example, that the slides advance automatically every fifteen seconds and cannot be advanced by hand, and that there are no presenter notes. The guide is explicit that this is worth repeating on the day rather than assuming the earlier briefing stuck.

Take the three mechanics. Do not carry the fifteen-second figure or the slide count anywhere - those describe that one format.

## The opening segment

Source: MLH hackathon organizer guide, opening-ceremony page (`MLH/mlh-hackathon-organizer-guide`). The guide frames the opening as tone-setting - celebrated like a festival start, creating energy meant to last the whole event - and names what must be covered:

- What the event is, framed for people attending for the first time.
- Who the organizing team is and how to reach them.
- Practical details: wifi, the communication platform, venue logistics.
- The schedule, with major deadlines called out.
- Sponsor content, explicitly coached to be kept short.
- The rules, and for a competitive format, prize categories.
- A named partner presentation slot - five to eight minutes in the source's own format.

Adapt the last item to whatever your event's equivalent opening slot is (a welcome keynote, a sponsor welcome, an organizer intro). The rest transfers directly, as a published opening-content checklist.

## The closing segment

Same guide, closing-ceremony page:

- **Pre-announce the closing.** An announcement that the closing is about to start, rather than a silent transition into it.
- **Slides over live narration** when announcing results, and collect whatever is being announced from partners _in advance_ rather than live.
- **Energy discipline, stated explicitly**, on the grounds that people tend to remember the beginning and the end of an event for years.
- **The guide's own recommendation is to avoid live demos at the closing entirely** when judging is still concluding, preferring that people browse submitted recordings instead. Live demos are named as the expensive, failure-prone option - not the default.

### The live-demo timing breakdown

The guide's worked example of budgeting a live, in-the-moment segment (same page):

| Component                       | Minutes |
| ------------------------------- | ------- |
| Demo                            | 3       |
| Questions                       | 1-2     |
| Setup and swap to the next team | 5-6     |
| **Total per team**              | **10**  |

Setup and swap consume more than half the slot, which is the guide's own point in giving the breakdown. Timing figures elsewhere cover _session_ lengths and buffers; this one costs the execution risk inside a slot.

Present it as that event's number for that format. It is not a general conference constant, and attaching it to an unrelated segment invents a benchmark.

### Teardown as a timed group activity

Self-set mechanic worth naming: run the venue handback as a short, timed group activity rather than a silent departure. One worked shape - organizers walk every room announcing a fixed countdown ("three minutes to pack up"), paired with a pre-ceremony instruction that every room must be cleared and cleaned before the closing segment starts, since nobody returns to it afterward. The timer is what turns "please tidy up" into something a tired room actually does before leaving.

## Filling a scheduled dead-time gap

Self-set mechanic: any block where the room is captive and waiting on something happening out of sight - a jury behind closed doors, a result being tallied - is the hardest slot on the sheet to leave unscripted, and it deserves its own row rather than a silent gap. One worked shape: recruit a handful of people already in the room as facilitators by a show of hands, have them rotate through small seated groups every few minutes with a short set of escalating questions, and open by naming and dismissing the awkwardness directly rather than pretending it isn't there - state plainly what will not happen (no forced participation) and name the legitimate ways to opt out (stay seated, step out, sit with someone you already know). The same captive window is also the cheapest place to collect a feedback survey, on screen as one of the offered options, rather than by email after everyone has gone home.

## A positive and a negative row

**Negative - a row lifted from the published schedule:**

> 16:00-16:30 - Lightning talks (Main hall)

Nothing here can be executed. No owner, no tech owner, nobody knows where the next speaker stands, nothing is said, and when the second speaker's laptop will not mirror there is no named person to call. This row is the reason the cue-sheet menu deletes the attendee-facing schedule as a staff document rather than demoting it.

**Positive - the same block as cue-sheet rows:**

> **15:56-16:00 · Main hall · Transition into lightning block**
> Owner: Priya (room lead). Tech: Sam, on the house laptop; all six decks already in `/lightning` as PDF.
> Priya walks all six speakers to the queue chairs stage-left before 15:56 and confirms the order out loud with them.
> Said: "Six lightning talks, five minutes each, hard stop - I'll stand up at four minutes. Your slides are already loaded; Sam advances, not you."
> Escalates to: Marco (on duty, 14:00-18:00) if a speaker is missing at 15:58 - run the block short one, do not delay the block.

> **16:00-16:30 · Main hall · Lightning talks 1-6**
> Owner: Priya. Tech: Sam. Handover between speakers is a file switch, not a laptop swap.
> Priya introduces each speaker by name and topic only; the MC does not do these.
> Escalates to: Marco if the block runs past 16:34 - the disruption order protects the closing plenary, so cut the sixth talk rather than the break.

The difference is not length. It is that every failure the block can produce already has a name attached to it, and the decision that failure forces was made before the day rather than in front of an audience.
