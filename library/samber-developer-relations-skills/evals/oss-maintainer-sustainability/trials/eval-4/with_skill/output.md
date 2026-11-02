**Next action (20 min):** run the baseline below, then pin the announcement. Don't switch the bot on yet.

```bash
gh issue list --state all --limit 2000 \
  --json number,title,state,createdAt,updatedAt,closedAt,labels,author,comments > issues.json
python3 scripts/triage-baseline.py issues.json --stale-days 90
```

I could not run your interview, so I assumed the answers below. Correct any that are wrong:
- You want the same project with far fewer hours.
- You work solo.
- The top drains are hostile comments and the daily tagger.
- Issue inflow is unknown. I'll ask below.
- No security report path exists yet.

I did not run or test any config. Check input names against the current `actions/stale` README before you commit.

## Verdict on the plan

Don't ship it as described. Four problems:

1. **Silent bulk close is the named failure mode.** 500 closures with "closed as stale" read as contempt, and they confirm the "is it abandoned" comments.
2. **A 90-day idle rule can't tell stale from confirmed.** Bugs waiting on you would close, which tells reporters their evidence was worthless.
3. **It works once.** Without intake cuts, the backlog refills in about six months. This is a one-time reset, not a recurring bot.
4. **It doesn't touch your top drain.** Hostile comments and the daily tagger come first.

Two figures need correcting:
- Tidelift's 58–60% is maintainers who **quit or considered quitting**, not "experience burnout." The skill's findings file says no Tidelift report matches "59% burnout and 35% harassed," so drop the 35% and don't put either figure in public text.
- Your conclusion holds: overload is the base rate, not a flaw in you.

## Your budget in numbers

4 h × 60 × half on the tracker ÷ 15 min per reply = **8 first replies a week, about 32 a month**. The "half" and "15 min" are the skill's defaults, not measured, so replace them after one real session.

- **Published window:** a first reply within 30 days. A reply is not a promise of a fix.
- **Inflow check:** if new issues exceed about 32 a month, cut intake before you publish the window.
- **Bridge hours:** setup costs about 7 hours (my estimate), above your 4 h cap. Treat it as a dated bridge through **2026-11-07**, then hold 4 h a week.

## Sequence

Today is Fri 2026-10-23.

1. **Sat 10-24, about 4 h:**
   - Enable private vulnerability reporting and add `SECURITY.md`.
   - Add issue forms with blank issues disabled, and route questions to Discussions.
   - Commit the README status block.
   - Create the labels `confirmed`, `needs-info`, `keep-open` and `backlog-reset`.
2. **Sat 10-24, about 2 h:** hand-label the issues that must survive with `confirmed`.
   - The bot can't see reproductions, so you decide.
   - Use `gh issue list --search "sort:reactions-desc"` and `sort:comments-desc` for the top 40–60.
   - Add anything you ever replied to with a diagnosis.
3. **Sun 10-25:**
   - Run the workflow with `dry-run` on and read the list.
   - Pin the announcement.
   - Run it live to **label only**. No closing happens in this run.
4. **Sat 10-31:** run it again. Items still labelled and untouched get closed with the comment below.
5. **From 11-01:** enable the weekly `needs-info` sweep.
   - Intake cuts and this loop go live with the reset. That is what stops the backlog refilling.

## Config 1: one-time reset

Save as `.github/workflows/backlog-reset.yml`. It runs manually only.

```yaml
name: backlog-reset
on:
  workflow_dispatch:
    inputs:
      dry-run:
        description: "Log what would happen and change nothing"
        type: boolean
        default: true

permissions:
  issues: write
  pull-requests: write

jobs:
  reset:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          debug-only: ${{ inputs.dry-run }}
          # Issues only. PRs waiting on the maintainer are never touched.
          days-before-pr-stale: -1
          days-before-pr-close: -1
          days-before-issue-stale: 90
          # Run 1 labels. Run 2, a week later, closes whatever is still labelled.
          days-before-issue-close: 7
          stale-issue-label: backlog-reset
          # Empty: the pinned announcement is the warning, the label is the marker.
          stale-issue-message: ""
          close-issue-reason: not_planned
          exempt-issue-labels: "confirmed,keep-open,security,pinned,blocked"
          exempt-all-issue-milestones: true
          exempt-all-issue-assignees: true
          # Oldest first; 500 issues exceed the default of 30 operations per run.
          ascending: true
          operations-per-run: 600
          # A comment from the reporter removes the label (default behaviour).
          remove-stale-when-updated: true
          close-issue-message: >-
            Thanks for reporting this. I'm closing it as part of a one-time
            backlog reset (see the pinned announcement). This is not a verdict
            that the problem is invalid or fixed. Pennyroyal has one maintainer
            with about 4 hours a week, and I can't keep hundreds of old issues
            honest with that time. If this still affects you on a current
            version, comment with a minimal reproduction and the version number.
            I'll reopen it when I see it, which can take up to 30 days.
            Questions belong in Discussions, and security reports in SECURITY.md.
```

