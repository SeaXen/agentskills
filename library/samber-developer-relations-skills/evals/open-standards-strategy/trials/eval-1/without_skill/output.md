# Open Standards Strategy — Corvado Platform

**Owner:** VP Platform | **Audience:** Executive Team | **Status:** Draft for review | **Cycle:** H1 OKR
**Before you present this:** the bracketed items marked `[VERIFY]` are placeholders — I don't have visibility into our actual EDI transaction set coverage, current API versioning history, or specific partner names, so I've framed those as questions to answer with your team rather than invented facts. Everything else is a strategic position you can adopt as-is or amend.

---

## 1. Executive Summary

Corvado sits in the middle of other people's supply chains. Every shipper, carrier, 3PL, and customs broker we connect to has their own systems, their own data formats, and their own integration budget — and none of them chose us because we're easy to talk to on the inside. They chose us because we're easy to connect to on the outside.

**Open standards are not a compliance checkbox or an engineering nicety. They are our distribution mechanism.** Every hour we spend building on top of an open standard instead of inventing a proprietary one is an hour a customer's IT team doesn't spend writing custom glue code to adopt us — and every hour we spend contributing fixes back to a standard we depend on is an hour that standard stays healthy enough for the next customer to rely on it too.

This strategy commits Corvado to three things:

1. **Adopt open standards by default** wherever one exists and fits, and require a documented justification to build proprietary instead.
2. **Publish and document our own interfaces as if they were the standard** — versioned, stable, deprecation-noticed, and readable without a sales call.
3. **Participate**, not just consume — join the working groups that govern the standards we depend on, contribute fixes upstream, and put engineering time behind the ecosystem that carries our traffic.

This is a platform strategy, not a marketing strategy. It changes how we design integrations, how we version APIs, how we evaluate build-vs-adopt decisions, and how we allocate a small, explicit slice of engineering time to standards-body work. It does **not** commit us to open-sourcing our core product, and it does not require unanimous industry consensus before we ship — sections 4 and 7 draw that line explicitly.

---

## 2. Why This Is a Platform Strategy, Not a PR Position

Three forces make this concrete and urgent rather than aspirational:

- **Integration cost is our biggest sales-cycle tax.** Enterprise shippers and carriers evaluate us partly on how many weeks their EDI/API team needs to go live. Standards compliance directly shortens that number.
- **Our partners are consolidating around a handful of standards whether we participate or not** — GS1 identifiers, EDI X12/EDIFACT transaction sets, and increasingly DCSA's REST/JSON API specs for ocean and inland freight. If we don't track these, we drift into being the integration that always needs a custom adapter, which is a quiet but real churn and win-rate risk.
- **Regulatory and customs-facing data flows (e.g., import/export declarations, chain-of-custody) are standards-governed by definition.** Non-compliance here isn't a design choice, it's a liability.

The OKR framing ("open standards strategy") is really asking: *when a partner's system speaks a standard we don't, whose problem is that, and what did we do about it proactively instead of reactively?*

---

## 3. Scope — What "Open Standards" Means for Corvado

To keep this actionable, we're scoping "open standards" to four concrete domains rather than treating it as one abstract commitment:

| Domain | What it covers | Primary standards bodies / specs relevant to logistics |
|---|---|---|
| **Data interchange** | How shipment, order, and inventory data moves between us and partners | ANSI X12, UN/EDIFACT, GS1 (GTIN, GLN, SSCC), EPCIS/CBV, UN/CEFACT |
| **API design** | How our own and partners' systems talk over HTTP | OpenAPI 3.x, JSON:API or equivalent, DCSA REST specs (ocean/track-and-trace), OAuth 2.0 / OIDC |
| **Identity & security** | Auth, signing, and trust between systems | OAuth2/OIDC, mTLS, JSON Web Tokens, SOC 2 / ISO 27001 as the credibility layer that makes API openness safe |
| **Openness of our own platform** | How discoverable, documented, and lock-in-free our own interfaces are to the outside world | Public API docs, semantic versioning, published deprecation policy, data portability/export guarantees |

Explicitly **out of scope** for this document: open-sourcing Corvado's core product, and general OSS license policy for third-party dependencies (that's covered separately by [Legal/Eng dependency policy — VERIFY this exists; if not, flag as a gap]).

---

## 4. Guiding Principles

1. **Adopt before you build.** If an open standard covers the use case, use it. Deviating requires a written justification reviewed by Platform (see §7).
2. **Extend, don't fork.** When a standard is close but incomplete for our use case, propose an extension upstream before shipping a private variant. Ship the private variant only if upstream timelines don't fit the business need, and track it for eventual reconciliation.
3. **Document like a standard, not like a product feature.** Public-facing APIs get versioned contracts, changelogs, and deprecation notices — regardless of whether the audience is an external partner or an internal team. External developers should never need an account manager to understand what an endpoint does.
4. **No silent lock-in.** Customers and partners can always get their data out in a standard, machine-readable format. We compete on product quality and service, not on how hard it is to leave.
5. **Contribute in proportion to what we depend on.** If a standard or open-source library is load-bearing for Corvado, we owe it more than bug reports — see §6.
6. **Openness has a budget, not a blank check.** Standards work competes with roadmap like everything else. We fund it explicitly (§8) rather than treating it as free-time goodwill that evaporates under deadline pressure.

