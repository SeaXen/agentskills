Using the developer-journey-map skill (read in full above, plus all four references) to build this. Three of your requests collide with the skill's own evidence rules, so I'm flagging each inline rather than silently complying — see the callouts in Scope, the Try row, and Gaps.

I don't have live access to Orrery's GitHub/PyPI/npm data, so every Signal cell that needs a real pull is marked `[PULL]` with the exact command to run — I'm not inventing plausible-looking numbers, per the skill's own rule against a "confident fake number."

---

# Developer journey map — data engineers, 2026-09-19

## Scope

**Segment:** data engineers (single segment — this map does not cover platform teams or analytics engineers; a hybrid OSS+cloud product tends to attract both, and mapping both together would blend two different friction sets).

**End state:** production usage of Orrery Cloud (the paid product) — not production usage of the open-source library alone. This distinction matters: a data engineer can run the OSS checker in production for years and never touch the cloud tier. That path is a real, likely common outcome for an OSS+cloud business and is explicitly **out of scope** for this map's terminal stage, but it is the single biggest commercial risk in this model and belongs in your next planning cycle, not buried inside this map.

**Stage model — API and platform five-stage arc** (Awareness → Onboarding → Integration → Production → Advocacy; `gtm-developer-ecosystem`), chosen by deletion: the funded end state is "production usage," which is this model's terminal stage verbatim. Revell six-stage (terminal: standardization), AAARRRP (terminal: revenue/product), Orbit (terminal: advocate) and the OSS contributor funnel (terminal: return) all have a different terminal state and were dropped, not ranked. Revert to the OSS contributor funnel later if a maintainers' team ever asks "why do OSS users never contribute" — that's a different funded question with a different tail.

I split **Awareness** into two rows, **Discover** and **Evaluate**, per the skill's split rule ("split a stage only when it has two distinct exit events with different owners"): landing on the repo (marketing-owned) and deciding it's mature enough to try (docs/product-marketing-owned) are different jobs with different owners for a library that competes on trust (data quality tooling lives or dies on "do I believe this won't silently pass bad data"). This is a split within one published model, not a blend of two models — the skill explicitly forbids blending.

**Pushback #1 — the 4.1M all-time download counter is not going in this map as a signal.** The skill's signal-hygiene rule rejects monotonic counters outright: "total stars, cumulative signups and all-time downloads only go up and cannot fall when the journey breaks." 4.1M lifetime downloads can't tell you whether this month is better or worse than last month, and it spans years of PyPI + npm + registry mirrors at once, so it isn't attributable to one owner or one period either. It's a real, legitimate marketing milestone — use it in a blog post, a README badge, a release note — but it does not answer any question this map exists to answer. I've kept it here in Scope as context and replaced it in the Try row below with the metric that actually moves: monthly install rate, by ecosystem.

**Assumption to confirm:** self-serve cloud signup, no procurement gate, so the buyer lane collapses (see below). Flag me if Orrery Cloud has an enterprise tier with a sales motion — that reopens a real buyer lane.

## Journey

