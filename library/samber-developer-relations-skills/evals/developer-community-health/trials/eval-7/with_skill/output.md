# Fernwood community health — verdict + framework

## Should you buy the $900/mo platform?

**❌ No — not now.** Three independent reasons, any one of which is sufficient:

- **Budget contradiction.** You said zero budget. $900/mo ($10.8k/yr) isn't "not yet" — it's off the table regardless of the platform's merits.
- **You haven't exhausted the free rungs.** The instrumentation reality-check rule: promote to a paid community-data platform only when three things hold *together* — multiple venues (yes, you have that), a named pipeline owner (yes, you), **and** a question the free rungs have already failed to answer twice. You're at zero attempts on the free rungs. Nothing has failed yet because nothing's been tried.
- **At your actual active scale, the two things they're selling are hand-solvable.** Participation inequality (Nielsen, 2006 — roughly 90% lurk / 9% occasional / 1% heavy) means your 1,800 members are more like ~18 core people and ~160 occasionals doing almost everything visible. Cross-platform identity for ~150–200 people is a spreadsheet with two columns (Discord handle, Discourse handle), not a $10.8k/yr pipeline. Cohort retention is arithmetic on two CSV exports (Discourse's user list has join date and last-seen; a free Discord bot or Server Insights covers the other side).

**The actual fire you should be fighting isn't identity or cohorts — it's the 90-day Discourse window.** That's a real, board-relevant risk ("Retention windows" trap: rented venues cap history, and backfill is often impossible). The fix costs $0: a recurring calendar reminder to export Discourse's admin CSVs monthly into your own spreadsheet, forever, starting this month. Do that and the vendor's "retained history" pitch stops being a reason to pay them — you're already retaining it yourself.

**When to actually revisit this:** after 2–3 quarters of manual tracking, if a specific decision keeps stalling because identity-matching or cohort math is genuinely unanswerable by hand at the volume you're seeing, *or* budget appears from elsewhere. Even then, get a quote for a self-hosted/open-source community-analytics stack first — the CHAOSS ecosystem has free tooling that does the same job as a category of paid platforms.

---

## Assumptions (flag these back to me if wrong — they drive the sheet below)

I don't have a live interview here, so I inferred the following from your message. Correct any of these at the next review and the sheet updates:

- **Primary outcome: support deflection** — members answer each other's usage questions so the support load doesn't sit entirely on one person, with product feedback as a close secondary. (You didn't state this explicitly; if it's actually product feedback or retention, the metric ranking below shifts.)
- **No open-source contributor base.** Closed source, no public repo → the "contributor funnel" pillar can't use forge/git data at all. Reframed below as a *participation* funnel (lurker → poster → regular), not a code-contribution funnel.
- **Individual-adoption, not account-based.** Nothing suggests Discord/Discourse members map to named customer accounts, so I'm treating this as an individual-adoption community, not B2B-account community. If most active members actually cluster into a handful of paying company accounts, that's worth checking — it would change the unit of measurement from "person" to "account" and surface expansion signal you're currently blind to.
- **No acute symptom.** You didn't describe a specific worry (no drop, no burned-out maintainer complaint) — this reads as the "no idea if it's working" case, not diagnosis mode.
- **Nothing is currently tracked except total member count** (1,800) — which is exactly the failure mode this framework exists to avoid: it only ever goes up and can't detect a community going quiet.

---

## Primary outcome

Peer support and light product signal: the Discord + Discourse community answers its own usage questions and surfaces feedback, so the one community person's and engineering's time isn't consumed by repeat troubleshooting.

## Metric sheet

