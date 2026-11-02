# Bellweather Hack judging: where to start

The arithmetic decides most of this, so start there. I read the `hackathon-judging` skill and its allocation reference, and I haven't asked you anything yet.

**One caveat:** the expo-versus-stage choice normally belongs to `event-format-selection`, and this skill treats it as a fixed input. I'm not re-deciding it. Below is the arithmetic that constrains that choice, and you can feed it to that step.

## 1. Stage pitch doesn't fit

At a stage pitch the whole jury sits together and teams present one after another. Every judge sees every team, so the judge count doesn't help. The cap is `N ≤ W / t`, where `N` is teams, `W` is judging minutes and `t` is judge time per team.

For the window I used 180 minutes as a stand-in for "the whole afternoon". This is an assumption, so please replace it with your real number.

| Format | `t` | Max teams in 180 min |
| --- | --- | --- |
| Stage pitch (MLH slot, setup and swap included) | 10 min | **18** |
| Stage pitch, tight | 5 min | 36 |
| Expo table | 4–5 min | 36–45 |

Your lowest case is 40 teams, and stage at 10 minutes needs 400 minutes for that. Even the tightest stage figure of 5 minutes misses by a few teams. ❌ Stage pitch fails across your whole range, unless you run parallel stages, which is a format change.

## 2. Expo tables fit, as a sampled panel

Past the full-coverage cap, 22 judges split into panels. Each team gets `k = floor((J × W) / (N × t))` judges, with `J = 22` and `W = 180` assumed:

| Teams (N) | `t` = 5 min | `t` = 4 min |
| --- | --- | --- |
| 40 | 19 judges per team | full coverage fits (45-team cap), but with almost no slack |
| 70 | 11 | 14 |
| 100 | 7 | 9 |
| 140 | 5 | 7 |

- ✅ **Even at 140 teams, every team gets at least 5 judges.** The upper limit, where not even one judge per team fits, is about 790 teams, so that's not a risk for you.
- ⚠️ **These `t` values are optimistic.** The 3–5 minute expo figure allows nothing for walking between tables or writing notes. Treat each `k` as an upper bound, not a promise.
- **You have more judges than you need.** Three or four judges per team is plenty. With surplus capacity you can lengthen the slot instead of maximising `k`. At 140 teams and `k = 3`, the slot could be up to about 9 minutes. That is a trade-off for you to decide.

## 3. Slot length

- **Default:** 4–5 minutes per team: about 2–3 minutes of demo, 1 minute of questions, and the rest for walking and scoring. MLH's own judging round uses 4 minutes including 1 minute of travel.
- **Reserve 15–20% of the window as buffer.** That absorbs teams that aren't at their table.
- ❌ **Never shorten `t` on the day.** It re-scores whichever teams were seen first. Compute the plan at your worst case (about 140 teams) and then run it at whatever turns up.

## 4. Consequences of 22 judges

- **Raw averages break across panels.** One harsh judge shifts only their slice. Use per-judge normalization, not a raw average. With full coverage it wouldn't matter, but you're in the sampled-panel case.
- **Build the allocation map after submissions close.** Prepare a spreadsheet template now, so that the real team count fills in a named list of judge, teams, order and start time. A judge without a written list improvises, and a team ends up unvisited.
- **Sponsor judges are a conflict-of-interest risk.** "Every sponsor wanted a seat" matters. If any sponsor funds a prize track, "no formal process" is off the table. You'd need declared recusal plus a replacement judge. If a contract requires a sponsor's rep to judge their own track, that rep stays on that track only, paired with a neutral judge, and the composition is disclosed in the rules before submissions close.
- **Check the judge list against the entrant list.** Do it before scoring opens.
- **Compose panels by judge type.** A technical judge and a business judge see different things.

## 5. Question I need next

**How many minutes run between submission close and the ceremony start?** Please give a number, such as 13:30 to 16:45 = 195 minutes. Every row above depends on it.

After that I'll ask one at a time:

1. Is a sponsor funding a prize track, and does a contract require their rep to judge it?
2. Which evaluation categories does the published brief already name?
3. What did the published rules promise about tie-breaks and disputes?
4. Will teams get per-team feedback, and is there a window after the ceremony to write it?
5. Can you run a volunteer pre-screen, and who breaks a tie on the record?

The full plan has six sections, which I'll present one at a time for your sign-off before judging opens:

1. Allocation
2. Rubric
3. Combination rule
4. Tie-break ladder
5. Conflict rule
6. Announcement plan

Nothing is scored until all six exist in writing.