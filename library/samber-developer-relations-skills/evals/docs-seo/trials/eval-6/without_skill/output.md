**Verdict: reject sprints 1 and 2 as scoped. Recut to ~3-5 days, not 3 sprints.**

## Why HowTo and FAQPage sprints buy nothing

- Google killed HowTo rich results entirely, desktop and mobile, worldwide. Announced 2023-08-08. No exceptions. 310 pages of HowTo markup render zero rich result.
- Google restricted FAQPage rich results to "well-known, authoritative government and health websites" same date. Docs site not in that set. 94 pages of FAQPage markup render zero rich result too.
- Both changes are 3 years old as of today (2026-09-23). Agency quoting "rich-result uplift" off this either uses stale pre-2023 CTR data, or hasn't checked eligibility. Red flag either way.
- Test before you believe me or them: pull any FAQPage-marked page from a non-government, non-health competitor site through Google's Rich Results Test, then search the exact query live. No FAQ dropdown shows. Same test for HowTo, any tutorial site.

## Article sprint: real but small

- Article schema on "everywhere else" pages doesn't produce a distinctive SERP rich result for docs/help content. It mainly feeds Top Stories/Discover eligibility (irrelevant to you) and entity signals (author, dateModified).
- Some value: freshness signal, sitelinks search box context, cleaner entity graph. Not "rich-result uplift" — don't let the agency price it as such.

## What's actually worth doing (cheap, keep)

1. **BreadcrumbList across all 1,800 pages** — still fully supported, drives real SERP breadcrumb display for deep docs URLs. One Mintlify template/partial change, not per-page authoring. Hours, not sprints.
2. **Organization + WebSite schema, homepage only, once.** Entity clarity, search box eligibility.
3. Confirm Mintlify's template layer (`docs.json` / layout partials) before agreeing to any per-page hand-tagging model at all. If templatable from existing MDX frontmatter (title, steps, question headers), this is a build-script job, not 404 pages of manual technical-writer authoring. Sizing the work as writer-hours-per-page is the wrong model regardless of schema type.

## If the real goal is AI-answer citation, not classic rich results

Google's own guidance: structured data **not required** for AI Overviews. Where JSON-LD does help is non-Google engines (ChatGPT, Perplexity, Claude) extracting passages — but the leverage there is content structure, not markup:

- Check `/llms.txt` and `/llms-full.txt` exist — Mintlify auto-generates these on most plans. Verify, don't rebuild.
- Check robots.txt doesn't block GPTBot, ClaudeBot, PerplexityBot, Google-Extended.
- Restructure top-traffic how-to pages into self-contained 40-60 word answer blocks + numbered steps. This is the actual driver behind the Princeton GEO study's +37-40% citation boost — writing quality, not JSON-LD.

This work is legitimate technical-writer time. It's also not what the agency proposed.

## Questions to send the agency before signing anything

1. Name the exact rich result you're targeting for HowTo and FAQ. Show a live Search Gallery link.
2. Show 3 live examples of that rich result appearing today on a non-government, non-health, non-recipe site.
3. Is the uplift estimate based on data from before 2023-08-08?

**Next action:** run one FAQPage-marked competitor page through Google's Rich Results Test (search.google.com/test/rich-results) and search the query live — confirms point 1 in under 5 minutes, gives you the evidence to push back today.