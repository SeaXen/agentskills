## Where to start: treat "top pages" and "orphan pages" as one project, not two

Your two findings aren't competing priorities — they're cause and effect. The quickstart, the Python SDK install page, and the three how-tos already have traffic and internal authority. The 47 orphans and the dead-end reference pages are exactly what that authority isn't reaching. The fix for one is the input for the other: use the five winning pages as the internal-link donors that rescue the highest-value orphans, instead of running "polish the top 5" and "clean up 47 orphans" as separate workstreams.

### Step 1 — Triage the 47 orphans before touching any on-page SEO

You can't decide "link it" vs. "delete it" without sorting them first. On a 900-page Docusaurus site, orphans are almost always one of four things:

- **Bucket A — valuable, just unlinked.** A how-to or guide that's topically close to your five top pages but never got a link when it shipped. Fix: link it from the relevant hub page.
- **Bucket B — security/compliance-relevant, regardless of traffic.** SOC 2 or pen-test summary, subprocessor list, data residency/retention policy, SSO/SAML setup, audit-log or API-key-rotation docs, DPA/security whitepaper. Treat these as top priority even if analytics shows near-zero pageviews — see the note below on why.
- **Bucket C — stale or superseded.** Old version docs, deprecated endpoints, duplicate pages from a past restructure. Don't spend linking budget here: 301-redirect to the current page or noindex and drop from the sitemap.
- **Bucket D — genuinely niche reference minutiae.** Fine to stay low-traffic, but "zero inbound links" is still the defect, not the traffic level. Give each at least one contextual link from its parent page.

Cross-check the 47 against Google Search Console's "not indexed" report. That tells you which ones Google has actually dropped versus which are just thin on internal links — that's your real urgency order within the list, not the crawler's binary orphan flag.

### Step 2 — Fix the reference pages that link nowhere, same audit, opposite direction

Reference pages that dead-end are usually a template problem, not a per-page one — auto-generated per-endpoint pages show params/response/errors and stop. Fix the template once: add a "used in" / "related" block that pulls from the same tags/categories your how-tos already use, so every reference page links to (a) the how-to that exercises that endpoint and (b) two or three sibling endpoints. This is the same motion as Step 1 in reverse — the reference page becomes the link source, the orphaned how-to becomes the target — and it scales across all 900 pages from one PR instead of hundreds of manual edits.

### Step 3 — Turn the five known top pages into deliberate hubs

They already win the traffic; more keywords on pages that already convert is diminishing returns. The lever is using their authority to pull readers (and crawlers) deeper. On each of the five, add:

- A "Next steps" block linking to two or three deeper pages, prioritizing Bucket A/B rescues.
- Descriptive **inline contextual links**, not just sidebar entries — sidebar links carry less topical-relevance signal than in-content links.
- Breadcrumbs, if not already present. Cheap in Docusaurus, guarantees one more internal link per page, and helps anyone navigating a 900-page tree orient themselves.

Only after the linking is fixed, do the conventional polish on these five specifically: unique titles under 60 characters with product + task keyword ("Send your first record to Grantham Data in under 5 minutes" beats "Quickstart | Docs"), self-referencing canonicals, and HowTo structured data on the three how-tos. Also confirm the Python SDK install page isn't cannibalizing a generic "Installation" nav page for the same query — common on Docusaurus sites with per-language install tabs.

### Step 4 — The check specific to your buyer

Analytics measures developers. It doesn't measure the security reviewer who reads three to five pages right before a six-figure contract signs — that traffic is a rounding error in aggregate numbers but decides 100% of your deals. That's exactly why Bucket B above gets treated as high priority independent of pageviews: an unlinked SOC 2 summary or audit-log doc is a bigger business risk than an unlinked changelog page, even though your crawl tool scores them identically.

Concretely: link the security/compliance pages directly from the quickstart and the SDK install page — "see how we handle encryption and audit logging" placed right where a developer sets up credentials is a natural, non-salesy bridge. It seeds the reviewer's due-diligence path before legal even asks for the doc, which shortens the security review cycle. Your analytics will never surface this as a win because pageviews aren't the metric that matters for that reader.

### Sequencing

1. **This week:** export the 47 orphan URLs and the reference-pages-with-no-outbound-links list, sort into the four buckets. Spreadsheet exercise, not engineering — 30–60 minutes once you have the crawl export.
2. **This week:** identify which orphans are Bucket B and link them from the quickstart and SDK install page. One hour of work, outsized deal-risk payoff.
3. **Week 2:** ship the reference-page template fix (auto-link to related how-tos/sibling endpoints). One PR, applies to all 900 pages.
4. **Week 2:** add "Next steps" blocks and breadcrumbs to the five hub pages; backfill links to rescued Bucket A orphans.
5. **Week 3:** prune Bucket C — redirect or noindex stale/duplicate pages so they stop diluting crawl budget.
6. **Week 3–4:** on-page polish (titles, meta descriptions, schema) — on the five hub pages only, not all 900.
7. **Ongoing:** re-run the orphan-page crawl monthly. New pages routinely ship without a nav entry on large Docusaurus sites, so this becomes a 15-minute recurring check rather than a one-time cleanup.

### What not to do

Don't spread SEO polish across all 900 pages before the internal-linking foundation is fixed — you'd be optimizing pages Google may not be reliably crawling in the first place. And don't let "it's only 40 pageviews a month" be the reason a compliance page stays orphaned; on your sales motion, that page's audience is smaller than a rounding error and worth more than most of your traffic.