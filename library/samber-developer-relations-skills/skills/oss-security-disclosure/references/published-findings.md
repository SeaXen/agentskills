# Published norms, incidents and time-sensitive facts

Read this when anchoring a timeline negotiation, explaining why a step matters, or checking a fact that changes often.

## Embargo defaults

Quote each with its owner; none is a standard.

| Owner | Default | Notes |
|---|---|---|
| Google Project Zero | 90 days to fix, plus 30 days for patch adoption when fixed early ("90+30") | A "Reporting Transparency" trial publicly lists vendor, product and deadline within about a week of reporting, with no technical detail |
| CERT/CC | 45 days after the initial report, regardless of patch availability | Extenuating circumstances (active exploitation, standards changes) move it earlier or later. The CERT Guide to Coordinated Vulnerability Disclosure separately advises treating declared timeframes as the start of a negotiation |
| Openwall distros / linux-distros lists | 14 days maximum, under 7 preferred | Only for not-yet-public issues, with a fix available or close |
| OpenSSF disclosure guide | 45-90 days as the common range; 90 days the longest default groups entertain | Notify downstream providers 1-30 working days ahead |
| Kubernetes Security Response Committee | Private distributors notified at least 7 days before disclosure | Committee capped at 10 members (security release process document) |

A reporter's 14-day deadline sits at the short end but inside published practice. For a small library fix it is usually meetable; for a fix needing several backports it is a counter-offer.

## Incidents

| Case | What happened | Lesson |
|---|---|---|
| curl, CVE-2020-19909 | A third party filed a CVE in 2023 for a 2019 bug curl had judged non-security and fixed. A database scored it 9.8; it was later lowered and marked disputed, not rejected. | Keep "not a vulnerability" reasoning public and citable. |
| curl becomes a CNA (2024) | The project became a CNA for its own products to stop bogus CVEs; the Linux kernel did the same. | Owning assignment is the strongest defence once bogus CVEs recur. |
| curl, CVE-2023-52071 | Requested through another CNA just before curl became a CNA; rejected only after weeks of escalation. | CNA status does not reach back to earlier assignments. |
| node-ip, CVE-2023-42282 | A misclassification bug scored 9.8; audit-tool noise pushed the maintainer to archive the repository; the code-host database later lowered it to low. | Challenge inflated scores in every database with the precondition spelled out. |
| curl bug bounty (2019-2026) | Confirmed share of reports fell from over 15% to under 5% during 2025, driven by machine-generated submissions; the bounty ended in January 2026 after 87 confirmed vulnerabilities and over 100,000 USD paid. | Money attracts low-quality volume; a bounty needs triage capacity behind it. |
| curl intake pause (2026) | The project refused all reports for about a month and called it one of its best decisions. | Declared intake pauses are a legitimate capacity tool. |

## Time-sensitive facts

Re-check these before quoting them; each has changed within the last two years.

- Code-host CVE review: GitHub documents "usually within 72 hours", but stated in October 2026 that reviews of repository advisories and CVE requests ran longer than documented. Request on acceptance.
- NVD scoring: since April 2026 NIST no longer routinely adds its own score when the CNA supplied one, so the maintainer's vector is what most scanners show.
- CVSS 4.0: accepted in GitHub advisories since September 2024, base metrics only in the database's edit form.
- EU CRA: Article 14 reporting applies from 11 September 2026; steward reporting and the rest of the regulation from 11 December 2027. ENISA's Single Reporting Platform went live on 11 September 2026.
- Code-host private reporting as intake: curl moved its intake there in February 2026 and back to a bounty platform a month later, citing missing ways to label low-quality reports and publish invalid ones.
