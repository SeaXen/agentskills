**Do this first (about 10 minutes for the first post, about 2 hours for all 30):** set the canonical URL on every dev.to post to your own blog URL.

## What went wrong

1. **Duplicate content, no canonical signal.** The RSS import copied the full text. Unless the feed or the post sets `canonical_url`, dev.to treats its copy as the original.
2. **dev.to has more authority than your blog.** Google has to pick one version of identical text. It picks the stronger domain, so it ranks the dev.to copies above you.
3. **Possible second cause: dev.to sometimes gets crawled first.** Their pages are crawled fast and linked from the dev.to feed, tags and newsletter. If your post was published in the feed before Google indexed your blog, dev.to can look like the original.
4. **The 25% drop matches the loss of rankings on your best tutorials.** Those posts lost their SERP positions and clicks to the copies.

**Confirm the diagnosis (about 20 minutes):**
- Open Google Search Console. Filter to your 30 tutorial URLs and compare clicks and impressions before and after six months ago.
- In Search Console's URL Inspection tool, check "User-declared canonical" and "Google-selected canonical" on a few of these URLs.
- Open the HTML of 3 dev.to copies and look for `<link rel="canonical" href="...">`. If it points at dev.to itself, you have the cause.

## Fix, without deleting any dev.to post

1. **Set the canonical URL on all ~30 dev.to posts.**
   - Open a post, then Edit, then Settings, then "Canonical URL". Paste your blog post URL. Save.
   - Or use the dev.to API. `PUT /api/articles/{id}` with `{"article": {"canonical_url": "https://yourblog/..."}}` and an `api-key` header. This takes about 15 minutes to script for all 30.
   - Check the HTML of 3 posts afterward. The `rel=canonical` tag must point to your blog.
2. **Fix the RSS import so future posts are right.**
   - In dev.to Settings, go to Extensions, then "Publishing to DEV from RSS". Your feed must include the original link. dev.to uses it to set the canonical URL on imported posts.
   - Turn on "Mark the RSS feed posts as drafts". This lets you review each import before it goes live.
3. **Make sure your blog is the canonical on its own side.**
   - Each blog page needs a self-referencing `<link rel="canonical">`.
   - The pages must be indexable: no `noindex`, no robots block, and in the sitemap.
4. **Publish to your blog first, then wait.**
   - Hold each dev.to import for about a week so Google indexes your original first. Request indexing in Search Console for new posts.
5. **Make the copies point back to you.**
   - Add a line at the top or bottom of each dev.to post: "Originally published at [your blog link]". This is a user-facing link and a backup signal.
   - Link to the original from your other pages. Internal links and external mentions help it win.
6. **Ask Google to recrawl.**
   - Use URL Inspection on your 5 best tutorials and click "Request indexing".
   - Optionally, on the dev.to copies of those same 5, do the same if you have access. If not, the canonical will be picked up on the next crawl.

## What to expect

- **Timing:** Google reprocesses canonicals over days to a few weeks. Expect the dev.to copies to drop and your blog to return over 2 to 8 weeks. Recovery is likely, but not guaranteed to hit the old position.
- **Canonical is a hint, not a command.** Google can ignore it if the dev.to page has strong links of its own, or if the content differs a lot. If the dev.to copies still outrank you after 6 weeks, take step 7.
7. **Fallback for stubborn posts.** Rewrite the dev.to version as a short summary with a link to the full tutorial. Or set the dev.to post to `noindex` if you can edit it (dev.to does not offer this for normal users, so it needs a request to their support).

## Check it worked

1. Search `site:dev.to yourusername "exact title"` to list the copies.
2. Compare Search Console clicks week over week for the 30 URLs.
3. Re-check the "Google-selected canonical" in URL Inspection. It must equal your blog URL.

**Next action:** open one dev.to post's settings, paste its blog URL into "Canonical URL", save. Then check its HTML for the canonical tag.