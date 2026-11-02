# Vantahold Developer Academy — Plan

## Read this first

Before scoping courses: two of your four signals aren't training problems, and building an academy won't fix them. Ship those two fixes in week one — they're cheaper than a single course module and they stop the bleeding while the academy is being built. Then size the academy to the one signal that actually is an education/activation problem, plus a small pilot for the one enterprise ask. Don't build a full curriculum platform yet — you don't have the ticket volume to justify it, and you'd be guessing at content before you have activation data to point you at what's actually confusing people.

## What the four signals actually mean

| Signal | Real root cause | Right fix | Is this an "academy" problem? |
|---|---|---|---|
| Biggest ticket cluster: "which endpoint returns settlement batches" | Docs *discoverability* failure — the answer exists (page 4 of the reference) but nothing routes people to it. A PDF-style linear reference has no search-by-task path. | Fix information architecture, not content. | No. Fix the docs site, don't write a course about something already documented. |
| 2nd biggest cluster: expired token → generic 400 → ticket | API *error-message* failure. The token flow is fine; the failure mode gives zero signal at the one moment a developer would actually read documentation (mid-debug, in their terminal). | Fix the API response and the SDK's error type. | No. A tutorial can't out-compete a bad error message — nobody reads docs before hitting this, only after, and by then they've already opened a ticket. |
| 62% of signups never complete a first successful API call | Activation failure — no fast path from signup to a working call (Minimum Path to Value). This is the one number that should worry you more than ticket volume, because it's silent churn: these people don't file tickets, they just leave. | Build a real 5-minute quickstart + activation instrumentation. | **Yes** — this is the actual academy-shaped problem. |
| One customer's platform team asked for a training session | n=1 signal for an enterprise enablement gap on complex reconciliation integrations, not evidence of broad self-serve demand. | Pilot a cohort session with that account before building a program around it. | Partially — validate with a pilot, don't build a course library off one request. |

Reframe for your VP: the academy isn't "we don't have enough content," it's "our funnel leaks at three different points, and only one of them is solved by content." Pitch it as a funnel-repair program with an education component, not a training platform.

---

## Phase 0 — Weeks 1–2: Stop the two ticket sources (engineering + docs, not "academy" work)

Do this first. Every day you delay, the academy is being built to compensate for bugs instead of teaching real concepts.

**Fix 1 — Settlement batch discoverability**
- Move "Which endpoint returns settlement batches?" out of page 4 of a linear reference and into three places it can be found from: (a) a task-based "Common Questions" page linked from the docs homepage, (b) the endpoint's own summary line surfaced in on-site search with the literal phrase developers use ("settlement batch," not just the endpoint name `GET /v1/settlements/batches`), (c) an internal redirect/synonym map so searching "settlement batch endpoint" in your docs search returns that page first, not a fuzzy full-text match buried below three other results.
- Add a one-line canonical answer at the top of the endpoint's own reference page: *"Returns settlement batches for a given date range. See also: reconciliation status, batch line items."* — most people asking this question are pattern-matching a name, not reading a description.
- Root-cause check before you ship: pull your docs' internal search logs for the actual query strings people typed. If "batch," "settlement," and "settlements endpoint" aren't already ranking this page #1, that's your bug, independent of content quality.

**Fix 2 — Expired token error**
- Replace the generic `400 Bad Request` with `401 Unauthorized`, error code `token_expired`, and a body that states what happened and what to do:
  ```json
  {
    "error": "token_expired",
    "message": "Your access token expired at 2026-09-20T14:03:00Z. Request a new token via POST /v1/auth/token, or use a refresh token if your integration supports it.",
    "docs": "https://docs.vantahold.com/authentication#token-expiry"
  }
  ```
- If you ship an SDK, give this its own catchable error type (`TokenExpiredError`), not a generic `APIError` — see the "Error Types to Distinguish" pattern; developers currently can't even programmatically detect this case, they're stuck reading a 400 and guessing.
- This single change should visibly dent your second-biggest ticket cluster within the first reporting cycle after release — track it explicitly (see metrics below) so you can show the VP a fast, cheap win before the academy itself ships anything.

Neither of these needs a "course." Building a tutorial titled "Handling Token Expiry" while the API still returns an undifferentiated 400 is teaching people to work around a bug instead of fixing it.

---

## Phase 1 — Weeks 2–6: Academy MVP, targeted at the 62% activation gap

