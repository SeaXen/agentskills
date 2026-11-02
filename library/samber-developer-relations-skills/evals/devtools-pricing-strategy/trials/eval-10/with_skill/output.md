One process note before the deliverable: this skill normally builds the memo section-by-section with sign-off at each step, because a wrong value metric propagates into every line below it. You asked for the whole thing in one pass for Tuesday, so I ran the full analysis myself and flagged every number that's sourced, self-set, or a placeholder you should replace before the board sees it — look for the ⚠️ markers.

---

# Pricing — Ambergate

## Inputs

Model: hosted API gateway, no self-hostable OSS edition of your own. Buyer: a platform/infrastructure lead with a team budget; at $6M ARR and 30 people you almost certainly have some accounts already crossing into procurement, but you haven't told me where that line sits, and I'm not going to invent one — the personal-card → corporate-card → procurement escalation is real but the dollar thresholds attached to it anywhere are folklore. Ask your own sales/CS people where deals actually start needing a PO.

Cost per unit (given): $95/instance/month at the median account, $310/instance/month at the 90th percentile. Current price: $450/instance/month flat, no free tier.

Scale check: $6M ARR ÷ ($450 × 12) ≈ **1,110 gateway instances** under management today. Useful for sizing every dollar figure below.

⚠️ Free alternative's true cost: not given. Your buyer's real ceiling is self-hosting an open-source gateway (Kong, Envoy, Traefik, KrakenD) plus the ops labor to run it — not a competitor's price list. You need this number before you can defend any price ceiling to the board; see Price points below for how to get it fast.

## Value metric

**Diagnosis first, because it's the whole memo.** Your current unit — per gateway instance — sits in the *capacity/entitlement* family (same family as "environments, clusters," priced at deployment time). That family's documented failure mode is: *"breaks when traffic varies wildly inside a fixed capacity."* That is exactly what a $95-median-vs-$310-p90 spread is. This isn't a pricing-level problem, it's a metric problem: your highest-traffic customers — plausibly your best customers — are the ones eroding your margin, and that erosion gets worse every month their traffic grows, for free.

Do the math once, out loud, because it kills the tempting cheap fix: raising the flat price to protect the 90th-percentile account's margin (say, to a 70% target) means pricing at 310/(1−0.70) ≈ **$1,033/month** — for everyone, including the median account that only costs you $95. That's the textbook signal from this skill's own playbook: *"revenue is flat while usage grows... change the metric, not the number."* A flat increase is the wrong tool here.

**Candidates considered:**

