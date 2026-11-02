# Bottom line for the board

The 340→9 number isn't a conversion rate — it's two different processes, on two different clocks, stapled together. Signups measure developer behavior this quarter; closed deals measure a ~3-month security-review-and-procurement process that mostly started last quarter. Comparing them same-quarter makes a healthy or unhealthy funnel look identical to a catastrophic one, because the denominator and the numerator were never the same cohort. Below is the actual map — two lanes, not one number — plus the one gap worth closing before the next board meeting.

---

# Developer journey map — backend engineers, 500-5000 person companies, 2026-09-19

## Scope

- **Segment:** backend engineers at 500-5000 person companies (one segment, no sub-segmentation requested).
- **End state:** paid conversion.
- **Buyer:** the developer is not the signer. Deals move through security review then procurement, ~3 months average — this forces a mandatory buyer lane (Step 4 of the skill), not a single funnel.
- **Stage model chosen:** the **API and platform five-stage arc** (Awareness → Onboarding → Integration → Production → Advocacy) for the developer lane, paired with a two-stage buyer lane (Technical approval → Commercial approval).
- **Why this model, and what got deleted:**
  - *Orbit levels* (explorer→advocate) — deleted. No purchase vocabulary; wrong fit for a paid B2B sale.
  - *OSS contributor funnel* — deleted. End state isn't outside contribution.
  - *AAARRRP* (terminal: revenue) — considered, set aside. Its single "Revenue" stage would fold the developer's own product adoption and the buying committee's 3-month security+procurement process into one un-splittable stage — which is exactly the flaw producing today's misleading 340→9 view, not a fix for it.
  - *Revell six-stage* (terminal: standardization) — considered, set aside for now. Real candidate for a **later** map once a first deal has closed and the question shifts to "does the org default to this tool" — that needs account rollup and buyer-side interviews this company doesn't have yet. Revisit at the 90-day re-read if that becomes the live question.
  - *API five-stage arc* — chosen. It's an API product, its boundaries (first call, integration, production) are the kind of thing product telemetry usually already logs, and it lets the buyer lane carry the actual "paid" event instead of a developer-lane stage pretending to represent it.
- **Caveat on every Owner cell below:** guessed from typical org shape for a company this size selling this kind of product. Nobody was interviewed for this map — confirm real owners before treating any row as assigned. That interview is the fastest way to make this map load-bearing.
- **Account rollup, unresolved:** it isn't stated whether the 340 signups are 340 distinct companies or fewer companies with multiple engineers each signing up (common when a backend team evaluates together). Until signups are rolled up by email domain/workspace, the buyer lane's true denominator is unknown — this is probably the single fastest fix available.

## Journey

| Stage | Developer's job | Entry trigger | Exit event | Touchpoints | Owner | Friction evidence | Signal |
|---|---|---|---|---|---|---|---|
| Awareness | "find something to stop hand-rolling RBAC/ABAC checks in every service" | search, peer mention, comparison content | creates a free-tier account | marketing site, docs landing, comparison pages, search, community mentions | marketing/growth (confirm) | no evidence yet | 340 free-tier signups last quarter (raw count — no top-of-funnel traffic captured yet, so no rate; treat as **inferred**) |
| Onboarding | "prove this actually enforces the access rule I need, from my laptop, before I show my team" | signup completed, opens quickstart | first API call that evaluates a **real, self-modeled** policy (not the seeded demo) and returns an allow/deny | quickstart, policy-modeling UI/DSL, SDK install, API keys, dashboard | developer experience / docs (confirm) | no evidence yet — no friction log run | not instrumented |
| Integration | "wire this into one real service my team can review, without breaking existing requests" | first success reached | authorization check called from code in a shared/staging environment, not localhost | SDK reference, policy-as-code docs, error handling docs, support | product/engineering (confirm) | no evidence yet | not instrumented |
| Production | "put this in front of real user traffic and trust it not to lock out or leak access" | staging traffic observed | sustained authorization-check volume against a live, customer-facing service for 14 consecutive days | runbooks, status page, plan/rate-limit docs, support, dashboards | product (confirm) | no evidence yet | not instrumented |
| Advocacy | "tell other teams this solved a problem worth solving" | months of stable production use | public talk, post, or unprompted recommendation naming the product | community, conference CFPs, changelog | DevRel/community | none gathered | not instrumented; likely below the 30-event floor once tracked |

Only Awareness carries a real number, and even that is a period count with no denominator, not a rate. Everything between "signed up" and "signed a contract" is currently invisible — that gap, not any one measured stage, is what makes the top-line ratio unreadable.

