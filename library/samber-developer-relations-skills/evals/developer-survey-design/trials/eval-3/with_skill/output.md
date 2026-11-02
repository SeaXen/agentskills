# Quillhaven survey post-mortem: is the CTO right?

**Short answer: no. Keep the data, don't re-run, and don't add a gift card draw.** The survey is usable. It supports narrower claims than "what developers think", and the report has to say so.

I skipped the full interview because this is a vetting job. I applied the claim ladder from `developer-survey-design` Step 2 and the "claims to refuse" list in `references/methodology-and-reporting.md`.

## Why the 20-30% rule is wrong

- **No methodological source backs it.** Response rate predicts bias poorly. A 30% rate from a skewed invitation list can be more biased than a 12% rate from a random draw.
- **Three of your four channels have no valid response rate.**
  - Newsletter, docs banner and Discord are open links, so "views" is not the same as "people who saw it".
  - Your 2% is completes divided by list size. It measures how much of the list converted, not a response rate, so don't print it as one.
  - Report the funnel instead: views where known, starts, completes, kept.
- **Published developer surveys don't meet that bar.** Go, Stack Overflow, JetBrains and State of Rust are all opt-in. They're credible because they state who answered and show the calibration comparison, not because of a response rate.
- **Your real weakness is who answered.** 1,270 of your 1,510 completes (84%) came from newsletter, docs and Discord. Those channels reach engaged fans. That limits what you can claim, but it doesn't make the data invalid.

## Why not re-run with a gift card draw

- **Draw effects are small and inconsistent.** Evidence for open-link developer surveys doesn't separate a draw from a badge, a donation or no incentive.
- **A draw adds compliance cost.** You'd need contact data in a separate store and sweepstakes rules per jurisdiction. If any respondents or partners are in the EU or UK, it also adds GDPR work.
- **A public incentive attracts bots and machine-written answers.** You'd need fraud screening you may not have.
- **It would likely worsen the bias.** Newsletter readers would still dominate.
- **Re-running discards your best asset.** The 2,000-user random invitation is the one thing most surveys lack.

If you re-run next year, the default is no incentive plus results shared with respondents first. Move to a donation only if the soft launch shows too few completes and the deadline is close.

## What to put in the report

### 1. Headline sentences (rung 1 and rung 2)

- **Rung 1, all respondents:** "X% of the 1,510 respondents…" Always allowed, with n and exact wording.
- **Rung 2, calibration group:** "X% of desktop-app users invited at random on first launch (2,000 invited, 240 completed, 12%)…" Always print the 12% beside the number. A random invitation with 88% non-completion still carries nonresponse bias.
- **Never write** "X% of developers", "of our users" or "of the ecosystem". An opt-in survey can't support those.

### 2. Funnel and source mix (a table, not a "response rate")

| Source | Completes | Share of 1,510 | Denominator to publish |
|---|---|---|---|
| Newsletter | 820 | 54% | 41,000 sent. Opens and clicks if you have them. Never a "response rate". |
| Docs banner | 310 | 21% | Banner views if analytics has them. Otherwise "unknown". |
| Discord | 140 | 9% | Members and link clicks if known. |
| Calibration (random) | 240 | 16% | 2,000 invited, 240 completed (12%). Add started. |
| **Total** | **1,510** | 100% | Minus cleaning exclusions, with counts. |

Add "kept after cleaning" and the count each rule removed: qualifiers, speeders, straight-liners, duplicates, bots. The 1,510 is raw completes.

### 3. The bias sentence (required, in plain words)

> Respondents over-represent engaged Quillhaven community members: 84% came from our newsletter, docs and Discord. They under-represent <non-English speakers, non-desktop users, lapsed users, whoever else you can name>. Percentages describe respondents, not all Quillhaven users or developers.

Write the target population and the sampled population as two separate sentences. The gap between them is the bias the report names.

### 4. Calibration comparison, question by question

- Show the random group (n=240) beside the self-selected group (n=1,270) on every core question.
- Where they differ, show both and say so. Go's Windows figure is the model: 33-36% random vs 16% self-selected.
- Don't claim they "agree" on subgroups below your minimum n. Label those "untested".
- Scope warning: the random group is first-launch desktop users, meaning newcomers on one platform. It calibrates against that population, not against all users. Say this in the report.

### 5. Rules the report states in advance

- **No margin of error.** AAPOR says it doesn't apply to opt-in samples. The calibration group may show sampling error, only with the stated assumption that nonresponse is ignorable.
- **Segment gaps** count only when they're large enough to change a decision and the direction holds in every channel that clears your subgroup minimum. Set that minimum now and label it self-set.
- **Distributions, not Likert means alone.**
- **Chart caption on every chart:** exact wording, who was asked, n, "multiple answers allowed" where true, "Don't know" handling, and "not weighted".
- **Suppress any cell under 10 respondents.**
- **Open text:** publish coded themes, never raw text.

### 6. Methodology section

Use the template in `references/methodology-and-reporting.md`. Fill in:

- Who ran and who paid for the survey.
- Dates and channels.
- Funnel and cleaning rules, with counts.
- "Not weighted."
- The full questionnaire.
- A link to the anonymised data, if you release it.

## Gaps to fill before you write it

1. **Started counts per channel.** You gave completes only, so I can't compute drop-off or the calibration group's started rate.
2. **Banner views.** Pull them from docs analytics. If you can't, write "unknown" rather than guess.
3. **Cross-channel duplicates.** A person may have answered through the newsletter and Discord. Check whether you tagged the source and whether the cleaning step dedupes.
4. **Calibration integrity.** Confirm the 2,000 invitees got single-use tokens kept apart from answers, and that no link was forwardable. If not, say that in the methodology.
5. **Telemetry bias check.** If you have OS, version or region data, compare it with the respondent distributions. Don't weight to install counts.
6. **Language.** If the survey ran only in English, name that gap in the bias sentence.

## For the CTO

Use this line: "Response rate has no methodological validity threshold, and three of our channels have no denominator. What decides credibility is stating who answered and comparing against a random sample, and we have that sample. We publish narrower claims, not no claims."

## Open question

Do you plan to publish the results or quote percentages externally, and are any respondents or partners in the EU or UK? A yes to either makes the privacy notice and the claim rules release blockers, and it pushes prize draws even further down the list.