Under five minutes means keeping about 12 of your 28 questions, not trimming wording. Three changes do most of the work:

1. Cut 3 of the 4 free-text boxes.
2. Shrink the 30-row grid.
3. Route people instead of showing everyone everything.

I haven't seen your 28 questions yet, so I can't say which 12 survive. Every time below is a planning estimate that your soft launch will replace.

## 1. Where the time goes now

| Item | Est. time |
|---|---|
| Grid, 30 rows × ~6 s | ~3 min |
| 4 free-text boxes × ≥1 min | ~4 min |
| ~23 other questions × ~22 s | ~8.5 min |
| **Draft total** | **~15 min** |

That is normal for a developer survey. Published ones run from a 12-13 minute median to about 30 minutes. It is also three times your budget.

No study sets an ideal survey length, so the five-minute cap is a constraint you chose, not a proven threshold. Hold it by measuring the median in the soft launch. Only write "about 5 minutes" in the invitation after you have measured it.

## 2. Re-ranking block

Answers 1-4 are still open, so this block is incomplete:

```
Answer 8 (one analyst, ~6 h, ~1,500 completes): open-text boxes cut before closed questions; paid ads deleted.
Answers 1, 2, 3, 4, 5, 7, 9, 10, 11: not given yet, so no other re-ranking applied.
```

## 3. Moves, biggest saving first

**A. Open text: 4 boxes become at most 1 (saves ~3 min, plus most of your analysis risk).**

- Cut all four "any other feedback?" boxes. None names a decision, and each costs the respondent a minute or more.
- Keep one optional box tied to a decision: "Describe the last time X got in your way." Place it before the demographics.
- Check the box against your hours. Fill rate is an assumption (~35%, so ~500 answers from 1,500 completes). Time yourself coding 50 answers. If 50 take 15 minutes, 500 answers cost ~2.5 hours, and four boxes would cost ~10 hours against your 6.
- To fit a ~1.5 h cap, show the box to a random third of respondents. That gives ~170 answers (about 50 minutes at that rate) and also shortens most people's survey.
- Never publish raw open text. Publish coded themes only.

**B. The grid: 30 rows × 4 levels becomes one small block (saves ~2 min).**

1. Put the grid through the decision table first. Ask which of the four levels any decision actually uses. If only "use regularly" matters, the grid becomes one multi-select.
2. Cut the tool list to what decisions or `publish` headlines need. Keep it to about 12 or fewer, in randomised order, so it fits one phone screen.
3. If you really need the awareness ladder, each respondent sees a random 10 tools out of the shortlist. Three random blocks give each tool ~500 respondents, and ten rows cost ~1 minute.
   - This is my suggestion, not a rule from the skill.
   - Caption each tool's chart with its own n.
   - Rewrite "use regularly" as "used in the last 3 months", with a concrete window.
4. Fix the grid's cleaning rule now: straight-lined grids are dropped, and you report how many.
5. Complete the survey on a phone. Grids fail first there.

**C. Routing (saves ~1 min on the average path).**

- Show a section only to people it applies to. "Everyone, no branching" is the opposite of the rule.
- Ask a qualifier first, then send each person only to the sections that fit their answer.
- Budget the longest routed path at 5 minutes. Then the median lands under it.

**D. The decision table on the remaining ~23 questions (saves ~2-3 min).**

Every question needs a decision, an owner, and an answer that would change the decision. Cut a question when it has no row. Also cut any question that:

- telemetry already answers (version, OS, region),
- nobody will act on either way, or
- your sample cannot answer.

Mark any question that exists only for a headline as `publish`. These compete for the same minutes. Keep your original number beside every kept, merged or rewritten question so the author can trace each one. Each cut should read "no decision named" or "telemetry answers this", never "bad question".

## 4. Target budget (longest path)

| Block | Est. seconds |
|---|---|
| Privacy notice + age gate | 15 |
| Qualifier + role | 25 |
| 6 core decision questions × ~22 s | 133 |
| Tool block (random 10 rows) | 45 |
| 1 optional open box (shown to a third) | 45 |
| 2 optional demographics, broad bands, last | 15 |
| **Total** | **~280 s (4:40)** |

- That is ~12 questions with a thin margin. If the soft launch comes in over 5 minutes, drop a core question before touching the tool block.
- Put decision-feeding questions early. Quality degrades with position.

## 5. Your six hours

| Task | Hours |
|---|---|
| Cleaning (qualifiers, speeders, straight-liners, duplicates, bots) | 1.0 |
| Analysis (distributions, not Likert means alone; source-channel cuts) | 2.0 |
| Open-text coding | ≤1.5 |
| Charts + methodology section | 1.5 |

- Skip paid ads. You don't have the hours to screen them for fraud.
- Set a minimum subgroup n before analysis, and hide subgroups below it. Merge or suppress any published cell under 10 respondents.
- Write the cleaning rules before fielding.

## 6. Test it before launch

1. An outside person reads every question and completes it on a phone.
2. Run five cognitive interviews if the date allows.
3. Soft launch to a small slice of one channel. Check median time, breakoff point and empty answers. Tag those responses `pilot`.
4. Re-price from the soft launch, then freeze the wording.

## 7. What I need from you

Send these and I'll produce the full decision table (kept questions and cuts, each with its reason) for you to validate:

1. The 28 questions, pasted with their numbers.
2. Which decisions the results feed, and who owns each one.
3. Whether results are published and quoted outside the team, such as in a report or sales deck.
4. The population (users, community members, the wider ecosystem) and the deadline.
5. Whether this is a one-off or the first of a yearly series.

Questions 2 and 3 matter most: if no decision owner and no publication plan exist, the skill recommends five user interviews instead of a survey.