Read the skill and its three reference files (`program-archetypes.md`, `build-vs-buy.md`, `charter-example.md`) in full. Saltmere's situation — sales-funded DevRel, a named technical-evaluation leak, company-adoption motion, tight capacity — maps closely to the skill's "evaluation-support" archetype and its worked company-adoption example. You asked for the whole document in one go rather than the skill's default section-by-section interview, so I built it directly from what you gave me and flagged every place I filled a gap with a stated assumption instead of inventing a number.

Quick note before the document: I inferred Position (CORE), the exact drop-off numbers, competitor names, and budget-ownership detail — none of that was in your message. They're flagged inline and repeated in Open Questions so nobody mistakes them for confirmed facts in the board pack. Everything else — driver, stage, capacity, deadline — is exactly what you stated.

---

# DevRel charter: Saltmere, Board Review Horizon (11 weeks, ~Sep 23 – Dec 9 2026)

## Position

CORE, built from what's known today — confirm the flagged items before this scope hardens.

**Community.** Saltmere's developers are engineers evaluating an on-device speech SDK for production integration — most likely mobile, embedded and ML engineers at companies formal enough to run a technical evaluation before buying. *[Assumed]* Engagement today appears to run entirely inside the sales-led evaluation process (calls, sandbox access, ad hoc engineering support), not through a public or self-serve channel. Evaluator seniority mix and where they research alternatives before ever talking to sales are unknown.

**Organization.** DevRel is two people — you, and one advocate reporting to you — funded directly by the CRO. That funding line is itself a signal: the program is currently read internally as a sales-support function, not a product or brand function. What DevRel has shipped to date, and what (if anything) was tried before this funding relationship started, are unknown.

**Relationships.** The competitive set for an on-device speech SDK typically includes cloud speech APIs (the incumbent most evaluators are migrating off, usually for latency, cost or data-residency reasons) and DIY on-device/open-source alternatives. *[Assumed]* Named competitors and any existing integration or channel partners are unknown.

**Ecosystem.** On-device speech is a category where the buying trigger is usually a constraint cloud APIs can't satisfy — offline operation, latency, or data never leaving the device. That's almost certainly the mechanism behind "losing deals at technical evaluation": the evaluator has to *verify* that constraint holds, not just confirm accuracy. Closing that verification gap is what the pillar mix below is built to do.

**Lifecycle stage:** starting. Series A, program newly funded on the back of one named, specific pain — not an established practice with prior history to build on.

## Driver

**Primary: sales enablement.** Owner: CRO. In the CRO's own words — "our sales team keeps losing deals at the technical evaluation, fix that."

**Secondary: product input.** Owner: Head of Product *(name to confirm)*. Every stalled evaluation is a specific, nameable reason a deal didn't close — that reason belongs in the roadmap with an owner, not just in a sales post-mortem.

## Goals

- **Primary — activation.** Journey step: evaluation. Drop-off: technical evaluations stalling or dying before reaching a decision (stated by CRO; not yet quantified — see Open Questions).
- **Primary — revenue.** Journey step: commitment. Drop-off: evaluations that do complete aren't converting to signed deals at the rate sales needs.
- **Secondary — product.** Reasons evaluations stall get routed to the roadmap with a named owner, instead of dying in a sales rep's notes.

## Audience

**Primary path: company adoption.** A developer or engineer evaluates hands-on; an approver (engineering lead, security/privacy reviewer, or both) signs off before the deal closes. This is exactly what "losing deals at the technical evaluation" describes.

**Primary segment this horizon:** the technical evaluator — mobile/embedded/ML engineers at companies running a formal buy process.

**Not served this horizon:** individual/hobbyist developers experimenting outside a company evaluation. If a self-serve trial motion exists alongside the enterprise one, that's an open question that would change this call — confirm before next horizon.

## Pillar mix

**Enablement 60% · Advocacy (pre-sales facing) 35% · Marketing 5% · Community 0%.**

