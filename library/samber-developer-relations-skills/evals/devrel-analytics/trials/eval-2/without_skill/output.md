# Pulling GitHub Insights history for a 9-month retrospective

## The hard limit, stated up front

GitHub's Traffic panel (Views/unique visitors, Clones/unique cloners, top referrers, popular paths) is a **rolling 14-day window**, server-side, full stop. It always has been. There's no export, no archive, no "go back further" toggle — GitHub simply doesn't store it past 14 days, and no third party mirrors it either, because none of this is emitted as a public event. Since nobody has been capturing it, **the actual weekly visitor/clone history since March is gone and unrecoverable.** I'd rather tell you that now than hand you a chart with a gap silently smoothed over.

What you *can* do: pull the current 14-day snapshot as a "run rate today" data point, reconstruct a defensible 9-month trend from things GitHub (or others) genuinely did retain the whole time, and start capturing traffic properly so your next retro doesn't hit this wall again.

## 1. Grab what's left (last 14 days only)

UI: **Insights → Traffic** (requires push access — not public). Shows Views/uniques, Clones/uniques with a daily/weekly toggle, plus top-10 referrers and top-10 popular content.

API, for a clean CSV instead of screenshotting the chart:

```bash
gh api repos/OWNER/REPO/traffic/views?per=week   --jq '.views[]   | [.timestamp,.count,.uniques] | @csv'
gh api repos/OWNER/REPO/traffic/clones?per=week  --jq '.clones[]  | [.timestamp,.count,.uniques] | @csv'
gh api repos/OWNER/REPO/traffic/popular/referrers
gh api repos/OWNER/REPO/traffic/popular/paths
```

Label this in the deck as a snapshot, not a trend line — it's 14 days of a 9-month story.

## 2. Reconstruct the 9-month trend from data GitHub *did* keep

- **Stars, full history, exact timestamps** — the best visitor-interest proxy you have:
  ```bash
  gh api --paginate -H "Accept: application/vnd.github.star+json" \
    repos/OWNER/REPO/stargazers --jq '.[].starred_at'
  ```
  Bucket by ISO week → your weekly growth chart since day one.

- **Forks, same idea:**
  ```bash
  gh api --paginate repos/OWNER/REPO/forks --jq '.[].created_at'
  ```

- **Commit activity — this one's free, GitHub already retained it.** `stats/commit_activity` and `stats/participation` cover the trailing 52 weeks, which at 9 months old means your *entire* project life is already sitting there:
  ```bash
  gh api repos/OWNER/REPO/stats/commit_activity
  gh api repos/OWNER/REPO/stats/participation
  gh api repos/OWNER/REPO/stats/code_frequency
  ```
  (First call sometimes 202s while GitHub builds the cache — retry once.)

- **Issues/PRs opened, closed, time-to-first-response** — persistent objects, not telemetry, so full history is always there:
  ```bash
  gh issue list --repo OWNER/REPO --state all --json createdAt,closedAt --limit 1000
  gh pr list --repo OWNER/REPO --state all --json createdAt,closedAt,mergedAt --limit 1000
  ```

- **GH Archive** (gharchive.org, also queryable via BigQuery public dataset `githubarchive`) — every public WatchEvent/ForkEvent/IssuesEvent/PullRequestEvent/ReleaseEvent since 2011, independent of anything you exported. Good cross-check on the above and catches anything since-deleted. Won't help with clones or page views though — those were never public events, so they're not in there either.

- **If Kestrelbase ships to a package registry** (npm, PyPI, crates.io, Docker Hub…), check that first — registries often retain far more history than GitHub traffic does (`npm-stat.com`, `pypistats.org`, crates.io's downloads endpoint). That may end up being your cleanest "adoption over time" chart.

## 3. What else to grab while you're in Insights, for the investor deck

- **Dependency graph → Dependents** — current count of public repos/packages depending on you. Strong adoption signal, but it's a snapshot with no history either — screenshot it now, start tracking weekly going forward.
- **Contributor count & growth** — unique commit authors over time, signals community beyond the founding team (derivable from `stats/contributors`, which also covers full history, not just 52 weeks).
- **Release cadence + per-asset download counts** (`/releases` endpoint) — shows shipping velocity and pull-based adoption.
- **Issue/PR health metrics** — median time-to-first-response, median time-to-close, open vs. closed ratio. Investors read this as maintenance quality, not just growth.
- **Security posture** — Dependabot alerts resolved, any CVEs and time-to-patch. Governance signal.
- **License + CITATION.cff presence**, and Google Scholar citation count if the project has any academic pickup.
- **External surface** — backlinks (Ahrefs if you're already using it), HN/Reddit threads, awesome-list inclusions.

## 4. Fix it so this gap doesn't repeat next retro

Traffic data disappears every 14 days whether you look or not. **Set up a weekly scheduled job (GitHub Action or cron) that hits the four traffic endpoints and appends the results to a committed CSV or an external store (S3, a Sheet).** That's the only way to have continuous weekly history by the time you do the 18-month retro. Minimal shape:

```yaml
# .github/workflows/traffic-snapshot.yml
on:
  schedule:
    - cron: '0 6 * * 1'   # weekly, Monday
jobs:
  snapshot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          gh api repos/${{ github.repository }}/traffic/views   >> traffic/views.jsonl
          gh api repos/${{ github.repository }}/traffic/clones  >> traffic/clones.jsonl
          gh api repos/${{ github.repository }}/traffic/popular/referrers >> traffic/referrers-$(date +%F).json
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - run: |
          git config user.name "traffic-bot"
          git config user.email "actions@users.noreply.github.com"
          git add traffic/
          git commit -m "chore(traffic): weekly snapshot" || echo "nothing to commit"
          git push
```
**This commits data weekly** — put it in a private repo if you'd rather not expose raw traffic numbers publicly.