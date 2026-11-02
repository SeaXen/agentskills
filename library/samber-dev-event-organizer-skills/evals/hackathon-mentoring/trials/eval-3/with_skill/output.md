# Mentor plan: Meridian Hack Weekend (40 teams, Fri night to Sun noon)

You asked for a quick answer, so I skipped the interview. I made assumptions where I had to and listed them at the end. Each one could change a rung.

## 1. Decision: keep both people in both roles

Put in a recusal rule and a contact log. Both are standard for this case.

- **Rule:** a mentor who materially helped a team recuses from judging that team. The hackathon-judging skill owns this rule and its recusal mechanics, so reference that skill and don't write a competing ladder.
- **Log:** the mentoring side owns the input data, a mentor-team contact log. The rule needs that list of "every team that person mentored", and the log is where it comes from.
- **Disclosure:** publish in the rules or brief, before submissions close, that two mentors also judge and recuse from teams they helped. Disclosed in advance, it's a rule. Found at the ceremony, it's a scandal.

## 2. Shrink the conflict instead of only managing it

The two infrastructure experts are needed both as mentors and as judges for the infrastructure track. Left alone, every infra team they help loses that judge. These steps keep that loss small.

1. **Split ownership of the infra track.** Assign each expert half of the infra teams as the named mentor. For any infra team, at most one expert is recused, so the other can still judge it. Say this on the request mechanic by name: "infra requests for teams 1–N go to A, teams N+1 onward go to B."
2. **Treat cover as a trade-off.** When the owner is off shift, the other expert covers. A cover visit that turns into real work makes the team conflicted for both. Prefer a second-level mentor (someone who has read the docs) for cover, and tell the team which level they're getting.
3. **Add second-level infra coverage.** Tag any volunteer who has used the stack as "has built with it" or "has read the docs", and ask at sign-up. Two experts don't cover a window running through the night.
4. **Stop scheduled visits before the final stretch.** The experts get an uninterrupted run-in, and so do the teams. They also need rest. A judge who has been awake for 36 hours scores badly.
5. **Keep mentor actions out of the repos.** The help-versus-build boundary below means no mentor commits land in a team's repository.

## 3. Mentor-team contact log

- **Who logs:** the two dual-role people log every visit themselves. Other mentors log too if it costs little, because the log doubles as the shared view of which teams are blocked. That view stops mentors clustering on one team.
- **Fields per entry:** team, mentor, start and end time, topic, and whether any code was touched or committed.
- **"Meaningful time":** your event sets this threshold, and it is not an industry standard. Write it down before Friday. Example: any visit beyond a quick answer, or any visit where the mentor touched the team's design or code.
- **Borderline cases:** recuse. Reassigning a judge costs little while no result exists yet.
- **Freeze and hand over:** freeze the log at Sunday noon and give it to whoever builds the judging allocation map. The map is built after the freeze, never before.
- **Cross-check:** teams declare any mentor commit in their submission. Compare that declaration against the log.

## 4. Judging side (rules owned by hackathon-judging)

- Treat the two experts as having reduced reach. Each is excluded from the teams they mentored.
- Run the feasibility gate with the recusals subtracted: `k = floor((J × W) / (N × t))`. It needs your judging window `W`, the demo contact time `t`, and `N = 40`. I don't have `W` or `t`, so I didn't compute it.
- Name a fallback for a team that loses too many judges to recusal, so its scores stay comparable. Check this for the infra track first.
- Never fix a short window by shortening `t` on the day. That re-scores whichever teams were seen first.

## 5. Mentor roster and coverage

