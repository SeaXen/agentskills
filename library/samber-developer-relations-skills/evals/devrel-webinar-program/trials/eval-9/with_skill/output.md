# Pinebarrow webinar series: measurement sheet and board slide

I built this from the `devrel-webinar-program` skill.

## Open decisions (read first)

No one was available to answer the interview, so these are assumptions. Each one changes the sheet if it is wrong.

| # | Decision | Status |
|---|---|---|
| 1 | **Series job = activation**: signup to first index. You stated this. Everything below ranks on it. | Given |
| 2 | **The CEO's 20-40% attendee-to-MQL benchmark is not a valid target.** The skill refuses it (see Diagnosis). | Needs CEO conversation |
| 3 | **The agency's 44% lead-to-MQL and 39% MQL-to-SQL are not Pinebarrow targets.** | Needs CEO conversation |
| 4 | A free tier or sandbox exists where an attendee can build a first index. Assumed, because "signups to their first index" implies a signup flow. | Assumed |
| 5 | I don't know how many episodes made up the 3,800, or how many live attendees, replay views or unique people there were. These cells are marked NEEDED. | Missing data |
| 6 | Host size and registrant source mix are unknown. Without them no population band applies, so the first two episodes of the new season set the live-attendance baseline. | Missing data |
| 7 | Named sales owner for the handoff contract. | Open |
| 8 | Region split of developers, which fixes the slot. Tuesday 11:00 ET is a placeholder. | Open |
| 9 | Whether any partner co-hosts, which triggers the joint-controller steps. | Open |

---

## 1. Diagnosis

**Denominators first.**

- **3,800 is registrations, not people.** Report unique registrants beside it. The same person across several episodes counts several times.
- **Registrations against the 11,000 invite list.** Only the registrations that came from list members count against it. Split them out (NEEDED). Until then, 3,800 / 11,000 = 34.5% is an upper bound and not a conversion rate.
- **410k LinkedIn impressions are an input, not a result.** Registrations per 1,000 impressions is 3,800 / 410,000 = 9.3. That is an upper bound for LinkedIn, because the 3,800 also includes email, community and other sources. Organic social registrants also tend to show up less than owned-list registrants.
- **"Attendee-to-MQL" has no valid benchmark.**
  - "20-40% of attendees become qualified leads" is on the skill's refused list. It cites "industry benchmarks" with no named study. Any attendee-to-MQL rate is unverified unless it states its sample and its MQL definition.
  - The agency's 44% and 39% are client data reported second-hand (First Page Sage). They rest on those clients' own MQL definitions and are lead-to-MQL and MQL-to-SQL. Those are different stages from attendee-to-MQL.
  - Neither figure transfers to Pinebarrow's funnel.
- **The series' job is not MQLs.** Making MQL the headline would judge it on a number the job never needed. It would also push sales to call every attendee, which lowers acceptance and burns the audience.

**Pattern read (Step 6).** I can't classify it yet. Registration looks healthy at 3,800. Live attendance and replay reach are not supplied, so I can't pick between "prefers on demand" and "bought registrants". Fill the episode log, then read:

- low registration and low attendance: fix the topic
- healthy registration, low live, healthy replay: invest in the replay
- healthy registration, low live, low replay: shift promotion to own users

**First fix:** replace the benchmark on the slide with Pinebarrow's own baseline and a dated commitment to set targets after the first two episodes. Details are in section 7.

---

## 2. Measurement sheet

### Tab A: Definitions (lock before filling anything)

| Term | Definition |
|---|---|
| Registrations | Form submissions, one per person per episode |
| Unique registrants | Distinct emails across the period |
| Live attendee | Registrant who joined the live session |
| Live attendance | Live attendees / registrants of that episode (the total-over-total ratio, not a mean of ratios) |
| 30-day on-demand | Unique viewers within 30 days of the session, on the platform plus any public video copy. Use views labelled "upper bound" if unique viewers aren't reported. |
| Total reach | Live attendees + 30-day on-demand viewers, all surfaces |
| Engaged attendee | Top third of attendees by watch share, questions and clicks. Set the thresholds from episodes 1-2. |
| Job metric | Attendee reaches first index within 30 days of the session |
| First index | Define the exact event, e.g. first successful index-create plus at least one upsert (OPEN: confirm with product, and log which event) |

