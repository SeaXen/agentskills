**Not good to go.** Tag first, publish second, and fix the five items below. About 30 minutes of edits, plus the time to cut the tags.

## Blockers

1. **Order is backwards.** Publishing Friday with the tag "over the weekend" leaves a public advisory pointing at a patched version that doesn't exist. Attackers get the details and users have nothing to install. Tag first, confirm the tag resolves, then publish.
2. **`Affected: < 2.3.4` leaves v1 out.** `github.com/pelmont/marrowq` (v1) is a different module path, and you said it's affected. Dependabot and `govulncheck` match per module path. Each module needs its own entry:
   - `github.com/pelmont/marrowq/v2`: `< 2.3.4`, patched in 2.3.4.
   - `github.com/pelmont/marrowq`: `<= 1.9.11`, patched in 1.9.12.
3. **`Workarounds: None` is probably wrong.** Callers can allowlist or validate the broker URL before `Dial()`. Operators can block egress to 169.254.169.254, or enforce IMDSv2 with hop limit 1. List these, because they protect people who can't upgrade today.
4. **A PoC gist in the references arms attackers on day zero.** Drop it for now. Link the fix commit, the release, and CWE-918 instead. Add the PoC 30 days or more after release. Also check the gist for internal hostnames or config before it ever goes public.
5. **The `retract` plan needs adjusting.**
   - A `retract` directive only takes effect once a newer version carrying it is published. Put it in the 2.3.4 `go.mod`, and in the 1.9.12 `go.mod` for v1.
   - Retract only the true affected range. Bisect for the first vulnerable version rather than assuming v2.0.0 or v1.0.0.
   - Retraction is not a security alert. It hides versions from `@latest`, but they stay installable. You still need the advisory.

## Decisions you need to make

- **Patch v1 or not?** I recommend a small 1.9.12 backport. Without it, v1 users have no fix except a major-version migration. If you won't patch it, the advisory must say so.
- **Severity.** "High" needs a CVSS vector and a rationale. Exploitability depends on whether the broker URL can come from untrusted input. Score it explicitly.
- **Publish day.** Not Friday at 6pm. Pick Tuesday to Thursday, when you're around to answer questions.
- **Reporter credit.** Confirm with the reporter that they want their handle credited.
- **Behavior change.** If the fix blocks private or link-local ranges, say so in the 2.3.4 notes. Many brokers legitimately live on private IPs.

## Steps

1. Decide whether to ship the v1 backport (1.9.12).
2. Bisect for the first affected version of each module.
3. Create the advisory as a **draft** (private). Use a temporary private fork if you want a private fix PR.
4. Merge the fix to a reviewed commit on `main`, and on the v1 branch for the backport. Add `retract` to each `go.mod`. Run the tests.
5. **Tag** `v2.3.4` (and `v1.9.12`) from those reviewed commits, not from your working branch. The Go proxy caches tags permanently, so a wrong tag can only be retracted.
6. Verify each tag resolves: `GOPROXY=https://proxy.golang.org go list -m github.com/pelmont/marrowq/v2@v2.3.4`
7. **Publish** the advisory and request a CVE through GitHub.
8. Open a report with `golang/vulndb` so `govulncheck` flags it. GitHub publication doesn't guarantee that.
9. Add the PoC reference after the grace period.

## Corrected advisory draft

**Title:** SSRF via unvalidated broker URL in `Dial()` and `DialContext()`

**Affected:**
- `github.com/pelmont/marrowq/v2`: `< 2.3.4`
- `github.com/pelmont/marrowq`: `<= 1.9.11`
- 0.x is end of life, was not assessed, and will not be patched. Treat it as vulnerable.

**Patched:**
- `github.com/pelmont/marrowq/v2`: 2.3.4
- `github.com/pelmont/marrowq`: 1.9.12 *(or "none", if you decide not to backport)*

**Severity:** High, with the CVSS vector you compute, plus a note that exploitation requires an attacker-influenced broker URL. This is CWE-918.

**Description:** `Dial()` and `DialContext()` connect to the supplied broker URL without validating the host. If an application passes attacker-influenced input as the URL, the client can be made to connect to internal services, including cloud instance metadata endpoints.

**Workarounds:**
- Upgrade.
- Until you can upgrade, validate or allowlist the broker URL before calling `Dial()` or `DialContext()`.
- Block egress to link-local addresses (169.254.0.0/16).
- Enforce IMDSv2 with a hop limit of 1.

**References:** fix commit, release notes, CWE-918. PoC to be added later.

**Credits:** reporter's GitHub handle, once they confirm.

Next: tell me whether you'll ship the v1 backport, and I'll draft the `retract` blocks for both `go.mod` files.