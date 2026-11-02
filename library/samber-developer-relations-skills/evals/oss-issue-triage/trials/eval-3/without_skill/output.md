## Is the plan sound?

Mostly, with one change I'd push back on: **don't hard-close on first contact.** A blunt "older than 18 months → closed" pass on 2,100 issues will sweep up real, still-valid bugs that just never got triaged, and a single mass-close of that size on a public repo tends to get noticed (HN/Twitter "project closes 2000 issues without reading them"). The standard, much safer pattern (what k8s, VS Code, etc. use):

1. **Mark stale first** (label + comment), don't close yet.
2. **Wait a grace period** (30 days is typical).
3. **Close only if nobody objected** in that window.
4. **Exempt** anything labeled security/confirmed-bug/pinned, or manually flagged "don't touch."

This is barely more work than a hard close and buys you goodwill instead of backlash. The script below implements it, is idempotent (safe to re-run), and doesn't care how often you run it — so it satisfies "run it every January" literally, while I'd still recommend wiring it to run monthly via the included workflow so the backlog never gets to 2,100 again in the first place. Your call which cadence to keep; the code doesn't change either way.

One practical note: the *first* run against 2,100 issues will eat a lot of API calls (label lookup + comment + patch, plus one events-lookup per already-stale issue on later runs) and will likely hit GitHub's hourly rate limit — the script sleeps and resumes automatically, but budget ~1–2 hours for the initial pass, not seconds.

---

## The messages

**Posted when an issue is flagged stale:**

> This issue has been open for 18+ months with no recent activity. As part of fernweb's regular triage, it's being flagged stale to keep the tracker useful for finding problems that are actually active.
>
> If this is still relevant — reproducible, still wanted, still blocking you — leave a comment and the stale label will come off, no other action needed.
>
> Without activity, this will close automatically in 30 days. That's a housekeeping step, not a verdict on the report. Closed issues can always be reopened.

**Posted at the actual close, 30 days later if nothing changed:**

> Closing after 30 days of inactivity following the stale notice above, as part of fernweb's periodic issue triage.
>
> This isn't a judgment that the report was wrong — just that we have no evidence it's still current. If you're hitting this on a recent fernweb version, open a fresh issue (or comment here) with repro steps and version info and we'll take another look.

---

## The script

`scripts/close_stale_issues.py`:

