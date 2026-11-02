# Northbeam Robotics Rust-at-breakfast: no-show plan and deposit answer

I read `event-no-show-management` and both reference files. The skill does not let me give you a deposit flow as a recommended mechanic, so there is no page copy, charge timing, refund trigger or late-arrival policy below. Nobody has measured that mechanic in developer-event organizing, and a confident flow would imply a practice that isn't there. What follows is the plan the skill does support, plus a deposit experiment you could run if you still want one.

## 1. Your numbers against the sourced bands

- **Your own data:** about 90 RSVPs and about 45 attendees is a 50% show-up rate. That matches the free-event band (40–60% no-shows) and the hackathon-network trendline (~50% across 323 events, scoped to free hackathons).
- **Posture:** free registration. The ticket posture itself belongs to `event-ticket-pricing`, so I don't reopen it.
- **Sample size:** this is one month's ratio, or at best a few. Keep any ratio you derive from it under the sourced 2x ceiling.

## 2. Catering

The first fix doesn't need a deposit.

- **Order for the expected show-up number, not the registration count.** Sending the registration count to catering is one of the skill's named failure modes.
- **Arithmetic:** 90 registered × 0.5 = **45 covers**. The other 45 is the overbooking buffer, named separately so nobody orders 90 breakfasts.
- **Open question:** when does your catering guarantee lock? If you can order for 45 and the caterer allows a small top-up, most of the "paid either way" cost goes away without touching registration.

## 3. Registration ceiling (my assumptions need your input)

You haven't given me the room's hard capacity or the date registration closes.

| Line | Value |
|---|---|
| Hard capacity (fire code or venue contract) | **C, not yet known** |
| Expected show-up rate | 50% (sourced trendline; your own ratio agrees) |
| Registration ceiling | **C ÷ 0.5 = 2 × C, and not one more** |
| Who closes the form | a named person, to be set by you |

- The occupancy limit is a gate. Expected attendance (ceiling × 0.5) must stay under it, and any overflow space needs the venue's written approval before registration opens.
- Do not leave registration open with no ceiling.
- Waitlist: FIFO, drained on a date you publish when the waitlist opens, with a claim deadline for anyone promoted.
- The skill rules out promoting one seat at a time as people cancel.

## 4. Deposit: the stated gap

**The evidence:**
- Eventtia reported a $3 refundable deposit dropping one previously free conference from 38% to 14% no-shows.
- 37signals ran a free Chicago breakfast with a $100 deposit refunded at the door. 55 paid and 50 showed up.
- Both are single events, not studies, and neither is a developer-event study. They are the closest evidence to yours, which is a free breakfast.

**Why it may not transfer to you:** the mechanic relies on the registrant's own loss aversion. A corporate attendee whose employer reimburses a $40 charge may not feel it. Nothing measures that, so don't plan on it as a lever.

**The three costs, if you run it anyway:**
1. A refund to every attendee, every month.
2. The accounting and tax handling that comes from moving money at all. Ask your accountant how held and forfeited deposits are treated. I won't guess.
3. A barrier that falls hardest on people who can't float $40, such as students and the unemployed.

**Established alternative:** a nominal fee, which belongs to `event-ticket-pricing`. It has organizer practice behind it, and it turns an unpaid RSVP into a headcount you can commit spend against.

## 5. If you run it as an experiment

State the measurement before you start. All thresholds below are self-set, not sourced.

1. **Baseline:** 50% show-up on free registration.
2. **Window:** decide the number of sessions in advance. One session is a sample of one, so I'd treat that as too few to conclude anything.
3. **Primary measure:** show-up rate among deposit-holders.
4. **Side effect to log:** the drop in registrations. The deposit changes who registers, so your 90 will fall.
5. **Ceiling rule:** if the deposit works, the 2x ceiling no longer applies. Treat the event like a paid or nominal-fee one and take no overbooking. Decide this before the first session, not after.
6. **Decision rule:** write down the show-up rate that makes you keep it and the rate that makes you drop it.
7. **Count every session:** registered, attended, walk-ins, waitlist promotions and how many of those arrived. Feed the realised rate to `event-market-fit`.

## 6. Decisions only you can make

I'm not choosing values for these, because the skill has no sourced practice behind them. Publish them before the experiment starts.

- When the card is charged, and whether it is a hold or a capture.
- What triggers the refund, and who or what fires it.
- How long after doors open a late arrival still counts as having attended.
- Whether forfeited deposits are kept, and who is told.
- Whether a no-deposit path exists for people who can't float $40.

**Late arrivals:** the only sourced mechanic is for unregistered arrivals, so a late deposit-holder isn't covered. For walk-ins who never registered, use a separate late-registration form that opens only after pre-registered check-in closes. Everyone completes the full registration form.

## 7. Handoffs

- **`event-budget`:** 45 expected covers, with the 45-registration buffer named.
- **`event-attendee-email-sequences`:** the ceiling and ratio in use, the ceiling-close date, and a brief for each waitlist promotion. Reminders and any deposit wording sit with that skill, not this one.
- **`event-attendee-experience`:** expected walk-in volume and the time the late lane opens.
- **Persistent memory:** record the capacity, the 50% rate and its source, the ceiling arithmetic, the published waitlist rule and the registered-versus-attended count.

## What I need from you

1. Hard capacity of the room, and whether any overflow space has venue approval.
2. Date the catering guarantee locks.
3. What you actually order today: 90 covers or some other number.
4. Whether you would run the experiment or take the nominal-fee route.