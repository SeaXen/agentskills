# Worked example: a two-person DevRel team

Read this when you need the shape of deliverables 1, 3 and 5 filled in. The company and every number are illustrative.

## Contents

- Situation
- Leak trace reading
- Re-ranking block
- Routing table and hour budget
- Handoff calendar

## Situation

A webhooks API company: two DevRel people, about four hours a week for feedback work, a 6,000-member chat community sending 25-40 requests a week, about 10 a week through support, a few from enterprise sales calls, and 3-5 a week as issues on open-source SDK repos. Two PMs plan in six-week cycles and say they "never hear from the community". Each PM reads DevRel's direct messages when pinged; nobody has agreed to anything. The next planning cycle starts in three weeks. The team wants a loop that lasts.

## Leak trace reading

20 requests over 90 days, at least three per channel.

| Stage | Count | Ratio | Lost |
|---|---|---|---|
| Asked | 20 | - | - |
| Captured | 8 | 40% of asked | 12 |
| Reached product | 7 | 88% of captured | 1 |
| Decision recorded | 3 | 43% of reached | 4 |
| Requester told | 3 | 100% of decided | 0 |

- 3 of 20 got a decision. All three came through a path with a built-in decision step: a public SDK issue and an account executive's CRM note. The 100% "told" rate is a symptom of that, not a strength.
- Five rows are one problem - events lost while consumers redeploy - asked in chat, support and a sales call. It reached a PM twice and was never decided. That row is the pitch.
- Capture loses the most requests (12 of 20), so capture rules are the stage to fix. The contract is still agreed first, but for a different reason: question 1 answered "someone informally", and that answer always puts Steps 1-2 ahead of intake design. Capture rules are built alongside the contract, because capture feeds the first review.

## Re-ranking block

```
- 3-week date: redirect-to-record and one decision review promoted; planning seat demoted.
- Lasting loop: planning seat and quarterly report kept, sequenced after two review cycles.
- 4 h/week for ~50 requests/week (~5 min each): log-on-behalf only for paying accounts and
  blockers; weekly digest deleted.
- Open-source SDKs + closed API, developers can't see product's tracker: public tracker is the
  record developers see, linked one-to-one from product's own items.
```

## Routing table and hour budget

| Channel | Weekly volume | Capture move | Owner | Notes |
|---|---|---|---|---|
| Chat, requests channel | 15-25 | redirect with the received reply; weekly sweep of threads without a link | DevRel | |
| Chat, help channel | 10-15 | answer how-to in place; redirect feature asks | DevRel | bugs to support |
| Support | ~10 | agent tags the ticket and pastes the redirect; DevRel sweeps the tag weekly | support, DevRel | ticket text never copied public |
| Sales calls | under 1 | account executive writes the problem in the customer's words; DevRel creates the record without naming the prospect | sales, DevRel | opportunity reference stays private |
| SDK issues | 3-5 | stays an issue; linked from its record; status mirrored | DevRel | bugs stay in the issue queue |

| Task | Hours/week |
|---|---|
| Redirect replies | 0.4 |
| Weekly sweep | 1.0 |
| Log on behalf (paying, blockers) | 0.8 |
| Merge and dedup | 0.5 |
| "Under review" replies at agenda freeze | 0.2 |
| Decided statuses, batched after each review | 0.6 |
| Review prep | 0.3 |
| Total | 3.8 |

The one-off backfill before the first review sits outside the weekly budget: capped at the eight largest problem clusters from the trace, everything else marked received.

## Handoff calendar

| When | Event |
|---|---|
| Week 1 | Pitch the contract to both PMs; agree it |
| Week 1-2 | Set up the record space, status labels, policy page, support macro, CRM note format |
| Week 2 | Backfill eight clusters |
| Week 2, end | Agenda for review 1 frozen and sent three business days ahead; "under review" replies to every agenda record's requesters |
| Week 3 | Review 1, 60 minutes, one week before planning |
| Week 4 | Batched replies on every status set at review 1 |
| Week 9 | Review 2, one week before the next planning cycle |
| Week 13 | Re-run the leak trace; review the contract |
| Week 15 | Review 3; ask for the planning seat; first quarterly report |
