# Quillmark quarterly health report — measurement framework

## First, the 24-hour question

**No — that figure is wrong twice over.**

1. **CHAOSS publishes no numeric target for any of its four Starter Project Health metrics.** Not 24 hours, not any number. It states expectations qualitatively ("keep up with incoming change requests and resolve them in a timely manner") and explicitly expects each project to set its own thresholds. CHAOSS also refuses cross-project comparison outright — the numbers exist to track your own trend, not to grade you against another project.
2. **The number that actually circulates "as a CHAOSS standard" is two business days — and it isn't CHAOSS's either.** It appears only inside VMware's case study on the CHAOSS starter-model page, as that company's internal guideline. So even the corrected figure must be attributed to VMware, not to CHAOSS.

A 24-hour first-response target is folklore — same family as "20% monthly-active ratio" and "40% seven-day retention": round numbers in circulation that no measurement backs. If the committee insists on quoting one before you have a baseline, it goes on the sheet labelled `hypothesis`, never as "the standard". After three quarters of your own data, replace it with your trailing median.

One warning before anyone adopts 24h anyway: a speed target on an all-volunteer project buys you drive-by "any update?" replies that close the measurement gap without helping the reporter. Speed-incentivized numbers get a counter-metric (below: reopen rate), or they rot into Goodhart behavior.

## Scope and routing

- This is the **open-source, no-purchase** case: the product is the repository and its ecosystem. No revenue, no pipeline, no CRM — the business-impact tier is empty by construction and gets *deleted*, not parked.
- If Quillmark also runs a chat venue (Discord/forum) whose activity and sentiment you want measured, that is a separate exercise (`developer-community-health`), not this sheet.

Assumed answers behind this framework — correct me where wrong:

- **Driver:** contributor community / project sustainability. Nobody funds this to sell anything.
- **Reader:** steering committee, quarterly, deciding where scarce volunteer attention goes.
- **Data:** the forge only (issues, PRs, commits, releases), zero engineering days for instrumentation.
- **Lifespan:** a sheet that still reads in a year, not a one-off slide.

**Spine:** CHAOSS Starter Project Health — the catalog's named spine for "the product is a repository". Driver-anchored on project health, legible to any steering committee, and its definitions keep your numbers comparable to other projects' published ones. Journey-stage and function-split spines both fit funded teams better than a volunteer project.

---

## The framework document

### 1. Driver and goals

Funded driver: **a sustainable contributor community** — the project must stay responsive and must not depend on a handful of people.

Goals (one primary each):

1. Responsiveness — newcomers get a human answer fast enough to stay.
2. Contribution sustainability — first-timers return; no single point of failure.
3. Shipping cadence — users get releases, security fixes especially.

### 2. Metric sheet

Four rows of eight metric fields. Every threshold carries its provenance tag — `sourced` (traceable publication), `baseline` (self-set from own history), `hypothesis` (folklore under test). Owners are role placeholders; ratify names at the steering meeting.

