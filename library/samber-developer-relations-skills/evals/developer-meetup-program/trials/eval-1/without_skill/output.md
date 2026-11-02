## What actually went wrong

Your new plan (cap RSVPs at 60, order food for 60) repeats the same mistake at a smaller scale. The bug isn't "too many RSVPs" — it's **ordering food to match RSVP count instead of expected attendance**. Last month proves the room was never at risk: 118 RSVPs produced only 41 bodies, well under your 60 seats. The room capacity was never the constraint; the food math was.

## Your real numbers

- Show-up rate: 41 / 118 = **35%** (no-show 65%)
- That's worse than your friend's "half won't come" rule (50% no-show) — trust your own data over a differently-sized group in a different city.
- Pizza cost: €640 / 118 ordered ≈ **€5.43/head**

## Why capping RSVPs at 60 doesn't fix anything

Apply your own 35% rate to a 60-cap: expected attendance ≈ **21 people**. Apply your friend's more optimistic 50%: ≈ **30 people**. Either way you get a half-empty room *and* still waste 50–65% of whatever food you order for "60" — same ratio as before, just smaller euros. You've shrunk the waste, not solved it, and you've also throttled your visible community size for no reason (the room was never overflowing).

## What to do instead: decouple the two numbers

**RSVP cap** controls room-overflow risk. **Food order** should track expected attendance. Don't set them equal.

1. **Keep RSVP volume roughly where it was — around 110–120, not 60.** At 35% show-rate that's 39–42 expected attendees, comfortably under 60 with margin if turnout is better than usual. Your last event's 118 RSVPs was actually a reasonable number for a 60-seat room *if* you'd assumed a 50% show rate (118 × 0.5 = 59 ≈ capacity) — the RSVP volume wasn't the problem.
2. **If you want a hard ceiling for peace of mind**, use a soft cap with waitlist (Meetup.com supports this natively): open ~120 spots, first 100 confirmed, rest waitlisted, promote waitlisted people if you see cancellations. This gives you an overflow safety valve without artificially shrinking the event.
3. **Order food for expected attendance, with a small upside buffer** — running out is worse for community goodwill than minor waste:
   - Expected attendance at 120 RSVPs × 35% ≈ 42
   - Add ~15–20% buffer for upside variance → **order for ~48–50 people**
   - Cost: 48 × €5.43 ≈ **€260** — down 59% from €640, while still covering a plausible good-turnout month.

## One caveat

35% is one data point (last month only). Before locking this in, pull RSVP-vs-attendance from your other 5 editions. If the average is consistently near 35%, trust it over your friend's outside benchmark. If last month was an outlier (bad weather, holiday-adjacent, competing event) and your true historical average is closer to 45–50%, shift the food order up toward ~55 people accordingly.

## Cheap lever worth adding

Send a "still coming?" reminder 24–48h before the event — it reliably lifts show-up rate and gives you a same-week signal. If your pizza vendor allows next-day ordering, place the order the morning of based on reminder responses instead of committing to a headcount weeks out — turns a guess into an adjustable, near-real-time number.