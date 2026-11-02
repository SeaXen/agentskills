## Bottom line

❌ Don't open a public rule marketplace. The rule library is not a complement here — it's the product you sell. Making it free and community-authored commoditizes your own core, not a supporting layer. Gate G4 fails, worst direction, same failure shape as the declined case in this skill's own reference examples.

✅ Do this instead: (1) ship a private, per-tenant custom-rule extension point to close the six-customer gap now, (2) pilot a narrow, invite-only rule-intake channel that feeds your own curated library — not a public marketplace, no revenue share, you keep editorial control. Below is the full decision memo and the concrete structure for both.

---

## Hypothesis (tested against growth's pitch)

Forced into the skill's required shape, growth's pitch reads:

> Because customers need **rules we don't cover** that we will not build, **security engineers** will build them on **a public marketplace**, earning **reputation**, which makes our product more valuable to **platform teams** by **wider coverage**.

Two blanks stay vague: builder ("security engineers" names no organization with its own reason to build) and return ("reputation" is not an economic actor's incentive). This is the exact shape of a hypothesis this skill's own worked examples send back before evaluating anything else.

**Commoditized complement check (G4) fails on top of that, independent of the vague blanks**: you told me the rule library is "the thing customers actually pay for." An ecosystem is supposed to commoditize a *complement* so demand for your *core* rises. Here the proposed giveaway *is* the core. Abundance of free community rules doesn't sell more scanner — it removes the reason to pay Vaultmark specifically, since free CSPM rule sets already exist in the wild (Checkov, tfsec, Prowler, ScoutSuite, OPA/Rego policy sets). You'd be donating your moat into a space a bigger, better-funded open project or CNAPP vendor can absorb faster than you can build exclusivity around it (envelopment risk, G6).

## Gates

- 🔴 **G4 commoditized complement** — FAIL, worst direction. Rule library is the paid core, not a complement. Decisive on its own.
- 🔴 **G3 identified builders** — FAIL. No named organization or team with its own business reason to build has been contacted. "Security engineers" is a persona, not a builder.
- 🔴 **G6 envelopment** — FAIL. Free, community-sourced misconfiguration rules already exist as open-source projects and inside hyperscaler-native tooling. Nothing about donating rules publicly is non-generic to Vaultmark.
- ⏳ **G1 counted demand** — UNKNOWN. Six customers asked for missing rules, but not itemized: same gaps repeated, or six unrelated one-offs? Resolver: pull the six tickets, tag by cloud provider + compliance framework + control ID, check overlap. Owner: head of product. Date: 2026-10-04.
- ⏳ **G2 externalizable interfaces** — UNKNOWN. Is the rule schema/DSL stable enough to expose to customers today, even privately? Resolver: engineering assessment of rule-schema stability. Owner: eng lead. Date: 2026-10-18.
- **G5 staffing** — not separately evaluated; see cost-centre correction below, it's the real number that decides whether even the narrow pilot is worth running.
- **G7 complement readiness** — not evaluated. G3, G4, G6 already decide it, same as this skill's own declined-case precedent.

## Why "kills our biggest cost centre" is wrong

Authoring a rule is not the expensive part. Verifying one is: confirming it fires correctly against real (not toy) configs, confirming its mapped compliance control is legally/audit-defensible, and re-testing it as cloud provider APIs shift weekly. That verification requires the same security expertise your internal analysts already have. A community marketplace does not remove that cost — it relocates authorship to unpaid volunteers while leaving your analysts on the hook for the exact same review work, now arriving in unpredictable volume from people with no obligation to fix a rule when it breaks. Before anyone signs off on "this saves cost," size it: analyst-hours to verify one submitted rule vs. analyst-hours to author one in-house. Nobody has measured this yet — treat it as unknown, not settled.

## Rung — chosen and rejected

**Chosen: stay at rung 2 (vendor-built) for the core library**, plus **rung 4 (in-product extension points)** for the immediate customer gap.

- Rung 4 fits exactly: the skill lists "rules" as a canonical rung-4 example. Customers' own internal teams need behavior changed inside your product (their own coverage gap), not a public good shared across your whole customer base. When the only positive economic actor is the customer's own internal team, that's a rung-4 case, not a rung-5/marketplace case — which is exactly the situation here, since G3 has no other builder archetype identified.

**Rejected:**
- Rung 3 (partner-built, listed) and rung 5 (installable apps) — no named builder archetype exists yet (G3 fail); premature.
- Rung 6 (runtime platform) — nothing here needs your execution context; not in play.
- Public marketplace as growth described it — this isn't on the ladder at all in its "anyone, free, public" form; the closest the ladder gets is rung 3, which still requires listing standards, a review pass, and partner contracts you'd be held to. Growth's version has none of that scaffolding and fails G4 regardless.

## Structure: what to actually build

**1. Extension point — private custom rules (ship this, solves the 6-customer ask now)**

- Publish a stable rule schema/DSL customers can author against, scoped to their own tenant only. Their rules never leave their account, never touch other customers, never enter your paid library automatically.
- Safety boundary: custom rules run in the same sandboxed evaluation path as your own, can't execute arbitrary code, can't read other tenants' data.
- Stability commitment: version the schema from day one, 90 days' notice on breaking changes to it — this is the obligation you're taking on, name an owner now (eng lead).
- This is fully reversible and cheap. It does not touch your moat, because nothing here is shared or public.

**2. Rule-intake pilot — narrow, invite-only, not a marketplace**

If you want to test whether outside contribution genuinely lowers cost (rather than assume it), run this as a bounded pilot:

1. **Access**: invite-only. Start with the six requesting customers' engineers, hand-picked — not a public submission form. This is the skill's own "recruit a founding cohort by hand" pattern, scoped to people who already have a reason to want the gap closed.
2. **Submission format**: your schema only, never freeform code — this is what makes review tractable and keeps arbitrary logic out of customer cloud accounts. Required with every submission: target service, provider, the specific compliance control claimed (framework + control ID), a known-bad config fixture, a known-good config fixture, rationale.
3. **Automated gate before any human touches it**: schema validation, fixture pass/fail, duplicate check against the existing 1,900, a heuristic flag for overly broad matches (false-positive risk).
4. **Human review** — same analyst tier that authors your rules today, not a junior triage role: correctness beyond the two fixtures, compliance-mapping accuracy (this is your audit/legal exposure if wrong), false-positive estimate, assign a maintenance owner before acceptance.
5. **Outcome**: accept as-is, accept-with-edits (your analyst reworks it — treat submissions as drafts, not merges), or reject with a stated reason (duplicate / too narrow / false-positive risk / unverifiable compliance claim).
6. **No two-tier trust label.** An accepted rule joins the same weekly-maintained library as everything else, same guarantee. Showing customers a "community, unverified" badge undercuts the exact compliance-grade trust they're paying for.
7. **Contributor terms**: submission assigns the rule to Vaultmark (or dual-license), zero revenue share — per this skill's own pricing principle, don't tax or pay out before you know there's real, repeatable supply. Reward is non-monetary: public credit, early access to new rule packs, a private advisory-channel invite.
8. **Track one number that settles the debate**: analyst-hours per accepted external rule vs. analyst-hours per internally authored rule. Run it one full quarter before scaling access past the founding cohort.

## Measurement

- Baseline today: 0 customer-authored custom rules, 0 external submissions, 6 open coverage requests.
- Target: custom-rule extension point live and used by at least 3 of the 6 requesting customers within one quarter of ship.
- Pilot intake (if run): submissions per quarter, acceptance rate, analyst-hours per accepted rule vs. in-house baseline — this last number is the actual test of growth's cost-centre claim.

## Kill / reopen criteria

- **Kill the extension point** if fewer than 3 of the 6 requesting customers use it within one quarter of ship — the gap wasn't the blocker growth thought it was.
- **Don't scale the intake pilot past the founding cohort** unless analyst-hours per accepted external rule comes in below in-house authoring hours for two consecutive quarters — if not, it's not cheaper, it's just outsourced review with extra steps.
- **Reopen the full marketplace question** only if: eight or more distinct rule gaps get requested by five or more customers (this skill's own default threshold), or a named security vendor/consultancy asks in writing to publish rules for referral value (real G3 evidence, not a persona). Review date: 2026-12-15. Owner: head of product.

## Next action (2 minutes)

Pull the six customer tickets and tag each by cloud provider, service, and specific compliance control requested. That single list resolves G1 and tells you whether this is one real gap or six unrelated ones.