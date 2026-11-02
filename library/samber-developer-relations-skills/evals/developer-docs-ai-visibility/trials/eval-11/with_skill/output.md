# Why Google's AI Overviews show a competitor's snippet and not Marrowick's code

## Verdict

1. **Two self-inflicted blocks hit the same code.** `data-nosnippet` plus `max-snippet:0` tell Google not to use your code or page text in AI Overviews. Separately, click-loaded JSON tabs leave no code in the HTML that crawlers and AI fetchers read. Either one alone could produce this symptom.
2. **This is a retrieval problem, not a training-recall problem.** AI Overviews run on Google's Search index. Fixing the pages can change the answer, and the fix has no model-release lag.
3. **First two levers:** remove both snippet controls on the reference and how-to pages, then server-render the code into the HTML. Measure with a prompt panel before and after.

I haven't fetched docs.marrowick.com, so everything below is diagnosis from what you described. The checks that confirm it are listed at the end.

## What's wrong

### 1. The snippet controls remove you from the answer on purpose

- Google vendor docs say a page must be indexed and snippet-eligible to appear in AI Overviews or AI Mode. That claim is vendor-documented.
- `max-snippet:0` is equivalent to `nosnippet` for this purpose. It stops Google using the page's text in snippets and in AI features. You set it on the reference section, which is where "reverse geocode" lives.
- `data-nosnippet` on every code block carves the code out even on pages where the rest of the text is allowed.
- "The content is all there if you open the page" doesn't matter. Being visible to a person and being eligible for Google's answer are separate. You opted the code out of the second.
- The competitor's snippet appears because theirs is the only eligible code for that question.

### 2. The code probably isn't in the HTML at all

- Your code lives in tabs that load from a JSON endpoint on click. A crawler never clicks, so the tab content never loads for it.
- Googlebot does run JavaScript. Many AI fetchers do not, and on-click loading hides content even from renderers that do.
- A plain HTTP fetch of a single-page React app typically returns an empty shell with no body text and no code. This is the "docs invisible without JavaScript" failure mode.
- Fixing the snippet tags alone may change nothing for the other assistants. Those fetchers won't see the code either.

### 3. The scraper defence never worked

- `nosnippet` and `data-nosnippet` only govern Google's own display features. A scraper ignores them.
- The tabs' JSON endpoint is public. Anyone can fetch your samples directly, so the block stops the one reader you want and none you don't.
- You've paid in AI visibility and bought almost no protection.

## Fix plan

Ordered by value per effort. Rows 2 and 3 come from the pipeline diagnosis, not from this skill's lever table.

| # | Change | Effort | Why |
|---|---|---|---|
| 1 | Delete `max-snippet:0` and every `data-nosnippet` on code in the reference and how-to pages | Hours (config and template) | Restores snippet eligibility |
| 2 | Server-render or statically generate code blocks into the HTML. Ship the default tab's code, ideally all tabs, in the initial response. Keep the JSON call only for progressive enhancement. | A build change | Crawlers and no-JS fetchers see the code |
| 3 | Give "reverse geocode" its own URL and page, with a heading naming the task and the call in the opening lines, per language client. Tabs that hide a language behind a click should become anchors or separate URLs. | Per page | An addressable page can be cited |
| 4 | Put the current API version in the title, first heading and opening line | One template edit | Version identity in page text |
| 5 | Protect samples at the CDN or WAF if scraping really hurts: rate limits, bot management. Add a license notice. | Config | Real scraper control, which snippet tags never gave you |

If a legal or business reason still demands blocking Google's AI features, `nosnippet` is the only lever that does it. In that case, accept that you'll lose AI Overviews citations for those pages. Don't expect both outcomes.

## Verify before and after

1. **Rendering check.** Fetch three key pages with `curl` and no JavaScript. The reverse-geocoding code should appear in the response body. If it doesn't, cause 2 is confirmed.
2. **Snippet check.** Inspect the response headers and meta tags for `max-snippet:0`. Inspect the page source for `data-nosnippet` on code blocks.
3. **Access check.** Read `robots.txt` and the CDN bot rules. A "block AI crawlers" preset that disallows `Google-Extended` also removes you from grounded Gemini answers. Flag any such rule. Googlebot and AI Overviews are unaffected by that token.
4. **Index check.** Search Google for the reverse-geocode page and confirm it's indexed. Search Console will show whether impressions fell around the date the tags shipped. That date correlation is first-party evidence worth pulling.

## Measure the result

- **Baseline first.** Build a panel of about 10 developer-phrased prompts, such as "how do I reverse geocode with Marrowick" and the exact error strings. Write an answer key from the correct endpoint, parameters and current version. Run each prompt 5 or more times per assistant, with search on. Report pooled rates with n and intervals, never a single run.
- **Control design.** The snippet and template change touches many pages. Roll it out to one section first and keep another as control. Otherwise compare against the logged baseline and void the comparison if a model release lands in between.
- **Re-run horizon.** Re-run the same panel 4 to 8 weeks after the last change goes live. Retrieval fixes can show up in that window.
- **First-party signals.** Collect at least 14 days of Search Console and log data before quoting any number. Clicks from AI Overviews arrive as ordinary Google organic traffic.
- **Targets to agree now:** the owned page cited, and the code shown, on the reverse-geocode prompt family, above the baseline with separating intervals.

## What no docs change fixes quickly

- Citation and ranking outcomes are **pending**. Re-crawl and re-index run on Google's schedule, days to weeks. Shipped page changes are verifiable today, but I can't promise a lift or a date.
- If the competitor's snippet comes partly from older training data in other assistants, only a later model release changes that. The Overviews symptom you described is a search-index problem and should respond to the fix above.

## Questions that would sharpen this

1. Are the snippet controls applied site-wide through a CDN or a framework default, or only in templates you control?
2. Which languages do the tabs cover, and is one language the default?
3. Do you have Search Console impression data from before and after the change?
4. What scraping harm triggered this? Copied samples, API abuse, or competitor lifting? The answer decides what real protection looks like.