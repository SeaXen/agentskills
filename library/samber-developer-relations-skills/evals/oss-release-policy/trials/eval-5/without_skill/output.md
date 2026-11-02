Recommendation: keep MAJOR.MINOR.PATCH numbering and drop the "semver as API contract" idea. Version the project file format separately, with its own number. The file format caused your 3.5/3.6 incident, and no app version scheme would have prevented it.

I haven't seen the 3.6 change itself. Where the draft depends on what it was, I've marked an assumption.

---

# Ferncast Versioning and Compatibility Policy

Status: draft for team review. Applies from the next release after 3.8.2.

## 1. Why this exists

- Ferncast is an application. Nobody imports it, so semver's API-compatibility promise has no consumer.
- Users, colleagues who share files, and the Debian and Fedora packagers need to answer two questions from a version:
  1. Is this newer than mine?
  2. Can I still open files from, and send files to, the people I work with?
- The app version answers question 1. The project-file format version answers question 2.

## 2. App version: `MAJOR.MINOR.PATCH`

We keep the numeric shape, but define the parts by what users experience, not by API.

| Part | Bump when | Cadence |
|---|---|---|
| MAJOR | A breaking project-file format change (§3.4), or a redesign that changes how users work | Rare, planned at least 2 cycles ahead |
| MINOR | The normal scheduled release: features, fixes, additive file-format changes | Every 6-8 weeks |
| PATCH | A fix-only hotfix. No features, no format change | As needed |

Rules:
- Pre-releases are `3.9.0-beta.N` and `3.9.0-rc.N`. This is valid semver, so the Electron auto-updater can order versions and run beta/stable channels.
- Git tags are `vMAJOR.MINOR.PATCH`, signed. Packagers build from the tag tarball.
- The release date is never encoded in the version. The cadence is a target, not a promise. A slipped release keeps its number.
- We don't claim "strict semver". The README and release notes say: "Version numbers follow MAJOR.MINOR.PATCH. They describe the app, not an API."

Why not date versions (e.g. `2026.10.0`):
- Their one benefit, "how old is this build", is already in the About dialog and the changelog.
- They would not have prevented the 3.6 incident.
- Switching now costs an announcement, a packager heads-up, and an update-channel check, in exchange for a label change.
- Revisit only if we move to releases more often than every 4 weeks.

## 3. Project file format

### 3.1 Two numbers in every file

Every project file stores:
- `formatVersion`: an integer. It changes only when the on-disk structure changes in a way defined in §3.3.
- `minReaderFormat`: the lowest `formatVersion` a reader must understand to open the file safely.

The About dialog and `--version` print both the app version and the highest format version the app can read and write.

### 3.2 Guarantees

1. **Backward:** Every Ferncast release opens every project file from any earlier 3.x release. Dropping this needs a MAJOR bump and a published migration path.
2. **Never silently altered:** Opening a file never rewrites it on disk. When a save would upgrade the format, the app asks first and keeps a `<name>.pre-<version>.bak` copy.
3. **Forward, graceful failure:** A release that meets a file with `minReaderFormat` above what it supports must refuse to open it and say so plainly:
   - what is wrong ("This project was saved by Ferncast 3.9 and needs a newer version"),
   - what to do (update, or ask the sender to export a compatible copy).
   It must never show a generic "corrupt file" error and never open the file partially.
4. **Unknown fields survive:** Readers keep fields they don't recognise and write them back unchanged on save. An older version editing a newer file must not strip data.

### 3.3 Change classes

| Class | Examples | `formatVersion` | Allowed in |
|---|---|---|---|
| Additive | New optional field, new optional track type. Older readers can ignore it and still open the file correctly | Unchanged | MINOR |
| Compatible bump | Structural change old readers can't use, but the app can also write the previous format | +1, `minReaderFormat` unchanged only if old readers still load the file correctly | MINOR, only with "Save compatible with previous version" (§3.5) |
| Breaking | Old readers can't open or would misread the file | +1, `minReaderFormat` raised | MAJOR only |

### 3.4 The rule that would have caught 3.6

A MINOR release may not raise `minReaderFormat`. Anything that does ships as a new MAJOR, announced at least one release cycle earlier in a beta.

Assumption: the 3.6 change was a breaking change shipped in a minor with no warning in 3.5. If it was additive but 3.5 was strict about unknown fields, the gap is §3.2 rule 4 instead. Under this policy, rule 4 is a release requirement, and the 3.6 and 3.7 readers must be checked against it.

### 3.5 Sharing across versions

Because colleagues run different versions, and Linux distro builds lag behind auto-updated Mac and Windows builds:
- **Save compatible with previous version:** every MAJOR release offers this for the whole next MAJOR line (e.g. 4.x can write 3.x-readable files). Features the older format can't represent are listed in a confirmation dialog before saving.
- A plain "Save" always writes the current format.

### 3.6 Testing (release gate)

- Keep a fixtures folder in the repo with one real project file per release since 3.0, plus one file using every feature.
- CI opens each fixture in the current build, saves it, and re-opens it. A failure blocks the release.
- CI opens a synthetic file with an unknown field and a raised `minReaderFormat`. It checks that the field is preserved and that the refusal message appears.
- Every PR that touches serialisation answers one question in its description: "Which change class from §3.3 is this?"

## 4. Release process (fits the half-day budget)

1. Freeze: one week before the target date, only fixes merge.
2. Run the §3.6 fixture suite and the usual build checks.
3. Cut `-rc.N`. Publish it to the beta channel and email the packagers.
4. Release notes must contain a **File format** section, even if it just says "No change."
5. Tag, publish, and let the auto-updater roll out. Roll out in stages (e.g. 10%, then 100% after 48 hours).
6. Hotfix PATCH releases skip steps 1 and 3 but still run step 2.

Budget: this adds about an hour to the half-day release, mostly the fixture suite, which should be automated.

## 5. Linux and the packagers

Debian and Fedora packagers don't auto-update, so their users stay on old versions longer. That is where cross-version file problems will hit hardest.
- Send the `-rc` announcement to the packagers at least 7 days before a MINOR and 21 days before a MAJOR.
- State the `formatVersion` change (or "none") in the announcement.
- Keep a `PACKAGING.md` with build steps, bundled dependency versions, and the point of contact for security fixes.
- Don't ask packagers to adopt our update cadence. Support files from their versions per §3.2.

## 6. Decisions we need from you

1. **3.5 users today:** A 3.5.x patch that detects newer files and shows the §3.2 rule 3 message would fix the symptom. Does 3.5 still get updates, and are you willing to ship it?
2. **What exactly changed in 3.6?** I need to place it in §3.3 to confirm rules 2 and 4 are enough.
3. **Backward-read window:** I wrote "all 3.x" in §3.2 rule 1. Do you want a shorter window, e.g. current and previous MAJOR?
4. **Packager contacts:** I need names for the §5 announcement list.

Next step: answer question 2 with the 3.6 commit or changelog entry. Every other section depends on it.