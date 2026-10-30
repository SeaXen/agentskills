# Identifiers, scoring and advisory content

Read this when choosing how to get a CVE, scoring severity, or filling the advisory.

Contents: CNA menu, scoring rules, advisory fields, version ranges, ecosystem databases, disputes.

## CNA menu

Order by efficiency for a small project on a code host: code-host CNA > foundation or ecosystem CNA > MITRE CNA of Last Resort > becoming your own CNA.

| Path | You do | You get | You owe |
|---|---|---|---|
| Code-host CNA (e.g. through the repository advisory) | Click "request CVE" on the draft advisory | CVE tied to the advisory; scanner alerts and ecosystem-database import after the host reviews it | Nothing ongoing; review from hours to weeks |
| Foundation or ecosystem CNA (Apache, Eclipse, Python, Linux kernel and others) | Follow the foundation's security process | Fast assignment inside the foundation | The foundation's process; the code-host CNA cannot assign where another CNA's scope covers you |
| MITRE CNA of Last Resort (cveform.mitre.org, "CVE ID Requests") | Fill the form with product, versions, evidence | A CVE when no other CNA covers the product | A queue that can run weeks; say so if a disclosure date is near |
| Become your own CNA | Apply through the CVE Program; follow the CNA Operational Rules | First right to assign, and first right to refuse | Rule compliance and record quality, permanently |

- Efficiency starves the last rung: high value, high standing cost. Promote it when third parties have already filed CVEs against the project, or when the project issues several CVEs a year. Becoming a CNA does not cover IDs another CNA assigned earlier.
- CNA Rules give "the CNA with the most appropriate scope" the first opportunity to assign, and also the first opportunity not to assign. Request as soon as a report is accepted: whoever assigns first writes the record.
- Hosts that are CNAs assign through their advisory or issue flow; hosts without one, or self-hosted forges, go to MITRE's form.
- The reporter or their employer already holds a CVE: use it, request no duplicate, and agree record content with the assigning CNA.
- A vulnerability that lives only in a dependency is the dependency's CVE, not yours - unless you ship that code inside your own artifact.
- No separate CVE for the same bug in an end-of-life line.

## Scoring rules

- Publish the full vector, never only a label. Give a CVSS 3.1 vector, which every consumer reads, and add a 4.0 vector where the host accepts one.
- Use base metrics only. Threat or temporal metrics make the score change over time and are not editable in every database.
- Score the reasonable worst-case integration, as FIRST's CVSS 3.1 User Guide directs for libraries: assume a reasonable integrator passes untrusted input wherever the API plausibly receives it, and score in that configuration. Whether the docs declare the input trusted is a scope or by-design decision (SKILL step 2), never a vector downgrade.
- Attack Complexity High (3.1) or Attack Requirements Present (4.0) only for conditions outside the attacker's control: a race window, a network position, a secret the attacker must obtain. How the integrator wired the library is not one.
- Privileges Required: the privileges the attacker needs in the calling application in that worst-case integration. "Anyone who can submit the input" is None; when typical applications gate that input behind a login, say so in prose.
- Scope (3.1): Changed only when the impact reaches components under a different security authority than the vulnerable one. FIRST's examples include sandbox and virtual-machine escapes, and web flaws whose impact lands in the user's browser (cross-site scripting). A library that enforces a sandbox and fails to is the hard case: write the reasoning down either way, because this one metric moves a score from 9.8 to 10.0 and reviewers will ask. CVSS 4.0 replaces Scope with separate subsequent-system impact metrics.
- Crashes: in memory-safe code, a panic, exception or controlled abort is availability impact only. In memory-unsafe code (C, C++, unsafe blocks, native extensions), check whether the crash comes from memory corruption: out-of-bounds write, use-after-free, double free. If it does, or you cannot rule it out, score the achievable confidentiality and integrity impact and say why in prose.
- Write the precondition in prose too. Readers act on the description, and databases often display your score unchanged.

```
✓ Good - CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
         "Denial of service when an application passes untrusted input to Parse
          without the MaxDepth option."
✗ Bad  - CVSS:3.1/AV:N/AC:H/... with the same text: AC:H used for the integrator's
         choice of options, against FIRST's guidance to score the reasonable
         worst-case configuration.
✗ Bad  - "Critical 9.8 RCE" copied from the report, no vector, no precondition.
```

## Advisory fields

| Field | Content |
|---|---|
| Title | Vulnerability class + affected API or feature. No payload. |
| Summary | One line: who is affected and what an attacker gains. |
| Affected / patched | One row per supported line (see next section). |
| Affected functions | The exported functions, methods or entry points that reach the flaw. Scanners with reachability analysis use them to avoid false alarms. |
| Description | Preconditions, impact, what the fix changes in general terms. |
| Workarounds | A real configuration or usage workaround, or "none - upgrade". Do not write "none" by default. |
| Severity | Full vector + label. |
| CWE | The most specific one that fits. |
| Credits | Reporter as finder or reporter; fix author as remediation developer; reviewers as remediation reviewer. Confirm consent and spelling first. |
| References | Fix commit, release, CVE record. No proof of concept in public until users had time to upgrade. |

Name affected APIs and versions precisely. A library's dependents need them to detect exposure. Leave out step-by-step reproduction and payloads.

## Version ranges

- One range per supported line: `>= 2.0.0, < 2.3.4` and `>= 1.0.0, < 1.9.12`, never a single `< 2.3.4` that marks the patched 1.9.12 as vulnerable.
- Use exact released versions. Untagged commits and pseudo-versions break automated database imports.
- List each separately published package or module path (a new major under its own path is its own entry).
- Fill the fixed version before publishing. Without it, scanners alert with no upgrade path.
- Mark versions you did not check as unknown, not safe.

## Ecosystem databases

Publishing the advisory on the code host is the main path. Ecosystem databases then import it, and each needs a check.

- **Go:** the Go vulnerability database opens an import issue for each Go advisory and assigns a GO- ID. Without affected symbols, govulncheck falls back to package or module level and flags dependents that never call the flawed code. Correct imports through the database's report and feedback forms. Tag a semver release for the fix. The database and govulncheck are the primary signal; `retract` is optional (release-runbook.md).
- **npm, PyPI, RubyGems, Maven, NuGet, crates.io:** the code-host advisory database feeds most scanners. Rust's RustSec database takes advisories as pull requests. Registry-side actions (deprecate, yank) are in release-runbook.md.
- **OSV:** most databases export to OSV, so a correct source advisory propagates. Check the OSV entry after import.

## Disputes

- Ask the assigning CNA to dispute or reject. Expect DISPUTED; REJECTED is rare once a record is published.
- Publish the reasoning: the documentation line, the trust assumption, the closed report.
- File corrections with every copy: code-host advisory database, ecosystem database (Go uses a NOT_A_VULNERABILITY exclusion), OSV.
- Code-host database curators do lower inflated scores when shown the precondition.