```python
#!/usr/bin/env python3
"""Two-phase issue triage: mark old open issues stale, then close them after a
grace period if nothing pushes back.

Idempotent and cadence-agnostic: every decision is made from stored timestamps
on GitHub, not from when this script last ran, so it's safe whether it's
invoked manually once a year or on a monthly schedule.

Usage:
    GITHUB_TOKEN=... python scripts/close_stale_issues.py --repo fernweb/fernweb            # dry run
    GITHUB_TOKEN=... python scripts/close_stale_issues.py --repo fernweb/fernweb --live      # mutates

Requires: pip install requests
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from datetime import datetime, timedelta, timezone

import requests

API = "https://api.github.com"

STALE_AFTER_DAYS = 18 * 30          # "older than 18 months" with no activity
CLOSE_AFTER_STALE_DAYS = 30         # grace period once labeled stale
STALE_LABEL = "stale"
# Anything with one of these labels is skipped entirely. "no-stale" is an
# explicit maintainer opt-out for a single issue that doesn't fit the others.
EXEMPT_LABELS = {"security", "pinned", "no-stale", "help-wanted", "bug:confirmed"}
MAX_ACTIONS_PER_RUN = 500           # cap writes per invocation; rerun to continue
REQUEST_DELAY_SECONDS = 1.0         # pace writes to stay under secondary rate limits
# Our own labeling call bumps the issue's updated_at too. Without this buffer,
# every freshly-stale issue would look like "someone just responded" on the
# very next run and never close.
STALE_UPDATE_BUFFER = timedelta(minutes=5)

STALE_COMMENT = """This issue has been open for 18+ months with no recent activity. As part of fernweb's regular triage, it's being flagged stale to keep the tracker useful for finding problems that are actually active.

If this is still relevant — reproducible, still wanted, still blocking you — leave a comment and the stale label will come off, no other action needed.

Without activity, this will close automatically in 30 days. That's a housekeeping step, not a verdict on the report. Closed issues can always be reopened."""

CLOSE_COMMENT = """Closing after 30 days of inactivity following the stale notice above, as part of fernweb's periodic issue triage.

This isn't a judgment that the report was wrong — just that we have no evidence it's still current. If you're hitting this on a recent fernweb version, open a fresh issue (or comment here) with repro steps and version info and we'll take another look."""


def gh_session(token: str) -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    return s


def _check_rate_limit(resp: requests.Response) -> None:
    if resp.headers.get("X-RateLimit-Remaining") == "0":
        reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
        wait = max(reset - time.time(), 0) + 1
        print(f"Rate limit hit, sleeping {wait:.0f}s", file=sys.stderr)
        time.sleep(wait)


def paginated_get(session: requests.Session, url: str, params: dict | None = None):
    params = dict(params or {})
    params.setdefault("per_page", 100)
    while url:
        resp = session.get(url, params=params)
        _check_rate_limit(resp)
        resp.raise_for_status()
        yield from resp.json()
        url = resp.links.get("next", {}).get("url")
        params = None  # the "next" URL already carries the query string


def ensure_label_exists(session: requests.Session, repo: str, live: bool) -> None:
    resp = session.get(f"{API}/repos/{repo}/labels/{STALE_LABEL}")
    if resp.status_code == 404 and live:
        session.post(f"{API}/repos/{repo}/labels", json={
            "name": STALE_LABEL,
            "color": "ededed",
            "description": "No activity for 18+ months; closes after a grace period unless someone responds.",
        })


def fetch_open_issues(session: requests.Session, repo: str):
    url = f"{API}/repos/{repo}/issues"
    for item in paginated_get(session, url, {"state": "open", "sort": "updated", "direction": "asc"}):
        if "pull_request" in item:
            continue  # this endpoint returns PRs too; skip them
        yield item


def stale_label_added_at(session: requests.Session, repo: str, number: int) -> datetime | None:
    latest = None
    for event in paginated_get(session, f"{API}/repos/{repo}/issues/{number}/events"):
        if event.get("event") == "labeled" and event.get("label", {}).get("name") == STALE_LABEL:
            latest = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return latest


def mark_stale(session: requests.Session, repo: str, issue: dict, live: bool) -> None:
    number = issue["number"]
    print(f"[stale]  #{number} {issue['title'][:60]!r}")
    if not live:
        return
    session.post(f"{API}/repos/{repo}/issues/{number}/comments", json={"body": STALE_COMMENT})
    labels = [l["name"] for l in issue["labels"]] + [STALE_LABEL]
    session.patch(f"{API}/repos/{repo}/issues/{number}", json={"labels": labels})
    time.sleep(REQUEST_DELAY_SECONDS)


def close_issue(session: requests.Session, repo: str, issue: dict, live: bool) -> None:
    number = issue["number"]
    print(f"[close]  #{number} {issue['title'][:60]!r}")
    if not live:
        return
    session.post(f"{API}/repos/{repo}/issues/{number}/comments", json={"body": CLOSE_COMMENT})
    session.patch(f"{API}/repos/{repo}/issues/{number}", json={"state": "closed", "state_reason": "not_planned"})
    time.sleep(REQUEST_DELAY_SECONDS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="owner/name, e.g. fernweb/fernweb")
    parser.add_argument("--live", action="store_true", help="actually write to GitHub; default is dry-run")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        sys.exit("GITHUB_TOKEN env var required")

    session = gh_session(token)
    ensure_label_exists(session, args.repo, args.live)

    now = datetime.now(timezone.utc)
    actions = 0

    for issue in fetch_open_issues(session, args.repo):
        if actions >= MAX_ACTIONS_PER_RUN:
            print(f"Hit MAX_ACTIONS_PER_RUN={MAX_ACTIONS_PER_RUN} — rerun to continue.")
            break

        labels = {l["name"] for l in issue["labels"]}
        if labels & EXEMPT_LABELS:
            continue

        updated_at = datetime.strptime(issue["updated_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

        if STALE_LABEL in labels:
            stale_since = stale_label_added_at(session, args.repo, issue["number"])
            if stale_since is None:
                continue
            if updated_at > stale_since + STALE_UPDATE_BUFFER:
                continue  # someone responded after the stale notice — leave it
            if (now - stale_since).days >= CLOSE_AFTER_STALE_DAYS:
                close_issue(session, args.repo, issue, args.live)
                actions += 1
        else:
            age_days = (now - updated_at).days
            if age_days >= STALE_AFTER_DAYS:
                mark_stale(session, args.repo, issue, args.live)
                actions += 1


if __name__ == "__main__":
    main()
```

## Automating "every January"

`.github/workflows/issue-triage.yml`:

```yaml
name: issue-triage
on:
  schedule:
    - cron: "0 9 1 1 *"    # 09:00 UTC, Jan 1st — matches your stated cadence
  workflow_dispatch: {}     # lets you trigger extra runs manually, e.g. to drain the first backlog

permissions:
  issues: write

jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install requests
      - run: python scripts/close_stale_issues.py --repo ${{ github.repository }} --live
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

`secrets.GITHUB_TOKEN` (the Actions-provided token, not a personal PAT) already has issues:write once the `permissions:` block above is set, so there's no token to create or rotate.

If you want the backlog to genuinely never reaccumulate rather than just getting an annual purge, change the cron to `"0 9 1 * *"` (monthly) — the script's logic doesn't change, it just processes whatever's eligible each time, in smaller, less noticeable batches.

**Rolling out on the current 2,100 issues:** first run only marks things stale (nothing closes same-day). Either wait 30 days for the next scheduled run to close the survivors, or trigger `workflow_dispatch` again after the grace period. If you'd rather skip the grace period for this one-time backlog clear and close immediately, set `CLOSE_AFTER_STALE_DAYS = 0` for that single run — but that's the blanket-close behavior I'd advise against for a repo this size.