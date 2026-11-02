# TrailStack Conf lessons-learned log

**Edition:** TrailStack Conf, 400 attendees, single day
**Date of event:** Saturday 2026-10-10 (assumed from "ended Saturday")
**Log written:** 2026-10-14, 4 days after doors closed
**Status:** Draft built from raw team notes, not yet from a debrief session. The timeline is reconstructed from memory only.

## What I changed from your notes

- **Names became roles.** The log describes gaps and systems, not people. Priya and the AV technician appear only as roles. Priya's improvised fix is recorded as a practice that worked.
- **"Better volunteers" and "the AV guy kept screwing up" are not findings.** Neither has a mechanism, an owner or a date. Each is rewritten below.
- **Only registration gets a root-cause analysis.** The skill's rule is 5-Whys only when a finding:
  - recurs or would recur by default,
  - has a structural cost, and
  - has an obvious fix that treats the symptom.

  It also warns that 5-Whys on every entry buries the one finding that needs it. The other three get the standard three-part entry. I say below what would promote AV to a second 5-Whys.
- **Nothing is invented.** I don't know your arrival numbers, staffing counts, AV setup or tent contract. Those are marked as gaps to fill, not guessed.

## What went well

| # | What worked | What made it work | Preserve next edition |
|---|---|---|---|
| W1 | The registration queue was cleared quickly once two floor volunteers were pulled in at 09:15. | A decision-maker at the desk acted on the spot, with no approval chain. | Write the authority to reassign floor volunteers into the day-of runbook, so it doesn't depend on one person's judgment. Otherwise this is a bus-factor finding wearing a compliment. |
| W2 | The gluten-free count error was caught and fixed by 1pm. | Someone flagged it and catering responded the same day. | Name who flags dietary issues and which catering contact they call. Both are currently implicit. |

## Lessons-learned entries

### L1: Registration queue delayed the first talk (RCA below)

- **Category:** Nobody owned it, probably. See the RCA for the other candidate.
- **What happened:** The queue reached the building entrance, and the first talk started 10 minutes late.
- **In the moment:** At 09:15, two floor volunteers were pulled to the desk and the queue cleared. The notes don't say when, or what the floor looked like while they were away.
- **Next edition:** Size the desk against the arrival curve rather than headcount. Roster a named float role for the first hour. Set a hard rule that the first session doesn't start until the queue is below a stated length. Also add check-in tooling if the cause turns out to be the process (see RCA).
- **Owner:** Volunteer lead (name to confirm)
- **Due:** At roster build, 6 weeks before doors.
- **Routes to:** `event-run-of-show` (arrival curve, float role), `event-team-structure` (see TH1).

### L2: Microphone handoffs failed repeatedly in track B all afternoon

- **Category:** Checklist or review miss, or nobody owned it. Unconfirmed, see the open facts.
- **What happened:** Mic handoffs in track B were unreliable across the afternoon. They failed more than once, and the problem persisted rather than being fixed after the first failure.
- **In the moment:** Not recorded. Nothing in the notes says it was escalated or fixed.
- **Next edition:**
  1. Add a track-level AV checklist: handoff order, spare mics and batteries, and a named AV contact per room.
  2. Add a mid-day AV check-in at the lunch break.
  3. Brief speakers on the mic procedure before their slot.
  4. Add "track B AV" to the AV vendor debrief.
- **Owner:** AV lead (name to confirm)
- **Due:** AV vendor conversation within 2 weeks (2026-10-28). Checklist by the vendor contract signature.
- **Open facts to collect before closing this entry:**
  - Was the failure technical (hardware, batteries) or procedural (no handoff plan, a speaker-order change)?
  - Was it staffed and briefed?
  - Why did it persist all afternoon?
- **5-Whys trigger:** If the answer is "the same person held the AV for both tracks" or "no one had authority to stop and fix it", promote this to a second RCA.
- **Routes to:** `event-run-of-show`. If the AV person was a contractor, also `event-budget` (vendor fee and SLA).

### L3: Gluten-free lunch count was wrong

- **Category:** Checklist or review miss
- **What happened:** The gluten-free meal count didn't match actual need.
- **In the moment:** Flagged to catering and fixed by 1pm.
- **Next edition:** Send the catering order against the registration dietary field with a confirmation round-trip a few days before the event. Add a small buffer for walk-ups. Owner and date below.
- **Owner:** Catering lead (name to confirm)
- **Due:** At catering order, 2 weeks before doors.
- **No deeper analysis, by design.** The cost was contained, it was fixed the same day, and a 5-Whys here would crowd out L1.
- **Open fact:** Was the miss in the count sent to catering, or in the dietary data collected at registration? The fix differs.

### L4: Rain flooded the sponsor tent mid-morning

- **Category:** First-time failure mode, unless a weather risk was already on the register. In that case, known risk with no treatment.
- **What happened:** Rain flooded the sponsor tent mid-morning.
- **In the moment:** Nothing could be done during the event. This is a complete entry. An empty middle part doesn't mean the entry is unfinished.
- **Next edition:**
  - Add outdoor weather exposure to the risk register as a scored risk.
  - Require a wet-weather plan for any outdoor sponsor space: ground cover or raised flooring, drainage, an indoor fallback and a decision trigger.
  - Add a sponsor-contract clause on weather.
  - Confirm who tells sponsors, and when, if their space is lost.
- **Owner:** Sponsor and venue lead (name to confirm)
- **Due:** Before the next venue or tent contract is signed.
- **Routes to:** `event-risk-management` (new category), `event-budget` (any sponsor refund or goodwill cost).
- **Open fact:** "Nothing anyone could do" may be true on the day. It is not true at planning time. The decision to site sponsors outdoors with no fallback is the thing to examine.

