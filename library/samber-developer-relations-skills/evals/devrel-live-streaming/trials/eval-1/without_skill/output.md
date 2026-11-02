# Ferrolite live-stream launch plan, Q1 2027

**Do this first:** this week, apply for or confirm live access on every destination. That means LinkedIn Live for the company page and your profile, and live-streaming eligibility on X. Approval can take days to weeks, and it is the one thing that can break a Jan 4 start.

## Assumptions (tell me which are wrong)

- ℹ️ Quarter = Mon Jan 4 to Fri Apr 2, 2027 (13 weeks, 39 streams). Nov-Dec is prep.
- ℹ️ Slot = 16:00-18:00 CET (10:00-12:00 ET), Mon/Wed/Fri. This is a placeholder. Check where your 4k monthly signups are located and move the slot if needed.
- ℹ️ Goal = signups and activation for Ferrolite (managed Postgres). Views are a means, not the goal.
- ℹ️ You have no producer or moderator today. You are the host, the chat reader, the demo driver and the clipper.
- ℹ️ I have no baseline for your current reach. Week 1-2 data sets the targets, and I don't invent any here.

## Plan as you specified

- 3 streams a week, 2h each, on Twitch, YouTube, LinkedIn (company page and your profile) and X, all at once through Restream.
- Restream's merged chat overlay is on screen. You answer from one window.

## Risks to settle in rehearsal (not after launch)

1. ⚠️ **Chat coverage.** Before Jan 4, confirm which of the five destinations Restream actually ingests chat from, and whether replies from the merged window post back to the originating platform. Verify it per platform with a test stream. If LinkedIn or X comments don't flow in, keep a second tab open for them and plan for a slower reply rate there.
2. ⚠️ **One screen, five audiences.** The overlay shows every platform's chat to every platform's viewers. Chat from Twitch or X can appear on the LinkedIn page, a company page, with your employer's name on it. Decide now:
   - Show only messages you approve, or only questions. Or drop the overlay and read questions aloud.
   - Add a chat moderator or bot with a short code of conduct and a ban list shared across platforms.
3. ⚠️ **Solo load.** Streaming 6h a week, plus prep and clipping, is roughly 12-14h of your week (my estimate). Mitigation: a rotating Ferrolite engineer joins as co-host, who also watches chat. Aim for at least 1 of 3 streams a week.
4. ⚠️ **Live demos on a real product.** Use a dedicated demo org with no customer data. Hide connection strings and API keys with a screen-capture region or scene that excludes the terminal history. Rotate any credential that appears on screen.
5. ⚠️ **Audience split.** Twitch and X are casual and LinkedIn is professional. One 2h show won't fit all of them equally. Pick one primary audience per day (see formats) and let the others ride along.

## Formats (one per weekday, so the schedule is predictable)

| Day | Show | Primary audience | Purpose |
|---|---|---|---|
| Mon | **Build**: one app built on Ferrolite all quarter, one episode per week | developers (Twitch, YouTube) | activation: viewers copy the steps |
| Wed | **Postgres Clinic**: live query plans, indexes, migrations, backups, using viewer-submitted problems | developers and DBAs (YouTube, X) | trust, searchable clips |
| Fri | **Ship Log + Guest**: what changed in Ferrolite this week, customer or engineer guest, Q&A | buyers and leads (LinkedIn) | pipeline, product feedback |

### 2h run-of-show (same shape every time)

| Min | Segment |
|---|---|
| 0-5 | Welcome, today's goal, one link in chat |
| 5-20 | Setup and recap of last episode |
| 20-85 | Main work (demo, build, or clinic) |
| 85-100 | Chat Q&A, answered in the order received |
| 100-115 | Wrap-up, what you finished, what is next |
| 115-120 | One call to action, then end |

Rules:
- Pin one tagged link per stream.
- Read a question aloud before answering, so viewers on other platforms follow.
- Never promise a feature date on air.

## Prep schedule (Nov 2026 - Jan 2027)

