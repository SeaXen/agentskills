# Does the plan cover it? No.

Two of the three items won't fix the problem you saw, and one can hurt your v3 customers.

## Why the plan misses

ChatGPT showed no sources, so it answered from memory, not from a live fetch. The model learned `ferrowave.connect(url, { group })` from v3 docs, blog posts, GitHub code, and Stack Overflow answers scraped before v4. Search-index controls can't change what a trained model remembers. They only affect tools that browse or retrieve. Changes you make now will reach trained models slowly, if at all.

## Item by item

**1. Canonical tags from v3 to v4: drop or narrow.**
- A canonical tag says "these pages are the same content." v3 and v4 consumer-group pages are not, because the API differs. Google will likely ignore the tag.
- If it is honored, v3 customers who search for a v3 error get v4 pages with the wrong API.
- Google also says not to combine canonical with noindex. The signals conflict, and the outcome is unpredictable.
- Keep canonicals only for pages whose content is genuinely unchanged between v3 and v4.

**2. Noindex the whole v3 tree: don't, at least not yet.**
- About a quarter of paying customers are on v3 and probably find those pages through search. Noindex removes them from search results.
- Noindex doesn't touch model memory, as above.
- Noindex only works if crawlers can fetch the page, so never pair it with a robots.txt block.
- If you want v3 out of search, set a v3 end-of-life date first. Once the date is public, noindex or redirects are defensible. Before that, a visible version label does more good than hiding the pages.

**3. llms.txt listing v4 pages: fine, but low value.**
- It costs almost nothing, so ship it.
- I'm not aware of evidence that major LLM providers use it for retrieval or training. Don't count it as a fix, and don't report it to leadership as one.
- Make it point at the migration guide too, and consider offering `.md` versions of docs pages, since coding agents fetch markdown.

## What to add

1. **Visible version labels on every v3 page.** Put a banner at the top ("You're viewing v3 docs. Client v4 changed this API. See the v4 equivalent"). Also put "(v3)" in the `<title>` and H1. When a model or retriever extracts a snippet, it carries the version with it. This is the highest-impact change for retrieval-based answers, and it keeps v3 usable for customers.
2. **A v3-to-v4 migration page that quotes the removed API verbatim.** Include `connect(url, { group })`, label it "removed in v4", and show the v4 replacement. Retrieval matches on the strings people ask about, and future training data then sees the old call paired with "removed".
3. **A strong v4 page for this exact question.** Title it "Consumer groups in Node (client v4)" with a complete runnable example. Make sure the unversioned docs URL resolves to v4.
4. **A clear runtime error in client v4.** Calling `connect` with `group` should throw a message that names the removed option and links the migration page. Coding agents and developers who paste hallucinated code hit this error and self-correct. This works whatever the model remembers. Check whether v4 already does it.
5. **Package and repo hygiene.** Check the npm README, GitHub README and examples, and shipped type definitions and JSDoc. Coding assistants read `node_modules` and repos. Any v3 snippet left there keeps the problem alive.
6. **Third-party content.** Search for old tutorials, Stack Overflow answers, and blog posts showing `connect(url, { group })`. Post updated answers where you can.
7. **The Python client.** Check whether it has the same removal and the same stale content.
8. **A baseline and a recurring test.** Write 20–30 realistic questions ("set up a consumer group in Node", "retry failed messages in Python", and so on). Run them monthly against ChatGPT, Claude, Gemini, and Perplexity, with browsing on and off. Record whether each answer uses the v4 API and cites your docs. This tells you whether anything worked. It also tells you which failures come from model memory (slow to fix) and which from retrieval (fixable now).

## Set expectations

Parametric memory (what a model learned in training) will improve only as models retrain. The fast wins are in browsing and retrieval answers, plus coding agents reading your package and errors. Tell stakeholders that.

## Questions for you

- Do v3 customers reach docs mainly through search or through in-app links?
- Is there a v3 end-of-life date, or can you set one?
- Does client v4 currently throw a helpful error for the removed `group` option?

These answers decide whether the end-of-life date and noindex timing change.

## Suggested sprint

1. Add the v3 banner and titles.
2. Publish the migration page.
3. Improve the v4 consumer-group page.
4. Add the runtime error.
5. Audit READMEs, types, and examples.
6. Ship llms.txt.
7. Run the baseline test set.
8. Apply canonical tags only where content is unchanged.
9. Hold noindex until the end-of-life date exists.