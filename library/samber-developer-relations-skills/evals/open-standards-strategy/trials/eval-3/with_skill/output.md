Using open-standards-strategy to decide Tessral's posture toward the anomaly score exchange effort.

# Standards decision: Anomaly Score Exchange interface

**Date:** 2026-09-24 · **Owner:** _name the accountable exec — not yet assigned_ · **Review:** 2027-03-24, or immediately if the six vendors circulate a Working Draft

## Answer

**No. Don't chair it, don't co-found it, and don't put your one senior engineer on it as a text-writing contributor either.** The commoditization test kills all three before staffing or venue even come up. Below is why, and what to do instead.

## Landscape

- **Standard:** "Anomaly score exchange" — request shape, score normalization, explanation payload. No spec exists today; nobody publishes it.
- **Proposer:** a coalition of six historian/SCADA vendors, not Tessral. They invited you in; you did not initiate this.
- **Venue / IPR mode:** undetermined — not yet asked. Irrelevant to the chair decision below; relevant the moment posture moves to Contribute or above.
- **Implementations:** zero.
- **Your counted demand:** not established. Nothing in the ask names a customer deal, RFP, or ticket that requires this interface. The demand you do have evidence of is the *six vendors'* demand, not yours — and their demand and your interest point in opposite directions (see commoditization test).
- **Conformance suite / mark:** none.

## The four tests

- **Demand test:** unproven on your side. Passes on theirs. Doesn't decide anything here, because the next test already caps the posture regardless.
- **Commoditization test — decisive.** You said it yourself: "the entire product is the scoring model and the score API around it." Request shape, normalization, and explanation payload *is* that API. The standard doesn't cover a shared seam next to your product — it covers the product. Whose demand rises when this layer gets cheap and interchangeable? The six historian/SCADA vendors': they get a plug-compatible market of anomaly engines, can source from anyone, and pay no integration tax to switch away from you. This is Shapiro & Varian's "commoditize complements" play, run by the platform side against the complement layer you occupy — chairing the effort would mean your engineer does the governance labor for a coalition executing that play against you. Per the skill's rule, naming your own product as the layer sets the ceiling at **Extend**. Contribute, Co-found, and Drive are off the table, not just ranked last.
- **Control test:** even setting the ceiling aside, score it. Installed base, strength in complements, and brand/reputation almost certainly sit with the six-vendor coalition, not with one anomaly-scoring vendor they're courting. No single asset decides a standards fight, but four-plus of seven against you is not a position from which "chair" is fundable — it's the textbook case for Contribute at most, and here even that's excluded by the test above.
- **Cost test — independently fatal for "chair."** Chairing a six-party effort is a governance commitment, not an attendance one: convening, arbitrating consensus, and staying through however many revisions it takes to ship v1 — realistically a multi-year, renewing horizon. You've been offered one senior engineer for a fixed 18 months. That funds a defensive seat at a normal working-group pace; it does not fund the chair's chair. Walking away from a chair role mid-effort reads worse in front of six vendors than never taking it — an irreversibility the skill flags explicitly.

## Decision

**Posture: below Extend for now — observe, don't author.** Extend is the ceiling once a base spec exists to extend; none does yet, so the honest present-tense posture is closer to Ignore with a watch, not a rung on the ladder that implies obligation.

- Do not accept the chair.
- Do not send the engineer as a working-group member who writes spec text or votes.
- Send someone — doesn't need to be the senior engineer — to **observe only**: track drafts, flag if the emerging text (a) forces a lossy remapping of your normalization scheme, or (b) ships with no defined behavior for vendor extensions. Both are the "embrace-extend-extinguish inflicted on you" failure mode arriving by accident rather than malice; catching them costs a fraction of a headcount, not a chair.
- Reserve the offered 18-month engineer for your own roadmap. If the group ships a spec, implement it as a client (**Consume**) and layer your explanation depth, confidence bands, and model-specific metadata on top as documented extensions (**Extend**) — that's where your differentiation is allowed to keep living under this test.

## Alternatives rejected

- **Drive:** rejected — commoditization test names your own product as the layer; control test shows a weaker asset position than the coalition inviting you.
- **Co-found / Chair:** rejected — same commoditization ceiling, plus the cost test: chairing needs a multi-year renewing commitment, you have a fixed 18-month single-engineer budget. "Category leader" is a brand goal, not a cleared test; the mechanism that would actually deliver it here (visible control of the interface) is precisely what the commoditization test forbids.
- **Contribute (join the WG, write text, no chair):** rejected on the same commoditization ceiling — shaping the text still spends scarce engineering defining the interface that erases your own switching costs, just with a smaller title.
- **Full ignore, no observer at all:** rejected — leaves you blind to a spec six platform vendors could finalize with no accommodation for how your model's scores or explanations are shaped, and forfeits the (cheap) chance to get an extension point written in before it's locked.

## Staffing

No dedicated headcount now. Observer role: a few hours a month, any technical hire, not the offered senior engineer. Full 18 months stays on product.

## KPIs and thresholds

| Metric                                                                 | Threshold                             | Sourced or baseline | By when    |
| ----------------------------------------------------------------------| -------------------------------------- | -------------------- | ---------- |
| Customer deals/RFPs explicitly naming this exchange format            | ≥ 2 in a rolling 12 months             | Baseline             | Ongoing    |
| A published draft ships with no defined extension-point behavior      | Any occurrence → escalate observer ask | Baseline             | Immediate  |
| A procurement or regulator requirement names a certification mark for this spec | Any occurrence → re-open at Conform only | Baseline | Immediate |
| Independent, vendor-uncontrolled implementations of the eventual spec | 2, before treating it as real          | **Sourced** — RFC 6410 §2.2's bar for "the spec is real," not a target Tessral sets | At review |

## Kill / promote rule

- **Promote to Conform** — never past it — the moment a buyer, tender, or the coalition's own procurement questionnaire starts naming a certification mark. That's the one condition where this stops being a preference and becomes market access.
- **Promote to Drive/Co-found:** not while these facts hold. Would require Tessral to first acquire real installed base or complement leverage independent of this invitation — not a plausible 18-month change.
- **If observation surfaces a hostile normalization scheme or a missing extension point:** respond by publishing your own documented compatibility layer (the Extend rung's own obligation), not by escalating into the working group to fix it from inside.