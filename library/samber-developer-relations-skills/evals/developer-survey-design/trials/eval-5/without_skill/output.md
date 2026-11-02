# Saltmarsh Developer Survey trend slide

**Marketing can use the Go claim, with a footnote. They can't use the Kubernetes claim as written.**

## Slide (ready to paste)

**Title:** Go keeps growing as the primary language for Saltmarsh developers

**Headline stat:** Go as primary language: **31% → 36%** (+5 points)

| | 2025 | 2026 |
|---|---|---|
| Respondents (completes) | 2,410 | 1,880 |
| Go as primary language | 31% | 36% |

**Footnote (on slide):** Same question wording and position both years. 2026 adds two new recruitment channels (docs banner, partner newsletter). The +5 difference is outside sampling error (±2.9 pts at 95%). Samples are self-selected, not representative of all developers.

**Do not put Kubernetes on this slide as a trend.** Use the replacement below.

## Why Go passes

- **Wording and position:** both years are identical, so there is no instrument change.
- **Sampling error:** 31% at n=2,410 gives ±1.9 pts, and 36% at n=1,880 gives ±2.2 pts. The 95% interval on the difference is about ±2.9 pts, so +5 is a real shift in these samples (z ≈ 3.4).
- **Remaining risk:** the sample mix changed. If docs-banner and partner-newsletter respondents skew Go, part of the +5 is audience change, not adoption change.

**Check before publishing (about 10 minutes):** compute Go share for newsletter and Discord respondents only, in both years. Then choose the wording:

- **Like-for-like channels also show about +5:** keep "Go adoption up 5 points."
- **Like-for-like shows a smaller rise (say +2):** headline the like-for-like number, and mention the full-sample figure in the footnote.
- **Like-for-like shows no rise:** drop the claim. The full-sample number then reflects the new channels, not growth.

## Why Kubernetes fails

"44% → 52%" compares two different measurements.

1. **Different question.** "Which of these deployment targets do you use?" is not "Where do you run Saltmarsh in production?" The first asks about any use, including dev, test and side projects. The second asks only about production.
2. **Different base.** The production screener removed people who don't run Saltmarsh in production. The 52% is a share of production users, not of all respondents. It likely runs higher than an all-respondent share, because production users skew toward orchestrated infrastructure. That would mean the 8 points are partly or wholly an artifact, but we can't tell which direction or how much.
3. **Different position.** Question 5 versus question 12 changes context and fatigue effects. Earlier answers prime later ones.
4. **Different sample.** The same channel-mix caveat as Go applies. Here it stacks on the instrument change, so it can't be separated out.

The sampling-error math (±3.0 pts on the difference) says nothing about this. Sampling error covers random noise, not a changed question and base.

## What marketing can say about Kubernetes

Pick one:

- **Safe now:** "**52% of Saltmarsh production users run it on Kubernetes**" (2026 survey, n = production respondents). It's a point-in-time fact, not a trend. Put the production-screener n on the slide.
- **Trend, if the data allows:** check whether last year's Q5 respondents can be narrowed to production users. If last year had any production-use question, or a "use in production" qualifier, recompute 2025 on that base. Compare it to 2026's 52%, and compare the option list too. If the base and options match, a trend is defensible. If not, there is no trend.
- **Not safe:** "Kubernetes adoption up 8 points." It will be quoted, challenged, and lose credibility for the Go number too.

## Message to send marketing

> Go: yes, ship "Go up 5 points" (31% → 36%). I'm running one like-for-like check on newsletter and Discord only, and will confirm today.
>
> Kubernetes: please don't use "up 8 points." We changed the question wording, moved it behind the production screener, and so changed who's counted. 44% and 52% measure different things. Use "52% of production users run Saltmarsh on Kubernetes" instead. If we can rebuild last year's number on a production-only base, we may get a real trend later.
>
> Next survey: keep wording, position and screener fixed on any question we want to trend.

## Method note for the appendix

- **Sample sizes:** 2,410 (2025), 1,880 (2026).
- **Recruitment channels:** 2025 was newsletter and Discord. 2026 adds a docs banner and a partner newsletter.
- **Sample type:** self-selected, so no population inference.
- **Intervals:** simple-random-sample 95% intervals, which are optimistic for a convenience sample.

## Rule for next edition

Lock wording, order, and screener position for any question marketing wants to trend. Report channel-level splits alongside the headline.