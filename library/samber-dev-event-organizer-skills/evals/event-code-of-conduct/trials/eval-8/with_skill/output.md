# HackUZH reporting design review

**Verdict: do not publish as written.** Each of your three privacy rules removes a part of the pipeline the skill treats as mandatory. Together they leave a published policy with no pipeline behind it, which is the failure the skill exists to prevent. The privacy goal is legitimate, and you can meet it by limiting what is kept, who sees it, and for how long. Banning records altogether does not meet it.

This is not legal advice. Retention and deletion rules for incident records belong to whoever holds the university's privacy obligations. The sponsor and recruiter clause belongs to counsel through `event-sponsor-agreement`. Anything involving a crime or an imminent threat goes to emergency services first.

## Why this event is the hard case

- Judges are professors who grade the reporters.
- Recruiters hold the internships the reporters want.
- The reporting population is 500 students under a power gradient, and that gradient runs in both directions.

The skill promotes the anonymous path in exactly this situation, and it lists "students at a university-hosted hackathon" and "sponsor booth staff" by name. Your design removes it.

## Findings

### 1. 🔴 Face-to-face only removes the channel this event needs most

- A student must give their name and face to an organizer and accuse a professor who grades them, or a recruiter who controls an internship. That is the reporter most likely to stay silent.
- It cannot take a report after the event. The skill's default is an email alias, an on-site responder, named alternates and an anonymous path. You keep one of those.
- It cannot take a report from the event chat or from the people who can't or won't speak in person (anxiety, disability, language, a 3am shift change).
- It has no route for a report about the organizer you would be speaking to. The skill requires at least two more named contacts, one outside the organizing chain.
- "An organizer" is unspecified. Who is it, and are they trained, visible and reachable overnight?

### 2. 🔴 "Nothing gets written down" is not possible, and it breaks four things

- **The policy contradicts itself.** It says nothing is written, then says notes are destroyed. Organizers will take notes on their phones anyway, uncontrolled, unless you design the notes.
- **There is no capture.** The runbook needs date, location, the reporter's words, the identity of the reported person, witnesses and a danger check. Without a record, the escalation to the response leads depends on memory.
- **Sanctions cannot be proven or appealed.** An ejection or ban with no written cause fails the "written notice stating exact cause" step. The appeal rung also needs evidence to review.
- **Closure cannot be audited.** You cannot show every reporter got a closing message, and you cannot produce the transparency report.

### 3. 🔴 Destroying notes at 48 hours cuts off the response before it ends

- PyCon's clock is 24 hours to meet and one week to follow up with the reporter. Aurora and Gardiner's is 24 hours to acknowledge and 10 business days to decide.
- A 48-hour destruction date falls before any of these clocks finish. A report made on day 2 is deleted before it can be decided, notified or appealed.
- You have not published a response clock at all. Publish one that fits inside the event, then set retention to outlast it.

### 4. 🔴 "No files on individuals across years" makes the ladder meaningless

- **Repeat offences:** rung 2 exists only because someone can check whether this is a repeat. A professor or recruiter reported in 2026 is a first offender again in 2027.
- **Bans:** a ban from future events is a record of an individual. You can publish the rung but cannot execute it.
- **Silent reset:** the people most likely to repeat are the ones who return every year, such as judges and sponsor recruiters.
- The skill is explicit here: "Safety outranks privacy: refusing to keep records... is privacy misapplied."

### 5. 🟠 No independent route, though the power gradient requires one

- The skill deletes the "single organizer as responder" option. It promotes an external trust-and-safety contractor when no independent body sits above the team.
- Here the likely respondents are university staff, and the accused may be their colleagues.
- Ask whether the university has an ombuds or harassment office to escalate to. Use it as the appeal body and as the route for reports naming a professor. Judges are university employees, so an internal procedure may already apply and may bind you.

### 6. 🟠 Scope is missing

The policy must name these explicitly:

- **Judges, mentors and professors:** they are bound by the policy, not exempt.
- **Sponsors and recruiter booth staff:** they are in scope but bound through the sponsor contract, which needs the compliance clause and the ejection-without-refund right.
- **Spaces:** the venue, overnight areas, transport, afterparties, unofficial gatherings and the event chat, with the dates the chat is in scope.
- **Conduct outside the event:** state your stance. For an event, admission is the lever, so act inside your spaces on outside evidence.

### 7. 🟠 Retaliation and conflicts of interest are unaddressed

- Add a recusal rule so a judge never scores a student who reported them, or a student they teach.
- Add a rule that recruiters cannot condition an internship on anything conduct-related. Add a no-retaliation promise to the policy.
- The recusal rule starts the moment a team member realizes it applies.

### 8. 🟠 No sanctions ladder, appeals or visible enforcement

- Publish the ladder before the first incident: warning, separation requirement, removal of privileges (including a judging or booth role), ejection, ban. Pair each rung with a community impact.
- State which rungs carry an appeal, to whom, in what form and by when. MLH allows appeals only for suspensions and bans.
- Everyone who knew about a violation must learn a response occurred, without details.

## Redesign that keeps your privacy goals

| Your rule | Keep the intent | Replace with |
|---|---|---|
| Face-to-face only | Reporters are not exposed in writing | Add three channels: visible on-site responders, a private alias, and an anonymous path. The reporter chooses how much identity to disclose. Never require it. |
| Nothing written | No casual notes on phones | Use one written intake form, minimal fields, a random case code, stored on a restricted device or account. Only the 3-6 team members can see it. A leak is grounds for removal from the team. |
| Delete at 48 hours | No indefinite narratives | Set a written retention rule that outlasts the clock and appeal window. Delete the narrative and evidence after it. Keep a minimal ledger. |
| No cross-year files | No dossiers on students | Keep only: case code, person identifier, rung, date, and ban or expiry date. Reporters are never recorded in the ledger. Reporter identity is never shared with the accused. |

The retention periods and the ledger design are for your privacy lead or counsel to set and approve. The ledger above is the minimum that lets rung 2 and bans work.

## Pre-publication checklist

1. Publish the response team: 3-6 named people, each with a contact. Include one person outside the organizing chain.
2. Put responders in visibly distinctive shirts and reserve a private room. Put its number on the responder card.
3. Publish a response clock that fits inside the event.
4. Name who holds public-statement authority.
5. Add the sponsor contract clause via `event-sponsor-agreement`.
6. Rehearse two or three cases before doors open, including one naming a judge and one naming a recruiter.
7. Commit to a transparency report: counts only, no identities, no narratives.

## Questions I need answered before the final policy

1. Is HackUZH an MLH member event? If so, MLH's policy and incidents process bind you, and your design is not yours to choose.
2. Who sits on the organizing team (students, staff, professors), and could any of them be the subject of a report?
3. Is this a one-off or annual? Annual points firmly to the ledger.
4. Does the university have an ombuds or harassment office you can route to or appeal to?
5. What is the publication deadline, and what is the effort ceiling (live staffing overnight, budget for an external contractor)?
6. Is there an existing values document or a prior edition's policy to adapt?

I'd recommend adapting an established text, such as MLH's, and adding the university escalation path.