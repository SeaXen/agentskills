# Lumenshift certification program charter (draft v1)

Date: 2026-10-23. I could not interview you one question at a time, so I made assumptions. The 8 items under "Confirm before sign-off" at the end can change the design. Every number below is **self-set** unless it says otherwise. I quote no vendor figures.

## Verdict up front

- ❌ Two exams, "Certified Professional" and "Certified Expert", in six months does not pass the gate. Nobody outside Lumenshift counts certification yet, and no tender names it.
- ✅ Build the ceiling tier now, and make Expert the headline. Expert is earned by a **reviewed client project plus a live defence**, not an exam.
- ✅ Write down the event that unlocks the role certification, so the CEO sees a path and not a no.

## 1. Gate verdict

- **Outside consumer:** your consultants' clients. They shortlist from the 'Find a partner' directory and by word of mouth.
- **Action they take:** they ask "are you certified?" That is reported second-hand by consultants. No tender or contract names certified people.
- **Ceiling:** skill badge. Role certification needs a buyer contract or procurement checklist that counts certified people.
- **Rejected alternative:** a free completion or showcase badge alone. It cannot tell a client who the expert is.
- **Requested tier above the ceiling:** "Certified Professional" and "Certified Expert" as role-level exams. I deliver the ceiling tier. The trigger that unlocks the requested tier is in section 6.
- **Evidence gap:** "clients ask" rests on consultant anecdotes. In weeks 1–4, collect a count of asks and 5 client conversations. If clients turn out to ask for nothing, the gate fails and a public learning path replaces this program.

## 2. Candidate designs (ordered by efficiency)

| | A. Professional-only badge | **B. Expert-first (recommended)** | C. CEO's ask |
|---|---|---|---|
| Tier | Skill badge | Skill badge, via reviewed project | Role certification ×2 |
| Format | Auto-graded hands-on, unproctored | Project dossier, double-scored, live defence | Proctored exams |
| Levels at launch | 1 | 1 | 2 |
| Serves | ~400 consultants, "are you certified?" | The top consultants clients fight over, the CEO's headline | Both |
| Build in 6 months at 10 h/week | Fits | Fits, with reviewers | No: two banks, two standard-setting studies, two renewal cycles |
| Weakness | No headline, no "expert" signal | Most consultants get only a free completion badge until the trigger fires | Above the gate ceiling; the Expert exam has the smallest pool, hardest cut score and most public failure |

Why B: clients choose between consultants, and the signal that changes that choice is "this one is verified expert". Consultants already hold delivered client work, and a defence tests the person, not the artefact. Choose A instead if breadth matters more to you than the headline.

**Your pick is needed before section 3 onward is final.** The rest of this charter assumes B.

### Design B in one place

- **Level names:**
  - "Lumenshift Expert" carries the **skill-badge tier**. Its claim is bounded and evidence-based: "delivered a production-grade Lumenshift solution to a published rubric and defended it live".
  - A free "Lumenshift Foundations" completion badge for the prep course carries the **completion tier**.
  - "Professional" is deferred (section 6 has its trigger).
- **Naming:** reserve the prefix "Certified" for the role tier. Putting it on a skill badge invites a tender writer to read it as role competence. Present this to the CEO as a rename that is earned when the trigger fires.
- **Format:** reviewed project plus 45-minute live defence.
- **Proctoring and identity:**
  - A human watches the defence on camera. There is no face matching and nothing is recorded, so there is no biometric processing.
  - A consent-based reference check with one client contact confirms the candidate led the delivery.
- **AI policy:** allowed. The claim is "works with their own tools". The defence is the human-attributable step.
- **Deleted options:** the Expert exam, any multiple-choice assessed credential, proctoring services, a test-centre network, an exam-delivery partner (no proctored sittings), and a second level at launch.

## 3. Competency blueprint

Placeholder domains, to be replaced by a job task analysis before anything is published:

1. Solution design and data modelling.
2. Workflow logic, error handling and retries.
3. Integrations and API use.
4. Security, permissions and governance.
5. Performance, monitoring and operations.
6. Client delivery: handover, documentation, change management.

- **Method:**
  1. Interview 10–12 practitioners, a mix of freelancers and firm staff.
  2. Read escalated support tickets and project post-mortems.
  3. Rate each task for frequency and cost of a mistake.
  4. Derive the domain weights from those ratings.
- **Weights:** none yet, since inventing them would make them features-derived. They are self-set from that analysis. Publish domains and weights.
- **Cost of waiting:** none. This analysis is reused unchanged if the role certification is built later.

## 4. Build plan (against 260 owner hours: 10 h/week × 26 weeks)

