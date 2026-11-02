# Charter: Hollowmere "First Flag" developer sessions

**Owner:** Priya (DevRel lead) · **Status:** Draft for Marketing review · **Date:** 2026-10-23

## 1. Decision needed from Marketing

**Weekly 60-minute webinars are not feasible with this team.** Here is the capacity math.

| Resource | Hours per month |
|---|---|
| Priya | 6 |
| Second advocate | 6 |
| 3 backend engineers (2h each) | 6 |
| **Total** | **18** |

- A weekly webinar means about 4 to 5 live hours a month.
- Prep, promotion, follow-up and the demo environment typically triple that. The total is about 15 to 20 hours a month, which is the entire budget with nothing left for travel season, v3 docs or support.
- The likely outcome is a decaying series: thin sessions, falling attendance, and a quiet stop around week 6.

**Proposal:** two live sessions a month, plus an always-available replay. Every week still has a v3 touchpoint, because a replay or clip goes out on the off weeks. Marketing gets a steady cadence of assets without a promise we can't keep.

**Options if Marketing insists on weekly:**
1. Add budget for a contractor or host. This is the only option that keeps quality.
2. Run weekly sessions that are only a replay watch party. This costs almost no live hours but gives weak conversion.
3. Run weekly for 4 weeks around launch, then drop to biweekly. This burns 16 hours or more in month one. It is only safe if travel season really starts after launch month.

## 2. Goal and one metric

**Goal:** new signups create their first flag.

**Primary metric:** the share of new signups who attend (live or replay) and create a first flag within 7 days, compared with signups who didn't attend.

- Registrations, attendance and replay views are tracked but never reported as success.
- **Baseline first:** pull the current signup → first-flag rate and time-to-first-flag before session 1. Set the target after session 2, once there is real data. I won't invent a number now.
- **Self-reported source:** add "heard about us at a session" to signup or onboarding.
- **Success test for the series:** after 3 sessions, attendees' first-flag rate is clearly above the baseline. If it isn't, change the format or stop. Don't add more sessions.

## 3. Format

**A follow-along workshop, not a presentation.** Title: "Ship your first feature flag in 20 minutes."

| Segment | Minutes | Content |
|---|---|---|
| Setup | 5 | Free account, API key, starter repo |
| Create the flag | 15 | Attendees create a flag live while the host does it |
| Targeting and rollout | 15 | One v3 feature in a realistic use case |
| Q&A | 10 to 15 | Engineer answers |
| CTA | 5 | Invite teammates (the free tier allows 5 seats), links to docs |

- **Length:** 60 minutes at launch, then test 45.
- **Fixed template:** the same structure every time. Only the use case and the v3 feature change. This is what keeps prep low.
- **Starter repo:** a maintained sample project in 2 or 3 languages. Pick the languages by top SDK usage.
- **Recording:** record every session. The replay is the durable asset, with a 10-minute "first flag" cut as the evergreen onboarding clip.

## 4. Schedule and time zones

- **Slot:** 11:00 ET / 08:00 PT / 17:00 CET. It covers North America (60%) and Europe (30%) in working hours.
- **Not served live:** the "elsewhere" 10%. Send them the replay within 24 hours and include a note in the invite.
- **Cadence:** the 2nd and 4th Thursday of each month.
- **Off weeks:** a replay clip or a short written v3 tip in the newsletter and community.
- **Later test:** rotate one session a quarter to a Europe-friendly slot if Europe signups underperform.

## 5. Roles and hours per session

| Who | Does | Hours per session |
|---|---|---|
| Lead advocate (rotates between Priya and the second advocate) | Host, demo, run-of-show | about 3 |
| Other advocate | Chat moderation, follow-up email | about 1 |
| One engineer (rotates) | Co-host, answers deep questions, 30-minute rehearsal | 1.5 |
| Marketing | Registration page, promotion, email sends, CRM tagging | 0 DevRel hours |

**Monthly totals for 2 sessions:**

| Group | Hours | Budget | Left over |
|---|---|---|---|
| Advocates | about 8 | 12 | 4 |
| Engineers | about 3 | 6 | 3 |

The advocates' 4 spare hours cover replay clipping, the monthly report and slippage. The engineers' 3 spare hours cover starter repo maintenance. Don't schedule new work into the spare hours.

## 6. Marketing's part

- Registration page, promotion and reminder emails: 1 week out, 1 day out, 1 hour out.
- Follow-up to attendees within 24 hours. The first email carries the replay and a link to the exact "create your first flag" step. Non-attendees get the replay with the same link.
- Tag registrants and attendees in the CRM and product analytics so the primary metric can be computed.
- Promote only to new signups and trial users first. They are the target. Broader promotion is secondary.

## 7. Timeline (3 weeks to launch)

| When | What |
|---|---|
| Week 1 | Pull baseline. Lock the template and starter repos. Marketing builds the registration page. Pick the launch use case. |
| Week 2 | Full dry run with the engineer co-host. Fix every friction point in the starter repo. Start promotion. |
| Week 3 | Launch week: session 1 with v3. Send follow-up within 24 hours. Review chat questions for docs gaps. |
| Week 4 | Session 2. Retro, then set the target using real data. |

## 8. Risks and stop rules

- **Travel season:** advocate time drops to 6 hours each. Pre-record the evergreen workshop in week 2 so a session can run as a replay with live chat if a host is away.
- **Engineer time:** if the 2-hour allowance is cut, sessions run advocate-only with Q&A answers posted afterward.
- **Low attendance:** under 15 live attendees on two sessions in a row means we fix promotion or topic before running a third, not add sessions.
- **No lift:** if attendees' first-flag rate is not above the baseline after 3 sessions, pause the series and review the format.
- **Live demo failure:** the pre-recorded fallback and a working starter repo are mandatory. Rehearse every session.
- **Scope creep:** v3 deep dives, customer panels or guest speakers need a separate decision and separate hours.

## 9. Review

Retro after session 2 and again after session 4, covering the primary metric, hours used against the budget above, and whether to keep, shrink or stop the series.

## 10. Questions for you

1. Can I get the baseline signup → first-flag data this week?
2. Which SDK languages should the starter repo cover first?
3. Does travel season start before or after the v3 launch month?