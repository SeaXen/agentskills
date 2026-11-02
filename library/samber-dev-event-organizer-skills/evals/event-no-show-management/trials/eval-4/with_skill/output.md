# Kestrel Conf: no-show plan (250 seats, free, two days)

I read the skill and both references. Your 09:45 release with an SMS to seat 114 is the one mechanic the skill marks as untested. So the setup below is built differently: overbook up front, drain the waitlist before doors, and keep your live release as a labelled experiment. I haven't asked you the interview questions. Anything marked **confirm** is an assumption.

## Why not wire it as described

1. **The timed-claim waitlist feature is documented only for pre-event use.** It handles cancellations and expired holds, and one platform calls it "not an in-event promotion strategy". Nothing I found shows it taking badge-scan data as a trigger. **Confirm** this with your ticketing vendor before you promise an afternoon of work.
2. **A 30-minute SMS window gives low odds.** Someone texted at 09:45 has to read it, travel and arrive by 10:15. A walk-in already standing in your building is a stronger attendance signal than a promise.
3. **Late registrants lose their seat.** Anyone released at 09:45 who arrives at 09:55 is turned away. That costs more trust than an empty chair costs money.
4. **"Seat 114" only works if seats are assigned.** If it's open seating, there is no seat to release. **Confirm.**
5. **SMS needs a phone number and consent.** In France that means GDPR consent collected on the waitlist form. If you didn't collect it, you can't text.

## Numbers I need from you

| # | Question | Why |
|---|---|---|
| 1 | Registrations last year, per day | "60 no-shows" is 24% if you had 250 registered. That wouldn't look half empty. Either registrations were higher or day 2 dropped much more. |
| 2 | Is 250 the fire-code or venue limit, or just the seat count? | The occupancy limit is a hard gate. |
| 3 | Catering lock date | It decides whether the waitlist can change the catering number. |
| 4 | Do you have waitlist phone numbers and consent? | Needed for any SMS. |
| 5 | Is the venue open-door or badged? | Decides whether walk-ins exist. |
| 6 | Organizer hours in the last two weeks | Sets how much hand work is possible. |

## The plan

**1. Set the registration ceiling and close the form.**
- Free event, so plan against the free band (40-60% no-show, the Event Tech Live figure). Use the MLH figure for the ceiling: about 50% show up, aim for 2x, never exceed 2x. That is 500 registrations at most.
- Your own count from last year beats borrowed figures, but it is a sample of one. Keep your ceiling under 500.
- Formula: ceiling = 250 ÷ (1 − your no-show rate).
- **Illustration only, assuming 250 registered and 60 no-shows.** The rate is 24%, so 250 ÷ 0.76 ≈ 329. Expected attendance would sit right at the 250 limit with no margin, so you would pick about 300 (expected ≈ 228). Replace this with your real numbers.
- Do this per day. Write the ceiling as a number in the form config, and name the person who closes it.
- If you want standing room or an overflow room, get written venue approval before registrations open against it.

**2. Open the waitlist when you hit the ceiling.**
- Order by signup (FIFO). Proximity ordering takes hand work and discloses an allocation rule built on location data.
- Publish the rule, the drain date and the claim window the moment the waitlist opens.
- Drain it in one batch on a named date before the catering lock.
- This is where the vendor's timed-claim automation fits, because it's the pre-event use it was built for.
- Collect phone numbers with explicit SMS consent on the waitlist form.

**3. Day-1 doors, with scanners as the counter.**
- Scan every badge. This is your registered-vs-attended count and the single cheapest number on the page.
- Pre-registered check-in runs first. The walk-in lane opens only after that window closes, around 09:45.
- The walk-in lane is a separate form, and everyone still completes the full registration form. Give the desk your predicted walk-in volume. The desk owner is `event-attendee-experience`.
- Waitlist-fed walk-ins ("unclaimed seats open at 09:45, be here by 10:15") only make sense if the venue is badged and has no walk-up crowd, and if you can reach the waitlist within a day. **Confirm.** Otherwise the queue at the door fills it for free.
- Do not release a registered person's seat at 09:45. The walk-in lane fills the room from below without anyone tracking who failed to arrive.

**4. Use day 1 scans to protect day 2 (my own construction, not a sourced mechanic).**
- Evening of day 1, message everyone who didn't scan in: "Confirm for tomorrow or release your seat by 20:00."
- Promote the waitlist overnight from released seats, before doors open. This keeps the mechanic pre-doors, which is the version with practice behind it.
- Brief `event-attendee-email-sequences` with the trigger, audience, deadline, what changes for the recipient and the ratio in use. It writes the send.

**5. Run your 09:45 live release as a measured experiment, only if you still want it.**
- Run it on day 2 only, with a small seat batch.
- Decide the stop rule in advance, for example "stop if fewer than half of promoted people arrive".
- Track promotions sent and promotions arrived.
- A promotion with no claim deadline holds a seat indefinitely, so keep the window.
- Treat it as a test, not a replacement for steps 1-4.

**6. Catering.**
- Send `event-budget` the expected show-up number, never the registration count.
- State the gap between the two as the overbooking buffer.
- Illustration: 300 registered and about 228 expected means you order for about 228, with a 72-person buffer named separately.

**7. Deposit.**
- I don't recommend a refundable-deposit mechanic. There is no developer-event practice behind it.
- Two single-event data points exist. Eventtia: a $3 deposit moved no-shows from 38% to 14%. Basecamp: a $100 deposit gave a 90% show rate.
- It would add refund handling, accounting and tax duties, and a barrier for scholarship-type seats.
- If you want a lever in that direction, the nominal fee is the established one. It belongs to `event-ticket-pricing`.

## Done checklist

- Expected attendance sits under the venue limit, with the arithmetic and arrival assumption written down. This is a pass/fail gate.
- Registered-vs-attended is recorded per day. This is also pass/fail.
- Track these self-set signals: actual attendance against capacity, waitlist promotion yield, walk-in volume against prediction, and catering ordered against eaten.
- Feed the realised show-up rate to `event-market-fit`.
- Save the capacity, rate, ceiling and arithmetic, the published waitlist rule and the final counts. That is next year's own ratio.

## What I did not verify

I didn't check your ticketing tool's integrations. I also assumed the 60 no-shows were out of about 250 registrations, and the skill's own figures are population bands, not targets for your event.

Send me the answers to the table above and I'll replace the illustrated numbers with your real ceiling.