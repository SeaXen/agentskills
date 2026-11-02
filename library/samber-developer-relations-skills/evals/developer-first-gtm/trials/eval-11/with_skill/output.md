# PQL rule — Ostrich Labs

## Don't adopt "5 seats + 30 days" as-is — two separate problems with it

**"Seats" isn't a field you have.** That rule was written by a company whose product has a workspace/org object — seats count members of that object. Ostrich Labs has no such object. If you paste "5 or more seats" into your rule, you've written a condition that can never evaluate to true — there's no seat count anywhere in your data to check it against.

**Even if it did map, don't copy the number.** Cohort shapes don't transfer: their scale, ICP, deal size, and self-serve maturity are not yours. "Battle-tested at their scale" is exactly the reasoning to distrust — it's tested at *their* scale. The threshold has to come from your own accounts that already converted, not from a blog post. Keep the *shape* of their rule (a depth+spread threshold, OR'd with a boundary-contact override) — that structure is sound. Replace every number and every signal with something Ostrich Labs can actually measure.

## Fix rollup before fixing the number — this is the real blocker

You have exactly one join key: signup email. A third of it (gmail.com and similar) can't be rolled up to a company at all — two `@gmail.com` signups are unrelated as far as your data is concerned. That splits your base into two tracks that need different rules, not one rule with a workaround bolted on:

- **Track A — corporate-domain accounts (~2/3 of the 5,600).** Roll up by email domain into a company-level account. This is the only segment where "spread" (a second developer at the same company) is measurable at all.
- **Track B — free-mail accounts (~1/3).** No rollup possible. Each signup *is* the account. Do not force a multi-user spread signal onto this segment — it will permanently read as "1 user" and silently exclude a third of your base from ever reaching a human, which is worse than an imperfect rule because nobody will notice it's happening.
- This is a build item, not a footnote: one more field (ask company name at signup, even as unvalidated free text; or a project/database ID you can later cluster on) upgrades Track B later. Until then, treat the gap as known and explicit.

## Translate "seats" into signals a vector DB actually produces

There's no seat count, but there is real usage telemetry. Substitute:

- **Depth** (stands in for "this is real, not a seat count"): sustained query/write volume over a rolling window rather than a one-day spike; indexes/data retained rather than deleted after a test; calls arriving at a regular cadence consistent with a production integration rather than an ad-hoc script.
- **Spread** (Track A only, since it needs rollup): a second distinct email address on the same company domain becomes active; more than one API key active under that domain.
- **Boundary contact** (works for both tracks — doesn't depend on rollup at all, which makes it the most reliable signal you have): hits a rate/storage/index-count limit more than once; opens the billing or upgrade page; asks support about production readiness, backup/restore, SLA, or a security questionnaire.

## The threshold — two sentences, one per track

> **Track A (corporate domain):** An account, rolled up by email domain, becomes qualified when **2 or more distinct users on that domain are active** and **usage has been sustained for 3+ weeks**, or when **anyone on that domain hits a plan limit twice or opens the billing/upgrade page**. Qualified accounts are contacted by <role> within **hours, not days**, with a technical offer — a capacity/limits conversation or a production-readiness review. Accounts below the threshold get product and docs only; no human contact.

> **Track B (free-mail, no rollup):** A free-mail account becomes qualified when it shows **3+ weeks of sustained production-pattern usage** (recurring calls, data retained — not a one-off test) or **hits a plan limit twice or opens the billing/upgrade page**. Same response window, same technical-offer rule, same do-not-contact-below-threshold rule as Track A.

Label these honestly: **2 users / 3 weeks are self-set placeholders, not sourced from anything** — including not from the competitor's post. Before you ship this, pull the accounts that already converted to paid (even a handful) and check what their depth/boundary values looked like 2-4 weeks before they paid; set N and M there instead. Don't keep 5/30 even as a placeholder — it's calibrated to a concept (seats) you don't have.

## Before you staff this

Run the sales-economics check, don't skip it because the bigger company clearly can afford to: a human contacting qualified accounts should return roughly 4x their fully loaded cost. At 5,600 free accounts, work out how many will actually cross the threshold per month and at what realistic contract size before assigning a person to answer the signal — if the math doesn't clear, the honest fix is a self-serve upgrade prompt triggered by the same signals, not a PQL rule with nobody behind it.

Write the do-not-contact line down explicitly, and review both thresholds quarterly once you have a few months of qualified-to-paid data to check them against.