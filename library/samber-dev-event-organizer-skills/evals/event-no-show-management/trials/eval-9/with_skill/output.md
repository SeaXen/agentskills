# Helvetia Go Conf: promote the 40 nearest waitlisters during event week?

**No, not as proposed.** Three separate problems stack up. Each one is fixable.

## 1. Event week is after the catering lock

- Catering locks 21 days out. A mailing in the week of the event lands about two weeks after the lock.
- A promotion that late fills chairs, but it can't change the number catering works from. That number is already fixed.
- The waitlist only helps the budget if you drain it before the lock. If the lock has already passed (it has, if the event is under 3 weeks away), the waitlist is a seat-filling tool only. Don't present it as a cost lever.

## 2. The numbers don't allow a flat 40

- **Ceiling.** Free event, so plan on the free band: about 50% show-up. This is the MLH trendline across 323 events. It's the one figure written as an instruction: aim for double, and don't go over double.
- **Arithmetic.** 320 seats ÷ 0.5 = 640 registrations. You closed at exactly 640, which is the sourced ceiling.
- **The 40 breaks it.** 640 + 40 = 680, over double. Expected attendance becomes 680 × 0.5 = 340, above your 320 hard capacity. The occupancy limit is a gate, so the ratio moves and the room doesn't.
- **What to do.** Promote one-for-one against cancellations, so registered stays at or below 640. The 180 are a holding list, not a second batch.
- **Check first.** Does 320 seats equal the venue's occupancy limit, or is that limit higher or lower? Who approved any overflow in writing?

## 3. Sorting by postcode distance is the wrong rule for this event

- **Weak evidence.** The proximity idea comes from the MLH guide, which gives a reason ("closer people are more likely to show up") and no measured gain. Treat the benefit as unquantified.
- **It contradicts your pitch.** The landing page sells a draw from four countries. A rule that visibly ranks Zurich locals first and sinks people who travel from Germany or Austria is the contradiction someone will find. Decide whether you can defend it publicly before adopting it.
- **Changing the rule mid-window.**
  - It's an allocation decision made on registrants' location data.
  - The rule has to be published when the waitlist opens.
  - Your waitlist is already open. If the page promised first-come-first-served, or said nothing, switching now reads as invented after the fact.
- **Postcodes break across borders.** Swiss, German and Austrian postcodes aren't comparable. "Distance" needs geocoding, and the list needs hand-ordering. That's effort you may not have in the final two weeks.
- **It only fits some of the conditions.** Proximity ordering makes sense when you can spare the hours to order the list by hand and the waitlist is far enough past the ceiling that order changes who gets in. The second holds here, since 180 people compete for a few seats. The first is unconfirmed.

## What I'd do

1. **Use first-come-first-served, drained in one batch on a named date.** It's the default, it's easy to defend to anyone skipped, and it costs an afternoon. If the event is over 3 weeks away, drain it before the lock.
2. **Size the batch to real cancellations.** Keep registered at or below 640. The reminder sequence will generate cancellations. Ask `event-attendee-email-sequences` to include a "can't make it, release your seat" link.
3. **Publish the rule now.** State the order, the drain date, a claim deadline (24–48 hours is realistic, and claim windows matter more the closer you are to the event) and who decides.
4. **Treat a late promotion as short-notice.** Someone coming from Germany or Austria can't re-plan travel in a week. If you promote that close, a rule like "promoted seats are claimed within 24 hours or move on" is honest about it.
5. **Give catering 320 as expected show-up, not 640.** Name the 320 buffer separately so nobody orders 640 lunches. If the lock has passed, the number already sent is the one that stands.
6. **Plan a walk-in lane at the door.** It should open after the pre-registered check-in window closes, with a separate form that everyone completes in full. Send `event-attendee-experience` the expected volume. The lane only makes sense if unregistered people can physically reach your desk.
7. **Record registered, attended, walk-ins, and how many promoted people arrived.** If you really want to test the proximity idea, the only evidence you'll get is your own promotion yield. Run it as a small experiment with the rule published, not as a surprise.

## What I need from you

1. Event date, to know whether the 21-day lock has already passed.
2. Whether the page or confirmation email said anything about waitlist order.
3. The venue's actual occupancy limit, and whether 320 seats is it.
4. Whether you have a prior edition's registered-versus-attended count.
5. Whether anyone has hours in the last two weeks to order and mail the list.

## Caveats

- 50% is a hackathon-network figure for free events, and none of the sourced figures cover a four-country single-track conference. Treat it as an upper bound.
- A larger check-in-verified sample found about a 28% median no-show rate for free events. If your show-up rate runs better than 50%, a full 640 could overfill the room. That's another reason to promote against cancellations and not top up.
- Deposits aren't recommended. There's no established attendance mechanic for them in developer events. A nominal fee is the lever with practice behind it, and it belongs to `event-ticket-pricing`.