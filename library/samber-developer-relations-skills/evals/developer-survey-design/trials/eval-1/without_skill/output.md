# Kelpline State of Feature Flags 2026: final questionnaire

I cut the draft from 15 to 14 questions and reordered them. Most answers fit in about 8 minutes. Every question is optional unless marked.

## Intro text (shown above Q1)

> Thanks for helping shape Kelpline's roadmap and docs. The survey takes about 8 minutes. Answers are anonymous unless you choose to leave your email in the last section. We will publish only aggregated results, and we will never publish individual answers or company names.

## Section 1: Your use of Kelpline

**1. Which of these best describes how you use Kelpline today?** *(required, single choice)*
- Running in production
- Running in staging or pre-production only
- Developing or testing locally
- Evaluating it for a future project
- I used it in the past but stopped

*Skip logic: if "stopped", jump to Q9 and Q12.*

**2. In which environments do you evaluate flags with Kelpline?** *(select all that apply)*
- Production
- Staging or pre-production
- Development or CI
- Other (please specify)

**3. How long have you used Kelpline?**
- Less than 3 months
- 3 to 12 months
- 1 to 2 years
- More than 2 years

**4. Which other feature-flag tools have you used in the past 12 months?** *(select all that apply)*
- Flagpole
- A tool built in-house
- Config files or environment variables
- Other (please specify)
- None

## Section 2: Experience

**5. How likely are you to recommend Kelpline to a colleague?**
Scale from 0 (not at all likely) to 10 (extremely likely).

**6. How would you rate Kelpline's performance compared with the tool you used before?** *(show only if Q4 is not "None")*
- Much slower
- Slightly slower
- About the same
- Slightly faster
- Much faster
- Not sure

**7. In the last 3 months, what slowed you down or stopped you?** *(select all that apply)*
- SDK bugs
- Missing SDK for my language (please name it)
- Documentation
- Pricing
- Performance
- Authentication or SSO
- Other (please specify)
- Nothing slowed me down

**8. Where did you get stuck the last time you used Kelpline?** *(free text, up to 500 characters)*
Please describe what you were trying to do and what happened.

## Section 3: Priorities

**9. If we could improve only one thing next quarter, which would help you most?** *(single choice)*
- SDK coverage (more languages or better SDKs)
- Documentation
- Dashboard
- Performance
- Authentication or SSO
- Pricing or packaging
- Something else (please specify)

**10. Which documentation would help you most?** *(select up to 2)*
- Getting-started tutorials
- SDK reference
- Production deployment and operations guides
- Migration guides from other tools
- Troubleshooting guides
- Other (please specify)

## Section 4: About you

**11. What is your role?**
- Software engineer
- Platform, DevOps or SRE
- Engineering manager
- Product manager
- Other (please specify)

**12. How many engineers work at your company?**
- 1 to 10
- 11 to 50
- 51 to 200
- 201 to 1,000
- More than 1,000

**13. What is your company's approximate annual spend on feature-flag tooling?**
- Nothing
- Under $1,000
- $1,000 to $10,000
- $10,000 to $50,000
- More than $50,000
- I don't know or prefer not to say

## Section 5: Follow-up (optional)

**14. Would you like us to follow up with you?** *(select all that apply; leave blank to stay anonymous)*
- Show me a demo of Kelpline Cloud
- Invite me to a short interview about my answers
- Send me the survey results

*If you select any option, show:* Email address: ______ *(Name is optional.)*
> We will use your email only for the options you selected. It is stored separately from your answers, and you can ask us to delete it at any time.

## What I changed and why

- **Dropped version and OS (old Q3, Q4).** Telemetry already reports both, along with self-hosted versus cloud. Self-reported answers would be less accurate than telemetry and would add length.
- **Added the production question (Q1, Q2).** This is the biggest gap in the draft. Marketing wants a production-usage headline for the launch blog, and the draft had no question that could support it. Telemetry shows what is running but not whether it is production.
- **Moved name and email to the end, optional, with consent.** Collecting them first lowers completion and makes answers non-anonymous. Merging the demo request (old Q10) into the follow-up section keeps sales leads out of the survey data.
- **Replaced "How much do you love Kelpline?" with a 0 to 10 recommend question (Q5).** The original wording was leading, and the recommend scale is a standard format you can benchmark against.
- **Rewrote the Flagpole statement (old Q6) as Q4 plus Q6.** "Kelpline is faster than Flagpole" is leading and ties the survey to one competitor. It also would not survive a challenge if published. Only people who have used another tool see the new comparison.
- **Merged the tutorials and SDK docs questions (old Q7, Q8) into Q10.** They were yes/no questions that would almost all be answered "yes". Q10 asks respondents to pick their top two docs needs.
- **Aligned Q7 and Q9 options.** The old Q12 left out auth/SSO and pricing, which Q11 offered. I also added "Nothing slowed me down" and "Other" fields.
- **Turned budget (Q13) and company size (Q12) into ranges.** Both are now optional and sit at the end of the survey.

## Decisions for you and the team

1. **Headline wording.** Respondents are self-selected, so the headline must read "X% of survey respondents run Kelpline in production", not "of Kelpline users". If marketing wants a population claim, take it from telemetry instead (opt-out limits that too). Check the wording with marketing before the launch blog.
2. **Noor, Q9 options.** Confirm the list matches the real roadmap candidates. I added auth/SSO and pricing to the draft's four options.
3. **Privacy.** Kelpline's privacy policy should cover the survey and the Q14 email. If you have EU respondents, GDPR applies, so a legal check before launch is worthwhile.
4. **Missing-language SDKs.** Q7 asks respondents to name the language. That gives you a ranked list for SDK prioritisation.