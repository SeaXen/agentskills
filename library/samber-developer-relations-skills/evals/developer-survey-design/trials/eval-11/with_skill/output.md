Next action: pull five numbers from your data (list at the bottom). About 30 minutes. Everything below is ready to paste once you fill the `<...>` slots.

No calibration sample exists, so every number in the report sits on **rung 1: "X% of respondents"**, with n and exact wording. Three of your five plans need a rewrite, one needs a cut, and one is fine with an addition.

## Verdict per planned item

| # | Plan | Verdict |
|---|---|---|
| 1 | "Satisfaction averages 4.1/5" | Rewrite: show the distribution, not the mean alone |
| 2 | Enterprise cares more about SSO | Cannot claim. Enterprise is confounded with the partner channel |
| 3 | Region chart with 7 from Africa | Merge the cell. It is under 10 |
| 4 | 25 verbatim answers | Cut to coded themes plus a few checked quotes |
| 5 | Response rate for the CFO | Undefined for open links. Give the funnel |
| 6 | Weight to 61% Linux | Do not weight. Use it as a bias check |

## 1. Satisfaction

Never print a Likert mean alone. Show all five bars, the exact wording, n, and the "Don't know" rule.

> **How satisfied are you with Greywater Postgres Extension?** `<exact wording>`
> Asked of: `<all respondents | respondents who use it>` · n = `<answered>` · single answer
> 4.1 out of 5 is the mean. Distribution: `<%1 / %2 / %3 / %4 / %5>`. "Don't know" is `<excluded | shown>`.
> Source: Greywater Postgres Extension survey 2026; respondents recruited through newsletter, docs, Discord and a partner mailing; not weighted.

Add one extra cut: satisfaction by source channel. If the channels differ much, say so in the text. Newsletter and Discord respondents are mostly engaged fans, so 4.1 likely runs high.

Do not write "developers are satisfied", and do not print a margin of error.

## 2. Enterprise and SSO

You cannot write "enterprise cares more about SSO." The reading rule says a segment gap counts only when:
- it is large enough to change a decision, and
- its direction holds in every source channel that clears the subgroup minimum.

Here, nearly all 38 enterprise respondents came from the partner mailing. Company size and channel are tangled together. The partner list may simply be people who care about SSO.

Do these checks:
1. Count enterprise respondents outside the partner channel. If that count is under your self-set minimum, the gap is **untested**. Never call it "agreeing".
2. Confirm the minimum was set before analysis. If it was set after seeing the 38, say so in the methodology.
3. Compare enterprise and startup inside the partner channel only, if both groups clear the minimum there.

Publishable rewrite:

> Among the 38 enterprise respondents, SSO ranked as the top blocker. Among the 610 startup respondents, it ranked fifth. Almost all enterprise respondents came through the partner mailing, so we cannot tell whether company size or recruitment channel explains the gap. We treat it as untested.

Decision use: this is a lead, not a roadmap input. If SSO is a real roadmap decision, run a targeted follow-up with enterprise users. Ask it as a rank question with the same wording. Also hide any cross-tab cell under 10, such as enterprise × region.

## 3. Region chart

Seven is under the 10-respondent floor. Merge Africa into a bigger cell, for example "Africa and other regions (n=`<x>`)". Check the other slices too.

Add to the caption: "Regions under 10 respondents are merged." Name the language bias if the survey is English only, because speakers less comfortable in English are under-sampled. Do not use the chart to say anything about Africa.

## 4. Voice of the community

Never publish raw open text. Publish themes, then a few quotes checked for names, employers, products and incidents.

1. Code all open answers into themes by hand or with model help checked by a person. State which in the methodology.
2. Show each theme with its count and the share of open-text answerers.
3. Under each theme, add one or two quotes. Strip names, employers, and rare role-plus-country-plus-size combinations.
4. Say how you picked the quotes. Chosen quotes are illustrations, not a sample.

If you keep more than a handful, each of the 25 must pass the check above. Do not label them with role, company size, or region unless that group has at least 10 respondents. Section caption:

