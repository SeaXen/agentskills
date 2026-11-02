**Yes, suggest the blog as a source.** It's the standard route, and it works from your RSS feed. A small blog can be declined or sit in the queue for a while, so submit it in good shape and have a fallback.

I wrote this from memory of daily.dev's flow and didn't check their live docs. Their menu labels may differ slightly.

## Steps

1. **Check the feed first.** Open the Hugo feed, normally `https://gopherlog.dev/index.xml`, and confirm:
   - It's valid. Run it through a feed validator.
   - Links are absolute.
   - Every item has `pubDate`, a title and a description.
   - The `<head>` has `<link rel="alternate" type="application/rss+xml" href="...">`. Hugo's default templates usually include it.
   - If your RSS only has summaries, that's fine. daily.dev links readers back to your site.
2. **Check each post's social metadata.** Every post needs an `og:image` and `og:description`, because daily.dev shows a cover image and summary. Posts without an image look weak in the feed and are more likely to be rejected.
3. **Submit the source.** In daily.dev, find "Suggest a new source" (it's in the sources/feed menus, or search the site for "submit source"). Paste the blog URL and the RSS URL.
4. **Wait for review.** A human reviews submissions, so it can take days to weeks. They look for:
   - Developer-focused content.
   - Original writing, not reposts.
   - Regular updates.
   - No pure promotion.

   Go performance deep-dives with benchmarks fit this well.
5. **Claim the source once it's live.** daily.dev has a flow for blog owners to claim or contact them about their source. Look for it on the source's page. Claiming gives you the creator view and lets you fix wrong metadata.

## Fallback while you wait, or if declined

- **Post links by hand.** Each new post, you can share the link on daily.dev yourself, either on your profile or in a relevant Squad. It's manual, but it works from day one.
- **Make a small Squad** for Go performance and post each article there.
- **If declined,** the rejection usually names the cause, such as a missing image, too few posts or a broken feed. Fix that and resubmit.

## What to expect

At about 2 posts a month, your posts won't reach many people through the feed unless they get upvotes early. daily.dev ranks on early engagement and tags, so the first hours matter. Ranking depends on the title and cover image, so spend time on both. Treat daily.dev as one distribution channel next to Hacker News, r/golang and Go Weekly. It won't replace them.