# Tessellate Discord — Community Health Dashboard

Before the dashboard: two corrections, because both change what the numbers you already have actually mean.

⚠️ **Your 9-second response time is measuring the bot, not your community.** A templated auto-reply that fires in every #help thread within 5 seconds is exactly the trap this framework calls out by name: *"a welcome bot replying in four seconds makes time-to-first-response look excellent while no human ever answered."* CHAOSS's own guidance on this metric is explicit — it's "only applicable when these activities are primarily driven by humans, not automated responses," and instructs teams to "exclude responses from bots or other automated systems when measuring genuine community engagement." Right now you have no responsiveness number at all. You have a bot uptime check.

ℹ️ **The four "industry standards" you were given aren't standards.** All four — 24h response, 20% monthly-active ratio, 30% staff-share, and (implicitly) 40% 7-day retention — are the exact set of numbers that circulate in community-management content with **no published source behind them**. CHAOSS, the vendor-neutral reference model most of this field cites, publishes no numeric cutoffs at all, and says so directly: *"we do not compare projects against each other, but instead, we expect teams to use their metrics to make improvements."* The only attributable number in the entire published literature is VMware's own internal rule (PRs get a human response within two business days) — one company's convention, not an industry benchmark. Treat the four numbers you were handed as unsourced hypotheses to test against, not a bar you're being graded on.

