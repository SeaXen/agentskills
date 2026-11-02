# Fennick workshop curriculum: standardised program

## Open decisions (assumed, since I couldn't interview you)

I couldn't ask the interview questions, so each answer below is assumed. Correct any of them and the design changes where noted.

| # | Assumption | If wrong |
|---|---|---|
| 1 | The first job is **technical win in open opportunities** (prospects). | If it's adoption in existing accounts, the grant rule keys on usage and the challenge format moves up. |
| 2 | Requests come from AEs and there's no written grant rule. I have no conversion data. | Run the diagnosis below before you commit to the redesign. |
| 3 | SEs deliver. Their hours are limited, and one week of prep per workshop is the cost to cut. | If hours still don't cover demand, tighten the grant rule before cutting rehearsal. |
| 4 | Attendees can't build on the prospect's own environment. Fennick can provision sandboxes (projects or environments with SDK keys). | If labs need customer data, that moves to build-on-your-use-case with security sign-off. |
| 5 | Workshops are a mix of on-site and virtual. Some prospects run VPNs or managed laptops. | If networks are locked down, delete laptop installs and make the customer-network dry run mandatory. |
| 6 | Each SE keeps their own deck and lab, with no shared repo or maintainer. | If shared modules already exist, start from the best one. |
| 7 | No hard first date. | With a hard date, ship one module and one lab, not the catalog. |

## What's wrong with the current format

- **Three hours of slides before any hands-on is a feature tour.** The skill sets lecture blocks under 15 minutes. In the MongoDB full-day kit, two 90-minute workshop blocks fill about six hours.
- **One big build-from-scratch lab fails in the worst way.** If an attendee stalls at minute 20, everything after it is lost, and the room can't skip ahead. Attendees leave believing the product is hard.
- **A week of prep per workshop is the cost of building each one from zero.** The fix is reusable modules, not faster SEs.
- **Nothing in the current setup ties a workshop to a buying decision.** No grant rule means every request is granted, so every workshop costs a week.

## 1. Grant rule (sign it with a named sales owner before the next request)

**Prospect workshop.** Grant only when all four hold:

1. An open qualified opportunity exists, with a named champion.
2. Discovery named one use case the workshop will prove.
3. A decision maker attends at least the opening or the readout.
4. A next-step agreement is written before the date is set.

If the opportunity is qualified but has no champion, grant only a short virtual follow-along. Its agreed next step is naming the champion.

Everything else gets the decline menu, cheapest first:

1. An existing self-paced lab or tutorial path.
2. A one-hour architecture or office-hours session.
3. A recorded workshop plus a take-home lab.
4. A full workshop.

Requests that fail the rule go to the sales owner, never straight to an SE. Requests beyond the quarter's delivery hours queue by opportunity stage. Apply the rule to every request, including the CEO's.

| Pressure | Answer |
|---|---|
| "A workshop will unblock the stalled deal." | Deals stall on decisions, not skills. |
| "Give the unhappy customer a free day." | A rushed goodwill workshop makes the product look hard. |
| "They want training on everything." | That is paid training, so route it to the education program. |
| "The whole team wants to come." | No champion or decision maker means no next step. |

**If workshops already run:** score last quarter's workshops against this rule, then read POC outcomes on the qualified subset only. Keep the program for one gated quarter if that subset converts, or if too few qualified workshops exist to tell. Stop it if qualified workshops also produce no next step. No independent study of workshop-to-POC conversion exists, so use your own numbers.

## 2. The catalog: modules named by developer problem

Each module is 60–90 minutes. Each one targets one discovery use case and has script-verifiable checkpoints, with a solution state for each checkpoint so a stuck attendee can skip forward. Build backward: the use case, then the evidence a checkpoint shows, then the exercises.

The module titles below are proposals. Replace them with the use cases your discovery notes actually name.

