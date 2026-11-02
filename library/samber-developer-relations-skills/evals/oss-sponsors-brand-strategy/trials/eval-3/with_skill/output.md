# Open-source sponsorship portfolio — Corvid Freight, 2026

## Mandate

**Primary: internal engagement.** Re-engage the 90 engineers, fix platform-team morale, reverse the contribution drop-off. This is what breaks every tie below — which project wins the budget, which metric decides renewal.

**Secondary: supply-chain assurance** (assumed default, not stated — confirm). Corvid sells to logistics operators, not developers, so a "reach" mandate would return employer-brand/recruiting value only, not a marketing case anyone at review will believe. Supply chain is the cheapest complementary motion and gives engineers a visible "we fund the stack you actually run" backdrop that reinforces the primary mandate instead of competing with it.

Ranking the four mandates against each other would be false precision — engagement wins outright per the head of engineering's stated goal.

## Budget

$180,000/year ÷ 90 engineers = **$2,000/developer/year** — lands exactly on the published pledge floor (more than $2,000/FTE, **published**). ℹ️ Note the pledge requires strictly *more than* $2,000; if Corvid ever wants to sign that pledge formally, price a token amount above the floor. The only disclosed real-world spend, for context, is $3,700/developer (**published**, single self-reported data point) — $2,000 is a credible starting line, not the top of the market.

| Line | Share | Amount/yr | Mandate served |
|---|---|---|---|
| Breadth (dependency graph) | 16.7% | $30,000 | Secondary — supply chain |
| Employee-nominated fund | 66.7% | $120,000 | Primary — engagement (also plays the depth role, see below) |
| Reserve | 16.7% | $30,000 | Either, opportunistic |

Reserve sits at the upper edge of the 10–20% self-set default because the effort ceiling (below) leaves little slack to improvise a fourth motion if something breaks.

## Model chosen, and what the others deliberately fail at

Three motions, not the usual four — **no separate depth line**. Reasoning:

- **Breadth**: near-zero effort, automatic coverage. Fails at visibility — nobody in engineering will feel this line even though it's the cheapest credibility the program buys.
- **Employee-nominated fund, re-cadenced quarterly, doubling as depth**: this is the only model in the menu that buys engagement at all — "the thing it buys does not appear on any other row." Fails at targeting precision (votes drift toward famous projects, not necessarily the ones load-bearing for Corvid).
- **Foundation membership: cut.** Nothing in the interview named a foundation that governs Corvid's stack. Joining one for adjacency is dues for a room nobody at Corvid sits in. Revisit only if a specific foundation (e.g. one governing a core platform dependency) turns out to matter.
- **A standalone depth motion: cut, folded into the fund instead.** Depth normally costs "about a week per project to select, clear and brief, plus a renewal conversation every year" per project — running that *and* a separate nomination cycle *and* breadth would not fit inside the effort ceiling below. The nominated fund's own selection process (nomination + vote) already produces a named, verifiable relationship — that *is* depth, done once, not twice.

⚠️ **The direct tension in this brief**: the effort-ceiling rule this skill uses says "an effort ceiling of a few hours a month deletes the employee-nominated fund" — and four hours a month is exactly that. Taken literally, the model built for your stated primary mandate is the one the skill's own default would delete. I did not delete it, because deleting it leaves the primary mandate served by nothing. Instead I redesigned its cadence (below) to fit the stated budget. Flagging this explicitly rather than silently picking a side — if four hours a month turns out to be too tight in practice, the fix is a longer cycle (semiannual, two winners a year), not more line items.

## Why quarterly, not the reference monthly cadence

The published reference (FOSS Contributor Fund, O'Brien & Grover, O'Reilly 2021) runs monthly: $10,000/month, one project per cycle, "a standing job — a cycle to run, eligibility to check, a vote to administer, a result to communicate," every month. Twelve of those a year does not fit a 4-hour/month total admin budget that also has to cover breadth and reserve.

Quarterly cuts recurring administration roughly 3x: four cycles a year, each concentrated (~8–12 hours: open nominations, run the eligibility filter, run the vote, announce, start the winner's invoice), then near-zero the other two months of the quarter. That averages out close to the stated 4h/month — tight, not comfortable. It also gives each winner a large enough check to be worth the announcement, which is the point of an engagement mechanism: a visible quarterly win reads better internally than a diffuse monthly trickle nobody notices.

**Design**: one flagship project wins $30,000 per quarter. If the top vote-getter can't sensibly absorb that (a solo maintainer with no entity to invoice, or a project whose governance can't receive a lump sum that size), split the quarter's pool across the top 2–3 nominees instead — a fallback rule, not the default path, so the common case stays one invoice per quarter.

Reuse breadth's resolved dependency list and verified funding destinations as the nomination ballot's starting pool — it's already been measured, and seeding the ballot with underserved candidates (not just famous ones) is exactly what the published fund's own retrospective recommends.

## Targets

⚠️ Not populated — I have no SBOM, lockfile, or repository to resolve Corvid's actual dependency graph from, and this skill is explicit that funding decisions must be measured, never estimated or invented. Send a lockfile (or point me at a repo) and I'll run:

1. Resolve the full dependency tree (direct + transitive) via `deps.dev` or your manifests.
2. Deduplicate by maintaining owner, not by package — one maintainer often stands behind a dozen dependencies.
3. Pull maintenance/health signals per repo (Scorecard `Maintained` 0–10; disqualify anything scoring 0–3 without a revival plan).
4. Resolve and **verify** a funding destination per owner (`FUNDING.yml`, org-level fallback, registry metadata) — dead links get excluded, not silently listed.
5. Report the honest denominator: "resolved N of M dependencies; K had no source repository," never a bare percentage.

