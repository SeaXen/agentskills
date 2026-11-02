# Solstice Systems Conf: ticket decisions

## Decision

| # | Proposal | Verdict |
|---|---|---|
| 1 | Cut regular to 165 EUR now | ❌ Don't run |
| 2 | 48-hour flash code, 40% off | ❌ Don't run |
| 3 | Unannounced 90 EUR surcharge from Monday | ❌ Don't run |
| 4 | 15% group discount on any tier | ✅ Run, with the tier restriction below |

Run only #4. Hold prices, and do one diagnostic before touching any price.

## Why each one lands where it does

### 1. Cut regular to 165 EUR: ❌

- **It undercuts early buyers.** 165 is below the 190 EUR early-bird price. Everyone who paid 190 or 240 sees the price fall below what the discounted buyers paid. Expect refund requests and a lasting "wait for the next cut" habit.
- **It can't recover its revenue.** The numbers below are self-set arithmetic:

  | Scenario | Remaining 159 seats |
  |---|---|
  | All sold at 240 EUR | 38,160 EUR |
  | All sold at 165 EUR | 26,235 EUR |

  At 165 EUR you need about 110 sales just to match what 110 sales at 240 EUR would bring. The cut only pays if the status quo would sell fewer than about 110 of the 159 seats, and you don't know that yet.
- **It skips the diagnosis.** A slow sale can be demand, marketing, or price. `event-market-fit` separates the three, and the skill says to act on price only after that read. No one has done it.

### 2. 40% flash code: ❌

- **It's the cheapest price on the table.** 240 × 0.6 = 144 EUR, below both the early bird (190) and proposal 1 (165). Early buyers who paid 190 are 24% over the flash price.
- **It's a third discount step.** The ladder would then be early bird, regular, flash. The skill says a third phase works only as a late surcharge, never as a third discount. Extra discount steps read as pressure tactics and teach every buyer to wait for the next one.
- **It cannibalizes sales.** Buyers who would have paid 240 take the code instead. The flash needs at least 96 sales at 144 EUR to match 159 × 240 / 159... more precisely, to match 58 regular sales at 240 EUR, it must sell roughly 1.67 seats for each seat it displaces. That is hard to know in advance and hard to police once the code leaks.

### 3. Unannounced 90 EUR surcharge: ❌

- **It breaks the skill's "never" rule.** The skill says never announce a price increase the buyer couldn't have seen coming. A surcharge is legitimate only when it is published from the day tickets go on sale, and this one was never announced anywhere.
- **It punishes the wrong people.** Springing 240 → 330 EUR (+37.5%) on fence-sitters, who are the buyers you still need, looks like a bait-and-switch.
- **Its size isn't backed.** The one sourced surcharge is EuroPython's 1.5x step (EUR 300 → 450). Your +90 is smaller, but nothing here says it's right.
- **How to fix it if the team wants a deadline.** Announce a dated step publicly now, with real notice, and size it to the sourced range. Only do this after the market-fit read, and only if the read says price isn't the problem. I don't recommend leading with it.

### 4. 15% group discount: ✅ with restrictions

This is the skill's default bulk mechanic, and a 15% discount for five or more in one order is a published precedent (devopsdays Halifax 2026). Run it with these rules:

- **Applies to the regular 240 EUR tier only.** It never stacks on the early bird, a late surcharge tier, or any flash or promo code. Stacking discounts the same seat twice. GopherCon excludes its early and late tiers for this reason.
- **Threshold: 5 or more tickets in one order.** Self-service, no approval step. Without "same order" it becomes a code that circulates.
- **Floor check:** 240 × 0.85 = 204 EUR, which is above the 190 EUR early-bird price. No group buyer pays less than an early buyer did, so it creates no fairness problem. This is the reason to cap it at the regular tier.
- **If your buyers pay by invoice:** offer invoicing on request at full price, as a payment rail and not a discount. Do this only if you have an entity that can issue invoices. If not, drop it.

## What to do instead: ⏳ this week

1. **Get the sales data.** Pull sales per week since the early bird ended, split by buyer type if you can. You need 159 more seats in about 35 days, which is roughly 32 per week. Compare that with your actual recent pace.
2. **Run the market-fit read** (`event-market-fit`) to separate demand, marketing and price. Change a price only if it points at price.
3. **Check the budget target.** You gave no ticket-revenue target, so I can't say whether the current ladder is short. Total expenses minus the sponsorship share is what tickets must raise. If that number doesn't exist, run `event-budget` before any price move.
4. **Check comps.** The skill subtracts comps (sponsors, speakers, organizers, volunteers) from capacity before pricing. I took "250 paid seats" as already net of comps. Confirm that.
5. **Confirm the refund and transfer policy is published** beside the price, with a dated cutoff. If it isn't, write it now, before any price change.
6. **Hand acquisition to `event-marketing-plan`.** If the diagnosis says marketing is the gap, the lever is outreach to employer-funded teams (the group discount helps there), not a lower price.

## Assumptions and limits

- Early bird: 190 EUR, ended three weeks ago. Regular: 240 EUR. Stated by you.
- Sold: 91 of 250 (36.4%). Stated by you.
- All arithmetic above is self-set, not sourced. The skill has no benchmark for what sell-through is normal at five weeks out, and I'm not inventing one.
- I did not run the skill's full interview: payer mix, effort ceiling, recurring versus one-off, and community versus vendor-run are all unknown. If Solstice is vendor-run and priced against marketing budgets, a higher top price is more defensible, and the group discount matters less.