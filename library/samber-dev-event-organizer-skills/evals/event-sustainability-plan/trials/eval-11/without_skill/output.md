# Marrowgate Connect (Chicago, ~2,000 attendees): GHG inventory boundary, v0.1 draft

## Read this first

I set up the Scope 1/2/3 structure and a "paid by Marrowgate" view that matches finance's request. I did not make the three exclusions silent, and I did not use "what we pay for" as the boundary rule. ⚠️ Three reasons:

- **The GHG Protocol doesn't draw boundaries by who pays.** It draws them by organizational control (Scope 1 and 2) and by value-chain influence (Scope 3). Scope 3 is, by definition, emissions that sit on someone else's books, so "it's their problem" doesn't exclude an item.
- **Speaker flights, sponsor travel and venue electricity are Scope 3 for Marrowgate if the event causes them.** Venue electricity is the venue's Scope 2, and Marrowgate's Scope 3 (upstream leased assets or purchased services). Both can be true at once. Scope 3 double counting across companies is by design.
- **"Only what we pay for" would also drop attendee travel,** which is usually the largest block for a 2,000-person conference. An inventory that drops it will look very low, and an auditor or reviewer is likely to challenge that.

The GHG Protocol lets you exclude Scope 3 sources if you disclose the exclusion and justify it. Valid reasons include materiality, no data, or no influence. "Someone else pays" is not on that list. So the boundary below has two tiers. Finance gets its paid-by-us number, and nothing is excluded without a written reason.

## 1. Boundary rules

| Item | Setting |
|---|---|
| Reporting entity | Marrowgate (same consolidation approach as the corporate report; see open question 1) |
| Inventory unit | Marrowgate Connect, Chicago, one event cycle: build-up, show days, tear-down |
| Gases | CO₂, CH₄, N₂O, plus refrigerants if applicable; reported as CO₂e |
| Structure | Scope 1, Scope 2, Scope 3 by category, as the corporate report requires |
| Tier A | Emissions from activities Marrowgate pays for or directly controls. This is the figure that feeds the corporate report. |
| Tier B | Emissions the event causes but others pay for. Each item is either quantified and reported as a separate line, or listed in the exclusions register with a reason. |
| Double counting | Staff travel and office energy already in the corporate inventory are tagged and not added again. |

## 2. Scope structure

| Scope or category | What goes in | Tier |
|---|---|---|
| **Scope 1** | Fuel in Marrowgate-owned or operated vehicles and generators, refrigerant leaks from equipment it operates. Likely ~0 for a rented venue. | A |
| **Scope 2** | Electricity, heat or cooling at premises Marrowgate controls. Likely ~0 at a rented venue unless the contract hands you operational control of the building on event days. | A |
| **Cat 1: purchased goods and services** | Catering, AV and staging production, registration and badges, printing, swag, signage, agency fees. If the venue bills energy or utilities in the rental price, they sit here. | A |
| **Cat 4: upstream transport** | Freight of staging, booth materials and swag, if Marrowgate pays | A |
| **Cat 5: waste** | Waste and recycling from build, show and tear-down | A |
| **Cat 6: business travel** | Marrowgate staff and contractors: flights, hotels, ground. Speaker travel that Marrowgate books or reimburses goes here too. | A |
| **Cat 8: upstream leased assets** | Venue electricity, heat and cooling during the contract period. This is Marrowgate's Scope 3 and the venue's Scope 2. | B (or A if separately billed) |
| **Speakers, self-funded** | Flights and hotels paid by the speaker's employer | B |
| **Sponsor staff** | Travel and lodging paid by sponsors, plus booth builds and shipping they pay for | B |
| **Attendees** | Travel to and from Chicago, hotel nights | B |

For attendee, speaker and sponsor travel, no standard category fits cleanly. Practice varies between Cat 9 and "other downstream". Pick one, state it in the methodology, and keep it fixed year to year.

## 3. How your three exclusion instructions map

| Instruction | Handling | Disclosure line |
|---|---|---|
| Exclude speaker flights, employers pay | **Split by who pays.** Speakers Marrowgate books or reimburses go in Cat 6 (Tier A). Self-funded speakers go in Tier B. | "Self-funded speaker travel: [included as a separate line / excluded: reason, estimate]" |
| Exclude sponsor staff travel, sponsors' problem | Tier B, not Tier A. Quantify with a simple estimate (sponsor headcount × origin distance). | Same pattern. Sponsors may need this data for their own Scope 3. |
| Exclude venue electricity, venue's Scope 2 | Not Scope 2 for you, but Scope 3 Cat 8 or Cat 1. Report it if the contract separates energy, or estimate by area × event days × a building intensity factor. | "Venue energy: included as Cat 8 estimate / excluded: no metered data and below materiality threshold" |

If finance still wants all three out, the decision is theirs. It needs to appear in the exclusions register with a reason from the allowed list (materiality, data, influence), plus an order-of-magnitude estimate of what was left out.

## 4. Exclusions register (template)

| Source | Status | Reason | Estimated size | Owner | Review date |
|---|---|---|---|---|---|
| Self-funded speaker travel | open | ... | ... | ... | ... |
| Sponsor staff travel | open | ... | ... | ... | ... |
| Venue energy | open | ... | ... | ... | ... |
| Attendee travel | open | ... | ... | ... | ... |

Fill each row with either "included, see line X" or "excluded", with a reason and an estimate. A row with no estimate is not an exclusion, it's a gap.

## 5. Methodology notes

- **Spend-based first, activity-based later.** Use EEIO spend factors for Cat 1 (catering, AV, printing) now, and replace the largest lines with activity data (meals served, kWh, kg) as vendors supply it.
- **Attendee travel** comes from registration data: origin city or ZIP, mode assumption by distance, flight distances with a radiative-forcing treatment you choose and document.
- **Public claims:** Tier A alone must not be presented as "the event's footprint". Any external statement ("X tonnes for Marrowgate Connect") should say which tiers it covers.

## 6. Open questions

1. **Consolidation approach:** does the corporate report use operational control, financial control or equity share? The scope assignment must match it.
2. **Venue contract:** is energy billed separately or included in the rental, and is it sub-metered?
3. **Who pays what:** does Marrowgate cover any speaker flights, hotel blocks or sponsor shipping? This sets the Tier A/B split.
4. **Overlap:** which Marrowgate staff travel and office energy is already in the corporate inventory, so I can tag it and avoid double counting?
5. **Materiality threshold:** does the corporate report use a threshold, such as 1% of the total, that defines "not material" for exclusions?
6. **Attendee data:** is origin location available per attendee, or only country or region?

Answers to 1, 3 and 5 would let me make this v1.0. Tell me whether finance accepts the Tier A/B split. If they want a strictly pay-only version, I'll build it with the register above attached.