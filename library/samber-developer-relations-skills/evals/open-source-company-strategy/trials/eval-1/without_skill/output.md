## Recommendation: Open-source the engine, but as a phased, source-available transition — not a clean MIT/Apache give-away

**Verdict:** Do it. The market is already commoditizing your engine whether you act or not — two competitors moved last spring, and your own engineers (the people closest to the technical differentiation) have independently concluded the same thing for a year. But the specific move that fails is "flip the license switch." The move that works is a staged transition that protects the $6.1M while you rebuild the pricing lever around ops tooling.

### Your framing is right, with one correction

"Commoditize your complement" only holds if the thing you're giving away is genuinely a *complement* to what you now sell — not the product the $6.1M is currently billed against. Right now it's the same thing: you charge $4,200/core/year for engine access, full stop. Open-sourcing it doesn't commoditize a complement to your revenue model, it deletes your revenue model's enforcement mechanism. The strategy is sound; the sequencing is the risk. You need the ops-tooling business built and salable *before* or *simultaneously with* removing the ability to gate the engine — not after.

You said the work has already moved to ops tooling. That's the tell the strategy is timed correctly, not evidence the license change is free.

### The real exposure: 38 customers, concentrated risk

With 38 accounts averaging ~$160K/year, this isn't a long-tail SaaS base where a few churns wash out in the noise. Losing your top 5–8 accounts because they read "open source" as "stop paying" would be a material revenue event, fast. Before any announcement:

- Segment the 38 by what they're actually paying for — pure engine access with minimal tooling/support usage vs. accounts already deep in your ops platform. The first group is your churn risk; the second group is your proof the new model works.
- Call your top 10 accounts by revenue *before* anything is public. Frame it as "here's where we're taking the product," not "here's a surprise at your renewal." Get a read on what they'd pay for post-open-source (support SLAs, enterprise ops features, migration help). Soft-commit renewals under the new packaging before you commit to the change publicly.
- Rewrite the commercial contract for existing customers so the invoice is explicitly for support/SLA/ops-platform access, not "engine license" — same dollar figure, different label, reduces the psychological cliff at renewal.

### License choice: don't go fully permissive

Apache/MIT maximizes goodwill and adoption but hands away your only remaining lever during the transition — anyone (including a customer) can fork, self-support, and stop paying the day you flip it.

Use a **source-available license with a delayed open-source conversion** — the pattern HashiCorp, CockroachDB, and Sentry used (Business Source License: source visible and modifiable immediately, production/competing-hosted-use requires a commercial agreement, auto-converts to Apache-2.0 after ~3–4 years). This gets you:

- The market narrative your competitors already claimed ("we're open too"), which is the actual near-term goal.
- A contractual block on a competitor or hyperscaler standing up "Halyard Engine Cloud" and reselling your work without a deal — lower risk for you than it was for Redis/Elastic/Mongo since this is a specialized on-prem time-series engine, not a horizontal database attractive to managed-hosting resale, but still worth closing off.
- A multi-year runway to prove the ops-tooling business can carry revenue on its own before the engine becomes unconditionally free.

⚠️ Expect pushback: BSL isn't OSI-approved, and part of your engineers' motivation is likely developer/community credibility, not just competitive pressure. If that's the primary goal, a pure Apache license on an *older, feature-frozen* major version (keep current/next-gen engine internals and performance work proprietary a while longer) gets you real community trust without giving away the current shipping product.

### What stays closed

Everything that constitutes the ops tooling — the actual place your engineers' time goes and the thing you said is the real product now: clustering/HA orchestration, multi-tenant management, security/compliance tooling, monitoring integrations, migration/upgrade automation. This is your new price anchor. Name it, package it, and start selling it as the product line explicitly, not as a bundled afterthought to the engine license.

### Don't let the retention threat drive the timeline

Three of seven engineers wanting this for a year is a useful signal about where technical peers see the market heading — weigh it as data. One person threatening to leave is not a reason to make a $6.1M licensing decision on an accelerated clock. If you agree with the strategic logic on its own merits (you do, based on what you've described), move on the business timeline the revenue transition requires, and handle the retention conversation separately and directly with that engineer.

### 90-day sequence

1. **Weeks 1–3:** Segment the 38 accounts by revenue composition; identify top 8–10 by ARR.
2. **Weeks 2–6:** Direct conversations with those accounts — gauge willingness to pay for ops tooling/support post-change, get informal commitments.
3. **Weeks 4–8:** Finalize BSL terms (change date, additional-use grant scope) and repackage the commercial offer around ops tooling + SLA, not engine access.
4. **Weeks 8–10:** Rewrite existing contracts for renewal under new packaging, starting with accounts already committed.
5. **Week 10+:** Public open-source release, once your top-revenue accounts are already converted or in active conversion — so the announcement lands on a market, not a vacuum.