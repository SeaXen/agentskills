# Saltmere Developer Relations Strategy

**Prepared for:** Board Review, [insert date — 11 weeks out]
**Owner:** [Your name], DevRel Lead
**Team:** 2 (DevRel Lead + 1 Developer Advocate)
**Capacity:** 70 hours/month combined (~16 hrs/week)

---

## 1. Executive Summary

Saltmere funds DevRel for one reason: **sales loses technical evaluations it should win.** Not a top-of-funnel awareness problem, not a community-growth problem — a conversion problem at the one stage where a developer or ML engineer sits down with our SDK and decides whether it's real.

This strategy treats DevRel as a **deal-acceleration function first**, and a developer-ecosystem function second. Given 70 hours/month of combined capacity, we cannot run docs, community, content, events, and advocacy at once. We are cutting everything that doesn't move technical-evaluation win rate in the next 11 weeks, and sequencing the rest for after.

**What this document commits to:**
- A diagnostic sprint (weeks 1–2) that replaces assumption with evidence on why technical evals are lost
- Three prioritized program pillars, each with an explicit hours budget, built to close the gaps the diagnostic finds
- A formal operating model with Sales — when DevRel gets pulled in, what we own, how losses feed back into the roadmap
- A board-ready metrics dashboard tied to technical-eval win rate and sales cycle time, not follower counts
- An explicit list of what we are **not** doing yet (open community, events calendar, student program) and why

**The ask:** validate this plan, fund a small tooling/benchmarking budget (Section 12), and give us the 11 weeks to show a measurable shift in technical-eval outcomes before the next capacity conversation.

---

## 2. Why DevRel, Why Now

Saltmere sells an SDK that runs speech models on-device. That single fact shapes everything about how deals are won or lost:

- The buyer is technical by default. Nobody buys an on-device speech SDK without an engineer testing it against their hardware, their audio conditions, and their latency budget.
- The proof burden sits with us, not the buyer. Cloud speech APIs are the default the buyer already trusts; we have to justify the on-device trade-off (privacy, offline, latency, cost-at-scale) with evidence, not claims.
- Technical evaluation is where trust is made or lost. A single unrepresentative benchmark, an undocumented platform gap, or a slow answer to a hard integration question is enough to lose a deal that marketing and sales otherwise won fairly.

The CRO isn't funding DevRel for brand awareness. They're funding it because every lost technical evaluation is a lost deal the sales team already worked to get. That's the mandate, and it's the one this plan is built around.

---

## 3. Diagnosing Technical-Evaluation Losses (Weeks 1–2)

We do not yet know precisely why technical evaluations are lost — only that they are. Before building anything, we spend the first two weeks (a bounded ~12 hours) turning that into evidence:

| Action | Source | Output |
|---|---|---|
| Pull the last 2 quarters of closed-lost deals that reached technical eval | CRM / Sales | Loss reasons, tagged by pattern |
| Interview 3–5 AEs/SEs on the objections they hear most in technical calls | Sales team | Objection frequency ranking |
| Shadow or review notes from 2–3 live technical evaluations in progress | Sales pipeline | Real-time friction points |
| Audit current docs/quickstart against the platforms prospects actually test on | Docs site | Coverage gap map |
| Pull win/loss data by hardware target and competitor, if tracked | CRM | Segment-level pattern |

**Hypotheses to validate, not assume true:**
- Benchmarks (WER, latency, footprint) are either missing, not reproducible on the buyer's own hardware, or not credible against the competitor they're comparing us to
- Platform/hardware coverage in docs lags what's actually being evaluated (e.g., mobile-first docs, embedded/RTOS targets underserved)
- Time-to-first-successful-inference in a POC is too slow, and evaluators stall or default to the incumbent
- Domain/accent/noise-condition customization is unclear, so evaluators assume worse accuracy than reality
- Sales has no fast escalation path to a technical resource mid-evaluation, so momentum dies waiting on us

The diagnostic output becomes the actual brief for Pillars 1–3. **Everything after week 2 gets re-prioritized against what we find**, not against this document's assumptions.

---

## 4. Operating Thesis

DevRel at Saltmere, for the next two quarters, is **evaluation infrastructure for Sales**, built with developer-grade credibility. Three consequences follow:

