**Next action:** triage the 30 forum questions into the five buckets in section 4. That takes about half a day for one DevRel, and it becomes the first agenda and the first write-up.

Your two proposals rank last and second to last. The recommended program is an async intake thread plus a biweekly drop-in call, with a published rotation.

## Open decisions (needed before the first session)

The skill gates the format on six interview answers. You gave three. Everything below is provisional until you confirm these:

1. **Region and time zone.** You said staff and users share one zone. Which one? Poll users before fixing the slot.
2. **Names and caps.** Which 4 engineers and 2 DevRel? How many sessions can each hold on a bad month? Has each engineer's manager agreed in writing?
3. **Support and security channels.** Is there a support team, a sales contact and a private security channel? Are your users paying customers, open-source users or both?
4. **Recording limits.** Is there anything that can never appear on a recording (customer data, unreleased features, regulated or EU users)? Which language will sessions run in?
5. **Start date and promotion.** Is this a standing program or one AMA for a launch? A one-off AMA is out of scope for this skill. Which channels already reach your users?

## 1. Ranking for your job: hear product feedback

Your answers moved the ranking in four places:

- **30 unanswered questions:** the demand gate (5 or more unanswered) passes, so live formats are allowed.
- **Job is product feedback:** the drop-in call is promoted, because follow-up questions in conversation produce the richest requests.
- **4 engineers:** cadence is capped at biweekly. Weekly needs about 6 engineers.
- **No support team mentioned:** the staffed queue loses its only justification.

The ranking:

1. **Drop-in call plus async intake (recommended).** It is a biweekly fixed slot with one DevRel host and one rotation engineer, taking pre-submitted questions first. It gives the deepest back-and-forth and the best product signal, at about half a staff-day per cycle.
2. **Async thread only (week 0 to 2, and permanent as the intake).** It costs an hour or two a week and serves every time zone. It is the right way to clear the 30 backlog questions before going live. It never tests whether people will show up for a person, so it is not enough alone.
3. **Livestream panel with 3 engineers (your proposal; postpone).**
   - It has the highest reach and value, but it breaks the engineer cap. Biweekly needs 6 engineer seats a month, and 4 engineers at one session each give 4. Even monthly uses 3 of 4 seats with one spare, so there is no slack.
   - It needs a panel and production every session.
   - It cannot do live debugging, and a one-way show gives product weaker feedback than a conversation.
   - It also carries the heaviest compliance cost: recording notice, consent, captions and pre-publication review.
   - Promote it when drop-in sessions regularly run out of time, the rotation holds 3 or more people, and the audience is big enough that one answer serves dozens.
   - The cap arithmetic is my reading of the skill's per-session cap applied to panel seats.
4. **Booked 1:1 slots.** They go deepest per asker, which suits feedback, but cost an hour per asker and have no reach. Promote them only for partners or plugin authors who need their own code on screen. If you run them, never record them, and keep their notes internal-only.
5. **Discord office-hours channel with a 1-hour answer promise (your proposal; delete).**
   - This is a staffed queue, which is a standing support job. The skill says to delete it unless a support team owns it.
   - Stripe promises 15 minutes on published Monday-to-Friday hours with a staffed team. Two DevRel cannot cover business hours through holidays and sick days, and one broken promise teaches users the channel is unreliable.
   - A second surface also repeats the forum problem: 30 questions already sit unanswered.
   - Whether to open a Discord at all is a separate decision, covered by `developer-community-launch`.
   - If you want a speed promise anyway, publish a softer one for the async thread, for example "triaged within 1 business day". That figure is my baseline; replace it after the pilot.

No organization publishes office-hours attendance or deflection benchmarks. Every target below is self-set.

## 2. Charter (one page)

```
Program:        Ossifer Office Hours
Job:            Product signal (hear feedback directly from users)
Audience:       Ossifer users (paying/OSS: open decision 3), all levels
Format:         Drop-in call + async intake thread
Slot:           One slot, biweekly, anchored in the users' time zone (set by poll)
Staffing:       Host H1, backup host and notetaker H2; engineers E1-E4, cap 1 session/month each
Scope card:     Section 5, published before S1
Recording:      None. Write-up published instead, so users speak freely
Outputs:        Write-up within 2 business days; docs tickets; feedback records
Pilot:          Backlog sprint Oct 26 - Nov 6, 2026. 6 sessions, Nov 12, 2026 - Feb 4, 2027. Review week of Feb 8, 2027
Demand bar:     Median >= 3 distinct non-staff askers per cycle (live or async) AND >= 1 merged docs fix + feedback record per 2 sessions. Below it, drop to async-only for a quarter and re-test
Operating bar:  No silent cancellation, no engineer over the cap, write-ups on time in all but one session
```

Notes on the charter:

- **Feedback bar:** because the job is product signal, consider raising the feedback-record target to at least 1 per session. That is my suggestion and it is self-set.
- **Notetaker:** invite a product manager as a second notetaker so product hears users first-hand. This is optional.
- **Routing to product:** the skill hands routing of feedback into product decisions to `developer-feedback-loop`.
- **Empty room:** hold the slot even with an empty queue. After 10 minutes with nobody in the room, answer the forum backlog for the write-up, then close. Two empty sessions in a row means change the slot and promotion before the cadence.
- **Cycle timeline:** nudge the intake thread at T-72h. At T-48h, triage the queue and send the engineer the prep brief and scope card. Publish the write-up at T+2 business days. The T-24h cancel check applies to livestreams only.

