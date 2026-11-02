# Partner-delivered customer workshops for Tessaract

**Short answer:** a one-hour webinar plus a deck and a lab repo is not enough. It skips four things: a grant rule, a lab environment standard, certification, and a quality check on each delivery. One consultant for 20-30 people also breaks the staffing rule. Set it up in the phases below.

## Open decisions (assumed, please confirm)

I couldn't interview you, so I inferred these answers from your request. Each one changes the plan.

| # | Assumption | What changes if wrong |
|---|---|---|
| 1 | The first job is technical win in open opportunities, not adoption. | If it's adoption, the grant rule keys on usage and the challenge format moves up. |
| 2 | Workshops are free presales, capped at one day. Partners deliver them for Tessaract-sourced accounts or accounts they co-sell. | If partners charge their client, it's paid services. Then the grant rule, catalog and certification still apply, but the next-step agreement belongs to the partner's SOW. |
| 3 | Tessaract provisions the lab environments. Partners never host them. | If partners host, the lab-defect risk and the data-handling burden move to them. |
| 4 | Labs use synthetic API traffic and a deliberately vulnerable sample app, never customer data. | If any lab needs customer APIs or traffic, that is build-on-your-use-case and needs the customer's written security agreement. |
| 5 | Delivery is mostly virtual or on site in Germany and Brazil. Customer networks are unknown. | Locked-down networks make the dry run mandatory (it already is) and delete laptop installs. |
| 6 | The existing deck and lab repo have never been run end to end by someone outside Tessaract. | If they have been, Phase 1 shrinks. |
| 7 | There is no hard first date. | With a hard date, ship one module and one lab, not a catalog. |
| 8 | The 4 SEs can spare about 40 hours per quarter combined for the partner program in a bad quarter. | This is a placeholder. Name the real figure before Phase 2. |

## What breaks in the current plan

| Your plan | Problem | Fix |
|---|---|---|
| One-hour recorded webinar = enablement | Watching is not delivering. Nobody has run the lab, led a room or fixed a stuck attendee. Bad workshops leave attendees believing the product is hard. | Webinar becomes step 0 of a certification ladder (Phase 2). |
| Deck + lab repo, then "good to go" | An untested lab fails at minute zero on a customer network. Lab repos nobody tests decay within a release or two. | Automated checkpoint tests, a Tessaract-provisioned environment, a named maintainer (Phase 1). |
| One consultant per 20-30 people | The rule is 1 instructor plus 1 helper per started block of 10. That means 20 attendees need 1 + 2 and 30 attendees need 1 + 3. A solo consultant cannot unblock 20-30 people. | Cap cohorts or add helpers (Phase 3). |
| Partners "staff themselves" | No quality gate, no grant rule, no one deciding which accounts get a workshop. | Same grant rule for partners, certification, observed first deliveries. |
| Goal: "scale beyond 4 SEs" | Scale without a grant rule just multiplies goodwill workshops. | Gate first. Scale the qualified ones. |

## 1. Grant rule (partners follow the same one)

Sign it before any partner delivers. It needs a named sales owner and a named SE/DevRel owner. Apply it to partners' requests too.

**Prospect workshop: grant only when all hold**
- [ ] An open qualified opportunity exists, with a named champion in the account.
- [ ] Discovery names one use case, mapped to a catalog module (for example "find undocumented APIs in production traffic").
- [ ] A decision maker attends the opening or the readout.
- [ ] A next-step agreement is written before the date is set.

**Customer adoption workshop** (if you add this job): a named customer-side owner, a usage gap, and a next step measured in usage.

**Otherwise offer, in this order:**
1. A self-paced lab.
2. A one-hour architecture or office-hours session.
3. A recorded workshop plus a take-home lab.

**Partner-specific rules:**
- Requests that fail the rule go to the sales owner, never straight to a partner.
- The partner does not self-grant. A Tessaract AE or partner manager signs each grant. Log the request, decision and attendees against the opportunity.
- Cap each workshop at one day of delivery. Anything longer is paid services.

## 2. Catalog

Start with one module and one lab, not a catalog. Add a module only when two or more qualified accounts need the same missing use case.

| Field | Standard |
|---|---|
| Title | The developer's problem, for example "Find and block an unauthenticated endpoint in 30 minutes". Not "Intro to Tessaract". |
| Length | 60-90 minutes per module |
| Checkpoints | Each is script-verifiable and ships a solution state, so a stuck attendee can skip forward |
| Languages | Decide per partner: German and Portuguese materials, or English labs with local-language facilitation. Translate lab text only if a script still verifies the checkpoints. |

