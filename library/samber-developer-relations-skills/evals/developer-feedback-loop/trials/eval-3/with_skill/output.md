**Do now (5 min):** message Tomas. Ask him to fix the date of review 1 in week 3. Do not ask for the planning seat yet.

Your plan breaks on hours, so I cut part of it. 15 + 35 + 9 = 59 requests a week. 180 min ÷ 59 is about 3 min per request. The skill's line is 5 min. Below it, logging every request is impossible and the digest goes.

I produced only deliverable 3 (the intake spec). Deliverables 1, 2 and 4–7 are not done. Tomas's agreement stands in for the contract. The leak trace is not run and is week 1 below.

## Your plan, checked

| Your plan | Verdict | Why |
|---|---|---|
| Log every request with full context | **Cut** to paying accounts and blockers, max ~6 a week | 59 × 5 min = 4.9 h, more than your whole budget. Tomas also cannot decide 250 records in a monthly hour. |
| Friday digest | **Deleted** | It informs and decides nothing. The 0.5 h goes to the decision review. |
| Ask for a planning seat now | **Postponed** to review 3 (~week 11) | The seat is the costliest ask. Make it after two reviews have produced statuses and records have shipped. Asking now risks the monthly review you already have. |

## Intake spec

### Assumptions to confirm (tell me which are wrong)

1. Tomas's backlog tool takes a form or email-in, and a "feedback" item type with a filtered view.
2. The Python SDK repo is public. The API is closed.
3. Support can add a ticket tag and a macro.
4. The 3 h a week excludes content, and you work alone (no moderators).
5. Segment names come from Tomas's tool. I use free, paid, enterprise and prospect as placeholders.

### Re-ranking block

```
- Board review in 4 weeks: redirect-to-record and one decision review promoted;
  planning seat demoted.
- Still running in a year: planning seat and quarterly report kept, sequenced
  after two review cycles (seat asked at review 3, first quarterly report ~week 13).
- 3 h/week for ~59 requests/week (~3 min each): log-on-behalf only for paying
  accounts and blockers; weekly digest deleted.
- Closed API + public SDK repo: Tomas's backlog is the record of truth for
  decisions; SDK issues stay on GitHub, linked one-to-one from a backlog item.
- Private record: the redirect points to a public intake form, and status replies
  go to the channel where the requester asked.
```

### Record of truth

- **Tomas's backlog tool**, with type "feedback" and a view.
- Two views:
  - **Inbox:** raw form submissions. Only you see it.
  - **Agenda:** merged records you have sent for review. Tomas reads only this one.
- Keep account names, revenue and ticket text out of any public text.
- **SDK feature requests** stay as GitHub issues. Each links to its backlog record.
- Exempt linked issues from the stale bot. A bot closing an "under review" request reads as a no nobody decided.

### Routing table

| Channel | Weekly volume | Capture move | Owner | Notes |
|---|---|---|---|---|
| Discord | ~35 | Reply with the form link (this is the "received" reply). Weekly sweep of threads with no link. | You | Answer how-to in place. Send bugs to support. |
| Support | ~15 | Agent tags the ticket and pastes the macro with the form link. You sweep the tag weekly. | Support, you | Support tells its own requesters. Ticket text is never copied public. |
| GitHub, SDK | 8–10 | Features stay as issues, linked to a record. Bugs stay in the issue queue. | You | See `oss-issue-triage` for the queue. |
| Sales, CS | not stated | Add a row if prospects ask for things. Use the segment "prospect"; the opportunity reference stays private. | Sales | None today. |

**Form fields (5):**
1. What were you trying to do?
2. What stopped you?
3. Current workaround.
4. Severity: blocker, slows down, or cosmetic.
5. OK to contact you? (This is the consent field.)

### Capture rules

- Write every record problem-first. The title names the problem in the developer's words. The requested fix has its own field.
- When a request arrives as a solution, ask one question: "what were you trying to do when you needed this?"
- Count distinct requesters, once per record across channels. Report reactions beside that count.
- Merge on the same problem, not the same request. Split when different problems sit behind one request.
- **Log on behalf** (full evidence, ~10 min each) only for:
  - paying accounts, and
  - blockers.
- Cap it at about 6 a week.
- Keep the review agenda to at most 8 records. This is a planning figure; 8 records fit a 60-min review.
- Mark the rest "received", with a note that they wait for the next cycle.

### Hour budget (steady state, 3.0 h a week)

| Task | Hours/week |
|---|---|
| Redirect replies (Discord) | 0.5 |
| Weekly sweep (Discord, support tag, GitHub) | 0.6 |
| Log on behalf (paying, blockers, max ~6) | 0.5 |
| Merge and dedup | 0.3 |
| "Under review" replies at agenda freeze | 0.1 |
| Decided statuses, batched after each review | 0.3 |
| Review prep and attendance (~2 h a month) | 0.5 |
| Quarterly re-trace (~1.5 h a quarter) | 0.1 |
| **Total** | **2.9** (0.1 buffer) |

- Log on behalf is the elastic line. The weekly trace may show that bugs and how-to questions make up most of the 59. If so, move the freed hours to logging and sweeping.
- The weekly count of 59 includes bugs and how-to questions. I did not guess the feature-request share. Week 1 measures it.

### Out-of-loop routes

- **Bugs:** support or the GitHub issue queue.
- **Security reports:** the private disclosure channel, never a public thread or the form.
- **How-to questions:** support and docs.
- **API preview or design-partner feedback:** that program's own cadence.

### First 4 weeks

| Week | Hours | Work |
|---|---|---|
| 1 | 3.0 | Leak trace on 20–30 recent requests, at least 3 per channel (~1.5 h). Build the form, views, status labels, support macro and tag (~1.5 h). |
| 2 | 3.0 | Redirects start (0.5). Backfill the largest clusters, up to 8 (~2 h). Freeze the agenda 3 business days before review 1. Send "under review" replies. |
| 3 | 3.0 | Review 1, 60 min, chaired by Tomas. Write every status into its record before the meeting ends. |
| 4 | 3.0 | Batched replies on every status set at review 1, in the requesters' channels. Board slide (~1 h, taken from the sweep). |

- Review 1 must land by the end of week 3. Otherwise the board has no decisions to show.
- The week 1 trace is also your baseline for the board slide.

### What the board sees

- The leak trace baseline from week 1.
- Review 1: records decided out of records on the agenda, and requesters told within 5 business days.
- Do not claim shipped-from-feedback unless a change traces to a record that existed before the work was scheduled and is linked from its release note. Zero is an honest number.
- Re-trace in week 13 gives the after.

**Next:** message Tomas today to fix the week-3 date for review 1. That unblocks the 4-week timeline.