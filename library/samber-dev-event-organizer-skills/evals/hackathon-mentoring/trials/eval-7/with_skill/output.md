# Lumen Hack mentor plan: is it enough?

**No. Two of the three pieces need changing.** Here is what to change, what to keep, and what I still need from you.

## Verdict on your three pieces

| Piece | Verdict | Why |
|---|---|---|
| Priya takes all help requests by DM and forwards them | ❌ Replace | One person is a single point of failure. She sleeps at some point in 36 hours, and 03:00 is when the most teams are blocked. |
| Office hours at 10am and 4pm both days | ⚠️ Keep as a supplement only | The window runs through Saturday night. A team blocked at 02:00 does not wait for 10:00. |
| Two rooms, 36 hours straight | ℹ️ This is why you need more | A multi-room, overnight event moves you up to a routed request channel and a staffed mentor area. |

### 1. Priya's DM routing
Routing every request through one named person's DMs is a rung this plan deletes outright. It looks like the cheapest queue, and it fails at the hour you need it most.

"Costs nothing" is also wrong. A routing job is a standing job for the whole window. It puts every technical question on the person running ops, at the hour ops is hardest to run.

Her instinct is good: one clean record. You can keep that and drop the single point of failure.

- Replace the DMs with a **shared request channel**. Mentors watch it, and teams post there.
- Make at least **two people** work the routing, in shifts. Priya can be one of them, with a second routing person covering the overnight hours.
- The channel history is your clean record. It gives you the "requests that waited longest" and "requests that found nobody" signals for free.
- Have mentors claim a request in-thread ("taking this"). Two mentors then don't pile onto one team.

If you can't staff two routers, publish a fallback route that needs no routing, such as the staffed mentor area below. Do not fall back to Priya's DMs.

### 2. Office hours at 10am and 4pm
Office hours give a good expertise match but the worst latency. They answer questions that can wait, and hackathon blockers mostly can't.

Keep them as a supplement, for example for design critique or architecture sanity checks. They cannot be the mechanic. Four fixed slots over 36 hours leave most of the window uncovered, and the whole night.

## What I'd put in place

**Request mechanic (the part participants read).** Publish it where the brief is published, and repeat it at opening. It states four things:

1. **How to recognise a mentor.** Use a visible marker (lanyard, vest or sticker) and a named mentor role in the event chat.
2. **How to ask.** Post in the request channel. Or, in the room, walk up to the staffed mentor area.
3. **What to expect.** Someone will come. Asking early is normal.
4. **What happens when nobody covers the skill.** The route is spelled out, so a gap reads as a known limit.

**Staffed mentor area (one per room).** With two rooms, "find a mentor" stops working as an instruction. Staff one area per room, or one central area plus the channel.

**Overnight hours.** Decide now whether 22:00–08:00 is fully staffed, thinly staffed, or published as unstaffed. Publish whichever you pick.

My default is thin staffing with a named router and a few mentors on rotation. Name the router for each night hour. Never leave overnight implicit.

**Coverage depth.** Don't size by headcount.

- I won't give you a mentors-per-team number for 50 teams. No sound ratio exists. The one published figure is for themed events, counts non-expert participants, and measures project supply rather than mentor staffing.
- Size by **coverage units**: one per challenge track, one per named sponsor technology, and one for the general stack every team touches (git, deploy, the main language).
- Set a level per unit: *unstaffed and published*, *available*, or *guaranteed for stated hours*. A sponsor technology required for a track needs *guaranteed*.
- Tag every mentor with what they have actually **built with** versus only **read the docs on**, using the brief's own track names.
- I'll hand the guaranteed hours to your volunteer shift plan as a constraint ("this tag, present, these hours"). Shift arithmetic, buffers and no-show backfill live there.

**Push coverage (mentors roaming).** If mentors will roam, rate-limit them.

- Cap each visit and show a visible timer.
- Give teams a "do not disturb" signal they control.
- Publish a list of who knows what.
- Keep a shared view of blocked teams, so mentors don't cluster on the team that pitched loudest.
- Stop scheduled visits before the final stretch so teams get an uninterrupted run-in.

**Mentor briefing (cover these in it).**

- Where to be, when, and that a slot is a commitment.
- How requests arrive, in the exact form teams use.
- Who to escalate non-technical issues to.
- A pointer to your code-of-conduct escalation script, not a paraphrase of it.
- **The help-versus-build boundary.** Mentors explain, diagnose, unblock and demonstrate. They do not write code that ships in a submission. Any demo code goes outside the team's repo, and a team that already took mentor commits declares them in the submission. This matters most if any prize has cash value.
- Power-dynamics guidance: ask before touching a laptop, don't evaluate the idea, and say aloud when you don't know.
- If sponsor staff mentor: a written rule that they don't pitch or recruit while mentoring, mirrored into the sponsor agreement.

**Uncovered skill route (publish it).**

1. Check the roster's "read the docs" level.
2. Ask the sponsor's channel.
3. Ask the room, as a request only.
4. Tell the team plainly, early. A team told at hour 4 can pivot; one told at hour 30 cannot.

**Mentors who also judge.** If any mentor is also on the judge list, keep a log of which mentor spent meaningful time with which team. The recusal rule and mechanics belong to your judging plan.

## Open questions

I can't finalise coverage depth or the briefing level without these. Answer in any order:

1. What are the **challenge tracks**, and at what **sponsor-integration depth** (named funder only, optional bonus, required for one track, or sole substrate)?
2. Is the event **themed** with set problems, or **open**?
3. Who is **already committed** to mentor: community members, alumni, sponsor staff? Is any sponsor staffing commitment in a signed agreement?
4. Do **prizes carry cash value**, and does a sponsor fund one? If yes, the boundary must be stated explicitly in the briefing.
5. Is any mentor also on the **judge list**?
6. Have these mentors mentored before, and is this a **one-off or recurring** event?
7. What is your **effort ceiling**? Can you staff two routers live, and does a shift grid already exist?
8. By what **date must the roster close** and the mechanic reach participants?
9. Is the event fully in person?

## Pass check before the window opens

All five must exist in writing, with no blanks:

1. Expertise tags mapped to the brief's tracks.
2. Coverage commitment per track.
3. The request mechanic as teams will read it.
4. The mentor briefing, including the boundary sentence.
5. The escalation route for an uncovered skill.

Today you have none of the five.

## Next step

Which should I do next: draft the participant-facing request mechanic, or wait for your answers to the nine questions and then finalise coverage per track? I'd answer questions 1, 4 and 7 first, because they change the plan the most.