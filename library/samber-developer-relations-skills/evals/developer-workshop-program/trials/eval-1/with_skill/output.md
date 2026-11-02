**Next action (10 min):** send the VP the message in section 5. Do it before building anything. The day only runs if Brightwell names an owner and a decision maker by Monday noon.

I read the SKILL.md and both references. Your request covers one workshop, so this has the grant decision, the reshaped agenda, the brief and the scorecard.

## 0. Assumptions (open decisions, none confirmed)

1. Job is adoption and retention, because the account is a renewal. Rank adoption formats first.
2. Pelorus has existing catalog modules and vendor-provisioned disposable clusters. If not, fall back to section 7.
3. Brightwell owns no usage gap I can name yet. Two incidents are the only known context.
4. "Next Tuesday" is Nov 3, three days out. Nov 10 is better.
5. No Brightwell laptop or VPN facts are known.
6. A second person (another SE, support or on-call engineer) can be borrowed for the morning.

## 1. Grant decision: reshape, do not grant as asked

Rule for a customer adoption workshop: a named customer-side owner, a targeted usage gap, and a next step measured in usage.

| Check | Status |
|---|---|
| Named Brightwell owner (champion) | ❌ none |
| Usage gap targeted | ❌ none named. The incidents are not a usage gap |
| Next step measured in usage, agreed before date | ❌ none |
| Decision maker at opening or readout | ❌ CTO declines |
| Scope fits one day of delivery | ❌ "everything" is paid training or services |
| Staffing: 25 attendees need 1 instructor + 3 helpers | ❌ you have 1 SE |

As asked, this is the failure mode "Goodwill workshop": granted to soothe a renewal, no champion, no next step. A workshop cannot fix two incidents. Teaching 25 people "everything" in a hurry also leaves them thinking the product is hard.

**Reshape to:**

- **Morning:** guided lab half-day, 10 attendees, one use case.
- **Afternoon:** 60-minute architecture and operations session for all 25. It has no labs, so the helper ratio does not apply.

This is the decline-menu path: a half-day lab plus a one-hour architecture session instead of the full day.

**Gate:** the morning runs only if every item below is done by Monday noon.

1. Brightwell names a platform-team owner. Call them the champion.
2. That owner names one use case, ideally tied to the incidents.
3. A decision maker attends the 20-minute readout. The CTO is not needed. A VP Eng or head of platform who signs off the technical renewal works.
4. The next-step agreement in section 4 is signed by the champion and your AE.
5. A second person is confirmed for the morning.

If any item is missing, run the afternoon session only and move the lab. The afternoon session is the one-hour architecture session from the decline menu.

## 2. Agenda

### Morning: guided lab half-day, 10 attendees, 1 instructor + 1 helper

```
09:00  Welcome, goal of the day, success criterion (Brightwell owner + SE)    10 min
09:10  Incident follow-up: what changed since the two incidents,               10 min
       what today covers and does not (AE + Brightwell owner)
09:20  Problem framing: the use case in their words                             10 min
09:30  Module 1 - lab (checkpoints 1-3)                                        60 min
10:30  Break                                                                   15 min
10:45  Debrief module 1, 10-minute concept block                               15 min
11:00  Module 2 - lab (checkpoints 4-6)                                        60 min
12:00  Readout with decision maker: checkpoint results, next step              20 min
12:20  Close: take-home lab path and help channel                               5 min
12:25  End. Lunch.
```

Module rules:

- Module titles name the developer's problem. Example: "Detect and recover from a stalled consumer group within 5 minutes."
- Pick the two catalog modules closest to the incident use cases. Build no new module in 3 days.
- Each checkpoint is script-verified and ships a solution state.
- Lecture blocks stay under 15 minutes. Attendees type, helpers point.

### Afternoon: architecture and operations session, all 25, SE alone

```
13:30  Reference architecture for their workload                  20 min
13:50  Operating it: failure modes, alerts, runbooks              25 min
14:15  Open Q&A led by their questions, collected the day before  20 min
14:35  Take-home path and help channel                            10 min
14:45  End
```

This is a talk plus Q&A, not a workshop. It answers "whole team gets time" without a 4-person staffing need.

## 3. Lab environment and logistics

