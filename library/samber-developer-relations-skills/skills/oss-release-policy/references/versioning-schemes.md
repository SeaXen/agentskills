# Versioning schemes catalog

One entry per scheme in real use. Each entry gives the promise the number makes, where it fits, who uses it, what tools do with it, and how hard it is to leave. Read the entry for every scheme still on the table after SKILL.md step 2.

Contents: SemVer · SemVer 0.x · ZeroVer · CalVer (six shapes) · Go semantic import versioning · PEP 440 · Debian and RPM · Maven qualifiers · Build and serial numbers · Two-number apps · Asymptotic · Editions · Marketing versions · Rolling releases

## SemVer 2.0.0 (`MAJOR.MINOR.PATCH`)

- **Promise:** MAJOR on any incompatible change to the declared public API, MINOR for additions and new deprecations, PATCH for compatible fixes. The spec opens with "MUST declare a public API": the promise covers only what that declaration lists.
- **Fits:** libraries, SDKs, plugins and anything a package manager resolves through ranges.
- **Users:** the npm and Cargo ecosystems by convention, Go modules by force.
- **Tooling:** every resolver and update bot assumes it. Dependents' automerge rules for minors and patches are only safe if your minors and patches truly never break.
- **Leaving it:** easy upward. A CalVer number like `26.1.0` sorts above any `x.y.z` below 26.
- **Critique:** Hynek Schlawack calls it "a TL;DR of the changelog" and tells consumers to treat every update as potentially breaking. Its value scales with how precisely the public API is defined.

## SemVer 0.x (`0.MINOR.PATCH`)

- **Promise per spec:** none at all. "Anything MAY change at any time."
- **Promise per resolver:** npm caret and Cargo treat the left-most non-zero digit as the breaking digit. `^0.4.2` never takes `0.5.0`, and `0.0.z` releases are always breaking.
- **Fits:** a project whose surface is still moving and whose users accept that.
- **Rule to publish:** "0.MINOR is our breaking digit, 0.x.PATCH is a compatible fix". Writing this down turns 0.x into a usable scheme, because it matches what resolvers already do.
- **Exit:** the SemVer FAQ says software already used in production should probably be 1.0.0. See SKILL.md step 2 for the 1.0 criteria.

## ZeroVer

0ver.org's satire of projects that stay in 0.x for years while being depended on in production. It carries no promise, and some practitioners advise against depending on such libraries at all. Apache Kafka, which left 0.x for 1.0 in 2017, is the best-known graduate. It is never a scheme to recommend. Treat it as the failure state of an undeclared 0.x.

## CalVer

calver.org: CalVer "deliberately does not attempt to communicate breaking changes". Pair every CalVer shape with a written, time-based compatibility or deprecation policy, or the number is only a date stamp. Use unpadded segments (`26.4.0`, not `26.04.0`): padded segments are invalid SemVer, Cargo and Go reject them, and npm and PEP 440 strip the zeros, so the git tag and the published version disagree.

| Shape | Promise once paired with a policy | Fits | Users |
|---|---|---|---|
| `YY.N` / `YY.N.MICRO` | N-th release of the year; fixes on MICRO | Tools on a fixed calendar | pip (quarterly, N = quarter 0-3), packaging |
| `YY.M` / `YY.0M` | Release month; support length readable from the number | Distributions, suites | Ubuntu (`26.04` LTS), LibreOffice |
| `YY.M.MICRO` | Same-year stability | Formatters, frameworks with time-based deprecation | Black (same output across a calendar year), Twisted, pyOpenSSL |
| `YYYY.MINOR.MICRO` | Year plus counter | IDEs, end-user apps | JetBrains, Home Assistant (`YYYY.M.MICRO`) |
| `YYYY.0M.0D` | Snapshot date of the data | Data bundles | certifi, yt-dlp (padded tags, unpadded on PyPI: the drift above) |
| `YYYYx` | Year plus release letter | Data published a few times a year | IANA tz (`2026a`) |

