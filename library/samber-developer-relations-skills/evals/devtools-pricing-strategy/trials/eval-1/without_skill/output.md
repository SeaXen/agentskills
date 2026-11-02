**Recommendation: don't meter evaluations this year. Switch value metric to what you already read (projects + environments), add a cheap monthly usage band on top, defer real-time metering to next budget cycle — and even then, never price raw eval count.**

**Diagnosis.** Seats flat 14 months, evals up 9.5x (40M→380M). Usage decoupled from headcount — flag evaluation is machine-to-machine traffic, not a collaboration metric. Per-seat pricing caps revenue below value delivered by design. Current run-rate: 19 × 5.4 seats × 210 accounts ≈ $21.5K/mo. Tiny relative to 380M evals/mo served — you're underpricing the infra, not just mispricing seats.

**Don't build billing-grade per-evaluation metering.** Two separate mistakes stacked in "go usage-based":
1. Spending a quarter on metering before knowing market accepts usage pricing at all.
2. Pricing raw eval count even once built. Bad value metric — unpredictable bill, no clean link to perceived value, feels like a tax not a fair charge. LaunchDarkly and peers price on MAU/connections/seats, never raw evaluations, for this exact reason.

**Phase 1 — repackage now, current data, no new engineering (days):**
1. Pull projects + environments per account, last 14 months. Check correlation against eval growth. This confirms or kills the proxy before pricing commits to it.
2. Build 3 tiers gated on projects + environments (seats stay, low weight). Example: Starter — 3 projects / 2 envs. Growth — 15 projects / 5 envs. Scale — unlimited + SSO + audit log + SLA.
3. Flat price per tier, not seat-multiplied. Growth is the anchor tier.

**Phase 2 — coarse usage signal, parallel, cheap (days, not a quarter):**
4. Monthly batch job counting evaluations per account off existing logs — you already count 380M/mo somewhere for ops. Aggregation query, not new instrumentation.
5. Use the count only to place accounts in a usage band, monthly, self-serve visible. Overage = flat step price per band crossed ("+$X/mo per +25M evals"), never per-unit billing. This skips the expensive parts — proration, real-time enforcement, dispute handling — which is almost certainly where the "quarter" estimate actually lives.

**Phase 3 — real-time billing-grade metering. Next budget cycle, conditional.** Build only if Phase 1+2 data shows projects/environments correlate poorly with real usage, or customers demand precise self-serve dashboards. Still price on bands, never raw evaluations.

**Rollout on the 210 existing accounts:**
- New pricing on new signups first — clean read before touching the base.
- Grandfather current accounts ~2 renewal cycles (6 months), not forever.
- Communicate 3+ months ahead: usage grew 9x, plan reflects it, headroom included.
- Offer: lock legacy per-seat price if they move to annual now.
- Expect churn concentrated in lowest-usage, most price-sensitive accounts — acceptable, that segment is least profitable relative to infra cost anyway.

**Watch:** net revenue retention (should rise), churn on the grandfathered cohort, new-tier conversion, and whether the projects/environments proxy actually tracks real usage (step 1's output).

Next: run step 1 — pull projects + environments per account against eval growth. Confirms the hybrid model holds before anyone touches the pricing page.