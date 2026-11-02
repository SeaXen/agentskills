# Developer education charter — Wrenmoor Certified Gateway Engineer, 2026 H2 → 2027 launch

The interview this skill normally runs one question at a time was pre-empted — you gave the tier decision, price, format, staffing model, and a retirement plan up front. I've built the charter around those as fixed inputs and marked every gap with an explicit assumption instead of stopping to ask. Three parts of the brief conflict with this framework's certification refusal checklist and its retirement guidance; flagging those isn't optional for this deliverable, so they're called out below before the charter proper, with the lowest-cost mitigation available given the "decision is made" constraint.

## ⚠️ Risks this design accepts as stated

1. **Impartiality conflict.** The team that writes and sells the $1,200 prep course also sets the pass/fail line. This is the exact conflict ISO/IEC 17024 exists to police: *"a body that also sells training must show that the training does not compromise the certification's impartiality... selling the course that guarantees the exam is exactly the conflict the standard polices."* Wrenmoor doesn't need accreditation, but the moment a customer, partner, or rejected candidate asks "who decided 42/60 was passing, and do they profit if I buy the $1,200 course first?" there's no good answer under the current design. **Mitigation that costs no new budget line:** move cut-score ownership to a panel of engineers who don't touch course revenue (field/solutions engineering, support, product) — the education team authors items and delivers the course, it does not decide the threshold. This is a staffing/process change, not a spend.
2. **Unfunded item security, on the highest-fraud-risk format.** 60 recall-style multiple-choice questions is the cheapest exam format to build and, per this framework's own vendor evidence, *"the first to be devalued by leaked content."* "We'll deal with it if it happens" is the certification-theater failure mode this skill names by default. Proctoring (already decided) buys identity verification and session monitoring for free as part of the vendor's base per-seat fee — that's not nothing. What's genuinely missing and does need money eventually is a rotating item bank and exposure analysis. I've written that gap into the kill rule below as an observable trigger instead of a line item, so it doesn't block launch but doesn't get forgotten either.
3. **Revoking the 2024 badges is the wrong fix for the stated problem.** The goal — "nobody confuses the badge with the certification" — doesn't require revocation, and revoking retroactively is a named failure mode here: *"Honor every credential already issued to its published validity window — revoking retroactively destroys trust in every future credential."* Pulling live pages and invalidating ~300 people's credentials the same week you ask the market to trust a new, more expensive credential from the same company is a self-inflicted wound. See the retirement plan under Operating model for the alternative that achieves the actual goal.

Everything below is designed to work even if you don't act on any of these — they're flagged, not blocking.

## Gate verdict

Not independently evidenced here — the brief states the tier decision as made, not the underlying problem it solves (support load, stalled enterprise deals, partner delivery quality, hiring-market signal). I haven't rejected a cheaper rung because no evidence was given to weigh against one; I've designed the operating model for the rung you chose. **Flag, not a blocker:** if this program is ever challenged internally on ROI, you will be asked what evidence justified certification over a badge, and "we decided to" is not a defensible answer to that question later. Recommend capturing the real answer (which of: deals blocked on trained staff / partner implementation quality / hiring-market demand / support load) before the first cohort, even retroactively — it's the difference between defending the program in a budget review and re-litigating it.

## Audience and motion

**Assumed, not confirmed:** primary audience is platform/infrastructure engineers at enterprise customers and integration partners, secondary is individual bottom-up practitioners building a resume credential. Basis for the assumption: a $1,200 prep course plus proctored delivery is priced and gated for someone whose employer pays or who is chasing a job-market signal, not for the free/public/low-friction motion this framework recommends for students and hobbyists — at that price a login wall doesn't suppress a funnel you weren't running anyway.

**Confirm before build:** if any real share of the target audience is self-funded individual developers, the $1,200 course price (nearly 3x CKA's full $445 exam fee, itself the field's most expensive comparator on file) will suppress that funnel almost entirely. That may be intended — flag only so it's a choice, not a surprise.

## Chosen tier

**Rung 5 — proctored certification**, as given. Rejected rungs are not mine to reject since the tier arrived as a decision, but for the record against this framework's own ordering: rungs 1–3 were skipped without the "tried it, hit its ceiling" evidence this framework asks for, and rung 4 (skill badge) is the one the refusal checklist would currently point to, given the unfunded item-security and cut-score-impartiality gaps above.

