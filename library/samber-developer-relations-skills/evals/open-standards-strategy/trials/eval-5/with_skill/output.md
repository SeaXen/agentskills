# Standards decision: OpenLedgerFeed vs. LedgerWire

**Date:** 2026-09-24 · **Owner:** _(name the exec who owns this — not "the team")_ · **Review:** +90 days from Track A ship date

## The one-line verdict

Three features and a marketing push do not fix this. The thing stalling deals isn't a feature gap — it's that **LedgerWire reads the legacy CSV convention every ERP already emits, and OpenLedgerFeed doesn't.** That single fact reclassifies this as a fight you're structurally losing, not a fight you're behind in on shipping velocity. Fix that fact first. Everything else is secondary.

## Landscape

| | OpenLedgerFeed (yours) | LedgerWire (Marrowcast) |
|---|---|---|
| Independent implementations | 6 | 5 |
| Publisher | Nordhall | Marrowcast |
| Reads legacy CSV drop convention | No — requires integration rewrite | Yes — native |
| Conformance suite / cert mark | Not stated — assume absent | Not stated — assume absent |
| Named counted demand | "Every enterprise deal since April" — needs actual names/count | — |

Three things to confirm before this record is final, flagged rather than assumed away:

- **"6 independent implementations"** — confirm none are Nordhall's own SDKs across languages recounted as separate implementations. That's the same inflation trick as counting your own reference implementation twice, and it's the first thing a skeptical buyer or a Marrowcast rebuttal will check.
- **What Nordhall actually monetizes.** If you sell tooling/platform on top of the event-stream layer, standardizing that layer is correctly a commoditization *win* — more implementations means more deals for what you actually charge for. If you sell the format's own implementations directly, your ceiling on this ladder is Extend, not Drive, and the plan below changes. Everything past this paragraph assumes the former, because pushing "adoption numbers" as your KPI only makes sense if adoption of the *format* is the asset, not the product.
- **Neither spec's IPR/venue is stated.** If OpenLedgerFeed is currently just "a spec Nordhall publishes" with no separated legal layer, that's a real gap once this goes to Step 4 below.

## Classify the fight before picking a tactic

Per Shapiro & Varian's four battle types: classify by which side is backward-compatible with what's already installed.

- Marrowcast is compatible with the installed base (the legacy CSV convention every ERP integration already emits).
- You are not (you require a rewrite).

**That's Revolution versus Evolution, and you're the Revolution.** The framework's own reading of this cell: you're asking adopters to pay a switching cost the incumbent isn't, so you need performance "compelling" enough that they accept it anyway. Absent that, the compatible side wins slowly by default — not because it's better, but because it's cheaper to say yes to.

Three generic features don't clear that bar. They're not compelling enough to justify a rewrite on their own; they're normal roadmap. Meanwhile the buyers who are "waiting to see which one wins" aren't waiting for either of you to ship faster — the "waiting to see which wins" language is the textbook fragmentation signal, the same one OpenTelemetry's own framing named directly: with two credible specs for one job, the benefit customers want is consolidation, not a feature.

So the board's plan attacks the wrong variable. It spends a quarter of engineering on a knife fight over feature count while the actual blocker — a rewrite cost that only one side is asking for — sits untouched.

## Decision

**Posture: keep Driving OpenLedgerFeed, but change what you ship and open a truce channel in parallel.** Don't pick one; run both, because they hedge each other — the compatibility fix protects you even if Marrowcast never responds, and the truce channel, if it lands, ends the stall faster than any roadmap can.

### Track A — kill the switching cost, not the feature gap (this replaces the board's "3 features")

Ship a CSV-ingestion bridge for OpenLedgerFeed: existing ERP integrations emit the same legacy CSV drop they already emit today, and it maps into OpenLedgerFeed events without a rewrite on the integrator's side. This is the one feature that changes the battle classification — it moves you from Revolution (pay a switching cost) toward Evolution (compatible, minimal adoption cost), which is the only lever the framework says works against an incumbent playing the compatible side.

If the board wants three shipped things next quarter, make them:
1. The CSV bridge (the one that matters).
2. A versioned conformance mark + public registry (see Track C) — cheap, and neither spec has one yet, so it's uncontested ground.
3. One genuine differentiator on top of interop, positioned as Extend, not as parity — something Marrowcast's CSV-native design structurally can't match, if one exists. If it doesn't exist, ship two things, not three padded to hit a number.

### Track B — open a truce conversation with Marrowcast, from strength

This is the direct answer to "every deal has stalled since April": the stall is fragmentation, and fragmentation's own cure — per the OpenTelemetry precedent — is consolidation, not victory. "The main benefit to the ecosystem is the consolidation itself, not some specific and shiny new feature."

Approach this while you hold the better hand, not after: 6 named independent implementations against 5 is leverage at the table, and "one's strength in battle is an overriding consideration when meeting to conduct truce talks." Waiting until Track A ships and the compat gap closes only strengthens that hand further.

