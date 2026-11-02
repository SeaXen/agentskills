# Requirements register: dimensions, tests, template

Use this catalogue to find rows for the register in Step 2. Add a row only when an interview answer or an observed pain calls for it.

## Dimensions and their pilot tests

| Dimension                 | Ask                                                                                                                                             | Pilot test                                                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Authoring model           | Who edits: engineers in pull requests, writers, support or DevRel staff without Git habits?                                                     | The least technical editor publishes a one-line fix unaided; time it                                                |
| Review                    | Must every change be reviewed before it goes live?                                                                                              | A reviewer approves from a preview link; nothing publishes without approval                                         |
| Build owner               | Who upgrades, patches and fixes the build, how many hours a month?                                                                              | Name in the register; one dependency upgrade done during the pilot                                                  |
| Hosting constraint        | Third-party hosting allowed? Data residency? Air-gapped readers?                                                                                | Written confirmation from security; offline build artefact if air-gapped                                            |
| Access control            | Customer-only or partner-only pages? SSO with the company identity provider? Are readers external users, and is the platform priced per reader? | A gated page is unreachable logged out, absent from site search and the sitemap, reachable with an SSO test account |
| Edit permissions          | Do teams own sections (each PM edits only their pages)?                                                                                         | An editor scoped to one section cannot publish outside it                                                           |
| Scale                     | Pages today and in a year?                                                                                                                      | Full-size build or import completes; record build minutes                                                           |
| API reference             | Generated from a spec (OpenAPI, AsyncAPI, GraphQL, docstrings)?                                                                                 | The real spec renders; a spec change appears without hand edits                                                     |
| Versions                  | Versions kept live, and in which states?                                                                                                        | One page renders per live version with the right banner                                                             |
| Locales                   | Languages, and translation vendor format?                                                                                                       | One translated page renders with a working language switch                                                          |
| Outputs                   | PDF or offline bundle needed? Content reused across products?                                                                                   | Generate the PDF; one reused snippet updates in two places                                                          |
| Search                    | Built-in, external service, or company search?                                                                                                  | Ten real reader queries (from logs or tickets) return the right page in the top three                               |
| Branding and integration  | Must the site share the company header, analytics, consent banner?                                                                              | Header, analytics event and consent banner work on a pilot page                                                     |
| Search-engine controls    | Canonicals per version and locale, title templates, noindex on previews, static or server-rendered HTML?                                        | View-source of a pilot page shows the canonical and title in the HTML; a preview URL carries noindex                |
| API explorer              | Interactive "try it" with real auth, generated multi-language samples?                                                                          | An authenticated call succeeds from a pilot reference page                                                          |
| Vendor continuity         | Support SLA, uptime history, roadmap and ownership risk?                                                                                        | Status-page history and a written support SLA                                                                       |
| Machine-readable surfaces | Markdown per page, `llms.txt`, spec files at stable URLs?                                                                                       | Fetch the markdown version and the index file of a pilot page                                                       |
| URL preservation          | Inbound links and ranking pages to keep?                                                                                                        | Ten top-traffic old URLs resolve or 301 to the same content                                                         |
| Exit cost                 | Can content, assets and navigation leave? (Analytics and feedback data export: differentiator.)                                                 | Run the export; diff page count, images and nav against the source                                                  |
| Accessibility             | Accessibility standard required by customers or law?                                                                                            | Run an automated accessibility check on three pilot pages                                                           |

## Register template

```
| # | Requirement (outcome) | Source (pain or constraint) | Type | Test | Weight | Evidence per candidate |
|---|---|---|---|---|---|---|
| 1 | A support engineer publishes a fix without Git | Interview Q2: 6 support editors, no Git | knockout | Timed unaided edit | - | A: tested pass / B: claimed |
| 2 | Customer-only pages behind company SSO | Interview Q4 | knockout | SSO test account | - | A: vendor-published / B: tested pass |
| 3 | Build owner named, within the standing-hours ceiling | Interview Q3 | knockout | Owner and upgrade log | - | ... |
| 4 | Export returns content, assets, nav | Exit cost row | knockout | Export diff | - | ... |
| 5 | Top 10 old URLs kept or redirected | URL preservation row | knockout | URL check | - | ... |
| 6 | Search finds answers to real queries | Ticket log | differentiator | 10-query test | 3 | ... |
| 7 | Build under 5 minutes at full size | Current pain | differentiator | Build timing | 2 | ... |
```

Rules:

- **Do:** write requirements as outcomes a person observes, not feature names.
- **Do:** fix weights before scoring and keep them on the page.
- **Don't:** mark a knockout passed from a vendor page; `vendor-published` only keeps a candidate in the pilot.
- **Don't:** list more than about eight knockouts, excluding the three standing rows (exit cost, URL preservation, owner); a longer list hides wishes.
