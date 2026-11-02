**Next action (30 min):** export registrants for episodes 4-6 from the platform with their UTM or source tag. Compute live ÷ registered per source. That number decides the fix, and no one has it yet.

**Verdict:** The series is not failing. It sits flat at about 22% live, the bottom of the matched band (20-35%). The 35-45% average and the 3+ reminder lift are refused stats. Replay carries the series: live is about 10-13% of reach. Fix order: promotion mix and a reason to attend live first, reminders as a one-episode test.

## Open decisions (assumed, no interview possible)

Settle before Jan 12 (about 5 hours total):

1. **Job = feature depth.** You named no free tier, trial or open deals. If a free tier or sandbox exists, job = activation: add one follow-along lab per season, and the job metric becomes 30-day first meaningful action (first trace).
2. **Sales owner unnamed.** I assumed no written handoff rule exists.
3. **Slot unknown.** I assumed you keep your current slot. Check it sits in the working day of your largest developer region.
4. **Speakers unnamed.** I assumed 4 or more engineers, with a manager-agreed 2 h/month each.
5. **Partner only sends its newsletter.** I assumed registrants sign up on your form and the partner gets no list.

Can wait: budget (I assumed reallocating existing paid spend, no new money), episodes 1-3 data, region split.

## 1. Diagnosis

| | Ep 4 | Ep 5 | Ep 6 | Pooled |
| --- | --- | --- | --- | --- |
| Registrants | 270 | 290 | 285 | 845 |
| Live | 58 | 65 | 61 | 184 |
| Live ÷ registrants | 21.5% | 22.4% | 21.4% | **21.8%** |
| No-shows | 212 | 225 | 224 | 661 |
| Platform on-demand views | ~90 | ~90 | ~90 | |
| Public YouTube views (30 days) | 350-450 | 350-450 | 350-450 | |
| Total reach (upper bound, views not unique viewers) | 498-598 | 505-605 | 501-601 | |

**Benchmarks**

- **Your own baseline is flat.** Live attendance runs 21.4-22.4% over three episodes. Registrations hold at 270-290, above Goldcast's B2B average of 251 registrants.
- **The matched band is 20-35%.** You are a small host, and 75% of registrants come from paid LinkedIn or a partner list. Demio shows 22% for hosts under $1M and 28% for software hosts. BrightTALK shows 34%. Goldcast 2025's own averages divide to 21%. All of these are vendor customers, and none isolates developers.
- **ON24's 60% is the wrong comparator.** It fits large hosts mailing their own list. Your own list is 25% of registrants.
- **Refused: "industry average 35-45%".** Its citation chain never resolves to a study.

**Reminders**

- **Refused: "3+ reminders lift attendance 20%".** It has no source.
- **Even if true, the gain is small.** A 20% relative lift takes 21.8% to about 26%, roughly 12 more attendees per episode.
- **One episode cannot prove it.** With about 280 registrants, one episode has a standard error of about 2.5 points, so only a jump of about 5 points or more reads as signal.

**Pattern read:** healthy registration, low live attendance, healthy replay reach.

- **Replay reach is high.** YouTube alone draws more views than you have registrants.
- **The audience prefers on demand.** Invest in the replay and give live a reason that more emails cannot.
- **The platform replay is not mostly no-shows.** At most about 40% of no-shows could have watched it (90 views ÷ 212-225 no-shows, an upper bound).
- **Caveat:** the YouTube views probably include non-registrants found through search or LinkedIn. That means pattern 3 (registrants bought by paid or partner promotion, who never come back) can still hide inside the 22%. Per-source attendance separates the two.
- **Illustration, not data:** if your own list attended at 45%, it would supply about 32 of 61 attendees. The 212 paid and partner registrants would then attend at about 14%.

**First fix, in order:**

1. Compute attendance and cost per live attendee per source, including LinkedIn spend ÷ LinkedIn attendees.
2. Move promotion effort to own list and community, and into the final week (49.6% of registrations arrive in the last 7 days, 15.3% on the day).
3. Give live a reason: an engineer answering live, and an unrecorded after-show.
4. Test the VP's reminders in episode 7 (see the season plan).

