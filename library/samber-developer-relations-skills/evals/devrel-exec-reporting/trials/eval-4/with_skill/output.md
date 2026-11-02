# Board slide: DevRel provisional report, ready for Monday

**Your numbers are strong enough without the "700k developers" figure, and I left it out.** Downloads count installs, not people. CI runs, mirrors and re-installs inflate them, and one developer can appear on npm and PyPI. One director asking "700k of what?" would discount every other number on the slide. The slide below keeps all your numbers and labels each one for what it is.

## Assumptions (please confirm)

1. The board has no stated DevRel goal, so I used a three-number layout with no goal ledger. Give me the goal in the board's words and I will rebuild the table around it.
2. The framework doesn't exist, and the deadline is under four weeks. So the slide is **provisional**, claims no attribution, and asks the board to approve a framework.
3. "18% of 1,150 signups" means 18% of all signups, about 207 people. If it means 18% of the people who answered, change the table's "of 1,150" to "n=<respondents>" and say what share answered.
4. All figures cover "last month" or "to date" as you gave them. I assumed no prior-period history. Pull the history before Monday (see "To pull before Monday").
5. Program cost and whether salaries are in or out are unknown, so those are placeholders.
6. Dates in the next-period commitments are proposals.

## The slide

```markdown
# DevRel - Q4 2026 - for the Board
Provisional: no agreed metric framework. Attribution: none claimed.

DevRel reaches developers at scale and has one early outcome signal; the program has no
agreed outcome metric yet.
Decision asked: approve building a metric framework with a written attribution rule,
by Thu 5 November 2026.

## Results table

| Board question        | Metric                                          | This period                                   | Baseline / threshold  | Status            | Label                          |
| --------------------- | ----------------------------------------------- | --------------------------------------------- | --------------------- | ----------------- | ------------------------------ |
| Do developers adopt?  | Package downloads, last month (not developers)  | 700k (npm 410k + PyPI 290k)                   | none yet, pulling     | none (baselining) | measured (downloads, not people)|
| Does DevRel feed growth? | Signups naming a talk, blog or community     | 18% of 1,150 signups, about 207               | none yet              | none (baselining) | self-reported                  |
| Is attention building?| GitHub stars, cumulative                        | 14.2k                                         | none yet, pulling     | none (baselining) | measured (cumulative)          |

## Leading indicators carrying slow outcomes

| Lagging outcome                     | Leading indicator                  | Expected lag | Pull-through so far          | Label |
| ----------------------------------- | ---------------------------------- | ------------ | ---------------------------- | ----- |
| Pipeline, revenue, retention        | none in a framework yet            | unknown      | pending, next read <date>    | n/a   |

No business outcome is claimed. Choosing the leading indicators is part of the framework
decision below.

## What did not work

No metric missed a threshold this period, because no thresholds exist yet.
Dropped since last time: none (first report).
Known weakness: 18% leaves 82% of signups unexplained by this question, and the answer
is volunteered.

## Cost per outcome

Program cost <amount> (salaries <in / out>). Cost per outcome: not computed, because
no outcome is attributed to DevRel yet.

## Decision asked

Approve a metric framework. Options: (A) approve it now, with first read in <month>;
(B) keep reporting reach numbers only. Recommendation: A, because without it each
future report repeats this one and the program has nothing to defend at budget time.
Needed by Thu 5 November 2026.

## Next period (proposed commitments)

1. Framework draft with attribution rule and baselines - by <date>.
2. Four-quarter history for downloads, stars and signup source - by <date>.
3. First framework read - <date>.

---

Appendix
- Definitions: downloads = registry-reported install counts, include CI and mirrors.
  Signup source = free-text-free "how did you hear about us" form question.
- Attribution rule: none claimed. Self-reported source is a signal, not credit.
- Blind spots: podcasts, word of mouth and hallway conversations show up only if
  the signup form names them. Discord members are a cumulative total, not active members.
- Activity: 9 meetups. Discord 6,800 members total.
```

## Why it is built this way

- **Downloads are shown as 410k + 290k, never as developers.** Both are the same unit, downloads, so the 700k total is legitimate. "Developers" is not.
- **The 18% is labelled self-reported.** It is the only number that links DevRel to growth, and the label protects it. I wrote "named a talk, blog or community", not "came from" or "generated". No causal verb appears.
- **Stars and Discord are cumulative totals with no baseline.** Stars stay on the slide as a measured attention row. Discord and the 9 meetups go to the appendix, where activity counts belong.
- **The slide shows three numbers, as a board expects.** Meetups are an activity log. They answer "were you busy", not "what did it move".
- **There is no ROI multiple and no revenue language.** You have no pipeline data, and a multiple would be unsupportable.
- **There is a "What did not work" row.** A page with no misses reads as filtered.
- **The ask is the framework.** With no agreed metrics, approving one is the only decision the numbers support.

## To pull before Monday (about 2 hours)

1. **Four quarters of history** for npm and PyPI downloads, GitHub stars and the signup-source answer. A board reads trend against your own history, and history turns "baselining" into real baselines. If the 18% was higher or lower last quarter, add a column.
2. **Respondent count** for the signup question, so the 18% has a real n.
3. **Program cost, and whether salaries are in or out.**
4. **A one-line board goal**, if one exists.

Send me those four and I will finalize the slide with trend and cost.