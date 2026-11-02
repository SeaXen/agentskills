# Sanity check: your 40/30/20/10 split — verdict first

**The money is roughly right. The shape is wrong, in one place that matters for the board.**

Three of your four "mandates" are real, independent spending motions. The fourth — "10% because we signed a public pledge" — isn't a spending category at all. The pledge is a floor your *total* qualifying spend either clears or doesn't, plus a report you publish. Treating it as a quarter-sized bucket alongside the other three double-counts money you're already spending under supply-chain and developer-brand, and if your engineering headcount is above ~15 FTE, a standalone $31k slice wouldn't even clear the pledge's own $2,000/FTE floor on its own — so as a dedicated line it's simultaneously redundant *and* too small to mean anything by itself.

Fix: fold the pledge into a compliance check on the whole program, not a line item. That frees real dollars — which I've routed to a reserve line (you had none; the skill defaults to 10-20%, you had 0%) and to breadth, which is exactly what improves the coverage number the pledge's own published exemplar reports on.

Net effect on your instinct: after fixing the structure, the three real motions land at **39% / 29% / 19%** — within a point of your original 40/30/20. You didn't get the sizing wrong. You got the *category* wrong on the fourth line.

One more structural point before the board sees this: four mandates weighted against each other implies you can trade them off — "3 points less brand buys 3 points more supply chain." You can't, cleanly; they're different goals with different owners and different renewal tests. What the weighting *should* do is set one **primary** (breaks ties on the last dollar and on what the annual report leads with) and the rest follow. Your ranking already does this — supply-chain is clearly #1 — I'm just making it explicit and structural rather than implicit in a ratio, because a ratio without a named primary is the thing a board member is trained to poke at.

Everything past this point is the full brief, built on that fix. Figures are labeled **(published)** — sourced, drifts over time, re-check before quoting — or **(self-set)** — this skill's starting default, not a market rate; argue with it.

---

# Open-source sponsorship portfolio — Nord Ledger, 2027

## Mandate: primary and secondary, and what breaks ties

- **Primary: supply-chain risk reduction.** Owned by Engineering/Security — consistent with your framing and the highest weight. Breaks every tie on the last dollar; the annual report leads with dependency coverage, not with a placement count.
- **Secondary: developer brand.** Owned by DevRel/Marketing. Wins the tie only when the primary is indifferent (e.g., two dependencies of equal exposure, one with a visible README).
- **Internal engagement** and **pledge compliance** are real, but neither breaks ties — they're judged on their own separate terms (participation rate; floor met + report published), not against the other two.

**Open question, needs your answer before this locks:** does Nord Ledger sell to developers (payments API/SDK evaluated by engineering teams), or to non-developer buyers (finance, ops)? If the former, developer brand is a real marketing/pipeline return and depth placements should be priced against traffic like a media buy. If the latter, "developer brand" mostly returns employer brand and recruiting — size it against your hiring budget, not a pipeline number, or it won't survive a board challenge on ROI.

## Budget: total, per-developer check, split, reserve

**Total: $310,000 for 2027.**

**Per-developer check — I need your FTE engineer count to finish this line.** The math you can run immediately:

- Industry pledge floor **(published)**: >$2,000/FTE developer/year.
- One disclosed program's actual spend **(published, single self-reported point)**: $3,700/developer.
- Breakeven for your $310k: $310,000 ÷ $2,000 = **155 developers**. Above that headcount, the *whole* $310k (before excluding non-qualifying spend — see below) doesn't clear the pledge floor on its own, and you should not publish a pledge-compliant report without either raising budget or being explicit that the pledge covers a subset of the org.
- Four categories don't count toward the floor even if paid **(published)**: money to a company-controlled project, software benefiting Nord Ledger exclusively, a maintainer you already employ, or any deal with substantial reciprocal benefits beyond a thank-you. Net these out before you publish a "we cleared the floor" claim.

| Line | Share | Amount | What it buys |
|---|---|---|---|
| Breadth (supply chain, primary) | 39% | $122,000 | Automatic coverage across the dependency graph |
| Depth (developer brand, secondary) | 29% | $91,000 | ~6-10 named relationships on real traffic surfaces |
| Employee-nominated fund (internal engagement) | 19% | $60,000 | $5,000/month, one project per cycle |
| Reserve | 12% | $37,000 | Maintainer in trouble, mid-year load-bearing dependency, incident |
| Pledge compliance | — | $0 dedicated | Tracked as pass/fail against total qualifying spend above; reported annually, not budgeted separately |

