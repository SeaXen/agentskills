## Verdict

**Reject proposal as scoped. Quoted rich-result uplift does not exist.**

Two of three schema types target rich results Google killed, not degraded — killed:

| Markup                    | Status                                                                    | Verdict            |
| -------------------------- | -------------------------------------------------------------------------- | ------------------- |
| `HowTo` (310 pages)         | Rich result removed August 2023. Documentation deleted.                    | Zero uplift possible |
| `FAQPage` (94 pages)        | Narrowed to gov/health 2023, stopped appearing entirely **7 May 2026**.    | Zero uplift possible |
| `Article` (remaining ~1,400)| No docs-specific rich result ever existed for this type.                   | Harmless, low value  |

Today is 2026-09-23. FAQPage's cutoff was over four months ago. This isn't "outdated best practice" — it's markup for SERP features that no longer render, full stop. Whatever numbers the agency quoted for uplift, they can't come from Google Search as it exists today.

## Cost of proposal as scoped

Per-page hand-authored `HowTo` step markup (310 pages) + `FAQPage` Q&A markup (94 pages) = 404 pages of manual structured-data work, three sprints of a writer's time, for two schema types producing zero incremental SERP inventory. This is the skill's own named failure mode: "per-page whack-a-mole — 400 hand-written [items] instead of one template change." Same shape here, worse: even the template-level version of this work would be worth nothing, because the destination rich result doesn't exist.

## What actually moves the needle on 1,800 Mintlify pages

Redirect the three sprints here — these are template-level changes, so each one reaches every page, not just 404:

1. **Title template rewrite.** Docs titles are generated from `docs.json`'s `name` field plus per-page frontmatter. Fix the shape once (`{task/symbol} | {product} {section}`, query term first, brand last) — reaches all 1,800 pages, not 310.
2. **`BreadcrumbList` markup.** Still renders as a rich result. Docs have a real hierarchy to express it. Sitewide, one implementation.
3. **Internal linking repair.** Orphans first, dead ends second, then contextual prose links from the quickstart and top how-tos, plus cross-mode links (tutorial → reference → how-to → troubleshooting). Docs sites have nav links everywhere and contextual links nowhere — this is usually the single highest-value fix on a reference-heavy site, and it's exactly the kind of work a traffic-ranked page list never surfaces on its own.
4. **Descriptions for pages that matter** — quickstart, top how-tos, top reference entries. Let the rest fall back; don't generate filler for 1,800 pages.

That's a defensible three-sprint scope: one template edit reaching every page, one sitewide breadcrumb pass, and a linking pass that's the actual long pole (worth the writer hours the agency proposed spending on dead markup).

## What I didn't verify

No docs URL, Search Console access, or crawl was available for this consult — this answers the specific proposal, not a full audit. Unverified: whether Mintlify's current frontmatter/`docs.json` setup already supports a clean title-template override, and whether the docs are versioned (changes the linking-fix priority). If EM wants the full picture — indexability, canonical posture, Core Web Vitals — that's a separate audit pass with its own interview.

**Next action:** send the EM this verdict table plus the redirected scope (items 1-4). If they want the full site audit instead of just this proposal review, say so and I'll start the crawl-based audit.