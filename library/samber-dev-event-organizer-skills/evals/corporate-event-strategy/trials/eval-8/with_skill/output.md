# DriftCon Year 3: ownership and goals strategy brief

I followed `corporate-event-strategy` and its two references. The skill is meant to run as an interview, one question at a time. I couldn't ask you anything, so every answer I had to assume is marked ⚠️ and listed at the end with what it would change.

## 0. Recommendation up front

- Reject the colleague's three goals.
- Fund DriftCon through a multi-function committee with a named executive sponsor. Marketing is no longer the sole owner.
- Set two goals, adoption and pipeline influence, each with four measurement fields. Fall back to adoption-first if the pipeline join doesn't exist.
- Write the handover before January, and have the VP Marketing run the funder conversations herself while she still has the political capital.

## 1. Why the colleague's goals fail

"Thought-leadership positioning, brand impressions, qualified lead capture" is the objective language of a sponsor prospectus. It describes what a company buys at somebody else's event. Using it for the host's own goals narrows DriftCon to whatever a booth would have delivered.

| Colleague's goal | Verdict | Reason |
|---|---|---|
| Thought-leadership positioning | ❌ Deleted | This is ecosystem goodwill only. It has no number to defend a line, and it must be deleted once any co-funder exists. Product, DevRel and sales are all stakeholders. |
| Brand impressions | ❌ Deleted | This is reach or attendance counted as an outcome. It is the fallback number teams use when the real one is late. |
| Qualified lead capture | ❌ Rejected | A booth-scan metric. It needs an attendance-to-CRM join, and for a developer audience (see §2) it records influence, not conversion. |

The sponsor frame also hides the real problem. DriftCon isn't short of a goal. It is short of an owner who survives January.

## 2. Audience and buyer-and-user

**Audience the list can assemble.** ⚠️ I'm assuming the invite list is Driftline users, customers and prior DriftCon attendees. That is a room of people who already use the product. A goal aimed at people who have never bought would need an acquisition campaign nobody has budgeted.

**Buyer and user.** ⚠️ For CI/CD observability I'm assuming this is **separated**. The engineer or platform team evaluates and adopts, and an engineering or platform leader signs.
- Any attendance-to-opportunity join measures **influence, not attribution**.
- The deliverable must say "influence" everywhere. Calling it attribution gets caught the first time someone checks one record.
- If your product is actually self-serve and bought by the developer, the pipeline goal can be stated more strongly.

## 3. Goal mix: three candidates

| | A. Adoption-first | B. Blend (adoption and pipeline influence) | C. Pipeline-first |
|---|---|---|---|
| Speed of a readable number | Slow | Slowest (the slower read gates it) | Fastest |
| Durability through a bad quarter or owner change | Good | **Best** | Weak |
| Instrumentation effort | One join (product telemetry) | Two joins plus a reconciliation owner | CRM join plus an agreed rule |
| Funding consequence | Product co-funds cleanly | Product and sales both fund, each against its own number | Sales co-funds; product would hold a veto with no metric |

**Recommendation: B.** The deciding factor is durability. The owner is leaving, and the blend is the only goal with a second story when one number has a bad quarter. The promotion conditions are all required:
1. Year 3 is a compounding annual program. ✅
2. Both joins exist or can be built. ⚠️ Unknown.
3. Someone can hold the measurement job through the quarter after the event. ⚠️ Unnamed.

If condition 2 or 3 fails, **fall back to A**. Run it first and add pipeline influence the year the join exists. Pipeline-first (C) is rejected: the room is mostly existing users, and nothing says a hard reporting date forces speed over durability.

**Rungs rejected, so the goal doesn't widen later:**
- Ecosystem goodwill only is deleted, not demoted. It survives only as a behavior constraint on how DriftCon runs, for example no hard-sell program slots.
- Attendance count is deleted.
- Pipeline-first is rejected for the reasons above.

## 4. Budget ownership

**Model: multi-function committee with a named executive sponsor.**
- Product, DevRel and sales all have a stake. That is more than one co-fund rung can absorb.
- It is a compounding program, and this is the only model where DriftCon isn't one person's discretionary spend.
- The cost is real. Every decision on audience, date or program becomes multi-party, and each funder is owed a standing report in its own terms.

**What each function buys, and the coupling check:**

| Function | Buys | Funds against | Claim it holds | Does not get |
|---|---|---|---|---|
| Product | Depth with users, roadmap demos in a venue it controls | Adoption goal | Program slots for roadmap content | Veto over the pipeline number or the guest list |
| Sales | Accounts it works in a welcome setting (the dinner track) | Pipeline-influence goal, only once the join exists | Weight on the dinner guest list | Control of the main-stage audience |
| DevRel | Flagship community moment | ⚠️ Unknown whether it puts money in. It owns the adoption and community read either way. | Say on the speaker and attendee experience | Ownership of the budget line |
| Marketing (successor) | Day-to-day operation of the event | Remainder of the line | Operating decisions and the single event calendar | The goal, alone |

