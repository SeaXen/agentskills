# Trellisway integration-engineer credential — education charter

Straight answer first: **don't ship 60 MCQ + 70% cutoff as-is.** That's the exact shape this skill calls "certification theater" — arbitrary pass mark, recall-item format, no standard-setting, nothing behind it if Northbridge's lawyer ever asks "how was 70% decided." Fixable in your same timeline and budget. Below is the buildable version.

## 1. Gate verdict

Education is justified. Evidence: procurement explicitly blocks signature on integration-engineer certification — this is "deal blocked on trained staff," the textbook trigger, not inferred. Rejected cheaper alternative: better docs/onboarding alone — doesn't satisfy a contractual "certified" requirement, so skipping straight to a credential is correct here, not scope creep.

## 2. Audience and motion

- **Primary:** Northbridge Freight's integration engineers. Enterprise motion — credential is procurement currency, not portfolio signal.
- **Not in scope (yet):** bottom-up/public devs, students. Don't design for them — different rigor, different funnel logic.
- **Consumer of the outcome:** Northbridge procurement (contract gate) + your own CRO (deal closure).

## 3. Chosen tier — skill badge (rung 4), not proctored certification (rung 5)

Promote to full certification only when all three hold:
1. Named buyer counts certified heads → **yes**, Northbridge.
2. Second-year recertification funded, not hoped for → **no**, $80k is this-FY only.
3. One person owns item bank indefinitely → **no**, 10h/week + 5h/week, no standing role committed.

2 of 3 missing → build a **skill badge**, market it to procurement as "Trellisway Certified Integration Engineer." Confirm with Northbridge's procurement team, this week, whether their contract language requires proctored/third-party-verifiable rigor or accepts a vendor-issued credential — that answer changes the build, get it before week 2.

Rejected:
- **Curated path only** — no credential, doesn't satisfy "certified" wording in the deal.
- **Full proctored certification** — needs job task analysis, standard-setting panel (5-15 SMEs per exam version), item security, appeals, funded recertification forever. Your team has 15h/week combined and one year of budget. Unbuildable, and once holders exist you can't quietly retire it.

**Escalation trigger to rung 5** (write this down, revisit later): a second enterprise contract in the same fiscal year also requires certified-heads counted, AND a recurring budget line beyond this FY gets approved, AND someone owns the item bank as a standing role.

## 4. Competency map

Draft only — validate against real Northbridge integration engineers and your SE's deployment history in week 1-2, not against Trellisway's feature list:

| Competency (hypothesis) | Evidence | Badge-worthy? |
|---|---|---|
| Workflow design w/ conditional logic + error handling (retries, idempotency) | Graded practical: build a workflow in sandbox tenant | Yes — top consequence |
| Debugging a failed run via logs/run history | Graded practical: given a broken workflow, fix it | Yes — top frequency (support load) |
| Auth/connection setup (API keys, environments) | Formative check only | No — too low-consequence to gate on |
| Webhooks/event triggers | Formative check only | No |
| Testing → production promotion | Formative check only | No |

Rule: badge gates on the **2 highest-frequency/highest-consequence tasks only**. Everything else is a knowledge check, ungraded, feeding the badge attempt — not the other way round. This is also why 60 MCQ is oversized: you don't have grading bandwidth (15h/week) to run a 60-item bank with rigor, and a big recall bank is exactly what leaks first.

