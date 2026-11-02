# Verdict: not ready to merge

The draft names a scheme but doesn't yet say what the number promises. I checked it against the oss-release-policy checklist, and it fails 4 of the 5 pass checks. Details follow. I read the draft only, not the graniteq repo, manifests or changelog.

## Pass checks

| # | Check | Result |
|---|---|---|
| 1 | Every template section is filled or marked "none" | ❌ "TBD", "Whenever" and "On request" are placeholders. "Known past breaks" and "Changes to this policy" are missing. |
| 2 | Every supported line has an end date or ending event | ❌ 1.x and 2.x read "as long as people use it", which never ends. |
| 3 | The capacity arithmetic fits the maintainers' hours | ❌ There is no arithmetic, and no hours figure to test it against. |
| 4 | The exclusion list has at least one entry, and the runtime section names the metadata field | ❌ The exclusions are "TBD" and no metadata field is named. |
| 5 | A release-time check exists (tag, pom version and changelog agree) | ❌ None. |

## Blockers

1. **"Any change to the public API. Exclusions: TBD."**
   - SemVer without a declared surface promises nothing.
   - Hyrum's Law means someone depends on everything observable, so the exclusion list protects you more than the inclusion list does.
   - For a Java broker client, write three lists:
     - **Covered:**
       - exported packages and signatures (binary compatibility, JLS ch. 13);
       - documented behaviour;
       - default values such as timeouts, retries and ack mode;
       - exception types;
       - config keys;
       - supported broker and wire-protocol versions;
       - the `module-info` or `Automatic-Module-Name`;
       - any third-party type that appears in your signatures (a logging or Netty type, for example). Bumping its major is breaking for you.
     - **Not covered:** `*.internal.*` packages, log message text, `toString()` output, and anything the docs call a bug.
     - **Opt-in unstable:** anything marked `@Experimental` or similar, and how you mark it.

2. **"Java 11+. We'll drop old Java versions when it makes sense."**
   - This is not a rule.
   - The Maven ecosystem doesn't enforce a runtime floor. A bump to `maven.compiler.release` lands in dependents' builds as a class-version error at runtime.
   - Name the metadata field that declares the floor, for example `maven.compiler.release` plus a CI job on the oldest JDK.
   - Dropping a Java version that the vendors and distros still support is breaking, so it ships in a major, announced one release ahead.
   - Dropping one that is past end-of-life everywhere could ship in a minor. You have to pick that, because nothing in Maven decides it for you.

3. **`3.5.0-FINAL` is a real trap on Maven Central.**
   - Maven orders qualifiers as `alpha < beta < milestone < rc < snapshot < (release) = final = ga < sp`.
   - So `3.5.0-FINAL` compares equal to `3.5.0`. Dependents and tools can't tell them apart.
   - Central never allows republishing a version. If `-FINAL` goes out wrong, you can only fix forward.
   - Maven 4 also discourages `final`.
   - Replace it with numbered candidates (`3.5.0-RC1`, `-RC2`, so the tenth sorts after the ninth). Treat anything with a pre-release label as unsupported.
   - State that `-SNAPSHOT` builds are mutable by design, unsupported, and never a release.
   - State that withdrawal means "release a fixed version". There is no yank on Central.
   - State what triggers a withdrawal: a security hole, data loss, or a break shipped as a minor or patch.

4. **The supported-versions table promises more than anyone can staff.**
   - 1.x and 2.x have security fixes "as long as people use it", with no end.
   - That is two extra lines for the life of the project.
   - Size them first:
     1. Count security fixes from the last 12 months.
     2. Time the last backport.
     3. Monthly cost = ordinary release hours + extra lines × fixes per month × hours per backport.
     4. Compare to the maintainers' real monthly hours.
   - Example with made-up numbers (replace them with yours). 3 fixes a year across 2 lines at 2 h per backport is about 1 h a month, plus about 2 h a month of ordinary releases.
   - Pick a fixed window per line, with an end date or an ending event. For example, "2.x: security only until 12 months after 3.0.0 shipped". Move 1.x to unsupported unless you can show real users and real hours.
   - Say what happens to issues on unsupported lines: closed with a link to the table unless they reproduce on a supported line.

5. **The table is pasted in two places.**
   - Two copies drift within a release.
   - Keep it in RELEASES.md and link to it from SECURITY.md. If the forge expects the table inside SECURITY.md, put it there and link the other way.
   - Also make every security advisory list the patched version on each supported line. Otherwise update bots propose a major jump instead of the backport.

