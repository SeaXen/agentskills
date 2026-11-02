# dev.to is outranking your blog because the 30 imports probably aren't canonicalised

**Short answer:** the dev.to copies most likely carry no `canonical_url` pointing at your blog. Google treats the two pages as duplicates and picks dev.to, which is the stronger domain. You can fix this without deleting anything: set the canonical on each live post, tick the canonical option on the RSS source, and verify in Search Console.

I read the playbook and its reference file but couldn't inspect your live dev.to account or blog. The diagnosis below is the likely cause, and the checks in step 1 confirm it.

## What went wrong

1. **Canonical is opt-in on the RSS import** [code default]. The "Mark the RSS source as canonical URL" box is not ticked by default. If nobody ticked it six months ago, every imported post canonicalises to itself on dev.to. Google then sees two identical pages and picks the stronger domain.
2. **Your best tutorials were hit first.** They rank well, so they are the pages where a second copy competes.
3. **The imports kept the original post date** [code default]. If nobody deleted the `date:` line before publishing, the posts went out back-dated and outside the signed-in feed, permanently. They got almost no on-platform reach, so the duplicate was all downside.
4. **Possible mismatch with the playbook's fit verdict.** For a team with an engineering blog and docs-style content, the verdict is *syndicate only*. That means canonical-ticked import, new posts only, and the best drafts published one at a time. Publishing about 30 posts at once is the opposite.

Two caveats:
- A canonical tag is a hint to Google, not a command. It usually works when the two pages are near-identical, but expect weeks, not days.
- The 25% drop may not be entirely dev.to. Step 1 separates the causes.

## Fix, in order

**1. Confirm the cause (30 minutes)**
- In dev.to Settings → Extensions → RSS, check whether "Mark the RSS source as canonical URL" is ticked.
- Open 3 of the 30 published posts and view source. Look for `<link rel="canonical">`. If it points at `dev.to/...`, that's the bug.
- In Search Console, pull the top 30 queries for your tutorials, then compare clicks and impressions before and after the import started. Check that the drop is concentrated on the pages that have dev.to copies. If the drop is site-wide, something else is also going on, such as an algorithm update or a technical change.
- Check your own blog pages for a `noindex` tag or a canonical pointing somewhere unexpected. Each blog page must be indexable and self-canonical.

**2. Set the canonical on all 30 published posts (about 2 hours)**
- Open each post's editor and add `canonical_url: https://yourblog.com/the-original-post` to the front matter. Use the exact blog URL, including trailing-slash style and https.
- Do this for every post, starting with the best tutorials that Google is currently ranking above your blog.
- In the same pass, delete any `date:` line, since the date came from the import.
- Keep the content identical to the blog version. Divergent copies weaken the canonical signal.

**3. Fix the source so it doesn't recur**
- Tick "Mark the RSS source as canonical URL" now, and note the date you did.
- Point the import at your DEV **organization**, not a personal account. Posts under the organization get the sidebar CTA and keep the backlink exemption.
- Imports land as drafts. Publish only the best ones, one at a time. Leave the rest on the blog.

**4. Clean up hygiene on the 30 posts**
- Set the AI tier on each post: Hand Written, AI-Assisted or Fully Autonomous.
- Check that any post naming your product is human-written, and add an affiliation line: "I work on {product}; this post uses it, and the trade-offs section covers where it falls short."
- Look for removed tags or moderator comments, and fix the posts against the tag rules.
- Don't re-post anything. A repeat makes it worse.

**5. Help Google reprocess**
- Request indexing in Search Console for your 10 most important blog URLs.
- Make sure your sitemap is current.
- Add one internal link from a related blog page to each of the top tutorials.
- Recheck rankings at 2, 4 and 8 weeks.

## If it doesn't work

If dev.to still outranks you after about 8 weeks with correct canonicals, the options that keep the posts live are:
- Unpublish (not delete) the 5-10 competing tutorials back to draft. Published posts can be moved back to drafts and restored later, so this is reversible.
- Keep the long-tail posts live and the best tutorials blog-only.

I'd do this only after step 5 has had time to work.

## Going forward

| Item | Rule |
|---|---|
| Cadence | Weeks 1-2: earn first by commenting on 3-5 posts a week in your tags, with no links. Week 3: wire syndication. Weeks 3-8: one full post every 1-2 weeks, answering every comment within 24 hours. |
| Which posts | New posts only. Ship best tutorials to dev.to with canonical set from day one. |
| Hours | Under 2 hours a week: comments plus new-post syndication only. |

## Metrics

- Blog clicks and impressions for the 30 tutorial URLs (Search Console), weekly.
- Which URL Google shows for each query: the blog or dev.to.
- Referral sessions from dev.to to the canonical page, and CTA clicks.
- Hygiene, with a pass threshold of zero: removed tags, spam labels, moderator comments, AI-disclosure notes.

## Questions that would sharpen this

1. Was the canonical box ticked? Step 1 answers that.
2. Did all 30 posts go out under a personal account or the organization?
3. How many hours a week can someone spend on dev.to?

The playbook's rule that only one question be asked at a time bends here, because you asked for the full answer.