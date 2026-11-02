Do first, today: email the logistics customer's contact and ask legal for a decision date. Approval needs 6–8 weeks (baseline), and the panel was 3 weeks out.

## Open decisions (assumed; correct me)

1. **Job = feature depth.** No free tier, trial or open deals were named. If a free tier exists, the job becomes activation, and episode 1 becomes a follow-along lab.
2. **Engineers speak, advocates host.** Assumed: 2 platform engineers give 2 h/month each, with manager agreement. Needs confirming.
3. **Slot Tuesday 11:00 ET (17:00 Paris), 40 min.** Assumed: North America and Europe both large. Needs your region split.
4. **Sales owner for the handoff:** unnamed. Without a written rule, attendee data goes to product nurture only.
5. **Dates:** 5.1 must have shipped by 2027-01-19. Budget is unknown, so no paid promotion in season one.

## Diagnosis

You gave no numbers, so there is nothing to compute. The season has five defects:

1. **Three release episodes.** 5.1, 5.2 and roadmap are 3 of 6 episodes. Releases must stay under a third of a season.
2. **A comparison pitch.** "Ironvale vs the alternatives" is a sales topic, not a developer problem.
3. **A panel nobody can moderate.** Nobody on your side has run one, so the panel is deleted.
4. **An unapproved customer.** Legal has not approved, and approval needs 6–8 weeks, not 3.
5. **Wasted demand.** The forum's top-voted threads (consumer lag, dead letters) are unused, and they are your best topics.

First fix: lead with the forum topics, cut to one release episode, and move the customer to week 17.

## Charter

```
Series name: Ironvale Under Load (working title)
Job (first): feature depth. Secondary: community voices
Audience: backend engineers running queues in production, intermediate; region split open
Format mix: live demo, engineer conversation, customer story, Q&A (1 release episode max).
  Panel deleted: nobody can moderate with prep time.
Cadence and length: monthly, 40 min
Slot: Tue 11:00 ET (17:00 Paris). Test slot Thu 11:00 ET on eps 3 and 5.
  Ep 5 (2027-03-16): US clocks moved 03-14, EU 03-28 -> announce 16:00 Paris.
Season: 5 episodes, 2026-11-17 to 2027-03-16
Speaker pool: 2 advocates host/demo; 2 engineers (2 h/month each); 1 customer
  (approval pending); named backup per episode.
Replay policy: ungated chaptered copy within 48 h; 2 clips/episode; captions + transcript.
  Nothing gated (job is not deal acceleration).
Budget: platform, captioning: open. Paid promotion: none in season one.
Data retention: delete registrant/engagement data 12 months after season end (baseline)
Handoff contract: sign before episode 1, sales owner open
Continue bar:
  - total reach, live attendance, returning share not below median of eps 1-2
    on two of eps 3-5
  - returning share 20% or more by ep 4 (baseline)
  - job metric: attendee accounts adopt lag alerts / dead-letter config within
    30 days, ahead of matched non-attendees (confirm telemetry exists)
  - stop: two seasons failing job metric, or no backlog for a season
```

## Season plan (provisional past episode 5)

| # | Date | Format | Topic | Speaker | Backup | Replay | Signal |
|---|------|--------|-------|---------|--------|--------|--------|
| 1 | 2026-11-17 | Live demo | Why is my consumer falling behind? Diagnosing lag end to end | Advocate A, host B | Advocate B runs demo | Chaptered + 2 clips | Lag-config adoption |
| 2 | 2026-12-15 | Engineer conversation (replaces "Meet the platform team") | Poison messages: how we designed dead-letter handling | Engineer 1, host A | Engineer 2 | Chaptered + 2 clips | Dead-letter adoption |
| 3 | 2027-01-19 | Live demo (the one release episode) | Upgrading consumers to 5.1: what changes, what to try first | Advocate B + 5.1 engineer | Advocate A | Clip within days | 5.1 feature adoption |
| 4 | 2027-02-16 | Customer story | How a logistics team runs queues at scale (title agreed with customer) | Customer engineer, host A | Engineer conversation on retries/idempotency | Chaptered + 2 clips | Questions per 10 attendees |
| 5 | 2027-03-16 | Q&A | Ask the Ironvale engineers: top forum questions | Engineer 2, host B | Engineer 1 | Chaptered | Returning share |