6. **"Backports: On request."**
   - Say which fixes get backported (security only, or also data-loss bugs), to which lines, and who decides.
   - Say how they're numbered. Maven Central has no dist-tags, so use a release branch such as `release-2.x` and publish a patch on that line (2.9.4, not 3.4.x).

## Smaller fixes

- **Cadence "Whenever."** Use feature-based with a maximum gap, for example "a merged fix ships within N weeks", with security fixes out of band. You get predictability at near-zero overhead.
- **Deprecation "We mark things @Deprecated."**
  - Add the minimum window in releases and time.
  - Name the replacement in the Javadoc `@deprecated` tag, using `@Deprecated(since="…", forRemoval=true)` where removal is planned.
  - Add a changelog entry in the minor that deprecates.
  - Remove only in the next major, no sooner than N months. Pick a window spanning at least two releases at your cadence.
- **"Who can cut a release: Dmitri."**
  - That is one person with no fallback.
  - Name the roles that hold Central publish rights and the GPG signing key, and say what happens if they're unavailable.
  - If Dmitri really is the only one, this is a sustainability problem. The oss-maintainer-sustainability skill covers it.
- **Add a release-time check.** CI fails unless the tag, the `pom.xml` version and the changelog entry agree.
- **Add the missing sections.**
  - "Known past breaks": list breaks shipped under the wrong number that stay, or write "none".
  - "Changes to this policy": say how far ahead a change is announced.
  - Put a one-line scheme statement at the top of the changelog, linking to RELEASES.md.

## Draft you can start from

Items in `<angle brackets>` are decisions only you can make.

```markdown
# Release policy

## Version numbers
We use Semantic Versioning (`MAJOR.MINOR.PATCH`). MAJOR changes on any
incompatible change to the surface listed below, MINOR adds compatible
features and deprecations, PATCH is a compatible fix.

## What we consider breaking
Covered: exported packages and signatures (binary compatible), documented
behaviour, default timeouts/retries/ack mode, exception types, config keys,
supported broker and wire-protocol versions, <third-party types in our
signatures>.
Not covered: `*.internal.*` packages, log message text, `toString()` output,
behaviour the docs call a bug.
Opt-in unstable: <marker, e.g. @Experimental>; outside this promise.

## Runtime support
Java 11 and newer. The floor is declared by `maven.compiler.release` and
tested on JDK 11 in CI. Dropping a Java version still supported by
<vendors/distros> ships only in a major, announced one release ahead.
<Dropping one past end-of-life everywhere may ship in a minor: yes/no.>

## Pre-releases and channels
Candidates are `X.Y.Z-RC1`, `-RC2`, ... and are unsupported. `-SNAPSHOT`
builds are mutable development builds, never releases. Published versions
are immutable; a bad release is fixed forward with a new version. We
withdraw (and say so in the changelog) only for a security hole, data loss,
or a break shipped as a minor or patch.

## Release cadence
Feature-based. A merged fix ships within <N> weeks. Security fixes ship out
of band.

## Supported versions
| Line | Status      | Fixes         | Supported until                    |
|------|-------------|---------------|------------------------------------|
| 3.x  | current     | all           | while current                      |
| 2.x  | maintenance | security only | <date, or N months after 3.0.0>    |
| 1.x  | unsupported | none          | ended <date>                       |

Issues on unsupported lines are closed with a link to this table unless they
reproduce on a supported line. (Single copy; SECURITY.md links here.)

## Backports
Security fixes only, to lines marked maintenance. <Role> decides. Each ships
as a patch on that line, cut from `release-2.x`. Advisories list the patched
version of every supported line.

## Deprecation
`@Deprecated(since, forRemoval=true)` plus a Javadoc `@deprecated` tag naming
the replacement, and a changelog entry in the deprecating minor. Removal only
in the next major, at least <N> months and two releases later.

## Known past breaks
<List, or "None.">

## Who can cut a release
<Roles> hold Central publish rights and the signing key. Fallback:
<named second person>. CI checks that tag, pom version and changelog agree.

## Changes to this policy
Announced in the changelog one release before they apply.
```

## Questions only you can answer

Each one decides a placeholder above:

1. How many hours a month can the maintainers spend on releases and backports?
2. How many security fixes did you ship in the last 12 months?
3. Are real users still on 1.x and 2.x?
4. Who besides Dmitri can publish to Central?
5. What were the last two things that broke users? They show where your real public surface sits.
6. Which Java versions do your target adopters run past upstream end-of-life?

Once those are answered and the five checks pass, it's mergeable.