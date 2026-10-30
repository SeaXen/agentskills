# Charter, rotation and write-up templates

## Contents

1. Program charter
2. Rotation calendar
3. Session write-up
4. Session log and pilot review, healthy and failing

## 1. Program charter

One page. Settle these before the first session, so they are not re-argued every week.

```
Program:        [name]
Job:            [one primary job: unblock users | surface docs gaps | product signal | contributor growth]
Audience:       [who, which products, which skill level]
Format:         [async thread | drop-in call | livestream | booked slots | staffed queue] + async intake
Slot:           [day, time in audience time zone, cadence]; second slot trigger: [region] ≥ 25% of users
Staffing:       Host [name], backup host [name]; engineer rotation [names], cap [sessions/month each]
Scope card:     [link]
Recording:      [policy, where published, retention]; reviewed before publishing by [name]
Outputs:        Write-up within 2 business days; docs tickets; feedback records
Pilot:          [start date] to [review date], [N] sessions
Demand bar:     [job metric: askers per cycle | first merged contributions], [docs fixes + feedback records per 2 sessions]; below it -> [fallback format]
Operating bar:  no silent cancellation, no engineer over [cap], write-ups on time in all but one session
```

## 2. Rotation calendar

Book a quarter ahead, with manager sign-off for every engineer. The cap is the promise that keeps them on it.

| Date   | Engineer        | Area             | Backup | Prep brief sent | Confirmed |
| ------ | --------------- | ---------------- | ------ | --------------- | --------- |
| Thu 6  | A. (controller) | upgrades, CRDs   | B.     | Tue 4           | yes       |
| Thu 13 | C. (storage)    | volumes, backups | A.     | Tue 11          | yes       |
| Thu 20 | B. (API)        | webhooks, RBAC   | C.     | -               | pending   |

The prep brief carries the pre-submitted live questions and the scope card. An engineer who reads the questions two days ahead answers better, which is the reason Kubernetes gave for asking users to submit in advance.

## 3. Session write-up

Publish within 2 business days (baseline) where the intake thread lives. This is the artifact absent users get, and the proof of value for the next announcement.

```
## [Program] - [date], with [engineer], [area]

### Answered
- **[Question, in the asker's words]** - [answer in 2-4 lines] - [docs link or new docs ticket]

### Answered here, not live
- **[Question]** - [answer]

### Redirected
- [Topic] → [destination]. (No names.)

### Logged for the product team
- [Request or bug, in the user's words] → [feedback record / issue link]

### Docs we are fixing
- [Page] - [what was missing] - [ticket]

Next session: [date, time in audience zone, calendar link]. Submit questions: [link].
```

## 4. Session log and pilot review, healthy and failing

Columns per session: date, held or cancelled, distinct non-staff askers (live or async), questions answered live, answered async, redirected, docs tickets opened, docs fixes merged, feedback records, engineer present, write-up published (days).

**Healthy pilot, 8 sessions:**

| Signal                  | Value        | Read                                           |
| ----------------------- | ------------ | ---------------------------------------------- |
| Sessions held / planned | 8 / 8        | Rotation holds                                 |
| Median distinct askers  | 5            | Above the demand bar of 3                      |
| Askers who came back    | 3 of 22      | Most users come once with one question; normal |
| Docs fixes merged       | 6            | Above 1 per 2 sessions                         |
| Feedback records        | 4            | Product heard it                               |
| Write-up lag            | median 1 day | Absent users served                            |

Verdict: continue. Re-run the time-zone split, then decide on a second slot.

**Failing pilot, 8 sessions:**

| Signal                  | Value            | Read                                                                |
| ----------------------- | ---------------- | ------------------------------------------------------------------- |
| Sessions held / planned | 6 / 8            | Two silent cancellations: engineer absent, no backup                |
| Median distinct askers  | 1                | Below the bar                                                       |
| Docs fixes merged       | 0                | Questions answered, nothing changed; same three questions came back |
| Write-up lag            | 2 of 6 published | Absent users got nothing                                            |

Verdict: stop the live session. Run an async thread for a quarter with the same rotation, publish the three repeat answers as docs, and re-test demand before going live again. The stop rests on the demand bar: one asker per session and no docs fix. The operating fixes - a named spare engineer, write-ups on time - come with the async quarter, so the re-test is fair.
