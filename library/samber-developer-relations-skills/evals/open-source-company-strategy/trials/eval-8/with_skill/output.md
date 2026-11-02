# Decision-rights model — Ostrava Mobility open source approvals

## The proposal solves the right problem with the wrong mechanism

"One consistent answer" is the right goal. "OSPO signs off on everything" is not how you get there — it's why every request is currently a three-week negotiation, and making the OSPO the sole approver will make that worse, not better.

Two different questions are being asked every time a business unit wants to publish something:

1. **Should we open this?** — a business-context call: does it help or hurt the BU's competitive position, does it touch a customer contract, does it give away the thing the BU sells.
2. **Is this compliant to open?** — a specialist call: license, patent, trade secret, export control, security.

Your OSPO — two people plus a part-time attorney — is built to answer question 2 for six business units. It cannot also answer question 1 for six business units, because it doesn't have and can't acquire the business context that answer requires (roadmap, contract terms, competitive read) fast enough to be useful. Route both questions through OSPO and every request turns into OSPO interviewing the BU from scratch to reconstruct context the BU already has — which is the negotiation you're describing. Google separates these explicitly: the "okay to release" call sits with the launch creator's manager, stated on the record as "the open source office frequently lacks the business context to make it"; OSPO-equivalent review runs in parallel, not as a gate the business call has to clear first.

**Recommendation: split the two calls, and get your consistency from one published rubric applied by all six BUs, not from one small team reviewing all six BUs' judgment calls.**

## Assumption to confirm

Treating Ostrava as a hybrid: public/listed (highest reversal exposure — a walked-back decision is shareholder-visible, not just community-visible) crossed with a multi-BU conglomerate (the live axis per request is usually *enabler vs. differentiator inside that BU's product*, not *deployment mode vs. a hyperscaler*, unless a specific BU's core platform is the hyperscaler-commoditization risk). If one BU's ask is actually "defend our SaaS core against a competing managed service," flag that request — it escalates straight to Tier 3 below, it doesn't follow the standard path.

## Roles

| Role | Owns | Does not own |
|---|---|---|
| **BU business decider** (the requesting BU's engineering director or product owner — named per BU, not "the BU") | The should-we call: competitive exposure, customer-contract conflicts, differentiation. Approves or blocks on business grounds. Writes the one-paragraph business case. | Compliance sign-off. Cannot self-clear license/patent/trade-secret/export/security. |
| **OSPO** | The compliance call: license selection against the allowlist, trademark, security-contact assignment, release-checklist completion. Maintains the published tiering rubric so every BU applies the same test. Publishes precedent so BU 4 doesn't relitigate what BU 1 already settled. | The business call. Does not evaluate whether a BU *should* want to open something — only whether it's clean to. |
| **Attorney (part-time)** | Patent and export-control review, folded into OSPO's compliance track, not a separate queue. | Business call. |
| **Named executive sponsor** (pick one — CTO is the standard placement; confirm) | Final decider on Tier 3 only: anything precedent-setting, anything a BU and OSPO disagree on, anything touching a customer contract or the product core. | Routine approvals — if this person is deciding Tier 1/2 requests, the model has already failed. |

Consistency comes from the rubric this table implies plus the tiering below being the same document for all six BUs — not from a single throat to choke.

## Triage: three tiers, not one queue

Most of what's generating three-week fights is almost certainly Tier 1 material moving at Tier 3 speed. Fix that first.

| Tier | What lands here | Business call | Compliance call | Target turnaround |
|---|---|---|---|---|
| **1 — Fast track** | Enablers, internal tooling, non-differentiating infrastructure, client SDKs with no embedded business logic, standard OSI license (MIT/Apache-2.0), no customer data | BU director self-certifies against a published checklist (default: approve) | OSPO async scan against the license allowlist; default-approve unless flagged | 3 business days |
| **2 — Standard** | Reference implementations, protocol/format specs, anything adjacent to but not inside the differentiating layer of a BU's product | BU director writes the business case, approves or blocks | OSPO + attorney review in parallel with the business call, not after it | 10 business days, run concurrently — not 10 + 10 |
| **3 — Escalation** | Product core, anything touching a customer contract, anything a BU and OSPO disagree on, anything one BU's decision would set precedent for the other five | Executive sponsor decides, informed by BU case + OSPO/legal review | Same review, presented to the sponsor, not gating | Next scheduled review (biweekly recommend), or ad hoc for a live deal/renewal deadline |

Tier 1 and 2 run business and compliance review **in parallel**, matching the skill's own inbound-policy pattern (automatic for allowlisted cases, reviewed for the rest) applied outbound. Sequential review is most of where your three weeks are currently going.

## Default posture

Approve unless a named person states a specific, written reason not to. Silence is not a block. An unanswered request past its tier's SLA auto-escalates one tier up rather than sitting in limbo — that alone should kill most of the current negotiation pattern, since "nobody said no, nobody said yes" stops being a valid end state.

## Disagreement path

BU business decider and OSPO disagree (BU wants to ship, OSPO flags a compliance issue; or OSPO clears it but a different BU objects on competitive grounds) → escalates to Tier 3, executive sponsor decides. No standing negotiation between OSPO and a BU — that's the exact three-week pattern this model exists to remove.

## Commitments to publish

State these publicly (internally is fine to start; GitLab publishes theirs externally once the org is confident in them):

1. A Tier 1/2 approval will not be reopened or walked back without executive-sponsor sign-off, announced before it takes effect. Docker's 2017 rename drew severe backlash with no license change and no code withdrawn at all — governance surprise is priced independently of what actually moved. As a listed company, that price includes analysts and press, not just forks.
2. The rubric and tiering criteria are the same document for all six BUs — no BU gets a stricter or looser bar than another.
3. OSPO's SLA per tier is a commitment, not a target: a breach is escalated automatically, not absorbed as "OSPO is slow again."

## Operating model — the resourcing gap in the original proposal

Two people plus a part-time attorney is a reasonable size for the compliance-reviewer function (Tier 1 async scans, Tier 2 parallel review, Tier 3 support) across six BUs. It is not a reasonable size to also be the business decider for 600 engineers — that's the mismatch that produced the three-week negotiations, and it doesn't go away by giving OSPO more formal authority; it goes away by giving the business call to people who already have the context, which costs no new headcount, since it's the BU directors' existing job.

If you want a second FTE, spend it on OSPO's actual bottleneck — compliance throughput and rubric maintenance — not on hiring OSPO staff to learn six BUs' business context from scratch.

## Re-evaluation trigger

Review at the next planning cycle, plus immediately if: a Tier 1/2 SLA is missed twice in a quarter (rubric or staffing problem), a BU escalates a disagreement more than once in a quarter (rubric gap, name the gap), or a competitor ships a managed/open equivalent of something Ostrava has kept closed (reopens the business call, doesn't retroactively change compliance verdicts already issued).

---

This covers decision rights only, per your ask. It doesn't yet inventory which specific assets each BU is trying to publish — running Steps 1–6 per pending request (starting with whatever's currently stuck) would tell you which tier each one actually belongs in and validate the SLA targets against real cases before you present this to the exec team.