# Kelpline "State of Feature Flags" survey: decision table and final questionnaire

I followed the `developer-survey-design` skill, and it changed more than the wording. I cut 9 of your 15 questions, rewrote 4, and added 5. I did this alone, so the interview and the per-step validation with Noor and marketing haven't happened. Treat this as a draft for them to confirm.

## Re-ranking

```
Answer 2 (headline percentage planned for the November blog): claim rules are release blockers.
Answer 4 (first edition of a yearly series): core module marked now, to be frozen word for word next year.
Answer 7 (telemetry reports version, OS, self-hosted vs cloud): version and OS questions deleted; deployment mix becomes a bias check.
```

## 1. Decision table

**Kept or rewritten**

| New | Orig | Question (short) | Decision | Owner | Answer that would change it | Publish | Module |
|---|---|---|---|---|---|---|---|
| Q1 | new | Furthest stage in last 12 months | Qualifier; production headline; segments every cut | Marketing | Production share differs sharply between self-hosted and cloud: the headline leads with the segment | publish | core |
| Q2 | new | Self-hosted / cloud / both | Segments cuts; bias check against telemetry | Noor, Marketing | The telemetry mix and the respondent mix diverge widely: the sample is skewed and the bias sentence names it | internal | core |
| Q3 | 11 | What slowed or stopped you (last 3 months) | Ranks all blockers against the roadmap candidates | Noor | A non-roadmap blocker outranks the candidates: raise it | internal | core |
| Q3b | new | Which missing language SDK(s) | Picks which SDK to build next | Noor | One language dominates: build it first | internal | core |
| Q4 | 12 | Improve only one thing next quarter | Final order of next quarter's investments | Noor | One option wins in two or more segments: ship it first | internal | rotating |
| Q5 | 15 (split) | Task you were doing when last stuck | First docs sprint | Docs (you) | One task tops two segments: that is the sprint | internal | core |
| Q6 | 15 (split) | Open text: what happened | Same docs sprint, with real examples | Docs (you) | Repeated phrasing exposes a missing page or wrong example | internal | core |
| Q7 | 13 | Role | Segment cut only | Noor | Roles diverge on Q4: split the roadmap argument | internal | core |
| Q8 | 14 | Company size (bands) | Segment cut only | Noor, Marketing | Enterprise-sized respondents rank auth/SSO first: prioritise it | internal | core |

**Cut**

| Orig | Question | Reason |
|---|---|---|
| 1, 2 | Name, work email | Identifiers stay out of the response table. Optional follow-up goes in a separate form. |
| 3, 4 | Version, OS | Telemetry answers both. |
| 5 | "How much do you love Kelpline?" | Praise in the stem, and no decision attached. |
| 6 | "Faster than Flagpole" | Agree/disagree inflates agreement. A speed claim needs a published benchmark, not opinions. |
| 7, 8 | More tutorials? Better SDK docs? | Wishlists return yes. Q4 and Q5 replace them with a trade-off. |
| 9 | Annual tooling budget | No decision or owner named. |
| 10 | Demo of Kelpline Cloud? | Lead capture makes the survey marketing, so marketing-email consent rules apply. A link on the thank-you page replaces it. |

## 2. Questionnaire

Target median is about 6 to 7 minutes on the longest path. This is my estimate, and the soft launch must time it. Questions 1 to 6 feed decisions, so they come first. Demographics come last and are optional.

**Page 0: notice and age gate (before Q1)**
- Privacy notice, per the skill's template. It names who runs the survey, the purposes, the legal basis, the processor, the retention date, the rights and the suppression rule.
- "I am 16 or older." Anyone who says no is routed to the end.

**Q1. Which best describes how you have used Kelpline in the last 12 months?** *(single choice, fixed order; core, publish)*
- I have not used Kelpline → end of survey
- Evaluated it only
- Development or test environments
- Staging or pre-production
- Production, serving real users or business processes

**Q2. How do you run Kelpline?** *(single choice; core)*
- Self-hosted
- Kelpline Cloud
- Both
- Don't know

