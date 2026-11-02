# Why not docs-first, and what to build instead

Skip the quickstart. Enablement-first is the default first move almost everywhere because most programs are serving people who haven't adopted yet — the docs fix a leak between "signed up" and "got value." That's not your leak. 4,000 companies already got a self-hosted workflow engine into production; nobody does that off a bad quickstart. Your leak sits three years downstream of the docs, at renewal, and it's a relationship problem, not a discoverability problem.

Two conditions override the default ranking here, both present at once: the driver is retention of an already-adopted installed base, and your chair explicitly asked for a compounding asset, not a quarter number. That combination promotes **community-first** over enablement-first. Below is the full charter.

**Archetypes considered, briefly:**

| | Enablement-first (the default) | Evaluation-support | Community-first (recommended) |
|---|---|---|---|
| Fits | Adoption *before* first success — activation | Re-evaluation gates in enterprise renewal | Retention of an installed base, referral |
| First bets | Quickstart, error coverage | Reference architectures, security answers | Venue, founding cohort, champion recognition |
| Starves | Events, community | Hobbyist content, broad awareness | Paid reach, gated content |
| Effort | Quarter of one person's time, then near-zero | Quarter of one person's time, standing sales coordination | Standing job, daily answer-time discipline |
| Fastest signal | Share reaching first success | Evaluations reaching a technical decision | Questions answered by non-staff, week-4 return rate |
| Wrong pick when | Nobody's activating yet — not your case | Product is bought bottom-up, not your case | Base too small/async for conversational density — untested, see open questions |

Enablement-first isn't deleted — it survives as a downstream maintenance line, fed by what the community actually gets stuck on, instead of a guess made before anyone asked. Evaluation-support is worth revisiting if open question 1 below turns up renewal stalling at a procurement gate rather than a relationship gate, but nothing in what you've told me points there yet.

---

# DevRel charter: Vasterly, Q4 2026 – Q1 2027

## Position

**Community.** ~4,000 companies self-host Vasterly, a substantial installed base with no confirmed venue of our own. Engagement pattern is unknown — likely transactional (support tickets, maybe scattered GitHub issues) rather than peer-to-peer. This is the central fact the docs-first advice misses: the audience isn't small and forming, it's large and already committed, just not connected to each other.

**Organization.** Two people, real budget, no prior structured devrel effort described. Reporting line to the board chair, who set the mandate directly and will be the one reading results against it. Whether "real budget" includes these two salaries or only program spend is unconfirmed — flagged below, because a plan built on the wrong side of that line proposes work nobody can pay for.

**Relationships.** Self-hosted, workflow-engine category — competitors likely include both hosted-first alternatives and other self-hosted orchestration tools. Each of the 4,000 companies is simultaneously a customer and a potential peer-reference for the next one; nothing currently connects them to each other.

**Ecosystem.** Renewal-funded, not signup-funded — the business model is closer to enterprise infrastructure software than to a developer-signup SaaS. This matters for every choice below: reach and conversion metrics don't touch the thing the board is watching.

**Lifecycle stage.** Growing as a product (4,000 companies, years of production self-hosting), but starting as a devrel program (two people, nothing structured yet). That mismatch is the whole story — most "start with docs" advice is written for programs where the product is also starting.

## Driver

Developer adoption, in its retention phase: keeping the 4,000 companies who already adopted us, not acquiring new ones. Owner: the board chair, who set the three-year compounding mandate directly and rejected a quarterly-number framing.

Secondary: product input. Self-hosted operators carry the operational pain — upgrade breakage, scaling limits, missing integrations — that plausibly drives non-renewal, and today nothing routes it back with an owner.

## Goals

- **Primary — Retention** (journey step: standardization). Best current read, pending validation: renewal risk concentrates in accounts where one internal champion carries the whole relationship — when that person leaves or goes quiet, nothing else sustains the renewal case.
- **Primary — Referral** (journey step: advocacy). Best current read: problems one company solves in its deployment stay invisible to the other 3,999 — no peer proof compounds outward, which costs both internal seat expansion and new-company word of mouth.
- **Secondary — Product** (journey step: recurring evaluation, at renewal). Best current read: operational pain that actually threatens renewal isn't systematically captured or fed to the roadmap with an owner.

