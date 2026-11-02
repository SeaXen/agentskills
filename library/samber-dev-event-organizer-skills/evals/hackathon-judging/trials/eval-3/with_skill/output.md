# Larkfield Hack judging setup

Both ideas are dropped or redirected below. Z-scoring is not needed, and a deliberation meeting is not possible, so there is none.

## 1. Allocation: full coverage fits

- N = 14 teams, t = 8 min, W = 120 min, J = 5.
- Full coverage needs N ≤ W / t, and 14 ≤ 15, so it fits.
- Feasibility gate: k = floor(5 × 120 / (14 × 8)) = floor(5.36) = 5. Each team gets all 5 judges.
- Each judge walks all 14 tables: 14 × 8 = 112 min. That leaves 8 min of slack, one slot.
- ⚠️ The 8 min is judge time per team, swap included. Spending the slack on a no-show is the only buffer, so do not cut t on the day.

**Rotation map.** Each team hosts one judge per slot, and judges stay out of each other's way.

- Slots run 1 to 14, 8 min each. Slot s starts at minute 8 × (s − 1).
- Judge offsets are J1 = 0, J2 = 3, J3 = 6, J4 = 9, J5 = 12.
- In slot s, judge Jx visits team ((offset + s − 1) mod 14) + 1.
- Offsets differ mod 14, so no two judges are ever at the same team in the same slot.
- Example: J1 goes 1, 2, 3 … 14. J2 starts at team 4 and wraps through 14 to 1, 2, 3.
- Print one named sheet per judge, listing teams in order with start times.
- No-show rule: skip the team, note it, and revisit in the spare slot at minute 112. Never skip a team.

## 2. The severe judge: do not z-score

- A uniformly harsh judge scores every team, so he subtracts the same constant from all 14.
- His shift to each team's average is about 2 × 1/5 = 0.4 points. The same amount comes off every team, so the order does not change.
- Normalizing corrects a sampled panel, where a judge sees only a slice. Under full coverage it is pure overhead.
- **Combination rule: raw average of the weighted totals.** Publish that one rule and do not switch mid-round.
- Z-scoring also rescales each judge by their own spread. A judge who happens to score in a narrow band gets amplified, which can move ranks for no good reason.
- ℹ️ My inference, not in the skill: "two points below" may be clipped by the floor of a 1-5 sheet. A 3 becomes a 1, but a 2 cannot go to 0. A clipped judge is not a constant shift, and neither raw averaging nor z-scoring fully fixes it. Have the data person check last year's sheet for a pile of 1s from him. If it is there, brief him on the full range and ask for no floor-hugging. That is a briefing fix, not a math fix.
- Your data person can run z-scores privately as a sanity check. If the ranking is identical, nothing changes. The published rule stays the raw average.

## 3. Trains: independent scoring, no meeting

- The skill deletes synchronous consensus when judges leave straight after their slot. That is your case, so it is off the table.
- Each judge scores alone at the table, on the sheet, and hands it in before leaving. A sheet that has not been handed in does not count.
- Judging stops at minute 112 and all sheets are in by minute 120. The organizer tallies afterwards. Judges do not stay to deliberate.
- Do not re-score after the fact. A second pass scores a memory, not a project.

## 4. Rubric (placeholder, needs your brief)

- Use the categories your published brief already names and keep their exact wording.
- Cap them at 4. Use integer weights summing to 100, on a 1-5 integer scale per criterion.
- The weighted total is computed by the sheet, never by the judge.
- Put the heaviest weight on the criterion a judge can actually observe in 8 minutes, such as a working demo.
- Publish the category names and any elimination list. The numeric weights can stay internal.
- Skip the mandatory written comment unless you promise teams per-team feedback and have a window to write it in.

## 5. Tie-break ladder (publish before submissions close)

1. Higher score on the highest-weighted criterion.
2. More judges who put the team first among the 14 they all saw. This works from the sheets alone, so no one has to be in the room.
3. A named tie-break judge decides, on the record, in one sentence. This must be the one judge staying past 120 min, or an organizer with that authority named in the rules.
4. Co-award, only if the prize is divisible and the rules said so.

## 6. Conflict of interest

- Default: self-declared recusal, as one line in the judge brief. With full coverage, a recused judge simply skips that table. Record it and drop that judge's score for that team.
- With 5 judges, a team that loses 2 or more judges is no longer comparable. Fallback: rank on the remaining judges' average and note it.
- If a sponsor funds a track or a sponsor rep is a judge, the plan changes. See the questions below.
- Check the judge list against the entrant list before scoring.

## 7. Judge brief (6 items, in writing before scoring)

1. Criteria, with weights.
2. Scale, with what a 1 and a 5 mean.
3. Conflict rule and who to tell.
4. Their rotation sheet.
5. The clock: 8 min per team. If behind, skip the notes, never the team.
6. What happens to their scores: raw average, per-judge scores are not published, and the tie-break may reach for their sheet. Add that the sheet must be handed in before they leave.

Call judges in an hour before the start and send the sheet with the calendar invite.

## 8. Announcement and contest path

- Prepare the winner list before the ceremony and announce from slides.
- Announce rank and criteria. Do not announce per-judge scores or weights.
- Publish one contest path before submissions close: a named recipient, a short window that closes before prizes are paid, and what can change. An arithmetic or eligibility error can change a result, a judge's opinion cannot.

## 9. Gate and signals

- Before scoring opens, these six must exist in writing with no blanks: criteria and weights, scale, rotation map, conflict rule with fallback, tie-break ladder, contest path.
- Record these for next year: whether all judges finished inside the window, no-shows, recusals, and any floor-clipping from the severe judge.

## Questions I need answered

1. What categories does the published brief name?
2. Does any sponsor fund a track, and does a sponsor rep judge it? If so, the track needs its own weighted total, the rep confined to that track, a neutral co-judge, and a drop-test.
3. Which judge is not leaving by train? That judge is the tie-break judge.
4. Do teams get per-team feedback, and is there a window afterwards to write it?
5. What did last year's published rules promise on ties and disputes?
6. Is every judge confirmed for the full 120 minutes?