Shape a truce offer like the OpenTelemetry merge, not like a surrender:
- Bridges preserving compatibility with both predecessors — including your own new CSV bridge, which becomes the on-ramp for the merged spec too.
- A dated end to parallel development.
- The merged spec positioned as the next major version of *both*, not a third option and not "Marrowcast adopts our format."
- Joint governance seated with both sides from day one.

Price this honestly before proposing it: it costs you the "we won" narrative and some unilateral roadmap control. It buys the only thing actually blocking revenue right now — unblocked deals, on both sides, immediately.

**Kill rule for Track B:** if Marrowcast doesn't engage within 60 days of a real outreach (not a press release — a direct conversation), stop waiting on it. Proceed on Track A alone, and don't let the door being unanswered turn into a standing distraction. Revisit only if a specific new trigger appears — e.g., a shared customer names both specs in one RFP.

### Track C — ship the conformance mark first, since neither of you has one

Neither spec has a test suite or certification mark. That's a "paper standard" risk on both sides — every implementer can claim support and buyers can't verify it, which is a second, quieter reason deals are stalling on top of the fragmentation story. A versioned mark + a public registry of certified implementations gives procurement a checkable claim instead of a vendor's word, and it's cheap: self-service, free, one maintained page. That directly serves the buyer who says "waiting to see which wins" — it gives them a way to de-risk adopting yours today instead of waiting for the market to settle on its own.

### Track D — reframe the marketing push, don't cancel it

"Adoption numbers" marketing is legitimate — Shapiro & Varian call expectations management a real tactic, not spin, as long as the numbers are real. Two conditions before it goes out:
- Numbers must be named and independently verifiable (confirm the "6" first, per the landscape flag above) — a number that doesn't survive a rebuttal is worse than no number.
- Lead with the compatibility fix once it ships, not with feature count. "Now reads your existing CSV drop, zero rewrite" answers the actual objection sitting in every stalled deal; "three new features" doesn't.

## Venue and IPR — only relevant if Track B lands

If a merge gets traction, recommend hosting the combined spec as a Git-based community specification or a foundation-hosted consortium (the OpenTelemetry path), not a heavier body — speed matters more than formal neutrality at this stage, and foundation hosting still buys enough credible neutrality to kill the "one vendor controls this" objection from both companies' existing champions. Default the IPR mode to royalty-free: nothing in this brief suggests either side monetizes patents here, and royalty-free is what keeps every existing ERP vendor's own tooling able to implement it. This is a charter-time decision — write it down before anyone drafts governance text, because it isn't revisable without re-chartering later.

## Staffing

Name one owner for Track A (engineering) and one owner for Track B (whoever has the standing relationship or can get one with Marrowcast — likely not the same person). Track A is a quarter of engineering time, already inside the board's stated budget. Track B is hours per week of a senior person's time, not a team.

## KPIs and kill rule

| Metric | Threshold | Sourced or baseline | By when |
|---|---|---|---|
| Stalled deals unblocked after CSV bridge GA | ≥ 50% of the named-stalled cohort | Baseline — set from this market's own sales cycle, replace with your real number | One quarter post-GA |
| Marrowcast engagement on truce outreach | Any substantive response | Baseline | 60 days from outreach |
| Independent implementations, either spec | Track growth, not just the current 6-vs-5 snapshot | Sourced floor: 2 independent interoperating implementations is IETF's own bar (RFC 6410 §2.2) for calling a spec real — you're already well past it; the number to watch now is growth rate, not the floor | Ongoing, reviewed quarterly |
| Conformance suite adoption | Every implementation claiming support has passed | Baseline | 6 months from suite launch |

**Kill rule:** if the CSV bridge ships and stalled-deal conversion doesn't move within one quarter, the switching-cost theory was wrong or insufficient — escalate to the board for a real go/no-go on continued independent Drive versus a formal Co-found overture through a neutral foundation, rather than shipping more unrelated features on the same losing axis. If Track B produces a truce, your obligation to the 6 existing OpenLedgerFeed implementers is a named migration path and a bridge to the merged spec — not a silent sunset. Whoever owns a spec owns the migration off it.

## What this rejects, and why

- **"Ship 3 features + market the adoption numbers," unmodified** — rejected because it doesn't touch the mechanism causing the stall (a rewrite cost only your side imposes) and risks losing a full quarter while, per the framework, the compatible side wins slowly by default anyway.
- **A pure feature/performance race (Revolution, doubled down)** — rejected because "compelling enough to justify a rewrite" is a high bar three incremental features almost certainly don't clear, and the brief gives no evidence they would.
- **Doing nothing and waiting for Marrowcast to blink** — rejected because "waiting to see which wins" is buyer language for "neither of you is winning," and every quarter of stall is revenue neither side gets back.