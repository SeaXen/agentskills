# HackTheHarbor feedback plan: review and survey intro

I based this on the `event-feedback` skill and its four reference files. I haven't run the skill's interview, so the assumptions are listed at the end. The plan has 5 problems, and 3 of them break the anonymity you want.

## Verdict

| # | Plan item | Verdict | Fix |
|---|---|---|---|
| 1 | Anonymous survey | ✅ Right call | Promise it inside the form. Say "anonymous", not "confidential". |
| 2 | iPad draw | ❌ Contradicts #1 | Drop the draw. Use in-room capture instead. |
| 3 | Rate each of 6 judges by name on fairness | ⚠️ Risky | Ask about fairness of the process instead. |
| 4 | Rate "your assigned mentor" | ⚠️ Breaks anonymity | Ask about mentor help in general. |
| 5 | Publish best quotes | ⚠️ Consent is missing | Ask for consent in the survey, or don't publish. |
| 6 | General satisfaction only, otherwise | ⚠️ Gaps | Add team, tooling and continuation questions, plus a second survey. |

### 1. The iPad draw and anonymity can't coexist
- A draw needs an identity attached to each response. The skill's rule is: when anonymity is required, delete the incentive rung.
- Any trick that links "who finished" to "what they said" gives people a reason to doubt the promise. Doubt makes the judge and mentor ratings unusable.
- You don't need the draw.
  - Emailed surveys get 10-30% (credible, from Explori). With 90 hackers that is about 9-27 answers.
  - In-room capture gets 40-60% (directional, vendor figures). That is about 36-54 answers.
  - In-room capture beats the incentive on response rate and on effort. The skill's data puts the draw's lift at roughly half again, from one case study.
- Add one line to the closing ceremony run of show.
  - Show a QR code or short link while everyone is still in the room.
  - Give 5 minutes, before anyone leaves.
  - Keep the email as a fallback, with one reminder 3-4 days later and no more than two reminders in total.
- Send the email within 24-48 hours of the end. That timing is practitioner consensus, not a measured effect.
- Send the fallback through each team's own chat as well as the general list. This is the skill's own convention, not a measured figure.

### 2. Rating 6 judges by name on fairness
- Anonymity is the right setting here. Fairness and named-person ratings are exactly where the skill says to turn it on.
- Per-judge numbers will still be weak.
  - Judges saw different teams, so each judge gets a handful of ratings at most.
  - A fairness score on a named person from 4 respondents is noise, and it can hurt a volunteer judge unfairly.
- Ask about the process instead, which is what the skill's hackathon layer lists: fairness, clarity of criteria, and transparency of the decision.
- Per-judge ratings only make sense if you have a decision they feed. Ask yourself: "Would I replace or re-brief a judge based on this?" If so, tell me who decides, and I'll add a "which judges did you present to?" filter question.

### 3. "Your assigned mentor" breaks anonymity
- To answer, a hacker must pick their mentor, which reveals their team. With about 3 teams per mentor, a rating plus one free-text comment identifies the writer.
- Ask about mentor help overall instead:
  - Was a mentor available when you needed one?
  - Did the feedback help?
  - Was there an "I need help now" path?
- Do not ask for the team name or the mentor's name.
- Nobody should be able to tell who wrote what, so aggregate everything. Report a theme only when several people raised it.

### 4. Publishing quotes needs consent at collection time
- An anonymous respondent can't be asked afterwards. Without consent in the form, the quote stays internal.
- Add a checkbox next to the open question: "OK to quote this anonymously in our recap."
- Never publish a quote that names a person. Redact the name and keep the substance.
- Any free-text report of a code-of-conduct violation goes to your CoC reporting pipeline and nowhere else. It is not a survey finding.
- Raw exports stay with the core team. Judges and mentors see themes only.

### 5. Missing hackathon measures
- A conference-style survey would measure your catering, not your hackathon. Add the hackathon layer: team formation and collaboration, tooling and API quality, and wifi and overnight logistics.
- Plan a second, separate survey 1-2 weeks later on whether teams kept working. Asked on the day, it only collects intention. MLH's 2014 survey of 920 hackers found 69% continued their projects, a useful comparison point.

### 6. Keep it short
- Aim for under 5 minutes. Surveys of 2-3 questions got a 15.97% median response rate and surveys of 7+ got 6.87%, from a study of 267,564 responses. Every question needs an owner and a decision. The question list below has 10 questions in total.

## Suggested instrument (about 4 minutes)

| # | Question | Decision it informs |
|---|---|---|
| 1 | How likely are you to recommend HackTheHarbor to a friend? (0-10) | Overall health |
| 2 | How likely are you to join next year? | Return intent |
| 3 | How easy was it to find or form your team? (1-5) | Team-formation format |
| 4 | When you needed a mentor, how quickly did you get help? (1-5) | Mentor staffing |
| 5 | How useful was the feedback you got from mentors? (1-5) | Mentor briefing |
| 6 | Were the judging criteria clear before you presented? (Yes / Partly / No) | Criteria publication |
| 7 | Did the judging process feel fair? (1-5) | Judging format |
| 8 | Did tools, APIs or docs from sponsors slow you down? (Yes / No) + which | Sponsor tooling |
| 9 | Was there anything about the venue, food, wifi or sleeping setup that made it harder to work? | Logistics |
| 10 | What is the one thing we should change next time? (open) + quote-consent checkbox | Top priority |

If you need per-judge scores, this is where they would go (see item 2).

## What happens to answers
- Report the response rate next to every number.
- Group free text into themes with counts, and don't average satisfaction with return intent.
- Within a week, send a short "you said, we changed" note with 2-3 changes. This is the main predictor of next year's response rate.
- A public findings post makes sense since you're already writing a recap. Publish only what has consent, and say what the survey got wrong.

## Survey intro text

> **HackTheHarbor feedback: 4 minutes, anonymous**
>
> Thanks for building with us this weekend. Your answers decide what we change for next year, so please be blunt.
>
> **This survey is anonymous.** We don't collect your name, email or team name, and we can't see who wrote what. Please don't write names in the comment boxes. Only the core organizing team reads the raw answers. Judges and mentors will see only summarized themes, never individual comments.
>
> We ask about judging and mentoring as a whole, not about named people. If you want to report a safety or conduct concern, please contact [CoC contact] directly. This survey is not the right channel for that.
>
> At the end, you can choose whether we may quote your comment, anonymously, in our recap blog post. If you don't tick the box, your comment stays internal.
>
> We'll share what we learned and what we're changing within [X days].
>
> [Start]

## Check before sending
- ⚠️ In your survey tool, turn off collection of IP addresses, email addresses and any login requirement, or "anonymous" is false.
- Fill in [X days] and [CoC contact] before you publish.
- If any hackers are under 18, tell me. That changes the consent wording.

## Assumptions I made, tell me if wrong
- ℹ️ The event is still running, so the closing ceremony can take a line in the run of show. If it has already ended, the in-room option is gone and you're on email only.
- You have no budget-critical sponsor decisions riding on the survey.
- Q7 (one-off or recurring) is unknown. I assumed recurring because you plan a recap post.