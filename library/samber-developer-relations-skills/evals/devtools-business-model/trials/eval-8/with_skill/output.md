# Business model, Braidmark — Finance's per-call add-on

## What's actually happening

Seat count flat, API calls tripled, source is CI pipelines and coding agents wiring in automatically. That's not new demand — it's the same accounts moving migrations off named humans and onto machines. Per-seat pricing is decoupling from usage because usage no longer requires a seat.

## Reject the literal ask

Don't stack a per-call charge on top of full seat price, same accounts, both bills independent. That's charging twice for one expansion in value on the same customer relationship — consumption and seats measuring the same underlying activity. It fights itself:

- Customers can shrink the side that's easy to shrink (consolidate logins, cut named seats) while the side driving your cost — CI/agent calls — keeps growing untouched. Net effect: seat revenue erodes, call revenue absorbs the blame, total take may not even move.
- It reads to the buyer as a second bill for something they already pay for monthly. On a metric that's been $30/seat for multiple quarters, that's a trust event on renewal, not a neutral packaging tweak.
- Unbounded per-call billing with no caps or forecast tooling is exactly how consumption pricing dies: bill shock, then a public complaint from a dev audience that notices immediately.

## Recommended model: consumption primary, seat floor secondary

Restructure the value metric instead of adding a line to it.

- **Primary:** meter the thing actually driving cost and value — completed schema migrations executed via the API, not raw API calls (raw calls include health checks, dry-runs, retries the customer doesn't control; migrations executed is countable, forecastable, and the number the customer's own CI logs already show).
- **Secondary:** keep the $30/seat line, but re-scope it as a committed-spend floor, not an independent multiplier — the seat price becomes a monthly minimum credited against metered usage, with overage billed only above what the floor already covers. This is the combination the model explicitly supports (consumption plus a committed-spend floor), not the one that fights (consumption plus seats on the same value).

This keeps something Finance can put on a board slide (a revenue line that finally moves with the tripled usage) without billing the same automation twice.

## Paid boundary / value metric checks

- Already counted: yes — migration runs show up in the customer's own CI logs and agent run history.
- Grows with value: yes — more automated migrations is the value Braidmark delivers, not a side effect.
- Forecastable: only if you ship usage dashboards and spend caps/alerts before billing on it — not optional, it's the GTM cost of this model.
- Measurable in one sentence: "one metered unit per schema migration executed through the API, however it was triggered." Raw call count fails this cleanly; migrations executed passes.

## GTM consequence

- Build before billing: per-account usage metering, a customer-facing usage dashboard, spend caps/alerts, and a migration path for existing seat contracts (grandfather window, not a silent switch).
- First three investments in order: (1) usage metering + dashboard, (2) caps/alerts, (3) contract migration tooling for the seat→floor conversion.
- No new sales motion forced — this rides on existing accounts, not new logos.

## Leading indicator

Share of accounts whose metered usage already exceeds their seat-floor equivalent, read monthly. That's the population where the floor is under-pricing them today — it tells you the deal is there before you touch a single contract.

## Validation experiment (before touching any real contract)

Shadow-meter migrations-executed for 30 days across current seat accounts, show them what their invoice would have been under floor + overage, don't bill it. Passes if: (a) most shadow invoices land within a floor customers would recognize as fair given their seat spend, and (b) the metered total covers your actual per-migration compute cost with margin to spare. Fails if either the invoices spike unpredictably or the metric can be gamed by batching/caching calls without reducing actual migrations run.

## Risks

1. **Renewal-time trust hit.** Changing the value metric on live $30/seat contracts, even framed as a floor conversion, reads as a price change. Signal: renegotiation requests or churn spiking in the quarter after rollout.
2. **Metric gaming.** If you ever meter raw calls instead of completed migrations, customers batch/cache to dodge it. Signal: call volume drops sharply at rollout while independently-tracked migration count doesn't.
3. **Floor mis-sized.** Set the seat-floor credit too generous and the tripled usage still doesn't show up in revenue. Signal: metered overage revenue stays near zero despite the shadow-billing data showing real overage.

## Revisit triggers

- A major CI/agent integration multiplies automated volume again — re-check floor sizing before it compounds.
- Top-20 accounts show churn or downgrade requests above an agreed threshold within two quarters of rollout — failure condition, reopen with seat-only pricing as the fallback.
- A competitor wins switch deals on pure per-seat simplicity — re-examine whether the hybrid is worth the billing complexity it costs you.

Out of scope for this memo, hand to `devtools-pricing-strategy`: the actual $/migration rate, the floor size in seats-equivalent, and free-tier/overage tier shape. This memo settles the model question — meter the automation, don't double-bill it — not the price points.