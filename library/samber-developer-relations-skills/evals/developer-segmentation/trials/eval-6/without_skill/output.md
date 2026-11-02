## Sanity check: the three numbers don't compose into a segment size

**Verdict: the math is broken, not just optimistic.** You're adding two supply-side catalogue counts to your own product's install count and treating the sum as a population of buyers. None of the three is a count of people, and none isolates the niche Loomstack actually sells to.

### Why each number fails on its own

**2.1M models on the hub** — this is a cumulative artifact count since 2016, not a headcount. It's dominated by:
- Duplicate variants of the same handful of base models (a single Llama/Qwen release spawns hundreds of GGUF/AWQ/LoRA/quant re-uploads, often from the same few prolific accounts)
- Bot/automated uploads and abandoned repos
- Every ML domain — vision, speech, tabular, robotics — not just LLM applications

The number of *distinct people* who've ever pushed a model is a small fraction of 2.1M, and the number who are actively building evaluated LLM applications is smaller still.

**940K datasets** — same category error. It's a marketplace catalogue size, spans all ML domains, and tells you nothing about how many people need to evaluate an LLM app.

**380K/month downloads of your own package** — this isn't a market-size input at all. ⚠️ It's your own current usage, which means including it in a market-size sum double-counts customers you already have as if they were untapped opportunity. It's also inflated: PyPI download counts count every `pip install`, including CI/CD reinstalls (no default local cache on ephemeral runners → every build re-pulls), Docker rebuilds, and mirrors. Distinct-human-triggered installs are typically a fraction of raw downloads — for a testing/eval library that lives in CI pipelines, real unique monthly users could plausibly be 10-30% of the raw number, so more like 40K-115K, not 380K.

**The combination error:** you're summing two "how big is the marketplace" numbers with one "how much do people already use my thing" number. They measure different objects (artifacts vs. installs), at different funnel stages (external catalogue vs. your own product), across a scope broader than your ICP (all of ML vs. LLM-app evaluation specifically). There's no valid operation — sum, average, or otherwise — that turns those three into "addressable segment of ML engineers."

## What actually sizes the segment

Your real ICP isn't "ML engineers" — it's narrower in one direction (people building/shipping *LLM-powered applications*, evaluation-conscious) and broader in another (most of them are regular software/backend engineers bolting an LLM call onto a product, not classically-titled "ML engineers"). Size it as a funnel from the total developer population down:

| Layer | Definition | Estimate |
|---|---|---|
| Global professional developers | All software devs | ~30-40M |
| → build LLM-powered features (RAG, agents, chat, copilots) | Not just using Copilot to write code — shipping a product with an LLM in it | ~15-20% → **~5-7M (TAM)** |
| → evaluate output quality with any structured process | Test sets, scored eval loops, automated grading — vs. manual spot-checking | ~20-30% of the above → **~1-2M (SAM)** |
| → would adopt a dedicated third-party eval harness | Vs. in-house script, free-tier-only tooling, or "good enough" as-is | ~10-20% of the above → **~100K-350K (SOM)** |

**Segment size: TAM ≈ 5-7M, SAM ≈ 1-2M, realistic near-term SOM ≈ 100K-350K.**

These developer-population and adoption-rate figures are working estimates from general market knowledge, not numbers I pulled live just now — WebSearch wasn't available in this session. Before this goes in a deck, replace the layer-1/2/3 percentages with real figures from Stack Overflow / GitHub Octoverse / SlashData Developer Nation (base developer population) and a genAI-adoption survey (LangChain State of AI, Menlo Ventures, a16z, or Retool) for the "build LLM apps" and "evaluate formally" splits — those move the estimate by 2-3x depending on the year and definition used.

## Where your real traction number lands

Your corrected ~40K-115K real monthly PyPI users sits inside the SOM band (100K-350K) — a meaningful chunk of the *realistic* near-term buyer population, not a rounding error against an imaginary 3M-strong market. That's a genuinely strong data point. It's just a different, much smaller, and much more defensible claim than "2.1M models exist, therefore huge market" — and it's the one worth leading with to investors, because it's evidence of actual pull, not catalogue size of a marketplace you don't sell into.