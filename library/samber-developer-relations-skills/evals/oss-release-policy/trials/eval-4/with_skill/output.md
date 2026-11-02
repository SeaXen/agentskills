❌ **Do not tag `1.0.0` on either registry.** `1.0.0` sorts below `2026.3.1`, so the plan fails the ordering check in `references/scheme-switching.md`. I did not run the checks below. This is from the skill's reference and the registry rules.

## What breaks if you tag 1.0.0

| Surface | Result |
|---|---|
| PyPI | pip picks the highest version. `pip install marrowline` keeps installing 2026.3.1 and never selects 1.0.0. |
| PyPI fix | The epoch `1!1.0.0` works, but it is permanent. A pin `==1.0.0` means epoch 0 and fails. |
| npm | A fresh install follows the `latest` dist-tag, so it could get 1.0.0. Recent npm refuses a lower-than-latest publish without `--tag`. Every `^2026.3.1` range is stranded and never sees 1.0.0. |
| Debian | dpkg ranks 1.0.0 below 2026.3.1. The packager must add epoch `1:` before the release, or apt never upgrades. |
| Cross-registry | npm shows `1.0.0` and PyPI shows `1!1.0.0`. "Same number everywhere" is gone. |

## Recommendation

Ship the SemVer break as **`2027.0.0`**, marketed as "Marrowline 1.0".

- Ordering holds on npm, PyPI and dpkg. No epoch is needed, and the same number appears on both registries.
- The mapping table in the announcement covers marketing's "1.0". The number the resolver sees stays 2027.0.0.
- Cost: the major is a counter that starts at 2027, not a year. The next break is `2028.0.0`, and that is "Marrowline 2.0". The policy says so explicitly.
- Rejected alternatives: `1!1.0.0` with a Debian epoch, or a new package name (`@marrowline/sdk` and `marrowline` both lose their install base).
- The skill says you pick. If you pick the epoch route, see "If you choose 1.0.0 anyway" at the end.

I wrote the deliverables for 2027.0.0.

---

## Deliverable 1: RELEASES.md, "Version numbers" section

Square-bracket items need your input. I did not invent them.

````markdown
# Release policy

## Version numbers

From 2027.0.0, Marrowline uses Semantic Versioning (`MAJOR.MINOR.PATCH`).

- MAJOR: an incompatible change to the covered surface below.
- MINOR: a backward-compatible addition or a new deprecation.
- PATCH: a backward-compatible fix.

Before 2027.0.0 we used calendar versions (`YYYY.M.PATCH`). The last one is
2026.3.1 [or the final 2026.x release]. The number said when we shipped, not
what broke.

The MAJOR starts at 2027 so that every new version sorts above every calendar
version on npm, PyPI and Debian. It is a counter, not a year. The next
breaking release is 2028.0.0 even if it ships in 2027.

| Product name | Package version |
| ------------ | --------------- |
| Marrowline 1.0 | 2027.0.0 |
| Marrowline 2.0 | next MAJOR (2028.0.0) |

Both registries publish the same version number: `@marrowline/sdk` on npm,
`marrowline` on PyPI. Pre-release spelling differs only where the registry
requires it (see Pre-releases).

## What we consider breaking

Covered: [exported names and signatures, documented behaviour, default values
such as timeouts and retries, error classes and their codes, serialized formats,
shipped TypeScript types and the supported TypeScript range, Python type hints].
Not covered: [paths outside the `exports` map and private modules, log text,
undocumented ordering, behaviour the docs call a bug].
Opt-in unstable: [`experimental` modules; none if none].

A changed default is breaking when callers could rely on it. When unsure, we
ship a MAJOR. Dropping a runtime that its upstream still supports is breaking.

## Runtime support

[Node.js lines: Active and Maintenance LTS, declared in `engines.node`.]
[Python versions: declared in `Requires-Python`; pip and uv fall back to the
last compatible release.] Dropping a runtime that upstream no longer supports
ships in a MINOR, announced one release ahead. [Debian Python users: the floor
follows Debian stable's Python, not only upstream's, if you target them.]

## Pre-releases and channels

| Registry | Release candidate | Channel |
| -------- | ----------------- | ------- |
| npm | `2027.0.0-rc.1` | dist-tag `next` |
| PyPI | `2027.0.0rc1` | pre-release, excluded from default installs |

`latest` never points at a pre-release. Old-line patches use their own tag
(`calver-2026` on npm). Published versions are immutable: we fix forward and
withdraw with `npm deprecate` or PyPI yank, only for a security hole, data loss,
or a break shipped as a MINOR or PATCH.

## Supported versions

| Line | Status | Fixes | Supported until |
| ---- | ------ | ----- | --------------- |
| 2027.x (1.0) | current | all | while current |
| 2026.3.x (last calendar line) | maintenance | security only | [date, proposed: 12 months after 2027.0.0] |
| older | unsupported | none | - |

The 2026.3.x backports ship as a PATCH on that line. Security advisories list
the patched version of every supported line.
Issues on unsupported lines are closed with a link to this table unless they
reproduce on a supported line.

Capacity check [fill in before publishing]:
monthly hours = ordinary releases + (security fixes per month on the old line ×
hours per backport). Example inputs: [last 12 months' security fixes] × [hours
per backport]. The result must fit inside the maintainers' monthly release hours.
If not, shorten the window.

