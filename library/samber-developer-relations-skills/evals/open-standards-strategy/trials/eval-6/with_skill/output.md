# Standards decision: Dataset Lineage Handoff Manifest ("the Spec")

Date: 2026-09-24 · Owner: Caldmere engineer — **not yet named, see gap below** · Review: 12 months post-v1

## Landscape

- **No spec both peers have agreed on covers this job today** — you're co-founding from scratch. Before locking that in, close one open question in parallel (it does not change the venue/IPR answer below, so it doesn't block Thursday): check whether OpenLineage, an existing lineage-interchange spec hosted at LF AI & Data (a Linux Foundation umbrella — confirm current details before citing to peers), is already 80% of this job. Two credible specs for the same handoff suppress adoption of both. If it's close, the cheaper move is proposing your manifest as an extension or a version of that spec inside the same foundation, not a parallel one.
- **Implementations today**: zero — this is a pre-v1 effort. All three planned implementations (Caldmere + 2 peers) would be author-controlled at launch, not independent. That's normal for a co-founded spec at month zero; it's also exactly why the KPIs below track adoption *outside* the founding three, not just the three.
- **Counted demand**: two peer vendors, each with a named engineer committed for two years. That's real, costed commitment, not a belief that "everyone wants this" — treat it as the demand evidence.
- **Conformance suite / certification mark**: none yet — to be built with v1 (Step below).

## Decision

