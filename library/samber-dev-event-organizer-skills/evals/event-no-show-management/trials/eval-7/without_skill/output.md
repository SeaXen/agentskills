**Use your own 47%, not the board's 50%. Set the registration ceiling at 600, with a waitlist beyond it.**

## Your show rate

| Edition | Registered | Attended | Show rate |
|---|---|---|---|
| 2023 | 528 | 251 | 47.5% |
| 2024 | 612 | 289 | 47.2% |
| Pooled | 1,140 | 540 | **47.4%** |

- The two editions differ by 0.3 points, with the same venue and format. That is a stable signal, and it is your data.
- The 50% rule overstates attendance by about 2.6 points. At 600 registered, the board predicts 300 attendees and your history predicts 284.
- Two editions is a small sample, so don't treat 47.4% as exact. I assumed the rate could drift by about ±3 points. That assumption is mine, not something your data shows.

## Ceiling: 600 registrations

- The pure math gives 300 / 0.474 ≈ 633 registrations to fill 300 seats on average.
- I would not go that high. With 633 registrations, roughly half of all outcomes put more than 300 people in the room, and your seats are the hard constraint.
- At 600, expected attendance is about 284, leaving 16 seats of headroom. Using my ±3-point drift assumption, the chance of more than 300 showing is roughly 1 in 4. Those overflows would typically be small, around 10 people.
- If your venue's capacity cap is strict, use 560 instead. That gives about 265 expected and roughly a 7% chance of overflow.
- Open a waitlist at the ceiling and release it in batches as people cancel.
- Send a "confirm or release your seat" email 7 days out. It lowers no-shows and shrinks the uncertainty band.
- Your 612 registrations in 2024 were already near this ceiling, so expect to hit it. Demand grew 16% from 2023 to 2024.
- The board's 50% rule happens to give the same 600. Only the reasoning differs, and the attendance forecast will be wrong by about 16 people if you use 50%.

## Catering: use 47.4% on day-15 registrations, capped at 300

The 22 EUR contract locks 15 days out, before registration closes. So the number you lock is a forecast of attendance, not a count of registrations.

- **Formula:** lock = min(300, ceil(0.474 × registered at day 15 × 1.05)).
- **If you are at the ceiling by day 15:** lock 300.
  - That costs 6,600 EUR against 6,250 EUR for the 284 expected, so about 350 EUR of insurance.
  - Short-feeding a full room is worse than that.
- **If you are at 450 registered at day 15:** lock about 224.
- The 5% buffer is a judgment call. Shrink it if the contract allows a cheap late top-up.
- Never lock above 300, since you only have 300 seats.

## Two things to check before locking

1. **Your day-15 snapshots.** Registrations keep arriving after day 15, and late registrants may show up at a different rate. If your platform has registration timestamps, pull the registered-at-day-15 count and attendance for 2023 and 2024. That ratio is a better catering multiplier than 47.4%.
2. **The missing edition.** This is the fourth edition and you gave me two prior years. If a third edition's numbers exist, add them, because three points beat two.

Also tell me whether the contract lets you adjust the count after day 15, and what a top-up or a no-show refund costs. That sets how large the buffer should be.