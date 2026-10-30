# RELEASES.md template and worked example

Contents: Template · Worked example (Node.js library) · SECURITY.md supported-versions block · Changelog header line

Fill every section in SKILL.md step 8. A section left as "TBD" is a promise nobody owns. Delete a section only when the project truly has nothing there, such as a single supported line, and say so in one line.

## Template

```markdown
# Release policy

## Version numbers

We use <scheme> (`<shape>`). <One sentence on what each segment means.>
<0.x only: "Until 1.0, 0.MINOR is the breaking digit and 0.x.PATCH is a compatible fix.">
<CalVer only: "The number says when, not what broke. Compatibility is defined below.">

## What we consider breaking

Covered by this promise: <public surface list>.
Not covered: <explicit exclusions>.
Opt-in unstable: <how marked, outside the promise>.

## Runtime support

<Runtimes and host versions supported, the rule for dropping one, and the package-metadata field that declares the floor.>

## Pre-releases and channels

<Spelling per registry, channel, dist-tag or release branch per maintained line, what "stable" means. What triggers withdrawing a release.>

## Release cadence

<Model> - <interval or trigger>. <Maximum gap promise if any.> Security fixes ship out of band.

## Supported versions

| Line  | Status      | Fixes         | Supported until |
| ----- | ----------- | ------------- | --------------- |
| <x>   | current     | all           | while current   |
| <y>   | maintenance | security only | <date or rule>  |
| older | unsupported | none          | -               |

Issues on unsupported lines: <closed with a link to this table unless they reproduce on a supported line>.

## Backports

<Which fixes get backported, to which lines, who decides, how they are numbered.>

## Deprecation

<Warning mechanism, minimum window in releases and time, where it is announced.>

## Known past breaks

<Breaks shipped under the wrong number that stay, with version and what changed. "None" if none.>

## Who can cut a release

<People or roles holding publish rights and signing keys, and the fallback when they are unavailable.>

## Changes to this policy

<How and how far ahead the policy itself changes.>
```

## Worked example

Input: a Node.js HTTP client library on npm, 1.x with company users, two maintainers with about 4 hours a month for release work, one prior complaint about a minor release that dropped Node.js 18.

Output:

```markdown
# Release policy

## Version numbers

We use Semantic Versioning (`MAJOR.MINOR.PATCH`). Caret ranges (`^1.4.0`) never
pick up a new major, so upgrading to v2 is always the user's choice.

## What we consider breaking

Covered: every entry point in the `exports` map (`.` and `./middleware`), their
documented behaviour, the default timeouts, the error classes thrown and their
`code` values, and the shipped TypeScript types.
Not covered: any path outside the `exports` map, log message text, undocumented
property ordering, and behaviour the docs call a bug.
Opt-in unstable: none.

## Runtime support

We support every Node.js release line the Node.js project lists as Active or
Maintenance LTS. Dropping a Node.js line ships only in a major release, announced
one release ahead, with `engines.node` in package.json raised in the same release.

## Pre-releases and channels

Release candidates are tagged `X.Y.Z-rc.N` and published under the `next`
dist-tag, so `latest` never points at one. Nothing tagged `-rc` is supported.
A release is deprecated (`npm deprecate`) only for a security hole, data loss,
or a break shipped as a minor or patch. We never unpublish.

## Release cadence

Feature-based. A merged fix ships within four weeks. Security fixes ship as soon
as they are ready.

## Supported versions

| Line | Status      | Fixes | Supported until                                             |
| ---- | ----------- | ----- | ----------------------------------------------------------- |
| 1.x  | current     | all   | while current; then security-only for 12 months after 2.0.0 |
| 0.x  | unsupported | none  | ended 12 months after 1.0.0                                 |

Issues on unsupported lines are closed with a link to this table unless they
reproduce on a supported line.

## Backports

Only security fixes, and only to lines marked maintenance. Backports ship as a
patch on that line, cut from its `release-1.x` branch and published with
`--tag release-1.x` so `latest` stays on the current line. The advisory lists
the patched version of every supported line.

## Deprecation

Deprecated APIs carry a JSDoc `@deprecated` tag, emit one `DeprecationWarning`
at runtime, and get a changelog entry in the minor that deprecates them. They
are removed only in the next major, no sooner than six months after the
deprecation.

## Known past breaks

1.6.0 dropped Node.js 18 in a minor release. It stays dropped, because reverting
would break users who already upgraded; this policy's runtime rule exists so it
does not happen again.

## Who can cut a release

Both maintainers hold npm publish rights, with two-factor authentication
required on the package. If neither is available, no release ships until one is.

## Changes to this policy

Announced in the changelog one release before they apply.
```

What the example does on purpose:

- The runtime floor gets its own section and a metadata rule, because the prior complaint was about exactly that. Dropping a Node.js line is a major because npm treats `engines` as advisory by default: a minor that raises it still installs on the old runtime and fails there. The old break is recorded, not reverted.
- Backports publish under their own dist-tag, because `npm publish` moves `latest` by default and a 1.x patch would otherwise replace 2.x for every new install.
- Default timeouts are listed as covered, because a changed default breaks callers without a signature change.
- Security-only maintenance of v1 is limited to 12 months. Capacity check: about 3 security fixes a year × about 2 hours per backport ≈ 0.5 hours a month for the extra line, plus about 2 hours a month of ordinary releases, inside the 4 hours available.

## SECURITY.md supported-versions block

Keep the Supported versions table in one file only, because two copies drift within a release. Link to it from SECURITY.md. If the forge or a reporter expects the table inside SECURITY.md, move it there and link to it from RELEASES.md instead. The rest of SECURITY.md (reporting channel, embargo, advisories) is a different job.

## Changelog header line

```markdown
This project uses <scheme>. See [RELEASES.md](RELEASES.md) for what each number promises and which versions get fixes.
```
