**Next action (2 min):** pull three numbers from YouTube Studio: views on your last 5 videos, subscribers gained in the last 28 days, and the share of views from Search. Put them in the baseline row of section 5. The plan below uses my estimates until you do.

The deliverable has six sections: the math, the counter-proposal, the weekly hours budget, content, metrics, and the pitch to the CEO.

---

## 1. The math

**Cadence.** Daily with 5 Shorts a week means 5 Shorts and 2 long-form videos every week.

| Item | Hours/week |
|---|---|
| 2 long-form technical videos (research, script, record, review the cut, title/thumbnail) at ~6h each | ~12 |
| 5 Shorts (pick clip, hook, review) at ~0.5h each | ~2.5 |
| Comments and analytics | ~1 |
| **Total** | **~15.5h against your 8h** |

My per-video hours are estimates. Technical CDC content needs a working demo, and a demo that breaks on camera costs hours. The editor covers cutting and captions, not research, scripting, or recording.

**Subscribers.** The goal needs 640 to 10,000 by end of Q2 (June 30, 2027, assuming a calendar fiscal year). That is about 9,360 net subscribers in 8 months, or ~1,170 a month, or ~39 a day.

**Audience size.** The target buyer is a backend or data engineer running Postgres who is moving data to a warehouse, Kafka, or search. That audience is small and searches for specific problems. Subscribers from Shorts skew toward general viewers who will never buy a CDC service.

**Consistency.** YouTube staff have said publicly that upload frequency alone does not rank videos. Viewer satisfaction and watch time do. A steady schedule helps build a viewing habit, and that is the real value of consistency. I could not re-check this source today, so verify it before quoting it to the CEO.

## 2. Counter-proposal

Keep his instinct (consistent, visible) and change what gets produced.

**Cadence:**

| Phase | Long-form | Shorts | Why |
|---|---|---|---|
| Nov–Dec 2026 | Build a bank of 4 videos | 0 | Never ship the first video without a buffer |
| Jan–Feb 2027 | 1 every 2 weeks | 2 a week, cut from long-form | Learn what works |
| Mar–Jun 2027 | 1 a week | 3 a week | Scale once you have data |

That is about 1 long-form and 3 Shorts a week at steady state. It also includes a public schedule, so viewers see consistency even though it is not daily.

**Shorts rule:** only cut Shorts from long-form footage. Never write original Shorts. That keeps each one at ~30 min of your time.

**Not now:** daily posting, original Shorts, live streams, and Twitch.

## 3. Weekly hours budget (8h)

| Task | Hours |
|---|---|
| Research and script outline | 2.5 |
| Record, including demo setup | 2 |
| Review editor's cut and revisions | 1 |
| Title, thumbnail, description, chapters | 0.5 |
| Pick Shorts clips (editor cuts them) | 0.5 |
| Comments, analytics, community | 1 |
| Buffer | 0.5 |

**Editor's scope:**
- the long-form edit
- 3 Shorts with captions
- thumbnail drafts

I don't know the contractor's hours or rate. If they have ≤6h a week, drop to 1 long-form every 2 weeks.

## 4. Content: what to make first

Pick problems your buyers search for. Verify each title in YouTube autocomplete before you commit.

1. Postgres replication slot growing and WAL filling the disk: causes and fixes
2. `REPLICA IDENTITY` explained, and why your CDC events miss old values
3. `pgoutput` vs `wal2json` vs `decoderbufs`
4. Postgres CDC to Kafka, ClickHouse, or Snowflake: a working end-to-end demo
5. Debezium vs a managed CDC service: an honest comparison (neutral tone earns trust)
6. Zero-downtime Postgres migration using logical replication

**Format:**
- Show the working result in the first 30 seconds.
- Use 18pt+ code and add chapters.
- Give each video one searchable title and one clear CTA to a repo or trial.

Shorts come from the strongest 30 seconds of each video: a failure, a command, or a before/after.

## 5. Metrics and targets

Subscribers are a vanity metric here. A subscriber is not a trial signup. Track this set instead:

| Metric | Baseline (fill in) | Why |
|---|---|---|
| Views from Search per video | ___ | Measures buyer-intent traffic |
| Average view duration on long-form | ___ | YouTube's main quality signal |
| Impression click-through rate | ___ | Tests titles and thumbnails |
| Signups or demo requests via UTM link in descriptions | ___ | The only metric tied to revenue |
| Subscribers gained | 640 now | The CEO's number, kept visible but not primary |

**Subscriber target.** I can't derive a defensible number without your baseline. As a placeholder, 2,000–3,000 by June 30, 2027 is plausible for a niche B2B channel at this cadence. That is a guess to replace after six weeks of data. A channel of 640 subs with a niche audience can be fully healthy.

**Review point:** after 8 weeks (about late February). Set final targets there from observed numbers.

## 6. How to pitch it to the CEO

1. **Start with agreement.** "You're right that consistency matters. I want to make it visible and sustainable."
2. **Show the hours table.** His plan costs ~15.5h a week and I have 8.
3. **Name the real trade-off.** Daily posting means either lower quality or more people. Quality drives watch time, and watch time drives growth.
4. **Offer a gate.** If the 8-week data shows Shorts converting to buyers, add hours, a second contractor, or a producer. Daily at quality needs roughly 25–30h a week (my estimate).
5. **Reframe the goal.** Ask: "Do we want 10,000 subscribers, or customers who found us through video?" Propose trial signups from video as a co-primary goal.

## Open questions for you

1. How many hours a week does the contractor have, and at what rate?
2. What does the channel have now: video count, last upload date, average views?
3. Is there a budget to hire a second contractor if the 8-week data supports it?

**Next:** pull the three Studio numbers and paste them here. I'll fill in the baseline and tighten the targets.