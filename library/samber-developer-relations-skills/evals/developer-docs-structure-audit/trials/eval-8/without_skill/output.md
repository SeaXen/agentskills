## Docs Audit Feasibility: Corvid Streams (Mintlify, ~480 pages, no repo access)

**Bottom line: ~85-90% of a full audit is executable from the public site + analytics alone. The gap concentrates in three things — the authoritative redirect map, the true orphan/unpublished-page inventory, and anything that depends on git history. None of those three block a credible scorecard by the 30th.**

### The one question to resolve first — it changes everything

Confirm who owns the **Mintlify dashboard/subscription**, not just the git repo. The agency owns the content repo; that doesn't automatically mean they own the Mintlify hosting account. If Corvid Streams owns the Mintlify project directly, you likely already have (or can get in an hour, zero agency involvement):

- Mintlify's built-in **search analytics** — real user queries, including zero-result queries. This is a better content-gap signal than reading the repo would ever give you.
- Broken-link reports (Mintlify runs one in CI/dashboard).
- AI assistant conversation logs, if the docs chat widget is enabled.
- Deploy/build history — an indirect proxy for update cadence without needing git log.

Ask this before anything else. It's the single highest-leverage unlock in this whole audit.

---

## Feasibility matrix

| Audit layer | Weight | External coverage | What's blocked |
|---|---|---|---|
| **Technical foundation** (crawl, index, speed, HTTPS, CWV) | 25% | ~90% | Authoritative redirect map (docs.json); true orphan pages invisible by definition |
| **On-page optimization** (titles, meta, headings, URLs, internal links, alt text) | 20% | ~95% | None structural — see schema caveat below |
| **Content quality** (thin content, freshness, E-E-A-T, gaps, cannibalization) | 25% | ~85% | Author/editorial process (ask, don't need repo); freshness dates if Mintlify's "Last updated" footer is disabled |
| **Link profile** (backlinks, authority) | 15% | 100% | Nothing — this layer never touches the repo, third-party tools only |
| **Competitive position** | 15% | 100% | Nothing — external by nature |
| **Accessibility (WCAG 2.2)** | add-on | ~95% | Nothing meaningful — docs are template-driven, audit the templates once, sample the rest |
| **AI search / GEO visibility** | add-on | ~90% | Nothing — Mintlify auto-publishes `/llms.txt` and `/llms-full.txt` publicly, see below |
| **Site architecture / IA** | add-on | 100% | Nothing — rendered nav *is* the ground truth users experience |
| **Schema markup** | add-on | ~90% | Needs a rendering tool, not raw `curl`/`web_fetch` — see caveat |
| **Analytics / tracking quality** | add-on | 0-100% | Entirely dependent on what's in "our analytics property" — resolve the Mintlify-dashboard question above |

Weighted across the five core SEO-audit layers: **~91%** of the scorecard is fully executable with the access you have.

---

## Mintlify-specific shortcuts (use these — they launder around the repo-access wall)

1. **`/llms.txt` and `/llms-full.txt`** are auto-generated and public on every Mintlify deploy. `llms-full.txt` typically enumerates every page in the nav tree with content. Diff it against `sitemap.xml` and against your own crawl — mismatches surface orphan pages, noindex pages, and hidden/unlisted pages without touching the repo.
2. **Page footer "Last updated on [date]"** — if Corvid Streams has this Mintlify feature enabled, it's pulled from the file's last git commit date and rendered publicly. If it's on, you get real freshness data without git access. Check one page now to confirm it's turned on.
3. **`docs.json`/redirect completeness** can't be pulled directly, but you can approximate it: pull historical top URLs from Wayback Machine, Google Search Console's legacy indexed-URL list, or Ahrefs' historical top pages, then test each for a clean 301. This won't be exhaustive, but it'll catch the URLs that actually carry traffic/link equity — which is what matters.
4. **OpenAPI-based API reference pages** render fully in HTML — audit them like any other page.
5. **Schema detection**: `curl`/`web_fetch` strip `<script>` tags, so JSON-LD injected client-side won't show up. Verify via a rendered-DOM check (Claude in Chrome, or Rich Results Test) on a sample per page template rather than raw-fetching all 480.

---

## Narrow asks worth sending the agency now (none require repo access)

These are read-only exports, not access grants — a reasonable agency shouldn't refuse any of them even mid-quarter:

- Export of `docs.json` (navigation + redirects config) — one file, not the repo.
- The OpenAPI spec file(s) if API reference pages are generated from one.
- Confirmation of whether their CI runs Mintlify's broken-link checker, and if so, the last report.
- Confirmation of whether the "Last updated" footer feature is enabled.

Frame these as "send me the file," not "give me access" — it's a much easier yes, and it closes most of the remaining ~10% gap.

---

## Adapted scorecard — tag every line with a confidence label

Don't present an audit that reads as complete when a third of it is inference. Use the standard 5-layer scorecard, but add a **Coverage** column so stakeholders know what to trust fully vs. treat as directional:

| Layer | Score /10 | Coverage |
|---|---|---|
| Technical Foundation | [x] | Audited |
| On-Page Optimization | [x] | Audited |
| Content Quality | [x] | Audited (freshness: *Partial* if Last-updated footer is off) |
| Link Profile | [x] | Audited |
| Competitive Position | [x] | Audited |
| Accessibility | [x] | Audited (templates) + sampled |
| AI Search Visibility | [x] | Audited |
| Site Architecture | [x] | Audited |
| Analytics/Tracking | [x] | **Audited / Partial / Blocked** — fill in once the dashboard-ownership question is resolved |

Coverage labels: **Audited** (full external verification), **Partial (estimated)** (inferred, e.g., redirect map from known-URL sampling), **Not assessable** (genuinely requires repo — flag it, don't fake a score).

---

## Plan to the 30th (12 working days)

| Days | Work |
|---|---|
| 1 (Sep 18-19) | Resolve Mintlify-dashboard ownership. Send the four narrow asks to the agency. Pull GA4/Posthog/GSC exports. |
| 2-4 | Full crawl of all 480 pages (status codes, titles, meta, headings, internal link graph, images/alt). Diff `sitemap.xml` vs `llms-full.txt` vs crawl for orphans. Batch CWV via PageSpeed Insights/CrUX (site-wide field data covers all pages in aggregate; don't run per-page Lighthouse on all 480 — sample by template). |
| 4-6 | Content quality pass: thin-content flags, freshness (if available), competitor gap analysis, cannibalization via query data. Manual/qualitative depth only on top-trafficked 50-100 pages by analytics, plus a stratified sample of the rest — not uniform manual review of all 480. |
| 6-7 | AI-search pass: llms.txt/llms-full.txt quality, robots.txt AI-bot check, citation testing across ChatGPT/Perplexity/Claude/Google AI Overviews on your top 15-20 queries, schema spot-check via rendered DOM. |
| 7-8 | Link profile + competitive position via Ahrefs/Semrush/GSC — no dependency on anything above. |
| 8-9 | Accessibility: axe-core/Lighthouse against each unique page template + samples; manual keyboard/screen-reader pass on nav, search, and code blocks (shared chrome, so this covers the effective surface of all 480). |
| 9-10 | Synthesize into scorecard with coverage labels, prioritized fix list, executive summary. |
| 10-12 | Buffer: stakeholder review, revisions. |

**One risk to flag upward now, not on the 30th**: diagnosing is fully in your control; shipping fixes is not — the agency owns the deploy pipeline. If the audit is meant to kick off a remediation phase, get their turnaround commitment lined up in parallel, or the scorecard becomes a document nobody can act on.