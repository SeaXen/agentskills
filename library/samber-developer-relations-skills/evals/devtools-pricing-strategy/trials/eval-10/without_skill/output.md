# Ambergate Pricing Review — Board Briefing (2026-09-29)

## Executive Summary

Flat per-instance pricing ($450/mo, no usage tiers) is hiding a margin problem: average cost-to-serve is $95/instance (79% margin), but the top decile of instances costs $310 (31% margin). Blended across the base, real gross margin is closer to **~74%**, not 79% — the tail is quietly dragging the whole book down. Recommendation: replace flat per-instance pricing with three usage-based tiers (Standard/Growth/Scale) plus enterprise custom, keep the $450 entry price unchanged for the majority of the base, and phase in higher pricing for the top 10-20% of usage over two quarters. No change recommended to the no-free-tier stance. Pricing ownership should sit with a single named DRI (recommended: Head of Product), not stay ambient across whoever gets asked.

---

## 1. Current State & the Core Problem

| Metric | Value |
|---|---|
| List price | $450/mo/instance (flat, single tier) |
| Average cost-to-serve | $95/instance/mo |
| Top-decile cost-to-serve | $310/instance/mo |
| Margin, average instance | 78.9% |
| Margin, top-decile instance | 31.1% |
| Free tier | None |

Implied instance count at $6M ARR / $450 / 12 months: **~1,111 billed instances**. Top decile ≈ **111 instances**.

**Blended gross margin is lower than it looks.** If the bottom 90% of instances cluster near the $95 average and the top decile sits near $310:

- Total monthly cost ≈ (1,000 × $95) + (111 × $310) ≈ $129,400
- Total monthly revenue ≈ 1,111 × $450 ≈ $500,000
- **Blended gross margin ≈ 74%**, not the 79% the "average customer" number suggests.

**Root cause:** "per instance" is not a value metric — it doesn't track what actually drives cost or value. An instance handling 50x the traffic of another is priced identically but costs 3.3x more to serve. That's not a rounding error; it's the pricing model actively mispricing the tail. Two consequences, both live risks:

- ⚠️ **Margin concentration risk.** The heaviest 10% of instances generate the thinnest margin, and if their usage keeps growing, that margin keeps compressing — with no pricing mechanism to catch it.
- ⚠️ **Competitive exposure at the top.** A usage-based competitor can profitably underbid Ambergate specifically for its heaviest users (the ones a competitor can serve accurately and still profit from), while Ambergate is stuck cross-subsidizing them from everyone else.

---

## 2. Recommended Pricing Architecture

**Change the value metric** from "flat per instance" to "per instance + usage tier," where usage (illustrated below as monthly requests processed — substitute your actual dominant cost driver, e.g. bandwidth or connection count, once validated against real cost data) sets the tier and an overage charge covers growth within a tier.

| Tier | Price/instance/mo | Included usage (illustrative) | Cost-to-serve band it targets | Worst-case margin in band | Support / SLA |
|---|---|---|---|---|---|
| **Standard** | **$450** (unchanged) | ~5M req/mo | ≤ $120 | 73.3% | Email, next-business-day, 99.9% |
| **Growth** | **$850** | ~20M req/mo | $120–$200 | 76.5% | Priority (4h), 99.95%, advanced routing/WAF |
| **Scale** | **$1,450** | ~60M req/mo | $200–$310 | 78.6% | Dedicated support/TAM, 99.99%, SSO/mTLS/custom domains |
| **Enterprise** | Custom quote | Committed/negotiated | >$310, true outliers | Floor: 65% | Dedicated infra options, custom SLA, annual contract |

Worst-case margin at the top of every band is ≥73% — at or above today's *blended* 74%, and far above the 31% the top decile earns today. Overage beyond the included allowance: illustrative $12–$15 per additional 1M requests, calibrated from your actual marginal-cost regression before launch, reviewed quarterly.

**Why this shape:**
- Standard stays at $450 — no disruption for the ~75-80% of the base that's already profitable there.
- Scale's $1,450 is set so a $310-cost instance lands at the same ~79% margin the "average" instance earns today. This isn't a margin-expansion ask to the board — it's margin *consistency*, closing a gap the current model created by accident.
- Overage protects margin as any customer's usage grows *between* pricing reviews, instead of only catching it at the next repricing cycle.

**Value at stake (top decile only, illustrative):** Today, ~111 top-decile instances earn ~$140/mo margin each (~$186K/yr total). At Scale pricing with the same $310 cost, margin becomes ~$1,140/mo each (~$1.52M/yr) — a gross ceiling of **~$1.3M/yr upside** from this segment alone, before any churn or negotiation losses. Treat this as a ceiling, not a forecast.

