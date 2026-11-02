# Quarrystone customer workshop program

## Open decisions (assumed, no interview was possible)

Each answer below is my inference from your message. Correct any of them and I'll re-rank.

| # | Interview question | Assumed answer | What moves if wrong |
|---|---|---|---|
| 1 | First job | **Technical win in open opportunities (prospects).** Adoption workshops for customers are a second track and are not designed here. | If adoption comes first, the grant rule keys on usage and the challenge format moves up. |
| 2 | Who requests | AEs, on prospect request. 31 last quarter, 2 POCs. | None. |
| 3 | Delivery hours | DevRel + SE. The hours in a bad quarter are unknown. | The baseline is about 2.5 days × 31 ≈ 78 delivery days last quarter. If that's over budget, tighten the grant rule before cutting rehearsal. |
| 4 | Build-on | Quarrystone can provision a disposable cloud cluster per attendee. | If only trial sign-ups exist, the minute-zero failure risk rises. |
| 5 | Location | Prospect offices, with unknown VPN and managed-laptop rules. | If networks are locked down, delete laptop installs and make the on-network dry run mandatory. |
| 6 | Existing assets | One standard deck and one lab. Last end-to-end test date unknown. | Run the Step 4 test before the first gated workshop. |
| 7 | Deadline | None stated. Goal is a program that compounds. | If a hard date appears, ship one module and one lab only. |
| - | Sales owner who signs the grant rule | **Unnamed. Needed before the rule takes effect.** | Without a named signer, the rule is advice. |

## 0. Diagnosis

**Verdict: keep the program for one gated quarter. Stop it if the qualified workshops also produce no next step.** Your own data can't yet say "stop" or "the labs are the issue."

1. **The 40%/14% figure should not be used.**
   - It is a customer testimonial on a lab vendor's site. It is undated, has no sample, and doesn't define "trial."
   - Don't put it in the leadership deck. No independent study of workshop-to-POC conversion is known.
   - The related lab-vendor claims are refused too: "15% more pipeline," "244% ROI," "75% shorter deal cycles."

2. **The 4.6/5 survey measures level 1 (reaction) only.**
   - It shows people liked the day. It says nothing about whether the account moved.
   - ATD's 2019 survey (779 practitioners) found 83% of evaluators measure reaction and 38% measure results. Quarrystone is in the majority.
   - Keep the survey as a trend line. Never use it as the success metric.

3. **"The labs are the issue" is untested.**
   - Your agenda is 2 hours of slides plus a lab. The lab is the minority of the day.
   - A sourced default is lecture blocks under 15 minutes and hands-on for most of the time.
   - The slide-heavy format is a more likely suspect than the lab. Neither is proven, because no checkpoint data exists.

4. **The bigger structural problem is the booking rule.**
   - "AEs book whenever a prospect asks" means the grant rule fails by construction.
   - 2/31 (6.5%) is the full-population rate. It mixes goodwill workshops with real ones.
   - The skill's test is the rate on the qualified subset only.

**Retro-score the 31 before the leadership meeting. It takes about half a day with CRM access.**

1. For each workshop, record whether it met each of the four criteria below (qualified opportunity, named champion, one discovery use case, decision maker attending), and whether a next step was agreed before the date.
2. Count how many workshops meet all of them.
3. Read POC outcomes on that subset only.
4. Apply the call:

| Result | Call |
|---|---|
| The qualified subset converts | Keep and gate it. |
| Too few qualified workshops to tell (likely, since there was no gate) | Keep for one gated quarter. |
| Qualified workshops also produced no next step | Stop, or cut to the decline menu only. |

Also check the two POC accounts. Did they have a champion and a decision maker in the room? That is a hypothesis to check, not a finding.

## 1. Grant rule

Signed by: **[named sales owner]** and **[DevRel/SE owner]**, dated. It applies to every request, including executives' requests.

**Prospect workshop: grant only when all four hold.**

- [ ] An open, qualified opportunity exists at **[CRM stage]** or later, with a named champion inside the account.
- [ ] Discovery names one use case the workshop will prove, mapped to a catalog module (Step 2).
- [ ] A decision maker, or the person choosing the vendor, attends the opening or the closing readout.
- [ ] A next-step agreement is written before the date is set (Step 7).

**Edge case.** The opportunity is qualified but has no champion. Grant only a short virtual follow-along, whose agreed next step is naming the champion.

**Otherwise offer, in this order:**

1. An existing self-paced lab or tutorial path.
2. A one-hour architecture or office-hours session.
3. A recorded workshop plus a take-home lab.
4. A full workshop (only if the rule is met).

