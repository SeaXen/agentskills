# Slatecar contributor-setup audit

## Bottom line

**I can't verify this passes, and the two documents you gave me are themselves evidence that it probably doesn't — for reasons that don't require running anything to see.**

Per this skill's own cold-run protocol: *"If you cannot execute commands in your environment, say so plainly and ask the maintainer to run the sequence and paste the full output — including the failures. Do not mark [setup] passed by inspection."* I'm holding that line. What follows is what's provable from the text alone, separated from what genuinely needs a real run.

## What's provable without running anything

Your README gives a **self-contained, four-step sequence**:

```
git clone ...
cmake -B build
cmake --build build
ctest
```

Nothing in it references `./tools/dev-setup.sh`, CONTRIBUTING, or any prerequisite. Your CONTRIBUTING file says to run `./tools/dev-setup.sh` "first" — but doesn't restate the README's steps, doesn't say *first relative to what*, and doesn't fold into one canonical sequence.

That split is a defect on its own, independent of whether `cmake -B build` would actually fail. A newcomer who lands on the README — the default entry point on every forge — has zero textual signal that a setup script exists anywhere else. GitHub's own contributor-path guidance treats the README as the landing page and CONTRIBUTING as a second document a reader may never open before attempting to build. If your repo's real newcomer path is "README first, CONTRIBUTING only if something breaks," you've already lost the ordering that makes `dev-setup.sh` do anything.

Two Steinmacher et al. (2015) barrier categories apply directly:

- **Documentation** — the instructions exist, but are split across two files with no cross-reference and no single canonical sequence.
- **Technical hurdles** — for a C++ geospatial indexer, `./tools/dev-setup.sh` is almost certainly there to install the stack CMake's `find_package()` calls need cold — GDAL, GEOS, PROJ, maybe a vcpkg/conan bootstrap. None of that ships with a bare OS. Skip it, and `cmake -B build` doesn't degrade gracefully — it either fails at configure time with a `find_package(GDAL) — not found` style error, or worse, silently picks up a mismatched system GDAL and fails later at link time with an ABI error that means nothing to someone on their first PR.

There's a second, sharper risk hiding in the same gap: if `dev-setup.sh` bootstraps a package manager, it likely also produces a **toolchain file** (`vcpkg.cmake`, a conan-generated preset, etc.) that `cmake -B build` needs to be pointed at explicitly. Your README's command — bare `cmake -B build`, no `-DCMAKE_TOOLCHAIN_FILE=...`, no `--preset` — doesn't show that flag. So even a contributor who dutifully runs the setup script first may still hit a wall the README's literal command doesn't clear. I can't confirm this without seeing the script, but it's the single most common failure shape for exactly this pairing (manual `cmake -B build` next to a package-manager bootstrap script) in C++ projects with heavy native deps, and it costs nothing to check.

## What I can't tell you without a real run

- Whether `cmake -B build` fails outright with no deps installed, or partially succeeds against stale/system-provided GDAL/GEOS/PROJ and fails later.
- Whether `dev-setup.sh` itself invokes `cmake`/`ctest` internally (in which case the README's steps may be redundant, or worse, write to a conflicting build directory).
- Wall-clock time to first passing test — not stated anywhere, and the protocol requires recording it.
- Any platform assumption (Linux-only apt packages inside `dev-setup.sh`, Homebrew-only paths, etc.) — none of interview question 11's territory (database, API key, GPU, proprietary SDK) is visible from what you gave me.

To actually close this out, the fastest thing that moves it from "diagnosed" to "confirmed": have someone run the sequence on a genuinely clean machine or fresh container — not a maintainer's laptop with GDAL already on it from six other projects — and paste the full output, failures included. Short of that, pasting `tools/dev-setup.sh` itself would let me confirm or rule out the toolchain-file gap above without needing execution at all.

## Score

Scoped to the setup dimension only — I wasn't given issue-queue, CI, or response-time data, so I'm not fabricating scores for B1/B3/B4 or the review-loop checks. A full audit needs `scripts/contributor-path-audit.sh` and the last 10 external PRs, which I don't have.

**Blocking checks**

| Check | Result | Evidence |
|---|---|---|
| B2 — documented setup runs cold | **FAIL** | README's own 4-step sequence, read alone, never mentions `tools/dev-setup.sh`; CONTRIBUTING's step isn't integrated into a single sequence. That's an undocumented step for a README-only reader by definition, before any question of whether `cmake` itself errors out. Runtime outcome unconfirmed — needs a real cold run per the caveat above. |
| B1 — contribution is invited | Not evaluated | You didn't tell me what CONTRIBUTING says beyond the setup line — can't confirm it states accepted contribution types. |
| B3 — work available | Not evaluated | No issue-queue data given. |
| B4 — submissions get answered | Not evaluated | No response-time data given. |

**Relevant scored checks**

| Check | Score | Evidence |
|---|---|---|
| S2 — prerequisites pinned | **0/2** | Nothing in what you gave me pins toolchain/library versions — a bare `cmake -B build` with no toolchain file reference reads as prose-level instruction, not a pinned lockfile or container definition. Confirm or refute by showing me `dev-setup.sh`. |
| S3 — local gates match CI | Not evaluated | No CI config given. |

Everything else (S1, S4–S8) needs data outside this conversation.

## Fix, in order of damage removed per hour

1. **Collapse to one canonical sequence, stated once.** Put the real order — clone → `./tools/dev-setup.sh` → `cmake -B build [+ any toolchain flag it produces]` → `cmake --build build` → `ctest` — in the README, since that's what gets read first. Link CONTRIBUTING for policy (scope, review, legal gate), not for the steps themselves. This is a same-afternoon fix and it's the one that actually unblocks B2.
2. **Run it cold once, for real,** on a container or VM that has never touched this project, before claiming the fix worked. Paste me the output if you want it re-scored — that's the only way B2 moves off "unverified."
3. **Pin the toolchain** (S2) — a `CMakePresets.json` or a version file your package manager reads beats prose every time a contributor's local GDAL is a point release off from what you built against.

This isn't a wording problem. A setup that silently breaks on a clean machine produces no issue, no message, and no trace — it just produces someone who tried once and never came back, and you'd have no way to know that happened.