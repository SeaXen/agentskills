# Open source strategy — Kestrel Grid

## The number the CFO wants

**~$225K/year ongoing (range $180K–$270K), ~$235K in year one.** Built up line by line below — not a single vendor quote, a sum of named cost lines someone owns. Section "Operating model and budget" has the full table.

One more number that belongs next to it, not inside it: Kestrel Grid is **already spending ~$40K/year** rebasing the 40-patch scheduler fork at every upstream release. This plan redirects that spend into upstreaming rather than adding to the ask.

## Assumptions used

This is a one-pass deliverable, not an interview transcript, so these are stated rather than asked. Confirm before the board sees the number:

- Loaded engineering cost: $170,000/year ≈ $85/hour. Rescale every line pro-rata if your actual figure differs.
- What Kestrel Grid sells: licensed/deployed grid-balancing software plus support and integration services to utility customers — confirm the value-capture surface hasn't shifted to a SaaS or usage-priced model, which would change gate 3 below.
- The three repos are **not yet named** in your brief. I've scored plausible candidate types (telemetry/data SDK, an interchange data-format spec, a simulation/test-harness tool) rather than your real ones. Re-run the asset table in "Open" once you name them — the verdict changes completely if any of the three touches dispatch or control logic.
- Target foundation: unnamed in your brief. LF Energy is the obvious fit for grid-balancing software and is used here as the illustrative dues anchor. Get the actual quote before the board meeting — foundation dues move and are rarely published cleanly.
- Company type: treated as **public/late-stage software company**, not venture-backed startup, despite PE ownership. Reasoning below.

## Company type — why this isn't treated as a startup call

Ninety engineers, an established product, and a private-equity owner point away from "founder decides, low near-term reversal exposure" and toward the public/late-stage row: **defending an existing revenue line, deployment-mode boundary primitive, cross-functional decision with executive sign-off, highest reversal exposure of the three types.** PE ownership sharpens this further in one specific way none of the three named types fully capture: recurring opex gets underwritten against EBITDA, and the company will face an exhaustive OSS/IP audit at whatever exit eventually happens. A documented inbound policy and a clean upstream-contribution trail are exit-diligence assets, not just this year's cost — worth saying to the board explicitly, since it's the argument that lands with a PE-appointed director.

**Six weeks to the board is itself a structural signal, not just a deadline.** A hard date promotes interface-open and infrastructure-only, the only lines that need no tiering matrix and no standing feature-by-feature governance. Nothing you've described — three repos, a foundation seat, an upstream patch program — asks for buyer-tiered open-core (paid tiers inside an open product) in the first place, so the six-week window and the actual shape of the ask agree. That agreement is what keeps this number bounded instead of open-ended.

## What we sell

Grid-balancing software licensed and deployed to utility customers, monetized on the license plus support, integration, and certification work around each deployment. Confirm this is still accurate — it determines what "still stops a competitor" means in the competitive case below.

## Motive

Two distinct motives are in play, on different assets. Do not average them — one governs the three repos and the foundation seat, the other governs the scheduler patches, and they're measured differently.

**Primary, for the three repos and the foundation seat: trust and auditability.** Grid-balancing is critical infrastructure sold to a buyer (utilities) whose procurement and engineering staff run security and interoperability reviews as a purchase gate. This motive's evidence test is a named deal, audit, or compliance review where source access was actually requested — **you haven't given me that fact.** Before this goes to the board as "trust and auditability," find that case. If it doesn't exist yet, the honest motive is closer to plain distribution/ecosystem building around the SDK and data format, which is a fine motive but is measured on adoption and integration ease, not on procurement objections dropping — say which one you actually have evidence for, don't present the stronger-sounding one undemonstrated.

**Separate and already self-evidencing: lower maintenance through upstreaming**, for the 40-patch scheduler fork. Evidence test passed on your own numbers — you are already paying the private-maintenance cost (a rebase, every release) that this motive exists to eliminate. No external validation needed; this is close to a no-regrets move regardless of what the board decides on the other two items.

## Open

Placeholder scoring — replace the asset names once you confirm what's actually in the three repos, and do not let anything below pass gate check without that confirmation:

