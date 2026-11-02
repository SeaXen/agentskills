# Quarrystone Pricing Reset — Research Plan

## The plan as budgeted has the sequencing backwards

You're about to spend real panel money finding out what 300 strangers *say* they'd pay, while sitting on two years of instrumented usage data and complete churn records for 90 people who actually *did* pay, or stopped. Behavioral data from real payers beats stated-preference data from a rented panel every time they conflict. Mine what you have first — it tells you what to ask the panel, and it's the only dataset that can validate what the panel tells you back.

Revised order: **internal data → qualitative interviews → competitor teardown → Van Westendorp → synthesis → controlled rollout.** Three months is tight enough that phases below overlap rather than run sequentially.

---

## Phase 0 (Week 1): Fix the segment definition before fielding anything

"Four segments" only useful if defined by the same variable you'll eventually price on. Before the panel goes into field, nail down:

- **The candidate value metrics** — GB ingested/day, active hosts/agents monitored, query volume, seats, retention window (7/30/90 days), or some hybrid. Pull this from the usage instrumentation: which metric actually correlates with account value and expansion, not which one is easiest to explain.
- **The four segments, redefined on that metric** — not generic firmographic buckets (SMB/mid/enterprise) unless that's what the usage data actually clusters into. Run a quick k-means or manual bucketing on the 90 accounts by usage volume × growth rate × role (platform/DevOps vs. security vs. SRE) before deciding the segment cuts.
- **Map every one of the 90 current accounts into a segment.** This is the join key that lets survey results, churn analysis, and usage data talk to each other later. Without it, the Van Westendorp output floats free of anything you can act on.

⚠️ If the four segments were defined by whoever wrote the panel brief without reference to the usage data, stop and redo this first — everything downstream inherits the mistake.

---

## Phase 1 (Weeks 1–3): Mine the 90 accounts — this is your highest-confidence data

Run in parallel with Phase 0.