A reshaped request counts as granted, in its new format. A request answered from the decline menu counts as declined.

**Escalation.** Requests that fail the rule go to the sales owner, never straight to an SE.

**Capacity.** **[N]** delivery hours per quarter. Requests beyond it queue by opportunity stage.

**Rationalizations the rule must survive:**

| Pressure | Answer |
|---|---|
| "A workshop will unblock the stalled deal." | Deals stall on a decision. Workshops teach practitioners, who don't sign. |
| "The prospect is unhappy, give them a day." | Goodwill content built in a hurry leaves people thinking the product is hard. |
| "They want training on everything." | That is paid training or services. |
| "The whole team wants to come." | Without a champion or a decision maker, there is no next step. |
| "We'll figure out the next step afterwards." | Nobody owns the day after. |

**Request form** (AE fills it in, the SE lead decides):

```
Account / opportunity:        Requested by:        Wanted date:
Opportunity stage:            Champion:
Use case from discovery (one sentence):
Attendees (roles, count):     Decision maker attending? which segment
Environment constraints (VPN, managed laptops, data):
Proposed next step if the workshop succeeds:
Decision: grant | reshape (to: ...) | decline (alternative: ...)    By / date:
```

## 2. Catalog

Build each module backward: the use case the account must prove, then the evidence a checkpoint will show, then the exercises. Never start from a feature tour.

**Rules.**

- Pick and order modules per account from the discovery notes.
- Build a new module only when two or more qualified accounts need the same missing use case (baseline).
- Title each module by the developer's problem.
- Keep each module 60-90 minutes.
- Every checkpoint is script-verifiable and ships a solution state, so a stuck attendee can skip forward.

**Starter modules.** These are drafts. Confirm them against your last quarter's discovery notes.

| ID | Title (developer problem) | Use case it proves | Checkpoints (script-verifiable) |
|---|---|---|---|
| M1 | Make 1M support articles searchable by meaning, and get an answer back in the app | Semantic search and RAG retrieval | 1: collection created and loaded. 2: query returns the expected top result on a seeded query set. 3: the retrieval-quality check passes at the module's target. |
| M2 | Combine keyword and vector search with metadata filters without losing recall | Hybrid search and filtered queries | 1: filtered query returns only in-scope documents. 2: hybrid result beats the vector-only result on the seeded set. 3: latency check passes at the module's target. |
| M3 | Move your existing index over without a rewrite | Migration from the incumbent search or vector store | 1: data loaded. 2: query parity check passes. 3: cutover script runs. |
| M4 | Keep recall and latency stable as data grows 10× | Scale and operations | 1: scale-up step runs. 2: recall and latency checks pass on the larger set. |

**Setting targets.** Set the recall and latency targets per module from your own benchmark runs, and record them in the catalog entry. This skill sets no numbers for them.

**Catalog entry template:**

```
Module id / title:
Use cases it proves:
Format(s): guided lab | follow-along | build-on-your-use-case
Length: 60-90 min      Prerequisites: knowledge / machine and network / accounts
Checkpoints (script-verifiable): 1 ... 2 ... 3 ...
Solution state shipped per checkpoint: yes/no
Environment: provisioned
Slowest provisioning step and lead time:
Maintainer:        Last automated test pass:        Product version:
```

## 3. Format

**Default: guided lab half-day**, with these rules:

- Lecture blocks under 15 minutes.
- Hands-on for most of the day.
- A 20-minute closing readout with the decision maker (baseline).

The current 2-hour slide block is cut to about 35 minutes total, split across three concept blocks.

**Format order for a technical win.**

| Ranking | Order |
|---|---|
| Value | build-on-your-use-case > guided lab half-day > full day with executive session > short virtual follow-along > challenge event |
| Efficiency | guided lab half-day > short virtual follow-along > build-on-your-use-case > full day with executive session > challenge event |

Rough effort per workshop (baseline): short virtual follow-along about 1 day, guided lab half-day 2-3 days from existing modules, build-on-your-use-case a week or more.

**What this order starves: build-on-your-use-case.** It has the highest value for a technical win and is the strongest POC on-ramp. Promote it when the opportunity has a written evaluation plan and the champion has cleared the data question.

- It triggers the customer's security review if their data or environment is involved.
- With synthetic data matching their schema on Quarrystone infrastructure, it does not.

**Cap.** One day of delivery. Anything longer is paid training or professional services. A build-on-your-use-case split over an evaluation stays presales.

**Guided lab half-day agenda** (14 engineers, champion plus a director; adjust per account):

