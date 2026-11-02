# GreenStack Conf, 3-day format brief

## Answer up front

- **There is no 30% industry standard.** I found no published workshop percentage, and the events I can cite don't share one. Collapsing them into a single figure would invent a norm. Treat the number you read as unsourced.
  - SmashingConf runs 4 days: 2 workshop days with 8 workshops, and 2 single-track conference days with 12 speakers. That is 50% of days.
  - PyCon US sells separate 3-hour tutorials on dedicated days before three days of talks.
  - GOTO separates its masterclass day from the conference days.
  - DevOpsDays is roughly half curated and half self-organized, plus an optional pre-event workshop day.
- **Don't pick a percentage. Pick a structure.** Make workshops a separately ticketed day rather than a share of the talk program. For 3 days, that means 1 workshop day plus 2 curated talk days. By day count that is about 33% hands-on, but it is a consequence of the structure, not a target.
- **Don't run workshops in parallel with the talks.** Parallel workshops turn the event into a multi-track conference. Two conditions have to hold first, and I don't know that either does (details below).

**Assumption:** GreenStack is a community conference, meaning an open CFP and no sold stage slots. If it is vendor-run, tell me, because several defaults change.

## Why not parallel workshops

1. **It is a track-count decision.**
   - The published promotion condition for multi-track is a CFP oversubscribed about 8-10x relative to slots. For scale, swyx puts the norm at 8-12 speakers per day per track.
   - You haven't given me your applicant-to-slot ratio. Without it, parallel sessions risk empty rooms and a fragmented event.
2. **Workshops lose the marginal program hour.**
   - They rank second on value and second on effort, so they never win a slot inside the talk program.
   - They start to pay off once they move out of the program into a bracketing day, where the separate ticket also becomes a revenue lever.
3. **Attendee agency is real, but so is the cost.**
   - Five independent organizers chose single track on purpose: Strange Loop, GOTO, Monktoberfest, Deconstruct and SmashingConf. Their reasons are shared context, curation as editorial responsibility, the hallway track, and speakers who stay.
   - Parallel sessions would give those up. Multi-track is a scale decision, not a quality upgrade.
4. **The workshop day gives you the same choice without the cost.** Attendees pick talks only, workshops only, or both, because the tickets are separate. GOTO frames it this way: if you know your problem, take the masterclass; if you're scanning the landscape, take the conference.

## Three candidate structures

| | A. Bracketing (recommended) | B. Bracketing + open-space afternoon | C. Parallel workshops and talks |
|---|---|---|---|
| Days | Day 1 workshops (ticketed). Days 2-3 single-track curated talks. | Same, but each talk day ends with open space. | 3 days, workshops alongside 2+ tracks |
| Curation effort | Moderate | Moderate, plus open-space facilitation | Highest (a second curated stream and a balance policy) |
| Shared experience | Preserved | Preserved | Lost |
| Revenue lever | Workshop day sells separately | Same | Workshops bundled into one ticket |
| Fits when | Default | You want attendee agency without a second track | CFP oversubscribed 8-10x and workshops must run alongside talks |

**Recommendation: A.** Add B's open-space afternoon if attendees want more agency. It is the DevOpsDays architecture, and it steers tool-specific content out of the curated track.

### Day architecture for A

- **Day 1: workshop day.**
  - Optional and separately ticketed.
  - Workshop capacity, facilitator coverage and environment setup go to `workshop-program-design`.
- **Days 2-3: single-track talk days.**
  - The backbone is curated talks of about 25-30 minutes.
  - Add an Ignite block if you want more first-time speakers.
  - Use a fireside chat instead of a keynote for a high-profile guest who isn't a polished presenter.
  - Run no panels unless you have a prepared moderator who is willing to interrupt.
  - Keep long breaks, good food and quiet rooms, because the hallway track is a format choice.
- **Sponsors:** no program slots. Sponsor inventory is expo, side events and 1-minute inter-talk slots.

Strange Loop argues that "2-3 days is the sweet spot", which supports the expansion itself. Its own caveat is that the jump should rest on content depth and travel justification, not attendance alone. Selling out at 450 twice is strong demand evidence, but it doesn't answer whether you have enough quality content for 2 curated talk days.

## Triggers that would revise each choice

- **Go multi-track or parallel:** CFP applicants reach roughly 8-10x slots. Add plenary moments (opening, shared lunch, closing) if you do.
- **Shrink or drop the workshop day:** it sells under a threshold you fix in advance (for example 60% of capacity). The bracketing model makes this reversible.
- **Add the open-space afternoon:** attendees ask for more agency, or tool-specific talks start crowding the curated track.
- **Hybrid or livestream:** remote registrations stay above about 25-30% of paid attendance and cover their marginal cost. Until then, record and post after the event. Free livestreams draw well under 10% of sign-ups, a benchmark from academic conferences.

## Open questions

1. What was your CFP applicant-to-slot ratio last edition?
2. Is there a pool of workshop instructors, and do you have rooms for separate sessions?
3. What is the organizer headcount and budget for a 3-day run? Venue deposits are the main risk.
4. Do you want me to hand the approved structure to `event-schedule-design` for the grid, and to `event-positioning` if the single-track identity matters to your brand?

This is a strategy choice. Please confirm the structure (A, B or C) before I finalize it.