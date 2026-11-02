# Lanternfold office hours: plan

## Open decisions (answer these first)

1. ⚠️ **Do not launch a weekly livestream next Thursday (2026-10-29).** Two gates fail today (details below). Launch the async intake that day instead.
2. Where are your users, by region? I need a rough split from SDK download, docs or Discord analytics. The slot depends on it.
3. What is the one job: unblock users, find docs gaps, hear product feedback, or grow contributors? I assumed **find docs gaps and hear product feedback** for a beta SDK. Change it if wrong.
4. Have the two engineers' managers agreed to a cap in writing? Who is your backup host? Can anyone in the rotation shift their day for a late slot?
5. What can never be on a recording: customer data, unreleased features, regulated or EU attendees? Which language do sessions run in?
6. Do you have a support team, a sales contact, and a security disclosure channel? Which channels reach your developers (Discord, newsletter, GitHub, X)?
7. Can you recruit a third engineer? That decides weekly vs biweekly vs monthly.

I filled the plan with placeholders marked `[ ]` where an answer is missing.

## Why not a weekly livestream now

| Gate | Your situation | Result |
|---|---|---|
| Demand: 5 nameable questions from the last month that the docs did not answer | About 2 support questions plus 1 Discord thread | ❌ Delete every live format for now |
| Rotation: at least 3 people, with weekly needing about 6 engineers | You plus 2 engineers who join "when they can", no cap, no manager sign-off | ❌ Delete the livestream panel |

- **"It will grow once people hear about it" is untested.** Test it cheaply: announce an async thread and see if questions arrive.
- **Weekly with 2 engineers breaks the cap.** The cap is at most one session per engineer per month, and engineers must number at least sessions per month plus one spare. Weekly means about 4 sessions a month, so about 5 engineers. Biweekly with 2 engineers means no spare, so one absence cancels a session. "When they can" is the goodwill-rotation failure: engineers are gone by week four.
- **Weekly before demand is the "launch-weekly" failure.** Empty livestreams make poor YouTube content and teach users the program is dead.
- **The YouTube goal is a separate job.** A recording is a side effect of a livestream panel. It is a good second step, not the launch format. See "YouTube" below.
- **No benchmark exists for office-hours attendance.** Every target here is self-set (baseline).

## 1. Charter (provisional)

```
Program:        Lanternfold Office Hours
Job:            Surface docs gaps + product signal (assumed; confirm)
Audience:       Developers using the event-streaming SDK, public beta
Format:         Async intake from 2026-10-29. Then drop-in call (host + 1 engineer).
                Livestream panel later, only after the promotion trigger below.
Slot:           Thursday, [time] in the largest region's time zone, [cadence]. See slot plan.
Staffing:       Host [you], backup host [ ]; engineers A, B, C [C to recruit]; cap 1 session/month each
Scope card:     Section 4, published before the first live session
Recording:      Drop-in: record only with notice, or publish the write-up only.
                Reviewed before publishing by [name]. Retention [ ] (legal owns the wording for EU).
Outputs:        Write-up within 2 business days; docs tickets; feedback records
Pilot:          First live session 2026-12-03 to review 2026-03-04, 6 sessions (baseline)
Demand bar:     Median ≥ 3 distinct non-staff askers per cycle, live or async (self-set),
                AND ≥ 1 merged docs fix or feedback record per 2 sessions.
                Below it -> async thread for a quarter, then re-test.
Operating bar:  No silent cancellation, no engineer over the cap,
                write-ups on time in all but one session.
```

- **Announced pauses do not count as sessions.** The pilot extends instead.
- **Livestream promotion trigger:** drop-in sessions regularly run out of time AND three or more engineers are in the rotation. Then the recorded panel starts, with captions and a pre-publication review.

## 2. Slot plan (provisional until the region split exists)

1. Split active users by region. Treat zones as one region when a single slot reaches all of them inside 09:00-18:00.
2. Intersect the largest region's 09:00-18:00 with your and the engineers' hours.
3. If the overlap is empty, staff absorbs the cost: take the slot at your end of day, never the users' evening.
4. Write the slot in every region's local time. Any region outside 09:00-18:00 gets the async thread as its named path.
5. Poll the audience in the intake thread before fixing the slot. Publish it in the largest region's time zone with a calendar link. Give UTC only next to a date.
6. Anchor to the audience's time zone. EU and US change clocks on different weekends, so the gap shrinks by an hour for 2-3 weeks in spring and about a week in autumn.