- **5.2 sneak peek:** ship it as a 5.2 release episode in season two, after 5.2 ships. An unreleased preview dates fast and promises what the replay can't keep.
- **Roadmap 2027:** publish a written roadmap post with a comment thread. A webinar on future promises has no replay life.
- **Customer story, ep 4:**
  - **Approval:** legal must approve the title, slides and recording by 2026-12-22 (8 weeks before).
  - **Promotion:** do not promote before approval.
  - **Format:** the host interviews the customer. Send five questions a week ahead.
  - **Fallback:** if approval misses 12-22, run the backup.
  - **Release:** get a signed recording release from every speaker.

## Topic backlog (scored 0-2 each; the lag and dead-letter rows are forum-confirmed, the rest need a forum check)

| Topic | Job fit | Devs affected | Speaker | Replay life | Total |
|---|---|---|---|---|---|
| Diagnosing consumer lag | 2 | 2 | 2 | 2 | 8 |
| Dead-letter handling and redrive | 2 | 2 | 1 | 2 | 7 |
| Retries, backoff, idempotent consumers (verify on forum) | 2 | 1 | 2 | 2 | 7 |
| Upgrading to 5.1 | 2 | 1 | 2 | 0 | 5 |
| Queue vs log vs stream: how to choose (replaces "vs the alternatives") | 1 | 1 | 1 | 2 | 5 |
| Logistics customer story | 1 | 1 | 0 | 2 | 4 |
| 5.2 sneak peek | 1 | 1 | 1 | 0 | 3 |
| Roadmap 2027 | 0 | 1 | 1 | 0 | 2 |

Next 90 minutes of work: export the forum's top 20 threads by votes, then rescore rows 3 and 5. Feed Q&A ep 5 from the same export.

## Promotion

1. Open registration 2026-10-27 for ep 1 (3 weeks ahead). Keep promoting through the final week.
2. Order: own users and newsletter, then forum, then speakers' audiences, then social.
3. In each top-voted lag and dead-letter thread, post the episode link and invite the original poster to send questions.
4. Tag every replay link by episode.

## Handoff contract

Sign before ep 1, with a named sales owner.

| Tier | Signal | Route | Timing |
|---|---|---|---|
| A | Asked for demo, pricing or contact; clicked pricing/demo CTA | Sales, with episode and question | 1 business day |
| B | Engaged attendee at account with open opportunity | Account owner notified, no cold call | Next working day |
| C | Engaged (top third by watch share, questions, clicks) and ticked marketing box | Product nurture | Episode follow-up |
| D | Registered, attended briefly or not | Replay email only | Episode follow-up |

- **Sales acceptance bar:** 50% of Tier A (baseline). Read it back after each episode.
- **Never routed to sales:** Tiers C and D.
- **Form:**
  - Fields are name, email and at most one qualifying field.
  - The notice says the session is recorded and where it is published.
  - It says attendance, watch time, questions and clicks decide follow-up, and that sales may contact them.
  - It states retention (12 months), the opt-out and a privacy link.
  - It carries an unticked marketing-email box for everyone.
- **Legal:** record a legitimate-interest assessment before sales calls. Legal owns the final wording.
- **Customer as speaker:** the customer never receives the registrant list.

## Episode log

| Episode | Registrants by source | Live | Live/registrants | 30-day on-demand (platform + public copy) | Total reach | Returning | Live completion | Replay completion | Questions | Tier A / accepted | Replay published (h) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Pilot baseline | none supplied | | | | | | | | | | |
| 1-5 | | | | | | | | | | | |

The first two episodes set the baseline. Don't compare against vendor figures; the benchmark reports mix hosts and audiences.

## Effort check

By format:
- Demo: about half a day.
- Engineer conversation: about 1 day.
- Customer story: 1–2 days, plus the approval wait.
- Q&A: a few hours.

Season total: about 4 working days over 5 months, spread across two advocates and two engineers. Confirm that fits their bad-month hours.

Next: reply with answers to open decisions 1–4. That takes about 5 minutes, and then I can draft the engineer outreach and the legal request.