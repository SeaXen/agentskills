# Lever evidence

Contents:

1. How big travel is
2. Organizer-booked travel
3. Host city and rail access
4. Remote options, hubs, regional editions, cadence
5. Catering and food waste
6. Swag, materials, single-use plastics
7. Venue energy
8. What tech events actually publish

Most published numbers come from scientific conferences: no industry developer conference publishes a full category-level inventory. Each figure below carries a label: measured, surveyed, or modelled. Quote the label with the number.

## 1. How big travel is

| Study                                         | Event                                                      | Finding                                                                      | Label                              |
| --------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------- |
| Klöwer et al., Nature, 2020                   | AGU Fall Meeting 2019, 28,000                              | about 80,000 t CO2, about 3 t per scientist                                  | modelled                           |
| Barret, arXiv, 2020                           | same meeting, re-estimated                                 | about 50,500 t CO2e; up to 5x spread across factor choices                   | modelled                           |
| Burtscher et al., Nature Astronomy, 2020      | European astronomy meeting 2019, 1,240                     | 1,855 t CO2e from travel, 1.5 t per person; online successor 588 kg in total | surveyed sample (22%), extrapolated |
| Jäckle, ECPR General Conference, Hamburg      | 1,930 attendees                                            | 905-1,825 t from travel                                                      | modelled                           |
| Neugebauer et al., Journal of Cleaner Production, 2020 | European conference series                        | 0.57 t per participant; travel about 83% even with venue and food included   | full life-cycle assessment         |
| European wildlife-disease conferences (preprint, 2022) | several                                           | flying 87-97% of total, travel modes assumed by country                      | modelled                           |
| ICSE 2023 report (arXiv)                      | software-engineering research conference, Melbourne, 1,424 | about 5,000 t CO2e from air travel, about 3.5 t per attendee                 | modelled                           |

- Concentration: at AGU, about 36% of attendees produced 75% of emissions; virtual participation for the top-emitting 36% would cut 76% (Klöwer). At the astronomy meeting, intercontinental flights were 10% of respondents' trips and half their emissions.
- Trade-press figures such as "travel is 70-80%" or "90-95%" carry no method. Do not cite them.
- A local meetup inverts the picture: with everyone on transit, food and venue become the main lines.

## 2. Organizer-booked travel

- Keynotes, invited speakers and grant recipients are the only trips the organizer books or pays for, so the only travel it fully controls.
- DESNZ and the ICAO calculator publish class-specific flight factors; business and first cabins carry several times the economy factor because they take more floor space per seat; premium economy sits much closer to economy.
- Connecting itineraries add distance and an extra take-off and landing cycle against a direct flight.
- Policy levers: economy by default, direct where available, rail under a set journey time, regional keynote speakers where the programme allows, remote keynotes as an option.
- Access exceptions: a disabled speaker or grant recipient may need a premium cabin, a direct flight, or a flight where the rail journey is too long for them. Those exceptions are owned by `event-accessibility-inclusion` and override the policy.

## 3. Host city and rail access

- For AGU 2019 the footprint-minimising city was Detroit; San Francisco came out about 11% higher (Barret). With an intercontinental audience, relocation alone moves about a tenth.
- Klöwer modelled a central location plus biennial cadence plus virtual presentations together at a cut above 90%: the combination, not the city, does the work.
- ECPR (Jäckle): a more central venue saved between about 1% and 45% depending on the starting city; central venue, land travel and online participation for distant attendees together modelled 78-97%. Train versus coach among land travellers was "only of marginal relevance": replacing flights is what counts.
- A tropical-medicine society's decentralised option modelled up to 58% lower CO2e.
- Rail access shifts behaviour: among European survey respondents who flew to the 2019 astronomy meeting and had a rail connection, 85% had a train option under 24 hours (median 8 hours). In a later exit survey, 57% said they would have flown to rail-connected Leiden, against 67% observed flying to Lyon the year before. That compares a stated intention with an observed share at two specific meetings: never use it to judge either city for another event, whose own origin data decides.
- Rail precedents: Chaos Communication Congress with Deutsche Bahn (event ticket valid two days either side, "if you can, please travel by train"); an energy forum in Berlin with discounted rail rates; Goldschmidt 2019 publishing train times from major cities.

## 4. Remote options, hubs, regional editions, cadence

