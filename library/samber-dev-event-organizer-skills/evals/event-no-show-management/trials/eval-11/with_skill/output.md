# Redcliff Analytics: registration form and overbooking rule

**Neither proposal is adopted as written.** Reject the form-plus-confirmation change as a no-show fix. Reject "200% one week out" as a standing rule, and set a separate registration ceiling.

I couldn't ask the skill's interview questions, so the numbers below rest on stated assumptions. Treat them as defaults until you answer the open questions at the end.

## 1. Five-question form plus mandatory email confirmation: ❌ not as a no-show fix

The ops director's claim is that easy registration causes bad attendance. The evidence behind the skill says the link is mostly a confound.

- **Free events run the simplest forms.** Easier registration only looks correlated with worse attendance because of that.
- **Controlling for free versus paid removes the effect.** In a check-in-verified analysis of 860+ events, paid events show flat no-show rates of about 16-19%. This holds whether registration completes at 65% or 98%.
- **Most of the free-versus-paid gap sits at the event level.** The free-event median is about 28% no-shows against about 17% for paid. Within a single event, paying moves an individual's odds of showing by only about 2-4 points. Adding friction to a free event shouldn't be expected to close that gap.
- **Friction still has a cost.** Registrations will drop, and you can't tell whether the people lost would have shown up.

Adding five questions and a confirmation click is therefore a bet with a known cost and no evidence of benefit. The data she cites doesn't support it.

Concerns this proposal could legitimately address:

- **Fake or mistyped emails.** A confirmation click does fix this. It is a list-hygiene decision, not a no-show lever.
- **Knowing your audience.** A form with a few fields serves this. It is a marketing decision, not a no-show lever.

For no-shows itself, use these instead:

- **Reminder sequence.** `event-attendee-email-sequences` owns the design and copy. The ratios below assume it has already done its work.
- **Nominal fee.** `event-ticket-pricing` owns this. It is the only lever with real organizer practice behind it.
- **Refundable deposit.** I'm not recommending one. No established practice supports it for developer events. It would also add refund handling, tax and accounting obligations, and a barrier for people who need a free seat.

## 2. "100% two weeks out, 200% one week out" as the overbooking rule: ❌ wrong source, wrong job

The curve and the ceiling are two different instructions.

- **The 100%/200% curve is a marketing pace chart.** It comes from a free-hackathon guide's marketing timeline. It tells you whether registrations are on pace. It doesn't tell you how many to accept, and it belongs to `event-marketing-plan`.
- **The actual overbooking instruction is separate.** The same guide says about 50% of registrants show up for a free event, so aim for double the registrations, and do not go over double. This is the sourced 2x ceiling, with a cap.
- **A pace target has no stop.** Adopted as a standing rule, "200% one week out" has no cap. Leaving registration open with no ceiling is the one posture the guide forbids, because it guarantees registered people get turned away.
- **The multiplier is only borrowed.** It comes from free hackathons, which draw the loosest-commitment audience. For a different format, treat it as an upper bound, not a target.

### What I recommend instead

This is the arithmetic for a 120-seat room. It assumes a hard capacity of 120 and a free seat.

| Step | Value | Source |
|---|---|---|
| Hard capacity | 120 | Assumed; confirm with the venue |
| Aimed attendance | 120 | The room is the goal |
| Show-up rate, hackathon trendline | about 50% | Sourced, 323 events, free hackathons |
| Show-up rate, check-in-verified sample | about 72% (28% no-shows) | Sourced, free events across formats |
| Sourced 2x ceiling | 240 registrations | 120 ÷ 0.5, the upper bound |

- **240 is a ceiling, not a target.** If your event behaves like the larger sample, 240 registrations puts about 173 people in a 120-seat room.
- **The occupancy limit is a gate.** It is never traded against catering economics, so the ratio moves and the limit doesn't. Expected attendance must sit under the venue's stated limit under your arrival assumption.
- **If you have prior editions' registered-versus-attended counts**, use your own ratio. That number beats every sourced figure for your event. Still hold it under 240, because one edition is a sample of one. This is the own-ratio ceiling.
- **If you have no usable data, start below 240.** A first-pass ceiling of about 180-200 is my own construction, not a sourced figure. It keeps expected attendance near or under 120 even at a 72% show rate (about 130-144 at 180-200). Tune it with the realized count after the next session.
- **Write the ceiling down as a number.** Put it in the form configuration and name the person who closes the form.

### Mechanics around the ceiling

- **Waitlist.** Collect above the ceiling and promote first-come-first-served in one batch on a named date. Publish the ordering rule when the waitlist opens. Set a claim deadline for promoted people. Hand the promotion trigger, audience and deadline to `event-attendee-email-sequences` as a brief.
- **Day-of walk-in lane.** If people can physically reach your check-in desk, run a separate late-registration form, opened only after the pre-registered check-in window closes. Everyone still completes the full form. Hand your expected walk-in volume to `event-attendee-experience`.
- **Catering.** Order for the expected show-ups, not the registration count. At 240 registered and 50% expected, that is 120, with the 120-person buffer named separately. If you run a lower ceiling or a different expected rate, change the number to match.
- **Standing room or overflow.** Get written approval from whoever the venue names before registrations are accepted against it, never at the door.

## Decision

1. **Do not add the five-question form and mandatory confirmation click to fix no-shows.** If you want a confirmation click for list hygiene, argue it as that and accept the sign-up drop.
2. **Do not make 200% a standing rule.** Adopt a numeric ceiling instead: 240 at most, probably lower, set from your own past counts.
3. **Count registered versus attended every session.** It is the cheapest thing on this list, and it turns the borrowed ratio into your own.
4. **If no-shows are still the pain after that, take two things to the owning skills:** the reminder cadence (`event-attendee-email-sequences`) and a nominal fee (`event-ticket-pricing`).

## Open questions that would change these numbers

1. Is 120 the venue's hard limit, and is there any approved overflow?
2. Do you hold registered-versus-attended counts from earlier sessions in this series?
3. When does catering lock?
4. Do reminder emails already exist?
5. Can an unregistered person reach the check-in desk?
6. Is a nominal fee already ruled out?