| ID | Title (developer problem) | Proves | Checkpoints (example) |
|---|---|---|---|
| FF-01 | Ship a feature dark and turn it on for 5% of users without a deploy | Decoupling deploy from release | 1 flag created, 2 SDK evaluates it in the starter app, 3 percentage rollout verified |
| FF-02 | Target a feature to one customer segment, then roll it back in under a minute | Targeting and kill switch | 1 segment rule, 2 verified for in and out users, 3 rollback verified |
| FF-03 | Run an experiment and read the result | Experimentation | 1 variant assignment, 2 metric event received, 3 result read |
| FF-04 | Control flags from CI/CD and approvals without breaking prod | Governance, enterprise workflow | 1 flag change via API or CLI, 2 approval gate, 3 audit log entry found |
| FF-05 | Keep flags from rotting: find and remove stale ones | Lifecycle and tech debt | 1 stale flag found, 2 cleanup PR, 3 check passes |
| FF-06 | Evaluate flags in your stack (one variant per supported SDK or language) | Fit to the prospect's stack | Same checkpoints as FF-01 in the prospect's language |

**Module rules:**

- Don't use a module for a feature tour. "Introduction to Fennick: features and architecture" is the bad example.
- Build a new module only when two or more qualified accounts need the same missing use case.
- Every module uses one shared starter app, so attendees never build a demo app from scratch. Sample-app guidance is in `samber/developer-platform-skills@sample-app-strategy`.
- Keep the lab source in your own repository, versioned with the product, with one named maintainer per module.

## 3. Standard formats

Default to the **guided lab half-day**. The goal is for most workshops to be a different pick of modules, not a different deck.

| Format | When | Prep (baseline, once modules exist) |
|---|---|---|
| Short virtual follow-along (90–120 min, one module) | No champion yet, or adoption nudges | About 1 day |
| **Guided lab half-day (default)** | Qualified prospect with a named use case | 2–3 days |
| Build-on-your-use-case | Written evaluation plan, and the champion has cleared the data question | A week or more, plus the customer's review wait |
| Full day with executive session | Large deal that needs a roadmap or architecture readout | About a week |

Cap any workshop at one day of delivery. Anything longer is paid training or services.

**Default half-day agenda** (14 attendees, champion plus a director):

```
09:00  Welcome, goal of the day, success criterion (champion + SE)      10 min
09:10  Problem framing: the use case in their words                     10 min
09:20  Module A - lab (checkpoints 1-3)                                 60 min
10:20  Break                                                            15 min
10:35  Debrief module A, one concept block under 15 min                 15 min
10:50  Module B - lab (checkpoints 4-6)                                 60 min
11:50  Readout with the decision maker: checkpoint results, next step   20 min
12:10  Close; take-home lab path and help channel                        5 min
```

**What this replaces:**

- The morning slide block is gone. Concepts come in short blocks between labs.
- The one big afternoon lab becomes two or three modules with checkpoints.
- Architecture content goes into the 20-minute readout, or into a separate one-hour session for decision makers.

The full-day format stays available only for the executive-session case. If an AE asks for a full day, the answer is the half-day plus an architecture session.

## 4. Lab environment standard

1. **Default to a vendor-provisioned disposable environment.** One per attendee, pre-built with the starter app, least-privilege, and auto-expiring. This kills sign-ups and installs at minute zero.
2. **Size it from confirmed attendees plus two spares.**
3. **Set the time-to-live longer than the whole session, including breaks.**
4. **Test automatically.** For every checkpoint run setup, run the check (it must fail), run the solution, then run the check (it must pass). Do this nightly or on each product release, and again within 24 hours before each delivery.
5. **Tear down every environment after the session.** Give attendees a take-home path in their own account with explicit cleanup steps.
6. **Use synthetic data.** Never put customer data in a vendor environment without written agreement, and never collect attendee credentials for their own systems.
7. **Dry-run on the customer's network** with at least one on-site attendee running the prerequisites live. Ask in the logistics call about VPN, allowed outbound domains and ports, managed laptops, and who can fix any of it on the day.

If the starter app needs a safe place to break things, see `samber/developer-platform-skills@api-test-mode-design`.

## 5. Delivery and certification

