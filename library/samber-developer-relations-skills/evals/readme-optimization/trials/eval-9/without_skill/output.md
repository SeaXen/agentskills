Two things are actually being evaluated here: whether LedgerLink is technically trustworthy, and whether its governance can be trusted to stay that way. Banks and an insurer doing vendor security review will check both independently, and a foundation donation that isn't real yet won't help with either this quarter — so the README needs to lead with disclosure, not with the donation story.

Below is the actual content to add. It assumes you create `SECURITY.md` and `MAINTAINERS.md` alongside it — the README should not describe policies that live nowhere.

---

## Add near the top of README.md (badges)

```markdown
[![CI](https://github.com/brightmoor/ledgerlink/actions/workflows/ci.yml/badge.svg)](https://github.com/brightmoor/ledgerlink/actions/workflows/ci.yml)
[![CodeQL](https://github.com/brightmoor/ledgerlink/actions/workflows/codeql.yml/badge.svg)](https://github.com/brightmoor/ledgerlink/actions/workflows/codeql.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/brightmoor/ledgerlink/badge)](https://scorecard.dev/viewer/?uri=github.com/brightmoor/ledgerlink)
[![Go Report Card](https://goreportcard.com/badge/github.com/brightmoor/ledgerlink)](https://goreportcard.com/report/github.com/brightmoor/ledgerlink)
[![License](https://img.shields.io/github/license/brightmoor/ledgerlink)](./LICENSE)
```

Only include a badge for something that is actually wired up in CI today. An unearned badge is worse than no badge to a security reviewer — it reads as a false claim the moment they click through.

## New section: Security

```markdown
## Security

LedgerLink is used as core accounting infrastructure by financial institutions. We treat vulnerability handling accordingly.

- **Report privately** via [GitHub Security Advisories](https://github.com/brightmoor/ledgerlink/security/advisories/new) or **security@brightmoor.io** (PGP: [security.asc](./security.asc)). Do not file public issues for suspected vulnerabilities.
- **Response time**: acknowledged within 5 business days; fix or mitigation targeted within 90 days of confirmation, coordinated with the reporter before disclosure.
- **Supported versions**: current and previous minor release. Full table in [SECURITY.md](./SECURITY.md).
- **Static analysis**: every PR runs `go vet`, `staticcheck`, `gosec`, and CodeQL — results are public in the Actions tab.
- **Supply chain**: releases are built with GoReleaser, signed with [Sigstore/cosign](https://www.sigstore.dev/), and ship a CycloneDX SBOM. Verify with `cosign verify-blob ...` — instructions in [SECURITY.md](./SECURITY.md).
- **Independent audit**: none yet. [Replace this line the day one lands — do not claim an audit before it exists.]
```

That last line is deliberate. If a bank's security team asks "has this been audited" and the answer is no, the README should already say no. Getting caught overclaiming during diligence does more damage than the honest gap ever would.

## New section: Governance & maintainers

```markdown
## Governance & maintainers

LedgerLink has four maintainers, all currently employed by Brightmoor, the project's original author and sponsor. We state this plainly because maintainer concentration is a legitimate diligence question for financial infrastructure, and hiding it would not survive a real audit anyway.

- **Review requirement**: two maintainer approvals required to merge; no single maintainer can push directly to the ledger core.
- **Maintainer list**: kept current in [MAINTAINERS.md](./MAINTAINERS.md), including employer disclosure for each.
- **Governance transfer**: Brightmoor's board has approved moving project governance and the trademark to a vendor-neutral foundation. Target: [quarter/year]. Not yet complete — this section will be updated with the signed agreement and transfer date once it closes. Until then, Brightmoor is the accountable entity for security reports, licensing, and support.
- **Release cadence**: roughly monthly. See [CHANGELOG.md](./CHANGELOG.md).
```

Say "approved, targeting Q[X]," never "we're part of [Foundation]" or use a foundation's logo, until the transfer agreement is actually signed. A bank's legal/procurement team can and does check foundation membership rosters and trademark records; a premature claim is a diligence finding, not a credibility boost.

## New file: SECURITY.md

```markdown
# Security Policy

## Supported versions

| Version | Supported |
|---|---|
| Latest minor | ✅ |
| Previous minor | ✅ security fixes only |
| Older | ❌ |

Releases ship roughly monthly; a minor version stops receiving fixes once two newer minors have shipped.

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability.

Report privately through:
- [GitHub Security Advisories](https://github.com/brightmoor/ledgerlink/security/advisories/new) (preferred)
- security@brightmoor.io — PGP key: [security.asc](./security.asc)

Include affected version, reproduction steps, and impact.

## Process

1. Acknowledgment within 5 business days.
2. Severity assessment (CVSS) within 10 business days.
3. Fix targeted within 90 days of confirmation, or an agreed extended timeline for complex cases.
4. Coordinated disclosure and CVE assignment with the reporter.
5. Reporters credited in the advisory unless they request anonymity.

## Scope

In scope: the `ledgerlink` core module and official adapters in this repository.
Out of scope: third-party integrations, forks, and deployments the maintainers don't operate.

## Independent audit

None to date.
```

## Why this ordering, for this quarter specifically

- The Security and Governance sections are yours to ship this week — they don't depend on the foundation decision closing.
- The foundation donation is a good move, but it's a multi-month legal process; the README shouldn't imply it's done or imminent before it is. State it as an approved, in-progress goal with a target date — reviewers read that as more credible than silence, and it costs nothing if the timeline slips.
- Maintainer-employer concentration is the one fact you cannot write around. Disclosing it yourself, with the mitigating detail (two-approval merge rule), reads as an organization that understands its own risk profile — which is exactly what a bank or insurer's security team is trying to determine.
- Every claim above (SBOM, cosign signing, CodeQL, Scorecard) needs to actually be wired into CI before the badge or sentence goes in. If any of these aren't live yet, either stand them up first or write the README section for the ones that are and add the rest as they land — don't publish the aspirational version.