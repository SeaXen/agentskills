# Civic Forge: mentor headcount check and shift sketch

## Verdict

⚠️ **40 mentors isn't supported by the rule you read, and I can't give you a replacement number from a ratio.** The headcount has to come out of posts and hours.

### Why the one-per-four rule doesn't apply

The rule comes from Joshua Tauberer's `hackathon.guide`: "at least one subject matter expert + workable project for about every four non-expert participants". It fails on all four of its bounds:

| Bound | The rule | Civic Forge |
|---|---|---|
| Event type | Themed hackathons, with projects confined to one problem domain | ❌ Open theme, no tracks. The same source says open-ended events are "not good at" attracting these experts. |
| What it counts | Non-expert participants | Your 160 is total registrations. |
| Who the expert is | A domain expert embedded in one project, who "can only effectively participate in a single project" | ❌ You are budgeting rotating mentors, which is a different role. |
| Purpose | Project supply: stopping a third group of people "struggling to find something relevant to work on" | ❌ It is not a staffing formula. |

The mentoring skill says this outright: never convert it into mentors per participant. It also refuses any invented mentor-to-participant ratio or staffing formula, so I won't offer "1:8" or "1:10" as a swap.

160 ÷ 4 = 40 is arithmetic on a number that doesn't measure what you need. It may still turn out roughly right, but then by accident.

## What to size against instead

Expertise is the scarce thing, not headcount. The skill sizes coverage against coverage units, not against the room.

**Coverage units for Civic Forge.** Keep the list short enough to hold in your head at 03:00.

| Unit | Why | Commitment level |
|---|---|---|
| City open-data portal: API, dataset quirks, licensing | Every team builds on it, so it is the sole shared substrate. The brief has implicitly promised support. | **Guaranteed**: a tagged person present for stated hours |
| General stack: git, deployment, the dominant language | Every team touches it, whatever they build. | Available |
| Demo and presentation | Late-window need, mirroring Opportunity Hack's "presentation mentors in the final stretch". | Available, final stretch only |

Open theme means no track tags. Tag mentors by the portal and by technology, with depth recorded as "has built with it" or "has read the docs".

The portal is the city's. Its data team staff are your natural guaranteed-coverage source, so negotiate their named count and hours as a deliverable. Don't treat it as a volunteer sign-up.

## Headcount arithmetic

This belongs to `event-volunteers`: people needed at once × hours covered ÷ shift length = shift-slots. Sum the slots, divide by the shifts one mentor will actually take (ask at sign-up), then add a floater reserve.

Here is an **illustration with made-up inputs**, to show how 40 would fall out. These are not recommendations.

- Daytime, 18 hours, 4 mentors on the floor: 72 mentor-hours.
- Overnight, 12 hours, 2 mentors on the floor: 24 mentor-hours.
- Total: 96 mentor-hours, which is 24 slots at 4 hours each.
- At 1 shift per mentor, that is about 24 people. At 2 shifts each, about 12.
- Reaching 40 would need roughly 6 to 7 mentors on the floor at once for the whole window, or many short single shifts.

So 40 is a result of choices about simultaneous coverage, shift length and shifts per person. 160 ÷ 4 was never an input.

## Shift pattern sketch

It is a sketch because the hour-by-hour grid needs your run of show. Every hour below is a placeholder to replace.

1. **Hours 0–4, opening and team formation.**
   - Lead with portal specialists, since teams are choosing datasets and checking feasibility.
   - Add general-stack mentors for repo and environment setup.
2. **Hours 4–14, build-out.**
   - Keep the portal specialist guaranteed in every slot.
   - Add general-stack mentors for the main debugging load.
3. **Overnight, roughly hours 14–24.** Choose one deliberately and publish it:
   - **Staffed.**
   - **Thinly staffed:** one portal specialist plus one general mentor, reachable through the request channel.
   - **Published as unstaffed,** with the escalation route stated.
   - Don't use scheduled office hours as the only overnight route, because a 03:00 blocker won't wait for a morning slot.
4. **Hours 24–27, second morning.** Bring back the full portal-plus-general pair. Teams are stuck on integration.
5. **Hours 27–30, final stretch.**
   - Add demo and presentation mentors.
   - Stop scheduled visits ahead of the end, so teams get an uninterrupted run-in.

**Rules that apply to every slot:**
- Treat a slot as a commitment and presence beyond it as a courtesy.
- Use `event-volunteers`' rule that nobody leaves a post without confirmation of a replacement.
- Give each mentor a checkable minimum visit frequency per assigned team. This is a number your event sets for itself.
- Rate-limit roaming visits: a per-visit cap, a team-controlled "do not disturb" signal, and a shared view of which teams are blocked and on what.
- Mentors need a visible marker and a named role.
- If any mentor also judges, keep a mentor–team contact log and hand it to `hackathon-judging` for recusal.

## Open questions

Each one moves a rung, so I need your answers:

1. In person, digital or hybrid? How many rooms? Does the window run overnight, as 30 hours implies?
2. Can the city's data team commit named staff and hours? Is that in any signed agreement?
3. Are prizes cash? That makes a written mentor boundary on who touches the repo mandatory.
4. Is any mentor also on the judge list?
5. By what date must the mentor roster close? Is this a one-off or recurring event?
6. What is the effort ceiling? In particular, will anyone coordinate mentors live through the window?
7. Is there a returning mentor list or a user group that could send a block of people?

The shift grid, arrival buffers and replacement protocol then go to `event-volunteers`, and the mentor briefing to `hackathon-mentoring`.

## Team formation

Your task also pointed me at the team-formation skill. These are the open-theme answers it already gives; I haven't designed team formation here.

- A pitch-and-join round is the default mechanic, since participants bring their own projects.
- Publish a "Teams can be 1-4 people" style rule with the brief.
- Stock a project backlog and name a floor sweeper for anyone left unteamed.
- Set the membership cut-off after the sweep, not at the pitch round.

I can run that interview next if you want.