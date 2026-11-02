**Next action:** pull the Go share for newsletter and Discord completes only, in both years. It takes about 20 minutes if last year's responses carry channel tags. Until that is done, neither marketing line ships.

## Verdict

| Claim | Verdict | Why |
|---|---|---|
| "Kubernetes adoption up 8 points" | ❌ Not comparable | Wording, position and base all changed. |
| "Go adoption up 5 points" | ⚠️ Held | Wording and position match, but the source mix changed. It ships only if the like-for-like check passes. |

The trend rule is that a claim needs unchanged wording, unchanged position and a similar source mix. Kubernetes fails all three. Go fails the third.

**Kubernetes (44% to 52%)**
- Last year's Q5 asked "Which of these deployment targets do you use?" of everyone.
- This year's Q12 asks "Where do you run Saltmarsh in production?" of production users only.
- Those are different questions asked of different bases. Production users plausibly lean toward Kubernetes, so the 8 points may be screener effect alone.
- The new docs banner and partner newsletter change the sample too.
- Calling it "adoption" is also wrong. The figure is a share of respondents who chose an answer.

**Go (31% to 36%)**
- Same wording and same position, so the instrument is comparable.
- The sample is not. Last year was newsletter and Discord. This year adds a docs banner and a partner newsletter.
- Docs visitors and a partner's audience plausibly skew toward Go, so some or all of the 5 points may be new-channel mix.
- This is an opt-in survey, so no significance test applies. Don't print a margin of error.

## The check that decides Go

1. Filter both years to newsletter and Discord completes only.
2. Compute the Go share for each year and each channel separately. Record the n for each.
3. Apply the reading rule below.

**Reading rule (set before looking at the numbers).**
- Publish the trend only if the gap is large enough to matter and its direction holds in newsletter and in Discord separately.
- Both channels must clear your self-set subgroup minimum. Pick it before you look at the numbers.
- Show the docs banner and partner newsletter as "untested". Never show them as "agreeing".

**Prerequisite.** Last year's data needs a source tag per response. If it has none, the check is impossible and Go is "not comparable" too.

## Slide

**Title:** Saltmarsh Developer Survey, 2nd edition: what we can compare

**Left panel: Go as primary language (use this version if the check passes)**
- Headline: "Among newsletter and Discord respondents, Go as primary language rose from **X%** to **Y%**."
- Fill X and Y from the like-for-like cut.
- Caption: "What is your primary programming language? Asked of: all respondents from newsletter and Discord · n = [2025] and [2026] · single answer · Source: Saltmarsh Developer Survey 2025 and 2026; not weighted. This year's full sample, including docs banner and partner newsletter: 36% (n = 1,880)."

**Left panel, fallback if the check fails**
- Headline: "36% of 2026 respondents name Go as their primary language (n = 1,880)."
- Footnote: "Not compared with 2025: the recruitment mix changed."

**Right panel: Kubernetes (use this version either way)**
- Headline: "**52%** of respondents who run Saltmarsh in production run it on Kubernetes (n = [Q12 base])."
- Caption: "Where do you run Saltmarsh in production? Asked of: respondents who run Saltmarsh in production · n = [Q12 base] · multiple answers allowed · Source: Saltmarsh Developer Survey 2026; not weighted."
- Footnote: "The 2025 deployment question was worded differently and asked of all respondents. The two years are not comparable."

**Footer, on every chart so it survives cropping:** "Respondents came mostly from our newsletter and Discord, plus a docs banner and a partner newsletter this year. They over-represent engaged community members. Percentages describe respondents, not all developers."

## What marketing can say

- ✅ "52% of respondents running Saltmarsh in production run it on Kubernetes."
- ✅ "36% of respondents name Go as their primary language."
- ✅ After a passing check: "Among newsletter and Discord respondents, Go as primary language rose from X% to Y% year over year."
- ❌ "Kubernetes adoption up 8 points"
- ❌ "Go adoption up 5 points"
- ❌ Anything saying "developers" instead of "respondents"

## Fix for edition 3

Treat the deployment-target question as a core module. Keep the exact wording, position and base for every future year. Ask production deployment as a new question, not a replacement. If you want a Kubernetes trend next year, run the old Q5 wording alongside Q12 this once, before the next field window.

## Needed from you

1. Q12 base n (production users only).
2. Go share by channel for 2025 and 2026, if last year's responses were tagged.
3. Do you want a fallback slide only, or both versions?