This is the part that's genuinely an education problem, so this is where the academy build starts.

**1. True 5-minute quickstart** (the page that actually moves the 62% number)
- Structure: prerequisites (sandbox API key, one supported language) → one `curl` + one language SDK example that calls a real sandbox endpoint and returns a real settlement reconciliation result → "what just happened" explanation → next steps.
- Ruthless scope cut: the first call in the quickstart should be the single most representative reconciliation action (e.g., fetch a settlement batch and match it against a ledger entry), not an auth-only "hello world." A working call that produces a meaningful result is the actual activation event — define it precisely and instrument it (see metrics).
- Every code block must run unmodified when copy-pasted — test this in CI against your sandbox, not manually once at launch.

**2. Fix the empty state, not just the docs page**
- If signup drops people into a dashboard with no data and no clear first action, that's a second activation leak independent of docs quality. Add a "Make your first API call" prompt with a pre-filled sandbox curl command using their actual generated key — endowed progress (a key that's already there, already valid) removes a whole step versus telling them to go find it.

**3. Onboarding checklist (3–5 items, not more)**
- Example: Generate sandbox key → Make first API call → View a reconciliation result → Set up a webhook → Go live. Order by value, not by setup complexity. Show a progress bar. Celebrate completion of item 2 specifically — that's your activation event.

**4. Instrument before you scale content**
- Add funnel tracking: signup → key generated → first API call attempted → first API call succeeded (200) → second session returns. You cannot tell if the quickstart worked without this, and right now you only have the aggregate 62% — you don't know if people are dying at "never call the API" vs. "call it and get an error" (which loops back into Phase 0's error-message problem).

---

## Phase 2 — Months 2–3: Core guides + enterprise pilot

**Core how-to guides** — task-oriented, not reference-duplicate. Mine your support tickets for the next 3–5 most common questions after the two you already know about (this is now cheap: Phase 1's instrumentation plus a simple "was this page helpful?" widget on the reference tells you where the next cluster is, instead of guessing). Likely candidates for a reconciliation API: handling partial/paginated settlement responses, webhook retry semantics, matching failures and reversals, idempotency on reconciliation writes.

**Enterprise pilot, not a program yet**
- Run the one requested training session as a structured pilot: same content as your quickstart + guides, delivered live, with office hours format. Capture what questions come up live that your self-serve docs don't answer — that's your real signal for whether platform-team-specific content (bulk reconciliation, multi-entity settlement) deserves its own track.
- Only build a recurring enterprise enablement track if 2–3 more accounts independently ask, or if your CS/sales team flags it as a deal blocker. One request is a pilot, not a roadmap item.

---

## Phase 3 — Month 4+: Gate this behind data, don't pre-build it

Do not build yet: certification program, video course library, dedicated LMS platform, or a large multi-module curriculum. These are expensive, slow to produce, and you don't yet have evidence the gap is "developers need deep structured learning" rather than "developers need a working error message and a findable page" — which is what the current data actually shows. Revisit this list only if, after Phases 0–2, your activation rate has moved and ticket volume has *not* fallen proportionally to what Phase 0's two fixes should explain — that would be the actual signal that a deeper knowledge gap exists.

---

## Metrics that decide whether each phase worked

| Metric | Baseline | Target after Phase 0/1 | Why it matters |
|---|---|---|---|
| Tickets tagged "settlement batch endpoint" | current cluster size | -80% within one reporting cycle | Validates it was discoverability, not content |
| Tickets tagged "400 on auth" | current cluster size | -80% within one reporting cycle | Validates it was error-message, not education |
| Signup → first successful API call | 38% (100% - 62%) | +15–20 points | The actual activation metric — the one the VP should track weekly |
| Time to first successful call | unmeasured today | <5 minutes for sandbox users | Quickstart effectiveness |
| Quickstart page completion rate | unmeasured today | baseline first, then improve | Tells you if the page itself is the leak vs. something upstream (signup, key generation) |

Report the first two back to the VP explicitly as "academy program, phase 0" — it reframes two engineering/docs tickets as part of the same initiative and buys credibility for keeping Phase 3 gated instead of rushed.

## Team and cost

Lean on purpose: 1 technical writer (docs IA fix + quickstart + guides), 0.5 backend engineer for 1–2 weeks (error response + SDK error type), existing support/DevRel time for the enterprise pilot. No new platform spend, no LMS purchase, until Phase 3's gate is actually triggered by data.