| Family | Verdict | Why |
|---|---|---|
| Seats / users | Rejected | A gateway routes machine-to-machine traffic. Three platform engineers can run an instance doing 1M or 1B requests/month — seat count is blind to the thing that costs you money. |
| Consumption (requests processed, or GB transferred — whichever actually drives your infra bill) | **Survivor, promoted to overage layer** | Tracks the exact thing generating the $95→$310 spread. Needs metering investment, but you already have *some* visibility — you couldn't have computed a p90 cost figure otherwise. |
| Business outcome (endpoints managed, backend services routed) | Rejected as the billing metric | Weak cost correlation — an account routing 3 endpoints at huge volume looks nothing like one routing 300 at trivial volume. Worth keeping as a free-tier *limit* dimension, not the meter. |
| Capacity / entitlement (gateway instance — current metric) | **Kept, demoted to base/platform layer only** | Trivially meterable, already the unit customers budget in. The failure mode above is why it can't stay the *only* metric. |
| Percentage of a flow | Deleted | Ambergate doesn't move the customer's money (unless the gateway specifically fronts payment APIs — you didn't say so, so this is out). |
| Flat per unit of software | Not a new candidate | Same critique as capacity above; this is what you already have. |

**Five tests, applied to "requests processed" as the overage unit:**

1. Moves with value — yes, more traffic through the gateway is more value delivered.
2. Already counted — largely yes; most engineering teams watch request volume in their own observability stack regardless of what you bill on.
3. Forecastable — yes, *if* paired with a generous included allowance, a live usage dashboard, and alerts (Step 5 is not optional here).
4. Non-perverse — needs explicit design work: exclude health checks and retries from the billable count, and treat a legitimate traffic spike (a customer's product launch) as an anomaly-alert-plus-credit case, not a bill-shock case.
5. Cost-correlated — yes; this is literally the dimension producing your $95/$310 spread.

None of the five is a flat "no." The metric survives.

**Chosen architecture: hybrid.** Keep the $450/month instance fee as the platform layer (predictability, no disruption for ~90% of accounts), add an included throughput allowance, meter overage above it, and add a committed-spend option for accounts that outgrow self-serve. Two alternatives considered and rejected as the primary move, not deleted — they're the honest bracketing options:

- **Status quo (flat $450/instance, no change).** Zero effort. Gives up: the margin leak doesn't just persist, it compounds — every month your best customers' traffic grows, they get more valuable to you at cost and no more valuable to you at price.
- **Pure consumption (bill entirely on requests/GB, drop the instance fee).** Best possible cost-to-price correlation. Gives up: rewrites every one of your ~1,110 existing contracts at once, abandons the $450 anchor your customers already budget against, and needs a full metering-plus-dispute pipeline — a standing job, not a quarter of work. This is where you may end up in 18–24 months if traffic concentration keeps rising, not where you land by Tuesday.

Recommend the hybrid. It's the one repricing move that fixes exactly the diagnosed problem, reuses cost visibility you already have, and doesn't touch the number 90% of your base already trusts.

## Ladder

| Rung | Contents | Price shape | Trigger to climb |
|---|---|---|---|
| Free | **Not launching now — see below** | — | — |
| Starter (self-serve) | 1+ gateway instances, included throughput allowance per instance (set at roughly your current median usage — see Price points), core routing/auth, usage dashboard, email support (2 business days) | $450/instance/month + metered overage above allowance | approaching the allowance repeatedly, needing shared billing across a second team, needing an admin who isn't a hands-on user |
| Team | everything in Starter, plus roles/permissions, one consolidated invoice across all instances, longer log retention, basic SSO, priority support (1 business day), volume breakpoints | published per-instance rate at volume breaks + overage, annual option | security review, data residency need, an SLA requirement |
| Enterprise | custom IdP/SCIM, granular RBAC, audit logs, residency, dedicated/VPC deployment, SLA with credits, invoicing/PO, custom terms | "starts at $X/year," negotiated | — |

Gate placement check against the never-paywall list: core routing, auth, SDKs, usage visibility, config/log export, and security patches stay available at every rung, always. Basic SSO sits at Team, not Enterprise — the sso.tax convention (10% price-hike ceiling before it reads as an identity-tier gouge) puts custom IdP/SCIM/directory-sync at Enterprise instead, which is where the real marginal cost and the real buyer (compliance, not the user) sit.

**Team is a real, new rung, not cosmetic.** Right now a customer with 10 instances just pays 10× $450 with no org-level governance layer at all. Team packages that as roles, one invoice, and SSO — capability you don't have to gate behind more instances, because it's orthogonal to instance count.

## Free surface

**Recommendation: hold at zero for now.** Not because free tiers are wrong for this category — they aren't, and the developer-adoption-precedes-purchase argument (O'Grady, *The New Kingmakers*) is a fair reason to want one eventually — but because you have an open question that has to be answered first: is the $95 median cost dominated by a **fixed per-instance floor** (minimum compute footprint to run any gateway instance at all) or by variable throughput? If it's mostly fixed, a free instance costs you close to $95/month regardless of how little traffic it carries, and a "free tier" becomes an expensive multi-tenant-isolation problem, not a cheap marketing line.

Resolve that question, then revisit at the first quarterly pricing review (below) as a Phase 2 decision — a shared/multi-tenant free surface if the fixed-cost floor is real, a small dedicated-instance free tier if it isn't. Don't let it compete with the metric fix for engineering time this quarter; the metric fix is the one addressing money you're already losing.

## Price points

**Floor.** Marginal cost $95/instance median, $310/instance at the 90th percentile (given). Gross-margin target: this skill's own baseline for a pure software product is 80%, for pure usage-based pricing it's 62% (infrastructure lands directly in COGS) — both sourced, neither is you. Ambergate is a hybrid, so **70% is a self-set target for the p90 account**, roughly the midpoint, chosen because you keep a fixed platform-fee anchor rather than going pure-usage.

Today's p90 margin is 31% ($140 on $450) — below even the 62% usage-only floor, which is the clean, quantified case that something has to change before the board asks why your best accounts are your thinnest.

**Recommended near-term number, not the long-run target.** Closing the full gap to 70% in one step prices the overage at roughly $717/month on top of the $450 base for a p90 account (a 2.6× bill increase) — technically correct, not boardable as a first move. Instead:

- Set the included allowance at the throughput level implied by the $95 median cost, so the median account's bill does not move.
- Price overage so a p90 account lands near **55% margin in year one**: $310 / (1 − 0.55) ≈ $689/month total, i.e. roughly **+$239/month** above the $450 base for that specific decile.
- State a year-two target of 65–70% at p90 explicitly in the plan, reviewed at each quarterly cycle below.

⚠️ This is built from only two data points (median, p90) plus an assumed target margin — it's the right shape, not the exact final rate. Before Tuesday, pull the actual cost-per-million-requests (or per-GB, whichever is the real driver) from your infra billing so the overage rate is priced against a real curve, not an inferred one from two summary numbers.

**Ceiling.** For a category with a live open-source alternative, the binding ceiling is almost always "build it" — self-hosting Kong/Envoy/Traefik plus the ops labor to run it, not a competitor's list price. ⚠️ You haven't given me that number, and I'm not going to fabricate one to make this slide look finished. Two ways to get it before Tuesday, both cheap:
- Pull 3–5 recent loss reasons from CS/sales where "we'll self-host" was cited, and cost out what they'd actually be running (compute + roughly a quarter-FTE of ops time, the same shape as this skill's own worked example: infra cost plus loaded engineer-hours).
- Pull current public prices for Kong Konnect, Apigee, AWS API Gateway, Tyk Cloud, and Traefik Enterprise the day before the meeting — competitor prices are the weakest evidence in this whole memo (cheap, and just evidence of what someone else guessed), use them only to bound the number, never to justify it.

