**Do neither as proposed.** Both fixes aim at the right problem, which is empty seats, but the evidence behind each doesn't support the fix.

## 1. Form plus mandatory confirmation click: no

**The data is confounded.** Events with easy registration draw more casual signups, so their show rate (a ratio) is lower. Their absolute attendance can still be higher. A cross-event correlation doesn't show that adding friction to your event would raise turnout.

**The cost is certain, the gain isn't.** A mandatory confirmation click plus five questions will cut signups. Double opt-in alone typically loses a meaningful share of people, and a longer form loses more. If the show rate rises from 45% to 60% but registrations fall by half, you seat fewer people.

**What to do instead:** keep the single email field and add commitment after signup.
1. Send a calendar invite (.ics) in the confirmation email.
2. Send reminders at 7 days, 1 day and the morning of the event.
3. Add a reconfirm step about 3 days out ("keep my seat" / "release my seat"). Release unconfirmed seats to a waitlist. This gets the commitment effect without losing top-of-funnel signups.
4. Put a one-click "can't make it" link in every email, so people free their seat instead of ghosting.
5. Ask the extra questions on the thank-you page, optional, and only the ones you'll use.

**If she wants proof:** randomize. Show half of signups the long form and half the short one for a few sessions. Compare attendees per session, not show rate.

## 2. Make 200% the standing overbooking rule: no

**The guide's numbers are pacing benchmarks, not an overbooking formula.** "100% of goal two weeks out, 200% one week out" is a heuristic for whether an event is on track. It doesn't say how many registrations the room can safely absorb. Your correct overbooking factor is about 1 / your show rate, and the guide doesn't know your show rate.

**A fixed 200% fails in both directions.** Take 120 seats, and use the normal approximation to the binomial:

| Show rate | Registrations at 200% (240) | Expected attendees | Outcome |
|---|---|---|---|
| 40% | 240 | 96 | Fine, 24 empty seats |
| 50% | 240 | 120 | About a 50% chance of exceeding capacity |
| 70% | 240 | 168 | About 48 people turned away |

At a 50% show rate, a registration cap near 210 gives about a 2% chance of exceeding 120. Turning people away from a free workshop costs goodwill, so that risk should be small.

**What to do instead:**
1. Pull your history: registrations, attendees and registration lead time, per session. Compute the show rate, its spread across sessions, and whether late signups show up more often than early ones.
2. Set the cap from a quantile of that distribution, such as "P(attendees > 120) ≤ 5%". Don't set it from a percentage of goal.
3. Open a waitlist at the cap. Promote people from it as reconfirmations come in, which is where the reconfirm step above pays off.
4. Use the guide's 100%/200% numbers only as an on-track alarm, if at all.
5. Re-estimate the show rate every few sessions. It will shift once reminders and reconfirm are in place.

## Next step

Send her the per-session registrations and attendees. With a handful of past sessions I can compute your show rate and the actual cap.