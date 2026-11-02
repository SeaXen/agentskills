**No, your CTO is wrong. Don't bin the survey.** Keep it, and report it as a set of different samples, not one number.

## Why the 20-30% rule fails

- Response rate is a risk signal, not a validity test. What matters is whether responders differ from non-responders on the things you measure.
- A 70% rate from a biased frame is worse than a 12% rate from a random one. A high rate also gives no protection if the people who skip are the ones you care about.
- Studies comparing low-rate and high-rate surveys of the same population often find similar results on most questions. I'm recalling that from memory (Pew's 2006 comparison of a 25% and a 50% rate is the one I remember), so verify the citation before you quote it.
- Online surveys in a developer community commonly land at 2-15%. Your 2% newsletter yield is ordinary.
- A gift card draw raises completes. It does not fix bias, and it can make it worse:
  - It attracts prize-seekers.
  - It attracts duplicates and bots.
  - It adds legal overhead, because prize draws have rules that vary by country.

## What your four numbers can claim

You only have one computable response rate.

| Source | Invited | Completes | Rate | What it is |
|---|---|---|---|---|
| Newsletter | 41,000 | 820 | 2.0% | Self-selected, engaged subscribers |
| Docs banner | unknown | 310 | none | Self-selected readers |
| Discord | unknown | 140 | none | Self-selected, most engaged members |
| First-launch prompt | 2,000 (random) | 240 | 12.0% | Probability sample of new desktop users |

- **Newsletter:** 820 / 41,000 uses the sent list. If you have the delivered or opened count, state which denominator you used.
- **Docs banner and Discord:** no rate exists. Do not invent one.
- **First-launch sample:** the 95% margin of error at n=240 is about ±6.3 points worst case, and it only covers sampling error. Nonresponse is the bigger risk. It also covers new desktop users, not your whole community.
- **Pooling:** the 1,510 total is 54% newsletter, so a pooled result is mostly the newsletter's view. Don't headline it.

## What to put in the report

1. **Headline.** Answer each question per source, never pooled.
2. **Method and denominators.** Add the table above. Say plainly which sources have a rate and which don't.
3. **Representativeness.** State that three of four channels are self-selected and skew toward engaged users. Only the first-launch arm is random, and it covers new desktop users.
4. **Self-selection check.** For every question asked in all channels, compare each channel to the random arm. Large gaps show where self-selection moves the answer. Matching answers support using the bigger samples.
5. **Non-response check.** Compare the 240 completers to the 1,760 non-completers on what you already know, such as OS, app version, country and plan. Report any gaps. If they are large, weight the results on those variables.
6. **Data hygiene.** Dedupe across channels by email or user ID. Someone in the newsletter and Discord could have answered twice.
7. **Claims allowed and not allowed.**
   - Allowed: "Among engaged newsletter readers, X%." "Among new desktop users, X% ± 6 points, with 12% response."
   - Not allowed: "X% of the Quillhaven community," or any statement about all users.
8. **Limitations.** Include engagement bias, nonresponse in the random arm, no rate for two channels, and a cross-sectional snapshot.
9. **Recommendations.** Keep the random in-app sample as your anchor. Next round:
   - Add one reminder to the random arm.
   - Track impressions on the docs banner.
   - Record invite counts per channel.
   - If you test an incentive, test it on a random arm only, and compare its answers to this round's.

## CTO message

> The 20-30% figure isn't a validity threshold. What matters is who responded versus who didn't. We have a random sample at 12% and three self-selected channels. We'll report them separately, check them against the random sample, and rerun narrowly. A gift card draw alone won't fix bias.

**Next, in under 5 minutes:** pull the OS, version and country for the 2,000 invited users. That is step 5, and it is the single most persuasive piece of evidence for your CTO.