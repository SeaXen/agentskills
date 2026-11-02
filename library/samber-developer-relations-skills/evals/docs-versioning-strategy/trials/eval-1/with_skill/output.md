# Docs versioning plan: Ferrocast

**I recommend against turning on the dropdown, so there are no canonical tags to write.** Ferrocast has one callable API behaviour and four additive release names. A dropdown of those four would show readers pages that no client can call.

Assumptions: I couldn't interview you, so these are `ASSUMED`. Correct any that are wrong and I'll re-run the plan.
- Release names are marketing or changelog labels, not something a client can select.
- No release line has separate support.
- The docs have no per-release package or SDK reference.
- Docs fixes run at about 15 per month, which is a baseline.

Unvalidated sections: all of them, because you haven't agreed to any yet.

## Product class

Primary: **hosted API, one callable behaviour.** One deployment, no version header, no pinning, and nothing ever removed. Secondary: none, because there are no retired lines.

The decision for this class is latest-only reference, plus a changelog and an upgrade guide per breaking version. You have had no breaking versions yet.

## Docs version policy table

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| Live API (named 2025.1 today) | The only deployed behaviour | n/a | `current`, the only docs set | None. A breaking change would create a callable second version. | Every fix lands once |
| 2023.2, 2024.1, 2024.3 | Superseded labels, same endpoints still serving | n/a | None. They exist only as changelog entries and stamps. | n/a | n/a |

- **Unversioned content (all of it):** reference, guides, tutorials, concepts, changelog, blog.
- **Granularity:** there is one docs version, because every release name hits the same endpoints. A per-release docs set would describe behaviour that is no longer deployed.
- **URL shape:** an unversioned path (`/docs/...`). This is the allowed case: one supported line and latest-only docs. Don't put release names in URLs.
- **Consolidation redirects:** none. You aren't collapsing anything.
- **Components:** single component.

## Topology (brainstorm, then recommendation)

Rungs deleted by your answers:
- **Selector and per-major frozen sites:** deleted because the API is additive and has one callable behaviour.
- **Cumulative badges:** I'd drop these too. They need a lint for untagged changes, and you don't need them when nothing is ever removed.

Surviving options:
1. **Latest-only with "added in" stamps.** Each feature or field carries "added in 2024.3". The changelog and release-to-date page carry history. Standing cost is about zero, because every fix lands once.
2. **Selector over four releases.** This is the "free" platform toggle. It's the only other option, and I rejected it for the reasons below.

**Recommendation: option 1.** Rejected option 2, with these costs:
- **Wrong pages for live behaviour.** A reader choosing "2023.2" sees docs that omit fields and endpoints the live API returns today. The page is wrong about the API they're calling. A payments API dropdown works because each version is pinned and callable; yours isn't.
- **Backports.** Every fix to released behaviour has to be copied into each older version, or those versions rot.
- **Wrong-version arrivals.** Readers who land on 2023.2 from search will believe they are limited to that feature set.
- **Not free.** The platform makes the toggle free, but you still pay the standing cost. That cost is backports per fix × versions × minutes, plus support tickets from wrong-version readers.

Priced with baselines. These numbers replace `ASSUMED` ones after one month:
- **Latest-only:** 0 extra hours.
- **Selector with four versions:** 15 fixes × 100% touching released behaviour (since all four describe the same live API) × 3 older versions × 15 minutes ≈ **11 hours per month**. The skill's baseline of 10–20% of fixes qualifying assumes older lines with different behaviour, so it doesn't apply here.

## How to answer sales and the PM

The PM's goal is "enterprise customers can see the docs as of the release they evaluated." You can meet it without a dropdown:
- **"Added in" stamps** on every feature, field and endpoint, e.g. "Added in 2024.3". A reader evaluating 2024.1 can see what was there then.
- **A release-names page** mapping 2023.2, 2024.1, 2024.3 and 2025.1 to dates, linked from the changelog. Without it, the names mean nothing to a reader.
- **A per-release "what was new" section** in the changelog, so "as of 2024.1" is answerable in one page.
- **A "what changed since" link** in sales material, pointing to the changelog entries after the release the customer evaluated.

For sales, the line is: "Payments APIs have a dropdown because customers pin an API version and keep calling the old one. Ours has one version, so a dropdown would show them docs for an API they can't call."

If an enterprise customer needs a frozen copy of the docs for a procurement record, export `current` as a dated PDF or snapshot at that time. Don't keep it live in the docs build.

## Source layout and release cut

- **Layout:** the hosted platform, with versions off. One docs set, one build.
- **Built per deploy:** `current` only. No snapshots.
- **Release cut:** add the release name and date to the release-names page, convert "coming in X" marks to "added in X", and publish the changelog entry. The alias doesn't move, because there's no versioned path.

## Backport rule

- **Current in step:** 0, because there's one docs set built from main.
- **Maintained:** 0, because there are none.
- **Total:** 0 hours per month of version upkeep. Your effort ceiling is unknown, but zero fits any ceiling.
- **Rule:** fix once, in `current`. A frozen or archived copy never gets fixes.

## Reader routing

- **Default:** `current`, the only set.
- **Banners:** none. No page documents a non-current version.
- **Site search:** one scope, `current`.
- **Aliases:** nothing to alias.
- **AI feeds:** one `llms.txt`-style feed on `current`.

## Search-entry intent (for the docs SEO pass)

Everything is a single canonical set, so there are no per-version entries.

**Canonical tags on older versions: none are needed.** You have no older versions. Each page exists once, at one URL, so each page's canonical is its own URL. Adding a version dropdown is what would create duplicate or near-duplicate pages that need canonicals pointing at `current`.

If you later ship a breaking change and keep the old behaviour callable, the canonical posture and redirect mechanics belong to `samber/developer-relations-skills@docs-seo`. I only state intent here: `current` would be the canonical target, and any older callable version would get its own entry or be folded into `current`.

## Retirement procedure

- **Trigger:** none today. Nothing exists to retire.
- **If a second callable version appears:** snapshot the older one as static output and apply a frozen banner. Then archive it when it falls under the retirement threshold, a baseline of under 1% of docs views and of API traffic for two quarters. Redirect per page to the nearest `current` equivalent, never to the docs home.

## When to revisit

Reopen this plan when **any one** of these happens:
- You ship a breaking change, so two behaviours are callable.
- You add version pinning or a version header.
- You run a documented support window on an older release.

At that point the "selector over one site" rung applies, capped at the number of versions clients can call at once.

## KPIs

| KPI | Baseline | Target | Owner |
| --- | --- | --- | --- |
| Support tickets saying "docs don't match the API" | measure first | falling | you |
| Sales or PM requests for a "docs as of release X" view | count now | falling after the stamps and release-names page ship | you |
| Share of pages with an "added in" stamp | 0% | 100% of features added since 2023.2 | docs |
| Full build time | current | no growth at each release | docs |

## Next step

Tell me which assumptions are wrong, especially the first one: whether the release names are selectable by a client in any way. If they are, for example through a hidden header, behaviour flags, or per-account feature gating, the plan changes. I'd start with the stamps and the release-names page, since those are the part of the PM's request that works today.