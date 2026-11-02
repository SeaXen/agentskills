# Open source strategy — Auburn Ledger

*Prepared for exec review · six-asset verdict, structured per the company's open/closed decision framework*

---

## What we sell

Auburn Ledger sells operated, audited fintech infrastructure — a hosted ledger and reconciliation platform that banks, payment processors and other fintechs plug into rather than build themselves. Customers are companies with procurement and legal review, not individual developers with a card (**B2B**). What they pay for is not the code: it's the operated correctness of the ledger at scale, the compliance posture that lets their own auditors sign off, and the standing relationship (support, SLA, certifications) that a fork cannot replicate on day one.

*Assumption flagged for correction: I'm treating "reconciliation correctness, operated at scale, under compliance certification" as the actual value-capture surface. If sales or product would state it differently — e.g., value capture is really the bank/network partnerships and licenses, not operational scale — several verdicts below should be re-read against that instead. This is the one paragraph the rest of the brief inherits from; get it right before presenting downstream.*

---

## Motive

**Primary: commoditize your complement.** Every hour a prospective customer's engineers spend on integration plumbing — SDK wiring, message-format mapping — is an hour they're not moving transaction volume onto the platform, which is what gets billed. Cheaper, more standard integration raises demand for the operated ledger behind it. This is the same logic Spolsky's essay runs for IBM's add-in cards and Netscape's browser: give away the thing that removes friction to buying the thing you sell.

**Secondary, not measured: trust and auditability.** Fintech buyers run security and compliance review before they'll route money through a vendor. Evidence test for this motive is a deal, audit or compliance review where source was actually requested — confirm with sales/solutions engineering whether this has already happened; if it has, this motive is stronger than "secondary" and should be promoted before this brief goes final.

**Named and rejected:** *external demand pull* on the ISO 20022 schema specifically — plausible given industry-wide SWIFT MT→MX migration pressure, but not evidenced here. Treat it as a live candidate to confirm with sales (which customer or regulator, if any, is actually asking), not as the stated reason. A request is not a requirement; a renewal conditioned on it is.

Company type: **venture-backed startup** (Series B) selling into buyers who behave like enterprise procurement (banks, payment processors). Read this as a hybrid: the founder/CEO effectively decides per the venture-backed default, but the compliance review around each decision should run at enterprise weight — a Series B company still gets audited by a bank's security team the same as a public one would.

---

## Open

| Asset | Motive served | G1 — irreversible? | G2 — differentiating or context? | G3 — value capture | G4 — contributable? | G5 — owner | Verdict |
|---|---|---|---|---|---|---|---|
| **Java SDK** | Commoditize complement | Permanent, fine — no differentiating logic lives here once client-side pre-validation is confirmed absent | Context/enabler. Confirm no reconciliation matching logic ships client-side — if it does, strip it into the closed API first | Hosted ledger/reconciliation API, the account relationship, and compliance certifications stay closed; a forked SDK is inert without Auburn Ledger's backend | Yes — language idioms, async support, retry/backoff, typed clients are exactly what outside engineers send PRs for | **TBD — name + hours needed before publishing** | **Open** (interface-open) |
| **ISO 20022 message schema** | Commoditize complement + candidate demand pull (confirm) | Permanent, fine — the underlying standard is ISO/SWIFT's, not Auburn Ledger's IP; publishing a mapping hands over nothing the business was built on | Context — an implementation of a public standard, not proprietary invention | Value capture sits in the certified, validated-at-scale processing behind the schema, not the field definitions themselves | Yes — third-party implementers, integrators, even competitors build against shared interoperability formats; that's what makes it a standard | **TBD** | **Open** (interface-open) |
| **Chaos-testing harness** | Talent, secondary trust signal — neither measured as primary | Permanent, fine — it's a test tool, not the product | Context — validates infra resilience. Confirm no scenario encodes specific reconciliation edge cases; scrub before publishing if so | Nothing revenue-bearing to protect — a forked harness doesn't run against your production topology or scale | Contributable only after a genericization pass strips environment-specific config, secrets and topology references — real engineering work, not a repo push | **TBD — this is the classic "dump-and-run" risk category; do not publish before naming this owner** | **Open** (infrastructure-only), contingent on the genericization pass |
| **Conformance test suite** | Same as schema: trust/auditability + blocks a competitor from becoming the de facto "certified ISO 20022 compliant" gatekeeper | Fine, *if scoped as below* | **Condition attached — run this gate twice.** If scoped strictly to ISO 20022 structural/message-format conformance (well-formedness, field validation, schema versioning): context. If any assertion encodes Auburn Ledger's own settlement or reconciliation business rules: differentiating — carve those assertions out and score them under the reconciliation engine row instead | Unaffected either way — validating conformance to a public standard isn't something anyone resells | Yes, once scoped — this is exactly the kind of suite other implementers run and file edge cases against | **TBD** | **Open**, conditional on the scope split above being done *before* publishing, not discovered after |

