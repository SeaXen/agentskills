# Larkfield Hack judging setup

## Fit check

- 14 teams × 8 min = 112 min per judge, inside the 120-min block.
- Slack is 8 min in total, so the real constraint is changeover time.
- Treat each 8-min slot as 7 min of judging plus 1 min to move teams.

## Setup: parallel stations, every judge sees every team

1. Put each judge at their own fixed station, A to E. They are never in a room together.
2. Teams rotate. Every team visits all 5 judges once, and every judge sees all 14 teams.
3. Use the schedule below. Team `t` visits station `s` in slot `(t + 3s) mod 14`. Each team gets 2 free slots between visits, and each station sees one team per slot.
4. Each judge submits their score on a shared form (spreadsheet or form) before the next team arrives. Nothing is collected at the end.
5. There is no deliberation step. The organizer computes the result and announces it after the judges have left.

| Slot | A | B | C | D | E |
|---|---|---|---|---|---|
| 1 | 1 | 12 | 9 | 6 | 3 |
| 2 | 2 | 13 | 10 | 7 | 4 |
| 3 | 3 | 14 | 11 | 8 | 5 |
| 4 | 4 | 1 | 12 | 9 | 6 |
| 5 | 5 | 2 | 13 | 10 | 7 |
| 6 | 6 | 3 | 14 | 11 | 8 |
| 7 | 7 | 4 | 1 | 12 | 9 |
| 8 | 8 | 5 | 2 | 13 | 10 |
| 9 | 9 | 6 | 3 | 14 | 11 |
| 10 | 10 | 7 | 4 | 1 | 12 |
| 11 | 11 | 8 | 5 | 2 | 13 |
| 12 | 12 | 9 | 6 | 3 | 14 |
| 13 | 13 | 10 | 7 | 4 | 1 |
| 14 | 14 | 11 | 8 | 5 | 2 |

Each judge also sees the teams in a different order, which spreads order effects.

## Scoring: z-scoring is fine here, but check it first

⚠️ Z-scoring only separates judge severity from team quality when every judge scores the same teams. That is the reason for the fully crossed design above. If you split the teams across judges to save time, the severe judge's average would also reflect which teams he drew. Z-scoring could not tell the two apart.

⚠️ Z-scoring does two things. It removes the offset (the "two points below"), and it rescales the spread. If he scores almost everything 1 or 2, his SD is small. Z-scoring then stretches his small differences to the same weight as everyone else's. That can amplify noise.

Recommended calculation:

1. **Primary:** subtract each judge's own mean from their scores, then average across the 5 judges. This removes the offset and keeps the spread.
2. **Check:** compute the z-score version and the rank-sum version (sum of each judge's ranks).
3. **Compare the three.** If the top 3 are the same, publish the primary result. If they differ, look at the severe judge's SD from last year. It is probably the cause.
4. **Ties:** use the lower rank-sum. Nobody needs to meet to settle it.

With 14 teams and a 1-5 scale, expect ties on raw scores. Z-scoring will not fix that.

## Risks

- 🟠 **Changeover:** with only 8 min of total slack, a late team ripples down the whole grid. Add a timekeeper with a 6-min warning. Pre-assign teams a "wait zone" near their next station.
- 🟠 **Judge drift:** judges can't recalibrate without meeting. Send a one-page rubric beforehand and ask each judge to use the full 1-5 range at least once. This also keeps the severe judge's SD from collapsing.
- 🟢 **Late departures:** if a train forces a judge to leave early, his slots are the problem. Give him the earliest slot positions, or swap him with the fifth judge, who has no train.

## Question for you

Does "8 minutes of judge time per team" mean 8 min per judge (as I assumed), or 8 min for the whole panel? If it's the whole panel together, the design changes to one table with all 5 judges present. That conflicts with your "not in a room together" constraint. Tell me and I'll redo the schedule.