If you run it twice and an item is touched in between, `remove-stale-when-updated` strips the label and it survives.

## Config 2: ongoing sweep

Save as `.github/workflows/needs-info-sweep.yml`. It only touches issues where you asked the reporter a question.

```yaml
name: needs-info-sweep
on:
  schedule:
    - cron: "17 4 * * 1"
  workflow_dispatch:

permissions:
  issues: write

jobs:
  sweep:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          # Set to true for the first pass, read the log, then flip to false.
          debug-only: true
          only-issue-labels: needs-info
          exempt-issue-labels: "confirmed,security,pinned,blocked"
          days-before-pr-stale: -1
          days-before-pr-close: -1
          # Self-set clocks. Kubernetes closes at 20 days without a reporter reply.
          days-before-issue-stale: 21
          days-before-issue-close: 14
          stale-issue-label: stale-needs-info
          close-issue-reason: not_planned
          operations-per-run: 100
          stale-issue-message: >-
            I'm waiting on the information requested above. If there's no reply
            in 14 days this issue closes. A comment with the details keeps it open.
          close-issue-message: >-
            Closing because the requested information didn't arrive. Comment
            with a minimal reproduction and the version, and I'll reopen it.
```

Never add a rule that closes items waiting on you.

## Pinned announcement

Post it on Sat 10-24 and pin it. Then put its issue number in place of "pinned announcement" in the closing comment if you want a direct link.

```markdown
**Backlog reset: labelling on 2026-10-25, closing on 2026-10-31.**
I can't work through 620 open issues with the time I have. Issues older than
90 days with no activity and no confirmed reproduction get the label
`backlog-reset` now and close on 2026-10-31. Confirmed bugs stay open. If one
still matters to you, comment with a current reproduction and the version, and
the label comes off. Security reports belong in SECURITY.md, not here.
```

## README status block

I assumed the maintenance-only tier. Confirm or change it.

```markdown
## Project status

**Maintenance-only**

- Maintained by one person in their spare time, about 4 hours a week.
- Expect a first reply to issues within 30 days; many will wait longer. A reply is not a promise of a fix. Security reports: see SECURITY.md.
- In scope: bug fixes and compatibility with current runtimes. Not in scope: new formatting features and locales beyond the current set.
- Questions go to GitHub Discussions, not the issue tracker.
```

Fill the scope line with what you will actually decline. Feature requests then close by pointer, not debate.

## Hostile comments and the daily tagger

This is your top drain, so it comes before the sweep. Details belong to `developer-community-moderation`, which I did not load. This is the minimum.

- **For "abandoned or lazy" comments:** don't argue. The README block answers them. Hide the abusive ones as off-topic.
- **For the daily tagger, post once:** "Pennyroyal has one maintainer at about 4 hours a week. Repeated mentions don't speed up a reply, and further ones will be hidden. The status and response window are in the README."
- **If it continues:** hide, then block. One warning is enough.
- **For a flood:** GitHub's temporary interaction limits can restrict commenting to prior contributors.

## Two questions that change the plan

1. How many new issues arrive per month? Over about 32 means intake cuts get a bigger share of the weekend.
2. Who else can publish `pennyroyal` to npm? If the answer is nobody, you are the single key holder. That is a separate risk from the backlog, and I can plan it next.

## Review

- **2026-11-21:** re-read the ledger and check these:
  - Hours stayed at or under 4 a week.
  - Most new issues got their first reply within 30 days.
  - The README states a status.
  - A security path is named.
- **Earlier look:** if reopen requests exceed about 15 in the first week, widen the window publicly instead of working harder.