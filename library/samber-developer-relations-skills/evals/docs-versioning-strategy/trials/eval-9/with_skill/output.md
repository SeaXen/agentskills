**Next action:** answer the 3 open questions at the bottom, ~5 minutes. Everything below is `ASSUMED` until you do.

# Docs versioning plan: Windlass

**Assumptions (`ASSUMED`):**
- 2.x support end date is unknown. Supply it.
- 3.x is supported until 4.0 plus a window. Supply it.
- 2.x and 3.x differ in some instructions, but share one config schema.
- Docs are one branch, built by a static-site tool that supports custom directives or components.
- About 12 doc fixes per month, and the host can redirect.
- The writer has about 2h per month spare for standing work.
- 4.0 ships around 2026-12-23.

**Unvalidated sections:** all of them. No interview was possible, and no one has agreed to any section.

## Verdict

Cumulative badges for 2.x/3.x are allowed, with one hard gate and one scope limit.

- **Gate: a lint in the build step.** The skill deletes this rung when there is no lint capacity. Engineers merge docs PRs straight in, so any untagged change silently misleads 2.x readers.
- **Scope: badges cover 2.x and 3.x only.** Your model, Elastic, uses badges inside one major (9.x) and dropped per-minor sets at 9.0. The 4.0 config-schema rewrite is a major boundary, and the skill promotes per-major sites there. 4.x gets its own set.
- **Reject lint, or 2.x ends by about March 2027:** skip badges. Use "changed in 3.0" stamps on the 5-10 worst-differing blocks, plus a frozen 2.x snapshot at the 4.0 cut. The payoff window is too short for a full tagging pass.

## Product class

- **Primary:** several supported lines with breaking differences (2.x, 3.x, then 4.x). Self-hosted servers are pinned by users, so they stay on old lines.
- **Secondary:** old lines unsupported but still installed (1.x, if it exists; check downloads per version).

## Docs version policy table

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 4.x | unreleased, rewrite | n/a | `next`: draft branch, previews only, not in production | `current` at 4.0 release | n/a |
| 3.x | current | until next major | `current` | `maintained` at 4.0 release | released behaviour |
| 2.x | supported older | TBD (`ASSUMED`) | `maintained`, as badged blocks inside the 3.x set | `frozen` at support end | security, data loss, upgrade blockers |

- **Unversioned content:** tutorials with no difference, concepts, changelog, blog, community pages.
- **Granularity:** one docs set per major. 3.x minors are additive and get "since 3.N" stamps only.
- **URL shape:** versioned path plus `latest` alias.
  - Put the cumulative set at `/3.x/`, titled "3.x (includes 2.x notes)".
  - Put 4.x at `/4.x/`.
  - Segments are lines, not releases.
  - Moving current unversioned URLs to `/3.x/` now means the 4.0 cut never changes what a deep link means.
- **Consolidation redirects:** current unversioned `/x` to `/3.x/x`, per page. Hand the list to `docs-seo`.
- **Components:** the runner version drives the switcher. If there are separate SDK or agent versions, publish one compatibility matrix page.

## Topology

- **Reference:** link per-release CLI or API reference if the binary or registry generates it. Version only guides.
- **Chosen:** cumulative badges for 2.x/3.x, then per-major sets from 4.0.
- **Rejected:**
  - Latest-only strands supported 2.x readers.
  - A selector across 2.x and 3.x costs backports on two versions, with 2.x about to end.
- **Short-lived second line:** compare badges with stamps plus an early freeze once the 2.x end date is known. See the verdict.

## What to tag

**Rule:** tag a block only when it is true for some supported lines and not others. Untagged means "applies to all supported lines". Do not tag per patch.

Tag in this priority order, and stop when the worklist is done:

1. Install and system requirements.
2. CLI flags and commands.
3. Defaults and behaviour (retries, cache, timeouts).
4. Auth and permissions.
5. Upgrade-blocking steps.

Worklist source: the 2.x-to-3.0 changelog and migration guide. Do not read every page.

**Do not tag:**
- Config schema pages, because 4.0 rewrites them and they live in the 4.x set.
- Tutorials, concepts, the changelog and the blog.

## How to tag

**Page front matter, mandatory on every page:**

```yaml
applies_to:
  lines: [2.x, 3.x]
```

**Block directive, only where lines differ:**

```markdown
:::applies{lines="3.x" since="3.4"}
Runner pools support autoscaling.
:::

:::applies{lines="2.x"}
Set `pool_size` manually.
:::
```

- **Vocabulary:** `lines` is `2.x`, `3.x` or both. `since` is a 3.x minor, for additive features only.
- **Unreleased content:** use `coming-in="3.5"`. At the release cut, rewrite it to `since`.
- **Rendering:** the badge is visible text, for example "Applies to 3.x only · since 3.4". Crawlers and AI feeds then see it. Do not use CSS-only pills.

