# Format and lifecycle gates

Contents: what each gate means, the format matrix, the lifecycle matrix, and what to do when the format is not fixed.

A gate is a reachability test, not a ranking. It answers "can this row apply to this event at all", and it is always read from an answer the user gave or an artifact on disk - never inferred from the event's name, its ambition, or the user's tone.

Each gate's value comes from one place:

- Format gates - question 2, and once fixed, `samber/dev-event-organizer-skills@event-format-selection`'s output recorded in the context artifact.
- Lifecycle gates - question 3 and the artifact's edition number and property list.
- Company gate - question 4 and the artifact's funding model.

## Format gate matrix

| Gate         | Open when                                                                                                   | Rows it governs                                                                                                                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hackathon`  | The shape is a hackathon                                                                                    | `hackathon-brief-design`, `hackathon-team-formation`, `hackathon-mentoring`, `hackathon-judging`, `hackathon-cash-prize`                                        |
| `workshop`   | The format committed hours to hands-on sessions                                                             | `workshop-program-design`                                                                                                                                       |
| `virtual`    | Delivery mode is fully virtual                                                                              | `virtual-event-production`                                                                                                                                      |
| `hybrid`     | Delivery mode is hybrid                                                                                     | `hybrid-event-design`                                                                                                                                           |
| `in-room`    | Delivery mode is in-person or hybrid - that is, a physical room exists                                      | `event-venue-sourcing`, `event-attendee-experience`, `event-hospitality`, `event-production`                                                                    |
| `conference` | The event is at conference scale: more than one track, or an expo floor, or a named-guest and press surface | `event-press-relations`, `event-booth-experience`, `event-b2b-matchmaking`, `event-vip-management`, `event-official-social-program`, `event-vip-social-program` |
| `company`    | A company funds and owns the event                                                                          | `corporate-event-strategy`, `business-event-formats`                                                                                                            |

Three consequences worth stating, because each deletes rows a reader expects to see:

- A fully virtual event closes `in-room` outright: no venue to source, no room to lay out, no catering, no physical signal path. `virtual-event-production` replaces all four, and `event-accessibility-inclusion` still applies because its digital-access provisions need no room.
- `hackathon` and `conference` are not mutually exclusive. A multi-track conference running a hackathon track opens both, and `startup-pitch-contest` is ungated on purpose: it judges companies that existed before the event, so it fits either. When its award is equity-free cash, it reaches `hackathon-cash-prize` for payout mechanics despite that row's `hackathon` gate.
- `conference` is not a synonym for "big". Its threshold is qualitative and self-set, not a measured headcount: it opens when the event has the surface - a floor, a press pool, guests who create protocol obligations - not when the organizer hopes it will.

## Lifecycle gate matrix

Ask this in the shape `event-planning-timeline` already assumes: any edition can be planned, but only some skills have a previous edition to read.

| Gate         | Open when                                                                     | Rows it governs                                                                                                                             |
| ------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `first`      | This is edition one of something new                                          | `event-first-edition`                                                                                                                       |
| `recurring`  | Edition two or later                                                          | `event-team-structure`, `event-continuous-improvement`, `event-community-building`, `event-growth-strategy`, `tech-podcast-youtube-channel` |
| `properties` | The team runs more than one event property, or is deciding whether to add one | `event-portfolio-strategy`                                                                                                                  |

Two rows are commonly mis-gated and are not:

- `cross-event-promotion` is **not** recurring-gated. Its own interview asks whether the swap is a one-off boost for the coming edition or a compounding relationship, and it answers both. Gating it would delete the one acquisition lever a first edition can reach without a track record.
- `event-portfolio-strategy` gates on **property count, not recurrence**. A team running a single event forever never opens it; a team weighing whether to add a second format opens it on the day they start weighing, whatever edition the flagship is on.

The `recurring` gate is about having an edition to read, not about intent to repeat. A team that intends to recur but has not yet finished edition one still has nothing for `event-continuous-improvement` to compare.

## When the format is not fixed

Question 2 answers (a) "nothing fixed" and (b) "shape fixed, the rest open" both mean the format gate cannot be applied.

1. Route to `samber/dev-event-organizer-skills@event-format-selection` and stop. Do not offer a short-list drawn from gated rows.
2. Say which rows are suspended and why - the hackathon lane, the delivery-mode skills and the conference-scale population skills are unreachable until the shape and mode exist, not absent from the collection.
3. Record the returned decision in the context artifact the moment it exists, so the next session reads the gate instead of re-asking question 2.
4. Never guess a shape to unlock rows with. A misapplied gate routes confidently to a skill written for a different event, which is worse than routing to nothing.

Answer (b) is the partial case: a known shape opens `hackathon` and `workshop` while the delivery mode is still open, so `in-room`, `virtual` and `hybrid` stay suspended, and `conference` usually does too, since track count is part of what is still open.
