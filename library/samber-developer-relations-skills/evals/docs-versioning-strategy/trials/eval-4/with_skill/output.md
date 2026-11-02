# Tarnhelm docs: banner copy and version-switcher spec

I followed `docs-versioning-strategy` (SKILL.md and all three references). It calls for an interview, but you weren't available, so every unanswered item is marked `ASSUMED` and the deliverable is unvalidated.

**Four of your five asks conflict with the skill's rules, so I changed them:**

| Your ask | What I did | Why |
| --- | --- | --- |
| Reuse "You are viewing an older version. Go to the docs." on 5.0 beta pages | **Rejected.** Five state-specific banners, one shared component | The line has no status word and no consequence, and it links to the home page. On a beta page it says the opposite of the truth: 5.0 is newer, not older. |
| Docs home shows 5.0 beta | **Changed.** Home lands on 4.x | The default is always `current`, never `next`. Beta docs as default document features readers can't install. |
| Dropdown lists all 31 versions | **Rejected.** 4 entries plus one "All releases" link | A 31-entry list runs off the screen (SciPy's did). Exact-version needs are served another way (see Part 2). |
| Cookie, then redirect Google arrivals to the remembered version | **Replaced** with a non-redirecting suggestion | Redirecting search arrivals is on the skill's "Don't" list. |

## Assumptions

- **A1.** Current stable is 4.7. The latest per-release line is 4.x.
- **A2.** 3.x is supported with no end date given. 5.0 beta ships as 5.0 GA and becomes current.
- **A3.** The 2.x XML-parser CVE is public and has an advisory URL (`{advisory-url}`). If the CVE isn't public yet, drop the link and the "XML parser" wording from the banner and say "known security issue".
- **A4.** 1.x has no known vulnerability. **Please check whether 1.x shares the 2.x XML parser.** If it does, 1.x gets the insecure banner too.
- **A5.** Per-release Javadoc is published (Maven Central or javadoc.io). If it isn't, versioning the reference goes back on the table.
- **A6.** Minors within a line are additive, so docs are versioned per major.
- **A7.** No CI capacity for a docs lint.
- **A8.** Doc fix volume is 20 per month, for pricing only.

## Part 1: Docs version policy

| Version | Product status | Support ends | Docs state | Next transition and trigger | Backport? |
| --- | --- | --- | --- | --- | --- |
| 5.0 beta | Beta | n/a | `next` | Becomes `current` at 5.0 GA | Stays on main |
| 4.x (4.7) | Current stable | Until next major | `current` | `maintained` when 5.0 GA ships | Released behaviour |
| 3.x | Supported | `{date, ASSUMED}` | `maintained` | `frozen` at support end | Security, legal, data loss, upgrade blockers |
| 2.x | Unsupported, **unpatched CVE** | Ended | `frozen` | `archived` below threshold | Never |
| 1.x | Unsupported | Ended | `frozen` | `archived` below threshold | Never |

- **Granularity:** one docs version per major, so 31 releases collapse to four lines plus the beta.
- **Unversioned content:** tutorials, concepts that never changed, changelog, blog, the all-releases page.
- **URL shape:** `/4.x/` behind a `/latest/` alias, with line segments (`/3.x/`), not release segments. `/next/` serves the beta. Support replies, README and blog posts link to `/latest/`.
- **Consolidation redirects:** if per-minor URLs exist (`/4.2/*`), redirect each page to `/4.x/*`. Likewise for 1.x, 2.x and 3.x. These go to the docs SEO pass.

## Part 2: Version-switcher spec

**Entries (4 plus one link):**

```
Preview
  5.0 beta (unreleased)
Supported
  4.x (latest, 4.7)        <- default, checkmark
  3.x (supported)
Older versions (unsupported)
  2.x (insecure)
  1.x
-----
All releases and exact versions ->
```

**Exact versions for enterprise customers.** The "All releases" page is a single unversioned page with one row per release, 1.0 through 4.7, and these columns:

- release date
- docs line it belongs to (link to `/4.x/` etc.)
- changelog entry
- Javadoc for that exact release (A5)
- support status

Docs are per line. The exact release is answered by "added in", "changed in" and "removed in" stamps on pages and by the per-release Javadoc. This gives enterprises their exact version without 31 copies of the guides.

**Behaviour:**

1. **Default.** Landing is `current` (4.x). Docs home and `/latest/` resolve to 4.x. The beta is reachable only through the switcher or `/next/`.
2. **Same-page switching.** Switching keeps the page. If the page doesn't exist in the target, open the nearest ancestor section and show a one-line notice: "This page has no equivalent in {target}. Showing {section}."
3. **Search scope.** Search is scoped to the version being read (4.x by default). 1.x and 2.x pages are searchable only from their own pages and through "Older versions".
4. **Support state in labels.** Supported or unsupported is shown next to each label.
5. **Instrumentation.** Log switcher clicks and switcher 404s. Target is zero 404s. No public study measures switcher success, so treat this data as your evidence.

**Remembering the reader's choice (replaces your cookie plus redirect):**

- Store the choice **in the browser (`localStorage`), written only when the reader clicks the switcher**. It is first-party, never sent to a server, and only a functional preference. Confirm with whoever owns your consent policy.
- **Never redirect.** A reader arriving from Google keeps the page they searched for.
- **If the arrival's line differs from the stored line:** show a dismissible one-line suggestion under the state banner: "You last used 3.x. View this page in 3.x." Use the same-page and ancestor-fallback rules.
- **Docs root only:** a visit to `/` with no deep link and no search referrer may open the stored line. This is my judgment, not the skill's, so drop it if you want zero redirects.
- **Why:** a redirect changes what a search result means. PostgreSQL contributors listed cookie redirects from search visits as not recommended. Redirects also complicate canonicals, which belong to the docs SEO pass.

## Part 3: Banner copy

**One banner component, five states.** This replaces the two-banner worry: you maintain one component and one copy table. Each banner has a status word, a consequence and a same-page link to `current`. If the page is missing in 4.x, the link falls back to the ancestor section, with the same notice as the switcher.

| State | Where | Copy |
| --- | --- | --- |
| `next` | 5.0 beta pages | "This page documents Tarnhelm 5.0 beta, an unreleased version. Features here may change or not ship. See this page for the current release (4.7)." |
| `current` | 4.x pages | No banner. |
| `maintained` | 3.x pages | "This page documents Tarnhelm 3.x, a supported older release. See this page for the latest release (4.7)." |
| `frozen` | 1.x pages | "Tarnhelm 1.x is no longer supported and this page is a static snapshot. Upgrade, and see this page for the current version (4.7)." |
| `frozen`, insecure | 2.x pages | "Tarnhelm 2.x is insecure and no longer supported: its XML parser has a known vulnerability (`{advisory-url}`) that will not be fixed. Upgrade, and see this page for the current version (4.7)." |
| `archived` index | Archive page, later | "These versions are archived and receive no updates. Each page links to its current equivalent where one exists." |

- **Wording stays distinct.** The 5.0 banner never says "older" or "unsupported". PostgreSQL's reuse of its unsupported banner on devel docs is the failure to avoid.
- **"Insecure" is only for 2.x**, because it is the only line with a known, unfixed vulnerability (A4).
- **Replace the old banner on all existing 1.x, 2.x and 3.x pages.** "You are viewing an older version. Go to the docs." sends readers to the home page, which would now be 4.x, not their page.
- **The beta banner also keeps tickets down.** Django added its banner partly to ward off tickets against old versions.

## Part 4: Topology, source layout and release cut

**Chosen: selector over one site for beta, 4.x and 3.x, plus static snapshots for 2.x and 1.x.** This is `ASSUMED`.

- **Rejected: latest-only.** Enterprise customers are pinned to supported lines, and 3.x readers need their own pages.
- **Rejected: cumulative badges.** There is no CI capacity for the lint (A7), so an untagged change would silently mislead old-line readers.
- **Rejected: per-major frozen for 3.x.** A supported major on its own host costs the selector's backports plus a second deploy. It fits 2.x and 1.x.

**Layout:**

- **Branch or tag per version, build once and freeze.**
- **Built per deploy:** 5.0 (main), 4.x (release branch), 3.x (release branch). Previews build 4.x and 5.0 only.
- **Static snapshots:** 2.x and 1.x. Produce them before they leave the build, so toolchain upgrades can't break them.

**Release cut at 5.0 GA:**

1. 4.x becomes `maintained`.
2. The `/latest/` alias moves to 5.x.
3. The switcher updates, with the "latest" label moving to 5.x.
4. Banners swap.
5. The beta label and banner are removed.
6. "Coming in 5.0" marks become "added in 5.0".

## Part 5: Backport rule and price (all baseline, A8)

- **Rule:**
  - Backport released-behaviour fixes to `current`.
  - Backport to `maintained` only for security, legal exposure, data loss or an upgrade-blocking step.
  - Never fix `frozen` or `archived`.
  - Tag each doc PR with its backport targets at review time.
- **Keeping 4.x in step:**
  - This term is not zero, because main carries the beta.
  - 20 fixes × 50% touching released behaviour × 15 min ≈ **2.5 h/month**.
- **Maintained backports (3.x):** 20 × 15% × 1 × 20 min ≈ **1 h/month**.
- **Total:** about **3.5 h/month**, baseline. Replace the shares and minutes after one month. Compare the total against your standing-hours ceiling.
- **If over the ceiling:** drop the separate beta build and mark unreleased content inline ("coming in 5.0") instead. Or freeze 3.x early.
- **2.x CVE:** the rule does not backport to frozen versions, so the fix is the banner and the advisory link, not a docs edit.

## Part 6: Search-entry intent (for the docs SEO pass)

- `next`: no own search entry.
- 4.x: canonical target.
- 3.x: own entry or folded into 4.x, per the SEO posture.
- 2.x and 1.x: own entry only while downloads stay above the threshold and the SEO posture allows it.

Mechanics (canonical tags and redirect maps) belong to `docs-seo`. I wrote none.

## Part 7: Retirement and KPIs

- **Retirement:** 2.x and 1.x move to `archived` when both of these hold for two quarters:
  - under 1% of docs views
  - under 1% of downloads

  The threshold is baseline, so replace it with your own. Archived versions leave the dropdown and appear on an archive index.
- **Removal:** only when there are no measurable readers. Redirect each page to its nearest current equivalent, never to the docs home.
- **Announce** retirements in the changelog.

| KPI | Target (baseline) | Owner |
| --- | --- | --- |
| Wrong-version arrivals from search or AI referrals | Falling quarter on quarter | `{docs owner}` |
| Switcher 404s and "wrong version" tickets | Zero 404s, tickets falling | `{docs owner}` |
| Backport hours per month | Within the 3.5 h estimate | `{docs owner}` |
| Build time and versions built per deploy | No growth at each release cut | `{docs owner}` |
| Per-version share of docs views and downloads | Read quarterly against the retirement threshold | `{docs owner}` |

## Questions that would change this plan

1. **Q1.** When does 3.x leave support?
2. **Q2.** Is the 2.x CVE public, and does 1.x share the XML parser?
3. **Q3.** Do you publish per-release Javadoc?
4. **Q4.** How many doc fixes land per month, and what is your standing-hours ceiling?
5. **Q5.** Do 3.x and 4.x instructions really differ? If not, latest-only plus stamps would be cheaper than the selector.