**Escalation already spent:** there's no rung above this one — the next decision this program will face is retirement, not expansion. Write that expectation into planning now so "let's add a Master-level tier" isn't proposed in year two without new evidence.

## Competency map

No job task analysis was supplied — the domains below are a placeholder built from typical API-gateway practitioner tasks (routing/topology, authn/authz, traffic control, observability, security policy, deployment), **not** sourced from interviews, support tickets, or telemetry. Per this framework's own rule, a syllabus built this way "certifies familiarity with a menu, not ability to do the job," and a candidate can hold you to published domain weights you didn't actually derive from the job. Treat this table as a draft to replace, not a domain split to ship:

| Domain (draft, unvalidated) | Weight (draft) | Evidence type |
|---|---|---|
| Traffic management & policy (rate limits, retries, circuit breaking) | 25% | MC scenario items |
| Authentication & authorization (API keys, OAuth2/JWT, mTLS) | 20% | MC scenario items |
| Troubleshooting & observability (logs, metrics, tracing, failed-request diagnosis) | 25% | MC scenario items |
| Gateway architecture & topology (routing, upstreams, load balancing) | 15% | MC scenario items |
| Security policy enforcement (WAF rules, allow/deny, transformation) | 10% | MC scenario items |
| Deployment & lifecycle (config-as-code, versioning, rollout strategy) | 5% | MC scenario items |

Every domain here traces to an assumed task, not a sourced one — the pass threshold this framework sets (every module traces to a job task, restart if over 20% fail that trace) can't be checked until the real analysis exists. **This blocks item-writing in the 90-day plan below until it's done**, not because process demands it, but because a candidate who fails on a domain nobody validated against real work has a legitimate complaint.

## Credential decision

Certification, per the brief. Named external consumer: not stated — infer one of "enterprise buyer counts certified heads in a contract" or "job-market signal for individual engineers" before writing procurement-facing marketing copy, since the two audiences want different proof (formality and expiry for the first, portability and shareability for the second).

- **Validity and renewal — self-set baseline, none given in the brief:** proposing 2-year validity with a paid retake at a reduced fee, matching CKA and HashiCorp's model rather than AWS's discount-voucher or Microsoft's free-annual model, on the reasoning that a paid retake protects the exam-fee revenue line this program will need to fund its own recurring costs. This is a choice to defend, not an inherited standard — Microsoft's free/annual model exists specifically to maximize installed base over per-credential revenue, and that trade-off is yours to make deliberately.
- **Exam fee — self-set baseline, not specified in the brief:** proposing $299, distinct from the $1,200 prep course price, positioned near HashiCorp's Professional tier ($295) rather than its $70.50 Associate tier, since 60 scenario-style items at 90 minutes reads closer to that tier's difficulty than a pure recall quiz.
- **Format:** 60 multiple choice, 90 minutes, as given — a recall-item format, cheap to build, the more fraud-exposed choice per the risk flag above. Not a performance-based exam like CKA; that's a legitimate cost trade-off given the stated budget, just one worth naming as a trade-off rather than a default.
- **Cut score:** the brief hands this to the education team unconditionally. Recommend a lightweight modified-Angoff pass — 6–8 subject-matter experts from field engineering, support, and product (not education/course sales), one day, per exam version — both because a pass mark "picked by feel" is this framework's named certification-theater failure mode, and because moving the decision off the team that sells the $1,200 course is the direct fix for risk #1 above.
- **Portability:** issue on Open Badges 3.0 (1EdTech) rather than a platform-locked PDF or dashboard badge, so holders can post the credential to LinkedIn or a portfolio without depending on Wrenmoor's own site staying up — this is close to free to add if the certification platform vendor already supports it, and it's the difference between a credential someone actually uses and one they forget.

## Operating model

- **Owner:** one named person, accountable for exam and curriculum truth — not the education team as a group. *(Name TBD; placeholder until assigned.)* Estimated 10h/week steady state.
- **Staffing (hours/week, self-set estimates — confirm against real capacity):**
  - Item authoring: 2 SMEs × 6h/week during build, dropping to 2h/week/each at steady state for refresh.
  - Cut-score panel: 6–8 SMEs, 1 day, once per exam version (not weekly — budget it as a periodic event).
  - Proctoring/exam-ops coordination: 3h/week.
  - Candidate support and appeals intake: 2h/week.
  - Prep-course authoring/maintenance: assumed already staffed under the existing $1,200-course line — confirm it isn't double-counted against this program's budget.
