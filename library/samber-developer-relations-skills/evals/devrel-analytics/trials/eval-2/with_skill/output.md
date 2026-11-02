Snapshot today's 14-day traffic window right now — every day you wait, more of it ages out and is gone for good.

## 1. Bad news first: 9 months of visitor/clone history does not exist

GitHub's traffic endpoints (`views`, `clones`, `referrers`, `popular paths`) keep a rolling **14-day window only**, readable only by repo collaborators with write access — source: GitHub REST API "Metrics / Traffic" docs. Nobody exported it, so today you can see roughly the last 2 weeks. Everything before that is not archived anywhere — not in the API, not in GH Archive (that public event stream covers stars/forks/pushes/issues/PRs, never views or clones). No workaround recovers it. Say this plainly to investors rather than presenting a partial chart as if it were the full 9 months.

## 2. What partially substitutes for the missing period

These three are NOT rolling-window-limited — full history since repo creation is pullable today:

- **Stars per week** — `GET /repos/{owner}/{repo}/stargazers` with header `Accept: application/vnd.github.star+json` returns `starred_at` per stargazer, paginated back to day one. Bucket into weeks yourself.
- **Forks per week** — `GET /repos/{owner}/{repo}/forks?sort=oldest` returns `created_at` per fork, same full history.
- **Issues/PRs per week** — Issues/PR list API, full history, no window.

None of these are visitors or clones. Label them as separate series on the chart, never blended into a "traffic" number. Stars are also gameable and monotonic — report stars-*per-period*, never cumulative stars, if it goes in front of investors.

## 3. Recipe to start capturing views/clones/referrers going forward

Needs: a token (classic PAT, `repo` scope) belonging to someone with push access to the repo.

```bash
curl -H "Authorization: Bearer $GH_TOKEN" \
  https://api.github.com/repos/kestrelbase/<repo>/traffic/views?per=week

curl -H "Authorization: Bearer $GH_TOKEN" \
  https://api.github.com/repos/kestrelbase/<repo>/traffic/clones?per=week

curl -H "Authorization: Bearer $GH_TOKEN" \
  https://api.github.com/repos/kestrelbase/<repo>/traffic/popular/referrers

curl -H "Authorization: Bearer $GH_TOKEN" \
  https://api.github.com/repos/kestrelbase/<repo>/traffic/popular/paths
```

Run daily, not monthly — a monthly export loses half the 14-day window. Append each pull to your own store (a CSV committed to a private repo is enough at this scale). Example: a scheduled GitHub Action.

```yaml
# .github/workflows/traffic-snapshot.yml
on:
  schedule:
    - cron: "0 6 * * *"   # daily, 06:00 UTC
jobs:
  snapshot:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          DATE=$(date -u +%F)
          curl -sH "Authorization: Bearer ${{ secrets.TRAFFIC_TOKEN }}" \
            https://api.github.com/repos/${{ github.repository }}/traffic/views \
            > data/views-$DATE.json
          curl -sH "Authorization: Bearer ${{ secrets.TRAFFIC_TOKEN }}" \
            https://api.github.com/repos/${{ github.repository }}/traffic/clones \
            > data/clones-$DATE.json
          curl -sH "Authorization: Bearer ${{ secrets.TRAFFIC_TOKEN }}" \
            https://api.github.com/repos/${{ github.repository }}/traffic/popular/referrers \
            > data/referrers-$DATE.json
          curl -sH "Authorization: Bearer ${{ secrets.TRAFFIC_TOKEN }}" \
            https://api.github.com/repos/${{ github.repository }}/traffic/popular/paths \
            > data/paths-$DATE.json
      - run: git add data/ && git commit -m "chore: daily traffic snapshot" && git push
```

Name an owner for this job today. A cron job nobody owns breaks silently and you're back to a 14-day window six months from now.

## 4. What else to pull while you're in the API

- **First-time contributor count** — issues/PR API, filter by author's first contribution.
- **Time to first response** on issues/PRs — issue/PR timeline API.
- **Open-to-close ratio** — issues list API, state filter.
- **External PRs merged** — PR list, filter non-org authors.
- **Forks** (see above) — the one signal specific to sample/template repos too, if you have any.

## 5. Traps for the investor deck specifically

- **Clones ≠ people.** CI runs clone on every build. Report the raw number with that caveat attached, never as "N developers pulled the code."
- **Referrers are mostly stripped already.** Expect "(direct)" as the largest bucket even in a clean 14-day window — normal, not a tracking gap.
- **Never merge the pre-window (stars/forks) and post-window (views/clones) series into one line.** Different metrics, different meaning. Two labeled series, or two panels — not one blended "growth" line.

Next: pick who owns the daily snapshot job, then merge the Action above today — every day before it merges is another day of the 14-day window you can't get back.