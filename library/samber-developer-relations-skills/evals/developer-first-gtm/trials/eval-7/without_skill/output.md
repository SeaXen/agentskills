Not broken PLG funnel. No PLG funnel exists. That's fight.

## Real diagnosis

12,000 free accounts = vanity number. Revenue source (100% SDR cold email) shows real motion already: sales-led, free signup = lead list, not self-serve top-of-funnel. Growth lead defends metric ("self-serve conversion") that never existed here. Sales lead defends motion that already works. Same fight every quarter because both argue over wrong noun.

0% self-serve upgrade normal for API gateway. Three reasons stack:

1. **Activation, not funnel.** Most of 12k likely never route real traffic. Define aha moment (custom domain set, N requests/day sustained, prod key generated). Measure % hitting it. Bet: under 10%. Zero-usage account can't self-upgrade — no pain felt, no reason to click.
2. **Buyer mismatch.** Dev who signs up rarely holds company card for infra spend. Gateway purchase needs procurement, security review, sometimes SSO. Self-serve checkout button solves wrong step of buying process.
3. **No usage pressure.** Check limit design: does hitting free-tier ceiling actually block or degrade something dev feels? If limit soft or generous, forcing function never fires.

## Stop debating, start measuring

Pull 3 numbers before planning meeting (query work, ~half day):

1. % of 12k that ever hit defined activation event
2. % of activated accounts that ever hit free-tier limit
3. Of accounts SDRs closed, were they activated + at-limit, or cold signups?

If #3 shows won accounts were activated/at-limit, usage signal predicts revenue. Score all 12k on same signal. Feed SDRs top-scored accounts first instead of blanket list. A/B test: prioritized queue vs current blanket queue, compare close rate. This is a real, cheap experiment — 1 sprint to build score, 1 quarter to see close-rate delta.

## Reframe for meeting

Kill agenda item "fix PLG funnel." Replace with "usage-scored lead engine." Free tier = qualification layer feeding sales, not self-serve top-of-funnel. Split ownership so leads stop fighting over same number:

- **Growth lead owns:** activation rate, usage instrumentation, lead-score quality (PQL volume/quality). Drop self-serve conversion % from scorecard — it's not this product's motion.
- **Sales lead owns:** PQL-to-customer conversion, SDR sequencing by score.
- **Shared metric:** revenue per free signup (blended). One number, two owners, ends "whose funnel" argument.

Also settle explicitly: does average contract value justify self-serve checkout at all? If deals need invoice/procurement anyway, drop self-serve upgrade as a goal entirely. Button working is fine — expecting cold click-to-pay from infra buyers is fantasy.

## Next action

Pull activation-event hit-rate across all 12k accounts before Monday. That single number kills or confirms half of this quarter's argument before anyone opens a slide deck.