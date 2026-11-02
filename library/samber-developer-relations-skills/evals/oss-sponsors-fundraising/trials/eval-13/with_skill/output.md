Next action: **export SBOM/lockfiles across your services** and run them through the discovery process in section 4 below — that's what turns this brief into real project names.

Assumptions made, no interview run (deliverable was requested directly, not a back-and-forth):

- Primary mandate = **supply-chain assurance** (platform eng, "projects we depend on" — no reach/marketing language used).
- No secondary mandate stated. If Calderwood sells to developers, reach becomes viable secondary — flagged below, not built in.
- Stack/ecosystem unknown — I could not run actual dependency resolution. Template + method given instead of a real shortlist.
- Finance payment constraints (PO-only vs card) unknown — both paths covered.

Numbers below carry **(published)** or **(self-set)** tags per source discipline. Self-set = this skill's default, not a market rate — argue with it.

---

# Open-source sponsorship portfolio — Calderwood Analytics

## Mandate

Primary: **supply-chain assurance**. Ties break toward coverage and fragility, not visibility.
No secondary set. If wrong, say so — it reweights the scoring axes in section 4.

## Budget

$180,000/yr ÷ 240 engineers = **$750/developer/yr**.

Context, both **(published)**:
- Industry pledge floor: >$2,000/FTE developer/yr. $750 sits at 37% of that floor.
- Sole disclosed actual spend: $3,700/developer/yr (one observability vendor, self-reported). $750 is 20% of that.

Not a problem to fix immediately — most first-year programs start below the floor. Say this plainly in any internal framing rather than claiming a coverage level you haven't hit yet.

## Model chosen: Breadth + Depth (two tiers), no foundation membership, no nominated fund

Three shapes considered:

1. **Breadth only.** Near-zero effort, hits coverage fast, buys zero visibility, and misses the handful of projects your product would actually break without. Rejected as sole shape — leaves your most fragile dependencies underfunded relative to their exposure.
2. **Breadth + Depth (recommended).** Breadth covers the long tail automatically; Depth puts real money behind the small number of projects that are both heavily used and one-person-fragile. Matches supply-chain mandate directly: coverage + fragility are the two things being bought.
3. **+ Employee-nominated fund.** Buys engineering engagement, not supply-chain coverage — wrong axis for this mandate, and it's a standing administrative job (cycle, ballot, eligibility checks) nobody asked to run. Deleted, not demoted — add later only if an engagement mandate gets named separately.

Foundation membership deleted too — no evidence a single foundation governs enough of your stack to make dues worth more than direct sponsorship. Revisit only if discovery (section 4) shows concentration around one (CNCF, PSF, Rust Foundation, OpenJS, etc.) — membership can then substitute for part of Depth.

## Tiers — the actual answer to "how much per tier"

| Tier | Purpose | Count | Per-project range | Total/yr | Mechanism |
|---|---|---|---|---|---|
| **1 — Breadth / Coverage** | Automatic funding across the full dependency graph, direct + transitive | ~500–1,300 destinations | $48–$120/yr ($4–$10/mo) **(published)** | **$63,000** (35%) | Dependency-share platform, one aggregated payment |
| **2 — Depth-Core** | Named sponsorship for widely-used, single-/few-maintainer projects | ~15 projects | $1,500–$6,000/yr, avg $3,600 | **$54,000** (30%) | Per-maintainer, platform tier or invoice |
| **3 — Depth-Strategic** | Load-bearing infra you cannot replace quickly | 4–6 projects | $3,000–$12,000/yr | **$36,000** (20%) | Custom/invoiced, negotiated |
| **Reserve** | Incident response, maintainer-in-trouble, mid-year load-bearing surprise | uncommitted | — | **$27,000** (15%) | Held, released on named trigger |

Total: **$180,000**. Split is self-set — adjust shares, not the four-bucket structure, once real coverage numbers come in.

Tier 3 spread mirrors the one published precedent for depth allocations: $1,750–$15,000/project/yr **(published)**, not a flat number — a build-tool your whole SDK sits on is not the same cheque as a moderately-used parser.

## Target selection — the process, run this against your real stack

I can't name real projects without your SBOM. Run this once, then annually:

1. **Resolve the graph.** Pull SBOM/lockfiles per service, or hit `deps.dev`'s dependency API per package (npm/PyPI/Cargo/Go/RubyGems/Maven/NuGet supported). Get direct + transitive.
2. **Map to maintainer, dedupe by owner** — not by package. One maintainer often stands behind a dozen of your dependencies; the sponsorship decision is per person, not per package.
3. **Pull health signals per repo.** OpenSSF Scorecard "Maintained" check (0–10): 7–10 active, 4–6 ask first, 0–3 likely dormant — money changes nothing there. Add the Criticality Score (0–1) for ecosystem-wide importance.
4. **Find + verify funding destinations**, in order: repo's `.github/FUNDING.yml` → owner-level `{owner}/.github` fallback → registry funding metadata → project site. **Fetch every URL before it enters the list** — a 404 or "not enrolled" page excludes the candidate. Never carry a funding link from memory.
5. **Score survivors, weighted for supply-chain primary:**

| Axis | Question | Weight |
|---|---|---|
| Exposure | How much of our stack depends on it? | ×3 |
| Fragility | How close to one person stopping? | ×2 |
| Relationship value | Would we want this person reachable during an incident? | ×2 |
| Audience fit | Do its users look like our hires? | ×1 |

6. **Disqualify:** vendor-owned projects, employee-maintained (if you adopt a conflict-of-interest rule), dormant with no revival plan, live conduct/security controversy, subscription-only recipients (your budget pays one-off).
7. **Bucket survivors:** long tail with no destination gaps → Tier 1. Exposed + fragile, ~15 → Tier 2. The 4–6 you genuinely could not replace fast → Tier 3.
8. **Carry the denominator when reporting coverage** — "resolved 412 of 470 dependencies, 58 had no source repo," never a bare percentage.

Skip stars, download counts alone, or "what the staff engineer likes" — none of those measure exposure or fragility, and they systematically miss the single-maintainer long tail that $10/month actually helps.

## Procurement

- **Invoiced corporate billing** (GitHub Sponsors): $5,000 minimum/invoice, 30-day terms, 3% fee, 3-year agreement **(published)**. Clears most of Tier 3, none of Tier 2, none of Tier 1.
- **Below $5,000**: pay by card (up to 6% total fee) or route through a fiscal host (3–10% cut, public ledger) **(published)**. This is how Tier 1 and most of Tier 2 actually get paid.
- **Warning — sequence this correctly:** switching your GitHub org to invoiced billing cancels every existing card sponsorship; maintainers get a cancellation email. Do the billing-mode switch **before** the first sponsorship goes live, not after.
- Tax treatment (engineering opex vs marketing vs charitable) changes approval path — route to finance/legal, don't decide it here.

## Policy — publish before first payment

- Sponsorship buys visibility, sustainability, a relationship. Never roadmap position, merged PRs, or priority outcomes. Priority *triage* can be negotiated; priority *outcomes* cannot.
- No pressure on a maintainer to accept, advertise, or thank on schedule.
- State conflict-of-interest rule now: if any dependency is maintained by a Calderwood employee, exclude it or name who decides the exception.
- State recurring vs one-off per tier — a sponsorship silently dropped at budget close reads as withdrawal, not budget discipline.
- Never shame a project with no funding link or one that declines money — some maintainers refuse deliberately.

## Measurement

| Metric | Baseline | Target (yr 1) |
|---|---|---|
| Fundable direct dependencies covered | capture before first payment | 80% **(self-set — below the 95% frontier one program hit; that took a dedicated integration)** |
| Dependencies with dormant maintenance score | capture now | declining, named number |
| Median response time on issues you filed upstream | capture now | improving, named number |

Pass check at 12 months, annually after:
- 80%+ fundable direct dependencies covered.
- Every Tier 3 sponsee has one documented interaction beyond the payment.
- No policy breach raised by a sponsee.
- Renewal decision made for every target before next budget close.

Do not build a revenue-attribution case on this — nobody clicks a README logo and buys, and supply-chain assurance isn't a reach mandate anyway. Measure coverage and response time, ignore total-dollars-given as a success metric.

## Renewal

Re-run the whole discovery process (section 4) annually — dependency graphs move, funding links go stale, maintainers hand off projects. Decide every sponsorship's renewal **before** budget close, not after; a lapse from internal timing reads to the maintainer as a withdrawal, even when it isn't one.