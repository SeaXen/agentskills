**Do not push `v2.0.0` until `go.mod` says `module github.com/kestrelworks/tally/v2`.** Go rejects a `v2.x` tag on a module path with no `/v2`. This decision, and the calendar-version one below, cost you more than anything else in the plan.

## Two problems with the plan

1. **Calendar versions do not fit Go modules.**
   - `26.04` is not valid semver, and `v26.04.0` has a leading zero, so the Go tooling rejects it.
   - `v26.4.0` is valid, but major 26 forces the import path `.../tally/v26`. Every year-numbered major would then break all 900 importers' imports.
   - Ubuntu avoids this because it is not a Go module.
   - **Recommendation: stay on semver.** If you want the date visible, put it in release notes, not in the tag.
2. **An annual LTS is expensive at 6 hours a month.** For a library, Go's minimum version selection means users get the newest minor anyway, so a backport line rarely helps them. The policy below gives one optional, capped LTS line. Drop it if you prefer.

## Tags to push

Next Tuesday is 2026-10-27. Prep takes about 4 hours in total.

1. **Branch `release/v1` from tag `v1.14.3`** (about 1h).
   - Add `// Deprecated:` comments on the old exporter API, pointing to v2.
   - Add a README notice with the v2 date and the Go floor change.
   - Leave `go.mod` at `go 1.22`.
   - Push tag `v1.15.0`. This is the warning release the v1.12 complainers never got.
2. **On `main`, make it v2** (about 1.5h).
   - Set `module github.com/kestrelworks/tally/v2` and `go 1.24`.
   - Update every internal import, example and doc.
   - Run `go mod tidy`, `go build ./...` and `go test ./...`.
3. **Push `v2.0.0-rc.1` on Tuesday 2026-10-27.** Importers can test against it.
4. **Push `v2.0.0` at least 2 weeks after the rc**, about 2026-11-10, if no blocker is reported. Shipping it on 10-27 gives users no notice, which is what caused the last two complaints.
5. **Warm the proxy** after each tag: `GOPROXY=https://proxy.golang.org go list -m github.com/kestrelworks/tally/v2@v2.0.0`.

Do not push `v26.x`, `v2.0`, `v2.0.0.0`, or any `v2` tag before the `go.mod` change lands. Never move or delete a pushed tag. If a tag is bad, add a `retract` directive to `go.mod` and ship the next patch.

## Policy: version numbers

- Tags follow semantic versioning: `vMAJOR.MINOR.PATCH`. Calendar versions are not used. Go requires semver tags, and a new major version changes the import path.
- **MAJOR** covers any change that can break a user's build or behavior:
  - removed or changed exported API
  - changed defaults, such as the label separator
  - changed metric names or exporter output format
  - a raised minimum Go version
- **MINOR** adds backward-compatible API. It never changes a default or raises the Go floor.
- **PATCH** holds bug fixes only.
- A major release changes the module path suffix (`/v2`, `/v3`). The previous major lives on a `release/vN` branch.
- Before each major, the last minor of the old line ships deprecation notices. Every breaking change is announced at least 2 weeks before release, through an rc tag and release notes.
- Each major ships a migration guide listing every breaking change, with a before/after example.
- Pre-releases use `-rc.N`.
- Support:
  - The current major gets features and fixes.
  - The previous major gets security fixes only, for 6 months after the new major's GA.
- Optional LTS: the last minor of each major may be marked "LTS" and gets security fixes for 12 months. At most one LTS line exists at a time.

## Policy: runtime support

- The minimum Go version is the `go` line in `go.mod`. It changes only in a major release, never in a minor or patch.
- The minimum is announced in the release before it changes: the final minor of the old major plus the rc notes.
- CI tests the minimum Go version and the two newest Go releases.
- v2.0.0 requires Go 1.24 or newer. v1.x keeps its current floor, Go 1.22, until the v1 security window ends.
- When each major is planned, set its floor to the oldest Go release that upstream still supports. Go supports the two newest releases, so check go.dev/doc/devel/release. Go 1.24 may already be out of upstream support, so confirm before you raise or keep the floor.
- Do not set a `toolchain` line in `go.mod` that forces importers to download a newer toolchain.

**Next step (2 minutes):** run `git switch -c release/v1 v1.14.3` and start the deprecation comments.