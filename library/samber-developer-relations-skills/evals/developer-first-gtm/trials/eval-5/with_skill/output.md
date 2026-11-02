Skill loaded: `developer-first-gtm`. Given your last line asked for the deliverable itself, I ran the workflow without the step-by-step interview — stated facts from your prompt are used as given; anything I had to assume is flagged inline as **[assumed]** so you can correct it. Full memo follows.

---

# Developer-first GTM — Parapet

## Why "we should do PLG" is the wrong starting point

Your team's instinct is exactly the failure mode this kind of product hits hardest: bottom-up sounds cheap, so it gets assumed instead of tested. Run the actual entry gate — can a developer reach real value with no account, no approval, no call — and Parapet fails it structurally, not temporarily:

- First value requires a platform engineer to review and apply an admission controller into their cluster. That is a real approval step and a real infrastructure step. No onboarding polish removes it — the product sits in the request path of every pod creation, which is inherently something a platform team must sign off on.
- The product is not useful below three onboarded services. That is not "team-scale" value (a shared dashboard, a config in the repo) — it is a coverage threshold. A single self-serve user gets close to nothing.

Both facts, independently, rule out "download it and self-serve to value" as the revenue motion. PLG-as-reflex would spend a quarter building a self-serve funnel for a product that structurally cannot convert through one. That is the specific, expensive way this goes wrong.

It does not rule out a free surface entirely — it rules out using self-serve as the *money path*. Kept in its correct role (lead generation, not revenue), a free surface is still the cheapest lever you have, and it's what "PLG" is actually reaching for underneath the label.

## Assumptions made to finish this without a live interview

- **[assumed]** No dedicated sales/marketing headcount exists today — GTM work runs on founder/engineer time, consistent with "no new headcount" being the binding constraint rather than an unused option.
- **[assumed]** Some number of pilot/eval clusters already exist informally (nothing ships and gets a CTO worried about board optics from zero usage). Treated as the immediate inventory to work in the next 10 weeks.
- **[assumed]** Deal size sits in mid-to-high five figures to low six figures ACV — cluster-wide admission control is infra/security spend, not a per-seat tool.
- **[assumed]** Target buyer is a platform/infra engineering team already running Kubernetes at meaningful scale, with an existing (if informal) budget line for policy/admission control — the category (OPA Gatekeeper, Kyverno, Styra) already exists in their vendor evaluations.

Replace any of these with real numbers before the board meeting — everything downstream inherits them.

## Constraints

- **Business model / paid boundary**: undecided today (no free tier, no stated pricing unit). This memo proposes a boundary — audit-only/single-cluster policy-checking free, enforcement + multi-cluster + governance features (SSO, RBAC, audit log) paid — but that split needs your explicit sign-off before anything below gets built. Do not let it stay implicit.
- **Product friction**: real, not a preference. Approval + install + three-service threshold are structural properties of an admission controller. No motion here can pretend otherwise.
- **Response capacity**: existing team, no new hires this year. Any motion that requires a standing sales job is not available in 2026, full stop.
- **Board horizon**: 10 weeks to show revenue movement. This is a harvesting problem (close what already exists), not a funnel-building problem — a new motion cannot generate, staff, and convert its own pipeline in 10 weeks from a standing start.
- **Margin**: zero tolerance for reseller/marketplace cuts. Removes an entire motion outright (below).

## Friction gates

1. **Entry — fail, for the enforcement product.** Approval + cluster install are mandatory and non-removable. **Pass, for a narrower artifact**: an offline, audit-only CLI that lints a developer's existing manifests against policy locally — no cluster, no admission webhook, no approval, because it never touches the request path. This is the Sprocketd-style "sandbox" trick: split what needs infra from what doesn't, and sell only the part that needs infra.
2. **Value — fail, for the enforcement product**, exactly as you described: worthless below three services. **Partial pass, for the CLI**: one developer gets a real (if narrow) violation report against their own repo, in minutes, alone.
3. **Spread — pass, with design work.** Policy bundles as code, committed to a repo, checked in CI, surfaced as a PR status check — a second engineer sees a blocked/flagged PR as a matter of course. Build this deliberately; it is not automatic.

