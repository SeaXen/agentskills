# How to get Thornfield's product team to act on your feedback

## Short answer

Stop sending the Friday digest. A digest informs and decides nothing, and yours has a zero open rate and two replies ever. Replace it with a one-hour **decision review** once per six-week cycle. Hold it the week before planning, not the week after. Every record on its agenda must leave with a status.

Your meetings land the week after planning, so even a good meeting arrives once the cycle is already set. Notes like "good discussion, will consider" show that nobody has agreed to decide anything. The sales jump shows that the only working route into product today is an exec's calendar.

This follows the `developer-feedback-loop` skill. It assumes your PMs have agreed to nothing yet, which the skill treats as "someone informally". That means: agree the contract first, build intake alongside it, and don't buy a tool.

## Assumptions to confirm

I couldn't ask these, so I assumed the following. Tell me where I'm wrong, because some answers change the plan.

- **Hours:** you and the support lead have about 3–4 hours a week combined. If it's under 2, log-on-behalf is cut as well.
- **Next planning date:** unknown. I use "week 1 = planning" below, so please give me the real date.
- **Record of truth:** I assume the PMs already have a tool where they track ideas and planned work.
- **Public roadmap:** I assume none, and that you can't say no publicly yet.
- **Question I need answered:** who in product will actually receive and decide? Is it one PM per area, or both?

## 1. Leak trace (do this first, about 2 hours)

Sample the 20–30 most recent feedback requests from the last 60–90 days. Take at least 3 per channel: community, support, sales and any GitHub issues. Use the latest ones, not the memorable ones.

For each request, record five things:

- whether it was captured anywhere durable
- whether it reached product
- whether it got a decision
- whether the requester was told
- days to the first staff reply

Read it as a funnel and fix the stage that loses the most requests first.

- **Lost at capture:** you need capture rules.
- **Reached product but undecided:** you need the contract. I expect this is you, given the "will consider" meetings.

Find one problem that arrived through several channels and reached a PM but was never decided. That row is your pitch. Include any sales-driven request in the trace. It shows the exec route is not working either, because the jump changed the calendar but not the board.

## 2. Contract with the PMs (the core of the fix)

**Pitch to the PMs.** Open with what they get, not what you need.

> "One hour per six-week cycle, before planning. Records already deduplicated, with evidence and segment mix. Requesters who agreed to be contacted are available as interview candidates, so you don't have to recruit them. In return, each record leaves with a status."

If a PM declines a standing review, don't build the pipeline. Send the leak trace to the PMs' manager as a one-page finding and offer the smallest version: one review per quarter on the top five records.

**Decision rights.** Product decides what gets built, and sets planned, not planned and shipped. You capture, merge, write the evidence, draft public wording and tell requesters. Don't rank their roadmap. You'd become an unpaid PM with none of the authority.

**One-page working agreement**, to be stored next to the record of truth:

```
Record of truth:    <PMs' existing idea/backlog space, one "feedback" type + a view>
Product receiver:   <named PM per area, plus a backup>
Review:             once per 6-week cycle, 60 min, chaired by product, held the week BEFORE planning
Product promises:   every record on the agenda leaves with a status
                    (planned / not planned / needs discovery / revisit next cycle, max twice per record)
DevRel promises:    records meet the template; duplicates merged; agenda sent 3 business days ahead;
                    requesters told within 5 business days of a status change
Out of scope:       bugs -> issue queue/support, security -> private channel, how-to -> docs/support
Public statements:  you draft, product approves the reason; no dates unless product publishes them
Missed review:      records stay "under review"; after two misses in a row, raise with the PMs' manager
Review this agreement: one quarter out
```

The clause that matters most is "revisit max twice". Without it, "later" becomes the permanent status, and you get another "good discussion, will consider".

## 3. Handle the sales override

Don't fight it. Route it. Log the exec's request as a normal record with its private account value, in the same review. Put segment mix and account value beside each record, and don't fold them into a score. Weighing them is product's call. Account value is a legitimate input at a commercial company, but it shouldn't be the only one.

Agree one sentence with the VP of Sales: "Send me the customer's problem in their words, and I'll put it on the next review agenda." Add the exception rule to the contract: a genuine production blocker can go to the PM as a "blocker" record the same day, still recorded, and still gets a status at the next review.