| Item | Owner hours | Other effort |
|---|---|---|
| Job task analysis | 40 | Interviewee time |
| Rubric, candidate agreement, handbook, privacy check | 40 | Legal or privacy owner review |
| Reviewer calibration panel | 10 | 6 reviewers × 4 h |
| Founding pilot (8–10 invited top consultants) | 25 | Reviewer time |
| Issuing service (buy), directory credential field and opt-in | 20 | Web team time (to be confirmed) |
| Prep course on a MOOC marketplace | 20 oversight | Produced by a contracted trainer |
| Go/no-go and launch | 15 | |
| **Total** | **~170** | **~90 h buffer (about a third)** |

- **Rubric:** 5–6 dimensions matching the blueprint domains, scored 0–3 each.
- **Pass rule:** non-compensatory. A minimum score is required in every domain.
- **Dossier:** an anonymised architecture, evidence of a running production solution, a client consent note, and a "what I would change" section. The solution must run on a currently supported major version.
- **Fallback for work under NDA:** a Lumenshift-written sandbox case brief. Build it only if more than 25% of applicants lack showable work.
- **Capacity:** a cap of 10 candidates per quarterly cohort, so 40 a year. Demand above that goes on a waitlist.
- **Hours per candidate:** about 6 reviewer hours, which is 60 hours per cohort. Reviewers are Lumenshift solutions and support engineers, paid from the approved budget or time-allocated.
- **Cut line:** if the plan overruns, cut cohort size or the fallback brief. Never cut the pilot or the calibration panel.

## 5. Integrity plan

- **Cut-score method:**
  - The calibration panel scores 6 sample dossiers and writes the minimum evidence for each rubric cell. It uses the same panel logic as a modified Angoff study, adapted to a rubric (Cizek and Bunch, *Standard Setting*, 2007).
  - Every candidate is double-scored by two reviewers.
  - A third reviewer scores any gap above one point.
  - Reviewer agreement is reported per cohort.
- **Equating:** not applicable, since there are no exam forms. Calibration replaces it.
- **Item security:** nothing secret to leak. Publish the blueprint and rubric. The defence, not secrecy, protects the claim.
- **Proxy-sitting counter:** the live defence includes a change made on the spot in the candidate's own solution. The client reference check confirms who led the delivery.
- **Impartiality:** no reviewer scores their own colleague, anyone they trained, or a direct competitor's staff. Reviewers declare conflicts.
- **Privacy review:**
  - There is no automated face processing, so no biometric review.
  - Dossiers hold client data. Delete them 6 months after the decision, once the appeal window has closed.
  - Keep reviewer notes for appeals only.
  - Confirm candidate countries (question 10 below) for data-protection rules.
- **Accommodations:** extra time, a written-first or chat-based defence, and a documented appeal. Request before scheduling. Only the reviewer sees accommodation documents.
- **Candidate agreement** covers conduct, AI policy, dossier confidentiality, grounds for revocation, and an appeals decision-maker who sits **outside** the review panel. Name that person.

## 6. Renewal, version binding, retake, retirement and the role-certification trigger

- **Version binding:**
  - The badge is stamped with the major version tested. It has no expiry.
  - The verification page shows "tested on vN, supported until [date]".
  - You ship a major yearly, supported for two years, so at most two majors are live.
- **Optional re-stamp:** a free 30-minute delta defence on the new major, for holders who want the current stamp.
- **Re-alignment:** review the rubric within 6 weeks of each major's release. Refresh the job task analysis every second major.
- **Retake:**
  - A failed candidate receives a per-domain score report.
  - The waiting period is 60 days.
  - The cap is 2 attempts per 12 months.
  - A second attempt reviews only the changed parts, at half the fee.
- **Exam-version retirement:** announce 6 months ahead. Holders stay valid and keep their version stamp. Offer the re-stamp.
- **Program retirement:** honour every credential, keep verification live for 3 years after the last award, and refund fees for pending applications.
- **Role-certification trigger:** one written tender or buyer contract naming certified Lumenshift people. Alternatively, three independent client written requests in one quarter that name a certified level.
  - When it fires, the other two promotion conditions are already largely in place: budget for two years, and a standing owner.
  - Re-run the certification skill at that point with the job task analysis, the rubric and the reviewer panel already built.
- **Professional trigger:**
  - Expert has been live through one major or 12 months, whichever comes first.
  - A named consumer asks for a tier below Expert.
  - The auto-graded hands-on task, with a sampled live explanation, is then built.
  - Until then the path is the prep course and the completion badge.

## 7. Price, vouchers, verification

- **Fee logic:** a fee one engagement repays, charged per attempt, with seat bundles for firms. Freelancers pay out of pocket, so publish the prep course and a free practice quiz.
- **Break-even fee (formula from the build reference):**

  ```
  (yearly fixed + yearly operating) / attempts per year + cost per attempt
  ```