Gate 1 failing for the core product is decisive: bottom-up self-serve is not available as the revenue motion. It is available, narrowly, as a lead-gen wedge — worth building, wrong to fund the board number with.

## Rejected motions

- **Top-down with developer proof** — rejected for this year. The no-new-headcount ceiling deletes it outright: it requires a standing sales job and a maintained compliance-evidence base, neither staffable without a hire. **Revisit when**: qualified-account volume × realistic deal size clears 4x a fully-loaded rep's cost — that's the trigger to hire the first AE and promote this motion back onto the table explicitly, not slide into it by accident.
- **Ecosystem-mediated** — rejected, directly, by the no-margin mandate. A marketplace listing or reseller agreement is exactly the arrangement that requires permanent margin. Not revisited unless that mandate changes.
- **Bottom-up self-serve, full product** — rejected as the *revenue* motion. Gates 1 and 2 both fail structurally for the enforcement product; no funnel work fixes an approval step or a three-service value floor. Survives only as the lead-gen wedge described below — call it by its correct name, "bottom-up lead gen," so nobody mistakes CLI download counts for pipeline.

## Primary motion

**Developer-influenced sales (conversion-assist), run by existing team, against a concentrated list of known accounts, closed by selling the onboarding itself as the paid product.**

Money path: a platform engineering team with an existing K8s policy problem is identified (referral, existing pilot, inbound interest, or direct outreach to a named account list) → offered a scoped, paid pilot — a fixed-price, 6–8 week engagement to design policies and onboard their first three services, run by your existing engineering time → pilot's own success is the three-service value threshold being crossed, which is also the moment the product starts being useful → convert pilot to an annual contract for ongoing enforcement across the rest of the cluster.

This is the specific move that resolves your structural friction instead of fighting it: the thing that makes self-serve impossible — required hand-holding to reach value — is what you sell, not what you route around. It also needs zero new product work to start.

**10-week board lever, inside this motion**: work the existing pilot/eval inventory **[assumed to exist]** directly. Whoever already owns those relationships contacts each one this week with the paid-pilot offer. Target: convert a stated number of current pilots to signed contracts before the board date — put the real number in, not a placeholder, before this goes to the board.

**Prerequisite that must hold**: at least one existing contact per target account can approve a fixed-price pilot without a full procurement cycle. Verify this against your actual pilot list before committing to a board number — if it's false, the 10-week ask needs a different lever (e.g., expand scope of an already-signed account) and that's worth surfacing now, not at week 9.

## Secondary motion — bottom-up lead gen

**A free, audit-only policy-check CLI**, decoupled entirely from the enforcement product: no cluster, no webhook, no approval. Ships as a quarter of product work, no headcount, consistent with your constraint. Its job is to feed the top of the primary motion, not to convert on its own — label it "lead gen," not "PLG," in every internal conversation, so nobody starts measuring it against a self-serve conversion benchmark it was never designed to hit.

## Entry design

- **CLI first-value moment**: a developer runs it against their own manifests and sees every policy violation Parapet would catch, in under a few minutes, with nothing to install and nothing to approve.
- **Paid-pilot first-value moment**: the platform engineer sees a dry-run report across their real cluster — still gated by approval and install, which is fine, because this step is being sold, not self-served.
- **Stays open forever, no exceptions**: full docs, the policy library, a real pricing page, all limits, CLI source, troubleshooting content. Gating any of these loses a technical evaluation silently and you will not see it happen.

## Handoff rule

**Account rollup**: email domain + GitHub org (from CLI usage, opt-in) + self-reported company. Imperfect, immediate — a proper workspace/account object is a later build item once there's a hosted control plane to hang it on.

**Threshold** (self-set — replace N/M with your own conversion data the moment you have any; do not ship this sentence unchanged past your first real cohort):

