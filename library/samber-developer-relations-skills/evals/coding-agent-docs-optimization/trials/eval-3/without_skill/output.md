## The OKR number

**Don't put 95% in the doc — the task mix makes that number nearly meaningless, not just optimistic.**

Your 9 tasks aren't one population, they're two:

| Bucket | Tasks | Why first-try rate differs |
|---|---|---|
| Basic REST CRUD | 3 | Extremely well-represented pattern in every model's training data. If your docs have complete request/response examples and auth flow, agents nail this most of the time. |
| Deep/novel (streaming replay, custom partitioner, schema-registry failover) | 6 | Proprietary semantics, stateful setup, non-obvious failure modes, edge cases that only show up in your own docs — not general web knowledge. Success here is gated almost entirely by how complete *your* docs are, not by model capability. |

Realistic first-try ranges, based on how agentic coding benchmarks split between "common pattern" and "novel/stateful system" tasks:

- Basic CRUD: 80–95% first-try.
- Deep integration tasks: 15–45% first-try, and that's *with* decent docs — worse if the docs are missing error tables, state diagrams, or worked failure-recovery examples (which is exactly what schema-registry failover and custom partitioner docs tend to lack).

Blended (weighted 3:6), that lands around **45–60%**, not 95%. Put **55%** in the doc as the Q1 target if you want one blended number — it's a stretch goal, not a floor, and it's defensible if challenged.

Better than one blended number: **split it into two KRs.**

- KR1: ≥90% first-try success on basic CRUD integration tasks by Q1.
- KR2: ≥40% first-try success on deep integration tasks (streaming replay, partitioner, schema-registry failover) by Q1.

Reasons to split rather than blend:

- A single 95% target is achievable by gaming task selection (weight the eval toward CRUD) without improving the docs that actually matter.
- The deep tasks are the whole reason this OKR exists — a headcount ask built on docs work should be judged on the hard 6, not diluted by the easy 3.
- 95% on the deep bucket specifically is not credible for Q1 on any current agent, regardless of doc quality — that bucket depends on distributed-systems edge cases (partition rebalancing timing, failover state consistency) that no amount of prose documentation fully eliminates; a 95% target there would set the team up to visibly miss.

**Before finalizing either number: run the eval now**, not guess it. Take your actual 9 tasks, run them against Claude/GPT/Gemini agents against your current docs, count first-try passes, and use *that* as the baseline instead of a benchmark-derived estimate. It's a half-day of work and turns this into a real number instead of a defensible-sounding guess — which matters more once it's in an OKR someone will be held to.

## The 66% traffic stat

**⚠️ I couldn't verify this figure — I don't have live web access in this session, and I don't recognize "66% of documentation traffic is AI agents" as a specific, sourced figure from memory. Do not put it on the budget slide until you've pulled it from a named, citable source or your own logs. An unsourced flattering number is a bigger credibility risk in a headcount ask than a smaller, sourced one — the first question in the room will be "where's that from," and "I saw it somewhere" kills the slide's credibility along with everything else on it.**

Two things to check before you trust any version of this stat, sourced or not:

1. **"AI traffic" almost always means AI *crawlers*, not AI *agents*.** Public reports on bot traffic (Cloudflare, Fastly, Imperva-style bad-bot reports) that show large percentages are usually counting GPTBot/ClaudeBot/PerplexityBot/CCBot-style scrapers indexing content for training or retrieval-augmented answers. That's a completely different thing from a coding agent actively fetching your docs mid-task to complete an integration. Citing a crawler-traffic stat to justify "we need headcount so agents can complete integration tasks" is a category error — it would draw exactly the wrong follow-up question ("so are we optimizing for crawlers or for agentic task completion?") and the honest answer undercuts the ask.
2. **Even a real industry number isn't your number.** Aggregate web stats mix news sites, blogs, e-commerce, and docs together. A docs-specific site can legitimately have a very different bot/human split than "the web" as a whole — could be higher or lower.

What actually holds up on a budget slide: **your own docs server logs, filtered by user-agent, over the trailing 30–90 days.**

- Pull request logs for your docs subdomain.
- Bucket by user-agent: known AI crawlers (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Anthropic-AI, Google-Extended, Bytespider) vs. known agent/IDE tools (Claude Code, Cursor, Copilot, Windsurf — check for their UA strings or referrer patterns) vs. plain human browsers.
- Report the number you actually found, with the date range and methodology in a footnote. A specific, sourced, smaller number ("41% of our docs requests last quarter came from identified AI user-agents, per our own CDN logs, Jun–Aug 2026") is more persuasive to a budget committee than an unsourced 66%, because it survives someone asking "how do you know."

If you run that log pull and it comes back near 66%, great — use it, with the citation to your own analytics as the source. If it comes back at 20%, that's still a real, useful, honest number for the slide, and it won't blow up on you in Q&A the way an unverifiable one will.