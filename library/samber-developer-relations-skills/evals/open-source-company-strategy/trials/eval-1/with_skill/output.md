# Open source strategy — Halyard Systems

## Recommendation, up front

**Don't open the engine yet. Don't close the question either.**

Two of the four reasons on the table are not motives, per this skill's own diagnostic — say so plainly:

- **"Three engineers have pushed for a year, one may quit."** Real retention risk. Not a strategy. Route it into a talent motive or a contribution policy, never into the open/closed decision itself.
- **"Two competitors open-sourced their engines."** Their line served their value capture, which you can't see from outside. It might mean they'd already lost the engine as a differentiator and had nothing left to protect there — or it might mean they've built a different revenue mechanism you haven't. Copying the *move* without knowing *their* gate-3 answer is decoration.

The one fact that matters most in your message is this: **"the engine isn't really the core of what we do anymore, the ops tooling is."** That's not context — that's your actual gate 2 answer, and it points toward a real motive: **commoditize your complement**, correctly formed. But you're not there yet, because today 100% of your $6.1M ARR is billed *on the engine itself* ($4,200/core), not on the ops tooling. Open-sourcing the thing you meter, before the thing you'd meter instead is priced and proven, isn't commoditizing a complement — it's Spolsky's own counter-example, Sun giving away the hardware it sold. The complement and the product are still the same object in your business model, even if they're no longer the same object in your engineering org.

That gap — between where the value already sits and where the invoice still points — is the whole strategy problem. Close it before you touch the license.

## What we sell

Today: a time-series storage engine, on-prem, licensed per core, $4,200/core/year, $6.1M ARR, 38 customers. By your own account, the engine is not what customers are actually buying anymore — the ops tooling around it (deployment, upgrades, cluster management, and whatever operational surface your 7 engineers spend their time on) is doing the differentiating work, while the invoice still meters the engine.

*Open question, needed before Step 4 is final: is any part of the ops tooling sold or priced separately today, or is it 100% bundled into the per-core fee? If it's fully bundled, you have no second SKU to fall back on — that's the gap to close first.*

## Motive

**Not yet named with evidence.** Candidate: commoditize your complement, with the engine as the complement and the ops tooling as the product whose demand should rise. Evidence test per the skill: name the product whose demand rises, name the complement. Right now you can name the complement (the engine) but not the product, because the ops tooling has no independent price tag to rise against. Until it does, this motive fails its own test — it's the Java trap, not the DOS-licensing case.

