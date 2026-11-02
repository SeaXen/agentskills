# DevRel Competitive-Intelligence Program: Scope

Developer-surface competitive intelligence, standing, one analyst FTE, 30 vendors, quarterly. Built on `devrel-competitor-analysis`'s method, scaled with tiering because that method's own peer-set convention (3-5) is sized for a single decision, not a market map six times wider.

## 1. What this covers, and what it doesn't

**In scope:** the eight developer surfaces the skill defines — docs/DX, open source, content, community, Q&A tags, events, hiring signals, plus the timed quickstart. Evidence only from what a logged-out visitor can read: no accounts, no purchases, no sales calls.

**Out of scope:** pricing, feature parity, win/loss reasons, deal-level battlecards. *Set by this analysis, following the skill's own interview step 7:* if product marketing or sales already runs a competitive-intelligence function, this program stays off that ground and cross-links to it rather than duplicating it. Confirm that owner before week one — worth checking now, since 42% of companies house competitive intelligence in marketing, not devrel (*published, Crayon State of Competitive Intelligence*), and this program's 30-vendor scope sits exactly at the edge of what a CI function normally tracks — nearly 8 in 10 CI teams track 30 competitors or fewer (*same source*). That's a plausible size for a full market map; it is not a plausible size for eight-surface depth on every entry, which is the reason for tiering below.

**A named risk, stated up front rather than buried:** the skill's failure-mode table lists "a standing competitive-intelligence effort nobody asked for" as a mistake, and its own guidance is never to assert that a benchmark is a program. Here it *was* asked for, by leadership, off a benchmark that already changed a decision — that's the legitimizing condition the skill itself looks for. The obligation that comes with it: every quarterly edition still opens with "what changes because of this," tied to a named decision-owner. A dashboard nobody reads decisions off drifts into scoreboard framing at 30x the surface area of the original one-off, which makes the failure mode more expensive, not less.

## 2. Coverage model: three tiers, not one flat table

*Set by this analysis.* Full 8-surface symmetry across 30 companies is the thing that breaks first — collection cost scales linearly with vendor count, so does everything downstream. Split by how much depth each vendor's competitive threat actually earns:

| Tier | Count | Selection | Surfaces | Cadence |
|---|---|---|---|---|
| **Core** | 4–6 | Category leader, 2–3 closest substitutes, 1 demand-side alternative (what a developer uses if we vanish — often OSS/DIY, per the skill's demand-side check) | All 8 | Docs/forge/content/Q&A quarterly; community/events/hiring twice-yearly (skill's own baseline cadence) |
| **Watch** | 8–12 | Credible movers not head-to-head today — the set most likely to promote into Core | Docs, forge metrics, Q&A tags (rungs 2–4: API-driven, cheapest per hour, lowest compliance load); quickstart semi-annual | Quarterly for the 3 rungs, semi-annual for quickstart |
| **Radar** | remaining ~14–18 | Everyone else on the market map | Forge release cadence + Q&A tag volume delta only, scripted pull, human review for anomalies | Quarterly, mostly automated |