### Tab B: Episode log

Columns come from the skill's template, plus the activation columns this job needs. Past episodes enter as the pilot baseline and future rows stay empty.

| Episode | Date | Registrations | Unique new registrants | From invite list | From other sources (newsletter / social / community / paid / partner) | Live | Live / registrants | 30-day on-demand | Total reach | Returning attendees (share) | Live completion | Replay completion | Questions per 10 live | Tier A / accepted | Replay published (h) | First index ≤30d (attendees) | Activation rate (attendees) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Pilot baseline, year to date (aggregate)** | Jan-Oct 2026 | **3,800** | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | NEEDED | none (no contract yet) | NEEDED | NEEDED | NEEDED |
| Season ep. 1 | | | | | | | | | | | | | | | | | |
| Season ep. 2 | | | | | | | | | | | | | | | | | |
| Season ep. 3 | | | | | | | | | | | | | | | | | |
| Season ep. 4 | | | | | | | | | | | | | | | | | |
| Season ep. 5 | | | | | | | | | | | | | | | | | |

Formulas:

- Live / registrants = Live ÷ Registrations
- Total reach = Live + 30-day on-demand
- Returning share = attendees who attended at least one earlier episode ÷ Live
- Activation rate = First index ≤30d ÷ Live

Fill the past aggregate row from the platform export before the board meeting. If episode-level data exists, enter each past episode as its own baseline row.

### Tab C: Targets and bars

| Signal | Target | Basis |
|---|---|---|
| Total reach | Flat or rising vs baseline | Baseline |
| Live attendance | At or above the series' pilot median. Population band only once host size and source mix are known (see open decision 6). | Own baseline |
| Returning-attendee share | 20% or more by episode 4 (baseline) | Skill baseline, reset after season one |
| Live and replay completion | Track the trend | Goldcast 2026: 74% live, 91% on demand |
| Questions per 10 live attendees | At or above the charter bar, set from season one | Baseline |
| **Job metric: attendee 30-day first-index rate** | Ahead of the holdout group, pooled over the season | Directional; causal via the holdout in Tab D |
| Tier A handoffs: sales acceptance | 50% or more (baseline, sales to agree) | Contract |
| Replay within 48 h; next season's speakers booked | Every episode | Baseline |

### Tab D: Activation experiment (holdout)

An eligible invite list of about 11,000 is large enough to hold out. The skill's baseline is 10-20% of the list, held out from invitations for one season.

| Item | Value |
|---|---|
| Eligible list | 11,000 |
| Holdout at 15% (midpoint) | 1,650 held out |
| Invited | 9,350 |
| Range | 10% = 1,100 held out; 20% = 2,200 held out |
| Assignment | Random, fixed before episode 1, stored in a file with seed and date |
| Outcome | First index within 30 days of each episode date (same window for holdout) |

Rough sensitivity, assuming a 5% base activation rate. This is my assumption, not a Pinebarrow figure. With 1,650 vs 9,350, a lift of about 1.6 percentage points is detectable at 80% power. Recompute with the real base rate from the pilot row.

Caveats:

- The holdout controls invitations only. Held-out developers can still register through social or community channels. Log those as "holdout crossover" and keep them in their assigned group (intention-to-treat).
- Registrants outside the list aren't in the experiment. Compare them to matched non-attendees (directional only).
- Document this before the season starts. It is the only way to separate "the series causes first indexes" from "motivated developers attend".

### Tab E: Handoff tracker (per episode)

