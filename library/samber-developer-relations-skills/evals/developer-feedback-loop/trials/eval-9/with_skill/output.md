**Next action:** open the 412-row sheet and pull the 25 most recent rows from the last 90 days, at least 3 per channel. That is the leak trace (Step 1). It takes about 2 hours and is the evidence for your pitch to Anika.

The fastest path is not what you drafted. Three parts of the plan would slow you down or make the pile worse.

## What I changed from your plan

| Your plan | Change | Why |
|---|---|---|
| All 412 in the tracker | Cluster the 412 into problems. Write full records only for the biggest clusters (≤10) before planning. | A review decides roughly 10 records in an hour. 412 rows is a better-organized pile. |
| 38 labels | 3 labels plus 2 per-requester fields. Details in deliverable 4. | A big label set is applied inconsistently by week 3 and product stops trusting it. |
| P0-P3 and effort S/M/L | Dropped. | Priority and effort are Anika's calls. Severity per requester replaces P0-P3. |
| Weekly digests to Anika | Cut. One decision review before planning replaces them. | A digest informs and decides nothing. "Take a look, nothing formal" is a reader who stops opening it. |
| Anika "takes a look" | Agree a one-page contract with her first. | An informal receiver is a contract waiting to be written. |

412 requests over 18 months is about 5 a week. Steady state is cheap, so the one-off pile is the real work.

## Assumptions

You answered 1, 3 and 4 only. Correct any of these and I'll re-rank.

- You have about 5 h/week for this. Below about 6 h/week, cut the backfill to the top 6 clusters.
- The record of truth is Anika's existing tracker, private to developers, with a new "Feedback" type. If developers can see it, say so: the replies and the intake form change.
- There is no public roadmap. Anika approves the reasons for any public "no", and you post them.
- Planning is Fri 2026-11-20. Replace that date if it is wrong.
- Anika can decide on every area. If she covers only some, the contract needs a receiver and a backup per area.

## 1. Leak trace

Sample 25 requests from the last 90 days. Take the most recent per channel, not the memorable ones. Include discord, support, booth and sales, at least 3 each. Keep duplicates and mark them.

| # | Channel | Date asked | Captured? | Reached product? | Decision recorded? | Requester told? | Days to first staff reply |
|---|---|---|---|---|---|---|---|

- **Captured** means written anywhere durable beyond the original message. Your spreadsheet counts.
- **First staff reply** excludes peer answers and bots.
- **Funnel:** captured ÷ asked, reached ÷ captured, decided ÷ reached, told ÷ decided.

| Stage | Count | Ratio | Lost |
|---|---|---|---|
| Asked | 25 | - | - |
| Captured | fill in | | |
| Reached product | fill in | | |
| Decision recorded | fill in | | |
| Requester told | fill in | | |

I have not filled the table because I do not have your sheet.

- **Likely finding:** 412 captured and almost none decided. That means fix the decision stage first, which is the contract (deliverable 2).
- **Booth and sales rows:** these probably have no reply path. Count them as unanswered.
- **Pitch row:** find one problem asked through 2-3 channels that reached nobody. That one row beats any framework.

## 2. Product contract

**Pitch to Anika** (send Mon Nov 2, ask for 30 minutes):

> Anika, planning is on Nov 20. I have 18 months of feedback: 412 requests from Discord, support, booth notes and sales. I clustered them into about 10 problems, each with distinct requesters by tier and evidence links. I'm asking for one 60-minute review on Nov 17, chaired by you. Every record on the agenda leaves with a status from you. I'll send the agenda 3 business days ahead. Requesters who agreed to be contacted are yours for discovery calls. I handle capture, dedup, and telling requesters, including the no. You keep every decision. Here is one problem that reached nobody: [pitch row].

**Working agreement** (one page, stored next to the tracker):

