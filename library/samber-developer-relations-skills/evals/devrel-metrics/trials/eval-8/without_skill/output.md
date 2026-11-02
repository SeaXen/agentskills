## Verdict

- ❌ **305,000 as "monthly users" — indefensible.** Stop saying it before the next board meeting, including verbally. The number counts file fetches, not people.
- ⚠️ **240,000 docs sessions — weakly defensible.** Fine as a labeled traffic trend. Indefensible as audience size, which is how a board hears it.

## Why downloads can't be "users"

- **npm**: counts every tarball fetch — every CI run, Docker build, fresh clone, teammate install, any version. No user concept exists anywhere in that data.
- **PyPI**: same mechanics via the BigQuery/pypistats pipeline. PyPI itself removed download counts from project pages years ago because they get misread; what remains includes CI.
- **crates.io**: cargo caches locally, so humans rarely re-download. What's left is dominated by fresh CI builds.
- **The sum is worse than either part**: three registries, three different counting pipelines, added into one figure with no defined unit. It's mismatched-unit arithmetic — the total doesn't measure anything.
- **Magnitude**: CI-heavy packages commonly see 20–60+ fetches per active developer per month. At that ratio, 305k downloads ≈ 5–15k real monthly active developers. Verify against your own data before quoting any number.
- **The absurdity test**: every real user of your libraries needs an API key you issue. If 305k people used them monthly, your API logs would show it. They don't. The CTO can check in one afternoon.
- **Credibility cost**: one broken headline contaminates every defensible number in the deck. The new CTO found it in a week; the rest of the board will too.

## The replacement you already own

Your libraries call your own API — you hold exact ground truth the registries only proxy. Build the headline from API logs:

1. **Stamp every SDK request** with a standardized User-Agent (`nordholm-js/2.3.1`, etc.). One-line change per library; likely already half-true.
2. **Headline metric — monthly active developers**: distinct API principals with ≥1 successful SDK-attributed call, trailing 30 days. Deduped, real, auditable by the CTO directly.
3. **Decide human vs service-account treatment up front** and label it, or m2m keys will inflate the count later.
4. **Roll up by organization**: "active organizations" plus median developers per org. Boards price the second one.
5. **SDK share**: % of all API calls arriving via official SDKs vs raw HTTP. Direct measure of library reach — downloads never were.
6. **Version currency**: % of SDK traffic on latest stable, 30 days post-release. Signals security posture and support burden.
7. **Keep downloads, honestly labeled**: per-registry, "includes CI," trend only. Trends survive the CI share because it's roughly stable; the level never did.

## Fix the docs number

- **Report GA4 active users, not sessions.** A session is a 30-minute visit container; one developer generates many per month. Label the window (monthly vs quarterly) explicitly.
- **Hygiene pass**: exclude internal traffic, unify docs subdomains in one property, check consent-mode consistency.
- **Reconcile once against CDN/server logs** to size the bot share. GA requires JS, so the error runs both ways: headless/AI crawlers appear in GA, consent-refusing EU humans don't. Present that reconciliation — it reads as rigor, not weakness.
- **Pair with an outcome**: "docs-assisted activation" — % of new signups whose early journey includes docs and who reach first successful API call ≤7 days. Even a sampled join beats a raw session count.
- Keep 240k as a secondary line: "docs sessions (trend)" plus engaged-sessions %.

## Next board meeting: restate proactively

1. One slide: old number → why it overstated → new metric → new baseline. You found it; that's the position of strength.
2. Pre-compute and present your own ratio — "every active developer generates ~N downloads/month via CI" — so the CTO's poke becomes a number you already own.
3. Never re-sum registries into one figure again. Per-registry or nothing.
4. Frame the new set as a funnel: Reach (docs users, download trends) → Adopt (SDK-attributed actives, organizations) → Deepen (SDK share, version currency, 90-day retention). Boards fund the arrows, not the first box.

**Bottom line**: pull "monthly users" yourself before it gets pulled for you — your API logs already hold the real number, and it's the one metric in this whole list the CTO cannot poke a hole in.

*(Saved a Nordholm project memory so the restatement and replacements stay consistent if this comes back next quarter.)*