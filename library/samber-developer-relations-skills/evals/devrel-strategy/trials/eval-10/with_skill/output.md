# DevRel charter: Hestbury, Q4 2026 – Q1 2027

*Built by applying `devrel-strategy` directly against what you gave me, rather than a live turn-by-turn interview. Where the Interview (steps 1–14) would normally have gotten a direct answer from you, I've either drawn the conclusion the facts already support, or logged it as an Open Question below instead of guessing. Don't read any number in here as sourced — this is a first pass; every baseline is marked for what it actually is.*

## Position (CORE)

**Community.** Hestbury's community today is not a community — it's a distribution list of partners who've already signed and are now integrating the compliance API into their own products. There's no venue: no forum, no chat, nothing peer-to-peer. The only channel through which friction reaches you is the support ticket, which means engagement is 100% transactional and 0% self-serve. The strongest signal you already have — "partners keep filing tickets our docs should have answered" — is an enablement gap wearing a support-cost costume.

**Organization.** The product roadmap is locked through next year around a large enterprise commitment; there is no capacity this horizon to absorb anything DevRel routes back to product. Nobody has told me who owns docs today (engineering, product, or nobody) — that's an open question, but the ticket volume already tells you docs aren't closing the loop regardless of who owns them. The founder has a standing, explicit refusal to run a Discord or Slack of Hestbury's own, on the belief that it becomes a support queue. That belief isn't hypothetical here — the tickets are already the support queue the founder is trying to avoid creating a second front door for.

**Relationships.** Partners are the only named external relationship class. The business relationship is already closed — they signed — so what's broken sits entirely on the technical execution side, post-commitment. Nothing you've told me points to an unaffiliated, self-serve individual-developer audience distinct from partners; I'm not assuming one exists (see Open Questions).

**Ecosystem.** Compliance-automation is a regulated, accuracy-sensitive category. Partners embedding your API likely answer to their own internal compliance or security reviewers during implementation, not just at the point of signing — so documentation is still doing evaluation-support work even after the contract is signed. It's a public API, so self-serve technical execution isn't a nice-to-have on top of the product, it *is* the product experience for the partner's engineers.

**Lifecycle stage: growing.** You have a real partner base and a real enterprise commitment — this isn't a from-zero start. But the documentation-as-a-system maturity and the DevRel function itself are early.

## Driver

**Primary: developer enablement** — your own words. **Owner:** not named in what you gave me — flagged in Open Questions rather than invented.

**Secondary: ecosystem and partnerships.** The specific friction you named is with partners specifically, which is its own named driver in this framework; it's secondary because the words you used to fund the work were "developer enablement," not "partnerships."

**Explicitly not a driver this horizon: product input.** The roadmap is locked. Nothing DevRel surfaces gets built this year, so "route feedback to product" isn't a live goal — it's a way to burn trust with partners by asking them to repeat themselves into a queue that doesn't move.

## Goals

**Primary — Activation.** Partners' engineers reach a working integration without opening a ticket. Observed drop-off: partners are already past initial and deep awareness and past commitment — they signed — and are stalling at the technical execution step your journey model calls *commitment → standardization*. That's exactly where a docs gap shows up as a ticket instead of a churn signal.

**Primary — Retention.** Partners keep operating the integration without recurring ticket-driven friction. Same journey step, later in time: *standardization*. A partner whose engineers keep re-hitting doc gaps months in is a live renewal/expansion risk, not just a support cost.

**Secondary — Revenue.** Framed narrowly as *cost avoided*, not pipeline: fewer tickets is fewer support hours, and friction-free partners are less likely to stall an expansion. I have not been given a number connecting ticket friction to actual renewal or expansion risk — that link is inferred, not observed, and it's in Open Questions. Don't repeat "Revenue" externally as anything stronger than "estimated cost avoided" until that number exists.

Three goals, two primary, one secondary — at the cap this charter allows itself.

## Audience

