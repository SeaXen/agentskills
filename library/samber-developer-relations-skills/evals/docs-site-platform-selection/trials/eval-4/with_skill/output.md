# Docs platform selection plan: Ostrander Clearing

Sections below are written in one pass, as you asked. The skill normally has you approve each one before the next, so treat all of them as unvalidated. The two decisions that need your reply are marked 🎯.

## ASSUMED items

These were not in your brief. Correct any that are wrong.

1. ⏳ The contract ends about 2027-05-31, and the non-renewal notice period is unknown. Check the notice date first. A 60–90 day notice could fall in Feb–Mar 2027, or earlier if the renewal is automatic.
2. The 1,100 pages count each locale and version once. If they are multiplied by 3 versions and 3 locales, the conversion work is much larger.
3. "Our Okta SSO" means Okta federates the customers' staff, so readers are external users. The platform must not price per reader.
4. Every change needs review before it goes live (banking change control).
5. Your current vendor already meets EU residency. Whether it covers the editor, search index, previews and AI features is unconfirmed.
6. Current site details are unknown: custom component count, monthly traffic, top inbound URLs, PDF output, header and branding match. The inventory comes first in the schedule.
7. The one-off migration effort ceiling is unknown. The 10 h/month is the only effort figure given, and I treat it as the standing ceiling.
8. The pages are mostly guides, with the OpenAPI and AsyncAPI reference as a minority of the site.

## 1. Switch decision and root cause

- **Trigger:** forced move. The vendor moved customer-only pages to an enterprise tier and the renewal quote jumped. Staying unchanged is off the table, so the renewed plan stays in the shortlist and is scored like the others.
- **Pain classification:**
  - The cost jump is a platform pain (subscription multipliers).
  - The constraints (residency, Okta-gated pages, spec rendering, locales) are platform capability.
  - No findability, stale-page or broken-sample pain was reported. If any exists, route it to `developer-docs-structure-audit` or `docs-code-sample-standards`, because a new platform carries those over intact.
- **Risk to flag:** going from 38 to about 85 PM-owners raises content-quality risk, which a platform doesn't fix. The register therefore requires section-scoped edit rights and review-before-publish, so ownership stays enforceable.
- **Verdict:** the platform question is valid. Re-platform only if a candidate beats the renewed quote on both standing cost and the owner-hours ceiling.

## 2. Requirements register

Differentiator weights are fixed here, before any scoring. The weights are baseline values you can change now, but not after you see scores.

| # | Requirement (outcome) | Source | Type | Test | Weight |
|---|---|---|---|---|---|
| 1 | Content, editor, search index, previews, backups and any AI-feature processing stay in the EU. Support-staff access is documented. | Banks (Q4) | knockout | Written security confirmation plus a data-flow list per component | - |
| 2 | Customer-only pages sit behind Okta SSO. They are hidden when logged out, absent from site search and the sitemap, and not reachable by direct URL. No per-reader pricing. | Q4 | knockout | SSO test account; logged-out probes on all three surfaces | - |
| 3 | A PM scoped to one section can edit and propose changes there but cannot publish outside it. | 85 owners | knockout | Scoped test account tries an out-of-scope edit | - |
| 4 | A non-Git editor publishes a one-line fix unaided. | Writers, SEs, PMs | knockout | Timed unaided edit by the least technical editor | - |
| 5 | A reviewer approves from a preview, and nothing publishes before approval. | Banking change control (ASSUMED) | knockout | Preview-approval run | - |
| 6 | The real OpenAPI and AsyncAPI specs render, and a spec change appears without hand edits. | Content shape | knockout | Render both real specs, then change a field | - |
| 7 | Three live API versions render with the right banners, plus DE and FR with a working language switch. | Content shape | knockout | Same page in 3 versions, one DE page, one FR page | - |
| 8 | Full size (about 1,100 pages, times versions and locales if applicable) builds or imports. | Scale | knockout | Full-size run, build minutes recorded | - |
| 9 | Content, assets and navigation export. | Exit-cost standing row | knockout | Export diff | - |
| 10 | The top 10 old URLs resolve or 301 to the same content. The docs domain stays the same, because customers may allowlist it. | URL-preservation standing row | knockout | URL check | - |
| 11 | A named owner, within 10 h/month. | Q3 | knockout | Owner named; one dependency or config change done during the pilot, timed | - |
| 12 | Search finds the right page for real DE, FR and EN queries. | Differentiator | differentiator | 10 real queries from logs or tickets, right page in top three | 3 |
| 13 | Vendor continuity, support SLA, subprocessor change notice. | Banks | differentiator | Status history plus written SLA | 3 |
| 14 | Accessibility meets the standard your customers require. | Customer or legal (ASSUMED) | differentiator | Automated check on 3 pilot pages | 2 |
| 15 | Interactive "try it" with real auth. | Differentiator | differentiator | One authenticated call from a reference page | 2 |
| 16 | Markdown per page and `llms.txt`. | Differentiator | differentiator | Fetch both | 1 |

