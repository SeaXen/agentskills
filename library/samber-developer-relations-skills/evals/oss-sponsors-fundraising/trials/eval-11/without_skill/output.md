# quillstream Sponsorship Program

## The shape, in one line

Two passive, self-serve payment rails feeding a capped, tiered rate card that sells placement on your three existing surfaces (README, docs, newsletter) — no calls, no invoicing by hand, no entity.

## Why this shape

- **No entity, no fiscal host, personal bank account** → rules out Open Collective. Points you at rails that pay individuals directly: GitHub Sponsors and a Merchant-of-Record platform (Polar.sh).
- **2 hours/month floor** → rules out anything requiring a call, a custom deck, or per-issue ad-slot coordination. Pricing must be public and fixed; buying must be self-serve.
- **Money doesn't need to be fast** → let you cap sponsor slots instead of maximizing count. Scarcity protects the thing actually generating 41k+12k views: developer trust in your README and docs. A README that looks like a billboard stops converting, and the whole program dies with it.
- **Still paying in 2 years** → favor annual billing over monthly (fewer renewal touches per sponsor per year) and favor a small number of durable B2B relationships over a large number of one-off transactions.

## Payment rails — use both, they cover different buyers

**GitHub Sponsors** (individual layer)
- Zero setup cost beyond flipping it on. No entity, no invoicing, GitHub is the payment processor, payout goes straight to your personal bank account.
- Good for many small recurring sponsors ($5–$100/mo): individual devs, indie plugin makers, people who found real value in the library.
- Weak for landing $500+/mo company deals — companies' AP departments usually want a proper invoice to expense a recurring payment, and GitHub Sponsors doesn't produce one.

**Polar.sh** (company/rate-card layer)
- Built for exactly your situation: solo maintainer, no entity, acts as Merchant of Record — handles VAT/sales tax across countries, issues real invoices to sponsor companies, pays out to your personal bank account via Stripe Connect.
- This is what lets you sell $150–$900/mo tiers to actual companies without you becoming a part-time bookkeeper.
- Has a benefits API/webhook — a sponsor's payment can automatically trigger "add this logo" instead of you editing files by hand.

**Do not**: invoice manually as an individual across borders (VAT headache Polar exists to absorb), or accept "let's hop on a call to discuss a custom deal" in year one — a single such call burns your entire bad-month budget.

## The rate card

| Tier | Price | Placement | Slots |
|---|---|---|---|
| GitHub Sponsors — Supporter | $5/mo | Name in SPONSORS.md | Unlimited |
| GitHub Sponsors — Backer | $25/mo | + name in README "Backers" | Unlimited |
| Polar — Bronze | $150/mo ($1,500/yr) | Logo+link, README "Sponsors" (below fold) + docs footer strip | 6 |
| Polar — Silver | $400/mo ($4,000/yr) | + persistent logo in docs site header/sidebar (all 41k monthly views) + recurring newsletter footer credit | 4 |
| Polar — Gold | $900/mo ($9,000/yr) | + top-of-README placement (the first 5 seconds every evaluator sees) + one dedicated 2–3 sentence newsletter feature per quarter + "official sponsor" badge they can use in their own marketing | **2 — hard cap** |

Annual price = ~17% discount vs. monthly, pushed hard as the default: one renewal event per sponsor per year instead of twelve.

Gold capped at 2, Silver at 4, on purpose — scarcity is what lets you raise prices as traffic grows, and it's what keeps the README from degrading into an ad wall.

## Operational workflow — built once, then almost nothing

**One-time setup (~6–10 hours, outside the 2-hour/month budget, do this in one focused weekend):**
1. Enable GitHub Sponsors, define Backer/Supporter tiers.
2. Set up Polar.sh account, define Bronze/Silver/Gold tiers with checkout links.
3. **Build one automation**: a `sponsors.yml` that a GitHub Action regenerates nightly (or on Polar webhook) into the README's sponsor block and the docs site's sponsor strip. This is the single highest-leverage piece of work — it's what turns "new sponsor" from a manual edit into a zero-touch event.
4. Write the newsletter's recurring one-line sponsor footer template.

**Steady state (30–60 min/month normal, ≤2 hours bad month):**
1. Glance at the Polar/GitHub dashboards for new or churned sponsors — the render script handles the actual update.
2. Paste the templated sponsor footer into the newsletter issue.
3. Once a quarter, write the Gold-tier feature blurb (max 2, ~30–45 min total).

**Explicitly refuse**: one-off newsletter ad slots sold separately (per-issue coordination is a time sink), custom pricing on a call, monthly-only billing.

## Tax reality check

No entity is required to receive this income — in effectively every jurisdiction you declare sponsorship/advertising income as personal or self-employment income on your own return, same as freelance income. Set aside ~25–30% for tax. Polar and GitHub both export full transaction histories, so year-end reporting is a 10-minute task, not bookkeeping. What you're avoiding by refusing an entity is French/international corporate paperwork — that's a separate question from whether the money can land in your personal account, and it can.

## Rollout

- **Week 1**: build the automation (step 3 above) before selling anything — never manually edit a sponsor placement.
- **Week 2**: enable GitHub Sponsors, publish Polar rate card as a public page linked from README/docs footer.
- **Week 3**: email your own newsletter once, announcing sponsorship is open, rate card attached — your 9,200 subscribers are your best lead source for both individual and company sponsors.
- **Week 4 onward**: no outbound. Let the rate-card link do the selling; if a company reaches out, send the link, not a call invite.

## Honest revenue expectation

- **Year 1**: realistic to land 1 Gold + 2 Silver + 3–4 Bronze + ~20 small GitHub Sponsors by year end → roughly $2,000–2,500/mo run rate exiting the year, most of the ramp in H2.
- **Year 2**: both Gold slots filled, Silver near cap, Bronze refilling as it churns, GitHub Sponsors base growing with project adoption → roughly $3,500–4,500/mo run rate, and durable — annual billing plus a capped, high-trust surface means sponsors renew rather than get resold each year.

This is slow money, compounding, matching what you asked for — not a launch spike.