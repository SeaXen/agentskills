## Before you present this — two flags

**The "15% lift" stat.** I don't have a credible source for "star-history chart → +15% star conversion." It's a number that circulates in GitHub-growth-hacking content with no study behind it that I can find. Add the chart because it's a legitimate, cheap trust signal (shows the project is alive and growing) — not because "+15%" is a defensible number. Don't put that figure in front of leadership; if someone asks for the source, there isn't a good one.

**Stars alone won't prove the rewrite worked.** A before/after star count is confounded by anything else that happened in the same window — a HN/Reddit mention, a dependency bump pulling in traffic, a tweet, seasonality. If nothing else moved, the before/after number is fine as a headline. If anything did, log it now (see below) so you're not caught flat-footed if someone in the review asks "or was that the HN post?"

---

## Tracking plan

**Data to capture**

| Field | Source | Why |
|---|---|---|
| Star count at rewrite merge | Reconstructed from stargazer timestamps (GitHub doesn't store historical counts) | The "before" number |
| Star count daily since | GitHub API, `stargazers_count` | Trend + the "after" number |
| Concurrent promotion (posts, tweets, mentions) | Manual log | Confound-check |
| Traffic referrers (optional hedge) | Repo → Insights → Traffic (14-day window, resets weekly — pull it *now*) | Lets you say "growth came from README/search," not just "stars went up" |

**Assumption to fix if wrong:** I'm treating "last Tuesday" as **2026-09-15**. If you meant yesterday (2026-09-22), swap `REWRITE_DATE` below — everything else stays the same.

### Script: reconstruct before/after and build the chart

Needs `requests` and `matplotlib` (`pip install requests matplotlib`). Uses the unauthenticated GitHub API (60 req/hr) — set `GITHUB_TOKEN` if the repo has enough stargazers to need multiple pages.

```python
# star_tracking.py
# Reconstructs a before/after star count and renders a review-ready chart
# by walking the stargazers endpoint's `starred_at` timestamps — GitHub
# exposes no historical stargazers_count endpoint directly.
import csv
import os
from datetime import datetime, timezone

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import requests

REPO = "aubergine-systems/tinshed"
REWRITE_DATE = datetime(2026, 9, 15, tzinfo=timezone.utc)  # adjust if wrong
OUT_CSV = "tinshed_stars.csv"
OUT_PNG = "tinshed_star_history.png"

session = requests.Session()
session.headers["Accept"] = "application/vnd.github.star+json"
if token := os.environ.get("GITHUB_TOKEN"):
    session.headers["Authorization"] = f"Bearer {token}"


def fetch_stargazer_timestamps(repo: str) -> list[datetime]:
    timestamps = []
    url = f"https://api.github.com/repos/{repo}/stargazers"
    params = {"per_page": 100}
    while url:
        resp = session.get(url, params=params)
        resp.raise_for_status()
        for entry in resp.json():
            timestamps.append(
                datetime.strptime(entry["starred_at"], "%Y-%m-%dT%H:%M:%SZ").replace(
                    tzinfo=timezone.utc
                )
            )
        url = resp.links.get("next", {}).get("url")
        params = None  # pagination params are baked into the `next` url
    return sorted(timestamps)


def main() -> None:
    stars = fetch_stargazer_timestamps(REPO)
    before = sum(1 for t in stars if t <= REWRITE_DATE)
    after = len(stars)
    delta = after - before
    pct = (delta / before * 100) if before else float("inf")

    print(f"Before ({REWRITE_DATE.date()}): {before}")
    print(f"After  ({datetime.now(timezone.utc).date()}): {after}")
    print(f"Delta: +{delta} ({pct:.1f}%)")

    # writes a cumulative-count-by-day CSV for the review deck / re-plotting
    with open(OUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "cumulative_stars"])
        for i, t in enumerate(stars, start=1):
            writer.writerow([t.date().isoformat(), i])

    dates = [t for t in stars]
    counts = list(range(1, len(stars) + 1))

    fig, ax = plt.subplots(figsize=(9, 5), dpi=150)
    fig.patch.set_facecolor("#fcfcfb")
    ax.set_facecolor("#fcfcfb")

    ax.plot(dates, counts, color="#2a78d6", linewidth=2, solid_capstyle="round")
    ax.axvline(REWRITE_DATE, color="#eb6834", linewidth=1.5, linestyle="--")
    ax.annotate(
        "README rewrite",
        xy=(REWRITE_DATE, before),
        xytext=(8, 12),
        textcoords="offset points",
        color="#52514e",
        fontsize=9,
    )

    ax.set_title(f"{REPO} — star history", color="#0b0b0b", fontsize=13, loc="left")
    ax.grid(True, color="#e1e0d9", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#c3c2b7")
    ax.tick_params(colors="#898781", labelsize=9)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))

    fig.tight_layout()
    fig.savefig(OUT_PNG, facecolor=fig.get_facecolor())
    print(f"Wrote {OUT_CSV} and {OUT_PNG}")


if __name__ == "__main__":
    main()
```

Run it with:

```bash
GITHUB_TOKEN=ghp_xxx python star_tracking.py
```

**Run this once now** (captures "before" via reconstruction) and **again the morning of the review** (captures "after") — the script recomputes both every time, so re-running is cheap and always current. If you want a trend across the whole week rather than two snapshots, **schedule it daily** (cron or a GitHub Action) between now and the review; the CSV accumulates, and you can re-render the chart with the fuller trend the morning of.

### README star-history badge (the "put one in too" part)

Separate from the review chart above — this is the public, live one that sits in the repo itself:

```markdown
## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=aubergine-systems/tinshed&type=Date)](https://www.star-history.com/#aubergine-systems/tinshed&Date)
```

**Add this section to `README.md`** near the bottom. It has no way to annotate a specific date (no marker for "rewrite shipped here"), which is why the review deck needs the matplotlib version above instead — this badge is for public visitors, not for your leadership slide.

### Review summary template

Fill in from the script's printed output:

| | Value |
|---|---|
| Repo | aubergine-systems/tinshed |
| README rewrite shipped | 2026-09-15 |
| Stars before | *(script output)* |
| Stars now | *(script output)* |
| Delta | *(script output)* |
| Concurrent promotion in window | *(your log — none if you didn't post anywhere else)* |