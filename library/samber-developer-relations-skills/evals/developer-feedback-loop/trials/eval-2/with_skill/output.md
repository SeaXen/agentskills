# Quillbrook feedback loop: leak trace and product contract

**Fix the decision stage first, not capture.** Capture and decision each lose 10 requests, so the stages tie. Your receiver question breaks the tie, and your sample probably hides the true size of the capture loss. Capture rules still get built, in parallel with the contract (see 2).

## 1. Leak trace

| Stage | Count | Ratio | Lost |
|---|---|---|---|
| Asked | 24 | n/a | n/a |
| Captured (ticket note, DM to Ruth, or issue) | 14 | 58% of asked | **10** |
| Reached Ruth | 13 | 93% of captured | 1 |
| Decision recorded | 3 | 23% of reached | **10** |
| Requester told | 3 | 100% of decided | 0 |

**Why the tie goes to decision.** When two stages lose about the same, the fix follows who receives feedback today. Ruth is an informal receiver: she reads your DMs when you ping her, with no agreed review and no promise of a status. In that case the skill runs the contract first and designs intake alongside it.

**Why capture rules alone would backfire.** They would push more records toward a stage that decides 3 of every 13. You would get a bigger pile that nobody decides on.

**The 100% "told" rate is a symptom.** Your three decided requests almost certainly came through a path with a built-in decision step. That could be a public issue or an AE's note. Check which path each one took. It is the best evidence for how the loop should work.

**Reading "reached Ruth" with care.** It means you pinged her. It does not mean she reviewed the request. The 93% is the weakest number in the table.

### Why this sample can't be trusted for ratios

- **You picked the most-reacted requests.** The skill samples the most recent requests per channel, because popular ones are the ones that already got attention. Heavy reactions make a request likelier to be captured, so your 58% is probably flattering. True capture loss is likely above 10 of 24. That is why I would not call capture the smaller problem.
- **You covered only Discord and the forum.** You have open-source clients, so GitHub issues are a channel. Support belongs in the sample too, if you have it.
- **Sales is missing.** I know two AEs send a couple a quarter. Include them anyway, from memory or email: the skill wants at least 3 rows per channel so a quiet channel still shows. Its capture rate is 0% by definition, and that is a finding.
- **Removing the four duplicates hid a signal.** Keep duplicates in the sample and mark them. Four of 28 is 14% duplicates, even in a pile filtered for popularity. It means the same problem is asked in several places and nobody merges it.
- **The 6-minute first response doesn't count.** The Discord bot's acknowledgement is excluded. Mods are community members, so they are not staff either. Your real staff time-to-first-reply on feature requests is unknown. Add it as a column in the re-trace.

**Next action:** re-pull 3 to 5 of the most recent requests per channel (Discord, forum, GitHub issues, support, sales). Keep the duplicates and mark them. Re-run the table. Treat today's numbers as provisional until then.

## 2. Product contract with Ruth

**Decision rights:**

| Decision | DevRel (you) | Product (Ruth) | Support / Sales |
|---|---|---|---|
| Capture and link a request | owns | n/a | owns for their channel |
| Merge, split, label | owns | may correct | n/a |
| What gets built, when | informs | **owns** | informs |
| Status: planned / not planned / shipped | relays | **sets** | n/a |
| Public wording of a no | drafts | approves the reason | n/a |
| Telling requesters | owns | n/a | owns for their accounts |
| Dates in public | never | only if committed | never |

**Draft working agreement**, one page, stored next to the record of truth:

```
Developer feedback loop - working agreement (Quillbrook)

Record of truth:   <decide in intake spec; likely a public tracker for the OSS clients,
                   linked one-to-one from Ruth's own backlog items>
Product receiver:  Ruth, backup <name needed>
Review:            per planning cycle, 60 min, chaired by Ruth, scheduled before planning
Product promises:  every record on the agenda leaves with a status
                   (planned, not planned, needs discovery, revisit - max twice per record)
DevRel promises:   records meet the template; duplicates merged; agenda sent 3 business days
                   ahead; community requesters told within 5 business days of a status change
Sales/support:     AEs write the problem in the customer's words and tell their requesters
Out of scope:      bugs -> issue queue, security -> private channel, how-to -> docs/support
Staleness:         issues linked to a loop record are exempt from automatic stale closing
Public statements: DevRel drafts, Ruth approves the reason; no dates unless product publishes them
Missed review:     agenda records stay "under review" with a public note that the review moved;
                   two misses in a row, DevRel raises it with Ruth's manager
Review of this agreement: one quarter out
```

The clause that matters most is "revisit, max twice". Without it, "later" becomes the permanent status and the community reads silence as a no.

**The pitch to Ruth.** Open with what she gets, not with what you need:

- **It costs her one hour per planning cycle.** The records arrive already deduplicated, with evidence and a count of distinct requesters by segment. She doesn't have to be pinged.
- **She gets discovery contacts.** Requesters who agreed to be contacted are interview candidates she would otherwise have to recruit.
- **The trace is the proof.** Of 13 requests that reached her, 10 never got a decision. Bring one concrete example: a request asked in several places, from a paying account, that never got an answer. Pick it from your data, and use the re-pulled sample if it gives a better one.
- **Unanswered threads are public.** Each one looks like Quillbrook isn't listening, and the Discord bot's instant acknowledgement makes that worse.
- **If Ruth declines a standing review,** don't build the pipeline. Send the leak trace to her manager as a one-page finding. Offer the smallest version: one review per quarter on the top five records.

## 3. Open questions

I need answers to these before the intake spec, handoff calendar and metric sheet:

1. **Hours:** how many hours a week can the feedback work get, and from whom (you, support, mods)?
2. **Date:** is there a planning cycle, launch or board review this must feed?
3. **Scope:** do you want to clear today's pile once, or run a loop that still works next year?
4. **Volume and channels:** roughly how many requests a week per channel, and is there a support or GitHub issues stream beyond Discord and the forum?
5. **Tracking:** where does Ruth track ideas and planned work, can developers see it, and what are your product areas called there?
6. **Public rules:** who may say no in public, and is a public roadmap allowed?
7. **Leadership:** do they expect a report, a number, or nothing from this work?
8. **Your three decided requests:** which path did each take, and who decided?

Once I have these, I'll write the intake spec, including the capture rules you were drawn to. Those rules still matter, and they feed the first review.