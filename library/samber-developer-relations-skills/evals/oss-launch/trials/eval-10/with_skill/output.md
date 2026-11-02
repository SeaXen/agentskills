**Skip the delete-and-repost. Skip the 5-channel blitz too. Data points at README/positioning, not title — and both moves break rules this skill sets.**

## Why not delete + repost tomorrow

- ❌ HN treats a resubmission of a dead thread as a duplicate and buries it. Deleting first does not reset that — "wait 24h and repost" is explicitly *not* a recovery window per the playbook, it is a duplicate.
- Sanctioned recovery path: one polite email to HN moderators asking for the second-chance pool. Not resubmission.
- Novelty is one-time per channel. Relaunching before fixing the real bottleneck spends that budget for nothing.
- Only 1-2 days in. Skill says read Day-1/Day-7/Day-30 windows and let Day-30 decide — judging "flat" this early, then reacting, is premature by its own method.

## Why not hit 5 channels same day

- Rule: one anchor, everything else staggered amplification. "Four simultaneous 'primary' posts produce four dead threads" — you'd be running five.
- r/javascript, r/node, Lobsters, Dev.to, PH same day = same blurb pressure across all, reads as spam, gets removed. Context must be rewritten per community.
- Product Hunt is a **secondary** channel for dev tooling, not co-primary with Lobsters/Reddit. For infra/tooling the anchor is a general tech aggregator (HN or Lobsters — pick one, not both).

## What the numbers actually say

Day-1 diagnosis table, mapped to your metrics:

| Signal | Your number | Reads as |
|---|---|---|
| Clicks (unique visitors) | 1,340 | Not few — traffic arrived fine |
| Stars / visitors | 38 / 1,340 = 2.8% | Weak, not catastrophic |
| Cloners / visitors | 7 / 1,340 = 0.5% | Very low — this is the real bottleneck |
| Downloads vs prior week | flat | No install follow-through |

Pattern matches **"clicks fine, stars/clones low" → the README lost the ten-second read.** Fix is restructuring the top of the README + adding a demo, not the headline.

⚠️ One gap before trusting this: 4 points / 1 comment rarely sustains 1,340 *direct* HN clicks — HN ranking decays fast on low early votes, so that thread likely fell off `/newest` within an hour or two. Some real share of those 1,340 probably came from elsewhere (Twitter, search, GitHub explore, a bot crawl). Pull the referrer breakdown before concluding anything about HN specifically — the traffic panel window is short-lived, so do this now, it's unrecoverable once it rolls off.

## Next 4 steps

1. **Check GitHub Insights → Traffic → Referring sites** now, before the window expires. Confirms how much of the 1,340 is actually HN.
2. Run the cold-run protocol yourself: fresh directory, follow only the README, log every point you had to guess. Each guess is a defect.
3. Fix the top of the README from what that cold run finds (concrete value line, quickstart, demo) — this is the row-2 fix, not a title rewrite.
4. Leave the HN thread up. Wait for Day-7 npm numbers before deciding this was a "wrong channel" problem (the only symptom that justifies relaunching elsewhere).

Title polish is fine to fold into the README fix later, but it's not the lever the data points at.

**Next: pull the referrer report right now — that's the only piece of this that's actually time-limited.**