```
09:00  Welcome, goal of the day, success criterion (champion + SE)     10 min
09:10  Problem framing: the use case in their words                    10 min
09:20  Module 1 - lab (checkpoints 1-3)                                60 min
10:20  Break                                                           15 min
10:35  Debrief module 1, 10-minute concept block                       15 min
10:50  Module 2 - lab (checkpoints 4-6)                                60 min
11:50  Readout with the director: checkpoint results, next step        20 min
12:10  Close; take-home lab path and help channel                       5 min
Staffing: 1 instructor + 2 helpers (14 attendees, 1 per 10 rounded up)
```

**Short virtual follow-along**, for the decline menu and the champion-less case:

```
00:00  Goal and success criterion                   5 min
00:05  Concept block                                10 min
00:15  Lab, instructor builds while attendees build 60 min (one helper per breakout room)
01:15  Results, questions, next step                15 min
```

## 4. Lab environment standard

**Default: vendor-provisioned disposable environment.**

- One pre-built, least-privilege, auto-expiring cluster per attendee, with synthetic data.
- It needs no customer review.

Why not the alternatives:

- Attendee trial accounts are kept for the take-home path only. Each sign-up is a failure point at minute zero.
- A shared cluster means one attendee's mistake breaks everyone's lab.
- The customer's own environment is for build-on-your-use-case only, after written agreement from their security team.
- Laptop installs are deleted, because the network and laptop state are unknown.

**Rules for every lab:**

1. Find the slowest provisioning step and schedule from it.
2. Set every environment's time-to-live longer than the session including breaks.
3. Run an automated test of every checkpoint nightly or on each product release, and within 24 hours before each delivery (baseline): setup, check fails, solve, check passes.
4. Keep lab source in a Quarrystone repository, versioned with the product, with one named maintainer per module.
5. Tear down every environment after the session. Give attendees a take-home path in their own account with explicit cleanup steps.

**Pool sizing.** Confirmed attendees plus two spares (baseline). Start provisioning at least 1 hour before.

**Customer network checklist** (ask on the logistics call, answered in writing before the dry run):

- Must attendees be on a corporate VPN, even on site?
- Which outbound domains and ports does the lab need, and are they allowed?
- Do IP allow-lists apply?
- Are laptops managed, with install rights removed?
- Can attendees use a corporate email for outside sign-ups?
- Who on the customer side can fix any of this on the day?

**Security.**

- Attendees get lab-scoped credentials only.
- No customer data in vendor environments without written agreement.
- Never collect attendee credentials for their own systems.

## 5. Delivery and certification ladder

**Staffing.** One instructor plus one helper per started block of 10 attendees, rounded up (baseline). Virtual: one helper per breakout room.

**Who delivers**, efficiency first: SE with helpers > DevRel > certified partner. SEs already own the account context.

**Ladder.** This is this skill's construction. Vendors publish entry gates, not shadow ladders.

1. Run every module alone, end to end, on a fresh environment.
2. Help at one delivery.
3. Co-deliver: lead one module while a certified instructor leads the rest.
4. Lead a full workshop with a certified instructor observing and scoring against the checklist.
5. Certified. Re-run step 1 on every major lab version.

**Rehearsal.** Never walk in with an untested lab. Dry-run on the customer's network, with at least one onsite attendee running the prerequisites live.

**Instructor checklist:**

```
[ ] Ran every module alone on a fresh environment this week
[ ] Automated checkpoint test passed within 24 h of delivery
[ ] Dry run on the customer network with one onsite attendee
[ ] Environment time-to-live longer than the session
[ ] Helpers briefed: attendees type, helpers point
[ ] Lecture blocks under 15 minutes
[ ] Readout slot with the decision maker held
[ ] Teardown scheduled; take-home path and cleanup steps sent
```

**AE role.** The AE owns the opening, the readout, and the next-step conversation with the champion. An AE at the back of the room wastes the one meeting the workshop bought.

**Partners (later).** Apply the same grant rule and next-step agreement. Borrow AWS's gate: partner tier, a practitioner with an active certification, executive sponsorship, and a one-day onboarding before the first customer delivery.

## 6. Per-account workshop brief

```
Account / job / opportunity stage:
Success criterion and next-step agreement: <link>
Attendees: name, role, confirmed (calendar), prerequisites done
Modules and order:          Format:          Environment:
Logistics call date:        Dry run date (customer network):    Automated test date:
Instructor:      Helpers:   AE role: opening, readout, champion conversation
Follow-up owner and date of champion recap:
```

**Pre-workshop sequence.**