**Usage-to-price elasticity, from real behavior:**
- For every account, plot usage growth (chosen value metric) against price paid over time. Accounts that grew usage 3x without pushing back on price are under-priced relative to their willingness to pay — you don't need to ask them, you can see it.
- If Quarrystone has changed prices or tiers at any point in two years, treat that as a natural experiment: what happened to expansion and churn in the following quarter, segment by segment?
- Identify the accounts using materially more product than their plan intends (the ones you're currently under-monetizing) versus accounts paying for capacity they don't use (the ones a new value metric could shrink revenue from — flag these early, they're your rollout risk).

**Churn, decomposed by actual reason, not assumed reason:**
- Pull every churned account (should be a meaningful chunk of the 90+ historical base) and classify cancellation reason: price, missing feature, poor fit/never activated, competitor switch, company died, procurement/consolidation. Don't average these — a price-sensitive segment needs a different pricing response than a feature-gap segment.
- Within "price" churn specifically, check what they were actually paying and on what metric — this is direct evidence of a ceiling, more reliable than anything a panel will report.
- Cross-reference churned accounts' usage curves in the 60–90 days before cancellation. A account that flatlined usage before churning had a value problem; one that kept growing and still left had a price problem.

**Output of Phase 1:** a per-segment map of (a) revealed willingness-to-pay ceiling from real churn, (b) revealed willingness-to-pay floor from under-priced growth accounts, (c) which value metric tracks actual value best. This becomes the sanity check every later phase gets measured against.

---

## Phase 2 (Weeks 2–4): Qualitative interviews — the "why" the numbers can't give you

Run alongside Phase 1, informed by its early output.

- **8–10 interviews with recently churned accounts** (last 6–12 months), prioritizing "price" and "never activated" reasons from the classification above. Use 5-why laddering to get past the surface answer ("too expensive") to the comparison point (expensive *relative to what*, valued *against what alternative*).
- **8–10 interviews with your best accounts per segment** — high usage growth, low support burden, renewed without negotiation. These tell you what they'd tolerate paying more for, and which features they'd protect if forced to choose.
- **Ask what they compared you to when buying**, in their own words, before showing them the intern's competitor list. The named alternative is frequently not one of the 7 sites being scraped (could be "built it in-house on the ELK stack," or a budget line item, not a product).
- Recruit from inside your own base, not a panel — sales/CS can pull these lists in a day.

This phase is what makes the Van Westendorp numbers interpretable. A price point means nothing without knowing what it's being judged against.

---

## Phase 3 (Weeks 3–6): Fix the Van Westendorp study before fielding it

The method itself is fine for finding an acceptable price *range*. Three things in the current design will produce numbers you can't trust or act on:

**1. Panel composition is the biggest risk.** ℹ️ A generic 300-person market-research panel will not contain 300 people who buy log-search infrastructure. If the panel vendor is recruiting on demographics rather than role/buying authority, you'll get noise dressed up as data. Require:
- Screener questions that confirm the respondent has evaluated or bought observability/log tooling in the last 12 months, and states their role (platform eng, SRE, security, eng leadership).
- Weight recruiting toward your actual funnel — trial signups who didn't convert, and prospects in the sales pipeline — over cold panel respondents, if the panel vendor allows a mixed-source sample. A blend beats a pure cold panel for a niche B2B infra product.
- Cross-tab every result by "currently uses a log-search tool" vs. not — non-users' price sense for this category is close to meaningless.

**2. Van Westendorp gives no price metric.** Running it against "the product" without anchoring to a specific package (e.g., "50GB/day ingestion, 30-day retention, 5 seats") produces a price range nobody can act on, because respondents will each silently price a different mental picture of the product. Anchor each respondent to a description matching their own segment's typical usage, pulled from Phase 0's segment definitions — otherwise the four segments won't produce four meaningfully different curves.

**3. Van Westendorp alone doesn't test packaging or tiers**, only a single number's acceptability. If the reset includes any tier restructuring (not just a price move), pair it with a lightweight **Gabor-Granger** sweep (a few fixed price points at specific packages, "would you buy at $X") or a simple **MaxDiff on features** to learn what to gate at which tier. This can piggyback on the same panel, same fielding window, marginal added cost — don't let sunk budget on Van Westendorp foreclose adding either.

Once fixed, field weeks 4–6 (2 weeks in field is enough at n=300 across 4 segments; don't over-run this and eat into synthesis time).

---

## Phase 4 (Weeks 3–6, parallel): Reframe the competitor scrape

An intern scraping 7 public pricing pages will get list prices and tier structure — useful for packaging ideas, close to useless for "what do people actually pay," because:
- Infra/observability vendors negotiate hard; list price and street price diverge most at exactly the usage volumes your mid-market and enterprise segments sit at.
- Public tiers often hide the real value metric behind "contact us" past a threshold — exactly where your pricing reset decision matters most.

Redirect the intern's output to two things it's actually good for:
- **Value metric survey** — tabulate what each of the 7 competitors charges *for* (per-GB, per-host, per-seat, flat), not just how much. This is genuinely useful input to Phase 0's value-metric decision.
- **Packaging/tier pattern-matching** — what's gated at entry vs. mid vs. top tier, annual discount rates, overage handling. Feed this into tier design, not into the price-point decision.

Treat any competitor number as a directional anchor for the "next best alternative" floor, never as a target — matching a competitor's number copies their strategy, not their unit economics or their customers' willingness to pay.

---

## Phase 5 (Weeks 7–9): Synthesis into an actual pricing model

This is where the three data streams get reconciled, and where the real work — and the real judgment calls — happen:

1. **Triangulate willingness-to-pay per segment**: revealed (Phase 1 usage/churn), stated (Phase 3 Van Westendorp, screened panel only), and qualitative context (Phase 2). Where stated and revealed diverge sharply for a segment, trust revealed and treat the interview transcripts as the tie-breaker on why.
2. **Finalize the value metric** — the one that correlates with value delivered, scales as customers grow, is hard to game, and matches what Phase 4 shows competitors already train the market to expect (don't invent a metric nobody else uses without a strong reason).
3. **Draft 3 tiers (good/better/best)** against the segment definitions, priced inside the range Van Westendorp bounds and validated against the Phase 1 ceiling/floor evidence.
4. **Run the new model against every one of the 90 real accounts** (retroactively) before touching a single price. Flag every account that would move >30% in either direction — these are your highest-risk migrations and need individual attention (concessions, phased increases, or outreach) before rollout, not after a support ticket.

---

## Phase 6 (Weeks 9–12): Don't switch — roll out

Three months to "reset pricing" should mean three months to a *tested* new price, not a broadcast announcement on day 90.

- **New customers first.** Ship the new pricing to new signups/trials in week 9–10. Clean read on market acceptance with no relationship risk. Watch trial-to-paid conversion for 2–3 weeks before touching existing accounts.
- **Existing accounts: transition, not permanent grandfather.** Full grandfathering leaves money on the table indefinitely and does nothing to fix under-priced growth accounts identified in Phase 1. Move a first wave (the 5–10 lowest-risk accounts from the Phase 5 flag list) to the new price with 60–90 days notice and a concrete reason ("here's what shipped since your price was set"), a lock-in-old-price-if-you-go-annual offer, and a grace window. Expand in waves from there.
- **Expect churn concentrated in the segment(s) that were already flagged as price-sensitive in Phase 1/2** — that's a sign the research worked, not a sign the rollout failed. Budget for it rather than being surprised by it.

---

## Timeline at a glance

| Weeks | Workstream | Owner |
|---|---|---|
| 1 | Segment redefinition on usage data | You + data/analytics |
| 1–3 | Usage elasticity + churn decomposition (90 accounts) | You + data |
| 2–4 | Churned + top-account interviews | You/CS |
| 3–6 | Van Westendorp fielding (fixed screener + anchored package) | Research vendor |
| 3–6 | Competitor value-metric + tier teardown (redirected intern task) | Intern |
| 7–9 | Synthesis, tier/price draft, retroactive test against 90 accounts | You |
| 9–10 | New-customer rollout, watch conversion | You + growth |
| 10–12 | Staggered existing-account migration, wave 1 | You + CS |

## Biggest risks to flag now

- **Panel screener gets skipped to save vendor cost** → Van Westendorp output looks clean but measures the wrong population. Insist on the screener even if it shrinks usable n below 300.
- **Segments get defined by firmographics instead of usage** → survey results can't be joined back to the real accounts, and the whole exercise produces a report instead of a decision.
- **Competitor scrape gets treated as a price target** → you end up anchored to 7 companies' list prices instead of your own customers' revealed value, the opposite of the stated goal.
- **No retroactive test against the 90 real accounts before rollout** → the first time you learn a segment reacts badly is in production churn, not in a spreadsheet.