- **Coverage units:** one per challenge track, one per named sponsor technology, and one for the general stack. I haven't seen your brief, so list them from it.
- **Infra track:** set it to *guaranteed*, meaning a tagged person is present for stated hours. Tag in the brief's own words, and name sponsor products explicitly and separately from the general skill.
- **Hand the constraint to the shift plan** (event-volunteers skill): "this tag, present, these hours." Don't rebuild the shift grid here.
- **Staggering:** don't roster both experts at the same hours. Cover the hours when infra work is heaviest.
- **Overnight (Fri night to Sat morning):** decide whether it's staffed, thinly staffed, or published as unstaffed, then publish that choice. I'd recommend thin staffing: one expert on call, the other asleep, with the second-level mentor on the floor.
- **Slots:** take each person's slot from them at sign-up. A slot is a commitment. Presence beyond it is a courtesy that can't be scheduled against.

## 6. Request mechanic (publish before Friday opens)

- **Default:** identifiable mentors with a marker and a named role in the event channels. This is the cheapest real step.
- **Add for infra:** a request channel with routing, because a named person has to be reached. It needs at least two people able to route requests. Never use one organizer's DMs, because that person will be asleep at 3am.
- **Don't use office hours as the only route.** The window runs overnight.
- **Publish four things:** how to recognise a mentor, how to ask, what to expect, and what happens when nobody covers the need.
- **Mark the two dual-role people** as "also a judge, recuses from teams they help." Add a line telling them not to evaluate anyone's project.

## 7. Mentor briefing (name it "mentor briefing" to avoid confusion with the jury briefing)

- **Logistics:** where to be and when, how requests arrive, and who to escalate to. Include the code-of-conduct escalation pointer. The event-code-of-conduct skill owns the script.
- **Boundary:** mentors explain, diagnose, unblock and demonstrate, and they do not write code that ships in a submission. Anything shown in code goes in a scratch file or on a whiteboard, and the team types the version that lands. If a mentor has already committed to a repo, the team declares it in the submission.
- **Power dynamics:** ask before touching a laptop. Leave the project unevaluated. This matters most for the two judges, because a team will read their opinion as a verdict. Say out loud what you don't know.
- **Rung:** use boundary stated. Upgrade to boundary plus a scenario walkthrough if most mentors are new, sponsor staff are mentoring on their employer's code, or this event recurs.
- **Add** a one-paragraph engagement rule if any sponsor staff mentor (no pitching, no recruiting). Put the same term into the sponsor agreement.
- **Drop "no briefing"** if any prize has cash value. A mentor's unbriefed commit then becomes an eligibility question.

## 8. When no mentor covers a skill

Publish this route before the window opens:

1. Check second-level mentors first.
2. Ask the sponsor's channel.
3. Ask the room. It's a request only, never an assignment.
4. If nobody can help, tell the team plainly and early. A team told at hour 4 can pivot, but one told at hour 30 can't.

Log each gap against its track.

## 9. Interruption control

Mentors will roam, so rate-limit it:

- A per-visit time cap.
- A do-not-disturb signal each team controls.
- A published list of what each mentor knows.
- A shared view of who has visited whom.

The failure to watch for is several mentors on one team while another team goes untouched for hours.

## 10. Pass check before Friday opens

All five of these must exist in writing, with zero blanks:

- [ ] Expertise tags mapped to the tracks.
- [ ] A coverage commitment per track, with the infra hours stated.
- [ ] The request mechanic as teams will read it.
- [ ] The mentor briefing, including the boundary sentence.
- [ ] The escalation route for an uncovered skill.

Also decide the log and its recusal link: threshold defined, log owner named, freeze time Sunday noon, handed to the judging allocation owner.

## Assumptions and open questions

- Do you have cash prizes or a sponsor-funded prize? If so, the recusal and disclosure steps above matter even more.
- Do any sponsor staff mentor? If so, add the engagement rule and a sponsor-agreement term.
- What are your tracks? I assumed one infrastructure track plus general ones.
- What are `W` and `t` for judging? The gate needs them.
- Are the two experts the only people who know the infra track, or are others at second level? I assumed some second-level volunteers exist.
- Is one organizer assigned to route requests overnight? I assumed two people can work the routing.
- Are the rungs above right for your size? 40 teams in one or two rooms suggests a staffed mentor area plus the infra routing channel, but that depends on your space.