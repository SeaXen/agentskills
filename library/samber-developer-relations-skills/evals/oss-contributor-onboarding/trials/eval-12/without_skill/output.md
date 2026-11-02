One fact first, not a question: there is no Ashgrove repo in this environment (checked `~/project/github.com/*` — only your `example-repo` repo exists there, and nothing named Ashgrove anywhere reachable). I'm not fabricating specifics from a codebase I can't see. Below is a complete onboarding plan built on standard Kotlin/JVM serialization-library practice (the kotlinx.serialization playbook, effectively), structured around your real constraint: **7 weeks to a 1.0 API freeze (2026-09-24 → 2026-11-14)**. Swap in your actual module names, CI vendor, and chat platform where marked `[confirm]`.

---

# Ashgrove Contributor Onboarding Plan

## 0. Operating principle for this specific window

You are 7 weeks from a version-number promise, not a feature promise. The plan below optimizes for one thing: **grow the contributor pool without growing review risk on the serialization core.** Two tracks, kept structurally separate:

- **Core track** (encoders/decoders, the compiler plugin or KSP codegen, binary format internals): maintainers only until 1.0 ships. New contributors don't touch this even if capable — a subtle encoding bug found in week 6 is a slipped release.
- **Edge track** (docs, examples, additional format modules, test coverage, tooling, error messages, benchmarks): open to first-time contributors starting now. This is where onboarding investment goes.

Every piece below is labeled Core or Edge so you can gate it in issue templates and labels.

## 1. Day-0 environment (write this as `CONTRIBUTING.md` → "Getting Started")

Prerequisites:
- JDK 17+ (Kotlin/JVM target minimum — confirm your actual `jvmToolchain` version) `[confirm]`
- Kotlin plugin bundled with IntelliJ IDEA (Community is sufficient)
- Gradle via the wrapper only — never a system-installed Gradle (`./gradlew`, not `gradle`)
- Git ≥ 2.30

Setup steps, in order:
1. Fork, then `git clone` the fork (not the upstream directly).
2. `./gradlew build` — first run pulls dependencies and runs the full check task; expect several minutes.
3. `./gradlew test` — confirms the local toolchain matches CI before any code is touched.
4. If multiplatform (JVM/JS/Native targets): `./gradlew allTests`, and flag in docs that Native targets need platform-specific toolchains (Xcode for macOS/iOS targets, etc.) — most contributors will only run JVM locally, which is fine for Edge-track work.
5. Import into IntelliJ as a Gradle project; apply the repo's `.editorconfig` (ship one if it doesn't exist).

## 2. Repo hygiene to add or verify before the first outside PR lands

Standard files a serialization library at 1.0 is expected to have — treat missing ones as blockers, not nice-to-haves, since a library used for data interchange gets scrutinized on exactly this kind of polish:

- `CONTRIBUTING.md` — this plan, condensed to the actionable subset.
- `CODE_OF_CONDUCT.md` — Contributor Covenant is the default; don't write your own.
- `GOVERNANCE.md` — who merges, how maintainers are added, how disputes resolve. Short, even 1 page.
- `SECURITY.md` — a serialization library is a common injection/DoS surface (unbounded recursion, decompression bombs on binary formats); state a private disclosure address and response-time target explicitly.
- `.github/ISSUE_TEMPLATE/` — separate templates for bug report, feature request, and "good first issue" proposal.
- `.github/PULL_REQUEST_TEMPLATE.md` — checklist: tests added, KDoc updated, binary-compat check run, changelog entry added.
- `CHANGELOG.md` in Keep-a-Changelog format, `Unreleased` section always present.

## 3. Coding standards and automated gates

Kotlin-specific tooling, not generic advice:

- **ktlint or detekt** (pick one, don't run both) wired into `./gradlew check` and CI. This is the gate that stops style bikeshedding in review.
- **Binary Compatibility Validator** (`kotlinx-binary-compatibility-validator` / the newer `binary-compatibility-validator` KMP plugin) — non-negotiable for a library approaching 1.0. It snapshots the public ABI into `api/*.api` files; any unintentional public-surface change fails CI. Turn this on **now**, in week 1, not after 1.0 — it's the single highest-leverage tool for a pre-1.0 API freeze because it converts "did this PR silently change the public API" from a manual review judgment call into an automated diff.
- **Explicit API mode** (`kotlin { explicitApi() }` in the Gradle build) if not already set — forces every public declaration to have an explicit visibility modifier and return type. Catches accidental public leaks from internal helpers, which is exactly the kind of thing an eager first-time contributor introduces without meaning to.
- **KDoc required on all public API** — enforce via detekt's `undocumented-public-class`/`undocumented-public-function` rules, not just convention. A serialization library's public API *is* the product; undocumented public surface is a defect, not a style nit.
- Commit and branch naming: Conventional Commits (`feat:`, `fix:`, `docs:`, etc.), imperative mood, scope in parentheses when it aids changelog generation (e.g. `fix(json): handle null default values in polymorphic decode`).

## 4. Testing bar

- Unit tests co-located per module, standard.
- **Round-trip property tests** are the load-bearing test class for a serialization library: generate arbitrary data classes (or use a property-testing library like Kotest's `Arb`), assert `decode(encode(x)) == x` for every supported type combination — nullable fields, default values, polymorphism, collections-of-collections, empty collections vs. null. This catches the bug class that hand-written example tests miss.
- **Golden-file tests** for wire format stability — encode a fixed set of fixtures, commit the expected output, fail if it silently changes. This is your real defense against an accidental breaking wire-format change slipping into 1.0.
- Multiplatform: any Edge-track PR touching shared code must pass `allTests`, not just `jvmTest` — CI enforces this, contributor doesn't need to run every target locally.
- New format module (if any land pre-1.0): requires the full round-trip + golden-file suite before merge, no exceptions — this is where "good first issue" energy is most useful and most safely contained.

## 5. PR and review workflow

- One reviewer minimum for Edge track, two for anything touching `core`/the format-agnostic encoding engine — enforce via `CODEOWNERS`, not verbal policy.
- State a review SLA in `CONTRIBUTING.md` (e.g. "maintainers aim to give first feedback within 3 business days") — first-time contributors abandon PRs mostly from silence, not from rejection.
- DCO (`Signed-off-by`, enforced via a bot check) over a full CLA — lower friction for a library that wants drive-by contributors, still gives provenance. Skip a CLA unless legal has a specific reason to require one.
- Label triage vocabulary: `good first issue`, `help wanted`, `core` (maintainer-only, block external PRs politely with a comment), `1.0-blocker`, `post-1.0`. Apply `core`/`1.0-blocker` retroactively to every open issue this week — it's the fastest way to make the Core/Edge split legible to outside contributors without them having to ask.

## 6. Communication and recognition

- GitHub Discussions for Q&A/design threads over a chat platform if you want the discussion indexed and linkable from docs — chat is better for real-time coordination but the content evaporates. Use both if you already run a Slack/Discord `[confirm]`, but treat Discussions as the durable record.
- `AUTHORS`/contributors section generated (e.g. `all-contributors` bot) rather than hand-maintained — hand-maintained lists rot and create the appearance of favoritism when someone's missed.
- Tag first-time contributors' merged PRs in the next release's changelog by name — costs nothing, is the single highest-retention action for turning a one-off PR into a second one.

## 7. 1.0-specific policy to publish now, not at the release

Publish an `API_STABILITY.md` (or a section in `CONTRIBUTING.md`) stating, before any external contributor can be surprised by it:

- What "1.0" commits you to: semantic versioning on the public API from that point forward, binary-compatibility validator as the enforcement mechanism.
- Deprecation policy: minimum one minor version with `@Deprecated` + `ReplaceWith` before removal.
- Any `@ExperimentalSerializationApi`-style opt-in annotation for surfaces you're intentionally *not* freezing at 1.0 — this is what lets you keep shipping fast in format-specific modules without violating the 1.0 promise on core.
- A migration guide stub (even a placeholder heading) for 0.x → 1.0, so contributors fixing pre-1.0 API rough edges know to log the breaking change there.

## 8. Seven-week rollout, week by week

| Week | Dates | Focus |
|---|---|---|
| 1 | Sep 24–30 | Land binary-compat validator, explicit API mode, `CODEOWNERS`, issue/PR templates, `CONTRIBUTING.md`, `SECURITY.md`. Retroactively label all open issues `core`/`edge`/`1.0-blocker`. Ship the API-stability doc even in draft form. |
| 2 | Oct 1–7 | Open Edge-track backlog as `good first issue`: docs gaps, missing KDoc, property-test coverage holes, error-message clarity. Aim for 8–12 labeled issues, not a flood — quality of first-issue framing matters more than volume. |
| 3 | Oct 8–14 | First external PRs land. Watch review SLA closely this week — a slow first response to your first contributors sets the tone for the rest of the program. |
| 4 | Oct 15–21 | Mid-point check: is `core` actually staying maintainer-only in practice, or has scope crept? Re-tag anything misclassified. Start the 0.x → 1.0 migration guide for real. |
| 5 | Oct 22–28 | API freeze soft-starts: any new public-surface PR needs explicit maintainer sign-off, binary-compat diff reviewed by hand even though the tool passed. |
| 6 | Oct 29–Nov 4 | Hard freeze on `core` public API. Edge-track and doc contributions continue normally. Changelog assembly begins. |
| 7 | Nov 5–14 | Release-candidate stabilization only: no new features, bug-fix PRs reviewed same-day where possible. Publish the finished migration guide alongside the 1.0 tag. |

## 9. The one guardrail most onboarding pushes get wrong under deadline pressure

Recruiting contributors and hitting a hard date pull in opposite directions unless you actively separate them, which is the entire reason for the Core/Edge split above. The failure mode to watch for specifically: a well-meaning first-time contributor submits a genuinely good fix *inside* the core encoding path in week 5 or 6. Accepting it under time pressure — because it's correct and you don't want to discourage them — is how pre-1.0 libraries ship a last-minute regression that a rushed review missed. Decline politely, redirect to `post-1.0`, and say so explicitly in `CONTRIBUTING.md` now so it reads as policy, not personal rejection, when it happens.