Worked example from the skill: Paris hosts and 70% US users give 12:00 ET / 09:00 PT (18:00 Paris), published as "12:00 ET / 09:00 PT", never "18:00".

**Coverage pattern:** one slot plus async intake. Add a second slot only when a second region reaches 25% of users (baseline) and the rotation can staff both within the cap.

## 3. Timeline and rotation calendar (provisional)

| Date | Action |
|---|---|
| Thu 2026-10-29 | Launch the async intake: pinned thread plus form, scope card pinned, "no logs, keys or customer data" rule |
| Weekly to Thu 2026-11-19 | Answer in batches (1-2 hours a week). Track unanswered-by-docs questions. Poll time zones. Get manager sign-off. Recruit engineer C |
| Thu 2026-11-19 | **Demand and rotation check:** 5 named docs-unanswered questions and 3 engineers signed? If yes, announce Dec 3. If no, keep async and re-check in 3 weeks |
| Thu 2026-12-03 onward | Drop-in pilot |

**With 3 engineers, biweekly:**

| Date | Engineer | Backup |
|---|---|---|
| Thu 2026-12-03 | A | C |
| Thu 2026-12-17 | B | C |
| Thu 2027-01-14 | A | C |
| Thu 2027-01-28 | B | C |
| Thu 2027-02-11 | A | C |
| Thu 2027-02-25 | B | C |

- **C is the monthly spare and the backup for every session.** A covered session counts against C's one session per month.
- **The pause from Dec 18 to Jan 13 is announced** in every channel used for promotion.
- **With only 2 engineers, the cadence is monthly.** Alternate A and B, with the other as backup. A monthly pilot needs 6 sessions over two quarters (baseline), so the review moves to about June 2027.
- **Credit the engineer and their team by name** in the session and the write-up.
- **Book the rotation a quarter ahead.** Each engineer's manager agrees to the cap in writing and counts the session as work in their review.

## 4. Scope card (ready to publish, replace the examples with real questions)

```
## What to bring to Lanternfold Office Hours

Bring: "my consumer loses events after a rebalance", "how do I configure retries and backoff
in the producer", "is batch publish safe to retry", "which SDK version should I pin during beta".
Not here:
- Account, billing, plan or contract questions → [support link]
- Pricing, licensing or paid-tier features → [sales contact]. We answer only what the public
  docs say; nothing on roadmap or price.
- A suspected security vulnerability → [security disclosure channel]. Never raise it live
  or in a public thread.
- A bug you can reproduce → [GitHub issues]. Bring it and we'll help you write the report.
- A feature you need → we log it in [feedback record]; the product team decides.
- Debugging your own environment → we can't see it. Bring a minimal reproduction with
  secrets removed.

Sessions are [recorded with notice / not recorded]. [What is published, where, for how long.]
Our code of conduct applies: [link].
```

**Intake form (six fields only):**
1. Question, in one or two sentences.
2. What you tried, and the docs page you read.
3. Product and version.
4. May we read it out? Yes / Anonymise it / No, answer me in the write-up.
5. Time zone (optional).
6. Contact for the follow-up (optional). May we keep your handle on a feature request so you hear the decision?

Never ask for logs, configs or screenshots in the form.

**Triage 48 hours before each session:** answer live, answer async, redirect, docs gap, log for product. Most widely useful first. Never silently drop a question.

## 5. Per-cycle timeline

| When | Action |
|---|---|
| T-72h | Nudge the intake thread with the engineer's name and area |
| T-48h | Triage the queue. Send the engineer the prep brief and scope card |
| T+2 business days | Publish the write-up |

The 24-hour cancel check applies only to a livestream panel. A drop-in slot is held even with an empty queue.

## 6. Running the session

- **Run of show, 45 minutes:**
  - Minute -10: host and engineer test screen-share on a scrubbed demo environment.
  - Minute 0: welcome, recording notice, code of conduct, "no live debugging".
  - Minute 2: engineer introduces themself.
  - Minute 4: pre-submitted questions, 4-minute timebox each.
  - Minute 25: live questions.
  - Minute 40: parking lot read out.
  - Minute 43: next date and thanks by name.
  - Minute 45: end on time.
