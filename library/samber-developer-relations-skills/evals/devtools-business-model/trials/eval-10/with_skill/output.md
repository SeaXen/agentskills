# Business model — Runnelgraph

ℹ️ Two inputs need a swap before this ships to the team — flagged inline, not silently changed. Numbers marked ⚠️ are placeholders only the team has real data for; everything else is a decision, not a fill-in-the-blank.

**Decision already made, carried as given:** Runnelgraph stays 100% Apache-2.0, nothing closes. The company sells the managed service around it. That fixes the primary model to **hosted open source** — this memo works out its consequences, not whether it's the right call.

---

## Constraints

- **Licence.** Apache-2.0 across the codebase, already published, staying published. Permissive — no copyleft obligation exists to sell an exemption from, and no relicensing is on the table. This is the one constraint everything else in this memo has to survive contact with.
- **Deployment.** Runnelgraph runs today as software the customer operates themselves. Hosting only monetizes if self-hosting genuinely hurts — ⚠️ confirm with real evidence (upgrade-failure rate, on-call pages, version-lag among self-hosted deployments) before circulating this memo further. If self-hosting is easy, hosted open source has no prerequisite and the model is a wish.
- **Buyer.** The organization running Runnelgraph in production — a platform lead or engineering manager, not the individual who authored the graph. Sell risk removal (uptime, upgrades, backups, someone to page), not features.

## Rejected models

| Model | Blocking reason |
|---|---|
| Open core | Contradicts the decision already made — "fully Apache-2.0" means no proprietary layer to build. |
| Proprietary hosted SaaS | Collapses into hosted open source once nothing stays closed — there's no closed product left to sell as SaaS. |
| Dual licensing | Impossible under a permissive licence with no copyleft to exempt anyone from. |
| Source-available | No hyperscaler-absorption threat exists yet (see Revisit triggers). Pulling this lever now buys nothing and costs contributors and naming discipline for free. |
| Support/LTS as primary | Revenue scales with headcount, and there's no enterprise footprint yet to justify a support org before the hosted product proves out. Kept as the pre-named **secondary** — see Revisit triggers — not activated now. |
| Consumption metering | No metered value has been validated against real usage yet; nothing to bill without the hosted product existing first. |
| Ecosystem take-rate | No third-party plugin or listing liquidity exists. Almost never a first model anyway. |
| Embedded/OEM licensing | Apache-2.0 already gives an embedder everything they'd want to license. |

## Primary model

**Hosted open source.** Sold: running Runnelgraph for the customer — upgrades, backups, scaling, availability, and not being the one paged when it breaks at 3am. Every feature, every executor, the full server stays Apache-2.0 forever; the company sells operation, not code.

Prerequisite this depends on: operating Runnelgraph is hard enough that a platform team would rather pay than run it themselves. ⚠️ This is a claim, not yet evidence — validate it before committing further budget (see Validation experiment below).

## Paid boundary

- **Always free:** the full server, every executor and feature, the UI, the API, every authentication method including SSO, every security patch. Nothing withheld from the project.
- **Paid:** the hosted service itself, plus retention beyond the default window on that hosted service only.

Why the line holds: it isn't a feature line at all. Nothing is withheld from the open codebase, so there's nothing for a motivated contributor to fork around — the boundary is operational, not competitive with the community.

Paid-boundary test, in writing:

1. **Organization-only** — yes. A solo developer running Runnelgraph locally has no reason to pay for uptime SLAs or managed backups.
2. **Defensible without hostility** — yes. A contributor could self-host in a weekend; nobody is blocked from anything, so there's nothing to fork.
3. **Observable trigger** — yes. Upgrade failure, an on-call page, or opt-in telemetry showing version lag on a self-hosted deployment.
4. **Cost-to-serve covered** — ⚠️ pending. No free tier exists yet on the hosted side to cost; if a free hosted tier is ever added, its marginal cost per user must be computed in currency before launch, not assumed.
5. **Licence-compatible** — yes. Nothing about this model requires touching the licence.

## Value metric

Candidate: **concurrent graph executions** (or the closest equivalent — active graph runs). ⚠️ Confirm this is a number self-hosted teams already size their own infrastructure by before committing to it as the billed unit.

- Already counted: pending confirmation with actual self-hosted users.
- Grows with value: yes — it rises as more of the customer's workload runs through Runnelgraph.
- Forecastable: yes, if visible in their own dashboards before the invoice.
- Rejected: **seats.** Graph authors are a small fraction of who benefits, and headcount doesn't track usage as execution volume grows through automation.

