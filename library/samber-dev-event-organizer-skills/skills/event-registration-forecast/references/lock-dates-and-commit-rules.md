# Lock dates and commit rules

## Contents

- Lock-date catalogue
- Hotel room-nights
- The newsvendor rule
- Worked commit
- Tier mapping
- Handing the go/no-go criterion over

## Lock-date catalogue

Collect each date from the actual contracts; the timings below are typical shapes, not terms to assume.

| Commitment | Typical lock | Can it move after? | Cheaper mistake |
| --- | --- | --- | --- |
| Catering headcount guarantee | Days before the event, set by the caterer or venue | Up, sometimes, at a premium; rarely down | Usually over-ordering: hungry attendees cost more than spare covers |
| Hotel room block | Group rate commonly expires about a month out; a block can carry an ~80% usage guarantee | Can usually grow while rooms remain | Under-blocking: start small and add rooms as it fills |
| Venue cancellation fee | Steps up at fixed days-out points, e.g. 50% beyond 90 days, ~70% from 30-90, ~90% under 30 (representative, negotiated per contract) | No | Set by the go/no-go poll, not by this rule |
| Second room or larger-room option | The option's expiry in the venue contract | No | Depends on the price of the option against turning people away |
| Swag, badges, printed material | The print or order deadline | No, short of a rush order | Usually under-ordering for badges (everyone needs one); over-ordering for swag |

The hotel-block figures come from the DevOpsDays organizing guide: an ~80% usage guarantee when the block is the only business given to the hotel, a starter block of as few as five rooms grown as it fills, a rate code that typically expires about a month out. The cancellation steps are representative structures cited by contract specialists.

## Hotel room-nights

Convert attendance into room-nights before committing a block. Every input is own data or self-set; nothing here is a published ratio.

room-nights = attendance x out-of-town share x nights per guest / guests per room

- **Out-of-town share**: from last edition's registration postcodes or a registration question.
- **Nights per guest**: the nights the event actually needs. The DevOpsDays guide scopes a two-day event to the night before day one and the night between the days, never the night after the last day.
- **Guests per room**: 1 unless your attendees demonstrably share.
- Grow a block later only where the hotel confirms in writing that rooms can be added at the group rate. In a busy city week they often cannot, and the low-end commit then leaves attendees paying rack rate.

## The newsvendor rule

Inventory theory's newsvendor problem: one order, one selling period, uncertain demand. Order up to the quantile where the cost of one unit too few equals the cost of one unit too many: target quantile = cost of short / (cost of short + cost of over).

With only a low / mid / high band, use it as a direction, not a formula:

- Short costs clearly more than over → commit at the high end.
- Over costs clearly more than short → commit at the low end, and plan the next step up if the line can grow.
- A line that can still grow by a flex after the lock → commit the chosen end divided by one plus the flex.
- Roughly equal → the mid, and say so.

Write the comparison in words next to every commit figure ("one short lunch is a person without food; one spare lunch is a cover's cost, so high end"). A commit figure without its reason cannot be reviewed.

## Worked commit

Band for final registrations net of comps: low 347, mid 412, high 534. Comps: 40 speakers, 30 sponsor staff. Ticket-type attendance from the script: 364 / 422 / 528.

- Catering guarantee, 7 days out, can rise by 5% up to two days out: short costs more, so aim at high-end attendance, 528, and commit 528 / 1.05 = 503, keeping the 5% for a late surge. Give 503 as provisional now; re-run on the lock date and commit the figure that run gives.
- Hotel block, 30 days out, 80% usage guarantee, hotel confirms it can add rooms: over costs more, so commit low-end room-nights. With 40% out-of-town, two nights, one guest per room: 364 x 0.4 x 2 = 291 room-nights. Ask for more if pickup runs ahead.
- Badge print, 10 days out: short costs more; print to high-end registrations plus comps.

## Tier mapping

`samber/dev-event-organizer-skills@event-budget` defines the Good / Better / Best tiers. At each lock date, report which tier the **low end** funds. Commit scalable lines at that tier; commit locked lines per the newsvendor rule. Never pick the tier from the mid: the tier is the floor the event can still pay for if the low end arrives.

## Handing the go/no-go criterion over

`samber/dev-event-organizer-skills@event-risk-management` places go/no-go reviews just ahead of each cancellation-fee step and fixes thresholds before the meeting. Deliver to it:

- The registration threshold, as declared before the reading.
- The band at that date, and which end clears it: low clears, mid clears but low does not, or mid misses.
- The references and method behind the band.

The poll decides. A miss on the registration criterion alone is an input, not a cancellation.
