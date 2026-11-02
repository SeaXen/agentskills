I couldn't produce the one number, so this is a partial brief. I couldn't read last year's export or run the forecast script, and the numbers below are conditional on that.

- **Export not found.** You said it's on disk. I have no path, and my searches outside the skill folder were blocked.
- **No script run.** I couldn't run `forecast-registrations.py`, and the skill says not to do this arithmetic by hand.
- **Fix.** Send me the export's path and I'll run the command below. I'll need its days-out and cumulative columns. Ideally it also notes the early-bird close and the speaker announcement.

## What I can say now

**Projection from the generic curve alone: about 700. Don't take it to the board.**
- The bundled pooled lead-time curve has 42.8% of final registrations on hand at 45 days out. 300 ÷ 0.428 ≈ 700.
- It is one generic reference, so it gives no band, only a point guess. The skill requires a second reference before any lock date.
- Last year's 520 at the end sets the scale. Whether 300 is ahead of or behind last year at 45 days is unknown until I see its curve.

**Where the on-hand count should be at the board meeting, 32 days out.**
- On the pooled curve, 32 days out is 52.7% of final, against 42.8% now. That is a 1.23× ratio, so about 370 on hand. This is a provisional range for the pooled curve only.
- To fix the tripwire I need last year's curve. Declare the range before the board meets, not after.

**Your 380 break-even is not the same as the final.**
- You are at 300 now and need 380 final. That is 80 more in 45 days.
- Last year's curve will show whether 80 more is likely. Most registrations arrive late.

## Rules to bring to the board

1. **Fix the threshold before the meeting.** The threshold is 380, net of comps. The 32-day meeting is the last review before the 30-day fee step from 50% to 75%. Re-deciding at 30 days costs 25 points more if you then cancel.
2. **Cancel only on the band, and the poll decides.**
   - If the low end clears 380, go.
   - If the mid clears but the low doesn't, go, and downgrade the scalable lines.
   - If the mid misses 380, escalate to a go/no-go poll through `event-risk-management`.
   - A miss on registrations alone is an input to that poll, not an automatic cancellation. Whether the concept lacks demand is `event-market-fit`'s call.
3. **Pick the tier from the low end, never the mid.**
   - Good needs 380, Better 450, Best 550.
   - Good is the floor. If the low end is under 380, no tier is funded, which is the escalation case.
   - Lock the scalable lines at the highest tier the low end supports. Don't lock Best now.
4. **Badges lock at 12 days out.**
   - Print to the high-end registrations plus 75 comps (45 speakers and 30 sponsor staff). Everyone needs a badge, so being short costs more than a spare badge.
   - Re-run the forecast on the lock date and use that figure. Any number now is provisional.
5. **Count comps once.** The 300 is net of comps. The 75 comp badges are added separately. Don't mix them into the registration count or the break-even.

## Command to run once I have the export

```
python3 scripts/forecast-registrations.py --actuals actuals.csv \
  --reference last-edition.csv --reference assets/curve-pooled-lead-time.csv \
  --threshold 380 --checkpoint board:32 --checkpoint badges:12 \
  --types ticket-types.csv
```

## Questions I need answered

1. Where is the export? Is it net of comps and of refunds?
2. Did any milestone move between editions? That means the early-bird close, the speaker announcement, or a push. If one moved, I run last year's curve as is and shifted.
3. What is the room capacity? That decides the capacity read, the cap, and the waitlist date.
4. What are the show rates for speakers and sponsor staff? Without your own data I use the self-set defaults and label them.