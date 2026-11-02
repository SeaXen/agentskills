# Oakmere Data Days: Frankfurt vs Amsterdam carbon analysis

## Bottom line

**The move to Amsterdam does not save a meaningful amount of carbon. My estimate is a net change of about +3 tCO2e, roughly +0.3% of travel emissions.** That is well inside the error of the inputs, so the sign could go either way. I can't prove the co-organizer's claim with these numbers, and I wouldn't use it as a reason to move.

## Why the rail hub doesn't matter much

Long-haul flights make up about 90% of attendee travel emissions. That is the US, India and rest-of-world groups, 45% of attendees. Rail only competes for the Germany and nearby-EU attendees, who are about 8% of emissions. Frankfurt is also a major rail hub, with a long-distance station at the airport. Amsterdam's rail advantage is therefore small and applies to a small slice.

## Estimate

This is a first-order model. Assumptions:
- 900 attendees, split by your billing shares.
- Round trips, using great-circle distances to representative origin cities.
- Emission factors: 0.15 kg CO2e/pkm for flights, including a radiative-forcing uplift, and 0.06 kg/pkm for the German rail and air mix.
- Accuracy is roughly ±30% on absolute figures. The differences between cities are more reliable than the totals.

| Origin | Attendees | Round trip to FRA | Round trip to AMS | Total at FRA (t) | Change if AMS (t) |
|---|---|---|---|---|---|
| Germany | 270 | ~600 km | ~960 km | ~10 | **+6** (Frankfurt is central; Amsterdam is at the edge) |
| Rest of EU | 225 | ~2,200 km | ~2,300 km | ~74 | **+3** (the sign depends on the country mix) |
| US | 180 | ~15,000 km | ~14,400 km | ~405 | **−16** (Amsterdam is about 300 km closer to the US East Coast and Chicago) |
| India | 135 | ~12,800 km | ~13,300 km | ~259 | **+10** (Frankfurt is about 250 km closer) |
| Rest of world | 90 | ~18,000 km | ~18,000 km | ~243 | **~0** (not determinable) |
| **Total** | **900** | | | **~990 t (~1.1 t/attendee)** | **≈ +3 t (±1%)** |

Amsterdam gains on US travel. It loses about the same amount on German and Indian travel. The rest of the EU and the rest of the world could swing the result either way.

## What would change the answer

- **US share above roughly 35%:** Amsterdam would start to come out ahead.
- **A rest-of-EU mix dominated by the Benelux, UK or Nordics:** this tips toward Amsterdam, which is the only plausible route to a real win.
- **A rest-of-EU mix dominated by Poland, Czechia, Italy or Spain:** this tips toward Frankfurt.
- **Rest of world mostly from the Middle East, Africa or Asia-Pacific:** Frankfurt tends to be closer for the first two, and the two cities are about equal for Asia-Pacific.
- **Attendance response to the move:** German attendance could drop at a new venue, since the German share may partly reflect where the event is held. That would reduce the rail-based travel that the move is meant to help.

## Where the carbon is

If carbon is the goal, these levers matter more than the city:

1. **Speakers and sponsors flying in.** About 45% of attendees account for ~90% of emissions. Per-person emissions are highest for intercontinental speakers. An in-person event can still cut those flights, for example with regional speaker sourcing or a rule of one long-haul trip per speaker.
2. **Travel guidance for attendees.** Publish rail-first routes for Germany and nearby EU. Recommend direct economy flights, since connections and premium cabins add 20–200% per trip.
3. **Venue and catering.** On-site operations are likely a few percent of the total, roughly 20–35 t. A vegetarian-default menu and a venue with renewable power help, but they are small next to long-haul travel.
4. **Venue choice on other grounds.** The city is a lever only if attendee origins shift. A venue that is cheaper or better is a fair reason to move, but carbon isn't one here.

## Caveats

- Billing country is not travel origin. US-billed attendees may be based in Europe, and corporate billing often sits in a different country from the traveller.
- I used great-circle distance plus a single flat factor. Routing, aircraft type, cabin class and load factor are not modelled.
- Rest of EU and rest of world are the two biggest unknowns. They hold about 35% of attendees.

## Next step

Send the attendee origin city (or postcode) list from last year's registration, and whether each person was a speaker, sponsor or attendee. I'll rerun the comparison per person, with cabin class assumptions and ranges, so you and your co-organizer can see whether any real scenario favours Amsterdam. Until then, the data we have doesn't support the claim that the move is a carbon win.