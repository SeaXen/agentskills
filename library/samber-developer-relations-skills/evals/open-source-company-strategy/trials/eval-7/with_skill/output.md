# Open source strategy — Ferro Queue

## Scope check

This is the macro call — what opens, why, who decides — not license text, governance of an already-open project, distribution/SEO, or the pricing model itself. Three things fall out of this brief and get handed off separately, after the line below is set:

- Apache-2.0 vs. MIT, and CLA vs. DCO → `oss-license-strategy`
- the announcement itself → `oss-launch`
- running the repos once they exist (release cadence, issue triage) → `oss-governance`

## What we sell

Self-serve access to the broker. A platform engineer finds it, runs it in a sandbox, and the company gets paid later without a sales call in between — the value capture is the broker engine itself (however it's packaged: license, subscription, or a future hosted tier), not the code around it.

## Company type and what that fixes in advance

Venture-backed, Series A. Three consequences, not open questions:

- the founder/CTO decide, effectively unilaterally — the board is being informed and is applying pressure for a timeline, but this isn't a board vote
- the default motive at this stage is distribution ahead of monetization
- reversal exposure is low today and gets expensive fast once something has adopters — which is exactly why the timing of this decision (before anything is public) is the cheapest moment you'll ever get to make it

Two things you told me are fixed constraints, not preferences, and they both narrow the field before any gate gets applied:

1. **Hard date** (board in three weeks) → rules out any line that needs a tiering matrix or a cross-functional sign-off process to stand behind. You don't have three weeks to build that; you have three weeks to make one clean call.
2. **Low irreversibility appetite, stated directly by the CTO** → this doesn't just rank a buyer-tiered open-core line lower. It removes it from consideration today, regardless of how attractive it looks on distribution grounds.
3. **One-off, not policy** — noted, and the commitments section below is written narrowly so it doesn't accidentally become one.

## Candidate lines (ranked)

**1. Interface-open — recommended.** Open the wire protocol and the official client SDKs under a permissive license (Apache-2.0/MIT). The broker engine, clustering/HA, and any RBAC/multi-tenancy stay fully proprietary. Self-serve sandbox trial is served by a free-to-download closed-source build of the engine — trial doesn't require open source, it requires low friction, and those are different things. Cost: roughly one engineer at a few hours a week. Reversal cost if this goes wrong: near zero, because nothing you'd ever charge for is in the release.

**2. Buyer-tiered open core — the strong alternative, deleted by your own stated constraint, not by weakness.** This is the line I'd normally push hardest for a message broker sold to platform engineers: infrastructure that sits in every service's critical path is exactly the case where engineers resist adopting something they can't read, and where GitLab's model (individual-contributor features open, buyer-persona features paid) earns real trust. I'm not proposing it. You told me, unprompted, that you want to be able to walk this back in a year — and this is precisely the line where walking it back is expensive. Once the engine ships under an OSI license and gets adopted, "walking it back" is the HashiCorp/Elastic/Redis playbook: a fork appears within days, and you've bought a public community-trust event, not a private do-over. That is the scenario your CTO is asking you to avoid, and this line manufactures it. Revisit it later — see "Not yet" below — once there's an actual revenue line and appetite has changed, not before.

**3. Fully closed, nothing published — rejected.** Zero irreversibility, but it doesn't serve the self-serve motion either: engineers evaluating a broker they can't inspect at all, with no public protocol to build integrations against, face the same trust friction that made Redis/Elastic/HashiCorp's later reversals so costly in the first place — you'd be adopting the downside posture without any of the adoption upside. Rejected outright, not just ranked last.

## Motive

**Commoditize your complement.** The product is the broker engine (what you bill). The complement is the integration surface — the protocol and the SDKs a platform engineer has to write against before they can even start a sandbox trial. Lowering that cost raises adoption of the thing you charge for; it does not raise adoption of the SDKs for their own sake. Spolsky's own failure case (Sun opening Java, commoditizing hardware — the thing it sold) is the warning not to open the engine by mistake.

Evidence test, honestly stated since nothing has shipped yet: this is a hypothesis, not a validated fact. Watch, over the first two quarters after the SDKs ship, whether integration effort shows up as a stall reason in trial-to-paid conversion, and whether it drops. If it doesn't move, the motive isn't materializing and the ongoing SDK maintenance cost should be re-questioned — not the recommendation itself, since the downside was already priced at near-zero.

Rejected as the primary motive: **external demand pull** — no customer, regulator, or platform owner is requiring this; the board wants a decision, which is pressure, not a mandate, and refusal costs you nothing today. **Trust and auditability** is a plausible secondary effect (infra buyers who've watched Redis/Elastic/HashiCorp do care about this) but isn't being claimed as primary — you have no deal or audit today where source access was actually the blocker.

## Open

| Asset | Motive served | G1 — irreversible | G2 — differentiating/context | G3 — value capture once opened | G4 — contributable | G5 — owner |
|---|---|---|---|---|---|---|
| Wire protocol spec | Commoditize the integration complement | Permanent, and fine — a spec has no resale value on its own | Context/enabler | Broker engine, brand, and (later) hosting still capture value; nothing here is what you sell | Yes — third parties can implement against a published spec | **Needs a name and an hours/week commitment before the board meets. This gate is a veto — do not ship without it.** |
| Official client SDKs (start with 1–2 languages, not the full matrix) | Same | Fine — SDKs are commodity and trivially reimplementable by anyone regardless of your license choice | Context/enabler | Same | Yes — new-language ports and bug fixes are the standard first contribution | Same owner as above, or a named second person |

## Closed

| Asset | Gate failed | Why |
|---|---|---|
| Broker engine (core server) | **G1 (irreversibility)** — decisive on its own given your stated appetite | Run the test: "if this can never be closed again, does the decision change?" Yes, sharply — you'd forfeit the ability to gate clustering/HA behind a paid tier, and you'd inherit the exact fork-within-days exposure that HashiCorp, Elastic, and Redis each paid for after they'd already built a community around the open version. You have none yet, which is the cheapest possible moment to keep this closed, not the moment to test the waters. |
| Clustering, HA, multi-tenancy, RBAC | G1, and G3 | Same irreversibility problem, plus this is where your future paid tier is expected to live — opening it now spends the value-capture surface before you've built any other mechanism (hosting, support, brand) to replace it. |
| Admin/observability console | G3 (bundled) | No standalone reason to open a thin UI layer; ships with the paid product. |

## Not yet

| Asset | Condition that flips the verdict |
|---|---|
| Buyer-tiered open core on the broker engine | Revisit once there's a real revenue line, a support motion, and — critically — a change in the risk appetite stated in this brief. Also revisit early if a direct competitor ships a fully open broker engine in this exact space and buyers start refusing closed cores outright; that's the promotion condition this skill would normally apply to a dev tool sold to engineers, and it's the one thing that could override the constraint above. |
| Protocol conformance/test suite | Open once a second implementation exists — yours plus a partner's, or a community reimplementation — to test against. No second implementation yet means no contribution viability (gate 4), just unpaid publishing cost. |

## Competitive case

Named threat: a hyperscaler (AWS/GCP/Azure) or an incumbent broker vendor launches a managed or protocol-compatible service. Under this line, what they could take is the protocol and the SDKs — both already designed to be commodity, so losing exclusivity on them costs you nothing you were charging for. What you still hold: the broker engine's source, any future hosting/ops advantage, the brand and trademark on "Ferro Queue," and the support relationship. Nothing licensed away is something a hyperscaler could resell as a competing broker, because the broker was never released. Verdict: acceptable — and notably, this is the one place where the recommendation and the "walk it back in a year" instruction agree completely, since there's nothing here to walk back.

## Decision rights

- **Business call (should we do this):** CEO and CTO jointly — stated as shared already, no need to invent a committee for a three-week deadline.
- **Compliance review (is this okay to release):** outside counsel, in parallel, on exactly three things: license text choice (hand to `oss-license-strategy`), a trademark check on the "Ferro Queue" name before the repo goes public, and a secrets scan on the SDK/protocol repo history before the first push.
- **Escalation:** any future proposal to open the broker engine itself returns to this same CEO+CTO pairing — it does not get decided by an individual engineer shipping a "just the SDK" PR that quietly grows scope.

## Commitments

Published alongside the release, scoped narrowly on purpose:

1. Versions of the protocol spec and SDKs already released under Apache-2.0/MIT will not be re-licensed away from an OSI-approved license.
2. Opening the protocol and SDKs is not a commitment to open the broker engine. Say this explicitly — otherwise the market reads more into it than you decided.
3. If a future decision opens the broker engine, it will be announced in advance, with the reasoning, not shipped as a surprise. (This is the Docker lesson: they withdrew no code and changed no license, and still took the full reputational hit — governance surprise is priced on its own, independent of scope.)
4. This decision governs the broker's protocol and client libraries only. It sets no precedent for any future Ferro Queue product.

## Operating model and cost

- **Owner:** one named engineer, ~3–5 hrs/week to start (SDK maintenance across 1–2 languages, protocol doc upkeep, issue triage). Name them before the board meets — this is gate 5, and it's a veto, not a nice-to-have.
- **Release checklist:** license file + NOTICE, security-contact address, secrets scan on repo history, trademark note in the README (the code's license doesn't imply the name/logo are licensed the same way).
- **Contribution policy:** lightweight DCO, published on day one so early interest doesn't stall waiting on paperwork.
- **Legal:** a few hours of outside counsel on license choice and the trademark check — cheap, since Apache-2.0/MIT are boilerplate.
- **No foundation membership, no review board, no dedicated program office at this stage** — two small public repos don't need Series-A-stage machinery beyond one named owner.
- **Annual cost, rough order:** low five figures in engineering time. State this number to the board as the actual cost of the decision, not just the license choice — a cost nobody added up is the cost that gets cut mid-year, which is how repos end up abandoned.

## Measurement and re-evaluation

- **Objective for the open assets:** trial-to-paid conversion of the broker itself improves, and integration friction stops showing up as a stall reason in the pipeline. Not SDK downloads or GitHub stars — those measure the wrong thing for this motive.
- **Re-evaluation trigger:** your next planning cycle, or immediately if any of: a direct competitor ships a fully open broker engine, a prospect explicitly blocks purchase pending source access to the engine itself, or the SDKs draw zero external interest after two quarters (signal to shrink the maintenance spend, not to reopen the engine question).

## Check against the pass threshold

Passes: every asset appears once, one motive is named with its evidence test stated honestly (including where the evidence doesn't exist yet), value capture is a mechanism (engine + brand + future ops, not "the license"), the adversarial scenario names a real competitor class and states what survives, a named role decides with compliance reviewing separately, and a commitment is published that the company won't walk back.

Open before the board meeting, not after: **the named owner and their hours/week** for the SDK/protocol repos. Everything else in this brief is decidable today; that one field is a veto on shipping, not a detail.