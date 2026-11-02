## The actual problem

"We should do PLG" is being used as a synonym for *cheap, fast growth without sales effort*. For Parapet, none of the three structural facts support that:

- **Platform-engineer approval gate** — a human has to sign off before the product can even run. No amount of self-serve signup removes that gate; it's organizational, not a UX problem.
- **Cluster-wide blast radius** — admission control can break every workload in the cluster. Buyers are risk-averse by construction, not by unfamiliarity.
- **Value only appears after 3+ services onboarded** — the "aha moment" is a multi-week integration project, not a five-minute API call. Classic PLG (Vercel, Supabase, Stripe) works because the aha moment is *individual and immediate*. Parapet's aha moment is *organizational and cumulative*.

This is the same category shape as Vault, OPA/Gatekeeper, service mesh. None of those vendors got meaningful revenue from bottom-up individual signup in under a year — their real motion was years of OSS/community adoption converting into sales-assisted enterprise deals. Trying to compress that into 10 weeks with no new headcount isn't an aggressive PLG plan, it's a category error.

## Kill list — reject these for this cycle

- **Building a hosted free tier now.** Free-tier payback is measured in months to years (see Vercel/Supabase-style models); it cannot produce board-visible revenue in 10 weeks, and it consumes the exact engineering time you don't have.
- **Cloud marketplace listings.** Explicitly excluded by the no-margin constraint, and marketplace self-serve solves discovery, not the approval gate — irrelevant here anyway.
- **Reseller/SI channel.** Same constraint, same conclusion.
- **New devrel/growth hires or a new self-serve billing stack.** No headcount. Don't design a motion that requires one.
- **Net-new-logo PLG as the revenue lever for the board date.** Security/infra procurement cycles (legal, platform buy-in, budget) don't compress to 10 weeks regardless of funnel top. Chasing this wastes the window.

## What the "PLG" instinct gets right — keep these two things

1. **Product should do more of the convincing, so Sales does less.** Legitimate. The fix isn't a free tier — it's removing the *specific* friction (see below).
2. **Shorten the path from interest to technical proof.** Legitimate. Achievable without self-serve signup or hosted infrastructure.

## The motion: product-assisted expansion, not product-led acquisition

Name it precisely so the team stops arguing past each other: **this quarter is a sales-led expansion motion with a self-serve technical-proof artifact bolted on** — not PLG. PLG becomes real next year, funded by the revenue this motion proves.

**The actual unblocker: ship "audit mode" as the trial, not "Parapet" as the trial.**
Admission controllers already distinguish enforce vs. dry-run/audit. A scoped, time-boxed, audit-only install (can't block anything, single namespace, auto-expires) collapses the platform engineer's approval decision from "let this potentially break prod" to "let this watch and report." That's the entire activation blocker, solved with packaging, not new product. This is buildable by the existing team in days, not a quarter.

## Packaging — turn the 3-services threshold into the pricing tier, not a liability

- **Foundation (audit-only, up to 2 services):** low/no-commitment entry price. Gets the platform engineer to "yes" fast because it can't cause an incident.
- **Full (enforce mode, 3+ services):** the paid tier — priced at the exact point where the product's own value threshold kicks in. Value metric = services under active policy, which is easy to understand, hard to game, and scales with what the customer actually gets.
- **Milestone-triggered billing on existing pipeline:** for deals already in motion, offer contract terms where the committed ACV signs now but the payment clock (or a defined discount) starts at the 3rd-service milestone. This is a Hormozi-style offer-construction move — it de-risks the buyer's fear ("what if this stalls at 1 service and I've wasted budget") without discounting off list and without touching margin. Signed, milestone-triggered ACV still counts as bookings for the board.
- No marketplace, no reseller line anywhere in this structure — direct only.

## The 10-week plan (no new headcount — repurpose existing sales/CS/eng time)

**Weeks 1–2 — Triage, not top-of-funnel.**
Pull every account currently at 1–2 services onboarded or with a stalled PoC. This is your nearest revenue — closer than any new-logo motion could get in this window. Rank by ACV and by how close to the 3-service line they sit. Ship the audit-mode trial package in parallel (existing eng, scoped work, not a new product line).

**Weeks 3–6 — Unstick and land, not attract.**
AEs/CS run the audit-mode fast-track into every stalled account: replace "let us in for production enforcement" with "let us watch for two weeks, free of blast-radius risk." Use it to convert 1–2-service accounts to 3+ and trigger the pricing tier crossover. This is expansion revenue from people who already chose you — cheapest, fastest path to signed ACV you have.

**Weeks 7–9 — Close and prove.**
Push signatures on milestone-triggered contracts. Every account that crosses 3 services becomes a reference case — this is the proof asset that justifies real investment in PLG next year, not a marketing afterthought.

**Week 10 — Board readout.**
Report: signed/bookings ACV this quarter (not vanity signups), number of accounts crossed from sub-activation to full activation, and a funded ask for next year's actual PLG build (a real free/audit-mode self-serve tier, devrel headcount) backed by this quarter's conversion data — turning "we should do PLG" from a slogan into a costed, evidenced proposal.

## Why this satisfies all four constraints simultaneously

- **No headcount:** every action reuses existing AE/CS/eng capacity; audit-mode packaging is a scoping change, not a new product.
- **10-week revenue:** targets accounts already in-funnel, one activation step away — the only segment that can realistically close in this window.
- **No reseller/marketplace margin:** direct-only throughout; the offer engineering (milestone billing) creates deal flexibility without discounting or channel cuts.
- **No free tier today:** stays true — audit-mode is a scoped, time-boxed *trial*, not a permanent free product. The permanent free tier becomes next year's funded, headcount-backed bet, sequenced correctly instead of rushed.

## Tripwire to watch

If triage (Weeks 1–2) turns up fewer than a handful of accounts sitting at 1–2 services, the "expansion-first" bet doesn't have enough surface area — say so to the CTO immediately rather than discovering it in week 8. In that case the honest board message becomes "we have a pipeline-shape problem, not a motion problem," and the 10-week ask shifts to renegotiating what "revenue movement" can credibly mean this cycle.