---

## Closed

| Asset | Motive tested | Gate failed | Why |
|---|---|---|---|
| **Fraud-scoring model** | Trust and auditability — asserted, not evidenced (no deal/audit on record asked for the model source; confirm with sales) | **G1 (irreversibility) and G3 (value capture), both vetoes** | Publishing detection logic doesn't just risk a competitor reselling it — it arms every adversary who reads it to test evasion, a cost the standard reversal risk doesn't capture and that never goes away once shipped. Differentiating (G2): fraud accuracy is a directly priced trust asset for a fintech infra vendor. Value capture (G3) is the proprietary transaction-volume data behind the model; publish the logic and a forker gets the reasoning without the data, while adversaries get everything they need regardless. No named mechanism survives this. |

**Substitute for the trust motive, since the model itself is off the table:** a third-party audit or attestation — SOC 2 report, penetration-test summary, or a published model-governance disclosure describing controls without exposing logic or weights. The trust motive's own evidence test is "a deal, audit or compliance review where source was asked for" — an attestation satisfies that test without paying the adversarial-gaming cost. Route this to solutions engineering/compliance as a concrete alternative, not a consolation prize.

---

## Not yet

### Ledger reconciliation engine

This is the asset your CTO wants to open on a one-year trial, reversing to proprietary if adoption doesn't materialize. **Run the gates on that framing directly, because the framing itself is where this fails:**

- **Gate 1 — irreversibility (veto).** The plan assumes reversibility that does not exist. Every released version of an open source component stays licensed forever; taking it back closed stops *future* releases, it does not undo the release already made, and re-licensing needs every outside contributor's consent for anything they touched. "Pull it back in" is not available as an exit — pulling a *future* version closed is, but the version already shipped stays open, forkable, forever. Assume permanence and re-ask: does opening it still make sense? On what's stated today, no.
- **Gate 2 — differentiating.** Reconciliation correctness — matching, discrepancy detection, exception handling, the auditable integrity of the ledger — is plausibly the thing "Auburn Ledger" sells as fintech infrastructure. Confirm this explicitly with the exec team before finalizing, but treat it as differentiating by default given the company's name and market position.
- **Gate 3 — value capture (veto).** No mechanism has been named. "Put it out and see what happens" is not a mechanism — it's the exact shape of the failure this framework flags as *weak*: openness without a named answer to "what still stops a competent competitor from reselling this." An unmeasured trial is not evidence gathering; it's exposure with no stated return.

**Verdict: Not yet.** Not a "no" — a named condition. Revisit only once *both* are true:
1. Auburn Ledger has a value-capture mechanism a fork cannot copy — e.g., settlement finality operated under your licensed/regulatory status, an accuracy advantage that compounds with transaction volume (a genuine data network effect, not a claim), or a certified compliance tier customers buy independent of the code.
2. Leadership is prepared to treat the release as **permanent** from day one, not a one-year experiment — see the stress test below for why the difference matters to the adoption signal itself.

**What the reversal record actually says about the CTO's plan**, because this is the evidence, not an opinion:

| Case | What happened | Why it matters here |
|---|---|---|
| HashiCorp, 2023 | MPL-2.0 → BUSL-1.1 across all products | A community fork (OpenTF, now OpenTofu, under the Linux Foundation) emerged **within days**. Reversal cost is priced in fork speed, not quarters of goodwill. |
| Elastic, 2021 → 2024 | Apache-2.0 → SSPL, later added AGPL back | The founder said the relicensing knowingly caused a fork; three years later, described Amazon as "fully invested" in the resulting OpenSearch. The relicensing was reversible on paper — the fork it created was not. |
| Redis, 2024 → 2025 | BSD → RSALv2/SSPLv1, then AGPLv3 added back in Redis 8 | AWS and Google backed the Valkey fork before Redis reversed course. Redis's own CEO said the move achieved its licensing goal but "hurt our relationship with the Redis community" — a win and a loss conceded in the same sentence. |
| Docker, 2017 | `docker/docker` renamed `moby/moby` — **no license change, no code withdrawn** | Backlash was still severe (the announcing PR sat at 7 upvotes to 110 downvotes). This is the cleanest evidence that communities and buyers price *governance surprise*, independent of what was actually taken away. |

