# Distribution plan — slatevane

**First action:** open npmjs.com/package/slatevane. Check description, keywords, links. Do this today — costs 5 min, tells you if audit below finds real gaps.

**Reality check, upfront:** your 3-ask wishlist (quarterly newsletter + 2 integrations + 3-4 lists) costs more than 3 hours a month, forever, solo, can pay. Below is the version that fits. Newsletter push refused for now — reason in Refused section. One integration, not two. Lists: yes, as asked.

**Assumptions** (no interview run — task asked for direct deliverable; flag these, correct if wrong):
- Goal = grow adoption (downloads, dependents). Not funnel, not hiring signal, not commercial.
- No deadline, no 1.0/rewrite/conference on the calendar.
- Compounding preference (ties to "forever" in your ask), not one-off spike.
- No off-limits channels stated.
- No web access this session — audit below is a checklist for you to run, not a completed audit. Only confirmed number: 900 weekly downloads, individual devs, no other data.

## Position today

Confirmed: 900 weekly npm downloads, individual devs, dated 2026-09-24.

Unknown — run this 20-min checklist, one time, before touching anything else:
1. npm page: description matches current positioning? All keyword slots used? Links present — repo, docs, homepage, funding?
2. GitHub: topics set? Social preview image set? README states value prop above fold?
3. Dependents count (GitHub Insights → Dependency graph → Dependents, or npmgraph.js.org).
4. Any existing list/directory listing you forgot about? Search "slatevane" + "form state" on Google.
5. Last release date. Longest gap between releases in past year.

Expect 2 findings, per this skill's own pattern: one half-filled metadata field, one or two things quietly wrong. Fix before adding anything new — this is the cheapest work that exists and outranks every channel below.

## Adopter

Individual only, confirmed. Optimize for: registry findability, one-line install, presence in lists that ecosystem actually browses, zero-friction defaults. Not optimizing for: procurement legibility, SBOM, signed releases — company adoption isn't the goal, so skip that whole family.

## Foundation ring — weeks 1-4, ~4 hours, one-time

1. **npm metadata** (~1 hr): rewrite description in plain problem language ("form state", "TypeScript", "validation" — not invented branding). Fill all keyword slots. Add docs/funding links if missing.
2. **GitHub surface** (~1 hr): set topics (form-state, typescript, state-management, form-validation, react — whichever apply). Social preview image. README: value prop in first screen, real badges only (npm version, downloads, license, CI) — badges don't drive growth, they're legibility, not a lever.
3. **Trust minimum** (~1 hr): confirm LICENSE present and correct. Add short SECURITY.md with a contact. One line in README: "actively maintained, releases within N weeks." Cheap, hits license (45%) and active-maintenance (44%) — the two things developers say they check, per published survey data, even for individual adoption.
4. **package.json fields** (~30 min): `exports` map, `types`, `sideEffects` correct. This is the whole machine-readable-surface budget for now — deeper agent-doc work is a separate skill, not worth spending hours on yet.

Total: ~3.5-4 hrs. Spend across first month, don't spread thin.

## Sequence

**Stage 1 (Oct 2026):** Foundation ring above.

**Stage 2 (Nov 2026 – Feb 2027), curated lists, ~2-3 hrs total, then 15 min/list/quarter:**
- Target 3-4 lists real developers browse in this category: TypeScript-ecosystem "awesome" sub-lists, form/state-management comparison pages, framework-specific resource pages. Don't guess URLs blind — search "awesome [category]" and check last-merged-PR date before targeting one.
- Read each list's contributing.md. Match its entry format exactly — format failures get rejected before the project is even judged.
- Make 1-2 unrelated contributions (dead-link fix, typo) to each list before submitting slatevane. Improves odds, costs little.
- Submit 1 list a month, not all 4 at once — keeps it inside budget, avoids submission fatigue burning your only hours.

