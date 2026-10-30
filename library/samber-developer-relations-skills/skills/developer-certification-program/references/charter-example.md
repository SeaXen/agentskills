# Certification program charter: worked example

Illustrative. The company, the numbers and every threshold below are invented to show the shape; none is a benchmark.

## Contents

- Situation
- Positive example: the charter
- Negative example: the borrowed-benchmark charter
- What separates the two
- Failure modes

## Situation

A message-queue SaaS with an SI partner program. Two enterprise buyers asked last quarter whether the partner proposed to them had certified engineers, and the partner team wants Gold partners to hold two credentials each. The product ships a minor release every two weeks and a new major API version yearly, each supported for two years. One education lead can give the program eight hours a week; a solutions engineer is the named successor. The company wants the program to break even within two years.

## Positive example: the charter

**1. Gate verdict.** Outside consumer: buyer procurement teams choosing an implementation partner (two written requests last quarter). Action, to confirm: shortlisting partners whose engineers hold the credential; the first outcome metric tests it. The partner program's Gold requirement is the vendor's own mandate, so it counts only because buyers act on it. Ceiling: skill badge now; role certification needs a buyer contract that names certified people. Rejected alternative: partner implementation reviews alone, because buyers ask about people, not projects.

**2. Tier, format, proctoring, levels.**

- One level, "Implementer", carrying the skill-badge tier. Deleted: an expert level and any multiple-choice exam.
- Format: auto-graded hands-on tasks in a disposable tenant; checkers verify queue topology, retry policy and dead-letter handling end state.
- AI policy: assistants and docs allowed, because partner engineers use both on the job. The badge claims working competence with the engineer's own tools.
- Identity and proxy sitting: account login, plus a 15-minute live call on one pass in ten, where the holder explains and changes their own solution. Partner tiers pay for this credential, so proxy sitting is the named threat.
- Certification trigger: the first buyer contract that names certified people, plus funding for two years of re-alignment.

**3. Competency blueprint.** From twelve partner-engineer interviews and two quarters of escalated tickets: design topology 30%, configure delivery guarantees 25%, troubleshoot backlog and consumer lag 25%, secure tenants 20% (self-set from that analysis).

**4. Build plan.** Eight tasks (two per domain), two variants each, reference solutions, a pilot with ten partner engineers (enough to test task clarity and checkers, too few for item statistics), an issuing service bought rather than built. Estimated 70 owner hours over three months plus 30 reviewer hours (self-set).

**5. Integrity plan.** A panel of six senior partner engineers writes each task's minimum end-state checks from pilot solutions. Checkers run in CI against every minor release; a failing checker pulls that task variant from live forms until fixed. No face matching, so no biometric review; the verification page still lists holders by credential ID only. Accommodation: extended time on request.

**6. Renewal and retirement.** Badge stamped with the major API version tested, no expiry. On a new major version, a 30-minute delta task upgrades it; the older badge stays valid and labelled with its version while that API version is supported. Program retirement: verification stays live three years after the last issue (self-set).

**7. Price, vouchers, verification.** No fee to partner staff: Gold partners get four seats a year, Silver two; a seat is the allocation that caps hosting cost. Open Badges 3.0 credential, verification by credential ID, revocation for proven misconduct shown as "not valid", appeal to the head of partnerships. Partner agreement reworded from "certified engineers" to "engineers holding the Implementer badge".

**8. Operating model.** Owner: education lead, eight hours a week; successor: solutions engineer. Reviewers: two solutions engineers, two hours a month for checker failures. Budget line: partner program.

**9. Measurement, go/no-go, kill rule.** Outcome: buyer RFPs or contracts that name the badge; implementation escalations per project from badge-holding versus other partner teams. Health: Gold partners meeting the requirement, pass rate per task variant, checker failures per release, appeals. Go/no-go eight weeks before the conference: pilot pass data and all checkers green, else launch a completion badge and ship the assessed badge next quarter. Kill rule (self-set): no buyer naming the badge within 18 months.

**10. Where each number came from.** Interview counts, weights, hours, seat counts, windows and kill threshold: self-set. Panel method: modified Angoff adapted to end-state checks (Cizek and Bunch, Standard Setting, 2007). No other external figure used.

## Negative example: the borrowed-benchmark charter

> We will launch Associate, Professional and Expert certifications at the conference. Industry standard is a proctored 60-question multiple-choice exam, 70% to pass, valid for two years, $150 per attempt, so we will follow it. Success is 5,000 certified developers in year one and every Gold partner meeting the requirement, driven by free vouchers at every event.

## What separates the two

- The negative charter names no outside consumer; the partner requirement it counts as success is its own mandate.
- "Industry standard" hides several vendors' different choices; the positive charter labels every number.
- 70% has no standard setting behind it.
- Three levels at launch triple item banks and panels before one level has survived a release.
- Recall items are what assistants and leaked dumps answer best, and they test nothing partners do on the job.
- 5,000 voucher-driven holders measure the voucher budget, not the credential's value.
- No renewal, version binding, retirement, verification, go/no-go or kill rule.

## Failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Thousands of holders, no buyer or hiring use | No outside consumer | Re-run the gate; downgrade to a free badge or retire |
| Partners hold badges, customers ignore them | Consumer was the vendor's own mandate | Measure buyer-side outcomes; run implementation reviews |
| Pass rate jumps between quarters | Bank leaked, or tasks solvable unattended by agents | Rotate items, add a human-attributable step, run item exposure analysis |
| "Industry standard is two years" in the charter | Borrowed benchmark | Name who chose it and whether your release cadence fits |
| Cut score of 70% "because it looks right" | No standard setting | Run a study, or issue a completion badge |
| Holders stranded when an exam retires | No retirement rule | Honour until expiry, stamp the version, offer a path |
| Proctoring complaints or a privacy claim | Face processing without review or alternative | Privacy review, non-biometric path, human review of flags |
| Prep course sold as "guaranteed pass" | Training and certification not separated | Wall item writers off courseware, drop the guarantee |