**Q3. In the last 3 months, which of these slowed you down or stopped you? Select all that apply.** *(multi-select, randomised, "Other" and "Nothing slowed me down" fixed at the bottom; core)*
- SDK bugs
- No SDK for my language
- Docs missing or unclear
- Dashboard limitations
- Pricing or plan limits of Kelpline Cloud *(shown only if Q2 is Cloud or Both)*
- Performance
- Authentication or SSO
- Other (please specify)
- Nothing slowed me down *(exclusive)*

**Q3b. Which language(s) is the SDK missing for?** *(shown only if "No SDK for my language" is ticked; free-text list)*

**Q4. If we could improve only one thing next quarter, which would help you most?** *(single choice, randomised; rotating)*
- SDK coverage
- Docs
- Dashboard
- Performance
- Other (please specify)

**Q5. What were you trying to do the last time you got stuck with Kelpline?** *(single choice, randomised; core)*
- Install or deploy it
- Set up an SDK in my app
- Create flags, rules or targeting
- Roll out gradually (percentages, environments)
- Set up auth or SSO
- Migrate from another tool
- Upgrade a version
- Monitor or operate it
- Other (please specify)
- I haven't got stuck

**Q6. (Optional) Describe what happened the last time you got stuck.** *(open text, shown only if Q5 is not "I haven't got stuck"; core)*
"Please leave out names and company details."

**Q7. What is your role?** *(single choice, optional; core)*
- Software engineer
- Platform, DevOps or SRE
- Engineering manager
- Product manager
- Other (please specify)
- Prefer not to say

**Q8. How many people work at your organisation?** *(optional; core)*
1 / 2-10 / 11-100 / 101-1,000 / 1,001-10,000 / More than 10,000 / Not employed / Prefer not to say

**Thank-you page**
- A link to the results, once published.
- A separate, unticked "email me the results / follow-up" form, kept in a different store with no join key.
- A link to the existing Kelpline Cloud demo page, under its own consent.

## 3. The production headline

Q1 supports this claim and nothing wider:

> "X% of the N respondents who used Kelpline in the last 12 months run it in production (real users or business processes depend on it). Respondents came mostly from <channels>, so the figure describes respondents, not all users."

- ❌ "X% of developers run Kelpline in production" is not available from an open-link survey.
- ❌ Never print a margin of error on an open-link survey.
- ❌ Don't publish "Kelpline is faster than Flagpole". Only a published benchmark can carry that.
- 🎯 To reach the stronger claim ("X% of users invited at random"), send the survey to a random slice of CLI or cloud users. Print the invited-to-completed counts beside the number.

## 4. Choices for you to confirm

1. **Q2 stays.** Telemetry knows the self-hosted/cloud split but can't be joined to individual answers. Without Q2 you can't cut the headline by deployment. Compare its mix against telemetry as a bias check. Marketing may want it cut; this is the one place I'd push back.
2. **Q4 options** must be Noor's real candidates. "Docs" is yours, so decide whether it belongs in a roadmap vote.
3. **Q5 options** are my guess at doc areas. Replace them with your real doc sections.
4. **Q3 gained "Dashboard limitations".** Q4 offered Dashboard but Q3 didn't, so the two couldn't be compared.
5. **No role or company-size wording is copied** from a large published survey. If marketing wants to compare against Stack Overflow or JetBrains, copy their wording exactly instead.

## 5. What I still need to answer before launch

I made these assumptions and couldn't verify them:

- **Respondent location:** I assumed some respondents are in the EU or UK, so privacy rules apply in full.
- **Launch date:** If the survey must field before the November blog, you have little time. Under four weeks, skip cognitive interviews and keep an expert review plus a soft launch.
- **Analyst hours:** Q6 is the only open box. Time yourself coding 50 answers, then extrapolate.
- **Incentive:** I defaulted to none, with results shared first. A laptop raffle would add contact data, sweepstakes rules and bot entries.
- **Open channels:** The skill expects the channels to be tagged. You need distinct links per channel and a stated field window.

Next steps in the skill are the survey plan, pilot plan, privacy pack and publication plan, validated with you one at a time. I can draft the survey plan next.