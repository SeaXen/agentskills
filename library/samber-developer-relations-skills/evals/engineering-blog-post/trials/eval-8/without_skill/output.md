I haven't seen the post. You didn't give a path or paste the text, and I can't use `skill-wip/`. So I can't deliver the tightened prose, the title tag, the meta description or the alt text yet. Below is what is left to do, and what I need from you to do it.

## What I need

1. The post: paste the text or give a path outside `skill-wip/`.
2. The target keyword, or the question a reader would search for.
3. The Contentful field names: the slug, SEO title, SEO description, hero image and body type (Rich Text or Markdown).
4. Whether the post is already a Contentful draft with a URL, or still unpublished.

## What is left

**1. Prose tightening (my part, once I have the text)**
- Edit prose only. Leave the three code blocks, the two benchmark tables and the raw command output byte-identical. Check this with a diff before and after.
- Don't change numbers, units, version strings, identifiers or claims, because a colleague already verified them.
- Cut the usual LLM tells:
  - openers like "In today's fast-paced…" and closers like "In conclusion…"
  - filler such as "it's worth noting", "delve", "leverage", "robust", "seamless" and "crucial"
  - the "not just X, but Y" construction
  - triplet lists used by reflex
  - em-dash overuse
  - headings that restate the paragraph under them
  - sentences that announce what the next one will say
- Read the result aloud. Keep the author's own verbs and specifics. If a sentence only sounds smart, cut it.

**2. Check the pasted output before it goes live (you)**
- Scan the raw command output for hostnames, usernames, home paths, internal domains, IPs and tokens.
- Redact anything you wouldn't want public. A technical-accuracy review doesn't catch this.

**3. SEO fields (I draft, you approve)**
- **Title tag:** about 50–60 characters, with the keyword near the front. Add the brand only if it fits. It can differ from the H1.
- **Meta description:** about 140–155 characters. State what the reader gets, and name the concrete result if it is a benchmark post. No clickbait.
- **Slug:**
  - short, lowercase and hyphenated, with no date and no stop words
  - it must contain the keyword
  - in Contentful, check the slug field's uniqueness validation
  - the slug is part of the URL, so decide it now. If the post is already live under another slug, you need a 301 redirect.
- **H1 and headings:** one H1 only, and H2s that match the sub-questions readers ask.
- **Alt text:**
  - one description per image, about 125 characters or fewer, describing what the image shows
  - if a benchmark table is an image, put its numbers in the alt text or in a text version next to it. Better still, keep the tables as real HTML tables.
  - decorative images get empty alt text
  - in Contentful, alt text usually lives on the asset (its title and description, per locale), not on the entry. Check each asset.
- **Social and structure:** an OG/Twitter image and title, a canonical URL, and 2–4 internal links to related posts. Use Article/TechArticle schema if your front end supports it.

**4. Contentful checks before publishing**
- Preview the entry on the real front end and check four things:
  - code blocks keep their formatting, their language label and their horizontal scroll
  - tables render and don't overflow on mobile
  - the raw output keeps its line breaks
  - Rich Text doesn't turn code into plain paragraphs. If it does, use an embedded code entry or a Markdown field.
- Fill in every required field, including author, date and category/tags.
- Check the status in the entry sidebar: Draft, Changed or Published. Publish the entry, then publish the linked assets, or the images 404.
- If you use scheduled publishing, set the time and confirm the timezone.

**5. After it goes live**
- Fetch the live URL and confirm the title, description, canonical, OG image and status 200.
- Check that it appears in the sitemap.
- Request indexing in Google Search Console, and watch impressions and queries after a week or two.

Send me the post and the answers to the four questions above. I'll return the tightened text with the protected blocks untouched, plus the title tag, meta description, slug and alt text ready to paste into Contentful.