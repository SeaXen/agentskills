# Pricing — Flagstone

## Verdict

Your team's instinct is half right. Seats are broken — but full usage-based billing isn't buildable this year, and trying anyway just recreates the failure mode this skill calls out explicitly: **"revenue is flat while usage grows" is the signal to change the metric, not the number** [self-set, price-point-method.md]. Don't do a wholesale metric swap either way — it re-prices all 210 accounts at once and turns a metric fix into a churn event.

**Recommendation: an additive, two-phase hybrid.**

1. **This fiscal year (zero new engineering):** keep a small seat component for the real human surface (console/targeting-rule access), add a capacity fee on environments + projects — both readable off account records today — and attach a published, generous, *manually-enforced* evaluation ceiling per tier to start surfacing the real usage number without building a billing-grade metering pipeline.
2. **Next funded quarter:** replace the manual ceiling with metered evaluation overage, using this year's account-level usage data (collect it now, even coarsely) as the evidence for where to set the allowance.

This is exactly the shape the skill predicts for a starved consumption metric: **"a hybrid is not a compromise... it is also how a starved consumption layer gets bought in stages, under a metric that already works"** [self-set, SKILL.md step 2].

---

## Inputs

- **Model:** hosted SaaS, feature-flag evaluation. [given]
- **Buyer:** platform/eng lead with team budget; procurement enters once contract value clears roughly six figures a year — that threshold is Christoph Janz's field-sales heuristic, not a measured constant [sourced, pricing-evidence-base.md]. Below that, self-serve only.
- **Current economics:** 210 accounts × 5.4 seats × $19 = **$21,547 MRR / ~$258.5k ARR** [computed from given figures], flat for 14 months while evaluations grew 40M → 380M/month (9.5x) [given].
- **Cost per unit — the real gap.** You don't have it, and step 1 of this skill calls that a blocker, not an aside. Two different numbers are being conflated here and only one is expensive:
  - *Per-account, billing-grade evaluation metering* → a quarter of backend work, correctly out of scope this year.
  - *Aggregate cost-per-evaluation* (infra spend ÷ total monthly evaluations, company-wide, no new pipeline) → a finance/infra exercise, days not months. Get this number before setting any price floor. Without it, every number below is an experiment, not a decision.
- **Free alternative's true cost (the ceiling):** the feature-flag category has multiple self-hostable/OSS options (Unleash, Flagsmith, GrowthBook, and plain homegrown flag services are a well-known build-vs-buy case) [category knowledge, not a Flagstone-specific fact — confirm whether Flagstone itself ships an OSS core]. That ceiling is what a prospect compares your bill against, not your competitors' price pages.

## Value metric

Brainstorming mode, six families:

| Family | Verdict | Why |
|---|---|---|
| Seats | plausible, but proven broken | flat 14 months while usage rose 9.5x; evaluations run from application code, not from console logins — fails test 1 (moves with value) and test 5 (cost correlation) |
| Consumption (evaluations) | **deleted for FY**, target for next cycle | best cost/value correlation of any candidate, but unmeterable today without the unfunded quarter — "no funded billing engineering deletes consumption outright" [self-set, SKILL.md step 2] |
| Business outcome (MTU/MAU) | rejected for FY, worth a second look later | the category standard elsewhere (LaunchDarkly, Split, Statsig bill this way); needs unique-end-user dedup across evaluation calls — likely *not* cheaper to build than raw evaluation counting, so it doesn't dodge the budget problem this year |
| Capacity/entitlement (environments, projects) | **selected for FY** | trivially meterable off account records today; known weakness — "breaks when traffic varies wildly inside a fixed capacity" [value-metric-families.md], true here, so treat as a bridge, not the destination |
| Percentage of a flow | deleted | Flagstone touches no payment flow |
| Flat per unit of software | not a fit | no natural single unit below capacity |

One more thing worth flagging to the team before they build the funded metering layer: **raw evaluation count is a risky headline unit on its own.** It's perverse exactly like the worked "test runs" example in this skill's own reference — a team using an efficient client-side cache gets billed less than a team firing evaluate() on every render, i.e. it can punish good engineering [value-metric-families.md]. When the quarter does get funded, budget time to decide between raw evaluations, a normalized/capped count, or MTU — not just "build a counter."

**Chosen architecture: seats (small, kept) + capacity (environments, projects) now, metered evaluation overage layered in once funded.** Two alternatives considered and rejected:

- *Raise seat price, change nothing else* — cheapest, zero engineering, but doesn't touch the structural mismatch; the 9.5x-usage/flat-revenue story repeats next year, and it's the specific anti-pattern this skill's price-point checklist warns against.
- *Ship rough usage-based billing now anyway* — matches the team's instinct, but "unmeterable today" is a delete condition, not a negotiate condition; shipping billing off an unbuilt pipeline produces exactly the disputed-invoice failure mode Step 5 exists to prevent.

## Ladder

| Rung | Contents | Price shape | Trigger to climb |
|---|---|---|---|
| Free | 1 environment, 1 project, community support, full SDK access | $0 | second environment, or production traffic |
| Starter (self-serve) | up to 2 environments, 3 projects, included seats, email support | seat fee (current $19/seat, unchanged) + environment/project fee | 3rd environment, or an admin who isn't a flag user |
| Team | up to 10 environments, unlimited projects, roles, basic SSO, shared billing | seat fee + capacity fee, annual option | security review, residency, SLA ask |
| Enterprise | custom IdP/SCIM, audit logs, residency, SLA with credits, committed-evaluation pricing | "starts at $X", negotiated | — |