Every one of these companies is bigger and better-resourced than Auburn Ledger is today, and every one still ate a permanent fork or a public trust cost the moment reversal looked possible. A bank's security review team reads a "we might pull this back in a year" posture as exactly the signal that makes them not build on it — which would guarantee the CTO's own adoption test reads negative regardless of the engine's merits, because cautious buyers self-select out before the trial even runs. **The plan as stated is close to self-defeating: the thing being tested (would the market adopt it) gets suppressed by the condition attached to the test (we might take it back).**

If the goal is genuinely to learn whether the market wants an open reconciliation engine, a lower-cost way to get that signal without spending the irreversible license: publish the *interface* — the schema and SDK, already recommended Open above — and a detailed design write-up or a limited reference implementation of the reconciliation *algorithm's contract* (not the production engine), then watch whether that alone shifts pipeline. That produces real signal without a one-way door.

---

## Competitive case

**SDK and schema (Open).** A well-funded competitor, or a cloud provider building its own ledger-as-a-service, forks both and points them at a competing backend. What Auburn Ledger still holds: the operated, certified ledger and reconciliation platform, the compliance relationship, and the trademark. Neither fork can move a bank's money without Auburn Ledger's backend — or without independently earning the same certifications. Verdict: acceptable, nothing billed is lost.

**Conformance suite (Open, conditional).** Same competitor uses the suite to certify their own competing implementation against ISO 20022 faster. This is close to the intended outcome of opening a conformance suite for a standard — it grows the ecosystem Auburn Ledger operates in, and a rival "certified compliant" badge is exactly the chokepoint a neutral, jointly-usable suite prevents a single competitor from owning.

**Reconciliation engine, if opened as the CTO proposes.** Name the specific risk out loud: a hyperscaler or a well-capitalized payments company forks the engine and offers reconciliation-as-a-service to Auburn Ledger's own prospect list, undercut on price because they carry none of Auburn Ledger's R&D history. Run the question the framework insists on: *what does Auburn Ledger still hold?* On the value-capture mechanism named today — none. That is the line being wrong, not the fork being unfair; the fix is not a stricter license, it's not shipping until a mechanism exists.

---

## Decision rights

Split the business-context call from the compliance call — do not let one substitute for the other, and do not let the CTO's framing on the reconciliation engine become the deciding vote by default just because it was stated first.

