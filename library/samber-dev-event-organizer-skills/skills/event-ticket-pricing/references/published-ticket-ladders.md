# Published ticket ladders: real prices and dates

Every figure here belongs to one named event, on one date, in one market. Each event's own dates are given inline. Transpose the **ratios**, never an amount, across scale, region, or year.

## Contents

- Persona ladders (two full, published examples)
- Gating mechanics (date, ceiling-only, volume)
- Group and bulk mechanics
- Cross-subsidy tiers
- The free-by-design case
- How to transpose

## Persona ladders

**PyCon US 2026** (`us.pycon.org/2026/attend/information/`):

| Tier               | Price |
| ------------------ | ----- |
| Corporate          | $899  |
| Individual         | $469  |
| Student / academic | $139  |

Ratios: corporate:individual ≈ 1.9:1, individual:student ≈ 3.4:1, corporate:student ≈ 6.5:1. Tutorials are priced separately at $150 each - an add-on, not a rung of the ladder.

**EuroPython 2026** (`ep2026.europython.eu/tickets/`): three pass types (tutorial-only, conference-only, combined), each split Business / Personal / Education. Conference-only, for example: Business €500 + VAT, Personal €300, Education €135.

Ratios run lower than PyCon's: business:personal ≈ 1.67-1.78:1, personal:education ≈ 2.1-2.2:1, business:education ≈ 3.7-3.8:1.

The same three-way payer split (employer-funded, self-funded, student or educator) recurs under different label words with materially different ratios. Across these two events the top-to-floor range is roughly **1.7:1 to 6.5:1**, so report the range, not a single number, since one number would just be an average of two events.

## Gating mechanics

Three distinct mechanics exist, and none of these events runs more than two public price points in its time ladder. Where a third phase exists, it is a surcharge, not a third discount step.

- **Date-gated, surcharge form** - EuroPython 2026: regular price until 26 June 2026, then a "late-bird" step up (conference-only Personal €300 → €450, a 1.5x step). The price rises on a published date rather than a discount quietly expiring.
- **Date-gated, two-phase discount form** - devopsdays Austin 2023: Early Bird 15 Feb – 14 Mar, General Admission 15 Mar – 3 May. Prices sat behind a ticketing widget and were not published on the page; the two-phase date structure is the sourced part.
- **Ceiling-only disclosure** - devopsdays Minneapolis 2024 published one number: "before the price goes up to $299 on April 16th". The post-deadline price is public, the early price is not. A legitimate minimal shape: one announced date, one announced ceiling.
- **Volume-gated** - PyCon US: "the first 800 tickets sell with an Early Bird discount, and go fast" (PyCon 2016 registration post). The gate is a ticket count, not a calendar date, which caps the discount's cost instead of its duration.

## Group and bulk mechanics

- **devopsdays Halifax 2026** (`content/events/2026-halifax/registration.md`): "Groups of 5 or more get 15% off in the same order" - a flat percentage, self-service, stacked on whatever base price is active.
- **GopherCon** (gophercon.com): 5% off for 5-9 tickets, 10% off for 10 or more, applied **only to standard general-admission tickets** - explicitly not to the "Early" or "It's Go Time (Late)" tiers. This exclusion is the mechanic worth copying: it stops one seat being discounted twice.
- **devopsdays Amsterdam 2023-2024**: pay by invoice on request for bulk company orders. This is a **payment rail, not a discount** - full price, different rail. Sourced pages describe it as solving a corporate procurement problem, never as a price reduction.

## Cross-subsidy tiers

- **RailsConf** (railsconf.org): "Supporter Tickets… priced at a premium to help fund our programs and operations, including the Scholars and Guides program" - a voluntary pay-more tier whose premium is earmarked for a named accessibility program, distinct from a VIP upsell that buys the buyer something.
- **PyCon US**: the same cross-subsidy achieved through sponsorship rather than a ticket tier - a needs-based financial aid program (average grant roughly $700 in 2017) with reduced-rate tickets reserved for aid recipients, funded by sponsorship revenue.
- **PyCon US price commitment** (PyCon blog, 2016): "not only have we kept our Individual and Corporate prices stable as the conference has moved into larger and more expensive venues, but we have slashed our Student ticket prices by more than 40% over five years." The sourced counter-example to "scaling forces price increases" - prices held or cut deliberately, funded by sponsorship.
- **XOXO 2024** (xoxofest.com/guide/inclusion): pass price cut from $500 to $250 by shortening the program, framed as "a fair compromise" for "a small, independent festival" after losing the sponsorship that had funded roughly 20% free passes in 2018. Prices can move **down** as an event scales back.

## The free-by-design case

**FOSDEM** (`fosdem.org/2026/practical/`): "FOSDEM is free to attend. There is no registration. Just turn up!" - no ticket, no badge requirement, no registration step. Funded by sponsor contributions and on-site merchandise; donations accepted, never gating entry.

This is a full multi-track conference that could charge and deliberately does not. It is not the same as a free hackathon, where the format has no ticket-revenue line to begin with - FOSDEM is the sourced case of a priced model being available and refused.

## Nominal-fee rule

One organizer guide (devopsdays, `content/page/organizing.md`, "Ticket Pricing" → "Minimal Cost") publishes an actual rule rather than a price: charge **10-20% of what a typical commercial tech-conference ticket costs in the region**. The ticket's job is financial-risk spreading rather than funding. The same guide targets 75-80%+ of the budget from sponsorship (its budgeting section says "up to 75%", its Good/Better/Best targets say 80%+).

It also names the cost side: charging anything pulls in accounting and tax overhead, and the guide's own cross-border example is an organizing company needing a tax ID in another country, at a cost that "would take a significant portion of the event money."

## How to transpose

1. Pick the comparable whose **payer mix** matches yours, not whose city or headcount matches.
2. Set your floor price from your own per-attendee cost and your posture, never from the comparable's floor.
3. Apply the comparable's **ratio** to get the next rung up, then sanity-check the top rung against what an employer in your market approves without a purchase order.
4. Where two comparables disagree by 2x on a ratio - as PyCon and EuroPython do on corporate-to-student - pick the one whose funding model matches yours and say which you picked.
5. Re-read the source page before reusing any figure here. Registration pages change every edition. Each number above is a snapshot, not a standing fact.
