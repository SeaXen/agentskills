# Brightwell pricing — holes found

**Bottom line:** this stacks two failure modes the skill names explicitly — an invented unit with no published conversion, and three compounding metrics — on a product where the invented unit is also the dominant line. It fails the skill's own predictability bar before a customer even sees an invoice.

## 🔴 Critical

**1. The credit is an invented unit with a conversion you're refusing to publish.**
Vendor-defined units only avoid reading as obfuscation when three things are true at once: a published conversion table, a calculator that takes the customer's own numbers, and stability — "silently reducing what a credit buys is a price rise plus a deception, and gets read as both." "We'd rather not publish a table because it moves with model costs" is that exact scenario, stated as a design choice. When your inference cost drops and you quietly tighten the actions-per-credit ratio to protect margin, customers cannot tell the difference between a legitimate cost pass-through and a stealth price increase — and they will assume the worse one.

Closest sourced precedent: GitHub Copilot's move to "premium requests" and then full usage-based billing (Jun 2025 → Jun 2026) — an ambiguous consumption unit on an AI dev tool produced a 435-comment FAQ thread at 904 downvotes to 22 upvotes. Same product category, same mechanism.

**2. Three compounding metrics.** Credits (consumption) + seats + per-repo fee is the skill's own named failure mode, verbatim: "Each one defensible alone; together they need a spreadsheet, and a bill that needs a spreadsheet does not get approved." "All three lines grow independently" is the income-statement version of that same sentence — it's a revenue-side virtue and a buyer-side defect. Nobody described what earns each layer its place; the hybrid-stack rule is "add a layer only when it earns it," not "add a layer because it's a distinct thing to bill."

**3. The self-set predictability test fails by construction.** The bar this skill holds itself to: a target customer estimates their bill from public materials in under two minutes, within ±20% of the real invoice, on three usage profiles (self-set baseline, not an industry number). With the conversion table withheld and "roughly one credit per action" immediately qualified as unstable, there's no public material to estimate from. This isn't a rough edge to smooth in the FAQ — it's the design.

## 🟠 Major

**4. No margin floor shown, on a product where one almost certainly bites.** Consumption-priced products need the floor computed at the 90th-percentile account, not the average, with a deliberate margin target — sourced figure: usage-only pricing sits at a 62% median gross margin against an 80% median for software generally, because inference/infra cost sits in COGS (Aleph × Benchmarkit, 2026). Nothing here says whether $0.10/credit was checked against actual model cost on the worst-case review action — a large diff or a multi-file monorepo PR plausibly costs several times what a two-line PR costs to review. If that check hasn't run, the price is a guess wearing a decimal point.

**5. The per-repo fee is the rejected candidate from this skill's own worked example.** "Repositories — rejected. Uncorrelated with value: one busy monorepo dwarfs fifty dormant repositories." Concrete failure: an org with 500 mostly-archived/forked/mirror repos pays $300/month in platform fees for near-zero review volume, while an org running everything through five monorepos pays $3/month while driving most of your actual inference cost. The fee taxes repo sprawl, not usage — it will feel arbitrary to exactly the customers who inspect it.

**6. Seats are a human-count metric bolted onto a bot-triggered product.** AI code review is invoked by CI on pull requests, not by someone logging in — this is the textbook seat-collapse setup: "value grows through automation, CI, service accounts or agents." Watch for flat-or-falling seat count while credit spend rises (the product doing more review work per human, which is the pitch), and for teams buying the minimum seats and routing everything through service accounts. If that happens, two of your three "independently growing" lines are actually decoupled from what's driving your cost, and the seat fee becomes a headcount tax rather than a value proxy.

**7. "Review action" itself is undefined, and the ambiguity is where the Copilot backlash actually came from.** Does a force-push retrigger a review and burn another credit? Does a flaky-infra rerun on the same commit? Value-metric test #4 — "does it punish retries or good engineering" — is unanswered. An unpublished conversion rate on top of an undefined unit is two layers of "trust us" stacked on the one line customers will scrutinize hardest.

## 🟡 Missing before this ships (Step 5 is a hard requirement, not a nice-to-have)

- No calculator for the metered component — required for any consumption line.
- No stated cap policy (hard vs. soft), threshold alerts, or anomaly detection. Without them, an individual developer or small team on a personal card carries open-ended downside on the credit line. The cautionary case here is Netlify's $104K bandwidth bill: different product, same root cause — no spend cap, no anomaly alert, and the vendor ends up forgiving the bill anyway. The credit is always cheaper than writing the cap up front.
- No free surface mentioned. A bottom-up motion needs a permanent entry rung with a real limit, not a trial — nothing here says whether an evaluator can run this on a real side project without a card.
- No ceiling check. What's the cheapest real alternative — a competitor's AI reviewer, a self-hosted model, or a team just doing manual review a bit longer? Nothing shown here bounds $12 + $0.60×repos + credits against it, and that's the number a technical buyer will reach for first.

## What to tell finance

"All three lines grow independently" is correct and is not the argument for this design — it's the argument against it. Three independently-moving numbers, one of them an unpublished ratio you've reserved the right to change, is the shape of a bill nobody can approve on sight. Before shipping: publish the credit conversion (even as a range, with a stated review cadence for how it can move), put a hard cap or a flat-fee floor under the credit line for the personal-card segment, and get a real answer for whether the per-repo fee is earning its place or just adding a third meter to a bill that already has two.