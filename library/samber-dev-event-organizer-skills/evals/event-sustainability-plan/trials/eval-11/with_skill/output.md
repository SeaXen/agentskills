# Marrowgate Connect: event inventory boundary

I did not set up the boundary exactly as ESG instructed. Excluding those three lines is fine for the corporate GHG report, but not for the event inventory or any public figure.

The skill (`event-sustainability-plan`) requires counting all participant travel: attendees, speakers, volunteers and sponsor staff. Leaving out the dominant line is "the most common way an event footprint misleads". So I split one ledger into two views:

- **View A, event inventory.** The full 9-category boundary. It feeds the public page and the post-event report.
- **View B, corporate GHG report.** Scope 1/2/3, filtered to what Marrowgate pays for or controls. It is derived from View A, with no separate data collection.

## Where ESG's instructions land

| ESG instruction | View B (corporate report) | View A (event inventory) |
|---|---|---|
| Exclude speaker flights, employers pay | ✅ Agree for employer-paid trips. They sit in the speakers' employers' Scope 3. | ❌ Counted, flagged "employer-paid", employer named as co-reporter. Never claim a reduction twice. |
| Exclude speaker trips Marrowgate pays | ⚠️ Not covered by "employers pay". Keynotes, invited speakers and travel grants Marrowgate books are **in**. | In. Marrowgate owns these lines outright. Record cabin class and direct vs connecting. |
| Exclude sponsor staff travel | ✅ Agree. They sit in the sponsors' inventories. | ❌ Counted by default, since they travel because of the event. Sponsors are co-reporters. |
| Exclude venue electricity (venue's Scope 2) | ✅ Agree if Marrowgate does not control the venue. It is not Marrowgate's Scope 2. | ❌ Counted, with kWh metered via the venue contract. The venue also reports it. |
| Include only what we pay for | ✅ This becomes the filter for View B. | ❌ Not a boundary rule for View A. Applied to View A it would drop most of the footprint. |
| Structure as Scope 1/2/3 | ✅ View B uses it. | The skill's method uses the 9 Net Zero Carbon Events categories. Scopes are a mapping on top. |

⚠️ **The biggest gap in the instructions is attendee travel.** Marrowgate Connect is a 2,000-person customer conference. Customers' flights and hotels are probably paid by the customers or their employers. "Only what we pay for" would then exclude the dominant line from View B. That is correct for a corporate inventory and fine for ESG. It is also why View A has to stay whole. Published conference studies put travel at roughly 80-97% of an event's footprint.

## Boundary table

Owner means whose inventory the line also belongs to.

| NZCE category | View A | Scope in View B | In View B? | Owner / co-reporter |
|---|---|---|---|---|
| Travel: Marrowgate staff | In | Scope 3, business travel | Yes | Marrowgate |
| Travel: invited speakers and grants Marrowgate pays | In | Scope 3, business travel | Yes | Marrowgate |
| Travel: employer-paid speakers | In, flagged | none | No | Speaker's employer |
| Travel: sponsor staff | In, flagged | none | No | Sponsors |
| Travel: attendees and customers | In | none | Only if Marrowgate pays | Attendee or their employer |
| Accommodation | In | Scope 3 for room blocks Marrowgate pays | Paid portion only | Split by payer |
| Food and beverage | In | Scope 3, purchased services | Yes (Marrowgate pays the caterer) | Marrowgate |
| Energy (venue) | In | Not Marrowgate's Scope 2 | No | Venue operator |
| Production and materials | In | Scope 3, purchased goods | Yes | Marrowgate |
| Waste | In | Scope 3 (venue and caterer waste) | Confirm with ESG | Venue and caterer |
| Local transportation (shuttles) | In if material | Scope 3 | Yes if Marrowgate hires them | Marrowgate |
| Freight and logistics | In if material | Scope 3 | Yes if Marrowgate ships | Marrowgate |
| Digital (streaming) | In if streamed | Scope 3 | Yes if Marrowgate pays | Marrowgate |
| Scope 1 (fuel on Marrowgate-controlled equipment, such as generators) | In if any | Scope 1 | Yes | Marrowgate |
| Scope 2 (purchased electricity) | n/a | Scope 2 | Likely none for a rented venue | Venue |

- I mapped to scopes only where the skill's reference supports it: attendee travel and accommodation sit in Scope 3, and venue electricity is Scope 2 only when the organizer controls the venue.
- The finer scope categories (purchased services, waste, upstream leased assets) are my reading. ESG should confirm them against the corporate methodology.
- Common exclusions to state openly in both views: venue embodied carbon, water, and Marrowgate's year-round offices.

## Rules for the two views

1. **View B is a filtered subset of View A.** Each row carries a payer flag (Marrowgate, employer, sponsor, attendee, venue). View B is every row where the payer is Marrowgate. Nothing is collected twice.
2. **Excluded rows are not deleted.** They stay in View A with an owner, so nobody quietly drops the dominant line.
3. **Public figures use View A only.** The public page may not use the View B number as "the event's footprint". If ESG's number is smaller, say so: "Marrowgate's reported share is X of an event total of Y."
4. **Label every line** measured, surveyed or estimated, and report ranges, not points.
5. **Pull emission factors from one named public set** (UK DESNZ, ICAO or ADEME), with edition year and unit. I have not typed any factors, because the skill forbids uncited ones. State the radiative-forcing choice for flights once and keep it across editions.
6. **Do not report any reduction twice.** If an employer's Scope 3 and the event inventory both contain a speaker flight, only one of them may claim the saving.

## What to tell ESG

- The exclusions are right for the corporate report, and View B applies them.
- They cannot define the event inventory. If the boundary is "only what we pay for", Marrowgate cannot publish an event footprint or a sustainability page without misleading readers by omission.
- No offset-based "carbon neutral" claims. In the EU this has been a blacklisted practice since 27 September 2026, and a ticket sold to individuals is in scope. Keep offsets or contributions as a separate line.

## Questions I need answered

I could not size the estimate or rank levers without these. One at a time, in this order:

1. Does Marrowgate pay for any attendee travel or hotel (customer travel programme, VIP block, partner trips)? If not, View B contains almost no attendee travel.
2. Which speaker and keynote trips does Marrowgate book or pay for, and are there travel grants?
3. What are last year's attendee origins by region, and roughly how many fly long-haul? Is Chicago central to them?
4. What is open: is the venue signed, is the registration form live, and is the catering contract signed? A signed item closes its lever for this edition.
5. Which marketing jurisdictions apply (EU, UK, US states) and who is the audience (individuals or only companies)? This sets the claim rules.
6. By what date must this land: before the venue contract, before registration opens, or after the event?
7. Does ESG want a one-off figure or a baseline for future editions? Who owns this, and how many hours per month do they have?

## Next steps

1. Marrowgate confirms the payer-flag approach with ESG, including the rows marked "confirm".
2. Add origin, mode and nights fields to registration before it opens. Use a distance band or departure city, never a postcode. They cannot be recovered after the event.
3. Put kWh, meals served and waste kg into the venue and caterer contracts before signature. This also gives View A its energy line, even though View B excludes it.
4. Once you answer the questions, I build the screening estimate with ranges and the concentration line, then the lever plans and the public page draft.