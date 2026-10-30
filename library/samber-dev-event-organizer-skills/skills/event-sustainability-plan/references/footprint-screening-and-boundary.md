# Footprint screening and boundary

Contents:

1. Factor sets and the radiative-forcing choice
2. Screening worksheet
3. Data-quality labels and ranges
4. Boundary: the 9 categories
5. Double counting: one owner per line
6. Registration and contract fields
7. Worked shape

## 1. Factor sets and the radiative-forcing choice

Never type a factor from memory. Ask the user to pull the current edition of one named set and record set, edition year and unit for every line.

| Set                                                  | Use it for                         | Caveat                                                                                                                        |
| ---------------------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| UK DESNZ greenhouse gas conversion factors (annual)  | flights, rail, coach, car, hotels  | Flight factors published with and without radiative forcing (multiplier 1.7 on CO2), and by cabin class. Air factors can move 15-40% between editions; restate the baseline when the edition changes. |
| ICAO Carbon Emissions Calculator                     | per-route flight CO2               | CO2 only, no non-CO2 effects, all-economy seating. Used by UNFCCC for its own conferences.                                    |
| ADEME Base Empreinte                                 | events held in France              | National reference set; use it where French reporting expects it.                                                            |
| Exponential Roadmap harmonised flight guide          | harmonising flight method          | Recommends radiative forcing of 1.7 or more plus upstream fuel emissions.                                                     |

- **Radiative forcing (RF).** DESNZ multiplies flight CO2 by 1.7 for non-CO2 effects; other methods use higher multipliers. Flights dominate events, so this one choice moves the total by tens of percent. Recommend including it, state it on the page, and never switch between editions without restating the baseline.
- **Factor spread.** Different sets give up to about 5x different results for the same flight. One set per inventory.
- **Distance.** Use the set's own convention (DESNZ adds an uplift to great-circle distance). Do not add your own.

## 2. Screening worksheet

The goal is the size and the concentration of the footprint, not precision. Build it from last edition's registration data, or from the organizers' best guess by region, labelled as such.

| Line                       | Activity data                                                       | Factor                                   | Low  | High |
| -------------------------- | ------------------------------------------------------------------- | ---------------------------------------- | ---- | ---- |
| Long-haul flights          | people × return trips × distance band, from origin buckets          | set's long-haul factor, with RF          |      |      |
| Short-haul flights         | same                                                                | set's short-haul factor, with RF         |      |      |
| Rail and coach             | people × return distance                                            | set's rail / coach factor                |      |      |
| Car                        | people ÷ occupancy × return distance                                | set's car factor                         |      |      |
| Accommodation              | non-local attendees × nights                                        | set's hotel-night factor for the country |      |      |
| Local transport            | usually small; estimate only if shuttles are run                    | set's bus / taxi factor                  |      |      |
| Food and beverage          | meals served × menu type                                            | a cited per-meal factor                  |      |      |
| Venue energy               | metered kWh for event days, or venue estimate                       | grid factor for the country and year     |      |      |
| Materials, swag, freight   | item counts × mass, freight distance                                | cited material factors                   |      |      |
| Waste                      | kg by stream                                                        | set's waste-treatment factors            |      |      |

Origin buckets: local (transit or walk), same country, neighbouring countries with rail options, rest of continent, intercontinental. Split each bucket by likely mode, then use low and high mode shares to make the range.

**Concentration line.** Under the table, write: "Long-haul flyers are N% of participants and M% of travel emissions." Every lever decision reads this line first. In the AGU study, about 36% of attendees produced 75% of emissions; at a European astronomy meeting, intercontinental flights were 10% of trips and half of the emissions.

**Speakers and staff.** Count speakers, volunteers, organizers and sponsor staff as their own rows. Speakers often fly further and are the population a remote option reaches most easily. Rows the event books itself (keynotes, grants) also record cabin class and direct versus connecting: business and first cabins carry several times the economy factor, and connections add distance and take-offs.

## 3. Data-quality labels and ranges

| Label     | Meaning                                                  | Typical lines                                 |
| --------- | -------------------------------------------------------- | --------------------------------------------- |
| measured  | metered or weighed by someone accountable                | venue kWh, waste kg, meals served             |
| surveyed  | self-reported by participants                            | departure city, travel mode, nights           |
| estimated | modelled from assumptions                                | screening travel, materials, last-year proxy  |

