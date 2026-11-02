# Tidewater Lisbon: release the extra 60 tickets? Catering head count?

**Do not release the 60. Give the caterer 360.** I based this on the `event-no-show-management` skill and its two reference files.

## The decision

| Question | Answer |
|---|---|
| Release 60 more tickets? | ❌ No. Stay at 400 registrations. |
| Head count for the caterer | **360**, with a 40-head buffer named separately |
| Waitlist | Yes, FIFO, drained before the 14-day catering lock |
| Deposit | None recommended |

## Why no overbooking

**1. The "free crowd" reading is the wrong band.**
- Paid events see 90-97% of tickets convert to attendance, a 3-10% no-show rate (Event Tech Live).
- Free events see 40-60% no-shows.
- At 290 EUR you are in the paid band. Her "everyone knows a chunk never shows up" is true of free events.
- The overbooking ceilings (2x) were sourced from free hackathons. The skill deletes both ceilings for any paid event, so there is no ratio to tune.

**2. "Employers pay, so it behaves like free" is a hypothesis, and I can't use it.**
- Every show-up figure is measured against price posture, not against who paid. Nothing in the data splits employer-paid from self-paid.
- The one within-event measurement (860+ events, 195-event follow-up) puts payment's effect on an individual's odds of showing at only 2-4 points. That says little either way about employer-funded seats.
- The Basecamp deposit case names the same limit: a reimbursed attendee may not feel the money.
- So her argument could be right, but it is unmeasured. We can't sell 60 seats on it.

**3. The arithmetic shows the risk.**

| Registrations | No-show rate | Expected arrivals | Against the 400 limit |
|---|---|---|---|
| 460 | 3% | 446 | ❌ over |
| 460 | 10% | 414 | ❌ over |
| 460 | 13% | 400 | break-even |
| 460 | 17% (paid-event median in the larger sample) | 382 | fits |

- 460 fits only if at least 13% of ticket holders skip. The paid band says 3-10%.
- Even the more pessimistic 17% paid median only just clears it, with no margin.
- The occupancy limit (fire code, venue contract, insurance) is a gate. It is never traded against catering savings.
- The two errors are not symmetric. An empty chair costs one cover. Turning away someone who paid 290 EUR costs a refund and a public account of it.

## Catering: 360

1. Hard capacity is 400 (assumed, see below). We are sold out, so registrations are 400.
2. The expected show-up rate comes from the Event Tech Live paid band, 90-97%.
3. 400 × 0.90 = **360**, the low end of the band. 400 × 0.97 = 388 is the high end.
4. The number to send is the expected show-up, never the registration count.
5. State the buffer in the handoff: 400 registered − 360 guaranteed = 40 heads of cover that we are not paying for.

**Why the low end.**
- Her employer-funded hypothesis, if true, pushes no-shows up, not down.
- The larger check-in-verified sample puts paid events at about 17% no-show, which is about 332 heads.
- 360 sits between that and the band's upper edge. I did not average the sources. I took the paid band as primary and used the 17% median as a check on the downside.

**Contract checks to make before the lock.**
- Ask whether the caterer allows an upward top-up after the lock, and at what overage rate.
- Ask whether it allows a downward tolerance, for example ±5%.
- A top-up option makes 360 low-risk, because under-ordering then costs a surcharge instead of hungry people.
- Speakers, crew and sponsors who eat are not in the 400. Add them as a separate line.

## Waitlist

Since we are sold out, open a waitlist now.
- **Order:** signup order (FIFO), drained in one batch.
- **Drain date:** before the 14-day lock, for example 16 days out. Only promotions made before the lock move the catering number. After the lock, a promotion fills a chair but does not change the guarantee.
- **Claim window:** a stated deadline, for example 48 hours, then the seat moves on.
- **Rule:** publish the ordering rule, the drain date and the claim window on the page when the waitlist opens.
- **Owner:** one named person decides.
- **Emails:** hand the trigger, audience and deadline to `event-attendee-email-sequences` as a brief. Do not draft the emails here.

## Day-of gap

- With no overbooking, expect about 12-40 empty seats (3-10% of 400, or up to about 17%).
- Plan no walk-in volume.
- Any unregistered arrival goes through a separate late form, opened only after pre-registered check-in closes, and completes the full registration form. The check-in desk skill owns the staffing.
- Do not open the door with no form.

## Deposit

I don't recommend a deposit mechanic, because no established practice stands behind it for developer events. The only data points are single events (Eventtia, Basecamp). A deposit would carry refund handling, tax and accounting obligations, and a barrier for scholarship seats. The nominal-fee lever belongs to the ticket-pricing skill, and a 290 EUR ticket has already done that job.

## How to settle the disagreement with her

Test her hypothesis instead of betting on it.
- **This edition:** add a required "who pays" field to registration (employer or self). Count registered versus attended, split by that field, and keep the numbers.
- **Next edition:** if employer-paid seats really show up at a free-band rate, you will have your own measurement. Even then, the skill still takes no overbooking on a paid event. The data would change the catering estimate, not the ceiling.

## Assumptions to confirm

I could not run the interview, so the plan rests on these.
- 400 is the binding capacity (fire code and venue contract), with no overflow space and no written approval for one.
- 290 EUR is the real price for most of the 400. A large block of comped seats would behave as free seats and change the maths. Count those separately.
- You have no prior-edition registered-versus-attended count for this event in this format. If you do, that number beats every figure above for your event, but hold it under the sourced band.
- The reminder email sequence is already designed and dated. If it isn't, it should run before these numbers are final.

## Capacity plan summary

| Figure | Value | Source |
|---|---|---|
| Hard capacity | 400 | assumed from your brief, confirm with the venue |
| Show-up rate | 90-97% | sourced (Event Tech Live, paid band) |
| Registration ceiling | 400 | self-set, no overbooking |
| Catering guarantee | 360 | self-set (400 × 0.90) |
| Buffer | 40 | arithmetic, named separately |
| Waitlist | FIFO, drained by about 16 days out | self-set |
| Walk-in volume | none planned | self-set |
| Deposit | none | stated gap |

Record 400 registered, the attendee count, walk-ins, waitlist promotions with how many arrived, and covers eaten against the 360. Those become your own ratio next year.