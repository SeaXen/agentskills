# São Paulo Kubernetes Meetup — Program Review & Plan

## The direct answer: don't build the points system

A leaderboard is the wrong tool here, and it's worth saying why before handing you a plan that replaces it.

**Your board is treating a normal distribution as a problem.** Jakob Nielsen's participation-inequality data (2006, sourced) says roughly 90% of any community lurks, 9% contribute occasionally, and 1% produces most of the activity. Forty-to-fifty-five people showing up monthly, for a year, with four people running the room, is not a broken funnel — it's close to what a healthy group looks like at this stage. The lever isn't "convert the lurkers." It's lowering the barrier to the *next rung* for the slice of that 90% who are already one nudge away from it.

**Specifically on points/badges/leaderboard:**

- It rewards the wrong behavior. A three-in-a-row badge measures passive attendance, not the thing you actually need — someone taking a lightning slot, working the door, or reviewing a talk submission. You can get a maxed-out leaderboard with zero new organizers.
- It costs the scarcest resource you have. Someone has to build the site feature, track attendance accurately, and keep it current forever. That's more standing work for the same four people who are already the bottleneck — the thing this plan needs to fix, not add to.
- No program this skill drew on runs one. CNCF Community Groups, DevOpsDays, HashiCorp User Groups — all sourced, all long-running, none gamify attendance. Their retention mechanic is a person asking another person directly, and handing over a real piece of ownership. That's a stronger signal than an absence of counter-examples proves it's *wrong*, but it's a strong hint that the organizers who've kept rooms alive for decades didn't reach for this tool.
- It can work against you. A public "who's been here the most" ranking reads as an in-group scoreboard to a first-timer. It rewards people who already feel ownership and does nothing for the people you're trying to move.

**The actual finding underneath your question:** the risk in this group isn't the 45 people who eat and leave. It's that exactly one person outside your door team ever speaks, and nobody besides you appears to run the program itself. That's this skill's "founder-shaped group" failure mode — *one person owns the listing, the room, and every decision* — even though your headcount looks nothing like a dying group. A points system for attendees doesn't touch that risk at all. Below is what does.

I answered your seven gating questions from what's in your message and flagged every place I filled a gap with an assumption rather than a fact — confirm or correct these before you act on the plan:

| # | Question | What I used |
|---|---|---|
| 1 | New or existing | Existing, ~12 editions, attendance flat-healthy at 40-55 for a year — **not declining, so this is a depth problem, not a rescue** |
| 2 | Room | Kubernetes practitioners; assumed mixed seniority, mostly attending on their own time — **confirm: work-time attendance changes the promotion checklist** |
| 3 | Host model | Assumed **independent, vendor-neutral** given "my board" reads as an organizing committee, not a company. If a company or CNCF chapter structure actually owns this, say so — it changes who can veto a program decision |
| 4 | Success in a year | Inferred as "a self-sustaining organizer bench," since that's what your board actually asked for | 
| 5 | Fixed date pressure | None stated — treated as an open horizon |
| 6 | One evening vs. multi-year | You're a year in and your board is planning ahead — treated as a **two-year mandate** |
| 7 | Organizer ceiling | 4 people total, but only 1 (you) appears to hold program decisions; 2 hold one narrow area (door); 1 holds only speaking — **treated as an effectively solo-run program for planning purposes** |
| 8 | City / headcount / venue | São Paulo, 40-55, venue access already exists (1 year running) |
| 9 | Budget | Unstated — assumed in-kind (food + room), the meetup-scale norm |
| 10 | Channels | Unstated — flagged as a gap in the charter below |
| 11 | Two speakers today | You have one reliable one, not two — this is the second real risk, addressed in the pipeline section |
| 12 | Fixed constraints | Kubernetes topic, monthly cadence already running |

Two of the seven answers move the plan directly: the two-year mandate (Q6) rules out cosmetic fixes and points at building a real speaker/organizer pipeline; the near-solo organizer ceiling (Q7) rules out anything that adds standing work — including the leaderboard — until that's fixed.

---

## Program charter

```markdown
# São Paulo Kubernetes Meetup

**Room:** Kubernetes practitioners, mixed seniority, attending on their own time (confirm)
**Host model:** Independent, vendor-neutral community group, run by a small organizing board (confirm - if a company or CNCF chapter formally owns this, name it)
**Purpose:** Build a self-sustaining organizer and speaker bench, so the program survives any one person stepping back — named as the one outcome for this year, not "grow attendance" (attendance is already healthy)
**Format:** Anchor + lightning (one 25-min talk, plus 2-3 five-minute slots); fallback is a study group / hands-on session working through a CNCF or CNCF-adjacent spec, needing no confirmed speaker
**Rhythm:** Fixed monthly slot, evening, day TBD - confirm and hold it (a repeatable slot beats date-shopping every month)
**Program decisions:** Currently one person (you). Target: two organizers reviewing every proposal's title, takeaway, and slides against one test - "could someone with no stake in a vendor's product give this talk?"
**Organizers:** You (program - today); door duo (recruit one into a named role: speaker sourcing or comms); regular speaker (recruit into program, not just delivery)
**Venue:** Confirm current host and how long it's booked
**Money:** Assumed in-kind (room + food); confirm who signs for it
**We don't:** sell speaking slots, share the attendee list, let a sponsor run past a stated stage-time cap
**Accounts:** Confirm who besides you can access the listing, the mailing list, and any social account - this is the single biggest exposure right now
```