All six metrics start **baselining** — you have no prior periods and the only historical asset (Discourse) ages out at 90 days, so today's snapshot is baseline period 1, not a finished reading. Thresholds below are the field's commonly-quoted starting points, explicitly labeled — replace every one with your own trailing median once you have 3 monthly periods (SKILL's own minimum before trusting a cutoff).

| Metric | Pillar | Formula | Source (free, ≤3h/mo) | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Active participants / month | Activity | distinct non-bot people who posted in Discord + Discourse (hand-merged identity, top ~150–200 active people only — no need to map all 1,800) | Discord Server Insights (enable the free "Community" server feature) + Discourse Admin → Users/Topics reports | baselining | set at trailing median after 3 periods (self-set) | You | Diagnose before acting — check for launch/release burst first |
| Non-you share of monthly messages | Activity | messages not written by you ÷ total | same two sources, manual tally on a sample if full counts aren't exportable | baselining | <30% "healthy" / >50% "act now" (unsourced/folklore — starting hypothesis only) | You | Recruit/recognize a couple of regulars to answer before you do |
| Zero-reply rate, forum (7-day window) | Responsiveness | Discourse topics with 0 replies within 7 days ÷ total topics | Discourse Admin topic list, sort by reply count (built-in, no plugin needed) | baselining | <10% healthy / >25% act now (unsourced/folklore) | You | Weekly 10-min sweep of unanswered topics; note Discord-side responsiveness stays unmeasured for now — too costly to track by hand, revisit if Discord becomes the main support channel |
| Second-post rate within 90 days (Discourse join cohorts) | Contributor funnel | first-time posters who post again within 90 days ÷ first-time posters, by monthly join cohort | Discourse Admin Users CSV export (join date, last-seen); sample rather than track every user if volume is high | baselining | set after 3 monthly cohorts (self-set); widen the cohort window if any monthly cohort is under ~10 people — daily/weekly cohorts here will just be noise | You | Review how long newcomers wait for a first answer |
| Absence factor (posts) | Concentration | smallest number of people producing 50% of monthly posts, combined venues where identity is mapped | manual: rank posters by message count, count down to 50% (CHAOSS definition; the repo script doesn't apply — no git history here, compute by hand from the ranking) | baselining | factor of 1–2 = single point of failure, worth a name on the watch list (self-set interpretation, not a published cutoff) | You | If it's you or one member, that's a personal bus-factor risk — worth surfacing to leadership even without a full sheet |
| Recommendability | Sentiment | "How likely are you to recommend this community?" — Likert, scored promoters% − detractors% | 2-question quarterly pulse via a free Google Form or native Discord poll | baselining, report response rate alongside the score always | drop of >15 points from your own baseline (self-set) | You | Interview a few detractors from the free-text answer |

Pass-threshold check: every row has a definition, a free source, an explicit baseline state, a labeled threshold, and a named owner + action. Six metrics, all four pillars covered, one bonus concentration row — under the 8-metric ceiling.

## Collecting this in under 3 hours/month

One-time setup (~20 min, do this once): enable Discord's free "Community" server feature to unlock Server Insights — no bot, no engineering, no cost.

Monthly (~100–120 min):
- Pull Discord Server Insights numbers — 10 min
- Pull Discourse Admin reports (Topics/Posts/Users) + sort topic list by reply count for zero-reply rate — 20 min
- Export Discourse Users CSV, update your running cohort spreadsheet — 20–30 min
- Hand-tally non-you share and absence factor from the same exports — 20 min
- Update the spreadsheet, write the one-page reading against baseline — 20–30 min

Quarterly, add ~30–45 min in that month for the recommendability pulse (post it, wait a few days, score it).

This leaves buffer inside your 3-hour ceiling even in survey months, and it's the exact habit that solves the 90-day-retention problem for free — you're building your own permanent history one month at a time, starting now, before this month's data ages out.

## Findings (day-one, evidence you already gave me)

1. **The only thing currently tracked is a vanity number.** Total Discord members (1,800) can only go up and, per this framework's own failure-mode list, can't detect a community going quiet. Confidence: high — you stated it directly.
2. **You're one Discourse retention window away from losing history you can't get back.** The free tier's 90-day cap means anything not snapshotted this month is gone permanently once it ages out. Confidence: high — stated venue constraint, not inferred.
3. **The vendor's pitch targets a problem you don't have yet.** Cross-platform identity and cohort retention are real needs only once manual tracking demonstrably fails — you're at zero manual attempts, so the pitch is solving a hypothetical, not an observed, gap. Confidence: high, given the "zero budget" and "no prior tracking" facts already stated.

## Actions

| Action | Owner | By when | Metric it should move |
|---|---|---|---|
| Enable Discord Server Insights (free Community server feature) | You | This week | Active participants |
| Export Discourse Users CSV and start the cohort spreadsheet — do this before any more history ages past 90 days | You | This week | Second-post rate, absence factor |
| Run first zero-reply sweep on the forum | You | Within 2 weeks | Zero-reply rate |
| Send the vendor a "not now" with the specific revisit condition (2–3 quarters of manual tracking, or a named unanswerable question) | You | Next vendor touchpoint | — |
| Field the first 2-question recommendability pulse | You | This quarter | Recommendability |

## Watch list

- Discord-side responsiveness stays unmeasured for now — no cheap native source; revisit only if Discord overtakes the forum as the main support venue.
- First-time-poster tracking on Discourse may need to move from "track everyone" to "sample" if volume is high — check after month one.
- Whether active members cluster into a handful of paying company accounts (would flip this from individual-adoption to B2B account-based reading) — worth one look at your CRM/license data if easy.
- Primary-outcome assumption (support deflection) — confirm or correct at next review; it drives which metric gets weight if you ever have to cut further.

## Next review

One month from your first data pull — re-check whether the collection plan actually fit inside 3 hours, and whether "baselining" can start converting to real thresholds on the metrics with enough data (funnel and absence factor will likely still be baselining; activity and responsiveness should have one real reading).