## Split this into 4 separate tickets, not one

Bundling FAQPage schema + heading rewrites + a full crawl audit + canonical cleanup + internal linking redesign into one ticket means that when rankings move (up or down), you won't know which change caused it. Each of these has a different blast radius and a different measurement window. Sequence them so each layer is stable before the next one lands on top of it — this follows the same crawlability → indexability → renderability → signals dependency order any technical SEO diagnosis uses: fixing what pages *say* is wasted effort if Google isn't crawling/indexing the *right* URL yet.

## First, correct the premise with marketing

Google significantly cut back FAQ rich results in **August 2023** — they're now shown almost exclusively to a narrow set of authoritative government and health sites. A dev-tools troubleshooting section copying a competitor's FAQPage markup is very unlikely to get the expanded SERP snippet today, regardless of markup quality. Two things follow:

- Don't sell this internally as "we'll get the expanded result." Check current SERP behavior for a couple of target queries manually before promising anything.
- Ship the markup anyway — it's good hygiene, it helps AI answer engines (ChatGPT, Perplexity, AI Overviews) lift your Q&A directly since those aren't bound by the same 2023 restriction, and `mainEntity` Q&A pairs give you a forcing function to make headings genuinely match search intent. Just reset the "why" from "get rich results" to "improve machine-readability and AI-citation odds."

## Sequenced plan

**Phase 0 — Baseline (before touching anything, ~1 day)**
Export current state so the later phases are measurable: GSC Performance (clicks/impressions/position) per troubleshooting URL, current canonical map, current rich-result/enhancement status, current internal-link count per page. Without this you can't attribute movement to any later phase.

**Phase 1 — Crawl audit + canonical cleanup (own ticket, sitewide, ships first)**
This is foundational, not cosmetic: if a troubleshooting page's canonical points somewhere else, or duplicate URL variants exist (trailing slash, params, http/https), any schema or heading work you do on the non-canonical copy is invisible to Google anyway. Do the full diagnostic in order — robots.txt / sitemap → canonical/duplicate-content → renderability → then signals. Let this land and get reconfirmed in GSC's Coverage/canonical report (typically 1-2 weeks) before layering content changes on top, so a later ranking shift isn't confused with this phase's effect.

**Phase 2 — Pilot: heading rewrite + FAQPage schema on 5-8 of the 34 entries (own ticket)**
These two changes ship together, not separately — a valid FAQPage's `mainEntity` answer text has to match the visible on-page content exactly, so the heading rewrite and the schema are really one content edit, not two workstreams. But roll it out as a pilot before touching all 34:

- Rewrite headings to match real query phrasing, but keep the underlying keyword the page already ranks for inside the question (`Why is my function timing out?` not just a generic reformat) — these pages likely have existing earned rankings, and a blanket bulk rewrite with no signal-check is exactly the kind of change that quietly tanks a page that was already working.
- Validate every page's markup in Rich Results Test before merging.
- Watch GSC Performance + Enhancements for 2-3 weeks on just the pilot set.

**Phase 3 — Roll out to remaining 26 entries (own ticket)**
Only after the pilot shows no ranking/CTR regression. Same pattern: heading + matching FAQPage schema per page, validated individually.

**Phase 4 — Internal linking redesign (own ticket, last, separate project)**
Do this last and don't fold it into the troubleshooting-page work — it's sitewide, a different blast radius entirely, and you want the anchor text pointing into these 34 pages to use their *final* question-format headings, not text you're about to change twice. Standard checklist applies: no orphaned troubleshooting entries, descriptive anchor text (not "click here"), hub-and-spoke from a troubleshooting index page if one doesn't exist yet, 5-10 contextual links per page as a rough guide.

## Why this order and not, say, linking-first-then-content

Canonical/crawl issues, if any exist, can silently split ranking signals across duplicate URLs — building an internal-linking structure or schema on top of that before it's fixed just reinforces the wrong URL. Content-level changes (headings, schema) are cheap to pilot and roll back per-page; sitewide architecture changes aren't, so they go last, once the page-level content is finalized and stable.