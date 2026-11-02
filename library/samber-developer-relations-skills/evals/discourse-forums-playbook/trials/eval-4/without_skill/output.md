Don't sign off on any of the three as written. The agency has skipped the diagnosis. The cheap checks below may explain the zero traffic, and two of the three recommendations carry real risk.

## Verdict

| Agency ask | Verdict | Why |
|---|---|---|
| Move to `/community` | ❌ Not now | Weak evidence, high cost, and it fixes nothing if the cause is indexing or content. |
| QAPage on every category | ❌ No | It is wrong for Announcements and Feature Requests. It risks a structured-data manual action. |
| Auto-generate ~200 topics from docs | ❌ No | It matches Google's scaled-content-abuse policy and would damage the forum itself. |

## 1. Subfolder vs subdomain

- Google says it treats subdomains and subfolders as equivalent for ranking. The "subfolders rank better" claim is anecdotal and comes from case studies with survivorship bias.
- A subdomain forum with zero traffic usually has an indexing or content problem. A different URL path doesn't fix that.
- The migration is costly:
  - Discourse supports a subfolder install, but it needs `DISCOURSE_RELATIVE_URL_ROOT`, a rebuild, and a reverse-proxy rule on the main site. It is also a recurring upgrade-pain point.
  - You would need to 301 every URL and expect a temporary ranking dip.
  - The forum has been indexed for 8 months with little to lose, so the downside is small. The upside is also unproven.
- A subfolder is a reasonable choice later, once the forum has traffic worth consolidating and you have confirmed the cause isn't something else.

## 2. QAPage schema everywhere

- Discourse already emits `DiscussionForumPosting` markup on topics. The `discourse-solved` plugin adds Q&A markup for topics with an accepted answer.
- QAPage is only valid for pages that pose one question with user-submitted answers. Announcements and Feature Requests aren't that, and marking them up is a mismatch between markup and visible content. Google can respond with a manual action that removes rich results.
- Google has also been cutting back on rich-result types. Check the current Q&A eligibility in Search Central before you spend effort on it.
- Do this instead: install `discourse-solved` and enable it only on support and Q&A categories. Then confirm the markup in the Rich Results Test on one solved topic.

## 3. Auto-generated topics from docs

- Topics that restate docs pages are duplicate, thin content. That fits Google's scaled-content-abuse policy, which applies regardless of whether a human or an LLM wrote them.
- They also don't help the community. Real users get a forum seeded with bot posts that nobody answers.
- The docs already rank, or can. Duplicating them splits that signal.
- Do this instead:
  - Seed 20–30 real threads from support tickets, Discord or Slack questions, and GitHub issues. Use the real wording, with accepted answers.
  - Link from the docs to the matching threads.
  - Add "Ask the community" links on error pages and docs pages.

## What to check first (about half a day)

1. **Search Console**: add `community.pellucid.dev` as its own property. Compare "Indexed" with "Discovered, not indexed" and "Crawled, not indexed".
2. **Crawl blockers**: confirm these Discourse settings:
   - `login required` is off.
   - `allow index in robots txt` is on.
   - No `noindex` header or tag is served.
   - `robots.txt` doesn't disallow the forum.
3. **Sitemap**: check that Search Console received the sitemap, and that `/sitemap.xml` and `/robots.txt` resolve.
4. **Content volume**: count public topics with 2+ replies. Fewer than ~50 indexable, substantive threads is normal for a young forum with near-zero impressions.
5. **Links in**: count referring domains and internal links from pellucid.dev and the docs. Check for a link in the main nav or footer.
6. **Query fit**: look for impressions with no clicks (a snippet or ranking problem) versus no impressions (an indexing or content problem).

## What I'd sign off on Friday

1. Approve only the diagnostic audit above, with the agency delivering Search Console findings.
2. Approve `discourse-solved` on Q&A categories only.
3. Approve a seeding plan using real threads, plus docs-to-forum links.
4. Defer the subfolder move until the audit shows no other cause, and revisit it in about 90 days.

## Reply to the agency

> We'd like to start with an indexing and crawl audit of community.pellucid.dev (Search Console coverage, robots, sitemap, noindex checks). We're declining auto-generated topics (scaled-content risk) and QAPage on non-Q&A categories (markup/content mismatch). Please send evidence, for example comparable subdomain-to-subfolder migrations with before/after data, if you still recommend the move.

Two caveats: I haven't looked at your live forum or Search Console data, so the audit may point somewhere I haven't guessed. Google's current rich-result support also changes, so verify Q&A eligibility before you rely on it.

If you send the Search Console numbers, I can turn them into a specific diagnosis.