```
Developer feedback loop - working agreement

Record of truth:   Product tracker, type "Feedback"
Product receiver:  Anika (<name> per area where she does not cover it), backup <name>
Review:            Per planning cycle, 60 min, chaired by Anika
Product promises:  Every record on the agenda leaves with a status.
                   "Revisit next cycle" at most twice per record; the second revisit is the last.
DevRel promises:   Records meet the template. Duplicates are merged.
                   Agenda sent 3 business days ahead.
                   Community requesters told within 5 business days of a status change.
Support / sales / booth promise: they tell requesters who came through their channel.
Out of scope:      Bugs -> support or issue queue. Security -> private channel. How-to -> docs and support.
Public statements: DevRel drafts, product approves reasons. No dates unless product has published them.
Missed review:     Agenda records stay "under review" with a note that the review moved.
                   After two misses in a row, DevRel raises it with Anika's manager.
Review of agreement: 2027-02-02
```

**Decision rights:** product sets planned, not planned and shipped. Product owns what gets built and when. You capture, merge, label, write evidence and tell requesters. Only product publishes dates.

**If Anika declines a standing review:** do not build the pipeline. Send the leak trace to her manager as a one-page finding. Offer the smallest version: one review per quarter on the top 5 records.

## 3. Intake spec

**Re-ranking block**

```
- Planning in 3 weeks: redirect-to-record and one decision review promoted; planning seat demoted.
- Question 4 (clear the pile once vs a loop that lasts) is open. I assumed both:
  the near date governs cycle 1; the planning seat and quarterly report start after two reviews.
- ~5 h/week for ~5 requests/week (~60 min each): hours are not the constraint.
  Log on behalf for paying accounts and blockers; weekly digest deleted anyway (no reader).
- Private record of truth: redirect points to a public intake form;
  status replies go to the channel where the requester asked.
```

**Routing table** (fill the weekly volumes from your sheet)

| Channel | Weekly volume | Capture move | Owner | Notes |
|---|---|---|---|---|
| Discord | from sheet | Redirect with the "received" reply and the intake form link. Weekly sweep of threads with no link. | DevRel | Bugs go to support. |
| Support | from sheet | Agent tags the ticket and pastes the redirect. You sweep the tag weekly. | Support, DevRel | Ticket text never copied into a public place. |
| Sales | from sheet | Account exec writes the problem in the customer's words. You create the record without naming the prospect. | Sales, DevRel | Segment "prospect". Opportunity reference stays private. |
| Booth | batches after events | Post-event: you cluster the notes and link them to records. Skip notes with no contact. | DevRel | Biggest channel bias risk: every requester is a prospect or event-goer. |

**Hour budget** (5 h/week assumed, ~2.6 h steady state)

| Task | Hours/week |
|---|---|
| Redirect replies | 0.3 |
| Weekly sweep | 0.5 |
| Log on behalf (paying accounts, blockers) | 0.5 |
| Merge and dedup | 0.3 |
| "Under review" replies at agenda freeze | 0.2 |
| Decided statuses, batched after each review | 0.5 |
| Review prep | 0.3 |
| **Total** | **2.6** |

**One-off backfill (outside the weekly budget, about 11-14 h over weeks 1-2):**

1. Run a first-pass clustering with a cheap model (Haiku-class). It suggests merges. You confirm every one.
2. Count distinct requesters per cluster, across channels, once each.
3. Rank clusters: blockers first, then distinct requesters.
4. Write full records for the top ≤10.
5. Add a `cluster ID` column to the sheet for the other rows. Mark them "received" with a note that they wait for the next cycle.

**Stale data:** 18 months old. Re-check that the problem still exists before writing a record. Drop what shipped already.

**Out-of-loop routes:** bugs go to support. Security goes to the private channel. How-to goes to docs and support.

## 4. Record template and label set

Your 38 labels (14 fixed + 24 product areas) become:

| Your labels | Becomes | Kind | Values |
|---|---|---|---|
| Product areas (24) | **area** | label, single value | 6-10 areas. Merge areas that share one product owner. Ask Anika to name the final list. |
| (new) | **type** | label | feature request, DX friction, docs gap |
| (new) | **status** | label | received, under review, needs discovery, planned, not planned, shipped, duplicate |
| Customer tier (free, pro, enterprise) | **segment** | per requester, rolled up | free, pro, enterprise, prospect |
| P0-P3 | **severity** | per requester, rolled up | blocker, slows down, cosmetic |
| Source channel | **Sources** | field on the record, not a label | discord, support, booth, sales |
| Effort S/M/L | dropped | | Anika can add her own estimate field in review. |

