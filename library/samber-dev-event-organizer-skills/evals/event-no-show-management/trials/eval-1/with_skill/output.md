# MetaForge Dev Nights, March: no-show plan

Skill used: `event-no-show-management`, with both reference files.

## Do this today

1. **Close the registration form now at 341.** Turn on a waitlist so new sign-ups go there.
2. Tell the caterer **171 covers**, which is 2,394 EUR at 14 EUR a head.
3. Do not use 45%.

## Capacity: 180

- The venue contract's 180 is the binding number.
- The fire certificate's 195 is a separate legal limit. It gives you no extra seats.
- Any standing or overflow space needs written approval from the venue before you sell against it. Do not improvise it at the door.

## Why not 45%

- Your colleague's two numbers measure different things. The 40-60% is a no-show band for free events, attributed to Event Tech Live. The 30-50% is a descriptive drop-off range from the MLH hackathon organizer guide.
- Averaging them gives a number that answers no question. It also isn't a figure anyone can defend to the venue.
- The skill uses the one figure that is written as an instruction. The MLH guide says about 50% of people who register for a free event show up (323 events). It says to aim for double your target and **not go over double**.
- Your event is free, so you're in the free band. That is the right band.

## The arithmetic

| Line | Value | Source |
|---|---|---|
| Hard capacity | 180 | venue contract |
| Show-up rate | 50% | MLH trendline, free events |
| Sourced ceiling | 180 ÷ 0.5 = **360 registrations** | sourced 2x rule |
| Registered now | 341 | yours |
| Expected show-ups at 341 | 341 × 0.5 ≈ **171** | self-set arithmetic |
| No-show buffer | about 170 | named separately |

**Why close at 341 instead of 360:**
- At 360, expected attendance is exactly 180, the limit, with zero margin.
- The free-event band tops out at 60% show-up. At 341 registrations that is 205 people.
- A larger check-in-verified sample (860+ events) found a lower free-event median no-show rate of about 28%. At 341 registrations that is about 245 people.
- A high turnout puts you over a contract and insurance limit. A low turnout only costs a few empty chairs. Those two risks are not equal.
- The 19 slots between 341 and 360 add only about 10 expected people.
- Treat 360 as the absolute maximum, never a target.

**Who enforces it:** name one person who closes the form and owns the number. I can't name them for you.

## What the caterer gets

- **171 covers.** This is expected show-ups, not the 341 registrations.
- Sending 341 would cost 4,774 EUR, about 2,380 EUR of food nobody eats, with no refund.
- If you'd rather cover the room fully, 180 covers costs 126 EUR more. That insures against the walk-in lane filling toward 180.

## Waitlist

- Order is first-come, first-served. Drain it in one batch on a fixed date, and publish that rule on the page when the waitlist opens.
- The catering guarantee locks in 12 days. A promotion after that date fills chairs but no longer moves the catering number. Choose a drain date before the lock if you want it to count.
- Give each promoted person a claim deadline, with a date and time.
- Hand the trigger, audience and deadline to `event-attendee-email-sequences` as a brief. Don't write reminder copy here.
- Tell that skill the form closed, so no "last call" email goes out afterwards.

## Day-of

- Run a separate late-registration form. Open it only after the pre-registered check-in window closes.
- Everyone who arrives still completes the full form.
- The lane stops the moment the room reaches **180 people**.
- Expected walk-ins are small, roughly 0 to 9. Hand that volume to `event-attendee-experience` for staffing.

## Deposit

I don't recommend a deposit. Two single-event examples exist (Eventtia, 37signals) but no established practice does. A deposit adds refund handling, tax and accounting work, and a barrier for people who can't easily pay. If you want fewer no-shows next time, a nominal ticket fee has real organizer practice behind it. That decision belongs to `event-ticket-pricing`.

## Two things I couldn't confirm

1. **Do you have last edition's registered-versus-attended count?** Your event is recurring and catering locks early, so your own measured ratio would beat the borrowed 50%. Even then, keep the ceiling at or under 360.
2. **Can an unregistered person walk up to your door?** If the venue is access-controlled, the walk-in lane has no population. In that case, tell the waitlist the night before that unclaimed seats open at a named time.

## After the event

Record these five numbers: registered, attended, walk-ins, waitlist promotions, and how many promoted people arrived. They become April's own ratio instead of a borrowed one.