- **Platform class:** proctored delivery vendor (already decided) plus a certification/badge-issuance platform supporting Open Badges 3.0. Keep every item, rubric, and courseware source in a repository Wrenmoor owns — not solely inside the proctoring or authoring vendor's tool. The reference case here is Katacoda's public site shutting down 15 June 2022 after the O'Reilly acquisition, taking every embedded scenario with it for vendors who hadn't kept their own copy.
- **Refresh trigger — self-set baseline, Wrenmoor's release cadence not given:** re-align the item bank within 8 weeks of any release that changes routing, auth, or policy behavior candidates are tested on; full item-bank review annually regardless. Adjust the 8-week figure once the real release cadence is confirmed — it's borrowed as a rough comparator from CKA's published 4–8 week Kubernetes re-alignment commitment, not a number Wrenmoor is bound to.
- **Pricing:** $1,200 prep course (given) plus a proposed $299 exam fee (self-set, see above), paid by candidate or employer.
- **Localization:** defer — no locale has demonstrated demand yet, and each language multiplies the refresh bill this program hasn't sized.
- **Partner delivery:** not addressed in the brief. If partners implement Wrenmoor gateways for customers, a train-the-trainer path tied to partner tier is the standard next move for this audience — flagging as a likely year-two addition, not building it now.

### Legacy badge program retirement (2024 cohort, ~300 holders)

Recommend against the stated plan of pulling badge pages and revoking badges. It solves a labeling problem with a trust-destroying tool. Alternative that achieves "nobody confuses the two" without the downside:

1. Stop new badge issuance now (already implied by "shut down").
2. Keep existing badge verification pages live at their current URLs, each with a clearly dated banner: *"This program closed in <launch month> 2026 and has been succeeded by the Wrenmoor Certified Gateway Engineer certification. Badges issued under this program remain valid as originally awarded."*
3. Do not revoke. The ~300 holders earned something real; invalidating it the same week you ask the market to trust a harder, more expensive credential from the same company undercuts the new program before it starts.
4. Cross-link from the new certification's marketing page to the retired badge's banner page, so the distinction is explained rather than erased.

This is a recommendation, not a rewrite of your plan — if there's a reason (legal, trademark, a badge that was never meant to be permanent) that forces revocation, that reason belongs in this section as the documented cause, per this framework's retirement guidance, so the same question doesn't get re-litigated in eighteen months with no record of why.

## Budget shape

All figures below are this charter's own baseline, not sourced from a vendor or from Wrenmoor's actuals — replace with real numbers once known.

- **Year one build:** ~350 person-hours (item authoring for a bank of ~240 items across 4 rotating forms, one cut-score study, certification-platform integration, badge-retirement communication) plus proctoring vendor setup and per-seat contract, plus certification/Open-Badges platform subscription.
- **Year two recurring:** ~15h/week steady state (item-bank refresh tied to the release trigger above, annual cut-score re-validation, proctoring per-seat cost scaling with candidate volume, appeals handling). This is the number that actually decides whether the program survives — if year two can't be staffed at this level, that's the signal to not start year one, not a problem to solve after launch.
- **Not budgeted, flagged as a gap, not a blocker:** item-bank rotation depth beyond the initial 4 forms, exposure analysis, and any response to a confirmed leak. See kill rule.

## Measurement plan

| Level | Metric (one primary) | Cohort-1 target (self-set baseline) |
|---|---|---|
| Reaction | Candidate exam-experience complaint rate | <5% of sittings — a baseline to reset after cohort 1, not a validated norm |
| Learning | Pass rate and per-domain score distribution | No target set pre-launch — a pass rate near 100% means the exam isn't assessing anything; a rate collapsing near zero usually means a broken exam environment, not incompetent candidates. Check environment before curriculum. |
| Behavior | Product usage depth (feature adoption) among certified holders, 90 days post-cert, vs. matched non-certified accounts | Directional only in cohort 1 — no target until a matched-comparison baseline exists |
| Results | Enterprise deals or renewals citing "trained/certified staff" as a factor, per quarter | Baseline first, target set from cohort-1 data |