**Primary segment: partner-integrator engineers** — the individual developers, inside already-signed partner companies, who personally write the integration code. The *relationship* is company-adoption (someone else signed), but the *felt experience* and the metrics that matter are individual-developer: time-to-first-success, troubleshooting, self-serve resolution. Build for that.

**Not served this horizon:** any unaffiliated, self-serve individual developer evaluating the API without a partner agreement — if that segment exists at all. I don't have evidence it does; see Open Questions. If it turns out to exist, most of what this charter funds (quickstart, reference, compliance answers) still serves it — that's deliberate, see below.

**Artifacts that serve both paths, built once:** the integration quickstart, the API reference, the compliance/security/licensing answer set, and honest statements of what the product doesn't do.

## Pillar mix

**Enablement, funded above token level. Everything else — advocacy, marketing, community — at token or zero.** One pillar funded properly beats four funded at 25%, and this program has exactly one problem named by its funder: docs aren't answering the questions partners already have. Community is starved on the founder's explicit, standing refusal, not a resourcing call — don't revisit this quarterly, it isn't a live question.

## Step 3 — Candidates considered, and why two were deleted before ranking

Two archetypes were deleted outright rather than ranked last, per the skill's own instruction not to park ruled-out shapes at the bottom where they come back as scope:

- **Product-feedback** — deleted. The roadmap is locked through next year around the enterprise commitment; there's no capacity to act on anything this archetype would surface.
- **Community-first** — deleted. The founder will not fund a venue of Hestbury's own, and nothing in what you've told me argues for testing that refusal this horizon.
- **Contributor-first** — also deleted, on applicability grounds: nothing here describes an open-source project or public repository. There's no codebase to recruit contributors into.

That leaves three survivors, in this skill's own efficiency order:

**Candidate A — Enablement-first (recommended)**
- Over-invests in: enablement (quickstart, troubleshooting, reference).
- First three bets: rebuild the integration quickstart to first successful call; close troubleshooting coverage for the top ticket-generating errors; ship an agent-/machine-readable API reference surface.
- Deliberately starves: events, content reach, any community venue.
- Capacity needed: roughly a quarter of one person's writing time to start, near-zero maintenance after — this skill's own baseline for the archetype, and realistic for a single owner.
- Fastest signal: tickets per 100 active partner integrations, and share of partner integrations reaching a working call without a ticket.
- Wrong pick when: ticket-mining shows partners aren't actually stuck on documentable mechanics but on account-specific config or contract terms no generic doc can fix. Test this in the first 4–6 weeks (see bet 2) before assuming it away.

**Candidate B — Evaluation-support**
- Over-invests in: enablement (enterprise-flavored) plus advocacy, pre-implementation facing.
- First three bets: reference architectures for common integration patterns; a written security/licensing/compliance answer set; named production references.
- Starves: hobbyist content, broad awareness, generic troubleshooting volume.
- Capacity needed: about the same quarter of writing time as A, plus a standing coordination relationship with whoever owns partner/sales accounts — a second standing relationship A doesn't require.
- Fastest signal: implementations reaching a working technical decision without escalation, and time from partner kickoff to first successful integration.
- Wrong pick when: ticket-mining shows the actual pattern is "how do I call X" mechanics rather than compliance/security/licensing questions — then this is a more expensive way to solve a problem A already covers.

**Candidate C — Reach-first**
- Over-invests in: content and search reach.
- First three bets: search-durable content on compliance-automation problems partners already search for; a couple of matched ecosystem appearances; a repeatable launch beat.
- Starves: docs depth, troubleshooting coverage, any partner-facing enablement work.
- Capacity needed: a standing job — the cadence is the product, and stopping it loses everything it compounded.
- Fastest signal: qualified non-paid arrivals, and whether new arrivals reach first success at the same rate as existing partners.
- Wrong pick when: **now.** This archetype's own documented failure condition is reach into a leaking activation path — it "burns the audience once and teaches it the product does not work." That's precisely the situation you described.

