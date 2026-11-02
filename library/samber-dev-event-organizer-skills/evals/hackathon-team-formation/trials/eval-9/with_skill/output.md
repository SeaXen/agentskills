# Harbourlight Hack (140 people): holes in the "whiteboard instead of pitch round" plan

**Verdict:** ⚠️ Don't drop the pitch round. Keep the whiteboard as a second surface. The "30-person" reason is a misreading, and the plan leaves no way to count who is still unteamed.

**Next action for you:** answer the 5 questions at the bottom. Then I'll lock the decision set section by section.

## Holes, worst first

1. ❌ **The 30-person rule is misread.**
   - The guide says "In a small event (up to about 30 people), you can have all of the participants introduce themselves."
   - That threshold governs *everyone introducing themselves*. The pitch round runs at any size.
   - At 140 people, only pitchers speak, at 1 minute each. The real scale problem is the number of pitchers, not the headcount.
   - The guide publishes no maximum number of pitches and no point at which to split the round. Any cap you set is your own figure.

2. ❌ **A board with no round is the weakest matchmaking option.**
   - The pitch round beats the board on coverage, project fit and effort.
   - The board reaches only people who walk past it. Its project text has nobody next to it to answer questions.
   - It still needs someone to keep it current all day.
   - "Browse whenever they like" means teams form at 10:00, 12:30 and 15:00. Time-to-first-commit becomes unpredictable, and the mechanic is supposed to finish before the first line of code.
   - The board has one legitimate use. It is the written output of the pitch round, so latecomers and the floor sweeper have something to point at.

3. ❌ **Letting people post ideas they won't build breaks the guide's own rule.**
   - The guide says: "Do not allow anyone to pitch an idea that they will not be working on... unless there really are not enough ideas to go around."
   - Joiners attach to a project with no author. Nobody answers their questions, and nobody coordinates teams of four or more.
   - "More ideas is better" is false here. It makes the board longer to read and leaves dead entries. Hackers in a 140-person room cannot tell which entries are live.
   - The exception only holds when ideas run short. With 140 people that is unlikely, and I don't know your pitcher count yet.
   - The supply you need is **joinable** ideas, not **more** ideas. A joinable project has ready-to-go tasks for newcomers and a build environment that starts in under 20 minutes. Anything weaker is, in the guide's words, "a line of text".

4. ❌ **There is no way to count who is still unteamed.**
   - The coverage gate needs a moment when the mechanic ends and a known number of people without a team.
   - A board open all day has no such moment. The sweeper has nothing to target and the escalation has no trigger.
   - The sweeper also needs to know which teams have room, and that means rosters written down when the mechanic ran.
   - Nobody owns this role in your plan. A named person is needed for the whole hacking window, not "whoever is free".

5. ⚠️ **The plan creates an expectation of being teamed and has no safety net.**
   - Announcing any mechanic means "solo is fine" no longer answers the person it failed.
   - The offer order is: a short-handed team, then a stocked project, then solo as a choice. Today you have none of the first two.

6. ⚠️ **Rolling formation collides with the change cut-off.**
   - If people form teams all day, you need a published wall-clock cut-off after the sweep and before judging opens.
   - Without it, the roster handed to judging and to prizes is not the roster that gets scored.
   - A freeze at the pitch round would stop the sweep placing anyone, because the team with room could no longer take them.

7. ⚠️ **Physical issues (my reasoning, not published practice).**
   - One whiteboard next to the coffee for 140 people is a queue.
   - Handwriting is hard to read and entries get erased or crowded out.
   - A free-form entry has no required fields. Use a template: lead's name, problem, skills or help needed, and whether it is open to newcomers. The guide's pitch content works as that template.

8. ⚠️ **No size rule is mentioned.**
   - Pick "Teams can be 1-4 people" or your own number, and publish it with the brief before registration closes.
   - 140 people means roughly 35 to 140 teams depending on the cap, and that sets your judging load.
   - Check the prize medium first if prizes are non-cash.

## What your plan gets right

- ✅ A written board is a **non-verbal route** into matchmaking. The pitch round assumes people are comfortable talking to strangers at volume.
- ✅ It handles latecomers and the shy better than speech alone.
- ✅ It can double as a way to enter an idea in writing. That makes it a real accessibility accommodation, not just a fallback.

## Recommended shape

Each item below is a draft until you confirm the answers to the questions at the end.

1. **Size rule:** "Teams can be 1-4 people." The number is yours to decide, and the guide's reason for it is one organizer network's observation with no study behind it. Hand it to `hackathon-brief-design`.
2. **Mechanic:** a pitch-and-join round, with the whiteboard run as its output and as a written entry route.
   - It runs straight after the welcome and before any hacking.
   - One minute per pitch, with a named person who cuts pitchers off. State the cut-off rule out loud first.
   - Only people who will build the project may pitch. This is stated before the round opens.
   - A pitcher sign-up sets the round's length. Duration is pitcher count × 1 minute plus handover. For example, 25 pitchers is about 25 minutes before overhead. That figure is illustrative and not a benchmark.
   - If pitchers are too many, run a written-entry-only tier for the overflow instead of a longer round. That cap is your own call.
   - Hand the duration and the ordering constraint to `event-run-of-show`.
3. **Board design:**
   - It has a template and two labelled zones. Zone one is "led by a person here" (from pitches). Zone two is "organizer-stocked, joinable" (curated, each entry meeting the 20-minute bar).
   - Unowned guest ideas do not go on the board by default. Allow them only if the pitch sign-up shows too few projects, and label them "needs a lead".
   - Add a second board or a digital mirror if the coffee spot becomes a queue.
4. **Unteamed protocol:**
   - A named floor sweeper for the whole window, rostered via `event-volunteers`.
   - The roster is captured as the round ends. This creates the count the coverage gate needs.
   - Sweep passes are anchored to the day's clock: end of the pitch round, first meal, first workshop break.
   - Offer order: short-handed team, stocked project, then solo as a choice.
   - Say "a project of one is okay too" at the opening.
   - Count the unteamed people but never roster them by name.
   - If minors take part, treat the sweep as a safeguarding interaction under the event's existing posture.
5. **Change policy:** open until a published cut-off, then frozen. The cut-off is a wall-clock time after the last sweep and before judging opens. Say what happens to a team that falls below a composition fraction, if any track has one.
6. **Pre-publication gate:** five items in writing with no blanks.
   - Size rule with its solo answer.
   - Composition fraction, if any.
   - Mechanic with its duration.
   - Named owner of the safety net.
   - Wall-clock change cut-off.
7. **Signals to record:** solo versus team registrations, unteamed count when the sweep ran, what each unteamed person did next, actual pitch-round length against budget, and membership changes after the cut-off. These are self-set measures. Do not borrow another event's numbers as targets.

## Questions I need answered (one at a time, in this order)

1. Is Harbourlight themed with organizer-supplied problems, open with participants bringing their own, or both? This sizes the project backlog.
2. How many of the 140 registered as an existing team, and how many alone? An estimate is fine, and "we don't collect it" is also a useful answer.
3. How many people are bringing a project, and is this a first-hackathon crowd? This sets the round length and whether an organizer-stocked backlog is needed.
4. Do you have a second room, and may minors attend? This decides whether a mixer is even possible and how the sweep is handled.
5. Who is actually free during the hacking window to sweep the room, as opposed to being nominally on the schedule? If nobody is, I'll say plainly that the sweep and escalation are removed.

Once these are answered I'll present each section for your approval, one at a time. Nothing goes into the brief until you approve it explicitly, because publication is the point of no return.