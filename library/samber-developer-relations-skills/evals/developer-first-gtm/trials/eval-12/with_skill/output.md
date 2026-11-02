# Developer-first GTM — Tilcrest

**The one-line finding:** "A developer is a developer" is true exactly until the CLI has run its first migration. After that moment, Tilcrest already has two different buyers, not one — you've just been reporting them as one. The evidence is in your own prompt: banks and insurers won't touch the product before SSO, audit logs and an MSA exist. That's not a preference a good onboarding flow can smooth over — it's a failing entry gate for that segment, full stop. A single onboarding flow and a single blended conversion number don't unify two developer segments; they hide which one is actually working.

---

## Constraints

- **Business model** has two paid boundaries already operating in practice, not one ladder: a $9/month card-based plan (volume/usage boundary), and an enterprise boundary made of governance features — SSO, audit logs, an MSA. The second boundary is a procurement and legal gate, not a feature toggle.
- **Product friction** differs by segment. Indie devs and two-person consultancies can install a CLI and point it at a database themselves — no approval needed. Platform teams inside regulated institutions cannot: their own security policy blocks any tool from touching anything until SSO/audit/MSA exist. Same product, two different friction profiles.
- **Response capacity** already exists for the enterprise side, whether or not it's named — someone at Tilcrest negotiated the MSAs you already have with banks and insurers. That's a real, working human motion; it's just undocumented and unmeasured. The self-serve side needs zero human touch, and should keep needing zero.