**Line for the VP:** at 21.8% against a matched 20-35% band, the series is flat and low in range, not failing. Total reach is about 500-600 per episode against about 280 registrants. We test her 5-reminder idea on episode 7, so it becomes data.

## 2. Charter

```
Series name: <current name>
Job (first): feature depth (assumed). Secondary: activation if a free tier exists
Audience: backend/SRE engineers; region split open decision
Format mix: live demo + engineer conversation alternating; one Q&A episode (live engineer
  answers are the reason to attend live). Lab only if a free tier exists
Cadence and length: monthly, 40 min (baseline)
Slot: current slot; test a second slot only on two episodes of the same format
Season 2: 4 episodes, Jan 12 to Apr 13 2027 (no December episode: holiday dip).
  Next quarter = episodes 7-9; episode 10 closes the season review. All provisional
Speaker pool: internal engineers (manager-agreed hours), named backup per episode,
  1 community answerer invited; customer story optional, approval 6-8 weeks ahead
Replay policy: ungated chaptered YouTube copy within 48 h, 2 clips per episode, captions
  + transcript, links tagged by episode. Replay email points to the platform copy so
  viewer-level data stays tied to a registrant
Budget: existing LinkedIn spend reallocated, platform, captioning; honoraria none (open decision)
Data retention: 12 months after season end (baseline)
Handoff contract: signed <date before Jan 12>, sales owner <open decision>
Continue bar (set before episode 7):
  - baseline = pilot median (eps 4-6; enter eps 1-3 to finalize): live 61, live ÷ registrants
    21.5%, total reach from exact YouTube counts
  - no metric (total reach, live attendance, returning share) below baseline for three
    consecutive episodes
  - returning-attendee share: bar set from episodes 7-8
  - job metric: feature adoption of attendee accounts ahead of matched non-attendee accounts.
    With an eligible list in the thousands, hold back a random 10-20% from invitations
    for one season for a causal read
  - stop rule: two seasons failing the job metric, or no backlog for a season
Open decisions: see top
```

## 3. Season plan (provisional)

One lever per episode, so each result is readable. Noise is about ±5 points per episode.

| # | Date | Format | Topic | Speaker | Backup | Replay | Lever / signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | Tue Jan 12 | Live demo | Tracing a slow request across services, end to end | Engineer A | Engineer B | Chaptered + 2 clips | **Reminders 2 → 5 (VP's test), mix unchanged.** Compare live % to 21.8% |
| 8 | Tue Feb 9 | Engineer conversation | Alert noise: from pages nobody reads to pages that matter | Engineer C (built it) | Engineer A | Chaptered + 2 clips | **Promotion mix:** cut paid by about half, move to own list and community. Compare per-source attendance |
| 9 | Tue Mar 9 | Q&A episode | Ask the engineers: the quarter's top-voted questions | Engineers A + C | Engineer B | Chaptered by question | **Reason to attend live:** live answers + 15-min unrecorded after-show |
| 10 | Tue Apr 13 | Live demo | Incident end to end: pager to root cause | Engineer B | Engineer C | Chaptered + 2 clips | Season review on three consecutive episodes |

- Both dates avoid the US/EU clock-change gap (US Mar 14, EU Mar 28).
- Start a customer story approval by Feb 16 only if one is wanted for season 3.
- Episode 9 needs a standing question backlog: pull top-voted community and support questions for a week before. If you cannot, swap in topic E below.

## 4. Topic backlog (provisional)

Score 0-2 each. Replace these scores with your community questions, docs searches with no result, and trial drop-off data.