Rows 1–8 are the eight knockouts. Rows 9–11 are the three standing rows. Capabilities the current site already depends on (preview links, redirects, custom components, analytics, branding) become extra knockouts once the inventory exists. They would break the cap of eight, so if more than a few appear, move wishes down to `nice`.

## 3. Platform classes

No product names in this section.

**Deleted:**
- **Knowledge-base CMS:** weak on code, versioning and review for developer docs.
- **Custom build:** no funded platform team, only 10 h/month.
- **Spec-driven reference portal as the main platform:** reference is a minority of the site, so promote it only as a component beside a guides platform. This option is kept as a fallback if a candidate's native AsyncAPI rendering fails knockout 6.

**Surviving classes:**

| Class | Runs | Leaves |
|---|---|---|
| Stay and fix (the renewed incumbent) | No migration, no URL change. | The seat curve to 85 editors on the gated tier. Exit cost stays as is. |
| Hosted docs platform (EU-capable) | Vendor runs build, hosting and search. Standing hours are lowest. | Seat, site and gated-tier multipliers. Vendor security and subprocessor review. Proprietary components. |
| Self-hosted generator, with a Git-backed web editor, in your EU hosting, with Okta at the edge | No licence and no seat pricing. It stays inside reviews you have already passed. Cheapest exit. | Owner hours for upgrades, search, auth proxy, editor layer, 3×2 version/locale builds, AsyncAPI rendering. |

**Re-ranking:** the skill's default tie-break tips toward self-hosted. You have a named owner, many editors, and a hosting constraint. Your answers move this in two ways:
- 10 h/month is small for a self-hosted stack that also needs a web editor for about 85 non-Git editors, an Okta-gated edge, a search service and a 3×2 build matrix. Neither the skill nor I can verify that estimate. It is a pilot measurement. This pushes toward hosted.
- The trigger is price, and the multiplier curve (38 → 85 editors, about 2.2×, on a gated tier) is the driver. This pushes toward self-hosted. The bank-review advantage also favours self-hosted.

🎯 **Decision 1: which class?** Recommended: **hosted docs platform (EU-capable) as the primary, with the self-hosted generator as one pilot candidate.** The 10 h ceiling is the binding constraint. The self-hosted pilot acts as the price check, and it wins only if its measured owner hours fit within 10. If you choose differently, say so and I'll re-run Steps 4–6. I've written this choice as ASSUMED until you confirm.

## 4. Shortlist: three candidates

The candidates are listed in order of selection (user first, then incumbent, then importers, then live research). No vendor claim below is verified. Every knockout must be checked against the vendor's own current docs and pricing page, never a comparison article. Mark each `vendor-published` or `claimed`, and drop a candidate only on a published failure.

1. **Incumbent's renewed enterprise plan** (forced-move rule). Ask for the quote in multipliers at 85 editors, the gated tier, readers, and locales and versions.
2. **One EU-capable hosted platform.** Seeds to research: Mintlify, GitBook, ReadMe, Fern, Document360. These are examples only, not a ranking. The first filter is a published EU region that covers the editor, content store and AI features, plus Okta SSO for readers on the plan you would buy.
3. **One self-hosted generator** with Git-backed web editing. Seeds: Docusaurus, Astro Starlight, MkDocs Material, Antora, plus a Git-backed CMS layer. The first filters are AsyncAPI rendering, DE/FR locales and 3 versions.

**Multipliers to record, without prices:** editors (38 now, 85 in a year), sites (preview or staging), gated pages or tier, SSO, readers on gated pages, languages, versions, AI features, custom domain.

**Vendor questions to send now** (this starts the bank security review in parallel):
- Where do the editor, content store, search index, preview builds, backups, logs and AI features run, and which subprocessors touch them?
- Is Okta SSO for external readers on the plan you'd buy?
- What is the notice period for subprocessor changes?

## 5. Pilot

