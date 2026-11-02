**Verdict up front:** Don't do CTO's plan as stated. It optimizes for the wrong funded driver, kills the one thing that actually competes with the rival's docs (a single, cross-product enterprise integration story), and leaves zero backup per squad. Recommended instead: hub-and-spoke, 2-person hub + 4 spokes covering 5 squads, reporting line to Product (not Engineering, not 5 separate EMs). Detail below.

---

# DevRel org design brief — Halcyon Robotics, 2026-09-23

## Situation

Trigger: CTO wants to move from centralized (6 advocates → you) to fully embedded (1 advocate per squad → that squad's engineering manager), starting next quarter.

Funded driver, per you: **sales enablement** — sales loses enterprise deals to a competitor with better integration docs. Mechanism is developer enablement (docs), but the money is justified by sales outcomes, not by product feedback. This distinction decides the whole brief — see Reporting line below.

CTO's stated reason ("advocates close to code") is real value, not fake — but it's a proxy for a different driver (product input) than the one funding the headcount. A shape optimized for product-input has to be tested against *sales enablement*, not assumed to transfer.

**Root-cause check before any re-org:** you haven't told me technical writing is an owned function anywhere. If nobody owns integration docs as a named surface today — separate from whatever advocates write as a side effect — moving advocates closer to code fixes proximity, not ownership. Confirm this before the re-org, because if technical writing is unowned, that's the actual fix, and it costs nothing to test first: name one owner, give them 4 weeks, re-measure.

## Work inventory

Incomplete — you gave me headcount and squad count, not surfaces. Fill this before locking anything; every re-org that skips it re-assigns work someone invisible is already doing.

| Surface | Owner today | Manager | Hours/wk | If it stops |
|---|---|---|---|---|
| Enterprise integration docs | **CONFIRM** | **CONFIRM** | **CONFIRM** | Sales keeps losing deals on this exact gap |
| Quickstarts / SDK samples | advocate(s) | you | ? | — |
| Community / forums | ? | ? | ? | — |
| Blog / content | ? | ? | ? | — |
| Conference / events | ? | ? | ? | — |
| Champions program | ? | ? | ? | — |

Action: before quarter start, get each of the 6 advocates to list their real surfaces and hours. Two minutes each, done in one sync.

## Reporting line

> DevRel reports to **Product**, because the funded driver is sales enablement and Product owns enablement depth and roadmap proximity — the two things an enterprise buyer's docs evaluation actually tests. This line will starve awareness/distribution. **Marketing** covers that gap via a named distribution partner, reviewed end of Q1.

Why not Engineering, despite CTO's push: the skill's own decision rule routes sales-enablement driver to product or marketing, never sales, and only product/engineering for a *product-input* driver. Engineering is right when the mandate is technical depth for its own sake; here the mandate is closing enterprise deals, which needs enablement + narrative Product is better placed to own.

CTO stays a **named co-sponsor** with real input on the docs program — collaboration-mode interlock, not the reporting line. That gets him the access he's actually after without collapsing headcount into 5 separate engineering managers.

If Product won't take ownership: fallback line is Engineering, with the tradeoff spelled out — optimizes technical depth and credibility, starves narrative and budget defense; counter-move is a measurement interlock with Marketing/Finance and an explicit ban on advocates absorbing feature work.

## Shape

Three candidates, ordered by efficiency (centralized > hub-and-spoke > embedded):

**A — Centralized, unchanged, add sales interlock.**
Cheapest, reversible in a week. Doesn't buy CTO's proximity ask. Doesn't fix docs credibility with engineers who currently don't review advocate-written docs. Rejected: doesn't move the funded driver, and ignores a real stakeholder ask with no counter-offer.

**B — CTO's plan as stated: 1 advocate per squad, reports to that squad's EM.**
Fails on inspection:
- Embedded is only justified when all four hold: driver is product input (ours is sales enablement — fails), squads have genuinely different audiences (unconfirmed — enterprise buyers likely evaluate the *whole platform's* integration story, not squad-by-squad — probably fails), each squad can fund and level the role (unconfirmed), a craft owner survives outside the squads (not named in CTO's plan — fails). Missing even one kills it; this fails at least two.
- **6 advocates into 5 squads doesn't divide.** One squad gets 2, or one gets 0, or someone floats — CTO's plan doesn't say which. Flag this gap directly to him; it's evidence the plan wasn't fully specified.
- Zero backup per squad. One advocate per squad = bus factor of one everywhere, with no floating reserve.
- Least reversible shape there is: each advocate gets levelled and promoted by an EM using engineering criteria that don't describe advocacy work. Retention leak, not a loud failure.
- Conway's Law cost, and the sharpest reason to reject: a team split by squad produces per-squad docs, not the cross-product integration story the competitor is beating you on. This plan can make the actual competitive gap **worse**, not better — 5 fiefdoms, no one owns the enterprise buyer's end-to-end journey.

**C — Hub-and-spoke. Recommended.**
- Hub: 2 people (you + one senior advocate) — owns enterprise integration docs standard, cross-squad IA, the sales interlock, and stays the named craft owner for leveling/promotion.
- Spokes: 4 advocates, dotted-line proximity into squads — sit in squad standups, Slack, one collaboration sprint per major launch — but stay on DevRel headcount and DevRel ladder.
- 4 spokes for 5 squads: doesn't divide either. Rank squads by enterprise-deal exposure (which squads' integrations actually show up in lost deals) and give the top 4 dedicated spoke coverage; hub covers the 5th lightly until headcount grows. **Action: get that ranking from Sales/Deal-desk before quarter start** — this is the one number that decides staffing, not a guess.
- Floor: hub of 2-3 + 2+ spokes — you clear it exactly at 6. Zero slack past that; flag as known risk, not hidden.
- Buys CTO's proximity without the fragmentation, the reversibility problem, or the ladder collapse.
- Costs: a quarter to stand up, a quarter to unwind if wrong, standing coordination overhead (spoke syncs).

