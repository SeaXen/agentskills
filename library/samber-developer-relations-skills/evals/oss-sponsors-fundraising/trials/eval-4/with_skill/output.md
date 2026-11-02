## Bottom line

Don't publish this as-is. Three of the five rewards are priced as if they cost nothing to deliver, when they're actually the most expensive rewards in the whole catalogue. Run each one through the skill's own test — *what does this cost every month at ten times today's sponsor count (14 → 140)?* — and the ladder breaks in the same three places the skill's reference "weak ladder" example breaks, plus one worse case it doesn't even cover.

## Ranked by damage

**1. $200 — "I'll build one custom integration a quarter for you."**
This is a bespoke-integration promise, the single most expensive reward category the skill tracks ("a second job": monthly calls, per-sponsor content, bespoke integrations). At 14 sponsors you don't know yet how many will land on this tier; at 140, if even 10 do, that's 10 custom integrations every quarter — a full engineering commitment sold at $200/month self-serve, with no scope boundary on what "an integration" means. The skill is explicit about this exact shape: *"Cut any reward that fails the ten-times test... Do not promote them into a tier perk — move them out of the ladder entirely and sell them through the corporate-lane step, where the price matches the obligation."* This belongs as a negotiated retainer with a written scope (the reference ladder prices a comparable named-commitment tier at $4,000/month, capped, written scope) — not a checkbox at $200.

**2. $30 — monthly 30-minute 1:1 video call.**
This is the exact failure mode in the skill's own worked "weak ladder" diagnosis: *"A 1:1 call at $50. At 40 sponsors that is a working week per month, sold at a rate no consultant would accept. It is the first thing to break, in public."* Yours is worse — cheaper ($30 vs $50) and it's the second-lowest tier, so it's the one most people will pick. At 140 sponsors, even a modest fraction choosing this tier is multiple unpaid working days a month, permanently, the moment it's published (GitHub Sponsors tier prices can't be edited — only retired, with existing sponsors grandfathered at the old price).

**3. $75 — "priority support, I answer your issues within 24 hours."**
The skill draws a hard line here: *"Priority triage can be sold; priority outcomes cannot."* Framed as "answer," not "resolve," you're technically on the triage side — but the reward catalogue still files "guaranteed response times without a contract" under the same "second job" bucket as the call and the integration. A 24-hour SLA to every sponsor at $75+ isn't bounded by a seat cap or a written scope, so it scales the same way the call does: fine at 3 sponsors on this tier, unsustainable at 30.

**4. $400 — "everything above, plus logo in README."**
Because it's cumulative, your most expensive tier inherits all three problems above *and* adds a placement reward with no traffic number attached — the skill flags this as its own failure mode ("logo somewhere" — a benefit an approver can't evaluate is a benefit nobody buys). Right now this tier is the worst deal in the ladder to actually deliver on, not the best one to sell.

**5. No company tier.**
Companies pay from a budget line and need something a budget-holder can defend — pricing tied to real traffic ("logo on the README, X views/month"), not "everything above." $400 is roughly at the individual/company boundary the skill uses as a baseline, but nothing here is *named or priced for a company buyer*. If any company depends on your project, there's real money being left unclaimed above $400.

## What's fine as-is

- **$10 — name in BACKERS.md.** Pure gratitude, no perk, sitting below the tier that will actually convert. That's the correct shape — the skill specifically warns against the opposite (a partial-perk tier just under the converting tier siphons everyone to the cheap option), and a no-perk floor tier doesn't have that problem.

## Suggested rewrite

Same five rungs, same spirit, but the fragile rewards move out of the self-serve ladder and the cheap-to-deliver rewards fill the middle:

| Tier | Price | Reward | Cost at 140 sponsors |
|---|---|---|---|
| Backer | $10 | name in BACKERS.md | ~0 |
| Supporter | $25 | name in BACKERS.md + thanks-page listing | ~0 |
| Team | $100 | small logo in README + docs footer *(needs your traffic numbers)* | ~10 min/quarter |
| Business | $250–500 | large logo in README/docs sidebar + **quarterly group** office hours | ~1h/quarter |
| Infrastructure | negotiated, ≥$1,000, written scope | above + capped issue-triage SLA and/or scoped integration work, sold as a retainer through direct outreach, not self-serve | bounded by contract |

The monthly 1:1 call either gets dropped, capped to an explicit seat limit ("first 3 sponsors only"), or repriced high enough that a working-week-a-month is actually worth it to you — don't publish it as an uncapped self-serve tier.

## Before you finalize prices, I need two things

1. **README/docs monthly traffic** — the skill's rule is to price placement against real numbers ("logo on a README with 20k monthly views"), not against tier generosity. Without a number, the $400/logo tier is unpriceable and unprovable to a company approver.
2. **Can you name any companies that actually depend on the project?** If yes, that's where the real money is, and it's worth building a proper company-priced tier above $400 rather than folding company buyers into the individual ladder.

One platform note, since this reads like a GitHub Sponsors ladder: whatever you publish is **permanent** until retired and replaced — existing sponsors stay on the old terms. Fix the $30 and $200 tiers before they go live, not after; walking them back costs goodwill the skill explicitly warns is expensive.