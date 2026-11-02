# Extraction plan: docs.parallaxmetrics.io page-2 queries (positions 5–20)

## 1. API and property scope

Use the Search Console API's `searchanalytics.query` method (Node package name is `searchconsole` v1; REST path is still under `webmasters/v3` for historical reasons):

```
POST https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query
```

Two property shapes are possible — check which one is verified before building the filter:

- **Dedicated subdomain property** (`https://docs.parallaxmetrics.io/`, URL-prefix type): `siteUrl` is that exact string, URL-encoded. No extra page filter needed — every row is already docs traffic.
- **Domain property** (`sc-domain:parallaxmetrics.io`, covers the whole domain + all subdomains): `siteUrl` is `sc-domain:parallaxmetrics.io`. You **must** add a `page contains docs.parallaxmetrics.io` filter or you'll pull marketing-site rows in with docs rows.

Both shapes are handled below with one filter block; it's a no-op (matches everything) if you're on the dedicated docs property, since every returned page URL will contain that string anyway.

## 2. Date range

GSC's API only retains a rolling 16 months — so "16 months of data" means: pull all of it, don't window it further.

- `startDate`: 16 months back from today → `2025-05-20`
- `endDate`: today minus a 3-day lag buffer (last 1–3 days are often incomplete/unfinalized) → `2026-09-17`
- `dataState: "final"` — omit `dataState` or set explicitly to `"final"` so you don't pull in still-revising partial days. Do **not** use `"all"` for this report; it'll shift on re-run.

## 3. Request body

```json
{
  "startDate": "2025-05-20",
  "endDate": "2026-09-17",
  "type": "web",
  "dataState": "final",
  "dimensions": ["page", "query"],
  "dimensionFilterGroups": [
    {
      "groupType": "and",
      "filters": [
        { "dimension": "page", "operator": "contains", "expression": "docs.parallaxmetrics.io" }
      ]
    }
  ],
  "rowLimit": 25000,
  "startRow": 0
}
```

Notes on the parameters:

- `dimensions: ["page", "query"]`, not just `["query"]`. Position is an impressions-weighted average — if a query ranks on both a doc's overview page and a reference page, a query-only pull blends those two positions into one number and can hide a page-2 page behind a page-1 page. You need the page+query pair to act on the right URL.
- `type: "web"` explicitly excludes Image/Video/Discover result types, which don't have a comparable organic "position" concept.
- **`position` is not filterable server-side.** `dimensionFilterGroups` only accepts `query`, `page`, `country`, `device`, `searchAppearance` as filter dimensions — `position`, `clicks`, `impressions`, `ctr` are metrics, not filterable dimensions. Pull everything, filter position client-side (step 4).
- Optional refinement: add a second filter `{ "dimension": "query", "operator": "notContains", "expression": "parallax" }` to strip brand queries out of the page-2 list — a branded query stuck on page 2 is a different problem (SERP/brand issue) than a topical query stuck on page 2, and mixing them muddies prioritization.

## 4. Pagination — you will exceed 25,000 rows

`rowLimit` caps at 25,000 per call. A 16-month page+query pull on any active docs site will very likely blow past that. Loop on `startRow` until a page comes back short:

```typescript
import { google } from 'googleapis'

type GscRow = {
  keys: [string, string] // [page, query]
  clicks: number
  impressions: number
  ctr: number
  position: number
}

const PAGE_SIZE = 25000
const SITE_URL = 'sc-domain:parallaxmetrics.io' // or the docs URL-prefix property
const DOCS_FILTER = 'docs.parallaxmetrics.io'

async function fetchAllRows(startDate: string, endDate: string): Promise<GscRow[]> {
  const auth = await google.auth.getClient({
    scopes: ['https://www.googleapis.com/auth/webmasters.readonly'],
  })
  const searchconsole = google.searchconsole({ version: 'v1', auth })

  const rows: GscRow[] = []
  let startRow = 0

  while (true) {
    const res = await withBackoff(() =>
      searchconsole.searchanalytics.query({
        siteUrl: SITE_URL,
        requestBody: {
          startDate,
          endDate,
          type: 'web',
          dataState: 'final',
          dimensions: ['page', 'query'],
          dimensionFilterGroups: [
            {
              groupType: 'and',
              filters: [{ dimension: 'page', operator: 'contains', expression: DOCS_FILTER }],
            },
          ],
          rowLimit: PAGE_SIZE,
          startRow,
        },
      }),
    )

    const page = (res.data.rows ?? []) as GscRow[]
    rows.push(...page)
    if (page.length < PAGE_SIZE) break
    startRow += PAGE_SIZE
  }

  return rows
}

async function withBackoff<T>(fn: () => Promise<T>, attempt = 0): Promise<T> {
  try {
    return await fn()
  } catch (err: any) {
    const status = err?.code ?? err?.response?.status
    if ((status === 429 || status >= 500) && attempt < 5) {
      await new Promise((r) => setTimeout(r, 2 ** attempt * 1000))
      return withBackoff(fn, attempt + 1)
    }
    throw err
  }
}
```

