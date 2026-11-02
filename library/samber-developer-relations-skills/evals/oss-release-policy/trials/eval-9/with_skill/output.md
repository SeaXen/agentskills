# Quillforge release policy: versioning, deprecation, and what to tell users

I didn't run the full interview, so the assumptions are listed at the end. You can drop in the sections below as written.

## Recommendation

Switch to CalVer in the `YY.N.MICRO` shape, with a written time-based deprecation rule. Twisted's `YY.M.MICRO` is the closest model, and pip's `YY.N` is the closest to your cadence.

- **Why not SemVer:** the skill ranks SemVer above CalVer for package-manager readers, but it names your case as the exception. Single-digit compatibility is impossible when every release removes something in some corner, and you already run a time-based deprecation rule.
- **The alternative:** one SemVer major per year that batches all removals. It keeps the resolver protection, but it would stretch your deprecation windows to a year or more and force a rewrite of the process you already run. I'd only pick it if you can't accept the bot problems below.
- **The cost you accept:** resolvers and update bots read the year as a major and N as a minor. The user-facing section below exists to deal with that.

The ordering check passes: `7.14.x` sorts below `27.1.0` under PEP 440, so no epoch is needed. Never shorten the year to `YYYY` later, and never go back to a small SemVer major without an epoch.

## RELEASES.md sections

### Version numbers

We use calendar versioning (`YY.N.MICRO`), written in normalized PEP 440 form, for example `27.2.0`.

- `YY` is the year of the release tag, so a release that slips into January takes the new year.
- `N` is the ordinal of the feature release within that calendar year (1, 2, 3). It restarts at 1 each January. We never publish an empty release to fill a slot.
- `MICRO` is for compatible bug and security fixes to a release that has already shipped.
- Segments are never zero-padded. The git tag, the wheel filename and the PyPI entry all read `27.2.0`.

The number says when a release shipped, not what broke. We do not publish a new major for removals. The compatibility rules are in "What we consider breaking" and "Deprecation".

We moved from `MAJOR.MINOR` (last release `7.15`) to this scheme. Every `YY.N.MICRO` version sorts above every `7.x` version.

### What we consider breaking

CalVer moves the contract into prose, so this section must exist before the scheme switch ships. It needs three lists.

- **Covered:** public modules and names, documented behaviour, default values, exception types, serialized formats, and the supported Python range. With roughly 2,000 modules, list the public namespaces by name. Don't say "everything documented".
- **Not covered:** underscore-prefixed names, undocumented modules, message text, and anything the docs call a bug.
- **Opt-in unstable:** any `experimental` namespace, and how it is marked.

A removal or an incompatible change to a covered item is a breaking change. Breaking changes ship only through the deprecation rule below.

Dropping a Python version follows the runtime rule. Declare the floor in `Requires-Python`. pip and uv fall back to the last compatible release, so dropping a Python version past upstream end-of-life may ship in a feature release (`N`). Dropping a version upstream still supports is breaking and follows the deprecation rule.

### Deprecation

Anything we plan to remove is deprecated first. **Removal comes no earlier than two feature releases and 12 months after the first release that warns, whichever is later.**

- **Warning mechanism:** a `QuillforgeDeprecationWarning`, a subclass of `DeprecationWarning`, so standard filters still work. A `@deprecated` marker (PEP 702) goes on the object for type checkers. Python hides `DeprecationWarning` outside `__main__` and test runners by default, so the docs tell users how to surface it (see the pip and bots section).
- **Warning text:** the replacement, the release that first warned, and the earliest removal release. We compute that release when the warning ships, record it in the changelog, and never move it earlier.
- **Where it is announced:** the changelog entry for the warning release, and a "Deprecated" entry in the docs with a stable identifier (`QF-DEP-0042`) that the warning also prints. The identifier is worth having because you deprecate in every release.
- **Where removal happens:** only in feature releases (`N`), never in `MICRO` releases.
- **Exception:** a security fix may remove or change a covered item without the full window. The advisory says so.
- **Transition:** everything already deprecated under 7.x keeps the 7.x rule (two releases). We publish that list, with the earliest removal release for each item, in the `7.15` announcement. Removals under the new 12-month rule start with deprecations issued in the first CalVer release.

That 12-month window is a change from today. Three releases a year means two releases is about 8 months. Twelve months is what Twisted uses, and pip uses at least 6. The longer window is the price of dropping the major bump as a signal. It also means each deprecated item stays in the tree for about four releases, so expect the maintenance bill for deprecated code to rise.

