# Ecosystem strategy — Halyard Systems field-service scheduling

**Bottom line:** Build the SAP work-order connector yourselves, on a version-controlled internal API, to hit the 6 March deadline. Do not open a partner or app ecosystem — your own constraints rule it out, and the evidence doesn't clear the bar yet either. That same API becomes the reusable asset for the three asset-management connectors after Meridian closes. This is real "opening up" (documented API, vendor-built connectors), deliberately not a platform play.

**Assumptions I'm making because the brief doesn't state them** — confirm all four in week 1, none of them block starting:
- No public API or webhook surface exists today.
- Nobody has told you which of the three asset-management systems has more than one account asking for it — pull that breakdown from the CRM, it changes build order.
- No unofficial integrations (scripts, scrapers) are currently running against you.
- Meridian's SAP environment (module, version, on-prem vs. cloud) is unconfirmed.

---

## Hypothesis

Because our customers need work-order and asset data synced with their systems of record — SAP for Meridian, three different asset-management platforms for five other accounts — that we have not built, **we** will build the highest-demand connectors ourselves on a documented, versioned integration API, earning **contract renewal and expansion revenue**, which makes Halyard more valuable to **utility operations and IT buyers** by **removing the manual re-entry gap that is currently the stated blocker to at least one renewal.**

Commoditized complement: data movement between Halyard and the systems of record. Not commoditized: the dispatch, prioritization and compliance logic that is what utilities actually buy Halyard for.

Note this hypothesis names "we" as the builder, not a third party — that's the honest outcome of the gates below, not a weaker version of the template.

## Evidence

- Meridian Power, $430k ARR, renewal 6 March: written procurement statement that renewal depends on a working SAP work-order integration. Contractual, dated, unambiguous — the strongest form of demand evidence this skill recognizes.
- Five other accounts requesting connectors across three named asset-management systems. Exact account-to-system mapping not yet pulled — do this before sequencing connectors 2–4.
- No unsupported customer-built glue reported and no other stalled deals reported. Confirm this is genuinely zero, not just unreported.

Four named complements total (SAP + 3 AM systems), against this skill's own default bar of five for opening an ecosystem. Below bar for the ecosystem question — irrelevant for Meridian, whose evidence is a signed-adjacent commitment that stands on its own regardless of the ecosystem count.

## Gates