**Identity join** (required before launch, per this framework — it cannot be reconstructed after the fact): candidate email → product account → usage telemetry, plus a tag on CRM opportunities/renewals for "certified staff" as a stated factor. Confirm this join is legally and technically possible before the first cohort sits the exam.

**Not measured this year, stated in advance:** revenue directly attributed to certification — no clean counterfactual exists with a first cohort this small, and claiming one would be exactly the kind of correlation-as-causation this framework warns against.

## Kill rule

Two, since this design carries two distinct failure modes:

1. **Volume:** if candidate sittings in the first 12 months fall below the number needed to fund one item-bank refresh and one cut-score re-validation cycle (roughly 150 sittings at the proposed $299 fee against the year-two recurring cost above — self-set threshold, recalculate once real vendor pricing is in hand), review at the 12-month mark: stop authoring new items, honor all certifications already issued to their stated validity window, and reopen the gate with real evidence before proposing this rung again.
2. **Integrity:** if item-bank exposure or a confirmed leak occurs and no budget appears for rotation/response within one full exam cycle, publicly downgrade the credential to a skill badge rather than keep selling a compromised exam as a certification — this is the direct consequence of shipping risk #2 above uncorrected, written down now so it's a pre-agreed response and not a crisis decision.

## First 90 days

1. **Weeks 1–4:** Real job task analysis (interviews, support-ticket review, telemetry) to replace the placeholder competency map above — item writing does not start until this exists.
2. **Weeks 3–5 (parallel):** Recruit the independent cut-score panel (field engineering, support, product — explicitly not the education/course-sales team); select and contract the certification/Open-Badges issuance platform.
3. **Weeks 5–9:** Author the item bank (4 rotating forms) against the validated competency map; technical review by SMEs outside the authoring team.
4. **Week 9:** Cut-score study (modified Angoff, one day, the independent panel).
5. **Weeks 9–10:** Publish the legacy-badge retirement banners (see Operating model) at least two weeks before certification launch — announce the change before the last old-badge holder finds out from a revoked link.
6. **Week 11:** Pilot cohort (internal or design-partner customers), first-cohort baseline metrics captured.
7. **Week 13 — first learner-visible artefact:** public launch of the Wrenmoor Certified Gateway Engineer exam and prep course; legacy badge pages live with retirement banners, not revoked.

## Where each number comes from

| Number | Status |
|---|---|
| $1,200 prep course price, 60 MC items, 90 minutes, proctored, "decision is made" | Given by the user — not sourced or self-set, an input constraint |
| ~300 legacy badge holders, 2024 program | Given by the user |
| $299 exam fee | This charter's own baseline, positioned against HashiCorp Professional's $295 (see below) |
| 2-year validity, paid retake renewal model | This charter's own baseline, chosen over three published alternatives (see below) |
| CKA: $445, 2 hours, performance-based, 2-year validity, re-aligned within 4–8 weeks of a Kubernetes minor | Sourced from this skill's certification-program-design reference — re-verify against Linux Foundation's current CKA page before quoting to a buyer |
| HashiCorp Associate: $70.50, 1 hour, MC, 2-year validity | Sourced from the same reference — re-verify against HashiCorp's current per-product certification page |
| HashiCorp Professional: $295, 4 hours (lab + MC), 2-year validity | Same source, same re-verification caveat |
| AWS: 3-year validity, 50% discount voucher retake, free activity-path renewal at entry tier | Same source, same caveat |
| Microsoft role-based: 1-year validity, free unproctored open-book renewal within a 6-month window | Same source, same caveat |
| Modified Angoff panel size (5–15 SMEs) | Sourced from the same reference (standard-setting methodology, not vendor-specific) |
| Open Badges 3.0 / 1EdTech format | Sourced from the same reference |
| Katacoda shutdown, 15 June 2022 | Sourced from the same reference, cited as the platform-dependency cautionary example |
| Competency domains and weights | This charter's own unvalidated placeholder — explicitly flagged as not sourced from a real job task analysis, to be replaced in weeks 1–4 |
| Staffing hours, item-bank size (240 items/4 forms), build/recurring hour estimates, kill-rule volume threshold (150 sittings), all measurement targets | This charter's own baseline throughout — none of these are industry figures, all need replacement with Wrenmoor's real numbers as they become available |