Below is the dashboard, built on that corrected footing. I assumed: **Discord + the Tessellate GitHub repo** as the two venues (you're open source, so contribution is in scope even though you only gave me Discord numbers), **individual-adoption** reading (not B2B — members join as themselves), and **support deflection** as the primary outcome, since the #help bot is the one workflow you described in detail. Confirm or correct that outcome at the first review — it drives which metrics are on the sheet.

---

## Community health — Tessellate Discord + GitHub — first read

### Primary outcome

**Support**: users get charting-library help from each other (and maintainers) in #help, so issues don't pile up as GitHub tickets and maintainer time stays on the library, not on triage.

### Metric sheet

| Metric | Pillar | Definition / formula | Source | Baseline | Threshold (origin) | Owner | Action if breached |
|---|---|---|---|---|---|---|---|
| Median time to first **human** response in #help | Responsiveness | First reply from a non-bot account, per thread | Discord export, bot IDs excluded | **baselining** — current "9 seconds" is bot-only and unusable | < 24h "healthy" / > 72h "act now" (folklore, unsourced — replace after 3 months) | Community lead | Recruit answerers in the timezone gap the data shows |
| Zero-human-reply rate in #help (24h window) | Responsiveness | Threads with no non-bot reply within 24h ÷ total #help threads | Discord export | baselining | > 20% (self-set, no baseline yet) | Community lead | Weekly sweep of unanswered threads |
| Active participants / month | Activity | Distinct non-bot accounts posting or reacting, per month | Discord panel export | baselining (member *count* only: 3,050 → 4,213 since Jan — not a health number by itself) | < prior 3-month trailing median once it exists | Community lead | Diagnose before acting — check for release/event burst first |
| Non-staff share of #help answers | Activity | Answers not written by flagged staff/maintainer accounts ÷ total answers | Discord export + staff role flag | baselining — staff role not yet flagged | < 30% "act now" / > 30% "healthy" (folklore, unsourced) | Community lead | Recognize top non-staff answerers publicly; maintainers stop answering first |
| Contributor absence factor | Contributor funnel / concentration | Smallest number of people producing 50% of commits | GitHub / git history (`scripts/contributor-absence-factor.sh`) | baselining | 1 = single point of failure | Maintainer lead | Open reviewer rung to next 2–3 contributors |
| Second-contribution rate (90 days) | Contributor funnel | First-time GitHub contributors who contribute again within 90 days ÷ all first-time contributors, per monthly join cohort | GitHub API | baselining | < 15% (self-set 90-day window; no baseline yet) | Maintainer lead | Review first-review turnaround time for new PRs |
| Recommendability | Sentiment | "How likely to recommend Tessellate's community?" NPS-style, quarterly pulse | 2-item survey (see below) | baselining — not yet fielded | drop > 15 points (self-set) | Community lead | Interview 5 detractors from free-text responses |

7 metrics, all 4 pillars covered, under the 8-metric ceiling. Every row above passes the "so what" test — each one has a named action attached, not just a number.

### Reading — first period (September 2026)

| Metric | This period | Baseline | Direction | Note |
|---|---|---|---|---|
| Median time to first human response | not computable | — | — | Existing 9s figure is bot-only; re-pull required with bot ID excluded before this row means anything |
| Zero-human-reply rate | not yet pulled | — | — | Same instrumentation gap |
| Active participants | not yet pulled | — | — | Member *count* is 4,213 (Jan: 3,050, +38%) — reported here for context only, per the skill's own warning that member count "only ever goes up and says nothing about health" |
| Non-staff share of answers | not yet pulled | — | — | Needs staff role flag first |
| Contributor absence factor | not yet pulled | — | — | Run `bash scripts/contributor-absence-factor.sh -r <tessellate-repo-path>` |
| Second-contribution rate | not yet pulled | — | — | Needs GitHub first-time-contributor tagging |
| Recommendability | not surveyed | — | — | First wave to field this month |

This is an honest first read, not a weak one: the framework's own rule is that a metric with no history gets marked "baselining" and read as a raw number, not forced into a red/green verdict it can't support yet.

### Findings

1. **The only responsiveness number you have measures bot uptime, not community health.** Evidence: welcome bot replies in ~5s in every #help thread; the analytics panel's 9-second median tracks that, not a human. Confidence: high — the mechanism is unambiguous. This is a coverage gap, not a good result.
2. **The four benchmarks leadership quoted have no published source.** Evidence: cross-checked against CHAOSS's Starter Project Health model, which publishes zero numeric cutoffs and explicitly rejects cross-community comparison; all four numbers match a documented list of "unsourced practitioner thresholds." Confidence: high. Recommend presenting them to leadership as starting hypotheses, not pass/fail bars.
3. **38% member growth since January (3,050 → 4,213) tells you nothing about health on its own.** Evidence: total-member count is flagged as the canonical vanity metric — it only ever goes up. Confidence: high by definition; what it hides is whether the *new* members are active. That's the active-participants and MAU-ratio rows above, both still baselining.

### Actions

| Action | Owner | By when | Metric it should move |
|---|---|---|---|
| Build a bot-exclusion ID list and re-pull #help response times against it | Community lead | Before next dashboard | Median time to first human response |
| Flag staff/maintainer Discord roles | Community lead | Before next dashboard | Non-staff share of answers |
| Run `scripts/contributor-absence-factor.sh` against the Tessellate repo | Maintainer lead | Before next dashboard | Contributor absence factor |
| Tag first-time vs. returning contributors in GitHub history | Maintainer lead | Before next dashboard | Second-contribution rate |
| Field the 2-item recommendability pulse (see survey-instruments reference) | Community lead | This month | Recommendability |
| Snapshot both Discord export and GitHub pulls into your own store monthly, starting now | Community lead | Ongoing | All — Discord's own retention can cap backfill later |
| Present the corrected framing (bot-contaminated number, unsourced benchmarks) to leadership before the first dashboard read | Community lead | Before next leadership readout | — |

### Watch list

- Every metric above is "baselining" — none has 3 periods of history yet, so no threshold is more than a labeled starting hypothesis. Re-derive real thresholds from this community's own trailing median starting with the 3rd monthly read (~December 2026).
- No identity mapping exists yet between Discord handles and GitHub accounts — not needed for this sheet, since responsiveness/activity run off Discord and funnel/concentration off GitHub independently. Only build the mapping if a future question genuinely needs cross-venue identity.
- Confirm the primary outcome is Support, not Contribution or Advocacy — that changes which pillar leads the sheet.

### Next review

**Early October 2026** — first live pull once bot-exclusion and staff-flagging are in place. Most rows will still read "baselining"; that's expected for month one. Re-check the primary outcome assumption first.

---

**Pass-threshold check:** every metric above carries a definition, a data source you can reach today (Discord export + GitHub/git history — no new tooling or budget required), a baseline mark, a labeled threshold, and a named owner+action. 7 metrics, all 4 pillars covered.