# DevForge feedback plan

## Do this first (today, about 1 hour)

1. **Add a 5-minute "scan the QR" slot to tomorrow's run of show.** Put it while the judges deliberate, before the winners are announced (~10 min).
2. Build the participant form below in your form tool, with no login and no email field (~40 min).
3. Put the QR code and a short URL on the main-hall screen slide. Tell the MC to read it out (~10 min).
4. Check that your registration terms let you send a follow-up email in 10 days. Do this before step 3 of the send schedule (~5 min).

## Assumptions (correct me if any are wrong)

- You are the only decision-maker on these answers.
- DevForge is not a hiring event, so there are no talent-pipeline questions.
- Demo day is Thursday 15 Oct 2026, from today's date. A "weekend" event ending on a Thursday looks odd, so check this. The offsets (D+1, D+11) still work if the date is different.
- You are fine with a draw-free survey (see Anonymity).

## What changed from the conference survey

| Conference item | Hackathon version | Why |
|---|---|---|
| Overall satisfaction 1-10 | Recommend 0-10 (Q1) | One comparable number. Four rating scales collect one blended impression. |
| Session ratings | Cut | There are no sessions. Replaced by team, mentor, judging and API questions. |
| Venue and catering ratings | One tick-box question (Q8) | A checklist of what got in the way beats separate ratings. |
| Likelihood to return | Folded into Q1 and Q9 | Return intent is imagination. Q9 asks about concrete next steps. |
| One open comment | "One thing to change" (Q11) | A bounded box gets a priority. An open box gets nothing or an essay. |
| Not asked before | Team formation, mentor wait, judging fairness, API obstacles, project continuation | These are the substance of a hackathon. A conference core alone would only measure catering. |

## Survey 1: participants (demo day, in the room)

Anonymous, 11 questions, about 3 minutes. Ten are taps and one is an open box. Each question names the decision it feeds, and all decisions are yours.

**Header text:** "Anonymous. We collect no name, email or team. Mentors, judges and sponsors only see group results. To report a conduct issue, contact [CoC contact], not this form."

| # | Question | Answers | Decision it feeds |
|---|---|---|---|
| 1 | How likely are you to recommend DevForge to a developer friend? | 0-10 | Overall verdict, one number kept separate from the rest |
| 2 | How did your team come together? | Came as a team / Formed at the event / Joined after start / Worked solo | Whether to run a team-formation session next time |
| 3 | What was the longest you waited when you wanted a mentor? | Never needed one / No wait / Under 10 min / 10-30 min / Over 30 min / Asked, never got help | Mentor staffing (14 mentors is enough or not) |
| 4 | The judging criteria were clear before I started building. | Agree-disagree, 1-5 | Whether to publish criteria earlier |
| 5 | The way winners were picked felt fair to me. | Agree-disagree, 1-5 | Judging process |
| 6 | Which sponsor APIs did you build on? | Sponsor A / B / C / none (multi-select) | Splits Q7 by API |
| 7 | What was the biggest obstacle using it? | Docs / Getting keys / Rate limits / SDK bugs / Missing examples / Support / None | Feedback to each sponsor and API selection next time |
| 8 | Did any of these get in the way of building? | Wifi / Food / Space or seating / Noise / Sleep options / Nothing (multi-select) | Venue and catering choices |
| 9 | Where does your project stand right now? | Next work session already planned with a date / Intend to continue, nothing planned / Pushed code to a repo / We're done | Baseline for the follow-up (see Survey 2) |
| 10 | What is the main thing that would stop you continuing? | Time / Team scattering / API access ending / Unsure it's worth it / Lost interest / Need infrastructure or credits / Nothing | What you can offer to help teams continue |
| 11 | What is the one thing we should change next time? | Open box, plus a checkbox: "OK to quote this anonymously in a public recap?" (default: no) | Anything the closed questions missed |

If you need it shorter, cut Q8 first, then Q2. Every cut question raises the response rate. The largest available study found short surveys more than double the median response rate of long ones (15.97% for 2-3 questions against 6.87% for 7 or more).

**Why the slot sits before the winners are announced:** winners may rate fairness differently from everyone else. This is my own judgment and not measured. If there is no deliberation gap, use the last slot before the awards. Do not put it after the awards, because people start leaving.

**Q9 is an intention proxy.** It does not answer your main question. Asked on the day, a continuation question only collects intention. Survey 2 is the real answer.

### Anonymity and free text

- **The promise is anonymous.** It covers mentor quality and judging fairness, so no name, email or team field is collected. Say so in the form header, as above.
- **No prize draw.** A draw needs an identity, and that breaks the anonymity promise.
- **Small cells:** with 3 APIs and about 130 people, hide any breakdown with fewer than 5 respondents.
- **Who reads raw free text:** you only. Redact names before passing anything on.
- **Conduct allegations** go to your code-of-conduct contact and are never survey findings.
- **Quotes:** only quote text where the box was ticked. An anonymous respondent can't be asked afterwards.

### Send schedule

