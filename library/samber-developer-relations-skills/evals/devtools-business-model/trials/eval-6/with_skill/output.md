## Sanity check: Pipesmith's revenue plan

**Bottom line:** none of the three lines you listed is a business model — GitHub Sponsors and the $6/mo badge are the same thing (sponsorship) counted twice, and consulting-when-it-comes is a bridge, not a destination. As written, this plan has no line item that a company has a *reason* to sign, which means it has no revenue plan yet, just a sustainability plan for the project. Below is the actual gap analysis and what I'd put in its place.

### Why each line falls short

- **GitHub Sponsors ($5/$25/$100).** Donations fund maintainers, not two salaries. There's no reason a company signs this — it's goodwill from individuals, and individuals "pay small amounts for convenience... and churn fast." Keep it, but don't put it in the company's revenue plan or headcount math. If you want to optimize this channel specifically, that's a different skill (`oss-sponsors-fundraising`), not a P&L line.
- **$6/mo "Pipesmith Pro" badge.** This *is* GitHub Sponsors again, just with its own checkout. It gates nothing — no feature, no capability, nothing an individual needs that they don't already have — so it fails the first paid-boundary test outright (organization-only: a solo dev has no reason to pay beyond ego, and a company has zero reason to). Running it alongside the Sponsors tiers most likely splits the same small pool of goodwill dollars rather than growing it, and invites "what do I actually get for $6 vs. the $5 tier" support tickets that cost you time for nothing strategic. I'd fold it into the Sponsors tiers or drop it.
- **Consulting, opportunistically.** Legitimate as a bridge — it buys cash and customer intimacy early, and it's the fastest way to learn who's actually running Pipesmith in production and what they'd pay for. Dangerous as the plan, because "when they come in" means zero GTM investment: no packaging, no rate card, no inbound funnel, and it caps growth at two people's calendar. Unscoped one-off engagements also blur into a services trap — billable hours, not a repeatable line.

None of these three violates the real landmines (you're not paywalling security patches, SSO, or community contributions, and you're not gating data export) — you're just not selling anything yet.

### Constraints

- **Licence:** MIT, already shipped, fully permissive. Dual licensing is dead (no forcing function — permissive code can't retroactively demand a commercial licence from anyone who already has it). No relicensing lever exists here worth discussing; nothing suggests a hyperscaler-absorption threat that would justify one anyway.
- **Deployment:** Pipesmith is a library — it runs entirely on the customer's side today. No infrastructure cost to you now, but also no hosted product to sell without building one.
- **Buyer:** unknown. 400k monthly downloads tells you adoption, not who's inside it — and downloads overcount real usage (CI reinstalls, transient environments). You don't yet know what fraction of that number is a company running this in a production data pipeline versus a side project.

Wardley mapping skipped — Pipesmith is a single component, not a multi-layer stack.

### Archetype scan

| Archetype | Status | Why |
|---|---|---|
| Support / LTS | **possible, promote** | Matches a 2-person effort ceiling exactly — no SRE, no billing engineering, no hosted infra needed. Classic first paid product for "high adoption, MIT library, zero revenue." |
| Open core | possible, mid-term | No paid boundary exists yet (no enterprise features built). Premature until you know what orgs actually need beyond the core lib. |
| Hosted SaaS / hosted open source | blocked today | There's nothing to host — Pipesmith isn't a server. Becomes viable only if you build a companion product (e.g., managed pipeline execution/scheduling), which is a quarter+ of engineering you don't have yet. |
| Dual licensing | blocked | MIT already shipped; no forcing function. |
| Source-available | blocked | No credible hyperscaler threat exists; would cost contributors and buy nothing. |
| Consumption metering | blocked | Nothing metered; no backend exists to bill against. |
| Ecosystem take-rate | blocked | No two-sided liquidity at this stage. |
| Embedded / OEM | worth one question | Only viable if Pipesmith is hard-to-rebuild plumbing another vendor would rather license than reimplement — you'd know if this has come up. |

### Recommended primary: Support & LTS, sold, not waited for

**What's sold:** SLA on issue response, backport commitment on pinned versions, roadmap input, direct access (office hours / private channel), migration help on major version bumps.

**Paid boundary:** everything in the library stays MIT forever — nothing withheld, nothing to fork around. Paid = time-bound guarantees, not features. This clears all five paid-boundary tests: org-only (a solo dev doesn't need an SLA), non-hostile (nobody forks a response-time guarantee), observable trigger (production deployment, an issue filed from a company domain), licence-compatible (no relicensing), and cost-to-serve is your own time, which you can price directly rather than guess at.

**GTM consequence:** founder-led outbound, not "wait for inbound." Find who's actually running this in production — opt-in telemetry, GitHub's dependency graph, issue-tracker company domains — and approach them directly with a real support offer instead of hoping a consulting lead shows up. No new hire required to start; this is sized to two people.

**Value metric:** not yet defined precisely — pin it to something the buyer already tracks (environments covered, or pipelines/seats under the contract), not billable hours.

**Leading indicator:** number of qualifying conversations with companies confirmed running Pipesmith in production (not downloads, not stars), and their conversion rate to signed contracts.

**Secondary, once validated:** whatever support conversations reveal companies actually want beyond an SLA (managed execution, governance/lineage, specific connectors) becomes the open-core or hosted-product candidate — sell the version people are already asking to pay for, not the one you'd enjoy building.

### Risks

1. **Adoption isn't production usage.** Much of 400k/month may be transient (CI, evaluation). Signal: low share of outbound conversations confirming business-critical use.
2. **Support eats the founders whole.** Two people selling, supporting, and building at once stalls the product. Signal: >50% of a week going to paying-account tickets within the first quarter.
3. **No real boundary forms — it degrades into custom billable work.** Signal: contracts require bespoke code changes instead of the standard SLA+backport package.

### Revisit triggers

- A company asks to pay for something past standard support (hosting, a specific integration) → reopens open core / hosted SaaS.
- Support signings plateau below what funds two salaries after two quarters → reconsider whether support alone can carry the company.
- Telemetry shows most usage isn't production → revisit whether the addressable paying market exists at this size at all.

### Threshold check

- Paid-boundary tests: pass for Support/LTS as scoped above; not yet run for open core (no boundary defined) or hosted (no product exists).
- One primary (Support/LTS), no second primary competing with it — Sponsors and consulting demoted to non-revenue/bridge status, which is correct, not a hedge.
- Value metric: directionally right (something the buyer already tracks), not yet pinned to a specific unit — needs your input.
- Cost-to-serve: unquantified — you need to price your own time on backports and response SLAs before signing the first contract.
- Deal size vs. motion: too early to model LTV:CAC meaningfully; revisit once you have 2-3 signed contracts.
- Revisit triggers: three written, one is a failure condition (support plateauing).

Open items I don't have enough from you to fill in: your runway/timeline for needing real revenue, whether you have any telemetry or other way to see who's running Pipesmith in production today, and whether anyone has ever asked to license Pipesmith for embedding (OEM signal). Those three answers would sharpen the leading-indicator targets and confirm or kill the OEM row.