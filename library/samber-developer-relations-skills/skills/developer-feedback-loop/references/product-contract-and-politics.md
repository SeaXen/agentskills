# Product contract and politics

Read this before Step 2 (the contract) and whenever product ignores, overrides or offloads the loop.

## Contents

- Decision-rights table
- Contract template
- Pitching the contract to product
- Review meeting agenda
- Political failure modes and moves
- Bias handling

## Decision-rights table

| Decision | DevRel | Product | Support / Sales / CS |
|---|---|---|---|
| Capture and link a request | owns | - | owns for their channel |
| Merge, split, label | owns | may correct | - |
| Evidence quality of a record | owns | may send back | contributes |
| What gets built, when | informs | **owns** | informs |
| Status planned / not planned / shipped | relays | **sets** | - |
| Public wording of a no | drafts | approves the reason | - |
| Telling requesters | owns | - | owns for their accounts |
| Dates in public | never | only product, only when committed | never |

Product owning the decision is not a concession. A DevRel team that decides priorities becomes an unpaid product manager without the authority, the roadmap context, or the engineering capacity behind the role. Guillaume Laforge, who has held both hats, put it plainly: "it's tough to do two jobs like these at the same time".

## Contract template

One page, agreed with the product lead, stored next to the record of truth.

```
Developer feedback loop - working agreement

Record of truth:      <where canonical records live>
Product receiver:     <named person per area, plus a backup>
Review:               <monthly | per planning cycle>, <duration>, chaired by <product>
Product promises:     every record in the review agenda leaves with a status
                      (planned, not planned, needs discovery, revisit next cycle - max twice)
DevRel promises:      records meet the template; duplicates merged; agenda sent <N> days ahead;
                      requesters told within <N> business days of any status change
Out of scope:         bugs (-> issue queue), security (-> private channel), how-to (-> docs/support)
Staleness:            issues linked to a loop record are exempt from automatic stale closing
Public statements:    DevRel drafts, product approves reasons; no dates unless product publishes them
Missed review:        agenda records keep "under review" with a public note that the review moved;
                      after two misses in a row, DevRel raises it with <product lead's manager>
Review of this agreement: <date, one quarter out>
```

"Revisit next cycle - max twice" is the clause that matters most; it counts per record, and a revisited record stays "under review" publicly with the next review date. Without it, "later" becomes the permanent status of every inconvenient record, and the community reads silence as no.

## Pitching the contract to product

Open with what product gets, not with what DevRel needs.

- **Ask for an hour, not a process.** One review per planning cycle, agenda sent ahead, records already deduplicated.
- **Offer discovery access.** Requesters who agreed to be contacted are interview candidates product does not have to recruit.
- **Bring one traced leak.** A request that came in through three channels, from a paying account, and reached nobody, makes the case better than any framework.
- **Name the cost of not deciding.** Every unanswered request is a public thread where the company looks like it is not listening.

If product declines any standing review, do not build the pipeline yet. Run the leak trace (Step 1), send it to the product lead's manager as a one-page finding, and offer the smallest version: one review per quarter on the top five records.

## Review meeting agenda

```
1. Shipped since last review (2 min) - which records closed, requesters notified?
2. Revisit items from last cycle (10 min) - decide or mark "not planned"
3. New records, blockers first, then by distinct requesters; segment mix and private account
   value shown beside each, never folded into a score (30 min) - status per record
4. Signals without a record yet: emerging themes, sentiment shifts (10 min)
5. Statuses to publish and who drafts each reply (5 min)
```

The output is a status change per record, written into the record before the meeting ends. Minutes without status changes are not a decision.

## Political failure modes and moves

| Failure | Sign | Move |
|---|---|---|
| Product ignores the digest | open rate near zero, no replies | stop the digest; move the same content into the decision review |
| DevRel as unpaid PM | DevRel writes specs, ranks the roadmap, gets blamed for misses | hand the ranking back; send evidence, not priorities |
| Feedback as ammunition | DevRel cites "the community wants" to win an internal argument | show requester counts by segment, including who does not want it |
| Sales override | one account's ask jumps the queue via an exec | log it as a record with its private account value, same review |
| Roadmap leak | DevRel tells the community something is "coming" | only relay statuses product set; no dates |
| Credibility loss | product stops trusting DevRel's records | fewer, evidence-dense records; publish which past records shipped |

Credibility compounds from one habit: track and report which records led to shipped changes. Guillaume Laforge's advice to advocates is the same - "list, and track, and report about all those feedback elements that you bring upstream, and check how it's being enacted or not". A short, maintained list of the top few problems per product area, rather than everything ever heard, is what product keeps reading.

## Bias handling

- **Loudest voice.** Report distinct requesters and representation, not mention counts. Des Traynor's "But 713,000 people want it" is the volume argument product strategy exists to refuse.
- **Biggest customer.** Account value is a legitimate input in a commercial company. Put it beside requester counts so product sees whether the long tail wants the same thing; never let it replace them.
- **Recency.** The thread from yesterday feels urgent. The review agenda orders blockers first, then distinct requesters, not by date.
- **Channel bias.** Social skews to vocal power users, support to dissatisfied users, sales to prospects' perceptions, chat to the most engaged members. A record whose requesters all came through one channel carries that channel's bias; say so in the record.