**Recommendation: Enablement-first.** It's the archetype your own funding language already names, it targets the one drop-off you've actually observed, it needs no new standing relationship to start, and it's the cheapest of the three to reverse if the ticket-mining in bet 2 proves it wrong. Candidate B isn't discarded — bet 3 below is borrowed from its bet list, because Hestbury's compliance-product context makes a security/licensing answer set worth funding regardless of which archetype wins. If ticket-mining shows most tickets are compliance/security questions rather than integration mechanics, re-weight toward B without waiting for the full-horizon review.

## Bets

| # | Bet | Goal | Owner | Signal | Review |
|---|-----|------|-------|--------|--------|
| 1 | Rebuild the integration quickstart so a partner engineer reaches a working authenticated call without opening a ticket | Activation | DevRel lead, reviewed by engineering | Share of new/renewing partner integrations reaching a working call within 14 days, without a ticket | 2026-11-18 |
| 2 | Mine the last two quarters of partner tickets; close troubleshooting-doc coverage for the top errors generating them | Activation + Retention | DevRel lead, drafted from support data | Tickets per 100 active partner integrations; docs deflection on targeted categories | 2026-12-02 |
| 3 | Write the security/licensing/compliance answer set once — the questions a partner's own reviewer re-asks during implementation | Retention | DevRel lead, signed off by whoever owns compliance/legal internally (name TBD) | Reduction in pre-integration and mid-implementation compliance/security tickets | 2026-12-16 |
| 4 | Ship a machine-readable API reference surface generated from the existing API spec | Activation | DevRel lead, reviewed by engineering | Reduction in "how do I call X" tickets | 2027-01-13 |

Four bets, inside the three-to-five range this skill sets as its own ceiling.

## Build vs buy

| Bet | Source | Latency | Setup cost | Reviewer | If it stops |
|-----|--------|---------|------------|----------|-------------|
| 1 — Quickstart rebuild | In-house | ~3–4 weeks | None beyond writing time | Engineering lead | Reverts to current (broken) state — no decay below that |
| 2 — Troubleshooting pages | In-house drafting; contractor editor for surge once volume is known | ~4–6 weeks after ticket-mining | One style brief for the contractor | Whoever triages partner tickets today | Pages stay, don't decay; mining pipeline stops |
| 3 — Compliance answer set | In-house only — no menu here | ~4–5 weeks | Legal/compliance sign-off once, reopened at material product change | Compliance/legal owner (TBD) | Frozen, doesn't self-correct — needs an owner to keep it current |
| 4 — Machine-readable reference | In-house build; contractor may build the generator tooling, not the content | ~5–6 weeks | Generator build time | Engineering lead | Reference goes stale against the live API without someone maintaining the generator |

No agency and no community-sourced option anywhere on this sheet: none of these four bets is a recurring content-volume play (the published agency pattern's own ~6-month pipeline setup doesn't fit a ticket problem you need closed this horizon), and there's no community venue funded to source contributions from. Bet 3 in particular is a hard red line — "any claim about the product's limits" is never outsourced, full stop, no ranking, no exception.

## Staffing

**Stage: seed (assumed).** Nothing in what you gave me states current DevRel headcount — I'm assuming one generalist owns this, and flagging the assumption in Open Questions rather than treating it as confirmed. At seed, finish bet 1 before adding scope anywhere else.

**Next capability:** a technical writer or docs engineer, triggered when the single owner's authoring/review backlog exceeds two weeks for two consecutive months — the same trigger this skill's own worked example uses for this exact archetype. Not before: a second hire without a demonstrated backlog adds coordination cost this program doesn't need yet.

**Not hiring:** a community manager. No community pillar is funded this horizon, so there's nothing for the role to run.

## Refused

- **No Discord or Slack of Hestbury's own**, this horizon or any future one absent a founder reversal. Explicit standing refusal; the founder's stated reason — it becomes a support queue — is already true of the ticket volume you have today, just arriving through a different door.
- **No product-feedback loop or promise to route partner friction into the roadmap** this horizon. The roadmap is locked around the enterprise commitment. Collecting friction the org can't act on costs trust with both partners and product — this is very likely what the team most wanted to do and can't yet.
- **No conference sponsorship or paid content-reach push** this horizon. Awareness isn't the funded driver, and reach into an unresolved activation leak burns the audience it reaches.
- **No agency-produced content pipeline** this horizon. Its setup latency doesn't fit a problem that needs closing now, and there's no reach/volume goal on this charter to justify starting that clock.

