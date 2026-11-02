Using the **devtools-pricing-strategy** skill. I've read the SKILL.md and all six reference files (value-metric families, packaging ladder, price-point method, evidence base, change-case corpus, worked memo). This is the "cloud version of your own Apache-2.0 project" invocation — self-host ceiling and open-source rung go first.

Below is the complete memo, one go since you asked for the deliverable rather than a live back-and-forth. Every number is tagged **[given]** (from you), **[assumed]** (an illustrative placeholder I set because you didn't have the figure — swap in your real one), or **[baseline]** (this skill's own default, not an industry standard).

---

# Pricing — Kestrelbase Cloud

## Inputs

- Model: hosted version of an Apache-2.0 self-hosted product. Engine stays open. **[given]**
- Existing base: ~1,400 self-hosted deployments **[given]** — this is both your best lead-gen channel and the audience that already knows the true cost of the alternative.
- Buyer: a platform/infra lead with a team budget for the core rungs; procurement enters once residency, SLA or custom terms are asked for. **[assumed — confirm]**
- Marginal cost: $0.0009 / million points ingested, $0.011 / GB-month stored. **[given]**
- Self-host true cost, mid-sized team: $260/month infra + 5 eng-hours/month. **[given]** Valuing the labor at $120/hr loaded (mid-market senior/SRE rate) **[assumed]** → **$860/month all-in**.
- Nearest managed competitor: $400/month flat. **[given]**
- Heaviest 10% of beta accounts cost ~4x the median account. **[given]** — this is your 90th-percentile signal; use it, not the average, for the floor (this skill's baseline).

**Finding worth flagging before anything else:** the binding ceiling is *not* self-hosting. $860/month all-in for self-hosting is *higher* than the competitor's $400 flat. The number Cloud has to beat is $400, not $860 — self-hosting only wins on ceiling math for the labor-averse who already run it, not on raw cost. Price above $400 and you lose to the competitor on price with strictly more product risk (unproven service) attached.

## Value metric

Brainstorming mode, six families against the five tests:

| Family | Verdict | Why |
|---|---|---|
| Seats | rejected | A TSDB is written to by pipelines and agents, not logged into by headcount. Seat count would sit flat while ingestion scales orders of magnitude — the exact seat-collapse pattern the reference catalogue warns about. |
| Consumption (points ingested + GB-month stored) | **selected** | See five tests below. |
| Business outcome (e.g. "devices monitored") | rejected | No single outcome unit is universal across Kestrelbase's actual use cases (IoT, financial tick data, observability) — the general-purpose nature of a TSDB breaks this family. |
| Capacity/entitlement (cluster size, retention window) | rejected as headline, kept as tier shape | Predictable and trivially meterable, but correlates only loosely with your actual cost driver (points + bytes), and you were given the real unit cost — using an abstracted capacity number would throw that away. |
| Percentage of a flow | deleted | Not a payments product. |
| Flat per product | rejected | Ingestion volume varies by orders of magnitude across a hobby deployment and an industrial sensor fleet — the "one busy monorepo" failure mode. |

Five tests, in writing, for consumption (points ingested + GB-month stored):

1. Moves with value? Yes — more data trusted to the service is definitionally more value extracted.
2. Already counted? Yes — ingestion rate and disk usage are the two metrics every TSDB operator already watches; this is the least foreign metric you could pick.
3. Forecastable? Yes for ingestion (device count × sample rate is usually known in advance); storage trails predictably behind it.
4. Non-perverse? Yes — nothing about paying per point ingested rewards bad engineering or punishes retries/health checks the way a per-test-run or per-request-with-retry metric can.
5. Cost-correlated? Yes by construction — it's literally the unit your given marginal costs are denominated in.

All five pass. One re-ranking factor applies: you already have a working metering pipeline — the beta program's account-level cost data (the "4x" figure) proves it's instrumented and funded today. Per the skill's re-ranking rule, an existing metering pipeline promotes consumption to the top of the default efficiency ordering, which otherwise buries it. That rule fires here.

**Two other architectures considered, then rejected in favor of a hybrid:**

- **A — Pure metered, no base fee.** Bill = ingestion × rate + storage × rate, nothing else. Gives up a predictable floor (bad for your own revenue forecasting and for the free-tier cost model) and gives small accounts a $0.03 line-item invoice that reads as an accounting nuisance, not a subscription.
- **C — Capacity tiers, consumption only as overage.** ("Up to 10M pts/day, 50GB = $X/mo.") Predictable for the customer, but the heaviest-decile accounts either blow through a tier for free until the next coarse jump, or get punished by a jump that also catches accounts nowhere near that heavy. Weak cost correlation, exactly the failure mode the reference calls out.
- **B — Hybrid: platform fee + included allowance + metered overage + committed spend at the top — recommended.** This is the standard mature-devtool shape, and it's the only one of the three that gives light accounts a single predictable number *and* keeps the heaviest decile's revenue tracking their actual cost via overage.

Seats are **not** the billing axis anywhere in this design — unlimited console seats ship free from Team upward, so nobody is incentivized to share logins.

## Ladder

Built in efficiency order (self-serve paid first), shown in customer-journey order:

| Rung | Contents | Price shape | Trigger to climb |
|---|---|---|---|
| **Free** | Full core engine access, 100M points/mo, 1GB-month stored, 7-day retention, 1 project, community support, no card | $0 | exceeding the allowance, or needing retention past a week |
| **Starter** | 5B points/mo + 50GB-month included, 30-day retention, up to 3 seats, email support | $49/mo + $0.0045/M points and $0.055/GB-month overage | a second team, or an admin who never ingests data |
| **Team** | 25B points/mo + 250GB-month included, 90-day retention, unlimited seats, roles, shared billing, basic SSO, 1-business-day support | $249/mo + same overage rates, 16.7% off annually | security review, residency, or an SLA requirement |
| **Enterprise** | Custom IdP + SCIM, directory sync, granular RBAC, audit logs, EU/US residency, private deployment option, SLA with credits, invoicing | starts at $40k/year **[assumed anchor]**, committed volume at a discounted overage rate | — |

Everything above is illustrative sizing **[assumed]** built from your real cost figures — the rates are not.

**Never-paywall check:** core engine, SDKs, CLI are already Apache-2.0 and stay that way regardless of Cloud — nothing here takes anything from the 1,400 existing installs. Data export works at every rung, forever. Basic SSO sits at Team, not gated as an enterprise surcharge (the sso.tax bar is 10%; Team's list price makes SSO a rounding error, not an identity tax).

## Free surface

100M points/month, 1GB-month stored, 7-day retention, one project, no card. **[assumed sizing]**

- Raw marginal cost per free account: 100M × $0.0009 + 1 × $0.011 ≈ **$0.10/month**.
- Total exposure if all 1,400 known self-hosters tried the free tier simultaneously: ~$140/month raw — trivial. **[assumed, upper-bound scenario]**
- Ceiling on total free-tier cost as a share of paid gross profit: set at 10%, reviewed monthly once real signup data exists. **[baseline default, unmeasured pre-launch]**
- Abuse policy: rate ceiling on the ingestion API, one free workspace per verified org domain, no separate mining/spam carve-out needed since ingestion itself is metered and capped.
- Warnings at 70/85/95% of the monthly allowance **[baseline]**, then writes queue/throttle — reads stay live, no data deleted as enforcement, ever.

## Price points

**Floor.** Raw unit cost is given: $0.0009/M points, $0.011/GB-month. Adding an illustrative support-hours line (0.3 hrs/account/month at $80/hr loaded **[assumed]** ≈ $24/account/month for typical accounts, more for heavy ones) and modeling at the 90th-percentile account (given: ~4x median cost): floor cost for a heavy account ≈ $12.60 raw + ~$80 support **[assumed]** ≈ $93/month.

Target gross margin: 80% (software median, sourced), chosen deliberately over the 62% usage-only baseline because your actual infra COGS ratio is unusually low relative to price at plausible volumes — flagged explicitly since this is a judgment call, not a given fact. At 80%, overage rates are raw cost × 5: **$0.0045/M points, $0.055/GB-month** — these are the published overage rates above.

**Ceiling.** Lowest of: self-host all-in $860/mo, competitor $400/mo flat, build-it (n/a — it's already built and downloadable), do-nothing (n/a — a database is an "enable," not a "nice to have"). **Binding ceiling = $400/month.**

**Placed numbers.** Team at $249/month sits at 62% of the $400 ceiling and 29% of the $860 self-host all-in cost — a clear, legible win against both real alternatives without reading as a fire sale. Starter at $49/month undercuts even the infra-only slice of self-hosting ($260/mo) by 5x before counting the 5 hours/month of labor at all.

Evidence used, in efficiency order: no live usage-value correlation exists yet (pre-launch), so this is priced from the floor-plus-margin-and-ceiling-sanity-check method for "no data at all," published as an **experiment with a review date**, not a final number. Once beta/GA data lands, re-derive from usage-value correlation and win/loss — that ranks above the reasoning used here.

**Sanity check across three usage profiles** (the predictability test: estimable within ±20% in under two minutes):

1. Hobbyist inside free tier → **$0**, exact.
2. Median beta profile (3B pts/40GB) → inside Starter's allowance → **$49/mo flat**, exact.
3. Heaviest-decile profile (~10B pts/140GB, ~4x median cost) → inside Team's allowance → **$249/mo flat**, exact.
4. A genuine outlier beyond Team's allowance (50B pts, 600GB) → $249 + (25,000M × $0.0045) + (350 × $0.055) = $249 + $112.50 + $19.25 = **$380.75/mo** — still under the $400 ceiling even at 2x Team's included volume, computable from the two published rates alone.

All four pass the two-minute/±20% bar without a support call.

## Mechanics

- Annual discount: 16.7% ("two months free" anchor, sourced), applied to Starter and Team, no stacking with volume breaks.
- Volume breakpoints published on both overage rates at higher committed thresholds (mirrors the worked pattern — publish the step-downs, don't hide them behind a sales call).
- Committed spend: available once an account's trailing overage exceeds ~$500/month, at a further discount off the list overage rate — the natural bridge into Enterprise.
- Discount ceiling: 20%, approvable only by the pricing owner named below; anything deeper requires a multi-year commitment.

## Predictability

- Public price page with the four numbers above, plus a calculator taking points/month and GB-month as inputs.
- Live usage against the included allowance, a projection to period end, mirrored on a usage API.
- Alerts at 70/85/95% of allowance **[baseline]**, plus an anomaly alert at 3x the trailing daily ingestion rate — a TSDB's version of Netlify's bandwidth-spike failure is a sensor fleet misconfigured to over-report; design for it now, not after the first bill-shock thread.
- Cap defaults: Free and Starter default to a **soft pause on new writes** once the allowance is hit (reads stay live, nothing is deleted) — framed as a pause, not a hard cutoff, because dropping writes on a database is worse than the bandwidth-cap case the "hard cap" language was written for. Team and Enterprise default to soft cap: service continues, overage bills, alert fires.
- Itemized invoices: plan fee, included allowance, ingestion overage, storage overage, credits — each its own line.
- A pre-approved runaway-usage credit (illustrative: up to $500 **[assumed]**) for support to grant without escalation when the anomaly alert clearly traces to a misconfiguration, not real growth.

## Change plan

Not a repricing — this is a new product, and the existing 1,400 self-hosted deployments owe nothing to the launch:

- **Self-hosted/OSS users:** unaffected, permanently. State explicitly, in the first paragraph of the launch announcement, that the Apache-2.0 engine's scope of what stays free is not changing and will not close later — silence here reads as intent to close and gets priced in immediately by exactly the community you're launching to.
- **No existing paying cohort** to grandfather — there is no live price being changed.
- Publish rates at launch, not "contact us" for the first three rungs — a bottom-up motion where entry pricing is hidden is read as a lead form, per the skill's own rule.

## Measurement

Pre-launch, so these are targets from day one, not baselines yet:

- Free-to-paid conversion: developer-product median is ~5% (sourced), track by cohort at account level within six months.
- Net revenue retention: ~100% good / ~120% great for bottom-up (sourced) — this only starts moving once overage billing has months of history.
- Share of accounts landing near a tier boundary (signals mis-sized allowances).
- Average discount and its trend against the 20% ceiling.
- Gross margin per account, floor at 70% even though the illustrative model above clears 80%+ comfortably — leave headroom, given the support-cost line above is a guess.
- Billing-support tickets per 100 accounts — the cleanest proxy for whether the two-dial calculator is actually working.
- First full pricing review: two quarters post-GA.

## Revisit triggers

- Gross margin per account (especially the 90th-percentile cohort) below 70% for two consecutive months.
- Overage revenue exceeding 45% of total — means the included allowances were set too small.
- The competitor drops below $400/month, or ships a self-hostable/open edition of their own — the ceiling math above moves immediately.
- More than 5% of accounts hitting the anomaly alert in a month — cap defaults are wrong, not the customers.
- Real usage data shows the median/heavy-decile profiles used here (3B pts/40GB and ~10B pts/140GB) are wrong by more than 2x — the whole tier sizing above was built on illustrative numbers and needs re-anchoring to actual beta telemetry the moment it exists.

## Owner

No ARR figure given, so treat this as pre-$50M-ARR by default: name a standing group — product, finance, one customer-facing voice — with the review date above, rather than leaving it to whoever shipped the launch. Do not wait for a dedicated pricing hire; that role typically doesn't arrive before ~$50M ARR (sourced), and the risk at this stage is neglect, not under-resourcing.

## Threshold check

- Value metric: five tests answered in writing, none "no." **Pass.**
- Predictability: three of four usage profiles land on an exact flat number; the fourth resolves from two published rates in under two minutes. **Pass, pending real usage data to replace the illustrative profiles.**
- Free surface: total marginal cost is a number ($0.10/account), ceiling set at 10% of paid gross profit. **Pass, ceiling unmeasured until launch — flagged, not resolved.**
- Every rung below Enterprise is published, and every rung has a written trigger. **Pass.**
- Margin at 90th-percentile account clears target using illustrative volumes. **Conditional pass — re-run this specific check the day real beta usage numbers replace the assumed 3B/40GB and 10B/140GB profiles; that's the single most load-bearing assumption in this memo.**