---

## 5. Current State — What We're Actually Starting From

This section needs your input before it goes to the exec team; I've laid out the questions rather than guessing at answers.

| Area | Status | Question to close before Friday |
|---|---|---|
| EDI transaction set coverage | 🟡 Unknown | Which X12/EDIFACT transaction sets do we support today, and which are custom-mapped per customer? `[VERIFY]` |
| Public API documentation | 🟡 Unknown | Is there a public, versioned API reference today, or is it behind a partner portal / sales gate? `[VERIFY]` |
| API versioning discipline | 🟡 Unknown | Do we have a deprecation policy today, even informally? Has a breaking change ever shipped without notice? `[VERIFY]` |
| GS1 identifier usage | 🟡 Unknown | Do we natively support GTIN/GLN/SSCC, or do partners map into our own internal IDs? `[VERIFY]` |
| DCSA / ocean track-and-trace | 🟡 Unknown | Relevant only if we touch ocean freight — confirm scope. `[VERIFY]` |
| Standards body membership | 🔴 Likely none | Are we a member of GS1, DCSA, or UN/CEFACT today? If not, this is a zero-cost first move (see §8). |
| OSS contribution track record | 🟡 Unknown | Do any engineers currently contribute upstream to dependencies we rely on? |

**Recommendation:** run a 2-week platform audit in the first two weeks of H1 to fill this table with real answers before committing to the roadmap numbers in §8. Everything below is sequenced assuming that audit happens first.

---

## 6. The "Good Ecosystem Citizen" Commitments

These are the specific, checkable commitments the exec team is being asked to back. Each has an owner and a cadence, not just a value statement.

**Consume responsibly**
- Track upstream deprecations of every standard/spec version we depend on; don't let a customer discover a sunset before we do.
- File issues upstream instead of patching around bugs in standards libraries or reference implementations where feasible.

**Publish honestly**
- Every externally-consumed API gets a public changelog and a minimum notice window before breaking changes (recommend 90 days for anything customer-integrated; shorter only for pre-GA endpoints explicitly marked as such).
- Data export/portability is a documented, self-serve capability for every customer-owned dataset — not a support ticket.

