# Parallax Metrics — striking-distance extraction plan + impressions correction

Scope note: this covers the striking-distance pull and the "fix existing pages" workflow only (SKILL.md steps 3 + 8-9, scoped to Tier 1 data). It doesn't expand into net-new topic discovery — that needs your supported-axes and adoption-mode answers first, which you haven't given me. Say the word if you want that layer added.

## 1. What to request

This is the Google Search Console Search Analytics API case (`searchAnalytics.query`), since 16 months matches GSC's retention window exactly. If your console is different, the shape below still applies — adapt field names.

**Pull queries joined to pages, not queries alone** — you need the landing page to catch cannibalization and to route each query to the right fix target.

```json
POST https://searchconsole.googleapis.com/webmasters/v3/sites/sc-domain:parallaxmetrics.io/searchAnalytics/query
{
  "startDate": "2025-05-20",
  "endDate": "2026-09-19",
  "dimensions": ["query", "page"],
  "dimensionFilterGroups": [
    { "filters": [{ "dimension": "page", "operator": "contains", "expression": "docs.parallaxmetrics.io" }] }
  ],
  "rowLimit": 25000,
  "startRow": 0,
  "dataState": "all"
}
```

Notes on the request itself:

- **rowLimit maxes at 25,000, defaults to 1,000.** Set it explicitly — the default silently truncates.
- **Paginate on `startRow`** in increments of 25,000 until a response returns fewer rows than requested. 16 months of query×page pairs on a docs site will very likely exceed one page.
- **Use `dataState: "all"`**, not the default fresh-only state, or you lose the tail of the 16-month window to the rolling data-freshness cutoff.
- **Filter to the docs subdomain/path at request time**, not after — the domain property will otherwise return rows for marketing pages, blog, app UI, etc. mixed into the same set.
- Position comes back as a metric, never a filter — there is no server-side way to ask for "position 5-20 only." Pull wide, cut client-side (below).
- The API's own reference is explicit that it "does not guarantee to return all data rows but rather top ones" — treat whatever lands as a floor on real demand, not a census.

## 2. Filtering to position 5-20

After the full pull lands:

1. Compute average position per (query, page) row as returned — GSC already averages it over the date range, no extra math needed.
2. Keep rows where `5 <= position <= 20`. That's the striking-distance convention this skill uses — proven demand, unwon ranking. It's a convention, not a measured cutoff; widen it if your SERP has more than 10 organic slots worth competing for (time-series DB docs often compete against Stack Overflow and vendor comparison content past slot 10).
3. Drop rows with fewer than ~3 impressions/month average — at 16 months that's under ~50 impressions total, too thin to trust the position average, which GSC itself computes as a noisy daily blend of wherever you happened to rank.
4. Keep clicks and impressions per row alongside position — you'll need both for prioritization in step 3.

## 3. What to do with the landed rows

1. **Join check first.** Group by query; flag any query with more than one distinct landing page. That's two of your own pages splitting one search intent — fix the cannibalization (canonicalize, merge, or differentiate on-page) before doing anything else with that query, because pushing rankings on a page that's competing with your own sibling page wastes the work.
2. **Normalize near-duplicate queries.** Strip version numbers, casing, and pluralization (`"parallaxmetrics retention policy"` vs `"parallax metrics retention policies"`) and cluster. Run the merge test from SKILL.md where you can inspect live SERPs: count shared URLs in the top-10 organic set between two candidate queries — 7-10 shared = one page, 4-6 = separate pages in one cluster, 2-3 = cross-link only, 0-1 = unrelated.
3. **Tag every surviving cluster with evidence**, not just a number: source = GSC query report, count = total impressions/clicks for the date range pulled, date = export date, label = **Measured**. That's what makes the list auditable later instead of a number nobody can retrace.
4. **Route each cluster to a fix.** For striking-distance queries this is almost always "update existing page," not "write new page" — the page already ranks, something specific is capping it at 5-20. Per cluster, name the specific weakness: stale content, no runnable example for the query's exact intent, thin coverage of a failure condition the query implies, wrong page targeted by internal links. Genuinely unwinnable ones (a reference lookup Google itself owns, e.g. generic "time series database" definitional pages) go on a do-not-target list with the reason — don't quietly drop them, log the refusal.
5. **Prioritize the fix queue** by impressions × (1/position) as a rough proxy for "value left on the table," then sanity-check the top 20 by hand against business proximity (a page-2 query for `"parallaxmetrics vs influxdb"` matters more than one for a niche config flag, even at equal impressions).
6. **Re-pull on a cadence**, not once. Position 5-20 is a moving target — re-run this same request monthly and track which clusters crossed into position 1-4 (your movement metric) versus which regressed.

## 4. The "412,000 impressions" number

Don't refresh it "the same way" — the method itself is the defect, not the staleness. Flag this to whoever owns that reporting line.

**Why summing query rows is wrong:** GSC withholds low-volume/rare queries from the query-dimension report for privacy. That's not a rounding effect, it's rows that never appear at all. Any total built by summing the `query` dimension is therefore a floor on real impressions, not the real number — and the gap between that floor and the truth grows with site size and long-tail depth, which means the undercount itself has probably gotten worse since the last person ran this, not just the raw total shifted. The skill this plan follows is explicit on this point: query rows must never be summed into a site total.

**What to request instead for a trustworthy total:**

```json
{
  "startDate": "2025-05-20",
  "endDate": "2026-09-19",
  "dimensions": [],
  "dimensionFilterGroups": [
    { "filters": [{ "dimension": "page", "operator": "contains", "expression": "docs.parallaxmetrics.io" }] }
  ],
  "dataState": "all"
}
```

Dropping the `query` dimension entirely (or using `["page"]` alone if you need it broken out per page) returns GSC's own aggregated total — no per-query privacy suppression applies to the aggregate, so nothing gets silently dropped. Cross-check against the Search Console UI's Performance report filtered to `docs.parallaxmetrics.io`, which uses the same aggregated path, not a client-side sum.

**Report it as two numbers, not one:** the aggregated total (Measured, this endpoint, this date) as the real figure, and — if you want continuity with the old reporting — the query-row sum labeled explicitly as a floor, so whoever reads it next doesn't inherit the same false precision. Expect the aggregated number to be noticeably higher than 412,000; how much higher tells you how long-tail-heavy your query distribution actually is.