Split's broken before you even get to strategy. Same $440k, apply user's own percentages: 41 + 31 + 19.5 + 13 = 104.5%. That's $459,800 — $19,800 over budget, baked into the source data itself (respondents answered on inconsistent bases, so shares never summed to 100 in the first place). Two booths at $180k checks out against 41% — the multiplication is fine. The input isn't.

Three separate problems, not one:

1. **The 41% figure is history, not a target.** DevRel.Agency's *State of Developer Relations 2024* — only 47 of 310 respondents answered this question, shares sum to 104.5%, categories omit community/tooling/education entirely. It's evidence events have historically dominated spend. It is not a benchmark to mirror, and the source study says so explicitly.
2. **Two big booths is the wrong shape for a solo first hire regardless of price.** You're Seed stage — one generalist, no prior devrel function. The stage rule is one archetype, one bet, finished before a second starts, and it names event sponsorship as the specific thing not to do at this stage. Running two flagship booths (logistics, staffing, travel, lead follow-up) consumes a solo hire's entire quarter and leaves nothing for the technical foundation (docs, samples, reference architecture) a booth visitor would need to actually evaluate the product.
3. **No evidence the leak is awareness.** VP Eng wants adoption — that's a conversion problem until proven otherwise. Spending on reach before fixing evaluation burns the audience you just paid to bring in.

Below is the actual charter — built from the CORE framework, Leggetter's driver/goal model, and this skill's archetype ranking, not from the survey split. I don't have your funnel data, your existing docs state, or confirmation of who signs the purchase, so those are marked as open questions rather than guessed at.

---

## What I inferred vs. what's still open

Given, in your words: product (payments-reconciliation API), stage (Series A, 22 people), you're the first DevRel hire, sponsor (VP Engineering), driver (developer adoption), budget ($440k), deadline (January board meeting).

Assumed, flagged for confirmation in the charter: audience path is company-adoption (a developer evaluates, but payments data implies a security/finance/eng approver signs) rather than solo bottom-up; secondary driver is sales enablement/revenue, since a Series A board meeting usually wants a number the funnel produces, not adoption in the abstract; $440k includes your own salary, since your draft treats "salaries" as one of four buckets it's drawn from.

Not given anywhere, treated as unknowns: current activation funnel data, what docs/sandbox/samples already exist, who actually signs the purchase, whether any of the $180k is already committed, the exact January date.

## Shape comparison (working material, not part of the charter itself)

| | Enablement-first | Evaluation-support | Reach-first (your draft) |
|---|---|---|---|
| Fits | Adoption, activation leak | Sales enablement, company-adoption, enterprise motion | Adoption *at awareness stage*, employer brand |
| First bets | Quickstart to working call, error-page coverage, agent-readable docs | Reference architecture, scoped PoC kit, security/compliance answer sheet, named references | Conference stages, launch beats, search-durable content |
| Starves | Events, community | Hobbyist content, broad awareness | Community, champions, certification |
| Effort | ~quarter of one person's writing time, then near-zero | ~quarter of one person's time + standing sales coordination | Standing job — the cadence is the product |
| Fastest signal | Share of signups reaching a second successful call | Evaluations reaching a technical decision; time to working PoC | Non-paid qualified arrivals |
| Wrong pick when | Nobody arrives at all | Product is bought bottom-up by individuals | Onboarding leaks — reach into a broken funnel burns the audience once |

Efficiency and value orders both rank enablement-first first. Evaluation-support is second on value, third on efficiency — it directly serves the revenue-adjacent secondary driver a January board meeting almost certainly wants. Reach-first ranks near the bottom on both, and the Seed-stage overlay names it as the thing not to run yet. Recommendation: lead with enablement-first, fold in evaluation-support bets since they're nearly free reuse of the same material, keep one modest event presence instead of two flagship booths, refuse the rest this horizon.

---

# DevRel charter: Tesserine, H1 (through January board meeting)