Run the same 8 pages on all three candidates (the skill's maximum for a pilot).

| # | Page |
|---|---|
| 1 | The page with the most custom components |
| 2 | One real OpenAPI reference page |
| 3 | One real AsyncAPI reference page |
| 4 | The quickstart |
| 5 | A page that differs across the 3 live versions |
| 6 | One DE page and one FR page (counted as one slot) |
| 7 | The longest page |
| 8 | One customer-only page |

**Tasks and pass thresholds** (written before the pilot starts):

| Task | Who | Pass |
|---|---|---|
| One-line fix | The least technical editor, unaided | Done with no developer help |
| Scoped PM edit | A PM test account | Cannot publish outside its section |
| Approve from preview | Reviewer | Nothing live before approval |
| Full-size build or import | Owner | Completes, minutes recorded |
| 10 real search queries | Anyone | At least 8 return the right page in the top three, across EN, DE and FR |
| Export | Owner | Page count, images and nav match the source |
| 10 old top URLs | Anyone | All resolve or redirect to the same content |
| Gated page | Okta test account | Hidden when logged out and on all three surfaces; visible when logged in |
| Residency | Security | Written confirmation plus a data-flow list covering every component, including AI features |
| Owner hours | Owner | One dependency or config change done and timed. Self-hosted also does the auth-proxy and editor-layer upkeep. |
| Proprietary component count | Owner | Recorded as the exit-cost evidence |

**Scoring:** a failed knockout removes the candidate. Differentiators use the weights from Step 2.

## 6. Cost

All figures are baseline or ASSUMED until the pilot replaces them.

**Standing:**
- **Owner hours:** a baseline of 4–8 h/month for hosted and 12–20 h/month for self-hosted. These are not measured and the pilot replaces them. The self-hosted range sits above your 10 h ceiling. If the pilot confirms that, the self-hosted candidate is out.
- **Subscription:** expressed as the multipliers from Step 4 against 38 editors now and 85 next year (about 2.2×). Compare the incumbent's quote against the hosted candidate's, and don't compare list prices.

**One-off:**
- Conversion of each proprietary component.
- Navigation mapping and the redirect map.
- A content freeze window.
- Review time. Every converted page gets a review, so size it from the page counts and your reviewer capacity.

**Exit:**
- Components to convert.
- Export gaps.
- URL shape the next platform must reproduce.
- **Rule of thumb:** self-hosted exits cheapest. Hosted exits cost the proprietary component count from the pilot.

If any candidate exceeds 10 h/month standing, return to Step 3 and take the next class, or narrow the scope (for example, move guides and keep the reference on the existing platform).

## 7. Decision record and schedule

**Schedule against the contract end.** The new site is live and verified, with the old one kept in parallel, at least 4 weeks before the contract ends.

| When | What |
|---|---|
| Now (about 2 days) | Find the contract's notice and auto-renew date. Ask the incumbent for a 1–3 month extension option as the rollback path. |
| Nov 2026 (about 3 weeks) | Approve the register and the class. Run the current-site inventory. Send the vendor residency and subprocessor questions. |
| Dec 2026 (about 3 weeks) | Step 4 knockout checks on the vendors' own docs. Start the bank vendor security review for the likely winner. |
| Jan 2027 (about 4 weeks) | Pilot, in parallel across the three. |
| Early Feb 2027 | Decision record signed. |
| Feb–Apr 2027 | Migration, freeze window, parallel run. |
| Early May 2027 | Cutover. The old site stays live until the new one is verified. |

Bank security review is the item most likely to run long, so it starts in December.

**Record contents:** the decision; trigger and root-cause verdict; the register with results per candidate; classes considered and why each fell; pilot results; standing, one-off and exit cost; standing owner and migration owner; schedule against the notice date, with the old site live in parallel and the rollback path; assumptions; revisit triggers.

**Revisit triggers (check quarterly):**
- Editors past about 85.
- Owner hours past 10.
- A plan or price change on the gated tier.
- A subprocessor change that touches residency.
- An owner leaving the platform team.
- A knockout regression.

**Handoffs:**
- Redirect map, canonicals and indexing at cutover: `docs-seo`.
- Which versions migrate and in what state: `docs-versioning-strategy`.
- Which locales migrate or freeze: `docs-localization-strategy`. These last two aren't in my installed skill list, so I couldn't confirm them.
- `llms.txt` and markdown endpoints: `coding-agent-docs-optimization`.

## 🎯 Decision 2 and next steps

1. **Contract notice date.** Tell me the date, or I'll keep it as ASSUMED. Everything above depends on it.
2. **Confirm or change Decision 1** (hosted primary, self-hosted as the price check).
3. **Send me:** your current vendor's name, the custom component count, and the top 10 URLs. Then I can run the live Step 4 checks and fill in the shortlist.

I haven't saved any of this to memory; say so if you want the register and class stored.