**I did not write the three-major, all-fixes version, because your own numbers say you can't deliver it.** Here is the math:

| Item | Hours/year |
|---|---|
| Budget (3 h × 12) | 36 |
| Normal releases (2/month × 1 h) | 24 |
| Left for backports | 12, or about 6 backports |
| Old 4.x line alone last year (9 patches × 2 h) | 18 |
| Two old lines at that rate (5.x and 4.x) | 36 |

The 3 security advisories alone cost 12 h if each hits both old lines (3 × 2 lines × 2 h). That is your entire backport budget with nothing left for bug fixes. If you want the original promise, you need about 5 h/month, not 3. The alternatives are to release monthly instead of twice a month, or to find more maintainer hours.

The text below promises only what 12 h/year can cover. Replace `YYYY-MM-DD` with the real dates once 6.0.0 ships.

---

## Supported versions

Brightwater supports the current major in full. It supports the previous major for a fixed period after the next major ships, and security fixes only.

| Version | Status | Receives | Support ends |
|---|---|---|---|
| 6.x | Current | New features, all bug fixes, security fixes | When 7.0.0 is released and its support window starts |
| 5.x | Maintenance | Security fixes, and regressions that break previously working code | 12 months after 6.0.0 (`YYYY-MM-DD`) |
| 4.x | Security only | Security fixes only | 3 months after 6.0.0 (`YYYY-MM-DD`) |
| 3.x and older | End of life | Nothing | Already ended |

- **Until 6.0.0 ships:** 5.x is current and 4.x is in maintenance. 5.3.1 is the latest 5.x release.
- **Support windows:** A new major starts a 12-month maintenance window for the previous major. The major before that gets 3 months of security-only support. We publish the end dates in the release notes of each new major.
- **No new features** are added to any version other than the current major.
- **Security fixes** follow the process in `SECURITY.md`. Report vulnerabilities privately, not in public issues.
- **Ended versions:** We publish no more releases for them, including security fixes. We do not delete them from npm. Advisories still list them as affected when we know they are.
- **Need longer support?** Contact us about sponsored backports (see below).

## Backports

A backport is a fix made on `main` and then applied to a maintenance branch (`5.x`, `4.x`). We fix on `main` first and backport second.

### What qualifies

| Fix type | 5.x | 4.x |
|---|---|---|
| Security vulnerability (any severity) | Yes | Yes, during its window |
| Regression that breaks code valid on that line | Yes | No |
| Data corruption or incorrect validation result (a schema accepts invalid input, or rejects valid input) | Yes, if the fix is a small, low-risk change | No |
| Other bug fixes | No | No |
| Performance, features, deprecations | No | No |

The maintainers decide whether a fix is low risk. A fix that needs a behavior change, a new option, or a large diff is not backported. In that case we document a workaround or point to the upgrade path.

### How it works

1. Fix the bug on `main` with a test.
2. Label the issue or PR `backport-5.x` and/or `backport-4.x` if it qualifies. We label security fixes ourselves.
3. Cherry-pick the fix onto the maintenance branch. Do not rewrite the fix for the old line unless it cannot apply cleanly.
4. Run CI on the maintenance branch. Publish a patch release to npm under the correct dist-tag so `latest` doesn't move (for example, `npm publish --tag v5-maintenance`).
5. Update the changelog and, for security fixes, publish the advisory with all fixed versions listed.

### Timing

- **Security fixes:** We aim to publish backports to all supported lines together, within 14 days of the fix landing on `main`. Critical issues are handled faster when possible.
- **Regressions and corruption fixes:** These are batched into a monthly maintenance release for 5.x. We don't cut a release for each one.
- **Capacity limit:** We reserve about 1 hour per month for backports. If a window has more qualifying fixes than we can ship, security fixes go first. The rest wait or are declined, and we say so on the issue.

### Community and sponsored backports

- **Pull requests welcome:** A PR against a maintenance branch that meets the table above can be reviewed and released without maintainer authoring time. Include a test and a link to the fix on `main`.
- **Longer support:** Organizations that need a line supported past its end date can sponsor it. Contact the maintainers for terms.

### Not covered

We do not backport fixes for bugs in your own code or in dependencies we don't control. If a dependency vulnerability affects a supported line, we backport the dependency bump when it is a patch-level change.

---

**Decisions for you:**
- **Window lengths:** 12 months for 5.x and 3 months for 4.x are my picks to fit about 6 backports/year. Longer windows need more hours.
- **Security SLA:** 14 days is a placeholder. Only keep it if you can actually hit it.
- **Release cadence:** Moving normal releases to monthly would free 12 h/year, enough to widen 4.x's window. Say if you want that version.