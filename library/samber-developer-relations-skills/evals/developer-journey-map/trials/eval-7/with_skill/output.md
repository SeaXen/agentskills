Two edits to the CX template were necessary before I could fill it in — both required by the skill, not optional style choices. I'll explain them inside the deliverable itself (Scope section), then give you the complete map.

---

# Developer journey map — platform engineers, 2026-09-19

## Scope

**Segment:** platform engineers. **End state:** production usage.

**Stage model — API and platform five-stage arc** (Awareness → Onboarding → Integration → Production → Advocacy), *beingsmit/technical-product-gtm*, carried via the `gtm-developer-ecosystem` skill.

Deletion pass against the stated end state, production usage: Revell's six-stage model terminates at standardization, AAARRRP at revenue, Orbit levels at advocate/community, the OSS contributor funnel at return/contribution — none of those tails is "workloads running in production," so all four come off the menu. The API/platform five-stage arc is the only published model whose terminal stage is production usage, and it's also the cheapest to stand up (an hour to a week — its boundaries usually already sit in product telemetry: install events, exporter usage, uptime), so no further ranking was needed.

**Why your five drafted stage names don't appear below.** Your CX template's names — "aware of need," "understands the value proposition," "feels confident," "commits," "champions" — describe a state of mind, not something a developer does that can be observed, counted, or timestamped. This skill's own reference material uses "developer understands the value proposition" as *the* textbook example of an unusable exit event: nobody can be accountable for a feeling. I kept your count and order and replaced each label with the matching observable stage:

| Your draft (state of mind) | Replaced with (observable stage) |
|---|---|
| developer becomes aware of need | Awareness |
| developer understands the value proposition | Onboarding |
| developer feels confident in the product | Integration |
| developer commits | Production |
| developer champions | Advocacy |

