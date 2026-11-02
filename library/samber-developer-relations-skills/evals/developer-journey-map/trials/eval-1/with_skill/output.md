Using the developer-journey-map skill. This is normally a live interview (13 questions, one at a time) before any row gets written — since you asked for the finished deliverable in one shot, I've answered those questions from what you gave me and flagged every place I inferred rather than confirmed. Those flags live in **Scope** and **Gaps** below; check them before you present this.

---

# Developer journey map — platform engineers, 1000+ person companies, 2026-09-19

## Scope

**Segment:** platform engineers at 1000+ person companies. One map, this segment only.

**End state:** standardization — Tarnhelm becomes the org-wide default, not "that team's tool." This is the literal board question, and it's why the stage model below is not the one on your wiki.

**Stage model chosen: Revell's six-stage developer journey** (initial awareness → deep awareness → evaluation and validation → commitment → standardization → community and advocacy). It is the only published model with an explicit standardization stage — the others delete on contact with your end state:

| Model | Terminal stage | Why it's off the menu here |
|---|---|---|
| Your 2024 wiki diagram (discover → try → adopt → contribute → advocate) | advocate | This is this skill's own "unsourced default" — a merge of three other frameworks, never a published model. Its tail is advocacy, not standardization, so it can't see the gap the board is asking about. It's superseded, not deleted for being wrong — it was just built to answer a different question. |
| AAARRRP | revenue | Ends at money and product feedback, not org-wide default status. |
| Orbit levels | advocate | Community-depth model; no evaluation/production/standardization vocabulary at all. |
| API five-stage arc | production | Tempting — its early boundaries (SDK init, first call) sit directly in your telemetry, cheapest to run. But "production" is a bar these five accounts already cleared; the model has nothing to say about what happens after. |
| OSS contributor funnel | return (repeat contribution) | Not your motion — no open-source contribution path here. |

Normally Revell is the *most* expensive model to stand up (a quarter, mostly account rollup + buyer-side interviews). Two things collapse that cost for you specifically: sales ops already built the full account rollup, and a renewal being pinned to org-wide-default status is exactly the case this skill says to promote Revell despite the cost — the rollup it forces is the point, not the overhead.

**Buyer role:** developer is an influencer, not the signer. The platform engineer is the internal champion; the economic buyer (VP Eng / procurement, customer-side) signs at renewal. *Inferred — confirm who actually signs at your two renewal-pinned accounts.*

**Motion:** mixed. Initial technical adoption is self-serve within a team; expansion to org-wide default and renewal are sales-assisted, enterprise motion.

**First map or refresh:** first map. The wiki diagram has no exit events, no owners, no signals — it's a sketch, not a previous version, so the continuity rule doesn't bind you to it.

