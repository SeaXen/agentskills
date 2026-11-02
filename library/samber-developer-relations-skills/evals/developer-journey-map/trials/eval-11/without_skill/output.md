# Halloway Developer Journey Map v0.1

**Company:** Halloway (payments API)
**Segment:** Engineers integrating Halloway at e-commerce platforms
**End state:** Production usage (live transaction volume flowing through Halloway)
**Stage model:** five-stage API arc — Awareness → Onboarding → Integration → Production → Advocacy
**Known leak (team consensus, ~1 year standing):** SDK reference docs
**Working assumption:** Onboarding is healthy — near-zero onboarding support tickets. No discovery run on this map; stages are shaped around the known leak, not re-derived from scratch.

---

## Stage 1 — Awareness

**Goal:** Engineer at an e-commerce platform decides Halloway is worth a signup.

**Key actions:** finds Halloway via docs-site SEO, comparison content, a colleague's recommendation, or a sales-assisted lead from the platform's business side; skims pricing and the API reference landing page before committing.

**Exit event:** account created, API keys issued (test mode).

**Signal:** not instrumented in this map — out of scope for the current leak.

---

## Stage 2 — Onboarding *(healthy — not the leak)*

**Goal:** first successful test-mode call.

**Key actions:** reads the quickstart, installs an SDK, sets test API keys, fires a first test transaction (e.g., a test-mode charge or payment intent).

**Exit event:** first successful test-mode API call completes.

**Signal:** support-ticket volume for onboarding is low and has stayed low. Treated as healthy per team consensus — no map changes proposed here.

**Caveat worth carrying forward, not acting on now:** ticket volume measures *escalated* friction, not all friction — an engineer who gets the quickstart working fine but silently struggles later doesn't generate an onboarding ticket either way, so this signal says "onboarding isn't broken," not "onboarding is optimal." Doesn't change where we're pointing the fix; worth remembering if Integration work later doesn't fully close the gap.

---

## Stage 3 — Integration *(the leak)*

**Goal:** wire Halloway into the platform's real checkout/payment flow — beyond the one happy-path call from the quickstart.

**Key actions, in the order engineers actually hit them:**
- Implement webhook receipt and signature verification (async payment confirmation, disputes, refund events).
- Handle the real error taxonomy: declines, network errors, gateway timeouts, idempotency conflicts.
- Add idempotency keys correctly for retries on a checkout flow that itself retries.
- Handle multi-currency and, if applicable, 3DS/SCA challenge flows.
- Implement refunds, partial refunds, and disputes/chargebacks.
- Pick the right SDK method overloads and types for their language (Node, Python, Ruby, PHP, Java, Go — however many Halloway ships).

**This is where the SDK reference docs are the exit path, not the quickstart.** The quickstart carries an engineer through one call. Everything above requires them to live in the SDK reference — and that's the surface the team has flagged as broken for a year. Concretely, reference-doc friction at this stage tends to cluster around:

- **Language parity gaps.** A concept (e.g. idempotency key handling, or a webhook helper) is documented with a code sample in one SDK language and silently missing or stale in others — engineer assumes it doesn't exist in their language and hand-rolls it.
- **Generated-vs-hand-written mismatch.** Auto-generated method signatures (types, required/optional params) drift from hand-maintained prose and examples elsewhere in the same doc set, so the two disagree on what a call actually needs.
- **Thin edge-case coverage.** The happy path (single charge, single currency) is well documented; refunds, disputes, multi-currency, and retries are exactly the material engineers need at this stage and exactly what's thinnest.
- **Error taxonomy not mapped to action.** Error codes are listed, but the reference doesn't say what an integration should *do* on each one (retry-safe vs not, user-facing vs internal) — engineers guess or reverse-engineer it from behavior.
- **Non-runnable samples.** Copy-pasted reference examples don't compile/run as-is (missing imports, placeholder values that aren't obviously placeholders), so trust in the whole reference erodes past the first bad sample.

**Exit event:** integration passes the platform's own internal review/checklist and requests production API keys — i.e., engineer believes they've covered the real-world cases, not just the demo case.

**Signal:** not instrumented — this is the stage the team should start measuring (time-in-stage, doc-page bounce/search patterns, GitHub-issue and community-forum volume against SDK repos as a proxy, since ticket volume likely undercounts self-solved or abandoned friction here the same way it would in Onboarding).

**Where engineers actually go instead of the reference doc, when it fails them:** SDK source on GitHub, GitHub issues/discussions, Stack Overflow, or trial-and-error against the sandbox. None of that shows up as a support ticket, which is consistent with low ticket volume coexisting with a real doc leak — the two aren't in tension.

---

## Stage 4 — Production

**Goal:** first live transaction, then sustained live volume.

**Key actions:** swap test keys for live keys, process first real transaction, monitor error rates and latency under real traffic, scale to full checkout volume.

**Exit event:** live traffic flowing at the platform's expected volume with no open blocking issues.

**Signal:** not instrumented in this map.

**Interaction with the leak:** a rushed or incomplete Integration stage (because the reference docs pushed the engineer to guess rather than confirm) tends to surface here as production incidents — a mishandled error code or a missed idempotency case that only shows up under real traffic patterns. Worth watching whether Production incident volume moves once Integration-stage docs improve.

---

## Stage 5 — Advocacy

**Goal:** renewal, expansion (new payment methods, new currencies, new regions), referral, case study.

**Key actions:** engineer or their team extends usage, becomes an internal reference for other teams at the platform, or refers Halloway externally.

**Exit event:** expansion usage or referral/case-study participation.

**Signal:** not instrumented in this map.

---

## Summary

| Stage | Status | Leak? |
|---|---|---|
| Awareness | not instrumented | no |
| Onboarding | healthy (low ticket volume) | no |
| **Integration** | **not instrumented, but confirmed leak by team consensus** | **yes — SDK reference docs** |
| Production | not instrumented | downstream risk from Integration leak |
| Advocacy | not instrumented | no |

The map confirms the shape the team already believed: the leak isn't at first-call (Onboarding), it's at real-integration (Integration) — webhooks, errors, idempotency, refunds, multi-currency, multi-language parity — exactly the material that lives only in the SDK reference docs and nowhere in the quickstart. Handing off from here for whatever comes next (audit of the reference docs themselves, instrumentation of time-in-stage, or a docs rewrite plan).