Standing eligibility filter for every candidate, in both breadth and the nominated fund: OSI-approved license, able to receive funds, not maintained by a Corvid employee. That last filter matters more than usual here — if the platform team's morale problem includes wanting to upstream work on something they themselves maintain, that's a case for contribution *time*, not sponsorship cash; keep it on a separate list.

## Amounts per target

| Line | Tier logic | Surface |
|---|---|---|
| Breadth | $4–$10/month per dependency (**published** reference range), routed as one consolidated spend, not priced per project | None — coverage, not placement |
| Nominated-fund winner | $30,000/quarter, self-set — above the highest published single depth line ($15,000/yr, session-replay library, **published**) because it's a quarterly, not annual, award | Named relationship; whatever visibility the winner already offers (README/site credit), never requested as a condition |
| Reserve | Sized to one depth-tier emergency without reopening the budget | N/A |

## Procurement

Both finance constraints — **no company cards at all**, purchase order against a **$5,000 minimum per invoice** — point to the same fix: pay in pre-funded lump sums, never per-transaction.

1. **Set up invoiced corporate billing on the primary sponsorship platform before any sponsorship is placed.** Sequencing matters: switching an already-sponsoring org to invoiced billing cancels its existing sponsorships and sends maintainers a cancellation email. Doing it first avoids that entirely.
2. **Breadth**: route through a dependency-share aggregator (thanks.dev-style) funded by one upfront PO ≥ $5,000 (e.g., the full $30,000 breadth line, invoiced once or in quarterly $7,500 tranches — all clear the minimum). The aggregator distributes the $4–10/month per-dependency amounts automatically; Corvid never issues a $10 invoice.
3. **Nominated fund**: each quarterly winner's $30,000 clears the $5,000 minimum on its own — no bundling needed. Start vendor onboarding (tax forms, sanctions screening) for the eligibility-checked nominee pool *before* the vote closes, not after a winner is announced, so a promised payout never stalls behind paperwork in public.
4. **Reserve**: pre-fund a balance with a fiscal host (Open Collective-style) via a single PO ≥ $5,000. Fiscal hosts pay out against a ledger, so individual emergency disbursements below $5,000 don't each need their own invoice — the PO already cleared the minimum once.

⚠️ **Open item, needs finance/legal sign-off**: invoiced corporate billing on the main platform runs under a **3-year agreement term** before renewal (**published**). Nobody has confirmed Corvid will sign that. If legal won't accept a multi-year platform agreement, route everything through fiscal hosts instead — no card option exists as a fallback given the no-cards rule.

Tax treatment (marketing spend vs. engineering spend vs. charitable giving) changes approval path and books differently by jurisdiction — that's a question for Corvid's own finance/legal, not a call this brief makes for you.

## Policy

Publish before the first payment:

```markdown
# Open-source funding policy — Corvid Freight

## Why we fund
We fund the open-source projects our platform depends on, and let engineers
nominate and vote for a project to receive a larger quarterly award — to keep
Corvid engineers engaged with the ecosystem we build on.

## What we fund
Eligibility: in use by us, OSI-approved license, able to receive funds, not
maintained by a Corvid employee. Vendor-owned projects and dormant projects
(no revival plan) are excluded.

## How much and how often
Breadth: automatic, monthly, across our dependency graph. Nominated fund:
quarterly, one flagship award per cycle (occasionally split among the top
nominees). Both recurring unless stated otherwise at renewal.

## How a project is chosen
Breadth: automatic, from our resolved dependency graph. The quarterly award:
nominated by any employee, voted on by employees who contributed to open
source during that cycle, filtered against the eligibility rule above before
the ballot opens.

## What sponsorship does not buy
No roadmap position. No merged pull requests. No priority outcomes. No
obligation to advertise us, thank us, or respond to us faster than anyone else.

## Conflicts of interest
Projects maintained by a Corvid employee are excluded from cash funding;
we support those with contribution time instead.

## Disclosure
Employees who publicly advocate for a project we fund disclose the relationship.

## Contact
<named OSPO administrator>
```

## Measurement

| Mandate | Measure | Ignore |
|---|---|---|
| Internal engagement (primary) | Employees contributing per cycle; nominations submitted; participation rate | Fund size alone |
| Supply chain (secondary) | Share of fundable dependencies covered; dormant-dependency count; response time on issues Corvid files upstream | Total dollars given |

Capture every baseline **before the first payment** — today's contribution rate and today's dependency coverage are the only numbers in this table with any authority. Put a named owner on each row.

**Pass threshold** (self-set), checked at 12 months then annually: every quarterly winner's placement (if any) verified live; ≥80% of fundable direct dependencies covered (self-set, deliberately below the one published 95%+ frontier, which took a dedicated platform integration to reach); a renewal decision made for every line before budget close; zero policy breaches raised by a sponsee.

Publish a short annual report — year, developer headcount, total paid, amount per recipient, one honest paragraph on what went wrong. That last paragraph is what makes it read as a program instead of a press release.

## Renewal

Decide every line's renewal before budget close, not after — a lapse caused by internal timing reads to a maintainer as a withdrawal. End a sponsorship only for a stated reason: the dependency is gone, the project is dormant, the mandate changed, or a policy breach. Never for a disagreement over a technical decision — that's exactly the influence this policy promises not to buy.

Re-run dependency discovery annually before the target list renews; funding destinations go stale and the graph moves.

## What to confirm before this goes live

- Secondary mandate = supply-chain assurance (my default, not stated).
- Whether the 90 engineers get any dedicated work time to nominate/vote, beyond the administrator's 4 hours/month.
- Whether legal will accept the 3-year invoiced-billing term, or the program routes through fiscal hosts only.
- A lockfile or SBOM, so the target list stops being a process description and becomes real, verified rows.