**Effort ceiling used:** three weeks to planning close. Account rollup and SDK-init/first-eval telemetry already exist, which covers the cheap end of Revell. The one piece that doesn't exist yet — evidence for *why* standardization stalls — needs champion interviews, which are feasible inside three weeks because you only need to run them at five accounts, not recruit cold.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Initial awareness | "find something better than hand-rolled config toggles" | hears about Tarnhelm — peer inside the same company, search, conference, outbound | visits docs/repo, or requests workspace access | website, docs, internal Slack/wiki mentions from an already-adopting team, conference | marketing/DevRel for external channels; **no owner** for intra-account word-of-mouth | no evidence yet | not instrumented — *inferred stage* |
| Deep awareness | "decide if this replaces what we built, and if it fits our stack, before touching code" | reaches docs/product pages | provisions a workspace / requests an SDK key | docs, SDK reference, comparison content | docs owner / product marketing | no evidence yet | not instrumented — *inferred stage* |
| Evaluation and validation | "prove flags work in our stack without committing" | SDK initialized (telemetry event) | first flag evaluation call succeeds (telemetry event) | SDK, quickstart docs, dashboard, support channel | developer experience / product (SDK team) | no evidence yet — run a friction log this week, it's the cheapest evidence you have access to | **instrumented** — share of SDK-init'd workspaces reaching first evaluation within 7 days. *Pull from telemetry, value not pulled into this document.* |
| Commitment | "trust this to gate a real production release for my team" | first evaluation succeeds + repeat calls | sustained production flag evaluations for 14 consecutive days | dashboard, runbooks/on-call docs, SDK, support | product (Tarnhelm SDK/platform team) | indirect confirmation this stage is healthy: 5 of top 10 accounts already carry 200+ active developers (your own framing) | **instrumented** — active developers per account, trailing 12-month trend. *Pull from CRM account rollup.* |
| **Standardization** | (champion, same segment, senior/staff) "make this the company's default, not my team's private tool" | a second and third team in the account adopt independently, or a platform/architecture lead opens an internal RFC | Tarnhelm named as the sanctioned flag provider in the account's own onboarding template, service-scaffolding, CI template, or architecture decision record | customer's internal wiki/RFC process, architecture review board, Tarnhelm Solutions Engineering / enterprise DevRel, renewal conversation | customer's platform/architecture lead decides; **no Tarnhelm-side owner currently accountable for driving it** | the board's own framing: 5 of top 10 accounts, 200+ developers each, zero standardization event on record. Not yet cross-checked with champion interviews. | not instrumented — below the 30-event floor even once captured (10 accounts total); publish as a dated raw list, never a rate |
| Community and advocacy | "tell other teams, and the outside world, this was worth it" | standardization reached, or a strong individual success pre-standardization | named public mention (talk, blog, case study) or formal reference-customer agreement | community, conference CFPs, customer marketing, changelog | DevRel / customer marketing | no evidence yet | not instrumented, expect below small-N floor — raw dated list |

## Buyer lane

Present. B2B, renewal-gated, developer is influencer not signer.

Roll to account before reading this lane — already done: sales ops' CRM rollup groups by account.

| Buyer stage | Exit event | Owner | Signal |
|---|---|---|---|
| Champion armament | champion has a reference architecture, internal-adoption pack, and pre-cleared security/licensing answers in hand | Solutions Engineering / enterprise DevRel (Tarnhelm side) | not instrumented — count of top-10 accounts with a delivered adoption pack |
| Renewal / economic approval | renewal signed with expanded or org-wide license terms | Sales / Customer Success own the account; signer is the customer's economic buyer | for the 2 renewal-pinned accounts: days from "org-wide" ask to signature — raw dated list (n=2, below floor) |

Signal families:
- **Depth** — active developers per account, already available and healthy (the CRM rollup covers this).
- **Spread** — distinct teams/workspaces per account. Not broken out today. Recommend extending the rollup to count teams, not just headcount — this is what turns "200 developers" from one number into evidence of whether it's one team or eight.
- **Boundary contact** — an account asking about org-wide licensing, SSO/RBAC at scale, or explicitly saying "we want to standardize on this." Not tagged today. This is the single cheapest, highest-leverage addition on this whole map: ask CS/AE to tag it as a CRM note field starting now, and it becomes your cleanest exit event for this lane going forward.

## Moments

- **First success** — SDK initialized and a real flag evaluation returns a value. Already instrumented; exact median time is one telemetry query away.
- **Moment of truth** — not the purchase, and not first production use (both already happened, repeatedly, at team level). It's the standardization decision: whether a platform/architecture lead formally proposes Tarnhelm as the company default. This is quieter than a sales moment — a wiki edit or an RFC submission, not a signature.
- **Abandonment point** — nothing abandons the product; usage holds at 200+ developers per account. What stalls is organizational: the standardization *ask* is never made, because no one, on either side, is accountable for triggering it. That's earlier and duller than a technical-trust story, which is probably not what the board expects to hear.

## Leak

**Standardization.**

