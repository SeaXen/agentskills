# DriftCon Build Weekend: judging round plan

## ❌ Premise check: 15 judges cannot each walk all 48 tables

- One judge covering 48 tables at 5 min each needs 240 min. The window between submission close (15:30) and the ceremony (17:00) is 90 min, and some of that has to go to scoring and deliberation.
- Full coverage would take 15 × 240 = 3,600 judge-minutes. We have about 750 (15 judges × 50 min).
- Adding the 6 Northwind judges still helps. It raises the number of independent views per team, not coverage per judge.

| Judges | Walk time each | Visits available | Views per team |
|---|---|---|---|
| 9 | 55 min (11 slots) | 99 | 2 |
| 15 | 50 min (10 slots) | 150 | 3 |

Comparability comes from overlapping assignments, one shared rubric, and normalization. It does not come from every judge seeing every team.

**Assumption:** the 5 minutes includes walking between tables. If your ops lead meant 5 minutes of pure demo, plan on 6–7 minutes per slot and drop to 2 views per team.

## ✅ Recommendation: accept Northwind's 6 judges

Three views per team is the minimum for a defensible ranking. With two views, one harsh judge decides the result.

- **Northwind conflict rule:** Northwind judges skip any team that uses Northwind's platform or is competing for a Northwind prize. Count these teams now and balance the load for them.
- **Briefing:** all 6 new judges attend the same briefing as the other 9.
- **Fallback:** if Northwind cancels, run the same plan with 2 views per team and 11 slots (see below).

## Timeline (judging day)

| Time | What | Owner |
|---|---|---|
| 15:00 | Judge briefing: rubric, walk lists, calibration example | Judging lead |
| 15:30 | Submissions close. Late arrivals are scored only if a judge already has them in a slot. | Ops |
| 15:35–16:25 | **Main round:** 10 slots of 5 min, 3 views per team | Judges |
| 16:25–16:30 | Scores in, normalize, build the shortlist | Score keeper |
| 16:30–16:45 | **Finalist top-up:** top 6 teams get 2 extra views from judges who have not seen them | Judges |
| 16:45–16:55 | Judges' room: pick the winners | Judging lead |
| 16:55 | Result handed to MC | Judging lead |
| 17:00 | Ceremony | MC |

⚠️ This is tight, with 5 min of slack at most. If the main round slips, **cut the top-up** and decide from the main-round scores. Don't cut the main round.

## How the assignments work

1. **Pre-assign by table number, not by content.** This can happen a week ahead. Tables stay fixed, so no-shows just leave a gap.
2. **Each team gets 3 judges in a chained pattern.** Team *t* is seen by judges *t*, *t+1*, *t+2* (mod 15). Neighbouring judges share teams, so every judge's scores are linked to the others'. Disjoint judge groups would leave the scoring scales unlinked, so don't use them.
3. **Each judge gets 9–10 teams.** Judges at 9 teams get a free slot, useful for a re-look or a sponsor-conflict swap.
4. **A script produces a round-by-round schedule.** It assigns each judge one table per 5-minute slot, with no two judges at the same table in the same slot. This is a bipartite edge-coloring problem, and it is solvable in 10 colors because the max degree is 10.
5. **Each judge gets a printed walk list** with slot number, table number and team name. Staggered starts keep crowds off any one table.
6. **Conflicts:** judges list their own conflicts (employer, mentee, relative) by day −7. The script excludes those pairs and re-balances.

## Scoring

- **Rubric:** 4 criteria, each scored 1–5, equal weights. Suggested criteria: problem and impact, technical depth, completeness of the working demo, and clarity of the pitch. Lock the wording at the briefing.
- **Per-visit timing:** about 3.5 min demo and Q&A, 1 min scoring, 30 s walking.
- **Entry:** scores go into a shared sheet or form right after each visit, one row per judge × team. Nobody scores from memory at the end.
- **Flag:** each judge marks their top 2 teams.
- **Normalization:** subtract each judge's mean from their scores, then average per team. The chained overlap is what makes the judge offsets estimable.
- **Shortlist (6 finalists):** the top 6 by normalized score, plus any team flagged by 2 or more judges. Break ties by the flag count.
- **Prize decision:** finalist top-up scores are averaged with the main-round scores. The judges' room can override the formula for prizes, but must write down why.

## What I need from you before building the schedule

1. Confirm the main window runs 15:35–16:25 and whether table numbers are fixed.
2. Confirm that 5 minutes includes walking time.
3. Tell me which teams use Northwind's platform, and which prizes Northwind sponsors.
4. Decide whether you want the schedule script written (about 40 lines of Python, run once teams and judges are final).

## Fallback if only 9 judges

- 2 views per team, 11 slots, window 15:35–16:30.
- The top-up becomes a quick check by all judges of the top 4 teams.
- Treat the winner as a close call between neighbouring teams, since 2 views give a weaker ranking.