All four rungs carry a **published, generous evaluation ceiling per tier** (illustrative: Starter 25M/mo, Team 250M/mo, Enterprise negotiated) — stated as fair-use, checked manually at renewal from whatever aggregate log data exists, not billed per-unit. Label it exactly that to customers: capacity pricing with a fair-use ceiling, not "usage-based" — calling it usage-based when it isn't billed per-unit is the "invented unit" failure mode this skill flags (obfuscation, regardless of intent).

## Free surface

Needs a real number if one doesn't exist today — "generous" isn't a quantity. Recommend 1 environment / 1 project, uncapped seats (console access isn't the scarce resource), with the same evaluation soft ceiling pattern as paid tiers. Compute its total marginal cost as a share of paid gross profit once the aggregate cost-per-evaluation number above exists; that's a same-week calculation, not the quarter-long one.

## Price points

No floor yet — that's the aggregate cost-per-unit gap above. Until it lands, treat every number here as an **experiment with a review date**, per this skill's explicit fallback for "no data at all" [price-point-method.md].

- **Floor:** pending the aggregate cost-per-evaluation figure, modeled at the 90th-percentile account once you have it.
- **Ceiling:** the lower of self-host (if Flagstone ships OSS) and build-it — for this category, a homegrown or OSS flag service is a real, well-trodden alternative, so price the capacity fee to look obviously cheaper than a sprint of engineering plus ongoing on-call, not just cheaper than competitors.
- **Don't touch the $19/seat number in this migration.** One structural change (new capacity axis) at a time; stacking a seat price hike into the same announcement reads as extraction and makes the 9 unhappy accounts in the change plan below harder to hold, per Step 6's "pair the increase with delivered value" rule.

## Mechanics

- Annual discount inside the observed band, ~15–20% [sourced, InnerTrends 100-company sample].
- Volume breakpoints on environment/project count, published.
- Discount ceiling set and pre-approved before the first negotiation.

## Predictability

- Public price page with the capacity fee and the fair-use ceiling stated in real numbers, not adjectives.
- Show whatever evaluation signal you can surface today, even if coarse/batch — the goal is to get customers used to seeing the number before it's ever billed.
- A written fair-use policy (what happens above the ceiling: outreach and a conversation this year, not a service pause) — and say explicitly that metered, real-time billing on this axis is coming, with no date promised until the quarter is funded.
- Itemized invoices: seat fee, capacity fee, separately.

## Change plan

- **Cohort: all 210 existing paying accounts.** Before publishing anything, pull environment/project counts per account (this is the trivial read the prompt already confirms is available) and model who pays more vs. less under the new capacity fee — exactly like the worked example's 31-pay-less/9-pay-more split. Don't publish until that table exists.
- **Grandfather the current $19/seat rate** for existing accounts for a stated window (e.g., 12 months); apply the new capacity fee to new signups immediately.
- **Never retroactively gate anything currently free** (environments, projects, evaluations) — the failure mode here would be quietly capping environments accounts already run at. If any account already exceeds the proposed capacity bands, that account is grandfathered explicitly, named, called before the announcement.
- **Notice:** 60+ days, blog + email, FAQ live same day. Name who answers the public thread and what concession is pre-approved (likely: an extended grandfathering window for anyone who asks).

## Measurement

Track from rollout: seats/account (expect continued flattening — that's fine now, it's no longer the whole story), environments+projects/account, net revenue retention (bottom-up bottom-up band: ~100% good, ~120% great [sourced, Lenny's Newsletter]), free-to-paid conversion (developer median ~5%, about half the non-developer median [sourced, same source]), gross margin per account once the floor exists, billing-related support tickets, and — critically — **evaluations per account, captured however cheaply possible starting now.** This becomes the usage-value correlation evidence (the strongest evidence tier in this skill's own ranking) for sizing the real metered layer next cycle, instead of guessing again.

## Revisit triggers

- The metering quarter gets funded → move immediately to seats (small) + capacity + metered evaluation overage; this interim ladder was never the destination.
- Gross margin drops once the floor is computed.
- Any account's evaluation volume clears another order of magnitude before the next review — a sign the capacity bands are already stale.
- A competitor ships a materially cheaper self-hosted or free-tier alternative — tightens your ceiling.

## Owner

Below the pricing-specialist threshold (~$50M ARR) [sourced, Kyle Poyar] — name a standing group now (product + finance + one customer-facing voice) with the review date above as the forcing function, rather than leaving this to whoever's loudest on the "go usage-based" thread.

## Threshold check

- Value metric: five tests answered in writing above, none silently "no" — pass, with capacity's weak cost-correlation flagged as the known, accepted gap for this interim phase.
- Predictability (target ±20%, under two minutes): not yet testable — needs the published capacity price page first.
- Free surface marginal cost as % of paid gross profit: blocked on the aggregate cost-per-evaluation number — get that this week, not this quarter.
- Every rung has a written trigger: pass, per the ladder table above.
- Never-paywall list: pass — nothing currently free (environments, projects, evaluations already in use) gets retroactively gated.

**Bottom line:** the "go usage-based" instinct is correct about the destination and wrong about the timeline. Build the bridge this year with data you already have; spend the quarter, when it's funded, on the metric that won't need fixing twice.