## Position

*Community.* Unknown — no data on active integrations, support volume, or existing venues was available for this draft. Treat this as a real gap: baseline instrumentation is folded into bet 1, not assumed away.

*Organization.* DevRel does not exist yet as a function. You are the first and only hire, sponsored by the VP of Engineering at a 22-person company. No prior devrel-shaped work (founder blogging, support-led community answers) is on record — this is a from-zero build, not a rescue of a stalled effort. Ownership of docs and any existing content outside this program is unconfirmed.

*Relationships.* Unknown — no named competitors, resellers, or integration partners were given. Payments reconciliation is a category with established incumbents; whether any compete directly for the same evaluators is unconfirmed.

*Ecosystem.* Payments reconciliation is narrow, technical, B2B infrastructure. Evaluators most likely arrive while solving a specific integration problem — closing the books, matching settlement batches against a ledger — not by browsing. Payments data typically pulls a security or compliance reviewer into the purchase, which argues for company-adoption over individual adoption (see Audience, and Open question 2).

*Lifecycle stage:* starting.

## Driver

Developer adoption. Owner: VP of Engineering, who funds and will defend the role.
Assumed secondary: sales enablement — a Series A board meeting in January is unlikely to accept "adoption" with no revenue-adjacent number behind it. **Confirm with the VP of Engineering before this ships**; if adoption really is the only driver, drop bet 3 and evaluation-support entirely and put that capacity into bet 1 and 2 instead.

## Goals

Primary — activation: share of technical evaluators who reach a working reconciliation run (journey step: evaluation). No funnel data exists yet to name the actual drop-off number; establishing it is part of bet 1, not a precondition for starting.
Primary — revenue (assumed secondary driver): evaluations that reach a technical decision (journey step: evaluation → commitment). Provisional on the driver confirmation above.
Secondary — product: integration friction routed to the roadmap with a named owner, cheap enough to run alongside the other two even at Seed capacity.

## Audience

Primary: backend/platform engineers integrating reconciliation into an existing finance or payments stack, at companies past early-stage tooling but not yet enterprise-scale procurement. Approver: an engineering lead or security/compliance reviewer, given the sensitivity of payments data — assumed, not confirmed (Open question 2).
Not served this horizon: individual hobbyist adoption (not the realistic buyer for this category), and full enterprise procurement (named references, security questionnaires) beyond the single answer sheet in bet 3.

## Pillar mix

Enablement 55%, advocacy/evaluation-support 30%, marketing 15%, community 0%.
Community is deliberately starved: no installed base or venue exists yet, and a Seed-stage program with one hire cannot run more than one archetype without diluting all of them. This mix is this skill's own baseline, not a benchmark — move it once real funnel data exists.

## Bets

1. **Quickstart to a working reconciliation run, plus tested samples** in the languages real evaluators actually use (unconfirmed — default to the two most common backend languages in payments infra until sales engineering names them). Goal: activation. Owner: you, in-house. Signal: share of sandbox signups completing a real reconciliation run. Review: week 8.
2. **Troubleshooting coverage for the top integration failure points** (currency mismatch, rounding, partial settlement) plus an agent-readable docs surface. Goal: activation. Owner: you, sourced from support/engineering tickets. Signal: support tickets per 10 new integrating accounts; organic arrivals on error-code pages. Review: week 10.
3. **One reference architecture, a scoped proof-of-concept kit, and a written security/compliance answer sheet** for the most common integration pattern. Goal: revenue (secondary driver, pending confirmation). Owner: you, with engineering/security review. Signal: evaluations reaching a technical decision; time from first contact to working PoC. Review: week 12 — lands before the board meeting.
4. **Friction logs from the first design-partner integrations, routed to the roadmap with a named owner.** Goal: product. Owner: you log, VP Engineering accepts. Signal: friction items reaching the backlog with an owner. Review: monthly.

## Build vs buy

