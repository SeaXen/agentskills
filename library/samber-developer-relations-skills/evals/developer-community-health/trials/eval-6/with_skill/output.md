Using the developer-community-health skill (read in full, along with metric-catalog.md, survey-instruments.md, and health-report-template.md — the contributor-absence-factor.sh script doesn't apply, since there's no git/forge history behind a Slack Connect community).

Two things need your confirmation before this report is "real" rather than a draft — flagged inline below rather than blocking delivery: the primary outcome (I inferred one), and whether "34 people posted" already excludes Quarrystone staff. Everything else uses what you gave me.

---

# Community health - Quarrystone Customer Slack - August 2026

## Primary outcome

*Assumed — confirm with VP before next cycle.* **Success**: sustained engagement in the customer Slack is a leading indicator of account health, retention and expansion — customers who get peer/product help here are less likely to churn quietly and more likely to surface expansion signals early. Every metric below should plausibly move when that signal moves. If the real mandate is support deflection (ticket reduction) instead, swap metric 4's threshold framing accordingly — the metric itself doesn't change.

This is a **B2B community**: the unit that matters is the customer account (41 of them), not just the person. Two of the six metrics below exist specifically to make the account visible — plain "member count" and "message count" hide account-level risk (e.g., 30 of your 34 posters could belong to 3 accounts).

## Metric sheet

| Metric | Pillar | Definition / formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Monthly active user % (MAU%) | Activity | Distinct non-staff, non-bot individuals who posted or reacted in the period ÷ 187 total members | Slack member list + channel export (venue analytics rung) | **Baselining** — this is the first reading | 20% healthy / <10% act-now (**folklore, unsourced — replace with your own trailing median after 3 months**) | Community lead | Diagnose before acting: check for account concentration, event/no-event distortion |
| Active account coverage | Activity (B2B unit) | Customer accounts with ≥1 active member in the period ÷ 41 | Slack handle → account mapping (hand-maintained; **not yet built**) | **Baselining — data gap, see Watch list** | <60% of accounts represented (**self-set**, revisit after 3 periods) | Community lead / CS ops | Reach out to the silent accounts named at renewal or QBR risk |
| Message volume / growth | Activity | Total human messages (staff+bots flagged and excludable) per month, trend vs trailing baseline | Slack export, snapshotted monthly into your own store | **Baselining** — only "34 posters" given, no message count yet | No fixed threshold; read as trend once 3 points exist | Community lead | n/a until baseline exists |
| Unanswered question rate | Responsiveness | Question threads with zero human reply within 2 business days ÷ total question threads | Manual weekly sweep of channels (feasible at this volume — no forge/API here) | **Baselining** | >20% (**folklore, unsourced**) | Community lead | Recruit a second answerer rotation; flag account by name |
| New account activation | Contributor funnel (B2B) | Accounts posting for the first time this period, reported as a **named list with dates**, not a rate (41 accounts is small-N — a percentage here would be noise) | Slack export + account mapping | **Baselining** | n/a — read qualitatively until 3+ periods of history exist | Community lead / CS | Loop new account's CSM in if no post within 30 days of Slack invite |
| Recommendability (NPS-style) | Sentiment | "How likely are you to recommend this community to other people?" — Likert, scored **promoters % minus detractors %** | Quarterly pulse survey | **+33** (n=6, 3.2% response rate) — see caveat below | n/a — treat as a hypothesis, not a threshold, until response rate clears ~30 responses | Community lead / VP sponsor | Widen distribution before trusting any swing in the score |

All six metrics carry a formula, a source, a baseline (or an explicit "baselining" mark), a threshold labeled by origin, and an owner+action — per this skill's pass criteria. Four pillars are covered: Activity (3), Responsiveness (1), Funnel (1), Sentiment (1).

## Reading - August 2026

| Metric | This period | Baseline | Direction | Note |
|---|---|---|---|---|
| MAU% | **18.2%** (34/187) | none yet | — | First reading. Sits just under the unsourced 20% "healthy" folklore line — not a real signal on one data point |
| Active account coverage | not computed | none | — | Identity-to-account mapping doesn't exist yet (see Watch list) |
| Message volume | not computed | none | — | Only poster count was captured, not message count |
| Unanswered question rate | not computed | none | — | No sweep run yet this period |
| New account activation | not computed | none | — | Needs the same account mapping as coverage |
| Recommendability (NPS) | **+33** | none | — | n=6 of 187 (3.2% response rate). Report the score and the response rate together, always — a 33 built from 6 answers is a conversation starter, not a trend point |

