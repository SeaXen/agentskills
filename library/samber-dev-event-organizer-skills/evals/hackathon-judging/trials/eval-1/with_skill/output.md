# DriftCon Build Weekend: judging round plan

## ❌ The full-coverage plan does not fit

Letting all 15 judges walk all 48 tables is arithmetically impossible, and the extra judges don't change that.

- Window `W` is 15:30 to 17:00, which is **90 min**.
- Expo contact time `t` is **5 min** per team.
- Full coverage needs `N × t ≤ W`, so `N ≤ 90 / 5 = 18` teams.
- At 48 teams, each judge would need 48 × 5 = **240 min**, which is 150 min more than exists.
- The cap has no judge count in it. Every added judge still has to walk all 48 tables, so Northwind's 6 people cannot extend full coverage.
- Five minutes is also an optimistic upper bound. It allows little for walking and note-writing, so treat every number below as a ceiling.

## ✅ What fits: a sampled panel (Band 2)

The cap is `W / t = 18` teams. The sampled-panel limit is `(J × W) / t`, which is 162 teams with 9 judges and 270 with 15. Our 48 teams are between 18 and 162, so a sampled panel is feasible.

Judges per team is `k = floor((J × W) / (N × t))`:

| Judges | Zero buffer | Plan with a 15-min tally reserve (14 visits each, 70 min) |
| --- | --- | --- |
| 9 | k = 3 | 126 visits, so **k = 2** |
| 15 | k = 5 | 210 visits, so **k = 4** (192 needed, 18 spare) |

**Accept Northwind's offer, but for the right reason.** It doesn't buy full coverage. It lifts every team from 2 judges to 4, which makes the field much more comparable. It also adds conflict-of-interest exposure, covered below.

## Timeline

| Time | What happens |
| --- | --- |
| 14:30 | Judge briefing, before submissions close. The usual "one hour before ceremony" slot is 16:00, which is inside the judging window. |
| 15:30 | Submissions close. |
| 15:30 to 15:35 | Strike non-submitters from the map. Each judge's list just gets a gap. |
| 15:35 to 16:45 | Visits: 14 teams × 5 min = 70 min per judge. |
| 16:45 to 17:00 | Combine scores, run the drop-test and tie-break, load the slides. |

## 1. Allocation map

1. Number tables 1 to 48 along one physical walking loop, so ring order equals walking order.
2. Each judge gets a named list of 14 consecutive tables on that ring, with a start time.
3. Start offsets are spaced about 3.2 tables apart (48 / 15). Neighbouring judges overlap heavily, which gives every team 4 judges at minimum.
4. Overlap also chains the judges' scores together, which the normalization below needs.
5. Different judges start at different tables, so no team is always scored first or last.
6. Each panel mixes judge types: technical, business, domain, sponsor.
7. Check per-team coverage in a spreadsheet before the day. I reasoned the spacing by hand and did not run it.
8. Fallback if a judge falls behind: skip the notes, never skip a team. The overlap means a skipped tail table is still covered by neighbours.
9. If a team loses judges to recusal, route a replacement from an adjacent offset and record the swap. Never "average what is left".
10. If a judge arrives late, `W` shrinks for them. Confirm each judge's arrival in minutes, not "afternoon".

## 2. Rubric

The brief's category names are fixed upstream and I haven't seen them. This is a placeholder shape to map onto them. Keep the brief's exact wording.

| Criterion | Weight |
| --- | --- |
| Working demo | 35% |
| Technical execution | 25% |
| Fit to the brief | 25% |
| Presentation | 15% |

- **Scale:** integer 1 to 5 per criterion, at most four criteria. The sheet computes the weighted total, never the judge.
- **Written comments:** none inside the 5-minute slot. Add them only if teams are promised per-team feedback and you have a post-event window to write it.
- **Weights:** publish the category names and the elimination list. Keep the numeric weights internal unless you want them public.
- **Elimination gate:** keep it as a separate yes/no artifact, written against how this theme invites gaming. Print it next to the eligibility text in the brief.

## 3. Combination rule

- **Use per-judge normalization.** Each judge sees only 14 of 48 teams, so a harsh judge's offset lands on their slice only and moves the ranks. Convert each judge's scores to z-scores within their own slice before averaging.
- Normalization is computed from 14 teams each, which is thin. The ring overlap is the mitigation.
- **Raw averaging is wrong here.** It only cancels when every judge scored every team.
- **Synchronous consensus is out.** No window to convene, and no deliberation room is staged.
- **No organizer override** of the combined result.

