Two things wrong, do both, in order. Not "domain vs subfolder."

## 1. Real problem live now: unresolved duplicate indexing

`ridgeline.readthedocs.io` and `docs.ridgeline.sh` both return 200, same content, both in Google. That means canonical signal not working between these two right now. Growth head diagnosis half-right: dupe content real problem. Fix wrong: adding third URL space (`ridgeline.sh/docs`) on top of two broken ones gives Google 12,000 URLs to dedupe instead of 8,000. Worse, not better.

**Cheap fix, no migration:** 301 `readthedocs.io/*` → `docs.ridgeline.sh/*` now. Collapses dupe in days, zero risk, reversible, doesn't touch 4,000 pages on primary domain.

## 2. Real cause of traffic slide: JS-injected rendering, not URL structure

Traffic slid "since" React swap. That timeline points straight at the rewrite, not at subdomain-vs-subfolder.

Three broken pieces:
- **Canonical tag injected by JS** — Google guidance says canonical must be in raw HTML, not client-injected. Inconsistent detection explains why both domains stayed indexed.
- **Page body injected by JS** — content not in initial HTML. Adds render-queue delay/risk at 4,000-page scale. Sphinx static HTML never had this problem.
- **Sidebar nav injected by JS** — Sphinx toctree used to give crawler a fully static link graph. If nav only renders after JS execution, deep pages lose internal link discovery and link-equity flow.

Search widget with no plain links isn't itself a crawl bug (search results shouldn't be indexed), but confirms front end built with zero SEO care. Corroborates the timeline.

**Consequence for the proposal:** move this same React app to `ridgeline.sh/docs`, same broken canonical/body/nav stays broken. Slide continues on new URL. Migration risk spent, root cause untouched.

## 3. "Subfolder inherits authority" — weak, unproven claim

Google (Mueller, Illyes, repeatedly) says modern systems treat subdomains and subfolders equivalently for ranking. Case-study evidence for subfolder wins exists but confounded — those migrations usually also fixed redirects, speed, content, so gains not isolable to URL structure alone. Ask growth head for a case study on a docs site your scale, not a general SEO blog claim.

## 4. Cost math for 4,000-page move, if pushed anyway

- Needs 4,000+ correct 1:1 redirects (readthedocs.io/* AND docs.ridgeline.sh/* → ridgeline.sh/docs/*). Any gap = lost link equity or 404 at scale.
- Serving Sphinx/RTD build under a path of the React main site isn't DNS-only — needs reverse proxy or folding docs build into main deploy pipeline. Real infra project, not a redirect rule.
- Sitemap, Search Console reverification, historical performance data reset — makes next 12 months of diagnosis harder, another confound layered on top of the current confound.
- Well-executed migrations still see 1-3 month dip. This site already declining — stacking migration risk on unexplained decline is the wrong sequencing.

## What to propose instead

1. **Now:** 301 `readthedocs.io` → `docs.ridgeline.sh`. Kills dupe indexing this week.
2. **Now:** check Search Console Coverage report on both domains — see whether Google already picked a canonical. Confirms diagnosis before any spend.
3. **Next:** fix canonical tag, body content, sidebar nav to render server-side or pre-JS, not client-injected. This is the actual traffic-slide fix, needed regardless of domain.
4. **After 4-6 weeks:** measure. If slide stops, root cause confirmed, folder-authority migration becomes optional nice-to-have, not urgent.
5. **Only then**, if growth head still wants folder bet: scope full migration separately, planned properly, not rushed off a broken diagnosis.

## Line for the meeting

"Two domains are already indexed with identical content — that's the real bug, and a 301 fixes it this week. Traffic started sliding when we shipped the React rewrite, and canonical/body/nav are all JS-injected, against Google's own guidance — that's the more likely cause, and it'll survive the domain move untouched if we don't fix it first."

Next: run the Search Console Coverage check on both domains today, before agreeing to anything.