| Topic | Job fit | Devs affected | Speaker exists | Replay life | Total |
| --- | --- | --- | --- | --- | --- |
| A Tracing a slow request across services | 2 | 2 | 2 | 2 | 8 |
| B Alert noise: pages that matter | 2 | 2 | 1 | 2 | 7 |
| C Incident end to end, pager to root cause | 2 | 2 | 1 | 2 | 7 |
| D Ask the engineers: top questions | 2 | 2 | 2 | 1 | 7 |
| E High-cardinality metrics without the bill | 2 | 1 | 1 | 2 | 6 |
| F Migrating to OpenTelemetry | 1 | 2 | 1 | 2 | 6 |
| G Sampling: what to keep when you cannot keep it all | 1 | 1 | 1 | 2 | 5 |
| H Release roundup (the only release episode; limit is under a third of a season) | 1 | 1 | 2 | 0 | 4 |

## 5. Handoff contract

```
Series: <name>                  Season: Jan-Apr 2027
Series job (first): feature depth
DevRel owner: <you>             Sales owner: <open decision>

Tier A - hand-raise
  Signal: demo/pricing/contact request; pricing or demo CTA click
  Route: sales queue   SLA: 1 business day
  Payload: episode, question asked, resources clicked
Tier B - engaged, open account
  Signal: engaged attendee or registered replay viewer AND account has open opportunity
  Route: account owner notification, no cold sequence. Next working day
Tier C - engaged
  Signal: top third by share watched, questions, resource clicks (thresholds from eps 7-8)
  Route: product nurture, only for registrants who ticked the marketing box;
         otherwise the replay email only
Tier D - registered
  Route: the replay email they registered for

Never routed to sales: Tier C and D, unless they later meet Tier A.
Sales acceptance bar: 50% of Tier A accepted (baseline); read back after each episode.
Review: at season end, tighten Tier A if acceptance stays under the bar.
Opt-out: honoured within 5 business days across sales and marketing tools (baseline).
Retention: 12 months after season end.
Legitimate-interest assessment for sales calls/account notes: <link, date> (record before first Tier A/B routing)
Signed: <DevRel owner> <Sales owner> <date>
```

**Form**

- Collect name, email and at most one qualifying field (company).
- Ask for a work email only if Tier B matching needs it.
- Disclose recording, engagement tracking, possible sales contact, retention and opt-out.
- Show an unticked marketing box to every registrant. Route Tier C on that box alone.

**Partner (35% of registrants)**

- Newsletter-only promotion needs nothing more. The partner gets no list.
- If the partner wants registrants or decides form fields, sign a joint-controller arrangement, name the partner on the form, and add a separate unticked partner box.
- Registrants who signed up on the partner's form and were passed over get the replay and the new notice only, with no sales route.
- Past registrants who never saw the sales notice get the replay and the new notice.

## 6. Episode log

| Episode | Registrants by source | Live | Live ÷ reg | 30-day on-demand (platform + YouTube) | Total reach | Returning | Live completion | Replay completion | Questions | Tier A / accepted | Replay published (h) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1-3 | enter | enter | enter | enter | enter | | | | | | |
| 4 | 270 (pooled 40/35/25 paid/partner/own; per-episode split to export) | 58 | 21.5% | ~90 + 350-450 | 498-598 | — | — | — | — | — | — |
| 5 | 290 (same pooled split) | 65 | 22.4% | ~90 + 350-450 | 505-605 | — | — | — | — | — | — |
| 6 | 285 (same pooled split) | 61 | 21.4% | ~90 + 350-450 | 501-601 | — | — | — | — | — | — |
| 7 | | | | | | | | | | | |
| 8 | | | | | | | | | | | |
| 9 | | | | | | | | | | | |
| 10 | | | | | | | | | | | |

Enter exact YouTube counts, and label them "upper bound" where they are views rather than unique viewers.

## Before Jan 12 (about 5 hours)

1. Per-source export for episodes 4-6, plus LinkedIn spend (30 min).
2. Meet sales and sign the contract (45 min).
3. Score the backlog from real community and support questions (2 h).
4. Tag every replay link by episode (1 h).
5. Brief the VP with the verdict above (15 min).

Next: run step 1 and paste me the per-source attendance rates. I will rewrite the episode 8 lever from that.