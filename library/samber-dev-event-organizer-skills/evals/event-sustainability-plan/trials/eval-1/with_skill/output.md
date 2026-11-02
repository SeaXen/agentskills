# KestrelConf sustainability page, with what to fix before it goes live

I followed the `event-sustainability-plan` skill and its three reference files. The skill's interview is one question at a time, but you asked for the deliverable in one go. So I worked from what you told me and listed the gaps as bracketed placeholders. I invented no numbers and no emission factors.

## 1. Can you call it a carbon-neutral conference?

No. Three reasons:

1. **Offsets can't support the word.** Since 27 September 2026, the EU has blacklisted any claim that a product is "carbon neutral", "climate neutral" or "CO2 compensated" because of offsetting (Directive 2024/825). That holds whatever the credit quality. You sell tickets to individuals in Europe, so the page is in scope. The UK Green Claims Code, the US FTC Green Guides and the Swiss ruling on FIFA 2022 point the same way. Your US buyers add exposure.
2. **The 350 kg estimate is a sponsor's rule of thumb, not a calculation.** It has no method, no cited factors, and no flights in it. Published per-attendee figures for conferences are much higher, though none is KestrelConf's number:
   - 0.57 t per participant (Neugebauer, full life-cycle assessment)
   - 1.5 t (European astronomy meeting, surveyed)
   - about 3.5 t from air travel alone (ICSE 2023, modelled)

   At 1,100 attendees, that range is roughly 630 to 3,850 t. 350 kg sits below all of it, so "400 t covers more than our estimate" may be false. In FIFA 2022, the offsets covered less than a third of the organizer's own estimate.
3. **The page would hide the biggest source.** Published studies put attendee travel at 80–97% of conference footprints. A page about plastic, lanyards and lunch that never mentions flights misleads by omission.

You did real work, and you can say so. Say it without "neutral", without "offset" as a claim, and with a measured number as soon as you have one.

## 2. Before publishing: 3 weeks

1. **Today, add travel questions to the live registration form.** Ask for departure city or distance band (not postcode), main travel mode, and nights of accommodation. Make them required, with "prefer not to say" and one line on why you ask. Fallback: use billing country as an origin proxy and label it "estimated". Without this you can never compute the dominant line. **This edit changes the live form.**
2. **Run a screening estimate this week, about half a day.**
   - Pull one current factor set: UK DESNZ conversion factors for flights, rail, hotel night and grid. Record set, edition year and unit.
   - Choose radiative forcing for flights (DESNZ uses ×1.7). I recommend including it. State the choice on the page.
   - Bucket attendees by origin from last edition's billing countries.
   - Report a low–high range, plus the line "Long-haul flyers are N% of participants and M% of travel emissions."
3. **Get the broker paperwork.** You need project name, registry and standard, vintage, removal versus avoided emissions, the retirement record, and the price. Check the credits against the ICVCM Core Carbon Principles label. Without these, the contribution paragraph below can't be written.
4. **Confirm the facts in section 3's checklist.** Each page line must trace to something true and scoped.
5. **Have someone qualified review the page for EU, UK and US rules.** This is not legal advice.
6. **Publish the pre-event variant.** The figures come from your own estimate, so label them "screening estimate".

## 3. Draft page (pre-event variant)

Brackets are for you to fill. Delete any line you cannot confirm.

---

### Sustainability at KestrelConf

KestrelConf is a 2-day developer conference in Lisbon for about 1,100 people. This page says what we measure, what we change, and what we do not claim.

#### Our footprint

*Use ONE of these two versions.*

**Version A (no estimate done yet):**
We have not yet measured the footprint of KestrelConf. Until we do, we publish no total. By [date], we will publish a screening estimate as a range, with the method.

