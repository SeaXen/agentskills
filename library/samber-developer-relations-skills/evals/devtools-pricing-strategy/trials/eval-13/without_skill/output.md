## The $9 cap is the wrong call — here's why

"Developers are price sensitive" is a half-truth that gets misapplied constantly. Devs are sensitive to **paying for something replaceable or low-stakes** — a linter, a snippet manager. They are *not* sensitive to paying for infrastructure that touches data integrity, saves real hours, or removes real risk. Evidence sitting in every dev's expense report already: GitHub Copilot ($10–39/mo), JetBrains (~$25/mo), Linear ($8–14/seat), 1Password Business ($8/seat), Vercel Pro ($20/seat), Warp, Sentry, PlanetScale. A **sync engine** — where the failure mode is "I lost work" or "my data diverged" — sits closer to that anxiety-relief category than to a nice-to-have.

The bigger problem isn't the number, it's using **one number for two buyers**:

- An indie on a personal card and a bank platform team have unrelated budgets, unrelated approval processes, and unrelated willingness to pay. Capping *everything* at $9/mo doesn't make you accessible to the bank — banks don't buy a $9/mo tool for a platform-wide sync layer, price signals credibility and support depth they need. It just caps your revenue from the segment that would pay 100–1000x more.
- Bottom-up spread and a low-friction indie tier are good instincts. Keep those. But "bottom-up" describes how the *indie tier* lands (self-serve, card, no sales call) — it doesn't mean the enterprise tier has to inherit the indie price.

**Recommended shape:**

| Tier | Buyer | Price | Motion |
|---|---|---|---|
| Solo/Indie | Individual dev, own card | ~$12–20/mo/seat (not $9 — leave room to not be "the cheap one nobody trusts with their data") | Self-serve, no sales |
| Team | Small startup team | Per-seat, scales with seats/devices/data synced | Self-serve up to a cap, invoicing optional |
| Platform/Enterprise | Bank platform team | Custom, annual contract, likely $20k–$150k+/yr driven by seats + environments + compliance needs | Sales-assisted, SSO, audit logs, on-prem/VPC option, SOC 2 |

Pick a value metric that scales (seats, synced devices, data volume, environments) — a flat fee anywhere in this stack gives you no expansion revenue as an account grows.

## The procurement-threshold question — and why "price just under it" won't work for a bank

There's no single universal number — it's set per-company policy — but the commonly cited **rule-of-thumb range** in SaaS/PLG pricing commentary is:

- **Under ~$500–$1,000/yr**: nobody notices, expensed freely.
- **~$1,000–$5,000/yr**: usually still card-swipeable, maybe needs a manager's nod.
- **~$5,000–$10,000/yr**: the common inflection point — many companies require a PO, a signed MSA, or finance sign-off above here.
- **Above ~$10,000–$25,000/yr**: procurement, legal, and security review become close to certain at most mid-size+ companies.

That range is real for a generic SaaS tool bought by a manager with a card. **It does not apply the way you're hoping for a bank buying a sync engine.** Banks trigger vendor security review by **category**, not by price:

- Anything that touches source code, customer data, or connects into internal infrastructure gets a mandatory InfoSec/vendor-risk review — SOC 2 report, pen test, DPA — regardless of whether the contract is $500 or $50,000. A local-first sync engine is squarely in that category.
- Pricing at $4,999/yr to dodge the procurement dollar threshold buys you nothing here. The security review happens anyway; you've just also capped your revenue at the same time.

**Implication:** don't try to price under a procurement line for the bank segment — assume the review is happening no matter what, and price to the value delivered to a platform team instead (engineering hours saved, outage/data-loss risk avoided), which lands well above any "avoid procurement" ceiling anyway. Where "price just under the threshold" *is* the right play is the **Team tier** — a growing startup, not yet bank-scale, where staying under ~$5–10k/yr keeps the sale on a manager's card instead of triggering a formal buying process.