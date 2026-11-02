# Open Source Release Strategy — Six Technical Assets

**Prepared for: Executive Team**
**Scope: Java SDK · ISO 20022 message schema · ledger reconciliation engine · chaos-testing harness · fraud-scoring model · conformance test suite**

## Summary verdicts

| Asset | Verdict | Confidence |
|---|---|---|
| Java SDK | **Open source** | High |
| ISO 20022 message schema | **Open source, scoped** | High |
| Conformance test suite | **Open source** | High |
| Chaos-testing harness | **Open source, after redaction audit** | Medium |
| Ledger reconciliation engine | **Do not open source** | High |
| Fraud-scoring model | **Do not open source — no** | High |

Four of six clear a bar for release. Two don't, and one of those two is the subject of a proposal from the CTO that this document argues against directly, below.

## The criterion that sorts these six

The four "yes" assets are infrastructure and tooling that make it easier to *integrate with* or *verify* the product. The two "no" assets *are* the product — they encode the specific logic customers pay for instead of building themselves, or the specific logic that keeps bad actors out. That distinction, not "how sensitive does this feel," is what should decide each case. Concretely:

- **Does publishing it hand a competitor your differentiation, or just your API contract?** SDKs and conformance suites expose contracts, not the differentiated internals behind them.
- **Does publishing it hand an adversary a blueprint for evasion?** This applies to exactly one asset here, and it's disqualifying on its own regardless of any adoption upside.
- **Is the value we'd lose by publishing it reversible if the bet doesn't pay off?** Competitive exposure is only partly reversible. Security exposure is not reversible at all.

## Per-asset detail

### Java SDK — open source

The SDK is glue code: it calls a documented API and shapes the response into idiomatic Java. Every serious payments/fintech infrastructure vendor competing for the same enterprise buyers — Stripe, Adyen, Plaid, Modern Treasury — publishes client SDKs, and enterprise security reviewers now routinely expect to audit the client library they're asked to embed. Withholding it is friction with no offsetting protection, since the API surface it wraps is knowable from documentation regardless. Recommend Apache 2.0 (patent grant matters here — it removes a legal-review blocker for enterprise buyers) and generation from the OpenAPI spec so it doesn't become a maintenance sink.

### ISO 20022 message schema — open source, scoped

ISO 20022 itself is a public standard; publishing a conformant schema is a contribution to interoperability, not a disclosure of anything proprietary. Banks and payment networks that publish their own ISO 20022 usage guides do so for exactly this reason — it's what lets counterparties integrate without a support ticket, and it reads as maturity in vendor diligence. The condition: publish the canonical message layer only. Before release, strip anything that maps the standard onto your internal systems — internal field mappings, routing logic, fee/pricing encodings, or references to specific downstream vendors. The standard is public; your implementation's internal wiring isn't, and shouldn't become public as a side effect of publishing the former.

### Conformance test suite — open source

This is the highest-leverage release of the six. A test suite doesn't reveal implementation — it defines correct behavior, and whoever publishes the reference definition of "correct" for a given interface tends to have that definition adopted as the de facto standard everyone else validates against. That's a durable ecosystem position, not a one-time PR win, and it pairs naturally with the schema release above: ship them together as one interoperability credibility package. Risk is low by construction; the main task is confirming none of the test fixtures leak real customer-shaped data or internal environment details.

### Chaos-testing harness — open source, conditional on a redaction pass

Chaos engineering tooling is a well-worn credibility play (the Chaos Monkey lineage exists for this reason) and signals engineering maturity to exactly the enterprise and bank customers who run vendor resilience questionnaires. The methodology itself isn't the moat — the systems it tests are. Before release, audit for anything that maps to real production topology: internal service names, specific failure-injection targets, or scenarios derived from actual past incidents, any of which functions as an attack-surface map in the wrong hands. If the harness is currently wired directly into production hooks, the cleaner release is a generalized, pluggable version decoupled from your specific infrastructure, not a literal export of what's running today.

### Ledger reconciliation engine — do not open source

This is core IP for a company whose value proposition rests on doing reconciliation correctly so customers don't have to build it themselves. The hard part of a reconciliation engine — the accumulated handling of rounding, timing corrections, multi-currency FX, chargebacks, partial settlements, edge cases discovered over years of production incidents — is exactly what's on the page if the source is public. That's not a hypothesis to pilot; it's the product. See the dedicated section below responding directly to the proposal to ship this one and watch what happens.