## Findings

1. **MAU% (18.2%) cannot be read as good or bad yet — there is no baseline, and it's a single number against an unsourced folklore band.** Evidence: 34/187, no prior period on record. Confidence: none (first reading) — do not report this to the VP as "healthy" or "at risk," report it as the starting point.
2. **The NPS score is not yet trustworthy as a metric, only as a hypothesis.** Evidence: 6 respondents out of 187 members (3.2%) — well below the ~30-response floor this skill's own catalog uses before treating a survey result as anything but qualitative. Confidence: low. A swing to +10 or +60 next quarter with a similarly small n would not, by itself, mean anything moved.
3. **The most important number for a B2B community — account coverage — doesn't exist yet.** Evidence: you know 34 people posted, not how many of the 41 accounts they belong to. It's entirely possible those 34 people sit in 8 accounts and 33 accounts are silent, which is a materially different story than "34 of 187 people are engaged." Confidence: n/a — this is a data gap, not a finding.

## Actions

| Action | Owner | By when | Metric it should move |
|---|---|---|---|
| Build a hand-maintained Slack-handle → customer-account mapping (41 accounts, low volume — a spreadsheet is enough) | Community lead | Before next month's reading | Active account coverage, new account activation |
| Start a monthly snapshot of raw message counts and MAU into your own store (sheet/DB) — Slack retention limits mean you can't backfill later | Community lead | Before next month's reading | Message volume / growth |
| Confirm whether the "34 posters" figure already excludes Quarrystone staff and any Slack apps/bots in the workspace | Community lead | This week | MAU%, message volume (both are meaningless if staff/bots are mixed in) |
| Run a manual sweep of the last 30 days for questions with no reply within 2 business days, to get the first responsiveness reading | Community lead | Before next month's reading | Unanswered question rate |
| Confirm the primary outcome (success/retention signal vs. support deflection) with the VP | Community lead | Before this report is finalized | Frames which threshold direction matters on every metric above |
| Check each of the 41 accounts' contracts/DPAs before any bulk export of Slack Connect message content — cross-company data in one workspace raises more privacy exposure than a single-tenant community | Community lead / legal | Before the next bulk export | Privacy gate — not a metric, a precondition for computing any of the above |

## Watch list

- Account coverage, message growth, unanswered-question rate and new-account activation are all "baselining" — the instrumentation to compute them doesn't exist yet. Expect this report to look thin for one to two more cycles while the mapping and snapshot habit get built; that's expected, not a failure.
- NPS response rate (3.2%) is too low to support a trend line. See survey design notes below before the next quarterly wave.
- Staff/bot exclusion is not yet confirmed for the 34-poster figure — treat MAU% as provisional until that's checked.

## Next review

**2026-10-15** — first month with account coverage and message volume computed; re-check MAU% now that staff/bots are confirmed excluded or not.

---

## Quarterly NPS survey — design notes for the next wave

Since you're planning the next one, three changes would make the number worth reporting instead of just collecting:

- **Keep it to the two-item pulse**, nothing longer at quarterly cadence: (1) "How likely is it that you would recommend this community to other people?" (Likert), (2) "What is the most frustrating thing about participating here?" (free text, optional).
- **Widen distribution before the next send.** 6 responses from 187 members is a 3.2% response rate — even a modest improvement to, say, 15-20% (28-37 responses) would put you near the floor where the score stops being pure noise. A realistic B2B lever: ask each of the 41 account owners/CSMs to nudge their own account's Slack members, rather than one blast to the whole channel.
- **Report response rate next to the score every time**, in every future version of this report — "+33 (n=6)" not just "+33." That discipline is what stops a future reader from treating month-to-month swings on a 6-person sample as a real trend.
- **Keep the scoring convention consistent going forward**: promoters % minus detractors %. Confirm the +33 you already have was computed this way (not the CHAOSS knowledge-base page's inverted phrasing) so the next wave is comparable to it.
- **Segment consistently**: define the survey population once ("all Slack Connect members active in the last 90 days," or "all 187 members" — pick one) and keep it fixed between waves, or the trend measures your sampling change, not sentiment.
- Given only 41 accounts, consider a lightweight **lapsed-member question** for anyone who's gone quiet 60+ days — those members hold the answer to *why* an account went dark, and account-level silence is a bigger risk signal here than it would be in a large open-source community.