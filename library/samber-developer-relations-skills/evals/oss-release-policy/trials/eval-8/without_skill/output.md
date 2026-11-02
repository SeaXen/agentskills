# Pellbrook Versioning Policy

**Status:** Draft v0.1, 2026-10-23
**Owner:** Platform / API team (name to confirm)

## 0. Decisions needed before adoption

Two requirements conflict. The policy below resolves them in a specific way, so please confirm or overrule the resolution.

1. **"SDKs always carry the same version as the API" cannot hold once the API uses dated versions.**
   - A dated version like `2026-11-15` is not a semver string.
   - SDKs also need patch releases (bug fixes, typos, retries) that must not create new API versions.
   - **Resolution used here:**
     - The three SDKs share one version number with each other (lockstep).
     - Each SDK release pins exactly one API date.
     - A published compatibility table maps SDK version to API version.
   - If you must keep literal equality, the API would have to be semver-versioned, which defeats the move to dated versions.
2. **The webhook library is independent.** It follows its own semver and never tracks the API version (see §4).

## 1. Scope and principles

- Treat every published version identifier as a contract.
- Never break a pinned consumer without a published sunset date.
- Version each artifact by what it promises, not by what ships beside it.

| Artifact | Scheme | Tracks API? |
|---|---|---|
| Hosted REST API | Dated (`YYYY-MM-DD`) | n/a |
| SDKs (node, python, ruby) | Semver, lockstep across the three | Pins one API date per release |
| Webhook verification library (npm, OSS) | Semver, independent | No |
| Renovate config (internal) | Unversioned, reviewed by PR | No |

## 2. Hosted REST API

### 2.1 Scheme

- Name versions by release date: `2026-11-15`.
- Today's `/v2` becomes the baseline. Name it by the date it is frozen (assign this date at cutover).
- Send the version in a request header, `Pellbrook-Version: 2026-11-15`. Do not put it in the URL.
- Keep `/v2` URLs working as an alias for the baseline version for the whole deprecation window.

### 2.2 Account pinning

- Pin each account to the version of its first API request.
- A request header overrides the pin for that request only.
- Upgrade an account's pin only on explicit action (dashboard or API), never automatically.
- Provide a test-mode upgrade path, so integrators can try a new version before switching live traffic.

### 2.3 Breaking and non-breaking changes

Non-breaking changes ship to all versions with no new date:

- New endpoints
- New optional request parameters
- New response fields
- New enum values on output-only fields (document that clients must tolerate unknown values)
- New webhook event types
- Performance and bug fixes

Breaking changes ship only under a new dated version:

- Removing or renaming a field, endpoint, or enum value
- Changing a field's type, format, or meaning
- Making an optional parameter required
- Changing default behavior, error codes, or status codes
- Changing authentication or idempotency semantics
- Changing pagination or rate-limit behavior in a way that breaks clients

When unsure, treat the change as breaking.

### 2.4 Cadence

- Release at most one breaking version per quarter. Batch breaking changes.
- Announce at least 30 days before the version becomes the default for new accounts.
- Each version needs a changelog entry and a migration guide listing every breaking change, a detection signal, and before/after code.

### 2.5 Deprecation and sunset

1. Mark the old version deprecated in docs and in a `Pellbrook-Deprecation` response header on affected requests.
2. Email account owners with API traffic on that version.
3. Keep a version supported for at least 24 months after the next version ships. *(Placeholder: confirm. Payments integrators move slowly.)*
4. Publish the sunset date at deprecation time and never move it earlier.
5. Before sunset, send reminders at 90, 30, and 7 days.
6. After sunset, return a documented error (not silent behavior changes).

Security fixes can override this timeline. If a fix needs a breaking change, apply it to all versions and give the longest notice possible.

## 3. Official SDKs (node, python, ruby)

### 3.1 Scheme

- Use semver `MAJOR.MINOR.PATCH`.
- All three SDKs publish the **same version number** at every release, even when a language had no change. This keeps support answers simple ("SDK 4.2.0").
- Each SDK release pins one API date as its default `Pellbrook-Version`. The SDK sends this header on every request.

### 3.2 Bump rules

