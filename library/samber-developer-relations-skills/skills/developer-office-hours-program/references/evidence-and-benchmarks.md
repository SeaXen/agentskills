# Evidence and benchmarks

Every figure the skill uses, with its source or its baseline label. Quote sourced figures with the source attached. Call baselines "our target", never "the industry standard".

## Contents

1. Sourced figures and practices
2. Baselines set by this skill
3. What no one publishes

## 1. Sourced figures and practices

| Figure or practice                                                                                                                                                                                            | Source                                                                                          | Kind                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------------- |
| Volunteer commitment capped at 1 hour per month per developer; a rotating panel shares the load                                                                                                               | Kubernetes blog, "Expanding User Support with Office Hours", Castro and Dmitichenko, March 2018 | Staffing design        |
| Two editions per month: 14:00 UTC (Europe) and 21:00 UTC (Americas)                                                                                                                                           | Kubernetes Office Hours announcements                                                           | Time-zone pattern      |
| Questions collected all week in a chat channel and a forum thread; "If you post a question in advance, you might get better answers"                                                                          | Kubernetes blog, March 2018                                                                     | Intake                 |
| Panel "doesn't have access to your cluster, so live debugging is off topic"                                                                                                                                   | Kubernetes Office Hours run sheet                                                               | Scope rule             |
| Employers donating engineering time thanked by name in the launch post and episode outros                                                                                                                     | Kubernetes blog, March 2018                                                                     | Engineer retention     |
| Western edition "on hiatus" (January 2020), an edition cancelled "due to panelist time conflicts"; announcements stop after March 2021                                                                        | discuss.kubernetes.io announcements                                                             | Failure pattern        |
| "We answer at least 10 questions per session and have helped 500+ people to date"                                                                                                                             | Kubernetes blog, Meet Our Contributors, Paris Pittman, July 2018                                | Self-reported activity |
| 65 episodes over 3 years                                                                                                                                                                                      | "Lessons Learned from 3 years of Kubernetes Office Hours", Kubernetes Office Hours team, 2020   | Output count           |
| The 1:1 Hour mentoring format discontinued; pairs spent the hour choosing tools, "mentors need a script/instructions"                                                                                         | kubernetes/community mentoring index and tracking issue                                         | Failure pattern        |
| Staff join a question thread "within 15 minutes" during open hours, Monday 04:00 UTC to Friday 21:00 UTC; thread read-only once solved                                                                        | Stripe docs, Discord developer help                                                             | Service commitment     |
| Valid: unexpected API error, webhook not working, how to build a flow. Invalid: how to do X in the dashboard, why a payment was declined, when a payout arrives. Private account issues go to support; no DMs | Stripe docs, Discord developer help                                                             | Scope rule             |
| Asker must be "comfortable having the conversation in public"                                                                                                                                                 | Stripe docs, Discord developer help                                                             | Consent pattern        |
| "The meeting will be canceled if there are no questions"; answers timeboxed to 4 minutes or less; rotating notetaker and timekeeper; 25-minute blocks, biweekly                                               | GitLab handbook, Commercial Solutions Architect Office Hours (internal audience)                | Session control        |
| "If you have a demo environment, revoke all tokens after recording videos"                                                                                                                                    | GitLab docs, token overview                                                                     | Credential hygiene     |
| Regular sessions recorded, "bonus" sessions not                                                                                                                                                               | kOps office hours page                                                                          | Tiered recording       |
| Recording stopped so participants can speak freely                                                                                                                                                            | Real Python office hours                                                                        | Tiered recording       |
| Weekly drop-in, no agenda or invitation needed; at least one board member attends                                                                                                                             | Django Software Foundation board office hours                                                   | Format                 |
| A weekly bookable 30-minute slot "had not been used much", folded into the biweekly meeting                                                                                                                   | Python Steering Council, discuss.python.org                                                     | Demand adaptation      |
| Weekly internal 30-minute meeting on curated community issues, one engineering squad invited per week, agenda two days ahead                                                                                  | Grafana community support squad                                                                 | Docs and feedback loop |
| "Office Hours" label on resulting issues and merge requests                                                                                                                                                   | GitLab                                                                                          | Traceability           |
| Discontinued in November 2023 "due to fiscal constraints"                                                                                                                                                     | Creative Commons                                                                                | Shutdown cause         |

## 2. Baselines set by this skill

| Baseline                             | Value                                                                                                                                 | Replace with              |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Demand gate                          | 5 questions from the last month that docs did not answer, nameable today                                                              | Your own channel count    |
| Pilot length                         | At least 6 sessions: one quarter for weekly or biweekly, two quarters for monthly                                                     | -                         |
| Engineer cap                         | One session per engineer per month, about 75 minutes with prep and pre-check                                                          | Your rotation's real load |
| Second slot trigger                  | Another region at or above 25% of active users                                                                                        | Your own analytics split  |
| Cancel cutoff, livestream panel only | No pre-submitted question 24 hours before the session                                                                                 | Your own lead time        |
| Write-up deadline                    | 2 business days after the session                                                                                                     | -                         |
| Repeat-question rule                 | Same question family seen twice, in a session or any channel, opens one docs ticket                                                   | -                         |
| Default demand bar                   | Median 3 or more distinct non-staff askers per cycle, live or async, and at least 1 merged docs fix or feedback record per 2 sessions | The charter's own bar     |
| Operating bar                        | No silent cancellation, no engineer over the cap, write-ups on time in all but one session                                            | -                         |
| Cycle timeline                       | Intake nudge 72 h before, triage and prep brief 48 h before, cancel check 24 h before                                                 | Your own lead times       |

## 3. What no one publishes

- No organization publishes unique attendees, repeat-attendance rate, deflection rate, docs changes per session, or measured time-to-answer for office hours. Stripe publishes a response commitment, not a measured result.
- No program publishes a GDPR recording notice, lawful-basis statement or retention policy for office hours. Legal review owns that wording.
- Any attendance target is therefore self-set. Say so when presenting one.
