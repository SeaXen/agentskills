# Decision: none of the three as written. Publish 4.7.1 that reverts the default.

## Why not your options

- ❌ **(a) Delete tag, republish 4.7.0.** npm never lets you reuse a version number, even after unpublish. Deleting the git tag changes nothing on the registry. Unpublishing a package with 300k weekly downloads also breaks every lockfile pinned to 4.7.0.
- ❌ **(b) `4.7.0+hotfix`.** Semver ignores build metadata when comparing versions, so npm treats this as 4.7.0 again and it can't be a separate release.
- ⚠️ **(c) Tell people to pin 4.6.x.** Use it as a stopgap only. It makes 40 users do work to fix your mistake, and the other ~300k keep floating onto 4.7.0.

## Do now

1. Revert the default to the process TZ on a branch.
2. Add a regression test: with `TZ=America/New_York` and no `timezone` option, a `0 9 * * *` job fires at 09:00 New York.
3. **Publish 4.7.1** (`npm publish`). Ranges like `^4.6.0` resolve to the highest matching version, so 4.7.1 replaces 4.7.0 for anyone who reinstalls or updates. Moving the `latest` tag alone would not help them.
4. **Deprecate 4.7.0** (`npm deprecate tidewatch@4.7.0 "Changed default timezone to UTC, jobs fire at the wrong hour. Upgrade to 4.7.1."`). This prints a warning on install.
5. **Pin the issue.** Open a pinned issue and close the 40 duplicates with a link to it. Say what happened, who is affected (anyone on 4.7.0 whose process TZ isn't UTC), and the fix: upgrade to 4.7.1, or pin 4.6.x until you can.
6. Publish a GitHub release for 4.7.1 and a changelog entry. Describe the behavior change honestly. Do not write "bug fix".
7. Add an advisory note for people whose jobs already ran at the wrong hour on 4.7.0: they should check for missed or duplicated runs.

## Ship UTC properly later

- **Next minor:** add an explicit `timezone` option. If it's unset and `TZ` isn't UTC, log one warning that the default will change in v5.
- **v5.0.0:** change the default to UTC, with a migration guide that says what breaks and how to detect it.

Some users who adapted to UTC in the last day will be affected by the revert. That group is small and the deprecation message covers them.

## Policy text to add

> ### Breaking changes are defined by behavior, not signatures
>
> A change is **breaking** if code that worked on the previous version can produce a different result without any code change on the user's side. This covers function signatures, defaults, timezones and locale, ordering, rounding, error types, log or output format, retry or timeout values, and the semantics of existing config. Breaking changes ship only in a **major** version.
>
> 1. **Default changes need a gate.** Before changing any default, list the observable differences in the PR description. If there are any, the change is breaking.
> 2. **Warn first, flip later.** Add an explicit option and a runtime warning in a minor release. Flip the default only in the next major.
> 3. **Soak before stable.** Publish risky majors, and any release touching time, scheduling or numeric behavior, first under the `next` dist-tag (e.g. `5.0.0-rc.1`). Wait at least 7 days and test against the top dependents.
> 4. **No "bug fix" label for default changes.** The changelog must name every behavior change under a "Behavior changes" heading.
> 5. **Never unpublish, never retag a version.** Published versions are immutable. The remedy for a bad release is the **next patch version**.
> 6. **Bad-release response (target: within 4 hours of the first confirmed report):**
>    1. Revert, test, and **publish** the patch.
>    2. **Deprecate** the bad version with a message that links to the fix.
>    3. Pin one tracking issue and close duplicates against it.
>    4. Write a short post-mortem in the repo within 7 days.
> 7. **Release owner signs off.** The release owner confirms the PR description lists behavior differences (rule 1) and that this release type doesn't need a `next` soak (rule 3). This is a checklist item in the release PR template.

## Post-mortem notes

- **Root cause:** the review was based on "no signatures changed" as the compatibility test. The policy now replaces that test with "can the same code produce a different result?"
- **Process gap:** a default changed with no soak period and no warning.
- **Check:** add a CI test suite that runs the scheduler under a non-UTC `TZ`, so this class of change fails before release.