- **Notetaker is someone other than the host.** Log handles only when the asker agreed.
- **Empty room:** after 10 minutes with nobody, answer the forum backlog for the write-up and close. Log the session as held with zero askers.
- **Two empty sessions in a row:** change slot and promotion before cadence.
- **Engineer drops out:** the backup takes it. If both are out, announce the cancellation. Never cancel silently.
- **Recording notice, said before recording and again when it starts:**
  > "This session is recorded and published on [where] within [N] days, and kept [how long]. If you'd rather not appear, keep your camera off and use the chat. Don't share a screen showing tokens, customer data or internal hostnames."
- **Before publishing a recording:** review every screen-share for tokens, keys, hostnames and customer names. Revoke any token shown. Honour every "don't read my name" request.

## 7. YouTube: how to get the content without the empty livestream

- **Now to Dec 3:** build the content from the async answers. Each docs fix or write-up can become a short screen-recorded answer.
- **Drop-in pilot:** record with notice if you want clips, and publish only after the review above. Otherwise publish the write-up.
- **Livestream panel:** start it when the promotion trigger fires. It is the format whose answers reach every viewer, but it needs a panel and production every session. Live debugging is impossible there.
- **If it grows into a recurring series of demos or labs with registration and a sales handoff,** it is a webinar program, not office hours.

## 8. Loop after every session

1. Write-up within 2 business days: answered, answered async, redirected, logged for product, docs we are fixing. Link it in the next announcement.
2. Group repeat questions into families. Open one docs ticket the second time a family appears, in any channel. If the family is an error, write it as a troubleshooting page.
3. Log every feature request and bug in the feedback record, in the user's words, with the handle if consented. Then delete the raw session log.
4. Label resulting issues and docs changes "Office Hours" so the pilot review can count them.

## 9. Session log and write-up skeletons (empty)

**Session log columns:** date | held/cancelled | distinct non-staff askers | answered live | answered async | redirected | docs tickets opened | docs fixes merged | feedback records | engineer | write-up lag (days)

**Write-up:**
```
## Lanternfold Office Hours - [date], with [engineer], [area]
### Answered
- **[Question in the asker's words]** - [2-4 line answer] - [docs link or ticket]
### Answered here, not live
### Redirected
- [Topic] → [destination]. (No names.)
### Logged for the product team
- [Request or bug, in the user's words] → [feedback record / issue link]
### Docs we are fixing
- [Page] - [what was missing] - [ticket]
Next session: [date, time in audience zone, calendar link]. Submit questions: [link].
```

## 10. Measurement (current values)

| Signal | Target (self-set unless noted) | Now |
|---|---|---|
| Sessions held / planned; held with zero askers | All held; none cancelled silently | not measured yet |
| Distinct non-staff askers per cycle | Median ≥ 3 | not measured yet (support: ~2 questions, Discord: 1 thread) |
| Docs-unanswered questions, last month (demand gate) | ≥ 5 named | about 3, if none were docs-answerable. Count them exactly |
| Questions answered or redirected | Every one | not measured yet |
| Write-up lag | ≤ 2 business days | not measured yet |
| Merged docs fixes + feedback records | ≥ 1 per 2 sessions | not measured yet |
| Engineer sessions per month | None over 1 | no cap agreed yet |

Do not report recording views. They are a viewer-vanity metric. Count distinct askers and docs fixes.

## 11. Pilot review (2027-03-04 for the biweekly case)

- **Demand bar decides continue or stop.** Both conditions must hold. Otherwise drop to the async thread for a quarter and re-test.
- **Operating bar decides what to fix, never whether to stop:** no silent cancellation, no engineer over the cap, write-ups on time in all but one session.
- Everything past the pilot is provisional.

## Your next actions

1. ⏳ 15 min: answer the open decisions above, especially region split and engineer availability.
2. ⏳ 30 min: ask both engineers' managers for a written cap of one session per month, and ask for a third engineer.
3. ⏳ 1 hour: publish the scope card, intake thread and form. Announce Thursday 2026-10-29.