Commitment converts well — five accounts each carrying 200+ active developers, sourced from your own CRM rollup. Initial and deep awareness are unmeasured, not confirmed broken, so neither can be nominated over a stage with confirmed failure. Standardization is the one stage with direct, board-level evidence of non-conversion, and it's also the end state you named for this exercise — the explicit case in which this skill says to promote a late, expensive stage over the cheaper early ones it would otherwise lose to every quarter.

Owner: currently nobody on the Tarnhelm side is accountable for making a customer's internal RFC happen. Proposed: Solutions Engineering / enterprise DevRel jointly, starting with the two renewal-pinned accounts.

Why it leaks (BJ Fogg's B=MAP — hypothesis, pending the interviews below):

- **Most likely: prompt missing.** Champions could plausibly propose standardization and the org would likely say yes — 200+ developers per account is not a trust problem. But nothing in your current motion ever explicitly asks them to, or hands them what they'd need to do it with. There's no lifecycle trigger at "you just crossed 100 developers in this account" that tells anyone to open that conversation.
- **Second: ability.** Even prompted, writing a company-wide tooling mandate isn't a routine task for an individual platform engineer — no reference RFC template, no pre-cleared security/licensing pack, no reference architecture to copy from.
- **Least likely, not ruled out: motivation.** A champion may see no personal or team upside in spending political capital on a cross-org mandate.

Don't lock in which of the three before running 5-8 champion conversations across the five flagged accounts (protocol: would they propose standardization, did they try, what stopped them). Three weeks is enough to run these at five accounts you already have a relationship with — it is not enough to run them cold.

## Handoff

- **Owner:** Solutions Engineering / enterprise DevRel, jointly, starting with the two renewal-pinned accounts.
- **Signal to watch:** count of top-10 accounts with Tarnhelm named in an internal RFC or golden-path artifact — raw dated list, not a rate (n<30).
- **Re-read date:** 2026-12-18 (90 days, this skill's default), and again immediately ahead of each renewal-pinned account's renewal date regardless of that clock.

## Gaps

- Initial and deep awareness: inferred, no self-reported-source field or pre-SDK-init provisioning event exists. Add a "how did you hear" capture and a workspace-provisioned telemetry event.
- Commitment: the 14-day sustained-production exit event isn't a distinct telemetry event today — only SDK init and first evaluation are captured. Add it.
- Standardization: no instrumentation exists for RFC/golden-path mentions or team-spread per account. Extend the CRM rollup to break developer count out by team/workspace, and have CS/AE tag "standardization" conversations as they happen.
- Community and advocacy: no tracking of unprompted mentions; expect volumes under the 30-event floor regardless of what you add.
- Buyer lane: boundary-contact tagging (org-wide licensing, SSO-at-scale questions) doesn't exist in CRM today — cheapest, highest-leverage instrumentation ask on this whole map.
- Owners: Marketing, Docs/Product Marketing, Product, and Solutions Engineering are this document's best inference from typical org shape, not confirmed against Tarnhelm's actual org chart. Confirm before treating any of them as final — question 8 of this skill's interview (who owns each surface) was never actually asked of you.

---

**Quality gate, reported straight:** one exit event and one owner per row — pass, and DevRel only solely owns one of eight rows, so the "map nobody else agreed to" failure mode doesn't apply here. Friction evidence cited or marked "no evidence yet" — pass. Exactly one leak, named owner, re-read date — pass. Inferred stages labelled — pass. Signal coverage — **fails** the 60% line: nothing in this document carries a pulled number, because it was built from your brief, not a live query. Three of the eight signals are already defined against data you hold (evaluation-stage conversion, commitment depth, buyer-lane depth) and just need running; two genuinely don't exist yet (standardization, boundary contact). Fits on one page — no, and won't while the buyer lane and B2B evidence trail stay in; if you need a one-pager for the board itself, the Journey table plus Leak and Handoff sections alone will do it. Shipping with the gaps named rather than inventing numbers to close them, per this skill's own rule.