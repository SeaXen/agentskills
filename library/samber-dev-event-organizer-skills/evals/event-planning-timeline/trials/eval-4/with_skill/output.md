# Oversight plan: Vantage Cloud user conference, Lisbon, 11 September (3rd edition, ~900 attendees)

I read the skill and both references before writing this. I assumed the event is 11 Sep **2027**, about 47 weeks out. It's a recurring, company-run event with six owners, one per track.

## Verdict

Don't add a new meeting. Your Tuesday standup already qualifies as the skill's *cadence variance review*. That review is normally the costliest oversight layer. It qualifies because you have five or more parallel owners and an existing check-in everyone attends, so the marginal cost is near zero.

The monthly round-the-room all-hands is the weak part. The skill calls it a checkpoint with no pre-written action, which degrades into a status meeting. It also leaves you exposed to the "unwatched middle", the quiet months before the final sprint where drift compounds.

Oversight has three layers:

| Layer | What it is | Where it runs |
|---|---|---|
| 1. Weekly variance review | Actual vs plan, per track, exceptions only | Tuesday standup |
| 2. Pre-written checkpoints | Dated condition, pre-decided action, owner | Replaces the monthly all-hands |
| 3. Event-driven replan | Floor for broken foundations (venue lost, anchor sponsor out, CFP badly undersubscribed) | Ad hoc, runs the replan procedure |

## Layer 1: Tuesday standup becomes the variance review

Keep the 30 minutes. Change the format:

1. Each owner gives one line: next milestone, actual vs plan, and whether a latest-safe date or a gate is now at risk (about 3 min each, 18 min total).
2. Spend the remaining ~12 min on gates at risk and on firing any checkpoint action that is due.
3. Read three numbers from the tracker: buffer consumed per track, tracks behind, gates at risk.
4. Skip anything on schedule. "On track" gets one word.

**Slip rule:** a track's slip exceeds its buffer when a milestone that feeds a gate is late. Per the buffer policy, buffer lives only on irreversible commitments, scope tiers and external lead times. Most milestones therefore have no padding, so any late gate-feeding milestone goes on the replan list. It doesn't get debated.

Use one shared tracker, the simplest one the team will actually update. Write tasks as finished states ("The CFP form is live") and bucket them by weeks to doors-open ("S-12"). Tag each task by track so owners can filter. S-buckets carry over to next year's edition unchanged.

## Layer 2: checkpoints replace the monthly all-hands

Each checkpoint has four fields: date, one measurable condition, a pre-written action, and an owner who executes it without a meeting.

The dates and conditions below are **illustrative placeholders**. Replace each with your real constraint (contract windows, vendor lead times, sponsor budget cycles). Take thresholds from edition 2's actual curves and from `event-market-fit`. I invented none.

| When | Condition | Pre-written action | Owner |
|---|---|---|---|
| Now (S-47) | Any of the six tracks has no single accountable owner, or the team & volunteers track has none | Lead organizer assigns an owner by next Tuesday | Lead organizer |
| Before date announcement | Payment infra live, venue contract signed and code of conduct published, all three | If any is unmet, hold the announcement | Ticketing owner |
| Sponsor budget-cycle date (set from sponsors' real fiscal calendars) | Signed sponsor revenue below the Better-tier threshold | Downgrade one tier (Best → Better) and cut the scope item listed for that tier | Budget owner |
| CFP close + selection | Submissions or accepted speakers below the edition-2 baseline | Open invited-speaker track and extend outreach. Don't move the date. | Program owner |
| Early-bird close | Sales below the edition-2 curve | Escalate the marketing push and hold catering at Good-tier quantities | Marketing owner |
| ~S-8 | Any gate into the final month is unmet | Fire the replan procedure | Lead organizer |
| Combined gate (~S-4, anchored to the real lead time) | Sponsors unconfirmed or speakers unannounced | Lock merchandise artwork without the unconfirmed names and announce the confirmed speakers only | Sponsors + program owners |
| Caterer's real lead time | Final headcount not frozen | Order at the frozen-headcount floor. Add plates later. | Ticketing owner |

**The monthly all-hands:**
- Keep it, but change the agenda to the checkpoints due that month plus gates at risk.
- Drop the round-the-room review.
- Cancel it in any month with no checkpoint due. That's your call, not the skill's.

**Revenue-tier checkpoints** apply if budget depends on revenue not yet booked, which is normal for sponsor-funded events. Then define Good/Better/Best versions of the conference before more tickets sell. Downgrade on a date, driven by revenue received. This decouples "do we run" from "did tickets sell".

## Gates the standup must watch

Each gate names both sides:

- Date announced ⟸ payment infra live (ticketing) and venue contract (venue)
- Sponsor prospectus assembled ⟸ draft budget approved (budget)
- Program announced ⟸ speakers confirmed
- Program-driven marketing push ⟸ program announced
- Catering and swag orders ⟸ final headcount (ticketing)
- Sponsor fulfillment ⟸ agreements signed, which feeds marketing and venue

For every irreversible commitment (venue deposit, catering order, print run), record its **latest-safe date** and owner, and hold the commitment open until then. Don't pad milestones uniformly.

## Layer 3: the floor

When a foundation breaks:

1. Rebuild actual state per track.
2. Flag the gates now at risk.
3. Spend buffers in order: latest-safe slack, then a tier downgrade, then scope cuts.
4. Cut the item that unblocks the most downstream milestones, not the one most behind.
5. Rewrite the remaining checkpoints against the new plan.
6. Tell the team which lever was spent.

Company-run adds one lever: spending to recover execution slips (rush fees, contractors). Money doesn't recover calendar physics, so a compressed CFP stays compressed.

**Standing rule:** once the date is announced, the date holds and scope moves. As a recurring annual event, a moved date costs you the most trust.

## How to know it works

Four pass/fail gates on the plan itself:
- Every cross-track dependency is an explicit gate.
- Every irreversible commitment has a latest-safe date and an owner.
- Every checkpoint has all four fields.
- Every track has exactly one owner.

Final verdict: the date never moved after announcement, and every scope cut happened at a checkpoint rather than mid-crisis.

## Open questions that would change this

1. Is the date announced and the venue signed? An announced date is no longer a variable.
2. Are there external deadlines (sponsor fiscal cycles, venue contract windows, a grant calendar)? These pull checkpoints earlier.
3. Is there a multi-venue setup, a contract penalty clause, or paid production staff? If so, promote the affected tracks to a task-level critical path.
4. Does the budget rely on unbooked sponsor revenue? If so, the tier ladder becomes mandatory.
5. Who owns team & volunteers? None of your six tracks covers it.
6. Please confirm the year. If it's 11 Sep 2027, that's a Saturday, which matters for venue and catering contracts.

Checkpoint conditions and thresholds need your edition-2 data. Once you have that data, I can fill in the table.