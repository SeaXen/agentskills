# Cadence rungs as artifacts, and the seam with the edition's own channels

Contents: the four cadence rungs as concrete artifacts; the dormancy notice; a worked pulse plan and a negative example; the between-editions register delta; the two-sided seam table.

Nothing here is measured. Every shape below is illustrative and this skill's own construction unless labelled otherwise, and none of it carries an engagement figure to hit.

## What each rung is, concretely

- **Dormant-but-open** - posting frozen, archive readable and searchable, member list intact and owned, one dated notice pinned. Nobody is on a rota. The space still does work: it is reachable in one post, and it keeps answering search queries from people who arrive months after the edition.
- **Occasional pulse** - one recurring artifact on a stated rhythm, produced by one named person, and nothing else. A digest of what the community shipped, or a spotlight on one member's work. The rhythm is whatever that person can hold for the whole gap - a rhythm chosen for how it looks in a plan is the one that lapses.
- **Continuous light** - a standing rhythm of prompts and discussion threads. No live sessions, no sub-channels, no calendar. Its real cost is that somebody must have something to say every cycle, in the register, without an edition to talk about.
- **Continuous heavy** - recurring live sessions, sub-channels by topic, and a moderation load that never drops to zero. At this rung the space has become a programme in its own right, and the question of whether it should be a standing meetup series instead is a real one to put to the user.

## The dormancy notice

The one artifact the default rung requires. It converts silence from a signal of abandonment into a stated posture, which is the whole of why dormancy scores high on robustness.

Worked shape, an unsourced template:

> **This space is quiet until {next edition's build-up}.**
> The archive stays open and searchable - it is the point of keeping this here.
> Nobody is moderating day to day right now. {Name} owns the space and reads reports at {route}.
> You will hear from us here when {next edition} opens.
> Posted {date}.

What makes it work: a date, a named owner, a conduct route that still functions, and a promise small enough to keep.

Negative example - the same notice without those four:

> Things are a bit quiet at the moment but we'll be back with lots of exciting stuff soon! 🎉

It promises activity on no date, names nobody, and leaves the conduct duty unassigned. A member who reads it in month five concludes the event is over.

## A worked pulse plan

One page, written before the gap starts, covering the whole gap. Illustrative slots, not a prescribed calendar:

| Slot            | Artifact                                    | Owner                    | Source material that already exists       |
| --------------- | ------------------------------------------- | ------------------------ | ----------------------------------------- |
| Post-edition    | Archive is up, talks linked, thank-you      | Owner                    | The edition's own recordings and feedback |
| Mid-gap, first  | Digest: what members shipped since          | Owner                    | Members' own posts, asked for once        |
| Mid-gap, second | Spotlight: one member, one thing they made  | Owner                    | An ask, in the register, to one person    |
| Build-up opens  | Handback: next edition's channels take over | Owner + channel designer | The next edition's plan                   |

The column that matters is the last one. Every slot is filled from material that exists anyway; a pulse plan whose slots need original work is a continuous-light plan with fewer rows.

Negative example: a twelve-slot calendar with a theme per month, written the week after an edition by a team still running on adrenaline. It is abandoned by the fourth slot, and the abandonment is more visible than the silence it replaced.

## The between-editions register delta

Do not write a voice. Write the delta against the register `samber/dev-event-organizer-skills@event-cultural-identity` already fixed, so it stays auditable:

| Register attribute (fixed elsewhere) | Its between-editions expression                      |
| ------------------------------------ | ---------------------------------------------------- |
| {attribute 1}                        | What it sounds like with no event imminent           |
| {attribute 2}                        | What it sounds like when the news is somebody else's |
| {attribute 3}                        | What it sounds like when nothing has happened        |

The third row is the one that matters. A register designed for a stage has to survive a month with no news, and that is exactly when a team invents a second, chattier voice by accident.

## The seam with the edition's own channel architecture

Both skills state this seam. The table pairs the two halves and makes no new claim of its own.

|                | Within-edition channel architecture                                | This skill                                                  |
| -------------- | ------------------------------------------------------------------ | ----------------------------------------------------------- |
| Object         | The channels that exist _because_ an edition is happening          | The space in the gap after wind-down decides one persists   |
| Starts         | When someone registers                                             | When the edition's channels wind down                       |
| Ends           | At the published wind-down date                                    | When the next edition's build-up opens                      |
| Owns           | Roster, message-class routing, multi-writer consistency, wind-down | Cadence posture, conversion mechanism, member list, handoff |
| Same platform? | Usually yes - the seam is the job, not the tooling                 | Usually yes                                                 |

Two handovers, not one: the space comes to this skill at wind-down, and the **live member list** goes back at build-up with its consent basis and its reachable count stated. A handback that arrives as "the Discord still exists" is not a handback.

## Sizing thresholds, and what they do not cover

Christopher Allen's community-size thresholds (Life With Alacrity, 2009) - 7, 13, 50, 90, 150, with the widely-repeated "5/12/45" set a misquote - describe groups with ongoing interaction. They put the event-relevant break where "a small conference that worked well at 60 participants tries to grow and finds at 100 participants they can't sustain a high enough intimacy level."

Two non-transfers, both load-bearing here:

1. A dormant archive has no ongoing interaction, so the thresholds say nothing about it.
2. A member list is a stock, not a group. Five hundred members of whom a handful talk is a normal shape for an event's space and is not a failure against Allen's numbers.

The same break shows from the other side: some local communities plateau around 100 people per gathering and treat that as a good format, not a growth failure. Read it as one report consistent with Allen's break near 100, not as a ceiling. Whether to push past it is `event-growth-strategy`'s call.

Use the thresholds only to set expectations about how many members actually talk to each other under the two continuous rungs. Never as a target membership number, and never quoted as a benchmark this skill's output is scored against.
