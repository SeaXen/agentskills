**Next action:** don't announce yet. Open 10 of the 40 `good first issue` tickets and check each for a stated goal, file pointers, and a way to verify the fix. About 30 minutes. If most fail, the call won't fix the backlog.

The deliverable below is the whole design. The skill's interview couldn't run, so every answer I assumed is listed first.

## Open decisions (answer these, then adjust)

1. Job of the program. I assumed **contributor growth**, from "get more people contributing code".
2. Name five questions from the last month that docs didn't answer (issues, chat, PR comments). Without five, run the async thread only and fix those docs first.
3. Where are contributors? I don't know the region split, so the slot is a placeholder.
4. Names, home time zones, and sessions per month each of the 3 devs can hold on a bad month. Do the other two have employer or manager buy-in?
5. Start date. I assumed a standing program, not a one-off.
6. What can never be recorded, and which language do sessions run in?
7. Is there a security disclosure channel? I assumed GitHub private vulnerability reporting.

## Three changes to your plan

1. **Success metric: first merged contributions, not attendance.** Attendance and YouTube views are viewer vanity. Nobody publishes an attendance benchmark, so any head-count target is self-set. Count how many of the 40 tickets get claimed and merged by people new to the repo.
2. **Format: booked pairing slots on starter issues, plus an async intake thread.** A public "ask us anything" call gets drive-by questions and spectators. Contributors need someone with the issue open next to them. The skill ranks booked slots first for contributor growth.
3. **Recording: don't record the slots.** Booked slots are never recorded, and private code and context come up in them. The reusable output is a written write-up, which also feeds the docs. If you want YouTube content, make a separate "codebase tour" video. That is content, not office hours.

## 1. Charter

```
Program:        Pinewake Contributor Hours
Job:            Contributor growth (first merged contribution)
Audience:       Developers who use Pinewake and have never merged a PR to it
Format:         Booked 30-min pairing slots on good-first-issue tickets
                + async intake thread (GitHub Discussions category, pinned all week)
Slot:           [day/time in largest region's zone, TBD from poll]; biweekly block
                of up to 3 slots; second slot if another region >= 25% of users (baseline)
Staffing:       Host: [maintainer]; backup host: [dev 2]
                Engineers: dev A, dev B, dev C; cap 1 session/month each
Scope card:     section 4 below, pinned in the thread
Recording:      Slots never recorded. Async thread and write-ups are the record.
Outputs:        Write-up within 2 business days; docs tickets; feedback records
Pilot:          2026-11-12 to 2026-02-18 review, 6 sessions
Demand bar:     >= 6 of the 40 tickets claimed and >= 3 merged by first-time
                contributors over the pilot (baseline, self-set);
                >= 3 merged docs fixes + feedback records (1 per 2 sessions)
                Below it -> async thread only for a quarter
Operating bar:  No silent cancellation, no engineer over cap,
                write-ups on time in all but one session
```

Numbers marked baseline are mine. Replace them with your own after the pilot.

## 2. Slot plan

1. Poll contributors and issue commenters for region and availability. Don't guess.
2. Take the largest region's 09:00-18:00 and intersect it with your working hours.
3. If the overlap is empty, put the cost on staff and take the slot at your end of day. Name who still falls outside their working window.
4. Publish the slot in the largest region's time zone with a calendar link. Give a named async path to every other region: the intake thread.
5. Anchor in that zone. EU and US clocks shift on different weekends, so the gap changes by an hour for 2-3 weeks in spring and about a week in autumn.

Default coverage is one slot plus async intake. Promote to two slots per cycle only if a second region reaches 25% of users and the rotation can staff both.

## 3. Rotation calendar

Three devs, biweekly, one session each per month. Capacity check: the cap needs sessions per month plus one spare, which is 2 + 1 = 3. This works but is tight, so get a written manager agreement for each dev.

| Date (provisional) | Engineer | Backup |
| --- | --- | --- |
| Thu 2026-11-12 | A | C |
| Thu 2026-11-26 | B | C |
| Thu 2026-12-10 | C | A |
| Thu 2027-01-14 | A | B |
| Thu 2027-01-28 | B | C |
| Thu 2027-02-11 | C | A |

- Announce Dec 24 and Dec 31 as paused. Pauses don't count as sessions. Extend the pilot if a session slips.
- If a third dev can't commit, drop to monthly. The pilot then lasts two quarters.
- Credit the engineer and their employer by name in each write-up.

## 4. Scope card (ready to publish)

```
## What to bring to Pinewake Contributor Hours

Bring: "I want to take issue #N, where do I start in the codebase?",
"how do I run the test suite locally", "which package owns X",
"is this fix the right layer", "my PR failed CI and I don't know why".
Not here:
- A suspected security vulnerability -> [private security reporting]. Never raise it live or in a public thread.
- A bug you can reproduce -> GitHub issues. We will help you write the report.
- A feature you need -> we log it in [feedback record]; the maintainers decide.
- Debugging your own deployment -> we can't see it. Bring a minimal reproduction with secrets removed.
- Licence, commercial or hosting questions -> [contact].

Slots are not recorded. Notes become a public write-up with no names unless you agree.
Our code of conduct applies: [link].
```

## 5. Session cycle

| When | Action |
| --- | --- |
| T-72h | Nudge the thread with the engineer's name and area; list 5 open starter tickets |
| T-48h | Triage submissions: answer live, answer async, redirect, docs gap, log for product |
| T-24h | Booking closes; engineer gets a prep brief and the scope card |
| Session | Notice, code of conduct, no live debugging of anyone's environment. Pair on the ticket. |
| T+2 business days | Publish the write-up |

- Hold the slot even when no one booked. After 10 minutes with nobody there, answer the thread backlog for the write-up, then close.
- If the engineer and the backup are both out, announce the cancellation publicly. Never cancel silently.
- After two empty sessions in a row, change the slot and promotion before the cadence.
- Open a docs ticket the second time any question family appears, in a session or any channel.

## 6. Skeletons (empty)

**Session log columns:** date, held or cancelled, distinct non-staff askers, tickets claimed, PRs opened, PRs merged, docs tickets opened, docs fixes merged, feedback records, engineer, write-up lag in days.

**Write-up:**
```
## Pinewake Contributor Hours - [date], with [engineer], [area]
### Answered
- **[Question in asker's words]** - [answer, 2-4 lines] - [docs link or ticket]
### Answered here, not live
### Redirected
### Logged for the product team
### Docs we are fixing
Next session: [date, time, calendar link]. Submit questions: [link].
```

## 7. Measurement (not measured yet)

| Signal | Target | Value |
| --- | --- | --- |
| Sessions held / planned | All held | not measured yet |
| Distinct askers per cycle | Self-set, default median >= 3 | not measured yet |
| Starter tickets claimed / merged by newcomers | >= 6 / >= 3 over pilot | 0 / 0 baseline |
| Docs fixes + feedback records | >= 1 per 2 sessions | not measured yet |
| Write-up on time | 2 business days | not measured yet |
| Engineer sessions per month | None over 1 | not measured yet |

Everything past the pilot is provisional.

## Separate from this design

The onboarding path (CONTRIBUTING, dev setup, ticket quality) belongs to the `oss-contributor-onboarding` skill. Run it after the 10-ticket audit if most tickets fail.

**Next:** run the 10-ticket audit, then send me the answers to the seven open decisions.