**Contribute back, proportionally**
- Any open-source dependency classified as "load-bearing" (breaks core product flows if it disappears) gets a named internal owner responsible for upstream engagement — security patches, version bumps, occasional PRs — not just passive consumption.
- Target: engineering time budget of **2–5% of platform team capacity** allocated to upstream contribution and standards participation, reviewed quarterly. (This number should be sized against your actual platform headcount — flag if 2-5% is unrealistic given current roadmap pressure, and we scale it down rather than commit to a number we'll quietly ignore.)

**Participate in governance**
- Join the standards bodies that govern the specs we depend on most (starting candidates: GS1 membership, DCSA if ocean-freight-relevant, UN/CEFACT working group observation). Membership tiers for GS1/DCSA are typically low-cost relative to enterprise sales cycle value — this should be one of the cheapest line items in the whole strategy.
- Send an engineer or the VP Platform to at least one relevant standards working group session per quarter, and report back findings to the platform team.

**Say no on the record**
- Where we deliberately deviate from a standard (§4, principle 2), document why in an internal ADR (architecture decision record), so "why don't we support X" has a real answer six months later instead of institutional memory loss.

---

## 7. Decision Framework — Adopt, Extend, or Build Proprietary

Use this at design time for any new integration surface, not retroactively:

```
Does an open standard already cover this data/interface?
├─ Yes, and it fits our use case
│     → Adopt it directly. No exceptions without Platform sign-off.
│
├─ Yes, but it's missing something we need
│     → Propose an extension upstream first.
│       If timeline doesn't allow waiting:
│       → Ship a documented superset, track for upstream reconciliation,
│         log an ADR explaining the gap.
│
└─ No standard exists / the space is genuinely novel
      → Design it openly anyway: versioned, documented, exportable.
        This is where Corvado can propose a de facto standard —
        credibility comes from being first and open, not from
        being closed.
```

The failure mode this framework exists to prevent: engineers defaulting to a proprietary format because it's faster this sprint, and that format quietly becoming the thing forty customer integrations depend on three years later. That's how most vendor lock-in gets created — not by strategy, by accretion.

---

## 8. Roadmap

**H1 (this cycle) — Foundation**
1. Weeks 1–2: Run the current-state audit (§5) — assign an owner, close every `[VERIFY]`.
2. Weeks 3–4: Publish (or clean up) a public, versioned API reference with an explicit deprecation policy — even if scope is limited to our most-used endpoints first.
3. Month 2: Join GS1 (and DCSA if ocean-freight is in scope) — lowest-cost, highest-credibility move available.
4. Month 2–3: Identify our top 3 "load-bearing" open-source dependencies and assign named internal owners.
5. Month 3: Write the first 2–3 ADRs documenting existing intentional deviations from standards, so the backlog of undocumented decisions starts shrinking instead of growing.
6. End of H1: Report to exec team — audit results, API doc launch, standards body memberships secured, contribution-time budget proposal with real headcount numbers.

**H2 and beyond — Depth**
- Formal RFC process for new integration surfaces, reviewed against §7 before build starts.
- First upstream contribution(s) from the load-bearing dependency owners.
- Evaluate whether Corvado should publish its own open spec for a genuinely novel piece of our data model (only if §7's "no standard exists" branch surfaces a real candidate — don't manufacture one for the sake of a headline).
- Quarterly standards-body attendance cadence in steady state.

---

## 9. What We're Explicitly Not Doing

Being clear about boundaries protects the strategy from scope creep and from being weaponized against normal product tradeoffs:

- **Not** open-sourcing the core platform. This is an interoperability and integration strategy, not an OSS business model change.
- **Not** requiring every internal API to be public — internal service boundaries stay pragmatic; this applies to customer- and partner-facing surfaces.
- **Not** blocking shipping when no standard exists or timelines genuinely don't allow waiting on a working group — §7's proprietary branch is a legitimate, documented path, not a failure state.
- **Not** a unilateral veto for engineers to slow-roll roadmap work by invoking "standards purity" — the ADR requirement exists precisely so deviations are fast to approve and cheap to document, not a bureaucratic gate.

---

## 10. Success Metrics

Track these quarterly, report at the OKR checkpoint:

- **Integration time-to-live** for new enterprise customers/partners (target: trending down as standards adoption increases — this is the metric that actually ties to revenue).
- **% of customer-facing API surface covered by a published, versioned contract** (target: 100% for GA endpoints by end of H2).
- **Number of breaking changes shipped without the committed notice window** (target: zero — this is a trust metric, treat any miss as an incident, not a rounding error).
- **Standards body memberships held** and **working-group sessions attended**.
- **Upstream contributions made** (issues filed, PRs merged) against load-bearing dependencies.

Avoid vanity substitutes — "number of standards mentioned in sales decks" or "pages of documentation written" measure effort, not outcome. The metrics above measure whether partners actually integrate faster and trust us more, which is the entire point of doing this.

---

## 11. Governance

- **Owner:** VP Platform, accountable to CTO for OKR delivery.
- **Decision rights:** Platform team owns the adopt/extend/build framework (§7) and approves ADRs documenting deviations. Individual engineering teams retain implementation authority within that framework.
- **Review cadence:** Quarterly review against the metrics in §10, folded into the existing platform roadmap review rather than a separate meeting.
- **Escalation:** Disputes over "should this be a standard or proprietary" that can't be resolved at the Platform level escalate to CTO, with the ADR as the artifact under discussion — not a re-litigation from scratch.

---

## Appendix A — Standards Glossary (for the exec audience)

- **ANSI X12 / UN/EDIFACT** — The two dominant EDI (Electronic Data Interchange) standards for transactional logistics documents (purchase orders, ASNs, invoices). X12 is more common in North America, EDIFACT internationally.
- **GS1 (GTIN, GLN, SSCC)** — Global identifier standards for products, locations, and shipping units. The barcode/RFID layer of the supply chain.
- **EPCIS** — GS1's standard for sharing visibility/traceability event data (where an item was, when, and what happened to it) between trading partners.
- **DCSA** — Digital Container Shipping Association; publishes REST/JSON API standards for ocean freight booking, track-and-trace, and e-documentation. Relevant if Corvado touches ocean freight.
- **UN/CEFACT** — UN body producing trade facilitation and e-business standards, broader than EDI.
- **OpenAPI** — The de facto standard for describing REST APIs in a machine-readable, versionable format.
- **OAuth 2.0 / OIDC** — Standard protocols for authorization and identity federation between systems.

## Appendix B — Open Questions for the Audit (Week 1–2)

1. What EDI transaction sets do we support today, and how many are customer-specific custom mappings vs. standard?
2. Do we have a public API reference today? If yes, where; if no, what's blocking publishing one?
3. Has a breaking API change ever shipped without advance notice? If so, what happened downstream?
4. Are we DCSA-relevant (do we touch ocean freight/booking data)?
5. What's a realistic contribution-time budget given current platform headcount and roadmap load — is 2-5% actually available, or does this number need to start lower?