| Tier | Signal | Count | Routed to | Timing | Accepted |
|---|---|---|---|---|---|
| A: hand-raise | Asked for a demo, pricing or contact; clicked a pricing or demo CTA | | Sales, with episode and question | Within 1 business day | |
| B: engaged, open account | Engaged attendee or replay viewer at an account with an open opportunity | | Account owner notified, no cold call | Next working day | |
| C: engaged | Engaged attendee who ticked the marketing box | | Product activation nurture | Episode follow-up | n/a |
| D: registered | Registered, attended briefly or not at all | | Replay email they registered for | Episode follow-up | n/a |

MQL, if the company still reports it, is counted from Tier A only. It is a secondary column, never the headline.

---

## 3. Board slide: draft

**Title:** Developer webinars: reach, and whether it gets developers to their first index

| Metric | Value | Note |
|---|---|---|
| Registrations, 2026 YTD | **3,800** | Registrations, not unique people. Unique registrants: [NEEDED] |
| LinkedIn impressions | **410k** | Awareness input. 9.3 registrations per 1,000 impressions, an upper bound for LinkedIn because the 3,800 includes all sources |
| Live attendance | [NEEDED]% of registrants | The new baseline for next season |
| Total reach (live + 30-day replay) | [NEEDED] | |
| Attendee-to-MQL | [NEEDED]%, with our MQL definition printed on the slide | No external benchmark shown (see below) |
| **Job metric: attendees reaching first index in 30 days** | Measured from episode 1; holdout from next season | The number that matches the series' purpose |

**Footnote for the 20-40% benchmark:** "We don't compare against a 20-40% industry figure because it traces to no named study. Our target is set from our own first two episodes."

**Talking points for the CEO (3 sentences):**

1. "Registrations and impressions show we reach developers, but the series exists to get them to a first index, so that's the number we'll report next to them."
2. "The 44% and 39% figures are one agency's clients under their own MQL definitions. They don't transfer to our funnel, and committing to them would set us up to miss a target that measures a different thing."
3. "We'll set our own conversion targets after the first two episodes, which leaves us with a number we can defend in the next board meeting."

If the CEO insists on an MQL target for the board, the defensible version is: report Pinebarrow's own attendee-to-MQL rate under Pinebarrow's own definition, with no external comparison.

---

## 4. Charter (one page, provisional)

```
Series name: [open]
Job (first): activation, signup to first index.   Secondary: feature depth (recall, filters, scale)
Audience: backend and ML engineers building search/RAG, intermediate; region split NEEDED
Format mix: engineer conversation and live demo alternating; one follow-along lab per season
  on the free tier (job = activation and a free tier is assumed, interview Q1/Q4)
Cadence and length: monthly (default; sized from capacity), 40 minutes; lab 55 minutes
Slot: Tuesday 11:00 ET placeholder; test a second slot on two episodes of the same format
Season: 5 episodes, Nov 2026 to Apr 2027 (provisional; skips December)
Speaker pool: internal engineers (agree hours with managers), community answerers,
  at most 1 customer (start approval 6-8 weeks ahead); named backup per episode. All OPEN.
Replay policy: ungated chaptered copy within 48 h; 2 clips per episode; captions and transcript;
  gate the lab environment only
Budget: platform, paid promotion (none in the first episodes; shift promotion to own list),
  lab infrastructure, captioning, honoraria. All OPEN.
Data retention: registrant and engagement data deleted 12 months after season end (baseline)
Handoff contract: signed [date], sales owner [name]. OPEN.
Continue bar (written before episode 1):
  - no metric among total reach, live attendance, returning share below the first-two-episode
    median on two of episodes 3-5
  - returning-attendee share: 20% or more by episode 4
  - job metric: attendees' 30-day first-index rate ahead of the holdout
  - stop rule: two seasons failing the job metric, or no backlog for a season
Open decisions: see the list at the top.
```

## 5. Season plan (provisional)

Dates are Tuesdays. Everything here past the first season is provisional.