## Deprecation

A deprecated API gets a runtime warning, a docs note and a changelog entry in
the MINOR that deprecates it. It is removed no earlier than the next MAJOR and
[six] months later.

## Known past breaks

Calendar versions did not promise compatibility. [List any month-to-month
break you know of, or "none known".]
````

## Deliverable 2: Migration announcement

Publish this one release ahead of 2027.0.0, as the skill's checklist requires. It goes in the changelog, the blog and the GitHub release. Update the date and support fields first.

````markdown
# Marrowline 1.0: a new version number, and what it means for you

**TL;DR:** Marrowline 1.0 ships on [launch date] as package version
**2027.0.0** on npm (`@marrowline/sdk`) and PyPI (`marrowline`). From then on we
follow Semantic Versioning. Nothing changes for you until you choose to upgrade.

## What changes

- Until now, versions were calendar-based (`2026.3.1`). The number said when we
  released, not whether something broke.
- From 2027.0.0, `MAJOR.MINOR.PATCH` means what SemVer says. We declare the
  covered surface in [RELEASES.md](RELEASES.md).
- "Marrowline 1.0" is the product name. The package version is 2027.0.0.
  Future majors count up from there: 2028.0.0 is Marrowline 2.0.

## Why 2027.0.0 and not 1.0.0

`1.0.0` is lower than `2026.3.1`. pip would never install it, and npm ranges
like `^2026.3.1` would never match it. Starting the SemVer major at 2027 keeps
every tool, including Debian's, sorting the new releases above the old ones.
We ran the ordering check on npm, PyPI and dpkg: [paste results].

## What you need to do

| You have | What happens | Action |
| -------- | ------------ | ------ |
| npm `^2026.3.1` | Stays on 2026.x. Never picks up 2027.0.0. | Change the range to `^2027.0.0` when you are ready. |
| PyPI `marrowline~=2026.3` | Stays on 2026.x. | Change to `marrowline~=2027.0` when ready. |
| PyPI `marrowline` unpinned | Moves to 2027.0.0 on next resolve. | Pin `<2027` first if you are not ready. |
| Exact pin | No change. | Read the [migration guide](link) before bumping. |
| Debian package | The packager will update it. | [Link to the packager thread.] |

Breaking changes in 2027.0.0 are listed in the [migration guide](link), ordered
by how many users each affects.

## Support for the calendar line

2026.3.x gets security fixes only, until [date]. After that it is unsupported.

## Update bots

Dependabot and Renovate read 2026 → 2027 as a major update and open a pull
request that needs a review. That is correct. From 2027.0.0, your minor and
patch automerge rules are safe: we only break in a MAJOR. The meaning of each
segment is in [RELEASES.md](RELEASES.md#version-numbers).

## Timeline

- [Today]: this announcement, with release 2026.x.y carrying the notice.
- [Date]: `2027.0.0-rc.1` on npm (`next`) and `2027.0.0rc1` on PyPI.
- [Launch date]: 2027.0.0 on both registries.
- [Date]: end of security fixes for 2026.3.x.

Questions: [issue link or discussion link].
````

## Dependabot and Renovate

1. **Major detection.** Dependabot reads the leading segments as major.minor.patch whatever the scheme. 2026.3.1 → 2027.0.0 is a major PR, which is right. Renovate can flag it as breaking and Dependabot cannot. State in the release notes that this is a real break.
2. **Old automerge rules were wrong.** Under CalVer, a month bump looked like a "minor", so dependents may have merged it unreviewed. After the switch, their minors and patches are safe only if yours never break. A break shipped in a minor reaches production by automerge. When in doubt, ship a major.
3. **Security PRs follow the advisory.** List 2026.3.x as a patched range in every advisory. Otherwise bots propose a jump to 2027.x instead of the backport.
4. **If you tag `1.0.0` on npm anyway:** dependents on `^2026.3.1` get no PR, ever. The bot sees nothing higher. For `1!1.0.0` on PyPI, I did not verify how Dependabot classifies an epoch, so check its docs before launch.
5. **Dependent cooldowns.** Their `semver-major-days` or `minimumReleaseAge` delays the 2027.0.0 PR on their side. That is expected.

## Open items and next action

You need to fill in:

- The covered and excluded surface.
- The runtime floors.
- The old-line window, with the capacity arithmetic.
- The dates.

I assumed everything else. Debian is the one surface the skill says to tell directly, before the release.

**Next, in order:**

1. Tell the Debian packager now. Ask which version stable carries and whether they need an epoch.
2. Confirm 2027.0.0 or the epoch route with product and marketing. Get the launch date moved only if you want the version released in 2027.
3. Run the ordering check: `python -c "from packaging.version import Version as V; print(V('2027.0.0')>V('2026.3.1'))"`, `npx semver -r '>2026.3.1' 2027.0.0`, `dpkg --compare-versions 2027.0.0 gt 2026.3.1`.

## If you choose 1.0.0 anyway

- PyPI publishes `1!1.0.0`, with a permanent epoch.
- The packager adds `1:`, and must do it before the release.
- npm publishes `1.0.0` with `--tag latest`. Every existing range is stranded, so the announcement must tell users to rewrite them.
- The "Why 2027.0.0" section and the mapping table go away.