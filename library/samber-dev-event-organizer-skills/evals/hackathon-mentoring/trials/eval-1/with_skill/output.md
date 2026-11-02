# Riverbend Build Days: mentor plan

## Short answer

I won't give you a number, because any mentors-per-hacker figure would be invented. The only published ratio (1 expert per about 4 non-experts, from `hackathon.guide`) doesn't apply to your event. It covers themed events only, counts non-expert participants rather than teams, and describes experts embedded in projects rather than floating mentors. Its purpose is project supply. All it tells you is that expertise is the scarce thing, not headcount.

Your mentor count comes from three steps:

1. List the expertise your teams actually need.
2. Set which of it must be on the floor, and in which hours.
3. Hand that constraint to the shift arithmetic in `event-volunteers`. That skill returns the headcount, because it owns shift length, arrival buffers and no-show allowance.

Your 340 registrations and 18 teams change the count only indirectly, through how many stacks they bring.

## What your situation changes

| Fact | Effect |
|---|---|
| Open theme, own projects | The sponsor and track fixed points are absent, so coverage units must come from your teams' stacks. |
| No sponsor technology | No sponsor track at required depth or deeper, so nothing is "guaranteed" by sponsor promise. "No mentor programme" stays a legal option on paper. |
| Two food sponsors | They are not a mentor source. Don't make staff a sponsorship deliverable. |
| 44 hours (Fri 18:00 to Sun 14:00), both nights | The overnight hours are the main design problem. |
| One room | The room is small enough to make a staffed area workable, so your request mechanic can be simple. |

I'd still run a programme. 340 hackers working through two nights with no route to help is the "blocked team abandons the build" scenario. The "none" rung fits events small enough that a programme isn't needed.

## Working it out, step by step

1. **Collect stack data first.** Add one field to registration, and refresh it at check-in because teams will have formed by then: "main language/framework, and anything you expect to get stuck on". This is your substitute for tracks.
2. **List coverage units.**
   - The general stack every team touches: version control, deployment, the 2 or 3 dominant languages.
   - One unit per stack cluster that shows up in the data. Pick a cutoff you can defend, for example "enough teams to matter". Don't build a unit for every one-off.
3. **Set a commitment level per unit.**
   - Dominant general stack: *guaranteed* for stated hours.
   - Every other cluster: *available*, meaning someone holding the tag is reachable through the request mechanic.
   - A cluster nobody covers: *unstaffed, published as such*.
4. **Decide the overnight hours explicitly.** Choose staffed, thinly staffed, or published as unstaffed, and publish whichever you choose. Don't let it default.
5. **Stagger specialties against when teams need them.** Teams in an open event usually need design and scoping help early, and debugging and deployment help from late Friday through Saturday. Presentation help matters in the final stretch.
6. **Hand the constraint over** as "this tag, present, these hours". `event-volunteers` then returns shift length, buffers and the headcount.

The headcount is the number of people needed to keep your guaranteed units present across the hours you chose to staff, plus the buffer and replacement allowance from `event-volunteers`. Cutting the staffed hours or the guaranteed units is the lever that lowers it.

## Design choices

**Coverage depth: rostered mentor shifts.** Recruiting plus a shift grid is a one-off cost and gives you named people who are there to help. "Expertise-matched roster" is promoted only for a required sponsor track or a one-domain themed event, so you don't meet its condition. Keep tags light anyway: one tag per coverage unit, with a depth of "has built with it" or "has read the docs", asked at sign-up. On-call from organizers is risky here because it sends every technical question to the people running the schedule, at the hours the schedule is hardest to run.

**Recruitment: community and alumni only.** The mixed pool is promoted only when the brief names sponsor technology, and yours names none. Use a warm-list ask, not an open call: local user groups, past participants, partner companies' engineers, maintainers of the libraries your teams use. If you ask someone from a food sponsor to mentor, treat them as an individual volunteer. Add the engagement rule (no pitching or recruiting) if they wear a company badge.

**Request mechanic.**
- Start with **identifiable mentors**: a marker plus a named role in your chat channel.
- Upgrade to a **staffed mentor area** if the mentor crew is larger than your organizing team.
- **Office hours** can supplement but never be the only route, because the event runs overnight.
- **Never route requests through one organizer's DMs.** That person will be asleep at the worst hour. Any routing needs at least two people who can work it.
- Publish the mechanic where teams read the brief, before 18:00 Friday, and repeat it at opening. State how to recognise a mentor, how to ask, what to expect, and what happens when nobody covers a skill.

**Mentor briefing: boundary stated.** Mentors explain, diagnose, unblock and demonstrate, but don't write code that ships. Anything shown in code goes in a scratch file outside the team's repo, and if a mentor has already committed, the team declares it. Every briefing also covers slot and location, how requests arrive, who to escalate non-technical issues to, and the code-of-conduct pointer. Upgrade to boundary plus scenario walkthrough if most mentors are first-timers or this event will recur, since you write it once and reuse it. If any prize carries cash value, "no briefing" is off the table.

**Rotation and interruption.**
- Take shift slots from mentors at sign-up. A slot is a commitment, and presence beyond it is a courtesy.
- Give each mentor a visit cadence for their slice of teams. You set the number for this event.
- Stop scheduled visits before the final stretch so teams get an uninterrupted run-in.
- If mentors roam, rate-limit them: a per-visit time cap, a team-controlled "do not disturb" signal, a published list of who knows what, and a shared view of blocked teams. With 340 people in one room, several mentors converging on whichever team pitched loudest is the likely failure.

**Uncovered skill route (publish it):**
1. Check the roster's "read the docs" level first.
2. Ask the room. Frame it as a request, never an assignment.
3. If still nobody, tell the team plainly and early enough that they can pivot.

**Contact log.** Keep a mentor-team log only if any mentor is also on the judge list. Hand it to `hackathon-judging` for recusal.

## Pass threshold

Before 18:00 Friday, these five must exist in writing with no blanks:

1. Expertise tags mapped to your coverage units.
2. Coverage commitment per unit, including the overnight decision.
3. The request mechanic as teams will read it.
4. The mentor briefing with its boundary sentence.
5. The route for a skill nobody covers.

During the event, record these self-set signals live: the longest-waiting requests and their stack, hours where a unit had no tagged mentor present, and requests that found nobody. Compare them only against your own next edition.

## Questions that would change this plan

1. Do any prizes carry cash value? That removes "no briefing" and may raise the briefing depth.
2. Is any mentor also a judge? If so, you need the contact log.
3. When must the roster close, and when must the request mechanic reach participants? A close date favors community and alumni only.
4. Who is already committed to mentor, and have they mentored before?
5. How many organizer hours do you have before the event, and will anyone coordinate mentors live? A low ceiling means the simple mechanic stays.
6. Do you have a last-edition list, a user group, or a university department that would send several people?
7. Will you publish the overnight hours as staffed, thin, or unstaffed?

Answer these one at a time and I'll fill in the coverage table and the roster constraint you hand to `event-volunteers`.