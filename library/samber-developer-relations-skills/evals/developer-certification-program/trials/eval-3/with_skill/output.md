**Do not sign the proctoring contract yet.** The design has 4 blockers, and the vendor you picked adds legal risk without fixing the main flaw.

Nothing in the design has a source, so I label every figure in it self-set. That covers 60 items, 90 minutes, 70%, 180 items, 3 years and 2 forms. Next step: read the "Next action" at the bottom.

## 🔴 Blockers

**1. Design contradicts itself: unproctored, AI banned, then a proctoring vendor.**
- Unproctored multiple-choice measures search and assistant use. The skill deletes it as an assessed credential. Keep it only as a free practice quiz.
- "AI strictly prohibited" is enforceable only under live or test-centre proctoring with screen capture. Never ban what you cannot detect.
- Face matching proves who started the sitting. Gaze flags watch the eyes. Neither sees a second device, a chat window or a colleague off camera.
- The vendor adds cost and legal exposure, but the ban stays unenforceable.
- The ban also fights the job. Observability engineers use assistants daily.

**2. Face matching and AI gaze flagging are automated face processing, with no privacy work done.** That is the main compliance cost driver. Your four sites make it worse:
- **Chicago:** Illinois BIPA needs a written release before collecting face geometry, a published retention and destruction schedule, and carries a private right of action. Proctoring vendors have faced class actions.
- **Germany and France:** GDPR treats biometric data used to identify a person as special-category data. You need a lawful basis, a special-category condition, a retention limit and a DPIA. The vendor is your processor, but the duty stays with you.
- **EU AI Act:** AI that monitors prohibited behaviour during tests in education and vocational training is listed as high-risk. Check how it applies to a vendor credential before you deploy gaze flags to EU candidates.
- **Bangalore:** I did not research Indian rules. Check them. India's data-protection law is the starting point.
- **Missing in the design:** a non-biometric path, published retention, human review of every flag before any sanction, and accommodations. Gaze flags also misfire on candidates with disabilities or neurodivergence.
- Run the privacy review before you choose the vendor, not after.

**3. The tier claim does not match the build.**
- Customers write "engineers certified" into support contracts. If a contract counts certified people, the ceiling is role certification. If it only mentions them in passing, the ceiling is a skill badge.
- You have not shown me the clause. Get the wording first.
- Role certification needs a job task analysis, a standard-setting study per blueprint, equated forms, item security, a real identity check, an appeals path and a funded renewal cycle. Your design has none of these.
- The promotion test has 3 conditions: an outside consumer acting at role level, 2 funded years, and a standing owner of the item bank. You have an owner, a successor and 2 funded years. Condition 1 is unproven.
- Funding gap: validity is 3 years, but funding covers 2. Holders exist for 3+ years after the last sale. You owe the claim as long as holders exist.
- Support wrote the items. If they do not hold the bank long term, the owner condition fails too.

**4. The item bank cannot support a pass/fail credential.**
- 180 items written by the support team, with no job task analysis, no bias review, no pilot and no item statistics. Never score an unpiloted item.
- Support tickets reflect what breaks, not what the role does. A feature-derived or ticket-derived blueprint certifies a menu, not the job.
- "Two parallel forms rotated monthly" means two fixed forms that every candidate eventually sees. Brain-dump sites will have both within a few cohorts. 180 items give about 60 spare. You need exposure analysis and many more forms.
- No anchor items are mentioned, so there is no equating. 70% on two forms of unequal difficulty is two different standards.
- 70% has no standard-setting method behind it. A failed candidate or a buyer's lawyer can break it. Run a modified Angoff panel (5-15 experts), or issue a completion badge.
- Keep item writers off prep-course authoring.

## 🟠 Gaps

- **Validity 3 years, no version binding.** Bind the credential to the supported major version or to a calendar blueprint review. Name who chose 3 years and whether your release cadence fits. Add a short hands-on delta task for renewal, with the sampled live check, so renewal is not the proxy-sitting route.
- **Proxy sitting is unaddressed.** Customers put this credential in contracts, so one strong engineer sitting for colleagues is the named threat. Counter it with a 15-minute live explanation on a sample of passes, announced in the candidate agreement.
- **Name risk.** "Engineer" is a regulated title in some places, such as Canadian provinces. I believe Germany protects "Ingenieur" too, but I did not verify that. Check before you print it. Say what a "Brightmoor Certified Engineer" is allowed to claim.
- **Missing sections:** price, vouchers, verification, revocation, appeals, retakes, retirement of a form, program retirement, outcome metric, go/no-go and kill rule.
- **Price:** compute a break-even fee per attempt. Formula: (yearly fixed + yearly operating) ÷ attempts per year + per-sitting cost − amount a partner program or contract absorbs. You have not done this, so you cannot judge whether the vendor's per-sitting cost fits.
- **Language and access:** 90 minutes for 60 items in what language? Candidates in Germany, France and Bangalore may sit in a second language. Add extra time, a score report per domain, and an accommodations path before scheduling.
- **Verification:** use signed Open Badges 3.0, with revocation updating the status entry. Make any public directory opt-in.

## 🟢 What works

- Real outside demand: customers write the credential into contracts.
- Named owner, named successor, and funding.
- An item bank exists as raw material.
- Four regions force the privacy question early, before launch.

## Three candidate designs

Ordered by efficiency. Build sizes are my estimates, not sourced.

1. **Skill badge now.** Auto-graded hands-on tasks in a disposable tenant (query, alert, dashboard fixes). Assistants allowed. Account login, plus a live defence on about 1 pass in 10. No face matching. Rename it "Brightmoor Certified Practitioner" or similar, not a title that implies role competence. Weeks of work, not months.
2. **Role certification, full.** Job task analysis, Angoff panel, equated forms, a live-online human-proctored hands-on exam with no face matching, a funded renewal cycle. Heavy: a panel, environment hosting per sitting and a bigger bank. Needs the clause evidence and funding past year 2.
3. **Skill badge now, role certification on a trigger.** Ship option 1. Write the trigger as an observable event: a contract that names certified people, plus funding for the holder lifetime. Then build option 2.

**Recommendation: option 3.** It meets customer demand soonest and defers the expensive obligations until the contract evidence is in hand. If a customer clause already names certified people, pull option 2 forward and keep option 1 as the fallback.

## Before you sign the vendor contract, require

- A DPA naming the vendor as processor, with a sub-processor list and EU/IN data residency terms.
- No stored face templates by default, plus a non-biometric option such as live human identity check or test centre.
- Retention and deletion terms, and BIPA-style written release handling for Chicago.
- Flags go to a human reviewer. No auto-sanction.
- Accommodation handling and appeals support.
- Per-sitting price for live online versus automated, so you can feed the break-even fee.
- Data export and exit rights. You keep the master holder record.
- Award decisions stay with Brightmoor.

## Next action

Send me the exact wording of 2 or 3 customer support-contract clauses. About 10 minutes to pull. That decides whether the ceiling is a skill badge or a role certification, and which design to build.