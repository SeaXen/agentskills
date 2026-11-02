**Pick none of (a), (b) or (c) as the fix. Publish 4.7.1 with the process-TZ default restored, and deprecate 4.7.0.** Your policy skill says a break shipped by accident in the latest release gets a fix release that restores compatibility, "never a re-tag".

I didn't run the full interview. I haven't seen tidewatch's repo, so the policy text below assumes SemVer on npm. Check the bracketed values.

## Why not a, b or c

- **(a) Delete the tag and republish 4.7.0: impossible.** npm never lets you republish a version, even after unpublish. Registry mirrors and caches keep the old tarball. Some installs would get the broken 4.7.0 and some the fixed one under the same number.
- **(b) `4.7.0+hotfix`: does not work.** SemVer ignores build metadata when ordering versions. npm strips it. Resolvers would see it as 4.7.0, so nobody receives it.
- **(c) Pin 4.6.x: a stopgap, not a fix.** It leaves `latest` pointing at the broken release. Every fresh install of `^4` still gets it. Use it only as a workaround in the announcement, until 4.7.1 is out.

## Do now (about 30 minutes if tests cover the scheduler)

1. Branch from the 4.7.0 tag. Restore the process-TZ default and keep everything else in 4.7.0.
2. Add a regression test. With `process.env.TZ` set to a non-UTC zone and no `timezone` option, a `0 9 * * *` job must fire at 09:00 in that zone.
3. Bump to `4.7.1`, add a changelog entry that names the break, and run `npm publish`.
4. Run `npm dist-tag ls tidewatch` and confirm `latest` points to 4.7.1.
5. Run `npm deprecate tidewatch@4.7.0 "Changed default timezone to UTC; jobs fire at the wrong hour. Upgrade to 4.7.1."`
6. Post one pinned issue and a release note. The note says:
   - 4.7.0 changed the default timezone from the process TZ to UTC.
   - Jobs scheduled during the 4.7.0 window may have fired at the wrong hour. List the affected window.
   - Anyone who set `timezone` explicitly is unaffected.
   - Anyone who adapted to UTC in the last day must now set `timezone: 'UTC'` explicitly. This is the cost of restoring the old default.
7. Close the 40 issues as duplicates of the pinned one.

Do not unpublish. Do not delete the 4.7.0 git tag, since the registry does not follow git tags.

**If you still want UTC as the default:**
- **4.8.0:** add an opt-in `timezone: 'utc'` option and a one-time warning when no timezone is set.
- **5.0.0:** flip the default, with a migration guide.

## Policy to add to RELEASES.md

Replace the "What we consider breaking" section and add the "Known past breaks" and "Accidental breaks" text. Prose is normal English because it ships in the repo.

```markdown
# Release policy

## Version numbers

We use Semantic Versioning (`MAJOR.MINOR.PATCH`). Caret ranges (`^4.6.0`) never
pick up a new major, so a major upgrade is always the user's choice.

## What we consider breaking

Covered by this promise:
- Every export in the `exports` map, with its signature and documented behaviour.
- Every default value, including the default time zone, locale, missed-run and
  overlap handling, retry policy, and jitter.
- Error classes and their `code` values, and the shipped TypeScript types.

A changed default is a breaking change, even when no signature changes. Changing
when, how often, or in which order a job fires is a breaking change.

Not covered: paths outside the `exports` map, log message text, and behaviour the
docs call a bug.
Opt-in unstable: [none / list].

Doubt rule: if we are unsure whether a change is breaking, we treat it as
breaking and ship it in a major. Dependents automerge minors and patches, so a
break shipped as a minor reaches production without review.

## Changing a default

A default may change only in a major release, and only after this sequence:
1. One minor release adds an explicit option that selects the new behaviour.
2. The same release warns once at startup when the option is unset and the
   behaviour would differ.
3. The major release flips the default, and the migration guide lists the change.

Calling a default change a "bug fix" does not exempt it. Our own judgment that the
old default was wrong is not a reason to skip the sequence.

## Accidental breaks

If a release breaks the promise above, we do not re-tag or republish it. Within
one working day we:
1. Publish a patch that restores the previous behaviour.
2. Move `latest` to the patch and run `npm deprecate` on the broken version.
3. Add the break to "Known past breaks" and to the changelog.

If restoring the old behaviour would break users who already adapted, because the
break is older than the latest release, it stays and is recorded under "Known
past breaks".

## Pre-releases and channels

Release candidates are tagged `X.Y.Z-rc.N` and published with `--tag next`, so
`latest` never points at one. We never unpublish, and we deprecate a release only
for a security hole, data loss, or a break shipped as a minor or patch.

## Release gates

CI blocks a publish unless all of these hold:
- The git tag, `package.json` version, and changelog entry agree.
- The defaults snapshot test passes (see below). A diff in that snapshot requires
  a major version bump in the same pull request.
- Every pull request that touches a default carries the label `breaking-default`.
  Release notes list those pull requests under "Breaking".

## Release cadence

Feature-based. A merged fix ships within [4] weeks. Security fixes ship out of band.

## Supported versions

| Line  | Status      | Fixes         | Supported until                      |
| ----- | ----------- | ------------- | ------------------------------------ |
| 4.x   | current     | all           | while current                        |
| 3.x   | maintenance | security only | [12] months after 4.0.0 / [date]     |
| older | unsupported | none          | -                                    |

Issues on unsupported lines are closed with a link to this table unless they
reproduce on a supported line.

## Known past breaks

4.7.0 changed the default time zone from the process TZ to UTC. 4.7.1 restored it.
4.7.0 is deprecated on npm.

## Who can cut a release

[names or roles] hold npm publish rights, with two-factor authentication required.

## Changes to this policy

Announced in the changelog one release before they apply.
```

**Defaults snapshot test.** This is the mechanical gate that would have caught 4.7.0:
- Export the resolved defaults object, including the resolved time zone under a fixed non-UTC `TZ`.
- Compare it to a committed `defaults.snapshot.json` in CI.
- A snapshot change without a major bump in `package.json` fails the build.
- Keep one snapshot test per default that affects scheduling, not only the time zone.

## What is still open

The bracketed values are unanswered. The skill requires the capacity arithmetic to fit your maintainer hours, and I can't do that without your numbers. I need:
1. Maintainer hours per month for releases and backports.
2. Whether 3.x gets security-only fixes, and for how long.
3. Who holds npm publish rights.

**Next:** reply with those three, and I'll finalise the table and the capacity arithmetic. In the meantime, start on the 4.7.1 branch.