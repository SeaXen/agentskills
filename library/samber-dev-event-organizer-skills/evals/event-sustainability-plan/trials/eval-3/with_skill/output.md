# Oakmere Data Days, 2nd edition: does moving Frankfurt → Amsterdam cut carbon?

## The answer

**The move saves nothing measurable. On your billing mix it is a wash, and it leans slightly worse.**

- Average one-way distance per attendee comes out about **+1% longer** for Amsterdam, which I'd call a ±3% wash (table below). Frankfurt is already near the audience's centre.
- Amsterdam wins on the US group (about −350 km one way). It loses on India (+300 km) and Germany (+185 km), and is marginally worse on the rest of the EU and the rest of the world.
- Frankfurt is also a rail hub (main station plus the airport long-distance station), so Amsterdam has no rail advantage that offsets this.
- The rail argument only helps flyers who have a rail option. About 45% of your audience (US, India, rest of world) is long-haul, and no train replaces those flights.
- The skill's evidence shows relocation helps when the current city is off-centre. One conference modelled a 45% cut from a central venue. With an intercontinental audience and a well-placed city, the best alternative moved about a tenth. Frankfurt is not off-centre here, so you land at the bottom of that range.

I can't "prove" the move wins, because the numbers don't support it. What I can say is that the move isn't the biggest carbon lever, and the levers below are bigger.

**Method and limits:**
- I computed great-circle distances by hand for representative origin cities per billing country. A script run was blocked, so these are approximate (about ±5% per city) and not tool-verified.
- Billing country is only a proxy for where people travel from.
- I did not apply emission factors, because I can't cite one from memory. Absolute tonnes are placeholders until you pull a cited factor set.
- Amsterdam's other lines (Dutch versus German grid factor, hotel-night factor) are unquantified and likely small next to flights.

## 1. Closed and open

| Item | Status | Effect |
| --- | --- | --- |
| Format: in-person | **Closed** | Remote attendance tier deleted. Remote *speaking* moves up. |
| Venue | **Open (unsigned)** | Host-city rung is live, but it's a weak lever here. |
| Registration form | Assumed not yet open for edition 2 | If it is live, fall back to billing country and label it "estimated". |
| Catering, swag | Assumed open | Plant-based default and waste asks are still available. |
| Cadence | Open, community decision | Next-edition commitment, not an edition-2 action. |

## 2. Screening estimate

**Origin buckets** are last year's billing countries, with 900 attendees:

| Billing group | Share | People | One-way km to FRA (avg) | to AMS (avg) | Δ AMS − FRA |
| --- | --- | --- | --- | --- | --- |
| Germany | 30% | 270 | ~300 | ~485 | +185 |
| Rest of EU | 25% | 225 | ~1,030 | ~1,080 | +55 |
| US | 20% | 180 | ~7,540 | ~7,190 | −350 |
| India | 15% | 135 | ~6,760 | ~7,060 | +300 |
| Rest of world | 10% | 90 | ~6,760 | ~6,810 | +50 |
| **Weighted mean** | 100% | 900 | **~3,545** | **~3,595** | **+50 (+1.4%)** |

Quality label: **estimated** (billing-country proxy, hand-computed distances). Plausible range for the Amsterdam − Frankfurt gap: **−3% to +3%**. Direction depends on the true US versus India split. Amsterdam gains about 0.7 km on the mean for each point of attendance that shifts from India to US, so it would need a much more US-heavy audience to win.

**Concentration line (estimated):** long-haul flyers are about 45% of attendees and about 90% of passenger-km. Their share of travel *emissions* needs the factor set, but it will clearly exceed 60%. That puts you in the **long-haul profile**.

**Absolute totals** (factor set: UK DESNZ conversion factors, current edition, flights with radiative forcing of 1.7, to be fetched and recorded by you):

| Line | Activity data | Low (t CO2e) | High (t CO2e) | Label |
| --- | --- | --- | --- | --- |
| Long-haul flights | ~405 people × return trip | [fill] | [fill] | estimated |
| Short/medium-haul flights | share of 495 EU/German attendees × return trip | [fill] | [fill] | estimated |
| Rail | German and EU attendees by train | [fill] | [fill] | estimated |
| Accommodation | non-local × nights | [fill] | [fill] | estimated |
| Speakers, volunteers, sponsor staff | [counts needed] | [fill] | [fill] | estimated |
| Venue energy, food, materials, waste | not yet measured | [fill] | [fill] | estimated |

Set the range from low and high flight-mode shares: 70–90% of the EU group flies, 20–50% of the near-German group flies, all long-haul flies.

## 3. Boundary (Net Zero Carbon Events, 9 categories)

| Category | In/out | Owner |
| --- | --- | --- |
| Travel | In (dominant line) | Organizer for trips it books; each participant's employer also counts employer-paid trips |
| Accommodation | In | Organizer inventory |
| Food and beverage | In | Organizer, with caterer data |
| Energy | In | Organizer, with the venue also reporting it |
| Production and materials | In | Organizer (swag owned by sponsors where sponsor-bought) |
| Waste | In | Organizer, with venue and caterer weights |
| Local transport | In if shuttles run | Organizer |
| Freight | In if material | Sponsors and organizer |
| Digital | In if streamed or recorded | Organizer |

Exclusions to state openly: venue embodied carbon, water, the organizers' year-round office.

## 4. Lever plans (long-haul profile, format closed)

Ranking by efficiency, with the remote attendance tier deleted and the venue rung treated as open: organizer-booked travel policy > remote speaking option > train-times page > plant-based default > venue energy ask > rail deal > host city > cadence > regional hub.