1. Logistics call with the champion 2-3 weeks out (baseline). Collect attendee roles, skill levels and prior product exposure, plus the network rules.
2. Publish prerequisites in three parts: prior knowledge, machine and network state, accounts.
3. Confirm attendance by calendar acceptance. Size environments from confirmed attendees plus two spares.
4. Run the dry run on the customer network, and the automated checkpoint test.
5. Brief the AE.

**Next-step agreement.** Write it with the champion before the date is set.

```
Account:                      Workshop date:
Success criterion: <observable, e.g. "3 attendees reach checkpoint 4 with their own schema">
If met:     <POC scope | evaluation plan | architecture review>   Date:   Owner (Quarrystone):   Owner (account):
If not met: <fix cause, re-scope, or stop>                       Decided by:
Agreed by champion: <name, date>      Agreed by AE: <name, date>
```

**After the workshop.**

0. If no next-step agreement exists, agree one with the champion before any other follow-up.
1. Within one business day (baseline), send the champion a recap:

```
Subject: <account> workshop results and next step

Thanks for hosting on <date>. Results:
- Module 1: <x of y> attendees reached checkpoint 3
- Module 2: <x of y> reached checkpoint 6
Success criterion "<criterion>": met / not met
Next step as agreed: <step> on <date>, owners <names>
Attendees keep the lab here: <take-home path>; questions go to <help channel>.
```

2. Attendees get the take-home lab and a help channel. They get technical help, never a sales call or a nurture sequence. The AE talks to the champion and the decision maker.
3. Run the agreed step. If the criterion failed, fix the cause (wrong attendees, broken lab, wrong use case) before offering a second workshop.

## 7. Scorecard

**Per account** (Kirkpatrick's four levels):

| Account | Job | L1 rating | L2 checkpoint completion | L3 active at 30 / 60 days | L4 next step executed in 30 days | Notes |
|---|---|---|---|---|---|---|

- **L1:** the existing end-of-day survey plus one open question. Track the trend only.
- **L2:** from the lab check scripts. Baseline after one quarter.
- **L3:** attendees active in their own trial or production cluster at 30 and 60 days.
- **L4:** agreed next step executed, POC started, or technical win.

**Program row per quarter:**

- Requests, granted, reshaped, declined.
- Show rate against confirmed attendees.
- Lab defect rate (sessions with a checkpoint failing for environment reasons).
- Delivery hours per workshop.
- Next-step execution rate.
- Comparison-group result.

**Log every workshop against its opportunity on the day it is granted,** with attendees linked and the grant decision recorded. No metric above survives without this.

**Comparison.** Compare workshop accounts against matched opportunities without a workshop. Qualified requests deferred for capacity add a few more.

- Workshop accounts are selected for momentum, so raw influenced pipeline overstates the effect.
- Report it as "influenced," never as caused.

**Baselines.**

- The retro-scored 31 are the starting point for the grant-rate and next-step rates.
- Every "baseline" figure in this document is this skill's default.
- Replace each one with Quarrystone's own after one quarter.

## 8. Pass threshold

Review each quarter. The first gated quarter sets the baselines. Apply the threshold from the second quarter. Continue unchanged only if all four hold:

| # | Condition | Fix if it fails |
|---|---|---|
| 1 | Next-step execution rate is at or above the first quarter's rate, pooled over at least 10 workshops (pool quarters if fewer). | Tighten the grant rule. |
| 2 | No live session hits an environment-caused checkpoint failure. Failures the dry run catches count as the test working. | Fix the test rule in Step 4, then the maintainer. |
| 3 | Every instructor in the quarter sits on the certification ladder. | Pause uncertified delivery. |
| 4 | Delivery hours fit the hours named in the interview. | Use the decline menu before cutting rehearsal. |

## What to tell leadership

1. Keep the program for one gated quarter. The 2/31 rate mixes ungated goodwill workshops with real ones, so it can't yet justify a stop.
2. Quarrystone will retro-score the 31 workshops this week and report the qualified subset's result.
3. From next quarter: no workshop without the grant rule, a signed next-step agreement, and a decision maker in the room.
4. The 4.6/5 survey stays as a trend line. It is not a success metric.
5. The vendor lab statistics won't appear in any business case. Quarrystone will build its own baseline and matched comparison.

**Next actions, in order:**

1. Name the sales owner who signs the grant rule.
2. Retro-score the 31 workshops.
3. Run the automated checkpoint test on the current lab to see whether it passes today.
4. Cut the slide block to about 35 minutes and rebuild M1 around script-verifiable checkpoints.