- **Staffing:** one instructor plus one helper per started block of 10 attendees, rounded up. Add one helper per breakout room for virtual sessions. Attendees type and helpers point.
- **Order of delivery:** SE with helpers first, then the education team, then certified partners.
- **Certification ladder** (this skill's construction, not a vendor standard):
  1. Run every module alone on a fresh environment.
  2. Help at one delivery.
  3. Co-deliver by leading one module.
  4. Lead a full workshop while a certified instructor observes and scores.
  5. Certified. Re-run step 1 on every major lab version.
- **Rehearsal is mandatory.** Nobody delivers an untested lab.
- **AE role:** the opening, the readout, and the next-step conversation with the champion. An AE at the back of the room wastes the meeting the workshop bought.

## 6. Per-workshop brief and next-step agreement

Before the date is set, write the next-step agreement with the champion:

```
Account:                       Workshop date:
Success criterion: <observable, e.g. "3 attendees reach checkpoint 4
                    with their own flag targeting rule">
If met:     <step: POC scope / evaluation plan / team rollout>
            Date:     Owner (Fennick):     Owner (account):
If not met: <fix cause, re-scope, or stop>
Agreed by champion: <name, date>     Agreed by AE: <name, date>
```

Brief per workshop:

```
Account / job / opportunity stage:
Success criterion and next-step agreement: <link>
Attendees: name, role, skill level, confirmed (calendar), prerequisites done
Modules and order:            Format:            Environment:
Logistics call (2-3 weeks out):   Customer-network dry run:   Automated test:
Instructor:      Helpers:         AE role: opening, readout, champion conversation
Champion recap owner and date (within 1 business day):
```

Use the attendee roles and skill levels to pick the modules. After the workshop:

1. Send the champion the checkpoint results, the criterion outcome and the agreed step within one business day.
2. Give attendees the take-home lab and a help channel. They get technical help, not a sales call.
3. If the criterion failed, fix the cause (wrong attendees, broken lab, wrong use case) before offering a second workshop.

## 7. Scorecard

Measure per account on four levels:

| Level | Signal |
|---|---|
| 1 Reaction | End-of-day rating and one open question |
| 2 Learning | Checkpoint completion per module, from the check scripts |
| 3 Behaviour | Attendees active in their own trial or production account at 30 and 60 days |
| 4 Results | Agreed next step executed within 30 days, POC started, technical win |

**Program row per quarter:**

- Requests, and how many were granted, reshaped or declined.
- Show rate against confirmed attendees.
- Lab defect rate: sessions where a checkpoint failed for environment reasons.
- Delivery hours per workshop.
- Next-step execution rate.
- Comparison against matched opportunities with no workshop.

Report influenced pipeline as influenced, never as caused, because workshop accounts are selected for momentum. Log every workshop against its opportunity the day it's granted, with attendees linked and the grant decision recorded.

**Pass threshold.** The first gated quarter sets the baselines, and the threshold applies from the second. Continue unchanged only if all four hold:

1. Next-step execution rate holds at or above the first quarter's, pooled over at least 10 workshops.
2. No live session hits an environment-caused checkpoint failure.
3. Every instructor sits on the certification ladder.
4. Delivery hours fit the hours you have.

I did not use the circulating figures on lab-to-trial lift, workshop pipeline lift or hands-on ROI. They trace to lab-platform vendors' marketing, with no independent study. Don't put them in your business case. Use your own baseline.

## Rollout plan (ordered)

1. **Week 1:** Collect the last 2–4 quarters of SE decks and labs. Identify the two or three use cases that recur. Get the grant rule signed by the sales owner.
2. **Weeks 2–4:** Build FF-01 and FF-02 on one shared starter app, with check scripts and solution states, in a repository with a named maintainer. Build the provisioned environment.
3. **Weeks 4–5:** Certify two SEs by running the ladder on those modules, then use the next qualified request as the pilot.
4. **After the pilot:** Add modules only when two qualified accounts need the same missing use case.

Doing this raises the up-front cost, because the first modules take a week or more each to build. After that, a standard half-day should drop to the 2–3 days per workshop the skill estimates. These are order-of-magnitude baselines, so replace them with your measured hours after one quarter.

## Decisions for you

1. Confirm the assumed answers above, especially #1 (prospects first) and #4 (can you provision sandboxes).
2. Name the sales owner who will sign the grant rule.
3. Share last quarter's workshop list, so I can run the diagnosis against the grant rule before you lock the design.

I haven't checked this against any Fennick data. The module titles and checkpoints are illustrative until your discovery notes confirm which use cases recur.