**Two columns from the CX template are dropped, not just left blank:** emotion score (out of 10) and opportunities. Emotion scores get invented at developer volumes — nobody is surveying platform engineers stage-by-stage, so a number here would be fiction wearing a metric's clothes, and it would crowd out the owner/signal columns that make the map actionable. An opportunities column turns this into a backlog before any evidence says which stage actually leaks; the Leak section below carries the one prioritized action instead, once there's evidence to support it. In their place: an **exit event** (what proves the developer moved on), an **owner** (who's accountable), and a **signal** (what number tracks it) — these are what make a developer journey map different from a poster.

**Two things are unconfirmed and assumed for now, flagged for you to correct:**
- *Commercial model.* Whether Gravelock is pure self-serve/OSS or has a paid enterprise tier changes whether Production needs a formal buyer lane. Defaulted below to "no formal lane" — see Buyer lane.
- *No evidence has been gathered yet.* No friction log, no interviews, no analytics pull — this skill's step 2 — has run against Gravelock specifically. Every friction/signal cell below is scaffolded (what to look for, who owns it), not measured. This is a first-draft skeleton to fill with real evidence, not a completed diagnosis. Treat the Leak section as a hypothesis to test, not a finding.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Awareness | "find a way to see what's happening inside our self-hosted infra without shipping telemetry to a third party" | hits a monitoring blind spot — an incident, a migration, a cost review of a hosted APM vendor | lands on Gravelock's docs or repo via search, a comparison post, or a peer/community mention | docs landing page, GitHub repo/README, comparison posts (Gravelock vs. hand-rolled Prometheus/Grafana, vs. hosted APM), platform-eng communities (r/devops, r/kubernetes, CNCF Slack, HN) | marketing or DevRel | no evidence yet | self-reported first touches/month, by source — not instrumented |
| Onboarding | "prove the agent actually collects real data from one of our hosts before I invest more time" | opens the install/quickstart docs | agent installed on one non-production host or cluster, first metric/log/trace visible in a dashboard | quickstart docs, install script / Helm chart / binary release, default config, bundled or connected dashboard | developer experience / docs owner | no evidence yet | median time from install to first visible data point; share of installers who reach it — not instrumented |
| Integration | "wire it into what we already run — our Prometheus/Grafana/OTel stack, our alerting, our RBAC — without breaking staging" | first local/staging data point reached | agent exporting into the team's existing stack (Prometheus scrape target, OTel exporter, or Grafana dashboard) on a shared or staging environment, with one alert rule configured | config reference, exporter/integration docs, dashboard templates, alerting docs, community/support channel | product/engineering (agent + exporters team) | no evidence yet — general reference only, not Gravelock-specific: Larios Vargas et al. (ESEC/FSE 2020, DOI 10.1145/3368089.3409711) found maturity/stability (62%) and active maintenance (44%) rank among the top developer library-selection criteria; worth testing whether that holds for Gravelock's integration decision specifically | share of first-success installs reaching a configured shared-environment integration within 30 days — not instrumented |
| Production | "trust this enough to put it on call for a real workload" | staging integration confirmed working | sustained agent uptime and data flow from a production host/cluster for 14 days, with an alert routed to an on-call rotation | runbooks, agent health/status endpoint, alerting integration (PagerDuty/Opsgenie), upgrade docs, support channel | product (agent reliability), jointly with the platform engineer's own team | no evidence yet | share of integrated environments reaching 14-day sustained production traffic — not instrumented |
| Advocacy | "tell other teams or the outside world this was worth deploying" | one full quarter in production | unprompted public or cross-team mention — a talk, a blog post, an internal wiki write-up another team reads, or a referral that becomes a new Awareness-stage lead | community forum/Discussions, conference CFPs, blog/changelog, internal eng wiki | DevRel/community | no evidence yet | unprompted mentions by named practitioners/quarter — not instrumented (expect below the ~30-event floor; publish as a dated raw list, not a rate, once tracked) |

All five stages are labelled `inferred`/`not instrumented` — no Gravelock-specific evidence exists yet.

## Buyer lane

None confirmed — self-serve/OSS assumed, pending your correction. Even without a formal purchase, a self-hosted agent that touches production infrastructure and collects telemetry commonly triggers an internal security or dependency-policy review before a platform team goes to Production; per this skill's guidance for open source with no purchase, that's modeled as friction inside Integration/Production above, not as a separate lane.

If Gravelock has a paid enterprise tier, promote this to a real two-stage lane instead: **Technical approval** (security questionnaire cleared, owned by security/solutions engineering) and **Commercial approval** (contract signed, owned by sales), entering at boundary contact — someone opens an RBAC or audit-log page, asks about data egress, or requests a security questionnaire. Roll individual signups up to an account (by email domain or workspace) before reading anything in this lane; that rollup hasn't been confirmed to exist yet either.

## Moments

- **First success** — first metric/log/trace visible in a dashboard from a real host (end of Onboarding). Time-to-value not yet measured.
- **Moment of truth** — the decision to point the agent at a production host with an alert wired to on-call. This is your "commits" stage — the point where the team stops evaluating and starts depending on it, not merely "feeling confident."
- **Abandonment point** — not yet evidenced. Structural hypothesis only: for self-hosted infra agents, install is usually the easy part (one binary, one Helm chart); making it play nice with an already-heterogeneous stack — existing exporters, RBAC, existing alert rules — is typically where time and patience run out. Needs a friction log and abandonment interviews to confirm or relocate.

## Leak

**Hypothesis, not a diagnosis — no stage has a measured rate yet.** Structural candidate: **Integration**. It's the earliest stage where a platform engineer runs into someone else's decisions (existing scrape config, existing RBAC, existing alert rules) rather than their own, which is an ability problem (B=MAP), not a motivation one — the classic failure mode here would be reaching for a "why Gravelock" content push when the actual blocker is an undeclared prerequisite in the integration docs. This cannot be confirmed until step 2 evidence exists; do not act on it as-is.

## Handoff

- Owner of the fix (once confirmed): product/engineering, who owns the config reference, exporter docs and integration surface.
- Signal to watch: share of first-success installs reaching a configured, shared-environment integration within 30 days.
- Re-read date: 2026-12-18 (90 days), and immediately after any onboarding rewrite, new exporter release, or pricing change.

## Gaps

Every stage is inferred — no friction log, no completed-journey or abandonment interviews, and no analytics pull has been run against Gravelock. What would close each gap:
- **Awareness** — a self-reported "how did you hear about us" field at signup/download.
- **Onboarding** — install-time telemetry (opt-in) marking first successful data point.
- **Integration** — an event when an exporter/dashboard config is saved in a non-local environment.
- **Production** — uptime/heartbeat tracking per deployed agent, joined to a 14-day sustained-traffic window.
- **Advocacy** — a lightweight log of talks, posts and internal mentions DevRel becomes aware of.

Also unresolved: whether a paid tier exists (changes the Buyer lane), and whether Onboarding/Integration/Production have any owner distinct from "the product team" today — if not, that's itself a finding worth surfacing before the next re-read.

## Quality gate check

- One exit event per stage, phrased as an observable event: **pass**.
- One owner per stage, at least one outside DevRel: **pass** (developer experience, product/engineering, product).
- ≥60% of stages carry a real current signal value: **fail** — 0%, nothing instrumented yet. Shipped anyway with gaps named, per this skill's own rule that an honest map with holes beats a complete map with invented numbers.
- Every friction claim cites its source, no evidence mixed with hypothesis: **pass** (all cells say "no evidence yet"; the one general citation is explicitly marked as not Gravelock-specific).
- Exactly one leak nominated, with owner and re-read date: **pass with caveat** — nominated as a hypothesis, not a data-backed diagnosis; treat accordingly.
- Inferred stages labelled everywhere: **pass**.
- Fits on one page: **pass**.