**Open items to confirm before locking numbers** (don't fabricate these — pull them from your own data):
- Who currently handles enterprise conversations, and how many hours a week that realistically is.
- Whether usage can be rolled up to an account today (workspace object, license key, email domain) for either segment.
- Actual contract size on the enterprise side, to run the 4x sales-economics test properly.

## Friction gates, run per segment (this is the load-bearing evidence)

**Indie developers / two-person consultancies**
- Entry — **pass.** Install CLI, point at their own database, generate and apply a migration plan. No account required for the core loop.
- Value — **pass.** One developer sees their own schema change correctly, alone.
- Spread — **pass, likely weak.** Migration files land in the repo and run in CI, so a second developer usually sees them on the next pull or PR check — but nothing forces an invite. Verify the actual share of single-developer accounts at 60 days before assuming this is strong.

**Platform teams, insurance and banks**
- Entry — **fail, by your own account.** SSO, audit logs and an MSA are demanded before anyone is permitted to run the CLI against anything that matters. This isn't a bad first-run experience — it's a procurement block that product polish cannot remove.
- Value — **team/org-scale.** A platform team's value is coordinated, governed schema change across many services, not one developer's local run.
- Spread — not the operative mechanism here. Adoption happens through standardization, not virality.

Two different gate results from two different populations, from your own data: that's the proof "a developer is a developer" doesn't survive first contact with the customer.

## Rejected motions

- **Ecosystem-mediated** — rejected for now. No partner, marketplace or SI relationship named. Revisit only if a cloud marketplace listing becomes a real procurement shortcut for the regulated segment.
- **Developer-influenced sales as the entry motion for the regulated segment** — rejected. This motion requires usage to attribute and threshold on. Banks and insurers generate no usage to threshold on, because they won't start using the product pre-MSA. There's no signal to wait for.
- **One shared onboarding flow (the currently proposed rebuild)** — rejected. An entry designed for a card-swiping indie developer and a compliance-gated platform team at once serves neither: force segment A through security paperwork and you've added the exact approval step that fails their entry gate; force segment B through a $9/mo card flow and you've told a bank's platform team that Tilcrest doesn't understand how they buy, which turns them into an internal opponent before evaluation even starts.

## Primary motion: bottom-up self-serve

**Segment:** indie developers, two-person consultancies.
**Money path:** install → run against own database → adopt in real projects → card, no human ever required.
**Prerequisite:** individual/small-team developers can pay $9/month without anyone's approval — true today.
**What this needs:** self-onboarding CLI, open docs/pricing/limits, in-product upgrade, billing/dunning, per-account usage analytics. No new headcount.

## Secondary motion: top-down with developer proof

**Segment:** platform teams inside insurance companies and banks.
**Why promoted over its normal ranking:** all three override conditions from the skill apply simultaneously — the buyer already funds this category (schema-migration tooling is already inside platform-team budgets), the market is a concentrated, nameable list of accounts (regulated financial institutions), and a compliance mandate decides the purchase, not a developer's preference.
**Money path:** compliance pack satisfies security → pilot on a sandboxed/self-hosted instance with SSO already enabled → architecture-group standardization → MSA.
**What this needs:** a maintained compliance evidence base (SOC2 posture, SSO/RBAC status, sample audit-log output, DPA/MSA template), a named owner, and — the part that's easy to skip — a genuinely good developer experience inside the trial, because a mandated tool developers hate gets routed around and churns at renewal.

These two are the combination the reference material explicitly names as working: a self-serve floor that lets developers adopt willingly, with a top-down motion for the accounts where a buyer signs. Don't try to make the top-down motion primary just because contracts are bigger — it needs a standing job and compliance maintenance; the self-serve motion doesn't, and it's already producing half your usage for free.

## Entry design — the actual onboarding answer

Don't build one flow. Build one shared front door that forks on a real signal, and never make one segment walk through the other's friction.

**Shared, always open regardless of path:** full docs, real pricing (the $9/mo number, plus an honest description of how enterprise pricing works even if it's "talk to us"), all limits, error/troubleshooting content. Both audiences evaluate before they'll talk to anyone — gating this loses technical evaluations silently, on both sides.

**Path A — try it now.** CLI install command on the homepage and in docs. No signup wall. Runs against a local or sandbox database. First-value moment: *a migration plan generated and applied against their own database, in their own terminal.* Count every step between "arrived" and that moment — target removing or deferring anything that isn't required, and defer account/card creation until after value, not before.

**Path B — regulated industry.** Surfaced explicitly (a clear link, not a default), for the segment that self-identifies or arrives from a known enterprise/financial-institution domain. Leads straight to the compliance pack, current SSO/RBAC status, a sample audit-log output, and a request-a-pilot form that routes to a named human — not a card. First-value moment for this path isn't a migration running; it's *a platform engineer's security team accepting the compliance packet*, because that's the actual gate standing between them and touching the product at all.

Never route Path A traffic into Path B's paperwork, and never route Path B traffic into Path A's card flow. That's the concrete fix to "one flow for everybody."

## Handoff rule

**Segment A (self-serve):** no human contact below any threshold. Write the do-not-contact line down and hold it — nobody at Tilcrest emails a $9/mo signup. If, once account rollup exists, an account shows real depth and spread (multiple active contributors, CI integration, sustained volume) suggesting it's outgrowing the $9 plan, that's a future developer-influenced-sales trigger — note it as a revisit trigger, don't build it this quarter on top of the other two changes.

**Segment B (regulated):** the handoff *is* the front door, not a later threshold. The moment someone requests the compliance pack, visits the SSO/audit-log page, or arrives from a known regulated-industry domain, route to a named owner within hours, with a pilot offer — never a generic "learn about your needs" call. Route by role: the platform engineer gets a limits/architecture conversation; the champion gets the enablement pack; security/legal gets the risk answers (license, data handling, SLA, security posture, exit plan) unprompted, before they ask.

## Expansion path

- **Segment A →** more developers on the same team, triggered by a second contributor touching shared migration files; product-owned.
- **Segment B →** more teams inside the same institution, triggered by a new business-unit workspace or an internal referral, once a platform/architecture group standardizes on Tilcrest; owned jointly by the account owner and the champion. Multi-thread every regulated account at two engaged contacts, one manager-level — a single champion at a bank is a single point of failure, and the second, larger purchase will re-trigger security and legal review even after the first MSA is signed. Prepare that paperwork before the expansion conversation, not during it.

## What to report to the board

Kill the single blended free-to-paid number. It's not simplification — it's noise. A near-zero-friction $9/mo motion and a compliance-gated enterprise motion have different shapes, different timelines and different denominators; averaging them produces a number that moves for reasons the board can't diagnose, and can't act on.

Report at minimum two numbers, each cohorted at account level over a consistent window, each labeled with its source:

1. **Self-serve conversion** (indie/consultancy segment). Compare against the *developer-focused company median of 5%* and the pure-freemium self-serve bands of 3–5% (good) / 6–8% (great) — both sourced from Lenny's Newsletter's benchmark survey. This is the correct reference row; a blended B2B benchmark (3–5%/5–7%/8–12% depending on model) will make this segment look broken when it may be performing normally.
2. **Regulated-segment pipeline conversion** — compliance-pack requests → pilots started → signed MSAs. This isn't a freemium funnel at all, since this segment doesn't self-convert on a card; report it as a sales-pipeline conversion, not against a freemium band. Nobody publishes this number for devtools — it's yours to set from your own cohort, and label it self-set, not industry-standard.
3. Once each side has a real paid base, report **net revenue retention separately, per segment**, against the matching band: bottom-up SaaS (~100% good / ~120% great) for the self-serve base, enterprise SaaS (~110% good / ~130% great) for the regulated accounts. A blended NRR number will make a healthy bottom-up base look like it's underperforming an enterprise standard it was never trying to hit.

Cap the full leading-indicator set at five, all moving before revenue: share of installs reaching first migration applied in the first session; self-serve cohort conversion at account level; share of qualified regulated-segment leads contacted within the promised hours window; compliance-pack-request-to-MSA conversion; and, once measurable, the two NRR lines above reported side by side, never merged.

## Refused

No single onboarding flow for both segments. No blended board metric. No outbound to $9/mo signups. No enterprise-only path with no self-serve floor underneath it — that abandons the segment producing half your usage. No self-serve-only motion with no compliance pack — that keeps the regulated segment permanently locked out of a gate they've told you, directly, that they need cleared first.

## Revisit triggers

- Enterprise qualified-pipeline volume grows enough that a dedicated hire clears the 4x fully-loaded-cost bar.
- Self-serve accounts start showing real multi-developer depth at volume — the signal that developer-influenced sales should become the actual secondary motion, not just a note.
- A regulated account's sole champion leaves without a second, multi-threaded contact in place.
- A cloud marketplace or systems integrator emerges as a real channel into regulated accounts — reopen ecosystem-mediated.
- The board metric change itself: if segmented reporting still gets collapsed back into one number at the next deck, that's a signal the process broke, not the numbers.