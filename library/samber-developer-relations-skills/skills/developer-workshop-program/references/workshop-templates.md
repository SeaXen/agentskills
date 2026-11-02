# Workshop program templates

## Contents

- Grant rule
- Workshop request form
- Catalog entry
- Agenda: guided lab half-day
- Agenda: short virtual follow-along
- Next-step agreement
- Workshop brief
- Champion recap
- Instructor checklist
- Scorecard

## Grant rule

```
Grant rule - <company> account workshops        Signed: <sales owner>, <DevRel/SE owner>, <date>

Prospect workshop - grant only when all hold:
  [ ] Open qualified opportunity: <CRM stage or later>
  [ ] Named champion: <name, role>
  [ ] Discovery names one use case: <use case> -> catalog module(s): <ids>
  [ ] Decision maker attends opening or readout: <name, role>
  [ ] Next-step agreement written before the date is set

Customer adoption workshop - grant when all hold:
  [ ] Named customer-side owner: <name, role>
  [ ] Usage gap targeted: <feature unused / team not onboarded / ...>
  [ ] Next step measured in usage: <signal, date>

Otherwise offer, in this order:
  1. Self-paced lab or tutorial path: <link>
  2. One-hour architecture or office-hours session
  3. Recorded workshop plus take-home lab
Escalation: requests that fail the rule go to <sales owner>, never straight to an SE.
Capacity: <N> delivery hours per quarter; requests beyond it queue by opportunity stage.
```

## Workshop request form

```
Account / opportunity:            Requested by:            Wanted date:
Job: technical win | adoption     Opportunity stage:        Champion:
Use case from discovery (one sentence):
Attendees expected (roles, count):    Decision maker attending? yes/no, which segment
Environment constraints (VPN, managed laptops, data):
Proposed next step if the workshop succeeds:
Grant decision: grant | reshape (to: ...) | decline (alternative: ...)   Decided by / date:
```

## Catalog entry

```
Module id / title (developer problem):
Use cases it proves:
Format(s): guided lab | follow-along | challenge | build-on-your-use-case
Length: 60-90 min        Prerequisites: knowledge / machine and network / accounts
Checkpoints (script-verifiable): 1 ... 2 ... 3 ...
Solution states shipped per checkpoint: yes/no
Environment: provisioned | trial | shared | customer
Slowest provisioning step and lead time:
Maintainer:            Last automated test pass:            Product version:
```

## Agenda: guided lab half-day

Input: prospect, use case "ingest events and query them", 14 engineers, champion plus a director attending.

Output:

```
09:00  Welcome, goal of the day, success criterion (champion + SE)          10 min
09:10  Problem framing: the use case in their words                         10 min
09:20  Module 1 - lab (checkpoints 1-3)                                     60 min
10:20  Break                                                                15 min
10:35  Debrief module 1, 10-minute concept block                            15 min
10:50  Module 2 - lab (checkpoints 4-6)                                     60 min
11:50  Readout with the director: checkpoint results, next step             20 min
12:10  Close; take-home lab path and help channel                           5 min
Staffing: 1 instructor + 2 helpers (14 attendees, ~1 per 10, rounded up)
```

## Agenda: short virtual follow-along

```
00:00  Goal and success criterion                    5 min
00:05  Concept block                                 10 min
00:15  Lab, instructor builds while attendees build  60 min (helpers in breakout rooms, one each)
01:15  Results, questions, next step                 15 min
```

## Next-step agreement

```
Account:                       Workshop date:
Success criterion: <observable, e.g. "3 attendees reach checkpoint 4 with their own schema">
If met:     <step>             Date:          Owner (vendor):          Owner (account):
If not met: <step: fix cause, re-scope, or stop>   Decided by:
Agreed by champion: <name, date>      Agreed by AE: <name, date>
```

## Workshop brief

```
Account / job / opportunity stage:
Success criterion and next-step agreement: <link>
Attendees: name, role, confirmed (calendar), prerequisites done
Modules and order:              Format:              Environment:
Logistics call date:            Dry run date (customer network):    Automated test date:
Instructor:      Helpers:       AE role: opening, readout, champion conversation
Follow-up owner and date of champion recap:
```

## Champion recap

```
Subject: <account> workshop results and next step

Thanks for hosting on <date>. Results:
- Module 1: <x of y> attendees reached checkpoint 3
- Module 2: <x of y> reached checkpoint 6
Success criterion "<criterion>": met / not met
Next step as agreed: <step> on <date>, owners <names>
Attendees keep the lab here: <take-home path>; questions go to <help channel>.
```

## Instructor checklist

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

## Scorecard

| Account | Job | L1 rating | L2 checkpoint completion | L3 active at 30 / 60 days | L4 next step executed in 30 days | Notes |
| ------- | --- | --------- | ------------------------ | ------------------------- | -------------------------------- | ----- |

Program row per quarter: requests, granted, reshaped, declined; show rate vs confirmed; lab defect sessions; delivery hours per workshop; next-step execution rate; comparison group result.