Source is a field because one record collects several channels. Segment and severity are per requester because one record spans free and enterprise developers. A single label would erase that mix.

**Record template**

```
Title:            <problem in the developer's words, never the feature>
Problem:          <what they were trying to do, what stopped them>
Requested fix:    <verbatim, kept separate from the problem>
Job / use case:   <the outcome, one line>
Evidence:         <repro steps; verbatim quote with a link to the source message>
Workaround:       none | painful | acceptable (and what it is)
Severity:         blocker N / slows down N / cosmetic N
Requesters:       <distinct people> / <distinct orgs>, by segment (free / pro / enterprise / prospect)
Sources:          <channels, with links>
Status:           <one value>
Owner:            <product owner of the area, once reviewed>
--- private ---
Accounts:         <account IDs, tier, revenue band>
Contact consent:  <who agreed to be contacted for discovery>
```

**Good and bad:**

- **Bad:** "Add cold-start config!!! Lots of people on Discord want it. Big customer too. +14"
- **Good:** "Cold starts exceed our p99 budget on first request after idle. 7 people / 5 orgs: 3 free, 1 pro, 1 enterprise, 2 prospects. Workaround: painful, a keep-warm ping. Evidence: 3 Discord threads, 1 ticket, 2 booth notes, with links."

*(Adapt the example to your real top problem.)*

**Dedup rules**

1. Search before creating. Attach a new mention as a requester plus a link.
2. Merge on the same problem, not the same request.
3. Split when different problems hide behind one request.
4. Close duplicates toward the canonical record with a link.
5. Count a requester once per record, across channels.
6. A vote spike from one outside link counts as one event.

**Weighting inputs for Anika:** distinct requesters, distinct orgs, segment mix, representation (requesters ÷ active developers in that segment, as a range), influence, severity and workaround, and private account value shown beside the rest. Never hand her a single score.

## 5. Handoff calendar and review agenda

| When | Event |
|---|---|
| Mon Nov 2 | Leak trace (2 h). Send Anika the pitch. Start clustering the 412. |
| Tue Nov 3 | Pitch to Anika (30 min). |
| Wed Nov 4 | Contract agreed. |
| Wed-Fri Nov 4-6 | Set up the tracker (type, area, status, fields), intake form, support macro, Discord redirect text, policy page. |
| Mon-Wed Nov 9-11 | Write the top ≤10 records. Mark the rest "received". |
| Thu Nov 12 | Agenda frozen and sent. "Under review" replies to every agenda record's requesters. |
| Tue Nov 17 | **Review 1**, 60 min, chaired by Anika. Statuses written into records before the meeting ends. |
| Fri Nov 20 | Planning (assumed). |
| Mon-Fri Nov 23-27 | Batched replies for every status set at review 1. |
| Thu Jan 7, 2027 | Agenda frozen for review 2. |
| Tue Jan 12, 2027 | **Review 2.** Assumes an ~8-week cycle with a holiday gap. Adjust to Anika's cycle. |
| Tue Feb 2, 2027 | Re-run the leak trace and review the contract. Then ask for the planning seat and write the first quarterly report. |

**Agenda for review 1** (60 min)

```
1. Shipped since last review (2 min): n/a for review 1.
2. Revisit items from last cycle (10 min): n/a for review 1; use the time for item 3.
3. New records, blockers first, then by distinct requesters. Segment mix and private account
   value beside each, never folded into a score (30-40 min). A status per record.
4. Signals without a record yet (10 min).
5. Statuses to publish and who drafts each reply (5 min).
```

## 6. Status vocabulary, reply templates, public policy page

| Status | Means | Who sets |
|---|---|---|
| received | Captured and linked to a record. "We have it", nothing more. | DevRel |
| under review | On a product review agenda. A decision by that review, not a ship date. | DevRel |
| needs discovery | Product wants to talk to requesters. | Product |
| planned | Product committed to solving the problem. A date only if product published one. | Product |
| not planned | Product decided not to solve it now. Reason and best workaround included. | Product |
| shipped | Released, with a link to the release note. | Product |
| duplicate | Merged into another record. | DevRel |