> An account becomes qualified when two or more repos from the same GitHub org run the policy-check CLI within 30 days, **or** when anyone asks about production rollout, SSO/audit, or a security questionnaire. Qualified accounts are contacted by [named existing team member] within 24 hours with an offer to run the paid three-service onboarding pilot. Accounts below the threshold are not contacted by a human.

**Routing**:
- Platform engineer (the active user) → a rollout/limits conversation, not a pitch.
- Internal champion → the enablement pack (their own violation report as the internal case, a reference rollout architecture, a migration path from whatever ad hoc policy enforcement they run today).
- Security/approver → pre-answered risk material, unprompted, and specifically: what happens if Parapet itself fails or misbehaves inside the admission path. That is the first objection anyone will raise about a webhook that can block every deploy in the cluster — answer it before they ask.

**Do-not-contact line**: every CLI download that never crosses the threshold gets product and docs only. No exceptions — the failure mode here (email everyone who downloaded a K8s tool) burns exactly the audience least tolerant of it.

## Expansion path

| Vector | Trigger | Owner |
|---|---|---|
| More services, same cluster | The paid pilot's own delivery — walking from 3 services to full coverage | Product/account owner (this **is** the pilot's deliverable) |
| More clusters, same company | A second cluster or namespace pattern appears; internal referral | Account owner (founder/eng), with the champion |
| More governance surface (SSO, audit, org-wide policy CI) | A standardization ask from a platform/architecture group | Account owner — and this is the signal that justifies hiring the first AE |

**Multi-threading rule**: no account counts as landed with fewer than two engaged contacts — the platform engineer plus one manager-level sponsor. A single champion leaving an admission-controller account is not a soft risk; the next person to touch it, absent context, rips it out at the next incident.

## Leading indicators

| Indicator | Today | Target | By |
|---|---|---|---|
| Existing pilots converted to signed paid contracts | [fill in real count] | [fill in real target] | board date, +10 weeks |
| CLI: time from download to first violation report | not shipped | under 5 minutes | at CLI launch |
| Qualified accounts (CLI-sourced) contacted within 24h | not measurable yet | 100% (volume will be small) | ongoing from CLI launch |
| Repos per GitHub org running the CLI 2+ times in 30 days | not measurable yet | [set after first cohort] | one quarter after CLI launch |
| Cohort CLI-to-paid-pilot conversion, 6-month window | not measurable (n too small) | report next year | — |

Fill in the first row with real numbers before this goes to the board — an invented target in that row is the one number in this memo that cannot stay a placeholder.

## Refused

- No outbound to every CLI download — only to accounts crossing the written threshold.
- No gated docs, policy library, or pricing.
- No reseller or marketplace agreement that takes margin, under any framing.
- No enterprise-only tier sold with no paid-pilot floor beneath it — every small account still needs a route in.
- No new sales headcount this calendar year, and no quiet workaround (a contractor titled to dodge the letter of the constraint is still headcount).

## Revisit triggers

- Qualified-account volume × realistic deal size clears 4x a fully-loaded rep's cost → hire the first AE, and explicitly promote top-down-with-developer-proof back onto the table rather than drifting into it.
- A cloud marketplace becomes the only procurement path into a segment you can't otherwise reach → force the margin conversation back to the CTO by name; do not re-reject ecosystem-mediated by default.
- CLI ships high download volume but qualified-account volume stays near zero for two quarters → the wedge doesn't connect to the paid product; redesign the CLI's "ask for the full report" step rather than adding more downloads.
- Day-60 multi-repo CLI usage per org stays low two quarters running → the PR/CI spread mechanic is the problem, not the sales motion.

---

**The direct answer to the room**: don't do PLG. Do developer-influenced sales, run by the people you already have, closing a short list of accounts you can name today — and build a small free CLI alongside it, correctly labeled as lead gen, so that in a year the same motion has a self-refilling top of funnel instead of a founder cold-emailing every quarter.