| Asset | Motive served | G1 irreversible | G2 differentiating | G3 value capture | G4 contributable | G5 owner | Verdict |
|---|---|---|---|---|---|---|---|
| Telemetry/data ingestion client SDK | Trust/distribution | Permanent, fine — no dispatch logic | Context (enables integration, doesn't win deals alone) | Deployment, certification, support contracts | Yes — utility-side integrators can patch their own connectors | Named engineer, ~5h/wk | **Open**, pending confirmation it holds zero dispatch logic |
| Grid data interchange format / schema | Trust, block-a-standard | Permanent, fine | Context | Certification + deployment relationship | Yes — third parties can implement against a published spec | Named engineer, ~2–3h/wk | **Open** |
| Simulation / synthetic-load test harness | Infrastructure-only, talent | Permanent, fine | Context | Nothing needed — no product code exposed | Yes, if it ships without internal grid topology data baked in | Named engineer, ~4h/wk | **Open**, conditional on scrubbing any real customer/topology data first |

## Closed

| Asset | Gate failed |
|---|---|
| Balancing/dispatch optimization engine and control-loop logic | G1 (never safely reversible) and G3 (nothing left to capture value on once published — no license retrofits the moat) |
| Any per-utility configuration, topology, or interconnection data embedded in the above three repos | G1 and G3, plus a live security concern: publishing control-plane behavior for critical infrastructure is a different risk than publishing an SDK, independent of business motive |

**This is the one line the board needs to hear stated out loud, not buried in an appendix**: if any of the three repos currently contains dispatch or control logic, stop and re-scope before publishing, regardless of budget approval.

## Not yet

Nothing in your brief clearly belongs here yet — but flag it if the three repos turn out to include anything genuinely differentiating (e.g., a proprietary forecasting model wrapped inside the "SDK"). Condition to revisit: a competitor ships an open equivalent, which would flip the value-capture calculus from "give it away for trust" to "commoditize before we're commoditized."

## Competitive case

A cloud vendor or a competing grid-software roll-up forks the published SDK and data-format spec and offers their own balancing product against it. What Kestrel Grid still holds: the proprietary dispatch/optimization engine itself (closed, above), the certification and interconnection-validation relationship each utility customer requires before anything touches their grid (a real, slow-to-replicate moat in this sector), existing support contracts, and the trademark. Nothing billed is given away. If any of that turns out not to be true once the three repos are actually specified, the line is wrong — move the asset, not the license.

## Decision rights

- **Business case ("should we do this")**: CTO/VP Engineering owns it, recommends to the CEO.
- **Compliance review ("is this okay to release")**: General Counsel or outside IP counsel, running licensing, patent, and trademark review in parallel — can block only on those grounds, not on the business case.
- **Final call**: CEO decides, presents to the Board given PE ownership and the scale of the recurring commitment — confirm the actual approval threshold with your CFO; PE boards often have a hard dollar line above which they must sign off.
- **Automatic escalation**: anything that would put dispatch or control-loop logic into a public repo escalates to CEO and Board immediately, no matter how small — this is the one gate no engineer should be able to clear alone.

## Commitments

No open-core paid tier exists here, so GitLab's "never move a feature to paid" promise doesn't apply directly. What does:

1. Dispatch, balancing, and control-loop logic never enters a published repo — an asset-level line, not a feature-tier one, held absolute regardless of roadmap pressure.
2. No repo publishes without a named maintainer and a stated release/response cadence already in place — no publish-then-staff-it-later.
3. If a published repo is ever deprecated, folded back into a closed release, or its maintainer changes, announce it with reasoning before it lands, not after.
4. Foundation membership tier is reviewed annually; a downgrade or exit is announced, not allowed to quietly lapse.

## Operating model and budget

Calibrated to operating-model.md's "Growth" stage: a named part-time owner, published inbound and outbound policies, an upstream-first default, one funded maintainer per open repository — not the full enterprise OSPO, not a single unfunded volunteer.

**Function assignment** (all six TODO Group functions, assigned even at fractional headcount):

| Function | Owner | Time |
|---|---|---|
| Strategy communication, internal/external | CTO/VP Eng | Folded into role |
| Release review, outbound | Named eng lead per repo | See maintainer time below |
| Inbound license/consumption policy | One engineer, part-time | 4h/wk |
| Community and contribution engagement | Repo maintainers | Folded into maintainer time |
| License/compliance review | General Counsel / outside counsel | On retainer |
| Upstream liaison (scheduler project) | One named engineer | 4h/wk steady-state |

**Annual cost, steady state (year 2 onward):**

| Line | Range | Point estimate |
|---|---|---|
| Repo maintainer time, 3 repos (12–18 eng-hrs/wk combined) | $66K–$80K | $73K |
| Outbound release/compliance hygiene, ongoing | — | $4K |
| Legal (licensing sign-off, trademark upkeep, foundation agreement) | $15K–$25K | $20K |
| Inbound OSS consumption policy (tooling + 4h/wk policy owner) | $35K–$50K | $43K |
| Foundation membership (confirm real quote; TODO Group's own published band is $5K–$250K+/yr, undated) | $25K–$75K | $50K |
| Upstream liaison, post-backlog steady state | $17K–$18K | $18K |
| Community presence (foundation events, minimal travel) | $10K–$15K | $12K |
| Security response allowance (contact, disclosure process) | — | $5K |
| **Total, steady state** | **$180K–$270K** | **~$225K/year** |

**Year one, additive:**

| Line | Cost |
|---|---|
| Release checklist / setup across 3 repos (license file, notices, secrets scan, trademark check) | ~$10K, one-time |
| Clearing the 40-patch upstream backlog (triage, cleanup, contribution-standard rework, ~12h/patch × 40) | ~$40K, one-time — funded by redirecting the ~$40K/year already spent on rebasing, not additive to the ask |

**Year one total: ~$235K. Steady state from year two: ~$225K/year.**

**On the scheduler patches specifically** — this is the cleanest win in the brief and stands regardless of what the board decides on the other two items: 40 patches rebased at every release, at an estimated 3 hours of conflict resolution and retest per patch, across roughly four upstream release cycles a year, is ~480 hours/year — about $40K — spent today with nothing to show for it and no line item anywhere. Upstreaming converts that into a one-time ~$40K cleanup plus a ~$18K/year liaison, netting a **~$23K/year structural saving starting year two**, and it deletes the risk of the fork silently diverging further from upstream every release it isn't merged.

**Inbound policy is not optional overhead — it's closing a live gap.** "Engineers just pull what they need" with no allowlist is a copyleft-license and supply-chain exposure sitting in a product sold into regulated utility infrastructure, and it is exactly the finding a PE-exit legal audit surfaces hardest. This line pays for itself independent of the outbound decision.

**On the foundation seat**: dues alone are the lowest-return rung on the participation ladder. If the goal is standards influence or a credible trust signal — not just a logo on a members page — pair the membership with at least one of: reporting issues upstream, or holding a governance seat once eligible. Paying and disappearing gets you neither.

## Measurement

| Program | Declared success signal |
|---|---|
| 3 repos + foundation seat | Utility procurement objections tied to auditability/interoperability measurably drop, and/or external contributor organizations appear on the SDK or spec — not stars, not downloads |
| Upstream patch program | Count of the 40 patches accepted upstream within 12 months; rebase hours per release trending to zero |
| Inbound policy | Time-to-approval on new dependency requests; zero unreviewed copyleft licenses found at the next audit |

**Re-evaluation trigger**: next annual planning cycle, plus an early re-read if a competitor ships a competing open interoperability layer, a utility customer's procurement team explicitly requests source access (upgrading the motive from assumed to evidenced), or the foundation's dues schedule changes materially.

## Handoffs — not done here

- License text for the 3 repos, CLA vs. DCO → `oss-license-strategy`.
- Running the repos day to day (maintainer ladders, succession) → `oss-governance`.
- Making the 3 repos discoverable once published → `oss-distribution-strategy`.
- The announcement itself → `oss-launch`.

## Before this goes to the board

1. Name the actual three repos and confirm none contains dispatch/control logic — the single highest-consequence unresolved item in this brief.
2. Get a real dues quote from the target foundation; the $50K point estimate is a planning placeholder, not a quote.
3. Find or concede the absence of a real case (a deal, an audit) supporting "trust and auditability" as the stated motive, rather than presenting it unevidenced.
4. Confirm your actual loaded engineering cost and rescale every line — $85/hour is a placeholder, not your number.