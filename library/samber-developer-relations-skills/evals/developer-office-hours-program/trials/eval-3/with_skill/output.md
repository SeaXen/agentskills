# Brimwater AMA: neither kill it nor go weekly. Move it to async for one quarter.

**Next action (10 min):** open one docs ticket titled "SDK init order", and list every sighting from June, July and August in it.

## Verdict

- **Stop the monthly live Zoom.** Run an async question thread for one quarter with the same engineers. Re-test live demand after that.
- **Do not kill it.** The repeat SDK init question shows real demand. The live call is the wrong channel for it.
- **Do not go weekly.** Weekly would multiply empty sessions. It would also need about 6 engineers, and you have 1 (cap arithmetic: engineers ≥ sessions per month + 1).
- **The bar failed on two counts.** June, July and August had a median of 1 asker, and there were 0 docs fixes. The skill's rule is that three sessions under the bar bring the review forward and point to async.

## Open decisions (answer any, charter adjusts)

I could not ask these, so each carries a stated assumption.

1. **User regions.** I assumed no split data, so there is no live slot yet. Send me the split from analytics.
2. **Second engineer plus manager sign-off.** I assumed none yet. Async needs 2 named engineers and 1 spare.
3. **Five unanswered questions from last month.** I assumed SDK init order is one family and four more are findable. The demand gate needs five.
4. **Recording limits.** I assumed none known: no regulated or EU-restricted users, and English only.
5. **Audience.** I assumed paying customers and open-source users, with a support team, a sales contact and a security channel. Fill in the real destinations on the scope card.

## What went wrong, and what leadership should hear

| Signal | Value | Read |
|---|---|---|
| Sessions held / planned | 3 / 4 | September was a silent cancellation, with the Zoom still live |
| Distinct askers | 2, 1, 0 (median 1) | Under the bar |
| Docs fixes merged | 0 | Same SDK init question keeps returning |
| Write-up lag | ~7 days (2 of 3 held sessions published) | The target is 2 business days |
| Engineer coverage | 1 engineer, no backup | One sick day ended September |

- **"3 askers is the benchmark" is not a published benchmark.** No organization publishes office-hours attendance targets. It is a baseline this skill sets, so call it "our target" in front of leadership.
- **The strongest failure is not attendance.** Answers did not change the docs, and the loop was late. Fix those first.
- **Do not report YouTube views as the metric.** Views are viewer vanity, and views do not show the program works. Report distinct askers, repeat families closed and docs fixes. Views can sit beside those as a secondary number.
- **Do not record the drop-in just to produce views.** Recording needs notice, captions and a pre-publication review of every screen-share.
- **Video for views, if leadership insists:** publish a 3-5 minute video that answers SDK init order, linked from the docs fix. That video has a clear purpose and no recording-notice problem.

## Do this week (about 90 min total)

1. **Open the docs ticket** for SDK init order (above). If it is an error or failure, hand the page to `developer-troubleshooting-docs`.
2. **Post the answer** in your community channel today, in 3-4 lines, with a link to the ticket.
3. **Announce the change** wherever the AMA was announced. Say the monthly Zoom is paused, questions go in the thread, and the live decision comes in February 2027.
4. **Remove the active calendar entries.** A calendar showing a session that stopped happening costs more trust than a pause.
5. **Get manager sign-off** for 2 engineers, plus a named spare, at one stint per month each.

## 1. Charter (provisional)

```
Program:        Brimwater Engineering Q&A
Job:            Surface docs gaps (primary). Product signal is secondary.
Audience:       Developers integrating the Brimwater SDKs and API.
Format:         Async intake thread only for the pilot. Drop-in call is the re-test.
Slot:           No live slot. Engineer answer batches Thursdays, weeks 2 and 4 of each cycle.
Staffing:       Host [name], backup host [name]. Engineers [A], [B], spare [C].
                Cap: 1 batch (~75 min) per engineer per month. Manager sign-off in writing.
Scope card:     Section 4 below.
Recording:      None. The text thread is the record.
Outputs:        Write-up within 2 business days of each batch. Docs tickets. Feedback records.
Pilot:          Mon 2026-10-26 to Fri 2027-01-29, three 4-week cycles (see section 3).
                Review Mon 2027-02-01.
Demand bar:     Median ≥ 3 distinct non-staff askers per cycle (self-set, no benchmark),
                and ≥ 1 merged docs fix or feedback record per cycle.
                Below it, keep the thread and fix discovery. Do not return to live.
Operating bar:  No silent cancellation, no engineer over the cap,
                write-ups on time in all but one batch.
```

- **Go-live trigger for the drop-in call:** the demand bar passes in at least 2 of 3 cycles, and 5 or more questions are pre-submitted for the first session.
- **Weekly or livestream trigger:** drop-in sessions regularly run out of time, and the rotation holds 3 or more engineers. Not before.