Reserve sits at the low end of the self-set 10-20% band. Push it to 15% if you'd rather buy slack than a slightly bigger fund or breadth line — trivial to move, say the word.

## Model: allocation models chosen, and what each deliberately fails at

Running three concurrent motions (breadth + depth + employee fund) is more than the skill's usual default of "breadth plus one other" — most working programs stop at two. That's a deliberate call here because you named three distinct real mandates, not a shortcut; know that it costs more admin than a two-motion program (below).

- **Breadth** (supply chain): near-zero discovery cost once your dependency graph is resolved. Buys coverage and an honest "we fund what we use" answer. Fails at visibility — a $6/month sponsorship never shows up on a slide.
- **Depth** (developer brand): a human decision per project, ~a week to select/clear/brief, plus an annual renewal conversation. Buys the only verifiable placement and the only named maintainer relationship in this portfolio. Fails at covering the long tail — that's breadth's job, not this one's.
- **Employee-nominated fund** (internal engagement): the highest-effort motion — a standing monthly job (nominate, check eligibility, vote, communicate). Buys engagement and a defensible selection story. Fails at targeting precision; votes drift toward already-famous projects, so seed each ballot with underserved candidates pulled straight from the breadth discovery list — that's a free synergy between the two motions, use it.
- **Foundation membership**: not included. Nothing in your framing names a foundation whose governance you need a seat at; joining one for adjacency is dues for a room nobody at Nord Ledger sits in. Revisit only if a specific foundation governs a project you're already funding at depth.

## Targets: ranked table

I can't produce a verified list without your actual dependency data — no repo, lockfile, or SBOM was provided for this conversation, and the skill is explicit that a funding link "from memory" is not acceptable to publish against. Here's the framework and what a real row looks like; send a lockfile or SBOM and I'll run it for real.

**Discovery method** (Step 4 of the skill, endpoints in `references/target-discovery-and-scoring.md`):
1. Resolve the full dependency tree (direct + transitive) from your lockfile/SBOM via `deps.dev` or equivalent per-ecosystem API.
2. Map each package to a repository, **deduplicate by maintainer, not by package** — one person often stands behind a dozen of your dependencies.
3. Pull a Maintained score (0-10) and a criticality signal per repo; below 3 is likely dormant — money changes nothing there.
4. Find and **verify** (fetch, don't assume) a funding destination per maintainer: `FUNDING.yml`, owner-level fallback, registry metadata, project site.
5. Report the denominator honestly: "resolved 412 of 470 dependencies; 58 had no source repository" — never a bare percentage.

**Scoring, once you have real candidates** — weights differ by which mandate a candidate serves:

| Axis | Weight for supply-chain candidates | Weight for developer-brand candidates |
|---|---|---|
| Exposure (how much of our stack depends on it) | ×3 | ×1 |
| Fragility (how close to one person stopping) | ×2 | ×1 |
| Audience fit (buyers/hires overlap) | ×1 | ×3 |
| Relationship value (reachable during an incident) | ×2 | ×1 |

Payability is a filter, not a score — no verified destination, no target; propose in-kind support instead. A dormant score (0-3) is also a filter, not a discount.

**Illustrative row shape** (composite, not a real target — this is what a defensible row looks like once you run discovery):

| Project | Deps covered | Maintained | Fragility | Destination (verified) | Amount/yr | Mandate |
|---|---|---|---|---|---|---|
| Auth-path crypto library | 3 direct | 8/10 | High — 2 maintainers | Fiscal-host collective ✅ | $12,000 | Supply chain |
| Payments SDK's CLI dep | 14 (1 direct, 13 transitive) | 9/10 | High — 1 maintainer | Sponsorship platform, personal ✅ | $6,000 | Supply chain + brand (dual) |

## Amounts: tier per target, and the surface it lands on

- **Breadth**: $4-$10/month per destination **(published)**. Start at **$6/month flat (self-set)**, routed through a dependency-share platform so it executes without per-maintainer outreach. Coverage target: **80% of fundable direct dependencies within year one (self-set)** — the only company that's published higher (95%+) built a dedicated platform integration to get there; don't present 80% as a compromise, it's the honest starting bar.
- **Depth**: no flat tier — take the number from each maintainer's own published ladder, and go custom/invoiced only when the project is genuinely load-bearing. One published depth portfolio ran $1,750 to $15,000 per project per year **(published)** — the spread is the lesson, not the average. At $91,000, expect roughly 6-10 relationships, not a uniform split.
- **Employee fund**: $5,000/month, one project per cycle. Half the size of the documented reference implementation ($10,000/month) **(published)** — appropriate if Nord Ledger's eng org is smaller than the large employers that run the full-size version; tell me your headcount and I'll sanity-check the fund size against it too. Eligibility, every one required: in use by Nord Ledger, OSI-approved license, able to receive funds, not maintained by a Nord Ledger employee.

## Procurement: payment path, minimums, sequencing

- **Set up invoiced corporate billing before the first depth sponsorship goes live**, not after. Switching an org to invoiced billing cancels its existing sponsorships **(published)** — sequence this wrong and your first maintainers get a cancellation email that reads as a withdrawal.
- Invoiced billing: **$5,000 minimum/invoice, 30-day terms, 3% service fee, 3-year agreement (published)**. Your depth line clears this comfortably combined across maintainers on one invoice; breadth's $6/month lines individually never will — route breadth through a dependency-share platform or a fiscal host instead, not invoiced billing.
- Fiscal hosts take **3-10% (published)**, the largest at 10%, and publish a public ledger — fine for maintainers not incorporated.
- **Vendor onboarding, tax forms, sanctions screening apply to individual maintainers exactly as to any supplier.** Start this for your ~6-10 depth maintainers immediately if approved — as a payments company, Nord Ledger's finance/legal likely already run stricter geography/sanctions screening than a typical software vendor; confirm whether that stricter bar rules out any candidate before you promise a date.
- Tax treatment (marketing vs. engineering vs. charitable spend) changes approval path and jurisdictional handling. That's finance and legal's call — I'm flagging it, not deciding it.

## Policy: what sponsorship does not buy, eligibility, conflicts, disclosure

Publish before the first payment — an unpublished policy reads as favoritism from outside:

- Sponsorship buys visibility, sustainability, a relationship. **Never roadmap position, merged PRs, or priority outcomes.**
- No pressure on a maintainer to accept money, advertise it, or perform gratitude on a schedule.
- Employees advocating publicly for a project Nord Ledger funds disclose the relationship.
- Eligibility: in use by us, OSI-approved license, can receive funds, not maintained by our own staff. Named owner and appeal path — **you need to name who decides and how a rejected nomination gets appealed; I don't have that answer yet.**
- Never shame a project with no funding link or that declines money — some maintainers refuse funding deliberately.
- State recurring vs. one-off per sponsorship. A sponsorship silently dropped at budget close reads worse than one never started.

**Redlines I don't have from you yet:** competitor-maintained projects, license restrictions beyond OSI-approved, anything legal has already flagged. Standard disqualifiers regardless: vendor-owned projects (money's a rounding error to a funded company), employee-maintained projects, subscription-only recipients against a one-off budget, live conduct/security controversies, dormant projects with no maintainer-agreed revival plan.

