# Community Rule Contributions at Vaultmark — Contribution Model & Review Queue

## The premise needs correcting first

Your head of growth's plan treats the rule library like a plugin marketplace (Zapier, Slack apps). It isn't one. Two differences that change the whole design:

- **A bad plugin wastes a user's time. A bad compliance rule creates a false sense of security or a false compliance failure.** A false negative in a misconfiguration rule means a customer's environment looks clean to an auditor when it isn't — that's a liability event, not a quality complaint. A malicious rule (crafted to suppress a specific misconfig class) is a plausible supply-chain attack on your customers' security posture, not a hypothetical.
- **Network effects don't apply to correctness.** More users writing plugins makes a plugin ecosystem more valuable (discovery, variety). More people writing detection logic for the same misconfig doesn't make any single rule more correct — correctness is a supply-side quality problem, solved by testing and expert review, not by crowd size. Calling this a "network effects moat" is a category error. The actual moat you're selling is: *verified accuracy + compliance-framework crosswalk + weekly freshness + audit-defensibility.* None of that comes for free from an open commons — all of it requires the same curation function you're trying to eliminate.

So: don't open the marketplace to kill the review function. Open it to change what your reviewers spend time on — from *authoring from scratch* to *triaging and hardening other people's drafts*. That's a real efficiency gain. "Kills our biggest cost centre" is not.

## What actually stays proprietary

Structure the program so contribution flows *through* Vaultmark, never *around* it:

- Contributors submit rule **proposals** — logic, rationale, test fixtures. Submission is not publication. Nothing reaches a customer scanner without passing your pipeline.
- Every contributor signs a CLA assigning or exclusively licensing the shipped rule to Vaultmark. A published rule becomes part of your proprietary 1,900+ set, not an open repo a competitor can ingest wholesale. This single mechanism is what preserves the moat your growth lead is worried about losing — community effort in, but distribution rights stay yours.
- Compliance-framework mapping and severity assignment are never community-authored. That's the part carrying legal/audit weight, and it's also the part that's hardest to crowdsource credibly — keep it as an internal, named sign-off.

## Contribution model

**Who contributes, tiered by trust (two tiers, not more — per your own gates on scope creep, don't over-engineer this):**

1. **Verified contributors** — security engineers at paying customers, invited individually, under CLA + NDA. This is where you point the 6 customers asking for missing coverage. Fast-tracked review, priority queue.
2. **Open contributors** — anyone, public submission form. Full pipeline, no fast track, capped intake until the pipeline is proven (see rollout below).

**Incentives — recognition and product value first, cash only where it targets a real gap:**

- Attribution ("Rule authored by [name], verified by Vaultmark") — portable credibility for a security engineer's résumé, costs you nothing.
- Product credits / extended seats for shipped rules.
- Targeted bounty (fixed $ per shipped rule) specifically for the compliance-framework gaps your 6 customers already named — cheap relative to FTE cost, and it buys you exactly the coverage you're missing instead of undirected volume.
- No open marketplace payout structure yet. You don't have proof of the FP/FN rate at scale — don't build a payout model around an unvalidated pipeline.

## Review queue — five gates, each with an owner and an SLA

```
Submit → Auto-lint → Sandbox efficacy scoring → Human technical review
       → Compliance mapping & sign-off → Staged rollout → Promote or sunset
```

1. **Auto-lint (bot, minutes).** Schema conformance, does it execute, does it ship test fixtures, license/plagiarism check against known open rulesets (Checkov, OPA/Rego, Trivy policies) to keep contaminated or non-licensable logic out. Free to run, rejects most junk before a human sees it.
2. **Sandbox efficacy scoring (bot, under an hour).** Run the rule against your labeled benchmark corpus (known-good and known-bad configs). Score precision/recall. Set a floor — anything below it auto-rejects with a specific reason returned to the contributor, so they can fix and resubmit without opening a support ticket. This is your actual quality bar, and it's the one thing an open commons rule set can't replicate, because they don't have your labeled corpus.
3. **Human technical review (internal security engineer).** Logic correctness, edge cases the corpus didn't cover. This is cheaper than authoring from scratch, but it is not free — budget it explicitly, don't assume it nets to zero.
4. **Compliance mapping & sign-off (internal compliance specialist, never community).** Maps to the specific framework clause, sets severity. This is the liability-bearing step and the one your customers are actually paying for.
5. **Staged rollout.** Ship new rules first as advisory-only / non-blocking to a subset of tenants. Watch real-world false-positive telemetry for ~2 weeks before it can fail a customer's compliance attestation. Promote on clean data; sunset on a fixed SLA (e.g., pulled after 90 days without a maintenance update following a breaking cloud-provider API change) so stale community rules don't silently rot into false negatives.

Publish the rubric for stage 2's floor and stage 3's common rejection reasons up front — it cuts junk submissions the same way good docs cut support load, and it keeps the queue self-service instead of requiring hand-holding on every rejection.

## Fix the 6 customers now, separately from the marketplace

Don't wait on the pipeline above to close a demand gap you already understand. Log the six requests, prioritize by customer count × framework criticality, commit a next-cycle SLA, and — this is the actual pilot — invite those six customers' own security engineers into the "verified contributor" tier under CLA/bounty. You get the coverage, and you stress-test the review pipeline with motivated, already-trusted contributors before opening to the public.

## Sequencing

Curated-invite pilot (the 6 customers + a handful more verified contributors) → measure real FP/FN rates and reviewer hours per submission → only then decide whether to widen intake, and at what cap. Given this is a regulated/security product, don't skip straight to public open submission on the strength of a network-effects argument that doesn't actually apply to this asset class.