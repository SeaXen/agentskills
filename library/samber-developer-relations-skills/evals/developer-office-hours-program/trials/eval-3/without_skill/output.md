**Do this first (30 min):** count how many times the SDK init-order question showed up in the last 90 days. Check support tickets, Slack or Discord, GitHub issues and the two write-ups. That number is your strongest evidence, and the AMA hasn't been the thing surfacing it.

## Verdict

Don't kill it and don't go weekly. Pause the live format, keep the AMA, and run a 6-week redesign that has to produce docs changes.

## Why not the other options

- **"3 askers is the benchmark."** This is folklore. I know of no measured source for it, so label it a hypothesis and drop it as a target.
- **You have 3 data points (2, 1, 0).** With that few, any rate or average is noise. Compare the AMA to its own history, not to someone else's number.
- **Weekly.** It multiplies the load on one engineer by 4. Your sick-day failure already showed there's no backup, and 4x the sessions at about 1 asker each means 4x the empty Zooms.
- **YouTube views.** Views are a reach metric. They can't tell you whether anyone's problem got solved, and they only go up. Leadership gets a number, but nothing improves.
- **Kill.** The data says the format failed, not the idea. The repeated init-order question proves developers have questions that go unanswered.

## The real problem

The AMA has no path from question to fix. You have a live slot, a write-up a week later, and no docs changes. An AMA works when there's a crowd, and you don't have one yet.

## Plan: 6-week redesign

1. **Today to day 2: ship the init-order fix.** Write or rewrite the SDK init-order section in the docs. Estimate: 2 to 4 hours with the engineer's input. This is your first docs change and it will probably stop the repeat question.
2. **Week 1: move questions to async.** Open a standing question form, plus a thread in Slack, Discord or GitHub Discussions. Label it "Engineering AMA: submit anytime."
3. **Week 1: seed the queue yourself.** Pull the top 5 questions from tickets, community channels and sales calls. Don't wait for people to ask. Real asker counts will stay low at first, and seeded questions keep each session worth running.
4. **Week 2 onward: switch to a monthly written AMA.** Don't hold the live session. The engineer answers the top 3 to 5 questions in writing, or in a short recording if that's easier. A live Q&A stays optional, a 30-minute slot only if 5 or more questions are waiting.
5. **Every session: publish within 48 hours and name a docs owner.** The write-up ends with "Docs change: <link>" or "No change needed, because X."
6. **Name a backup answerer** so one sick day can't cancel a session again. A second engineer, or you with written answers they review.

## What to report instead of views

| Metric | Why | Threshold |
|---|---|---|
| Docs changes shipped per cycle (primary) | Shows the AMA does something | `baseline`: 0 now; target 1 or more per cycle |
| Init-order questions per month in tickets and community | Shows the docs fix worked | `baseline`: the count from your first step; flag a drop |
| Questions submitted before each cycle, seeded and organic tracked separately | Shows whether anyone engages | `baseline`: starts at 0 organic; read as a trend |
| Days from session to write-up | Ownership | Currently about 7; target 2 |
| Views, if you record | Reach only, always paired with the docs-changes row | No target |

## Kill rule

If after 2 cycles there's no docs change and no metric moved, stop the AMA. Write that rule into your proposal so stopping is a scheduled decision, not an argument.

## What to tell leadership

Send a short proposal:

- 3 sessions held, 3 data points. Average is about 1 asker. N is too small for a benchmark.
- The "3 askers" figure is unsourced folklore.
- Weekly cadence adds load without fixing the missing question-to-fix path.
- Proposed: a 6-week redesign, a docs change per cycle, and a stop rule.
- YouTube: record the init-order answer as a short video linked from the docs page. It's evergreen and it supports a real problem. Report its views as reach, always next to the docs-change count.

## What I can't tell from here

- How many people attend the Zoom besides the askers.
- Whether the repeat question comes from the AMA audience or from other channels.

Share those two and I'll tighten the plan.

**Next:** run the 90-day count of init-order questions and send me the number.