Secondary candidate worth investigating, not yet evidenced: **block a competitor from owning a standard.** If the two competitors' now-open engines are converging on a de facto wire format or on-disk format that customers start expecting, you risk being the isolated proprietary holdout rather than the premium one. That's a real motive if true — but it needs a name (which competitor, what standard, what happens if you don't respond), not an inference from "they did it."

Not a motive, logged so it doesn't resurface as one next quarter: retention pressure from the team, and competitor mimicry.

## Open

None yet, at gate quality. Candidate for later, once split:

| Asset | Motive served | G1 irreversible | G2 differentiating | G3 value capture | G4 contributable | G5 owner | Verdict |
|---|---|---|---|---|---|---|---|
| Wire protocol / client SDKs | Commoditize the complement | permanent, likely fine | context (commodity already, per 2 competitors) | ops tooling + support | plausible, storage-engine ecosystems attract contributors | **unnamed** | **Not yet — needs an owner** |
| Engine's commodity internals (storage format, basic replication) | Commoditize the complement | permanent — confirm fine | context, pending your own split | ops tooling + enterprise features | plausible | **unnamed** | **Not yet — needs the split below** |

## Closed

| Asset | Gate failed |
|---|---|
| Whatever specific engine internals actually drive the performance/compression/query edge customers cite when they renew | Gate 2 — differentiating, by definition, until proven otherwise |
| Ops tooling: cluster management, upgrade automation, RBAC/multi-tenancy, backup/DR, monitoring integrations | Not a candidate at all — this is your emerging value-capture surface, the thing gate 3 needs |

*You haven't yet done the Sony-style split (media framework open, camera-effect recognition closed) on your own engine. That split is the actual Step 1 homework, and it's engineering + product work, not a licensing decision: name the specific mechanism — an index structure, a compaction strategy, a query planner heuristic — that is why a customer pays $4,200/core instead of using a competitor's now-free engine. Everything else in the engine is probably already context, especially now that two competitors have shown the market a free alternative exists.*

## Not yet

**The entire engine, as currently licensed, stays closed until two conditions are both true:**

1. The ops tooling (or an enterprise tier built on top of the open engine — multi-cluster management, compliance features, HA automation, premium support/SLA) has its **own price and at least a handful of customers paying for it as a distinct line**, proving customers will pay for it independent of the engine license.
2. The engine has been split into differentiating internals (stay closed, or open last, if ever) and commodity internals (open first).

Re-evaluation trigger: next planning cycle, or immediately if either competitor's open engine gains enough adoption that Halyard's proprietary engine becomes the outlier customers have to justify buying, or if a customer renewal is explicitly conditioned on open access (that would flip this to demand pull, a different and stronger case).

## Competitive case

*Fill in the two competitors' names yourself — this section is only real with them in it.* Generic version: a hyperscaler or either of your two now-open competitors forks your engine the day it's public and ships it as a managed service, at a fraction of $4,200/core, with more distribution than you have. What do you still hold?

- Today: **nothing.** The engine is the entire product. This is why gate 3 fails right now and why this is "not yet," not "open."
- After the ops-tooling line is built and priced: cluster operations at scale, upgrade/HA automation, compliance features, support SLAs, the trademark, and 38 existing relationships. A fork can run the code. It can't run your fleet-management story for a customer who already trusts you with production data.

If you open before that second column exists, you are giving away $6.1M of ARR-generating IP for nothing you can name — that is the definition of the wrong line in this skill's terms: move the asset (wait, build the second revenue surface), don't just retro-fit a license.

## Decision rights

- **Business call — should we open this, and when:** you, the founder. Given this is a single-product company where the decision reshapes the entire revenue model, this isn't delegable to engineering, however loud the internal push.
- **Compliance review — is it clean to open:** separate pass, before any announcement — check existing customer contracts for anything that constrains re-licensing or exclusivity (38 enterprise contracts at this ACV size often have IP or exclusivity language worth a lawyer's ten minutes), check copyright provenance on the engine code, and hand the actual license choice (MIT vs Apache vs a source-available instrument if you later decide the risk needs it) to `oss-license-strategy` — that's a separate decision from this one.
- Give the three engineers pushing for this a real role, not just a veto-by-attrition: name the most vocal one as the maintainer-designate for the eventual OSS project, with real allocated hours, once you're past "not yet." That converts a retention risk into the exact ownership gate 5 requires.

## Commitments

None to publish yet — you have nothing open. When you do move:

- Publish upstream-first as your engineering default before you publish anything else — a private patch to a public engine, re-paid at every release, is how the maintenance motive dies quietly.
- Whatever you open, commit publicly that it never moves back to paid. HashiCorp, Elastic and Redis each paid a fork-in-days price for narrowing an already-open line; don't create the conditions for your own version of that in eighteen months.
- Announce the boundary — which parts are open, which are the paid tier, and why — before the release, not after a customer or contributor discovers it.

## Operating model

Seven engineers total. Maintaining a public storage-engine repo — release review, issue triage, PR review, security disclosure — is a standing job, not a launch event, and it competes directly with the ops-tooling build you actually need to ship first. Before doing anything:

1. Name one owner and a real weekly-hours number for the eventual OSS engine (not "the team").
2. Write a one-page release checklist and a license-in policy — cheap, and the two artifacts the operating-model reference says a pre-scale company needs at minimum.
3. Don't start this while the ops-tooling pricing work is unstaffed — with 7 people, you can sequence this, not parallelize it.

Annual cost: not yet estimable without a named owner and hours/week — get that number before this goes to a board or investor conversation, or it gets cut mid-year and you're left with the exact abandoned-repository outcome this skill warns about.

## Measurement

Declared objective, once you move: growth in ops-tooling/enterprise-tier ARR, **not** downloads, stars, or adoption of the opened engine — adoption is the mechanism, the paid line moving is the signal. If in two years the engine has 10,000 GitHub stars and your ARR hasn't moved, the motive failed even though the launch looked successful.

## Bottom line — what to do this quarter

1. Do the internal split: name the 2–4 specific engine internals that are actually why customers pay $4,200/core today. Everything else is presumptively commodity, especially post-competitor-launches.
2. Price the ops tooling as its own line, even informally, with 2–3 existing customers, before touching the engine's license.
3. Tell the three engineers the real plan and the real timeline, with the most invested one given a named future role — this defuses the attrition risk without letting it write the strategy.
4. Put a date on "not yet" — pick the next planning cycle, and revisit with the split and the ops-tooling pricing signal in hand, not with the same three inputs you have today.