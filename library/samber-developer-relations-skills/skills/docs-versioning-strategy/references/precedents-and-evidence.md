# Precedents and evidence

Load when the user challenges a recommendation, or when a step needs a named precedent.

## Contents

- Retention by project
- Topology switches
- Source layout costs
- Backport rules
- Retirement data
- Sourced versus baseline figures

## Retention by project

| Project | Docs kept | Relation to support |
| --- | --- | --- |
| Kubernetes | current + 4 previous minors, older on snapshot hosts | wider than the 3 patched minors; docs availability declared separate from support |
| PostgreSQL | every version back to 7.x | header splits supported, development, unsupported |
| Python, Django | old release lines kept online | unsupported lines bannered; Django's banner says "insecure" |
| React | one docs set per major, no minor or patch docs | old majors archived at `NN.react.dev` |
| Vue, Angular | current major on main site, old majors on own hosts | archived banner |
| Elastic | one cumulative 9.x set with `applies_to` badges | dropped per-minor doc sets at 9.0 |
| Stripe | one current reference, tailored per account when logged in; changelog and upgrade guide | account-pinned dated versions |
| MongoDB | supported in main docs, end-of-life versions on a legacy index | "does not maintain or update legacy documentation" |
| Terraform providers | per-version menu in the registry; some vendors move old majors to PDF | docs for active provider versions until end-of-life |

## Topology switches

- React moved to react.dev in 2023 and redirected every old link to legacy.reactjs.org "to avoid 'breaking the web'".
- Angular users objected to latest-only docs in 2017; Angular moved to per-major hosts.
- Vue: "active maintenance of two major versions in parallel isn't sustainable for us"; Vue 2 docs froze on their own host.
- Elastic switched from per-minor doc sets to one cumulative set with version badges.
- Spring moved to a versioned docs generator from 6.0.9 and left earlier versions at legacy URLs with permanent redirects.

## Source layout costs

- Build-once-and-freeze tools (one branch per version) never rebuild old versions, so toolchain upgrades cannot break them.
- Docusaurus maintainers: "Most of the time, you don't need versioning as it will just increase your build time"; keep under about 10 versions; build 2-3 in previews; archive older versions as immutable deployments linked as external versions.
- Reported folder-per-version builds: 131 versions and about 50,000 files with high memory and build time; 20-minute builds running out of memory in CI. Single cases, self-reported.
- Docs-tool vendors claim large duplication savings from single-source versioning; treat as marketing, not measurement.

## Backport rules

- Django: documentation fixes "will be more freely backported to the last release branch" - the latest stable branch only, not older supported ones; after a release candidate, only release blockers and documentation fixes.
- GitLab: backport important docs changes to the current stable release; older releases "only rarely", for legal issues, emergency security fixes, and content that might block upgrades or cause data loss.
- Ansible docs: stable branches per minor, backport labels processed by a bot, small fixes backported at least to the latest stable branch.
- PostgreSQL: no effort spent fixing docs of de-supported versions.

## Retirement data

- pandas: 28 days of analytics showed about 120,000 views on old-version paths, about 2% of all views; one old line was still downloaded more than newer ones. Maintainers kept the versions.
- Adjacent case: python-future dropped content for Python 2.6 and 3.3 citing 0.04% and 0.02% of downloads. It concerns runtime support, so read it as an analogous threshold, not a docs-version retirement.
- No project publishes a traffic or download threshold for retiring a docs version.

## Sourced versus baseline figures

| Figure | Type |
| --- | --- |
| Kubernetes 5 documented vs 3 patched minors | sourced |
| Docusaurus "under about 10 versions" | sourced (maintainer guidance) |
| pandas ~2% of views on old versions | sourced |
| 10-30 minutes per backport | baseline, replace after one month |
| 10-20% of fixes qualify for older lines | baseline, replace after one month |
| Under 1% of views and downloads for two quarters to archive | baseline, replace with the team's own threshold |
