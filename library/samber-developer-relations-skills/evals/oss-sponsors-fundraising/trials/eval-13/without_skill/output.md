# OSS Sponsorship Program — Calderwood Analytics Platform Engineering

$180k/year, 240 engineers. Below is the selection method, the tier structure, and the governance process to run it every year.

## 1. Build the candidate list first

You can't fund what you haven't measured. Before assigning a dollar to anyone:

- Generate an SBOM across your actual production estate (`syft` + `grype`, GitHub's dependency graph, or Snyk/FOSSA if already licensed). Don't rely on `package.json`/`go.mod` at the repo level — aggregate across every service, because the same transitive dependency often shows up 40 times.
- Collapse to unique projects, not packages. `requests`, `urllib3`, and `certifi` all matter, but they don't need three separate line items — one line per maintaining entity/project.
- Cut anything trivially replaceable (a 200-line utility with five substitutes) from the candidate list before scoring. You're not funding npm-scale volume, you're funding load-bearing infrastructure.

Expect 150–400 unique projects in a 240-engineer org. You'll fund maybe 40–60 of them; the rest get nothing this cycle, which is fine — that's what the tiers are for.

## 2. Score every candidate on four axes

Weighted 0–5 each, no fifth axis for "we like them" — sentiment isn't a budget input.

| Axis | What it measures | How to score it |
|---|---|---|
| **Criticality** | How much breaks, and how hard recovery is, if this disappears | 5 = no viable swap, sits in the critical path of most services. 1 = dev-time convenience, swappable in a day. |
| **Blast radius** | How many internal teams/services actually touch it | Count distinct repos/services depending on it, bucket into quintiles. |
| **Sustainability risk** | Bus factor and funding gap | Check `git shortlog -sn` on the last 2 years, OpenSSF Scorecard's "Maintained" and "Contributors" checks, and whether the project already has a foundation or corporate backer. Single maintainer + no existing funding = 5. Backed by Linux Foundation/big-tech payroll = 1, regardless of how critical it is to you — your marginal dollar does nothing there. |
| **Leverage** | Does your money actually change an outcome | A $500 GitHub Sponsors tip to a project already pulling six figures from other sponsors is theater. A $500 grant that's 10% of a solo maintainer's total sponsorship income is real. |

Multiply Criticality × Blast Radius as your "importance" score, and Sustainability Risk × Leverage as your "impact-per-dollar" score. Rank by importance first, then let impact-per-dollar decide sizing within a tier — this is the actual mechanism that keeps you from just re-sponsoring whatever's trending.

## 3. The tier structure

Four tiers, $180k total. Round numbers, adjust ±20% once you've run the actual scoring pass — these are starting weights, not a formula to defend to the decimal.

**Tier 1 — Foundational (top importance score), ~$80k, 44%**
3–5 projects your entire platform sits on (e.g., your primary language runtime's ecosystem foundation, your core web framework, your CI/build toolchain, your primary datastore driver). $15k–$25k each, paid as a named annual sponsorship or a foundation membership (CNCF, Apache Software Foundation, PSF, Rust Foundation, OpenSSF — membership dues at silver/gold level often fund several Tier-1-caliber projects under one line item and buy you a voice in governance/roadmap). Prefer foundation membership over a single-project check when one exists — it diversifies the bet and gets you a seat at the table.

**Tier 2 — Load-bearing, ~$60k, 33%**
8–12 projects that are clearly important but not irreplaceable overnight — secondary libraries, key tooling, infra glue. $4k–$7k each. Direct recurring sponsorship (GitHub Sponsors org account, Open Collective) so it shows up as a stable line the maintainer can plan around, not a one-off.

**Tier 3 — Long tail, ~$25k, 14%**
30–50 smaller dependencies that scored moderate-to-low on importance but nonzero — don't hand-pick these individually, it's not worth committee time. Route this whole tier through **Tidelift** or **thanks.dev**, both of which ingest your actual dependency graph and auto-distribute proportionally to maintainers of what you really use, including deep transitive dependencies your scoring pass will never surface by hand. This is the tier that catches the single-maintainer left-pad-shaped risk you didn't know you had.

**Tier 4 — Reserve, ~$15k, 8%**
Held back, unallocated at the start of the year. Purpose: a critical dependency's maintainer announces they're stepping back, a CVE reveals a project you underrated, or a new team adopts something load-bearing mid-year. Spending from this tier doesn't wait for the annual cycle — it's the one line the committee (below) can deploy on a two-week turnaround.

## 4. Selection governance

- **Owner**: platform engineering lead + one security engineer + one rotating IC from a consuming team (not always the same person — rotate so scoring doesn't calcify around one person's taste). Three people, not a committee-by-consensus of twelve.
- **Cadence**: full re-score annually, ahead of budget planning. Quarterly 30-minute check-in to catch Tier 4 triggers (maintainer burnout announcements, new supply-chain findings, a dependency crossing from "nice to have" to "load-bearing" because a team built on it).
- **Inputs for scoring, not opinions**: SBOM diff since last cycle, OpenSSF Scorecard output, `git shortlog` activity, existing funding status (check the project's own FUNDING.yml / Open Collective page — most disclose this).
- **Exit rule**: a project can drop a tier or leave the list entirely at re-score time. Don't treat last year's recipients as an entitlement — communicate this upfront if you announce the program publicly, so nobody reads a non-renewal as a signal about the project's quality.

## 5. Payment mechanics

- Tier 1: foundation membership invoices (annual, via finance/legal — these are normal vendor contracts) or direct GitHub Sponsors/Open Collective for standalone projects without a foundation home.
- Tier 2: GitHub Sponsors org account or Open Collective, set to recurring monthly — steadier for the maintainer than one annual lump, and easier for you to pause/adjust without an awkward "we're ending the grant" conversation.
- Tier 3: single Tidelift subscription or thanks.dev budget covers the whole tier in one invoice; they handle distribution.
- Tier 4: kept in an internal budget line, deployed ad hoc via whichever mechanism the recipient already uses.

## Why this shape, not a flat per-project amount

A flat $180k / 60 projects ≈ $3k each wastes money two ways at once: it's noise to a foundation-backed project that doesn't need it, and it's too thin to matter to the solo maintainer who does. Weighting by criticality *and* discounting for existing funding is what makes $180k actually move outcomes instead of generating goodwill LinkedIn posts. The Tier 3 long-tail automation matters most in practice — hand-picking misses exactly the obscure, single-maintainer, deeply-transitive dependency that causes the incident you didn't see coming.