All three are stated as the best current read, not measured fact — see open questions. That's a gap to close in the first month, not a reason to wait.

## Audience

Primary: the operator/champion inside each of the 4,000 companies who runs Vasterly day to day and supplies the internal renewal case. This is a company-adoption motion layered on an individual relationship — the champion drives daily use, but renewal has to survive that person's absence, promotion, or departure.

Not served this horizon: brand-new prospects at companies not yet running Vasterly. That's an acquisition problem, and it isn't what the chair asked to fund.

Segment for the founding cohort: unset until account-level renewal-date and size data exists (open question 2). Provisional priority: champions at accounts renewing soonest and largest, once that list exists.

## Pillar mix

Community 55%, enablement 35% (built downstream of community threads, not upfront), advocacy 10% (folded into community work — champion recognition, not a standalone speaking track), marketing 0%.

Two pillars funded above token, per this skill's own capacity baseline for a two-person team. Marketing is deliberately starved: reach into an already-adopted base doesn't move renewal.

## Bets

1. **One venue for the install base**, async and searchable (default: a Discourse-style forum over chat — indexed answers keep paying off in year three, chat history doesn't; final pick depends on open question 4). Goal: retention + referral. Owner: community lead. Signal: questions answered by someone other than staff, week-4 return rate of the founding cohort. Review: week 8.
2. **Founding cohort, seeded by hand** — personally invite champions from the highest-value renewal accounts before opening the venue publicly. Goal: retention. Owner: community lead. Signal: founding-cohort participation rate. Review: week 6.
3. **Champion recognition inside the venue** — visible credit for the first peer answers, positioning champions publicly enough that their internal renewal case doesn't depend on them alone. Goal: referral. Owner: community lead. Signal: repeat contributors in month two. Review: week 12.
4. **Operational hardening guides**, drafted from the venue's hardest recurring threads (upgrades, scaling, migration) — documentation as an output of community signal, not a guess made first. Goal: retention (secondary: product). Owner: enablement lead. Signal: support tickets per hundred existing accounts. Review: week 14.
5. **A quarterly "what we fixed because you told us" note** — closes the product-input loop and doubles as renewal-trust evidence. Goal: product. Owner: enablement lead, product owner co-signs. Signal: shipped changes traceable to a community thread. Review: quarterly.

At most 70% of these two people's declared time is committed to the five bets above; the rest absorbs whatever the venue itself surfaces in month one.

## Build vs buy

| Bet | Source | Latency | Setup cost | Reviewer | If it stops |
|---|---|---|---|---|---|
| 1. Venue | In-house build (moderation policy is a red line); buy the hosting | 3–4 weeks to open | Platform pick + moderation policy | Community lead | A closed venue is public evidence against the program — don't open before the cohort is seeded |
| 2. Founding cohort | In-house only | Ongoing, by hand | None beyond time | Community lead | N/A — relationships aren't outsourceable |
| 3. Champion recognition | Community-sourced content (champions write it), in-house review | Rolling | Recognition policy | Community lead | Decays quietly; low cost to restart |
| 4. Hardening guides | In-house drafting; contractor for surge once thread volume outpaces two people | 4–6 weeks per guide | Style brief | Enablement lead | Guides go stale but don't actively mislead — acceptable if paused |
| 5. Feedback loop | In-house only | Quarterly | None | Enablement lead + product owner | Silent trust erosion if dropped — don't start it unless it can run every quarter |

## Staffing

Stage: grow — two existing people specializing now, not hiring yet. Community lead owns the venue, cohort, moderation, champion relationships. Enablement lead owns documentation and the product-feedback routing, both downstream of what the venue surfaces.

Next hire and trigger: a second community-facing person, or a paid/perked moderator role for an emerging champion, when answer-time discipline can't hold for two consecutive months, or founding-cohort volume outgrows one person's cadence. Not funding a formal champion/ambassador program yet — bet 3 is its seed; formalize only once density shows the Leggetter test (more output than input added).

## Refused

- No documentation rewrite as the opening bet. The standard advice assumes a program serving new arrivals; ours already got 4,000 companies to production. Docs still get built — item 4 — but downstream of what the community actually gets stuck on.
- No paid reach or advertising this horizon. It targets acquisition, not the driver the chair funded, and it's a standing job whose payoff doesn't compound the way an indexed venue does.
- No conference sponsorship or event program this horizon — doesn't fit two-person capacity, doesn't target renewal.
- No Discord/chat as the flagship venue, even though it's the "normal" choice the team may expect — chat history doesn't compound against a three-year mandate the way a searchable forum does.
- No formal enterprise procurement/security-questionnaire buildout until evidence shows renewals actually stalling at that gate rather than at the champion-relationship level.

## Open questions

1. What actually drives non-renewal today — any churn or exit-interview data? Owner: whoever holds customer-success/billing data, by week 3. This decides whether evaluation-support should ever get promoted.
2. Segmentation of the 4,000 companies by renewal date and account size — needed to prioritize the founding cohort. Owner: whoever owns the account list, by week 4.
3. Does the stated budget include the two people's salaries or only program spend? Owner: the board chair, before the next planning cycle.
4. Where, if anywhere, do these companies already informally gather (GitHub issues, an unofficial Slack, forum threads)? An existing venue should be adopted, not orphaned by a new one. Owner: community lead, by week 2 — gates bet 1's platform choice.
5. Are there any champions already willing to go on record? Owner: whoever has customer relationships today, by week 6 — without at least a few, the founding cohort has nothing to seed from.

## Exec narrative

Our 4,000 customers already chose us once; renewal depends on whether the person who championed that choice still has support two and three years later. This half we build one place where the people running Vasterly can solve each other's hardest problems in public, seeded by hand with real customers instead of opened cold and quiet. We are not rewriting the quickstart or buying advertising, because neither explains why an existing customer would choose not to renew. Every hard problem solved there becomes documentation and a product fix for free, so the same work keeps paying off instead of being redone each quarter. Watch for a rising share of questions answered by customers instead of us, and a founding group that keeps coming back — by year three this is a body of operating knowledge on running Vasterly that no competitor can copy quickly.

## Review

Re-decision at week 16 (end of Q1 2027), against the multi-quarter mandate, not a single-quarter number. Early re-decision if: the funding sponsor changes; the founding cohort's week-8 return rate is near zero (wrong venue or wrong seed list — check open question 4 first); or open question 1 reveals renewal actually breaks at a procurement gate, which would promote evaluation-support instead.

---

## Quality gate

**Structural — all pass:**
- Driver named once, in the funder's language, with a named owner (the chair). ✅
- Each goal carries a journey step and a stated drop-off — flagged as best-current-read pending validation, not resolved by silent assumption. ✅
- Every bet traces to one primary goal, has an owner, one signal, one review date. ✅
- Refused list is non-empty and includes the thing the team likely expected to build (docs-first, Discord). ✅
- Open questions written down, not assumed away — five of them, each with an owner and a date. ✅
- Nothing on a credibility surface is outsourced — moderation, champion relationships, and technical answers all stay in-house; only volume (surge documentation drafting, hosting) is bought. ✅
- Exec narrative carries no devrel jargon. ✅

**Numeric baselines — this skill's own defaults, moved once, argued:**
- Two pillars funded above token (community, enablement) — kept at default.
- Three goals (two primary, one secondary) — kept at default.
- Five bets — at the top of the 3–5 range, justified by two people covering both the venue and its documentation output; consider cutting to four if week-8 review shows bet 5 competing for the same hours as bet 1.
- 70% capacity ceiling — kept at default, stated explicitly in staffing.
- Five-sentence exec narrative — kept at default.

One real gap: goals 1–3 rest on inference from what you've told me, not on churn data you've confirmed exists. That's honestly logged as open question 1, with an owner and a week-3 deadline — not smoothed over, because it's the fact most likely to redirect this charter if it turns out wrong.