| Change | Bump |
|---|---|
| Pinned API date changes | MAJOR |
| Breaking change to SDK public surface (renamed method, removed option, dropped runtime version) | MAJOR |
| New endpoint or new optional parameter, same pinned API date | MINOR |
| Bug fix, docs, internal refactor, dependency update | PATCH |

- A new API date never ships in a MINOR or PATCH release. Users upgrade the API version only by upgrading the SDK major.
- Allow an explicit override option so users can set `apiVersion` to another supported date. The SDK types describe only its pinned version, so this is unsupported but permitted.

### 3.3 Release process

1. Tag one version across the three repos (or packages in a monorepo).
2. Run each SDK's tests against the pinned API version.
3. Publish all three together. If one fails to publish, hold the release and do not announce.
4. Update the compatibility table in the docs:

| SDK version | Pinned API version | Status |
|---|---|---|
| 3.x | `/v2` baseline date | Supported until (sunset date) |
| 4.x | (next date) | Current |

### 3.4 Runtime support

- Support the language versions that are not end-of-life when the SDK major ships.
- Dropping a runtime version is a MAJOR bump.

### 3.5 Maintenance

- Backport security fixes to every SDK major whose pinned API version is still supported.
- Backport bug fixes only to the latest major, plus one prior major for six months. *(Placeholder: confirm.)*
- Publish the SDK sunset on the same date as its pinned API version.

## 4. Webhook signature verification library (npm, open source)

### 4.1 Independence

- Version this library with plain semver, starting from the current **1.4.0**.
- Its version has no relation to the API version, and the compatibility table in §3.3 does not list it.
- The library verifies signatures. It does not parse or interpret event payloads, so API versioning does not affect it.
- Keep it that way. If a feature needs payload knowledge, build it in the SDKs instead.

### 4.2 Bump rules

| Change | Bump |
|---|---|
| Change to signature scheme handling that rejects previously accepted input, removed export, dropped Node version | MAJOR |
| New option, new export, new supported header format | MINOR |
| Bug fix, docs, dependency update | PATCH |

- Tighten verification (for example, a stricter timestamp tolerance default) only in a MAJOR, unless it fixes a security flaw. Document security-driven exceptions in the release notes.
- Treat an incorrect accept (a forged signature passing) as a security fix. Handle it under the security process, not the normal release train.

### 4.3 Hygiene

- Keep runtime dependencies at zero where possible. Every dependency is a supply-chain risk for a security library.
- Publish with npm provenance enabled, from CI only.
- Keep a `CHANGELOG.md` and GitHub releases in sync.
- Keep this policy's internal sections (including §5) out of the public repo. Link only to public documentation.

## 5. Renovate configuration (internal)

### 5.1 Principles

- Auto-merge only what CI can prove safe.
- Never auto-merge a major version.
- Wait before merging new releases, so a yanked or compromised release does not land (`minimumReleaseAge`).
- Pin CI actions by digest.
- Keep the config in an internal repository only. Do not publish it or copy it into public repos.

### 5.2 Policy

| Update | Dev dependencies | Runtime dependencies |
|---|---|---|
| Patch | Auto-merge | Auto-merge after 3 days |
| Minor | Auto-merge | Auto-merge after 7 days *(placeholder)* |
| Major | Manual review | Manual review |
| Security advisory | Immediate PR, human review | Immediate PR, human review |

Payment-critical packages (crypto, HTTP clients, database drivers, anything on the card or ledger path) never auto-merge at any level. List them in the `payments-critical` rule below.

### 5.3 Config

Use `renovate.json5` so comments are allowed.

