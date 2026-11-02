# brinepool: supported versions and release policy

**Draft for `SECURITY.md` and `docs/SUPPORT.md`. Review the items marked ⚠️ before it goes to the customer.**

I inferred a few rules from what you told me and could not verify them against your repo. Each is marked ⚠️ in the text and listed again at the end.

---

## 1. Versioning scheme

brinepool uses `0.MINOR.PATCH` and has not reached 1.0. The current release is **0.31.4**.

| Bump | What it contains |
|---|---|
| **PATCH** (0.31.4 → 0.31.5) | Bug fixes and security fixes. No intended change to documented behavior. |
| **MINOR** (0.31.x → 0.32.0) | New features and any breaking change. |

Before 1.0, a minor release can break compatibility. Pin to a minor version (`~> 0.31.4`) if you cannot absorb that. A pessimistic pin on the patch level only accepts fixes.

## 2. What counts as a breaking change

These ship only in a minor release and are listed under "Breaking" in the changelog:

- Removing or renaming a public option, method, or class.
- Changing the default value of an option (for example, the default retry count).
- Raising the minimum supported Ruby version.

Anything not documented in the README or API docs is internal and can change in any release.

## 3. Deprecation process

1. A feature is marked deprecated in a minor release. It emits a runtime warning and a changelog entry.
2. It is removed in the next minor release at the earliest. One release of warning is the minimum.
3. Changes to defaults get a changelog entry, but there is no runtime warning period.

Examples:

- **0.29:** removed the deprecated `legacy_signer` option after one release of warning.
- **0.30:** changed the default retry count from 3 to 5. A changed default can alter request volume and cost. If you depend on a specific value, set it explicitly instead of relying on the default.

## 4. Supported versions

| Version | Status | Receives |
|---|---|---|
| Latest minor (0.31.x) | ✅ Supported | Bug fixes and security fixes |
| Older minors (≤ 0.30.x) | ❌ Unsupported | Nothing. Upgrade to the latest minor. |

⚠️ This assumes you only patch the latest minor. If you have backported a fix to an older minor, add a row.

Fixes are released as a new patch version on the latest minor. There is no separate long-term-support line. The maintainers have about 5 hours a month in total, so backporting is out of scope.

## 5. Supported Ruby versions

brinepool supports **Ruby 3.1 and later**, as declared in `required_ruby_version` in the gemspec. CI runs against ⚠️ *[list the exact versions CI runs]*.

- Ruby 3.1 and 3.2 are past upstream end-of-life. brinepool still runs on them, but Ruby itself no longer receives security fixes there. Customers with their own security requirements should run a Ruby version that upstream still supports.
- Dropping a Ruby version is a breaking change (section 2). It ships in a minor release and is announced in the changelog.

## 6. Reporting a vulnerability

⚠️ *[Insert the real channel: GitHub private vulnerability reporting or a security email. Do not publish a channel you do not monitor.]*

Please do not open a public issue for a vulnerability.

- **Acknowledgement:** within 5 business days.
- **Fix:** best effort, no fixed deadline. The project is maintained by two people on a volunteer basis. Fixes ship as a patch release on the latest minor, with a changelog entry and, where applicable, a GitHub security advisory.
- **Disclosure:** coordinated with the reporter. Details are published once a fixed release is available.

## 7. Maintenance and releases

- brinepool has two maintainers. Combined capacity is roughly 5 hours a month.
- One maintainer holds RubyGems push rights. ⚠️ *[State here, or leave out, whether you have MFA enforced on the account.]*
- Releases happen when there is something to ship, not on a fixed schedule.

---

## Open items before this goes to the customer

1. **Support window (section 4).** I assumed latest-minor-only. If that is not what you do, the table is wrong.
2. **Security channel and timings (section 6).** I made up the 5-business-day acknowledgement. Pick a number you can keep with 5 hours a month. A missed promise reads worse in a review than a long one.
3. **CI matrix (section 5).** I don't know which Rubies you test against.
4. **Single push-rights holder.** A security reviewer will likely flag a single holder of push rights as a bus-factor risk. I stated it plainly instead of hiding it. If you can, add a second owner on RubyGems (they don't need to be a committer). That changes one sentence in section 7 and answers the question before it is asked.
5. **Default changes.** The 0.30 retry change had no warning period. The policy states that honestly. If you want to adopt a "warn before changing a default" rule, that is a new commitment and not documentation. Say so and I'll add it as a separate line.
6. **Changelog.** The policy promises "Breaking" labels in the changelog. Check that `CHANGELOG.md` actually uses them for 0.29 and 0.30. If it doesn't, add them before sending, since the reviewer may read it.