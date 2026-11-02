# Distribution plan — probe-lens

## Assumptions standing in for the interview

I don't have you live to ask one-at-a-time, so I'm running the skill's interview against what's in the request and flagging the two calls that matter most. Confirm or correct these before you run anything below — they're cheap to fix now, expensive to fix after hours are spent.

- **Ecosystem**: single host-product extension, VS Code-format, published to the VS Code Marketplace only. Inferred from the Cursor mentions — nothing else explains that pattern (see below).
- **Adopter type**: individual developer, primary. A VS Code/Cursor extension is a self-serve install; almost nothing gates it through a procurement process. Treat company adoption as a secondary beneficiary of the same fixes, not a separate track — **flag this one for correction if your issue tracker shows teams standardizing on it, not individuals.**
- **Capacity**: "8 hours a month for this" reads as the whole project — support, bug triage, any feature work — not a dedicated distribution budget. I've built this plan against **~3 hours/month recurring for distribution specifically**, leaving the rest for engineering. If 8h/month really is distribution-only, widen the test ring by one item.
- **Goal**: growing, retained installs — a compounding position, not a one-off spike. No launch event or deadline in view.
- **What's already in place**: unaudited beyond "on the VS Code Marketplace, 4,100 installs, 7 months." Everything in "Position today" below marked "unaudited" needs a look before you trust it.

## The Cursor signal, read correctly

This is the headline finding, and it isn't a feature request. Microsoft's Marketplace terms restrict use to Microsoft's own in-scope products — every VS Code fork is contractually barred from it. Cursor migrated to Open VSX in mid-2025 and proxies search through it. **If probe-lens isn't on Open VSX, Cursor users cannot find or install it through their extensions UI at all.** The repeated mentions in your issue tracker are almost certainly people who already tried and hit a wall, not people asking for a new integration. This is a coverage gap, not a product gap, and it's the cheapest fix in this entire plan.

## Candidate mixes

| | Coverage-first (recommended) | Ecosystem-depth | Downstream-first |
|---|---|---|---|
| What it is | Dual-publish + clean metadata on both marketplaces, no dedicated core channel yet | Concentrate on the OpenTelemetry/observability community specifically — its lists, its forums, its docs | Trust posture (signing, SBOM, verified publisher) + a "used by" wall aimed at procurement |
| Cost | ~3h/month | ~5-6h/month | ~4-5h/month + a one-time setup sprint |
| Serves | Individual, broad | Individual, narrow and deep | Company/procurement |
| Gives up | No concentrated community push | Coverage everywhere else | Bottom-up momentum, and a gate that may not exist for this product |

Ranked on the skill's four axes (canonical order, unchanged by this project's specifics):
- **Efficiency**: coverage-first > ecosystem-depth > downstream-first
- **Effort**: downstream-first > ecosystem-depth > coverage-first
- **Value, individual**: ecosystem-depth > coverage-first > downstream-first
- **Value, company**: downstream-first > coverage-first > ecosystem-depth

**Recommendation: coverage-first.** At a real ~3h/month, ecosystem-depth's relationship and community-forum work isn't affordable, and downstream-first is solving a procurement problem that doesn't clearly exist yet for an editor extension. Revisit ecosystem-depth once Open VSX proves the Cursor hypothesis and the team has more than 3h/month to spend — probe-lens serves a narrow enough audience (people already running OTel) that depth could compound later.

---

# Distribution plan — probe-lens

## Position today

- **Marketplace coverage**: VS Code Marketplace only (assumed). No Open VSX listing — this is very likely the entire Cursor phenomenon in your issue tracker.
- **Marketplace metadata**: unaudited. Check description wording (should use searcher vocabulary — "OpenTelemetry spans," "distributed tracing," "trace viewer," "APM" — not house terminology), every keyword/category slot filled, README rendering correctly inside the Marketplace's own sandbox (not just on GitHub), and doc/funding/issue-tracker links present.
- **Verified publisher status**: unaudited — cheap, one-time, worth checking.
- **Code-host surfaces**: GitHub repo exists (issue tracker implies it). Topics, social preview image, Discussions, releases feed — all unaudited.
- **Curated lists**: no evidence of presence on any awesome-vscode / awesome-opentelemetry / observability-tools roundup. Treat as absent until checked.
- **Release cadence**: unknown gap history over 7 months — check days-since-last-release and the longest gap.
- **Ratings/reviews**: unaudited — read the latest few for install-blocking complaints; this doubles as a churn signal.
- **Baseline**: 4,100 cumulative installs over 7 months is the only hard number in hand. The VS Code Marketplace has **no first-party install-stats dashboard** beyond the publisher page's cumulative count and a rough trend graph — you're currently flying blind on arrival sources. Snapshot GitHub repo traffic (referrers, cloners) today; that panel only keeps a rolling 14-day window, so an uncaptured baseline is gone for good.

## Adopter

Individual, primary (assumption — confirm). A dev finds and installs this themselves while debugging; nothing here is procurement-gated in the ordinary case. Both fixes below (Open VSX, metadata) serve individual adoption directly and cost nothing extra if company adoption turns out to matter later.

## Foundation ring — do this first, ~1 hour one-time, then minutes per release

1. **Publish to Open VSX** (Eclipse Foundation) via the same CI step that already builds the `.vsix` — add `ovsx publish` to the release workflow. This unlocks Cursor, Windsurf, VSCodium and Gitpod, the exact audience already visible in your issue tracker. Marginal artifact cost is near zero; the honest ongoing cost is a second store's version-compatibility range to track (minutes per release unless the two stores' supported-engine ranges diverge).
2. **Rewrite marketplace metadata** on both stores: description in searcher vocabulary, all keyword/category slots filled, README verified in-sandbox, docs/funding/issue links repaired.
3. **Verified publisher badge** on the VS Code Marketplace — under an hour, pure legibility, zero recurring cost.
4. **Stale-listing sweep**: search "probe-lens" and "opentelemetry vscode" / "trace viewer vscode" for any existing third-party mentions with wrong screenshots or dead links, fix or request correction.

