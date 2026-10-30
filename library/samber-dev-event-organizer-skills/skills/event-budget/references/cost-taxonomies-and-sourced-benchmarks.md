# Cost taxonomies and sourced budget benchmarks

## Table of Contents

- [How to read this file](#how-to-read-this-file)
- [Conference cost taxonomy](#conference-cost-taxonomy)
- [Hackathon cost taxonomy](#hackathon-cost-taxonomy)
- [The fixed-versus-per-head cut](#the-fixed-versus-per-head-cut)
- [Published itemized P&Ls](#published-itemized-pls)
- [Revenue-split actuals, side by side](#revenue-split-actuals-side-by-side)
- [Comp and scholarship allocation as a share of capacity](#comp-and-scholarship-allocation-as-a-share-of-capacity)

## How to read this file

Every figure below carries its organization, its year, and **the quantity it measures**. Those three things travel together; a number lifted without them goes wrong quietly. Two figures in this file measure something narrower than they appear to, and both are flagged where they sit.

Carry ratios across, not amounts. A per-person food cost from one country in one year is not a price for another; the useful content is its share of that event's total and its relation to the other lines. Amounts appear here - this is a budget skill and its sources are budgets - but they belong in this file, not in a recommendation.

## Conference cost taxonomy

Source: a community-conference organizing guide, public repository. Named income and expense categories, not a worked budget.

**Income:** sponsors, registrations. The guide frames sponsorship as potentially up to three-quarters of income depending on the tiers set, and states an operative target of 80%+ of budget from sponsorship once its scope-tier mechanic is in play.

Registrations are framed as filling the remainder - "price your registrations to cover the per-attendee costs" - not as the primary engine. This is organizing-guide guidance, **not an audited actual**.

**Expenses:**

- Venue.
- Internet (attendee access provisioning).
- Media (livestream, recording, captioning).
- Catering (breakfast, breaks, lunches; some venues mandate their own).
- Evening event.
- Merchandise.
- Badges and lanyards.
- Signage.
- Speaker expenses (speakers' dinner, small appreciation gifts).
- Administrative costs (insurance, taxes, accounting services).
- A per-edition contribution to the parent community, introduced 1 January 2025, sized at the equivalent of at least one full-price attendee ticket, payable any time between tickets going on sale and the first day. A free event owes nothing under that rule, since the amount is the ticket price multiplied by zero.

**Spend-approval process, from the same guide:** all major expenditures go to the organizing team for approval, to prevent conflict of interest and provide oversight. The common pattern is an organizer paying directly and claiming reimbursement, with sign-off required from at least one other organizer - never self-approved. The guide draws an appropriateness line inside overhead spend, and gives **no fixed threshold** - the test is local team judgement against regional norms:

- Reasonable: travel to run or learn from an event, local transport, team clothing, meeting food at typical regional prices.
- Not reasonable: organizer-only gifts, above-market meeting food, travel beyond participation needs.

**Money handling, from the same guide:** an event cannot announce a date until it has a working way to process money - "realizing too late that you cannot process money has led to rescheduled or canceled events." The typical solution is a local company handling invoicing and payment logistics, sometimes compensated with a sponsorship in return, and required outright in some countries for tax reasons. Run ticketing and sponsor payment links through the same processor account so invoicing flows through one place.

## Hackathon cost taxonomy

Source: a major hackathon-league organizer guide, public repository. A different shape from the conference taxonomy - food-dominant - and the two must not be blended.

**Categories, in the guide's own order of emphasis:**

- Food - named as one of the most significant costs and a primary driver of participant experience.
- Communication platform - free at base tier; budget only for an upgrade.
- Swag - shirts, stickers, bottles, lanyards.
- Prizes - the guide steers toward prizes with learning value over pure cash.
- Web hosting and internal tooling - flagged as the cost most often overlooked; student-run events can source much of it free through education programs.

**Per-person unit benchmarks (that guide's own figures, US hackathons):**

- Food: $8-10 per person per meal.
- Snacks and drinks: $10 per person.
- T-shirts: $5-8 per person, volume-dependent.
- Buses: $3,500 per bus, where transport is provided.

These are the source's absolute figures in its own market and year - carry the _relations_ across (food per meal against shirt cost against a bus) rather than the amounts.

**Meal claim-rate curve** (same guide, sourced from one university team's QR-code check-in data, generalized ±10%):

- Day 1 lunch: ≈90% of total registrations.
- Day 1 dinner: ≈80%.
- Midnight snack: ≈70%.
- Day 2 breakfast: ≈30%.
- Day 2 lunch: ≈60%.

Sponsor, volunteer, mentor and organizer allocations are ordered on top of these percentages, not inside them. The practical read: taper meal quantity per meal instead of ordering flat at headcount - the same add-late-rather-than-over-commit asymmetry the outflow menu ranks, applied at meal granularity.

**Contingency buffer** (same guide): a flat **$1,000-$3,000**, scaled to event size - "organizers will always need this extra money". The source gives **no percentage-of-budget framing**; it is a floor amount, not a share, and it is one organization's recommendation rather than an industry convention.

## The fixed-versus-per-head cut

This cut is **a convention carried over from general financial modelling, not measured against event data**: a fixed/variable split cross-cutting functional cost categories, applied to an event budget. The two taxonomies above group lines by function, not by whether a line moves with headcount.

Applied to them, the assignment of each named line below is **this skill's own construction**:

- **Fixed** - venue rental, signage, media production setup, insurance, accounting. None of them moves with the twentieth extra attendee.
- **Per-head** - catering quantity, badges and lanyards, swag, meal counts. All are driven by the expected-show-up number.
- **Per-speaker** - speaker expenses. A third driver, neither of the first two, and named as its own. Split it in two: the speakers' dinner and gifts named in the conference taxonomy above, and travel and hotel reimbursement, which that taxonomy does not name. Reimbursing speakers' travel and hotel is normal at community events, while speaker fees are not the norm. The reimbursement line scales with how far each speaker travels, so carry it per confirmed speaker, never as a flat share.

The same financial-modelling material names the cash-timing mismatch directly: revenue is not cash, because of payment terms, and expenses are paid before revenue is collected. That naming is the part that carries over. The recurring-revenue mechanics around it (retention, lifetime value, payback period) do not transfer to a single bounded edition and are not used here.

Its expense-buffer heuristic - "add 20% buffer to expense estimates" - is format-agnostic and usable, but it too is **a convention carried over from startup financial modelling, not measured against event data**. It is not an event-industry convention and must never be presented as one.

## Published itemized P&Ls

Source for this whole section: tech-conference budget benchmarks and fiscal structures. Its own coverage note: open, dollar-figure P&Ls are almost exclusively published by community and non-profit-run events; for-profit conferences do not disclose them.

### DebConf21 (online, 2021) - proposed budget

From a budget-proposal thread on the project's development mailing list. Ledger convention in the original: expenses positive, income negative.

- Registration income: 45,000 USD
- Sponsor income by tier: bronze 3,000; silver 2,000; gold 20,000; platinum 12,000; supporter 8,000 - total ≈45,000 USD
- Expenses: bursaries 13,100 USD; swag, pins, shirts and shipping ≈5,300 USD; video 100 USD
- Projected surplus: 30,000 USD

Quantity note: this is a **proposal**, not an actual. The online format also removes venue and catering entirely, which is why the expense side is unrepresentative of an in-person edition.

### DebConf16 (Cape Town, 2016) - final report actuals

- Total sponsorship raised: 152,850 USD, plus separate merchandise sales
- Registration: 16,000 USD, contributed by 59 attendees paying the professional or corporate fee
- Split: roughly 90% sponsor-funded / 10% registration-funded

Quantity note: this event's attendance is free by default, so the 90/10 split is a consequence of that model, not a target anyone set.

### IETF 79 (Beijing, 2010) - actual-versus-budget financial statement

- Registration revenue: 666,646 USD actual against 677,125 USD budgeted
- Cash sponsorship revenue: 30,000 USD
- In-kind sponsorship (meeting space and network operations): 275,000 USD
- Total revenue 971,646 USD; total expenses 616,441 USD
- Surplus to the parent organization: 355,205 USD, 45,344 USD above budget

Quantity note: registration is ≈69% of **cash** revenue and cash sponsorship ≈3%. The large in-kind component sits outside that cash ratio entirely - the sponsorship contribution to this event is materially larger than 3% in value, and quoting the cash figure alone misdescribes it.

### PSF / PyCon US 2023 - parent-organization financials

- Parent-organization total revenue 4,356,000 USD against 4,508,000 USD expenses (a small loss)
- PyCon US spending: 1,800,000 USD of that total
- Other lines: grants 677,000 USD; infrastructure including the package index 286,000 USD; fiscal sponsorees 204,000 USD
- Historical dependency ratio: the conference generates 63-65% of the parent organization's total revenue (63% in the 2019 report, 65% in the 2020 report)

⚠️ **Quantity note, load-bearing:** that 63-65% is an **event-to-parent-organization dependency ratio**, not a within-event sponsor-to-ticket split. The conference's own standalone P&L is not published anywhere; only its share of the consolidated statement is. Do not cite it as a revenue-mix figure.

## Revenue-split actuals, side by side

| Event, year                                                    | Sponsorship share                                                         | Registration share                           | Basis                                                |
| -------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------- | ---------------------------------------------------- |
| Community-conference organizing guide (guidance, for contrast) | up to 75%; 80%+ stated as the scope-tier target                           | remainder, priced to cover per-attendee cost | organizing-guide guidance, **not an audited actual** |
| DebConf16, 2016                                                | ≈90% (152,850 USD)                                                        | ≈10% (16,000 USD, 59 paying registrants)     | final report actuals                                 |
| IETF 79, 2010                                                  | ≈3% of cash (30,000 USD), plus 275,000 USD in-kind outside the cash ratio | ≈69% of cash (666,646 USD of 971,646 USD)    | audited-style financial statement                    |
| PyCon US / PSF, 2019-2020 reports                              | not separable in a single event P&L                                       | -                                            | see the dependency-ratio warning above               |

The three actuals disagree almost completely, and a structural choice explains each disagreement. Free-by-default attendance pushes one to ≈90/10; heavy in-kind provision of space and network pushes the other to a cash split that understates what sponsors actually contributed. Read the table as the range of postures that exist, never as a norm.

## Comp and scholarship allocation as a share of capacity

### PyCon US 2019

- 143 financial-aid recipients, from the parent organization's 2019 annual report
- Aid spend: 137,200 USD, a 17% increase over 2018
- ≈**4.4% of capacity received financial aid**

⚠️ **Caveat that travels with this figure, every time it is used:** the 4.4% divides 2019's recipient count by **2018's** checked-in attendance (≈3,260) rather than a same-year figure. It is an approximation across two different years, not a same-year ratio. Present it as an order of magnitude - "a low single-digit percentage of capacity" - and never as a precise allocation rule.

### DebConf (structural, not a single year)

No separate scholarship tier exists: attendance is free by default for community members, and only professional (200-650 USD) and corporate (1,000-1,300 USD) registrants pay. Effectively close to 100% of capacity is subsidized, funded by the 5-10% of attendees who pay a fee. This is the same structure behind its ≈90/10 revenue split above.

### What this does and does not close

It anchors the order of magnitude and nothing more. It does **not** produce a comp-allocation rule, and no percentage from one large conference transfers to a per-city community conference or to a private-sector one. Count committed comps from the agreements actually held - signed sponsor allotments, confirmed speakers, organizers, volunteers - and use the anchor above only as a sanity check on the order of magnitude.
