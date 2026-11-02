I wrote the three sections you asked for. I couldn't read the hollowmere repo, and the skill's interview needs answers I didn't have, so I wrote against the assumptions and open questions below. I ran no tooling. The ordering check at the end is a SemVer comparison I did by hand.

## Recommendation (needs your pick)

The skill ranks schemes by who reads the number. These are Cargo libraries, so SemVer ranks above CalVer, because resolvers and update bots read the year as major and the month as minor. You asked for a date, and that is only safe if the policy makes the year the breaking digit. The sections below do that, so Cargo's caret and Dependabot or Renovate read the number correctly.

- **Recommended, and written below:** lockstep CalVer `YYYY.M.FIX`, with breaking changes only in the first release of a calendar year.
- **Alternative:** lockstep SemVer `1.3.0`. A break in any one crate then bumps the major of all four, which means duplicate crates in dependents' trees. It also declares 1.0 stability while you still have experimental APIs.

## Draft for RELEASES.md

````markdown
## Version numbers

We use Calendar Versioning with lockstep numbering: `YYYY.M.FIX`.
`hollowmere-core`, `hollowmere-derive`, `hollowmere-async` and `hollowmere-cli`
always carry the same number, so "which version are you on" has one answer.

- `YYYY` is the release year.
- `M` is the release month, unpadded: April is `4`, never `04`. Cargo and
  crates.io reject leading zeros and two-segment versions.
- `FIX` is `0` for the first release of a month. Later releases that month
  are fixes only: `2026.4.1`, `2026.4.2`.
- Tags are `v2026.4.0`, one per release, covering all four crates.
  Announcements may say "the April 2026 release".

The number says when. Compatibility is defined here:

- Releases in the same year are compatible. `hollowmere-core = "2026"` means
  `>=2026.0.0, <2027.0.0`, and Cargo's caret agrees.
- A new year may break. Breaking changes ship only in the first release of
  a calendar year.
- The one exception is a soundness or security fix that cannot be made
  compatible. It is labelled "breaking fix" in the changelog and the advisory.
- The month never signals a break. Update bots will read it as a minor, so
  it is safe to automerge, apart from the MSRV rule in Runtime support.

The four crates are only supported at the same version. `hollowmere-core`
pins `hollowmere-derive` with `=`, and `-async` and `-cli` pin
`hollowmere-core` with `=`. Every release publishes all four crates, even
unchanged ones. Bug reports quote one number: `cargo tree | grep hollowmere`
or `hollowmere --version`.

Before the lockstep scheme, the crates were `core` 0.14.x, `derive` 0.14.x,
`async` 0.6.x and `cli` 1.2.x. Requirements like `hollowmere-core = "0.14"`
never pick up a lockstep release, so dependents edit them once.

## What we consider breaking

Covered by this promise:

- **core:**
  - public items, signatures and trait impls, including auto traits
    (`Send`, `Sync`);
  - documented behaviour and default values;
  - error types and variants;
  - serialized formats;
  - Cargo feature names and the default feature set;
  - types from other crates that appear in our public API.
- **derive:**
  - macro names;
  - accepted `#[hollowmere(...)]` attributes and their meaning;
  - the traits the macros implement.
- **async:**
  - public items and signatures;
  - documented cancellation and ordering behaviour;
  - the supported executors.
- **cli:**
  - flags and subcommands;
  - exit codes;
  - the machine-readable output (`--json`);
  - config keys and environment variables.

Doubtful cases are settled by the Cargo book's SemVer compatibility chapter.
When unsure, we treat it as breaking and defer it to the next January.

Not covered:

- `#[doc(hidden)]` items and `__private` paths, including what derive
  expansions call into;
- compile-error text from derive;
- `Debug` output, `Display` text of errors, panic messages and log text;
- human-readable CLI output;
- performance characteristics;
- behaviour the docs call a bug;
- mixing versions of the four crates.

Opt-in unstable:

- **Library crates:** APIs behind a Cargo feature named `unstable-<name>`,
  never in `default` and never enabled by a stable feature. Each is marked in
  rustdoc. It may change or disappear in any monthly release, with a changelog
  entry, but never in a fix release.
- **CLI:** commands and flags under `hollowmere preview ...`.
- **Libraries that depend on us:** they must not enable an `unstable-*`
  feature for their own users. Cargo unifies features across the whole tree.

Deprecation: a deprecated API carries `#[deprecated(note = "use X")]`, is
announced in the changelog, and is removed no sooner than the first release
of a year that is at least six months and two releases after the deprecation.

## Runtime support

The minimum supported Rust version (MSRV) is **1.78** (stable, May 2024).
It is declared as `rust-version` in `[workspace.package]` and inherited by all
four crates, so they never disagree. The proc macro builds on the same toolchain.

- **When it can rise:** only in a month's `.0` release, never in a fix release.
- **Notice:** the release before the one that raises it announces the new value
  in its changelog.
- **How far:** the new MSRV is a stable release at least 6 months old on the
  day of the bump. That is about four releases behind current stable.
- **Compatibility:** an MSRV bump is not breaking. Cargo falls back to an
  older hollowmere only with the MSRV-aware resolver (resolver 3, the default
  for edition 2024 workspaces, or `incompatible-rust-versions = "fallback"`).
  Older toolchains fail on `cargo update`, so the changelog names the new
  MSRV in its first line.
- **Dependencies:** a dependency update that needs a newer compiler is an
  MSRV bump and follows the same rules. Otherwise we hold the dependency back.
- **Editions:** raising our edition requires an MSRV that supports it, and is
  announced the same way.
- **CI:** a job builds the workspace on exactly the declared MSRV and on stable.
  A failure blocks the release.
- **Other floors:** none declared (platforms, `no_std`).
````

## Check results

- **Ordering:** `2026.x.0` sorts above `1.2.x`, `0.14.x` and `0.6.x` under SemVer comparison, so no epoch trick is needed. Run `cargo publish --dry-run` to confirm.
- **First number:** `2026.04` is already past (today is 2026-10-23). A November release would be `2026.11.0`.
- **First lockstep release:** it may carry pending breaks, since no existing range crosses into it. Keep MSRV at 1.78 there so the renumbering is the only surprise. The January-only rule starts after it.
- **Capacity:** I did no arithmetic, because I don't have your hours per month.

## Decisions I need from you

1. CalVer with the January-only break rule, or lockstep SemVer `1.x`?
2. Do your adopters run distro `rustc` (for example Debian stable)? If so, tie the MSRV floor to that toolchain instead of "6 months old".
3. May MSRV rise mid-year (written above), or only in January?
4. Which APIs are experimental today? I used `unstable-*` features and `preview` commands as the marker.
5. How many maintainer hours per month for releases? It decides whether I can write the supported-versions and backport sections.

Still unwritten: pre-releases and channels, cadence, supported versions, backports, known past breaks, who can cut a release, and changes to this policy. Your history of MSRV bumps "whenever we feel like it" belongs under known past breaks.