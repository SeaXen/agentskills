## Turning on a stale bot for mapshard

Straight answer first, then the reason, because the reason changes what "standard 60-day" should actually mean here.

### ⚠️ The plan as stated will misfire

"60-day setting, run it across the whole repo, anything that matters gets reopened" is not a stale-bot config — it's backlog bankruptcy wearing a stale bot's clothes. Those are different tools with different rules, and running one as if it were the other produces the exact failure this policy area is designed to prevent: **a confirmed bug closed by a bot tells the reporter their evidence was worthless.** A raw idle-time sweep with no state filter doesn't distinguish "reporter went quiet" from "still open because nobody on your side ever replied" — on a queue this size (1,400 open, oldest since 2022), the second bucket is likely large, not an edge case. And the reopen-if-it-matters assumption is asymmetric in practice: someone who already got silence for years is far less likely to notice a bot closure and come back than they were to reply to a human in the first place.

The defensible version of "turn on the stale bot" restricts the sweep to **items waiting on the reporter**, exempts everything waiting on you, dry-runs before it closes anything for real, and never runs as a single unscheduled weekend blast against 1,400 issues (GitHub's stale action also rate-limits itself — `operations-per-run` caps what one run can touch, so "the whole repo this weekend" won't actually execute as one pass regardless).

### The config to ship

```yaml
# .github/workflows/stale.yml
name: Close issues awaiting reporter reply

on:
  schedule:
    - cron: '0 6 * * 1'  # weekly — not a one-time weekend run
  workflow_dispatch:      # lets you trigger it manually to check the queue

permissions:
  issues: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          debug-only: true   # keep true until you've read one full dry-run report

          # Scope: only issues already flagged as waiting on the reporter.
          # A confirmed bug, an unlabeled backlog item, or anything waiting
          # on a maintainer is never touched by this job.
          only-issue-labels: 'needs-info'
          exempt-issue-labels: 'confirmed,accepted,blocked,security,pinned'

          days-before-issue-stale: 30
          days-before-issue-close: 14
          stale-issue-label: 'stale'
          close-issue-label: 'closed:no-response'

          stale-issue-message: >
            This is waiting on information from the reporter and has had no
            reply in 30 days. It closes in 14 days without an update —
            comment with the missing detail and it reopens automatically.
          close-issue-message: >
            Closing since this sat in "waiting on reporter" for 44 days with
            no reply. Not a judgment on the report — comment here or link a
            new issue to this one and it gets another look.

          # Issues only. PRs get their own gate order, never the issue rules.
          days-before-pr-stale: -1
          days-before-pr-close: -1

          operations-per-run: 200
```

**The catch:** `only-issue-labels: needs-info` means this bot closes nothing until that label exists and is actually applied. If mapshard has no state taxonomy today, this workflow will run clean and touch zero issues — which is correct, not broken. It means the real blocker isn't the workflow file, it's that nobody has marked which of the 1,400 are waiting on the reporter versus waiting on you. Minimum label set to add first (from this skill's taxonomy):

- `needs-triage` — nobody's looked
- `needs-info` — waiting on the reporter *(this is what the bot sweeps)*
- `accepted` — real, will be worked
- `blocked` — waiting on something external

### If the real goal is "clear most of 1,400 by Monday"

Say so explicitly and use the tool built for that, once:

- **Backlog bankruptcy** — announce it, mass-close everything past a stated age with a message explaining why and how to reopen, and ship the new intake/labels/policy live the *same day*. It's legitimate exactly once as the opening move of a new policy — a maintainer who tried this without fixing intake found the backlog back to the same size six months later, because nothing changed about what caused the pileup.
- It is a **`gh issue list` / `gh issue close` scripted, announced, one-time pass** — not a recurring cron job, and not something you point a stale-bot config at and walk away from for a weekend.

### Before either one, run the baseline

```bash
gh issue list --state all --limit 2000 \
  --json number,title,state,createdAt,updatedAt,closedAt,labels,author,comments > issues.json
python3 scripts/triage-baseline.py issues.json --stale-days 60 --format json > baseline.json
```

This tells you the actual split — untriaged share, how much is genuinely idle versus quietly confirmed, inflow-vs-outflow — before you decide whether 60 days, `needs-info`-only, or a one-time bankruptcy pass is the right shape. A queue that's 80% dead usage questions needs a different move than one that's 80% real bugs nobody ever answered, and right now that split is unmeasured.