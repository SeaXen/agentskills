# Documentation Scope Audit — Halyard Grid Docs

**Scope:** Evaluate the growth lead's proposal to compress architecture overview, security-model, rate/retention limits, cost model, and legacy-SCADA migration content to one paragraph each, redirecting effort into quickstarts.

**Finding, upfront:** ⚠️ The evidence does not support this cut. The premise — "developers want to copy-paste, not read essays" — is true for one audience this docs site serves and false for the audience that reads these five specific pages. Applying a self-serve-SaaS docs heuristic to a utility procurement sale conflates two different readers with two different jobs.

---

## 1. The premise assumes one reader. This product has two.

| | Integrating engineer | Evaluation stakeholder |
|---|---|---|
| Reads docs to | Ship code | De-risk a six-month purchase decision |
| Wants | Copy-paste, 5-minute time-to-first-success | A citable, written artifact for a questionnaire, RFP, or audit file |
| Reads a page | Repeatedly, while building | Once, before a PO is cut, often printed or PDF'd into a vendor file |
| Typical count per deal | 1-3 people | 4-10 people (security, compliance, OT/SCADA engineering, procurement, finance) |

The five flagged sections are pre-sale evaluation collateral, not post-sale integration collateral. "Developers want to copy-paste" is a true statement about the API reference and SDK quickstart. It is not a true statement about the audience for these five pages, because that audience is largely not developers.

## 2. Section-by-section

**Architecture overview** — Consumed by solution architects and security reviewers during vendor shortlisting, before any engineer touches an SDK. Utility RFPs typically require a submitted written architecture description; "we covered it on a call" does not satisfy that requirement. Cutting this to a paragraph doesn't remove the need, it moves the same content into a slower, unscalable channel: a sales engineer writing it out by hand, per deal.

**Security-model section** — ⚠️ Highest-risk cut on the list. The prompt already states this sale includes a formal security review. That review runs on a written security model to complete vendor risk questionnaires and internal audit records. Delete the page and the questions don't go away — they arrive by email instead, unscoped, and now cost sales-engineering time per deal rather than zero marginal cost per reader. This section isn't marketing copy competing for developer attention; it's the artifact that unblocks a downstream gate. Optimizing it for "page length" targets the wrong bottleneck — the constraint here is procurement/security throughput, not developer activation.

**Rate and retention limits** — For a utility buyer, retention figures intersect with the buyer's own data-governance and regulatory obligations. An unpublished number isn't one fewer question, it's the same question routed to a human, answered inconsistently deal to deal, with no audit trail. This is exactly the kind of fact that should live in a static, versioned doc rather than a rep's memory.

**Cost model** — Self-serve SaaS pricing pages and negotiated utility/hardware contracts serve different functions. Here the cost model page is a pre-qualification tool: it lets procurement estimate budget before requesting a quote. Cutting it doesn't reduce the buyer's need for the information, it just pulls the conversation earlier into a discovery call — a less scalable channel than a page.

**Migration-from-legacy-SCADA explainer** — Not an essay competing with a quickstart for attention. This is the document that carries the single biggest operational-risk conversation in the deal: replacing or augmenting a legacy SCADA layer touches grid safety and uptime. Its reader is an OT engineer managing change-risk, not a developer wanting "hello world" faster. A paragraph cannot carry a cutover risk narrative; shrinking it pushes the same discussion into unscalable pre-sales engineering calls instead of removing it.

## 3. Where the growth instinct is right

If there's a genuinely separate integrator audience — third parties writing polling/ingestion code against the telemetry API — that audience's docs absolutely benefit from the docs-as-marketing playbook: code-first, 5-minute time-to-first-success, minimal prose. That's the API reference, auth guide, and SDK quickstart. Those pages likely *are* underserved relative to the 260-page total, but that's a different fix than shrinking the five evaluation-stakeholder pages — it's adding a dedicated quickstart track, not repurposing procurement collateral into one.

## 4. What the audit recommends instead

- Add a one-paragraph TL;DR at the top of each of the five pages for skimmers. This captures the real insight ("busy readers won't parse an essay") without deleting the content a downstream reader needs to cite.
- Keep full depth as the page's default, uncollapsed state. Security and compliance reviewers cite specific sections in their own paperwork — content that's hidden behind a "read more" toggle isn't addressable the same way.
- Split navigation into two tracks — "Evaluate & Procure" vs. "Build & Integrate" — so the 260-page count stops reading as one undifferentiated wall. That's an information-architecture fix, not a content-deletion fix.
- Build out the quickstart/API-reference track for the integrator audience if it's genuinely thin — that's where the "copy-paste, not essays" rule actually applies.
- Before cutting anything: pull docs analytics on these five pages (traffic source, session count, company/account association where available), check how often sales engineering attaches them to security questionnaires or RFP responses, and ask solutions engineering how many deal-cycle hours they'd absorb if these pages stopped existing. That's the evidence base this decision should run on — not a heuristic imported from self-serve developer-tool docs.

## Bottom line

The audit does not back the instruction as given. It supports adding skimmable summaries while preserving full depth on these five pages, and building a genuinely separate, quickstart-first track for whatever integrator audience is actually underserved.