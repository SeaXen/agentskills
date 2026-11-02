**Do not build the intake pipeline yet.** The skill says that when nobody on product owns decisions, you do Steps 1–2 (leak trace, contract pitch) and stop. Intake feeding nobody gives you a better-organized pile. A public voting board with no decider adds visible unanswered asks.

So I am not delivering the label taxonomy or the PM digest. Reasons:
- **Taxonomy:** it is built in the area and segment names product uses, so it waits for a receiver.
- **Digest:** the skill rates it lowest value, since it informs and decides nothing. Product ignoring a digest is a named failure mode. A solo DevRel at about 35–40 requests a week also has too few hours to run it.
- **"Voted, then they will come around":** that is the vote-count failure mode. Votes are a signal beside distinct requesters by segment, not a lever on PMs.

Your deadline is the planning cycle in 7 weeks. The portal arrives in 2 weeks, so you have time to get an owner first.

## Deliverable 1: Leak trace

Run this week. Estimate: 2–3 hours, a planning figure, not a benchmark.

1. Sample 25 requests from the last 60–90 days. Take the most recent ones, never the memorable ones.
   - Discord #feature-requests: 12
   - Support tickets: 6
   - GitHub issues: 6 (3 Node SDK, 3 Go SDK)
   - Keep duplicates in the sample and mark them. The duplicate rate is a finding.
2. Fill one row per request:

| # | Channel | Date asked | Captured in a record? | Reached product? | Decision recorded? | Requester told? | Days to first staff reply |
|---|---|---|---|---|---|---|---|

3. Use these rules:
   - **Captured:** written anywhere durable beyond the original message. A ticket note, a DM to a PM or an issue all count.
   - **Reached product:** an agenda, comment or ticket that a PM saw.
   - **First reply:** from staff only. Peer answers and bots do not count. Leave the cell empty for unanswered requests and count them separately.
4. Read it as a funnel: captured ÷ asked, reached ÷ captured, decided ÷ reached, told ÷ decided. Fix the stage that loses most.
5. Expect decisions only on GitHub issues. They have a built-in reply path. Treat a high "told" rate as a symptom, not a win.
6. Pick one problem asked through two or more channels that reached nobody. That row is your pitch.

Stage table, to fill in:

| Stage | Count | Ratio | Lost |
|---|---|---|---|
| Asked | 25 | | |
| Captured | | | |
| Reached product | | | |
| Decision recorded | | | |
| Requester told | | | |

With nobody owning decisions, I predict the decision stage loses most. That is a prediction. Your trace decides.

## Deliverable 2: Product contract

### Decision rights

| Decision | You (DevRel) | Product |
|---|---|---|
| Capture, merge, label, write evidence | owns | may send back |
| What gets built, when | informs | **owns** |
| Planned / not planned / shipped status | relays | **sets** |
| Public wording of a no | drafts | approves the reason |
| Telling community requesters | owns | none |
| Dates in public | never | only if committed and published |

### Working agreement, one page

Send this to the PMs. Fill in the angle-bracket values.

```
Developer feedback loop - working agreement (Fernhollow)

Record of truth:   <the portal, or product's existing idea space - decide in the pitch>
Product receiver:  <PM name> per area (queue API / Node SDK / Go SDK), backup <PM name>
Review:            one 45-minute review before Q3 planning, then each planning cycle,
                   chaired by product
Product promises:  every record on the agenda leaves with a status
                   (planned, not planned, needs discovery, revisit next cycle - max twice)
DevRel promises:   records are problem-first with evidence; duplicates merged; agenda sent
                   3 business days ahead; community requesters told within 5 business days
                   of a status change
Support promises:  support tells the requesters who came through tickets
Out of scope:      bugs -> issue queue; security -> private channel; how-to -> docs/support
Staleness:         GitHub issues linked to a record are exempt from auto-close
Public statements: DevRel drafts, product approves reasons; no dates unless product publishes
Missed review:     records keep "under review" with a public note; two misses in a row
                   go to <PMs' manager>
Review of this agreement: one quarter after signing
```

The clause that matters most is "revisit next cycle, max twice". Without it, "later" becomes every status.

### Pitch to the PMs

You are asking for an hour, not a process. They said they are slammed, so lead with that.

1. **Ask:** "One 45-minute review in week 6, before planning. I send the agenda 3 days ahead, already deduplicated."
2. **Offer:** "Requesters who agreed to be contacted are interviewees you don't have to recruit."
3. **Evidence:** show the one traced request from the trace, asked in 2+ channels and decided by nobody.
4. **Cost of not deciding:** every unanswered request is a public thread where Fernhollow looks like it is not listening.
5. **Show the pile organized.** It costs them nothing to read and is your only leverage.

### Timeline

| When | Action |
|---|---|
| Week 1 | Run the trace. Book 30 minutes with both PMs. Pitch the contract. |
| Week 2 | Contract signed, or escalate. Portal goes live but is not announced publicly. |
| Week 3 | If still unsigned: send the trace to the PMs' manager as a one-page finding. Offer the smallest version, one review on the top five records. |
| Weeks 3–5 | Once signed, build intake: routing table, label set, status vocabulary, backfill of the largest clusters. |
| Week 6 | Review 1, before planning. |

Do not announce the portal or open voting until a receiver is named. A public board promises developers an answer.

## Open questions

Intake design needs these answers:
- **Hours:** how many hours a week can you give this? At about 5 minutes per request, 35–40 requests a week is about 3–3.5 hours.
- **Public roadmap:** is one allowed, and who may say no in public?
- **Priority:** what does product say decides priority today? What does leadership expect from this work: a report, a number, or nothing?

Next: open #feature-requests and copy the 12 most recent requests into the sheet.