**Posture: Co-found.** (Given, not re-litigated — you're past should-we.) Validated against the four tests anyway, because a co-founding record that skips them isn't defensible in front of the two peers either:

- **Demand test** — passed: two named peers, each staffing two years, is counted commitment.
- **Commoditization test** — passed: the layer being standardized is the interchange manifest between pipeline vendors, not what Caldmere sells (the pipeline product itself). Commoditizing the handoff format doesn't erode Caldmere's differentiation; it removes a cost all three of you currently pay separately.
- **Control test** — passed for Co-found, fails for Drive: no single company here holds a dominant share of the relevant assets (installed base, complements). Tarn's written refusal to implement a spec in Caldmere's GitHub org *is* the control test failing for solo Drive, stated by the peer directly rather than inferred.
- **Cost test** — passed: three named engineers over two years is fundable for a foundation-hosted venue's effort level. It would not be fundable for ISO or W3C's effort, which is part of why those are rejected below.

## Alternatives rejected

- **Drive (Caldmere publishes alone)**: rejected — control test fails; Tarn has told you in writing this is a dealbreaker, not a preference.
- **Own repo / Git-based community specification** (the efficiency default for everyone above Contribute): rejected on the named-party rule — a party has stated in writing it will not implement a spec living in your org, which is precisely the trigger to move one venue right, no further.
- **OASIS-style consortium**: rejected — it buys more neutrality than the specific objection requires, at the highest compliance cost of any venue (IPR mode can't change without closing and re-chartering the technical committee) and more effort than a 3-company effort needs. Nothing in your facts (no regulator, no enterprise buyer mandating formal process) triggers OASIS's promote condition.
- **IETF**: rejected for now — real neutrality, but its effort and open-to-anyone participation model are calibrated for standardizing a spec for the whole Internet, not for three named companies who need an incorporated, legally-equipped host to sit the work under by Thursday. Revisit if the spec later needs to become a general wire protocol beyond the three of you.
- **W3C**: rejected — the explicit promote condition (browsers must implement the surface) is absent by your own statement. This is a server-to-server manifest; W3C's royalty-free-only Recommendation Track and multi-month chartering buy nothing here that a foundation doesn't already buy cheaper.
- **ISO transposition**: rejected — the explicit promote condition (a tender, regulator, or public buyer requiring a standard number) is absent; nobody here sells to government, by your own statement. ISO is the slowest venue on the list and doesn't create adoption, it certifies adoption that already exists.

## Venue and IPR

**Venue: Foundation-hosted consortium** (Joint Development Foundation-style — e.g., under the Linux Foundation umbrella; confirm the exact host with peers, don't lock the brand before Thursday, lock the *type*).

Why this one, precisely: the only fact forcing a venue change is Tarn's written refusal to accept Caldmere-owned hosting. The rule for exactly that fact is "move one venue right of Git-based, no further absent another trigger." One step right of Git-based is foundation-hosted. It buys neutral incorporation, IP agreements, and governance structure fast, with far less process weight than IETF/OASIS/W3C/ISO, and none of those four have a fact in this brief that promotes them.

**IPR mode: Royalty-free (RF).** You hold no patents that read on this area and have never licensed IP to anyone — the RAND branch doesn't exist for you, and RF is the default this produces. RF also maximizes the implementer pool, which matters directly: your KPI below is independent adoption *outside* the three founders, and most data-pipeline tooling outside big vendors is open source, which a RAND or even non-assertion-only regime would exclude or chill. Recommend RF over a bare non-assertion covenant for the same reason: RF gives implementers an explicit grant, not just a promise, at zero incremental cost to you since you have nothing to hold back.

**Trademark holder: the foundation, not Caldmere.** Same logic as the venue choice — the complaint was ownership optics, and that applies to the mark as much as the repo. If Caldmere holds the trademark while the repo sits at a foundation, you've only half-answered Tarn.

**Charter-time commitments you cannot revise later** (flag to counsel explicitly, per your lawyer's Thursday question): the RF election and the trademark assignment to the foundation. Both are the two decisions this skill treats as irreversible without re-chartering — get counsel to review the actual charter language for these two clauses specifically, not the rest of the boilerplate.

## Conformance plan

- **Mark**: versioned per spec revision, expires when that revision is superseded — decide this at v1, not after implementations exist carrying an unversioned mark.
- **Registry**: one public page maintained by the foundation, listing certified implementations — this is what buyers/integrators actually consult.
- **Who runs the tests**: self-service (upload and pass) — no regulated domain or buyer-mandated observer is in play here, so witnessed testing would be pure overhead.
- **Cost to pass**: free — you want the implementer count outside the three founders to be the real signal of whether this spec is real; a fee suppresses exactly the population you need to prove that.

## Staffing

- Peer 1: named engineer, two-year commitment (per peer's own statement).
- Peer 2: named engineer, two-year commitment (per peer's own statement).
- **Caldmere: not yet named.** ⚠️ This is a gap, not a footnote — you're proposing to co-found as an equal, and showing up to charter the foundation without a matched two-year staffing commitment undercuts the "we're equal co-founders, not the owner" position that's the entire reason you moved off Git-based in the first place. Close this before Thursday if possible.

## KPIs and thresholds

| Metric | Threshold | Sourced or baseline | By when |
|---|---|---|---|
| Independent interoperating implementations beyond the 3 founding vendors | ≥ 2 | Sourced — RFC 6410 §2.2 / W3C Process §6.3.2's implementation-experience bar for calling a spec real | 18 months post-v1 |
| At least one implementer that is not one of the 3 founders | ≥ 1 | Baseline — this skill's default clock-and-customer-test, not an industry norm | 12 months post-v1 |
| Conformance suite pass rate among implementations claiming support | 100% | Baseline | Ongoing from v1 |
| Founding-vendor production integrations live | 3 of 3 | Baseline — internal delivery bar, not an adoption signal | 6 months post-v1 |

## Kill rule

If fewer than 1 non-founder implementation exists at month 12 **and** fewer than 2 independent implementations exist at month 18: stop investing in courting broader ecosystem adoption. Because three committed implementers already exist by design, "kill" here means freezing ecosystem ambition and keeping the spec serving the three founders' own interop — not withdrawing it, which would strand the very peers who staffed it. The foundation host publishes a status note saying adoption stalled, rather than letting the spec quietly rot. Any outside party that has already implemented v1 by that point gets 6 months' notice and a maintained bridge before any breaking v2 — the obligation runs from whoever owns the spec (the foundation, on your collective behalf) to whoever trusted it, independent of which founder proposed the kill.