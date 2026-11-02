# Fixing Clearmast's lead routing (Step 5: developer-to-buyer handoff rule)

Re-tuning the weights won't fix this. The model itself is the wrong shape — moving numbers around inside it just relocates the problem. Here's why, and what replaces it.

## Why retuning fails

Your score is a marketing-qualified-lead (MQL) construction wearing a developer-motion costume. **A lead that accumulates points for opening an email and visiting the pricing page tells you about marketing exposure, not about product usage.** Two things are compounding:

1. **You're qualifying users, not accounts.** Forty signups from one bank domain look like 40 leads and generate 40 emails, because nothing rolls usage up to an account before scoring. This is a mechanical bug, not a weighting problem — no set of point values fixes it, because the unit being scored is wrong.
2. **You're scoring intent-to-browse, not intent-to-use.** "Signed up in the last 7 days = 15" front-loads a third of your 60-point threshold onto every brand-new signup before they've done anything with the product. Add one pricing-page visit (10) and a docs visit (8) or two email opens (10), and a user who joined yesterday and skimmed your site crosses the line. That's **contacting on signup** wearing a disguise — the single behavior developer audiences punish hardest, which is almost certainly what's showing up as annoyed tweets and a 2% reply rate.

None of your four signals — email open, pricing visit, docs visit, signup recency — measures whether the product is doing real work for anyone. Retuning weights inside that set only changes *which* unqualified users get emailed first.

## Fix 1 — Roll usage up to an account before anything else

This is the line item that kills the 40-email bank problem directly, and it has to ship before any new threshold means anything.

- Best: an organization/workspace object in the product, if you have one.
- Otherwise combine **email domain** + **API key / install ID** — imperfect, but immediate, and enough to catch a corporate domain like the bank's.
- Flag free-mail domains (gmail, outlook) so they don't falsely cluster strangers into one "account."

Once this exists, the bank's 40 signups become **one account** with a spread signal already tripped (many active developers, same domain) — one qualification decision, one contact, not 40.

## Fix 2 — Replace the four scored inputs with real signal families

Drop pricing-page visits, email opens, and docs visits as *scored* qualification inputs entirely. Keep docs open to everyone, always — gating or scoring them just teaches developers to distrust the free tier. For a feature-flagging product, the signals that actually predict a purchase decision:

**Depth — is the product doing real work?**
- SDK initialized against a **production** environment, not just dev/staging
- Sustained flag-evaluation volume over multiple weeks (not a one-day spike from a demo)
- SDK/flag calls wired into a CI/CD or deploy pipeline

**Spread — is more than one developer involved?**
- Second and third active developer in the same account
- Invite sent and accepted
- Multiple services/repos with the SDK installed

**Boundary contact — did someone touch something only an org needs?** (strongest signal — maps directly to your paid boundary)
- Visited/clicked SSO/SAML, RBAC, or audit-log pages
- Hit a seat, environment, or flag-volume limit repeatedly
- Requested a SOC 2 report, security questionnaire, or DPA
- Opened billing/invoicing/procurement pages

Depth without spread is usually a solo power user (not yet an org decision). Spread without depth is usually an evaluation that hasn't committed — for the bank, that's likely exactly where you are right now, so don't fire an SDR email off spread alone; wait for depth or boundary contact to join it.

## Fix 3 — Write the threshold as one sentence, not a point total

Fill the blanks from *your own* conversion data (the usage level accounts historically had before they started paying), not from a round number like 60:

> An account becomes qualified when it has **N or more active developers** and **M weeks of sustained production flag evaluations**, or when **anyone in it touches SSO/audit-log/security-questionnaire pages**. Qualified accounts are contacted by **the SDR** within **24–48 hours** with **an environment-and-rollout-limits review**, never a generic "let's connect." Accounts below the threshold receive **no human contact** — product and documentation surfaces only.

You don't have N and M yet — pull them from the accounts that already converted (median active-developer count and usage duration before first payment), not from a blog post; cohort shapes don't transfer between companies. Until that data exists, a defensible starting guess is 2–3 active developers and 2–3 weeks of production usage — treat it as provisional and revisit quarterly.

Before staffing this: check the arithmetic. A salesperson added to a self-serve motion should return roughly **4x their fully loaded cost** in incremental revenue (*The Transition*, Lenny's Newsletter). If your realistic qualified-account volume × deal size doesn't clear that, the fix is a better self-serve surface, not a bigger queue for the SDR.

## Contact routing by role

Forty signups at a bank aren't 40 identical contacts even after rollup — route by who they are:

| Role | Gets | Never gets |
|---|---|---|
| Active developer | Help with what they're doing — a limits/quota conversation, migration help, a bug reply | "15 minutes to learn about your needs" |
| Technical champion | An enablement pack: their own usage numbers, a re-runnable benchmark, migration path, pre-answered risk questions | A pitch deck they can't reuse internally |
| Approver (security/architecture) | Risk answers unprompted: license, data handling, SLA, security posture | Feature marketing |
| Economic buyer | Cost comparison vs. status quo, ideally introduced by the champion | A cold email that bypasses the champion |

For an account like the bank — high firmographic fit, but still low on depth — the right early motion is often not "SDR email" at all. It's getting the security/compliance material in front of whoever hits the boundary-contact signal first, since regulated-industry accounts convert through that page, not through a founder-style pricing pitch.

## The do-not-contact line

Write this down explicitly, or it drifts back to every signup: **accounts below the threshold are not contacted by a human, ever, regardless of how recently they signed up.** Remove signup-recency as an input entirely — it's the one number in your old formula that guarantees false positives on day one.

## What to track for the next quarter (five or fewer numbers, all pre-revenue)

- Time from account rollup existing → first qualified account identified
- Share of accounts reaching the depth signal (production usage, sustained)
- Share of qualified accounts contacted within the 24–48h window
- Free-to-paid conversion at **account** level, by cohort (not per-user, not lifetime)
- Reply rate on SDR outreach, split by *why* the account qualified (depth vs. spread vs. boundary contact) — this tells you which signal is actually predictive, which no published benchmark will

One number for context, sourced: developer-focused companies show a median free-to-paid conversion of **5%**, roughly half the blended B2B median (Lenny's Newsletter, *What is good free-to-paid conversion*, survey of 1,000+ products). Your 2% is a reply rate on bad-fit outreach, not a conversion rate — don't conflate the two, and don't benchmark reply rate against this figure at all; it isn't the same measurement.

## What this rules out going forward

No contact triggered by signup recency alone. No scoring engagement with marketing content (email opens, page visits) as a qualification signal. No per-user contact on accounts that already have a rollup identity — one decision per account. No SDR outreach below the threshold, no exceptions for "they look big" (that's what boundary contact and the champion-pack routing are for, not an early email).

**Revisit the threshold when:** qualified-account volume exceeds what one SDR can contact within the response window (add headcount, or the 4x test needs re-checking), or when a full quarter of data shows the N/M values you started with don't match where paying accounts actually converted.