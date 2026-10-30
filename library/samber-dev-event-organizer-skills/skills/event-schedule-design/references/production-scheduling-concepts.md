# Manufacturing production-scheduling concepts

**Every concept in this file is borrowed from manufacturing production scheduling, not from events practice.** Its home domain is discrete and batch manufacturing - production lines, changeovers, shift crunch.

Use these as structuring analogies. Say where they come from wherever they reach a user, and never present one to a program committee, a sponsor or a speaker as established event practice.

## Contents

- Why a manufacturing source at all
- Graded buffer zones
- Disruption re-sequencing and the stability lock
- Changeover sequencing
- Levelled pacing
- Competing demand for a scarce slot
- What does not carry over
- Numbers that must not be reused

## Why a manufacturing source at all

Job-shop scheduling and session scheduling are the same shape of problem: discrete work units competing for scarce resources under time and dependency constraints, where a disruption to one unit propagates through the sequence. Talks are jobs, rooms are machines, the day is the shift. The shape transfers; the domain knowledge does not.

That similarity is exactly what makes the borrowing dangerous if left unlabelled - the analogies read as plausible event advice, and a reader who does not know their origin will repeat them as established practice.

## Graded buffer zones

**Source concept.** A time buffer protects the constraint operation. Buffer _penetration_ is tracked in three zones rather than as a binary state:

- Green: little of the buffer is consumed.
- Yellow: consumption triggers expediting.
- Red: consumption triggers management attention.

**Borrowed.** Size an inter-session buffer as a share of the preceding session's length rather than a flat number, and read its consumption as graded - comfortable, tightening, blown - rather than as on-time or late. The value of the grading is that it makes a room's drift visible while there is still time to act on it, instead of only after a session starts late.

**What does not carry.** The zone boundaries and the buffer-sizing percentage. Both are calibrated to a manufacturing line's variability, and there is no reason a conference room's overrun distribution matches it. Derive your own from recorded overruns, and say the thresholds are yours.

## Disruption re-sequencing and the stability lock

**Source concept.** On a disruption, the priority order is:

1. Protect the constraint's uptime.
2. Protect committed customer dates by tier.
3. Minimize the total changeover cost of the new sequence.
4. Level the remaining load.

Two mechanisms sit on top: a published re-sequencing communication timeline, and a **stability lock** - no further changes for a defined period - to stop chronic re-shuffling.

**Borrowed.** For a speaker no-show, a room AV failure or a talk that overruns badly:

1. Protect the plenary or keynote slot above everything else - it is the only moment the whole audience shares, and a drift there propagates to every track.
2. Protect the headline commitment the audience showed up for.
3. Minimize how many other sessions the fix disturbs; a repair that moves five sessions to save one is usually the wrong repair.
4. Lock the revised grid for the remainder of the block rather than continuing to re-shuffle as the day goes on.

The stability lock is the most useful borrowed idea here, because the natural instinct under pressure is the opposite: keep optimizing, and hand the audience a schedule that has changed three times by mid-afternoon.

**Boundary.** This priority order is a _design_ artifact - write it into the grid document in advance. Running it live on the day belongs to `samber/dev-event-organizer-skills@event-run-of-show`, not here.

**What does not carry.** The source's "communicate within 30 minutes" and "no further changes for at least 4 hours" figures. Both are shift-length artifacts of a factory. A conference block is not four hours by default and a schedule change reaches attendees through completely different channels.

## Changeover sequencing

**Source concept.** A changeover-time matrix records the setup cost between every pair of products, and the sequence is optimized to minimize total changeover cost. A heuristic ordering (light-to-dark, small-to-large) reduces cleaning between runs.

**Borrowed.** Room turnover (AV reset, seating reconfiguration, tables back to theatre rows, chairs on and off) is a real cost that depends on _which pair_ of sessions sit back to back in a room, not on either session alone. Two consequences:

- Buffer sized per room-pair is more accurate than one flat number, at the cost of per-pair bookkeeping (the starved rung in SKILL.md's buffer menu).
- Sequencing same-format sessions together within a room reduces how much has to change between them. This is the cheap companion to the expensive rung, and it costs one ordering decision.

**What does not carry.** The optimization machinery (nearest-neighbour construction, 2-opt improvement). A conference has a handful of rooms and a dozen or so sessions each; the matrix is small enough to read, and formalizing it buys nothing.

## Levelled pacing

**Source concept.** Levelled (heijunka) sequencing warns against front-loading the easy work and dumping the hard jobs at the end of the shift - the end-of-shift crunch.

**Borrowed.** Avoid clustering all the high-intensity sessions together, and specifically avoid putting the densest, hardest content in the last slot of the day. This is no longer the only thing this skill has to say about energy-curve pacing and graveyard slots - named organizer guides and peer-reviewed sources now cover both directly (`references/published-schedule-benchmarks.md` § Energy-curve pacing and graveyard slots: named sources). Those sources confirm this analogy's direction - the last slot of the last day is empirically the worst one at the conferences studied - but supply no mechanism; this analogy is what supplies one, which is what it still adds.

**What the sourced material adds that this analogy misses.** The post-lunch dip is a second risk window with its own physiological cause, separate from the end-of-shift crunch this analogy describes - a grid clean at day's end can still fail mid-afternoon. Read both, not this one alone.

Treat this heuristic as a prompt for reading your own grid, attach no number to it, and mark the resulting pacing read as judgment when presenting it alongside the sourced material.

## Competing demand for a scarce slot

**Source concept.** Dispatching rules: Earliest Due Date for high-variety short-run work, Shortest Processing Time for long-run low-variety work.

**Borrowed, loosely.** When several accepted talks compete for one prime slot, place the hardest-constrained first - a speaker with a single available day behaves like an earliest-due-date job. Fill the remaining slots with whatever places most simply. This is a structuring analogy for the order in which you make decisions, not a rule to apply mechanically; a grid built strictly by dispatching rule optimizes for placement effort rather than for the program anyone experiences.

## What does not carry over

Named explicitly so nobody reaches for them, these have no conference-scheduling analogue and should not appear in event-scheduling advice:

- OEE.
- MRP/ERP/MES integration.
- Union labour rules.
- Quality-hold mechanics.

Manufacturing's own operating context - discrete and batch manufacturing, 3-8 production lines, 50-300 headcount - is structurally different enough from a conference that any threshold it states is illustrative of a pattern rather than reusable.

## Numbers that must not be reused

- The ~50% constraint-lead-time buffer sizing.
- The 33% / 67% buffer-zone boundaries.
- The 85% utilization target.
- The 30-minute communication window and the 4-hour stability lock.

Each is a real figure in its own domain and a fabrication in this one. Where this skill needs a number, it either cites a published conference schedule by name or tells the user the threshold is theirs to set.
