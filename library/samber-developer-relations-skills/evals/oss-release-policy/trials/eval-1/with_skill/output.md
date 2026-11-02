# Release policy for `github.com/kestrelworks/tally`: version numbers, runtime support, and tags

The plan changes in two places. Stay on SemVer and make v2.0.0 a `/v2` module. Skip CalVer and the LTS for now.

## Decisions

**1. Calendar versions: no.** Go modules rule it out.
- Go accepts only SemVer. `26.04` is padded, so Go rejects it.
- `v26.4.0` would need a `/v26` import path, and a new path every year after that. Your ~900 importers would rewrite imports annually.
- If readability is the goal, put the release date in the changelog and in the supported-versions table. Humans get their date and resolvers get SemVer.

**2. v2.0.0: yes, with a `/v2` module path.**
- Go rejects a `v2.0.0` tag unless `go.mod` says `module github.com/kestrelworks/tally/v2`.
- v1 and v2 can coexist in one build. Importers move when they choose.

**3. Dropping Go 1.22: yes.** It costs v1 users nothing.
- v1 keeps its current `go` line, so nobody on 1.22 is forced off. They stay on v1.
- 1.22 is also past upstream support, which the Go rule allows.
- Your v1.12 complaint was a floor drop with no warning. The fix is the announcement rule in the runtime section below.

**4. Ubuntu-style yearly LTS: not at launch.** The skill ranks a designated multi-year LTS last for effort ("a team"). Check it against your 6 hours a month.

| Item | Hours/month | Basis |
|---|---|---|
| Ordinary releases | ~2.0 | **assumed**, not measured |
| v1 security-only backports | ~0.5 | **assumed** 3 fixes/year × 2 h ÷ 12 |
| **Total** | **~2.5 of 6** | |

- On those guesses an LTS line might fit, but nothing is measured.
- The v2 migration will eat support time through the first months.
- Decide at v2.0.0 plus 6 months, using real fix counts from the changelog.
- Promote an LTS only if change-controlled companies are among the importers and someone staffs the backports.
- If you do it later, designate one v2 minor per year and keep a `release-v2.N` branch. Don't encode it in the number.

## Section: Version numbers

```markdown
## Version numbers

We use Semantic Versioning 2.0.0 (`vMAJOR.MINOR.PATCH`), as Go modules require.

- MAJOR: an incompatible change to the surface listed under "What we consider
  breaking".
- MINOR: backward-compatible additions and new deprecations.
- PATCH: backward-compatible fixes.

From v2, the major version is part of the import path:
`github.com/kestrelworks/tally/v2`. A new major is a new package. v1 and v2 can
be imported side by side, and moving from one to the other means rewriting
imports. We batch breaking changes into rare majors.

We do not use calendar versions. Go modules cannot carry them past v1 without a
new import path every year. Release dates are listed in the changelog and in the
supported-versions table.

Release candidates are tagged `vX.Y.Z-rc.N` (numbered, so `rc.10` sorts after
`rc.9`). We do not use build metadata (`+...`) to tell releases apart.

Published tags are immutable: the Go proxy caches them forever. We fix a bad
release forward with a new patch version, and add a `retract` directive to
`go.mod` when a version must not be used.
```

## Section: Runtime support

```markdown
## Runtime support

The minimum Go version is the `go` directive in `go.mod`. Raising it forces every
dependent onto a newer toolchain or a failed build, so it is part of our
compatibility promise.

| Line | Minimum Go |
| ---- | ---------- |
| v2.x | Go 1.23 (`go 1.23.0`) |
| v1.x | unchanged from v1.14.3 |

Rules:

- We never raise the minimum in a patch release.
- Raising it above the oldest Go release the Go project still supports is a
  breaking change and ships only in a new major.
- Dropping a Go release the Go project no longer supports may ship in a minor. We
  announce it in the changelog and in this file at least one minor release and
  four weeks before it ships.
- Raising a dependency's `go` directive in a way that raises ours counts as
  raising ours.
- CI tests the minimum and the two newest Go releases.
- The v1 line keeps its minimum for its whole supported life.
```

The v2.0.0 floor is Go 1.23, which is what you asked for: drop 1.22 only.
- If you meant 1.24, change that one line and the table. The rules stay the same.
- **Verify before publishing.** I believe Go's two supported releases are now 1.26 and 1.27, which makes 1.23 through 1.25 unsupported upstream. Check go.dev/doc/devel/release.
- Expect a v2 minor to raise the floor soon. The announcement rule covers it.

## Tags to push

Run these in order.

1. **Create and push the v1 backport branch**, before v2 lands on `main`:
   ```
   git branch release-v1 v1.14.3
   git push origin release-v1
   ```
   v1 security patches go here as `v1.14.4` and later.

2. **Prepare the v2 commit on `main`** (this is code, not a tag):
   - Set `go.mod` to `module github.com/kestrelworks/tally/v2` and `go 1.23.0`.
   - Rewrite every internal import to `/v2`.
   - Run `go mod tidy && go build ./... && go test ./...`.
   - Confirm `grep '^module' go.mod` shows `/v2`.

3. **Push the release candidate** today or Monday. It serves as the "one release ahead" notice:
   ```
   git tag -a v2.0.0-rc.1 -m "v2.0.0-rc.1"
   git push origin v2.0.0-rc.1
   ```
   Fixes go in `v2.0.0-rc.2`, never a re-tag.

4. **Push the release** on Tuesday. I read "next Tuesday" as 2026-10-27. After CI is green on the same commit as the last rc:
   ```
   git tag -a v2.0.0 -m "v2.0.0"
   git push origin v2.0.0
   ```
   Then confirm the proxy sees it:
   ```
   GOPROXY=https://proxy.golang.org go list -m github.com/kestrelworks/tally/v2@v2.0.0
   ```

**Never push:**
- `v2.0.0` before `go.mod` carries `/v2`. Go will reject it.
- `v1.15.0` for the exporter rewrite. That is a break and needs the major.
- Any `26.x`, `v26.x` or `v26.04.0` tag.
- A moved or deleted tag. If `v2.0.0` is wrong, ship `v2.0.1` and `retract` the bad one.

## Supporting rows for RELEASES.md

Not requested, but the v1 window must exist before you tag.

| Line | Status | Fixes | Supported until |
| ---- | ------ | ----- | --------------- |
| v2.x | current | all | while current |
| v1.x | maintenance | security only | 2027-10-27 (12 months after v2.0.0) |
| older | unsupported | none | - |

- List the patched version on `release-v1` in each security advisory, so update bots offer the backport instead of a jump to v2.
- Put the two past breaks under **Known past breaks**: v1.12 dropped Go 1.20 in a minor, and v1.13 changed the default label separator. Both stay, because reverting would break users who already upgraded.
- Put the default label separator and the default values in the "covered" list of the breaking-changes section, since v1.13 broke callers without a signature change.

## Questions that could change this

1. **Real numbers:** how many fixes shipped in the last 12 months, and how many hours do ordinary releases take now? My 2.5-hour total is a guess. It affects the 12-month v1 window and the LTS call.
2. **Do your importers run distro Go?** Ubuntu 24.04 packages Go 1.22. If many adopters use distro toolchains, the floor should follow the distro's end-of-life, not upstream's.
3. **Who publishes?** The template needs "Who can cut a release". Do both maintainers hold publish rights?
4. **Exclusions:** I haven't seen your API. The exclusion list needs at least one entry. Candidates are `internal/`, error message text and ordering of unordered aggregation output.

Nothing here was run or checked against your repository. The numbers and the Go release status come from the skill's rules and my assumptions, not from your changelog or `go.mod`.