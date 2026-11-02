## `.github/workflows/stale.yml`

```yaml
name: Close stale issues

on:
  schedule:
    - cron: "30 1 * * *"   # daily; see note below on why this alone won't clear things in one weekend
  workflow_dispatch: {}     # lets you fire extra manual runs to grind through the backlog

permissions:
  issues: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}

          # Issues only for this pass — leave PRs untouched
          days-before-issue-stale: 60
          days-before-issue-close: 7
          days-before-pr-stale: -1
          days-before-pr-close: -1

          stale-issue-label: "stale"
          close-issue-reason: not_planned
          stale-issue-message: >
            Marked stale after 60 days of inactivity. Closes in 7 days if nothing
            changes — comment, remove the `stale` label, or reopen later if this
            is still relevant.
          close-issue-message: >
            Closed for inactivity. Reopen (or file a fresh issue with current
            details) if this is still a real problem.

          exempt-issue-labels: "security,confirmed,help-wanted,pinned"
          exempt-all-issue-milestones: true

          ascending: true           # hits the 2022 backlog first, not newest issues
          operations-per-run: 200   # default is 30 — nowhere near enough for 1,400 issues
          remove-stale-when-updated: true
```

## Two things in the plan that won't work as described

**⚠️ It will not clear anything out this weekend, by design.** `days-before-issue-close: 7` is GitHub's own "standard" — once an issue gets the `stale` label, it sits for 7 more days before actually closing. That gap is the whole point: it's the window people need to notice and respond. Set it to 0 or 1 if you want closures inside the weekend, but that guts the "people will reopen if it matters" safety net you're counting on — a same-day close leaves no real time to react. Standard settings mean: this weekend you mass-*label*, next week you mass-*close*.

**⚠️ `operations-per-run` throttles everything, default is 30.** Each mark-stale or close counts as one operation, capped per run. At the default, a scheduled run touches maybe 30 issues a day — you'd need ~47 days just for the first pass on 1,400 issues, before closures even start. I bumped it to 200 above; push higher only after watching one run for GitHub secondary-rate-limit errors (the action backs off, but very high values in a short window increase the odds of tripping them).

## To actually grind through it over a weekend

- Trigger `workflow_dispatch` manually every couple of hours Saturday/Sunday instead of relying on one daily cron — each run processes another `operations-per-run` batch.
- `ascending: true` means you're clearing the oldest (2022) issues first — the ones most likely to be genuinely dead — rather than shuffling recent ones.
- The four exempt labels cost nothing and cut real backlash risk: security reports and already-triaged (`confirmed`) issues going stale silently is the kind of thing that gets a project called out publicly. Drop them if you're confident there's nothing worth protecting in there.
- Run once with `debug-only: true` first if you want to see the exact list of issues that would be touched before it writes anything — worth doing once given the volume.