Efficiency order says A first, but A doesn't move the driver and ignores CTO's real ask. B fails its own justifying conditions outright. **C is the pick** — it's the only shape both true to the funded driver and to the "close to code" motivation CTO has, without paying B's costs.

## Coverage

| Function | State |
|---|---|
| Advocacy | owned — 6 advocates (82.2% of teams staff this, 2024 survey) |
| Community management | **CONFIRM** — not mentioned, flag if unowned |
| Technical writing | **CONFIRM — likely the real gap.** 42.7% of teams staff this (2024 survey); if unowned here, this is probably the actual cause of "worse docs," independent of org shape |
| Developer marketing | **CONFIRM** |
| Developer education | **CONFIRM** |
| DX engineering | **CONFIRM** |

Don't skip this. An unowned function hidden in an org-chart move is invisible until the next deal is lost on it.

## Roles

| Person | Surfaces | Backup | Capacity |
|---|---|---|---|
| Hub lead (you) | docs standard, sales interlock, craft/leveling | senior advocate (hub #2) | 70% (baseline, adjustable) |
| Hub #2 (senior advocate) | cross-squad IA, 5th squad light coverage | hub lead | 70% |
| Spoke 1–4 | top-4 exposure squads, 1 each | each other, paired | 70% |

Bus-factor-one risk: every spoke, by construction — flag it, don't hide it, and set the trigger below to catch it.

## Interlocks

- Squads (via spokes) — facilitation, decaying to X-as-a-service after launch — technical review in, docs/demo coaching out — arbiter: hub lead.
- CTO / Engineering leadership — collaboration, capped to the enterprise-docs program only, with an end date — technical credibility review in, roadmap access out — arbiter: hub lead, escalate to CTO.
- Sales — X-as-a-service, strictly — field objections and lost-deal doc gaps in, evaluation material out — arbiter: hub lead.
- Product — collaboration during launches, X-as-a-service otherwise — roadmap and launch dates out, developer feedback in — arbiter: Head of Product (your new manager under this line).
- Marketing — X-as-a-service — distribution and channel data out, content in — arbiter: hub lead.

## Ladder and titles

Advocates stay on a DevRel-specific ladder, owned by the hub lead — this is the whole point of keeping a craft owner. If CTO's plan had gone through as stated, advocates would level against engineering criteria that don't describe their work — a slow retention leak, flag this explicitly if he pushes back on hub-and-spoke.

## Budget

**CONFIRM.** You didn't say who owns headcount budget vs program budget — in 60% of surveyed programs (2024) these are different people. Get both names before quarter start; whoever approves the CTO's re-org may not be who funds it.

## Re-org triggers

- CTO or Product sponsor changes.
- A squad starts running its own devrel-shaped work without a declared interlock.
- Any spoke coverage stays bus-factor-one for a full quarter with no backup plan.
- Team crosses 10 people — shapes other than hub-and-spoke become affordable.
- The CTO collaboration interlock runs past its end date without renewal — sign it's becoming the default operating mode.
- Enterprise deal losses citing docs don't drop within two quarters of this move — signals the fix was proximity when the real gap was ownership (technical writing).

## Transition

1. **Week 1:** publish this brief. Pull the real work inventory from all 6 advocates. Get the squad enterprise-exposure ranking from Sales.
2. **Month 1:** confirm reporting line (Product vs Engineering fallback) with whoever owns that budget. Assign 4 spokes to top-4 ranked squads. Name hub #2.
3. **Quarter 1:** stand up the CTO collaboration interlock with its end date. Re-check bus-factor-one risk on each spoke.
4. **Unchanged until proven otherwise:** career ladder stays DevRel-specific, not engineering.

## Quality gate — self-check

- Work inventory: **fails** — you owe me real data, flagged above, not blocking delivery of the plan but blocking the final headcount math.
- Reporting line: **passes** — driver, leader, starved pillar, named cover, review date all stated.
- Shape: justified by coordination bought, not company-copying. B explicitly deleted with reasons, not just ranked low.
- Six functions: 1 of 6 confirmed owned (advocacy), 5 flagged **CONFIRM** — not blank, but not resolved either.
- Bus factor: flagged as known risk on every spoke, not hidden.
- Interlocks: one mode per adjacent team, each with a named arbiter.
- Capacity: 70% baseline stated as adjustable, not a benchmark.
- No headcount ratio quoted as benchmark. No compensation band anywhere.
- Re-org triggers: 6, all observable without a survey.

**Next action:** send the squad enterprise-exposure ranking request to Sales/Deal-desk today — it's the one number that decides who gets a spoke first, and it's a single Slack message.