- Report every line as a range. Two published estimates of one conference (AGU 2019) differ by about 60%.
- Report intensity per attendee as well as the total, so a bigger edition is not read as a worse one. Per attendee-day only as a secondary figure: adding a day lowers it without avoiding a tonne.
- Below about 80% origin-data coverage, keep travel as "estimated" and widen the range (self-set threshold).
- Never fill a missing line with a silent fallback factor; mark it "not estimated" and say why.

## 4. Boundary: the 9 categories

The Net Zero Carbon Events measurement methodology treats the event as a product and uses 9 categories rather than corporate Scope 1/2/3. Use them for the event inventory; map to scopes only if a corporate report needs it. Basic, intermediate and advanced tiers can be mixed by category.

| Category                               | Default         | Note                                                                                          |
| -------------------------------------- | --------------- | --------------------------------------------------------------------------------------------- |
| Travel to and from the destination     | in              | The dominant line. Never out.                                                                 |
| Accommodation                          | in              |                                                                                               |
| Food and beverage                      | in              | Food attendees buy themselves at venue cafés is excluded in the method's first edition.       |
| Energy                                 | in              | Venue energy for event days, including build-up if metered.                                   |
| Production and materials               | in              | Stage build, signage, badges, swag.                                                           |
| Waste                                  | in              |                                                                                               |
| Local transportation                   | in if material  | Shuttles, transfers.                                                                          |
| Freight and logistics                  | in if material  | Shipped AV, booth freight.                                                                    |
| Digital content and communication      | in if streamed  | Usually small; a fully virtual event's footprint is mostly here plus participants' devices.   |

Common exclusions to state openly: venue embodied carbon, water, organizers' year-round office.

**Corporate scope mapping, if asked.** For the organizer's own inventory, attendee travel and accommodation sit in Scope 3. Venue electricity is Scope 2 only when the organizer controls the venue, which is rare.

## 5. Double counting: one owner per line

| Line                          | Also counted by           | Rule                                                                       |
| ----------------------------- | ------------------------- | -------------------------------------------------------------------------- |
| Venue energy                  | the venue operator        | Report it in the event inventory; note the venue also reports it.          |
| Speaker flights paid by employer | the employer's Scope 3 | Count in the event inventory; never sell or claim the reduction twice.     |
| Travel grants and invited-speaker trips the event pays | nobody else | The organizer owns these lines outright. Count them; never drop them to improve the total. |
| Sponsor staff travel          | the sponsor               | Count by default: they travel because of the event. Name the sponsor as co-reporter. |
| Sponsor booth freight         | the sponsor               | Optional; count if material, otherwise list as excluded.                   |
| Renewable certificates bought by venue | the certificate market | Report location-based figure first; market-based only alongside it.     |

## 6. Registration and contract fields

Add these before registration opens; they cannot be recovered after the event.

- **Registration:** departure city or distance band (never a postcode: with a name it identifies people at small events), planned main travel mode (plane, train, coach, car, local transit or walk), nights of accommodation. Make the questions required with a "prefer not to say" option; optional fields rarely reach the coverage target. Add a one-line note stating the measurement purpose.
- **Fallback:** if the form is already live, use billing or registration country as a coarse origin proxy and label the line "estimated".
- **After the event:** a one-question survey confirming the actual mode, since planned and actual differ.
- **Privacy:** aggregate, then delete raw values once the report is published. Keep these fields out of sponsor lead-retrieval, badge-scan and attendee-list exports.
- **Venue contract:** metered electricity and heating kWh for the event days, supply contract type (renewable supply contract versus unbundled certificates), waste weights by stream, refrigerant top-ups if the venue reports them.
- **Caterer contract:** meals served by menu type, food waste weight, surplus donation partner and kg donated.
- **Swag and print:** item counts, unit mass, material; lanyard collection for reuse.

## 7. Worked shape

Input: 900 attendees, 2 days, European city; last edition 40% flew.

Output shape:

```
Origin buckets (from last edition's registration countries):
  local 25% | same country 20% | rail-reachable neighbours 15% |
  rest of continent 30% | intercontinental 10%
Mode assumption: intercontinental all fly; rest of continent 70-90% fly;
  rail-reachable neighbours 20-50% fly.
Factors: [DESNZ edition YYYY], flights with RF. User fetches values.
Concentration: intercontinental = 10% of attendees, [computed]% of travel.
Next step: compute the concentration line and the audience centre; they pick
  the profile. Here long-haul sits near the 40-60% band, so show both the
  long-haul and the rail plan. Compare host cities first only in the rail
  profile, or if the current city is off-centre.
```