| # | Date | Format | Problem-titled topic | Speaker | Backup | Replay | Job signal |
|---|---|---|---|---|---|---|---|
| 1 | 2026-11-10 | Live demo | From zero to your first index in 20 minutes | OPEN (internal eng) | OPEN | Ungated chaptered + 2 clips | First-index rate |
| 2 | 2027-01-12 | Engineer conversation | Why recall drops as your index grows, and what to tune | OPEN | OPEN | Ungated chaptered + clips | Returning share |
| 3 | 2027-02-09 | Follow-along lab | Build semantic search on the free tier, with attendees | OPEN + chat helper | OPEN | Re-runnable lab, scheduled replay | **First-index rate (primary)** |
| 4 | 2027-03-09 | Live demo | Filtered search without wrecking latency | OPEN | OPEN | Ungated chaptered + clips | Questions |
| 5 | 2027-04-13 | Engineer conversation | Moving from pgvector to a dedicated index: what broke | OPEN | OPEN | Ungated chaptered + clips | Total reach |

Release episodes: 0 of 5 (cap is under a third).

## 6. Topic backlog (scored 0-2 per column)

| Topic | Job fit | Developers affected | Speaker exists | Replay life > quarter | Total |
|---|---|---|---|---|---|
| First index in 20 minutes | 2 | 2 | 2 | 2 | 8 |
| Build semantic search on the free tier (lab) | 2 | 2 | 1 | 2 | 7 |
| Recall drop as the index grows | 1 | 2 | 1 | 2 | 6 |
| Filtered search latency | 1 | 2 | 1 | 2 | 6 |
| pgvector migration | 1 | 1 | 1 | 2 | 5 |
| Cost of a 100M-vector index | 1 | 1 | 1 | 2 | 5 |

These are hypotheses. Re-score with real inputs: top forum questions, docs search terms with no result, and the trial step with the largest drop. The sign-up-to-first-index funnel's biggest drop-off step should set the order.

## 7. Handoff contract

Draft, to be signed by DevRel and a named sales owner before episode 1. Legal reviews the wording.

- **Route on behaviour, never on attendance alone.** Tiers A-D are in Tab E. Tier C and D are never routed to sales unless they later meet Tier A.
- **"Every attendee is an MQL" is rejected.** Reasons: sales works leads that never wanted contact, developers who get a call after a technical session stop registering, and the series gets judged on volume its job doesn't need.
- **Sales acceptance bar:** 50% of Tier A (baseline). Read it back after each episode and tighten Tier A if acceptance stays under the bar.
- **Form:** name, email, at most one qualifying field. Notice that the session is recorded, that attendance, watch time and clicks are used to decide follow-up, and that the sales team may contact them. Include the opt-out, the retention period and a privacy-notice link.
- **Marketing email:** one unticked opt-in box shown to every registrant. Tier C nurture goes only to those who ticked it, whatever their country.
- **Sales calls and account notes** based on webinar behaviour need a recorded legitimate-interest assessment.
- **Past registrants** who were never told sales may follow up get the replay and the new notice. They don't enter the tiers.
- **Partners:** a partner who decides fields or follow-up makes the episode co-hosted. That requires a signed joint-controller arrangement, the partner named on the form, and its own unticked box. Never hand a sponsor the full list.

## 8. What to do before the board deck (in order)

1. Pull from the webinar platform, per episode: registrations, unique registrants, live attendees, on-demand views, source split (~30 min).
2. Pull from product analytics: for each past attendee, whether they created a first index within 30 days, and the same for matched non-attendees.
3. Fix the exact "first index" event with product, then fill the pilot row in Tab B.
4. Randomise the 15% holdout (1,650 of 11,000) and store the file with its seed and date.
5. Replace the benchmark footnote on the slide, and put the MQL definition on it.

Everything marked NEEDED is a number I could not invent. The slide should not go out with a blank in those cells.