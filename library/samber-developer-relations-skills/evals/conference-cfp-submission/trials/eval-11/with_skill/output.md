Using the **conference-cfp-submission** skill for the two questions inside its scope (reuse, and the new Hartfield submission), and handing off the other two per its explicit boundary ("scope ends at submit... hand off rather than drifting") to **tech-talk-outline** (narrative arc + slides) and **developer-live-demo-design** (demo reliability) — both confirmed present in this repo and read in full.

One rule from `references/proposal-pack-template.md` governs everything below: *"Never invent an employer, a customer name, a metric, an award or a prior talk. Where the user has not supplied one, write the placeholder as a question."* I don't have the talk's topic, either March event's name, slot length, the demo's tech, or Hartfield's CFP page — so parts 3 and 4 end in real, specific questions instead of invented content.

## 1. Is the PyData Grenoble talk a problem for the two March events?

Almost certainly not a *reuse* problem, but check two things this week, not on stage:

- ⚠️ **Recycled-content clause.** Pull each accepting event's CFP page or speaker terms and look for the line on whether a previously-delivered talk is eligible (`references/event-research-checklist.md` flags this as its own row — most community events allow reuse, some ask you to say so, a few ban it outright for "new content" tracks). If either submission form had a "has this been given before?" field, go check what you actually answered there — a wrong or blank answer is a disclosure problem, not a reuse one, and it's the only version of this that can void an acceptance after the fact.
- ⚠️ **Recording collision.** If PyData Grenoble published a recording, some organizers treat "publicly available as a recording" differently from "previously given live." Check each March event's terms for that distinction before assuming silence means it's fine.
- ✅ **Cheap insurance:** send each March organizer one line now — "heads up, I gave a version of this at PyData Grenoble in October, recording here if useful" — even where no rule requires it. The skill's own logic on employer disclosure applies identically here: *"reviewers find out anyway, and a hidden affiliation reads worse than a declared one."* Costs nothing, and it's the kind of thing that reads badly if a chair discovers it unprompted instead.

Net: proceed, but confirm those two things before the first March date, not after.

## 2. Should you fire the same proposal at Hartfield Cloud Days?

Yes, with 15 minutes of checking first — "it's already written" is exactly the trap Step 2 warns about (fit, not effort, is what wins a slot):

1. **Re-read Hartfield's CFP page before pasting anything** (Step 1). Field list, character caps, and format/duration rarely match the two events you wrote this for verbatim — a caps breach or a wrong-field paste is the single most common way a ready-made proposal loses.
2. **Check track and audience fit independently**, don't assume it because two other events said yes. A proposal that fit a data/ML track and a cloud-infra track can still miss Hartfield's actual track descriptions.
3. **Check anonymity rules.** If Hartfield reviews blind and your accepted version names an employer or product, strip it before resubmitting.
4. **Check the recycled-content clause here too** — same as above.
5. **Disclose the two other acceptances in "notes to reviewers"** if the field exists. Once schedules publish, a chair who searches your name finds both anyway; better they hear it from the proposal.
6. ⚠️ **The real constraint isn't the CFP, it's your calendar.** You'll now be defending three editions of one talk in one stretch. What's Hartfield's event date relative to the two March dates? If it lands close behind them, that's fine — the talk is rehearsed by then. If it lands *before* either March date, you're debuting the talk at event #3 instead of Grenoble, which changes what "already given" even means for the other two's disclosure line above.

Tell me Hartfield's actual event date and I'll fold it into the season-tracking file this skill recommends (event / format / angle / verdict / feedback, one row per event, so the next CFP season starts from it instead of memory).

## 3. Slide deck and narrative arc — routed to `tech-talk-outline`, blocked on inputs

This skill stops at submission; structuring the accepted talk is `tech-talk-outline`'s job, and it explicitly treats "same talk, different slot" as its own case rather than one outline copied twice. It also gates hard on inputs before producing an arrow, an arc, pillars, or a slide skeleton — I don't have any of the following yet, and inventing them would just be fiction with your name on it:

1. Paste the accepted title + abstract, and the outline you submitted, if any.
2. Slot length for each of the two (soon maybe three) events, and whether Q&A sits inside or after — these often differ even when the talk is "the same."
3. Who's in the room and which track, per event — hands-on engineers, staff/architects, managers, mixed.
4. Is the live demo required by the abstract, optional, or your own addition?
5. What first-hand material already exists (incident, benchmark, migration, repo, blog post)?
6. Recorded at either event?
7. Any hard constraints — corporate template, embargoed numbers, co-speaker?
8. Rehearsal hours available before the first March date.

Send those and I'll produce the real deliverable: the arrow, 2-3 ranked candidate arcs, the pillars with their evidence, the realization point, a per-event time budget (they'll diverge once slot lengths differ), the slide skeleton, cut checkpoints, and a rehearsal plan — one shared spine, with the per-slot variants called out rather than three separate decks built from scratch.

## 4. Making the live demo not blow up — routed to `developer-live-demo-design`, blocked on inputs

Same situation. This is a demo-reliability-engineering job — risk register, fidelity tier, checkpoints, fallback, recovery lines, pre-flight checklist — not something this skill or a guess can responsibly fill in. Needed before I can build the runbook:

1. One sentence: what must the demo prove?
2. What does it touch — local code/service, your hosted product, a third-party API, a cloud account, real customer data?
3. Do you control each venue's network, or are you a guest? Is a hotspot realistic in those rooms?
4. Minutes budgeted for it, and what happens to the talk if it runs double?
5. What already exists — repo, script, seeded environment, recording, sandbox tenant?
6. What's already gone wrong when you've run this (or something like it) before — you said "not blow up," which reads like there's a specific failure mode in mind; name it.
7. Hard constraints — no screen recording, embargoed UI, locked-down laptop?
8. Rehearsal hours before the first date, and who owns the demo afterward?

One thing worth flagging now, before you answer: since this demo runs at two or three events this year, that re-run amortizes the cost of building a fully local/offline version (tier 2 on the fidelity ladder) — the skill's own ranking promotes exactly that tier once a demo isn't a one-off. Answer the above and I'll deliver the claim, the segment/checkpoint design, the tier recommendation, fallback assets, written recovery lines, and the pre-flight checklist as one runbook.