# Opening Halyard's platform — Meridian by 6 March, then repeatable

## The one decision that governs everything

Don't build a SAP connector. Build **one versioned, documented API + sandbox**, and let Meridian's own SAP team (or their integrator) build the SAP-side adapter against it. You have 22 people and 9 weeks — you cannot become SAP integration experts in that window, and you don't need to. Utilities running SAP for work orders already have SAP PI/PO, Integration Suite, or a middleware layer (Boomi/MuleSoft/Workato) and staff who operate it. Your job is to give them a stable, well-behaved surface to point that tooling at.

This choice is also what makes the CTO's two constraints compatible with each other:

- **"Nothing we can't withdraw from"** → you're committing to an API contract (versioned, deprecable with notice), not to a SAP partnership, a middleware vendor, or a bespoke integration SOW.
- **"No security review function"** → a public API with scoped tokens, a design checklist, and one contracted pentest is a fixed, bounded cost. A team that reviews every customer's SAP environment and every future connector by hand is not — it's the beginning of headcount you said you won't add.

Same shape solves Meridian and the other five accounts. The three EAM systems become adapters other people build against your API, not three more things your team maintains.

## Translating "no irreversible commitments" into specific choices

- Amend the Meridian contract via an order-form addendum with **mutual termination for convenience** (30–60 days), not a standalone integration SOW with its own exit terms.
- No uptime SLA or financial penalty clause tied to the integration. Commit to the API contract's behavior, not to availability numbers you haven't operated at scale yet.
- No exclusivity, no data residency promise, no multi-year term extension bundled into the amendment just to "lock in" the renewal — that trades a reversible problem for an irreversible one.
- Do **not** pursue SAP Certified/Endorsed App status now. That's a multi-year partnership commitment with SAP and it's not on the critical path — Meridian's SAP layer calling your REST API doesn't require it.
- If you need to move faster than in-house build allows, use a middleware vendor (e.g. for the sandbox/webhook layer) on month-to-month or annual-with-short-notice pricing. No multi-year platform license.
- Pentest and compliance-questionnaire vendors: pay per engagement, not a retainer. Bounded, one-off, reversible.

## What "security review" becomes without a security function

You're not staffing a function — you're building review into things that already have a fixed cost and don't scale with headcount:

1. **Architecture does the work**: scoped OAuth2 client-credentials tokens per customer, least-privilege endpoints (work order + asset data only, nothing broader), per-tenant isolation, IP allow-listing or mTLS for the SAP-side caller, audit logging, secrets rotation. This is what a reviewer would ask for anyway — bake it into the design so there's less to review.
2. **One checklist, reused every time**: OWASP API Top 10 + your own least-privilege/logging/rotation items, run as a design-review gate by you (CTO) plus one senior engineer before anything ships. Not a team — a 90-minute meeting per connector.
3. **One external pentest, contracted now**: book a scoped API security assessment this week (boutique firms can often turn around a focused engagement in 2–3 weeks if booked early). Fixed cost, fixed timeline, defensible artifact for procurement.
4. **Reuse, don't repeat, the compliance ask**: fill out one vendor security questionnaire (CAIQ-lite or Meridian's own form) and the pentest summary letter once. That packet is what you hand every future prospect asking about the same three EAM integrations — it's the artifact that scales, not a person.
5. **Skip SOC 2 for this deadline.** Type II takes 6–12 months of evidence; Type I is tight even at 9 weeks and likely isn't what Meridian's procurement lead is actually asking for. Confirm what they need in writing (see Week 1) before spending a dollar on it — don't assume.

## Timeline to 6 March (9 weeks from 2 Jan)

**Week 1 (2–9 Jan) — the highest-leverage week of the whole plan**
- Get Meridian's procurement lead and their SAP/integration team on a call. Get **in writing** exactly what "working integration" means: which data (work orders, status, completion, asset master?), which direction (push, pull, both), what counts as done, what their acceptance test looks like. "Working integration with SAP" is vague enough to blow the budget either by overbuilding or by missing what they actually meant — this call is the single highest-leverage action available this week.
- In parallel: book the external pentest firm. Draft the contract amendment with legal (termination-for-convenience language, no SLA penalty).
- Assign 1–2 backend engineers full-time to this through cutover. Don't hire.

**Weeks 2–4** — Design and build the versioned API: work order CRUD, status webhook, asset lookup, scoped auth, sandbox environment. Run the internal checklist review before Meridian's team starts integrating against it.

**Weeks 3–5 (parallel)** — Pentest runs against the sandbox. Fix findings as they land, don't batch them for the end.

**Weeks 4–6** — Meridian's SAP/middleware team (or their integrator) builds against your sandbox. Joint UAT starts as soon as the API is stable, not after it's "finished" — surface mismatches in what Week 1 promised early enough to fix them.

**Weeks 6–7** — Buffer for fixes. Deliver the security questionnaire + pentest summary to Meridian's procurement.

**Weeks 7–8** — Production cutover, monitoring on, sign-off from Meridian's side.

**Week 9 (by 6 March)** — Renewal signed, integration live, and you now have: a documented API, a sandbox, a review checklist, and a security packet — all reusable for the next five deals with no new hire.

**If Week 1 reveals you can't hit full bidirectional sync in time**: propose a phased Phase 1 (e.g. one-way status webhook + nightly reconciliation batch) as what ships for the 6 March renewal, with a written joint roadmap to full sync after. A phased, written scope is reversible and honest; a rushed full build that breaks under Meridian's real SAP traffic is not.

## Setting up the other five accounts / three EAM systems

- The API you build for Meridian is not SAP-specific in its bones — work orders and assets are the same shape whether the far end is SAP or an EAM system. Keep SAP-specific logic (IDocs, BAPIs, whatever Meridian's side needs) entirely on Meridian's side of the boundary.
- Publish the docs, sandbox, and auth flow as a standing "integration" page once Meridian is live. The next five customers' own IT teams or integrators self-serve against it — you're not scoping five bespoke projects.
- Keep a short list of 1–2 integration consultancies you can point customers to if they don't have in-house SAP/EAM capability. That's a referral, not a subcontract — no commitment on your side.
- Reuse the security questionnaire + pentest letter as-is for every subsequent deal. Re-run the pentest annually or on material API changes, not per customer.
- Decide whether a dedicated integrations role is justified only *after* Meridian proves the pattern holds and the pipeline of five materializes into signed work — don't staff ahead of evidence.

## What not to do

- Don't build a bespoke SAP adapter in-house — that's the fastest way to blow 9 weeks and end up needing the SAP expertise you don't have.
- Don't sign anything with SAP itself, a certification program, or a middleware vendor that runs longer than a year or lacks an exit.
- Don't let "security review" become a role requisition — it's a checklist, a contracted pentest, and a reusable questionnaire packet.
- Don't skip the Week 1 scoping call to save time — it's the one step that determines whether the other eight weeks are spent on the right thing.