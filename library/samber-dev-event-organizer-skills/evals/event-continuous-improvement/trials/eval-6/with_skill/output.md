# Solder & Code: cross-edition read for next-year planning

⚠️ I couldn't run the skill's interview, so some assumptions are open. Section 6 lists them.

**Scope.** I assume four editions of written debrief records. Every trend claim below is "N of 4 editions". The skill's filing gate, two-vs-three occurrence bar and entry formats are its own conventions, not published organizer practice. The only exception is the "twice is coincidence, three times is a pattern" heuristic behind the occurrence bar, which is a much older general rule.

## 1. Answers

| Question | Answer | Basis |
|---|---|---|
| Rebook Fork & Flame? | **Not unconditionally.** Rebook only if they pass a root-cause and capacity check against the new headcount, and the new brief carries a delivery-window penalty. Get one competing quote in parallel. | 2 of 4 editions late, a candidate rather than a pattern. The final verdict belongs to `event-vendor-sourcing`. |
| 500 attendees or cap at 350? | **The evidence doesn't support committing to 500. It also doesn't prove 350 is a hard cap.** Decide after the registration fix is load-tested and demand is checked. The decision belongs to `event-growth-strategy`. | One failure, at about 350, against three clean editions under 300. |
| AV costs? | **Itemize, then make one change.** Break down AV spend by line item and per attendee for all four editions. Then pick one lever, such as competitive bid, scope freeze or rental-vs-owned, and set a numeric check. | The spend rose in 3 of 3 consecutive intervals, which is a pattern by the occurrence bar. The cause is unknown. |

## 2. Filed entries

Conditions are written about systems and vendors, not people.

### Theme: lunch delivery timing (vendor)

- **Occurrences:** 2 of 4 editions (ed. 3 and 4), consecutive and most recent. Editions 1 and 2 were fine.
- **Status:** candidate, not pattern.
- **Gate:** passes. It is current, it would recur if the edition ran unchanged, and it points at a vendor and brief decision.
- **Condition:** 45+ minutes late delivery, with no contractual delivery window or fallback.
- **Open question:** what changed between edition 2 and edition 3? Headcount, menu, kitchen, venue access and delivery route are all candidates. Without that, I can't say whether it is vendor drift or a capacity limit the event outgrew.
- **Routed to:** `event-vendor-sourcing`, filed on Fork & Flame's own record this cycle. Hand over the evidence, not the verdict.

### Theme: registration capacity (platform)

- **Occurrences:** 1 of 4 editions (ed. 4). This is an entry, not a trend.
- **Condition:** pages timed out during the morning rush at about 350 attendees. Editions 1-3 stayed under 300 with no failure.
- **Gate:** passes, but it can't be called a pattern.
- **Hedge:** the observed ceiling is somewhere between 300 and about 350. Peak concurrent load, not total attendance, may be the real driver. I can't tell from the record.
- **Routed to:** `event-growth-strategy` as ceiling evidence only. `event-planning-timeline` gets the fix as a task.

### Theme: AV spend creep (budget line)

| Edition | AV spend | Change |
|---|---|---|
| 1 | 8k | — |
| 2 | 11k | +3k |
| 3 | 15k | +4k |
| 4 | 19k | +4k |

- **Occurrences:** 3 of 3 intervals rising, +138% overall. This meets the pattern bar.
- **What it doesn't tell you:** attendance, rooms, hours and scope per edition. A hardware conference may legitimately add camera feeds for bench demos, and that would be value rather than waste.
- **Routed to:** `event-budget` owns the cost model. I read the trend and don't re-model it. If one AV supplier drives most of the growth, the supplier file goes to `event-vendor-sourcing`.

## 3. Cross-theme risk

Moving to 500 changes catering, registration and AV at the same time. That makes each of the three fixes unattributable next cycle.

Whichever size you pick, don't change two of these three themes at once in a way that muddies the checks. Changing headcount and the fix together also breaks the attribution. If you go to 500 anyway, lock the fixes first and treat size as the experiment.

One more hypothesis, not a finding: lateness started in edition 3 while headcount was still under 300. So the caterer problem may or may not be size-linked. Test that before blaming growth.

## 4. Deliberate changes

I count these as three changes on three separate themes. Do not stack a second change on any single theme this cycle.

**CR-1: Catering brief and vendor decision**
- **Change:** ask Fork & Flame for a root-cause account and a capacity statement for next headcount. Require a delivery window with a penalty or credit clause and a named fallback. Solicit one comparable quote.
- **Because:** two consecutive late deliveries after two clean ones need an explanation before another deposit.
- **Check:** lunch served within 15 minutes of schedule, observed on the day and timestamped at the door. Treat a miss as a trigger for replacing the vendor next cycle. The 15-minute threshold is my suggestion, not a standard.
- **Routed to:** `event-vendor-sourcing`.

**CR-2: Registration load test**
- **Change:** load-test the registration platform at 1.5x the target headcount, using realistic morning-rush concurrency. Add a waiting-room or staggered check-in window if the platform supports one.
- **Because:** the failure is a capacity-and-fallback condition, and it is cheap to test before it fails live.
- **Check:** page response under load at the tested concurrency, plus zero timeouts during the live morning rush. Measure both at the platform, not by survey.
- **Routed to:** `event-planning-timeline` as a real task, and `event-growth-strategy` as evidence.

**CR-3: AV cost lever**
- **Change:** first, itemize AV by line and per attendee for editions 1-4 (a data task, not a change). Second, pick one lever from the breakdown.
- **Because:** a cost line that rose three times in a row needs its driver found before anyone caps it.
- **Check:** AV cost per attendee, or per room-hour, at edition 5 against a threshold set from the breakdown. A direction-only target such as "lower" invites a motivated reading.
- **Routed to:** `event-budget` and `event-vendor-sourcing`.

## 5. Hand-offs

| To | What |
|---|---|
| `event-vendor-sourcing` | Fork & Flame record: late in ed. 3 and 4. Include the CR-1 brief changes. |
| `event-growth-strategy` | Evidence only: one registration failure near 350, three clean editions under 300. Catering lateness began under 300, so it may not be size-linked. No size recommendation from me. |
| `event-market-fit` | Whether demand for 500 exists (sellout speed, waitlist, return rate). I hold no demand data. |
| `event-budget` | AV trend. They own the model. |
| `event-planning-timeline` | CR-2 as a task with the date the load test must finish before registration opens. |

## 6. Persistence and what to do next

- **Log:** use an appended document, one dated heading per edition. Add a named owner and a named person who opens it before planning starts. "The team" doesn't count.
- **Audit:** run a kickoff pass before planning opens. Classify every entry as Keep, Update, Consolidate, Replace or Delete, and leave none unclassified.
- **Closure:** after edition 5, reopen CR-1 to CR-3 and append two columns: did it improve (yes/no), and why.

**Open assumptions that could change this:**
1. Do you hold written records for all four editions, or only some? If fewer, downgrade every claim.
2. How much of the team turned over? A rotation promotes the structured record and the written trend review.
3. When does planning start or the go/no-go land? That date is the deadline for CR-1 and CR-2.
4. Was anything different in ed. 3 for catering, such as headcount, menu or venue?
5. Do you have AV line items and attendance per edition?

Answer these and I can firm up the candidate-versus-pattern labels.