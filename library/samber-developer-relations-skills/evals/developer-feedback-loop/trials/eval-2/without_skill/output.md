# Fix decision first, not capture

Capture and decision lose the same number of requests, 10 each. The rates differ, and decision is the tighter constraint.

| Stage | In | Out | Lost | Pass rate |
|---|---|---|---|---|
| Capture | 24 | 14 | 10 | 58% |
| Reach Ruth | 14 | 13 | 1 | 93% (see caveat 2) |
| Decision | 13 | 3 | 10 | **23%** |
| Close the loop | 3 | 3 | 0 | 100% (n=3) |
| **End to end** | 24 | 3 | 21 | **12.5%** |

## Why decision beats capture

- **Decision is the bottleneck.** It decides 3 of 13. If you fix capture alone and every request is written down, roughly 5 get decided instead of 3. If you lift decision to 70% on the requests that already reach Ruth, about 9 get decided.
- **More capture means a longer queue.** Without a decision cadence, you add 10 named requesters waiting on an answer that doesn't come.
- **Both numbers are rough.** They assume new items behave like old ones. They probably don't, because the extra 10 are lower-reaction requests.

I'd do the decision fix first, with one small capture patch alongside (step 4 below).

## Weak spots in the trace

1. **The sample flatters capture.** You took the top 24 by public reactions. Those are the requests most likely to get noticed, so 58% is probably an upper bound.
2. **"Reached Ruth" is nearly circular.** A DM to Ruth counts as written down and as reached by construction. 13 of 14 shows the handoff works for DMs. It says nothing about whether Ruth had the request in a place where she could decide it.
3. **Sales is missing.** The AEs' requests are in no system, so capture there is 0% by your own account. They are few, but they likely come from paying customers.
4. **Reactions measure popularity, not weight.** A hosted-plan customer's request may have one reaction.
5. **Removing the four duplicates hid demand.** Each duplicate was probably a different person. Check whether those requesters were told when their request was decided. "All 3 told" may really mean 3 of 3 plus up to 4 unnotified.
6. **The 6-minute first response measures the bot.** It is an acknowledgment of the post, not of the request. The human response takes up to an hour. Don't fix this stage, but replace the metric with time to the first human reply that names an owner or a next step.
7. **100% on close is n=3.** The 10 undecided requesters hear nothing, so from their side the loop never closes.
8. **I don't have cohort age.** If some of the 10 undecided are only two weeks old, they aren't stuck yet.

## Plan

1. **Ask Ruth why each of the 10 is undecided (20 min).** Sort the answers into needs info, low priority, not her call, or no time. If most are "not her call", the fix is a named decision owner for the hosted control plane versus the OSS clients. If most are "no time", the fix is a cadence.
2. **Give the queue one home (30 min).** Move it out of DMs into one list Ruth owns. Each row gets a status: `new`, `yes`, `no`, `not now`, or `need info`. A `no` counts as a decision.
3. **Set a weekly 30-minute decision slot with an age limit (about 10 min to schedule).** Nothing stays `new` for more than two slots. Any status change triggers a message to the requester, including the duplicate requesters.
4. **Add the sales patch (15 min).** Give the two AEs one shared form or note, with a rule that every customer ask goes in the same day. It's cheap, and it covers the highest-value gap.
5. **Do the full capture-rule rewrite after one quarter of the new cadence.** Re-run this trace on a random sample of 24, not the top 24 by reactions.

## What would flip my answer to capture

- The 10 uncaptured requests include the ones from paying hosted-plan customers or large accounts.
- Ruth says she'd decide quickly if she saw them, and that the problem is she never sees them. That would mean the 10 stalled items are mostly waiting on information nobody captured.
- The uncaptured 10 cluster in one channel, such as the forum. Then it's a cheap, targeted capture fix, and I'd do it in parallel.

Which stage covers the 10 uncaptured requests: Discord, forum, or both? That's the first thing I'd want to know.