1. **We build for the evaluator, not the audience.** Every asset — doc, benchmark, sample app — is scoped to what a technical evaluator needs to say yes, not what maximizes reach.
2. **We measure through Sales' pipeline, not through our own top-of-funnel.** Win rate and cycle time on technically-evaluated deals are the metrics that matter. Stars, downloads, and community size are lagging indicators we track but do not optimize for.
3. **We say no to classic DevRel scope until this is working.** Community programs, events, and advocate/ambassador programs are real and valuable — they are also 3-year plays that a 2-person, 70-hour/month team cannot run alongside a live conversion problem. We sequence them in Section 14, not now.

---

## 5. The Evaluation Journey We're Actually Optimizing

Standard developer-journey models (awareness → onboarding → integration → production → advocacy) don't match how enterprise technical evaluations actually run. Ours does:

| Stage | What happens | Where deals die today (to confirm in diagnostic) |
|---|---|---|
| **Qualification** | AE loops in technical stakeholder | Wrong SDK entry point sent, no fast path to relevant docs |
| **Benchmark credibility** | Evaluator checks our accuracy/latency/footprint numbers | Numbers not reproducible on their hardware, or absent for their use case |
| **POC integration** | Evaluator runs our SDK against a real (or representative) audio pipeline | Time-to-first-successful-inference too slow; platform/hardware gap in docs |
| **Objection resolution** | Evaluator raises hard questions (customization, edge cases, licensing at scale) | No fast escalation to someone who can answer credibly |
| **Internal sign-off** | Evaluator has to convince their own team/leadership | We give them no artifact to carry that fight for us |

DevRel's job is to remove friction and supply proof at every one of these five points — and to make sure the evaluator has something to *show their own boss* at the last one.

---

## 6. Objectives & KPIs

**North star:** Technical-evaluation win rate on deals where DevRel is engaged, measured quarter over quarter against a pre-DevRel baseline.

| Tier | Metric | Why it matters | Baseline | 11-week target |
|---|---|---|---|---|
| Lagging (board) | Technical-eval win rate | Direct mandate | [insert current] | [set post-diagnostic] |
| Lagging (board) | Sales cycle length, qualification → technical sign-off | Deal velocity | [insert current] | Reduce by [X]% |
| Lagging (board) | Deals where a lost/at-risk deal was recovered after DevRel engagement | Proof of direct save | 0 (new tracking) | [n] recovered deals |
| Leading (team) | Time-to-first-successful-inference in POC | Predicts stall risk | [measure in diagnostic] | <30 min for top 3 platforms |
| Leading (team) | % of technical objections answered within 1 business day | SLA to Sales | [measure] | 90%+ |
| Leading (team) | Docs/benchmark coverage for platforms actually being evaluated | Root-cause fix | [gap map from diagnostic] | 100% of top 3 eval platforms |

We explicitly do **not** report community size, social followers, or content volume to the board as primary metrics. They appear, if at all, as context in an appendix.

---

## 7. Program Pillars (Prioritized, Hour-Budgeted)

70 hours/month combined. Everything below has to fit inside it — this is a forcing function, not a wish list.

### Pillar 1 — Sales-Embedded Technical Evaluation Support (≈30 hrs/month)
The direct fix for the CRO's mandate.
- Build and own a **technical objection library**: top 10–15 objections from the diagnostic, each with a validated answer, proof point, and owner (starter template in Appendix A)
- Define and staff an **escalation SLA**: any technical question stuck >1 business day in a live evaluation routes to DevRel directly
- Join technical-evaluation calls directly for deals above [insert deal-size threshold] or flagged as at-risk by the AE
- Post-loss debrief on every technical-eval loss: what broke, feed it into Pillar 2/3 backlog

### Pillar 2 — Remove Evaluation Friction: Docs & Quickstart (≈20 hrs/month)
Docs are the highest-leverage, most scalable lever available at this capacity — they work on every deal without a human in the loop.
- Rebuild the quickstart around the 5-minute rule: first successful on-device inference, not a platform tour, per the top 3 platforms evaluators actually test on
- Close the platform/hardware coverage gap the diagnostic surfaces first — this is a fix, not a nice-to-have, if it's confirmed as a loss driver
- Publish copy-paste-tested sample integrations for the top 3 evaluation environments (mobile, and whichever embedded/edge target shows up most in lost deals)
- Every doc page a technical evaluator lands on mid-eval gets a direct "ask a human" path back into Pillar 1's SLA