## Sequence

- **Weeks 1-2**: the four foundation items above, Open VSX first — it's the one fix that directly answers a signal you already have.
- **Months 1-3, passive discovery (~1-2h/month)**: tag the GitHub repo with `opentelemetry`, `vscode-extension`, `observability`, `tracing` topics (tagging alone doesn't surface it until the topic itself is curated, but it's a five-minute action with no downside); identify 1-2 curated lists a real OTel/observability audience reads, contribute a small unrelated fix to each first, then submit matching its `contributing.md` format exactly; spend 30 minutes checking whether OpenTelemetry's own ecosystem/tools registry has an editor-tooling slot — this behaves more like a connector-hub listing than a generic awesome-list.
- **Ongoing, conditional**: creator/newsletter seeding — not now (see Refused).

## Test ring (ends ~10-12 weeks after foundation completion)

- **T1 — Open VSX distribution.** Hypothesis: the Cursor mentions are latent demand blocked by store availability, not a feature ask. Signal: Open VSX weekly downloads reach a self-set 15-20% of the VS Code Marketplace weekly rate within 8 weeks, and new Cursor-related issue-tracker mentions drop to near zero. Cost: covered by the foundation ring.
- **T2 — One curated list or GitHub topic placement.** Hypothesis: the OTel/observability audience browses curated lists more than it cold-searches a marketplace. Signal: a visible bump in weekly installs coinciding with listing acceptance, or a tracked referral link if the list format allows one.
- **T3 (optional, cut first if hours are tight) — one OTel-ecosystem touchpoint.** A short mention contributed to a popular OTel-adjacent project's docs, or an entry in an OTel tools/registry page if one exists. Signal: referral clicks from that page. This is the most speculative of the three — drop it before dropping T1 or T2.

## Core channel

Not decided yet — revisit at the test-ring end date. The working hypothesis, given the evidence already in hand, is that the core channel is the extension-marketplace family itself, done as dual-store rather than single-store — i.e., "core" here means keeping both marketplaces flawless (compatibility ranges, changelog, ratings) rather than chasing a new inner-ring channel. Promote a curated list to core status only if T2's referral numbers rival marketplace search by the review date.

## Refused

- **Creator/newsletter seeding** (family 8) — highest recurring cost of any family; a 3h/month budget doesn't cover relationship work on top of the foundation and test ring. Reopens at a named milestone (a 1.0, a major visualization feature) with a dated quarterly calendar.
- **Downstream/system packaging** (family 4) — not applicable. probe-lens installs through an editor marketplace; there's no binary or CLI unit to package into Homebrew, apt, etc.
- **Trust/procurement build-out** (signing, SBOM, Scorecard, family 9) — refused beyond the free verified-publisher badge already in the foundation ring. No enterprise deal in view and no evidence editor-extension adoption is procurement-gated here. Reopens if a real enterprise evaluation stalls in procurement.
- **Directory sprint** (spray-and-pray list submissions) — refused. At 3h/month, a wide submission spree creates sweep debt you can't service; 1-2 lists a real audience reads beats ten nobody checks.
- **JetBrains/Chrome/Firefox store expansion** — refused for now. probe-lens is VS Code-format; porting to another host is a rebuild, not a republish, and the current signal (Cursor requests) is already answered by Open VSX. Reopens if a comparable demand signal shows up for a different host.

## Release rhythm

- No cadence found in the audit yet — set one going forward: a predictable **maximum** interval (propose 4-6 weeks, adjust to your real fix rate), never a mandatory minimum; security fixes out of band.
- Publish to both marketplaces in the same CI step so they never drift.
- Changelog owner: whichever of the two of you ships the release; batch small fixes into one entry rather than one release per PR — a two-person team is exactly where "dependency-bump-as-a-release" noise starts and trains users to ignore the feed.

## Review sweep

- Metadata and stale-listing re-check quarterly, first sweep at week 12, aligned with the test-ring end date so both happen in one sitting.
- Re-measure baseline (installs on both stores, ratings, GitHub cloners/referrers) on the same cadence — too noisy to watch weekly, and there isn't spare capacity to watch weekly anyway.
- Kill rule: anything in the test ring below its stated signal at the review date gets cut, not extended.

## Threshold check

- **Sourced** (stale listings fixed before new channels) — pending: run the sweep before T2/T3 submissions.
- **Metadata 100% filled**, both marketplaces — pending, target end of week 2.
- **Recurring cost vs. capacity** — foundation ring ~1h one-time + minutes/release; test ring ~1.5-2h/month → total recurring under 3h/month, ~60-65% of a 3h ceiling if that's the confirmed distribution budget. Tight against the skill's 60% guardrail — if the real number is lower, drop T3 first.
- **Every channel has owner/hours/signal/review date** — yes, as listed above, once you assign names to "owns the Open VSX CI step" and "owns list submissions."
- **No harmful-decay channel without a sweep date** — yes, both marketplaces and both list entries are on the quarterly sweep.

---

## Confirm before running

1. Is probe-lens actually absent from Open VSX today? (If it's already there and Cursor users still can't find it, the problem is metadata/search ranking, not coverage — a materially different fix.)
2. Is the 8h/month distribution-only, or does it also cover support and dev work? Changes the test-ring size.
3. Any signal of team/company-level standardization on probe-lens (not just individual installs)? Would promote company-adoption legibility work above where it sits now.