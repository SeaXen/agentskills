**Decision: keep all 14 Query Clinic videos public on YouTube. Do not gate the replays.** Gate a bundle of resources instead: the lab environment, the sample datasets and the query notebooks. Policy starts with next month's episode.

## Open decisions (assumed, because nobody could be asked)

1. **Job = activation.** I assumed this because the series' job is stated as getting trial users to first ingest and a free cloud tier exists. If the marketing director means deal acceleration, the answer changes (see "If he insists").
2. **Format = Q&A or live demo.** I assumed this from the name "Query Clinic".
3. **Missing numbers.** I have no registrants, live attendees or tagged signups per episode. I have only the 2-9k YouTube views, which count as an "upper bound".
4. **Still open:** slot, speaker pool, budget, and the sales owner who signs the handoff contract.

## Diagnosis

- **The 91% completion claim.** Goldcast 2026 reports 91% completion on demand against 74% live. That compares a small self-selected group (2.62% of registrants watch only on demand) with live attendees. It shows intent, not more value per viewer.
- **The "leads" claim.** The 2-9k YouTube viewers are anonymous. They were never leads and sit in no tier. A form does not recover them. It removes the ones who learn from video.
- **Developers learn from video.** Stack Overflow 2026: documentation 58.9%, video 41.1%. SlashData Q1 2025: tutorial videos are the second most valuable onboarding resource (32.7%).
- **Pulling the videos costs reach.** Moving 14 public videos behind a form kills their links and their reach. Across the 14 that is roughly 28k to 126k views today.
- **Gate-everything is the wrong option for this job.** The skill deletes it unless the first job is deal acceleration. A form fill is not a first ingest, and the activation path is exactly what a gate interrupts.
- **First fix:** count activation from replay viewers, which nobody does today. Tag every replay link by episode and measure signup, then first ingest.

## Charter

```
Series name: Query Clinic
Job (first): activate trial developers to first ingest. Secondary: feature depth
Audience: backend, data and IoT engineers on or near the free cloud tier. Region split: open
Format mix: live demo and engineer conversation alternate; Q&A only with a standing
  question backlog; one follow-along lab per season on the free tier (job = activation, free tier exists)
Cadence and length: monthly, 40 min; lab 55 min
Slot: open decision (largest region's working day); test slot on two same-format episodes
Season: 5 episodes, Nov 2026 to Mar 2027 (provisional; no Dec 19 to Jan 2 gap assumed)
Speaker pool: open decision; named backup per episode
Replay policy:
  - ungated chaptered YouTube copy within 48 h
  - 2 clips per episode
  - captions and transcript
  - the 14 existing videos stay public: add chapters, tagged links, an end-card to the lab
  - ungated library page embeds the public videos
  - gated bundle: lab environment, sample dataset, query notebooks (free-tier signup)
Budget: platform open; paid promotion none in season one; lab credits open; captioning open
Data retention: registrant and engagement data deleted 12 months after season end (baseline)
Handoff contract: signed <date>, sales owner <name> (open)
Continue bar:
  - no metric (total reach, live attendance, returning share) below the median of the
    first two episodes on two of the later episodes
  - returning share: 20% or more by episode 4 (baseline)
  - job metric: 30-day first-ingest rate of attendees and tagged replay signups ahead of
    matched non-attendees
  - stop: two seasons failing the job metric, or no backlog for a season
Open decisions: the four above, plus the sales owner
```

## Gate test (answers the director with data)

1. Episode 1: ungated replay plus the gated bundle.
2. Episode 2: same setup, a different bundle gate. Keep the video ungated in both.
3. Measure 30-day first ingest, not form fills.
4. Two episodes is directional only. State that plainly.
5. A full gate on a new episode needs the job changed first, signed by the series' owner.

## Season plan (provisional)

| # | Format | Problem-titled topic | Speaker | Backup | Replay type |
| --- | --- | --- | --- | --- | --- |
| 1 | Live demo | Fix your first ingest when the write returns an error | open | open | Ungated + bundle |
| 2 | Engineer conversation | Why a high-cardinality tag slowed a query 100x | open | open | Ungated + 2 clips |
| 3 | Live demo | Query 90 days of data fast with downsampling | open | open | Ungated + 2 clips |
| 4 | Follow-along lab | Ingest sensor data on the free tier in 30 minutes | open | open | Ungated; lab gated behind free-tier signup |
| 5 | Q&A | Top-voted community questions this season | open | open | Ungated + 2 clips |

Release episodes stay under a third of the rows.

## Topic backlog (0-2 per column, sorted by total)

| Topic | Job fit | Devs affected | Speaker | Replay life | Total |
| --- | --- | --- | --- | --- | --- |
| First-ingest errors | 2 | 2 | 1 | 2 | 7 |
| Cardinality blowups | 1 | 2 | 1 | 2 | 6 |
| Downsampling and retention | 1 | 2 | 1 | 2 | 6 |
| Slow query diagnosis | 1 | 2 | 1 | 2 | 6 |
| Free-tier limits explained | 2 | 1 | 1 | 1 | 5 |

These scores are placeholders. Re-score them from the largest trial drop-off step and the top forum questions.

## Handoff contract (sales owner open)

| Tier | Signal | Route | Timing |
| --- | --- | --- | --- |
| A | Asked for a demo, pricing or contact; clicked a pricing or demo call to action | Sales, with the episode and the question | 1 business day (baseline) |
| B | Engaged attendee or registered bundle downloader at an account with an open opportunity | Account owner notified, no cold call | Next working day (baseline) |
| C | Engaged attendee who ticked the marketing box | Activation nurture | Episode follow-up |
| D | Registered only | The replay email | Episode follow-up |

- **Anonymous viewers.** Anonymous YouTube viewers never enter a tier. Count them through tagged links only.
- **Marketing opt-in.** The form shows an unticked marketing box to every registrant. Marketing email goes only to those who ticked it.
- **Form fields.** Collect name, email and one qualifying field at most.
- **Form notice.** The form says that attendance, watch time and clicks are recorded, and that sales may contact the registrant.
- **Sales calls.** Calls and account notes need a recorded legitimate-interest assessment.
- **Acceptance.** Track Tier A acceptance after every episode and tighten Tier A if it stays under the bar.
- **Retention:** 12 months (baseline).

This gives the director what he actually needs: named hand-raises and account notes, plus signups traced to each episode.

## Episode log

| Episode | Registrants by source | Live | Live / registrants | 30-day on-demand (platform + YouTube) | Total reach | Returning | Live completion | Replay completion | Questions | Tier A / accepted | Replay published (h) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Past 1-14 (pilot baseline) | to pull | to pull | to pull | 2-9k views each (upper bound) | to pull | to pull | to pull | to pull | to pull | n/a | to pull |
| Season rows 1-5 | | | | | | | | | | | |

## If he insists on gating

- **Allowed only if the first job becomes deal acceleration.** That is a charter change signed by the series' owner, with its own continue bar and job metric.
- **Even then, don't pull the 14 public videos.** Gate new episodes only, and keep the old ones public as the top of the funnel.

## Pass check, end of season

1. Reach, live attendance and returning share are not below baseline.
2. The job metric moved in the attendees' favour.
3. Every replay is published within 48 hours.
4. The next season's backlog and speakers are booked.

**Next, about 20 minutes:** pull the 14-episode table (registrants, live attendees, YouTube views, tagged signups, first ingests) and send it to me. I'll fill the log and set the baselines.