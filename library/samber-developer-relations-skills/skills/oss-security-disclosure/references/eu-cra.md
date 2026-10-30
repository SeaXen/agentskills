# EU Cyber Resilience Act: who reports what

Read this when the project is monetised, company-run, shipped inside companies' products in the EU, or a report mentions active exploitation. This is decision input for a lawyer, not legal advice. Article references are to Regulation (EU) 2024/2847.

## Role test

Ask in order; stop at the first yes.

1. **Does an entity place a product containing the software on the EU market in the course of a commercial activity, under its own name?** That entity is a **manufacturer**. This includes companies that sell a product built on the project, and the project's own company when it monetises the software. Pure software-as-a-service is outside the CRA (Recital 12) unless it is remote data processing integral to a shipped product; it falls under other law.
2. **Is there a legal person (foundation, company), not a manufacturer, that systematically supports the project's development on a sustained basis, for software intended for commercial activities?** That entity is an **open-source software steward** (Art. 3(14)). The Commission's implementation guidance splits stewards by role: non-technical stewards (governance, branding) need only the cybersecurity policy; infrastructure stewards (hosting, CI) report severe incidents affecting that infrastructure; engineering stewards (employing developers, coordinating releases) report actively exploited vulnerabilities they become aware of.
3. Otherwise - individual volunteers, non-monetised projects, contributors to projects not under their responsibility - **outside the regulation** (Recitals 15 and 18). Regular releases, hosting on a public forge, funding or code from manufacturers, and donations, sponsorship or paid support that only recover costs do not by themselves make a project commercial; the Commission's guidance counts reasonable living expenses of individual maintainers as costs. A paid version, or support and donations priced beyond cost recovery, point the other way.

## Obligations by role

| Role | Reporting | Other duties | Fines |
|---|---|---|---|
| Manufacturer | Actively exploited vulnerabilities and severe incidents, to the CSIRT coordinator and ENISA through the Single Reporting Platform (Art. 14). Applies from 11 September 2026, including products already on the market. | Inform impacted users of the vulnerability and mitigations, where appropriate machine-readable (Art. 14(8)). Report vulnerabilities found in components, including open-source ones, to their maintainers and share fixes (Art. 13(6)). Full product requirements from 11 December 2027. | Yes; micro and small enterprises are exempt from fines for missing the 24-hour early warning |
| Steward | Art. 14(1) only to the extent involved in development; severe-incident duties for infrastructure it provides for development. Applies from 11 December 2027. | Documented cybersecurity policy that encourages voluntary vulnerability reporting; cooperate with market surveillance authorities on request (Art. 24). | No administrative fines (Art. 64(10)(b)) |
| Outside scope | None | None | None |

## Article 14 deadlines (manufacturers)

| Trigger | Early warning | Notification | Final report |
|---|---|---|---|
| Actively exploited vulnerability | 24 hours after becoming aware | 72 hours | 14 days after a corrective or mitigating measure is available |
| Severe incident affecting product security | 24 hours | 72 hours | 1 month after the notification |

The clock starts at awareness of active exploitation, not at report receipt. A privately reported, unexploited vulnerability does not start it.

## Other provisions to flag to a lawyer

- Voluntary reporting (Art. 15): anyone, including out-of-scope maintainers, may notify vulnerabilities through the reporting platform once that channel opens.
- Manufacturers also owe vulnerability-handling requirements from 11 December 2027 (Annex I, Part II): a coordinated disclosure policy, a contact address, free security updates with advisories, and a declared support period, generally at least five years (Art. 13(8)). A company-run project's supported-versions table should match that period.

## What this means for maintainers outside scope

- Expect manufacturers on 24-hour clocks to contact you about exploited bugs, and to forward vulnerabilities they find in your code (Art. 13(6)). A fast, named private channel in SECURITY.md is what they will look for.
- Machine-readable advisories with exact version ranges let them meet their user-notification duty without asking you.
- When exploitation is known, tell your known commercial integrators directly on the day you learn it.

## Steward checklist (from 11 December 2027)

- A written cybersecurity policy: how vulnerabilities are reported, handled, fixed and disclosed. SECURITY.md plus the disclosure process usually covers most of it; have a lawyer confirm.
- A named contact able to answer a market surveillance authority's request.
- Reporting process ready for exploited vulnerabilities in projects whose development the steward is involved in.