**Plan A, travel levers now (recommended)**
- **This edition:**
  - Write the organizer-booked travel policy: economy, direct flights, rail under a set journey time, regional keynotes. Access exceptions stay with the accessibility sibling.
  - Offer every speaker a remote slot, with the same slot and billing. Never use it in place of a travel grant. Target the US and India speakers first.
  - Publish a train-times page for the German and EU audience.
  - Make lunch plant-based by default, and add a food-waste weigh-and-donate clause.
  - Send the venue energy ask.
- **Venue choice:** decide Frankfurt versus Amsterdam on cost, availability and rail access to the venue. Carbon is a tie.
- **Next edition:** commit to *evaluating* cadence and a regional hub.

**Plan B, Plan A plus a next-edition structural commitment**
- Add a review of a biennial cadence, or a second hub for the US or India clusters.
- Cadence needs a community-wide decision, and a hub is a quarter-plus of work with a partner team.
- Both have the highest value and the highest effort, so I'd gate them on your effort ceiling (below) and on a partner team existing.

**Plan C, move to Amsterdam**
- Not recommended on carbon. It saves roughly 0%, and the move costs a new venue search, new contracts and new sponsor conversations.

**Effort ceiling:** unknown, because I haven't asked. I assumed one owner at a few hours a month with no budget, which fits Plan A. If you have more capacity, Plan B's cadence study is where the real tonnes are.

## 5. Data-capture schedule

| Deadline | What to capture |
| --- | --- |
| Before the registration form opens | Departure city or distance band (never a postcode), planned main mode, nights of accommodation. Required, with "prefer not to say". Add a one-line purpose note. |
| Before the venue contract is signed | Metered kWh for the event days, supply contract type (renewable supply contract versus unbundled certificates), waste weights by stream, walking or transit link to the rail station |
| Before the caterer contract is signed | Meals by menu type, food-waste kg, donation partner and kg donated |
| Before the swag and print order | Item counts, unit mass, material, lanyard collection for reuse |
| Within 2 weeks after the event | One-question survey on actual mode |
| After the report is published | Aggregate, then delete the raw origin data. Keep these fields out of lead-retrieval and badge exports. |

Target 80% or more of participants with origin and mode data. Below that, the travel line stays an estimated band.

## 6. Hand-offs

- **event-venue-sourcing:** criteria are rail access, metered energy data and waste-stream reporting. It picks the venue, and this plan does not.
- **event-format-selection:** receives the footprint delta of the options. Format stays in-person.
- **event-hospitality:** plant-based default, plus a food-waste measurement ask.
- **event-vendor-sourcing:** reusable lanyards, food donation and kg reporting go into the brief.
- **event-sponsor-pricing:** any cut to sponsor-bought lanyards or swag inserts.
- **event-accessibility-inclusion:** access exceptions to the travel policy, and the bendable-straw availability.
- **event-budget:** cost of each lever and any contribution line.
- **event-landing-page:** publishes the page text below.
- **event-debrief:** receives the post-event report.

## 7. Draft public page (pre-event variant)

> **Our footprint**
> We estimate [low]–[high] t CO2e for edition 2, based on last year's registration data ([low]–[high] t per attendee). Method: Net Zero Carbon Events categories, [UK DESNZ edition] factors, flights with radiative forcing. Travel is estimated from billing countries this year. From this edition on, we measure venue energy, meals and waste, and we ask your travel mode at registration.
>
> **Where it comes from**
> Travel is the large majority. About 45% of attendees travel from outside Europe, and those trips make up most of the travel emissions.
>
> **What we change this edition**
> - Written travel policy for trips we book: economy, direct flights, rail where practical.
> - Any speaker may present remotely, in the same slot with the same billing. Travel grants are unchanged.
> - Plant-based lunch by default, other meals on request.
> - Food surplus weighed and donated. We will publish the kilograms.
>
> **What we will change next edition**
> - We will study a biennial cadence and a second regional edition for our largest non-European audiences, and report what we find.
>
> **How you can help**
> - Train options from major cities: [routes and times].
> - Tell us how you travelled at registration. It is how we measure.
>
> **What we do not claim**
> We do not call this event carbon neutral.

Notes on the draft:
- It says nothing about the host-city decision, and you shouldn't claim Amsterdam or Frankfurt is lower-carbon.
- It contains no numeric reduction target and no offset-based wording.
- If you later fund a climate project, state the amount and the project on a separate line, and don't net it against the total.
- The EU rule against offset-based neutrality claims has applied since 27 September 2026. This is not legal advice, so have someone qualified review the page before it goes live.

## 8. Post-event report skeleton

| Category | In/out | Activity data | Factor (set, edition) | Low | High | Quality | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Travel | | | | | | | |
| Accommodation | | | | | | | |
| Food and beverage | | | | | | | |
| Energy | | | | | | | |
| Materials | | | | | | | |
| Waste | | | | | | | |
| Local transport | | | | | | | |
| Freight | | | | | | | |
| Digital | | | | | | | |

After the table, in order:
1. Totals and per-attendee ranges.
2. Concentration line.
3. Screening estimate versus result, with the main reason for the gap.
4. Actions taken and their labelled effect.
5. Any factor-set or boundary change, with last edition restated.
6. Data coverage.
7. Waste weights and kg donated.
8. Next-edition commitments.
9. Contribution, if any, on its own line.

## 9. What I need from you to tighten this

1. Who owns the plan, how many hours a month they have, and whether there is any budget.
2. Counts of speakers, volunteers and sponsor staff, with their origins.
3. Whether the registration form is live.
4. Last year's real departure cities or countries. The billing split alone leaves a ±3% gap, so with it I can't promise the move is worse, only that it isn't better.
5. The date the venue contract has to be signed.

**What to tell your co-organizer:** pick Amsterdam if the venue is better, cheaper or more available, but not for carbon. On your audience mix it is a tie, and the travel policy plus remote speaking move far more.