- **G1 counted demand**: **pass, for Meridian specifically** (contractual, single-customer, doesn't need the five-complement bar). **Unknown, for the asset-management connectors** — resolver: pull CRM breakdown of which accounts want which of the three systems, due within 1 week. Don't commit to building all three until this exists.
- **G2 externalizable interfaces**: **unknown** — resolver: architecture spike confirming work-order create/update/status can be exposed as a stable contract without a core data-model refactor. Due within 2 weeks; this is the real go/no-go for the March date, run it first, not last.
- **G3 identified builders**: **pass, trivially** — the builder is Halyard itself at this rung, no outside party to recruit.
- **G4 commoditized complement, not commoditized core**: **pass** — sync plumbing isn't what utilities buy Halyard for; dispatch and compliance logic is.
- **G5 staffing**: **pass, conditionally** — vendor-built connectors are a roadmap line item, not a standing team, but "maintain it forever against SAP's own API changes" is a real ongoing cost. Name an owner now (a borrowed senior engineer, not a hire) with a fraction of ongoing capacity reserved past the March launch, not just launch-sprint capacity.
- **G6 envelopment exposure**: **fail-with-cap** — SAP sells its own Field Service Management module and could bundle utility dispatch into it directly; whichever of the three asset-management vendors is largest likely has the same option. Cap investment: build a bounded, swappable connector against SAP's stable interfaces, not a deep bidirectional dependency on SAP-specific logic. Re-check this gate before investing further once the SAP connector ships.
- **G7 complement readiness**: **pass for SAP** — its work-order interfaces are mature, standard, and externally documented by SAP itself. **Unknown for the three asset-management systems** — resolver: confirm each vendor's API maturity before committing a build order.

## Rung

Two constraints delete most of the ladder before any ranking starts:

- "Not staffing a security review function" deletes installable third-party apps and a runtime platform — both require running someone else's code inside your boundary.
- "Not signing anything we can't withdraw from" deletes partner-built integrations listed by you — the one rung where another company's revenue starts depending on your surface, making withdrawal public breakage rather than an edit.
- In-product extension points don't apply here regardless — the demand is data moving between systems of record, not behavior changed inside Halyard.

What's left, and the two candidates worth presenting:

1. **Vendor-built integration only, no reusable layer** — fastest to a working SAP connector, nothing to generalize afterward. Rejected: every one of the next three connectors starts from zero, and the cheapest complementor supply you have (customers' own internal IT teams) never gets a surface to build against.
2. **Vendor-built SAP connector now, architected as a documented internal API from day one — recommended.** Same March delivery date, same team, same effort. The only difference is discipline in how the work-order contract is designed: versioned, with a stated deprecation notice, from the first line of code. Once proven against Meridian, generalize it and publish it for the asset-management connectors and for customers' internal IT teams to self-serve minor mapping work.

Recommendation: option 2. It costs nothing extra now and it's the only path that turns "solve Meridian" into "set up for the rest," which is what was asked for.

Reopen condition for the deleted rung (partner-built, listed): revisit only if demand crosses eight distinct complements requested by five or more customers, or a named systems integrator asks in writing to build against you — and only if the CTO's stance on unwithdrawable obligations changes. Don't design toward it before then.

## Complementor case

At this rung the builder is Halyard for the first two connectors (SAP, then whichever asset-management system the CRM pull shows has the most overlap). No external economics to test yet — you're building, not recruiting.

For asset-management connectors 3 and 4, once the API is proven and published, the lowest-friction complementor is the customer's own internal IT team — the archetype this skill flags as needing no business case, only low friction:
- Their return: avoided manual re-entry, faster time-to-value, no need to wait on your roadmap.
- Their cost: minimal, if your docs and sandbox are honest and the API is stable.
- Their alternative: staying on manual entry, or a competitor with a native connector.
- What you owe them: a sandbox in minutes and docs that don't require a support ticket to use — not a partner agreement.

Mirror test: at this rung both sides can walk away cheaply. That's expected and correct here — you are not building an ecosystem, you're publishing a surface. Don't oversell it internally as more than that.

## Flywheel

**Phase 1 (now → 6 March):** build the SAP connector as a vendor-built integration on an internally versioned API. Don't publish or document it externally yet — prove the pattern on the highest-stakes account first.

**Phase 2 (March → next two quarters):** generalize the same API, vendor-build the highest-demand asset-management connector as reference #2, then open documentation and a sandbox to customers' internal IT teams for the remaining systems. This is the loop: each proven connector cuts the build time for the next and removes a renewal objection for more accounts, which is the only argument for eventually revisiting the deleted partner-built rung.

Not subsidizing anyone in phase 1 — there's no complementor yet. In phase 2, the subsidy is free sandbox access and real documentation, nothing more.

Dependency outside your control, dated: Meridian's own IT team providing sandbox/test credentials and confirming their SAP module and version. Request this in week 1 — it is the single item most likely to blow the March date and you don't control it.

## Obligations

- **Surface stability**: version the internal work-order API from day one even though nothing external depends on it yet; state a 90-day breaking-change notice for when it does get published. Owner: integration lead (named, not hired).
- **Roadmap boundary**: Halyard owns and maintains the SAP connector indefinitely — write this down now so that if a partner-built model ever opens later, the switch is announced, not silent.
- **Support and escalation**: a sync failure against Meridian's SAP instance is your incident. Name an on-call owner and an acknowledgement SLA (e.g., 4 business hours) before go-live, given this connector sits directly on a $430k renewal.
- **Review and safety**: none required at this rung — no third-party code executes inside your boundary. This is exactly why this rung is affordable for a 22-person company; don't add review process you don't need.
- **Wind-down terms**: write a 12-month notice period for deprecating the SAP connector now, while it costs nothing, rather than improvising it under pressure if SAP's own field-service module later makes it redundant.

## Measurement

Baseline today: 0 connectors live, 0% of accounts with an active integration, 1 renewal contractually blocked.

Targets:
- SAP connector live and confirmed in writing by Meridian's procurement lead by 27 Feb — one week of buffer before the 6 March deadline, not zero.
- Asset-management connector #2 (highest-overlap system, per CRM pull) scoped by end of Q1, shipped by end of Q2.
- Time from a customer's internal IT team requesting sandbox access to a working test sync under 2 weeks, once phase 2 opens.
- Top-connector concentration tracked, not targeted — if SAP is still 100% of usage a year from now, that's one integration, not a pattern.

## Kill criteria

- If Meridian has not provided SAP sandbox access or confirmed module/version by 16 January, escalate to their procurement lead immediately — the March date is not achievable on the current plan without it, and that's a conversation to have in January, not February.
- If the G2 architecture spike (due within 2 weeks) shows the work-order data model can't be exposed without a core refactor, stop and renegotiate scope with Meridian rather than silently slipping the date.
- Don't start asset-management connector #3 or #4 if, two quarters after #2 ships, fewer than 2 of the 5 asking accounts have adopted it.
- Cap further SAP-surface investment and reassess before building more connectors if SAP visibly bundles field-service dispatch into its own suite (the G6 signal named above).