## 2. Slot plan

- **No live slot now.** Async serves every time zone and survives a week off.
- **When you go live,** put the slot in the largest region's 09:00-18:00. Overlap that with host and engineer hours. Publish it in that region's time zone.
- **Second slot** only when another region reaches 25% of users or more. That threshold is a baseline.
- **Prerequisite:** the region split from analytics. Without it, do not pick a time.

## 3. Rotation calendar (provisional)

The pause on Dec 21-Jan 1 is announced and does not count toward the pilot. Drop it if you work through the holidays.

| Cycle | Dates | Batch Thu wk 2 | Batch Thu wk 4 | Spare |
|---|---|---|---|---|
| 1 | Oct 26-Nov 20 | Eng A (Nov 5) | Eng B (Nov 19) | C |
| 2 | Nov 23-Dec 18 | Eng B (Dec 3) | Eng C (Dec 17) | A |
| Pause | Dec 21-Jan 1 | announced | announced | - |
| 3 | Jan 4-Jan 29 | Eng C (Jan 14) | Eng A (Jan 28) | B |

- **Spare:** the month's spare covers any dropped batch. A covered batch counts against the spare.
- **Credit:** name the engineer and their team in each write-up.
- **Prep brief:** send it 48 hours before each batch, with the triaged questions and the scope card.

## 4. Scope card (ready to publish, edit the bracketed parts)

```
## What to bring to Brimwater Engineering Q&A

Bring: "my SDK returns the default flag value right after startup",
"how do I bootstrap flags for server-side rendering",
"what happens to evaluations when the streaming connection drops".
Not here:
- Account, billing, plan or contract questions → [support link]
- Pricing or paid-tier questions → [sales contact]. We answer only what the public docs say.
- A suspected security vulnerability → [security disclosure channel]. Never post it in the thread.
- A bug you can reproduce → [issue tracker]. We will help you write the report.
- A feature you need → we log it in [feedback record]. The product team decides.
- Debugging your own environment → we can't see it. Bring a minimal reproduction, secrets removed.

This program is text only. Your post is the record, public and permanent.
Never post logs, keys or customer data. Moderators redact posts that do.
Our code of conduct applies: [link].
```

**Intake form, 6 fields only:**
1. The question, in 1-2 sentences.
2. What you tried, and the docs page you read.
3. SDK and version.
4. May we quote the question? Yes / Anonymise / No, answer in the write-up only.
5. Time zone (optional).
6. Contact for follow-up (optional). If you raise a feature request, may we keep your handle on it? Yes / No.

Do not ask for logs, configs or screenshots in the form.

**Cycle timeline for each batch:**

| When | Action |
|---|---|
| T-72h | Nudge the thread with the engineer's name and area |
| T-48h | Triage the queue, send the prep brief |
| T+2 business days | Publish the write-up |

**Triage buckets:** answer in batch, answer in a link, redirect, docs gap, log for product. A docs gap is any question seen a second time. Group variants into one family first (all "init order" variants are one). Never silently drop a question.

## 5. Session log and write-up skeletons

**Log columns per batch:** date, held or cancelled, distinct non-staff askers, answered, redirected, docs tickets opened, docs fixes merged, feedback records, engineer, write-up lag in days.

```
## Brimwater Engineering Q&A - [date], with [engineer], [area]

### Answered
- **[Question, in the asker's words]** - [answer, 2-4 lines] - [docs link or new ticket]

### Redirected
- [Topic] → [destination]. (No names.)

### Logged for the product team
- [Request, in the user's words] → [feedback record link]

### Docs we are fixing
- [Page] - [what was missing] - [ticket]

Next batch: [date]. Submit questions: [link].
```

Copy consented handles onto logged feature requests, then delete the raw log. Label resulting issues and docs changes "Office Hours" so the review can count them.

## 6. Measurement table

| Signal | Current | Target |
|---|---|---|
| Sessions held / planned | 3 / 4 | All held, none silent |
| Held with zero askers | 1 (August) | Tracked |
| Median distinct askers | 1 | ≥ 3 per cycle (self-set) |
| Questions answered | not measured | All answered or redirected |
| Write-up on time | 0 of 2 published | Within 2 business days |
| Docs fixes + feedback records | 0 | ≥ 1 per cycle |
| Engineer sessions per month | 1 engineer, no spare | None over cap, spare named |

## Pilot review on Feb 1, 2027

- **Both demand-bar items pass:** book a drop-in call, with the 5-question pre-submit gate.
- **Either fails:** keep the thread another quarter. Check the promotion and the docs placement before adding live time.
- **Operating bar fails:** fix the rotation first. It never decides whether to stop.
- Everything after the pilot is provisional.

**Next:** open the SDK init order docs ticket now, then send me your region split and the five unanswered questions. I will lock the charter and the first live slot.