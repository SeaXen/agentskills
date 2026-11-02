I can't give you a purchasing-power-adjusted grid, because the skill says there's no established method for one. It tells me to say so and let you decide, not to invent a formula. What follows is the structure to build the grid on and the scaling arithmetic. The numbers are self-set, not sourced.

## 1. Price grid for Berlin, São Paulo and Bangalore

**Seattle baseline ratios** (computed from your prices):

| Ratio | Seattle | Sourced range |
|---|---|---|
| Corporate : individual | 2.0 : 1 | 1.7 to 1.9 : 1 |
| Individual : student | 3.5 : 1 | 2.1 to 3.4 : 1 |
| Corporate : student | 7.1 : 1 | 3.7 to 6.5 : 1 |

The sourced ratios are from EuroPython 2026 and PyCon US 2026. Your ladder is steeper than both, especially at the student floor. Keep the ratios as the template, but decide on purpose whether the 7.1 : 1 spread is what you want.

**Scaling arithmetic.** The city factor is your choice. Pick each city's multiplier and read the prices off the matching column. The columns are arithmetic only, not a purchasing-power index for any city.

| Tier | Seattle (1.00) | ×0.75 | ×0.50 | ×0.35 |
|---|---|---|---|---|
| Corporate | $850 | $638 | $425 | $298 |
| Individual | $420 | $315 | $210 | $147 |
| Student | $120 | $90 | $60 | $42 |

Four constraints on the multiplier:

- **Set the floor from cost, not from Seattle.** The skill says to set the floor price from your own per-attendee cost, never from a comparable's floor. 300 seats carry a higher fixed cost per head than 700, so a deep discount may not cover the floor.
- **Treat the rungs differently.** Purchasing power mostly applies to the self-funded rungs, individual and student. The corporate rung depends on what an employer in that market approves without a purchase order. Berlin and São Paulo employers may not discount at all. Sanity-check each top rung locally.
- **Pick a currency per city.** That means EUR, BRL and INR price points, each rounded locally. EuroPython quotes "+ VAT", so check tax and registration obligations per country. Charging anything pulls those in, and cross-border sales can require local registration.
- **Publish the ratios and the rule.** If the grids differ, publish why, and keep the corporate and individual prices stable once they're public. PyCon held those flat while cutting its student price.

**Why I can't finalize the numbers.** The skill requires these before a ladder exists:

- **A budget with a ticket-revenue target.** Without one, a ladder under-prices tier by tier.
- **Comps subtracted from the 300 seats.** That covers sponsor allotments, speakers, organizers and volunteers, counted from the agreements you hold.
- **The payer mix per city.** It decides the shape of each ladder.

The same rules apply to each city: one dated gate, at most two public prices per persona, and a refund policy written before sales open.

## 2. Corporate listed first as an anchor, individual as the "obvious middle"

**It doesn't work as framed, and the skill gives no evidence that it does.** Three reasons:

1. **The anchoring advice is unconfirmed for tickets.** The skill's reference says real registration pages list personas in plain reading order, not in an anchoring order. It also says not to import anchoring advice from software pricing.
2. **These tiers aren't competing products.** Corporate, individual and student buy the same seat, split by who pays, and the buyer self-identifies. A decoy-middle design assumes buyers choose between options. Here a company-funded buyer who is nudged to "obvious middle" individual simply pays less. That is revenue leaking from your top-paying segment.
3. **The labels should name who pays.** "Corporate", "Individual" and "Student" read as self-descriptions a buyer can pick without justifying it.

**What to do instead.** List the tiers in plain order. If the marketer wants to test the layout anyway, run it as a measured experiment. Use the skill's persona-mix check: if corporate sells far below its planned share, either the payer mix was guessed wrong or the corporate price is above what employers approve without sign-off. Also note that listing corporate first is already the usual order, so the real change would be the "obvious middle" framing.

## Next question (1 of 10)

Does a budget exist for these three editions, with a total expense figure and the share assigned to ticket revenue? If not, I'd run `event-budget` first. Everything above stays provisional until it does.