# Why Google's AI Overviews never show Marrowick's code

Two independent problems each block it. Fixing only one won't help. I haven't seen your live pages, so check the confirmations at the end.

## 1. You told Google not to use the content

`max-snippet:0` is equivalent to `nosnippet`. Google documents that `nosnippet`, `data-nosnippet`, `max-snippet` and `noindex` apply to AI Overviews and AI Mode as well as classic snippets. The competitor's page is allowed as a source and yours isn't, so it gets cited.

Two details make it worse:

- **`max-snippet:0` covers the whole reference section.** It applies to all text on those pages, not only the code blocks. The prose around your samples ("Reverse geocoding converts coordinates to an address…") is excluded too, so the section can't be quoted at all.
- **`data-nosnippet` may be doing nothing.** Google honours it only on `<span>`, `<div>` and `<section>`, and it's unreliable when injected by JavaScript. If it's on `<pre>` or `<code>`, or added client-side, it's likely ignored. That wouldn't matter, because `max-snippet:0` blocks everything anyway.

## 2. The samples probably aren't in what Googlebot sees

"All there if you open the page" holds only after a click. Googlebot renders the page but doesn't click tabs. A sample fetched from a JSON endpoint on click never enters the rendered DOM, so it's never indexed. That would be true even with no robots directives.

Related risks, which depend on how the app is built:

- **No indexable URL per topic.** A single-page app with hash routes or client-only routing may expose no distinct, server-rendered URL for "reverse geocode". Fragments (`#...`) aren't indexed as separate pages.
- **A blocked endpoint.** If the JSON endpoint's host or path is disallowed in `robots.txt`, the samples won't load even if something triggers the fetch.
- **A non-200 shell.** SPA routes that return a soft 404 or a generic shell can hurt indexing.

## 3. The scraper protection doesn't work

Scrapers don't obey `nosnippet`, and they can call your public JSON endpoint directly. The directives only constrain Google, which is the one audience you want. Anything publicly readable can be copied, and code samples are meant to be copied.

## Fix

1. **Remove `max-snippet:0` from the reference section.** Set `max-snippet:-1` explicitly, or drop the directive.
2. **Remove `data-nosnippet` from code blocks.** Keep it only on content you really don't want quoted.
3. **Pre-render the samples.** Build them into the HTML at build time (SSG/SSR). Put all language panels in the DOM, not fetched on click.
4. **Give each task its own URL.** For example `/guides/reverse-geocoding`, with a visible default sample, one or two sentences of explanation, and the request and response above the fold. Per-language views like `/guides/reverse-geocoding/python` are fine, with canonicals.
5. **Move scraper defence to where it works.** Use rate limits and bot management on the JSON endpoint, a license notice, and a ToS clause. Don't use SEO directives for it.
6. **Measure after recrawl.** Re-inspect the pages, then expect weeks before AI Overviews change. Selection isn't guaranteed even once the content is crawlable.

## Confirm before changing anything

- **Search Console, URL Inspection, Live Test:** open "View tested page" and check the rendered HTML. If the `reverse_geocode` code isn't there, cause 2 is confirmed.
- **Robots directives:** run `curl -sI <url>` and view the page source. Look for `X-Robots-Tag` and `<meta name="robots">`. Check whether `max-snippet:0` is in the HTML or injected by JavaScript.
- **Endpoint access:** check `robots.txt` against the JSON endpoint's host and path.
- **Where the attribute sits:** grep the built HTML for `data-nosnippet` and note which element carries it.

Send me the rendered HTML for one reference page and the response headers, and I can say which of these is active.