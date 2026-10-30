# Ecosystem tooling: resolvers, pre-release grammar, update bots

Read this before writing the pre-release and channel rule (SKILL.md step 4) and before recommending any non-SemVer scheme. Tool behaviour changes between releases, so cite the tool's current docs to the user rather than this file when a decision hinges on one detail.

## Range matching and 0.x

| Ecosystem | Default range | 0.x behaviour | Pre-releases in ranges |
|---|---|---|---|
| npm | caret `^1.2.3` = `<2.0.0`; tilde `~1.2.3` = `<1.3.0` | `^0.2.3` = `<0.3.0`; `^0.0.3` = `<0.0.4` | Only when a comparator with the same `x.y.z` carries a pre-release tag |
| Cargo | caret by default | Left-most non-zero digit is the breaking one; `0.0.z` always breaking | Must be requested explicitly |
| pip (PEP 440) | `~=X.Y` = `>=X.Y, ==X.*` | No special rule: `~=0.4` takes any `0.x` from 0.4 up | Excluded unless requested or the only match |
| Go | Minimal version selection, no ranges | v0 has no compatibility promise | `v1.2.0-rc.1` is selectable only when required explicitly |
| Maven | Exact versions; ranges rare | None | `alpha` to `snapshot` sort below the release; `sp` and unknown qualifiers (`-jre`) sort above it |

## Pre-release spelling per ecosystem

| Ecosystem | Release candidate | Note |
|---|---|---|
| SemVer (npm, Cargo, Go) | `1.0.0-rc.1` | Use dot-separated numeric suffixes so `rc.10` sorts after `rc.9` |
| npm channel | publish with a non-default dist-tag (`next`, `beta`, `v1-lts`) | Recent npm refuses a pre-release or lower-than-latest publish without `--tag`; older clients and some CI actions move `latest` silently |
| PyPI | `1.0.0rc1`, `1.0.0b2`, `1.0.0.dev3` | Normalized form, no hyphen |
| Maven | `1.0.0-RC1` or `1.0.0-rc-1` | Qualifier order alpha < beta < milestone < rc |
| Debian packaging | `1.0~rc1` | Packager's rewrite; upstream keeps its own spelling |
| Go | `v1.0.0-rc.1` | Never tag `v2.0.0-rc.1` without the `/v2` path |

SemVer precedence ignores build metadata (`+build.7`), npm strips it, crates.io refuses two versions differing only in it, and PyPI rejects local versions on upload. Never use it to tell two releases apart.

## Update bots

| Question | Dependabot | Renovate |
|---|---|---|
| How is major detected? | Parses each ecosystem's grammar, then its update types read the leading segments as major.minor.patch whatever the scheme | Per-ecosystem versioning module (`pep440`, `cargo`, `gomod`, `maven`, `deb`, `regex`...) |
| Is "breaking" separate from "major"? | No | Yes: `isBreaking` flags 0.x, pre-release and some Python minors |
| CalVer | A year rollover reads as major, a month as minor | Same by default; `regex` versioning or per-package rules fix it |
| Cooldown | Per update type (`semver-major-days`...) | `minimumReleaseAge` |
| Security fixes | `update-types` filters apply to version updates only | Separate vulnerability rules |

Consequences for the maintainer:

- Under SemVer, dependents automerge your minors and patches. A break shipped as a minor lands in production unreviewed.
- Under CalVer, dependents' type-based automerge is wrong by default. Publish what each segment means so they can write a per-package rule.
- Under 0.x, every minor is a manual review for dependents. Bumping the 0.x minor for a plain fix costs them review time.
- Security update pull requests target the patched versions the advisory lists. List the backport on every old line in the advisory's patched ranges, or bots propose a major jump instead.

## Immutability and withdrawal

| Registry | Republish same version? | Withdraw a bad release |
|---|---|---|
| npm | Never (even after unpublish) | `deprecate`, move `latest` back |
| PyPI | Never reuse a filename or version | `yank` |
| crates.io | Never | `yank` |
| Go proxy | Cached forever | `retract` directive in a new release |
| Maven Central | Never | Release a fixed version |

Withdrawal mechanics belong to the publishing pipeline. The policy only states the rule: published versions are immutable, and a bad release is fixed forward.
