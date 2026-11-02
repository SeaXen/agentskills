# Business case: half-time technical writer for release communication

## The ask

Fund a 0.5 FTE technical writer (or fractional/contract equivalent) dedicated to release notes, changelogs, and in-product update messaging. Run it as a **two-quarter pilot** with defined KPIs before converting to a permanent line — this gives the CFO an exit ramp instead of an open-ended headcount commitment, which is usually the fastest way to get a "yes."

## The problem today

Release communication is currently a byproduct of engineering time, not a deliberate function:

- Engineers or PMs write release notes as an afterthought, at their fully-loaded rate — 3-5x a technical writer's cost — on a task outside their comparative advantage.
- Quality is inconsistent: some releases get detail, others get "bug fixes and improvements," which is functionally invisible to users.
- No one owns the funnel from "we shipped this" to "the customer knows, understands, and uses it." That gap is where feature adoption, expansion revenue, and renewal confidence leak out quietly — it doesn't show up as a line item, so it never gets fixed.

## ⚠️ On the two stats you're thinking of — flag before you use them

I don't have live web access this session (search was blocked), so I can't pull the exact citations. Rather than hand you a number I can't stand behind in front of a CFO, here's the honest state of each:

- **Linear**: Real and verifiable — Linear's changelog is widely cited in product/PM circles (Lenny's Newsletter, Reforge, their own blog/talks) as a best-practice example of treating release notes as a product-marketing surface (polished write-ups, embedded video/GIFs, changelog as brand asset). I don't have a specific credible "X% retention/upgrade lift" figure attributable to Linear — I'd be fabricating precision if I gave you one. Use it as a **qualitative exemplar** ("here's what best-in-class looks like"), not a quantitative citation. If you want the number, it's worth a direct search or asking a Linear team member — they've talked about this on podcasts.
- **App Store study on note length vs. ratings**: I can't verify a specific study with a specific percentage right now, and there's actually mixed academic literature on update frequency/ratings (some research finds frequent updates correlate with *lower* ratings when they introduce bugs, which cuts against a naive "more updates = better" framing). Don't cite a number here until you've found and read the primary source — search terms that should get you there: `"release notes" app store rating study`, `Apptentive OR Sensor Tower release notes ratings`, or app-store-review-mining papers from software engineering venues (MSR, ICSE). If a colleague half-remembers it too, it likely exists — just don't be the one who cites the wrong number in the room.

Better move: build the case on math the CFO can't dispute, below, and use Linear only as color.

## The financial case (fill in your own numbers — this is a model, not a memorized stat)

A CFO trusts a formula more than a footnote. Four independent levers, any one of which likely justifies the cost alone:

| Lever | Formula | Why it's conservative |
|---|---|---|
| **Churn reduction** | ARR × (churn-rate reduction attributable to comms) | Even 0.3–0.5pp of annual churn avoided on a mid-size ARR base typically exceeds a half-time salary outright. Users who don't know why they're paying more, or what they're missing, cancel silently. |
| **Support deflection** | ("what changed?" tickets/month) × 12 × (cost per ticket, ~$15–25 loaded is a common industry range) | Every unclear release generates predictable "did you change X" tickets. This is pure avoidable cost. |
| **Expansion/upsell lift** | (expansion ARR currently at risk from low feature awareness) × (estimated uplift %) | Product-led expansion depends on customers *knowing* a feature exists. Undocumented features don't get adopted, full stop — no study needed, it's definitional. |
| **Engineer time recovered** | (hours/month engineers/PMs spend drafting release copy) × 12 × (fully loaded engineer hourly rate) | This is the easiest one to make airtight: you're not adding a cost, you're moving an existing cost to someone 3-5x cheaper per hour who's also better at it. |

Plug in your actual ARR, churn, ticket volume, and engineer rate — the model holds even under pessimistic assumptions, because the role is cheap relative to any one of these levers moving even slightly.

## Cost side

Ranges only — verify against current market data before finalizing:

- **France/EU, employee**: mid-level technical writer, full-time fully-loaded (salary + charges patronales ~40-45%) roughly €53k–€75k/year → half-time ≈ **€28k–€40k/year**.
- **France, freelance/contract**: day rate ~€350–€550, ~10 days/month → **€42k–€66k/year** (higher than half-FTE due to margin, but zero commitment/severance risk).
- **US, employee equivalent**: full-time fully-loaded ~$80k–$100k/year → half-time ≈ **$40k–$50k/year**.

Either structure is a rounding error against the ARR-linked levers above once the company has more than a few hundred customers or a few million in ARR.

## Risk of inaction

- Nothing catastrophic happens immediately — this is exactly why it never gets prioritized. It shows up as a slow bleed: flat feature adoption, support tickets that never quite explain themselves, renewal calls where CS has to reconstruct "what did we even ship this year," and engineers quietly resenting the writing tax.
- Competitors with strong release communication (Linear being the visible example) compound a perception-of-velocity advantage even when actual shipping speed is comparable — this affects competitive deals, not just retention.

## Recommended pilot structure

1. **Scope**: all customer-facing release notes, changelog, and in-app "what's new" surfaces for two quarters.
2. **Baseline first**: before hiring, snapshot current feature-adoption rate for a recent release, current "what changed" ticket volume, and current NRR — you need a before/after, not a vibe.
3. **KPIs to track**: feature adoption rate on releases documented vs. prior baseline; "what changed" ticket volume; time-to-adopt for new features; qualitative CS/sales feedback on whether reps can now sell off release notes without escalating to engineering.
4. **Decision point**: at the two-quarter mark, compare the lever(s) above against actual cost. Convert to permanent only if the data clears the bar you set going in.

## What to do before the CFO meeting

- Pull your own ARR, churn rate, and current release-related support ticket volume — the model above needs those numbers to close the deal, and they're more persuasive coming from your own data than any external study.
- Skip citing Linear or the App Store study with numbers attached. Cite Linear as "here's what good looks like" with a screenshot of their changelog, and leave the App Store claim out entirely until you've found and read the source.