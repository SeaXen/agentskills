**Move: sell hosting of Trellisway, not features of it. Primary model = hosted open source. Secondary = support/LTS for air-gapped minority. First action: quantify cost-to-serve per workload before writing another line of infra code.**

Full workflow run below (devtools-business-model skill). Interview wasn't done turn-by-turn since you want final answer, not dialogue — assumptions stated where inferred, flag if wrong.

---

# Business model, Trellisway

## Assumptions (interview answers inferred, confirm or correct)

- No investor pressure stated → treat as bootstrapped-ish, 14mo runway = hard clock, not soft one.
- Revenue needed as signal by month 6-9, real money by month 12-14, else runway gone.
- Want compounding business, not one logo for board slide ("turn this into actual business" = mandate for asset, not stunt).
- Off table: relicensing Apache-2.0 already shipped code. Not stated explicitly but default stance for OSS project with 9,400 installs depending on it — confirm.
- Nothing metered today beyond opt-in install telemetry. No billing-grade usage data yet.
- No existing enterprise contracts, no support org, no sales function, no salespeople ever. Confirmed by you directly.

## Constraints

- **Licence:** Apache-2.0, already shipped, permissive. Every install today runs it free forever, that's locked. No forcing function for dual licensing exists under a permissive licence.
- **Deployment:** 100% self-hosted today. Nothing stops adding hosted option — that's reversible in a quarter, not a constraint against it.
- **Buyer:** 58% of installs run inside companies. Signer = platform/infra lead or engineering manager, not individual DAG author. Majority of current install base already selects for an org buyer.

## Rejected models

- **Dual licensing** — Apache-2.0 already published, permissive. No forcing function. Deleted, not demoted.
- **Source-available** — no credible hyperscaler-absorption threat exists today, nobody runs competing managed Trellisway. Pulling this now buys nothing, costs contributors and the 9,400-install community's trust. Revisit only if a cloud vendor ships a competing managed service.
- **Ecosystem take-rate** — no two-sided marketplace, no plugin liquidity mentioned. Premature by definition.
- **Embedded/OEM** — nobody embeds a workflow scheduler inside their own product typically, and Apache-2.0 already grants an embedder everything they'd want for free. No signal of demand.
- **Proprietary hosted SaaS (as distinct archetype)** — core stays open forever, so nothing proprietary exists to host exclusively. What's actually on table is hosted-open-source, not this.
- **Consumption metering (as standalone primary, today)** — nothing billing-grade metered yet, only opt-in install counts. Not deleted forever: becomes the value metric once hosted service exists (folded into primary below, not a separate model).
- **Open core (as primary, not forever)** — paid boundary here would be governance features: SSO, RBAC, audit log, multi-tenant management. Real candidate, but rejected as primary for one reason: that boundary sells to security/platform buyers who trigger a review-and-procurement motion, and you have zero sales capacity, zero sales experience, 14 months of runway. Pricing governance features for self-serve while the buyer actually needs a reviewed sale is the exact mismatch this skill flags as a classic failure — cost of the sale eats the contract, and you can't staff the sale anyway. Revisit if hosted conversion stalls, or a named enterprise explicitly asks to buy governance without hosting.
- **Support/LTS (as primary)** — revenue scales with headcount, you have none to spare and no support org. Demoted to secondary, sold later to the regulated slice of the 58% that will never leave self-hosted.

## Primary model

**Hosted open source.** Trellisway operates a managed version of the exact same Apache-2.0 server — scheduling, retries, run history, web UI, all identical to self-hosted. What's sold: not being on-call for your own scheduler. Uptime, upgrades, backups, scaling, migration off self-hosted state.

Prerequisite: self-hosting a stateful scheduler with DB, worker fleet, retries, and upgrade risk genuinely hurts at scale. This is the same operational shape that makes hosted-open-source work for every comparable orchestrator in this space — check your own telemetry for the tell: version lag, upgrade-failure issue volume, retry/error spikes on installs running >N workers. If that signal isn't there, this whole model is weaker than assumed — run that check before anything else.

Why this over open core, given your specific team: two ex-SRE founders are the exact skill the operational burden needs, that expensive function is already half-paid-for in headcount you have. Zero sales experience rules out anything needing a human-driven enterprise motion as primary — hosted open source can start pure self-serve: signup, point at DAGs, run pipeline, no human in the loop.

## Paid boundary

- **Always free:** full server, every executor, UI, plugin API, all auth methods including SSO, every security patch. Nothing from the OSS project moves behind a paywall.
- **Paid:** hosted operation only — uptime, managed upgrades, backups, migration tooling, run-history retention beyond a self-hosted-equivalent window, on-call escalation.

