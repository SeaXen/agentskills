Using the developer-journey-map skill to answer the sanity check and draft the map opening.

## The sanity check: don't open with those two comparisons

Both benchmarks fail before they reach the VP.

**"40-60% is normal quickstart conversion"** — no such figure exists as a citable benchmark. Every per-stage conversion rate in circulation for API/quickstart products is a single company's anecdote, with its own audience, product maturity, and definition of "started" and "succeeded." There is no methodology behind the 40-60% band anyone has published. Citing it against Northwind's 28% is comparing your funnel to a rumor, and any VP who's seen this kind of deck before will ask "whose number is that" and you'll have no answer.

**"20-40% is standard self-serve activation"** — this one is explicitly a figure this class of claim gets refused for. The most detailed public study on this exact question (OpenView's 2023 developer-tools benchmark survey, 1,000+ respondents) *declines to publish one activation rate at all*, on the stated grounds that the milestone differs by product — a Loom share, a Zapier zap, and a Kafka topic-create-and-consume are not the same unit of value. The two real numbers closest to your metric measure different things entirely:
- Lenny Rachitsky / Yuriy Timen's 2022 survey (500+ products, self-reported, "activated ÷ completed signups," milestone required to show ≥2x retention): median 25%, average 34% overall — but that's a self-reported panel, not an instrumented measurement, and "activation" there is whatever each company decided moved retention.
- Amplitude's 2025 B2B benchmark (2,600+ companies' actual instrumented data, Sept 2023–Sept 2024): day-7 return rate — a different definition again — puts the *median* B2B technical product at 2.1%, and 7% at the top quartile.

Both of those bracket 22% on the *generous* side under one definition and make it look exceptional under another. Neither supports "20-40% is standard." The round number floating around collapses two incompatible metrics into one folklore figure — that's a documented failure mode, not a gap in your data.

**Second finding, more useful than the first:** these two internal numbers may not even be two stages of one funnel. "28% of quickstart starters" and "22% of all signups within 7 days" have different denominators and different windows. Unless you already know what share of signups start the quickstart at all, you can't tell whether these are consistent (e.g., if 90% of signups start the quickstart, 28% of that ≈ 25% of signups — close to 22%, one coherent story) or wildly inconsistent (if only 40% start it, 28% of that is 11% of signups, meaning most of your 22% activation is happening *outside* the guided quickstart — a materially different and more interesting finding about where value actually gets delivered). Get the quickstart-start rate before either number goes in front of the VP as a stage-to-stage comparison — right now they're two point-in-time facts, not two rows of a funnel yet.

**What should open the map instead:** your own numbers, against your own history, full stop — "28% of quickstart starters reach first success, 22% of signups activate within 7 days; no external benchmark exists for either, and here is what we're doing about the lower of the two." That is a stronger opening than a fabricated gap, because it can't be shot down by someone Googling the 40-60% figure and finding nothing behind it.

---

# Developer journey map — backend engineers, Series-A–C startups, 2026-09-19

## Scope

