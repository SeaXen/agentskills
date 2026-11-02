# Readout draft: storage rewrite post

## Short answer for your VP

1. **Pipeline generated:** I can't give you a number from pageviews. Pageviews say nothing about pipeline. You need the pipeline attributed to those 22,000 visits, and you have to pull it from your CRM or analytics.
2. **Read-through target:** There is no credible industry benchmark for read-through rate. Don't present one. Give her a target derived from your own baseline instead.

## 1. Pipeline: how to get a defensible number

Pull these from your CRM and analytics. Use the same 30-day window as the pageviews, plus a lookback for deals that touched the post.

| Step | Metric | Source |
|---|---|---|
| 1 | Pageviews (22,000) and unique visitors | Web analytics |
| 2 | Signups, demo requests, or other conversions that started on the post, or whose first or any touch was the post | Analytics, signup form source |
| 3 | Of those, accounts that became qualified leads or opportunities | CRM |
| 4 | Pipeline $ on those opportunities | CRM |

Report two figures, labeled separately:

- **Sourced:** the post was the first touch and the opportunity was created after it.
- **Influenced:** the post was one touch among several in the deal's history, within a fixed lookback such as 90 days.

Fix the lookback window and the attribution rule before you pull the numbers. Don't choose them after seeing the result.

**If the pipeline number is small or zero:** say so, and say why. A technical post on a storage rewrite attracts engineers, and many of them aren't buyers. Pageviews also include bots, repeat readers and people who arrived from aggregators. Traffic that large from Hacker News or Reddit usually converts at a very low rate. Don't backfill a number with an assumed conversion rate. If attribution isn't instrumented, report that as a gap. The honest line is: "22,000 views, N signups, $X attributed pipeline. The post was not instrumented to capture more."

## 2. Read-through rate: why there's no benchmark

**Definition problem.** "Read-through rate" has no standard definition. It could mean scroll depth, time on page, finishing the article, or clicking through to a next page. Each tool defines it differently, so a benchmark from one source doesn't compare to another. Any single "industry average" figure you find is likely a vendor blog stat with unclear methodology. It would not hold up if she asked where it came from.

**Context problem.** Even with a clear definition, a general content benchmark wouldn't fit. Deep technical posts read differently from marketing posts, and a spike from a link aggregator reads differently from search traffic.

**What to give her instead:**

1. State your definition. For example, "reached 75% scroll depth with at least 2 minutes on page", measured in your analytics tool.
2. Measure it for this post and for your last 5 to 10 posts. Report the median and range.
3. Set next quarter's target relative to that baseline. For example: "hold the median, and raise the lowest-quartile posts toward it", or "+X points on posts over N words".
4. Segment by traffic source. Search and newsletter readers behave differently from aggregator spikes, so a blended rate will mislead.

**Suggested wording for the readout:**

> "There's no reliable industry benchmark for read-through, because the metric isn't standardized and published figures aren't comparable. Our baseline is X% across the last N posts (this post: Y%). I propose a target of Z% next quarter, measured the same way."

## Likely follow-up from her

- **"Isn't there any benchmark?"** Offer to look for published figures that name their metric definition and audience, and to present them as context only, not as the target.
- **"22,000 is our best ever. Doesn't that count?"** It's a reach result and worth stating as one. Reach is not pipeline, so keep the two sections separate.

## What I need from you to fill this in

- Pipeline $, opportunity count, and signups attributed to the post, plus the attribution rule you used.
- Your analytics tool and how it defines scroll depth or engaged time.
- Read-through data for the last 5 to 10 posts.

With those I can produce the final numbers and a target recommendation.