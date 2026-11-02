# DevForge post-event survey and send plan

## When to send

Don't rely on a single email. Intent is highest tomorrow and fades within days, so you need two touchpoints. Your main question also can't be answered by a survey alone, because intent to keep building overstates actual building.

| # | When | Channel | Purpose |
|---|------|---------|---------|
| 1 | **Tomorrow, while judges deliberate, before winners are announced** | QR code on the main-hall screen plus a MC reminder | Catches people in the room at peak attention. Collecting before the announcement keeps non-winners' disappointment out of the ratings. |
| 2 | **Tomorrow, about 7:30 pm Rotterdam time** | Email | Backup for people who left early or skipped the QR code. Close enough to the event that they still remember it. |
| 3 | **Saturday morning, about 10 am** | Email reminder to non-responders only | Last nudge. Close the survey after 7 days. |
| 4 | **30 days out (about Nov 14)** | 2-question email plus a repo check | This is the real answer to "did they keep building". |
| 5 | **90 days out (about Jan 13)** | Same 2 questions | Shows whether the projects survived past the first month. |

A few notes on this plan:
- Don't email at 5:01 pm. People are travelling and the email gets buried.
- Judges, mentors and sponsors get shorter, separate versions (below). Send theirs at touchpoint 2 as well.
- Add a "Copy your project's repo URL" field to the survey. It lets you check commit activity at 14 and 30 days without asking anyone, and that is the most honest measure you'll get.

## Participant survey (about 4 minutes, 15 questions)

I changed these from the conference survey:
- I dropped **session ratings**, since there were no sessions.
- I replaced them with ratings for the things participants actually experienced: kickoff, mentors, sponsor APIs, judging and demo day.
- I kept venue, catering, overall satisfaction and likelihood to return. Overall satisfaction stays on 1-10, but don't compare it directly with the conference score, because the audience and format differ.

**Intro text:** "4 minutes. Your answers shape DevForge 2027. Questions 12-15 are optional follow-up."

**About you**
1. Did you join with a team or form one at the event? (Came with team / Formed at event / Solo)
2. Experience level: (Student / Junior / Mid / Senior / Other)

**Overall**
3. Overall satisfaction, 1-10.
4. How likely are you to recommend DevForge to a friend, 0-10?
5. How likely are you to join DevForge again next year, 1-10?

**Rate each, 1-5 (N/A allowed)**
6. Kickoff and rules briefing
7. Mentors: availability, and usefulness of their help
8. Sponsor APIs: docs quality, access and credits, and support when stuck. Ask this once per sponsor, so you get a score for each of the 3.
9. Judging and demo day: clarity of criteria, fairness, format
10. Venue (space, power, wifi, quiet areas)
11. Catering and overnight or weekend logistics

**Will you keep building?** (your main question)
12. Do you plan to keep working on this project after this weekend? (Definitely not / Probably not / Unsure / Probably / Definitely)
13. What is the most likely path? (Continue with the same team / Continue solo / Fold into an existing product or job / Turn it into a startup / Open-source it / Archive it, it was a weekend experiment)
14. Realistic hours per week for the next month? (0 / 1-2 / 3-5 / 6-10 / 10+)
15. What is most likely to stop you? (Select all: time / team splitting up / sponsor API access or credits ending / unsure the idea is worth it / no funding / no mentor or feedback / other commitments / lost interest)
16. What one thing would most help you continue? (Select up to 2: sponsor credits that last / follow-up mentor session / a showcase or demo slot / seed funding or intro to investors / a team-matching channel / nothing)
17. What is your next concrete step in the next 7 days? (free text, optional)

**Open comment**
18. What's the one thing we should change? What's the one thing we must keep? (two short boxes, instead of one big box, which gets higher-quality answers)

**Follow-up consent (separate, unticked by default)**
- "I agree to be emailed about my project in 30 and 90 days." (Email, repo URL, team name)
- "I agree to share my project and contact details with the sponsor(s)." (Opt-in per sponsor, so a sponsor never gets data from people who didn't agree)

The survey is confidential, not anonymous, because it needs an email and repo URL for the follow-up. You're in the EU, so keep the consent wording explicit and the retention period stated (for example, "deleted after the 90-day check").

## Short versions for other groups

**Mentors (14), 2 minutes:** hours spent; how many teams helped; was matching with teams workable (1-5); were you briefed on the sponsor APIs (1-5); which teams do you think will keep going, and why; would you mentor again; what should change.

**Judges (5), 2 minutes:** were the criteria clear (1-5); was 5 judges the right number; was demo length enough; which criteria separated the top teams; did the winners reflect "will keep building" potential.

**Sponsors (3), a 15-minute call instead of a form:** how many teams actually used your API; how many working integrations you saw; support requests received; sign-ups or API keys created; would you sponsor again; whether you want a 30-day usage readout of those keys.

## How to read the continuation answers

- Treat "Definitely" plus 3+ hours per week plus the same team staying together as your **likely-to-continue** group. Count this group, not just the "Definitely" answers.
- Expect stated intent to come out well above actual activity. Use the survey for **why** teams stop, and the 30-day commit data for **how many** continue.
- Compare outcomes by sponsor API as well. A project built on an API with free credits that expire this week is much less likely to survive.

## Email text (touchpoint 2)

**Subject:** DevForge: 4 minutes to shape next year (and tell us if you're building on)

> Hi {first name},
>
> Thanks for building with us this weekend. Please take 4 minutes to tell us what worked and what didn't: {link}
>
> One question matters most to us: will you keep building your project? Tell us what would help you continue, and we will act on it.
>
> {Your name}, DevForge

## Next steps for you

1. Decide who owns tomorrow's QR slide and MC mention (the deliberation break is the best slot).
2. Build the form, and add the 3 per-sponsor rating rows.
3. Schedule the 30-day and 90-day emails now, along with the repo check.

One thing I couldn't verify: the sponsors' API credit terms. If credits expire within days, put that into question 15 as a named option, because it is probably the biggest cause of drop-off.