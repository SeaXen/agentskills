# Halvern retry-backoff docs: review of your three fixes

## 1. Verdict

- **Where answers go wrong:** ChatGPT (search on) and Perplexity cite the v2 retries page. v2 and v3 share a title and H1, so a retrieval system can't tell them apart.
- **Pipeline:** search-grounded retrieval, because both assistants show a citation. Page-level fixes can reach this. Your check was one run each, so it is a signal, not a baseline. I haven't confirmed that the same pages fail with search off, which would point to training recall.
- **First two levers:** (a) version identity in the text of every versioned page, and (b) a server-rendered opener on v2 that names the replacement. Fix 3, the 301, I'd drop.

## 2. Your three fixes

| Fix | Verdict | Adjustment |
|---|---|---|
| 1. Rename the v3 title to `Halvern v3 - Retry backoff` | ⚠️ Adjust | Apply the change to every version tree, not only v3. Put the searched term first: `Retry backoff (Halvern v3) \| Halvern Docs`. Put the version in the first heading or the opening line too. |
| 2. Inject an old-version banner from the analytics script | ❌ Replace | Server-render it as the first text in the main content. |
| 3. 301 the v2 retries page to v3 | ❌ Drop | Keep v2 live, with a banner and a link to the v3 page. |

**Fix 1 problems:**
- If only v3 is renamed, v2 keeps the old generic title, which now reads as the unversioned page. That is the page being cited.
- A version prefix puts the version before the term developers search for. Keep the term first and the version after it.
- Changing the title alone leaves the H1 identical. Add `Applies to Halvern v3.x` as the first body line, and the equivalent on v2.

**Fix 2 problems:**
- Many AI fetchers don't run JavaScript, so a banner injected after load is invisible to the readers you're targeting.
- It also depends on the analytics script loading, which ad-blockers and consent tools often prevent.

Ship this opener on v2 above any code:

```html
<p><strong>Deprecated: Halvern v2 is an older release.</strong>
This page is kept for teams still on v2. The current page is
<a href="/v3/guides/retries">Retry backoff (v3)</a>.
<code>OLD_SYMBOL</code> was removed in v3; use <code>NEW_SYMBOL</code>.</p>
```

Details for the opener:
- **Symbol names:** I don't know your removed retry options or methods. Fill in `OLD_SYMBOL` and `NEW_SYMBOL` for both the Ruby and Node clients, using the exact old spellings in code formatting.
- **Status wording:** don't say "end of support" unless v2 has actually reached it.
- **Where to put it:** one template edit covers all v2 pages. Don't style it into the sidebar.

**Fix 3 problems:**
- About 30% of installs still run v2. A 301 sends them to v3 code that doesn't work for them, and they lose the page they need.
- A third-party copy of the v2 content then takes the citation. Don't `noindex` v2 either, for the same reason.
- If you want to change canonical, indexing or redirect posture on the version tree, route that to the docs-seo skill (`samber/developer-relations-skills@docs-seo`). It is a search-indexing decision, not an AI-visibility one.

## 3. Panel and baseline

Run this before you ship anything, or you can't show later that a change worked.

1. **Prompts:** write them the way developers ask: "retry backoff with Halvern", exact error strings, "migrate retries from v2". Take them from tickets and docs search logs. Use one row per client, Ruby and Node.
2. **Answer key:** per prompt, list the correct v3 symbols and config keys and the deprecated v2 forms that must not appear.
3. **Minimum viable size:** 10 core prompts × 5 runs × the 2 assistants (ChatGPT and Perplexity), search on. Add search off on the 5 prompts with the worst answers. This is this skill's default size, not a vendor figure.
4. **Scoring:** score each answer for sources cited, owned page cited, version-correct, deprecated API and invented API. Report pooled rates per prompt family with n and an interval, never a rank.
5. **Why five runs:** repeated runs of one prompt rarely return the same list of sources (independently measured). Your single-run check can't support a conclusion yet.
6. **Agree targets now**, before the baseline runs:
   - zero deprecated-API answers on the three highest-traffic docs tasks, search on;
   - a version-correct rate above baseline, with intervals that separate;
   - an owned-page citation rate above baseline.

## 4. Access checks before editing pages

- Read `robots.txt` and the CDN bot rules per agent. The agents:
  - OpenAI: `OAI-SearchBot` for search, `ChatGPT-User` for fetch.
  - Perplexity: `PerplexityBot` for search, `Perplexity-User` for fetch.
- Check for a CDN "block AI crawlers" toggle that someone outside the docs team turned on.
- Fetch the v2 and v3 retries pages with a plain HTTP client and no JavaScript. Confirm the body text and code blocks are in the HTML.
- Check for `nosnippet` or `data-nosnippet` on code blocks.

## 5. Diagnose each failing prompt

Run these five tests on each failing prompt:
1. Search toggle.
2. Source request.
3. Version probe.
4. Log check for a fetch on the v2 path.
5. Index check: is the v2 URL still indexed?

If search-off answers also use v2 code, that part is training recall. No page edit fixes it quickly. Runtime deprecation warnings in the SDK release can, and so can version-matched docs delivered into agents.

## 6. Lever plan

**Track 1, ships now:**
1. Version in title, first heading and opening line, across all versions (fix 1, adjusted).
2. A server-rendered opener on v2 pages that names the replacement (fix 2, replaced).
3. A two-row old-to-new symbol map in the v2 opener until a full map exists in the migration guide.
4. Update or archive your own old blog tutorials, gists and example repos that show v2 retry code.
5. File feedback reports after the baseline: Perplexity's "Outdated information" and OpenAI's content report. They have no published turnaround, so log the dates.

**Track 2, if the SDK release is yours to change:**
- Runtime deprecation warnings in the final v2 release of the Ruby and Node clients that name the replacement and the docs URL.

**Dropped:**
- The 301 on v2.
- `llms.txt` as a citation lever. Server-log studies find AI search crawlers almost never request it.
- Generic AI-search rewrites: FAQ blocks, added statistics, pages split into fragments.
- Date bumps made to look fresh.

## 7. Measurement plan

- **Control design:** a title and opener template change touches every page, so it destroys your control. Roll it out to one section first, such as retries and the pages around it, and keep the rest as control. Otherwise compare against the baseline, log the model names and dates, and void the comparison if a model release lands in between.
- **Re-run:** run the identical panel 4 to 8 weeks after the last change goes live. Re-crawl and re-index take days to weeks. Training-recall levers show at the next model release.
- **First-party data**, with at least 14 days before you quote a share:
  - referrers from `chatgpt.com`, `perplexity.ai`, `claude.ai` and others, treated as a lower bound;
  - server logs by bot role and version path, verified against vendor IP ranges, using `scripts/ai-bot-log-summary.py --path-prefix /v2/ access.log`;
  - hits on old-version paths with no v3 twin;
  - support tickets tagged "code from an assistant".

## 8. What no docs change fixes quickly

- **Released model weights:** a model that already learned v2 retry code keeps producing it until a later model trains on a corpus where v3 dominates.
- **Outcomes:** citation and ranking changes are pending until the re-run. Page changes can be verified today. Don't promise a lift figure.
- Everything I've said about why assistants pick one source over another is practitioner inference. No vendor publishes a citation algorithm.

## Questions I need answered

These change the lever ranking:
1. Which v2 symbols were removed in v3 for the Ruby and Node clients, and what are their replacements?
2. Is v2 still supported, or only in use?
3. Is there a date this must show by, or is this a standing practice for every release?
4. What can you change: the docs template and build, the CDN bot policy, the SDK release, your own blog posts and example repos?