## 4. Intake (kept light, built alongside the contract)

- **Record format.** Write each record problem-first. The title is the developer's problem, and the requested fix goes in its own field. Product then compares solutions instead of voting yes or no on one design. If a request arrives as a solution, ask once: "what were you trying to do when you needed this?"
- **Counting.** Count distinct requesters and orgs, not mentions. Show reactions separately.
- **Labels.** Keep three single-valued axes (type, area, status) and two per-requester fields (segment, severity). Nothing more.
- **Capture moves.** The redirect reply (a link to the record) is the cheapest move, so use it everywhere. Add a weekly sweep for the rest. Log on behalf of the requester only for paying accounts and blockers.
- **Routing out.** Send bugs, security reports and how-to questions elsewhere at capture.

Rough weekly budget for about 3.8 hours: redirects 0.4, sweep 1.0, log-on-behalf 0.8, merge and dedup 0.5, "under review" replies 0.2, batched decided replies 0.6, review prep 0.3. Cut log-on-behalf first if hours drop.

## 5. Calendar (relative to your 6-week cycle)

| When | Event |
|---|---|
| This week | Run the leak trace and confirm the assumptions above |
| Next week | Pitch and agree the contract with both PMs |
| Following 1–2 weeks | Set up the record view, status labels and support/CRM notes. Backfill only the 8 largest problem clusters. Mark the rest "received" |
| 3 business days before review | Freeze and send the agenda. Reply "under review" to those requesters |
| Review 1 (week 5 of the current cycle if possible, otherwise the first available week before planning) | 60 min. Write each status into its record before the meeting ends |
| Week after the review | Batch replies to requesters for every decided status |
| Next cycle's week 5 | Review 2 |
| About 13 weeks after start | Re-run the leak trace and review the contract |
| Review 3 | Ask for a seat in planning, only once two reviews have run and product has seen records ship. Send the first quarterly report |

If planning is closer than 3 weeks away, the first review will be thin. Run it anyway on the top five records. A rushed first review beats another cycle with nothing on the board.

## 6. Review agenda

1. Shipped since last review (2 min): which records closed, and were requesters told?
2. Revisit items from last cycle (10 min): decide, or mark not planned.
3. New records (30 min): blockers first, then by distinct requesters. Never order by date or by who asked loudest. Settle a status per record.
4. Signals without a record yet (10 min).
5. Statuses to publish and who drafts each reply (5 min).

The output is a status change per record, written into the record before the meeting ends. Minutes without status changes mean the review didn't happen.

## 7. Close the loop with the people who asked

Use this status vocabulary: received, under review, needs discovery, planned, not planned, shipped, duplicate.

- Every status change triggers a reply, in the record and in the channel where the person asked.
- Say no as no. A "not planned" reply carries the reason product approved, the best workaround and what would change the decision. "On our radar" reads as yes to the asker and as evasion to everyone else.
- Never give a date product hasn't published. Treat "next cycle" as a date.

## 8. Metrics (three to five, with targets set from your own trace)

| Metric | Owner | Action if it slips |
|---|---|---|
| Decision rate: agenda records leaving with a status ÷ records on the agenda | Product | Raise it in the contract review, or shrink the agenda |
| Capture rate (from the quarterly re-trace) | You | Tighten the capture rule for the leaking channel |
| Closure rate: status changes told to requesters within 5 business days | You and support | Add the reply to the review's last agenda item |
| Time to first staff reply on a feature request (bots excluded) | You | Rebalance who covers which channel |
| Shipped-from-feedback | Product, you report | None. It's the outcome line for leadership |

Write the attribution rule for shipped-from-feedback before you count. A change counts only if a record existed before the work was scheduled and is linked from the release note. Without that rule, every shipped feature gets claimed.

Don't report feedback volume as a success metric. All targets are self-set. There is no public benchmark for these rates.

## What to do first

1. **Today:** answer the questions above, mainly the planning date and who in product will own decisions.
2. **This week:** run the leak trace and pick your best traced example.
3. **Next week:** pitch the one-hour pre-planning review and agree the one-page contract.
4. **Until then:** stop the Friday digest.