## What to tell users about pip and update bots

Publish this in the announcement and in the docs.

### pip and other resolvers

- **Existing ranges stay on 7.x.** `quillforge~=7.14`, `quillforge>=7.14,<8` and `==7.*` never select `27.x`. Nothing breaks, but nobody gets the new scheme until they edit the range once. Say that plainly in the announcement.
- **New ranges:**
  - `quillforge~=27.1` means `>=27.1, ==27.*`, which is "any 27.x from 27.1". It is the same calendar year, not a compatibility guarantee.
  - Quillforge stays safe to upgrade for anyone whose tests run clean of Quillforge deprecation warnings.
- **Safe upgrade rule:** warnings last at least 12 months before removal. Upgrade at least once a year, run your test suite with warnings as errors on each hop, and you will see every deprecation before it becomes a removal. Skipping several years in one jump can remove things you never saw warned.
- **Surfacing warnings:** `pytest -W error::DeprecationWarning` (or `-W error::quillforge.QuillforgeDeprecationWarning` to scope it), or `python -W error::DeprecationWarning`.
- **Pre-releases:** pip skips them unless asked. Use normalized spelling (`27.2.0rc1`).
- **Support for 7.x:** state which `7.x` line gets security fixes and until when (open item below). List every patched line in each security advisory's affected and patched ranges. Otherwise update bots propose a jump to `27.x` instead of the `7.x` backport.

### Dependabot and Renovate

- **How the bots read the number:**
  - The year rollover (`27.3` to `28.1`) reads as a major.
  - A change in `N` reads as a minor.
  - `MICRO` reads as a patch.
  - Neither bot knows our policy.
- **`7.x` to `27.x`:** the first upgrade shows up as a major PR, which is correct. Ask users to read the announcement before merging.
- **The real hazard:** the "automerge minors and patches" rule. Under this scheme a minor (`27.1` to `27.2`) can complete a removal whose warning has run its course. If a project never saw the warning, automerging that minor puts a break in production unreviewed.
- **What we ask dependents to do:**
  - Automerge only `MICRO` updates for `quillforge`.
  - Route `N` and year changes through CI with warnings as errors, and merge them only when the suite is green.
- **Renovate sketch** (check against the current docs; this is not verified here):

  ```json
  {
    "packageRules": [
      { "matchPackageNames": ["quillforge"], "matchUpdateTypes": ["patch"], "automerge": true },
      { "matchPackageNames": ["quillforge"], "matchUpdateTypes": ["minor", "major"], "automerge": false }
    ]
  }
  ```

- **Dependabot:** it has no equivalent per-package automerge control. Use its `groups`, or GitHub auto-merge conditioned on CI, and keep the CI warnings-as-errors job as the gate.
- **Cooldowns:** if dependents use Renovate's `minimumReleaseAge` or Dependabot's cooldown settings, a short cooldown on `quillforge` buys time for regressions to surface.
- **Distro packagers:** tell them directly before the first CalVer release. No epoch is needed because the numbers only go up. Do not reuse or lower a version.

## Announce and publish

1. Announce the scheme and this policy in the `7.15` release notes. The first CalVer release follows at least one release later.
2. Add this line at the top of the changelog: *"This project uses calendar versioning (`YY.N.MICRO`). See RELEASES.md for what each number promises and which versions get fixes."*
3. Link `RELEASES.md` from the README. Update the version badges and docs headers in the same release.
4. State the last `7.x` version and its support end date.
5. Record the ordering check and its result: `7.15.x < 27.1.0`.

## Open items before this is a complete policy

The skill's validation needs these, and I couldn't fill them without your answers.

- **Last `7.x` support window.** A security-only line for 12 months is the usual starting point. Size it first: security fixes in the last 12 months × hours per backport must fit the maintainers' monthly release hours. Send me the fix count and the hours and I'll show the arithmetic.
- **Public-surface lists.** The covered, excluded and unstable lists above are templates. At 2,000 modules, naming the public namespaces is a real piece of work.
- **Supported-versions table, backports, cadence, publish rights.** Not drafted. Say if you want them next.
- **Window length.** You currently deprecate for two releases. Confirm whether you accept the 12-month floor or want to keep 8 months (two releases), accepting a shorter warning period.
- **Assumptions I made:** Quillforge publishes only to PyPI, ships no CLI that other tools parse, and has company users with change control. If it also publishes elsewhere (conda, distro packages, containers), the tooling section needs extending.