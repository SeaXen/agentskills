## The actual problem

Weekly-Friday-forever collapsed because it had zero slack built in. One contract job was enough to break it, and once one Friday was missed, the public promise turned from motivating into shameful — which is why five months passed instead of one skipped week and a comeback. The commitment design itself, not your discipline, caused the collapse. Fix the design, not your willpower, or January repeats September.

The "is it dead" perception is a separate, smaller problem, and it's fixable this week, not in January.

## Do this now, not in January

**Reply to the two issues today.** Cost: 10 minutes. This is the highest-leverage move available and it doesn't wait for a relaunch.

> Not dead — I went quiet, the project didn't. ~30 PRs merged since the last post; see the commit log. I overcommitted to weekly updates, missed one, went silent instead of just saying so. Restarting in January with a cadence I can actually keep. Sorry for leaving this hanging — thanks for checking rather than assuming.

**Post one honest "state of the project" comment or short post now**, separate from the January relaunch. Say what shipped, say what happened, say when you're back. This is a changelog-updates "breaking change announcement" move applied to trust: name what changed, name why, name the timeline, don't make people guess. Silence reads as abandonment; an honest gap explanation reads as a person with a life. Waiting until January to address it means three more months of "is this dead" issues.

## Redesign the cadence before you restart it

The old system: weekly, Friday, public, no exceptions defined. Every one of those four traits is a fragility point.

| Old trait | Failure mode | Fix |
|---|---|---|
| Weekly | No buffer for a bad week | Biweekly, or "Friday-ish" with a defined window |
| Public zero-miss streak | One miss = shame = avoidance = silence | Publicly define a skip protocol *in advance* |
| Written same-day | Contract work crowds out writing time first | Log changes as you merge, write from the log, not from memory |
| "More soon" as filler | Vague promise nobody can hold you to, including you | Never post a placeholder; skip the week instead |

Concretely:

1. **Pick biweekly over weekly.** Half the deadlines, same cumulative signal of activity, much more slack per post. You can always post more often when you have the bandwidth; you can't quietly downgrade a public weekly promise without it looking like decline.
2. **Define the skip protocol publicly, in the relaunch post itself**: "If a cadence post doesn't land, I'll post a one-line skip note instead of going silent — 'busy week, back next time' takes 30 seconds and costs nothing." This converts "miss = collapse" into "miss = a Tuesday." It's the single change most likely to prevent a repeat, because it removes the shame trigger that turned one missed Friday into five months.
3. **Log as you merge, not when you sit down to write.** Keep a running `NOTES.md` or draft changelog entry appended at PR-merge time (30 seconds per PR). The update post becomes "paste the log, add two sentences of color" instead of "reconstruct three weeks from memory under deadline pressure." This is the same mechanic as Keep a Changelog's `[Unreleased]` section — accumulate continuously, publish periodically.
4. **Batch a buffer before you go public again.** Write 2-3 posts before announcing the restart, so week one's post isn't written the night before under first-week pressure. Publish on the announced cadence from the buffer while you rebuild the merge-time logging habit.
5. **Decouple "project is alive" from "I wrote prose this week."** A terse bulleted list of merged PRs, pasted with minimal editing, still proves activity. Perfectionism on the writing is what makes each post expensive enough to skip when busy — lower the bar for what counts as a valid post.

## The relaunch post

Write this once the buffer (point 4 above) exists. Structure, borrowed from changelog/announcement conventions:

- **What happened**: one paragraph, no over-apologizing. "Committed to weekly, a contract job ate five months, I kept merging but stopped writing."
- **Proof of life**: the ~30 PRs, maybe three genuinely interesting ones called out by name.
- **What's changing**: biweekly, not weekly; skip notes instead of silence when life happens.
- **Start date**: a specific January date, not "early January."

Keep it under a page. This is the same honesty move as the issue replies, expanded slightly, published once instead of dribbled as comment replies.

## Guardrail for the next contract job

The thing that actually killed the first run wasn't the missed week — it was going silent *after* the missed week instead of posting a 10-second skip note. Everything above optimizes for that one moment: when life gets busy again, the system's default action is "post one line and move on," not "stay silent until it's too awkward to come back." That default is what makes this restart different from the first attempt.