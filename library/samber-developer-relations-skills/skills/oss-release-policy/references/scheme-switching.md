# Switching versioning schemes

Read this when SKILL.md step 2 picks a scheme different from the one the project ships today.

## The ordering rule

Every new version must sort above every old version in every tool that reads it. Check the first new version against the highest old version under each resolver the project publishes to (`npm semver`, Cargo, PEP 440, Go, dpkg).

| Move | Ordering | What to do |
|---|---|---|
| SemVer `1.x` → CalVer `26.x` | Preserved (26 > 1) | Jump. pip went from 10.0.1 to 18.0; NVIDIA GPU Operator from 1.11 to 22.9.0 |
| SemVer `0.x` → `1.0.0` | Preserved | Ship 1.0 with the policy in the same release |
| CalVer `2026.x` → SemVer `1.0` | Broken (1 < 2026) | PyPI: epoch `1!1.0.0`. Debian: packager adds `1:`. npm and Cargo: no epoch, so keep the major at or above the last year (`2027.0.0`, then SemVer from there) or publish under a new name. Go: CalVer never got past v1 |
| CalVer `YYYY` → `YY` | Broken (26 < 2026) | Same as above. Never shorten the year |
| Year-based → marketing major | Preserved only if the new number is larger | Unity went from 2023 to 6000.0 internally so ordering held |
| SemVer major in Go | New import path regardless | Plan the `/vN` path; v1 users stay on v1 until they rewrite imports |

## What changes for dependents even when ordering holds

- **Range meaning.** A dependent's `~=22.0` or `^1.4` keeps working, but the guarantee behind it changes. State what each existing range now buys.
- **Bot rules.** Type-based automerge rules flip meaning. A CalVer month becomes a "minor" that bots merge unreviewed. Say so in the announcement.
- **Badges, docs and the changelog header** still describe the old scheme. Update them in the same release.
- **Downstream packagers** may need an epoch if a version ever sorts lower. Tell them before the release, not after.

## Announcement checklist

1. Publish the new scheme and the reason at least one release ahead. Node.js announced its move to one major a year, with every line becoming LTS, about a year before 27.0.0 shipped.
2. Put the new scheme and the policy link at the top of the changelog and in RELEASES.md.
3. Name the last version under the old scheme and its support end date.
4. State the ordering check you ran and its result.
5. Tell distro packagers and the main downstream dependents directly.

## Cases

| Project | Change | Stated reason |
|---|---|---|
| pip | 10.0.1 → 18.0, quarterly `YY.N` | Calendar releases plus a formal minimum 6-month deprecation |
| Black | `22.x` with a yearly stable style | Same output for a whole calendar year |
| Node.js | From 27 (2027): one major a year, the major matching the year, every line LTS | Odd releases saw little adoption; security releases across four or five active lines were unsustainable |
| Unity | 2023 LTS → Unity 6 (`6000.0.x`) | Yearly naming confused users when releases slipped past the year |
| Apple OSes | 18 → 26 | One number across all platforms |
| CPython | Proposal to number minors by year, 3.YY (PEP 2026), rejected | The steering council judged breakage risk low but the benefit too small to justify the churn |

The rejected PEP is the counter-case: a more readable number is not, on its own, worth the churn of re-teaching every user and tool what the digits mean.
