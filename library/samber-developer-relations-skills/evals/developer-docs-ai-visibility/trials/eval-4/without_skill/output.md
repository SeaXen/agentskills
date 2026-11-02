# Is the AI visibility methodology sound?

**Verdict: the direction is right, but the design isn't defensible yet.** Monthly cadence, these three engines, and mention rate plus share of voice are all reasonable. As drafted, though, the month-to-month changes would mostly be noise, and a skeptical exec could knock it down in one question. Four fixes matter most: repeat runs, a competitor set, prompts that look like real questions, and a clean testing setup. All of them fit your capacity if you automate collection.

## What's wrong with the draft

1. **One sample per keyword is noise.** LLM answers vary run to run, and list order varies even more.
   - Say the true mention rate is 10%. With 50 single-shot prompts, the 95% interval is about ±8 points, so 10% could read anywhere from 2% to 18%.
   - With 5 runs per prompt (250 samples), the interval narrows to about ±4 points. It's still wider in practice, because runs of the same prompt are correlated.
   - Without repeats, a "rise from 8% to 14%" tells you nothing.

2. **SEO keywords aren't AI prompts.** "vector database" typed into ChatGPT gets a definition, not a ranked vendor list. Your 50 keywords measure how the model handles a bare phrase, not how buyers ask.

3. **Share of voice has no denominator.** You need a defined competitor set (for example Pinecone, Weaviate, Qdrant, Milvus, Chroma, pgvector) tracked in the same responses. Without one you only have a mention count.

4. **Average rank is misleading.**
   - Many answers aren't lists.
   - Rank only exists when you're mentioned, so average rank is survivorship-biased. If you get mentioned more often, mostly at the bottom of lists, average rank gets worse while visibility improves.
   - Rank from a single sample is unstable.

5. **Your work laptop is a contaminated test environment.** Logged-in accounts bring memory, chat history, location, and possibly your own past brand queries. Results then reflect your account, not what a stranger sees.

6. **Roughly 150 manual queries a month eats your budget.** Half a day a week across two writers is about 17 hours a month. Hand-pasting and hand-coding answers would burn most of that and still give you one sample each.

7. **Mention-only tracking misses what docs can act on.** You're Head of docs, so the useful output is which sources the engines cite and what they get wrong about you. The draft logs neither.

8. **One Monday is a fragile snapshot.** Model updates, retrieval changes, or a one-off news item can shift a single day. You also never record the model version or whether web search was on.

## Recommended methodology

**Prompt set (about 50, frozen and versioned)**

Write prompts the way a developer would ask them, and tag each one by intent:

| Bucket | Count | Example |
|---|---|---|
| Category | ~10 | "What are the best vector databases?" |
| Comparison / alternatives | ~12 | "Alternatives to Pinecone for self-hosting" |
| Use case | ~12 | "Which vector DB should I use for RAG over 5M documents?" |
| Stack-specific | ~10 | "Vector database with a good Go client" |
| Problem / how-to | ~6 | "How do I add semantic search to a TypeScript app?" |

- Seed the buckets from your SEO keywords, then validate against sales calls, support tickets, and community questions.
- Keep a separate set of about 10 branded prompts ("What is Brindlecoast?", "Brindlecoast vs Qdrant"). Report them separately and leave them out of share of voice. They test accuracy, not discovery.
- Change the set at most once a quarter, with a version number, so trends stay comparable.

**Collection**

- Run each prompt 5 times per engine. That's 50 × 3 × 5 = 750 responses, plus the branded set.
- Use the official APIs with web search on, scripted. Check current pricing, but expect the API cost to be modest. Perplexity's API returns citations directly.
- Add a small manual spot-check in the consumer apps (logged out or a fresh account, memory off, fixed region). The UI and API can behave differently, so this guards against drift between them.
- Run over a 2–3 day window rather than one Monday.
- Store the raw response, model name and version, search on/off, date, and citations. You can then re-code history when your definitions change.

If neither writer can script this, you need an engineer for roughly a day, or a tracking tool. That's the one resource ask.

**Coding the responses**

- Mentions: automated match on an alias list (Brindlecoast, brindlecoast.com, package names for the Python/Go/TS clients).
- Competitors: same method, same list.
- Accuracy and framing: an LLM judge draws a sample, and a writer spot-checks about 10% of it each month.
- Tag each response as "answered from training data" or "used live retrieval". The levers differ: training-data presence moves slowly, while retrieval responds to your docs and third-party pages.

**What to report**

1. **Mention rate** per engine, with a confidence interval. Use a bootstrap over prompts, not over runs.
2. **Share of voice** against the defined competitor set.
3. **Citation rate:** how often your domain is cited, and which pages.
4. **First-named rate** instead of average rank, plus the rank distribution where answers are lists.
5. **Accuracy issues:** wrong or outdated claims about your product, languages, or features. These are the most actionable item for your team.
6. **Top cited sources** for the prompts you lose: competitor comparison pages, Reddit, GitHub, and so on.
7. Everything split by intent bucket. Category and comparison prompts are usually where you win or lose.

**Noise rule:** in month 0, run the full set twice in the same week. The gap between those two runs is your noise floor. Don't call a change real unless it exceeds that floor.

## Effort budget

These are my estimates, not measured numbers.

| Phase | Time |
|---|---|
| Setup (prompts, alias lists, script, coding, noise baseline) | ~2 months at half capacity, ~25–30 h |
| Monthly run, QA, and report | ~6–8 h |
| Fixes from findings (cited-page gaps, wrong facts) | the remaining ~9–11 h |

The fixes are the main output. A report that doesn't change anything in the docs is a cost center.

## Optional later additions

- Google AI Overviews and Gemini, because they reach the most searchers.
- Coding assistants (Cursor, Copilot, Claude Code). For a dev tool with three SDKs, "add vector search to my Go service" is a real discovery path. Test it quarterly, not monthly.

## What to tell leadership

- This measures *visibility in AI answers*. It doesn't prove revenue or cause.
- Month-to-month moves smaller than the noise floor won't be called trends.
- Share of voice depends on the competitor set you chose, so state the list.

## Questions that would change the plan

1. Can an engineer script the collection, or do you want a tracking tool?
2. Who is the audience for the numbers (exec, board, marketing), and what decision hangs on them?
3. Which competitors does sales actually meet in deals? That's your competitor set.
4. Do you want branded accuracy tracked, or only discovery?