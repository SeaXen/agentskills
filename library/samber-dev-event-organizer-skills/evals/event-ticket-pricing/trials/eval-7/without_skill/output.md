# Cascade API Conf 2027: price grid for Berlin, São Paulo and Bangalore

## 1. Price grid (USD equivalent)

Seattle stays at $850 / $420 / $120.

| Tier | Seattle (700 seats) | Berlin (300) | São Paulo (300) | Bangalore (300) |
|---|---|---|---|---|
| Corporate | $850 | **$750** | **$590** | **$440** |
| Individual | $420 | **$345** | **$235** | **$145** |
| Student | $120 | **$95** | **$58** | **$32** |

**Method.** The price is the Seattle price times (local price level ÷ US price level) raised to a weight. The weight is how much of the PPP gap to pass on to each tier.

| Tier | PPP weight | Why |
|---|---|---|
| Corporate | 0.5 | Employers budget in hard-currency terms. Salaries and software spend in Bangalore, São Paulo and Berlin tech firms are closer to US levels than local consumer prices suggest. |
| Individual | 0.8 | The attendee usually pays personally or expenses a small amount. This tier is mostly local purchasing power. |
| Student | 1.0 | Full adjustment. Local student budgets are the constraint. |

**Price level ratios used (US = 1.00).** These are my approximate values: Germany 0.78, Brazil 0.48, India 0.27. ⚠️ Check them against the latest World Bank ICP or OECD table before publishing. Small shifts move the prices by roughly 5%.

**Before you publish:**
- Charge in local currency (EUR, BRL, INR). Convert the USD figures at the rate on the day you publish, then round to local charm prices.
- Review the FX rate every six months. BRL and INR move enough to undo the adjustment.
- ℹ️ Seattle is pricier than the US average, so the real gap against Seattle is slightly smaller than these ratios imply. I ignored this. If you want to correct for it, nudge each city up about 5%.
- 🟠 Cross-border arbitrage is the main risk: a Seattle attendee buying a Bangalore ticket.
  - Travel cost already limits this.
  - Also require a billing country that matches the city, or a local company or student ID.
  - The corporate and student tiers need invoice-country checks anyway.
- 🟠 Check the unit economics per city. Venue, catering and AV costs don't scale with PPP. At 300 seats, Bangalore may only break even if the sponsor revenue is there. Run break-even per city before you lock the grid.

## 2. Corporate first, individual as "obvious middle": does it work?

**Partly. Corporate-first is fine. The "individual is the obvious middle" part works against you.**

✅ **Listing corporate first is fine.**
- High-to-low ordering is standard anchoring.
- It costs nothing, and a $850 ticket makes $420 look reasonable.

❌ **The decoy effect doesn't fit conference tiers.**
- A decoy works when the tiers are the same product at different feature levels, so buyers compare on one dimension.
- Your tiers are buyer types: who pays (employer or person) and who qualifies (student).
- Buyers don't compare tiers. They know whether their employer is paying, and they pick the tier that matches.

⚠️ **Steering buyers to the middle tier costs you money.**
- If most attendees are expensed by their employers, pushing "Individual" as the obvious choice sends corporate buyers to the cheaper tier.
- The $850 tier then becomes a decoy for $420. You lose up to $430 per seat on those buyers.
- Highlight the tier you want most buyers to take. For a conference that is usually Corporate, because it carries the most revenue per seat.

⚠️ **Corporate needs a real reason to exist.** Give it things employers care about:
- invoicing and PO payment
- VAT-compliant receipts
- group discounts (for example 5+ seats)
- a recording or slide-deck bundle
- a reserved-seat lounge or a sponsor-meeting pass

Without those, the only difference is price, and anyone with employer money will buy Individual.

**What I'd do:**
1. List Corporate first, and give it the "recommended for company-paid" badge.
2. Label Individual clearly as "paying yourself", and verify it at checkout (personal billing name, no company VAT ID).
3. Use time-based pricing as the real lever: early-bird, standard and late. Conferences get more from deadlines than from tier layout.
4. A/B test the layout on the Seattle page first. The metric is revenue per visitor, not conversion rate.
5. Don't copy one layout to every city. In Bangalore, where most buyers are individuals, highlighting Individual may be right. Test each city separately.

**One-line answer for the hire:** anchoring with a high first tier is fine, but nudging buyers toward the middle tier loses money when most attendees are company-paid.