1. Use vendor-provisioned disposable clusters, one per attendee. Size is 10 confirmed attendees + 2 spares. Install nothing on laptops.
2. Find the slowest provisioning step and schedule from it.
3. Set time-to-live longer than the session, breaks included.
4. Run the automated checkpoint test (setup, check fails, solve, check passes) within 24 hours before delivery.
5. Network checklist, answered in writing before the dry run:
   - Corporate VPN required on site?
   - Are outbound broker endpoints and ports allowed?
   - Do IP allow-lists apply?
   - Are laptops managed?
   - Who can fix any of this on the day?
6. Dry run: with 3 days' notice you cannot do the full network dry run. Get the champion or one attendee to run prerequisites and module 1 on Brightwell's network Monday, on a call with you. Skip the dry run and you risk the failure mode "Lab dies at minute zero".
7. Use synthetic data only. Brightwell data stays out of Pelorus environments.
8. Tear down all environments after the session. Send take-home steps with cleanup instructions.

## 4. Workshop brief and next-step agreement

```
Account: Brightwell Logistics     Job: adoption / renewal     Renewal: ~6 weeks (about 2026-12-12)
Workshop date: Tue <Nov 3 or Nov 10>     Format: guided lab half-day + architecture session
Champion: <name, role> (required)         Decision maker at readout: <name, role> (required)
Attendees (lab): 10, name / role / confirmed by calendar / prerequisites done
Attendees (afternoon): up to 25
Modules and order: <M1 ids>, <M2 id>      Environment: vendor-provisioned
Logistics call: <date>   Network check with champion: Mon   Automated test: <date, within 24h>
Instructor: you          Helper: <name>
AE role: opening, readout, champion conversation. Not at the back of the room.
Follow-up owner and date of champion recap: <SE>, within 1 business day
```

**Next-step agreement** (propose it to the champion, then sign):

```
Success criterion: at least 6 of 10 lab attendees reach checkpoint 4 on their own     [baseline]
If met:     <usage step, e.g. second team onboarded or runbook adopted>  Date: <within 30 days>
            Owner (Pelorus): <SE/CSM>   Owner (Brightwell): <champion>
If not met: fix the cause (wrong attendees, broken lab, wrong use case) before any second workshop
Agreed by champion: <name, date>     Agreed by AE: <name, date>
```

The 6 of 10 figure is a baseline set by this skill. Replace it with your own figure after one quarter.

## 5. Message to the VP of Sales (send today)

> Brightwell workshop is on, in a shape that can work. We can't run a 25-person "everything" day with one SE. It would end with no next step and could hurt the renewal.
>
> Plan: morning hands-on lab for 10 people on the use case behind their incidents. Afternoon architecture and operations session for the whole team of 25.
>
> I need three things from you by Monday noon:
> 1. A named Brightwell owner for the day.
> 2. A decision maker for a 20-minute readout. The CTO is not needed.
> 3. A second Pelorus person for the morning. I can't run labs for 10 alone.
>
> If these aren't confirmed, I run only the afternoon session and we book the lab once they are.
>
> Also: I'd like Nov 10 over Nov 3, so we can test the lab on their network. Renewal is still about 4 weeks away.

"Covering everything" is paid training or services. Route that to your education program, not to this day.

## 6. Scorecard

| Account | Job | L1 rating | L2 checkpoint completion | L3 active at 30 / 60 days | L4 next step executed in 30 days | Notes |
|---|---|---|---|---|---|---|
| Brightwell | adoption / renewal | end-of-day rating + 1 open question | M1 cp3: x of 10; M2 cp6: x of 10 | attendees active in their own account | step from section 4 | log against the renewal opportunity today |

Program-row notes:

- Log the workshop against the opportunity on the day it is granted, with attendees linked and the grant decision recorded.
- Report outcome as influenced, never caused. A renewal at risk is a selected-for-momentum account.
- Read first-quarter baselines for next-step execution rate, show rate, lab defect rate and delivery hours.
- Send the champion recap within 1 business day: checkpoint results, criterion met or not, agreed step and date.
- Attendees get technical help only. The AE talks to the champion and the decision maker.

## 7. Fallbacks

- **No lab modules close to the incident use cases:** drop the morning lab. Run the architecture session plus a 1-hour incident-prevention review with the champion. Book the lab after a use case is named.
- **No second person:** cap the lab at one instructor only if you accept the risk of a stuck room. Otherwise move the lab and run the afternoon only.
- **Network blocked on the day:** pivot the morning to an instructor-led walkthrough on shared screen. Send the lab path as take-home.

**Next:** paste section 5 to the VP now, and ask him which Brightwell contact owns the platform team.