- **Illustrative inputs only, replace with your numbers:**
  - yearly fixed 6,000 (build cost over a two-year major-version life)
  - yearly operating 4,000
  - 40 attempts
  - cost per attempt 360 (6 reviewer hours × 60)
  - result: about 610 per attempt
- **Vouchers:** the founding cohort is comped by voucher, with an expiry date, single use, no resale, tracked as its own campaign. Never report it as organic demand.
- **Credential format:** Open Badges 3.0 through a bought issuing service. Revocation updates the status entry, not only the web page.
- **Verification:** by credential ID or a holder-shared link. Show holder name, credential, version, issue date, "no expiry", and status. On revocation show "not valid" with no reason.
- **Directory:**
  - Extend the 'Find a partner' directory with a "Find a certified expert" filter showing name, firm, credential, version, region, languages and contact.
  - Listing is opt-in.
  - This is the main return on the fee, because it brings client leads.
  - The filter must not hide uncertified consultants, and rank is not for sale.
- **Wording:**
  - Never call the badge a certification to a buyer.
  - If any partner agreement says "certified", reword it to "holding the Expert badge".

## 8. Operating model

- **Owner:** you, 10 h/week. **Successor:** named in the plan, plus a handover rehearsal. The successor shadows two cohorts and runs one alone before month 12.
- **Reviewers:** 4–6 trained Lumenshift engineers, about 2 days per quarter each. From year 2, add Expert holders who are paid and conflict-checked.
- **Prep course:**
  - Host on a public MOOC marketplace. It is free, covers the blueprint domains, and carries a practice quiz.
  - A contracted trainer produces it. The course does not award the credential.
  - Add a hosted copy later if the 30 firms want to enrol staff.
- **Training partners:** deferred. Promote them once candidates ask for classroom or in-company courses. Firms teaching the product are the likely first partners.
- **Firewall:**
  - No training partner scores its own students.
  - Reviewers do not author prep courses.
  - Nobody sells "guaranteed pass".
  - Vendor staff keep the award decision.
- **Budget lines (two-year, amounts to fill):** issuing service, course production, reviewer time, directory development, privacy or legal review, interviewee thank-yous.

## 9. Measurement, go/no-go, kill rule

- **Outcome metrics (outside consumer):**
  - Directory contact requests to Expert holders versus non-holders.
  - Engagements holders won citing the badge, from a yearly holder survey plus a "how did you find us" field on client intake.
  - Tenders or contracts naming certification.
- **Health signals:** reviewer agreement, appeals, defence fail rate, cohort fill, days to decision, re-alignment time per major.
- **Holder count** is a health signal only. The verification page shows a live, verified holder count instead of a target.
- **Go/no-go: 2027-02-26** (8 weeks before a late-April 2027 launch). Required:
  - the job task analysis is done
  - the panel is calibrated on 6 samples
  - at least 6 founding dossiers are reviewed
  - the issuing service is live
  - the directory filter is live
  - reviewers are contracted
- **Fallback if go/no-go fails:** launch the completion badge and open Expert applications. Announce founding Experts as cohorts clear.
- **Kill rule:** by **2028-10-23** (18 months after launch), kill or restructure if any of these is true:
  - Expert listings draw no more than 1.5× the contact requests of non-holders.
  - Re-alignment misses its 6-week window on two consecutive majors.
  - Reviewer agreement falls below 80% within one point for two cohorts.

## 10. Where each number came from

- **Sourced:** only the Angoff method, cited to Cizek and Bunch, *Standard Setting* (2007). The 1.5×, 80%, 60-day, 40-per-year, 6-week, 6-hour, 25%, 8-week and 18-month figures are self-set. So are the hour estimates, the seat and fee illustration, and the retention periods.
- **Unknown yet:** job task analysis weights, actual budget, candidate countries.

## What to tell the CEO

- Expert **is** the headline: first in the directory, the top listing, launched in six months.
- It is earned on delivered work. Her best consultants already have that work, and the defence protects the name.
- "Certified" and the Professional exam come when one client puts certification in a tender. The analysis behind them is built now, so waiting loses nothing.

## Confirm before sign-off

1. How many consultants reported client asks, and what kind of clients?
2. Does an external event force six months, or is that a preference?
3. Which countries and languages do candidates work in?
4. What course, lab or sandbox assets exist today?
5. Must the program break even, or is it a cost centre?
6. Does the web team own the directory, and what capacity does it have?
7. Who is the successor, and who decides appeals?
8. When is the next major version released?

I saved this to project memory (`project_lumenshift-certification-charter.md`) because the skill asks for it. Say if you want it in CLAUDE.md instead.

**Next step:** pick A or B. Then answer questions 1, 2 and 5 first, since they could change the gate.