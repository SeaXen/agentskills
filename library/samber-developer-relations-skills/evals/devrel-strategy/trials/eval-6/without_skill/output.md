# What to build at Vasterly

## Reject "start with docs" — for this goal, not in general

Docs and quickstarts optimize first-success for a **new** user. Vasterly isn't acquisition-constrained — 4,000 companies are already installed. The binding constraint is staying installed.

Three reasons docs are the wrong first move here:

- **Wrong funnel stage.** Quickstarts move someone from zero to first success. Renewal is decided by someone who adopted Vasterly 18 months ago and now has to defend the line item in a budget review. Docs don't reach that person.
- **Not an asset — a maintenance tax.** Every release makes docs stale again. Year-3 value ≈ year-1 value, spent again each year. That's the opposite of what your chair asked for.
- **No moat.** Any competitor rewrites your quickstart in a week. Nothing compounds, nothing gets harder to copy over time.

Fund docs at maintenance level only — keep them accurate, don't make them the flagship investment. Put roughly 10% of budget there, folded into whichever of your two people touches product surface, and move on.

## Why self-hosted renewal breaks the standard playbook

Renewal in self-hosted infra isn't decided by product usage — it's decided in a budget review, by whoever inside the customer is willing to defend the line item. If nobody defends it, procurement cuts it on inertia, not dissatisfaction. The unit that actually churns is rarely "the product stopped working" — it's "the internal champion left, got reorged, or stopped caring."

Two things follow that most retention frameworks (built for hosted SaaS) don't account for:

- **You have no usage telemetry.** Self-hosted means no default phone-home signal across the base — the login-frequency/feature-drop health scores that hosted SaaS churn programs run on mostly don't exist for you. You need a substitute instrumentation layer, and it has to be something you can see: community engagement, not product usage.
- **Perceived vendor health is a renewal input, not a marketing nice-to-have.** A company that chose to self-host is explicitly underwriting 3–5 years of your continuity. Any signal that the project looks quiet reads as abandonment risk, independent of your actual uptime.

That reframes the brief: build the thing that (a) gives you visibility into account health you can't get from telemetry, and (b) manufactures internal champions who'll defend the renewal, faster than any competitor can copy it.

## The build: one integrated program, not four small ones

Two people can't run four half-built initiatives well, and half-built assets don't compound — they just cost money. Build one program with three tightly linked parts, so effort in one strengthens the others instead of splitting attention.

### 1. Closed practitioner network (the core asset)

A verified-install-only channel — not a public marketing Discord — for people who actually run Vasterly in production across the 4,000 companies.

- Verification by license/account ties every member to a real renewal-bearing account — this is what makes the channel a health-signal source, not just a nice community.
- Content is peer-to-peer: upgrade playbooks, scaling incidents, migration scripts. Vasterly staff moderate, don't dominate.
- Quarterly practitioner roundtables (video, recorded) — operators trade real production patterns with each other.
- This directly substitutes for the telemetry you don't have: engagement level per account becomes your renewal-risk proxy. An account with zero community presence 60 days before renewal is your highest-risk signal — flag it to CS, not marketing.

### 2. Champion program, fed by the network

Pull the most engaged practitioners out of the network into a small, invite-only tier — 5–10 people to start, per the standard advice on not overbuilding this early.

- Give them: early roadmap access, a direct Slack channel with engineering, conference sponsorship, public recognition. Not swag, not quotas.
- Their actual job: defend Vasterly internally at their own company's budget review. That's the renewal mechanism — you're manufacturing the internal advocate the framework above says decides renewal.
- Track who's a champion at every top-revenue account. An account approaching renewal with no identified champion is a CS escalation, not a marketing metric.

### 3. Annual practitioner gathering — the compounding, visible asset

Start small: a single-day "Ops Day," 60–80 people, attached to an existing conference rather than built as a standalone flagship — cheap in year 1, deliberately built to look bigger every year.

- This is the asset that most literally compounds: year 1 it's a small room; year 3 it's the thing a nervous procurement reviewer googles to check "is this company still real." Reputation and a video archive both accumulate — a competitor starting their own event in year 3 is three years behind, permanently.
- Feed it from the champion program (speakers) and the network (case material) — it costs less to run than a from-scratch event because the content already exists.

### The feedback loop that closes the circle

Quarterly sessions between engineering and your top-usage champions: "what's breaking your upgrade path." Publish what changed as a result. This is a direct churn-prevention lever — "the product stopped fitting our needs" is the single biggest non-price reason usage-based tools lose renewals, and it's the one lever docs can never pull.

## Team split

- **Person 1 — Network & Champions.** Owns the closed community, verification, roundtables, champion program, and per-account health flagging to CS. This person is your instrumentation layer.
- **Person 2 — Gathering & Product Loop.** Owns the annual event, the quarterly engineering feedback sessions, and case studies drawn from both. Also owns docs maintenance — light touch, not a project.

## Rough 3-year build-out

1. **Year 1** — Stand up the closed network (verified accounts only), recruit 5–10 champions, run one small Ops Day. Budget-light; the goal is real signal, not scale.
2. **Year 2** — Formalize the champion tier with real benefits, double the gathering's size, launch the quarterly engineering feedback loop, start per-account health flags feeding CS renewal conversations.
3. **Year 3** — Gathering becomes a recognized industry fixture; champion alumni start speaking externally on your behalf uninvited; network engagement is a standing input to your renewal forecast, not a side project.

## What to report to the board instead of a number

Your chair explicitly doesn't want a quarterly number — so don't hand her docs pageviews or MAU. Report the leading indicators that causally sit upstream of renewal:

- % of top-revenue accounts with an identified internal champion
- Community-active accounts as % of the base, trended
- % of at-renewal accounts flagged as champion-less 90 days out, and what CS did about it
- Gathering attendance and repeat-attendance rate, year over year

These are asset-value metrics, not output metrics — each one should be a strictly bigger number in year 3 than year 1, which is the actual test your chair is asking you to pass.