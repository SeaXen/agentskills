**Next action:** open your issue tracker and list every company that has asked for support, an invoice, a feature or a security review. That list is your first buyer evidence. If it's empty, the plan is not ready.

## Verdict on your numbers

The 4,200-seat figure is not a forecast. Don't plan on it.

- **No conversion rate exists.** Nobody has published a free-to-paid rate for a library, so "1% of downloads" is an invented input.
- **Downloads are not buyers.** CI runs, mirrors and transitive installs inflate the 420k. Only a company asking to pay counts as demand.
- **Your own math is off by 14x.** 4,200 seats × $29 is about $121,800 a month, against an $8k goal.

## What the goal actually needs

Fee rate is my assumption, 5%. Replace it with your real processor or merchant-of-record rate. The 5 seats per organization is also my assumption.

- Net per seat: $29 × 0.95 = $27.55 a month.
- Seats needed: $8,000 / $27.55 = about **291 seats**. That is 0.07% of downloads, not 1%.
- Organizations needed, at 5 seats each ($137.75 net per organization): about **59 paying organizations**.
- Demand test: 10 paying organizations within two quarters of launch. That is about $1,380 a month, 17% of the goal. It proves demand, not the goal.
- Timing: the salary-level cases took years. Sidekiq launched in 2012 and reported about $80k a month in 2017.
- Baseline: a job or contract at a company that depends on Cinderwell may beat your year-one revenue per hour. Compare quarterly.

## Gates

| Gate | Status | Evidence needed |
|---|---|---|
| Buyer | Unproven | Named companies in production that asked to pay. |
| Ownership | Pass | MIT inbound is permissive, and Pro is new code you write, so it is yours to sell. Name, domain and npm account: confirm you hold them. |
| Shape | Pass | An embedded library with org-scale features. Multi-node coordination fits. |
| Capacity | Open | You are full time, but I don't know what the second maintainer does or what customers will cost you in support hours. |
| Employer | Open | Confirm in writing that the employer you are leaving owns none of the code and has no claim on it. |

**Boundary risk:** bulk rendering may be something everyone needs. If it ships free today, you can't paywall it. If everyone needs it, it belongs in the free core. S3 output and multi-node coordination are safer paid features. Validate the list with named companies before you write code.

## Price shape

$29 per developer with no organization band is the pattern the skill says to avoid. FluentAssertions' per-developer price drew the strongest recent fork. AutoMapper's developer-count bands per organization drew far less anger.

For orientation only: River Pro charges $125 a month for up to 20 developers, and Sidekiq Pro is $99 a month. A 20-developer team on your plan pays $580. Add organization bands, bill annually, and offer a card tier plus an invoice tier. Take exact price levels to `devtools-pricing-strategy`.

## The two other items

- **Marketplaces.** They are a procurement channel, not a revenue source. No indie library has disclosed material marketplace revenue. They help only when enterprise buyers spend committed cloud budgets. List only after a buyer asks, and then only on the cloud marketplace. GitHub Marketplace is built around Actions and Apps, not npm libraries.
- **The "acquire and sponsor" email.** This is an exit, and it hands the trust decisions to the buyer. Treat it as a comparison for the review date, not as a safety net you can count on. Ask for the terms in writing: who owns the name and license, whether MIT stays, and what "sponsor" means in dollars and years. Don't mention Pro pricing to them yet.

## Recommended offer

Sell the paid add-on, opened by 2 or 3 capped support contracts with the companies already asking. The contracts pay within weeks. They also show which Pro features those companies would pay for.

## Dashboard KPIs

Every baseline below is one you set yourself. Say so on the dashboard.

1. **Companies asking to pay per month.** Count invoice, quote and security-review requests. This is the leading indicator. Record the pre-launch baseline now.
2. **Paying organizations against the threshold.** Target is 59 organizations, or 291 seats, at the current price and fee assumptions. Show the projected date: current rate of new customers minus churn.
3. **Demand test.** 10 paying organizations by two quarters after launch. If you are below that, revisit the boundary before adding features.
4. **Revenue per maintainer hour.** Count building, selling, invoicing and support hours. Compare quarterly against the employment baseline.
5. **Trust signals.** Outside PRs per month, plus activity on any fork of the free edition.

Diagnostics only, with no targets: docs visits to the Pro page, pricing-page views, checkout starts. Also track the 35k docs trend. Docs-funnel products are exposed to AI assistants answering from your docs. Tailwind's founder attributes a revenue drop close to 80% to that.

Add one kill or pivot condition. Example: if the demand test fails at two quarters, compare the acquisition offer and a job against your revenue per hour.

## Launch checklist (do before selling)

1. Publish the always-free list: everything free today, security fixes for the free edition, the docs, export, and community contributions.
2. Register the Cinderwell name before selling.
3. Decide who invoices: your own entity or a merchant-of-record service. Ask an accountant.
4. Write the rule for outside PRs that add a paid feature to the free core.
5. Run the EU Cyber Resilience Act role test in `oss-security-disclosure` before launch, since charging for software can make you a manufacturer.
6. Answer the continuity question in the contract: deployed versions keep working, and buyers get source access or escrow if you stop.

Never add telemetry or license checks to the free library. Ship the Pro package privately, with a per-customer credential.

## Open questions

- Which companies have asked to pay, and for what?
- What is the second maintainer's role, and do they hold any copyright?
- Does bulk rendering ship free today?
- What are your weekly hours for selling and support?
- Which country and entity will invoice?

**Next:** search the issues, then send the first company on that list a capped support-contract offer this week.