**The executive sponsor** must sit above all of them: CMO, CRO, CPO or CEO. Without one, the committee has every veto and none of the protection.

**Failure patterns to guard against:**
- **Product turns it into a launch vehicle.** Send that conflict to the event's published positioning, not into a program argument.
- **Sales turns it into a sales meeting with a program attached.** Keep the dinner track separate from the main-program audience.
- **The committee exists but never meets.** Test it by asking who ran the last review, not who is on the list.
- **No named line owner.** If January arrives with no answer to "who owns the line", that is the failure that kills the event. It fails silently.

**Sequence:**
1. Before January, the VP Marketing and the sponsor name the **line owner**, the person who holds the budget day to day after she leaves.
2. Hold the funder conversations with **the same four lines for every funder**: what they get, how it is measured, which decisions they gain a say in, and which decisions they don't.
3. Write the handover (§7) when the arrangement is made, not on her way out. The version written on the way out is always the thin one.

## 5. Measurement commitment

Written before registration opens. Every threshold is **self-set**. No industry figure transfers across companies for event ROI.

A goal missing any of the four fields is only an intention. Names below are placeholders to fill.

**Goal 1: adoption**
- **Metric:** share of attending accounts that activate at least one product capability they hadn't used before, in the window from event to next quarter close. Compare against a matched set of non-attending accounts, decided in advance.
- **Owner:** [named person in product analytics]
- **Source system:** product telemetry that identifies accounts
- **Read date:** the week after that quarter closes, before the planning cycle that renews the line

**Goal 2: pipeline influence** (only if the join exists)
- **Metric:** opportunities created within an agreed window on accounts with at least one attendee or dinner guest, under an attribution rule agreed before the event. Report it as influence, and compare dinner-track accounts against similar non-dinner accounts.
- **Owner:** [named person in RevOps or sales]
- **Source system:** the CRM
- **Read date:** [a date before the funding decision it informs]

**Observables to track** (self-set):
- **Goal-to-number latency:** a gap longer than the funding cycle means the goal can't defend its own line.
- **Funder attrition:** how many signers still fund it next cycle.
- **Goal drift:** whether the debrief scores the edition against this goal.
- **Counterfactual honesty:** state plainly whether a comparison set was used, or whether the number is a before-and-after read in which the event is one of several causes.

## 6. Three reviews, before invitations and registration go live

All three are ⚠️ status unknown. Route each to the company's own counsel; none is decided here.

1. **Company name on a room it doesn't control.** Terms, a code of conduct that binds staff as well as guests, and insurance. An incident can't be revised afterward.
2. **Attendee list moving into the sales CRM.** This is a personal-data decision for whoever holds privacy obligations, and it comes before registration. A list collected under the wrong notice can't be un-collected. It gates Goal 2.
3. **Customers and prospects hosted as guests.** This hits the dinner track directly. Check the company's gifting policy and the guest's employer's policy, which is often stricter. Public-sector and regulated guests are the common problem. Confirm the accounts can accept before the goal depends on them.

## 7. Handover document

Dated, short, and written now. It names:
- The goal mix and the rejected rungs, so the successor doesn't reopen settled arguments.
- Each funder, what each buys, and the claim each holds.
- The four measurement fields per goal, plus the source systems and the people who run the reports.
- The status and dates of the three reviews.
- The re-run triggers.

## 8. Re-run this analysis when

- The goal changes.
- A funder joins or leaves. The VP's departure and her successor's arrival count.
- The buyer-and-user answer changes because the product changed.
- The invite list stops matching the goal.

A goal change between editions goes back to `event-growth-strategy`.

## 9. Assumptions to confirm

| ⚠️ Assumption | If wrong |
|---|---|
| Buyer and user are separated | Pipeline can be framed more strongly, but the guest-list and consent work stays the same |
| The invite list is mostly existing users | If the target is non-users, you need an acquisition budget before any pipeline goal |
| Product telemetry identifies accounts, and a CRM join exists or can be built | Drop to adoption-first |
| Someone can hold the measurement job in the quarter after the event | Same fallback, because a blend without a reconciliation owner produces two numbers and an unwinnable argument |
| An executive above all functions will sponsor | Without one, don't create the committee. Fall back to the closest co-fund rung. |
| DevRel's role is operator and metric owner, not funder | If DevRel funds, add it as a committee seat |
| Planning-cycle date, ideally before the VP leaves | A hard date favors faster-reading goals |

The first thing I'd resolve is who the executive sponsor is, because every other part of the structure depends on that answer. Do you want me to draft the four-line co-funding pitch for each function?