**Default format:** guided lab half-day, with lecture blocks under 15 minutes and a 20-minute readout with the decision maker. Use the half-day agenda from the templates reference:
- Welcome and success criterion
- Problem framing
- Module 1 (about 60 minutes)
- Break
- Debrief
- Module 2 (about 60 minutes)
- Readout
- Close with a take-home path

**Later formats:** build-on-your-use-case once an opportunity has a written evaluation plan and the champion has cleared the data question. Challenge events suit customers with baseline skill and confuse early prospects.

## 3. Lab environment standard

Tessaract provisions and owns the environment. This is non-negotiable for partner delivery.

1. **Vendor-provisioned disposable environment per attendee.** Pre-built, least-privilege, auto-expiring. Attendee trial accounts are for take-home only. No laptop installs.
2. **Region.** Provision a EU region for Germany and a Brazil/LatAm-appropriate region for Brazil, if your platform allows it. Check the data-residency implications of both, GDPR and LGPD, with whoever owns privacy at Tessaract. I haven't verified your legal position.
3. **Synthetic data only**, shaped like the customer's APIs. Never put customer data in a vendor-held environment without written agreement. Never collect attendee credentials for their own systems.
4. **Automated checkpoint test.** For each checkpoint, run setup, confirm the check fails, run the solution, confirm the check passes. Run it nightly or on every product release, and again within 24 hours before each delivery. This is baseline, not a vendor standard.
5. **Repo ownership.** The lab source lives in your own repository, versioned with the product, with one named maintainer per module. Partners fork or consume it. They never edit the production copy.
6. **Time-to-live** longer than the session, including breaks.
7. **Slowest provisioning step** sets the schedule. Some cloud services need 48 hours. Test your own.
8. **Pool size** is confirmed attendees plus two spares. Start provisioning at least an hour before.
9. **Teardown** after the session. Give attendees a take-home path in their own account with cleanup steps.
10. **Customer network checklist**, answered in writing before the dry run:
    - VPN
    - Outbound domains and ports
    - IP allow-lists
    - Managed laptops
    - Corporate-email sign-ups
    - Who can fix any of these on the day

Dry-run on the customer's network with one onsite attendee running the prerequisites and the first module.

## 4. Delivery and certification ladder

**Staffing:** 1 instructor plus 1 helper per started block of 10 attendees. Virtual: add one helper per breakout room.

| Attendees | Minimum staff |
|---|---|
| up to 10 | 1 + 1 |
| 11-20 | 1 + 2 |
| 21-30 | 1 + 3 |

Your one-consultant plan covers none of these. You have two options:
- **Cap cohorts at 10** and run more sessions. This is the cheaper fix for early deliveries.
- **Staff 3-4 people** per 20-30 attendees. Helpers don't need instructor certification, only ladder steps 1-2.

