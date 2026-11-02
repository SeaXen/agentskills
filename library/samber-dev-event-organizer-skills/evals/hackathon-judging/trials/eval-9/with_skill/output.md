# Ferrowood Hack: judge brief (draft for your review)

I changed three things in your plan. The first two need your decision before this goes out.

1. **The two judges with side projects can't do both.** The skill's rule is that judges, organizers, volunteers and sponsors don't compete. Taking judging slots on Sunday while their projects sit in the open track means they score their direct rivals. Recommended fix: pull both entries from the ranking and let them demo hors concours. The scored field becomes 14 teams. The alternative is that they step down as judges, which leaves 3 judges and makes the mentor recusals below unworkable.
2. **Your five mentors are not neutral judges.** Knowing the projects is not a bonus. A mentor who helped a team build can't score that team. The brief therefore has a recusal rule for every team a judge mentored.
3. **Reading the brief aloud ten minutes before scoring is too late.** The skill says to send judges the written brief and scoring grid with the calendar invite, then walk through it in person a full hour before the ceremony. Ten minutes at check-in leaves no time to fix a recusal list or a missing team. Send the brief as soon as you approve it.

**Assumptions to replace before sending.** I don't have your published brief, your window, or your per-team time. Brackets mark these:
- The four criteria below are placeholders. Use the exact category names from your published brief, and keep the weights internal.
- `W` is the number of minutes between submission close and ceremony start.
- `t` is the minutes per team.

---

## Feasibility check (organizer-only, do this first)

Formula: full coverage fits only if `N × t ≤ W`. Adding judges doesn't change that.

| Teams scored (N) | t = 5 min | t = 10 min |
|---|---|---|
| 14 (after the two withdrawals) | needs W ≥ 70 | needs W ≥ 140 |
| 16 (if you keep them in) | needs W ≥ 80 | needs W ≥ 160 |

- If your window clears the number for your `t`, use full coverage. Every judge visits every team, minus their own recusals. You need no allocation map beyond a visiting order.
- If it doesn't, compute `k = floor((5 × W) / (N × t))`. With 5 judges, `k ≥ 1` is almost certain, so you'd run a sampled panel. In that case tell me, because the combination rule changes.
- Don't shorten `t` on the day to make it fit. That re-scores whichever teams were seen first.
- The 5-minute figure is an optimistic upper bound. It allows nothing for walking or note-writing.

**Mentor recusals break uniform coverage.** Each judge skips their mentored teams, so judges score different subsets. The "harsh judge adds the same constant to every team" argument then stops holding.

- Use per-judge normalization. Convert each judge's scores to z-scores within that judge's own slice before averaging.
- Each judge's slice is about 11 to 13 teams, which is right at the skill's rough "about a dozen" floor. Expect the correction to be rough.
- Keep a raw-average column next to it as a sanity check. If the two rankings agree on the podium, you're fine.

---

## THE BRIEF (send to judges in writing; walk through it in person 60 minutes before the ceremony)

### 1. Your role

You judge finished projects. You are not a mentor today.

- Score what the team shows you in the slot. Don't score what you remember from Saturday.
- You judge for Ferrowood Hack, not for your employer.

### 2. What you score, and how

Score each criterion from 1 to 5, as integers. The sheet applies the weights and computes the total. Don't do any arithmetic in the aisle.

| Criterion (use the published names) | What to look for in the slot |
|---|---|
| [Working demo] | It runs live when you ask it to, not as a recording or a slide. |
| [Technical execution] | The hard part was built, not stubbed. |
| [Fit to the brief] | It answers the published challenge, not an adjacent problem. |
| [Presentation] | The team can say what it does in one sentence. |

- **1** means it barely meets the criterion, or fails it.
- **3** means solid and unremarkable.
- **5** means the best you will see on that criterion today.
- Write one clause of evidence per criterion, not a paragraph. For example: "Demo 5: ran live, handled a bad input."
- "Great energy" is not on the rubric. Don't let it carry a score.

### 3. Your visiting list

Your list is attached: teams, order, and start time.

- You get [t] minutes per team: [demo/Q&A split] plus the walk.
- If you fall behind, shorten your notes. Never skip a team. An unvisited team is a dispute.
- Tell the judging lead if you are running more than 10 minutes behind.

### 4. Conflicts: recuse, don't disclose

**Mentoring counts as a conflict.** Before scoring opens, circle every team on the sheet that fits any of these:
- You mentored it or gave it code-level or design help on Saturday.
- It includes someone you work with, manage, are managed by, have invested in or are hiring.
- It is from a company you compete with directly.

Do not score those teams. Leave the row blank and tell the judging lead, [name]. We will route a replacement judge to that table.

Fallback if a team loses too many judges: if fewer than 3 judges remain for a team, the judging lead brings in a neutral replacement who did not mentor that team. We record the swap. We never average what's left and hope.

**Judges don't compete.** Nobody on this panel has a scored entry. The two side projects entered by organizers/judges are shown hors concours and aren't ranked. If you spot any other entry connected to a judge, tell the judging lead before scoring opens.

### 5. What happens to your scores

- We normalize each judge's scores before combining them, so your personal harshness or generosity doesn't move the ranking.
- We announce the ranking and the criteria. We don't publish per-judge scores or the numeric weights, and your name is not attached to any team's score.
- The tie-break may reach back to your sheet (see section 6). Fill it in legibly and completely.
- Scores are final once you hand in the sheet. We don't re-score after the demos, because a second pass scores a memory, not a project.

### 6. Tie-break (published before submissions closed [confirm: it must have been])

Walk the list in order and stop at the first step that separates the teams.

1. Highest score on the highest-weighted criterion.
2. Most judges who placed the project first among the teams they personally saw.
3. [Named tie-break judge] decides on the record, in one sentence.
4. Co-award, only if the prize is divisible and the published rules said so.

No coin flips and no random draws.

### 7. Challenges

[Named role] receives challenges until [time, before prizes are handed over]. Only an arithmetic error or an eligibility error can change a result. A judge's opinion can't. The answer cites the rubric and which criterion decided the outcome, not individual scores.

### 8. Logistics

- Arrive by [time], 60 minutes before the ceremony, for the walk-through.
- Hand in sheets at [place] by [time].
- The deliberation/results room is set up with [seating, drinks, pens]. Phones off during any deliberation. A result that leaks early is a result nobody trusts.

---

## Before you send it

The skill sets six items that must exist in writing, with no blanks, before scoring opens. Status today:

| Item | Status |
|---|---|
| Criteria with weights | ❌ you fill in the published names and set weights (integers summing to 100) |
| Scoring scale | ✅ 1 to 5, drafted above |
| Allocation map (judge, teams, order, start time) | ❌ build it once you know the window and recusals |
| Conflict rule and recusal fallback | ✅ drafted above |
| Tie-break ladder | ⚠️ drafted, but check it matches what your published rules said. Name a tie-break judge. |
| Contest path | ⚠️ drafted, but you need to name the role and the time |

**Check the recusals now.** Collect each mentor's list of mentored teams today, not at check-in. With five mentors and 14 to 16 teams, a team that several mentors helped could lose most of its panel. Fix that by recruiting one or two neutral volunteers as backup judges.

**Signals to record this edition.** Note which judges finished inside the window, which teams got fewer judges than the map promised, how many recusals fired, and how many challenges came in. Next edition, consider recruiting judges separately from mentors.

I didn't touch prize amounts or payout rules. If you have a cash prize, the skill hands that to `hackathon-cash-prize`.