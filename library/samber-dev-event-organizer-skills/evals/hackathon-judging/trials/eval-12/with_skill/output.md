# Greymoor Hack judging plan

**Verdict: keep the expo visits and the final discussion. Change the panel makeup, and change what the discussion covers.** Your plan has two problems.
- Same-type panels leave most teams without a key expertise.
- A discussion of all 72 projects can't fit in the time that remains.

The numbers below assume the 150 minutes cover visits, tallying and the discussion. If the discussion sits outside the 150, you have more room. Tell me.

## 1. Allocation

Inputs: N = 72 teams, t = 4 min, W = 150 min, J = 9 judges.

- **Full coverage cap:** W/t = 37.5, so 37 teams. 72 is above it, so full coverage is impossible. Adding judges doesn't raise this cap.
- **Triage threshold:** (J×W)/t = 337.5. 72 is below it, so this is Band 2 (sampled panel).
- **Feasibility gate:** k = floor(1350 / 288) = **4**. k ≥ 1, so the plan is feasible.
- 4 minutes with no setup or swap allowance is an optimistic ceiling. If the 4 minutes exclude walking, the slack below absorbs it.

Two ways to spend the window:

| Option | Judges per team | Visit time | Slack left |
|---|---|---|---|
| Three panels of 3, moving as a unit (24 teams each) | 3 | 96 min | 54 min |
| Nine judges routed individually | 4 | 128 min | 22 min |

**Recommendation: the panel option.** It's simpler, and the slack pays for the discussion. The individual-route option leaves no room for any discussion.

## 2. Panel composition: don't group by type

Make each panel one backend engineer, one VC and one designer.

- **Blind spots.** With same-type panels, a team in the VC slice is never seen by an engineer. Technical execution is then scored by people who can't judge it. Mixed panels give every team all three views.
- **Rank distortion.** With same-type panels, the panel *is* the judge type. A team's rank then partly records which type it drew, and normalization can't remove that. Mixed panels remove it.
- **Agreement speed.** Agreeing faster isn't a goal. Three judges of one type agreeing is one opinion counted three times.
- **Arguing.** Each judge fills in their own sheet and doesn't confer at the table. Disagreement gets averaged by the scoring, so nobody needs to argue it out.

Assign teams to panels at random. If there are tracks, spread each track evenly across the three panels. Stagger each panel's starting table so no team is always seen last.

## 3. Combination rule

Each judge saw 24 of the 72 teams, so a harsh judge's penalty lands on one slice only. **Normalize per judge**: convert each judge's scores to z-scores within their own 24 teams, then average. 24 teams per judge is above the roughly-a-dozen floor for a stable correction.

## 4. Discussion: shortlist only, in timed passes

- **Why not all 72.** The 54 minutes of slack give 45 seconds per team at most, before any buffer. Two-thirds of the room never saw any given project.
- **What fits.** Open-ended consensus is the "starved" rung. It works only with slack, and the ceremony start can't move.

Timed schedule (150 min):

| Minutes | Step |
|---|---|
| 0–96 | Visits |
| 96–110 | Buffer for no-shows and late starts |
| 110–120 | Tally and normalize |
| 120–145 | Discussion |
| 145–150 | Hand the winner list to the announcement |

Discussion rules:

1. **Pass 1, shortlist (16 min).** The top 8 by normalized score, plus any team tied at the cut. 2 minutes each. The panel that saw the team states the evidence in one sentence.
2. **Pass 2, podium order (9 min).** Order the top 3 only.
3. A named timekeeper enforces both passes.
4. Every device in the room is off the network for the whole discussion.
5. At the hard stop with no agreement, the normalized score decides. An organizer override of the judges' result is deleted from the options.
6. Ranks below the shortlist come straight from the normalized scores.

The shortlist size, the timings, and the rescue rule below are my own settings, not published standards.

**Rescue rule (optional).** Each judge may nominate one off-list team they personally visited. Cap it at 2 added teams in total.

## 5. Rubric and scale (placeholder)

I don't have your brief's categories yet. These are an illustration only, so replace them with the published ones.

- 1–5 integer scale per criterion, with 4 criteria at most.
- Illustrative weights: working demo 35, technical execution 25, fit to the brief 25, presentation 15.
- Weights stay internal. Publish the category names and the elimination list.
- The sheet computes the weighted total.

## 6. Tie-break ladder (publish before submissions close)

1. Highest score on the highest-weighted criterion.
2. Most judges who placed the project first among the teams they saw.
3. A named tie-break judge decides, on the record, in one sentence.
4. Co-award, only if the prize is divisible and the rules said so in advance.

No coin flip and no re-scoring.

## 7. Conflict rule

Default is **self-declared recusal**. The judge tells the judging lead, and a judge from another panel covers that table. Record each swap. If a team loses so many judges that its scores aren't comparable, route replacements from another panel. If any sponsor funds a track, switch to declared recusal plus an assigned replacement. If a sponsor's contract puts its own representative on its track, I'll add the hard-case handling.

## 8. Judge brief (six items, in writing)

1. Criteria and weights.
2. Scale, with what a 1 and a 5 mean.
3. Conflict rule and who to tell.
4. Their own team list, order and start time.
5. The clock: skip the notes, never skip a team.
6. How scores combine, that per-judge scores stay private, and that the tie-break may reach for their sheet.

Call judges in one hour before the ceremony, and attach the scoring grid to their calendar invite early.

## 9. Announcement and contest path

- Announce from prepared slides, with the rank and criteria only. Don't publish raw scores or numeric weights.
- Draft contest path: challenges go to a named role, the window closes before prizes change hands, and only an arithmetic or eligibility error can change a result.
- No live demos at the ceremony.

## 10. Signals to record

- Judges who finished their slice inside the window.
- Recusals that fired.
- Challenges received.

## Pass threshold: 0 of 6 locked

Six items must exist in writing before scoring opens:

- criteria with weights
- scale
- allocation map
- conflict rule
- tie-break ladder
- contest path

## What I need from you

1. Does the 150 minutes include the discussion?
2. Does the 4 minutes include walking between tables?
3. What are the brief's published categories?
4. Does any sponsor fund a track, and does a contract require its representative to judge?
5. Will teams get per-team feedback after the event?
6. What did the published rules already promise on ties and disputes?
7. Who can break a tie on the record?
8. Does any judge also mentor, or have ties to a team? Is any judge on the entrant list?