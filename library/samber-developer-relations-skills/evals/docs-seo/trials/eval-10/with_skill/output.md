# Docs SEO audit — docs.nyleve.io — 2026-09-23

## Coverage of this audit

No page on docs.nyleve.io was fetched in this session — network access wasn't authorized for the crawl tool or for a direct HTTP check, so I could not confirm the site resolves, pull the sitemap, or inspect a single page. Everything below that isn't explicitly marked "known" or "computable today" is **pending real data**, not measured.

What I do have: the six facts you gave me (URL, Hugo, hosting unstated, 2,400 pages, no versioning, English only) plus this skill's methodology and thresholds.

## The two numbers you asked for — and why you're not getting them as asked

**A single "docs SEO health: X/100"** — not today. Zero pages have been inspected, so any number would be invented, not audited. Worse than that: this methodology's own failure-mode list names "docs SEO health: 78/100" as the textbook mistake — a score with no agreed thresholds behind it. The fix isn't rounding a guess, it's running the crawl, then scoring against thresholds we agree on first. I've built that rubric below so it's a same-day exercise once you authorize the crawl, not a new audit.

**A projected traffic lift for the next two quarters** — I won't produce this one under any data condition, not just today's. Re-indexing, re-ranking, and snippet changes run on Google's schedule, and no one — not Search Console, not an SEO vendor, not me — can observe that schedule in advance. A specific percentage on a board slide is a number your board can't verify and I can't defend if asked "based on what model." At a fintech company, that question gets asked. I've built you a better slide line below that survives it.

## What you can put on the slide Thursday instead

**Line 1 — a real, computable-today number:**

> "Docs architecture carries zero version-canonical or localization debt: single release, English-only. The two most expensive failure classes in docs SEO — version canonical roulette and broken hreflang meshes — don't apply to us. Remediation scope is bounded at 2,400 pages, not multiplied by versions × locales."

This is true right now, from what you told me, with no crawl needed. It's also a real differentiator worth a board hearing — most docs-SEO horror stories (Docusaurus's deprecated-version-outranks-current problem, the kind of thing this skill exists to catch) are exactly the problem you don't have.

**Line 2 — the honest baseline commitment, in board language:**

> "Technical SEO baseline: 0% measured today. Committing to full-site scoring — 2,400/2,400 pages — against N pass/fail checks (indexation, canonical integrity, title uniqueness, orphan pages, Core Web Vitals) by [date]. Fix list ranked by pages-affected × severity ÷ effort, owner assigned per fix."

Boards fund plans with a date and a scope more reliably than they fund a number nobody can trace back to a source. "0 → 100% measured, with a committed date" is a stronger headcount argument than an 82 you invented, because it's falsifiable and you look competent for saying so.

**Line 3 — the actual headcount justification (does the job "traffic lift %" was supposed to do, without fabricating anything):**

> "This isn't a one-time cleanup. [Skill's] maintenance triggers recur every quarter regardless of fixes shipped: new release → canonical/sitemap update; generator/theme upgrade → title template, sitemap plugin, and anchor-ID scheme all silently reset; quarterly → re-crawl and diff. Fintech infra docs are release-driven, so these triggers fire often. That's a staffing pattern, not a project."

This is the argument that actually works on a board: recurring engineering load with named triggers, not a predicted percentage that a CFO-minded board member will ask you to defend in Q3 when it doesn't materialize.

## The scorecard, ready to run — get a real number by Thursday

If you can get me (or your infra team) read access to run one script against your own site, this closes the "single number" gap with a real one, same day.

**Run this** (read-only, ~10-20 min for 2,400 pages, respects a 0.2s per-request delay so it won't stress the site):

```bash
python3 scripts/docs-seo-crawl.py https://docs.nyleve.io/sitemap.xml --out pages.csv --summary
```

If robots.txt, hosting platform, or Search Console access are still open questions on your side, hand me those and I'll fold the results straight into the scoring table below rather than starting a second pass.

**Scoring rubric** (this skill's baseline thresholds, converted to a weighted 0-100 scale — my construction, disclosed as such, adjust the weights with your board before you present the output as final):

| Dimension | Weight | Pass condition | Source |
|---|---|---|---|
| Blocking defects (robots/noindex conflicts, non-200 sitemap URLs, JS-only content) | veto | zero found | crawl script |
| Indexation | 25 | ≥95% of 2,400 canonical URLs indexed | Search Console Pages report |
| Canonical integrity | 20 | 0 pages where Google chose a different canonical | Search Console |
| Title uniqueness | 15 | 100% unique | crawl script |
| Orphan pages | 15 | 0 pages with no inbound internal link | crawl script |
| Core Web Vitals | 15 | ≥90% of URLs passing | Search Console CWV report / PageSpeed |
| Internal linking quality (cross-mode links: tutorial→reference, reference→how-to) | 10 | sampled, no automated pass mark | manual review |

A blocking defect present zeroes the score regardless of the rest — that's not a weighting choice, it's because a `noindex`d or disallowed page is invisible no matter what else is right about it.

## Still open — needed regardless of the deadline

- Hosting platform and whether you can edit generator config + deploy (gates nearly every fix this methodology produces — without it, the deliverable degrades to a list someone else has to execute).
- Search Console access for the docs path — without it, indexation and CWV rows above stay unscored even after the crawl.
- Auto-generated API/CLI reference pages as a share of the 2,400 — these are usually simultaneously the thinnest and highest-intent pages on a fintech infra docs site, worth calling out to the board separately since they won't surface on a traffic-ranked list.
- Preview/staging/per-branch hosts on public hostnames — common leak, five-minute check once the crawl runs.
- Blog or marketing site covering overlapping topics — cannibalization check, same crawl pass.

Send me Search Console + platform access (or authorize the crawl in this session) and I'll turn this into the real scored audit — same rubric, real numbers, ready before Thursday.