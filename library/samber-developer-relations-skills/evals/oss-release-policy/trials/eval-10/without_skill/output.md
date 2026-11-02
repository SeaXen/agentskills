# Verdict: ❌ Don't merge yet

Two items are blockers, and the rest are gaps that make the policy unenforceable. Most fixes need a decision from you, so I've listed those at the end.

## Blockers

1. **`3.5.0-FINAL` breaks version ordering.**
   - SemVer treats any `-suffix` as a pre-release, so `3.5.0-FINAL` sorts *before* `3.5.0`.
   - Maven treats `final` as equal to the plain release, so the two compare as the same version.
   - Tools that resolve ranges will disagree on which one is newer.
   - Replace it with a SemVer-clean scheme such as `3.5.0-RC.1` or `3.5.0-M1`, and document the ordering.
   - Don't mention `-SNAPSHOT` as something you "publish". Maven Central does not host snapshots, so say where they live (a snapshot repository) and that they carry no stability promise.

2. **"Breaking = any change to the public API. Exclusions: TBD."**
   - A `TBD` in the central definition makes the whole policy unenforceable.
   - "Any change" is also wrong. Adding a method is not breaking under SemVer.
   - Define the public API: which packages count, and whether `internal` or `impl` packages are excluded.
   - Decide whether each of these counts as breaking: the wire protocol, supported broker versions, config keys, serialized formats, exception types, the minimum Java version, and the `Automatic-Module-Name`.

## Major gaps

3. **Supported versions.**
   - "As long as people use it" is an open-ended promise you can't verify. It commits you to security fixes for 1.x and 2.x indefinitely.
   - "While current" for 3.x is circular.
   - Give end dates, or a rule such as "N months after the next major".
   - 1.x is probably EOL.
   - State whether only the latest minor of a line is supported. For example, does 3.3.x still get fixes now that 3.4.x exists?
   - Define "current", "maintenance" and "EOL".

4. **The table is duplicated in SECURITY.md.**
   - The two copies will drift apart, and drift in a security table is worse than drift here.
   - Keep one source. Have SECURITY.md link to RELEASES.md, or generate the table from one file.

5. **Deprecation.**
   - "We mark things @Deprecated" gives no removal rule.
   - Use `@Deprecated(since = "…", forRemoval = true)` and a Javadoc pointer to the replacement.
   - Set a minimum window, for example at least one minor release and 6 months.
   - Allow removal only in a major release.
   - Require a migration note in the release notes.

6. **Runtime support.**
   - "When it makes sense" is not a criterion.
   - State which JDKs CI tests (11, 17, 21, and so on).
   - State whether raising the minimum Java is a major or a minor change. I recommend major, or at minimum an announcement one minor release ahead.
   - Tie the rule to LTS releases.

7. **Cadence: "Whenever."**
   - You don't need a rigid schedule, but state a target (for example, a minor release roughly every quarter, patches as needed).
   - Also state the response time for security fixes.

8. **Backports: "On request."**
   - Say who decides and on what criteria.
   - Say which lines are eligible: security and data-loss fixes only, or also regressions.
   - Say how to request one.

9. **Release authority: "Dmitri."**
   - A single named person is a bus-factor risk, and personal names age badly in policy docs.
   - Name a role or team and a backup.
   - Cover who holds the Central publishing credentials and signing key.

## Missing sections

- **Where release notes and changelog live.** Without this, deprecation notices have nowhere to go.
- **EOL announcement process.** Say how far ahead you announce, and where.
- **Security reporting.** Link to SECURITY.md for the process and expected response time.
- **Pre-release stability.** Say whether APIs can change between RCs.

## Decisions I need from you

1. What counts as public API, and what is excluded?
2. Is raising the minimum Java version a major or a minor change?
3. What is the end date or rule for 1.x and 2.x?
4. What is the deprecation window?
5. Which pre-release scheme do you want (`-RC.n` or `-M.n`)?
6. Who is the backup to Dmitri?
7. Do you want a target release cadence?

Answer those and I'll turn the draft into a mergeable version. I'll also change SECURITY.md to link to RELEASES.md.