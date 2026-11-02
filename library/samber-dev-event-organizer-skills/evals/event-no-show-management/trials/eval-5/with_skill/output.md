# No-show plan: Grenoble developer day (220 seats, 410 registered, 90 waitlisted)

I read `event-no-show-management/SKILL.md` and both references. I could not run the one-question-at-a-time interview, so the assumptions are listed first.

## Assumptions

- ⚠️ "Catering locks 7 days out" means 7 days before the event. If it means 7 days from today, the catering number below stays the same, but the waitlist batch can no longer change what catering orders.
- ⚠️ The event date is unknown, so dates are relative to event day **T**.
- ℹ️ 220 is the binding capacity. Nothing in the brief mentions standing room or an overflow space.
- ℹ️ The event is free to registrants. Ticket posture is `event-ticket-pricing`'s, so I did not reopen it.

## Main point

The room is more likely to be tight than empty, and access control removes both safety valves. You are already at 1.86× capacity, inside the sourced 2× ceiling. No unregistered person can walk in, and nobody can be squeezed in. The plan therefore needs a hard door count, not only arithmetic.

## 1. Ceiling and arithmetic

| Line | Value | Label |
|---|---|---|
| Hard capacity | 220 | given |
| Show-up rate used | ~50% | sourced: MLH trendline across 323 free events |
| Sourced maximum | 220 ÷ 0.5 = 440 | sourced: aim for double, never exceed it |
| **Ceiling held** | **410 (the current list)** | self-set |
| Expected arrivals | 410 × 0.5 = **205** | derived |
| Range at 40–60% show-up | 164–246 | free band |

- **Why 410, not 440:** the only valve above the ceiling is turning registered people away at the gate. At 60% show-up, 410 registrants already gives 246 arrivals, which is 26 over capacity.
- **Check-in-verified sample:** its free median is ~28% no-show. That would put about 295 at the door. It is a population figure, so I do not use it to set the ceiling, but it is why the door count below is mandatory.
- **Scope caveat:** no sourced figure covers a company-run campus day with ID checks. Treat 50% as a starting point, not a forecast.
- **Enforcement:** registration closes at 410 now. Name one person who owns that and who makes the 410 vs. 440 decision.

## 2. Waitlist: signup order, one batch, fixed date

- **Order:** signup order (FIFO). I do not recommend proximity ordering. It adds hand-sorting on location data, which you would have to publish, and no figure backs its gain.
- **Publish the rule now,** on the waitlist page and in the Slack Connect channel. It should state:
  - the order;
  - the drain date (T-5d);
  - a 24-hour claim window;
  - who decides.
- **No per-seat promotion on cancellations.** The skill deletes that option.

### The 72-hour approval list as the filter

You already have to collect legal names and ID details for the approved list. Make that the commitment step.

1. **T-6d:** every registrant must submit ID details. Anyone who has not done so by the deadline is released from the list. The deadline and its consequence are stated up front.
2. **T-5d, one batch:** let C be the number of registrants who completed the step. Promote waitlisters in signup order to fill **P = max(0, 220 − C)**, capped at 90. A promoted waitlister claims the seat by submitting ID details within 24 hours.
3. **If C ≥ 220:** no promotions.
4. **T-3d (72 hours):** submit the list to security. It contains the C + P people, plus the rest of the waitlist as a **standby tier** (see below). Standby people also submit ID details by T-4d.

⚠️ This filter is my construction, not a sourced mechanic. I assume completers show more often than the 50% average, so the rule fills the list to 220 names and not beyond. Measure that completion-to-attendance rate. It is your best data for next time.

## 3. Day-of: the gap absorber

- ❌ **Walk-in lane: deleted.** An unlisted person cannot pass the gatehouse, so there is no walk-up population.
- ✅ **Standby lane, if security approves.** The skill's conditions are met: access-controlled site and a channel that reaches the waitlist within a day. Slack Connect plus email covers that. The lane works like this:
  - The night before, tell standby people: "Not confirmed. Do not travel unless you get a go message by [named time]."
  - The gate keeps one running arrival count. At the named time (for example 09:45, after the check-in window closes), the count is N.
  - Release **one batch** of 220 − N go messages, in signup order, with a 30-minute claim window.
  - Standby people are already on the approved list, so they pass the gatehouse normally and are escorted in.
- **Expected volume to hand to `event-attendee-experience`:** about 15 seats at 50% show-up, up to ~56 at 40%. The desk can plan for 15–56 late arrivals.
- **One batch, not per-seat swaps.** A live named-seat swap is untested territory in the skill.
- **If security refuses post-cutoff entry:** the standby lane is deleted. Everything else still works, and you accept the 5–15% of seats that stay empty as the cost of the 72-hour rule.

## 4. Hard occupancy gate (pass/fail, not tradeable)

- Door count of 220 at the auditorium, with the counter owner named.
- If more than 220 arrive, entry order is the ID-details submission time. Publish that rule at the T-6d request so nobody is surprised.
- 🔐 Any overflow room (a livestream room, for example) needs written approval from whoever the venue names, before it goes on any page.

## 5. Questions to security and the venue, in writing

1. Can names be added or swapped after the 72-hour cutoff? Until when?
2. Can the approved list exceed 220 names, with the count enforced at the auditorium door?
3. Is an overflow room allowed?
4. How many arrivals can the escorts process per 15 minutes? Stagger arrival slots if the number is low.

## 6. Handoffs

- **Catering (`event-budget`):** send **205**, the expected show-up, not 410 and not 220. State the buffer separately: 410 − 205 = 205. Ask the caterer for a top-up flex to 220, the room maximum.
- **Reminder sequence (`event-attendee-email-sequences`):** I hand over briefs, not copy.
  - The ID-details request: trigger, audience, T-6d deadline, and the release consequence.
  - The waitlist promotion: T-5d, 24-hour claim.
  - The standby night-before notice, and the go message.
  - The ratio in use (410 held at a 440 maximum), and the time registration closed.
  - Waitlisters are told their names go to site security. Confirm this fits the consent they gave.
- **Check-in desk (`event-attendee-experience`):** the standby volume and release time above.

## 7. Deposit question

No deposit mechanic is recommended, and I cannot rank one. The evidence is two single events, not studies:

- Eventtia: a $3 deposit cut no-shows from 38% to 14%.
- 37signals: a $100 deposit refunded at the door gave a 90% show rate.

A deposit would carry three costs:

- refund handling for every attendee;
- accounting and tax obligations;
- a barrier for people who most need a free seat.

The sourced lever in that direction is a nominal fee, which belongs to `event-ticket-pricing`. With ID checks and escorts, your friction is already high.

## 8. Count and record

Record:

- registered (410);
- ID details completed (C);
- waitlist promotions (P) and how many of them arrived;
- standby released, and how many of them arrived;
- attended;
- covers ordered vs. eaten.

Hand the realised show-up rate to `event-market-fit`. Keep it as next edition's own ratio.

## What is sourced and what is mine

- **Sourced:** 50% show-up trendline, 2× ceiling, free and paid bands, FIFO default.
- **Self-set:**
  - holding at 410;
  - using the ID-details step as a filter;
  - P = 220 − C;
  - the standby tier on the approved list;
  - the 09:45 release time.
- **Not measured anywhere:** show-up for a campus-secured event. Your first-edition count is the only real data.