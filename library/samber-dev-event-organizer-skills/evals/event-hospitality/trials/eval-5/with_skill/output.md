# FerroCamp hospitality brief: breaks and the Datawisp offer

**Short answer:** there is no single litres-per-attendee ratio. Size each break by time of day. Your current plan, a full-day supply at 8am with volunteers then released, is a rung the skill deletes. Datawisp is a yes, with conditions.

## 1. Your current plan has to change

The plan is a station set up once in the morning and never touched. The skill deletes that rung outright. A refilled station reads as provision, and an empty urn by mid-morning reads as broken.

**Replace it with owned replenishment at each break:**
- Name one person per break who restocks against the published break times.
- Stock for the next break only, not the whole day. The convention refreshes roughly every 3-4 hours.
- This costs a rota slot. Ask `event-volunteers` for it, because they own the shift mechanics.
- Give `event-schedule-design` the service window as a requirement: the station is stocked and hot before each 25-minute slot starts. Do not move or lengthen any slot.

## 2. Quantities

**What the figures are.** The skill sources a consumption convention that several independent catering vendors repeat. Use it to check a quote, not to replace one.

**Planning figures:**
- **Morning break:** about 85% of people drink coffee, at about 1.5 cups each.
- **Afternoon break:** about 50% drink coffee, at about 1 cup each.
- **Evening:** no figure exists. Treat demand as lower than the afternoon.
- **Yield:** 1 gallon is about 15 cups (about 3.8 L).
- **Buffer:** add 10-15%.
- **Starting mix:** about 70% regular, 20% decaf, 10% tea or hot water. A technical audience may differ, so adjust.

**Worked example at 180.** The input should be your expected-show-up figure from `event-no-show-management`, not the registration count. I used 180 as a placeholder.

| Break | Cups | Gallons | With 10-15% buffer |
|---|---|---|---|
| Morning | 180 × 0.85 × 1.5 ≈ 230 | ≈ 15.3 | ≈ 17-17.6 gal, about 64-67 L |
| Afternoon | 180 × 0.5 × 1 = 90 | 6 | ≈ 6.6-6.9 gal, about 25-26 L |

I have not sized your third break. I don't know where it falls, and the convention gives no figure for an unspecified slot. Tell me which slot it is. Apply the morning or afternoon row if it matches one of them. If it falls near the evening, treat demand as below the afternoon figure.

**Check your quote against these numbers.** A station sized at one cup per attendee runs dry in the morning, whatever the rota behind it.

**Per-day totals.** Don't multiply one break's volume by three. The convention puts a full day at roughly double a single break's volume, not a flat repeat.

## 3. Datawisp: take it, with four conditions

Datawisp branding and paying for pastries is the "sponsor bought the break as a named branded surface" case. The skill names that case as a reason to promote the break rung.

**What changes:**
- The afternoon break moves up from owned replenishment to the catered break bar with dietary-labelled stations.
- Their money covers the effort and cost that rung adds. The skill defaults to the cheaper rungs only because nobody was paying.

**Conditions:**
1. **Allergen declaration.** Any break carrying food needs a readable declaration before items are taken. The pastries trigger this duty.
2. **Dietary coverage.** Pastries must carry the dietary categories FerroCamp has committed to. `event-accessibility-inclusion` decides which categories those are, so I haven't invented the list. If the pastry supplier can't cover one, you need a fallback item.
3. **Handover.** Someone must capture allergen detail when the delivery is received and carry it through to the station. Most missing declarations start at that handover, not at the table sign.
4. **Coffee stays owned.** The branded bar doesn't remove the need to restock coffee and tea. The afternoon break still needs its named owner.

**Not mine to decide:**
- Datawisp's price and rights, such as logo placement and exclusivity, sit with whoever owns your sponsorship terms.
- Venue rules on outside food go to `event-venue-sourcing`. Ask whether the venue lets a sponsor bring in food.
- Order lead times and delivery buffers go to `event-vendor-sourcing`.

## 4. Questions I need answered

1. **Break times:** what time are the three breaks, and is any of them next to lunch?
2. **Expected show-up:** what is the figure from no-show management?
3. **Dietary list:** which categories has FerroCamp committed to?
4. **Venue:** does it mandate its own caterer, and can a sponsor bring in pastries?
5. **Volunteer hours:** can you spare three restock slots per day?
6. **Other days:** does Datawisp want to brand only this afternoon break, or every day's?

Once you answer these, I'll turn this into the section-by-section brief for your approval, before anything is ordered.