- **Segment:** backend engineers at Series-A to Series-C startups.
- **End state:** production usage.
- **Stage model:** API and platform five-stage arc — Awareness → Onboarding → Integration → Production → Advocacy.
- **Deleted:** Revell six-stage (terminal stage is standardization, not production usage — no evidence this is an organization-adoption question); AAARRRP (terminal stage is revenue, and the funded question here is technical activation, not a company-wide monetization funnel); Orbit levels (terminal stage is advocate, says nothing about evaluation or production); OSS contributor funnel (end state isn't contribution). The API arc is also the cheapest to instrument here — first call, integration and production usually already sit in product telemetry, and Northwind already has two of those five signals.
- **Open items not yet confirmed** (this draft was built from the two numbers given, not a full interview — confirm before treating this as final):
  - Buyer lane: assumed **none — self-serve** for this segment (Series-A–C, backend engineer as decider), pending confirmation of whether any tier requires security review or procurement.
  - Whether this is a first map or a refresh — no prior version referenced, treated as first.
  - Effort ceiling and re-run cadence — defaulted to this skill's 90-day baseline.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Awareness | "find a Kafka alternative I don't have to operate" | search, peer mention, or comparison post | signs up / lands in the product | search, docs, comparison pages | Marketing | no evidence yet | not instrumented |
| Onboarding | "prove produce-and-consume works before I touch our real services" | opens the quickstart | **first successful produce-and-consume call** | quickstart, SDK install, API keys, dashboard | Developer Experience | no evidence yet | **28% of quickstart starters reach first success** |
| Integration | "wire this into a real service, topic and all" | first success reached | topic created + message consumed, wired outside the quickstart sandbox | SDK reference, topic config, error docs, support | Product | no evidence yet | not instrumented — the 22%/7-day activation figure likely straddles this stage and Onboarding; see Gaps |
| Production | "run this on call, for real traffic" | integration observed | sustained production traffic for a stated window plus alerting configured | runbooks, status page, limits docs, support | Product / SRE | no evidence yet | not instrumented |
| Advocacy | "tell other backend engineers it replaced our Kafka pain" | sustained time in production | public talk, post, or unprompted recommendation | community, CFPs, changelog | DevRel | no evidence yet | not instrumented |

Awareness, Integration, Production and Advocacy are unmeasured, not "inferred" — there's no proxy number for them yet, they're simply dark. That's flagged in Gaps, not papered over.

## Buyer lane

None — self-serve, provisionally. Backend engineers at this company stage are typically the decider without a formal procurement step. State explicitly if any paid tier actually routes through security review or a champion/buyer split — if so, this needs its own lane with its own owner before the map is final.

## Moments

- **First success** — first produce-and-consume call from the quickstart. Time-to-first-success not given; get it, it's usually the single most-watched number on this kind of map.
- **Moment of truth** — provisionally, topic-created-plus-consumed *outside* the quickstart sandbox, i.e. wired into a real service — this is where "I proved it works" becomes "I'm building on it." Confirm this is really what "activation" is measuring; if activation still happens inside the guided quickstart, the moment of truth hasn't been observed yet at all.
- **Abandonment point** — unknown. Nothing in the data given says *where* the 72% of quickstart non-completers or the 78% of non-activators actually stop. This is exactly what a friction log or three abandonment interviews would surface, and right now it's a guess either way.

## Leak

**Provisional nomination: Onboarding**, on the numbers available — it's the earliest stage with both a measured rate and a named owner (Developer Experience) able to change it. But this nomination is weaker than usual for two reasons, both worth saying to the VP rather than hiding: Integration and Production are completely dark, so a worse leak downstream can't be ruled out; and the 22% activation figure may not even be Onboarding's number — it may belong to Integration, or straddle both (see Gaps). Treat this as "best current read," not a settled diagnosis, until the reconciliation work below happens.

Why it leaks (B=MAP, applied only after the stage is picked, not before): most likely **ability**, not motivation — nobody who reaches produce-and-consume lacks a reason to try it, so the default developer-audience answer applies until a friction log says otherwise. Don't reach for a motivation fix (landing-page copy, a value-prop banner) without first walking the quickstart yourself and logging where the 11-minutes-on-auth-style friction actually sits.

## Handoff

- Owner of the fix: Developer Experience.
- Signal to watch: share of quickstart starters reaching first success (currently 28%), plus — once instrumented — quickstart-start rate as a share of signups, needed to reconcile against the 22% activation figure.
- Re-read date: 90 days (2026-12-19), or sooner if the quickstart, SDK, or activation definition changes.

## Gaps

- **Awareness, Integration, Production, Advocacy** — not instrumented. Each needs either product telemetry already logged but not surfaced, or a first pass of qualitative evidence (friction log, support-ticket clustering, exit interviews) before it can carry a real signal.
- **Quickstart-start rate** (% of signups who open the quickstart) — the single missing number needed to check whether 28% (of starters) and 22% (of signups, 7-day window) describe one consistent funnel or two very different populations. Pull this before the next version of this map, and before repeating either number to the VP as part of a "stage-to-stage" story.
- **Activation's true stage boundary** — confirm whether "topic created + message consumed within 7 days" happens inside the quickstart flow or after it, in real integration work. This decides whether it's Onboarding's exit event restated with a longer window, or genuinely Integration's.
- **Buyer lane** — confirm self-serve assumption; check if any tier has a security-review or procurement gate.
- **Friction evidence for every row** — none gathered yet. A single friction log run on the quickstart this week would upgrade the whole Onboarding row from "signal only" to a defensible root cause.

**Quality gate, reported explicitly:** fails signal coverage (2 of 5 stages carry a real value, well under the 60% baseline) — shipped anyway per this skill's own rule that an honest map with holes beats a complete map with invented numbers. All five stages have exactly one exit event and one owner outside DevRel is named (Developer Experience, Product, Marketing, SRE). Exactly one leak nominated, with owner and re-read date, explicitly marked provisional given the coverage gap. No friction claim is dressed up as evidence — every row says "no evidence yet" rather than a guess.