# Quillforge versioning and deprecation: policy sections, plus what to tell users

Part 1 is ready to paste into the docs. Part 2 is the pip and update-bot guidance. Part 3 lists the decisions I made for you and what to check before publishing.

---

## Part 1: Docs sections

### Versioning

Quillforge uses calendar versioning: `YY.M.P`.

- `YY` is the two-digit year of the release. `M` is the month of the release, without a leading zero. `P` is the patch number, starting at 0.
- Examples: `26.3.0` is a feature release tagged in March 2026, and `26.3.1` is its first patch.
- The tag assigns the number. A release that slips from December into January is `27.1.0`, never a late `26.12.0`.
- Pre-releases follow PEP 440: `26.11.0rc1`, `26.11.0.dev0`.
- The last SemVer series is `7.x`. Every calendar version sorts above it, so `pip install -U` needs no epoch.

**What a version number tells you**

| Release | Cadence | May contain |
| --- | --- | --- |
| Feature release (`YY.M.0`) | Three per year | New features, new deprecations, and removal of APIs whose deprecation period has ended |
| Patch release (`YY.M.P`, P ≥ 1) | As needed | Bug and security fixes only. Never deprecations or removals. |

- The year does not signal a break. Any feature release can remove things, and only the deprecation policy below limits what it removes.
- Nothing is removed without a prior warning, except under "Exceptions".
- Upgrading from a release that is warning-clean to the next feature release is safe. You can skip releases, but then the warning guarantee no longer covers you (see "Upgrade one release at a time").

**What the policy covers**

- Covered: names without a leading underscore in modules that appear in the API reference, documented settings, documented CLI commands and flags, and documented entry-point groups.
- Not covered: anything underscore-prefixed, anything in `quillforge.internal.*` or `quillforge.contrib.*.tests`, undocumented behaviour, and exact warning or error message text.
- Third-party code that reaches into uncovered parts can break in any release.

**Supported releases**

- The two most recent feature releases receive patch releases. Older releases get none, including security fixes.
- `7.14` receives security fixes only, until `<DATE: decide, suggest 12 months after the first calendar release>`.

**Exceptions**

A release may change covered behaviour without the full deprecation period only for:

1. A security vulnerability that cannot be fixed compatibly.
2. A behaviour that contradicts the documentation, where the documented behaviour is restored.

Each exception goes under "Behaviour changes" in the release notes, with the migration step. Exceptions never ship in a patch release unless they are the security fix itself.

**Upgrade one release at a time**

- Deprecations stay for at least two feature releases, so the most you can skip is one release (N to N+2) and still have seen a warning.
- If you skip further, read every release's "Removals" section between your version and the target.

### Deprecation policy

**Lifecycle**

1. **Deprecate in release N.** Emit the warning, document the replacement, and add a `deprecation` entry to the release notes.
2. **Keep for two feature releases.** The API works unchanged and keeps warning in N+1 and N+2.
3. **Remove in N+3 at the earliest.** This is also the first release where it is allowed to be gone. The release notes carry a `removal` entry.

Concrete example, with three releases a year:

- Deprecated in `26.3.0`.
- Still present, still warning, in `26.7.0` and `26.11.0`.
- Eligible for removal in `27.3.0`.

**Minimum time floor**

- At least 6 months must pass between the deprecating release and the removing release. This protects users if the release cadence ever speeds up.
- Both conditions must hold: two full feature releases and 6 months.

**Warning rules**

- Use `quillforge.QuillforgeDeprecationWarning`, a subclass of `DeprecationWarning`. This lets users target Quillforge's warnings without muting or escalating everyone else's.
- Mark deprecated functions and classes with `typing_extensions.deprecated` (PEP 702, in `warnings.deprecated` on Python 3.13+). Type checkers and IDEs then flag them without running the code.
- Set `stacklevel` so the warning points at the caller's line, not at Quillforge.
- Every message states four things: what is deprecated, what replaces it, the release that deprecated it, and the earliest removal release. Example:

  ```
  quillforge.routing.add_route() is deprecated since 26.3.0 and may be removed
  in 27.3.0 or later. Use Router.add() instead.
  ```
- `DeprecationWarning` is hidden by default unless triggered directly from `__main__`. Quillforge therefore enables `QuillforgeDeprecationWarning` display in its dev server, test client, and test-runner plugin.
- Document one line for CI:

  ```
  python -W error::quillforge.QuillforgeDeprecationWarning -m pytest
  ```

**Process rules for maintainers**

- Every deprecation and removal needs a `newsfragments/<issue>.deprecation` or `.removal` file. Release notes are built from these.
- Keep a machine-readable registry, `deprecations.toml`, with one row per deprecated name: `since`, `removable_in`, `replacement`.
- A CI gate fails any PR that deletes a name which is not in the registry, or whose `removable_in` is later than the next release.
- Never remove in a patch release.
- Undeprecating is allowed. Add a release-note entry.

