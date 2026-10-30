# SECURITY.md template and sizing

Read this when writing or fixing a project's security policy.

## Sizing rules

- **One primary channel.** Two equal channels split reports and nobody watches the second. A fallback is fine when labelled as a fallback.
- **Business days, sized to the worst month.** Promise what the responders can keep during a holiday or a release crunch.
- **Supported versions per release line.** List the lines that actually receive backports. For ecosystems where a new major version is a separate package or module path (Go `/v2`), list each one.
- **Scope = the documented API used as documented.** The out-of-scope list is the cheapest defence against low-quality reports, and it is the text you cite when closing one.
- **Safe harbor only for what the maintainers control.** Individual maintainers can waive only their own claims. Ship the section only after every named maintainer agrees and, on a company-run project, after legal sign-off; otherwise delete it.
- **State "no bounty" when true.** It removes the payment negotiation before it starts.
- **Agree with the host settings.** On hosts with private reporting, reporters can bypass the file; a policy naming an email address while the setting is on sends reports two ways.

## Template

Replace every `<...>`. Delete sections that do not apply rather than leaving placeholders.

```markdown
# Security Policy

## Supported versions

| Version / module | Security fixes |
|---|---|
| <latest major, latest minor> | Yes |
| <previous major> | Until <date or "6 months after the next major"> |
| Older | No - upgrade |

## Reporting a vulnerability

Report privately through <the repository's "Report a vulnerability" button / URL>.
Do not open public issues, pull requests or discussions for security problems.
Fallback only if you cannot use that channel: <alias read by at least two maintainers>.

Please include: affected version, a minimal reproducible proof of concept
against a released version, the impact you observed, and any suggested fix.
If you used AI tools, say so and confirm you verified the result yourself.
Reports without a reproducible proof of concept may be closed.

## What to expect (<volunteer-maintained | maintained by <company>>)

- Acknowledgement: within <5> business days.
- Triage decision (accepted, not a vulnerability, or more information needed): within <14> calendar days.
- Coordinated disclosure: we aim to publish a fix and advisory within <90> calendar
  days of the report, and we agree the date with you.
- We may pause intake during <holidays / announced periods>; pauses are announced here.

## Scope

In scope: <the public API of the packages above, used as documented>.
Out of scope: <inputs the documentation declares trusted or invalid; resource
use proportional to caller-supplied sizes unless documented as safe for
untrusted input; examples, tests and internal tooling; vulnerabilities in
dependencies that our code does not reach; unsupported versions; reports from
automated tools without a verified proof of concept>.

## Advisories and identifiers

We publish security advisories <on the repository's advisory page>, request CVE
IDs through <CNA path>, and score severity with CVSS <version> base metrics.

## Credit

We credit reporters in the advisory unless you ask otherwise. <This project
does not run a bug bounty and does not pay for reports.>

## Safe harbor

The maintainers will not pursue legal action against good-faith security
research that follows this policy, avoids privacy violations and service
disruption, and gives us the agreed time before public disclosure. This covers
only claims the maintainers hold; it cannot authorize testing of systems run by
users or third parties.
```

## Worked example: three-maintainer library

Input: three volunteers, about 4 hours each in a bad month, two supported majors, hosted on a code host with private reporting, no bounty, no company behind it.

Output decisions:

- Channel: private reporting only; no email fallback, because nobody wants to own an inbox.
- Targets: acknowledgement 5 business days, triage 14 days, disclosure default 90 days. A 48-hour acknowledgement was rejected: one maintainer's holiday would break it.
- Supported: current major fully; previous major for 6 months after each new major, then none.
- Scope: adds "panics on nil arguments the documentation forbids", which accounted for most closed reports last year.
- Identifiers: code-host CNA; revisit if a third-party CVE appears.

```
✓ Good - "Acknowledgement within 5 business days."   (kept during a holiday)
✗ Bad  - "We respond to all reports within 24 hours." (broken by the first absence)

✓ Good - one channel named, matching the enabled setting
✗ Bad  - an email address in the file while private reporting is also on, read by nobody
```