Run `fetchAllRows('2025-05-20', '2026-09-17')`. This is the raw dataset both downstream steps (page-2 report and total-impressions refresh) are built from — pull it once, derive both from it.

## 5. Filter for "page two" and act on the rows

Client-side, on the array from step 4:

```typescript
const pageTwo = rows.filter((r) => r.position >= 5 && r.position <= 20)
```

Calibration note: strict Google page-2 (10 results/page, no SERP features) is positions 11–20; 5–10 is technically still page 1, just below the fold on most SERPs today. If 5–20 was chosen deliberately (e.g., to also catch "below the fold on page 1" queries pushed down by featured snippets/PAA), keep it — just don't call the 5–10 subset "page two" in any report that goes to people who'll check that claim literally. Worth a one-line footnote in the deliverable either way.

Once you have `pageTwo`, before building a new content plan, run the **cannibalization/low-hanging-fruit screen**: group by `query`, and flag any query with more than one distinct `page` in the pageTwo set — that's two docs pages competing for the same query, splitting authority; fix by consolidating or differentiating, not by optimizing both independently.

Then score and prioritize:

```typescript
type ScoredRow = GscRow & { opportunityScore: number }

// Rough organic CTR-by-position benchmarks (non-brand, desktop, industry averages —
// not GSC-provided, used only to estimate uplift, not as ground truth).
const BENCHMARK_CTR_POS3 = 0.11

function score(rows: GscRow[]): ScoredRow[] {
  return rows
    .map((r) => ({
      ...r,
      // impressions already earned at this position, weighted toward rows closer to page 1
      opportunityScore: r.impressions * Math.max(0, BENCHMARK_CTR_POS3 - r.ctr),
    }))
    .sort((a, b) => b.opportunityScore - a.opportunityScore)
}
```

`opportunityScore` estimates incremental clicks if the page moved to a top-3 position, using the query's *actual* impression volume and *actual* current CTR gap rather than volume alone — this keeps a high-impression, already-decent-CTR query from crowding out a lower-impression query that's converting none of its page-2 impressions at all.

Output one row per `(page, query)` with: `page, query, impressions, clicks, ctr, position, opportunityScore`, tiered top/mid/low by score tertile. For each `page` with multiple queries attached, the action is almost never "write new content" (these pages already rank) — it's incremental: strengthen on-page targeting for the specific query terms, add/adjust internal links from higher-authority pages toward it, tighten title/meta if CTR is below the position-appropriate benchmark, or refresh content if position has been declining over the 16-month window rather than flat.

## 6. Refreshing "docs total: 412,000 impressions"

To reproduce the prior number **the same way** it was built: sum the `impressions` column across every row in the full dataset from step 4 (not just the page-2 subset) — same site scope, same 16-month window, same `page`+`query` dimensions.

```typescript
const refreshedTotal = rows.reduce((sum, r) => sum + r.impressions, 0)
```

Report that number as the like-for-like refresh. But flag this alongside it, because it's a documented gap, not a rounding error: **summing query-dimension rows always undercounts the real total.** Google excludes rare and potentially-identifying queries from the `query` dimension breakdown for privacy, while still counting their impressions in the property's aggregate totals — so a query-row sum is structurally a floor, not the true figure, independent of how carefully the pull was paginated. The previous "412,000" was very likely undercounting for the same structural reason, so a refreshed number computed the same way is comparable to it, but neither is the actual total.

To get the real total for the same window/scope, run one more call with no query breakdown:

```json
{
  "startDate": "2025-05-20",
  "endDate": "2026-09-17",
  "type": "web",
  "dataState": "final",
  "dimensions": [],
  "dimensionFilterGroups": [
    {
      "groupType": "and",
      "filters": [{ "dimension": "page", "operator": "contains", "expression": "docs.parallaxmetrics.io" }]
    }
  ]
}
```

This returns a single aggregate row — its `impressions` value is the true property-level total for docs.parallaxmetrics.io over the window. Report both numbers side by side (`query-row sum` vs `true aggregate`) rather than replacing one with the other silently — the gap between them is itself a useful, reportable figure (it's roughly the long-tail/anonymized-query volume you can't currently target by name), and it keeps whoever reads the refreshed report from assuming the query-sum figure is complete when the methodology guarantees it isn't.