**Deprecation table (published with each release)**

| Name | Deprecated in | Earliest removal | Replacement |
| --- | --- | --- | --- |
| *(generated from `deprecations.toml`)* | | | |

**Transition from 7.x**

- Everything already deprecated in `7.x` keeps its existing clock. The first calendar release counts as the next release in that count.
- The 7.x deprecation list is published once, with removal releases converted to calendar numbers, in the announcement.

---

## Part 2: What to tell users about pip and update bots

### 1. Ranges that cap at 7 will silently stop

The most important message. These pins now freeze users on 7.14 with no warning and no error:

- `quillforge<8`, `quillforge>=7,<8`
- `quillforge~=7.14`, `quillforge==7.*`

Tell them to do this:

- **Applications:** use a lockfile with exact versions, and raise the pin by hand or via a bot PR.
- **Libraries and plugins:** declare a lower bound only, for example `quillforge>=26.3`. If you must cap, cap at the next year, for example `quillforge>=26.3,<28`.
- **Everyone:** run CI with the `-W error::quillforge.QuillforgeDeprecationWarning` line above, so removals are caught one release before they happen.

### 2. pip itself behaves normally

- `26.3.0` sorts above `7.14` under PEP 440, so `pip install -U quillforge` works for anyone with no cap.
- Do not yank any 7.x release.
- Never switch between two-digit and four-digit years (`26` vs `2026`). Going from `2026.x` back to `26.x` would sort lower and need an epoch.
- Pre-releases are installed only with `--pre` or an explicit pin.

### 3. Dependabot and Renovate will misclassify updates

Bots classify updates as major, minor, or patch from the version segments. This is my understanding, so test it as described in the checklist. With `YY.M.P`:

- `7.14` to `26.3.0`, and every January release after it (for example `26.11.0` to `27.1.0`), counts as **major**.
- Every other feature release counts as **minor**, even when it removes an API that was deprecated two releases ago.
- Patch releases count as **patch**.

Consequences to spell out:

- **Ignore rules for major updates.** A rule such as Dependabot's `ignore: update-types: ["version-update:semver-major"]` blocks the jump from 7 to 26 and all later January releases. Users with this rule must remove it, or add an exception for `quillforge`.
- **Auto-merge of minor and patch updates.** Minor no longer means "safe", so auto-merging minors can merge a removal. Only auto-merge when CI passes with Quillforge deprecation warnings as errors. Otherwise, require a human review for every feature release.
- **Grouped update PRs.** Pull `quillforge` out of "all minor and patch" groups, or at least review it separately.
- **Release notes.** Dependabot and Renovate quote the GitHub release body in their PRs. Publish "Deprecations" and "Removals" headings on every GitHub release so they appear in the PR.

### 4. Code that reads the version

Plugin authors must stop doing these:

- `quillforge.VERSION[0] == 7`, or any `major == N` test. Use `packaging.version.Version(quillforge.__version__)` for ordering.
- Branching on version for features. Use feature detection (`hasattr`, try/except `ImportError`) where possible.

### 5. Downstream packagers

conda-forge feedstocks, Linux distribution packages, and internal mirrors that pin `quillforge<8` need the same range change as in point 1. Note this in the announcement, and send it to the main packagers directly.

### 6. Announcement checklist

Publish before the first calendar release, in the blog post, the release notes, and the docs home page:

1. The new scheme and the first calendar version number.
2. The `<8` and `~=7` freeze warning, with the replacement ranges.
3. The bot guidance from point 3.
4. The 7.x support end date.
5. The one-line CI command for deprecation warnings.
6. The converted deprecation table for everything currently deprecated.

---

## Part 3: Decisions I made, and what to verify

**Decisions for you to confirm or change**

- `YY.M.P` follows Twisted. Month is honest because it is assigned at tag time. The alternative `YY.N.P` (release-of-the-year) hides the date but avoids month questions when releases slip. I chose the month form.
- I added a 6-month floor to the two-release rule. Drop it if you want to keep the policy exactly as it stands.
- I added a `QuillforgeDeprecationWarning` subclass. Your current process may use plain `DeprecationWarning`, and a subclass is still compatible with existing filters.
- Security fixes for 7.14 need a real end date. I left a placeholder.
- Support for the last two feature releases lets users upgrade one step at a time. A longer support promise is a bigger commitment, so decide it deliberately.

**Please verify before publishing**

- Create one test repo with Dependabot and one with Renovate, pinned to `quillforge==7.14`, and confirm how each labels `7.14` to `26.3.0` and `26.3.0` to `26.7.0`. I'm confident about the general behaviour but did not test either bot.
- Check Twisted's current deprecation window if you cite it. I recall one year, but didn't confirm it.
- Run the CI gate against a past release to check that the `deprecations.toml` registry can be back-filled for all 2,000 modules. That backfill is the largest piece of work in this plan.