# Pipeline Hour: don't double paid promotion, close this run and reset

**Do this first:** refuse the budget increase and put paid promotion on hold at today's level. Then pull registrants by source and replay views for the last six episodes. Those two data sets decide the rest.

**Assumed (no one to interview, so I inferred each answer; correct any):**
- Job: activation, because your job metric is a first pipeline run and I assume a free tier or trial exists.
- One episode per month, so the last six are episodes 9-14.
- Your current registrant mix is mostly cold or paid, based on what the numbers show.
- Sales has no written handoff rule, and your capacity is unknown.

## 1. Diagnosis

| Ep | Registrants | Live | Live / reg | Returning share | Returning (approx.) | New attendees (approx.) |
|---|---|---|---|---|---|---|
| 9 | 210 | 53 | 25.2% | 30% | 16 | 37 |
| 10 | 260 | 62 | 23.8% | 26% | 16 | 46 |
| 11 | 240 | 46 | 19.2% | 22% | 10 | 36 |
| 12 | 300 | 54 | 18.0% | 18% | 10 | 44 |
| 13 | 310 | 53 | 17.1% | 15% | 8 | 45 |
| 14 | 330 | 53 | 16.1% | 14% | 7 | 46 |

- **Registrants rose 57% (210 to 330) and live attendance did not move (53 to 53).** The extra 120 registrants produced zero extra attendees. Live attendance fell from 25% to 16% of registrants.
- **Your loyal audience is leaving.** Returning attendees fell from about 16 to about 7 per episode. About 45 new people arrive each time and few come back, so the episodes aren't earning a second visit.
- **Registrations is the number the skill says neither team needs.** Doubling spend buys more of the one metric that is not working.
- **Paid ranks last by registrant intent.** The skill's promotion order puts your own users first and paid last. More paid will push live attendance below 16% and the returning share lower still.
- **Benchmarks don't excuse this.** Vendor bands (20-35% for small hosts) are a fallback only when a series has no history. Your own history comes first: you went from 25% to 16% on your own baseline.
- **The replay is 3-10 days late.** The skill's bar is 48 hours. About half of registrations arrive in the final 7 days (Livestorm data), so interest has decayed before the recording exists. You can't tell whether replays are working because you haven't reported replay reach. That is the gap between the "prefers on-demand" and "paid registrants" patterns in Step 6.
- **The job metric has been flat for about a year.** Roughly 600 attendees pooled is directional evidence only. Attendees are self-selected and should out-activate non-attendees by default, so no gap is a poor sign. No test has shown the series moves activation.
- **Pass threshold:** all four criteria fail.
  1. Live attendance and returning share are below baseline for four straight episodes.
  2. The job metric is flat.
  3. Replays run late.
  4. The backlog holds 2 topics, not a season (4-6).
- **The stop rule is met on two counts:** a flat job metric across about two seasons' worth of episodes, and a backlog that can't fill a season.
- **"14 months, no breaks" is calendar cadence, not an asset.** It is the "endless series" failure mode, so don't weigh it as a reason to keep going.

**First fixes:** per-source attendance, replay within 48 hours, and a backlog built from developer questions instead of marketing's calendar.

## 2. Charter (provisional, "Reset season")

```
Series name: Pipeline Hour (new charter; the old run ends after episode 16)
Job (first): activate developers to a first pipeline run (assumed). Secondary: none.
Audience: CI/CD engineers and platform/DevOps, intermediate. Region split: open decision.
Format mix: lab and engineer conversation (activation order; the lab carries the job).
Cadence/length: monthly, 40 min; lab 55 min. Bi-weekly rejected: no backlog, no backups.
Slot: current slot unchanged; the day/time test is open until per-source data is in.
Season: 4 episodes (E15-E18), dates open.
Speaker pool: internal engineers (hours per month are an open decision) + 2 community
  answerers; a named backup per episode. No customer story in season one.
Replay policy: ungated chaptered copy on the public channel within 48 h; 2 clips per
  episode; lab environment gated behind free-tier sign-up; captions + transcript.
Budget: paid promotion frozen at current level, no increase. Any new money goes to lab
  credits and captioning. Platform: current licence.
Data retention: registrant and engagement data deleted 12 months after season end (baseline).
Handoff: Tiers A-D below; sales owner = open decision.
Continue bar (set now, before E15):
  - live / registrants at or above 20% (baseline; the small-host band floor). Compare E17-E18
    with the median of E15-E16.
  - returning share at or above 14% (today's floor), 20% by E18 (baseline).
  - total reach (live + 30-day replay, all surfaces) flat or rising versus the median of
    E15-E16.
  - job metric: attendees' 30-day first-pipeline-run rate ahead of matched non-attendees
    (matched on signup cohort and plan), read pooled over seasons.
  - stop rule: one more season failing the job metric, or no backlog for a season, means
    announce the last episode.
Open decisions: sales owner; hours per engineer; free tier confirmed; region split.
```

