**Action:** commit the SECURITY.md below, then enable private reporting and make a second person able to receive reports (checklist after the file). About 40 minutes in total.

## 4 of your 5 asks changed

| You asked | Shipped | Why |
|---|---|---|
| Respond within 24 hours | Acknowledge within 5 business days, triage decision within 14 calendar days | 3 volunteers at 3–4 hours each can't keep 24 hours through one holiday. A missed published target costs more trust than a modest one you keep. An adopter's security team reads a kept 5 days better than a broken 24 hours. |
| security@ferrokv.dev and private reporting | Private reporting only | Two equal channels split reports, and reporters on GitHub can bypass the file anyway. Nobody on your team wants to own an inbox. Add a labelled fallback only if two people will read the alias. |
| $500 bounty | No bounty, stated in the file | A bounty attracts low-quality and machine-generated volume, and you have no funded triage hours. curl ended its bounty in January 2026 after this exact effect. Stating "no bounty" also removes payment negotiation. |
| Copied safe-harbor section | Kept, rewritten, and gated | Individual maintainers can waive only their own claims. A copied section from a big project usually carries company-legal wording you can't back. Ship it only if all three maintainers agree to it. |

The 90-day disclosure window is the skill's default for volunteers, and I kept it.

## SECURITY.md

Replace the three `<...>` placeholders and `<owner>` before committing.

```markdown
# Security Policy

## Supported versions

| Module | Version | Security fixes |
|---|---|---|
| `github.com/<owner>/ferrokv/v2` | latest minor | Yes |
| `github.com/<owner>/ferrokv` (v1) | <v1 end date, or "none"> | <Until that date / No - upgrade to v2> |
| Older releases | any | No - upgrade |

## Reporting a vulnerability

Report privately through GitHub:
<https://github.com/<owner>/ferrokv/security/advisories/new>
(the "Report a vulnerability" button on the repository's Security tab).

Do not open public issues, pull requests or discussions for security problems.

Please include:

- the affected version and module path (`ferrokv` or `ferrokv/v2`),
- a minimal reproducible proof of concept against a released version,
- the impact you observed,
- any suggested fix.

If you used AI tools to find or write up the issue, say so and confirm you verified the result yourself. Reports without a reproducible proof of concept may be closed.

## What to expect

ferrokv is maintained by three volunteers.

- Acknowledgement: within 5 business days.
- Triage decision (accepted, not a vulnerability, or more information needed): within 14 calendar days.
- Coordinated disclosure: we aim to publish a fix and advisory within 90 calendar days of the report, and we agree the date with you.
- We may pause intake during holidays or other announced periods. Pauses are announced in this file.

## Scope

In scope: the exported API of the supported modules above, used as documented.

Out of scope:

- inputs or files the documentation declares trusted or invalid,
- panics on arguments the documentation forbids (for example nil values),
- resource use proportional to caller-supplied sizes, unless the documentation says the API is safe for untrusted input,
- examples, tests, benchmarks and internal tooling,
- vulnerabilities in dependencies that our code does not reach,
- unsupported versions,
- reports from automated tools without a verified proof of concept.

## Advisories and identifiers

We publish security advisories on this repository's GitHub advisory page. We request CVE IDs through GitHub's CNA and score severity with CVSS 3.1 base metrics.

## Credit

We credit reporters in the advisory unless you ask otherwise.

ferrokv does not run a bug bounty and does not pay for reports.

## Safe harbor

The maintainers will not pursue legal action against good-faith security research that follows this policy, avoids privacy violations and service disruption, and gives us the agreed time before public disclosure.

This covers only claims the maintainers hold. It cannot authorize testing of systems run by users or third parties.
```

Delete the whole Safe harbor section if any of the three maintainers declines it. Nothing else in the file depends on it.

## GitHub settings

Owner is whoever has the role named in each step.

1. **Transfer the repo to a GitHub organization.** Settings → General → Danger Zone → Transfer. Old URLs and Go import redirects keep working. Do this first: a personal-account repo has only one person who can manage advisories, so you would have one responder. (Go module paths contain the owner, so check how `go get` and pkg.go.dev resolve the new path before announcing the move.)
2. **Give the second maintainer the role that receives private reports.** In the org, give them admin on the repo, or the org's Security manager role. Write access receives nothing. Add the third maintainer the same way if you want three responders.
3. **Enable private reporting.** Repo → Settings → Code security → Private vulnerability reporting → Enable.
4. **Each responder watches security alerts.** Repo → Watch → Custom → Security alerts.
5. **Confirm SECURITY.md appears.** Repo → Security tab → Policy.
6. **Record the scoring convention.** Use a CVSS 3.1 base vector on every advisory.

## Verify before sending to the adopter

All four must pass:

1. A second GitHub account files a test report. Both responders get the notification within one business day.
2. The channel in SECURITY.md matches the enabled setting.
3. The supported-versions table matches the tags that actually receive fixes.
4. A maintainer who did not write the file finds and follows the policy without asking you.

## Open questions (three placeholders in the file)

- **v1 support:** does `ferrokv` (v1) still get security fixes, and until when? Recommendation: 6 months after v2's release, or "none" if that date has passed.
- **Safe harbor:** do all three maintainers agree to it?
- **Commercial use:** is ferrokv monetised or backed by a company? Individual volunteers on a non-monetised project are outside the EU Cyber Resilience Act. If that changes, re-check it with a lawyer.

Expect the adopter, if they sell into the EU, to be a manufacturer under the Act, with 24-hour clocks on actively exploited bugs since 11 September 2026. A fast, named private channel is what they look for. Machine-readable advisories with exact version ranges (one range per module path) let them meet their own duties without contacting you.

**Next:** do step 1 (org transfer), then ask the second maintainer to accept the admin invite.