If that ceiling comes back below your $689 p90 number, that's not a pricing failure — it means the cost structure needs work before the price does, and it's a better thing to discover this week than in a lost-deal report next quarter.

**Evidence weighting used above:** your own two cost data points first (strongest available), competitor prices last (weakest, cheapest) — consistent with the evidence-strength order this skill uses; you have no win/loss or Gabor-Granger data yet, which is itself worth fixing before the *next* pricing cycle.

## Mechanics

- **Annual discount:** 15%, inside the observed 15–20% band that over half of a 100-company sample uses, anchored near the "two months free" convention (sourced, InnerTrends). Don't stack with volume breaks.
- **Volume breakpoints:** published discounts at 10+ and 25+ instances (⚠️ self-set defaults — check them against your actual instance-count distribution, which you have and I don't).
- **Committed spend:** available at Team/Enterprise — an annual floor in exchange for a lower overage rate, the natural bridge for accounts already running near their allowance every month.
- **Discount ceiling:** cap discretionary discounting at 20%, approvable only by whoever holds the finance seat on the pricing group below — anything deeper requires a multi-year commitment, decided before the first negotiation, not during it.

## Predictability

- Public price page with the base fee, the included allowance, and a calculator for overage.
- Live usage-vs-allowance dashboard, projected to period end, exposed through your API too, not just the UI.
- Alerts at 70/85/95% of the allowance, plus an anomaly alert at a sudden multiple of the account's own trailing average.
- **Cap style — this needs a deliberate call, not the generic default.** This skill's default is "hard cap for hobby/dev, soft cap for production." A gateway instance is usually *already* in a live request path even for small accounts — a hard cap here doesn't just stop a build, it takes down a customer's production API traffic. Recommend **soft cap as the default everywhere**, including Starter: service continues, bill accrues, alert fires. Reserve any pause behavior for accounts that explicitly opt into it (e.g., a genuinely non-production sandbox instance), not as the standing default.
- Itemized invoices: platform fee, included allowance, overage quantity × rate, credits — each its own line.
- A pre-approved runaway-usage credit policy, written down before you need it — Netlify's $104K bandwidth bill is the citable case: they forgave it and published a standing policy, but the cap, the alert, and the anomaly detection are what should have caught it first. Don't ship the overage mechanism without this.

## Change plan

This is the highest-risk part of the whole memo, because you're introducing a cap on something that was, in effect, unlimited before. Handled wrong, this is structurally the exact "retroactive gating" failure this market punishes hardest — the difference between "new capability, new price" (fine) and "we're now charging for what used to be free" (fork-and-front-page-thread territory) is entirely in how the transition is framed.

**The move that keeps this safe:** grandfather every existing account's current allowance at its own trailing-90-day usage average, at no cost increase, permanently — for that level of traffic. Overage only bills growth beyond that baseline, from a stated effective date forward. This reframes the announcement from "we're charging you for existing usage" to "we're not charging you for anything you already do; new headroom for growth costs extra" — which is the survivable version, not the Unity version.

1. **Cohorts:** ~1,000 accounts at or below the included allowance (no bill change — say so explicitly, first sentence of the announcement); the top-decile accounts (~110 accounts) whose trailing usage exceeds the new allowance, who get grandfathered per above; anyone under an existing annual contract (⚠️ you haven't told me if these exist — check before publishing a date).
2. **Grandfathering:** indefinite, tied to *usage level* not a calendar window — a customer's grandfathered allowance only becomes binding once they'd need to exceed their own historical baseline.
3. **Notice:** 90 days minimum before the new overage mechanism takes effect. Infra budgets are usually planned quarterly or annually; a shorter window is exactly the "one month is not notice for anything a budget covers" failure this market has punished repeatedly (PlanetScale, Docker, Unity).
4. **Pair it with delivered value:** ship the usage dashboard and calculator simultaneously — genuinely new value, not a cost pass-through with a coat of paint.
5. **Never reverse:** nothing here removes an existing free capability; it adds a metering layer with a hard floor under every existing account. Keep it that way in the announcement copy — don't let "capped allowance" read as "thing you used to get unlimited, now you don't," even though technically that's the mechanism. The grandfathered baseline is what makes that framing true, not just convenient.
6. **Personal outreach:** every one of the ~110 top-decile accounts gets a call from you or the account owner before the public announcement goes out — not after.
7. **Public thread:** you (CTO) or a named customer-facing lead answers it, with a pre-approved concession (a temporary allowance bump, or a 6-month price lock for anyone who asks) decided before the thread opens, not during it.

## Measurement

Track monthly, review quarterly:

| Metric | Baseline | Target |
|---|---|---|
| Gross margin per account (p90 cohort) | 31% | 55% year 1, 65–70% year 2 |
| Overage revenue as % of total revenue | 0% (new) | flag if it exceeds ~45% — that means allowances are set wrong, not that overage is working |
| Share of accounts within 15% of their allowance | unknown | track from launch |
| Average discount | unknown ⚠️ | ceiling 20% |
| Billing-related support tickets / 100 accounts | unknown | the cleanest proxy you have for whether the new bill is actually predictable |
| Net revenue retention | unknown ⚠️ | ~110% land-and-expand SMB good, ~130% enterprise great (sourced band; label it as such when you show the board — you don't have a baseline yet) |

Full review at Q1 next year; revisit sooner if any of the triggers below fire.

## Revisit triggers

- P90 gross margin below 55% for two consecutive months after launch.
- Overage revenue exceeds 45% of total revenue (allowances mis-set, not a win).
- More than 5% of accounts hit the anomaly alert in a month (cap defaults are wrong).
- A competitor ships a free hosted tier that changes your ceiling math.
- Top-decile cost climbs past $310 (re-underwrite the floor — infra costs move without asking).

---

## Measurement and pass threshold — reported explicitly

- Value metric: all five tests answered in writing, none "no" (test 4 needs the retry/health-check exclusion built in, not just assumed). **Pass, conditional on that build item.**
- Predictability: target customer estimates their bill within ±20% in under two minutes — **not yet testable**, the calculator doesn't exist yet. Build it before claiming this passes.
- Free surface total marginal cost as a share of paid gross profit: **not applicable** — no free surface is launching this cycle.
- Every rung has a written trigger event, every rung below Enterprise is public: **pass**, per the ladder table above.
- Gross margin at the proposed price clears the target at the 90th-percentile account: **not yet** — 55% year-1 target vs. 70% self-set target is a stated gap with a stated glide path, not a pass. Flag this to the board as a two-year plan, not a one-quarter fix.
- Never-paywall list: no violation. SSO stays near the 10% surcharge convention by sitting at Team, not Enterprise.
- Change plan: every cohort named, grandfathering explicit and usage-anchored, no public commitment reversed. **Pass.**

Bottom line for the board: don't raise the price, fix the metric. The number that's wrong is $0 of overage on your most expensive accounts, not $450.

---

## Who should own this going forward

At $6M ARR and 30 people, you're well below the roughly $50M ARR mark where a dedicated pricing hire typically shows up (Kyle Poyar), and the "CEO/leadership owns it" pattern from the OpenView survey of expansion-stage SaaS companies describes a later stage than yours — so neither "wait for a specialist" nor "it's just a leadership call" fits yet. The risk at your stage isn't the wrong owner, it's neglect: the widely-cited Patrick Campbell figure is that companies spend something like 10–14 hours a *year* on pricing, deliberately. That's roughly what produced the situation you're in now — nobody was checking cost-to-serve against price by cohort until this exercise.

**Recommendation: a standing three-person pricing council, not a single owner.**

- **You (CTO)** — you hold the cost-to-serve data and you're the one who caught this gap; own gross margin per account and the floor.
- **A finance/revenue owner** — whoever tracks ARR and billing today; owns overage-as-%-of-revenue, average discount, and NRR.
- **A customer-facing owner** — whoever runs support or CS; owns billing-ticket volume and price-related loss reasons, because they'll hear about a confusing bill or a p90 account's reaction before the P&L does.

Give the council the quarterly review date already in the Measurement section above — that's now your deliberate-attention floor, and it's already more structure than the 10–14-hours-a-year norm implies most companies have. Revisit whether a dedicated owner is needed as you approach the $50M ARR mark Poyar cites, not before.