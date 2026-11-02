# brinepool release policy

Using `oss-release-policy`. I skipped the scheme-switching reference because you said this only documents the current scheme.

Four inputs I couldn't see are marked **[confirm]**. Your five hours a month decided the support table: it allows one security-only line at a time.

## RELEASES.md

```markdown
# Release policy

## Version numbers

brinepool uses Semantic Versioning (`MAJOR.MINOR.PATCH`) and is in the 0.x series.
There is no plan for 1.0 and no date for one.

Until 1.0, **0.MINOR is the breaking digit** and 0.MINOR.PATCH is a compatible fix.
A change that can break existing callers ships as a new 0.MINOR, never as a patch.
Patch releases contain bug fixes and security fixes only.

Pin accordingly:

- `gem "brinepool", "~> 0.31.0"` takes patches of 0.31 only. We recommend this.
- `gem "brinepool", "~> 0.31"` means `>= 0.31, < 1.0`. It accepts every future
  0.MINOR, breaking ones included.

## What we consider breaking

Covered by this promise [confirm each item against the public API]:

- Public classes, modules and methods, and their documented signatures and behavior.
- Configuration option names and **their default values**. Changing a default
  callers rely on is a breaking change, even when no signature changes.
- Error classes raised and their hierarchy.
- Request-signing behavior and the S3-compatible operations we document.
- The `required_ruby_version` declared in the gemspec.

Not covered:

- Anything undocumented or marked `@api private`, and private or protected methods.
- Log and error message text.
- The order of unordered collections.
- Behavior the documentation calls a bug.

Opt-in unstable: none.

Defaults that change request volume, such as retry count, get a "Changed defaults"
entry at the top of the changelog entry for that release.

## Runtime support

brinepool supports Ruby 3.1 and later, declared in `required_ruby_version` in the
gemspec. RubyGems and Bundler use that field to fall back to the last compatible
release on older Rubies.

- We raise the floor only in a 0.MINOR release, announced in the changelog one release earlier.
- We never raise the floor past a Ruby version that upstream still supports.
- Ruby 3.1 and 3.2 have reached upstream end-of-life [confirm dates against
  ruby-lang.org]. We may drop them under the rule above.

## Pre-releases and channels

- Release candidates use RubyGems spelling: `0.32.0.rc1`, `0.32.0.rc2`.
  Bundler skips them unless a Gemfile asks for them.
- Release candidates are unsupported.
- Each maintained old line is cut from a `release-0.MINOR` branch, for example `release-0.30`.
- Published versions are immutable. We fix forward, then `gem yank` only for
  a security hole, data loss, or a break shipped in a patch release.

## Release cadence

Feature-based. A merged fix ships within six weeks [confirm]. We do not publish
empty releases. Security fixes ship out of band.

## Supported versions

| Line     | Status      | Fixes         | Supported until                         |
| -------- | ----------- | ------------- | --------------------------------------- |
| 0.31.x   | current     | all           | while current                           |
| 0.30.x   | maintenance | security only | <date: 6 months after 0.31.0 shipped>   |
| <= 0.29  | unsupported | none          | -                                       |

Rule going forward: when a new 0.MINOR ships, the previous 0.MINOR becomes
maintenance (security fixes only) for six months. Then it becomes unsupported.
At most one maintenance line exists at a time.

Issues on unsupported lines are closed with a link to this table, unless they
reproduce on a supported line.

## Backports

- Only security fixes go to a maintenance line.
- The maintainer who holds publish rights decides.
- A backport ships as a patch on that line, cut from its `release-0.MINOR` branch.
- The security advisory lists the patched version of every supported line, so
  `bundler-audit` and update bots propose the backport instead of a jump to the current line.

## Deprecation

- Deprecated options and methods emit a Ruby warning naming the replacement.
- They also get a changelog entry in the release that deprecates them.
- Removal happens only in a 0.MINOR release, after the deprecation has been
  present in at least two 0.MINOR releases and at least three months [confirm].
- Security-critical removals may be faster. The changelog says so.

## Known past breaks

- 0.29.0 removed the deprecated `legacy_signer` option after one release of warning.
- 0.30.0 changed the default retry count from 3 to 5, which raised request volume
  and cost for some users. Set `retries: 3` to restore the old behavior.

Both stay as shipped. Reverting would break users who already upgraded.
The deprecation and defaults rules above exist so neither repeats.

## Who can cut a release

One maintainer holds RubyGems push rights [confirm 2FA is required on the gem].
If that person is unavailable, no release ships, security releases included,
until they are back. The second maintainer reviews and merges but cannot publish.

## Changes to this policy

Announced in the changelog one release before they apply.
```

## Capacity check

The two inputs below are my assumptions. Replace them from your last 12 months of changelog.

| Item | Hours a month |
|---|---|
| Ordinary releases (assumed) | 2.0 |
| One security-only line: ~3 fixes a year × ~2 h per backport (planning default) | 0.5 |
| **Total** | **2.5 of 5** |

That leaves about 2.5 hours for triage and review. A second maintenance line would add roughly 0.5 hours a month and still fit, but I did not promise it.

## Also publish

- **SECURITY.md:** link to the Supported versions table. Keep the table in RELEASES.md only, so two copies can't drift.
- **Changelog first line:**
  `This project uses Semantic Versioning, in 0.x: 0.MINOR is the breaking digit. See [RELEASES.md](RELEASES.md) for what each number promises and which versions get fixes.`
- **Release-time check (CI):** fail when the git tag, the gemspec `version` and the top CHANGELOG entry disagree. This is a pass condition of the skill, and I did not write the script.

## Decisions for you

1. **Confirm** the public surface list. I wrote generic items because I haven't seen the code. The exclusions are the part the maintainers need most.
2. **Deprecation window.** The policy says two 0.MINOR releases and three months. That is stricter than the one-release warning before `legacy_signer` was removed, so it is a new commitment, not a record of past practice. Say if you want it looser.
3. **Ruby floor.** 3.1 and 3.2 have reached upstream end-of-life. Do any target adopters run distro Rubies, such as Debian's? That would be a reason to keep 3.1 anyway.
4. **Security response time.** The customer review will probably ask for one. I left it out because you didn't give a number. I'd suggest "patch within 30 days of a confirmed report" if you can staff it.
5. **Sole push rights.** The review will see a bus factor of one. Giving the second maintainer push rights removes it. If you decline, the "Who can cut a release" wording stays as written. See `oss-maintainer-sustainability`.
6. **0.30 end date.** Fill in the real 0.31.0 release date plus six months. If that date has already passed, mark 0.30 unsupported now.