Post each reply on the record and in the channel where the requester asked. Tracker notifications reach only subscribers, so a Discord or support requester learns nothing unless someone tells them there.

**received**
> Thanks, logged as <record link>, where <N> others hit the same problem. Product reviews these every <cycle>. I will post the decision there.

**under review**
> <record link> is on the agenda for the product review on <date>. You will get a decision there. That is a decision, not a delivery date.

**needs discovery**
> Product wants to talk to a few people hitting <problem>. If that is you, reply on <record link> with how to reach you. Talking to us commits neither side to anything.

**planned**
> Product has committed to solving <problem> (<record link>). No date is published yet. I will update the record when one is, and when it ships.

**not planned**
> Product reviewed this on <date> and won't build <requested fix> this year. The reason: <reason product approved>. Until then, the workaround is <link>. If your case isn't covered, say so on <record link>. That is what would reopen it.

Never write "great idea, it's on our radar". It reads as yes to the asker and as evasion to everyone else, so the request comes back every month.

**shipped**
> Shipped in <version> (<changelog link>). This came from <record link>. Thank you to everyone who added a use case. <One line on how it solves the problem in the record.>

**shipped, but not the fix requesters asked for**
> Shipped in <version> (<changelog link>). You asked for <requested fix>. We built <what shipped> instead, because <reason>. It solves <problem> this way: <one line>. If it doesn't cover your case, say so on <record link>.

**planned, now not planned**
> In <month> we said product would solve <problem>. That changed at the <date> review: <what changed and why>. Best workaround now: <link or "none exists">. I'm sorry for the reversal. <record link> stays open for use cases that would change this again.

**duplicate**
> This is the same problem as <record link> (<N> people). Closing this one so use cases land in one place. Please add yours there.

**Public feedback policy page** (link it from every reply and Discord channel topic)

```
How we handle feedback
- Where to post: <intake form link>. Chat is for conversation; requests posted there get linked here.
- What happens next: we merge duplicates, product reviews requests every <cycle>, and every
  reviewed request gets a status: received, under review, needs discovery, planned, not planned,
  shipped, duplicate.
- What decides priority: <factors Anika actually uses, e.g. severity, number of teams affected,
  fit with direction>. Votes are one input, not a ballot.
- What we can't take here: bugs -> <support path>; security -> <private path>; how-to -> <docs/support path>.
- What we won't do: give dates before we are sure, or keep requests open we have decided against.
```

**Privacy rules**

- Never copy a private support message, account name or revenue figure into a public place.
- Quote Discord publicly only when the channel is public and the quote is about the product.
- Ask before naming a company as a requester.
- Keep discovery-contact consent in the private record. Remove it when the requester withdraws.

## 7. Metric sheet

| Metric | Definition | Owner | Baseline | Self-set target | Action if it slips |
|---|---|---|---|---|---|
| Time to first staff reply | Feature request asked to first staff reply, median and p90. Bots and peers excluded. | You | trace | 2 business days | Rebalance the sweep or shorten the promise. |
| Capture rate | Requests linked to a record within 2 business days ÷ requests asked, from the re-trace. | You | trace | set after trace | Tighten the capture rule on the leaking channel. |
| Decision rate | Agenda records leaving with a status ÷ records on the agenda. | Anika | n/a (new) | 100%, revisit ≤2 times | Raise in the contract review. Shrink the agenda. |
| Closure rate | Status changes communicated to requesters in their channel within 5 business days ÷ status changes. | You, support | trace | 100% | Make the reply the last agenda item. |
| Shipped-from-feedback | Changes shipped that trace to a record. The record must exist before work was scheduled and be linked in the release note. | Anika, you report | 0 | none, it is an outcome line | none |

- **Baselines:** fill from the leak trace.
- **Targets:** all self-set. No published benchmark exists for these four metrics. Revisit after one quarter.
- **Volume:** feedback volume is not a metric.
- **Next re-trace:** Tue Feb 2, 2027.

## What to do first

Run the leak trace on Mon Nov 2, 2 hours. Then send Anika the pitch and ask for 30 minutes on Tue Nov 3.

## Open questions

These change the design:

1. Can developers see the product tracker?
2. Does Anika cover every area?
3. How many hours a week do you really have?