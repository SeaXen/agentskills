## Verdict

Partial no. The incident is real, but the two-part fix leadership wants — mandatory hard caps everywhere, kill the free tier — treats the symptom, not the mechanism, and the "mandatory hard cap on production" half is actively dangerous.

## What actually happened

Re-read the incident: a free-tier user's *public-facing images* got scraped. The attacker wasn't the free user — it was a third party hitting URLs the free user's site exposed. That's a scraping/traffic-abuse pattern, not a "free users are risky" pattern. Anyone's public image URLs are scrapable this way, free or paid. That distinction should drive the fix, because it means:

- A dollar cap (hard or soft) is a **financial control that fires after damage is done**. It didn't fail because it was missing a hard stop — it failed because nothing throttled the *request rate* or the *unique-parameter surface* in real time, so cost ran to $9,400 before anyone or anything intervened.
- The same scraping attack works against a paying production account. If your fix is "hard cap that cuts traffic," you haven't closed the hole — you've just changed the failure mode for paying customers from "surprise bill" to "surprise outage." For a production image API, broken images on a live site during a traffic spike is usually worse for the customer, and for you, than an invoice dispute.

## On "mandatory hard cap, production included"

Reject this as stated. A cutoff that kills serving on a production account the moment it crosses a threshold means your infra now DoSes your own paying customers during their best traffic days — a viral post, a launch, a legitimate spike. That's a reliability incident you'd be inflicting on yourself, on customers who did nothing wrong, to guard against a scenario (runaway free-tier bill) that a differently-shaped fix already prevents.

What to build instead:

- **Free tier: hard ceiling, mandatory, zero billing path.** Free should mean the meter literally cannot produce an invoice. At the limit, requests get a 429, not an overage charge. This alone makes the $9,400 scenario structurally impossible — not "capped at some large number," impossible.
- **Paid/production: soft caps by default, hard cap opt-in.** Alert at 70/85/95% of expected spend, auto-approve a reasonable overage buffer, let the customer configure a hard stop if *they* want one. This mirrors how AWS Budgets works — alerting is automatic, auto-shutoff is opt-in — for exactly this reason: providers don't get to unilaterally decide a customer's downtime is preferable to their bill.
- **Rate limiting and anomaly detection on every tier, ahead of billing.** Requests/sec per token, and a spike detector that auto-throttles on a sudden multiple of baseline traffic. This is what should have stopped the scrape at, say, $50 of anomalous usage instead of $9,400 — a threshold two orders of magnitude tighter than any cap leadership is likely to propose as a "hard cap."
- **Bound the transform-parameter space, at least on free tier.** Arbitrary width/height/quality/format combinations mean every scraped request can be a unique cache-key, forcing origin compute on every hit. Whitelist a set of presets (or clamp to a small discrete grid) for free tier, and normalize/cache aggressively at the CDN layer. This kills the specific mechanism the scraper exploited, independent of any cap.

## On killing the free tier

Reject this too, as a category error. A free tier is Spindrift's self-serve top of funnel — developers evaluate, build side projects, and refer other developers largely *because* they can do it without a credit card. Every credible competitor in this space (Cloudinary, imgix, imagekit) keeps one. Removing it doesn't remove the scraping vector (it still works against any public URL, paid included) — it just removes your acquisition channel while leaving the actual root cause unfixed.

The free tier didn't cause the $9,400. A free tier that could bill $9,400 caused it. Fix that property and the tier itself is fine to keep.

## Bottom line to bring back to leadership

Their instinct — "this can't happen again" — is right. Their proposed mechanism is wrong on both counts: caps belong on free tier as a zero-cost ceiling, not on production as an auto-cutoff; and the free tier should be fixed, not killed. Recommend: (1) make free tier billing-incapable by construction, (2) add rate limiting + spike-based auto-throttle across all tiers as the real fix for the scraping vector, (3) offer production customers configurable soft alerts with opt-in hard caps, never a forced default cutoff, and (4) bound the transform-parameter grammar on free tier to shrink the cache-bypass surface the scraper used.