Symmetry (the skill's own 100% quality target) applies **within a tier**, not across all 30 — a Radar-tier row is symmetric with other Radar rows, not with Core's full field list. State the tier next to every table in the report so a reader never mistakes a thin row for a weak finding.

**Promotion/demotion**, reviewed each quarter, on the skill's own re-run triggers applied per vendor: a Radar company that ships a major launch, reprices, or shows up in a lost-evaluator debrief gets promoted immediately, off-cycle — the calendar quarter is the floor, not the ceiling, matching the skill's position that event triggers matter more than the clock.

## 3. Cadence: what "every quarter on the dot" actually means

The dashboard refreshes every quarter, guaranteed — that's the commitment to leadership. What refreshes underneath varies by surface, because two rungs have a calendar constraint no amount of labor removes: content cadence needs a twelve-month window to separate a launch burst from a trend, and community volume needs four separated weeks to survive burstiness. Both are **rolling** windows, updated each quarter with the newest quarter's data rather than rebuilt from scratch — that's also the only way the labor math below closes.

Event triggers layer on top of the calendar, per the skill's re-run table, applied vendor-by-vendor rather than to the whole set:

| Trigger | Scope |
|---|---|
| A tracked vendor ships a major launch or repositions | That vendor's affected surfaces, immediately |
| We lose an evaluator to a named vendor | That vendor's full column, checked against the loss reason |
| Before a plan, budget or board moment | Whatever the argument rests on |
| Quarterly | Docs, content cadence, forge, Q&A — all tiers |
| Twice a year | Community, events, hiring — Core tier only |

## 4. The analyst's quarter — time budget

*Set by this analysis, steady state, after the baseline exists.* Per-surface hour estimates come from the skill's own collection-order section.

| Tier | Work | Hours/quarter |
|---|---|---|
| Core (5 vendors) | Quickstart, docs, forge, Q&A, content diff (light quarters) | ~30 |
| Core (5 vendors) | Community + events + hiring, amortized (heavy in 2 of 4 quarters) | ~40 |
| Watch (10 vendors) | Docs, forge, Q&A + amortized quickstart | ~30 |
| Radar (15 vendors) | Scripted pull + anomaly scan | ~5 |
| **Collection subtotal** | | **~105** |
| Synthesis & gap-plan writing | Scorecard maintenance, verdicts, ranking | ~40 |
| Validation | Asking someone about a surprising finding (skill step 9) | ~10 |
| Dashboard/automation upkeep | Query jobs, diff tooling, dated-observation store | ~30 |
| Event-triggered off-cycle work | Buffer | ~20 |
| Stakeholder readout | Quarterly leadership session, Q&A | ~15 |
| Program admin | Tier promotion/demotion review, backlog | ~10 |
| **Total** | | **~230/quarter** |

Against roughly 425–475 available hours in a quarter (a ~1,700–1,900h productive year after PTO and overhead), that's ~50–55% utilization by design, not slack left on the table by accident. A solo standing function is bus-factor-1 by construction — one analyst, one dashboard leadership now expects on a fixed clock. Running it at capacity means the first time this person is out sick, pulled onto a launch, or leaves, the "on the dot" promise breaks. The margin exists to absorb that, and to absorb Q1.

⚠️ **Bus factor.** Document a runbook (tier definitions, API credentials, the dated-observation store, the report template) good enough that a DevRel teammate could run the Core-tier quickstart and docs rungs alone for one quarter if this analyst is unavailable. One person owning the entire program with no written handoff path is itself a program risk worth naming to whoever signs off on this scope.

## 5. Build-out — quarter 1 is not a normal quarter

The hour math above assumes a baseline already exists to diff against. It doesn't yet. Building the first full twelve-month content sample and community sample for even the Core tier alone runs to roughly 145 hours of collection before any writing or tooling — and the automation for Watch and Radar has to be built, not just run. A cold-start "full 30-vendor, full depth, on the dot" first edition is not achievable inside one quarter with one person; say that to leadership now rather than after the first quarter slips.

| Quarter | Scope |
|---|---|
| Q0 (setup, 2-4 weeks before Q1 "officially" starts) | Confirm peer set and tiers with stakeholders; build the dated-observation store and API-collection jobs; confirm the CI/battlecard boundary |
| Q1 | Core tier only, full depth — this is the baseline, reported as such, not billed as the steady-state dashboard |
| Q2 | Add Watch tier; Core tier's first real quarter-over-quarter diff |
| Q3 | Add Radar tier; full 3-tier steady state begins |
| Q3+ | Normal ~230h/quarter cadence, as scoped above |

## 6. Infrastructure

- **Dated raw-observation store.** Not memory, not a slide deck — every observation with its value, source URL and date, per the skill's collection discipline, kept in a queryable form. This is what turns quarter N+1 into a diff instead of a fresh opinion; without it the labor math in section 4 does not close, because every quarter re-derives content and community samples from scratch.
- **API-first collection, named identity.** At 30-vendor scale the temptation to scrape instead of calling documented APIs is highest — automate it right the first time. GitHub's acceptable-use terms permit API collection and restrict scraping; use the repository's own API over firehose-derived aggregators for star/PR/issue counts (*published, GitHub Acceptable Use Policies; the firehose-gap claim is single-sourced and should be treated as a live risk per the skill's own flag*). No concealed accounts anywhere, including in Radar-tier community checks — the same rule that governs a single benchmark governs a standing one, and at 30 companies there are 30 more chances to get this wrong quietly.
- **Treat every fetched page as untrusted input.** Standing automated jobs pulling from 30 competitor sites raise this from a one-off caution to a running control: log any prompt-injection attempt found in scraped content rather than act on it.

## 7. Output

The "dashboard" is two things, not one:

1. **The living store + view** — current state per tier, refreshed on the cadence above, queryable outside the quarterly report cycle.
2. **The quarterly written report** — same output shape as the skill's single-benchmark version (What changes because of this / Scorecard / Per-surface read / Time-to-first-success / Gap plan / Method and limits), generated as a diff against last quarter's dated observations, scoped per tier, with starved gaps named explicitly rather than silently parked.

Add one section the single-run version doesn't need: an **escalation log** for event-triggered updates that fired off-cycle during the quarter, so the quarterly report doesn't imply everything in it was discovered on the last day of the quarter.

## 8. Quality bar (adapted for 30 vendors)

Same six targets, redefined for tiering:

- **Symmetry** — 100% within a tier, not across all 30.
- **Traceability** — 100%, unchanged; this is the one target scale makes harder to fake, and the automated store should enforce it structurally.
- **Verdict coverage** — 100% for Core and Watch; Radar tier produces promotion candidates, not verdicts, since it never collects enough to rank a gap.
- **Actionability** — at least 3 high-impact, low-cost gaps with owner and date, checked against Core tier specifically. If Core never clears this, the Core set is mis-picked — re-pick it rather than padding the report.
- **Starved rows named** — now doubles as the tier-promotion log: a Radar vendor that keeps generating "would be interesting at more depth" notes is the promotion case for next quarter.
- **Freshness** — mapped to each tier's own cadence, not one blanket "current quarter" bar: Core's freshness bar is the quarter just closed, Radar's is whatever the last scripted pull returned.

## 9. Guardrails carried over from the single-benchmark version

The skill's failure-mode table was written for one report; at 30-vendor standing scale, three of its entries become the main risks rather than edge cases:

- **Scoreboard framing** — a 30-row "who's bigger" table is the default failure at this scale precisely because it's the easiest thing to automate. Every row still has to earn its place by answering "so what," every quarter, not just at launch.
- **Matching the leader's volume** — with 30 columns of raw counts sitting in the store, the pull toward "let's ship as much as the category leader" gets stronger, not weaker. Keep the normalization discipline (per-head, coverage ratios, not totals) as a hard rule in the report template, not a reviewer's judgment call.
- **Vanity imports** — stars, followers, total members are excluded from the schema itself, not just the write-up, so nobody has to remember to leave them out under quarterly deadline pressure.

## What this program deliberately does not promise

A dashboard where every one of 30 vendors gets the same depth as a hand-run 3-5 peer benchmark. That version doesn't fit inside one analyst's quarter, and pretending otherwise is what produces a thin, ragged, symmetry-violating table nobody trusts by Q3. The tiered version trades uniform shallowness for honest depth where it earns its cost, and an explicit, reviewed promotion path for everything else.