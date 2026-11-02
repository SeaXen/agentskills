# Distribution plan — harrowbase

One-shot plan (you asked for the deliverable, not a back-and-forth interview). Assumptions I made where your brief didn't say — confirm these before locking hours against them:

- **Ecosystem**: not stated. Assumed harrowbase ships as a library pulled into a host app via one or two language package registries (not a standalone binary users install directly) — "embedded" implies it's linked into someone else's process, not run as its own service. This assumption drives the biggest call in the plan (see Refused). If it also ships a CLI/server binary, tell me — that reopens downstream packaging.
- **Off-limits channels**: none given. Assumed none, except: don't name a bank or insurer publicly without their written sign-off — regulated companies almost always require it, and outing one kills the relationship that might convert.
- **Current baseline beyond downloads**: dependents count, cloners, referral sources — not given. Marked UNKNOWN below; that's itself a finding (an unmonitored surface), not a gap to guess at.
- **Do first, before anything below, costs ~1 hour total, zero dollars**: go back to the 4 engineers whose internal push died. Ask each one exactly which gate killed it — security review, legal/license, no vendor to sign a support contract with, no SBOM, no named security contact, budget, something else. Their answer decides whether this plan's trust-signal work (below) is actually the fix, or whether the real blocker is "no company behind this OSS project," which is a business-model question, not a distribution one, and no channel work fixes it. Do this in week 1; it's the cheapest, highest-signal step available and it should reweight everything after it if the answer surprises you.

## Position today

Audit findings, from `references/coverage-audit.md`, mapped to what's known and what isn't:

- **Registry metadata**: UNKNOWN — not audited yet. Run the field-by-field check (description, keyword slots, categories, license, links, rendered README, version state) this week. Score it as a percentage; anything under 100% outranks every item below.
- **Downstream packaging**: none known. Check Repology anyway — copies get created without upstream knowing.
- **Curated lists/directories**: UNKNOWN — search the project name plus "embedded analytics" and check what competitor projects are listed in; that list carries the whole category.
- **Dependents**: UNKNOWN — pull this from the registry's own "dependents" view or deps.dev before anything else in this plan gets acted on. It's the number that tells you if individual-developer adoption is already compounding into other projects (family 7) or staying flat.
- **Arrivals**: no channel-level data given. Qualitative signal is strong and real — unprompted docs praise, 40k monthly downloads with no marketing spend implied — but that's word of mouth among individual developers, and it is *not* the same signal as "an approver will sign off." Four independent stalls in regulated companies this year says the individual-adopter funnel and the company-adopter funnel are different problems with different failure points.
- **Baseline, 2026-09-24**: 40,000 monthly downloads (source/registry not specified — record it precisely during the audit); 2 maintainers; 4 stalled enterprise procurement attempts YTD (1 bank, 2 insurers, 1 logistics firm); Apache-2.0, permissive, no known licensing objection reported so far.

## Adopter

Both, sequenced — not a 50/50 split. Individual developers and small startups are the existing volume engine; don't touch what's working there. Company adoption is the declared growth story for next year, and it needs different work, not more of the same work.

The mechanism matters: this is not an awareness gap. Engineers already find harrowbase, use it, and love it enough to champion it internally unprompted. It's an **approver gap** — a person who never used the product decides whether it's allowed in, and can block it without ever being wrong on the merits. Geoffrey Moore's framing (Crossing the Chasm) is exact here: pragmatic buyers want peer references in their own segment, and right now harrowbase has zero visible references in bank/insurer/logistics-adjacent segments — every champion who tried is fighting from zero social proof. Larios Vargas et al. (ESEC/FSE 2020, 115 practitioners) found the highest-rated adoption factors are maturity/stability (62%), usability (55%), documentation (51%), license (45%), active maintenance (44%) — four of five are things this plan can make *visible* without touching code, since docs and license are already in good shape; the gap is proving maturity, active maintenance and support posture to someone who can't just read the README to decide.

## Foundation ring (weeks 1–6, ~18–20 hours total one-time, then well under an hour/release to hold)

Stretched from the skill's default 4 weeks to 6 — 20 hours/month combined is a real ceiling and this ring includes concentrated setup work that shouldn't crowd out everything else in month one.

