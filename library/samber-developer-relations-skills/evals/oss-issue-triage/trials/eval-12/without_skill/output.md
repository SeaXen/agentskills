Straight answer to each ask, including where a number can't legitimately come from anywhere but your own data:

**1) Retention lost per additional day of first response — no fixed coefficient exists.**
There's no portable "X% retention lost per day" constant you can cite. It varies by project size, contributor type (first-timer vs. repeat), and issue complexity — treating it as a constant is exactly the kind of number that gets shot down in the first follow-up question. The only defensible version is one computed from nordvex's own history: bucket first-time contributors by the response latency they experienced on their *first* issue/PR (e.g. <24h, 1-2d, 3-5d, 6-10d, >10d), then measure what % of each bucket opened a second issue/PR within 90 days. That curve, built from your own tracker data, is your real number — and it's the one that survives scrutiny.

**2) 5 days → 3 days: % gain — depends entirely on #1, can't be answered independently.**
Once you have the real cohort curve, read off retention at the 3-day bucket and the 5-day bucket; the gain is the delta between those two points on *your* curve, not a generic percentage pulled from nowhere. Don't linearly interpolate between buckets you haven't measured — these curves are typically non-linear, with the steepest drop-off in the first 48 hours, so a flat "X% per day" rate would misrepresent your own data even after you have it.

**3) "3 minutes per issue" is not a standard figure.**
No such industry standard exists. Real triage time spans roughly 30 seconds (obvious duplicate/spam — close and label) to 15-20+ minutes (repro needed, ambiguous report, needs maintainer input); different projects report wildly different averages because "triage" itself isn't consistently defined. A flat 3-minute assumption is the single weakest point in the capacity model as it stands. Fix: time-sample 20-30 real triage actions (timestamp diff between issue-opened and first-label/response for a week of actual triage work), then report median + range and build low/median/high capacity scenarios — not one point estimate.

**4) Target untriaged % is a policy decision, not a lookup.**
Set it, don't source it. A reasonable, defensible starting target: 90-95% of open issues triaged (labeled + first response) within 48 hours, with under 5% sitting untriaged past 7 days. Anchor it to your own current baseline — measure what % is untriaged past 48h/7d today — so the target reads as "close this measured gap," not an imported "best practice."

**What this means for the deck.**
Items 1-3 aren't researched figures right now — there's no data source backing them (I was blocked from reading nordvex's own data for this answer, and no external standard exists for any of the three). Build the justification on four things you can actually produce in about a week:
- Current distribution of nordvex's time-to-first-response (you already have this in the issue tracker)
- A same-repo cohort retention-by-response-time curve (a few hours of scripting against the GitHub API)
- Time-sampled real triage duration, median + range, not a flat assumption
- Current-state capacity (issues/week × sampled minutes) vs. desired-state target (your policy target above) — the gap between the two is your headcount ask

That framing — "here's our measured baseline, here's the target, here's the gap" — holds up in the room. "We lose X% retention per day and it costs 3 minutes per issue, industry standard" invites exactly the question you can't currently answer: where did that number come from.