Bets 1, 2, 4: in-house. These are the credibility surface — a rented voice on your own quickstart or error pages is exactly what an evaluator checks for and exactly what a solo hire can produce inside a quarter with no vendor latency.
Bet 3: in-house content and judgment (the technical trade-off calls, the security answers), contractor for diagram/design production only. Reviewer: you plus whoever owns security/compliance sign-off. Agency is off the table this horizon — its own published setup latency runs about six months, which doesn't fit a January deadline.

## Staffing

Stage: Seed, one generalist. No second hire this horizon — nothing here has hit a queue a second person would relieve yet. Next capability, if triggered: contracted technical-writing surge support, only if the bet 1–3 backlog exceeds your bandwidth for two consecutive months. Not a community manager — there is no community to manage.

## Refused

- No second conference booth, and the one event kept is capped at a modest sponsor tier, not a flagship presence — this directly descopes the plan's original $180k, two-booth line.
- No community venue (Discord, forum) this horizon — no installed base to seed it with yet.
- No standing content/blog cadence beyond what bets 1–3 already produce as a byproduct.
- No swag program.
- No enterprise procurement material beyond the bet 3 answer sheet, until a named deal actually stalls on its absence.

## Open questions

1. Does the $440k include your own salary? Owner: Finance + VP Engineering, before budget sign-off — this resets every other number in this charter.
2. Who actually signs a purchase — the developer alone, or an approver? Owner: VP Engineering/sales, by week 2 — this is the load-bearing assumption behind Audience and bet 3.
3. Current activation funnel: how many sandbox signups reach a working reconciliation run today? Owner: whoever owns product analytics, by week 2 — sets bet 1's real target, not just its shape.
4. What already exists — docs, sandbox, sample repos, any support venue? Owner: you plus the docs owner, by week 1 — changes bet 1 from a rebuild to a from-zero build, which changes cost and timeline.
5. Is adoption the sole driver, or does the board expect a revenue number too? Owner: VP Engineering, before this charter is final — decides whether bet 3 exists at all.
6. Is any of the original $180k conference spend already committed? Owner: whoever signed it, immediately — if yes, it's sunk, and the real remaining budget is smaller than $440k.
7. Exact January board-meeting date. Owner: VP Engineering's office, immediately — every review date above is set against it.

## Exec narrative

Tesserine funds this program for developer adoption, per Engineering's mandate. Right now we don't know where technical evaluators drop out, so the first move fixes the two moments that decide every evaluation: reaching a working reconciliation run fast, and giving the person who approves the integration a written answer instead of a sales call. We are not funding two conference booths this half — nothing today shows evaluators are hard to find, and the evidence points at conversion, not reach. By the board meeting, expect a higher share of sandbox signups completing a real reconciliation run, and at least one technical evaluation reaching a decision. We'll report the actual numbers at review, whether or not they moved.

## Review

Re-decision at the January board meeting. Early re-decision if VP Engineering sponsorship changes, if the salary-inclusion question resolves in a way that moves program spend by more than 15%, or if bet 1's signal hasn't moved by week 10.

---

## Quality gate

Structural — all pass: driver named with one owner in the funder's words; each goal pinned to a journey step; every bet has owner, one signal, one review date; refused list non-empty and includes something the team wanted (the second booth); open questions written down, not assumed away; nothing on a credibility surface (docs, samples, security answers) is outsourced; exec narrative has no devrel jargon.

Baselines moved, and why: pillar mix (55/30/15/0) is this skill's own baseline, set here because no funnel data exists yet — move it once open question 3 answers. Bet count is 4, inside the 3–5 ceiling. Two primary goals plus one secondary — inside the cap, but goal 2 (revenue) is conditional on open question 5; if that comes back "adoption only," this charter needs a re-pass before the board sees it.

Next: send open questions 1, 2, 5, and 7 to the VP of Engineering — those four decide whether this charter's shape holds at all.