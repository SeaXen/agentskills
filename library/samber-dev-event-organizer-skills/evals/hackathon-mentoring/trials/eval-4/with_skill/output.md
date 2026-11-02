# Foundry Jam mentor plan: skip recruiting, but not "ask an organizer"

✅ **Your instinct holds on recruiting.** Skip it.
⚠️ **The mechanic needs work.** "Ask an organizer" with nothing else is the weakest version of the plan.

## 1. Why skipping recruitment is defensible

- "No mentor programme" is a real option for an open-theme event with no sponsor technology.
- Its main risk is a brief that promises support nobody staffed. You have no sponsor tech and no track promise, so that risk is absent.
- Tauberer's `hackathon.guide` ratio doesn't apply. It covers themed events and counts domain experts inside projects. Don't turn 60 participants and 6 organizers into a ratio either way.
- Expertise is the scarce quantity, not headcount. Six senior engineers are a good supply, if they cover what teams actually build.

## 2. Where "ask an organizer" fails

1. **Attention cost.** On-call from organizers is cheap to set up and the most expensive rung to live through. Every technical question goes to the people running the schedule, at the moment the schedule is hardest to run. Six people doing both jobs means someone is always pulled off a task.
2. **"Know everything" is untested.** Open theme means anything: ML, embedded, mobile, game engines, hardware. Six seniors rarely cover all of it. Check against the registration data before you trust it (step 3 below).
3. **Nobody can tell who to ask.** If 60 people can't tell organizers from participants, they conclude there's no help.
4. **Keyboard takeover.** Senior engineers fix things fast, and that is exactly the risk. If a prize has cash value, a commit by an organizer in a team's repo becomes a contested-authorship question at the ceremony.
5. **Possible judge conflict.** If any organizer also judges, they must recuse from teams they helped.

## 3. Recommended design

**Coverage rung: on-call from organizers, tightened.** Section by section, for your validation:

1. **Coverage commitment.**
   - One coverage unit per stack that registration reveals, plus one for the general stack (git, deployment, the dominant language).
   - Level for every unit is "available". Nothing is "guaranteed", because there is no sponsor.
2. **Expertise tags (30 minutes).**
   - Add one registration question: "What stack will you most likely build with?"
   - Tag each of the six with what they have *built with*, not just read about.
   - Use two depth levels: built with it, or read the docs.
3. **Recruitment.**
   - Recruit no one by default.
   - If a stack shows up that none of the six has built with, recruit for that tag only. Ask a user group, a past participant, or a maintainer of that library.
   - Start one to two weeks before the event. Warm lists answer in days.
4. **Request mechanic.**
   - Single room, no overnight, so identifiable mentors plus walk-up is enough.
   - Everyone on mentor duty wears a marker (badge colour or lanyard) and has a named role.
   - Publish this with the brief and repeat it at the opening.
   - Never use "DM one organizer". It fails when that person is busy or asleep.
   - If you add a chat channel, have at least two people working it.
5. **Rotation.**
   - Give the grid constraint to `event-volunteers`: at least 2 or 3 tagged organizers on the floor at any hour, so the rest can run the schedule.
   - Slots are the commitment. Presence beyond a slot is a courtesy.
   - Cover 9am to 9pm with no overnight gap. Say "no help outside these hours" in the brief.
6. **Mentor briefing (one page, for six people).**
   - Where to be, when, and how requests arrive.
   - **Boundary:** "Organizers explain, diagnose, unblock and demonstrate. They do not write code that ships in a submission. Show things in a scratch file or on a whiteboard, and the team types the version that lands. If an organizer already committed to a repo, the team declares it in the submission."
   - Ask before touching a laptop. Don't evaluate the idea. Say "I haven't used this" out loud.
   - Point to the code-of-conduct escalation script. Don't paraphrase it.
7. **Uncovered skill route (publish it).**
   1. Check the second-level (read-the-docs) people.
   2. Ask the room.
   3. Tell the team plainly that no help exists, early enough to pivot.
8. **Roaming discipline.**
   - Organizers will wander the room, so cap each visit with a visible timer.
   - Give teams a "do not disturb" card.
   - Keep a shared list of which teams are blocked and on what, so two organizers don't visit the same team.

## 4. Answers that would change the plan

| Question | If yes |
|---|---|
| Cash-value prize or sponsor-funded prize? | The briefing becomes mandatory. You can't skip the boundary. |
| Any organizer also judging? | Keep the contact log (who spent time with which team) and hand it to the judging plan. |
| Registration shows stacks none of you has built with? | Recruit for those tags only. |
| Recurring event? | Write the briefing once and reuse it. |
| Roster or request-mechanic deadline close? | Keep recruiting to a warm list only. |

## 5. Pass check (before 9am Saturday)

All five must exist in writing, with no blanks:

1. Tags mapped to the registered stacks.
2. Coverage commitment per unit.
3. The request mechanic as teams will read it.
4. The briefing, including the boundary sentence.
5. The escalation route for an uncovered skill.

These thresholds are self-set, so compare them only against your own next edition. During the day, record three things:

- Which request waited longest.
- Which hours had no tagged organizer on the floor.
- Which requests found nobody.

Those records tell you whether next edition needs real mentors.

## Next step

Do you want me to draft the one-page briefing and the registration question? Also tell me: are there cash prizes, and does any organizer judge?