| # | Metric | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|--------|------|------------|--------|----------|-----------|-------|--------------------|
| 1 **P** | Median time to first response | Engagement | median hours from issue/PR open to first *human* reply; bots excluded; CHAOSS definition verbatim | forge API | compute 3 prior quarters (full history exists on the forge) | trailing-median band; any 24h/48h figure quoted now = `hypothesis` (folklore — VMware's 2 business days, not CHAOSS); switch to `baseline` after 3 periods | triage rotation | audit rotation coverage gaps (weekends, timezones); recruit triagers |
| 2 | Change-request closure ratio | Engagement | closed (merged + rejected) ÷ opened, same quarter | forge API | 3 prior quarters | holding ≥ 1 (`baseline`, self-set — CHAOSS states this only qualitatively) | maintainers | stale-PR sweep with comment; cap work-in-progress per maintainer |
| 3 **P** | Repeat-contribution rate | Product impact | share of first-time contributors with a second merged PR within 6 months, by monthly cohort | forge API | 3 prior quarters | direction + range first two cycles (`baseline`); below 30 events/quarter → report the raw list with dates, not a rate | contributor-experience owner | fix good-first-issue list and CONTRIBUTING; interview five one-time contributors before changing anything |
| 4 | Contributor absence factor | Product impact | smallest number of people producing 50% of contributions | forge API | 3 prior quarters | direction only (`baseline`); alarm on a falling trend, not a level | steering chair | pair-review sole-ownership areas; recruit co-maintainers for them |
| 5 **P** | Release frequency + security-patch lag | Enablement | releases per quarter incl. point releases; days from security fix commit to release | forge tags | 3 prior quarters | self-set from own history (`baseline` — CHAOSS: "no two projects have the same needs"); security lag reviewed every quarter regardless | release manager | schedule a cut; unblock the release checklist |
| 6 | First-timer issue quality | Engagement | share of issues from first-time openers containing a repro or a docs reference | forge API + monthly manual scan | baselining | set at next review | docs maintainer | falling share → fix the issue template and docs entry points; this is the "stranger who read the docs" signal |
| 7 | Downloads / dependents delta | Reach | period delta only, never cumulative; request counts, **not people** (CI and mirrors included) | registry stats | start snapshotting now — registry history windows vary and are not backfillable | direction only (`baseline`); ships only because rows 3 and 6 carry its story | release manager | sharp move → check ecosystem breakage (new OS, new dependency versions) before interpreting |
| 8 | Qualitative evidence | Qualitative | verbatim contributor quotes + friction findings, each with source, date, confidence tag; a finding needs 5–10 independent data points | issue threads, list | 4 per quarter | fewer than 2 | steering chair | schedule two contributor conversations |

**Cut from the report: the 4,200 stars.** Cumulative stars cannot fall when the project stops working, so they carry no information; they are gameable and non-comparable across project types — "the Monopoly money of open-source metrics" (Ashley Hathaway, developerrelations.com, 2017). An issue opened by a stranger who read the docs beats a hundred stars; that is what row 6 measures.

**Counter-metric pairings (Goodheart guard):** row 1's speed incentive pairs with reopen rate / share of substantive first replies; row 2's throughput incentive pairs with reopen rate. Row 7's volume pairs with rows 3 and 6 downstream.

### 3. Attribution rule

Written before the period starts — a rule invented after the quarter is a narrative.

- **In use:** self-reported (one optional question in the issue/PR template: *"How did you find Quillmark, and what nearly stopped you?"* — stable option list, free text kept, read quarterly). Pre/post for bounded pushes (a CONTRIBUTING rewrite, an issue-template change) — pre-period recorded *before* the push, never after.
- **Claims allowed:** self-reported = direction and discovery only, reported as "self-reported", never as causation. Pre/post = direction and rough magnitude, no point estimates with decimals.
- **Lookback/stage:** none needed — no pipeline exists. The rule constrains report language: improvements are "associated with" a push whose pre-period was recorded; never "caused by" anything else.
- **Shared credit:** changes co-driven by an affiliated org or sponsor name both parties; nobody claims sole credit.
- **Rule changes** are announced as restatements; the trend breaks visibly, not silently.
- **Blind spots the rule cannot see:** lurkers, off-venue word of mouth, users of packaged distributions (Homebrew/Debian) invisible in registry counts.

### 4. Reporting

- **Monthly operational read** (internal): refresh rows 1–2 and 6; snapshot any traffic data — GitHub's traffic endpoints keep 14 days, so unsnapshotted data is gone.
- **Quarterly decision read** = the committee's health report: full sheet plus qualitative evidence, each metric against its own trailing baseline — never against another project's numbers.
- **Annual reset:** re-derive the sheet from the driver; expect half the metrics to change.
- **Five-sentence summary the committee can repeat without you:** "Newcomers get a first human reply in a median of [X] hours, against our own trailing baseline of [Y]. Of first-time contributors, [Z]% come back within six months. [N] people produce half the contributions — up/down from [N']. We shipped [R] releases, security fixes lagging by [D] days. Every threshold on this sheet is ours, derived from our own history — none is an external standard."

### 5. Known blind spots

- **Readers and users who never open an issue** — invisible. Closing costs docs analytics, but a third-party script misses most of a developer audience (Plausible measured 58% blocking Google Analytics on a tech audience, August 2021 — 82.3% on Linux); if ever added, report step-to-step ratios inside one source, never absolutes.
- **Chat/forum sentiment** — out of scope here; separate exercise if venues exist.
- **Expiring sources** — GitHub traffic: 14 days, write-access only. Registry series: months, not years. Snapshot from day one; a metric defined today may be uncomputable for last quarter.
- **Absence factor ignores knowledge specialization** (CHAOSS's own caveat) — someone can be 2% of volume and the only person who understands the parser.
- **Bot activity distorts rows 1–2** (CHAOSS's own caveat) — maintain the bot exclusion list, and keep it out of first responses.

### 6. Review

- Next review: end of next quarter. First three cycles are baselining — thresholds above hold as direction + range until then.
- **Kill rule, stated in the document:** any metric that has not changed a decision in two consecutive review cycles is removed. Removal is a scheduled event, not an argument.

---

## Pass-threshold check (run explicitly)

| Check | Result |
|---|---|
| 5–8 metrics | ✅ 8 |
| Six fields per metric (definition, source, baseline/baselining, threshold, owner, action) | ✅ all rows |
| ≥ 1 product/business-impact metric | ✅ rows 3, 4 |
| No monotonic primary | ✅ stars cut outright; downloads row is period-delta only |
| "So what" + ownership tests | ✅ every row has a named action a volunteer group can move in a quarter |
| Attribution rule written, methods + window named, shared credit worded | ✅ adapted: no "influenced" pipeline exists — shared-credit principle stated for sponsor co-work |
| Incentivized volume metrics have counter-metrics | ✅ rows 1, 2 ↔ reopen rate; row 7 ↔ rows 3, 6 |
| Thresholds tagged `sourced` / `baseline` / `hypothesis`; no `hypothesis` presented as target | ✅ the 24h figure appears only as tagged folklore |
| Blind spots non-empty | ✅ six named gaps |

**What needs ratifying at the steering meeting:** the three goals, the owner names behind the role placeholders, and the two template questions. Those are the only decisions embedded in this sheet; everything else is derivable from the forge on day one.