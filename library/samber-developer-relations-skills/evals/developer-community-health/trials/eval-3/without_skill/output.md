**Short answer: no, not as-is. The NPS number is wrong (sign flipped, and the sample is far too small to be a point estimate), and the 78% sentiment figure is being mislabeled as something it doesn't measure. Here's the breakdown.**

## NPS: -22 is the wrong number — should be +22

Standard NPS formula: **%Promoters − %Detractors** (passives count toward the denominator, not the subtraction).

- Promoters: 4/9 = 44.4%
- Passives: 3/9 = 33.3%
- Detractors: 2/9 = 22.2%
- NPS = 44.4 − 22.2 = **+22**, not −22.

You computed detractors minus promoters (22.2 − 44.4 = −22.2), which is the formula backwards. That's not a rounding quirk — it flips the story from "net positive among respondents" to "net negative," which is exactly the kind of thing that gets read literally in a QBR.

**Sanity-check tell:** a 78%-positive sentiment score sitting next to a −22 NPS should have set off alarms on its own — those two numbers contradict each other. Correctly signed, NPS (+22) and sentiment (78% positive) point the same direction. When two independent metrics of "do people like us" disagree sharply, that's usually a methodology bug, not a real finding.

**Bigger problem than the sign: n=9 is not usable as a point estimate.** That's a 0.35% response rate off 2,600 members, from a survey you don't say was randomly sampled — likely self-selected (people who felt strongly enough to click), which cuts both ways (fans and the annoyed both over-respond, quiet-satisfied members don't). Treating each response as +1/0/−1 and computing the standard error: SE ≈ 27.8 points, so a 95% CI on that +22 is roughly **−32 to +76**. One person switching from detractor to promoter moves the score by ~22 points. There's no meaningful point estimate here — it's noise dressed as a KPI.

**Recommendation:** either don't put NPS in the QBR this quarter, or present it explicitly as "n=9, directional only, not a tracked metric" — not as a number next to real KPIs. If you want a real NPS, send it to a proper random sample (or all 2,600) and expect responses in the dozens-to-hundreds before trusting the point value quarter over quarter.

## Discord sentiment: 78% positive measures message tone from your most vocal members, not "community sentiment"

It'll read as a customer-satisfaction number in a QBR. It isn't one. Specific gaps:

- **Selection bias.** Only people who post get scored. In a 2,600-member Discord, that's typically a small vocal fraction — a mix of power users/evangelists and people actively troubleshooting a problem. The silent majority (probably most of the 2,600) contributes zero signal either way.
- **Channel mix confound.** If the corpus spans support channels and general/off-topic channels, you're blending "help, this is broken" (skews negative regardless of overall satisfaction) with "lol thanks" banter (skews positive, has nothing to do with product satisfaction). The 78% is as much a function of which channels you pulled from as of actual sentiment. Worth breaking the score out by channel before trusting the aggregate.
- **Message-weighted, not member-weighted (probably).** If a handful of hyperactive users post most of the volume, they dominate the score. Check whether 78% is per-message or per-unique-member — those can diverge a lot.
- **Model validity, unchecked.** Generic sentiment models frequently misread technical support language (negations, terse troubleshooting phrasing, sarcasm) as negative or positive incorrectly. Before quoting 78% in a QBR, spot-check ~30-50 model-labeled messages by hand and see if you agree with the labels. If you haven't validated precision/recall on your own community's dialect, the number has unknown error bars.
- **No baseline.** 78% means nothing on its own without last quarter's number computed the same way. If this is the first quarter running it, say so — it's a baseline, not a trend.

**Recommendation:** report it as "Discord message-level sentiment (Q_, all channels, n=X messages, vocal-member subset)" rather than "community sentiment" — the label matters as much as the number. If you want an actual community-wide sentiment read, that's what the (larger-sample, correctly-signed) NPS-style survey is for, not the passive Discord corpus.

## Bottom line for the QBR

- Fix the sign: NPS from this sample is **+22**, not −22 — but caveat n=9 hard, or drop it this quarter.
- Relabel 78% as **Discord message sentiment**, not community sentiment, and note it reflects your most active posters, not the full 2,600.
- Don't present the two as comparable "community health" numbers without their different methodologies stated — right now they'd look contradictory (78% positive vs. −22 NPS) when in reality, corrected, they roughly agree.