> Themes coded from `<n>` open-text answers (`<hand | model-assisted, person-checked>`). Quotes are selected to illustrate each theme and are not representative. Names and identifying details removed.

## 5. Response rate for the CFO

No honest rate exists. An open link has no denominator, and a forwardable partner link has none either. Publish the funnel per channel.

| Channel | Views (if known) | Started | Completed | Kept |
|---|---|---|---|---|
| Newsletter | `<>` | `<>` | `<>` | `<>` |
| Docs | `<>` | `<>` | `<>` | `<>` |
| Discord | `<>` | `<>` | `<>` | `<>` |
| Partner mailing | `<sends, if partner shares>` | `<>` | `<>` | `<>` |
| Total | | `<>` | `<>` | 1,204 |

Add the cleaning counts: qualifiers, speeders, straight-liners, duplicates, bots. Say how many each removed.

Sentence for the CFO:

> This survey used open links, so a response rate does not exist. 1,204 responses were kept out of `<started>` starts. The funnel above is the honest measure. Response rate also predicts bias poorly, so it would not tell you how far to trust the numbers.

If the partner shares its send count, you may show sent, started, and completed for that channel as a funnel. Do not call it a survey response rate.

## 6. Weighting to 61% Linux

Do not weight. Installs count machines, not people. One developer may run many Linux CI containers, so 61% overstates Linux people. Weighting to that figure is rung 3 on a bad benchmark. It also fixes only OS, not the fan bias.

Do this instead:
1. Show the two distributions side by side: telemetry 61% Linux, respondents 40%.
2. Check whether telemetry is opt-in and who it covers, and say so.
3. Publish key results (satisfaction, top blockers) split by Linux vs non-Linux. Readers see how sensitive the numbers are.
4. Name it in the bias sentence.

> Respondents under-represent Linux: 40% of respondents use Linux, against 61% of telemetry-reporting installs. Installs count machines, not people, so we do not weight to them. Key results by OS are in the appendix.

## Methodology section (paste, then fill)

> **About this survey**
> `<Organisation>` ran the Greywater Postgres Extension survey from `<start>` to `<end>`. It was open to anyone; we invited people through our newsletter, docs, Discord, and a partner mailing sent by `<partner>`. `<N>` people started it, `<N>` completed it, and we kept 1,204 after removing `<rules, with counts>`. No random calibration sample was run.
>
> **Who answered:** respondents over-represent engaged community members and users of our own channels, and under-represent Linux users (40% of respondents against 61% of telemetry installs), `<non-English speakers if single language>`, and people outside our channels. The partner mailing brought mostly enterprise respondents. Percentages describe respondents, not all Postgres extension users. Results are not weighted.
>
> Each chart shows the exact question, who was asked, and how many answered. Multi-select totals exceed 100%. "Don't know" answers are `<excluded from | shown in>` percentages. Groups under 10 respondents are merged or hidden. Subgroups under `<self-set minimum>` are not shown. This minimum was set `<before | after>` analysis. No margin of error is shown because the sample is opt-in.
>
> `<Who could see and change the questionnaire, including the partner.>` The full questionnaire is `<link>`.

## Before publishing

1. The partner mailing may make the partner a joint controller. Check the privacy notice named the source list, and check who answers rights requests.
2. Have your data-protection contact review the quote section and the open-data plan, if any.
3. If anyone later quotes "X% of developers", rewrite it to "X% of respondents".

## Send me these five things

1. Satisfaction distribution (1 to 5 counts), overall and by channel.
2. Enterprise n by channel, and the date you set the subgroup minimum.
3. Funnel per channel: views, started, completed, kept, plus cleaning counts.
4. Exact wording of the satisfaction and SSO-rank questions.
5. Is this a one-off or edition one of a yearly series? If yearly, freeze these questions as the core module.

Step 1 of 6 done: claims fixed. Next: I fill the captions and the methodology once you send items 1 to 4.