## Open questions

- **Who owns/authorizes the DevRel budget** (name, role)? Needed to fill the Driver owner line honestly — currently blank rather than guessed.
- **Does a self-serve individual-developer segment exist** outside the named partner relationships, or is all API usage partner-mediated? Determines whether the "not served" line in Audience is actually empty.
- **What share of partner tickets are genuinely docs-answerable** versus account-specific config or contract questions no generic doc can fix? Sizes the real ceiling on bets 1 and 2 — get a first read from ticket-category mining before finalizing bet 2's scope.
- **Does ticket friction actually correlate with renewal or expansion risk** in named partner accounts? Without this, the secondary Revenue goal is an inference, not an observation — don't present it to the founder as more than that until it's checked.
- **Who currently owns docs** — engineering, product, or nobody? Determines the real reviewer for bets 1 and 4, and whether "docs engineer" is an existing role or the next hire.
- **Current DevRel staffing today.** Confirms or corrects the seed-stage assumption in Staffing.

## Exec narrative

DevRel is funded to make partners successful with our API on their own, not through our ticket queue. Partners keep filing tickets our documentation should already answer, which means integration is slower and more expensive for them, and for us, than it needs to be. This half we rebuild the quickstart, close the troubleshooting and compliance-reference gaps generating the most tickets, and make sure partner engineers get correct answers without waiting on us. We are not opening a Discord or Slack, sponsoring events, or promising roadmap changes this half, because none of those fix a documentation gap. By the end of the half you should see fewer tickets per active partner integration, and partners reaching a working integration faster.

## Review

Next full review: end of horizon (2027 Q1 close). Early re-decision if: bet 1's signal hasn't moved by 2026-11-18; the funding sponsor changes; or ticket-mining (Open Question 3) shows most tickets aren't actually docs-answerable, which would push the program toward Evaluation-support rather than deeper into Enablement-first.

---

## Quality gate — reported explicitly

**Structural — pass/fail, nothing negotiable:**

- Driver: one named reason, in the funder's own words. **Owner not named** — no name was given, and I'm not inventing one. This line is incomplete by design until Open Question 1 is answered; flagging rather than hiding it.
- Each goal names a journey step and an observed drop-off, not a preference. **Pass** — Activation and Retention both trace to the one drop-off you named; Revenue is explicitly labeled inferred, not observed, in the Goals section itself.
- Every bet traces to one primary goal, has an owner, a signal, a review date. **Pass.**
- Refused list is non-empty and includes something the team wanted. **Pass** — the product-feedback refusal is flagged as the likely wanted-but-cut item.
- Open questions are written down, not resolved by assumption. **Pass** — six logged, including the seed-stage staffing assumption.
- Nothing on a credibility surface is outsourced. **Pass** — bet 3 (compliance claims) is explicitly in-house only, no menu.
- Exec narrative uses no devrel jargon. **Pass** — five plain sentences, no "activation," "pillar," or "AAARRRP" in the narrative itself.

**Numeric lines — this skill's own baselines, not external standards, moved where I had reason to:**

- At most 70% of declared capacity committed: **not yet checkable** — no real headcount/hours number exists (Open Question 6). Apply once that's answered rather than fabricating a percentage now.
- At most two pillars funded above token level at seed/grow: **passes with room to spare** — only one pillar (enablement) is funded above token level here.
- Three goals maximum: **exactly three** (two primary, one secondary).
- Three to five bets: **four.**
- Five sentences for the exec narrative: **exactly five.**

---

# KPI dashboard: ten metrics, reported monthly

