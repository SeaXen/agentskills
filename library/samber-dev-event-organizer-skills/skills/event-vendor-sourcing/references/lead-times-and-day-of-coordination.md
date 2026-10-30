# Lead times, delivery buffers and day-of coordination

Contents:

- Work back, do not plan forward
- Catering lead time and delivery buffers
- The chafing-dish fire-code trap
- Swag and print lead times
- Quantity: the two padding logics, and the size-distribution benchmark
- AV, security and insurance timing
- The day-of delivery plan
- Distribution once it has arrived
- Returns and reconciliation

## Table of Contents

- [Work back, do not plan forward](#work-back-do-not-plan-forward)
- [Catering lead time and delivery buffers](#catering-lead-time-and-delivery-buffers)
- [The chafing-dish fire-code trap](#the-chafing-dish-fire-code-trap)
- [Swag and print lead times](#swag-and-print-lead-times)
- [Quantity: the two padding logics, and the size-distribution benchmark](#quantity-the-two-padding-logics-and-the-size-distribution-benchmark)
- [AV, security and insurance timing](#av-security-and-insurance-timing)
- [The day-of delivery plan](#the-day-of-delivery-plan)
- [Distribution once it has arrived](#distribution-once-it-has-arrived)
- [Returns and reconciliation](#returns-and-reconciliation)

## Work back, do not plan forward

Order the categories by their own deadlines, not by their spend. The largest line is rarely the earliest one:

- A print run that must clear a backorder binds months out.
- A caterer's headcount locks a fortnight out.
- A security firm may take a week.

An organizer who plans forward from today does the biggest thing first and misses the earliest thing entirely.

Build one commitment schedule per edition, each row a category, each row's date the _last_ date a decision can still be made - then hand it to `samber/dev-event-organizer-skills@event-planning-timeline`, which owns the work-back schedule someone actually executes against.

## Catering lead time and delivery buffers

A US student-hackathon organizer network publishes catering lead times. Those lead times transfer well; their per-person prices do not.

- **Place the order 2-4 weeks before the event.** A venue's own mandated caterer commonly requires finalizing sooner than that - ask, because the mandated case is both the more likely one at a university venue and the earlier deadline.
- **Delivery buffer depends on the service style**, and this is the reason service style is a brief field rather than a presentation choice:
  - **Plated or individual meals: deliver 30-60 minutes before serving.** Enough buffer to absorb a late delivery without the food going cold. The risk being managed is temperature.
  - **Family-style shared platters: deliver 60-90 minutes before serving.** More setup time is needed, and chafing dishes hold the temperature, so the cold-food risk falls and the setup risk rises instead.
- **Give the supplier an exact delivery location, a primary on-site contact, and a backup phone number.** The backup number is the item most often skipped and the one that matters at 07:00 on the day.
- **Agree who serves.** Some suppliers, university catering in particular, require their own staff.
- **Agree the return of reusable items** - chafing dishes, tablecloths, platters - with a pickup time rather than an open-ended arrangement.

## The chafing-dish fire-code trap

Chafing dishes burn fuel, and some venues restrict them for exactly that reason. Confirm with the venue before designing a family-style service around them, because the whole delivery-buffer and staffing plan for family-style service assumes they are permitted.

This is the same class of venue-imposed restriction as an overnight fire-code limit: invisible unless asked, decided by the building rather than by the supplier, and expensive precisely because it is discovered after the service style has been chosen and priced.

## Swag and print lead times

Swag and print lead-time guidance comes from hackathon and community conference organizing guides.

- **The lead-time driver is backorder risk, not shipping.** Interesting items are frequently out of stock, so the deadline is set by the supplier's stock position on the specific items and sizes you want. Ask for stock confirmation in writing before committing, and treat a ship date as meaningless without one.
- **Order stickers and other printed items with plenty of lead time too** - named separately from apparel in the source, which is a hint that print runs are routinely under-planned relative to shirts.
- **In-hand date, not ship date.** Add the venue's own receiving rules on top: from what date it accepts shipments, to what address, with what receiving fee, and whether anything can be stored securely before the event.

## Quantity: the two padding logics, and the size-distribution benchmark

There are two distinct padding rules in the sources, and they solve different problems. Do not blend them.

- **Late-order padding (a stockout hedge).** If apparel is ordered only a few weeks out, pad by **up to 30% per size and style**. The source's own framing: a few extra shirts is better than anyone going home without one. This is about ordering late, not about ordering early.
- **Early-order timing (a backorder hedge).** Order early enough that stock exists at all. This is about the calendar, not the quantity.

**Size distribution** from a hackathon organizer network's own event data, published as percentages of attendees:

| Size        | Share |
| ----------- | ----- |
| Unisex M    | ~43%  |
| Unisex L    | ~29%  |
| Unisex S    | ~13%  |
| Unisex XL   | ~10%  |
| Unisex 2XL  | ~3%   |
| Unisex XS   | ~1%   |
| Women's M   | ~7%   |
| Women's S   | ~6%   |
| Women's L   | ~3%   |
| Women's XS  | ~2%   |
| Women's XL  | ~1%   |
| Women's 2XL | <1%   |

Use this distribution to sanity-check an order's shape when you have no better data - it is far better than guessing proportions. Collect real sizes at registration whenever you can, which is both more accurate and recommended for inclusion.

Note what the distribution does _not_ say: it stops at 2XL because historical orders stopped at 2XL. Real demand exists at 3XL-5XL, and a supplier whose line does not reach there fails the brief regardless of what these percentages suggest.

## AV, security and insurance timing

None of these three has a standard lead time - say so rather than inventing one.

- **AV and production.** What matters more than a lead time is rehearsal. If the event streams, rehearse with the actual setup ahead of time and assign a named person to run the stream live. That rehearsal is a date on the schedule and a line in the supplier's quote, so it belongs in the commitment schedule.
- **The evening or social event is a second booking**, not an extension of the first. It commonly sits at a different location with its own venue, its own catering and its own timings. Source it as its own set of suppliers rather than as an add-on, and check the walking distance or transport from the main venue, which is what protects attendance.
- **Security.** Ask the venue and the firm; a building that requires specific approved firms will have its own notice period.
- **Insurance.** Some cover must be bound well ahead of the event, and some cover is unavailable once a known circumstance exists. The binding date belongs on the commitment schedule; `samber/dev-event-organizer-skills@event-risk-management` owns which cover is being bound and when the go/no-go dates fall around it.

## The day-of delivery plan

One row per supplier, agreed before the day and shared with whoever is on duty:

| Field                               | Why it exists                                                          |
| ----------------------------------- | ---------------------------------------------------------------------- |
| Supplier and what they are bringing | So the person at the door knows whether to let them in                 |
| Arrival window                      | Agreed with the supplier, not assumed                                  |
| Exact delivery location             | Building, entrance, dock, room - not the event's marketing address     |
| Primary contact and number          | One named person, reachable                                            |
| Backup number                       | Sourced practice, and the field most often left empty                  |
| Who receives and checks             | Someone physically present, who counts what arrived                    |
| Setup responsibility                | Theirs, yours, or split - decided in the contract, restated here       |
| Ready-by time                       | The serving or start time, from which their arrival window was derived |
| Teardown and pickup                 | Time and named responsible person                                      |

Hand these windows to `samber/dev-event-organizer-skills@event-run-of-show`, which owns what happens live when a supplier is late. This skill's job ends at the agreed window; theirs begins when it is missed.

## Distribution once it has arrived

Sourced catering-distribution practice, included because a supplier's on-time delivery is wasted by a bad serving plan:

- **Never route everyone through one table**, even at a small event. It creates long waits and overwhelms the serving team. Use multiple stations so more people are served at once.
- **Stagger the announcement.** Release one to three tables or rooms to the line at a time, then make a final call. A single blanket announcement sends everyone at once and produces a line of twenty minutes or more.
- **Store restricted-diet meals at a separate table and check names off a printed list** as they are handed out, so they are not taken by someone else. The sources repeat this safeguard verbatim across two documents, which is evidence it is standing practice rather than incidental advice.
- **Post the menu with allergen detail** where people queue, so they can plan before they reach the front.
- **Where meals come as dining-hall credits rather than catered food**, distribute the credits at check-in; a physical credit card can go straight into the welcome bag.

## Returns and reconciliation

- Collect and keep every receipt. Unopened surplus - prizes especially - can be returned, raffled, or carried into the next edition instead of written off. A team that has decided in advance who owns this recovers money a team that has not simply loses.
- Return the supplier's reusable equipment at the agreed time, to the agreed person. A missing chafing dish is a line on a final invoice.
- Record per supplier what they were briefed on, what they quoted all-in, what arrived, and whether it arrived inside the window. That record is next edition's referral list, and it is the only supplier benchmark that is genuinely true for this event.
