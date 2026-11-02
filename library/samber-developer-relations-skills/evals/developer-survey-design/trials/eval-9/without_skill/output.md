**No. Don't use it as written.** Reword the claim before it goes on slide 3. That takes about 10 minutes.

## Why the sentence fails

The sentence says "58% of backend developers." The survey can't support that.

1. **Self-selected sample.** The survey was open-link and promoted through Nimbusline's newsletter, Discord and conference talks. Those channels reach people who already care about serverless. People who run Wasm in production are over-represented there, so 58% likely overstates the real figure.
2. **No weighting.** Nothing corrects the sample toward the actual backend developer population. Six weeks of fielding doesn't fix that.
3. **The margin of error is invalid.** ±1.8% is the formula for a random sample at n≈3,104. A self-selected sample has no valid margin of error. The number gives false precision. Drop it, or put "unweighted, self-selected" next to it.
4. **Population claim.** "Backend developers" reads as all backend developers. The sample is Nimbusline's audience.
5. **Question wording.** "Do you run WebAssembly workloads in production today?" is fine. Some respondents may count edge functions, Cloudflare Workers or Fermyon as Wasm without knowing it. Others may count hobby or internal use as "production". Treat the number as "say they run Wasm in production", not verified usage.
6. **The headline number itself looks high.** Independent developer surveys usually put Wasm production use well below 58%. That gap is a further sign of audience skew. A skeptical enterprise buyer will notice it.
7. **Attribution risk.** The report belongs to a vendor that sells serverless. Buyers discount vendor-run surveys.

## What the slide can say

**Option A: recommended.** Keep the number and name the sample:

> "58% of respondents to Nimbusline's 2026 State of Serverless survey who identified as backend developers (n=3,104) said they run WebAssembly workloads in production. Self-selected, unweighted sample."

Put the second sentence in a footnote if space is tight. Don't cut it.

**Option B: safer in front of skeptical buyers.** Make the number a signal of early adopters:

> "Among serverless-engaged backend developers, a majority now report running WebAssembly in production (Nimbusline State of Serverless 2026, n=3,104)."

**Option C.** Find a second source, ideally a randomly sampled or weighted survey, and cite both. This is the strongest option. It's also the slowest.

## Rules for the slide

- Drop "±1.8%". Don't replace it with any other margin.
- Don't write "now", "most" or "the majority of backend developers" without the sample qualifier.
- Don't use the number as evidence of market adoption in claims, sizing or competitor comparisons.
- Link the methodology page in the speaker notes. Sales will get asked about it.
- Check the report's terms of use for citation or reuse limits.

## Next action

Send Option A to the sales team and have them replace slide 3's text. If they push back on the footnote, show them point 3 and point 6.

I haven't read the full report. I only have your summary of the methodology page. Do you want me to check the report's own caveats section? Those could change the wording.