### Fraud-scoring model — do not open source

This is a different category of "no" than the reconciliation engine, and the exec team should treat it that way rather than filing it under the same "competitive exposure" bucket. Publishing detection logic — features, thresholds, model structure — doesn't just cost differentiation, it hands an adversary a manual for evasion. Every serious fraud, WAF, spam-filtering, or credit-underwriting vendor keeps this class of logic closed for the same reason: the moment it's public, testing transactions against known thresholds becomes trivial, and the degradation in effectiveness isn't something a later "pull it back in" can undo — fraud rings don't forget what they learned. There's likely also a data-lineage angle worth a quick legal check: even without raw customer data in the repo, published feature-engineering choices can reveal inferences drawn from customer transaction behavior. If there's a genuine trust or DevRel goal behind this idea, the lower-risk version is a methodology whitepaper — describe the *approach* at a level that builds credibility without exposing exact features, thresholds, or weights.

## On the CTO's proposal for the reconciliation engine

The framing — open source it, see if it helps adoption over a year, pull it back into proprietary if it doesn't — treats this as a reversible experiment. It isn't, for two independent reasons, and the exec team should weigh both before signing off.

**First, "pull back" doesn't undo disclosure.** Once the engine is public, every prospective customer doing build-vs-buy, and every competitor, has had a year to read the reconciliation logic, fork it, and build on it. Re-closing the repository stops *future* commits from being public; it does nothing about everything already read, cloned, and absorbed. The asset being protected — the accumulated edge-case handling that makes reconciliation hard to replicate — doesn't come back by changing a license file.

**Second, "adoption" is the wrong single metric to gate the decision on.** Even in the scenario where open sourcing drives zero measurable adoption and the team pulls it back exactly as planned, that outcome tells you nothing about the competitive harm that occurred in parallel — a competitor building a comparable engine faster because yours was the reference, or an enterprise prospect deciding to build in-house because your own repo showed them it was tractable. Zero adoption and zero harm are not the same outcome, and the proposed experiment only measures the first one.

If the underlying question is "would open source meaningfully help our adoption," that's a legitimate thing to want data on — but it doesn't require betting the reconciliation engine to get it. The SDK and conformance suite releases recommended above test the same underlying hypothesis (does publishing our tooling move adoption) at a cost that's actually recoverable if the answer is no. Recommend running those first, watching the adoption signal for two to three quarters, and revisiting the reconciliation engine question only if that data suggests it's warranted — and even then, as a deliberate open-core strategic move (open a thin interface layer, keep the production engine and its edge-case handling closed), not a full release with a one-year trial period.

## Recommended sequencing

1. **Now:** Java SDK + conformance test suite. Lowest risk, fastest adoption signal, no dependency on other releases.
2. **After legal review of internal mappings:** ISO 20022 schema, released alongside the conformance suite as one interoperability package.
3. **After a redaction/security audit:** chaos-testing harness.
4. **Not this cycle:** reconciliation engine, fraud-scoring model. Revisit the reconciliation engine only after the above releases produce real adoption data, and only as an open-core design, not a full release.

## License and governance notes

Apache 2.0 for the SDK, schema, conformance suite, and chaos harness — the explicit patent grant reduces legal friction for the enterprise and bank customers most likely to actually adopt these. Decide up front whether releases live under a company GitHub org (faster, more control) or a neutral foundation (slower to set up, but the conformance suite in particular gains credibility as a common standard if it isn't perceived as company-controlled) — this matters most for the conformance suite, least for the SDK.

## Decisions needed from exec team

- Sign off on the four "yes" releases and the sequencing above.
- Confirm the reconciliation engine stays closed this cycle, and that any future revisit is scoped as open-core design work, not a reversible pilot.
- Confirm the fraud-scoring model is off the table entirely — recommend this one not be revisited on an adoption-metric basis at all, given the security dimension.
- Assign legal review owner for the ISO 20022 schema (strip internal mappings) and security review owner for the chaos harness (redact topology references).
- Decide company-org vs. foundation governance before the first release ships, since retrofitting this later is disruptive to any external contributors who've already shown up.