## Measurement: metrics per mandate, review date, pass threshold

| Mandate | Measure | Ignore |
|---|---|---|
| Supply chain | Share of fundable dependencies covered; dormant-dependency count; issue response time | Total dollars given |
| Developer brand | Placements live and verified; referral traffic from placement URLs; unaided mentions | Impressions estimated from stars |
| Internal engagement | Employees contributing per cycle; nominations submitted; participation rate | Fund size |
| Pledge | Floor met (total qualifying spend ÷ FTE devs); annual report published | — |

**Pass threshold, checked at 12 months then annually (self-set):** every paid placement live and verified; ≥80% of fundable direct dependencies covered; every depth sponsee has at least one documented interaction beyond the payment; no policy breach raised by a sponsee; a renewal decision made for every target before 2028 budget close.

Capture your baseline on every row **before** the first payment — it's the only number in that table with any authority, and it's currently unmeasured.

## Renewal: decision date, what would end each sponsorship

- Renewal decision for every target lands before the 2028 budget close, not after.
- End a sponsorship only for: the dependency is gone, the project's dormant, the mandate changed, a policy breach. Never for a technical disagreement — that's the exact influence the policy promises not to buy.
- Tell a maintainer before ending a sponsorship, with a reason and a date.
- Re-run discovery annually — last year's verified funding list is this year's unverified one.

---

## What I need from you before this goes to the board

1. **FTE engineer count** — closes the pledge-floor math and sanity-checks the employee-fund size.
2. **Developer-brand assumption** — confirm developers are a real buying influence, or tell me this is recruiting-driven; changes how the 29% gets defended in the room.
3. **A lockfile or SBOM** — the targets table above is a framework, not a real list, until I can run discovery against your actual stack.
4. **Who administers this** — DevRel/OSPO running depth + fund + reporting, with Engineering/Security signing off on supply-chain picks, is the default split; confirm or redirect.
5. **Redlines** — competitor projects, license restrictions, anything legal's already flagged.