**One flag before the sheet:** the skill this charter hands measurement decisions to (`devrel-metrics`) caps its own recommended sheet at five to eight rows — "a sheet of five that gets refreshed beats twenty that rot by month three." You asked for ten. I've built all ten, holding them to the same rigor that skill requires (six fields each, tiered, attributed, anti-vanity-tested) rather than either padding to hit ten or silently cutting to eight. The **kill rule** at the bottom is doing real work here, not just formality — it's the mechanism meant to bring this back toward a sustainable size after the first couple of review cycles, and I'd use it.

**Spine:** driver-anchored (AAARRRP) — chosen because the charter above already names the goals; one primary metric per goal.

**Driver and goals:** developer enablement (primary) — "partners keep filing tickets our docs should have answered." Goals: activation, retention, revenue (cost-avoidance framing).

## Metric sheet

| # | Metric | Goal | Tier | Definition | Source | Baseline | Threshold | Owner | Action if breached |
|---|--------|------|------|------------|--------|----------|-----------|-------|---------------------|
| 1 **P** | First-success rate, integration | Activation | Enablement | Share of new/renewing partner integrations reaching a defined successful authenticated call within 14 days of kickoff, with no ticket opened in between | Product/API analytics + support system (ticket-free flag) | baselining | set at next review once one period exists | DevRel lead | Cold-run the current integration path, fix the top failing step |
| 2 | Median time to first successful call | Activation | Enablement (supporting) | Kickoff → first successful authenticated call, median | Product analytics | baselining | baselining | DevRel lead | Instrument step-level drop-off to locate the slow step |
| 3 | Step-level drop-off, integration path | Activation | Enablement (supporting) | Share of partner integrations abandoning at each documented integration step | Docs + product analytics | baselining | baselining | DevRel lead + engineering | Prioritize the next doc/troubleshooting bet against the worst step |
| 4 **P** | Support ticket load per 100 active partner integrations | Retention | Enablement | Tickets opened ÷ active partner integrations × 100, trailing 30 days | Support system | baselining (support system should already have 1 period of history) | above trailing baseline for 2 consecutive months *(baseline)* | Support lead + DevRel lead | Mine top ticket categories into troubleshooting pages (bet 2) |
| 5 | Docs self-serve resolution / satisfaction | Retention | Engagement — **counter-metric to #4** | Share of resolved tickets where the partner reports (one optional question) "documentation could have answered this without a ticket"; or CSAT on the doc page tied to the resolution | Post-ticket micro-survey, self-reported | baselining | baselining | DevRel lead | If satisfaction drops while ticket count also drops, treat as suppression, not resolution — investigate before reporting #4 as improved |
| 6 | Docs/support search terms with no answer found | Activation | Engagement | Count and top terms per period where a partner's question found no existing doc answer | Docs search log, or ticket text if no search log yet *(instrumentation dependency — flag if absent)* | baselining | directional — watch top terms, no fixed line | DevRel lead | Convert top 3 recurring no-result terms into a doc or troubleshooting page each cycle |
| 7 | Cold-run defect count, integration path | Activation | Enablement | Failures found running the documented integration path on a clean/sandbox environment, monthly | Scheduled cold-run test | baselining | above 0, sustained 2 consecutive months *(baseline)* | DevRel lead + engineering | Fix before next content push; recurring defects mean restructure the doc, not just patch it |
| 8 | 90-day retention: ticket-flagged vs. non-ticket-flagged partners | Retention | Product impact | Cohort comparison — are partners who hit a doc gap (ticketed in their first 30 days) less likely to still be actively calling the API at 90 days than those who weren't | Product/API analytics joined to support system *(needs a cohort tag — instrumentation dependency)* | baselining, needs one full 90-day window post-tagging | baselining | DevRel lead + whoever owns analytics | If the gap is real and large, escalate integration-path fixes as the top priority next cycle |
| 9 **P** | Support cost avoided (deflection) from shipped troubleshooting content | Revenue | Business impact | Estimated ticket volume avoided in the specific category a shipped doc page targets, pre/post on a recorded pre-period per page | Support system, pre/post per targeted category | baselining per page shipped | reported, not targeted, for the first two cycles | DevRel lead | None while baselining; once stable, prioritize future troubleshooting bets toward the highest-deflection categories |
| 10 | Verbatim partner friction findings | Retention | Qualitative | Dated quotes and friction findings from real tickets/conversations, with the fix shipped and its date, tagged high/medium/low confidence | Manual log, DevRel lead | baselining | fewer than 2 logged findings in a period *(baseline flag)* | DevRel lead | Schedule direct partner conversations if the log goes quiet |

