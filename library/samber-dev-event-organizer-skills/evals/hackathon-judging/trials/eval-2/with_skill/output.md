# Kestrel Hack judging plan: 90 seconds per team won't work, so triage instead

The skill's arithmetic puts you in Band 3, where even one judge per team doesn't fit at 4 minutes. A 90-second visit is not a legitimate way out. I don't have your published rules, brief categories or volunteer count, so I've marked where those change the plan.

## 1. Allocation

Inputs: N = 210 teams, t = 4 min (expo), W = 100 min, J = 7 judges.

- Full coverage needs N ≤ W/t = **25 teams**. You have 210.
- One judge per team needs N ≤ J×W/t = 7×100/4 = **175 teams**. You have 210.
- k = floor(700 / 840) = **0**. That is Band 3, so only triage-then-finals is left.

**Four judges dropping out is what moved you across a band.** With all 11, J×W/t = 275, so k = 1 and the plan was feasible. The fix that needs no format change is getting judges back.

## 2. Why 90 seconds fails

- ❌ On paper t = 1.5 gives k = 2, which is why it's tempting.
- ❌ Even so, 210 × 1.5 × 2 = 630 of 700 judge-minutes. That is 90% of the window, with no buffer for a no-show and no time to compile scores.
- ❌ MLH's 4 minutes already includes 1 minute of judge travel. At 90 seconds, the demo is about 30 seconds.
- ❌ The skill says never absorb k < 1 by shortening t on the day. Teams seen first get a different visit than teams seen last, so you re-score the field. If the rules promised 4 minutes, you've also broken a published promise.
- ⚠️ "Push judges to move fast" is the failure mode described in the skill: judges skip notes, then skip teams.

## 3. The plan: pass/fail gate, then full visits for finalists

**Timeline (T = submission close)**

| Time | Step |
|---|---|
| T+0 to T+20 | Volunteers run a pass/fail gate: does it run, does it meet the brief's deliverable format, is it eligible. No scoring. |
| T+20 to T+85 | Finalists get full 4-minute visits. W₂ = 65 min of visits after the gate. |
| T+85 to T+100 | Compile scores, normalize, run tie-break, load slides. |

**Finalist cap.** Each judge fits 14 teams: 14 × 4 = 56 of 65 min, leaving about 14% buffer. So N₂ ≤ 7 × 14 = **98 finalists**.

| Judges (J) | Max finalists (14 per judge) |
|---|---|
| 7 | 98 |
| 9 | 126 |
| 11 | 154 |

- ⚠️ **The gate must cut at least 112 of 210 teams (53%).** I can't tell you the pass rate. If more than 98 teams pass, the gate alone doesn't fix this. You then need more judges or a format change.
- ⚠️ **The gate must be published before submissions closed.** A cut round teams didn't know about is the most contestable thing in this skill. If submissions are still open, publish the gate criteria now. If they're closed and the gate was never announced, tell me and I'll rework the plan.
- **Gate crew size** = 210 × (minutes per check) ÷ 20. At 1 minute per check that's 11 volunteers. Script the automated checks (repo public, links resolve) as submissions arrive.
- **Cut record.** Log every cut team with the failed requirement. That record is your answer to challenges.

## 4. Recover judges first (cheapest lever)

- With 11 judges, no gate is needed: 840 of 1,100 judge-minutes. It is thin after a compile reserve.
- Recruit **3 to 4 replacements** before submissions close. Nine judges with the gate gives 126 finalists, which loosens the cut to 40%.
- Replacements must have no ties to a team or a sponsor track. They can't be competitors, and a mentor can't score a team they mentored.
- Next edition, confirm about 1.5× the judges you need. 4 of 11 dropped out, a 36% no-show rate.

## 5. Format change (only if the gate and judge recovery both fall short)

Moving part of judging async (video) is a format decision. It belongs to `event-format-selection`, and it must be decided before the event. Don't improvise it on the day.

## 6. Rubric (placeholder weights)

I haven't seen the brief's categories, so these weights are the skill's worked example. Map them onto the brief's own wording, never rename.

- Working demo 35%, Technical execution 25%, Fit to the brief 25%, Presentation 15%.
- Scale is 1–5 integer per criterion, four criteria at most.
- No written per-criterion comment. There is no live time for it. Judges write one-clause evidence at most.
- Publish category names and the elimination list. Keep numeric weights internal.
- Elimination criteria are separate from the rubric. Write them against how this theme invites gaming.

## 7. Combination rule

- **Per-judge normalization** (rank or z-score within each judge's slice). Raw averages fail under sampling because a harsh judge's constant lands on one slice only.
- **No consensus round.** There's no window for one.
- ⚠️ Slices of 14 are just above the roughly-12 floor, so the correction is thin. If you can spare it, have each judge also score the same 2 to 3 shared teams. That costs finalist capacity.

## 8. Tie-break ladder (publish before close)

1. Highest score on the highest-weighted criterion.
2. Rung 2 as the skill writes it (count of judges placing the team first) is **degenerate at k = 1**. Replace it with higher normalized rank within the judge's own slice. This is my adaptation, so publish it explicitly.
3. A named tie-break judge decides on the record, in one sentence.
4. Co-award, only if the prize is divisible and the rules said so.

Refuse re-scoring and any coin flip.

## 9. Conflict of interest

- Self-declared recusal is the default, with replacement judges.
- With one judge per team, a recusal leaves a team with zero judges. Collect judge ties at recruitment and pre-assign a reserve judge for every flagged team.
- If any sponsor funds a track, "no formal process" is deleted.
- If a signed contract requires a sponsor judge: confine them to that track, pair them with a neutral judge, run the drop-test, and disclose before close.
- Check the entrant list against the judge list before scoring.

## 10. Judge brief (deliver before submissions close)

1. Criteria and weights.
2. Scale, with what a 1 and a 5 each mean.
3. Recusal rule and who to tell.
4. Their own team list, in order, with start time. Generate it by script from the gate output at T+20.
5. The clock: 4 minutes per team. If behind, skip the notes, never skip a team.
6. How scores combine, that per-judge scores aren't published, and that the tie-break may use their sheet.

## 11. Announcement and contest path

- Build the winner slides before the ceremony. Run no live demos at the ceremony.
- Announce rank and criteria only. Withhold per-judge scores.
- Publish a contest path with four parts:
  - A named role receives challenges.
  - The window closes before prizes change hands.
  - Only arithmetic, eligibility or missed-submission errors can change a result.
  - The answer cites the rubric and which criterion decided.
- Cut teams get the same path, answered from the cut record.

## 12. Gate check before scoring opens

All six must exist in writing: weighted criteria, scale, allocation map, conflict rule with fallback, tie-break ladder, contest path.

## 13. Signals to record

- Finalist visits completed inside the window.
- Gate pass rate and teams cut.
- Teams that got fewer judges than the map promised.
- Challenges received.

Revisions they trigger next edition: a gate pass rate above 47% means cap registration. Any skipped team means raise judge count.

## Questions that change this plan

1. Did the published rules promise 4-minute visits for every team, or announce a pre-screen?
2. How many gate volunteers do you have?
3. Can you recover 3 or more judges today?
4. What are the brief's evaluation categories, and does any sponsor fund a track?