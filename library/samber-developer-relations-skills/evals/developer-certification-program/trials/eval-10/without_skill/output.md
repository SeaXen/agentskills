**Start here (10 min):** Do not use "Certified Engineer" in Quebec or Ontario until counsel clears it. Pick a fallback name now, for example "Sindral Certified Developer". Everything else below stays valid under either name.

Four of your six draft decisions need a change.

| Draft decision | Verdict |
|---|---|
| 8 features × 12.5% | ⚠️ Change |
| 3 variants per feature | ✅ Keep, with equivalence checks |
| 75% of checks passed | ⚠️ Change |
| Skip pilot | ❌ Reverse |
| 120 h, no reviewers | ⚠️ Keep the hours, add substitute reviews |
| Accommodations in candidate record | ❌ Change |
| "Certified Engineer" | ❌ Hold |

## 1. Blueprint

- Equal weights mirror your product's feature list, not the agency developer's job. A rare feature gets the same weight as the daily one.
- Ground the weights in job data. Ask the 11 devs and your support team to rate each feature on frequency and damage-if-wrong (1–5). Use support tickets as a cross-check. Cost: 3 h.
- Equal weights are fine if the data supports them. Then you can say so.
- Add a **critical-safety flag**. Mark checks where a wrong answer breaks production, such as kill switch, targeting leaks, and wrong environment. Every critical check must pass.
- Normalize each task to a fraction first, then weight. Variants must have the same check count per feature. Otherwise a 10-check variant outweighs a 5-check one.
- Target about 8 tasks, 2–2.5 h per candidate. Longer than that raises dropout.

## 2. Three variants per feature

- Three variants support retakes without repeating a task and limit answer sharing. Keep three.
- 24 variants is your biggest cost. If time runs short, cut to **2 variants per feature** before you cut the pilot.
- Variants must test the same skill at the same difficulty. Same check count, same expected time, same trap type.
- Test every variant with a reference solution, which must pass. Also test a deliberately wrong solution, which must fail. This catches grader bugs.
- Add a written AI-assistance policy: allowed or not, and how you enforce it. Run one coding agent against each variant. If it passes with no effort, the task is too easy or too guessable.

## 3. Cut score

- A flat 75% of checks has no basis. It is also compensatory: a candidate can score 0 on one feature and still pass.
- Checks inside one task are correlated. Treat the unit as the task, not the check.
- New rule:
  1. Overall weighted score ≥ provisional cut.
  2. Every critical check passes.
  3. No feature below a floor of 50%.
- Set the provisional cut with contrasting groups from the pilot. Before the pilot, a Sindral solutions engineer who knows the 11 devs labels each as novice, competent, or expert. Place the cut between "borderline competent" and "novice".
- Label the first cohort **beta**. The cut is provisional. Review it after ~30 real attempts.
- Pass results must not claim more than "completed these tasks in the product".

## 4. Pilot: do it

- "11 is too few for statistics" is true and beside the point. A pilot finds broken tasks, ambiguous checks, wrong time limits, and grader bugs. 11 people is plenty for that.
- Assignment: 11 devs × 8 tasks = 88 attempts, about 3–4 per variant. Rotate variants so each gets 3–4 attempts, for example variant index = (dev number + feature number) mod 3.
- Run 3 of them think-aloud.
- Flag, do not test: a variant whose pass rate differs by more than 25 points from its siblings, or whose time exceeds 1.5×.
- "Friendly" devs are biased toward your product. Add 2–3 Sindral support staff who did not write the tasks.
- Cost: 16 h including fixes.

## 5. Time: 120 h, no reviewers

About 7 h/week over 17 weeks (Oct 26 to Feb 19). Budget:

| Phase | Hours | Weeks |
|---|---|---|
| A. Scope, job survey, blueprint, name, privacy design | 14 | 1–3 |
| B. Sandbox, auto-grader, results store | 28 | 3–7 |
| C. 24 variants + reference and wrong solutions | 34 | 6–11 |
| D. Pilot + fixes | 16 | 12–14 |
| E. Cut setting, handbook, retake/appeal/accommodation policy | 10 | 14–15 |
| F. Launch + buffer (15%) | 18 | 16–17 |

Beta opens about Feb 22, 2027. December is slow, so phase C tolerates a pause.

Substitutes for reviewers (author cannot review own work):

1. Wait 48 h, then re-read each variant cold.
2. Automated reference-pass and wrong-fail tests.
3. The coding-agent solve attempt.
4. Pilot devs act as task reviewers.
5. Ask one Sindral engineer for **3 h** to verify answer keys against the product. This is the only external review. It guards against wrong keys, which are the worst failure.

Not in the 120 h: maintenance. Budget roughly 2–3 h per product release that touches a tested feature. Set credential validity to 2 years, or until the covered major version is retired.

## 6. Accommodations

Do not put them in the general candidate record that support reads. This is health-related, sensitive data. Quebec's Law 25 and PIPEDA apply, and Ontario's Human Rights Code requires accommodation.

- Store requests in a separate restricted store. Name an owner.
- Support sees one flag only, such as "extended time ×1.5 approved". No reason, no diagnosis.
- Collect the minimum. Get express consent. Set a retention limit, for example delete 12 months after the last attempt.
- The certificate and badge must never show accommodation use.
- Write the process before launch: how to request, response time (for example 5 business days), who decides, and what is on offer. Offers include extra time, screen-reader-compatible sandbox, and breaks.
- The standard stays the same. Only the conditions change.
- Quebec law may require a privacy impact assessment for a new system holding personal data. Ask counsel, 1 h.
- Check whether Quebec French-language rules require French exam materials and candidate documents. I am not certain, so ask counsel.

## 7. Name

I am not a lawyer. Ask one before publishing the name.

- "Engineer" is a regulated title in Canada. In Quebec, the Ordre des ingénieurs du Québec (OIQ) enforces "ingénieur" actively. Ontario's Professional Engineers Act also restricts engineer titles. Certifying software devs as "Engineers" invites a complaint to Sindral and to the agencies that display it.
- Safer: "Sindral Certified Developer", "Practitioner", or "Specialist". French: "Développeur certifié Sindral".
- Display "skill badge" and "vendor credential" near the name. This is not a professional licence.

## 8. Remaining risks

- You are author, grader designer, and reviewer. The plan above reduces this and does not remove it.
- If agencies later use the badge as a partner-tier gate, stakes rise. Revisit the cut, the retake limits, and proctoring then. A beta label protects you only until that moment.
- Exam security is untested. Expect answer sharing among agencies. Three variants and a regular refresh slow it.

**Next:** Send the one-page job survey (feature frequency and damage ratings) to the 11 devs. About 20 min to write. Then book 1 h with counsel for the name and the privacy items.