**Primaries:** #1 (Activation), #4 (Retention), #9 (Revenue) — one per goal, as required. #8 and #9 satisfy the "at least one product- or business-impact metric" rule twice over. None of the ten is a monotonic cumulative count; all are rates, ratios, or bounded period counts, so none fails the monotonic test as a primary. #4 is paired with its counter-metric (#5) specifically because a team incentivized to cut ticket count could hit the number by discouraging tickets rather than resolving the underlying gap — pairing catches that.

## Attribution rule

- **Pre/post lift**, per shipped doc page, is the primary method — used only for metric #9. Each page's own pre-period is recorded before it ships. Claimed as direction and rough magnitude only, never a point estimate.
- **Self-reported micro-question**, attached to #5 — one optional question at ticket resolution. Read as self-reported, not as precision measurement.
- **No tagged-link/last-touch analytics** in this sheet — there's no net-new acquisition funnel being measured this horizon (the audience is existing, already-signed partners), so last-touch attribution has nothing to attach to.
- **No influenced-pipeline or sourced-revenue claim.** "Revenue" on this sheet means cost avoided (#9), never pipeline. This is a deliberate choice under the "no sales metrics on DevRel" position (Thengvall), consistent with the funded driver being enablement, not sales — and it's fixed for the horizon; any change is reported as a restatement, not a silent redefinition.
- **Named blind spots:**
  - A partner engineer who solves a problem and tells five colleagues, with no ticket and no doc-search hit, is invisible to every metric on this sheet.
  - AI assistants or search answering from Hestbury's own docs without a visit or a ticket are invisible here too.
  - A partner who quietly churns without ever filing a ticket won't show up in ticket-based metrics (#4–#7) — #8 has to be watched on its own terms, not read as a proxy confirmed by falling ticket counts.
  - If a self-serve individual-developer segment turns out to exist (Open Question 2 in the charter), this sheet doesn't cover it at all.

## Reporting

- **Monthly (operational):** all ten rows, one page, trend against trailing baseline, to the DevRel budget owner (name TBD — Open Question 1).
- **Quarterly (decision):** full sheet plus the qualitative log (#10), with kill-rule status per metric, to whoever holds the broader budget review.
- **Annual:** re-derive the sheet from the driver; assume several rows change once real baselines exist and the framework is pruned toward the 5–8 range this skill actually recommends.

**Five-sentence summary, repeatable without you in the room:** "Partners keep hitting our documentation gaps and filing tickets instead of self-serving. We're tracking how many reach a working integration without a ticket, how many tickets that costs us per 100 active partners, and whether ticket-hit partners stick around at the same rate as everyone else. Everything we ship gets checked against whether it actually reduced tickets in the category it targeted, not just whether it shipped. We're not claiming pipeline or revenue — only support cost avoided, and only once we can show it. Most of this sheet is still baselining; real targets get set once a period of history exists."

## Known blind spots

No visibility into word-of-mouth resolution inside a partner's own engineering org. No visibility into AI-assistant-mediated doc consumption. No cohort tag yet joining ticket data to usage data (#8's precondition) — that's roughly the same class of instrumentation gap this skill would hand to `devrel-analytics`. No coverage of any self-serve individual-developer segment, because its existence itself is an open question in the charter above.

## Review

Next review: end of horizon (2027 Q1 close), same as the charter. **Kill rule, stated up front given this sheet runs above the skill's own recommended ceiling:** any metric that hasn't changed a decision in two consecutive review cycles gets cut, not kept — the target is to be back inside 5–8 live rows by the second full review, once baselining is done and it's clear which of these ten actually get acted on.