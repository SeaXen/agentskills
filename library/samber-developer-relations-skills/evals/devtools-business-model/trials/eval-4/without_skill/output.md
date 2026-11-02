**Self-serve → inside sales: ~$8,000 ACV** (≈17 seats at $39/seat/mo)
**Inside sales → field sales: ~$75,000-100,000 ACV** (≈160-215 seats)

Reasoning behind each threshold:

**Why $8K is the self-serve ceiling**

Below that, Stripe checkout captures the value fine — no procurement, no security questionnaire, card on file, done. Above it, buying behavior changes independent of price sensitivity: a team big enough to need multi-tenant RBAC is big enough to have a manager who wants a demo, an invoice instead of a card charge, and a "who else uses this" conversation. That's not a self-serve UX problem you can fix with a better checkout flow — it's a different buyer.

The unit economics back this up. A first inside sales hire fully loaded (salary + commission + benefits + tools) runs ~$150K/year. To justify that hire you want ~4x quota coverage, so ~$600K in new ARR/year from that rep. With a short inside-sales cycle (30-45 days) a rep can realistically close 20-30 deals/year, which means average deal size needs to land around $20-30K for the rep to hit quota comfortably — but you don't wait until deals *average* that; you hire once a *consistent stream* of $8K+ deals shows up, because that's the segment the rep will nurture up toward $20-30K through expansion (more seats, more workspaces) rather than close cold. Concretely: hire the first AE when self-serve signups landing 15+ seats (or generating inbound "can we get an invoice/SSO/security review" requests) hit roughly 5-8/month, or when that cohort's annualized pipeline crosses ~$600K-$900K.

**Why $75-100K is the field sales trigger**

This is where the *product* itself tells you the buyer changed, not just the deal size. You said the paid tier's whole pitch is multi-tenant RBAC, retention policies, and SOC 2 compliance reporting — those are the exact features that pull in security teams, legal/procurement, and multi-year contract terms. A deal that size, in that feature set, stops being "one engineering manager expenses a tool" and becomes a 3-6 month cycle with a security questionnaire, a champion who needs help selling internally, and often a multi-threaded buying committee. Inside sales reps optimized for volume and short cycles aren't the right skill set for that motion — you need someone who can run a multi-stakeholder enterprise cycle, which is what a field/enterprise AE is for.

On the cost side: field AEs run $200-250K fully loaded with quotas of $1-1.5M ARR, which only pencils out once you have recurring $250K+/quarter of pipeline sitting in that $75-100K+ ACV band — otherwise you're carrying an expensive rep against deals too small to fill their calendar.

**Translated to seats** (at $39/seat/month = $468/seat/year):
- Self-serve: up to ~17 seats
- Inside sales: ~17-160-215 seats
- Field sales: 160-215+ seats

One flag: these are the standard SaaS-motion bands (self-serve <$5-10K, inside sales $10-50K, field >$50-100K ACV), not something derived from Kestrelbase-specific data — I don't have your actual conversion rates, sales cycle lengths, or where self-serve deals are currently stalling. If you've got that data (e.g., where free-to-paid conversions currently plateau, or what seat count correlates with "can we get on a call" requests), it'll sharpen these numbers a lot — happy to redo the math against it.