## 4. Tie-break ladder

Publish it before submissions close. Walk it in order and stop at the first rung that separates the teams.

1. Highest score on the highest-weighted criterion.
2. Most judges who placed the team first among the teams they personally saw.
3. A **named** tie-break judge decides on the record, in one sentence.
4. Co-award, only if the prize is divisible and the rules said so.

No re-scoring and no coin flip.

## 5. Conflict of interest (Northwind)

Northwind providing 6 of 15 judges is the main exposure, since 40% of the jury would be one sponsor's staff.

- **Default rule:** self-declared recusal. If you know someone on a team, manage or are managed by them, or are hiring or investing in them, you don't score them and you tell the judging lead.
- **Promote to declared recusal plus an assigned replacement** if Northwind funds any track, which I don't yet know. Collect each judge's employer and ties at recruitment.
- **No formal process is deleted** as soon as any sponsor funds a prize.
- **Spread Northwind judges around the ring.** No team's panel should be majority-Northwind: at most 2 of its 4.
- **Run the drop-test on every podium and track winner.** Recompute the rank without Northwind judges' scores. If the winner changes, tell Northwind before the ceremony and decide in advance who makes the call.
- **Disclose the jury composition in the published rules before submissions close.** If it comes out after the announcement it reads as a scandal.
- **Teams using Northwind's platform:** Northwind judges get an explicit "use of sponsor tech" rubric prompt. Without it, it bleeds into their other scores.
- **Eligibility checks:**
  - Check the entrant list against the judge list before scoring.
  - Judges who mentored a team recuse from that team.

## 6. Judge brief

Deliver in writing and in person at 14:30, with the scoring grid attached to the calendar invite beforehand.

1. Criteria in the brief's words, with weights.
2. Scale, with what a 1 and a 5 each mean.
3. The conflict rule and who to tell.
4. Their own list: which tables, in what order, starting when.
5. The clock: 5 min per team, skip notes and never a team.
6. What happens to their scores afterwards: normalization, no per-judge publication, the tie-break may reach for their sheet.

## 7. Announcement and contest path

- Prepare the winner list and slides before the ceremony, sponsor tracks included, from the sponsor's advance confirmation. Do not schedule live demos at the ceremony.
- Announce the rank and the criteria. Withhold per-judge scores and the numeric weights.
- Contest path, published before submissions close:
  - A named role receives challenges.
  - The window closes before prizes change hands. A 48-hour window means holding cash payouts until it closes. Confirm with the cash-prize skill.
  - Only an arithmetic, missed-submission or eligibility error can change a result, never a judge's opinion.
  - Answer in writing, with the process rather than the verdict.

## 8. Signals to record

- Judges who finished their 14 visits in the window.
- Teams that got fewer than 4 judges.
- Recusals that fired.
- Challenges received.

## Feasibility gate

- With 15 judges, `k = floor(1350 / 240) = 5`, and the reserve-adjusted plan gives 4. That is at least 1, so the plan is feasible.
- With only the 9 original judges, `k` is 3 on paper and 2 with the tally reserve. That is still feasible, but it gives a thinner and less comparable field.
- Do not shorten `t` on the day. That re-scores whichever teams were seen first.

## Six artifacts that must exist in writing before scoring

Pass when all six exist with zero blanks. Today only the structure is ready.

- [ ] Criteria and weights (needs the brief's categories)
- [ ] Scale
- [ ] Allocation map (needs the final judge names and the submitted-team list)
- [ ] Conflict rule and its fallback
- [ ] Tie-break ladder (needs the named decider)
- [ ] Contest path (needs the named recipient and window)

## What I need from you

1. What are the brief's evaluation categories? The weights above are placeholders.
2. Which prizes and tracks exist? Does Northwind fund a track, and does any signed contract require a Northwind judge?
3. Do the published rules already promise anything about criteria, ties or disputes?
4. Who is the named tie-break judge, and who receives challenges?
5. Are teams promised per-team feedback, and is there a post-event window to write it in?
6. Can all judges be on-site by 14:30, and what are their employers and ties?