Five gates:

1. **Org-only?** Yes. Uptime/ops/migration/on-call is something a platform team pays for, a solo dev self-hosting one node doesn't want it.
2. **Defensible without hostility?** Yes, strongest form — nothing is withheld from the project, so nothing to fork around. A contributor rebuilding this upstream would just be rebuilding your hosting infra for themselves, not taking a feature back.
3. **Observable trigger?** Yes — instrument via existing opt-in telemetry: version lag past N minor releases, upgrade-failure error signatures, worker-count crossing a scale threshold. Name the exact thresholds before launch, don't leave this vague.
4. **Cost-to-serve covered?** **Unknown — not yet quantified.** This is the gap. You don't run a hosted service today, so no real compute/DB/storage cost-per-workload number exists. Compute this in currency before committing engineering months, not after. This is the single highest-leverage next action.
5. **Licence-compatible?** Yes, no relicensing needed — Apache-2.0 explicitly permits operating a hosted service of the identical code.

Gate 4 is open. Model isn't proven until it closes.

## Value metric

**Concurrent / total pipeline (DAG) runs on the hosted service.**

- Already counted — teams size self-hosted clusters by this number today.
- Grows with value — more of their work running through Trellisway means more runs.
- Forecastable — visible in their own dashboards before any invoice.
- Rejected: per-seat. DAG authors are a fraction of who benefits, and seat count doesn't move as usage grows through scheduled/automated triggers — classic "seats on an automated product" failure mode.

## GTM consequence

Self-serve first, no human required for early contracts — matches your sales capacity exactly (none). First three investments, in order:

1. Migration tooling — self-hosted metadata DB to hosted, one-directional path that doesn't lose run history.
2. Metering + spend caps — bill shock in a developer audience becomes a public post, guard against this from day one, not retrofitted.
3. Third on-call hire — two ex-SRE founders staff early rotation, but name a limit (six months, not indefinite) before it eats the whole team.

Do not hire a salesperson yet. Nothing here requires one until self-serve conversion data says otherwise.

## Leading indicator

- **Primary:** self-host-to-cloud conversion rate, read monthly, among the cohort showing operational-pain telemetry (version lag, upgrade failures, scale threshold crossed). Target: instrument within this quarter, first read within 60 days of hosted GA.
- **Guardrail:** gross margin per workload, tracked alongside conversion. Illustrative floor to test against: 60% — replace with your own number once gate 4 above is closed, don't ship with a guessed floor.

## Risks

1. **Margin too thin.** Scheduler + worker compute may dominate cost per workload. Signal: gross margin per workload below floor in any month after month 3 of hosted GA.
2. **Self-hosting stays good enough.** Operational pain real but tolerated for free anyway. Signal: under 1% conversion from the pain cohort after two quarters.
3. **Runway outruns traction.** Zero paid hosted customers by month 9 of 14 leaves ~5 months to pivot or raise bridge. Signal: exactly that — zero paying hosted accounts at month 9, check the calendar now.

## Revisit triggers

- Cloud provider ships a managed Trellisway-compatible service → reopen source-available question (threat now credible, wasn't before).
- Gross margin per workload stays below floor two consecutive quarters after launch → reopen with open core or support/LTS as candidate primary (**failure condition**).
- Inbound requests for air-gapped/on-prem support exceed ~3-5/month → promote support/LTS from secondary to real capacity investment.
- Zero paying hosted customers by month 9 → emergency pivot or bridge conversation (**failure condition**, same as risk 3 above, listed twice on purpose — this is the one that kills the company).

## Threshold check

- Five paid-boundary tests answered in writing: 4 of 5 pass clean, gate 4 (cost-to-serve) open — not a "no", an unmeasured "unknown." Close before launch.
- One primary, one secondary: hosted open source primary, support/LTS secondary. Clean.
- Value metric customer already counts: yes, pipeline runs.
- Cost-to-serve quantified in currency: **not done.** First action item, see below.
- LTV:CAC / CAC payback modeled: not possible yet, zero revenue. Once first paid cohort exists, compare against Skok's SaaS-wide reference points (LTV:CAC above 3, CAC recovered in 5-7 months) — general SaaS benchmark, not devtool-specific, treat as a bar to test against, not a guarantee.
- Leading indicator named, instrumented within a quarter, target + date: yes, above.
- Three-plus revisit triggers, one failure condition: four given, two carry failure conditions.

Memo not fully closed until cost-to-serve gate clears. Everything else is ready to execute.

**Next: pull real infra numbers (DB, compute, storage per workload) and compute cost-to-serve in dollars. Without that number this whole model is unverified, not wrong.**