```json5
{
  $schema: "https://docs.renovatebot.com/renovate-schema.json",
  extends: [
    "config:recommended",
    "helpers:pinGitHubActionDigests",
    ":semanticCommits",
  ],
  // Every update waits for CI; automerge never bypasses required checks.
  automerge: false,
  automergeType: "pr",
  platformAutomerge: true,
  // Gives the registry time to yank bad or compromised releases.
  minimumReleaseAge: "3 days",
  // Caps review load; raise only if the queue stays empty.
  prConcurrentLimit: 10,
  schedule: ["before 6am on weekdays"],
  timezone: "Europe/Paris", // placeholder: set to team timezone
  labels: ["dependencies"],
  packageRules: [
    {
      description: "Patch updates auto-merge",
      matchUpdateTypes: ["patch"],
      automerge: true,
    },
    {
      description: "Dev dependency minors auto-merge",
      matchDepTypes: ["devDependencies"],
      matchUpdateTypes: ["minor"],
      automerge: true,
    },
    {
      description: "Runtime minors auto-merge after a longer soak",
      matchDepTypes: ["dependencies"],
      matchUpdateTypes: ["minor"],
      minimumReleaseAge: "7 days",
      automerge: true,
    },
    {
      description: "Majors always need a human",
      matchUpdateTypes: ["major"],
      automerge: false,
      labels: ["dependencies", "major"],
    },
    {
      description: "Payments-critical packages never auto-merge",
      matchPackageNames: [
        // Fill in: crypto, HTTP client, DB driver, ledger libraries.
      ],
      automerge: false,
      labels: ["dependencies", "payments-critical"],
      reviewers: ["team:payments-platform"], // placeholder
    },
    {
      description: "Pin GitHub Actions by digest, review all bumps",
      matchManagers: ["github-actions"],
      automerge: false,
    },
  ],
  vulnerabilityAlerts: {
    labels: ["security"],
    automerge: false,
    minimumReleaseAge: null, // security fixes skip the soak period
    schedule: ["at any time"],
  },
}
```

Verify the config with `npx --yes --package renovate -- renovate-config-validator` before merging changes to it.

### 5.4 Requirements outside the config

- Require passing CI and at least the repo's normal required checks before any merge.
- Enable branch protection so auto-merge cannot skip required checks.
- Review the config quarterly. Track auto-merged PRs that later caused incidents, and tighten rules when one occurs.

### 5.5 Interaction with Pellbrook's own packages

- Internal services consume the SDKs through Renovate like any dependency.
- An SDK minor or patch auto-merges under the rules above.
- An SDK major changes the pinned API date, so it always needs human review and a read of the migration guide.
- The webhook library follows the same rules as any dependency: patch and minor auto-merge, major goes to a human.

## 6. Ownership and changes to this policy

- Changes to this document go through PR review by the API owner and one SDK maintainer.
- Version-impacting decisions (new API date, SDK major) need a written note linking to the migration guide.
- Revisit the lockstep rule in §3.1 after the first two dated releases, using the real support cost as evidence.

---

# `@pellbrook/…` webhook verification library: 1.5.0 release notes (draft)

I don't know what changed since 1.4.0, and I did not look at the repo. I have not invented features. Replace each bracketed item with the real change, and delete the sections you don't need. Use 1.5.0 only if every change is backwards-compatible, per §4.2.

## 1.5.0 (2026-MM-DD)

This is a minor release. It's backwards-compatible, and upgrading requires no code changes.

### Added

- [New option, export, or supported header format. State what it does and give a 3-line usage example.]
- [Additional change, if any.]

### Fixed

- [Bug fixed. Describe the visible symptom, not the internals, and link the issue or PR.]

### Changed

- [Behavior that changed without breaking existing callers, such as improved error messages or updated types.]

### Security

- [Include this section only if relevant. If a verification bypass was fixed, follow the security disclosure process and publish an advisory instead of burying it here.]

### Upgrade

```sh
npm install @pellbrook/webhook-verify@1.5.0
```

[Replace with the real package name.] No migration steps are needed. Behavior for valid, correctly signed webhooks is unchanged.

### Compatibility

- Supported Node.js versions: [list, unchanged from 1.4.0 unless noted].
- Dependencies: [none added / list changes].
- This library is versioned independently of the Pellbrook API and SDKs. Any API version works with it.

### Checklist before publishing

1. Confirm no change rejects input that 1.4.0 accepted. If one does, make it 2.0.0.
2. Update `CHANGELOG.md` and create the GitHub release with this text.
3. Publish from CI with npm provenance.
4. Check the release notes for internal hostnames, paths, or customer names. The repo is public.