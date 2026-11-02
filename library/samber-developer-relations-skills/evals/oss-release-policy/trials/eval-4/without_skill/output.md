# Marrowline 1.0: announcement, versioning section, Dependabot notes

## ⚠️ Decide this before marketing locks the date

Going from `2026.3.1` to `1.0.0` is a version **downgrade** to every package manager. Both registries order versions numerically, and 1 is less than 2026.

| | PyPI (`marrowline`) | npm (`@marrowline/sdk`) |
|---|---|---|
| Plain `1.0.0` | Sorts below `2026.3.1`. `pip install -U` sees no upgrade and resolvers keep preferring the calendar releases. | New installs get it, because `latest` is a tag, not a max. Existing `^2026.3.1` and `>=2026.3.1` ranges never match it. |
| Fix | **Epoch**: publish `1!1.0.0`. Epochs outrank everything, so `1!1.0.0 > 2026.3.1`. | None. npm has no epoch. |
| Cost | The version prints as `1!1.0.0`. The epoch is permanent. Debian needs `1:` too (see below). | Existing users must edit their ranges by hand. |

Nothing can be republished or reused on either registry, so a wrong first upload is permanent.

**Recommendation, in order:**

1. **Cleanest option:** keep the "Marrowline 1.0" brand, but ship the first semver release as `2027.0.0`. Then:
   - Ordering works on both registries.
   - Debian needs no epoch.
   - Dependabot treats it as a normal major.
   - The cost is an odd-looking major number, with semver after that.
2. **If the number must be 1.0.0** (my assumption below): use `1!1.0.0` on PyPI. On npm, publish `1.0.0` with the `latest` tag, then run `npm deprecate "@marrowline/sdk@>=2026.0.0 <1.0.0" "Superseded by 1.0.0 (versioning moved from calendar to semver). Update your range to ^1.0.0."`. This is the only way to nudge npm users already on the old line.

Rehearse both on TestPyPI and a scratch npm scope first:

```bash
python -c "from packaging.version import Version as V; print(V('1!1.0.0') > V('2026.3.1'))"   # True
npx semver -r '^2026.3.1' 1.0.0                                                                  # prints nothing = no match
```

## Debian

- The Debian maintainer must add an epoch (`1:1.0.0-1`) when packaging the `1!1.0.0` upstream.
- Without it, apt considers `2026.3.1` newer and never upgrades. Debian epochs can never be removed.
- Tell the maintainer now, before the release date.
- Stable Debian users stay on 2026.3.1 until their distro picks it up. Say so in the announcement.

## Migration announcement (draft)

> # Marrowline 1.0
>
> **[Launch date]**: Marrowline SDK 1.0 is out on npm and PyPI. It is the same SDK, now with a stable API and semantic versioning.
>
> ## What changed
>
> - **Versioning.** We left calendar versions (`2026.3.1`) for [semver](https://semver.org). From now on, breaking changes only land in major releases.
> - **Stable API.** Everything documented in the reference is public API and covered by semver. [Link to the list of breaking changes, or "No API changes beyond versioning."]
>
> ## Why the version looks lower
>
> `1.0.0` is numerically lower than `2026.3.1`, so package managers will **not** upgrade you automatically.
>
> ## How to upgrade
>
> **npm**
> ```bash
> npm install @marrowline/sdk@^1.0.0
> ```
> Update any pinned range such as `^2026.3.1` in `package.json`. Automated update tools will not propose this change.
>
> **Python (pip)**
> ```bash
> pip install -U marrowline
> ```
> The PyPI version is `1!1.0.0`. The `1!` is a PEP 440 epoch that keeps it ordered above the calendar releases. It is the same 1.0.0 release. Pins like `marrowline==2026.3.1` or upper bounds like `<2027` must be changed by hand.
>
> **Debian**
> `apt` will offer 1.0 once the Debian package is updated, which is on the maintainers' schedule. Until then you have 2026.3.1.
>
> ## Support for the calendar line
>
> `2026.3.1` is the final calendar release. It receives security fixes until **[date]**, then it is end of life.
>
> ## Checking your version
>
> Code that parses the version string must accept `1!1.0.0` in Python. `importlib.metadata.version("marrowline")` returns it with the epoch.
>
> Questions or problems: [issues link].

## Versioning section (for README or docs)

> ## Versioning
>
> Marrowline follows [Semantic Versioning 2.0.0](https://semver.org) from 1.0.0 on. Earlier releases (2023 to 2026.3.1) used calendar versions.
>
> - **Patch** (1.0.x): bug fixes only.
> - **Minor** (1.x.0): backwards-compatible features. Deprecations are announced here.
> - **Major** (x.0.0): breaking changes, with a migration guide.
>
> **Public API:** everything in the published reference docs. Internals, undocumented modules, and anything prefixed `_` or under `internal/` can change in any release.
>
> **Deprecation policy** *(confirm these numbers)*: a deprecated feature stays for at least one minor release and 6 months before removal in the next major. It emits a runtime warning.
>
> **Same version on both registries.** npm and PyPI always ship the same version number. The one difference is that PyPI shows it as `1!X.Y.Z`. The `1!` is an epoch, because the project moved from calendar versions and PyPI orders by number. It is not part of the semver version.
>
> **Pre-releases:** `X.Y.Z-rc.1` on npm and `X.Y.ZrcN` on PyPI, published under the `next` dist-tag and never as `latest`.
>
> **Old-line patches:** publish them with `npm publish --tag legacy`, never as `latest`.
>
> **Support:** the latest major gets all fixes. The previous major gets security fixes for [N] months after the next major ships.

## Dependabot and Renovate: what to watch

1. **npm: no PR will open.** Dependabot treats `1.0.0` as lower than the installed `2026.x`, so it proposes nothing. Your own dependents get no signal except the deprecation warning, which is why the `npm deprecate` step matters. Bump your internal consumers by hand.
2. **PyPI: verify epoch parsing first.** I believe Dependabot's Python handling understands PEP 440 epochs, but I haven't confirmed it. Test in a scratch repo against TestPyPI before launch. If it fails, you get either no PR or a malformed one.
3. **Upper bounds block the upgrade.** `<2027`, `~=2026.3`, and `^2026.x` all exclude the new version. Dependabot will not rewrite them, so grep your own repos for those patterns.
4. **Update type will say "major".** Expect `semver-major` PRs and fix any `ignore` or grouping rules that assume minor or patch. From 1.0 on, `semver-minor` and `semver-patch` groups behave normally.
5. **Release notes.** Dependabot pulls the changelog from GitHub Releases. Create a release tagged `v1.0.0` and mark it "latest" explicitly. Use the same tag for both registries.
6. **Never publish a calendar patch as `latest` again.** A late `2026.3.2` on npm would take `latest` back from 1.0.0. Use `--tag legacy`.
7. **Renovate** behaves like Dependabot here. It will not pick a lower version, and it needs manual range edits.

Tell me which option you pick (`2027.0.0`, or `1!1.0.0` plus npm `1.0.0`). I'll then adjust the announcement text and fill in the dates and EOL policy.