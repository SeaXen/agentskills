# Methodology and reporting

What published developer surveys disclose, the caption and methodology templates, cleaning rules, and rewrites for headline claims.

## Contents

- What published surveys do
- Length anchors
- Disclosure list
- Methodology section template
- Chart caption template
- Cleaning rules
- Headline rewrites
- Claims to refuse

## What published surveys do

| Practice | Model | What it looks like |
|---|---|---|
| Funnel | State of Rust | views, started, completed (76.2% in 2025), published every year |
| Qualifiers and exclusions | Stack Overflow | age, consent and role screeners; about 15,000 responses excluded in 2025; sub-3-minute responses dropped in some editions |
| Calibration sample | Go | a random fraction of editor-plugin users invited; random and self-selected answers compared and shown apart where they differ (Windows use 33-36% random vs 16% self-selected) |
| Weighting with targets | JetBrains | region shares from its own developer-population estimates, a less-biased paid-ad and external-channel subsample as the baseline, employment status, languages, and an ad hoc down-weight of its own users; procedure published, benchmark partly self-estimated |
| Per-chart base | CNCF, Go | wording in the chart title, n on every chart, "don't know" handling stated |
| Bias in plain words | Stack Overflow, JetBrains, Go | "highly-engaged users were more likely to notice the prompts"; "some bias is likely present"; Go's note that self-selected respondents are among the most engaged and experienced, with random-sample results shown apart |
| Precision caveat | Rust | "cannot extrapolate too much from a mere 7 000 answers": a size caveat, never a substitute for the bias sentence |
| Open text | Go, Stack Overflow | hand-coded themes and selected quotes; free text removed from open data |
| Outline review | State of JS | the question outline opened for public comment before launch |

Even JetBrains' weighted results still over-represent its own users' tools, which is why weighting supplements a bias sentence and never replaces it.

## Length anchors

Go: 12-13 minute median. Stack Overflow: median rose from about 15 minutes (2022) to about 21 (2024), with 42% of those answering a feedback item calling the 2025 edition "too long". JetBrains: about 30 minutes on average from a routed 585-question bank. State of JS: 15-20 minutes stated in the invitation.

## Disclosure list

Adapted from the AAPOR Transparency Initiative. A credible report states:

- who ran and who paid for the survey
- the population definition
- data collection dates
- recruitment channels and the number of responses per channel
- the full questionnaire with exact wording, order and routing
- the funnel and every exclusion rule with its count
- weighting variables and benchmark sources, or "not weighted"
- the unweighted base for every subgroup shown
- any interval shown, with the model assumption behind it

## Methodology section template

```
About this survey
<Organisation> ran the <name> survey from <start> to <end>. It was open to anyone; we invited
people through <channels>. <N> people started it, <N> completed it, and we kept <N> after
removing <rules, with counts>. <A random sample of N <surface> users was invited separately;
where their answers differ from self-selected respondents, charts show both.>

Who answered: respondents over-represent <engaged community members / users of our own
channels / English speakers / ...> and under-represent <...>. Percentages describe
respondents, not all <population>. Results are <not weighted | weighted to <benchmark>,
source <...>; unweighted figures are in the appendix>.

Each chart shows the exact question, who was asked, and how many answered. Multi-select
totals exceed 100%. "Don't know" answers are <excluded from | shown in> percentages.
Groups under 10 respondents are merged or hidden.

The full questionnaire is <link>. <Anonymised data, without open-text answers, is available
under <licence> at <link>.>
```

## Chart caption template

```
<Exact question wording>
Asked of: <all respondents | respondents who use X> · n = <answered> · multiple answers allowed
Source: <survey name and year>; respondents recruited through <channels>; not weighted.
```

A chart cropped out of the report and posted alone must still carry this caption.

## Cleaning rules

Write them before fielding, report the count each removes:

- **Qualifiers:** outside the population (for example, never used the product), under the minimum age, declined the notice.
- **Speeders:** completion time below a self-set fraction of the median for the respondent's routed path, such as a third. Stack Overflow has dropped sub-3-minute responses in some editions.
- **Straight-liners:** identical answers down a grid of 6 or more items, combined with a speed flag. Straight-lining alone can be honest.
- **Duplicates and bots:** repeat submissions from one device or near-identical rows; nonsense in open text; impossible combinations (a student with 20 years at a large company).
- **Machine-written and farmed answers** (switch on before launch whenever an incentive is public): one attention or consistency check, one trap option nobody can have used ("FakeTool 3.0"), templated or identical phrasing across open-text answers, pasted text where the tool detects it.
- **Partials:** decide once whether a response that stops after the core module counts. JetBrains keeps partials past a key question.

## Headline rewrites

```
// ✗ "70% of developers prefer our CLI"
// ✓ "70% of the 2,140 respondents who use both the CLI and the console prefer the CLI.
//    Respondents came mostly from our newsletter and Discord."

// ✗ "Adoption of feature X doubled this year"
// ✓ "Among respondents, 31% reported using X (n=1,880), up from 15% last year (n=2,410).
//    The question was unchanged; this year's sample drew more from the docs banner."

// ✗ "Developers are 85% satisfied (±2%)"
// ✓ "85% of respondents rated themselves satisfied or very satisfied (n=1,204). The survey
//    used an open link, so no margin of error applies."
```

## Claims to refuse

| Claim | Why it fails |
|---|---|
| "n=385 gives ±5%" for an open-link survey | Holds only for random samples; AAPOR says no margin of error for opt-in samples |
| "We need a 30% response rate for validity" | No methodological source; response rate predicts bias poorly, and an open link has no rate |
| "Keep it under 5 minutes or nobody finishes" | No study sets an ideal length; published developer surveys run 12-30 minutes |
| "A prize draw will boost responses" | Effects are small and inconsistent; the real cost is compliance and fraud screening |
| "Weighting makes it representative" | Weighting corrects only the variables weighted, toward benchmarks that must exist |
| "Up 3 points since last year" with changed wording or channels | Different instrument or different sample; not comparable |
| "Developers say we are faster than X" in a sales deck | Opinion from a self-selected sample; a performance claim needs a published benchmark |
| "Segment A cares more about Y than segment B" from one channel | Holds only if the gap's direction holds in every channel that clears the subgroup minimum; smaller channels are "untested" |