| When | What | Reason |
|---|---|---|
| Demo day, deliberation slot | QR on screen, MC read-out, 5 minutes | Everyone is seated and the event is fresh. In-room response runs 40-60% against 10-30% for email. These are vendor figures, so use the ratio, not the numbers. |
| D+1 morning (Fri 16 Oct) | One email to all registrants with the same link, tagged `?src=email`. Also post it in any team chat channels you have. | Practitioner consensus is 24-48 hours, with no controlled test for technical events. Because the survey is anonymous you can't target non-responders, so word it "ignore this if you answered in the hall". |
| D+4 | Optional last reminder, only if the in-room count was under the floor | The cap is two reminders in total. More produces fatigue. |

**Response gate:** at least 52 responses (4 in 10 of 130). Below that, treat the collection as failed and do not read the audience as indifferent. Fix it by sending the email, shortening the form, or both. Report the response rate next to every finding.

## Survey 2: did teams keep building? (your main question)

This is a separate short survey. It is not a delayed version of Survey 1.

**When:** Monday 26 Oct (D+11), reminder on Thursday 29 Oct (D+14, the last one), closing around 1 Nov. The skill's window is 1-2 weeks after the event.

**How:** one email per participant, also posted in team chat channels if teams have them. A peer channel carries trust that a cold broadcast lacks. This is the skill's own convention and not a measured figure.

**Confidential, not anonymous.** It asks for team name so you can avoid double-counting teams. Say so in the header and promise aggregate-only use. It has 6 questions and takes about a minute. All are in the past tense, because behavior is evidence and plans are not.

1. Team name.
2. Since demo day, about how many hours did you spend on the project? (0 / under 2 / 2-5 / over 5)
3. Which of these have happened? (multi-select: pushed new commits / made the repo public / showed it to someone outside the team / applied somewhere with it (accelerator, grant, another hackathon) / nothing)
4. Did you work on it with teammates at any point since demo day? (Yes / No / Went solo)
5. Is a next work session on the calendar, with a date? (Yes / No / We've stopped)
6. If you stopped or slowed down, what was the main reason? (Time / Team scattered / API access ended / Finished what I wanted / Lost interest / Other). Then, optionally: "What one thing from us or the sponsors would help you keep going?"

### How to read it

- **State the response rate beside every continuation number.** Teams that kept building are likelier to answer, so the raw figure overstates continuation. Report "of the N who answered".
- **Floor:** about 13 respondents (1 in 10 emailed), and ideally at least one per team.
- **Reference point:** MLH's 2014 survey of 920 student hackers found 69% continued their projects afterwards. It is self-reported, student-only and 12 years old. Use it as context, not a benchmark.
- **Optional cross-check:** if teams submitted repo links, count public commits after demo day. It needs no response and counters the answering bias. This is my own suggestion. Only use public repos.
- **Q9 versus Q3 and Q5:** compare the share who had a dated next session on demo day against the share who actually worked afterwards. That gap tells you how much to trust intention next time.

## Short forms for the named roles

These are tiny populations. Report them by name, not as percentages. Send them D+1 morning by personal email. All are confidential, not anonymous.

**Mentors (14)**
1. Roughly how many teams did you help?
2. Where did teams get stuck most? (API docs / Auth and keys / Scope too big / Team conflict / Deployment / Other)
3. Did you have what you needed to help (briefing, API contacts, a way to escalate)? Yes or no, and what was missing.
4. Would you mentor again?

**Judges (5)**
1. Were the criteria usable for scoring?
2. Was there enough time per team?
3. What information about the projects did you lack?
4. Would you judge again?

**Sponsors (3)**
1. Was the audience a good fit for your goals? (Audience fit predicts renewal better than raw lead count. This is published, from Bizzabo, Formbricks and others.)
2. Did you meet the specific goals you set? (Yes / Partly / No, with the goal)
3. What did you see teams struggle with in your API?
4. Was our logistical support enough?
5. Would you sponsor again? (Yes / Maybe / No)

**If any sponsor answers "No" or "Maybe" to Q5, phone them that day.** Do not leave it in a spreadsheet. Each sponsor's verdict goes straight to `event-sponsor-fulfillment`. The ROI report to sponsors is a separate job in the opposite direction.

## Closing the loop

- **Default: a short "you said, we changed" note to all participants around D+7 (Thu 22 Oct).** Include a thank-you, the headline numbers, and 2-3 findings you are acting on. This does the most for next year's response rate at a low cost.
- If DevForge is a one-off, send only a thank-you and the headline numbers.
- A public findings post only makes sense if the event repeats and you plan a recap. The consent box in Q11 keeps that option open.

## Hand-offs

1. The whole findings summary goes to `event-debrief`, before the debrief meeting.
2. The qualitative read (Q1, themes, intent) goes to `event-market-fit`. That skill owns the behavioral demand verdict.
3. Sponsor verdicts go to `event-sponsor-fulfillment`, immediately.
4. Do not send anything to `event-continuous-improvement`. Findings reach it through the debrief log.

**Record for next year:** the instruments as fielded, send dates, response rate per role, headline numbers, theme counts, and what you promised about anonymity. This edition's rate means little until a second edition sits beside it.

**Not measured:** the 24-48 hour send window is practitioner consensus, and the "roughly half again" incentive lift comes from one case study. The in-room versus email gap comes from vendor claims. The question wording and the "before winners" timing are my judgment.