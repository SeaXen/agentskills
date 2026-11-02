# Mentor plan for DevHarbour Hack: should you take Northgate's offer as-is?

**No. Accept the six engineers, but not "we don't need anybody else".** Take them as the Northgate-track mentors and as one half of a mixed pool. Recruit a small community or alumni group for the general track. Get the commitment in writing before you say yes.

I applied the `hackathon-mentoring` skill (SKILL.md plus both references). I haven't asked you its interview questions yet, so the plan below rests on stated assumptions. Section 9 lists the answers that would change it.

## 1. Why "sponsor staff only" fails

- **Two tracks.** Six engineers who all know one platform leave every general-track team with nobody. The skill deletes the "sponsor staff only" option outright whenever the brief carries a general track next to a sponsor track.
- **Sponsor badges read as sales.** Participants may see a Northgate badge as a sales conversation, so even the Northgate teams may hesitate to ask for help.
- **The saving is smaller than it looks.** You skip a recruiting channel for the sponsor half. You still owe a written agreement, a briefing and a rule. The general track still needs its own warm list.

Your headcount is not the issue. I won't tell you six for 180 is too few or too many: the skill refuses to invent mentor-to-participant ratios, and nothing published supports one. The scarce thing is the right expertise in the right hours. Six Northgate specialists give you plenty of Northgate coverage and none for the general track.

## 2. Coverage depth by track

| Coverage unit | Commitment level | Depends on |
|---|---|---|
| Northgate track | **Guaranteed** if Northgate's tech is required for that track (it probably is). Otherwise **available**. | Q2 below |
| General track | **Available**, from community and alumni. | None |
| Shared stack (git, deployment, the dominant language) | **Available**, from both pools. | None |

- **Coverage rung:** rostered mentor shifts is the default. Promote to an expertise-matched roster if the Northgate track requires their technology. That is the likely case, so plan for it.
- **Guaranteed means a tagged mentor is present for stated hours.** Those are the hours the Northgate track is actually being worked, not "the whole weekend" in general.
- **"Whole weekend" is a courtesy, not a commitment.** Ask Northgate to commit to named slots. Presence beyond those slots is a bonus you can't schedule against.

## 3. Recruitment

**Rung: mixed pool with a written engagement rule.** The brief names a sponsor technology, which is the skill's promotion condition for this rung.

**Northgate engineers: a sponsorship deliverable, not volunteers.** Negotiate it in the sponsor agreement, not in a briefing email. Three things go in writing:

1. **Names.** Six named people, or at minimum a count plus the technology each covers.
2. **Hours.** Committed shifts matched to when the Northgate track is worked.
3. **The engagement rule.** They are there to unblock teams, not to pitch or recruit. Putting it in the agreement makes the later briefing a reminder, not a new condition.

If a Northgate engineer doesn't show, that is a fulfilment failure against a commitment. Handle it with Northgate. Don't backfill it as a volunteer no-show.

**Community and alumni: the general track.**
- Publish this as a warm-list ask, not an open call.
- Use a user group, past participants, or maintainers of libraries the brief depends on.
- Size it by coverage units: the general track plus the shared stack, across all hacking hours. Don't use a headcount ratio.
- Roster closing date (Q9) sets the lead time. A close date favours this warm list, because it answers in days while sponsor negotiations take weeks.

## 4. Expertise tags

- **Use the brief's own words.** One tag per track ("Northgate", "general"), plus Northgate's products by name, separate from the underlying skill. "Knows Northgate's SDK" and "knows the language it's written in" are different coverage.
- **Record depth in two levels: "has built with it" or "has read the docs".** Ask at sign-up. Don't infer it from a job title.
- **Keep the list short enough to recall at 3am.**
- **Ask Northgate for each engineer's tag and depth in the agreement**, so you aren't discovering gaps on Saturday.

## 5. Hand-off to the shift plan

Your constraint to `event-volunteers` is: "this tag, present, these hours." Concretely:

- A Northgate-tagged engineer is on the floor during every hour the Northgate track is being worked.
- A general-track and shared-stack mentor is present across all hacking hours.
- **Overnight:** decide whether those hours are staffed, thinly staffed, or published as unstaffed, and publish whichever it is. A Northgate engineer's overnight hours can't be assumed. Ask.

That skill owns shift length, buffers, confirmation and backfill. Don't rebuild any of it here.

## 6. Request mechanic (publish it where teams read the brief, before the window opens)

Baseline: **identifiable mentors**. Give them a visible marker and a named role in your channels. This is the cheapest intervention that works.

Promote to a **request channel with organizer routing** if any of these is true:
- The event is digital or hybrid.
- The space spans several rooms.
- Northgate questions must reach one named person.