**Partner gate** (borrowed from AWS's partner-delivered Immersion Day gate, adapted):
- Partner tier or agreement in place
- At least two practitioners who can reach instructor level, so one resignation doesn't end the program
- An executive sponsor on the partner side
- A one-day onboarding event before the first customer delivery. This replaces your one-hour webinar and includes the grant rule, the lab, a full dry run and the instructor checklist.

**Certification ladder** (this skill's construction; vendors publish entry gates, not shadow ladders):
1. Run every module alone, end to end, on a fresh environment.
2. Help at one delivery.
3. Co-deliver: lead one module while a certified instructor leads the rest.
4. Lead a full workshop with a certified instructor observing and scoring against the checklist.
5. Certified. Re-run step 1 on every major lab version.

Until a partner has a certified instructor, a Tessaract SE or a certified instructor is in the room for steps 2-4. Plan roughly 3 supervised deliveries per partner, about 9 across three partners. At about 1 SE-day each for the supervision itself, that's roughly 9-15 SE-days in the first quarter (baseline estimate, not a sourced figure). Compare it with your answer to assumption 8 before committing.

**Rehearse every workshop.** Pass the instructor checklist before each delivery:
- [ ] Ran every module alone on a fresh environment this week
- [ ] Automated checkpoint test passed within 24 hours
- [ ] Dry run on the customer network
- [ ] Environment time-to-live longer than the session
- [ ] Helpers briefed: attendees type, helpers point
- [ ] Lecture blocks under 15 minutes
- [ ] Readout slot with the decision maker held
- [ ] Teardown scheduled; take-home path and cleanup steps sent

**Quality check per delivery:** a Tessaract observer or the recorded session reviewed against the checklist, for the first N partner-led deliveries (set N after the first quarter). Partners also use the same workshop brief and champion recap.

## 5. Workshop brief (one per account)

```
Account / job / opportunity stage:
Success criterion and next-step agreement: <link>
Attendees: name, role, confirmed (calendar), prerequisites done
Modules and order:          Format:          Environment:
Logistics call date:        Dry run date (customer network):    Automated test date:
Instructor:   Helpers:      Tessaract AE role: opening, readout, champion conversation
Follow-up owner and date of champion recap:
```

**Next-step agreement** (written with the champion before the date is set):

```
Account:                       Workshop date:
Success criterion: <observable, e.g. "3 attendees reach checkpoint 4 with their own schema">
If met:     <step: POC scope, evaluation plan, rollout>   Date:   Owner (Tessaract):   Owner (account):
If not met: <fix cause, re-scope, or stop>               Decided by:
Agreed by champion: <name, date>      Agreed by AE: <name, date>
```

**Division of roles:**
- The partner instructor owns the room.
- The Tessaract AE owns the opening, the readout and the champion conversation. The AE does not sit at the back.
- Attendees get technical help and the take-home path. They never get a sales call or a generic nurture sequence.
- Send the champion recap within one business day.
- If the criterion fails, fix the cause (wrong attendees, broken lab, wrong use case) before offering a second workshop.

## 6. Scorecard

Log every workshop against its opportunity on the day it is granted, with attendees linked and the decision recorded. Without that, no metric below holds.

| Level | Signal |
|---|---|
| 1 Reaction | End-of-day rating plus one open question |
| 2 Learning | Checkpoint completion per module, from the lab check scripts |
| 3 Behaviour | Attendees active in their own trial or production account at 30 and 60 days |
| 4 Results | Agreed next step executed within 30 days; POC started; technical win; usage change |

**Program row per quarter, split by partner and by Tessaract-delivered:** requests, granted, reshaped, declined; show rate against confirmed attendees; lab defect sessions; delivery hours per workshop; next-step execution rate; comparison group result.

**Comparison group:** matched opportunities without a workshop. Report workshop pipeline as "influenced", never "caused". Workshop accounts are selected for momentum.

**Do not put these figures in your business case.** No independent study of workshop-to-POC conversion is known. Refuse the circulating ones on sight:
- "75% retention from practice by doing"
- "40% of lab users start a trial, up from 14%"
- "15% more pipeline from workshops"
- "244% ROI from hands-on labs"
- "nearly half of POCs fail"
- "evaluations under 90 days win 3X more often"

Use your own baseline after one quarter.

## 7. Pass threshold

The first gated quarter sets the baselines. From the second quarter, continue unchanged only if all four hold:

1. Next-step execution rate holds at or above the first quarter's rate, pooled over at least 10 workshops. With fewer, pool quarters before judging. Fix: tighten the grant rule.
2. No live session hits an environment-caused checkpoint failure. Failures the dry run catches count as the test working. Fix: the test rule, then the maintainer.
3. Every instructor that quarter sits on the certification ladder. Fix: pause uncertified delivery.
4. Delivery hours fit the hours you named. Fix: decline-with-alternative before cutting rehearsal.

Judge partners individually. A partner that fails 2 or 3 pauses delivery until it passes.

## Rollout order

1. **Phase 1, before any partner (Tessaract-owned):**
   - Write and sign the grant rule.
   - Build one module and one lab with checkpoint scripts and solution states.
   - Provision environments in each region.
   - Run the automated test.
   - Have an SE who did not write the lab run it cold.
2. **Phase 2, partner onboarding:**
   - Run the one-day onboarding event, with the recorded webinar as pre-reading only.
   - Partners reach ladder steps 1-2.
3. **Phase 3, supervised deliveries:**
   - Run ladder steps 3-4 on real qualified accounts, with cohorts capped at 10 or staffed to the 1 + 1-per-10 rule.
   - Debrief each delivery against the checklist.
4. **Phase 4, certified delivery:**
   - Certified instructors deliver with partner helpers.
   - Tessaract reviews recordings.
   - Run the first quarterly review against the pass threshold.

## What you decide next

1. Confirm or correct the 8 assumptions at the top. Assumptions 2 and 8 matter most.
2. Name the sales owner who signs the grant rule.
3. Decide cap-at-10 or staff-to-ratio for the first partner deliveries.
4. Name one lab maintainer and one SE to run the lab cold.

I can draft the signed grant rule or the onboarding-day agenda next.