# Buffers, checkpoints, and the mid-flight replan

Depth behind SKILL.md's buffer-policy and replanning-trigger menus, plus a worked illustrative example. Everything sourced is labeled. Every date in the worked example is invented to show the pattern.

## The two sourced buffer mechanics, kept distinct

Both come from a major community-conference organizing guide's cost-control advice. They are two different tools, not one "have contingency" idea:

**Delayed commitment** shrinks a single line item late.

- The guide's own words: don't overcommit on headcount, don't pre-pay the venue until you must, and order food late - "it's always easier to add a few extra plates as opposed to having too much food ordered."
- The mechanic generalizes to any commitment where the two directions of error are asymmetric. Under-committing early and scaling up late is cheap (extra plates, extra seats, a second swag run). Over-committing early and scaling down late is expensive or impossible (a deposit, a placed order, a signed contractor).
- On the plan, this becomes a _latest-safe date_ per irreversible commitment, and the discipline of not committing before it just because the money is available.

**The scope-tier ladder** re-scopes the whole event at a checkpoint. Before selling a ticket, define three costed versions:

- **Good**: bare-minimum viable, the floor below which the event doesn't run.
- **Better**: the expected niceties.
- **Best**: real headroom, the extra evening activity, the nicer badges.

Then write dated downgrade checkpoints driven by revenue actually received: on each date, if revenue hasn't reached the tier's threshold, the event downgrades one tier - a decision that fires automatically instead of being argued mid-crisis. Sourced rationale: for sponsorship-funded community events, this decouples "will we run at all" from "did tickets sell," so a soft sales signal downgrades the event instead of cancelling it.

Milestone padding, the third rung, has one legitimate use: lead times outside the team's control (visas, printing, shipping, venue paperwork). Everywhere else it fails silently - everyone plans to the padded date, so the buffer is spent before anyone decides to spend it.

## Checkpoint design

A checkpoint is four fields, all written in advance:

| Field              | What it holds                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Date               | A moment already meaningful in the plan - an announcement, early-bird close, a tier's revenue deadline, one month out    |
| Condition          | One measurable check: revenue vs. tier threshold, registrations vs. expectation, a gate's prerequisite done or not       |
| Pre-written action | Exactly what fires on failure: cut this scope item, downgrade one tier, escalate this push, trigger the replan procedure |
| Owner              | Who executes the action without a meeting                                                                                |

The mechanic generalizes the sourced go/no-go downgrade dates above. The specific conditions and thresholds are always self-set per event - this file deliberately gives none. For demand thresholds at sales moments, defer to `samber/dev-event-organizer-skills@event-market-fit` rather than inventing numbers.

A negative example, the checkpoint that isn't one: "Mid-March: review ticket sales." - no condition, no action, no owner. Mid-March arrives, sales are soft, the review notes it, and the actual decision happens six weeks later as an emergency. The pre-written action is the entire difference between a checkpoint and a status meeting.

## The mid-flight replan procedure

When invoked on an event already behind (interview Q6), or when a checkpoint fires the replan action:

1. Rebuild the actual state per track: which milestones are done, late, or not started - against the plan, not against memory.
2. Recompute each track's remaining runway to its terminal milestone and flag every gate now at risk.
3. Spend buffers explicitly and in order: first un-spent latest-safe slack (commitments that can still slide), then a scope-tier downgrade if the ladder exists, then scope cuts.
4. Cut scope at the gate level: cut the item whose removal un-blocks the most downstream milestones, not the item that is merely most behind.
5. Never move an announced date. Before announcement, a date move is a legitimate lever - price it against the external deadlines (venue windows, sponsor fiscal years) before using it.
6. Re-write the remaining checkpoints against the new plan: a replan that keeps the old checkpoint conditions re-fires them immediately.
7. Tell the user which lever was spent and what it bought - a silent replan hides exactly the information the debrief needs.

## Worked illustrative example

**Illustrative of the general pattern only.** Every date and offset below is invented for a fictional mid-size recurring community conference: none of it is a sourced runway. For the sourced, format-driven runways an actual plan should be calibrated against, use `samber/dev-event-organizer-skills@event-first-edition`.

Anchor: doors-open October 15.

External immovables:

- Venue holds its date only until January 31 (contract deadline).
- Two anchor sponsors close their budgets in April.

| Track             | Working backward from October 15 (illustrative dates)                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Venue & logistics | Walkthrough Oct 1 ← build-up plan Sep 1 ← deposit **latest-safe Jun 30** ← contract Jan 31 (external immovable) ← locked Jan 15                                    |
| Program           | Announced Jun 15 ← speakers confirmed May 30 ← selection May 15 ← CFP closes Apr 30 ← CFP opens Feb 15 ← designed Feb 1                                            |
| Sponsors          | Fulfillment scheduled Jul 1 ← agreements Jun 1 ← outreach starts Mar 1 (pulled early by sponsors' April budget close) ← prospectus Feb 15 ← tiers costed Feb 1     |
| Ticketing         | Final headcount **latest-safe Sep 20** (caterer's real lead time) ← early-bird closes Jul 15 ← sales open Apr 1 ← payment infra live Mar 15                        |
| Marketing         | Final push Oct 1 ← program-driven push Jun 15 (gated on program announced) ← date announced Apr 1 (gated on payment infra + venue contract) ← channels ready Mar 1 |

Gates visible in the table:

- Date announced Apr 1 waits on payment infra (Mar 15) and the venue contract (Jan 31).
- The sponsor track is pulled two months earlier than internal logic would place it, by an external fiscal-year deadline.
- Two latest-safe dates (venue deposit, final headcount) carry the delayed-commitment buffer.

Checkpoints for the same fictional event (conditions and thresholds invented, as they always are - self-set per event):

| Date   | Condition                                              | Pre-written action                                                          | Owner           |
| ------ | ------------------------------------------------------ | --------------------------------------------------------------------------- | --------------- |
| Apr 30 | Anchor-sponsor revenue below the Better-tier threshold | Downgrade Best → Better; cut the evening event from the plan                | Finance owner   |
| Jul 15 | Early-bird sales below expectation at close            | Escalate the community outreach push; hold catering at Good-tier quantities | Marketing owner |
| Sep 15 | Any gate into the final month still unmet              | Fire the replan procedure above                                             | Lead organizer  |