**Version B (once the screening estimate exists):**
We estimate [low]–[high] t CO2e for the [4th] edition, or [low]–[high] t per attendee. This is a screening estimate, not a measurement. It covers travel, accommodation, food and beverage, venue energy, materials, waste, local transport, freight and digital, using the Net Zero Carbon Events categories. Factors: [DESNZ, edition YYYY], flights including radiative forcing. Travel is estimated from [last edition's billing countries / your registration answers]. [Other lines] are [estimated / measured]. We exclude venue embodied carbon, water, and our team's year-round work.

#### Where it comes from

At conferences that have published an inventory, attendee travel is the large majority of emissions, typically 80–97% (modelled studies, mostly academic meetings). Most of that comes from the minority who fly long distances. We expect the same here, so travel is where we focus. *[Version B: replace with "Travel is [share]%. Flights from outside Europe are [N]% of participants and about [M]% of travel emissions."]*

#### What we changed this edition

- **Single-use plastic:** [exact scope: e.g. no single-use bottles or cups at the venue and on-site catering]. Bendable straws stay available on request, without questions.
- **Lanyards:** reusable lanyards, [collected at the exit for reuse next edition].
- **Lunch:** [half of the lunch dishes are vegetarian]. Other options remain available.
- **Data:** we now ask where you travel from and how, so next time we publish a measured figure.

#### What we will change next edition

*Publish only the commitments you actually make.*

- We will publish a full post-event report within [N] weeks, with ranges and the method.
- Before signing the next venue, we will compare host cities by how many of you can arrive without flying.
- We will offer speakers a remote slot, with the same slot length and billing. Travel grants are unchanged.

#### How you can help

- Tell us how you travel when you register. That is how we measure.
- Coming from [Spain / the Iberian Peninsula]? Rail and coach options: [routes and times, only if real].
- Travelling a long way? Consider combining it with other trips or meetings, and tell us.

#### Our climate contribution

We bought [400] t of certified carbon credits through [broker]. They come from [project, country], under [standard], vintage [year], as [removals / avoided emissions]. They were retired on [date] at [registry, serial range]. We sized the amount from [stated rule, e.g. "a rough early estimate we are now replacing with a measurement"].

**This does not cancel or offset KestrelConf's emissions, and we do not count it against our footprint.**

#### What we do not claim

We do not call KestrelConf carbon neutral, climate neutral, net zero or eco-friendly. We have not been certified by a third party. *[Add only if true: "Our sustainability management follows ISO 20121 (self-declared)." That needs a written policy, an issue review, supplier requirements and a post-event review. Otherwise say nothing about ISO.]*

---

### Fact checklist before publishing

- **Lanyards:** are they yours or sponsor-bought? Is the reuse scheme real? If sponsors fund them, route changes to `event-sponsor-pricing`.
- **Plastic ban:** does it cover sponsor booths and the venue's bar and cafe, or only your catering?
- **Lunch:** is "50% vegetarian" 50% of dishes or of meals eaten? Say which.
- **Credits:** were they bought for this edition or a past one? Are they retired in your name?
- **Offsets:** did the broker supply a registry link?

### Words to keep off the site, socials and sponsor decks

carbon neutral | climate neutral | CO2 compensated | net zero | climate positive | green | eco-friendly | "100% offset" | any home-made badge. Don't publish a numeric reduction target either. Publish action commitments instead.

## 4. Supporting plan

### Closed and open

- **Closed (assumed):** venue and format for this edition, the 400 t purchase, the lanyard and plastic decisions. I'm assuming the venue is signed. If it isn't, host-city comparison is a live lever.
- **Open (confirm):** registration form, catering contract details, whether talks are streamed, host city for the next edition, travel grants.

### Boundary (Net Zero Carbon Events, 9 categories)

| Category | In/out | Owner / note |
| --- | --- | --- |
| Travel | in | Attendees, speakers, volunteers and sponsor staff all count. Trips you pay for are yours outright. |
| Accommodation | in | Surveyed from registration nights. |
| Food and beverage | in | Meals by menu type from the caterer. |
| Energy | in | Venue metered kWh. The venue also reports it. |
| Materials | in | Badges, signage, lanyards. |
| Waste | in | Weights from the venue and caterer. |
| Local transport | in if material | Only if you run shuttles. |
| Freight | in if material | Booth freight is optional. |
| Digital | in if streamed | Usually small. |

### Lever plans

The right profile depends on your concentration line, which you don't have yet. Lisbon is at the western edge of Europe, so most flyers are short-haul with no practical rail option. That points to the domestic-flying profile, with US attendees adding a long-haul share.

- **Plan 1, recommended: quick rungs now, structural next edition.**
  - This edition: a written travel policy for anything you book (economy, direct, regional keynotes), a remote speaking option, a plant-based default with alternatives, a venue energy and waste-weight request, and the data capture.
  - Next edition: host-city comparison by audience centre, and a decision on a remote attendance tier.
- **Plan 2: Plan 1 plus a remote attendance tier now.** It moves more tonnes, but the engagement evidence is poor, the AV cost is high, and it belongs to `event-format-selection`.
- **Plan 3: cadence change, such as biennial or alternating in-person and online years.** Big effect, but a community-wide decision. Park it as a question for the next debrief.

Travel grants and access commitments win over every lever. Never rank speakers or attendees by their flight footprint.

### Data capture

| What | When |
| --- | --- |
| Origin, mode and nights | Add to the registration form now |
| Venue kWh, supply type and waste weights | Before the venue contract or addendum is signed |
| Meals by menu type, food waste and donated kg | In the caterer contract |
| Lanyard counts and reuse | Swag and print brief |
| Actual-mode follow-up survey | After the event |
| Delete raw origin data | After the report is published |

### Hand-offs

- `event-hospitality`: plant-based default and food-waste weighing.
- `event-vendor-sourcing`: reusable lanyards and kg reporting.
- `event-sponsor-pricing`: any sponsor-bought lanyards or swag.
- `event-venue-sourcing`: rail access, metered energy and waste-stream criteria.
- `event-accessibility-inclusion`: straws, dietary needs, grants.
- `event-budget`: lever costs and the credits line.
- `event-landing-page`: publishes this page.
- `event-debrief`: takes the post-event report.

### Post-event report skeleton

1. Nine-category table: in/out, activity data, factor (set and edition), low, high, quality label (measured, surveyed or estimated), owner.
2. Totals and per attendee, as ranges.
3. Concentration line.
4. Screening estimate versus result, with the main reason for the gap.
5. Actions taken and their labelled effect.
6. Any boundary or factor change since last edition. Restate the previous edition on the new basis before comparing.
7. Data coverage (target 80% or more with origin and mode).
8. Waste weights and kg donated.
9. Next-edition commitments.
10. The credits, on their own line, never netted against the total.

## 5. One line for marketing

Instead of "carbon-neutral conference", use: **"We're measuring KestrelConf's footprint and publishing the result."** It's true once the estimate is done, and no regulator can challenge it. The fastest route to publishing it is steps 1 and 2 in section 2 this week.