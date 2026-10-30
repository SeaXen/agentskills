# Cash flow, fiscal hosting, and the tax question

## Table of Contents

- [Outflows: when money leaves, and what leaving costs](#outflows-when-money-leaves-and-what-leaving-costs)
- [Inflows: when money arrives](#inflows-when-money-arrives)
- [What comes off the top](#what-comes-off-the-top)
- [Fund-access timing](#fund-access-timing)
- [The tax question, as contrast rather than rule](#the-tax-question-as-contrast-rather-than-rule)

Everything here is about **when money moves and what it costs to move it**, not what anything should cost. Each figure carries its source and date. The tax section deliberately states no rule.

## Outflows: when money leaves, and what leaving costs

### Venue and supplier deposits

Generic event-planning industry-guide mechanics, not figures measured on any particular event: deposits typically run **25-50% at signing**, with the balance due **14-30 days out**. Large conferences (300+ attendees) are typically booked **9-18 months ahead**, which sets the practical floor on how far in advance a capacity decision has to be made.

Post-2020, venues are frequently unwilling to renegotiate committed minimums (industry commentary, 2023). That is a structural tightening relative to every pre-2020 case study: a budget model that assumes a minimum can be talked down later is modelling a market that no longer exists.

### Attrition thresholds and food-and-beverage minimums

These are the core financial exposure of a venue contract: the organizer can owe the shortfall even when actual attendance comes in below the block or minimum committed to. The exposure is owed on the **commitment**, not on the turnout, which is precisely why cutting a fixed structural line late can cost more than keeping it.

One concrete instance from a community-conference organizing guide: a hotel offering a courtesy room block to an event that is _not_ also buying its meeting rooms and catering may require a guarantee that **at least 80% or so of the blocked room-nights are used**. The same guide's own mitigation is the staged posture in miniature:

- Start with a very small block, as few as 5 rooms.
- Scope it only to the nights genuinely needed - the night before day one and the night between days, explicitly not the night after the final day.
- Grow it as it fills, since hotels will generally allow additions.

The group rate code typically expires roughly a month before the event, which is a date the plan has to carry.

### The commitment-timing rule, in the source's own words

Same guide: "Don't overcommit on the number of people coming and don't do a pre-payment for the venue until you must. The same goes for food: it's always easier to add a few extra plates as opposed to having too much food ordered."

The asymmetry is the whole argument. Under-committing early and scaling up late is cheap and fast; over-committing early and scaling down late is expensive or impossible. Mark each commitment with its **latest safe date**, not the earliest possible one.

## Inflows: when money arrives

### Sponsorship payment schedules

Real published terms from event sponsorship agreements. Each is one organization's terms, not a market standard:

- One professional association (2021 conference): minimum **50% deposit due with the application**, due immediately on invoice receipt, with full payment by a fixed date; applications after that date require 100% upfront.
- One awards program: **80% on sign-up, 20% three months before the event** - collapsing to 100% in one installment if signing falls within three months of the event.
- One defence-industry conference (2026 contract): **100% deposit at signing**, no installment at all.
- One compliance association: balance in full on application submission and within 15 days of invoice receipt.
- One large language-community conference (2020): **full payment must accompany the form** to secure the space - 100% upfront with no installment path.

**Pattern:** real terms skew heavily toward large upfront commitments (50-100% at signing or application) rather than even installments. Generic vendor-agnostic guidance describing "deposit on signing, balance 30 days before the event" is a fallback pattern, not a verified figure - do not cite it as one.

Late-payment interest, where it is expressly stated in these contracts, runs **12-18% per annum**. Without an express clause there is no contractual right to interest at all. Drafting the clause belongs to `samber/dev-event-organizer-skills@event-sponsor-agreement`, not to budgeting; it matters here for one reason only: a sponsor who signs and pays late moves the inflow date the whole cash-flow model rests on.

### Ticket revenue

Ticket money arrives across the sale window rather than on one date. It spikes at named moments:

- Announcement.
- An early price ending.
- Speakers announced.
- The agenda published.
- Comp codes going out.
- After any reminder.
- In the final fortnight.

The shape of that curve, and what a shortfall against it means, belong to `samber/dev-event-organizer-skills@event-market-fit` and `samber/dev-event-organizer-skills@event-ticket-pricing`. What the budget needs from it is only this: **it is the latest-arriving revenue line, and it is the one that can miss.** That is the entire case for the sponsor-led posture and the downgrade ladder.

## What comes off the top

### Fiscal-host and fiscal-sponsorship fees

These are facts about a market, not recommendations - no host is being recommended.

| Host type                                      | Fee                                                                                                                                     | Date and status                                                                                                |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| One open-source funding platform, legacy model | 5% on card payments, 8% on manual bank transfers and checks                                                                             | ⚠️ **superseded** - see the row below                                                                          |
| The same platform, current model               | subscription-based; hosts still charging a host fee pay the platform a 15% share of that host-fee revenue                               | **changed March 2026** - verify current terms before citing                                                    |
| Its associated 501(c)(3) fiscal sponsor        | -                                                                                                                                       | **dissolved 31 December 2024**, displacing 600+ collectives; the platform continues under a separate 501(c)(6) |
| One software-freedom non-profit                | 10% of most member-project revenue and donations; higher negotiated for event-heavy projects                                            |                                                                                                                |
| One lighter-touch public-interest non-profit   | 5% of gross revenue, with fewer services in exchange                                                                                    |                                                                                                                |
| One student-focused fiscal sponsor             | flat 7% on all incoming funds, with no card, monthly, processing, legal, startup, transaction, card-issuing or subscription fees on top |                                                                                                                |

⚠️ **The 5%/8% row is legacy and must never be stated as current.** That platform's fee model changed in March 2026 and its associated 501(c)(3) fiscal sponsor dissolved at the end of December 2024. The dissolution is worth naming to an organizer currently sponsored there for a reason beyond price: displaced collectives had to migrate hosts, not merely absorb a fee change - a continuity risk, not a budget-line risk.

Published fiscal-sponsor fees typically run **7-14%**. Against that range the flat 7% sits at the low end and 10% mid-range; the legacy 5%/8% split by payment method was cheaper than both, which is exactly why quoting it as current would understate the deduction.

### Payment processing

Charged on both rails - ticket sales and sponsor payments - on top of any host fee. Running both through one processor account keeps the accounting in one place.

Any non-zero ticket price also pulls in accounting and tax handling that a free event does not carry. One organizer guide notes the cross-border case: an organizer running an event in another country may need a tax identifier there, and the cost of obtaining it can take a significant portion of a small event's money.

## Fund-access timing

From a hackathon organizer guide, as a pre-flight checklist. The budget-critical line is the last one:

- Can the organizing entity accept donations, and by what mechanism?
- Is the event covered by an institution's insurance, or are waivers needed?
- Who has signing authority for sponsor agreements, and how long does that review take? A slow signing process delays sponsor cash actually landing - a cash-flow risk, not only a legal one.
- Where are funds held, how are they accessed, what fees apply, and **what is the realistic timeline for actually being able to spend funds once they arrive in the account?**

That last question gates whether pre-event deposits can be paid on time at all. Ask it before the first deposit date is agreed, not after.

## The tax question, as contrast rather than rule

⚠️ **Nothing in this section is a rule, a rate, or advice.** The two contrasts below exist to show the reader that the question is real and has genuinely different answers in different places, so they route it to the fiscal host, a local accountant, or counsel instead of assuming. Tax treatment changes, and any of this may already be out of date.

**One large bloc:** admission to events, exhibitions and conferences is taxed **where the event physically takes place**, regardless of attendee or organizer domicile. Sponsorship is taxed under a different basis entirely - the payer's jurisdiction, under the general business-to-business rule. So the same event can face one treatment on tickets and several simultaneously on sponsorship, if its sponsors sit in different countries.

A bundled sponsorship-plus-booth package takes the treatment of whichever element an authority judges to _dominate_ the bundle - a practical argument for itemizing sponsorship and space separately rather than selling one blended line. A change effective 1 January 2025 moved virtual and livestreamed events to a consumer-location basis.

**One federal system without a national sales tax:** admissions taxation is set state by state, and non-profit status does **not** by itself settle it:

- One state exempts admission charges only where the organization qualifies under a specific charitable classification.
- Another has taxed admissions from non-profit-produced events since 2014, regardless of status, unless a specific short-duration or fundraiser exemption applies.

Separately, sponsorship and advertising revenue for a charitable organization there is generally an unrelated-business-income question rather than a sales-tax one - a different mechanism entirely, and conflating the two produces confidently wrong advice.

**What to do with this in a budget:** carry a named line for tax handling and a named open question - "who confirms the treatment of ticket revenue and of sponsorship revenue in this jurisdiction, and by when" - with an owner and a date. Record the answer when it comes back. Never state the answer yourself.
