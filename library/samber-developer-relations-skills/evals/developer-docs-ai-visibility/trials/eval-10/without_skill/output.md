# Adjustments to your three fixes

Your diagnosis fits: two pages with identical titles and H1s give an AI answer engine nothing to tell them apart, and the older page usually has more history and backlinks. Fix 1 is right but incomplete. Fix 2 won't work as designed. Fix 3 would hurt the 30% of installs still on v2.

## 1. Rename the title: keep it, but change both pages

- **Rename v2 too.** v2 is the page being cited, so its title and H1 need to say "v2". Renaming only v3 leaves the cited page unchanged.
- **Change the H1s as well as the titles.** Retrieval systems often quote the H1 or the first heading as the citation text.
- **Use one title pattern across the site, with the topic first.** For example:
  - v3: `Retry backoff (v3, current) | Halvern Docs`
  - v2: `Retry backoff (v2, legacy) | Halvern Docs`
  - Your proposed `Halvern v3 - Retry backoff` drops the "Docs" suffix. It also puts the version ahead of the topic, which makes your titles inconsistent with the rest of the site.
- **State the scope in the first paragraph of each page.** For example: "This page covers Halvern v3 (Ruby client 3.x, Node client 3.x)." Answer engines quote body text, not only titles.

## 2. Banner injected by the analytics script: don't

- **Most AI crawlers don't run JavaScript.** Bots such as GPTBot, OAI-SearchBot and PerplexityBot generally read raw HTML, so a banner added after load is invisible to the systems you're trying to influence. Users with ad blockers also won't see it, because analytics scripts get blocked.
- **It causes layout shift.** A banner added after load pushes the content down and hurts CLS (Cumulative Layout Shift).
- **Render the banner server-side or at build time** in the v2 template, as plain HTML at the top of `<main>`. Link it to the same page in v3 (`/v3/guides/retries`), not to the docs home.
- **Add machine-readable signals in the `<head>` of each v2 page:**
  - `<link rel="canonical" href="https://docs.halvern.dev/v3/guides/retries">`. Use this only where the v2 and v3 content is substantially equivalent. Google may ignore canonicals between pages that differ.
  - Drop the v2 URLs from `sitemap.xml` and list only v3.
  - List v3 only in `llms.txt`, if you publish one.
- **Don't add `noindex` to v2.** Your v2 users still need to find those pages.

## 3. 301 the v2 retries page: don't, unless v2 is end-of-life

- **v2 users would land on the wrong docs.** About 30% of installs are on v2. If the Ruby or Node retry options, defaults or backoff formula changed in v3, a 301 sends them to instructions that don't match their version. That is a support-ticket risk, and users will blame the docs.
- **It breaks the version switcher.** A v2 reader can no longer reach v2 retries from the v2 nav, and the page becomes the only v2 page that redirects.
- **A 301 is fast, but there's a cheaper way to get the same result.** Use a stable `/latest/` alias (for example `/latest/guides/retries`) that always serves v3. Point external links, READMEs, the Ruby and Node client READMEs, and your sitemap at the alias.
- **Keep the 301 for later.** Use it when v2 reaches end-of-life, or for a v2 page whose content is identical to v3.

## Check before you ship

- **Make sure v3 can be cited at all.**
  - Fetch the v3 page with `curl` (no JS) and confirm the full content is in the HTML.
  - Check `robots.txt` for blocks on AI user agents.
  - Check that v3 is in the sitemap.
  - If v3 is client-rendered or blocked, titles won't help. Find this out first.
- **Treat "identical titles" as a hypothesis.** Page age, backlinks and the lack of any v3 signal could all matter. Your fixes address the title and the missing version signal, but not the backlinks.
- **Measure before and after.**
  - Save the exact prompts and answers you used in your check.
  - Re-run them weekly for four to six weeks. Recrawl lag varies by engine, so one early re-check proves nothing.
  - Track which URL gets cited, and whether the answer matches v3 behavior, not only which URL appears.
- **Check the links that point at v2.** Update internal links, README links and blog posts to point at v3 or `/latest/`.

## Suggested order

1. Ship the server-rendered v2 banner, both titles and H1s, the opening version-scope sentence, the v2 canonical, and the v3-only sitemap.
2. Add the `/latest/` alias and repoint your own links to it.
3. Re-run the citation check after two to four weeks.
4. Add a 301 only for pages that are identical between versions, or once v2 is retired.