Pass threshold for the trace: every module must map to one of these tasks. If more than ~20% don't, you're back to writing from the feature list — restart from interviews (this 20% is this skill's own baseline, not a standard, move it if you have reason).

## 5. Credential decision

- Tier: **skill badge**, scoped to the 2 competencies above.
- Grading: **binary rubric per task**, not a percentage score. Example for the workflow-design task: "trigger fires correctly" / "error handled with retry+backoff" / "no hardcoded credentials." Pass = all critical criteria met. This replaces "70%" with something you can defend line by line — no standard-setting panel needed at badge tier, a checklist is enough.
- Format: **Open Badges** (1EdTech, free open spec) via a badge-issuing tool (Credly/Accredible/Badgr — get an actual quote before committing budget, I haven't verified current pricing).
- Named external consumer: Northbridge procurement now; future enterprise deals if the trigger above fires.
- Expiry: none in year one — flag to procurement as "revisit if Trellisway ships a breaking workflow-engine change." Confirm they don't need a stated renewal window in the contract itself.

## 6. Operating model

- **Owner:** you (DevRel lead), 10h/week, accountable for curriculum truth and grading rubric.
- **Technical review + practical grading:** solutions engineer, 5h/week.
- **Lab environment:** reuse Trellisway's existing sandbox/trial tenant. Don't build new lab infra — no budget or hours for it.
- **Learner support:** SE, ad hoc within the 5h.
- **Platform:** existing docs site for the curated prep content (rung 1, reused tutorials) + badge-issuing tool for credentialing. No new LMS.
- **Refresh trigger:** re-align practical scenario within 4 weeks of any Trellisway release that changes workflow-engine behavior — bound to your release cadence, not a calendar review.
- **Pricing:** free to Northbridge; this is deal-unblocking spend, not a revenue line.
- **Localization:** none — single account, English only, revisit only if demand appears.
- **Partner delivery:** none yet — no partner motion in scope.

## 7. Budget shape

- **Year one (this FY, ≤$80k ceiling):** badge platform subscription (~low thousands/year, get real quote), ~180 person-hours internal (15h/week × ~12 weeks to launch), sandbox infra $0 incremental. Most of $80k stays unspent — that's a ceiling, not a target. Reserve remainder for a second cohort or a contractor if hours run short.
- **Year two (recurring, unfunded today):** estimate 3-5h/week combined for issuance, occasional re-grading, and post-release refresh. **This is your real open risk** — nothing's committed beyond this FY. Get at least an informal nod from the CRO for that recurring number before launch, or plan explicitly to retire the program per the kill rule below rather than let it drift unowned.

## 8. Measurement plan

- **Reaction:** formative knowledge-check completion rate before the practical attempt. No target needed — diagnostic only.
- **Learning:** practical pass rate, target 80% within 2 attempts for cohort one (your own baseline — no vendor publishes pass rates to compare against).
- **Behavior:** badge holders' Trellisway usage (workflows created, error rate) 30/90 days post-badge. Identity join: Northbridge engineer email → Trellisway account → usage telemetry. **Agree this with Northbridge before launch** — can't be reconstructed after the fact, and it may need their sign-off to track named engineers.
- **Results:** primary target is binary — Northbridge contract signs. Secondary, longer-term: this badge gets cited in a second enterprise deal (= your rung-5 escalation trigger firing).
- **Not measured this year:** revenue attribution beyond the Northbridge deal itself — no clean counterfactual with one account.

## 9. Kill rule

If no external consumer (a second deal, a renewal argument) cites the badge within **two quarters of launch**, stop issuing new badges, honor existing ones, fold remaining content into docs. If the named owner (you) stops running this and nobody replaces the role within one release cycle, freeze rather than let it silently go stale.

## 10. First 90 days (fits before a Q1 launch, starting now)

1. **Weeks 1-2:** confirm with Northbridge procurement what "certified" must legally mean for the contract. Run 3-5 short interviews with their integration engineers + pull your SE's support/deployment notes for the real job task list.
2. **Weeks 3-4:** lock the 2 gating competencies, write the binary grading rubric, draft the formative knowledge check from existing docs (reuse, don't author from scratch).
3. **Weeks 5-7:** build the practical scenario in the existing sandbox tenant, pilot with 1-2 friendly engineers, adjust rubric off real pass/fail spread.
4. **Weeks 8-9:** stand up the badge-issuing tool, get CRO/legal sign-off on the exact credential wording (avoid "ISO-certified" or similar overclaims).
5. **Weeks 10-12:** launch cohort one with Northbridge's actual engineers, capture baseline pass rate, issue badges, report to sales as the unblock evidence.
6. **Week 13:** retro, report cohort-one numbers, raise the year-two staffing ask with the CRO before it's urgent.

## 11. Where each number came from

- ✅ Sourced (from this skill's own certification reference, re-verify before quoting to anyone): Kirkpatrick's four levels + "start from Level 4" guidance (kirkpatrickpartners.com); CKA/HashiCorp/AWS/Microsoft renewal models as four different shipped strategies, not a norm; Open Badges as free/open 1EdTech spec.
- ⚠️ Given by you, not vendor-sourced: $80k budget, 10h+5h weekly staffing, $400k ARR, Q1 deadline.
- ⚠️ My own baseline, needs real numbers to replace: badge platform cost estimate, 80%-in-2-attempts pass target, 20% module-trace threshold, the 2-competency cut, the whole hypothesis competency table in section 4.
- ❌ Rejected as indefensible: the original 70% cutoff (picked by feel, no standard-setting behind it) and 60-question recall bank (cheap, first thing to leak, doesn't test the tasks that actually block the deal).

## Next action

Send Northbridge procurement one question today: **does their contract require proctored/third-party-verifiable certification, or will a vendor-issued skill badge satisfy "certified"?** That single answer decides whether this plan holds or you need to renegotiate scope with your CRO before committing any of the 15 hours/week.