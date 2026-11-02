Next action: decide what to do with the 40 Discord responses before Monday. Everything else below is secondary.

## Biggest gaps (ranked)

1. **Fix the plan to tweak questions in week one.**
   - Editing a live survey makes early and late answers measure different things.
   - Responses from different wordings can't be pooled or compared. Results are due in three weeks, and you'd have no clean way to explain which version each respondent saw.
   - Freeze the questionnaire before Monday. Fix confusing questions only if the wording is clearly broken, and then log the change date.
   - Tag every response with a `survey_version` field. Tag it with the version the respondent saw, not the date.

2. **Don't pool the 40 Discord responses blindly.**
   - They answered the pre-edit version. Two questions have since changed, so those two columns aren't comparable.
   - Keep them as pilot data. For the 38 or so unchanged questions, pooling is probably fine. Document that choice.
   - For the two changed questions, either exclude the 40 or report them separately.
   - Discord regulars are self-selected, engaged users, so they skew the sample. Tag the source (`discord_pilot`) so you can run results with and without them.
   - Check one more thing: did those 40 see each other's comments? Public feedback can bias their answers.

3. **Do a quick cold test on the final version.**
   - The two changed questions were never retested. Have 3 to 5 people who haven't seen it take the final version, ideally while thinking aloud. Budget about 1 hour.
   - Do this before Monday. Once the newsletter goes out, you can't retract it.

4. **Think about the whole-newsletter blast.**
   - One send reaches everyone at once, so any bug hits the full list. Consider sending to about 10% first. Wait a few hours and check completion rate and drop-off points. Then send the rest the same day.
   - Plan a reminder around day 4 or 5, sent only to non-responders. Most responses arrive in the first 48 hours, and a reminder usually adds a meaningful bump.
   - Send time matters. Monday morning in the audience's main time zone is reasonable, but check where your readers are.

5. **Pre-define what "done" means.**
   - Pick a target response count and the minimum per segment you'll slice by (for example, by language or SDK version). Without it, you can't tell on day 7 whether you're on track.
   - Decide the close date now: day 21 minus time for analysis. Allow at least 3 to 4 days for cleaning and writing, so close the survey around day 17.

## Smaller checks

- **Mobile:** open it on a phone. Most newsletter reads happen there.
- **Duplicates and bots:** decide how you'll dedupe (one response per email, or a cookie or token). Test whether one person can submit twice.
- **Privacy:** state what you collect, how it's used, and whether answers are anonymous. If you're collecting emails or any EU respondent data, a short GDPR notice and a lawful basis are needed. Keep any contact field optional and separate from the answers.
- **Screening question:** confirm the survey filters for people who actually use the Ashgrove SDK. Newsletter subscribers include non-users, and their answers will dilute the results.
- **Length:** state the time to complete up front (for example, "about 5 minutes") and measure it in your test.
- **Incentive:** if you offer one, say so on the first screen and note it may bias who responds.
- **Tracking:** use a distinct UTM or link per channel (newsletter, Discord, social) so you can see source mix later.
- **Export and backup:** confirm you can export raw data, and take a copy daily.
- **Result owner:** name who writes up the results and who signs off, so the deadline doesn't slip at the end.

## Revised timeline

| Day | Action |
|---|---|
| Fri/Sat | Cold test (3 to 5 people), freeze questionnaire, add `survey_version` and source tags |
| Mon AM | Soft send to about 10%, check completion and drop-off |
| Mon PM | Send the rest |
| Day 4–5 | Reminder to non-responders |
| Day ~17 | Close |
| Day 17–21 | Clean, analyze, write up |

Next: before the weekend, list which two questions changed and tell me if you want the exact pooling rule for them written up.