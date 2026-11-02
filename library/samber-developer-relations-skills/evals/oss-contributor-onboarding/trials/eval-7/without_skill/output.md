## Verdict: broken for newcomers, works for contributors who read past the README

**The dependency you need most is invisible to the audience most likely to need it.**

A newcomer who clones the repo and follows the README top to bottom will run:

```
cmake -B build
cmake --build build
ctest
```

...without ever running `./tools/dev-setup.sh`, because the README never tells them to. That script only surfaces in CONTRIBUTING — a doc newcomers routinely skip, since it reads as "how to submit a PR," not "how to build the thing." You've split one required setup sequence across two documents that don't reference each other, and put the missing half in the doc fewer people open.

## Why this is likely a hard failure, not a rough edge

For a C++ geospatial indexer specifically, a `dev-setup.sh` step almost certainly does one or more of:

- Bootstraps a package manager (vcpkg/conan) or installs system libs (GDAL, PROJ, GEOS, Boost) that `find_package()` in your `CMakeLists.txt` depends on.
- Initializes git submodules.
- Generates code (protobuf/flatbuffers schemas, version headers) that source files `#include`.
- Sets environment variables (`VCPKG_ROOT`, toolchain file paths) that the `cmake -B build` configure step reads.

If any of that is true, skipping the script doesn't degrade the experience — it hard-fails at `cmake -B build` with a missing-package/missing-submodule error, before the newcomer even reaches `ctest`. C++ has no ambient package manager, so "the hard part" of onboarding for this kind of project *is* dependency setup — which is exactly the part you've made optional-looking.

I can't confirm this against the actual script or CMake output since I don't have the repo and can't execute anything here — but the structural problem (one required sequence, split across two uncross-referenced docs) is independently verifiable just from what you described, regardless of what the script turns out to do.

## Best case / worst case

- **Best case:** `dev-setup.sh` only does non-blocking things (installs a pre-commit hook, a linter) and `cmake`/`ctest` genuinely work standalone. If so, CONTRIBUTING is misleading contributors into an unnecessary step, but newcomers are fine.
- **Worst case (more likely given the project type):** newcomer's very first command sequence dies on a CMake configure error referencing a library they've never heard of, with no pointer back to the script that would have fixed it. First impression: broken repo, not a missing step. That's the impression that gets a project closed and not tried again.

You should know which of these is true — it's a five-minute check (read `dev-setup.sh`, or just try the README's three commands on a clean machine) — but the README/CONTRIBUTING split is a real defect either way.

## Score: 3/10

Not because the tooling is bad — `cmake` + `ctest` is a perfectly normal, idiomatic choice — but because the **one thing a setup doc exists to guarantee (a correct, ordered, complete path from clone to green tests) is the thing that's broken.** Points aren't lost for complexity; they're lost for an undocumented ordering dependency between two files that never acknowledge each other.

## Fix (small, high-leverage)

1. Add the `./tools/dev-setup.sh` line to the README, immediately before `cmake -B build`, as step 1 of the same numbered sequence — not as a separate "see CONTRIBUTING" pointer, which people skip.
2. Make CONTRIBUTING say "run the Quickstart in README, then continue here for PR workflow" instead of restating a competing setup path — one canonical sequence, referenced, not duplicated.
3. If feasible, make the failure self-diagnosing: a `CMakeLists.txt` check that fails fast with `"GDAL not found — did you run ./tools/dev-setup.sh?"` turns a confusing error into a one-line fix, independent of whether anyone read the docs correctly.