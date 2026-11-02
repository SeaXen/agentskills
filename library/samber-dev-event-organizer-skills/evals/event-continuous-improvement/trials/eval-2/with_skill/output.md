# DevHarbor Conf: what the three editions support changing

## Bottom line

Your record supports **one operational change: check-in**. It does not show that retention is an operational problem.

- **Check-in:** about 90 minutes in 3 of 3 editions. That is a pattern, not a candidate, and it is ours to fix.
- **Retention (45% → 30%) and two sponsor non-renewals:** these are demand signals. They belong to `event-market-fit`, which gets them as evidence below.
- **Check-in is not proven to cause the drop.** It was about 90 minutes in all three editions. A constant can't explain a change from 45% to 30%.
- Fixing check-in is still worth doing: it is cheap, reversible and worth doing even if retention turns out to have other causes. Don't tell the team it will bring people back.

I did not run the full interview, because you asked for a one-shot answer. The open questions are at the end, with what each would change. Everything here rests on three editions of records, which caps every claim at that evidence.

## What the numbers say

All derived figures are computed from your numbers.

| Edition | Attendees | Returning from previous edition | New attendees |
|---|---|---|---|
| Year 1 | 610 | n/a | n/a |
| Year 2 | 580 | 45% of 610, about 275 | about 305 |
| Year 3 | 495 | 30% of 580, 174 | about 321 |

- New-attendee inflow is roughly flat, at about 305 and then 321.
- The shrinkage comes entirely from fewer returners.
- That makes this a **return-rate** problem, which is demand. An operational fix aimed at the wrong target would give you a smooth event for an audience that has stopped coming.

## Filed entries

| Entry | Gate result | Theme | Count | Label |
|---|---|---|---|---|
| Check-in about 90 min | Passes all three: current, reproducible, generalizing | check-in throughput | **3 of 3 editions** | **pattern** |
| Return rate 45% → 30% | Passes, but it is demand, not operations | not ours | 2 data points | candidate, routed to `event-market-fit` |
| Two sponsors declined to renew | Same | not ours | 1 edition | entry, routed to `event-market-fit` |

I can't file anything else, because I only have the check-in line from your retro notes. No other entry has been through the gate.

**Condition line for the check-in entry.** I don't know why check-in is slow, so this is a gap, not a diagnosis. The retro notes should say which of these applies:

- one station
- badges printed on the spot
- network or ticketing problems
- staffing

If they only say "90 minutes", that is itself a finding: the debrief didn't capture the cause. Don't reconstruct it from memory; ask whoever ran the desk. Also pin down what "90 minutes" measures. It could be the queue window or the wait per person, and the fix differs.

## Deliberate change for next edition

Only one change per edition, so next year's outcome can be attributed.

```
CR-1  Cut check-in throughput constraint
Evidence:   check-in throughput, pattern, 3 of 3 editions (about 90 min each)
Change:     [pick after the condition line is known]
              - single station or on-site printing: pre-print badges and add a
                second station with a printed attendee list as offline fallback
              - network or tooling: offline list plus scan app that works without wifi
              - staffing: sized rota with a documented fallback owner
Because:    the 90 min recurred unchanged, so nothing in the current setup fixes it
Check:      longest observed wait <= 20 min at peak, timed by a named observer
            sampling every 15 min during the peak hour, observed at the door,
            not surveyed. The 20-minute bar is a self-set threshold, not a standard.
Routed to:  event-planning-timeline, as a task on next edition's plan
Outcome:    <fill at the closure pass, after next edition>
```

Record the return rate beside the check-in result for next edition. That is a paired read for `event-market-fit` to weigh. It is not a causal test.

## Routing hand-offs

I hand over evidence, not conclusions. The `event-market-fit` observation below is the one that matters most.

- **`event-market-fit`:**
  - Return rate was 45% then 30%, a 2-point series, so it is a candidate.
  - New-attendee inflow is flat at about 305 and 321.
  - Two sponsors declined to renew in year 3.
  - Check-in was about 90 min in all three editions. This is an observation, not a causal claim.
  - The retention and sponsor questions are theirs to answer. Possible causes include programme, price, audience fit and sponsor ROI.
- **`event-planning-timeline`:** CR-1 as a task. Needs the edition, an owner and the decision date in the work-back plan.
- **`event-growth-strategy`:** nothing yet. If the check-in cause turns out to be a capacity ceiling, I'd hand over that ceiling and the evidence.
- **`event-team-structure`:** nothing yet. The same would apply if the cause is a one-person desk.
- **`event-vendor-sourcing`:** only if the cause is a badge-printing or ticketing supplier. Then it becomes a rebook-or-not verdict on that vendor's own record.

## Persistence and audit

- **Persistence:** an appended document, one running dated document with a heading per edition. You hold three editions of records, so this default applies from edition two onward. It is cheap and survives turnover. Promote to a structured entry record if the team turns over a lot.
- **Trend detection:** theme grouping, counted by edition rather than by entry.
- **Audit:** a kickoff pass before planning opens. Classify every entry as Keep, Update, Consolidate, Replace or Delete, and finish it in one sitting. Add a closure pass after the edition ships, using the CR-1 record. Append two columns: did this improve, yes or no, and why.
- **Name a person.** One named person must open the log before planning kickoff. "The team" is how a log goes unread.
- **De-personalise before persisting.** Write conditions, not names. For example, "single station with no fallback", not "X forgot".
- **Log ownership:** the persisted log is itself a bus-factor mitigation. Tell the team that.

## Open interview questions

These change the rankings above if answered differently.

1. **Records:** are the retro notes in the three-part debrief form, with an owner and a date? Are there other findings? Right now I've filed one entry.
2. **Turnover (Q3):** how much of the team has changed? A full rotation would promote the structured record and the written trend review.
3. **Planning start (Q5):** when is the go/no-go for next year? That date is the deadline for CR-1.
4. **Horizon (Q6):** is this a compounding event meant to run for years? A one-off or closing edition would shrink the log setup.
5. **Effort ceiling (Q7):** how many hours are available between editions, and does anyone own a between-edition job?
6. **Who reads the log (Q8):** who opens it before planning?
7. **The check-in cause:** what did the retro say drove the 90 minutes?

## Provenance

- **Sourced, from the skill's references:**
  - MLH's guide covers only the first handover.
  - DevOpsDays' guide shows that a shared document survives turnover.
  - Fraser and Mancl back the practice of cross-edition retrospectives.
- **Borrowed from software practice:**
  - the filing gate
  - the Keep/Update/Consolidate/Replace/Delete audit
- **This skill's own construction:**
  - the 2-versus-3 recurrence bar
  - the rung orderings
  - the CR-1 form
  - the 20-minute threshold
- **Not established organizer practice:** none of the self-set items should be presented as such.