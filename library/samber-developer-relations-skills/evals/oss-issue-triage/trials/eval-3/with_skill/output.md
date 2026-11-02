## Short answer: no — for two separate reasons, not one

**1. "Older than 18 months" closes the wrong things, not just the stale ones.**
An age filter with no state check catches confirmed bugs nobody staffed, accepted feature requests waiting on a maintainer, and blocked items waiting on an upstream dependency — exactly as hard as it catches genuinely abandoned questions. The skill's defensible line: *auto-close only items waiting on the reporter; never one waiting on the maintainers* — a confirmed bug closed by a bot tells the reporter their evidence was worthless. Age alone can't tell those apart; state can.

**2. Repeating it every January is the documented failure mode, not a fix.**
Mass-closing everything past a threshold ("backlog bankruptcy") is legitimate **exactly once**, as the opening move of a *new* policy — paired with that policy and a new intake going live the same day. A maintainer who tried this on a six-month cadence reported: "it works once," then found the backlog back in the same state, because the underlying issue — no lifecycle rule for issues — was never fixed by the closure itself. An annual sweep is that same mistake on a longer clock: it resets the count once a year while inflow keeps outpacing throughput the other eleven months. It also can't work without capacity numbers I don't have for fernweb (triagers, hours/week) — those determine whether the queue can even shrink; no closing cadence substitutes for that arithmetic.

What actually holds long-term: **one bankruptcy pass now** (paired with the new policy) **+ a permanent, state-restricted sweep that runs continuously**, not annually.

---

## The two messages

**A — one-time bankruptcy pass (send once, this run only):**

```
This issue is being closed as part of a one-time reset of fernweb's backlog.

Starting today we're running a new triage process — see CONTRIBUTING.md#triage.
Clearing years of issues that accumulated with no working process is the opening
move, not a judgment that this report was wrong, low-value, or unwanted.

If this still applies to a current fernweb release, reopen it — no justification
needed. Once reopened it goes through the new intake and gets a real first response.
```

**B — permanent sweep, waiting-on-reporter items only (this is what should run indefinitely, not once a year):**

```
Closing this — we asked for {missing info} on {warn_date} and haven't heard back.

This isn't a judgment on the report. Reopen any time you have the info and it
picks up where it left off. If you reopen without it, we'll ask again before
it can move further.
```

Both name a reason and say how to reopen, per the skill's closing-policy template — a close with no reopen path is what makes maintainers look unreachable rather than just slow.

---

## The scripts

### 1. One-time bankruptcy pass

Dry-run by default, logs every candidate before touching anything, defaults to excluding states you'd regret closing in bulk (adjust the label names to fernweb's actual taxonomy — if fernweb has no state labels at all yet, that's worth fixing before this runs, since "everything's untriaged" and "everything's confirmed" need opposite defaults).

```python
#!/usr/bin/env python3
"""One-time backlog-bankruptcy close for fernweb. Run once, paired with the
new triage policy going live the same day. Not a recurring job -- see the
actions/stale config below for the permanent sweep."""

import argparse
import json
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone

REPO = "fernweb/fernweb"  # set to the real owner/repo
CLOSE_MESSAGE = open("bankruptcy-message.txt").read()

# Never bulk-close these regardless of age -- states waiting on maintainers,
# not on the reporter.
EXEMPT_LABELS = {"accepted", "needs-owner", "blocked", "security", "pinned"}

def list_candidates(cutoff_iso):
    out = subprocess.run(
        ["gh", "issue", "list", "--repo", REPO, "--state", "open",
         "--search", f"created:<{cutoff_iso}", "--limit", "5000",
         "--json", "number,title,createdAt,labels"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--months", type=int, default=18)
    p.add_argument("--live", action="store_true",
                    help="actually close issues; omit for dry-run")
    p.add_argument("--batch-sleep", type=float, default=2.0,
                    help="seconds between closes, avoids a notification storm")
    args = p.parse_args()

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.months * 30)
    candidates = list_candidates(cutoff.date().isoformat())

    to_close, skipped = [], []
    for issue in candidates:
        labels = {l["name"] for l in issue.get("labels", [])}
        (skipped if labels & EXEMPT_LABELS else to_close).append(issue)

    print(f"{len(candidates)} issues older than {args.months} months")
    print(f"{len(skipped)} exempt (labels: {EXEMPT_LABELS}) -- left open")
    print(f"{len(to_close)} candidates for closing")

    with open("bankruptcy-closed.log", "w") as log:
        for issue in to_close:
            num = issue["number"]
            print(f"{'CLOSE' if args.live else 'WOULD CLOSE'} #{num}  {issue['title'][:70]}")
            log.write(f"{num}\t{issue['createdAt']}\t{issue['title']}\n")
            if args.live:
                subprocess.run(
                    ["gh", "issue", "close", str(num), "--repo", REPO,
                     "--comment", CLOSE_MESSAGE],
                    check=True,
                )
                time.sleep(args.batch_sleep)

    if not args.live:
        print("\nDry run only. Re-run with --live once this list looks right.")

if __name__ == "__main__":
    sys.exit(main())
```

**Run it dry first, read `bankruptcy-closed.log` in full, then `--live`:**
```bash
python3 bankruptcy_close.py --months 18
python3 bankruptcy_close.py --months 18 --live
```

### 2. Permanent replacement for "every January" — a continuous, state-restricted sweep

This is the actual fix for "it comes back in six months": don't wait a year and re-amnesty, close the *specific* items waiting on a silent reporter as they age past a short, named clock — same mechanism every week, forever, with no annual event needed.

```yaml
# .github/workflows/stale.yml
name: Stale sweep
on:
  schedule:
    - cron: "0 6 * * *"
permissions:
  issues: write
jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          only-labels: "needs-info"          # never touches anything else
          exempt-issue-labels: "accepted,needs-owner,blocked,security,pinned"
          days-before-stale: 14
          days-before-close: 14
          stale-issue-label: "closing-soon"
          close-issue-message: |
            Closing this -- we asked for missing info and haven't heard back
            in 4 weeks. Reopen any time you have it; no justification needed.
          debug-only: true                    # flip to false only after reading a dry run
```

Run one cycle with `debug-only: true`, read the run log for what it *would* close, then flip the flag. This is the loop that replaces "every January": items only enter it once a triager applies `needs-info`, so it never touches a confirmed bug or an accepted feature request regardless of age.

---

## Still missing before this is a real policy, not just a script

I don't have fernweb's capacity numbers (triagers, hours/week) or the actual label taxonomy in use — both gate the design per the skill:

- Without capacity, I can't tell you whether 2,100 open issues is even a backlog problem or an inflow problem — that changes which lever (cut intake / add triagers / shorten the promise) actually closes the gap, and the annual-close instinct usually means nobody has run this arithmetic yet.
- If fernweb has no `needs-info`/waiting-on-reporter state today, the permanent sweep above has nothing to act on until issues start getting labeled — that's a triage-workflow gap, not a script gap.

Run `triage-baseline.py` against a real export before the bankruptcy pass — it'll tell you what share of those 2,100 is actually untriaged vs. confirmed-but-unstaffed, which changes what "closing everything older than 18 months" would actually be discarding.