Promote to a **staffed mentor area** if the space has more than one room, or the mentor crew is larger than your organizing team.

Rules that hold either way:
- Routing needs at least two people who can work it. Never route everything through one organizer's DMs: that person sleeps at the worst hour.
- Office hours can supplement but never replace a latency mechanic, especially if the window runs overnight.
- State four things to participants: how to recognise a mentor, how to ask, what to expect, and what happens when nobody covers the skill.

## 7. Mentor briefing

Every mentor gets, in writing:
- Where to be and when. A slot is the commitment.
- The request mechanic exactly as participants see it.
- Who to escalate to for non-technical issues, and the code-of-conduct escalation pointer. Point at `event-code-of-conduct`; don't paraphrase it.
- Power-dynamics guidance: ask before touching anything, don't evaluate the idea, and say aloud when you don't know.

**Help-versus-build boundary** (edit into your own voice; it's a line you set, not a standard to cite):

> Mentors explain, diagnose, unblock and demonstrate. Mentors do not write code that ships in a submission. If a mentor needs to show something in code, it is written outside the team's repository (a scratch file, a message, a whiteboard) and the team types the version that lands. If a mentor has already committed to a team's repository, the team declares it in the submission.

**Sponsor-representative rule** (to every Northgate engineer, mirrored in the agreement):

> While mentoring, you are helping the team in front of you with the problem they brought. Not a sales conversation, not a recruiting conversation, not a demo. If a participant asks about your company, pricing, or working for you, answer briefly and point them to your booth or team channel.

**Briefing depth.** "No briefing" is deleted if any prize carries cash value or a sponsor funds one, which is likely here, so confirm Q6. Use "boundary stated" as the default. Promote to "boundary plus scenario walkthrough" because Northgate staff are mentoring on a codebase their employer has a commercial interest in. Teams may build on Northgate's product during the hack, and a walkthrough gives you a written standard to hold the sponsor engineers to.

## 8. Contact log, interruption discipline, uncovered skills

- **Contact log: keep it if any confirmed mentor is also a judge.** This applies most to Northgate engineers, who sponsors often propose for the jury. Record which mentor spent meaningful time with which team. Hand it to `hackathon-judging` before the judge pool is fixed. That skill owns the recusal rule: a mentor who materially helped a team doesn't score that team. Whether a Northgate engineer sits on the jury is your decision. Q5 settles it.
- **If mentors roam:**
  - Cap each visit and show a timer.
  - Give teams a "do not disturb" signal.
  - Publish who knows what.
  - Share a live "blocked teams" view, so six Northgate engineers don't cluster on the loudest team.
- **Uncovered skill route.** Publish this before the window:
  1. Check the roster's second depth level.
  2. Ask Northgate's channel (that's what the commitment is for).
  3. Ask the room, as a request and never an assignment.
  4. Tell the team plainly that no help exists, early enough to pivot.

  Log every case as a coverage gap for next edition.

## 9. Questions that would change this plan

1. **Q1:** Is the event in person, digital or hybrid? How many rooms? Does it run overnight? This drives the request mechanic and overnight staffing.
2. **Q2:** What is Northgate's integration depth? Options: optional bonus, required for their track, or sole substrate. It sets "available" versus "guaranteed", and whether "no mentor programme" is even allowed.
3. **Q3:** Is the general track open (teams bring their own problems) or themed?
4. **Q4:** Is Northgate's mentor commitment already in a signed agreement? Does it name people and hours?
5. **Q5:** Is any Northgate engineer, or any other mentor, on the judge list?
6. **Q6:** Do prizes carry cash value, and does Northgate fund one? This deletes "no briefing".
7. **Q7:** Have these mentors mentored before? Does the event recur?
8. **Q8:** What is your effort ceiling, and is a volunteer shift grid already built?
9. **Q9:** What is the date by which the roster must close and the request mechanic must reach participants?
10. **Q10:** What already exists? Last year's mentor list, a user group that would send several people, or Northgate staff already on site for a booth.

## 10. Pass threshold before the window opens

All five items below must exist in writing with zero blanks. These are self-set bars, so compare them only against your own previous editions.

1. Expertise tags mapped to the two tracks.
2. Coverage commitment per track, with hours.
3. The request mechanic as teams will read it.
4. The mentor briefing, including the boundary sentence.
5. The escalation route for a skill nobody covers.

## What to tell Northgate

> "Thank you. We'd love your six engineers as our Northgate-track mentors. We'll recruit separately for the general track so every team has help. Can we agree named people, committed hours matched to when the Northgate track is worked, and a short engagement rule in the sponsorship agreement?"

Send me answers to Q1, Q2, Q4, Q5 and Q6 and I'll tighten the plan. I can also draft the agreement clause, or write the briefing and the participant-facing request-mechanic text.