### Pillar 3 — Credible Proof Artifacts: Benchmarks & Reference Architectures (≈15 hrs/month)
Directly targets the "your numbers aren't credible/reproducible" failure mode.
- Publish a benchmark methodology page: hardware used, audio conditions, how to reproduce it yourself — reproducibility is the credibility lever, not the headline number
- Keep benchmarks segmented by the conditions buyers actually care about (accent, noise, domain vocabulary) instead of one blended number
- One reference architecture doc per top evaluation platform, showing the integration a buyer's engineering team would actually ship, not a toy demo

### Pillar 4 — Lighthouse Technical Advocates (≈5 hrs/month, opportunistic only)
Not a champion program — capacity doesn't support one. A narrow, low-effort version:
- Identify 2–3 engineers at already-won customers willing to take a reference call or give a quote for a specific vertical/hardware target
- No content quotas, no swag program, no formal tiering — a short list Sales can call on when a live evaluator wants to hear from a peer, not from us

### Deferred — Not in Scope for the Next 11 Weeks
Named explicitly so the board sees this as a decision, not an oversight:
- **Open community (Discord/Slack, forums):** valuable eventually, but scaling community support costs more capacity than we have while the conversion problem is unsolved
- **Events, conferences, hackathon sponsorship:** high cost per hour of the 70, low direct line to technical-eval win rate at this stage
- **Champion/ambassador program, content bounties, student program:** all real 1–3 year plays (see Section 14) — starting them now would dilute the only mandate currently funded

---

## 8. Team & Capacity Model

| Person | Primary allocation (of 70 hrs/month) |
|---|---|
| DevRel Lead | Pillar 1 ownership (~20 hrs), Sales operating model, board reporting, diagnostic synthesis |
| Developer Advocate | Pillar 2 + 3 execution (~30 hrs), objection library co-maintenance, lighthouse advocate outreach |
| Shared | Post-loss debriefs, diagnostic sprint (weeks 1–2 only) |

**RACI with Sales for technical evaluations:**

| Activity | Sales (AE/SE) | DevRel |
|---|---|---|
| Qualify and loop in technical stakeholder | R/A | Informed |
| Answer known/documented objections | R | Consulted (owns the library) |
| Answer novel/unresolved technical objections | Informed | R/A |
| Escalation on stalled POC | R (flags it) | A (resolves within SLA) |
| Post-loss debrief | R (attends) | A (runs it, owns follow-up) |

This table exists because ambiguity about who owns a stuck technical question is itself a loss driver. Everyone at Saltmere who touches a technical evaluation should be able to point to this table.

---

## 9. Sales Partnership Operating Model

- **Trigger for DevRel engagement:** any deal that reaches technical evaluation and (a) exceeds [insert deal-size threshold], or (b) is flagged by the AE as at-risk, or (c) hits an objection not yet in the library
- **SLA:** documented/known objections answered same-day by Sales using the library; novel objections escalated to DevRel with 1-business-day response
- **Feedback loop:** every technical-eval loss gets a debrief within 5 business days; findings update the objection library, docs backlog, or get routed to product as a roadmap input — losses are not filed away, they're the primary input to this whole plan
- **Win loop too:** every technical-eval *win* gets a 10-minute debrief for what worked, so Pillar 1–3 investment tracks what's actually converting, not just what's failing

---

## 10. 11-Week Roadmap to Board Review

| Weeks | Focus | Deliverable |
|---|---|---|
| 1–2 | Diagnostic sprint | Loss-reason ranking, objection frequency, platform gap map, baseline metrics set |
| 3–4 | Build core assets | v1 objection library, SLA live with Sales, quickstart rebuild scoped |
| 5–7 | Ship & pilot | Quickstart + top-platform sample integrations live; benchmark methodology published; DevRel joining live evaluations |
| 8–9 | Iterate on real deals | Adjust objection library and docs from real post-loss/post-win debriefs; lighthouse advocate list assembled |
| 10 | Data close-out | Pull win-rate and cycle-time delta against baseline; compile board metrics |
| 11 | Board prep | This document finalized with real numbers, dashboard built, ask defined |

---

## 11. Metrics Dashboard for the Board

Presented as a single page, four numbers plus context:

1. **Technical-eval win rate** — baseline vs. current, deals where DevRel was engaged vs. not
2. **Sales cycle length** for technically-evaluated deals — baseline vs. current
3. **Deals recovered** — specific, named (anonymized if needed) instances where DevRel engagement reversed an at-risk evaluation
4. **Leading indicators** — time-to-first-successful-inference, objection SLA compliance, doc coverage — shown as the mechanism behind the lagging numbers, not as headline metrics themselves

