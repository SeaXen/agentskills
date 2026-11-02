## The sitemap failure and the noindex plan are two symptoms of the same root cause — page over-generation. Fix the generator, not the tags.

### 1. Why Search Console can't fetch the sitemap

Two protocol limits, both blown simultaneously:

- **50,000 URLs per sitemap file.** You have 62,400 in one file — invalid by spec, not just "large."
- **50MB *uncompressed* per sitemap file.** The limit applies to the decompressed content, not the 4MB you serve — your 71MB blows it by 42%. Gzipping harder doesn't help; Googlebot decompresses before it checks anything else.

"Could not fetch" at this size is almost always Googlebot giving up parsing an oversized/over-count file, not a network or gzip-header problem. Compression ratio is a red herring here.

**Fix, independent of the noindex decision:**
- Split into multiple sitemap files, each ≤50,000 URLs and ≤50MB uncompressed.
- Reference them from a `sitemap_index.xml`.
- List **only** canonical, indexable URLs in it — no noindexed or canonicalized-away pages. Mixing those in is itself a quality signal problem: Google has to crawl each one just to reconfirm "yes, still noindex," which burns the crawl budget you're trying to protect.

### 2. Blanket noindex on `/reference/` is the wrong call

It's one tag applied to two different problems that need two different fixes:

| Problem | What it actually is | Right tool |
|---|---|---|
| One page per schema field | Genuinely thin — a page can't say much about a single field | Eliminate the URL, don't just noindex it |
| One URL per SDK language, identical prose | Duplicate, not thin | Canonicalize, don't noindex |

Noindex doesn't solve either cleanly:
- It still requires crawling all 62,400 URLs to see the tag (unless you also `Disallow` in robots.txt, which then blocks canonical signals too) — no crawl-budget savings.
- It permanently forfeits any reference page that *should* rank — API reference is high-intent developer search ("Osmiq create customer endpoint," "Osmiq webhook signature field"). It's also the exact content shape AI answer engines (ChatGPT, Perplexity, Claude) like to cite verbatim as the canonical "how to call this API" source — noindexing the whole tree forecloses that channel too, not just classic SERPs.
- It's reversible-in-name-only: nobody revisits 62,400 noindex tags once applied. The consultant's fix becomes permanent by default.

### 3. The actual fix: collapse the URL count at the source

- **One URL per endpoint/resource/schema**, not per field. Fields become a table or `#anchor` section on that one page — same content, zero new crawlable URLs.
- **One URL per endpoint**, not per SDK language. Language selection becomes a client-side tab (JS toggle, no URL change) instead of 6 near-identical pages. If deep-linkable per-language URLs matter for existing backlinks, keep them but `rel=canonical` the 5 secondary ones to the primary.
- This alone takes 62,400 down to roughly (endpoints × schemas), likely low hundreds to a few thousand — an order of magnitude smaller, and now every remaining page has substantive, unique content worth indexing. No blanket noindex needed once the fragmentation is gone.

### 4. Sequencing

1. **Now:** shard the sitemap into an index of ≤50k-URL/≤50MB files; strip anything not meant to be indexed.
2. **Short term:** canonical the 6-language duplicates down to 1 primary variant per endpoint.
3. **Medium term:** rebuild the doc generator to emit one page per endpoint with fields as sections and languages as tabs.
4. **On cutover:** 301 (not noindex, not 404) the old field-level and secondary-language URLs to the new consolidated page + anchor — preserves existing backlinks and any AI-citation history instead of discarding it.
5. **Last:** once redirects are live and confirmed, `Disallow` the retired URL patterns in robots.txt to stop them being crawled at all.

Net verdict: don't noindex the tree — shrink it. The consultant's fix hides a symptom Google is right to flag; the actual defect is the generator producing 6× and field-level fan-out where one canonical page per endpoint would do.