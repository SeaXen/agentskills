# Developer journey map — e-commerce platform engineers, Halloway, 2026-09-19

## Scope

- **Segment:** engineers at e-commerce platforms integrating Halloway's payments API. One map, this segment only.
- **End state:** production usage — live traffic running through Halloway in a real checkout flow.
- **Stage model:** API and platform five-stage arc — Awareness → Onboarding → Integration → Production → Advocacy. Chosen over Revell six-stage (no standardisation question is being asked here), AAARRRP (no company-wide funnel to reconcile with in this request), and the OSS contributor funnel (end state isn't contribution). It's also the model whose boundaries usually sit in telemetry a payments API already logs — test-mode calls, live-mode calls, sustained traffic.
- **Discovery skipped, by request.** No interview, no friction log, no ticket-cluster count was run for this pass. The leak is entered as given: SDK reference docs, at the integration stage, based on roughly twelve months of standing team consensus. Evidence cells below say so explicitly rather than dressing that consensus up as measured data.
- **Buyer lane: assumed present, not confirmed.** Payments infrastructure typically forces a security/compliance sign-off (PCI-DSS exposure) even on an otherwise self-serve product. That assumption is used below to fill the lane; strike or correct it in the next pass if Halloway's actual go-to-market is fully self-serve.

## Journey

| Stage | Developer's job | Entry trigger | **Exit event** | Touchpoints | **Owner** | Friction evidence | **Signal** |
|---|---|---|---|---|---|---|---|
| Awareness | "find a payments API we can drop into checkout instead of duct-taping the one we have" | search, peer mention, or a marketplace listing (Shopify/WooCommerce app directory, comparison post) | lands on Halloway's docs or API reference | marketing site, docs homepage, search results, marketplace listing | marketing (outside DevRel) | no evidence yet | not instrumented |
| Onboarding | "prove I can process a test charge before I pitch this to my team" | opens the quickstart, creates a sandbox account | first successful test-mode charge via API or SDK | quickstart, sandbox dashboard, API keys page, sample code | developer experience | team-reported: support ticket volume at this stage is low, and the team reads that as "onboarding is fine." Directional only — developers who stall here typically leave without filing anything, so low ticket volume is suggestive, not conclusive. | not instrumented (only signal available is ticket volume, not a rate) |
| **Integration** | "wire real checkout logic into this — webhooks, refunds, disputes, retries, multi-currency — the stuff a test charge never touches" | first test-mode success reached; engineer starts building the real integration behind the storefront | first live-mode call from the production checkout code path | SDK reference docs, webhook docs, error/idempotency docs, support | docs / developer experience (owns the SDK reference) | standing team consensus, ~12 months running, naming the SDK reference docs as the blocker at this stage. Self-reported by the team; no friction log, ticket-cluster count, or exit interview has been run against it yet. | not instrumented — flagged in Gaps |
| Production | "keep this running without getting paged" | first live-mode call observed | sustained live traffic for 14 days with no rollback to the prior processor | dashboards, status page, runbooks, support | product | no evidence yet | not instrumented |
| Advocacy | "tell other e-commerce engineers this saved us the build" | sustained months in production | public talk, post, or unprompted recommendation | community, conference CFPs, changelog, case studies | DevRel | no evidence yet | not instrumented — expect below the 30-event floor; keep as a raw dated list |

All five stages are unmeasured this pass — mark every row's number as inferred where one is asserted at all. This is a known gap, not a hidden one (see Gaps).

## Buyer lane

Assumed present (see Scope caveat) — payments processing commonly triggers a security/compliance step even in an otherwise developer-led motion.

| Buyer stage | Exit event | Owner | Signal |
|---|---|---|---|
| Technical approval | security/PCI questionnaire returned and cleared | security or solutions engineering (outside DevRel) | not instrumented |
| Commercial approval | contract or usage agreement signed | sales (outside DevRel) | not instrumented |

If Halloway is in fact fully self-serve with no compliance gate anywhere, replace this section with "none — the developer decides and integrates directly" rather than deleting it silently.

## Moments

- **First success:** first test-mode charge processed from local/sandbox code. Currently unmeasured for time-to-reach.
- **Moment of truth:** the decision to route real checkout traffic through Halloway instead of falling back to the incumbent processor — sits at the Integration → Production boundary, immediately downstream of the stage the team believes is leaking.
- **Abandonment point:** inside Integration, at the SDK reference docs, per the team's year-long read. Note for the record: this is asserted, not yet observed in a friction log or exit interview — worth keeping in mind before this becomes the permanent story.

## Leak

**Integration**, as instructed. Reasoning that survives even without fresh evidence: Onboarding is reported clean (low ticket volume, team consensus), so Integration is the earliest stage in the model that (a) is claimed to leak and (b) has a clear, single owner — docs/developer experience — who can act on it without needing another team's buy-in first. That satisfies the earliest-and-owned rule the skill uses to pick one leak instead of three.

**Why it leaks (B=MAP):** this reads as an **ability** problem, not motivation or prompt. A developer who has already gotten a test charge working is motivated, and they already know exactly what they need to do next (wire webhooks, handle refunds/disputes, get idempotency and multi-currency right) — nothing needs to prompt them further. What plausibly breaks is the Ability Chain's mental-effort or routine link: if the SDK reference doesn't fully or clearly document error taxonomies, webhook payloads, idempotency semantics, or edge-case currency handling, the engineer is reduced to trial-and-error against a live payments system, which is exactly the kind of task developers abandon or route around by filing a ticket instead of finishing. A copy/positioning fix would be the wrong instinct here; the fix is removing steps or ambiguity from the reference itself.

## Handoff

- **Owner:** docs / developer experience team — they own the SDK reference.
- **Signal to watch:** none instrumented today. Recommended candidate: median time (or share reaching, within N days) from first test-mode success to first live-mode call — it isolates the Integration stage specifically and is a rate the owner can move. A second-best proxy if that's not available quickly: rate of Integration-stage support tickets that cite the SDK reference by name, as a share of Integration-stage tickets overall.
- **Re-read date:** 90 days out — **2026-12-18**, or sooner if the SDK reference ships a rewrite before then.

## Gaps

- **Every stage in this map is unmeasured.** Discovery and evidence-gathering were explicitly skipped for this pass, so no row clears the skill's 60%-signal-coverage bar. Per the skill's own rule, that doesn't block shipping the map — but treat every number above as absent, not as zero.
- **The Integration leak itself is undiagnosed by evidence, only by tenure.** Twelve months of team agreement is a reason to act, but it isn't a friction log, a ticket cluster count, or an abandonment interview — and none of those would tell you *which part* of the SDK reference is the problem (a missing webhook example, an undocumented error code, an idempotency edge case). A single friction log run against the reference docs, or a pull of the last quarter's Integration-stage tickets tagged by section, would cost under a day and turn "SDK docs are the problem" into "this page is the problem" before anyone budgets a docs rewrite.
- **Onboarding's clean bill of health rests on ticket silence**, which the skill flags as its own trap: developers who fail early usually leave without filing anything. Worth a lightweight sanity check (a quickstart cohort's day-1 completion rate, if that's already logged) before treating Onboarding as permanently settled.
- **Awareness and Advocacy have no evidence or signal at all** — both are fully inferred placeholders in this model, not findings.
- **Buyer lane is an assumption, not a confirmed fact about Halloway's go-to-market** — confirm whether a compliance/security gate genuinely exists before anyone builds a signal around it.