## 3. Season plan (provisional)

| # | Date | Format | Topic | Speaker | Backup | Replay | Signal to watch |
|---|---|---|---|---|---|---|---|
| 15 | open | Follow-along lab | Remaining topic 1, recast as a build-along: a first pipeline running in 30 minutes | Internal engineer + second staff member in chat | named | Ungated chaptered copy in 48 h; lab gated | Attendees who ran a first pipeline during the session |
| 16 | open | Engineer conversation | Remaining topic 2, framed as a problem | Engineer who built it | named | Ungated chaptered copy in 48 h + clips | Returning share |
| 17 | open | Live demo | Backlog #1 | Engineer | named | Ungated copy + clips | Live / registrants |
| 18 | open | Engineer conversation | Backlog #2 | Community answerer | named | Ungated copy + clips | Job metric |

- E15-E16 are the announced final episodes of the old run. E17-E18 happen only if the gate below passes.
- **Gate:** both final episodes publish within 48 hours, the backlog holds 4 scored topics, the charter is signed, and the per-source report exists.
- **Promotion test:** hold paid flat for E15-E16 and log attendance per source. For one episode, also cut paid to zero. If live attendance stays near 53, paid buys nothing and you have your answer for marketing.
- Rewrite any product-tour title as the developer's problem.

## 4. Topic backlog (provisional)

Scores 0-2 per column. They are illustrative: rescore them from real forum, support and trial-drop data.

| Topic | Job fit | Devs affected | Speaker exists | Replay life | Total |
|---|---|---|---|---|---|
| Debugging a flaky test in CI without re-running the whole pipeline | 2 | 2 | 1 | 2 | 7 |
| Cutting a 25-minute pipeline to under 10 with caching and parallelism | 2 | 2 | 1 | 2 | 7 |
| Getting a first pipeline green: the 5 failures new users hit | 2 | 2 | 2 | 1 | 7 |
| Secrets in pipelines: rotating without breaking deploys | 1 | 2 | 1 | 2 | 6 |
| Rolling back a bad deploy in under 5 minutes | 1 | 1 | 1 | 2 | 5 |

Sources to scan: support tickets and forum questions, docs searches with no result, the trial step before the first run with the biggest drop, incidents. Keep release episodes under a third of a season.

## 5. Handoff contract (provisional)

| Tier | Signal | Route | Timing |
|---|---|---|---|
| A | Asked for demo, pricing or contact; clicked a pricing or demo CTA | Sales, with episode and question | 1 business day (baseline) |
| B | Engaged attendee or replay viewer at an account with an open opportunity | Account owner notified, no cold call | Next working day |
| C | Engaged (top third by watch share, questions, clicks) who ticked the marketing box | Activation nurture | Episode follow-up |
| D | Registered, or attended briefly | The replay email | Episode follow-up |

- "Engaged" is defined from E15-E16 distributions.
- The form discloses recording and engagement tracking, and carries an unticked marketing box. Legal owns the wording.
- A named sales owner and an acceptance bar (baseline 50%) are open decisions.
- If sales refuses a written rule: no sales route, attendees go to product nurture only, and the open decision is logged.
- Never route "every attendee is an MQL". "38% of attendees become MQLs" is a refused statistic with no source.

## 6. Episode log (pilot baseline; "—" means not supplied)

| Ep | Regs by source | Live | Live/reg | 30-day on-demand | Total reach | Returning | Live compl. | Replay compl. | Qs | Tier A / accepted | Replay (h) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 9 | — | 53 | 25.2% | — | — | ~16 (30%) | — | — | — | — | 72-240 |
| 10 | — | 62 | 23.8% | — | — | ~16 (26%) | — | — | — | — | 72-240 |
| 11 | — | 46 | 19.2% | — | — | ~10 (22%) | — | — | — | — | 72-240 |
| 12 | — | 54 | 18.0% | — | — | ~10 (18%) | — | — | — | — | 72-240 |
| 13 | — | 53 | 17.1% | — | — | ~8 (15%) | — | — | — | — | 72-240 |
| 14 | — | 53 | 16.1% | — | — | ~7 (14%) | — | — | — | — | 72-240 |
| 15-18 | | | | | | | | | | | |

Replay times are the "3 to 10 days" range you gave. Fill the empty columns from the platform before E15.

## What to tell marketing

- Registrations stay out of the report. It shows live attendees, total reach, attendance per source and the job metric.
- Paid goes back on the table only if per-source data shows paid registrants attend and activate.
- Doubling now would buy registrants who don't show up, while the audience that does show up shrinks.