## Root-cause analysis: L1, registration

I'm escalating this one because the kind of fix matters: "better volunteers" would not have prevented it. All causes below are hypotheses to test against your data, not conclusions.

1. **Why did the first talk start 10 minutes late?** Attendees were still queued at registration when the first session was due to start.
2. **Why was the queue still there?** Arrivals outpaced check-in throughput during the opening window. The queue reached the building entrance, so the shortfall was large, not marginal.
3. **Why did throughput fall short?** Probably the desk was staffed for the average arrival rate, not the peak. Single-day events usually have a sharp arrival spike before the first session. The notes don't say how many desk positions or scanners there were.
4. **Why was it staffed for the average?** Probably no one sized the desk against an expected arrival curve. It may also have been staffed from available volunteers rather than from demand. The notes suggest one person was handling it, which points to a role that was not scoped or backed up.
5. **Why did no one catch that before doors?** Probably no pre-event check existed (a dry run, a stated queue-length trigger, a named float role) and no one owned the registration plan end to end.

**Root cause (hypothesis):** Registration capacity was not sized against the arrival peak, and the role had no backup or escalation trigger. "Better volunteers" does not address either. Better volunteers at the same desk size would still queue.

**What to test before accepting this:**
- Badge-scan or ticket-scan timestamps give the real arrival curve. Pull them.
- How many positions were staffed, and were all of them working?
- Was the slowdown at the desk itself (printing, lookups, name-matching) or just arrival volume?
- Did the first-session start time have a hold rule, or did it start on schedule regardless?

**Correction to the obvious fix:** The corrective actions are in L1 above. They are capacity sizing, a float role, a hold rule and a dry run. None is "recruit better."

## Reconciliations (handed back, not redesigned)

I can only run the checks for which you hold documents.

| Check | Status | What to do |
|---|---|---|
| **Risk register** | I haven't seen one. | Bucket each item as fired-and-held, fired-and-failed or fired-and-unscored. Rain is probably unscored. Registration surge and AV handoff may be either unscored or known with no treatment. Hand back to `event-risk-management`. |
| **Budget** | Not provided. | Likely variances to look for are the AV vendor cost, any sponsor refund or goodwill for the flooded tent, and catering corrections. Hand the variance table to `event-budget`. |
| **Run of show** | Partial. | Divergences: first talk +10 min, track B afternoon AV, tent loss mid-morning. Hand to `event-run-of-show`. |
| **Goals** | No written pre-event goals in your notes. | If none existed, any goal review is reconstructed, not measured. Say so in the log. Pass any sponsor-renewal risk from the tent to `event-market-fit` as a signal only. |

## Team-health findings (routed, not solved)

Phrased structurally, as the skill requires:

- **TH1:** The registration role appears to have had no backup and no staffing trigger. One person absorbed the first-hour peak. Route to `event-team-structure`.
- **TH2:** Track-level AV ownership and escalation are unclear in the notes. Route to `event-team-structure` and `event-run-of-show`.
- **Check in privately.** The note says one person was overwhelmed. Ask how they are doing and whether the workload was sized. That is a conversation, not a log line.
- **Team energy:** I don't know the team's state. Ask it plainly before scheduling the session. An exhausted team is the first finding.

## Action items

| ID | Action | Owner | Due |
|---|---|---|---|
| L1 | Size the desk against the arrival curve, name a float role, add a first-session hold rule | Volunteer lead | At roster build, 6 weeks before doors |
| L2 | AV vendor conversation, track checklist, mid-day AV check | AV lead | Vendor call by 2026-10-28 |
| L3 | Dietary confirmation round-trip with catering | Catering lead | 2 weeks before doors |
| L4 | Add weather risk, wet-weather plan, sponsor clause | Sponsor and venue lead | Before the next venue contract |
| W1 | Write the reassignment authority into the runbook | Run-of-show owner | At runbook draft |
| TH1 | Registration-role backup finding to team-structure | Debrief facilitator | 2026-10-21 |

**Zero-orphan test:** Not yet passed. Every entry has a role and a date, but the skill requires a named person. Replace each "(name to confirm)" with an actual person in the session. Until then this is a log in progress, not a finished one.

## Publication posture

- **Recommended default:** Recap plus retrospective, if the event is public.
- **Check first:** Whether any finding names a venue, caterer or AV vendor that could collide with a contract clause. L2 and L3 are the most exposed. Keep vendor names out of anything public.
- **Not recommended:** A transparency report, unless code-of-conduct reports were received. You haven't said whether any were.
- **Decision:** The team makes it in the session, not as homework.

## Handover

- The dated log goes to `event-continuous-improvement`, with no cross-edition comparison in it.
- The risk buckets go to `event-risk-management`.
- The variance table goes to `event-budget`.
- The run-of-show divergences go to `event-run-of-show`.
- The structural findings go to `event-team-structure`.
- Open items go to `event-planning-timeline` once next edition's plan opens.

## Questions I need answered to finish this

1. **Who held each named role, and who can be in the room?** Include the registration lead, the AV lead and the sponsor lead.
2. **Did you write goals before the event?**
3. **What do you hold in hand?** Check the risk register, planned budget and run of show.
4. **When does next edition's planning start?** That is this log's deadline.
5. **Is this a recurring event, and is it volunteer-run or staffed?**
6. **Were any code-of-conduct reports received?**
7. **Is it public?** This decides the publication posture.

## Measurement to record

- **Days from doors closing to debrief:** 4 so far. Record the actual date when it happens.
- **Named-role coverage:** to be filled in after the session.
- **Carry-through rate:** not applicable until edition two.