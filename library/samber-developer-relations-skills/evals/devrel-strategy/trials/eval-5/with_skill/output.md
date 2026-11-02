Charter below is the tightened deliverable. Biggest problem in your draft: 8 activities funded across 4 pillars, but your only headcount lands Q3 — nothing ships in Q1/Q2 as staffed. Fixed that first, then cut goals from 6 to 3, cut metrics from reach to behavior.

---

# DevRel charter: Ormont Labs, H1

## Position

**Community** — No devrel-owned community venue yet (Discord not launched). Docs exist but need work. GitHub stars named as a target metric — confirm a public repo already exists and has real traffic; that's unstated.

**Organization** — No dedicated devrel headcount today. Both planned hires (community manager, developer advocate) land Q3 — after H1 ends. Everything in the original plan was scoped as if staffed; it isn't yet.

**Relationships** — Edge functions is a crowded, technically literate market (Cloudflare Workers, Deno Deploy, Vercel Edge, Fastly Compute). Bar for credibility is high; developers here detect thin or agency-voiced content fast.

**Ecosystem** — Infra category. Individual devs can try it alone, but a runtime/platform purchase usually gets a second reviewer (architect, platform lead, security). "Support sales" in your goal list confirms a company-adoption motion exists alongside self-serve trial.

**Lifecycle stage: Seed.** One program, no specialist yet, work currently falls on founders/engineers as a part-time hat.

## Driver

Six goals were named with no single owner or ranking — that's a sponsor problem, not a strategy problem (every activity scores equally when everything is a goal). Best-fit read from what's given:

- **Primary driver: developer adoption** — product is self-serve infra, usage-before-revenue shape.
- **Secondary driver: sales enablement** — "support sales" implies a funded pipeline this already serves.

**Open question:** confirm with whoever owns the budget which of these they'd name first. This charter is built on the adoption-primary assumption — flip it and step 2 below changes.

## Goals (2 primary + 1 secondary — down from 6)

| Goal | AAARRRP | Journey step | Drop-off |
|---|---|---|---|
| Awareness | awareness | initial awareness | Not yet measured — no baseline exists before this plan. Flag as first thing to instrument. |
| Community/activation | activation | evaluation → commitment | Not yet measured. |
| Sales support | revenue | evaluation (company-adoption path) | Not yet measured — ask sales where deals currently stall. |

**Cut from goal list, not funded as standalone bets this horizon:**
- **Employer brand** — real side-effect of good devrel work, not something worth its own bet at seed stage.
- **Product feedback** — folds into the community bet later (H2) once Discord exists; not a funded pillar now.
- **Docs improvement** — reclassified: it's an enablement *bet* serving the activation goal, not a goal on its own.

## Audience

**Primary: company-adoption path.** A developer evaluates, someone else signs. Build evaluation material a reviewer can act on: reference architecture, security/licensing clarity, named production references.

Docs refresh (below) serves both paths at once — also cuts time-to-first-deploy for solo trial users — so it's built once, not twice.

**Not served this horizon:** deep self-serve growth loops, ecosystem/partner motion.

## Pillar mix

Funded above token level: **enablement, evaluation-support** (both live inside the enablement pillar this horizon).
**Deliberately starved: community, reach/marketing.** Discord, hackathons, monthly livestream, swag store, and 3 of 4 conferences — cut or deferred. Reason: four pillars funded at seed stage with zero dedicated headcount is the direct cause of "busy but not landing."

## Bets (3)

**1. Docs refresh** — goal: activation. Owner: developer advocate (once hired) / engineering lead until then. Signal: time-to-first-successful-deploy, not blog views. Review: end of H1.

**2. Evaluation content for sales** — reference architecture doc, security/licensing page, 1–2 named production references. Goal: revenue (secondary). Owner: advocate + sales liaison. Signal: evaluation-stage deals where sales cites devrel material, per sales' own report. Review: mid-H1 checkpoint, then end of H1.