- **Tooling:** bots read the year as major and the month as minor. A CalVer "minor" can run a database migration, and dependents' automerge rules misfire. A careful dependent encodes your written policy per package. A PEP 440 range `~=26.0` means "same calendar year", which fits Black's policy and promises nothing for pip.
- **Go:** unusable past v1, because every year would need a new `/vYYYY` import path.
- **Leaving it:** going back to `1.0` sorts below `2026.x`. Keep the major at or above the last year (`2027.0.0`, then SemVer from there), use an epoch where one exists (PEP 440, Debian), or publish under a new name.
- **Critique:** Jacob Tomlinson (Dask) notes CalVer does not make releases more regular and can imply semantics where none exist.

## Go semantic import versioning

- **Rule:** v2 and above require a `/vN` suffix on the module path. Each major is a distinct import path, so v1 and v2 can coexist in one build. A v2+ tag on a module without go.mod gets `+incompatible`.
- **Promise:** same as SemVer, enforced by the toolchain. Minimal version selection never picks a version nobody asked for.
- **Consequence:** a major bump is a new package. Users and bots must rewrite imports. The module proxy and checksum database cache every published tag: a deleted or moved tag never unpublishes. Withdraw with a `retract` directive.

## PEP 440 (Python)

- **Grammar:** `[N!]release[{a|b|rc}N][.postN][.devN][+local]`. The epoch defaults to 0. Pre-releases are excluded from ranges by default. `.postN` fixes packaging or docs only, never code. Local `+label` marks a compatible downstream rebuild, and PyPI rejects it on upload.
- **Normalization:** `1.0.0-beta.1` becomes `1.0.0b1`, and `2026.08.19` becomes `2026.8.19`. Write the policy in the normalized form, or tags and registry versions drift apart.
- **Promise:** ordering only. The compatibility promise comes from whichever scheme (SemVer or CalVer) you write inside the grammar.

## Debian and RPM (`[epoch:]upstream-revision`)

- The packager, not the upstream maintainer, owns these numbers. Debian's epoch exists "to leave behind mistakes in version numbering" and scheme changes, and policy says to use it sparingly.
- Tilde sorts before everything: `1.0~rc1 < 1.0`. An upstream tag `1.0-rc1` sorts after `1.0` in dpkg, so every distro rewrites it.
- Upstream duty: never reuse or decrease a version, and keep pre-release labels parseable so packagers can map them.

## Maven qualifiers

- Order: `alpha < beta < milestone < rc = cr < snapshot < (release) = final = ga < sp`. Unknown qualifiers sort after the known ones, so after the release.
- Maven 4 documentation encourages SemVer and discourages `CR`, `final`, `ga`, `release` and `SP`.
- Trap: flavour suffixes (Guava's `-jre`, `-android`) sort as qualifiers, not as variants.

## Build and serial numbers

- **Promise:** monotonic identity, nothing about compatibility. Chromium's `MAJOR.MINOR.BUILD.PATCH` uses BUILD.PATCH as the canonical code identity, and its major counts release trains.
- **Fits:** auto-updated applications, browsers, games, internal tooling with no programmatic dependents.

## Two-number apps

A marketing version (`4.2`) for humans plus a monotonic integer build number that app stores and auto-updaters require. Keep both in the policy and say which one a bug report must quote.

## Asymptotic

Knuth's TeX converges to π (`3.141592653`) and METAFONT to e. Each bug-fix release adds a digit. The promise is total stability. It fits finished software that will only ever receive fixes. A plain "feature-complete, fixes only" statement over SemVer buys the same promise without the joke.

## Editions

Rust ships breaking language changes as opt-in editions (2015, 2018, 2021, 2024). Crates on different editions interoperate, so the toolchain stays on 1.x and on a six-week train. This fits only a language or format that can compile old and new semantics side by side.

## Marketing versions

These are big round majors chosen for perception or platform alignment: Apple's OS 26, Unity 6 (internally `6000.0.x`). Never let a marketing number replace the technical one dependents resolve against. Publish the mapping when both exist.

## Rolling releases

There is no version promise. Snapshots are dated (Arch ISOs). This fits distributions and services consumed at head, never a library.
