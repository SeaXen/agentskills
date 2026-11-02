**Verdict:** the target is not ready to go to the board. The two numbers are fine as reference points. Turning them into promises has four problems.

## 1. Last year's rates may not be comparable (check first)

- ❓ What was their denominator (submissions, teams, or registrants)?
- ❓ How did they define "invalid" versus "disqualified"? Is a disqualification a subset of invalid?
- ❓ Was their event the same size, with the same kind of submission and the same rules?
- If you can't answer these, "under both" compares two different things. Ask the organizers for their definitions and counts, or label the numbers "indicative only".

## 2. Small numbers make the target mostly luck

160 registered is not 160 submissions. Hackathons often see about 50–70% turn up, and teams are 3–4 people. My assumption is roughly 20–35 submissions.

| Submissions | "Under 8%" means at most | "Under 4%" means at most |
|---|---|---|
| 25 | 1 invalid | 0 disqualified |
| 30 | 2 invalid | 1 disqualified |
| 35 | 2 invalid | 1 disqualified |

- One extra disqualified team swings the rate by about 3–4 points.
- With 1 disqualification out of 30, the 95% interval is roughly 0.6–16%. A result of 3% or 5% tells the board almost nothing.
- At the low end of my estimate you'd need a perfect zero to hit the 4% goal.

## 3. A lower rate isn't always better

- You can hit both numbers by validating loosely or by not enforcing the rules. That is Goodhart's law.
- Disqualifications are sometimes the right call. Examples are leaked utility data or rule violations.
- Real utility problems add risk. Submissions may contain sensitive grid data, which can mean confidentiality or critical-infrastructure obligations.
- Each of the 12 problems has its own data and format, so "valid" differs per problem. Rates will be uneven across them.

## 4. The target measures the wrong thing

Invalid and disqualified rates measure hygiene. Your event's value is the 12 real problems. The board probably cares more about whether those got usable answers.

## Suggested replacement

1. **Process target (you control it):** rules and a validity checklist published before kickoff, plus a pre-submission checker that teams run themselves. Then say "no submission is lost to a preventable format or rule error."
2. **Rate as a reported figure:**
   - Report counts and rates with the definitions stated.
   - Frame it as "at most X invalid and at most Y disqualified" once you know the submission count, not as a percentage promise.
   - Set the cap once you know the final team count, or after registration closes.
3. **Outcome metrics:**
   - How many of the 12 engineers get at least one usable solution?
   - What is the engineers' own rating of usefulness?
   - How many follow-up pilots or conversations come out of it?
4. **Add a guardrail:** a written data-handling policy agreed with the utilities before the event. A disqualification for a data breach is a valid outcome, and it should not count against you.

## Other plan checks

- Mentor ratio: 12 engineers for about 25–35 teams is roughly 1 per 2–3 teams. That works only if each engineer owns specific problems.
- Registration to show-up: plan for about 50–70%, and send reminders and a check-in step.

## Questions for you (reply with numbers)

1. What were last year's denominators and definitions?
2. What is your expected team count or submission count?
3. What kind of submission is it (code, model, report), and who judges validity?
4. Will any real utility data be shared with participants?

Once I have those, I can write the one-line target for the board.