- **Business-context call ("should we open this")** — CTO, per asset, using this brief as the working document. On the reconciliation engine specifically, given the stakes and the CTO's own stated leaning, this call should not be unilateral — escalate to CEO and board before any commitment is made, matching how GitLab routes its largest tiering decisions through the CEO as named final decider.
- **Compliance review ("is this okay to open"), run in parallel, with veto only on its own grounds** — General Counsel (or outside counsel, if no in-house GC yet) plus whoever owns security/compliance, reviewing for: money-transmission/banking-partner obligations, PCI/SOC 2 scope, data residency, and any confidential terms in existing customer or bank-partner contracts that would be violated by publication.
- **No asset ships without both sign-offs.** Neither role covers for the other — this is the same split Google runs (business call to the launch owner's manager, compliance to a parallel specialist review) and the one GitLab names explicitly in its pricing decision matrix.

---

## Commitments

Publish these alongside the SDK, schema, chaos harness and conformance suite at launch — not after, because the commitment is what makes the release durable enough to earn the adoption signal being sought:

1. Once published under an OSI-approved license, the SDK, ISO 20022 schema, chaos-testing harness and conformance suite stay published under that license. Auburn Ledger will not re-license them away from open source.
2. No artificial limits — repository count, request volume, feature gating — added to any open component to force an upgrade path.
3. Tests ship alongside each open component, not held back separately.
4. Any future boundary change — a feature moving out of the open tier, a new closed dependency introduced — is announced before it lands, with the reasoning stated publicly. Adding new paid capability *above* the line later is in scope; moving something already open *down* is not.
5. **The direct answer to the CTO's framing:** none of the four Open assets above is published as a trial. The point of stating this in public is that a "we might pull this back" posture is exactly the risk signal that suppresses the adoption it's meant to measure — a bank's security review prices governance risk the same way it prices code risk. If the reconciliation engine is opened later under the Not-yet condition above, it inherits this same commitment — permanent from day one, or not published.

---

## Operating model

Company stage reads as **Growth** on the standard scaling ladder (Series B, $9M ARR, moving past pre-PMF): a named part-time owner with legal on call, published inbound/outbound policies, an upstream-first default, one funded maintainer per open repository. Not yet the Enterprise tier (full board, foundation memberships, compliance tooling) — don't overbuild the office ahead of the number of repositories actually being opened.

- **Outbound policy.** A release checklist per new open repository before it goes public: license file, notices, secrets scan, dependency-license check, trademark check, a named security contact, a named maintainer. Apply this to all four Open assets before the first commit lands publicly — this is where the chaos harness's environment-specific config risk gets caught.
- **Inbound policy.** A license allowlist/denylist for anything the SDK or harness depend on, with an escalation path for anything on neither list.
- **Upstream-first.** If the chaos harness or SDK build on existing open source tooling, patches go upstream first and get consumed downstream — skipping this quietly kills the maintenance-sharing return the strategy is partly justified on.
- **Where to participate (ISO 20022/SWIFT ecosystem).** Start at "report issues / contribute fixes upstream" on anything Auburn Ledger consumes. Do not commit to a governance seat or a foundation membership at this stage — that's a later-stage rung, and premature spend here buys nothing yet.
- **Cost lines (order of magnitude, not a quote):** maintainer time is the dominant and most commonly under-budgeted line — roughly 0.3 FTE blended across the four open repositories at this stage (review, releases, issue response), plus a few hours of counsel review per release, plus a named security-response contact. No foundation membership needed yet. State the actual total once owners are named — an unbudgeted strategy is the direct path to the abandoned-repository outcome this framework exists to prevent.

**The one gap this brief cannot close for you:** every Gate 5 cell above reads "TBD." Name a real person and a real hours/week number for the SDK, schema, chaos harness and conformance suite before publishing any of them — an asset with no named owner does not ship, by this framework's own rule, however good the rest of its row looks.

---

## Measurement

| Asset | Declared success objective | Re-evaluation trigger |
|---|---|---|
| Java SDK | Growth in platform transaction volume attributable to SDK-driven integrations — not SDK downloads or GitHub stars | Next planning cycle |
| ISO 20022 schema | External implementers (partners, integrators, even competitors) adopt it without a compliance objection surfacing in their own audits; confirmed demand-pull requirement satisfied, if one exists | Next planning cycle, or immediately if a named customer/regulatory deadline exists |
| Chaos-testing harness | Candidates citing the project in interviews; contributor-to-hire conversions. Tolerate low or no external adoption — this motive doesn't need scale | Next planning cycle |
| Conformance suite | Outside organizations running it and filing conformance edge cases — direct evidence the contribution-viability gate actually passed | Next planning cycle |
| Reconciliation engine (Not yet) | N/A — not shipped | A competitor ships an open equivalent, **or** Auburn Ledger lands a named, revenue-provable value-capture mechanism — whichever comes first. Explicitly **not** a calendar year with no mechanism named, which is what the current plan proposes |
| Fraud-scoring model (Closed) | N/A — not shipped; trust motive served via attestation instead | Only if a competitor's open equivalent starts winning trust deals Auburn Ledger is losing — and even then, exhaust the audit/attestation route first |

**Brief self-check against the standard pass threshold:**
- Every candidate asset appears exactly once — yes, six assets, three buckets.
- One primary motive named, with its own evidence test — yes (commoditize complement); the secondary (trust) needs sales to confirm the evidence test.
- Value-capture answer is a mechanism, not a license, for every Open verdict — yes; the reconciliation engine's *lack* of one is exactly what keeps it at Not yet.
- Adversarial scenario written with a specific threat named — yes, run for both the Open assets and the CTO's proposed reconciliation-engine release.
- A named role decides, a separate named role reviews compliance, at least one commitment published — structure proposed above; needs exec sign-off on actual names.
- Annual cost stated — order-of-magnitude given; needs real numbers once owners are named.
- **Open item, not yet passing:** Gate 5 ownership — no individual is named for any of the four Open assets. This brief is not ready to execute against until that's filled in; it is ready to take to the exec team for the open/closed line itself.

---

## Next steps outside this brief's scope

This document draws the line and names the reasons. Three follow-on decisions belong to sibling work once the line above is approved: choosing the actual license and CLA-vs-DCO terms for each Open asset, setting up day-to-day governance once a repository is public, and planning the announcement. Flag these for separate work once the exec team signs off here — don't let license selection or launch planning start before this line is settled, since a wrong motive or a wrong verdict here propagates into all three.