| Stage | Developer's job | Entry trigger | **Exit event** | Touchpoints | **Owner** | Friction evidence | **Signal** |
|---|---|---|---|---|---|---|---|
| Discover | "find something better than ad-hoc asserts for catching bad data before it breaks a pipeline" | search, peer mention, conference/blog mention, aggregator link | lands on the Orrery docs site or GitHub repo | search results, GitHub README, docs homepage, comparison ("Orrery vs Great Expectations") posts, community threads | marketing / DevRel | no evidence yet | GitHub unique visitors, trailing 14 days: `[PULL: gh api repos/<org>/orrery/traffic/views]`. **Inferred beyond that window — see Gaps.** |
| Evaluate | "decide Orrery is mature enough to trust with our pipeline before writing a line of code" | reads docs, README, comparison content, license | clones the GitHub repo | docs (features/license/maturity pages), README, PyPI project page, npm project page, comparison threads | docs owner / product marketing | no evidence yet | GitHub clones, trailing 14 days: `[PULL: gh api repos/<org>/orrery/traffic/clones]`. **Inferred beyond that window.** |
| Try | "prove Orrery catches bad data in our data, in under an hour, without a rewrite" | `pip install orrery` / `npm install <js-companion>`, opens quickstart | first successful local data-quality check run | quickstart docs, CLI output, error messages | developer experience / docs | no evidence yet | See "Ecosystem split" below — **not** all-time downloads (Pushback #1). |
| Integration | "wire Orrery into our pipeline and point it at the cloud for history/alerting" | first local success reached, creates a cloud account / API key | first check run reports to Orrery Cloud from a non-local environment (CI, staging, scheduled job) | cloud signup, API key page, SDK docs, orchestrator (Airflow/dbt/Dagster) integration docs, support | product (cloud team) | no evidence yet | `not instrumented` |
| Production | "trust Orrery Cloud enough to gate a real deploy on it and get paged when it fails" | staging/CI traffic to cloud observed | 14 days of sustained production traffic to Orrery Cloud + an alerting rule configured | cloud dashboard, alerting integration, plan/billing page, runbooks | product (cloud team) | no evidence yet | `not instrumented` — **this is the funded end state and it currently has zero visibility; see Leak.** |
| Advocacy | "tell other data engineers Orrery saved us from a bad-pipeline incident" | sustained production use for several months | public talk, post, unprompted recommendation, or merged community contribution | community, conference CFPs, changelog, GitHub Discussions | DevRel / community | no evidence yet | `not instrumented`; below the 30-event floor once any exist — publish as a dated raw list, not a rate |

### Ecosystem split (Try stage — companion table, not a second Signal)

The skill caps every stage at one signal, and the skill's own registry footnotes say npm and PyPI counts are not comparable: **npm counts HTTP 200 tarball responses, including CI runners and mirrors — a request count, not an install or person count. PyPI's `pypistats` excludes known mirrors.** Reading "npm grew faster than PyPI" off raw magnitudes compares two differently-biased counters, not two ecosystems. What the data *can* support: each series' own month-over-month growth rate, read against itself.

| Ecosystem | Metric | Retention | Pull |
|---|---|---|---|
| PyPI (`orrery`) | monthly downloads, `pypistats` | 180 days | `[PULL: https://pypistats.org/api/packages/orrery/overall]` |
| npm (JS companion) | weekly downloads, npm registry API | 18 months | `[PULL: https://api.npmjs.org/downloads/range/last-year/<package-name>]` |

Report these as two adjacent sparklines with the bias caveat printed under the chart, not as a head-to-head race. If you genuinely need a cross-ecosystem comparison, the only defensible version is *"share of new installs coming from each ecosystem, trended over time"* — still biased by the same footnote, but at least internally consistent.

## Buyer lane

None — self-serve. The data engineer decides, installs, and (per the stated end state) drives cloud adoption without a separate economic buyer in view today. Stated explicitly per the skill's rule, not left blank by omission. If a sales-assisted enterprise tier exists or is planned, add a two-row lane (technical approval, commercial approval) joining at the Production stage, with **boundary contact** — someone opening an SSO/RBAC page, hitting a seat limit, requesting a security questionnaire — as its entry trigger; that's the cheapest, cleanest signal to instrument first if this lane becomes real.

## Moments

- **First success** — first successful local data-quality check run (end of Try). Time-to-first-success is not instrumented yet; instrument this before the next re-read, it's usually the cheapest high-value number on the whole map.
- **Moment of truth** — the first check run gated inside CI/deploy against Orrery Cloud (Integration → Production transition). This is where a data engineer stops evaluating a library and starts depending on a vendor.
- **Abandonment point** — **unknown.** No friction log and no exit interviews exist yet (Step 2 of the skill wasn't run against qualitative evidence, only registry counters). Do not guess here; a wrong assumed abandonment point is worse than an honest blank, because it directs the fix budget at the wrong stage.

## Leak

**Nominated: Integration → Production.** Not because a measured rate proves it leaks — nothing downstream of Try has a signal yet, so no rate can be computed there. It's nominated under the skill's explicit override: *"promote a stage when the end state from the interview is that late stage."* Your stated end state is cloud production usage, and it is the one stage the map currently cannot see at all. That is a bigger problem than any conversion number the earlier, better-instrumented stages could produce, because a fully optimized top-of-funnel funneling data engineers into a black hole is a worse outcome than a merely mediocre one that's visible.

Why it leaks (B=MAP) is **not diagnosable yet** — no friction log, no interview, no ticket data exists for this stage. A plausible, unverified hypothesis: **ability** — connecting a local OSS check to a hosted product plus CI wiring is a multi-step technical migration, not a five-minute `pip install`, and ability is usually the right default for a developer audience. Treat this as a hypothesis to test with a friction log, not a conclusion to act on.

## Handoff

- **Owner of the fix:** product (cloud team) — instrument the Integration→Production boundary (cloud signup event → first non-local check-run event → 14-day sustained-traffic + alerting-configured event) before anything else on this map.
- **Signal to watch:** share of Integration-stage accounts that reach 14-day sustained Production traffic. Not instrumented today; this is the number the next re-read should open with.
- **Re-read date:** 2026-12-18 (90 days), or sooner if you ship a pricing change, a docs rewrite, or a new SDK.

## Gaps

- **Discover/Evaluate 12-month view: not obtainable retroactively.** GitHub's Traffic API retains 14 days only (per the skill's own sourced limit) — there is no way to backfill a trailing 12 months today. Start a daily cron that snapshots `traffic/views` and `traffic/clones` into your own store now; in three months you'll have a real quarter, in twelve a real year. Until then, the "12-month" ask can only be answered from the day forward.
- **npm vs. PyPI "which ecosystem is winning": not a comparable question as posed.** See the Ecosystem split callout above — the two counters have different, uncorrectable biases (mirrors/CI included vs. excluded). Reframe as each series' own trend, or drop the cross-ecosystem framing.
- **All-time downloads (4.1M): excluded as a map signal by design**, not by oversight — it's a monotonic counter (see Pushback #1 in Scope). Keep it in marketing copy; it will never appear as a row Signal in this map or any re-read of it.
- **Integration, Production, Advocacy: zero instrumentation.** Needs a cloud-signup event, a first-non-local-check-run event, and a sustained-traffic+alerting event from the product team before the next re-read.
- **No friction log, no exit interviews, no support-ticket mining performed.** Every Friction evidence cell reads "no evidence yet" honestly rather than guessed. Run one friction log (newest team member, per the protocol) and recruit three developers who installed but never reached Production — that's the fastest way to actually locate the abandonment point instead of assuming it.
- **Signal coverage: below the 60% gate** (2 of 6 stages carry even a partial real value, and both are pending the `[PULL]` commands above). Shipped anyway per the skill's own rule — an honest map with holes beats a complete one with invented numbers — but don't let this version stand past the 90-day re-read without closing at least the Integration/Production gap.