**3. Focused conference presence** — 1–2 talks at events your actual ICP attends, not 4. Goal: awareness. Owner: founder/engineer until advocate hired, then advocate. Signal: qualified follow-up conversations per talk, not attendee count. Review: after each event.

Blog cadence folds into bet 2 (evaluator-facing, occasional) instead of standing at 2 generic posts/month with nobody assigned to write them.

## Build vs buy

- Docs + evaluation content: **in-house**. Voice and technical accuracy are a credibility surface — no agency, no contractor ghostwriting under the advocate's byline.
- Agency ruled out entirely for H1: its own setup latency (~6 months) doesn't fit a plan due this half.
- Conference talks: in-house speaker, whoever is closest to the topic.

## Staffing

Original plan hires two specialists simultaneously in Q3, skipping the seed-stage "one generalist first" step — and both land after H1 is over.

**Recommendation: pull the developer advocate hire forward** — as early in H1 as budget allows, no later than Q2. Advocate is the generalist-shaped role here: covers docs, evaluation content, and conference talks — i.e., all three funded bets.

**Community manager stays deferred**, gated on a real trigger: hire when Discord actually launches (H2), not on a fixed quarter. Hiring a community manager before there's a community to manage is buying idle capacity.

## Refused this horizon

- No Discord launch in H1 — a venue with nobody to moderate costs more trust than not opening it. Defer to H2 with the community manager.
- No hackathons in H1 (2 planned) — standing-job effort, no capacity to run one well.
- No monthly livestream — third reach-pillar commitment with zero staffing behind it.
- No swag store — lowest-leverage item on the original list, cut outright.
- Conferences capped at 1–2, not 4.
- No agency-written content under an in-house byline.

## Open questions

- Which driver (adoption vs sales enablement) would the actual budget owner name first?
- Real funnel data behind "build awareness" / "grow community" — does it exist, or is this a preference?
- Does Ormont Labs have a public GitHub repo today? Needed before "GitHub stars" means anything.
- Program budget: salaries included or not? Unstated — resolve before the build-vs-buy math is final.
- Can the advocate hire actually move earlier than Q3? Depends on approval timing, not decided here.

## Exec narrative

We're funding developer adoption first, with sales support as the direct second priority. We're refreshing docs and building evaluation material sales can use in active deals, instead of running eight parallel activities with no one staffed to do them. We're hiring a developer advocate as early as possible in H1 to actually execute this, and holding the community manager until there's a real community — Discord — for them to run. We're cutting hackathons, livestream, and swag this half; they cost more than we can staff right now. We'll know it's working when deploy time drops and sales cites our content in live deals, not from view counts.

## Review

Checkpoint mid-H1: advocate hire status, docs bet signal, first evaluation-content usage from sales. Full re-decision at H1 close, before H2 budget review. Early re-review trigger: advocate hire slips past Q2, or sales reports zero use of evaluation material by mid-H1.

---

**Quality gate check**

Structural (pass/fail, non-negotiable):
- Driver named, owner unnamed (role placeholder only) — **incomplete**, needs a real name.
- Goals pinned to journey steps — pass; drop-offs marked unmeasured rather than invented — pass.
- Bets: goal, owner, signal, review date — pass, all 3.
- Refused list non-empty, includes things the team wanted (Discord, hackathons) — pass.
- Open questions written, not assumed — pass.
- Nothing on a credibility surface outsourced — pass.
- Exec narrative, no jargon — pass.

Baselines moved, not backed by outside data (this skill's own defaults, stated here per its rule):
- 2 pillars funded (enablement, light advocacy) instead of the original 4 — moved down deliberately.
- 3 bets, 3 goals — within the 3–5 bet / 3-goal ceiling, not stretched.

**Next:** name the actual driver owner (real name, not role) and confirm adoption-vs-sales-enablement primacy — that's the one gap blocking sign-off.