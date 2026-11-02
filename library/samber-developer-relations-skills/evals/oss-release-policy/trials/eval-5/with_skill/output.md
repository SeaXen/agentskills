**Next action (2 min):** pick the scheme in section 2, then reply "SemVer" or "CalVer". The draft in section 4 assumes SemVer-shaped numbers and is one find-and-replace away from CalVer.

I read the SKILL.md and its four references. I answered the interview from your message and marked the answers I assumed.

## 1. What I assumed

| Interview item | Value used |
|---|---|
| Artifact | Electron desktop app, no importers. macOS and Windows auto-update. Debian and Fedora packagers maintain their own packages. |
| Scheme now | SemVer-shaped, 3.8.2. |
| Real public surface | The project file. The 3.6 break shows it. |
| Capacity | 4 h per release, a release every 6-8 weeks. **Not answered:** your monthly release-hours budget. |
| Assumed (check) | 3.5 users stayed stuck because Linux distro packages and disabled updaters lag. The auto-updater should have moved everyone else. |
| Assumed (check) | Project files carry no explicit format version today. |
| Assumed (check) | 3.8.2 does not show a clear "newer file" message when it opens a file from a newer format. |

## 2. Scheme: recommendation is stay on SemVer

The number's readers are humans, the auto-updater and packagers. No resolver reads it. By reader ranking that favors CalVer over SemVer, and a major costs almost nothing here because nobody has a range to edit. Two things override the ranking:

- **The 3.6 break was a missing signal, not a wrong number format.** CalVer "deliberately does not attempt to communicate breaking changes". Under CalVer, the only thing that warns of a format break is prose. Under SemVer, a rule like "format break means MAJOR" gives users one cheap warning channel.
- **SemVer is already shipped.** Switching needs a reason users would accept, and "it is the standard" is not one. The rejected PEP 2026 is the counter-case: a more readable number alone did not justify the churn.

| | **A. SemVer-shaped (recommended)** | **B. CalVer `YY.M.MICRO`** |
|---|---|---|
| Next number | 3.9.0, or 4.0.0 if the format changes | 26.12.0 (if it ships in December) |
| Promise | MAJOR means a user must act or a covered thing broke | The number says when, not what broke |
| Ordering check | No change | 26 sorts above 3 everywhere, so no epoch is needed. Tell packagers first. |
| Cost to leave | Easy | Hard: going back to 4.x would sort below 26.x |
| Burden | The team judges every release | None for the number, but all compatibility moves into prose |

If the team picks B, add one line stating that the year and month are not compatibility signals. Also keep the app version separate from the project format version, as in the draft.

## 3. Capacity arithmetic

- Ordinary releases: 6.5-8.7 per year × 4 h = 26-35 h per year, or 2.2-2.9 h per month.
- Out-of-band security releases: I assumed 4 per year, because Electron and Chromium fixes arrive often. 4 × 4 h = 16 h per year, or 1.3 h per month.
- Total: about 3.5-4.2 h per month.
- Extra supported lines: none. Your monthly budget is unknown, so no old line gets backports. Packagers carry their own.
- Release-candidate builds: only for releases that change the file format or bump MAJOR.

**If your real budget is under 4 h per month,** drop the release-candidate rule or lengthen the cadence. Tell me the figure and I'll recheck.

## 4. Draft RELEASES.md

````markdown
# Release policy

## Version numbers

Ferncast uses `MAJOR.MINOR.PATCH` (for example 3.8.2).

- MAJOR: something users must act on, or something covered below breaks.
- MINOR: new features, compatible with everything covered below.
- PATCH: compatible fixes.

The project file also has its own `formatVersion`, a whole number
stored in every file. The app version says what to install. The
format version says whether a file can travel to a colleague. Both
appear in Help > About and in any "cannot open" message.

Auto-updaters and app stores also need a build number. It is a
whole number that only goes up. Quote both the version and the build
number in bug reports.

## What we consider breaking

Covered by this promise:

- The project file format, for reading and writing (see "Project file format").
- User settings, export presets and library data that Ferncast reads on start.
- Default export settings (loudness, sample rate, encoder options), because a changed default changes users' output.
- Command-line flags, if any, and their exit codes.
- The minimum supported operating system versions.

Not covered: UI layout and styling, keyboard shortcuts not listed in
the manual, internal cache and log locations, log text, undocumented
fields in project files, and bit-exact output of lossy encoders
across versions.

Opt-in unstable: features marked "Experimental" in Settings. A
project file that uses one is outside the format promise and is
labelled as such in the file.

## Project file format

1. Every project file stores `formatVersion` and the app version that
   saved it.
2. Every release opens every format that any 3.x release has written.
   Reading old formats is never removed.
