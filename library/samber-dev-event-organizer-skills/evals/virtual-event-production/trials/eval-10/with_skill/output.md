# Sable Infra Summit: virtual KPIs and targets for the board

## Read this first

- **Self-set metrics.** Every number below is a commitment we choose. None is an industry standard, and the production skill I followed gives no benchmark for any of them.
- **Assumptions.** I could not run the interview, so I assumed the following. If any is wrong, the first three KPIs hold but the staffing and the fourth KPI change.
  - Posture: an event people are inside, with open chat and live Q&A.
  - Schedule: four sessions run one at a time, not in parallel.
  - Staffing: one named moderator and one technical watcher per session.
- **No audience-size benchmark.** The skill gives none, and it warns that going virtual can move attendance up or down. Two real editions illustrate this:
  - PyCon US 2021 (virtual) drew about 22% fewer people than 2019 (in-person).
  - KubeCon North America 2020 (virtual) nearly doubled its 2019 registrations.

## Gates (pass or fail before session 1)

Each gate is checkable before the first session and has no threshold to argue about. If a gate is open on the day before, the board hears it then.

1. Every live session has a named moderator, not a function. If no one is named, we close the chat for that session.
2. Every speaker has joined the platform the event actually runs on, at least once, before the day.
3. The fallback line is published where the audience will look, and the person who will say it live knows the sentence.

## Committed KPIs (the three the board can hold us to)

| # | KPI | Target | Floor | What a miss triggers |
|---|---|---|---|---|
| 1 | Sessions delivered without an audience-visible failure, over sessions scheduled. A session with no audio counts as a failure. | **4 of 4** | 3 of 4, and every failure meets KPI 2 | Any failure goes into a written post-mortem. We add a technical watcher or host, or move the speaker to a pre-recorded rung, before any next edition. |
| 2 | Time from a feed dropping to the audience being told something | **≤ 60 s** in chat and **≤ 2 min** on the feed | None. Over 2 min is a miss. | Rerun the drill with the same people. Check that the watcher is on a second device and outside the production path. |
| 3 | Speakers who joined a platform check before the day, over speakers scheduled | **100%**, done by T-3 days | None | Any speaker not checked by T-3 days gets an individual slot. If still unchecked at T-1, they move to a pre-recorded talk with the speaker live in chat. |

With only four sessions, KPI 1 moves in 25-point steps. One failure takes us from 100% to 75%, so the board should read it as a count, not a rate.

## Reported KPI (tracked, not committed)

| # | KPI | Target | What a miss triggers |
|---|---|---|---|
| 4 | Questions relayed to a speaker, over questions asked. It shows whether the moderation was real or nominal. | **≥ 80%**. Unrelayed questions get a written answer after the session. | Below 80%, add a second moderator or tighten the batching mechanic next time. |

## Audience KPIs: counting rules now, numbers later

The board will want reach and engagement figures. I will not invent a show-up rate. We fix the counting rules now and set the numbers from our own data.

- **Registered:** about 900 (the planning figure).
- **Unique live attendees per session:** counted from platform join logs.
- **Peak concurrent viewers per session.**
- **Attendees who joined at least 2 of the 4 sessions.**
- **Recording views within 30 days.**
- **Numeric targets:** set at registration close (about T-7 days), from our own sign-up curve and any earlier community events. They go to the board then, labeled as self-set.
- **If the board needs a number today:** I would give a range labeled as judgment, with no external source behind it.

## Cost line

I hand this to the event budget, split by what a lean tier drops:

- The feed survives every tier.
- The interaction surface and its staffing go first.
- Cutting staffing means cutting KPI 4 and weakening KPI 2. The board should see that link before it approves a lean tier.

## Before we publish this to the board

1. Confirm the four sessions run sequentially, or tell me how many overlap, and I re-staff.
2. Confirm chat and Q&A are open. If this is a watch-only feed, KPI 4 and the moderation gate drop out.
3. Record the three committed KPIs, and the action each one triggers, before the event, not after.