| By | Action |
|---|---|
| Nov 13 | Apply for and confirm live access on LinkedIn (page and profile), X, Twitch and YouTube. Connect all to Restream. |
| Nov 20 | Choose the demo app and write the 13-episode outline. Create the demo org, free of customer data. |
| Nov 27 | Design scenes: main, screen-only, guest, starting soon. Decide the overlay policy. |
| Dec 4 | Set up moderation: code of conduct, ban list, a mod or bot per platform. |
| Dec 11 | Private test stream to all five destinations. Check latency, audio, chat flow and replies. Write down what fails. |
| Dec 18 | Second test with 2-3 colleagues in chat, with a trial Wed Clinic. Fix the list. |
| Dec 19 - Jan 3 | Break. No streams. |
| Jan 1-3 | Schedule the week-1 events on every platform. Post the announcement. |
| Mon Jan 4 | Launch. |

## Quarter schedule (16:00-18:00 CET)

| Wk | Mon: Build | Wed: Clinic | Fri: Ship Log + Guest |
|---|---|---|---|
| 1 (Jan 4) | Ep.1: connection string in 10 minutes | Reading EXPLAIN | Quarter roadmap + AMA |
| 2 (Jan 11) | Ep.2: schema and migrations | Indexes that matter | Ship log |
| 3 (Jan 18) | Ep.3: auth and row-level security | Connection pooling | Customer guest |
| 4 (Jan 25) | Ep.4: background jobs in Postgres | Viewer slow-query hunt | Ship log |
| 5 (Feb 1) | Ep.5: backups | Point-in-time restore drill | Engineer guest |
| 6 (Feb 8) | Ep.6: read replicas | Replication lag | Ship log |
| 7 (Feb 15) | Ep.7: observability | Reading pg_stat_statements | Customer guest |
| 8 (Feb 22) | Ep.8: scaling up (resize, no downtime) | Vacuum and bloat | Ship log |
| 9 (Mar 1) | Ep.9: testing against a branch database | Locking and deadlocks | Engineer guest |
| 10 (Mar 8) | Ep.10: security hardening | Permissions and roles | Ship log |
| 11 (Mar 15) | Ep.11: migrating from another provider | Zero-downtime migration | Customer guest |
| 12 (Mar 22) | Ep.12: load test the app | Fix what the load test found | Ship log |
| 13 (Mar 29) | Ep.13: launch the app | Viewer's-choice clinic | Quarter retro + next-quarter vote |

Fill guest slots by week 2. Ask customers first, since their stories carry the most weight on LinkedIn.

## Weekly rhythm (about 12-14h)

| When | Task | Time |
|---|---|---|
| Fri before | Plan next week, book guests | 1h |
| Mon-Fri, before each stream | Rehearse and set scenes | 30 min x 3 |
| Mon-Fri, during | Stream | 2h x 3 |
| Within 24h after | Cut 2-3 clips, post, add timestamps | 1h x 3 |
| Fri | Review numbers, adjust | 1h |

## Measurement

- **Attribution:** one UTM-tagged link per stream per platform (`utm_source` = platform, `utm_campaign` = stream, `utm_content` = episode). Pin it and repeat it once on air.
- **Primary:** signups and activated projects (first successful connection) from tagged links. Compare with your 4k/month base as a trend, not as proof.
- **Secondary:** average concurrent viewers and average watch time per platform, chat questions answered, clip views.
- **Baselines:** set after weeks 1-2. Targets derive from them. Don't judge before week 3.
- **Report:** one page every Friday: per-platform signups, watch time, best clip, what to change.

## Decision gate: end of week 6 (Feb 12)

Review the per-platform numbers. For each destination, decide: keep, demote to clip-only, or drop. The criterion is signups and activated projects per hour of effort. A platform that adds chat load but no tagged signups by week 6 is a candidate to cut. Check this in the data; I'm not presuming the outcome.

If workload blocks you before week 6, the first cut is to drop the Wed overlay or one platform. Don't drop a stream day.

## Open questions

1. Is 16:00 CET right for your signups? Which regions are they in?
2. Do you have a moderator or co-host available, or must I assume solo?
3. Do you want the chat overlay on screen, or is reading questions aloud acceptable?
4. Who approves customer guests and any roadmap talk (legal and product)?