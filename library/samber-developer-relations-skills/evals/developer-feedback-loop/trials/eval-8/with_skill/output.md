# Review of your Lanternworks feedback slide

**Verdict:** don't send the slide as drafted. Three of its four claims fail under scrutiny. The ninth-metric idea would also hurt you. For Friday, use one number with a written attribution rule, backed by a small leak trace. The trace is a count of what happened to recent requests.

I read `developer-feedback-loop` and its references (`loop-metrics.md`, `feedback-record-and-taxonomy.md`). I have not seen your data, so every figure below is yours, unchecked.

## Line by line

| Draft line | Problem | Fix |
|---|---|---|
| "Feedback volume up 40% QoQ" | Volume isn't a success metric. More requests isn't better or worse by itself, and a sheet that celebrates volume rewards over-capture. A VP can also read +40% as "the product got worse". | Cut it. If you keep it, put it in the appendix as context, not as the headline. |
| "95% collect, 10% act, 5% tell customers (Gartner)" | I found no public Gartner source for the three-part figure. It traces to a vendor deck from around 2010 that carries only the 95% and 10% parts, and the 5% leg shows up later on vendor blogs. Cite it and someone will ask for the source. It also sets a bar ("only 10% act") that your own slide then has to clear. | Delete it. Your own numbers carry the slide. |
| "Median first response under 10 minutes" | Likely bot or auto-replies, or peer answers. In Hasan et al. (MSR 2023, 111k PRs), 35 of 50 sampled first responses within ten minutes were bots. Bot speed explained 0.33% of PR lifetime variance, against 64.7% for human response time. Peer answers on Discord are healthy, but they aren't the loop. | Redefine it as time from a feature request to the first reply from staff. Exclude bots, auto-replies and peer answers. Report the median and the 90th percentile. Count unanswered requests separately, because a median over answered ones hides them. |
| "11 of 14 features were community-driven" | "At least one Discord mention" claims every feature that anyone mentioned. By that rule nearly everything is "community-driven". It also ignores GitHub and support, so it undercounts too. | Use the attribution rule below. Expect the number to drop. |

**Attribution rule.** A shipped change counts when a feedback record existed before the work was scheduled, and the release note links that record.

Apply that rule to the 14 features. Report the count as "N of 14 trace to a record that predated scheduling". If the VP later asks what the 11 meant, you can show the rule instead of defending a claim.

Possible outcomes:

- **Few records predate scheduling.** The honest finding is that the loop isn't wired to planning yet. That is a stronger ask than an inflated win.
- **Many do.** You get a defensible headline.

## The nine extra metrics: don't

- **Cap:** the skill keeps three to five metrics, each with an owner and the action it triggers when it slips. Nine more makes thirteen or so, and the dashboard looks thorough while nobody acts on it.
- **Test for each metric:** a metric with no owner and no action is decoration.
- **Which ones:** there is no published benchmark for capture, decision or closure rate. Set targets from your own trace and label them self-set.
- **Avoid:** feedback volume, mention counts and vote counts as success metrics.

The set I'd use is below.

| Metric | Definition | Owner | Action if it slips |
|---|---|---|---|
| Time to first staff reply | Feature request to first human staff reply, median and p90 | DevRel | Rebalance the capture rota |
| Capture rate | Requests linked to a record within 2 business days ÷ requests asked (quarterly re-trace) | DevRel | Tighten the capture rule for the leaking channel |
| Decision rate | Records leaving the review with a status ÷ records on the agenda | Product | Raise it in the contract review and shrink the agenda |
| Closure rate | Status changes told to requesters within 5 business days ÷ status changes | DevRel and support | Add the reply to the review's last agenda item |
| Shipped-from-feedback | Changes shipped that trace to a record, per the attribution rule | Product, DevRel reports | None; it's the outcome line |

Pick the 3 to 5 you can actually measure now. I'd lead with shipped-from-feedback and time to first staff reply. The 2-day and 5-day windows are starting targets the skill sets, not benchmarks.

## A slide you can defend

> **Developer feedback, Q3**
> - **N of 14** features shipped this quarter trace to a developer-feedback record that existed before the work was scheduled and is linked from the release note.
> - Median time to first **staff** reply on feature requests: **X** (p90 **Y**; bots and peer answers excluded; **Z** requests unanswered).
> - Trace of the last 25 requests: **a** captured, **b** reached product, **c** decided, **d** requester told. Biggest loss: **[stage]**.
> - Next quarter: fix **[stage]**, re-trace on **[date]**.

If the trace shows most requests lost at the decision stage, that is the real finding. It tells the VP what to fund: a product receiver and a review cadence.

## What you need to do before Friday

1. **Run a mini leak trace (about 2 to 3 hours).** Take the most recent 20 to 30 feature requests from the last 60 to 90 days. Take them from Discord, GitHub and support, at least 3 per channel. Use the most recent, not the memorable ones. For each, record whether it was captured in a durable record, whether it reached product, whether it got a decision, and whether the requester was told. Also record the days to first staff reply. If you have fewer than 20 requests, skip the percentages and show the rows.
2. **Recount the 14 shipped features** with the attribution rule.
3. **Recompute the response time** with the staff-only definition.

## Questions that change the advice

Answer these in this order.

1. **Is there a named person on the product side who receives feedback and decides on it?** Yes, informally, or nobody? If nobody, the deliverable is the leak trace plus a pitch to product for a decision contract. Don't build an intake pipe that feeds nobody.
2. **What did the VP actually ask for: a number, a report, or something else?** A request for "a number" makes shipped-from-feedback the headline line, with the trace behind it.
3. **How many hours a week can the feedback work get, and from whom?** This decides which capture moves are affordable.

I'd also like to know where product tracks planned work and whether developers can see it.

One honesty note: if the recount gives a worse number than 11, the slide will look weaker. It will also survive the VP's first follow-up question, and the 11 would not.