## GTM consequence

Self-serve first: point an existing Runnelgraph config at the hosted service, migrate state, run in production same day. No sales hire before the first cohort of paying teams (⚠️ team to set the number — the reference example used twenty).

Build order:

1. Metering and spend visibility on the value metric, with caps and alerts from day one — unmetered consumption in a developer audience becomes a public complaint, not a renewal.
2. Migration tooling: self-hosted state and run history into the hosted service.
3. An on-call rotation sized to what the current team can staff without burning out — name the cap now (e.g., current headcount for six months, then hire), not after the pager goes off nightly.

## Leading indicator

**Primary:** self-host-to-cloud conversion rate, read monthly, among the cohort of self-hosted deployments that hit an operational pain signal in the last 90 days (upgrade failure, on-call page, or telemetry-flagged version lag). Target: ⚠️ team to set, with a date.

**Guardrail, tracked alongside it:** gross margin per workload, floor ⚠️ team to set (the worked reference in this skill's library used 60% for a comparable stateful server).

**Monthly dashboard, not the leading indicator — keep watching, don't mistake either for the signal:**

- MRR — this is the outcome the model produces. It confirms the model worked; it never warns you it's about to fail.
- GitHub stars — measures attention, not the operational pain the paid boundary is priced against. No model here converts stars directly.

Track both monthly for the board and for adoption reach. Read the self-host-to-cloud conversion rate for whether the model is actually working, because it moves before either of the above does.

## Risks

1. **Competition.** A cloud provider or well-resourced platform vendor ships a managed Runnelgraph-compatible service, undercutting on distribution and cost of capital. *Signal:* a public announcement of a competing managed offering, or a fork with visible commercial hosting intent. *Read:* monthly competitive scan, plus ad hoc on signal.
2. **Execution.** Running the hosted service pulls capacity from the open-source project itself — releases slow, community trust erodes, and the free side that hosting depends on decays. *Signal:* median time-to-first-response on GitHub issues doubling from the pre-hosting baseline, or the on-call rotation exceeding the staffing cap set in GTM consequence. *Read:* monthly, alongside gross margin.
3. **Market timing.** Self-hosting is annoying but not yet painful enough for a platform team to pay to remove it — the boundary never gets crossed. *Signal:* self-host-to-cloud conversion in the pain cohort stays under target two quarters after launch — this is the failure read on the leading indicator above, not a separate metric. *Read:* monthly.

## Revisit triggers

- A cloud provider or major platform vendor announces a managed Runnelgraph-compatible service — reopen the source-available/licensing question immediately. It's the one irreversible lever on this page, worth pulling only once this threat is real, not before.
- Gross margin per workload stays below the floor for two consecutive quarters — **failure condition.** Reopen with support/LTS as the candidate primary instead of hosted open source.
- Self-host-to-cloud conversion in the pain cohort stays under target after two quarters post-launch — reopen the paid boundary and value metric; operational convenience alone may not be a strong enough line.
- Inbound requests for on-premises or air-gapped support exceed ⚠️ team to set a number per month — support/LTS becomes viable as the secondary to actually add, not just the one named and parked here.

## Threshold check

- Five paid-boundary tests answered in writing, none "no": **4 of 5 pass; cost-to-serve is pending** real currency data — not a blocker to publishing this memo, but a blocker to launching a free hosted tier without it.
- One primary (hosted open source), one pre-named but inactive secondary (support/LTS): **pass.**
- Value metric the customer already counts: **pending team confirmation** against actual self-hosted usage patterns.
- Cost-to-serve quantified in currency: **pending**, flagged above.
- LTV-to-CAC and CAC-payback modeled against Skok's SaaS-wide reference points (>3 and 5–7 months): **not yet modeled** — do this before the first sales hire, using the self-serve motion assumed above; self-serve with no sales cost makes this the least risky item on the list, but write the numbers down rather than assume they clear.
- Leading indicator named, instrumented, with a target and date: **structure set, target/date pending team input.**
- Three revisit triggers with one failure condition: **pass** — four listed, one marked failure.

This memo is executable as written, with the ⚠️ items filled from real telemetry and financials before it goes to the board. Nothing above requires me in the room to resolve — they're data-entry, not decisions.