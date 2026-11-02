# Thornwick Rust Days, edition 1: travel footprint screening estimate

**I can't give you one defensible number for the deck.** Any single figure here would hide a spread of roughly ±17% around the midpoint, and every input is a guess. I can give you a range, and a sentence that fits on a slide.

## Headline for the sponsor deck

> **Screening estimate: roughly 280–400 t CO2e from participants' flights (about 340 t at the midpoint), using a provisional emission factor. Flights only, before accommodation, food, energy and materials. This will be refined once registration data is in.**

Do not put the midpoint on a slide alone. This range is provisional until you replace the factor (see below).

## Three problems with the inputs

1. **The 0.25 kg/passenger-km figure is uncited.** The skill's evidence rules forbid using a factor you can't name by set, edition and unit, because one uncited figure makes everything on the page unverifiable. Pull the current UK DESNZ conversion factors (or the ICAO calculator) and record the edition year. I couldn't fetch them here, so I did not type any from memory.
2. **I don't know whether 0.25 includes radiative forcing.** DESNZ multiplies flight CO2 by 1.7 for non-CO2 effects. That one choice moves the total by tens of percent. Pick one convention, state it on the page, and keep it across editions.
3. **Skip the extra 10% for detours.** DESNZ already adds its own uplift to great-circle distance, and the skill says not to add your own. I applied your 10% below because you asked, but it may double-count. If you use DESNZ, drop it. That lowers the total by about 9%, to roughly 260–360 t.

## Method and assumptions

Participants: 500 attendees + 30 speakers + 25 volunteers + 20 sponsor staff = **575**. Speakers, volunteers and sponsor staff all count, because leaving them out is the most common way footprints mislead.

Distances are my approximate great-circle figures from Zurich, labelled **estimated**.

| Origin bucket | People | Assumed flyers | Return distance | Flight pkm (low–high) |
|---|---|---|---|---|
| Switzerland (40%) | 230 | 0%, trains and local transit | – | 0 |
| DE/AT/FR/IT (30%) | 173 | 20–50% | about 1,200 km | 41k–104k |
| Rest of Europe (20%) | 115 | 70–90% | about 3,000 km | 242k–311k |
| US and Asia (10%) | 58 | 100% | 13,000–18,000 km | 748k–1,035k |
| **Total before +10%** | 575 | | | **1.03M–1.45M** |
| **Total with your +10%** | | | | **1.13M–1.59M** |

Multiplying the +10% pkm by 0.25 kg gives **283 t (low) to 398 t (high)**.

Sensitivity: every 0.01 kg/pkm of factor change moves the total by about 11–16 t. If your real factor is 0.15 or 0.30, the total is roughly 170–240 t or 340–480 t.

## Concentration line

**Long-haul flyers are 10% of participants and about 70–72% of flight emissions.** That is above the skill's 60% threshold, so the long-haul lever profile applies. Zurich is also central to the European buckets, so relocating the host city is not the lever.

For the first edition the strongest levers are:
1. An organizer-booked travel policy for speakers: economy, direct flights, rail for short routes.
2. A remote speaking option, offered and not imposed, which keeps travel grants unchanged.
3. A train-times page for the 70% of participants who are in Switzerland or its neighbours.

A remote attendance tier and cadence are bigger levers on paper. Treat them as next-edition decisions through `event-format-selection`.

## What is not in the number

Accommodation, food, venue energy, materials, waste and local transport are missing. They are second-order, but you still need them for a full inventory. Accommodation is the next line to add. I need the average hotel nights per non-local participant (about 345 people) and a cited hotel-night factor.

## Wording you may use

The skill's claim rules apply:
- The EU blacklisted offset-based "neutral" claims on 27 September 2026.
- Zurich is in Switzerland, where unfair-competition law applies. Have someone qualified review the page before it goes public.
- Don't call the event "carbon neutral" or "green".
- Don't promise a future cut without a plan behind it.
- Do show the method, the range and the actions.

Suggested sponsor-deck line:
> "Edition 1 screening estimate: [low]–[high] t CO2e from participant flights ([factor set, edition], with/without radiative forcing). Travel is the dominant source; about 10% of participants flying intercontinentally produce roughly 70% of it. We will measure origin and travel mode at registration and publish the measured result."

## To turn this into a final number

1. Tell me the factor set and edition you will use, and whether it includes radiative forcing. I'll recompute in one step.
2. Add origin and travel mode as required fields on the registration form before it opens. Use a distance band or departure city, never a postcode.
3. Confirm how many speakers or guests the event itself books, and their cabin class. Business class carries several times the economy factor.
4. Tell me the average hotel nights per non-local participant, so I can add the accommodation line.

I can also draft the full plan, boundary table and public page once you answer those.