3. Same-major rule: a file saved by any release of a major line must
   open, with all pre-existing content intact, in the first release of
   that line. A change that fails this is breaking.
4. A breaking format change ships only in a MAJOR release and raises
   `formatVersion`. It is never allowed in a MINOR or PATCH.
5. An older release that meets a newer `formatVersion` refuses to
   open it and says which Ferncast version is needed. It never opens
   the file partially. The release before the first format break must
   already contain this guard.
6. Opening an older-format file never rewrites it. The first save in a
   newer format asks for confirmation, says that colleagues on older
   versions may not be able to open the result, and keeps a backup of
   the original next to it.
7. After a MAJOR changes the format, "Save a copy for Ferncast N-1"
   stays available for 12 months. It lists any content that cannot be
   represented in the older format.
8. A format-changing release gets a release candidate at least one week
   before, a migration guide, and advance notice to the Debian and
   Fedora packagers.
9. Release gate: CI opens a fixture file for every `formatVersion` and
   opens a file saved by the new build in the first release of the
   current major. The release checklist asks "did the format
   change?". Yes means a MAJOR bump.

## Runtime support

- macOS and Windows: the minimum OS is set by the bundled Electron
  version. It is declared in the macOS bundle (`LSMinimumSystemVersion`)
  and in the update feed's minimum-OS gate. Dropping an OS version is
  breaking. It ships in a MAJOR, announced one release ahead with an
  in-app notice. Before the release, we verify that the updater does
  not offer it to machines that cannot run it.
- Linux: we support every Debian and Fedora release that the distro
  still supports, using the distro's end-of-life date, not the
  upstream one.

## Pre-releases and channels

Release candidates are tagged `X.Y.Z-rc.N` (for example `4.0.0-rc.1`).
They are served only on the opt-in beta update channel, never on the
default one. Nothing tagged `-rc` is supported. Packagers can rewrite
the tag to their own spelling.

A published version is never re-tagged or replaced. A bad release is
fixed forward and pulled from the update feed. We pull a release for a
security hole, data loss, or a break shipped as a minor or patch.

## Release cadence

Feature-based with a maximum gap. We aim for one release every 6-8
weeks and never go longer than 10 weeks when fixes are merged. We do
not publish empty releases. Security fixes ship out of band.

## Supported versions

| Line | Status | Fixes | Supported until |
| --- | --- | --- | --- |
| Latest release | current | all | while current |
| Anything older | unsupported | none | - |

Mac and Windows users are moved to the latest release by the
updater. Debian and Fedora package versions are supported by their
packagers. We look at issues on those versions only when they
reproduce on the latest release.

## Backports

We do not backport to older lines. Security advisories name the fixed
release and the commit, so packagers can backport to the versions
they ship.

## For distro packagers

- Versions only go up. We never reuse or lower one.
- Source tags are immutable and signed.
- Release notes list changes to the bundled Electron or Node versions
  and to build dependencies.
- A format-changing release has a release candidate at least one week
  before, and we notify packagers directly.

## Deprecation

A feature is deprecated in a MINOR release with an in-app notice that
names the replacement and a changelog entry. It is removed no earlier
than two releases and three months later, and only in a MAJOR. Read
support for old project formats is never deprecated.

## Known past breaks

3.6.0 changed the project file format in a minor release. Users on 3.5
could not open files saved by 3.6. The change stays, because reverting
would break users who already saved in the new format. Rules 3-5 of
"Project file format" exist so it does not happen again.

## Who can cut a release

At least two of the three developers can publish. Two people hold the
macOS notarization and Windows signing credentials and the update-feed
access. If neither is available, no release ships until one is.

## Changes to this policy

Announced in the changelog one release before they apply.
````

Changelog header line:

```markdown
This project uses Semantic Versioning for the app and a separate project file format version. See [RELEASES.md](RELEASES.md) for what each number promises.
```

## 5. Check against the skill's five conditions

1. Every template section is filled. I added one section, "For distro packagers".
2. Every line has an end rule.
3. The capacity arithmetic fits about 4 h per month, but your real budget is unconfirmed.
4. The exclusions list is non-empty, and the runtime section names the metadata fields.
5. A release-time check exists, in rule 9. Add a check that the tag, the app manifest version and the changelog entry agree.

## 6. Open items

- Confirm your monthly release-hours budget.
- Confirm the two credential holders.
- Check whether 3.8.2 has the newer-file guard. If not, ship it before any format change. It does not help 3.5 users today.
- Confirm that you can staff "Save a copy for the previous major" for 12 months. Drop rule 7 if you can't.
- Decide on a patch release that exports in the 3.5 format, so the 3.6 casualties can open their colleagues' files. That's a product fix, not policy.

**Next:** reply "SemVer" or "CalVer", then I'll fix the draft, run `/caveman-compress`, and `npx prettier --write` on the file.