## Buyer lane

Present. Developer is explicitly not the signer; deal requires security review then procurement.

| Buyer stage | Entry trigger (boundary contact) | Exit event | Owner | Signal |
|---|---|---|---|---|
| Technical approval | prospect's engineering/security team asks a compliance question, hits a plan/rate limit, opens an SSO or audit-log doc, or requests a security questionnaire | security questionnaire/review cleared | security or solutions engineering (confirm — may currently be founder/eng-lead led) | not instrumented as a rate; instrument boundary contact first — it's the cheapest, earliest, cleanest buy-signal available |
| Commercial approval | technical approval cleared, procurement engaged | contract signed | sales (confirm — may be founder-led) | **9 closed deals last quarter — below the 30-event floor, publish as a dated raw list, not a percentage.** Track median days from first boundary contact to signature (user states ~3 months) as the real quarter-over-quarter signal, not deal count. |

The developer lane counts people; this lane counts accounts. Roll signups to a company/workspace before reading it — see the rollup gap in Scope.

## Moments

- **First success:** first authorization check that evaluates a policy the developer actually modeled themselves. Time-to-first-success is unknown today — this is the single most valuable event to start logging.
- **Moment of truth:** boundary contact — engineering decides to put their own security team in the room, typically triggered by a free-tier limit, a need for SSO/audit logging, or a plan to move past one pilot service. This is where the two lanes actually connect.
- **Abandonment point:** unknown. No exit interviews have been run, and with a ~3-month median buyer cycle, many of this quarter's still-open deals aren't lost — they're mid-process. Don't label anything "abandoned" without first defining a stalled threshold (e.g., 45-60 days with no buyer-side movement); without that threshold, "9 closed" silently double-counts as "331 lost," which isn't true.

## Leak

**Onboarding — first successful policy-check call.** Nominated as a working hypothesis, not a measured finding: no interior stage carries real data yet, so this can't be argued from a computed rate. Three reasons it's the stage to work on first anyway:

- Earliest stage in the developer lane with a plausible owner able to act on it (developer experience/docs).
- Product-shape argument, not a borrowed benchmark: an authorization API requires the developer to model their own resource/policy graph before the product does anything useful — a materially higher ability bar than a typical CRUD-API quickstart. That's a claim about this product category, not a cross-company conversion figure, so it survives this skill's ban on quoting other companies' rates.
- By Fogg's B=MAP, this reads as an **ability** problem rather than a motivation one — backend engineers evaluating an authz API already have the motivating pain (they're actively trying to stop hand-rolling this); what's likely missing is a short enough path to a working policy model, not a better pitch. This is a hypothesis pending a friction log, stated as such — don't act on it as fact.

It beat the alternative "leak" candidate — the 340-vs-9 cohort mismatch — only because that mismatch is a reporting-methodology defect, not a journey stage with an owner who can fix a conversion rate. Fix the reporting in Scope's framing; fix Onboarding as the actual journey work.

## Handoff

- **Owner:** developer experience lead (confirm real name/team).
- **Signal to watch:** share of free-tier signups reaching a first successful, self-modeled policy-check call within 7 days of signup. Not instrumented today — standing up this single event is the first action, before any UX fix.
- **Re-read date:** 2026-12-18 (90 days out), and immediately after any quickstart or policy-modeling UI rewrite, pricing change, or new SDK release.

## Gaps

- Onboarding, Integration, Production, Advocacy: no signal instrumented at all. This map is well under the skill's 60%-coverage bar (2 of 7 rows carry a real value, and one of those two is below the small-N floor) — shipping anyway, per the skill's own rule that an honest map with holes beats a complete one with invented numbers.
- Awareness: signups are inferred as a rate — no traffic/referrer denominator exists yet; expect a large "direct/unknown" source bucket once one is built, that's normal, not a tracking bug.
- Buyer lane: 9 closed deals is below the 30-event floor — keep as a dated list. No visibility yet into deals that *entered* security review but didn't close, so no real "clear rate" can be computed until every review-opened event is logged, not just closes.
- Account rollup for the buyer lane is missing entirely — resolve whether 340 signups map to 340 companies or fewer before trusting any account-level read.
- No friction log, no exit interviews, and no owners confirmed with the actual team — this map's Owner column and Onboarding leak hypothesis are both best-guesses pending a real interview pass.
- Cohort mismatch: next quarter, report "of the signups from N quarters ago, how many have since closed" instead of same-quarter totals — that's the number that actually answers the board's question.