**Before finalizing tier boundaries:** the $95/$310 figures given here are two data points, not a distribution. Pull actual per-instance cost-vs-usage data and set the $120/$200 breakpoints from real deciles, not the illustrative midpoints used here.

---

## 3. Free Tier: No Change Recommended

Don't add an ongoing free tier. Cost-to-serve here is real infrastructure spend ($95/instance minimum), not near-zero marginal SaaS cost — a free tier is a direct margin drain, not a low-cost funnel. If self-serve top-of-funnel volume becomes a stated growth priority, the lower-risk options are a time-boxed trial (14-30 days, full-featured, card required) or a hard-capped, non-production "Sandbox" tier — neither is urgent for Tuesday; flag as a follow-up decision, not part of this repricing.

---

## 4. Rollout Plan

Don't flip pricing on the whole base at once. Sequence it:

1. **Now → Q4 2026:** Pull real usage/cost data per instance; validate the $120/$200 tier breakpoints and the overage rate against it.
2. **Q4 2026, new customers only:** Launch Standard/Growth/Scale for all new signups. This is the clean read on market acceptance — new customers have no anchor price to react against.
3. **Q1 2027, existing base, bottom 80-90%:** No action needed — they're at or below the Standard allowance, price unchanged.
4. **Q1–Q2 2027, existing top 10-20%:** 90-day advance notice. Frame as an upgrade (higher usage headroom, priority support, higher SLA), not a penalty. Offer to lock in current $450 for 12 months if they prepay annually now; consider a 20%-off first-year rate on the new tier to soften the move. Migrate in waves (5-10% first), watching churn and support volume each wave before expanding — not all at once.

Expect the highest-usage, thinnest-margin accounts to be the most likely to churn on this move. That's an acceptable, even favorable, trade — those are the accounts currently costing the most to keep at a loss-adjacent margin.

---

## 5. Risks & Open Questions

1. **Data gap:** tier boundaries above are illustrative from two data points (avg, top-decile). Real per-instance cost/usage data is needed before external commitment.
2. **Elasticity unknown:** no willingness-to-pay research has been done on the Growth/Scale price points. Treat $850/$1,450 as a first bet to learn from, not a final answer — watch new-customer conversion at these prices in Q4 before committing existing-customer migration dates.
3. **Support cost may be underweighted:** "$310 cost-to-serve" likely reflects infra only. Heavy accounts typically also consume more support/CS time — if so, true top-decile cost (and the case for Scale pricing) is even higher than modeled here.
4. **Entry-price risk to Standard:** $450 flat may already be a barrier for genuinely light/low-usage prospects if usage-based competitors quote lower entry prices. Not addressed by this plan — flag as a separate GTM question if bottom-of-funnel conversion is a concern.

---

## 6. Pricing Ownership — Who Should Own This

Recommendation: **a single named DRI, not a committee and not "whoever's in the room."** At 30 people, that should be your most senior product/commercial leader — typically a Head of Product. Concretely, that means:

- **Not the CTO.** You own cost data, which is essential input, but pricing is value-based, not cost-based (cost is the floor, not the basis) — owning both creates a structural bias toward cost-plus pricing.
- **Not Finance.** Same reasoning in reverse: valuable as a margin guardrail, not as the owner — finance-led pricing tends to under-price on value and over-index on cost recovery.
- **Not Sales.** Useful for market/willingness-to-pay signal, but a Sales owner biases toward discounting to close individual deals.
- **Not "ask the CEO/CTO each time."** That's the status quo you're trying to fix — it doesn't scale and it's why this keeps landing on your desk.

**Structure:** Head of Product (or your most senior PM if no formal Head of Product exists) is the DRI — proposes pricing changes, owns the pricing page and packaging. A quarterly pricing review (DRI + Finance for margin data + Sales/CS for field signal + you for cost/COGS input) reviews and stress-tests proposals. CEO approval required only above a materiality threshold (e.g., >15% blended ARR impact, or any new tier/plan launch). This gives you a name to point to next time you're asked, and a light process so it doesn't default back to you by inertia.

---

## 7. Decisions Needed at Tuesday's Board Meeting

1. Approve the shift from flat per-instance to usage-tiered pricing (Standard/Growth/Scale/Enterprise), in principle, pending data validation.
2. Approve the phased rollout (new customers Q4 2026, existing top 10-20% migrated Q1-Q2 2027).
3. Confirm no ongoing free tier; defer trial/sandbox decision to a later GTM discussion.
4. Approve Head of Product as pricing DRI, with quarterly review cadence and CEO-approval threshold as described.