**Scheme: 45-minute sessions on a 60-minute pitch, with a 15-minute changeover after every session and a 15-minute shared elastic buffer per block.**

Keep the COO's idea of a buffer with escalation thresholds. Change what the buffer is sized from and where it sits.

## Verdict on the COO's three numbers

- **50% of lead time: reject.** It gives a 22-minute gap, a 67-minute pitch and fewer sessions. The main delay is not duration variance. It is a fixed 7-minute stair walk plus crowding.
- **33% / 67% thresholds: keep.** Apply them to the elastic buffer (below).
- **85% utilization: reject for room time.** It fits random arrivals queuing for a shared server, and sessions are scheduled. Reuse it for seat fill instead (below).

## Two buffers

**1. Changeover buffer (fixed, never spent):**
- Every session ends 15 minutes before the next one starts.
- Size it from the physical route, not a percentage. Last year's lateness of about 10 minutes at zero gap is the measurement.
- Stairs 1→3 take 7 minutes. Add about 5 minutes for crowding and leaving late, and 3 minutes to find a seat.
- Use one uniform gap for all rooms. Slots stay synchronized and attendees can plan their own route.
- Do not shorten it when a session overruns. Count overruns against buffer 2.

**2. Elastic buffer (shared, 15 minutes per block):**
- It sits at the end of each block, before lunch, before coffee and before close.
- Aggregation is the reason to pool it. Overruns partly cancel across sessions, so one pooled buffer protects better than a small padding on every slot.
- Sizing: 3 sessions, with overrun standard deviation assumed at 3 minutes, gives √3 × 3 ≈ 5 minutes. Two standard deviations is about 10 minutes, rounded up to 15.
- **The 3-minute figure is my assumption.** Replace it with last year's overrun data. If the true standard deviation is 5 minutes, use 20–25 minutes.

## Day template

```
09:00–09:45  S1   10:00–10:45  S2   11:00–11:45  S3
11:45–13:00  Lunch (60) + elastic (15)
13:00–13:45  S4   14:00–14:45  S5
14:45–15:30  Coffee (15) + changeover (15) + elastic (15)
15:30–16:15  S6   16:30–17:15  S7
17:15–17:30  Elastic, then close
```

That gives 7 sessions per room per day and 35 per day across five rooms. The 50% rule gives about 6 per room.

## Escalation thresholds (per block, reset at each break)

Track cumulative lateness against the 15-minute elastic buffer.

- **Green, under 5 minutes (33%):** do nothing. Chairs hold time cards at 10 and 5 minutes before the end.
- **Yellow, 5 to 10 minutes (33–67%):** the stage manager alerts the chairs. Move Q&A in the next sessions to the corridor.
- **Red, over 10 minutes (67%):** the program lead acts. Hard-cut the overrunning talk and trim the break. The next block starts on time regardless.
- **Never spend the changeover.** Without it, the 10-minutes-late problem returns.

## Where 85% belongs

- Cap seat fill at 85%. Plan rooms so expected attendance is at most 85% of seats.
- A full room sends people back through the stairs and lift at the worst moment.
- Seat fill is the random-load case that the 85% rule is built for.

## Floor handling

- Reserve the slow lift for step-free access.
- Put a marshal on each stair landing during changeovers.
- Place the tracks people tend to pair on the same or adjacent floors.

**Test on day 1:** time door-open to seated for the floor 1→3 move. If the median is over 12 minutes, the gap is too tight.

**Next:** tell me which rooms are on which floors. I will check whether a pair of tracks can safely use a shorter gap.