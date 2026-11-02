## Sanity check: 3 solid pieces, 2 real problems

**Solid:**
- Prioritizing a concrete, revenue-bearing deal ($180k ARR) over speculative roadmap work is correct triage.
- Enterprise → Team → self-serve sequencing is defensible *if* the $180k deal is contractually real (signed, contingent only on these features) — confirm that before committing two quarters to it.

**🔴 Problem 1 — your roadmap doesn't build what's blocking the deal.**
You said the deal is blocked on **audit logs and SCIM**. The roadmap lists **SSO, RBAC, audit logs, SOC 2** — no SCIM. SSO and SCIM are different protocols (SSO = authentication, SCIM = automated user provisioning/deprovisioning); shipping SSO does not give you SCIM. If SCIM isn't explicitly scoped as its own workstream, you can finish this roadmap and still be blocked on the exact deal you built it for. Fix: add SCIM as a named deliverable, not an assumed side effect of SSO.

**🔴 Problem 2 — "entry tier will be contact us" contradicts having a free tier at all, and contradicts your own "self-serve later" plan.**
"Contact us" belongs on tiers with custom pricing, procurement, and high ACV (enterprise). Putting it on the *entry* paid tier means a developer who wants your cheapest plan has to book a sales call to give you money — for a dev-tool audience that's a top-of-funnel killer, not a qualification filter. It also burns AE time qualifying leads who would've just checked out with a card.
- If the goal is "stop a 500-person company hiding behind a $49/mo plan," the standard fix is a **soft gate** — self-serve checkout with a seat-count/usage field that routes over a threshold to sales — not blocking every entry-tier signup.
- Bigger issue: you said self-serve comes "some time after." But if entry tier is permanently contact-us, there's no self-serve tier to arrive later — self-serve *means* no human in the transaction. Either entry tier gets a self-serve checkout eventually (then don't build contact-us gating now, you'll rip it out), or it stays gated forever (then stop calling the later phase "self-serve"). Resolve which one you actually mean before scoping either build.

**🟠 Worth checking before you commit two quarters:**
- **SOC 2 timeline.** Type I can be done in weeks; Type II needs a 3–12 month observation window with an auditor, independent of your engineering timeline. If the $180k deal requires a full Type II report, that clock may not fit in "two quarters" regardless of how fast you ship SSO/RBAC/audit logs. Check whether the prospect will accept Type I + a contractual commitment to Type II — many will.
- **Single-logo risk.** You're sequencing two full quarters of enterprise infrastructure (SSO, RBAC, audit logs, SOC 2) behind one deal. Do a quick gut-check: is your free-tier funnel big enough that a self-serve team tier would plausibly generate comparable revenue faster, with far less engineering? If yes, deferring it for two quarters has a real opportunity cost. If your free tier is still small/early, enterprise-first is more defensible — but say that explicitly as the reason, since it's the actual tradeoff being made, not just "big deal first."

**Net:** the sequencing logic is fine on its face, but two components of it are internally inconsistent with what you said blocks the deal and what you said you want the funnel to look like. Fix the SCIM gap and the entry-tier/self-serve contradiction before locking the two-quarter plan — both are cheap to catch now and expensive to discover mid-build.