This is the **evaluation-support** archetype (sales enablement + company adoption, per the skill's archetype set) — the same shape a company-adoption/technical-evaluation problem gets in every version of this analysis. Marketing and community are deliberately starved: at 70 hours/month combined real capacity, funding a third pillar means funding three things at a level where none of them work. Community specifically has no density to justify a venue yet, and a venue is a standing job neither of you has hours for.

## Bets

Scoped smaller than this archetype's usual bet size (normally "about a quarter of one person's writing time" — closer to 120 hours each at typical capacity). At 70 hrs/month total, that scope doesn't fit; every bet below is a minimum-viable version, with depth explicitly deferred to a maintenance line next horizon.

1. **Proof-of-concept kit with a scoped success definition.** Goal: activation. Owner: advocate, reviewed by you and sales engineering (the kit has to match what sales already promises). Signal: share of evaluations that reach a completed PoC. Review: week 6.
2. **Security/privacy/licensing answer set** — the on-device, data-never-leaves-the-device story, written once. Goal: activation + revenue. Owner: you, reviewed by legal/security if one exists. Signal: evaluations no longer stalled pending a security or compliance answer. Review: week 8.
3. **Reference architecture for the top one or two platforms evaluators actually build on.** Goal: activation. Owner: advocate. Signal: reduction in integration back-and-forth during evaluation. Review: week 10.
4. **One named production reference.** Goal: revenue. Owner: you, with account/customer success sourcing the customer. Signal: a public reference an evaluator can check. Review: week 8 — **contingent**; if no customer will go on record by then, cut this bet rather than let it slip past board review (see Open Questions).

## Build vs buy

| Bet | Source | Latency | Reviewer | If it stops |
|---|---|---|---|---|
| 1. PoC kit | In-house | ~2 weeks to v1 | Sales engineering lead | Reverts to ad hoc, unscoped PoCs — the current failure mode |
| 2. Security answer set | In-house (judgment/red line — this is a claim about the product) | ~2 weeks | You | Stays as scattered answers in call notes |
| 3. Reference architecture | In-house content; contractor for diagram production only | ~3 weeks | Advocate | Docs go stale; not urgent to unwind |
| 4. Named reference | In-house relationship; contractor for interview transcription only | Depends on customer availability | You | No public proof point; not a decaying surface, just an absent one |

No agency anywhere: an agency's published pipeline setup alone runs ~6 months, which doesn't fit an 11-week horizon. No community-sourcing: no contributor or community density exists yet to draw on.

## Staffing

**Stage:** Grow, two generalists, neither yet specialized. Capacity: 70 hrs/month combined; committing 49 hrs/month (70%) to the bets above, holding 21 hrs/month for sales fire-drills and support.

**No new hire this horizon.** Trigger for the next hire: PoC-kit requests from sales exceed what two people can turn around inside a live sales cycle for two consecutive months. If that trigger fires, the next hire leans solutions-engineering/pre-sales, not a generalist advocate or a community manager — neither of those removes the constraint that's actually binding.

## Refused

- **No conference sponsorship or travel this horizon.** Doesn't touch the technical-evaluation leak, and the budget it would take is bet 1 and bet 2 combined.
- **No public community venue (Discord/forum).** No density to seed it, and it's a standing job neither of you has hours for.
- **No top-of-funnel content or blog series this horizon.** The team wants this — it's refused anyway, because 70 hrs/month can't fund two archetypes at once, and awareness isn't the funded driver.
- **No broad developer marketing push.** Same reasoning: it reaches people who aren't the ones currently saying no to a deal.

## Open questions

- **How many evaluations stall, and where exactly.** CRO named the pain qualitatively; no number exists yet. Owner: you + sales ops, by week 2 — this sets the real baseline for bet 1's signal and the whole charter's credibility at board review.
- **Does the CRO-funded budget include your two salaries, or only program spend?** Unconfirmed. Owner: CRO, before the next planning cycle — this changes what "funded" actually means in front of the board.
- **What's been tried before to unblock evaluations, and why didn't it work?** Unknown. Owner: you, via sales interviews in the first two weeks.
- **Will any current customer go on record as a named reference?** Unresolved — bet 4 depends on it. Owner: account/customer success, by week 6; if no by week 8, cut the bet rather than carry it into the board pack unresolved.
- **Who does Saltmere actually lose evaluations to — cloud APIs, another on-device vendor, or a DIY build?** Unknown in detail. Owner: you + product marketing — this shapes how bets 2 and 3 are framed.
- **Does a self-serve/individual-developer trial path exist alongside the enterprise motion?** If yes, Step 4's audience call needs revisiting next horizon.

## Exec narrative

Sales is funding developer relations because deals are dying during technical evaluation, not before it. Over the next eleven weeks we are building the three things evaluators ask for and can't currently get fast enough: a proof-of-concept kit with a clear finish line, a straight answer to the security and privacy questions our on-device architecture should already be winning on, and reference architectures for the platforms evaluators actually build on. We are not running events, starting a community, or writing top-of-funnel content this horizon — none of that reaches the person currently saying no. Success is more evaluations finishing, and finishing faster, not more people hearing about us. By board review, we should be able to show how many evaluations moved from stalled to decided, and hand sales a repeatable kit instead of a one-off scramble each time.

## Review

Re-decision at board review (~Dec 9 2026 — confirm exact date). Early re-decision triggers: the CRO sponsor changes, bet 1's signal hasn't moved by week 8, or bet 4's reference fails to materialize by week 8.

---

## Quality gate

**Structural — all pass:**
- Driver: one named reason, one named owner, in the funder's own words. ✓
- Each goal names a journey step and a drop-off. ✓ (Note: the drop-off is stated qualitatively by the CRO, not yet quantified — that's the first open question, not a gap in the charter's logic.)
- Every bet has one owner, one signal, one review date, traced to one primary goal. ✓
- Refused list is non-empty and includes one thing the team wanted (the content push). ✓
- Open questions are written down, not resolved by assumption. ✓
- Nothing on a credibility surface is outsourced — PoC kit, security answers, and the reference are all in-house. ✓
- Exec narrative: five sentences, no devrel jargon. ✓

**Baselines — none moved.** Capacity commitment sits at exactly 70%, two pillars funded above token level, three goals, four bets, five-sentence narrative — all at this skill's default. The real constraint isn't the numeric gate, it's that 70 hrs/month forces each bet to be scoped far smaller than this archetype's usual size; that's called out inline rather than hidden in the bet descriptions.