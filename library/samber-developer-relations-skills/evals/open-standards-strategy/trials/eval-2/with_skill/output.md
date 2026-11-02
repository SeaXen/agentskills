Using **open-standards-strategy** to decide Helvar's posture toward FleetLink 2.1.

Core move: this is **two decisions on two horizons bundled into one question**. Don't let the urgent one drag the strategic one along for the ride.

---

## Decision 1 — FleetLink 2.1, for the renewal (11-week clock)

**Landscape**

- Spec: FleetLink 2.1, owned by an industry consortium (not IETF/W3C/Git-based). Venue is a given here, not a choice — the spec already exists and procurement already named it.
- ℹ️ **Unverified, check this week:** does *implementing* FleetLink 2.1 require the EUR 48k membership, or is the spec publicly implementable and only the vote/TC-seat is gated behind membership? Many consortia decouple these — Khronos lets non-members become certified "Adopters" for a separate, much smaller fee. If FleetLink works the same way, you may not owe EUR 48k at all to close this deal.
- ℹ️ **Unverified:** does a conformance suite / certification mark exist? If procurement's "hard requirement" means a checkable certification claim on paper, you need Conform, not just Consume. If it means "interoperates with our robots," Consume is enough. Ask the customer's procurement contact directly which one they mean — it's the cheapest fact you can buy this week.
- Demand: one named customer, EUR 1.4M, contractually forcing the question. That clears the demand test on its own.

**Four tests**

- **Demand:** passed — named account, dated, real money.
- **Commoditization:** FleetLink is the wire format between your orchestrator and the robots/WMS around it — not what you sell. You sell the orchestration logic on top. Commoditizing the interop layer *helps* you (cheaper integration → more fleets you can sit on top of), so you are not capped at Extend the way you would be if FleetLink were your own product.
- **Control:** irrelevant here — there's no rival spec and no war. FleetLink isn't contested; it's just required. Skip the seven-asset scoring and the standards-war framework entirely — they only fire when an incompatible rival technology is fighting for the same adopters.
- **Cost:** two engineers, bounded implementation task, fits inside 11 weeks. This is an engineering sprint, not consensus-venue participation — treat it as such.

**Posture: Consume, upgrading to Conform only if the certification mark is what procurement literally wants.**

Not Contribute. An 11-week deadline is inside two quarters — that alone deletes Contribute, Co-found, Drive from this decision. Don't let "we're implementing FleetLink anyway" slide into "so let's also join the TC" — that's a different horizon, different cost, different evidence bar. Handle it in Decision 2.

**What to do with the two engineers, starting next week**

| Weeks | Work |
|---|---|
| 1–2 | Read FleetLink 2.1 spec + IPR terms; confirm with the consortium (not just the customer) whether implementation needs membership; gap-analysis against your current internal message model |
| 3–6 | Build the FleetLink 2.1 client (produce + consume messages) |
| 7–8 | Integration test against the customer's actual fleet or a reference robot vendor |
| 9–10 | Procurement documentation; conformance test run only if the mark is required |
| 11 | Buffer / close |

That leaves ~1 week of slack against the deadline — tight, not reckless.

**Conformance plan (only if Conform is triggered)**

- Certify against 2.1 specifically, note the version and expiry — don't let an unversioned claim quietly outlive the spec once 3.0 ships.
- Get listed in the consortium's public registry if one exists — that's what a procurement/legal reviewer actually checks, not your claim.
- Prefer self-service testing over witnessed, if offered — cheaper, faster, no standing obligation.

**KPIs / kill rule**

| Metric | Threshold | Sourced / baseline | By when |
|---|---|---|---|
| Client passes interop test against customer's fleet | 100% of message types in their procurement spec | baseline | week 10 |
| Certified + listed in public registry (if required) | done before signature | baseline | week 10–11 |
| Engineering spend | ≤ 20 engineer-weeks | baseline | ongoing |

Kill rule: if the spec turns out to require witnessed certification or a materially larger scope than expected by week 6, escalate to the customer for a short extension rather than silently slipping — don't discover this in week 10.

---

## Decision 2 — VP Eng's ask: join the technical committee for FleetLink 3.0

Defer this. Don't decide it this week, and don't fund it out of renewal urgency. Reasons, by the skill's own logic:

- **Horizon is right, evidence isn't.** ~2 years to 3.0 is a legitimate Contribute horizon — this isn't premature on timing. But right now your counted demand for FleetLink is **one customer**. That's enough to justify Consume (cheap, reversible). It is thin justification for EUR 96k+ over two years plus a named engineer's sustained multi-year attendance — Contribute is priced in years of standing commitment, not a sprint.
- **No named outcome yet.** "Get a say in 3.0" is exactly the failure mode the skill calls out: influence goes to whoever shows up with a specific text change and stays for it. Before joining, VP Eng should be able to name the actual FleetLink 3.0 change Helvar wants — a message type, a versioning guarantee, whatever it is. If nobody can name it, the seat buys attendance, not influence.
- **IPR mode is unverified and semi-permanent.** ℹ️ Find out whether this consortium runs RAND, RF-on-RAND, RF-on-Limited-Terms, or a non-assertion covenant before joining — the mode can't be changed without re-chartering the whole committee. If Helvar holds or might hold any patents adjacent to fleet messaging, this goes to counsel first, not engineering.
- **Commoditization test doesn't block it** — since FleetLink isn't Helvar's differentiator, Contribute (or even Drive, if the assets were there) isn't foreclosed the way it would be if you standardized your own product. So this isn't a "never" — it's a "not yet, not on this evidence."

**Revisit trigger:** after the renewal closes, run a real pipeline check — how many other deals/RFPs in the next two quarters also name FleetLink. If it's several, not one, and VP Eng can name a specific 3.0 change to push for, re-run this as its own decision with its own venue/IPR/staffing review. Until then, the free version of "keeping a say" is watching the consortium's public output and draft revisions — costs nothing, buys situational awareness, doesn't commit two years of headcount to a single customer's ask.

**Baseline kill rule for that future review:** fewer than ~3 additional named deals citing FleetLink within 2 quarters, or no specific 3.0 change identified → don't join; keep monitoring publicly instead. (Baseline — replace the "3" with your actual pipeline data; I don't have it.)

---

## Bottom line

- **This week:** verify (a) does implementing FleetLink 2.1 require the EUR 48k membership, (b) does procurement want functional support or a certified mark, (c) the consortium's IPR mode.
- **Next 11 weeks:** two engineers build a FleetLink 2.1 client (Consume, upgrading to Conform only if the mark is explicitly required). This is the only thing standing between you and the EUR 1.4M renewal — treat it as a bounded engineering sprint, not a standards commitment.
- **Not this week:** the TC seat. Same standard, different decision, different horizon, different evidence bar. Revisit it after the renewal closes with real multi-customer demand and a named 3.0 ask — not as a rider on this deal's urgency.