The purpose line matters most here: naming "self-sustaining bench" instead of "grow attendance" is what makes the rest of this plan the right one instead of a bigger, better-decorated version of the same four-person show.

---

## Edition plan — three editions out

| Edition | Date (illustrative) | Format | Speaker status | Venue | Sponsor | Promotion |
|---|---|---|---|---|---|---|
| N+1 | Tue 13 Oct | Anchor + lightning | Confirmed: regular speaker (anchor). **Open**: 2 lightning slots — direct-ask 3 named regulars this week | Current host, confirm through edition N+3 | None needed at this scale | Announce 3-4 weeks out leading with the anchor talk's topic, not the venue |
| N+2 | Tue 10 Nov | Anchor + lightning | **Provisional**: harvest a speaker from a recent regional K8s/CNCF event (ask while their talk is still fresh) | Same | — | Include an open CFP link in every announcement from N+1 onward |
| N+3 | Tue 8 Dec | Fallback: study group / spec walkthrough | n/a — no external speaker needed, protects December against cancellations | Same | — | Frame as "no talks in December, come work through \<a CNCF project's docs/spec\> with us" |

Two editions confirmed ahead is this skill's health line for a speaker pipeline; you're currently at less than one (a single informal volunteer with no backup), so the real near-term work is filling N+1's lightning slots and locking N+2's speaker before either date arrives.

---

## Speaker pipeline board

| Date | Format | Speaker 1 | Speaker 2 (lightning) | Status | Slides received |
|---|---|---|---|---|---|
| 13 Oct | Anchor + lightning | Confirmed — regular speaker | 2 open — direct-ask, not open call | Venue confirmed | No |
| 10 Nov | Anchor + lightning | Provisional — conference-harvest candidate | 1 open | Venue confirmed | No |
| 8 Dec | Study group | n/a | n/a | Fallback, no speaker needed | n/a |

Sourcing order to work, ranked by yield: (1) ask three specific regulars by name for a 5-minute slot — an open call only reaches people who already think of themselves as speakers; (2) open a standing CFP link, live on every announcement, not a monthly scramble; (3) watch for anyone from the room speaking at a regional K8s/CNCF/cloud-native event and ask them to repeat it locally that same week; (4) trade speakers with a neighboring city's cloud-native or DevOps group.

---

## Edition log skeleton

Fill this the night of every edition — the trend across rows is the signal, one row tells you about the weather:

| # | Date | Format | Speakers | RSVP | Door | Repeat % | New faces | Notes |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

You have a year of history with no log — reconstruct the last three editions' door counts from memory or RSVP exports if you can, so the scorecard below starts with real numbers instead of "not measured yet" across the board.

---

## Scorecard baseline

| Signal | Target | Current | Basis |
|---|---|---|---|
| Attendance at the door | Stable or rising over 3 editions | 40-55, stable for ~12 editions — **already passing** | Baseline (this skill) |
| Show-up rate (attended ÷ RSVP) | ≈70% | Not measured yet | Arithmetic on CNCF's ~30% no-show figure |
| Repeat attendance | ≥40% | Not measured yet — **this is the number that actually tells you if the same people keep coming or if it's fresh churn every month** | Baseline |
| New faces per edition | >0 | Not measured yet | Baseline |
| Speakers sourced from the room | ≥1 in 3 | 0 confirmed — every edition currently runs on one person outside the room's own bench | Baseline |
| Editions confirmed ahead | ≥2 | <1 | Baseline |
| Organizer count / employer spread | ≥2 people, ≥2 employers | 4 people, but 1 effective program organizer | CNCF |
| Gap since last edition | ≤90 days | Passing (monthly) | CNCF |
| Attendees per edition | >10 | Passing, well above bar | CNCF |

### Pass-threshold check against what you told me

1. No gap over 90 days, ≥6 editions/year — **pass**.
2. At least two editions have confirmed speakers — **fail**. You have one informal volunteer and no visible pipeline.
3. Door attendance stable/rising, above 10 — **pass**, comfortably.
4. Repeat attendance ≥40% with new faces every edition — **not measured**. Start logging this edition.
5. At least two organizers from at least two employers, shared account access — **fail on substance**. Four warm bodies, one decision-maker, and account access concentrated in one person is exactly the exposure that ends a program the month that person can't show up.
6. No sponsor overran its cap / no unplanned pitch — **not applicable yet**, revisit once you take on your first sponsor.

Two of six failing, on the two lines that predict whether this program exists in eighteen months. That's where I'd spend the board's attention — not on a leaderboard for the audience, but on turning your door duo and your regular speaker into actual co-organizers with named ownership, and getting a second and third speaker into the pipeline before either failing line becomes a missed edition.

### What I'd tell the board, in order

1. Recruit a real co-organizer from the door duo or the regular speaker within the next two editions — give them one named area (speaker sourcing or comms), not just more door duty.
2. Open a standing CFP and start direct-asking three named regulars for lightning slots this month.
3. Formalize anchor + lightning as the default format — it's the one that manufactures next year's speakers out of this year's audience, and it fits the pattern you already have informally.
4. Log door count, repeat rate, and new faces starting this edition. You can't tell a healthy plateau from quiet decline without it.
5. If the board wants a visible recognition gesture, use a stage shout-out and a name on a "who spoke / who volunteered" page — recognition tied to a contribution, not a badge tied to a headcount. It costs nothing to maintain and it points at the behavior you actually want more of.
6. Shared account access for the listing and any socials, this month, regardless of anything else on this list — it's the one item on here that's cheap to fix and catastrophic to leave.