# Shift handoff protocol

The on-duty rotation itself is published practice. DevOpsDays' organizing guide says: "Consider assigning 'on duty' shifts so one person isn't the SPOF for all last-minute decision-making in crisis mode" (`devopsdays/devopsdays-web`, `content/page/organizing.md`). The handoff structure below is borrowed from on-call incident-response practice and adapted to a conference day.

Carry the structure. Never carry its tooling, its domain or its timing figures as an events benchmark, and when you hand a handoff format to a team, say it is borrowed from incident-response practice rather than implying an events-industry norm.

## What carries over

### 1. An overlap window, not an instant switch

The outgoing person does not stop when the incoming person starts. Budget a short window with two distinct phases: one to write the handoff down, one to talk through it. Splitting the window matters more than its length - writing first forces the outgoing person to notice what they know and have not said, and the conversation then covers the gaps rather than reconstructing everything verbally.

Set your own window length. The source's figures are for a different domain and different stakes; borrowing them would dress a guess as a benchmark.

### 2. A checklist gate with a mandatory-entry rule

Fix the sections a handoff must cover, then apply the rule that makes the checklist work: **no handoff is complete until every section has an entry or an explicit "none"**.

The explicit "none" is the load-bearing detail, and it is the whole reason it carries over well. It distinguishes _nothing to report_ from _nobody checked_ - indistinguishable on a rushed sheet, and precisely the ambiguity a day-of handoff invites when two people are standing in a corridor and one of them is already late for something.

Sections worth fixing for an event on-duty handoff, adapted rather than copied from the source's own list:

- **Open problems** - anything unresolved right now, with who is already on it.
- **Sessions or segments running off-plan** - over-running, moved, or cut, and what the printed sheet now gets wrong.
- **People** - who is missing, late, unwell, or has left; who has been on their feet for six hours.
- **Venue and tech** - anything that broke and is being worked around rather than fixed.
- **Decisions already taken** this block that the next person would otherwise re-take.
- **Coming up in the next block** - the fixed points and the known risks in them.

Six sections, each with an entry or "none". A handoff that fits on one screen is one people will actually complete.

### 3. A separate template for handing off mid-incident

A routine handoff and a handoff during a live problem are different documents. The incoming person inheriting an active situation, such as a room already half-evacuated, a keynote speaker already forty minutes out, or an escalation already with the venue, needs a denser, narrower brief than a clean end-of-block one. That brief covers what is happening, what has already been tried, who is already involved and reachable, what decision is pending, and what the deadline on that decision is.

The failure this prevents is specific: a routine template used mid-incident produces a tidy summary of a day that is no longer the point, and buries the one decision the incoming person has to make in the next ten minutes.

Where possible, do not hand off mid-incident at all - hold the boundary until the situation closes. Where that is impossible, use the denser template and keep the outgoing person reachable past the end of their shift.

### 4. Live verification before the outgoing person leaves

The source's own mechanic is firing a test alert and confirming the incoming person receives it before the overlap window ends. The equivalent here is direct and cheap: **confirm the incoming person can actually reach and be reached on the coordination channel, live, before the outgoing person walks away.** Not a verbal assurance that they have it.

Three things look identical to a working setup right up until the first escalation:

- A radio with a flat battery.
- An app whose notifications are muted.
- A channel nobody added them to.

One message sent and answered while both people are standing there catches all three.

### 5. An async fallback for when there is no overlap

Where the outgoing person has already left - an early-morning-only volunteer, an overnight-to-morning changeover - fall back to a written quick handoff plus a short recorded walkthrough, and name someone reachable who was there. This is the source's own timezone-gap solution and it maps cleanly onto a shift boundary nobody is present for.

Treat the async path as the exception it is. A rota where several boundaries have no overlap is a rota problem, not a handoff problem, and it belongs back with whoever built the shift plan.

## What does not carry over

Do not carry any of this across:

- **The source's tooling** - alerting platforms, chat integrations, deployment and configuration-change tracking. None of it has an events equivalent, and naming it makes the borrowing look like a fit when it is an analogy.
- **The source's timing figures.** Its overlap-window numbers are calibrated to incident response, not to a conference corridor. Set your own and say they are yours.
- **Its postmortem apparatus** and the sibling-skill chain it links into. An event's equivalent is the closeout capture and the retrospective, which are shaped by different questions.
- **The framing that a shift boundary is a risk to be minimized.** In on-call it often is. At an event the rotation exists for the opposite reason - the sourced justification is spreading crisis decisions across people so no one person is the single point of failure, which means the boundary is doing wanted work, not tolerated damage.

That last difference is the one to keep in view when adapting anything else from the same source.