1. **Debrief the 4 stalled deals** (above). ~1 hour. Do this before spending a single hour on the items below — it tells you if they're the right hours to spend.
2. **Registry metadata fix**: fill every field (description in the problem's vocabulary, all keyword/category slots, license, docs/repo/funding links, current version visible as default install). ~2–3 hours.
3. **Trust and procurement posture** (the core bet of this plan — highest expected leverage for the stated goal):
   - `SECURITY.md` with a named contact and a disclosure SLA.
   - Signed releases (Sigstore/cosign, or the language ecosystem's native equivalent).
   - SBOM (SPDX or CycloneDX) generated per release in CI.
   - OpenSSF Scorecard wired into CI, target score above 7.
   - A one-paragraph versioning/support statement in the README and on the registry page — what an approver looks for first and currently can't find without asking someone.
   - ~10–12 hours one-time (mostly GitHub Actions template wiring, not custom code), minutes per release after.
4. **Machine-readable surfaces spot-check** (family 10): confirm install instructions and versioned docs are structured enough for search/answer engines and coding agents to quote correctly. Docs are already strong, so this is a check, not a rebuild. ~1 hour.

Gate: don't open the test ring until items 2–3 are done. A stale metadata field undermines the exact legibility argument this plan is built on.

## Sequence

- **Weeks 1–6 (through ~2026-11-05)**: Foundation ring, above.
- **Months 1–4 (through ~2027-01-24)**: Test ring, below. Chosen to end 5–6 weeks before the funding decision, leaving February to package results into the deck rather than still be mid-experiment.
- **~2027-02-15**: freeze metrics for the funding narrative. Whatever's true then is what gets presented — don't keep changing the story past this date.
- **March 2027**: funding decision.

Triggers that reorder this plan:
- **A stalled deal restarts once trust posture ships** → that confirms procurement was the actual blocker; double down on legibility work, skip the integration test (T2) entirely and put those hours into closing the second and third reference.
- **The debrief in step 1 surfaces "no vendor to contract with" as the real blocker** → stop; this becomes a business-model conversation (dual licensing, a support offering), not a channel-mix problem, and no amount of SBOM work fixes it. Flag it back to whoever owns that decision immediately, don't spend the 20 hours discovering it slowly.
- **Downloads keep climbing but zero company-repo dependents appear by month 3** → the individual-developer funnel is healthy and isolated from the company funnel; don't add awareness channels, the awareness isn't the gap.
- **Regulated-industry fix-request pressure shows up** (EU CRA reporting obligations start September 2026, SBOM documentation enforceable December 2027 — binding manufacturers, expect it as demands relayed from downstream companies, not direct liability) → this validates the SBOM/signing work was worth doing now rather than later; don't take on more than a documented disclosure SLA.

## Test ring (months 1–4, ~2027-01-24 end date, ~6–8 hours/month)

- **T1 — Reference wall.** Get 1–2 named case studies from existing happy individual-adopter companies (small startups already using it in production, lower-stakes sign-off than a bank) live on the site, and re-approach the 4 stalled companies now that the trust posture exists — same product pitch, this time with an answer to "who's using this" and "what happens when it breaks." Cost: ~4 hours/month relationship work. Signal: at least one named or credibly-anonymized company logo live, and at least one of the 4 stalled deals re-opens. Kill date: 2027-01-24 — if none of the 4 has re-engaged and no new company reference exists, the trust-posture theory (this plan's central bet) is wrong or insufficient, and the debrief answers from week 1 need re-reading.
- **T2 — Integration surface.** Find the single highest-fan-in project harrowbase's users already run it alongside (a data pipeline tool, a BI layer, a specific web framework — whichever shows up most in your dependents once you pull that number) and pursue an official adapter or a "works with X" doc entry, offered upstream first. Cost: ~3–4 hours/month during the window. Signal: adapter installs, and at least one dependent that is a company-owned repository rather than an individual's.
- **T3 — One curated list**, not a sprint. Find the single most-browsed embedded-analytics or self-hosted-data-tools list, contribute something unrelated to it first, then submit. Cost: ~1 hour total plus a quarterly sweep. Signal: referral arrivals from that listing.

## Core channel

Decide at 2027-01-24 between: the trust-posture + reference-wall motion (T1), or the integration surface (T2), based on which one actually produced a company-owned dependent or a reopened deal. Default lean, given the evidence already in hand — four independent procurement deaths versus zero evidence yet that an integration would have saved any of them — is the reference-wall motion. Dependency position is the cheaper one to hold forever once earned (near-zero maintenance), so don't discard T2's finding even if T1 wins; a good T2 result becomes next year's core channel instead.

## Refused

- **System/distro packaging (Homebrew, apt, etc.)** — refused. The install unit is a library pulled through a language package manager, not a standalone binary; the entry cost is a policy review and it's irreversible once shipped, for a channel that doesn't match how anyone actually installs harrowbase today. Reopens if harrowbase ships a standalone binary/server mode that companies deploy directly — confirm this isn't already true.
- **Extension/plugin marketplaces, artifact/connector hubs (families 5, 11)** — refused as not applicable; harrowbase isn't an editor extension or a platform plugin. Reopens only if T2 targets a host platform with its own plugin catalog (e.g., a BI tool's connector marketplace) — then it folds into T2, not a separate line item.
- **Directory/listing sprint (10+ submissions)** — refused. At 20 hours/month combined, the quarterly sweep on more than 1–2 listings alone eats the budget, and a stale listing actively damages the exact company-adoption goal this plan serves. Reopens if capacity increases (a hire, a co-maintainer taking release engineering).
- **Recurring creator/newsletter seeding, started now** — refused until T1 and T2 both resolve. Cost is relationship work nobody but the 2 maintainers can do, and payoff stops the moment the pitching stops — wrong place to spend hours before the reference wall exists to pitch. Reopens as one dated, narrow push in January–February 2027 (1–2 relevant newsletters, not a campaign) — but only if T1 produces a real citable company reference by then. If it doesn't, skip it rather than force a pitch with nothing to show.
- **Publicly naming any of the 4 companies without their sign-off** — refused, permanently, not just for now. Reopens per-company only on their explicit written consent.

## Release rhythm

Commit to a maximum interval (propose 6 weeks) for ordinary fixes — never a minimum. Security fixes go out of band within 72 hours. Batch small changes into readable releases; every release ships notes (a distribution asset, not paperwork — dependency bots, packagers and "last published" liveness checks all read it). If a gap runs long anyway, an explicit "stable, maintained, low change rate" line in the README is the cheap fix for the liveness signal. Given the company-adoption goal, also decide whether to formalize a maintenance/LTS branch statement — this is exactly the kind of versioning promise the legibility argument above depends on, and it's a documentation decision, not new engineering.

## Review sweep

- First listing/package sweep: 2026-12-15.
- Metadata re-check: every minor release.
- Test-ring re-decision: 2027-01-24, with authority to kill T1, T2, or T3.
- Metrics freeze for the funding deck: 2027-02-15.
- Full plan re-decision: 2027-03-15 (post funding decision either way).

## Threshold check

- Sourced (stale listings fixed before new channel added): pending — no listings audited yet, gates test-ring start.
- Adopted bar (supply-chain score >7, green attestations), for company adoption in scope: pending — target set, CI wiring is a foundation-ring item, not measured yet. Do not sell this internally as a download driver — the evidence (OpenSSF Scorecard literature, Sigstore's own uncontrolled figures) supports procurement enablement, not growth. It's the fix for the four dead deals, not a marketing win.
- Registry metadata 100% filled: pending — audit not yet run.
- Recurring cost ≤60% of 20-hour capacity: ✓ by design — ~10–11 hours/month recurring once foundation work lands, leaving room for support load and the unplanned.
- Every channel has owner, hours estimate, named signal, review date, and no harmful-decay channel without a scheduled sweep: ✓ — built into this plan as written.

## What this plan deliberately doesn't do

It doesn't promise stars, downloads, or a viral moment — none of the evidence base supports trust work producing that, and pitching it that way sets up a credibility problem the next security question will pay for. It doesn't chase individual-developer growth further; that funnel already works and isn't the stated goal. It doesn't try to fix "no company to contract with" if that's what the week-1 debrief finds — that's a decision for whoever owns pricing/legal, not a channel to add here.

## Handoffs (not executed in this plan)

- Registry-page and README legibility copy → `readme-optimization`.
- Release notes format → `changelog-writing`.
- Family 10 execution (structured docs for search/agents) → `coding-agent-docs-optimization`.
- If T1 produces a real reference by Q1 2027 and you want a proper announcement moment around it → `oss-launch`, timed to the milestone, not before.
- Ongoing narrative between now and March → `build-in-public`.

**Next action**: send the 4 re-approach messages (step 1 above) this week — nothing else in this plan should get hours until those answers are in.