**Stage 3 (Mar–Jun 2027), ONE framework integration, ~10-15 hrs entry, spread over 4 months:**
- Pick ONE adapter, not two. This family's cost is "high and recurring per integration" — a second adapter doubles your permanent maintenance surface, and unbounded adapter sprawl is the named trap for solo maintainers.
- Decide which framework by evidence, not guess: check your own GitHub issues/discussions for "does this work with X" requests. Whichever framework users already ask for, build that one first.
- Ship it, get it merged/linked from that framework's own docs or examples if possible — that's the actual payoff, not the package existing standalone.
- Hold cost after shipping: ~0.5-1 hr/month (version bumps, occasional compat fix). This becomes your main recurring line item going forward.
- Second integration: not before 2028, and only once the first one's upkeep is proven to fit inside budget for a full year.

## Test ring

Empty by design. At 3 hrs/month, running 2-3 parallel time-boxed experiments alongside foundation work isn't affordable — this skill's own guidance for tight capacity is to skip the test ring, not shrink it. The one real bet you're making is the integration choice in Stage 3; its own kill condition (below) serves as the experiment.

## Core channel

None chosen yet. Capacity doesn't support sustaining a channel beyond foundation + list upkeep + one integration hold. Revisit if monthly hours ever grow, or once Stage 3 proves out — if the integration clearly outperforms everything else, it becomes the core channel by default, not by new spend.

## Refused

- **Quarterly newsletter/podcast seeding** — refused for now. Highest recurring-cost family of all eleven, ranks last on efficiency. A single honest pitch already costs ~1.5-3 hrs; a real quarterly cadence eats your entire monthly budget and starves lists + integration. Rule this plan follows: promote creator seeding only at a dated milestone, once foundation + passive discovery already hold. You have neither yet. **Reopens when:** a real milestone lands (1.0, notable rewrite) worth pitching, OR monthly hours grow past ~3, OR someone else (co-maintainer, volunteer) takes the relationship work.
- **Second framework integration** — deferred, not refused outright. **Reopens:** 2028, after first adapter's maintenance load is proven sustainable for a year.
- **Trust/procurement work beyond the minimum** (SBOM, signed releases, Scorecard chase) — refused. No evidence this drives downloads; it's procurement enablement, and you have no company-adoption goal to enable. **Reopens:** if a company user files an issue asking for it, or company adoption becomes an explicit goal.
- **Downstream packaging** (Homebrew, distro repos) — n/a. Library installs inside node_modules, not as a standalone binary. Permanent packaging cost for zero benefit.
- **Extension/connector marketplaces** — n/a. No editor extension, no connector product.

## Release rhythm

Maximum interval: fix lands within 6 weeks. No mandatory minimum — don't ship empty releases just to look active. Batch small changes into one readable release. Security fixes: out of band, fast. Changelog owner: you, folded into normal maintenance time, not extra distribution budget — it's dual-purpose already. If a gap runs long, the README's "actively maintained" line (foundation ring) is the cheap correction; don't spend extra hours reassuring anyone beyond that.

## Review sweep

Quarterly, 1 hour, first sweep **2026-12-15**: recheck the 3-4 list entries still resolve and describe you accurately, recheck npm metadata hasn't drifted, recheck integration adapter still builds against latest host-framework version, re-measure downloads/dependents against baseline. Kill anything producing no signal.

## Threshold check

- Sourced bar (stale listings fixed before new channel added): **pending** — depends on you running the Position-today checklist first.
- Registry metadata 100% filled: **pending**, fixed in foundation ring week 1.
- Recurring cost ≤ 60% of 3 hrs/month = ≤1.8 hrs/month: **pass by design** — steady state (list sweep ~0.33 hr + integration hold ~0.5-1 hr + quarterly review ~0.33 hr) lands around 1.1-1.7 hrs/month once Stage 3 ships, leaving slack.
- Every channel has owner/hours/signal/review date: **pass** — owner is you throughout, dates given above.
- Supply-chain score >7: **not pursued** — individual adoption only, no procurement gate to clear.

**Next:** run the 5-item Position-today checklist above. Takes 20 min, tells you exactly which foundation fixes are real vs already done.