- Tao et al., Nature Communications, 2021 (modelled life-cycle): fully virtual cuts about 94% of carbon; keeping more than half in person, carefully selected hubs for a hybrid conference can cut about two-thirds.
- WCRP/SPARC General Assembly 2022, three hubs on three continents (Kremser et al., BAMS, 2024; surveyed): travel emissions down by a factor of 2.3-4.1 against a single location.
- Cadence: an event held every second year halves its annual travel emissions if attendance per edition holds; pent-up demand often grows biennial editions, so model both. Alternating in-person and online years is the softer version. Cadence also moves sponsor revenue and the budget across editions.
- Counterweight: hybrid formats cost markedly more in AV and logistics, and remote engagement is often low. ACM CHI lost money on full hybrid in 2022 and dropped remote attendance; ACM SIGMETRICS stopped hosting hybrid conferences for lack of attendee participation (ACM SIG Governing Board minutes, 12 April 2024). A remote tier justified only by carbon can fail on engagement, which is why the format call sits with `event-format-selection`.
- Remote speaking for long-haul speakers is the narrowest version: one pre-recorded or live-remote slot, no full remote audience to serve. Same slot length, same billing on the schedule.

## 5. Catering and food waste

- ECPR Hamburg (modelled): a fully vegetarian menu would save 16.1 t and a vegan menu 23.1 t over four days, against 905-1,825 t of travel. About 1-3% of travel: small, but cheap and visible.
- The Royal Geographical Society made all conference lunches vegetarian or vegan from 2019.
- KubeCon + CloudNativeCon North America 2023 reported more than 4,800 lb of food donated and more than 11,000 lb composted. Weights are the metric; CO2 "avoided" figures from food redistribution rarely disclose a method.
- Before promising donated kilograms, confirm the venue's exclusive caterer allows donation and that local food-safety and donor-liability rules permit it.
- Choice architecture: a plant-based default with alternatives on request keeps the dietary commitments owned by `event-accessibility-inclusion` intact.

## 6. Swag, materials, single-use plastics

- The footprint of the International Coral Reef Symposium 2022 in Bremen used about 6 g CO2e per paper conference pass (a vendor factor) and about 8 kg per t-shirt. Swag carbon is small next to travel, and it sits in textiles, not badges.
- No measured carbon reduction from a swag policy exists in the published record. The case is waste and labour: short-lived, cheap plastic. Swag-site retention statistics are vendor marketing.
- Reuse precedents: sponsor-collected lanyards for reuse (KubeCon NA 2023, run by the lanyard sponsor), lanyard rental libraries, undated signage.
- Refill stations: Web Summit 2022 reported 17,837 single-use bottles avoided.
- Single-use bans need an access exception: keep bendable straws available without asking, since some disabled attendees cannot drink without them.
- Swag bags and lanyards are often sponsor inventory (PyCon US sells swag-bag inserts and lanyards). Cutting them is a sponsor-pricing decision, not only a sustainability one.

## 7. Venue energy

Ask the venue for:

- metered electricity and heating for the event days, in kWh;
- the supply contract type: a renewable supply contract tied to generation, or unbundled certificates bought separately;
- waste streams by weight;
- refrigerant top-ups, if reported;
- the walking or transit link to the main rail station.

"Electricity offset by renewable energy credits" (KubeCon NA 2023 wording) describes market-based accounting, not a physical change. Report the location-based figure first.

## 8. What tech events actually publish

| Event                           | Published                                                                                                                     | Carbon total |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------ |
| KubeCon + CloudNativeCon (CNCF) | transparency reports with food donated and composted weights, sponsor-collected lanyards, recycled lanyards, certificate-backed venue power | no |
| Chaos Communication Congress    | rail partnership and train-first travel page                                                                                  | no           |
| Web Summit                      | 2017 "carbon-neutral" claim via tree planting, as reported by the Irish Times; later bottle and food-redistribution figures                | no           |
| FOSDEM                          | hosts energy and sustainability devrooms                                                                                      | no           |
| PyCon US                        | sells swag-bag inserts and lanyards in its sponsor prospectus                                                                 | no           |
| ICSE 2022 and 2023              | post-conference sustainability reports, air travel only                                                                       | yes          |

A developer conference that publishes a measured inventory with its method stands out simply by doing it.