## Lint

It runs inside the existing build command, so there is no new CI. It fails the build on:

1. A page with no `applies_to`.
2. An unknown line, or a `since` above the latest released minor.
3. An unclosed or empty directive.

**What it cannot catch:** a behaviour change written into untagged text. Two controls cover that gap:
- **PR template checkbox, required wording:** "Does this change differ between 2.x and 3.x? If yes, tag it."
- **Weekly sweep by the writer, 30 min:** run `git log --since=7.days -p -- docs/` and fix untagged differences. This costs about 2h per month and is the real safety net.

**Cost:** about half a day of engineering time, baseline. The writer does not write it.

## Source layout and release cut

- **Layout:** one cumulative source on main until 4.0.
  - 4.x draft lives on branch `docs-4x`, previews only.
  - Engineers' PRs for 4.0 config go to `docs-4x`. Everything else goes to main.
  - Built per deploy: `current` only. Snapshots: static output for `frozen` versions.
- **Release cut, one checklist in the release process:**
  1. Cut release branch `docs-3.x` from main.
  2. Merge `docs-4x` into main.
  3. Move the `latest` alias to `/4.x/`.
  4. Put the `maintained` banner on `/3.x/`.
  5. Update the switcher.
  6. Rewrite "coming in" marks to "since".

## Backport rule and cost (baseline figures, replace after one month)

- **Before the cut:** `current` builds from main, so keeping it in step costs 0. The weekly sweep adds about 2h per month.
- **After the cut:** `current` is 4.x on main, so that term is 0 again. 3.x becomes `maintained`: 12 fixes × 15% qualifying × 1 version × 20 min ≈ 36 min per month.
- **Total:** about 2.6h per month before the cut, and under 1h per month after. Compare it with your real ceiling.
- **Rule:** backport to `current` for released behaviour. Backport to `maintained` only for security, legal exposure, data loss or an upgrade blocker. Never fix `frozen` or `archived`. Tag backport targets in the PR at review time.

## Rollout

Today is 2026-10-23, so there are about 9 weeks to the cut.

1. **Week 0 (about 1h):** answer the 3 questions below. If the 2.x end date is before about March 2027, switch to the lean option in the verdict.
2. **Week 1:**
   - An engineer writes the lint, and a script backfills `applies_to: [2.x, 3.x]` on all pages.
   - Moving `/x` to `/3.x/x` also happens now, with its redirect list.
3. **Weeks 2-3 (writer, time-boxed):** tag the priority list from the changelog worklist. Stop when it is exhausted.
4. **Week 3:** ship badge rendering, the PR template checkbox and a short CONTRIBUTING note. Send engineers one message with the two example directives.
5. **Weeks 4-8:** run the weekly 30-min sweep. Track misses found per sweep. A falling count shows engineers are tagging.
6. **Weeks 6-8:** write the 4.x rewrite on `docs-4x`. Freeze new 2.x/3.x tagging work.
7. **Cut day (about 2026-12-23):** run the release-cut checklist above.

## Reader routing

- **Default:** `current`, reached through `/latest/`.
- **Switcher:** same-page switch, with fallback to the nearest ancestor section.
- **Banners:** `maintained` on 3.x after the cut. Use the template from `banners-and-selector.md`.
- **Search:** scoped to the version being read.
- **Links:** support replies, the README and blog posts link to the `latest` alias.
- **AI feeds:** `current` only.

## Search-entry intent (handed to `docs-seo`)

- `current` is the canonical target.
- `maintained` 3.x gets its own entry, or is folded into `current`. `docs-seo` decides.
- 2.x has no own pages, because it lives as badges inside the 3.x set.

## Retirement procedure

1. **Trigger:** 2.x support end moves 2.x to `frozen`. Stop tagging new 2.x differences.
2. **Evidence:** check per-version views and downloads. Baseline threshold to archive: under 1% of views and downloads for two quarters.
3. **Snapshot** the set, swap to the frozen banner, and redirect per page to the nearest current equivalent.
4. **Announce** the retirement in the changelog.

## KPIs (baselines)

| KPI | Target |
| --- | --- |
| Untagged differences found per weekly sweep | falling to 0 |
| Wrong-version tickets and arrivals | falling quarter on quarter |
| Lint build failures per month | stable or falling |
| Standing docs hours per month | within the estimate above |
| Switcher 404s | 0 |
| Per-version share of views and downloads | read each quarter against the retirement threshold |

## Open questions

1. When does 2.x support end, and 3.x after 4.0? This decides badges versus the lean stamps option.
2. Does your docs tool support custom directives or components? Which tool is it?
3. Do you approve a half-day lint step in the existing build? Without it, badges are out.

**Sections written without agreement:** all. Confirm them one at a time, starting with the product class.