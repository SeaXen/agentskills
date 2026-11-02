# DevRel Q3 2026 Report for the CTO

**Prepared for:** CTO · **Period:** Q3 2026 · **Owner:** [name], DevRel

## Summary

- ✅ **Time to first successful API call fell from 22 to 14 minutes (median).** This is the metric DevRel most directly controls, and it improved.
- ⚠️ **SDK issue responsiveness missed its threshold.** 78% of issues were answered within 2 business days, against the 80% we agreed in January.
- ✅ **6 community feature requests shipped.**
- ℹ️ **Influenced pipeline was $260k.** This is shared credit with Sales, not sourced revenue (rule below).

**Decision requested:** [Fill in. Example: "Approve one extra triage rotation slot to close the 2-point responsiveness gap."]

## Metric sheet

| Metric | Result | Previous | Threshold | Status |
|---|---|---|---|---|
| Time to first successful API call (median) | 14 min | 22 min | [target agreed in January] | ✅ Improved by 8 min (36%) |
| SDK issues answered within 2 business days | 78% | [prev. quarter] | 80% (agreed in January) | ⚠️ 2 points under |
| Community feature requests shipped | 6 | [prev. quarter] | none (small count) | ℹ️ List below |
| Influenced pipeline | $260k | [prev. quarter] | none yet | ℹ️ Shared credit |

### 1. Time to first successful API call: 14 min (was 22)
- **Definition:** median minutes from signup to the first API call returning a 2xx response. [Confirm the exact events and data source.]
- **Why it matters:** it is the first-run experience in engineering terms, and docs, quickstarts and SDK fixes move it directly.
- **What drove the change:** [name the 1–2 changes, e.g. quickstart rewrite, SDK default fix]. Without a named cause, the CTO will ask.
- **Caveat:** a median hides the tail. Add the 90th percentile if you have it.
- **Next action:** [e.g. attack the remaining slowest step].

### 2. SDK issues answered within 2 business days: 78% (threshold 80%)
- **Definition:** share of new SDK issues that got a first human response within 2 business days. [State whether bot replies are excluded.]
- **Read:** we missed by 2 points. Say plainly what caused it ([e.g. release week, one person on leave]) and whether it was a burst or a trend.
- **Number of issues in the quarter:** [N]. With a small N, one or two issues move the percentage, so report the count next to the rate.
- **Next action:** [owner] to [specific fix] by [date].

### 3. Community feature requests shipped: 6
List all six, since the count is small enough to show:

| Request | Source (issue/Discord) | Shipped in | Requested by |
|---|---|---|---|
| [ ] | | | |

Add one line on how many were requested versus shipped, so the 6 has a denominator.

### 4. Influenced pipeline: $260k
- **Rule (written before the quarter):** an opportunity counts as influenced when a contact on the account [engaged with DevRel, e.g. attended an event, posted in the community, or opened a DevRel-owned asset] within [N]-day lookback before opportunity creation. [Fill in the actual rule agreed with Sales.]
- **Credit is shared with Sales and Marketing.** Do not call this "sourced" or "generated".
- **Lag:** enterprise cycles run 2–4 quarters, so most of this will not close this quarter.
- **Number of opportunities behind it:** [N]. If a single deal is more than half the total, say so.

## Two additions I left out of the main page

You said the page felt thin. Four metrics that each drive a decision is a stronger page than six where two are weak, so I did not pad it.

**Community sentiment score (average of Discord emoji reactions).** I would not put it in front of the CTO yet, for these reasons:
- Reactions are sparse and self-selected. People react to announcements, not to complaints, so the average skews positive.
- The same emoji means different things in different channels, so averaging them mixes unlike signals.
- It has no baseline, and the quarter-over-quarter change would be noise, which invites the question "what does a 4.1 mean?"
- It can be gamed once people know it is measured.
- It has no attached action. If it dropped 20%, nobody would know what to do differently.

If you want to keep it, track it quietly this quarter and mark it "baselining" in an appendix. Put it on the main page once you have three quarters of history and a defined rule for what counts. A stronger version is a sample of 20–30 threads read and coded by a person each quarter, which a CTO will trust more than an emoji average.

**Blog pageviews (180k).** This is a reach number, and the CTO's likely reply is "so what?" Two further problems: client-side analytics undercounts developer audiences badly (many block it), and a pageview total says nothing about whether anyone built something. If you include it, make it a context line, not a result:

> *Context: the blog drew 180k pageviews (client-side analytics, undercounts developer traffic). [N]% of readers continued to the docs, and [N] signups cite the blog as their source.*

Without the downstream ratio, I would cut it.

## Optional additions that are real signal

If you want a fuller page, these would actually help and use data you may already have:
- **Median first-response time on SDK issues**, as a companion to the 78% (the median shows how late the misses were).
- **Reopen rate on closed SDK issues**, as a counter-metric so fast answers are not rushed ones.
- **Self-reported "how did you hear about us"** at signup, to back up the influenced-pipeline number.

## Blind spots

- Influenced pipeline over-counts by construction and lags by 2–4 quarters.
- Time-to-first-call covers only developers who completed a call. Those who gave up are not in the median. [Add the drop-off rate if available.]
- [Anything else you cannot currently measure.]

## Next quarter

1. [Action for the responsiveness gap, owner, date]
2. [Action to cut time-to-first-call further]
3. [Start tracking sentiment and blog-to-docs ratio as baselines]

---

**Before sending, please fill in:** the previous-quarter values for metrics 2–4, the January target for metric 1, the six shipped requests, the cause of the responsiveness miss, the attribution rule wording, and the decision you want from the CTO. I did not invent any of these.