# Edition two money model: approach

I haven't seen last year's budgets, actuals or cash-flow file, so everything below is method plus decision rules. Where a number is needed, I name the file it comes from. Each item has the same shape: the problem with the current framing, the replacement, and what to run on last year's data first.

## 0. Frame: one model, three views

Build edition two on one driver-based model. Its inputs are attendance, ticket mix, sponsor count and tier, and fixed commitments. Its three outputs are:

1. **Budget** for approval, with three versions mapped to scenarios (see item 3).
2. **Variance report** for the board (item 2).
3. **Cash-flow** with commit gates (item 3).

Items 1 to 3 are decisions inside this model, not separate topics.

## 1. Scholarship tickets: size from cost and need, not from "what big conferences do"

**Problem.** A 5% figure copied from larger conferences has no link to our cost, our demand or our sell-through. The "big conferences do it" claim is also unverified, and their scale and funding differ from ours.

**What a scholarship seat costs depends on one fact: do we sell out?**

| Situation | Real cost of one comp seat |
|---|---|
| Seat would stay empty | Marginal cost only: catering, badge, swag |
| Event sells out | Marginal cost plus the lost ticket price |
| Scholarship includes travel or lodging | The stipend, which usually dwarfs the seat |

**Approach.**

1. **Count all comps together.** Speakers, sponsor-included passes, volunteers, press and scholarships come from the same capacity. The 5% should be a total comp ceiling or a scholarship line inside one, not an add-on.
2. **Pull last year's sell-through curve** from the actuals. Find the date we hit 90% and 100%, if we did. This sets the displacement cost.
3. **Set scholarships as a dollar line, not a percentage of capacity:**
   - Cost = seats × (marginal cost + displaced ticket price × probability of sellout) + stipends.
   - Convert it to a share of total budget so the director can compare it with 5%.
4. **Size seats from demand.** Open applications early. If last year's demand was unrecorded, treat edition two as the measurement and record applicants, awards and show-up.
5. **Add a release rule.** Unclaimed scholarship seats go to the paid pool on a fixed date, such as 3 weeks out, if we are near capacity.
6. **Consider sponsor-underwritten seats** (a "sponsor a seat" add-on). This turns part of the cost into revenue and gives sponsors a cleaner story.

**Ask the director:** what is the goal (access, diversity, pipeline of future speakers)? A stated goal lets us pick the number and later report whether it worked. If they confirm 5% is a values commitment, then ✅ fund it as a policy line, not as something other conferences "allocate".

## 2. Board reporting: one number hides the story

**Problem.** "2% under budget overall" is a net of offsetting variances. It could mean revenue 8% short and costs 10% cut, or sponsorship flat and a one-off windfall. Last year's number "worked" because nothing large offset. We don't know that until we test it.

**Step 1: test last year before changing anything.** Using the per-line actuals and the approved budget version, compute the variance for every line. Check these three things:
- the sum of absolute variances against the net variance (a large gap means heavy netting)
- the largest favorable and unfavorable lines
- how many variances came from timing rather than permanent savings

**Step 2: replace the single number with a one-page board report:**

1. **Headline.** Net result against budget, with the baseline version named. State in dollars first, percent second.
2. **Revenue and cost, separately.** Variance on each, never netted against the other.
3. **Category table.** Revenue lines are tickets, sponsorship and other. Cost lines are venue, food and beverage, AV, speakers, marketing, staff and scholarships. Each gets budget, actual, variance and a direction flag.
4. **Flexed budget.** Re-state the variable cost lines at actual attendance. This separates "we sold fewer tickets" from "we overspent per head". This is the most useful column for the board.
5. **Materiality rule.** Any line past ±X% and ±$Y gets one sentence of cause. Set X and Y from last year's line-level volatility. Do not guess them.
6. **Nature tag.** Mark each variance as timing, one-off or structural. Structural variances carry into edition three.
7. **Cash position and reserve.** The surplus or reserve at close matters more to a board than the variance percentage.

**Cadence.** Report at fixed checkpoints (budget approval, 90 days out, 30 days out, close). Always compare against the same approved version, so the baseline cannot drift.

## 3. Sponsor concentration: "probably renewing" is not revenue

**Problem.** Two sponsors gave 70% of last edition's sponsorship, and their renewals are verbal. Without signed commitments, 70% of sponsorship revenue is at risk. The real exposure is that share multiplied by sponsorship's share of total revenue, which comes from last year's actuals.

**Scenarios.** Map the three costed budget versions onto them:

| Scenario | Assumption | Budget version |
|---|---|---|
| Signed only | Count only contracts in hand, plus pipeline at a haircut | Floor (the version we can fully commit to) |
| One anchor renews | One of the two stays, at full or reduced tier | Middle |
| Both renew | Last year's pattern repeats | Ceiling (upside, not the plan) |

Only the floor version should justify non-refundable commitments. I don't know the three versions' contents. If they don't line up with these scenarios, rebuild them so they do.

**Controls.**

1. **Get commitments.** Ask both anchors for a signed letter of intent or deposit by a set date. "Probably" turns into yes, no, or reduced, and either answer helps planning.
2. **Cash-flow commit gates.** Use last year's projection to list each fixed commitment (venue deposit, AV contract, speaker travel) with its date and refundability. Tie each to a trigger, such as "sign the venue deposit only after anchor A is signed or committed spend is below the floor-scenario revenue".
3. **Cost flex plan.** For each cost line, mark whether it is cuttable and how late. If both anchors lapse, we should know before the vote which lines move.
4. **Diversify sponsorship.** Set a target that no single sponsor exceeds a chosen share of sponsorship revenue. Ask what price points and tiers would bring in mid-size sponsors. Track the pipeline by stage with a probability haircut, not by name.
5. **Payment timing.** Check when anchor cash arrived last year relative to spend. If it came late, either bring invoice dates forward or accept a reserve to bridge the gap.
6. **Trigger dates.** Set go/no-go dates for the board: "If total signed sponsorship is below $Z by date D, we switch to the floor budget."

## What to do next, in order

1. Compute last year's line-level variance and sell-through curve. Both come from files we already have, so this answers items 1 and 2 on real evidence.
2. Get the sponsorship share of revenue and the cash-flow commit dates. This sizes the item 3 risk.
3. Ask the director for the scholarship goal, and the treasurer to review the report template with last year's numbers dropped in.
4. Bring all three, with numbers filled in, to the board as the edition two money model.

Decisions I need from you:
- Is the 5% a values commitment or a benchmark?
- Do the three costed versions map to floor, middle and ceiling, or were they built differently?