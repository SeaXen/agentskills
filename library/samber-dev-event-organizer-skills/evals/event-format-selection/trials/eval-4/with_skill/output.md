# CodeSprint format review: hybrid is the weak point

**Verdict:** the plan doesn't hold up as written. Two of its choices are the ones the sourced hackathon record argues against: hybrid delivery and every team pitching on stage. I'd keep the 48-hour in-person core and change those two.

This is a structural review under `event-format-selection`. The scoring rubric belongs to `hackathon-judging` and the challenge brief to `hackathon-brief-design`.

## 1. Delivery mode: hybrid for a hackathon

For hackathons the skill deletes hybrid outright. It does not just rank it low. The source is Major League Hacking (MLH), whose organizer guide says: "We will not be working with hybrid events… hybrid events are worse for both organizers and hackers." It also says "a well run digital hackathon is more than just a Discord."

MLH's named failure modes map onto your plan:

- Judging reads as inconsistent because remote teams can't present science-fair style next to on-site teams.
- Sponsors work their booths, so remote teams get fewer sponsor interactions.
- Workshops run late or stay in-person-only, and virtual participants get no notice.
- Side activities skew physical, so remote engagement drops.
- Swag and prize fulfilment skew to people in the building.
- Cross-format team collaboration is harder.

"Everyone judged together at the end" is where those problems concentrate. MLH's preference is constraint-driven, not universal doctrine. It is still the strongest published evidence, and a student volunteer team is the kind of organizer it describes.

**Options:**

| | Structure | Trade-off |
|---|---|---|
| **A (recommended)** | In-person only. Discord stays as an internal tool for announcements, mentor requests and team-finding. | Remote teams drop out or travel in. Lowest effort and risk. |
| B | Two events under one name. An in-person hackathon plus a separate digital one with its own video judging and its own prizes. | Honors the remote teams, but it is roughly two productions and needs more volunteers. |
| C | Keep hybrid. | Maximum cost and risk. Not a safe middle. |

**To confirm A:** how many of the ~40 teams are remote, and why? The skill's hybrid promotion needs remote registrations reliably above ~25-30% of paid attendance and covering their marginal cost. "Teams asked to join remotely" isn't evidence. If remote teams are only a handful, A is clear. If they are close to half, B deserves a serious look.

## 2. Judging: all 40 teams pitching on stage

Stage pitch is the weakest fit at your size. It is serial, so it doesn't scale.

| Per-team slot | Total for 40 teams |
|---|---|
| 3 min pitch + 2 min Q&A + 1 min changeover (6 min) | ~4 h |
| 5 min pitch + 2 min Q&A + 1 min changeover (8 min) | ~5.3 h |

These are my arithmetic, not sourced figures.

The costs of running 40 serial pitches:

- Judges tire, and late teams score worse than early ones.
- 250 hackers sit through hours of pitches right after 48 hours without sleep.
- Technical judges can't touch the demo, which is the thing they want.
- Teams pitch hours after their build ends, and the finale loses energy.

Stage pitch does give a strong winner narrative. Expo tables don't, and the skill's catalog marks them weak on that. Two-stage covers both needs.

**Candidates:**

| | Structure | Fit |
|---|---|---|
| **A (default)** | Expo table. Judges rotate through teams, 3-5 min each, in parallel. | Scales to 40 teams and gives real demo contact. No shared moment. |
| **B (promote if Q11 below is yes)** | Two-stage. Expo round, then the top ~5-6 teams pitch on stage. | Strongest winner narrative, moderate scale. The skill ranks it the most judge-hours and staging effort. |
| C | Stage pitch for all 40. | Does not scale. Not recommended. |

Two-stage is the "starved" option because it costs the most. The skill promotes it only when press or sponsor reporting needs a legible on-stage finale. A university or sponsor often does, and a finals stage is easy to justify to them. If it doesn't apply, expo table alone is the right call.

Match the jury to the format. Technical judges go to the expo round and business or sponsor judges to the finale. Judges still need rubric prompts so their priority surfaces in a short slot. That detail goes to `hackathon-judging`.

## Recommended structure

1. **Shape:** hackathon. Keep it, since the goal is artifacts and team formation.
2. **Delivery:** in-person, 48 h, at the engineering building. Discord is support tooling only.
3. **Judging:** expo-table round with a parallel jury, then a top-5/6 stage finale if sponsors or the university need one.
4. **Remote teams:** option B (a separate digital hackathon) only if the numbers justify it.

## Questions I need to finalize

1. How many teams, and how many hackers, are remote, and why can't they travel?
2. Does a sponsor or the university need a visible on-stage finale?
3. How many judges, and are they technical, business, or mixed?
4. What is the volunteer headcount and the effort ceiling?

## Revision triggers for next edition

- Remote registrations reliably above ~25-30% and covering their cost: revisit hybrid, or run option B.
- Expo judging produces inconsistent scores or judge complaints: add the stage finale.
- Sponsors stop needing a finale: drop back to expo only.

## Hand-offs

- `hackathon-judging`: rubric, weights, jury mechanics.
- `hackathon-brief-design`: challenge document and challenge tracks. A "track" there is a thematic category, not a parallel session stream.
- `event-schedule-design`: the 48-hour grid and demo-slot layout.

I haven't asked the interview questions interactively, so this is a recommendation with stated assumptions, not an approved format brief. Tell me which option you want for delivery and judging, and I'll finalize section by section.