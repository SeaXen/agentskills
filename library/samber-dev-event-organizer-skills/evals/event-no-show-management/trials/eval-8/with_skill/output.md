**Next:** paste the four drafts here. Then I'll run `event-attendee-email-sequences` on them.

I did not rewrite the emails, for two reasons:
- Your drafts weren't in your message, so I have nothing to rewrite.
- `event-no-show-management` forbids drafting reminder copy. That belongs to the sibling skill, and writing it here would leave two conflicting sequences.

## Verdict: the 268 is not an email failure

Your numbers:
- 268 attended out of 480 RSVPs is a **55.8% show rate** and a **44.2% no-show rate**.
- Sourced free-event no-show band: 40-60% (Event Tech Live).
- Sourced show-up trendline: about 50% for free hackathons (MLH guide, 323 events).
- Larger check-in-verified sample: median ~28% no-show for free events.

You landed inside the free band and slightly above the 50% trendline. That is normal for a free event, so the figures alone don't show an operations failure.

I can't say how much one confirmation plus a T-1 reminder cost you. No source I have measures an individual email's effect. Four better-timed sends will probably help, but I won't promise a number.

The skill also says to read a low show rate as a demand question first. `event-market-fit` separates demand, price, audience and reminders. Run it before anyone gets blamed.

## What went wrong operationally

I only know what you told me. These are the gaps the numbers show, plus facts I can't verify.

1. **32 seats were empty (268 of 300).** You accepted 1.6x the room (480 ÷ 300), below the sourced 2x. The room ran at 89%.
2. **I can't see a written ceiling.** The skill requires a registration ceiling as a number in the form config, with a named person who closes it. Did one exist?
3. **I don't know of a waitlist.** At 480 you never hit a ceiling, so you may not have needed one. A rule is still needed for next time.
4. **I don't know the walk-in count.** Is it inside the 268? The skill requires counting registered, attended, walk-ins and waitlist arrivals separately.
5. **I don't know what number catering got.** If it was 480, that is a named failure mode: the registration count is not the number that eats.

## Plan for edition 3

Assumptions: the hard capacity is 300 with no overflow approved. Free posture is fixed upstream. This edition is your only measured data.

| Line | Value | Source |
|---|---|---|
| Capacity | 300 | your venue; confirm fire code and contract |
| Show-up rate | 55.8% | your edition 2 (sample of one) |
| Sourced ceiling | 600 (300 ÷ 0.5) | MLH, "do not go over double" |
| Break-even registrations | 538 (300 ÷ 0.558) | own ratio |

**Do not use 600.** At your own 55.8% rate, 600 registrations expect 335 people in a 300-seat room. The occupancy limit is a gate, not a menu rung. It beats the sourced 2x.

**Do not use 538 either.** It expects exactly 300 people, with no margin. Your better reminders are meant to raise the show rate, which pushes it over.

**Proposed ceiling: 500 registrations.**
- At 55.8% that expects about 279 people.
- At 50% it expects 250.
- At 60% it expects exactly 300.
- If reminders lift you past 60%, you are over the limit. Get written overflow approval from the venue before registration opens, or lower the ceiling.

Decisions for you:
- **Ceiling owner:** name the person who closes the form at 500.
- **Waitlist:** use FIFO, drained in one batch on a fixed date. Publish the rule when the list opens. Add a claim deadline for promoted people.
- **Walk-in lane:** use a separate late form, opened only after pre-registered check-in closes. Everyone completes the full form. Hand the expected volume to `event-attendee-experience`.
- **Catering:** send expected show-ups of about 280, with the buffer named separately (500 − 280 = 220). Never send 500.
- **Deposit:** I recommend none. No established practice supports it for developer events. The costs are refund handling, tax and accounting, and a barrier for scholarship seats. A nominal fee is `event-ticket-pricing`'s lever.

## Questions I need from you

1. Did you have a ceiling, a waitlist or a walk-in lane? If so, how many walk-ins came?
2. What headcount did catering get, and when did it lock?
3. Does the venue's fire-code limit equal 300, and is any overflow space available?

## Handoff

For `event-attendee-email-sequences`, the inputs are:
- Ceiling: 500, closing date TBD.
- Audience: registered people, then promoted waitlisters.
- Your four dates: T-14, T-7, T-2 and morning-of.
- The ratio in use, so no "last call" email goes out after the form closes.