## 3. Slot plan

1. Split active users by region. You say one zone, so there is one region and no second-slot trigger. A second slot applies only if another region reaches 25% of users.
2. Intersect the users' 09:00-18:00 with host and engineer hours. Break ties toward the slot cheapest for hosts.
3. If the overlap is empty, push the cost onto staff and take the slot at the hosts' end of day.
4. Poll users, then publish the slot in the users' local time with a calendar link.
5. Anchor it in that time zone. Clock changes in other regions shift the gap for a few weeks.
6. Give any user outside 09:00-18:00 a named async path: the intake thread and the write-up.

## 4. Rotation calendar (one quarter, provisional)

Dates assume Thursday. Shift them to match the poll. If you have US users, Nov 26 is Thanksgiving, so move S2. Dec 24 is an announced pause, and paused dates do not count as sessions. H1 hosts every session, and H2 takes notes.

The cap check is that no engineer has more than 1 session in any month. The month's spare engineer is the backup for every session that month.

| Session | Date | Engineer | Backup |
| --- | --- | --- | --- |
| S1 | Thu Nov 12 | E1 | E4 |
| S2 | Thu Nov 26 | E2 | E4 |
| S3 | Thu Dec 10 | E3 | E4 |
| Pause | Thu Dec 24 | - | announced pause |
| S4 | Thu Jan 7 | E4 | E2 |
| S5 | Thu Jan 21 | E1 | E2 |
| S6 | Thu Feb 4 | E2 | E3 |

Before S1, send each engineer the prep brief with the pre-submitted questions and the scope card, and get manager sign-off. Credit each engineer and their team by name in the session and the write-up.

**Backlog triage for the 30 forum questions** (the skill's five buckets):

1. Answer live: needs explanation or a judgement call, and is useful to others. Most widely useful first.
2. Answer async: a one-link answer, or the asker cannot attend. Goes in the write-up.
3. Redirect: matches an out-of-scope line on the scope card. Send it to the named destination with a personal note.
4. Docs gap: docs should already answer it, or it is the second sighting. Answer it live, then open a docs ticket.
5. Log for product: a feature request or bug. Record it in the user's words.

Group repeat questions into families before opening docs tickets, so each family gets one ticket.

## 5. Scope card (ready to publish)

Replace the examples with real questions from your forum, in your users' words. Replace the bracketed destinations with real links.

```
## What to bring to Ossifer Office Hours

Bring: "my index build stalls at high ingest rate", "how do I size shards for 50M vectors",
"is this filter query supposed to be slow", "what changed in the upgrade from vX to vY".
Not here:
- Account, billing, plan or contract questions -> [support link]
- Pricing, licensing, paid-tier features -> [sales contact]. We answer only what the public docs say.
- A suspected security vulnerability -> [security disclosure channel]. Never raise it live or in a public thread.
- A bug you can reproduce -> [issue tracker]. We will help you write the report if you bring it.
- A feature you need -> we log it live in [feedback record]; the product team decides.
- Debugging your own environment -> we can't see it. Bring a minimal reproduction with secrets removed.

Sessions are not recorded. We publish a write-up within 2 business days at [link].
Our code of conduct applies: [link].
Never post logs, keys or customer data in the intake thread. Moderators will redact it.
```

**Intake form (6 fields only):**

1. The question, in 1-2 sentences.
2. What you tried, and the docs page you read.
3. Product and version.
4. May we read the question out? Yes, anonymise it, or no (answer in the write-up only).
5. Time zone (optional).
6. Contact for the follow-up (optional). If you raise a feature request, may we keep your handle on it so you hear the decision?

Never ask for logs, configs or screenshots in the form.

## 6. Session log and write-up skeletons (empty)

**Session log columns:** date, held or cancelled, distinct non-staff askers (live or async), answered live, answered async, redirected, docs tickets opened, docs fixes merged, feedback records, engineer present, write-up lag in days.

**Write-up skeleton:**

```
## Ossifer Office Hours - [date], with [engineer], [area]

### Answered
- **[Question, in the asker's words]** - [answer, 2-4 lines] - [docs link or new docs ticket]

### Answered here, not live
- **[Question]** - [answer]

### Redirected
- [Topic] -> [destination]. (No names.)

### Logged for the product team
- [Request or bug, in the user's words] -> [feedback record / issue link]

### Docs we are fixing
- [Page] - [what was missing] - [ticket]

Next session: [date, time in users' zone, calendar link]. Submit questions: [link].
```

After each session:

- Publish the write-up within 2 business days.
- Open a docs ticket the second time any question family appears, in any channel.
- Log every feature request and bug in the user's words. With consent, copy the handle into the record so they hear the decision. Then delete the raw session log.
- Label resulting issues and docs changes "Office Hours" so the pilot review can count them.

## 7. Measurement table (not measured yet)

| Signal | Target | Current |
| --- | --- | --- |
| Sessions held / planned, and held with zero askers | All held; none cancelled silently | Not measured yet |
| Distinct non-staff askers per cycle | Median >= 3 (self-set) | Not measured yet |
| Questions answered live + async | All answered or redirected | Not measured yet |
| Write-up within 2 business days | All but one | Not measured yet |
| Merged docs fixes + feedback records | >= 1 per 2 sessions (consider raising feedback records) | Not measured yet |
| Engineer sessions per month | No engineer over 1 | Not measured yet |

Everything past the pilot is provisional.

**Next:** reply with answers to the 5 open decisions. Then start triaging the 30 forum questions.