No follower counts, no star counts, no content-volume metrics on this page. If asked, they're in the appendix as context, explicitly labeled as not the thing we're optimizing for.

---

## 12. Budget & Tooling Ask

Beyond the existing 2 headcount, this plan needs a small, specific budget — not a headcount ask yet:

| Item | Purpose | Est. cost |
|---|---|---|
| Benchmark hardware (representative of top eval platforms) | Reproducible, credible benchmarks | [insert estimate] |
| Docs platform / search analytics upgrade, if current one lacks it | Track quickstart completion, search gaps | [insert estimate] |
| Small reference/reward budget for lighthouse advocates (no formal program, but real thank-yous) | Sustain the 2–3 reference relationships | [insert estimate] |

Total ask: [insert total] over the 11-week period. No community platform, no swag program, no event budget requested at this stage — consistent with Section 7's deferrals.

---

## 13. Risks & Mitigations

| Risk | Mitigation |
|---|---|
| Diagnostic finds the real driver is a product gap, not a DevRel-fixable one | Route findings to product immediately in week 2; don't force a DevRel fix onto a product problem — report it plainly to the board |
| 70 hrs/month proves insufficient once real deal volume hits the SLA | Track SLA breach rate explicitly; use it as the evidence base for a future capacity ask, not an assumption |
| Sales doesn't adopt the objection library or escalation path | Co-build it with the AEs/SEs interviewed in the diagnostic, not for them; revisit adoption at week 4 checkpoint |
| Benchmark numbers, once public, get contested by a competitor or a buyer's own testing | Publish methodology openly so our numbers are defensible by being reproducible, not just asserted |
| 11 weeks isn't enough for win-rate to move on slow enterprise cycles | Report leading indicators honestly as the interim proof; frame win-rate as a trailing confirmation still in progress, not fabricate an early win |

---

## 14. Beyond the Board Review: 6–12 Month Trajectory

This plan is deliberately narrow. Once technical-evaluation win rate shows sustained improvement, the sequencing for expansion — contingent on additional capacity, not assumed —:

- **Months 3–6:** Formalize the lighthouse advocate list into a small, invite-only champion program (Pillar 4 → real program) once Pillar 1–3 no longer consume most of the 70 hours
- **Months 6–9:** Open a narrow, low-maintenance community surface (likely GitHub Discussions or a single Slack channel, not a full Discord) scoped specifically to technical-eval and integration support — community as scaled version of Pillar 1, not a separate initiative
- **Months 9–12:** Revisit events/conference presence, scoped to the specific technical communities where our top eval platforms' engineers actually are, not general developer marketing

Each step is gated on the current pillar proving out and freeing capacity — not on a calendar. The board ask at that point will be capacity (a third hire), justified by SLA breach data and win-rate trend from this plan, not by aspiration.

---

## Appendix A — Objection Library Starter (to populate from diagnostic)

| Objection (hypothesis — confirm in diagnostic) | Real concern | Response owner | Proof point |
|---|---|---|---|
| "Your accuracy numbers don't match what we're seeing on our hardware" | Distrust of benchmark methodology | DevRel | Reproducible benchmark methodology doc |
| "You don't document our target platform/chipset" | Integration risk, timeline risk | DevRel (docs) | Platform coverage roadmap + workaround |
| "How does this handle our specific accent/domain vocabulary?" | Fit-for-purpose doubt | DevRel + SE | Customization guide, segmented benchmark |
| "Cloud API X is already proven at our scale" | Switching risk | Sales + DevRel | Reference customer at comparable scale |
| "What's the real cost at N million devices?" | Pricing/licensing clarity | Sales | Licensing model doc, TCO comparison |

*(Full library to be built from actual diagnostic findings in weeks 1–2 — this is a starting shape, not a finished artifact.)*

## Appendix B — Glossary

- **Technical evaluation:** the stage where a prospect's engineer(s) test the SDK against their own hardware, audio conditions, and integration requirements before internal sign-off
- **Time-to-first-successful-inference:** time from SDK install to first working on-device inference in a realistic POC setup
- **Lighthouse advocate:** a customer engineer willing to speak informally to a prospect, without a formal program structure