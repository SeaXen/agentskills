# Docs platform decision: Kelpline

**Decision: move to a hosted docs platform, with the tech writer as named owner and a two-candidate pilot before signing. The target is live by the end of January 2027 (baseline).**

Status: unvalidated. You asked me to skip the interview, so no section was agreed with you one by one. Every `ASSUMED` item is listed below.

## Assumptions to correct

- ASSUMED: no customer-only or SSO-gated pages.
- ASSUMED: no PDF or offline output, no content reuse across products, no locales.
- ASSUMED: every support-engineer edit needs the tech writer's review before it goes live.
- ASSUMED: the tech writer can own the site at about 2 hours per month, with no engineering time.
- ASSUMED: editors grow from 7 now to at most 10 in a year, on one site.
- ASSUMED: custom components on the current site are few. Please count them.
- UNKNOWN: monthly docs traffic and the top-10 URLs. Pull them from analytics before the pilot.
- UNKNOWN: any capability the current site relies on that you haven't mentioned, such as preview links, redirects, analytics, search service or company header.
- NOT CHECKED: I haven't verified any vendor's current pricing, plans or features. Step 4 checks are still to do, and nothing below is `tested`.

## 1. Root cause

| Pain | Cause | Route |
| --- | --- | --- |
| Plugin two majors behind, build broke twice | Platform ownership: nobody owns upgrades | This skill |
| Support engineers can't fix docs, so they ping the writer | Platform authoring model: no web editing | This skill |
| Findability, stale pages, wrong examples | None reported | Not routed |

Both pains are platform pains. A move won't carry a content problem over, because you reported none. If findability or broken samples show up later, route them to `developer-docs-structure-audit` or `docs-code-sample-standards`. They won't be fixed by a platform change.

## 2. Requirements register

Weights are fixed now, before any candidate is scored.

| # | Requirement (outcome) | Source | Type | Test | Weight |
| --- | --- | --- | --- | --- | --- |
| 1 | A support engineer publishes a fix without Git | 6 non-Git editors | knockout | Timed, unaided one-line edit | - |
| 2 | The writer approves from a preview, and nothing goes live before approval | Review of non-engineer edits (assumed) | knockout | Preview link exists, and the draft stays unpublished | - |
| 3 | The real OpenAPI spec renders, and a spec change appears without hand edits | Current reference plugin | knockout | Render the production spec, change an endpoint, re-check | - |
| 4 | 300 pages import or build at full size | Scale | knockout | Full import; record minutes | - |
| 5 | A named owner stays within the hours ceiling, with zero engineering hours | VP decision, Arjun's departure | knockout | Owner named, plus one upgrade or config change done unaided during the pilot | - |
| 6 | Content, assets and navigation can be exported | Standing row: exit cost | knockout | Run the export, diff page count, images and nav | - |
| 7 | The top-10 old URLs resolve or 301 to the same content | Standing row: URL preservation | knockout | URL check | - |
| 8 | Search returns the right page for 10 real queries | Support tickets | differentiator | 10 queries from tickets, right page in top 3 for at least 8 | 3 |
| 9 | Interactive "try it" with generated samples | API product | differentiator | An authenticated call succeeds from a pilot page | 2 |
| 10 | The company header and analytics work on pilot pages | Current site | differentiator | Header and one analytics event fire | 2 |
| 11 | `llms.txt` and markdown per page exist | Assistants using the docs | differentiator | Fetch both for a pilot page | 1 |
| 12 | Edit and feedback data can be exported | Exit cost | differentiator | Export attempted | 1 |

Add any capability the current site relies on that I couldn't see. Each one becomes another knockout, up to about eight in total.

## 3. Platform class

**Stay and fix fails.** Knockout 1 fails on Docusaurus, and so does knockout 5 once the standing cost is priced:

- Upgrading the plugin and the framework needs an owner, and you have zero engineering hours.
- Adding a Git-backed editor layer for support engineers adds one more component to maintain.
- Managed hosting for the same generator removes hosting, not upgrades.

**Classes deleted:**

- **Self-hosted docs generator (Docusaurus):** no build owner, so it fails. This is the "free means free" failure mode, and the site has already rotted once.
- **Custom build:** there is no platform team.
- **Knowledge-base CMS:** it is weak on code, versioning and an OpenAPI reference. It fits help-center articles, not these docs.
- **Spec-driven reference portal:** it ranks lower unless generated reference is most of the site. Reference is one part of 300 pages. A second system for guides would add an owner you don't have.

**Survivor: hosted docs platform.** It has a web editor, previews, and no build for anyone to maintain. Its cost is subscription multipliers and proprietary components, which the pilot measures.

**Answering the CTO.** Docusaurus has no licence fee, but the cost is standing engineering hours. The VP set those to zero, and the site has already broken twice without an owner. A free tool with no owner cost you two build breaks and a plugin two majors behind.

The recommendation flips if engineering commits named monthly hours. A named owner plus 7 or more editors would then tip the tie toward self-hosting. Only a written, committed allocation counts, not "engineering will help". A one-off contractor upgrade doesn't fix the standing cost.

## 4. Shortlist

Take two candidates, not three, because the live date is inside a quarter. Select them from the class examples: Mintlify, GitBook, ReadMe, Fern, Document360. Prefer products that import Docusaurus Markdown/MDX cheaply. I haven't verified any of these.

Before the pilot, check each candidate's current docs and pricing page, never a comparison article. Mark each knockout `vendor-published` or `claimed`, and drop a candidate only on a published failure.

Record these multipliers for each candidate, without quoting prices:

- Whether support engineers count as full editors, or whether a cheaper limited role exists. This is the biggest cost driver here.
- Editors now (7) and in a year (10, assumed).
- Number of sites (1).
- Whether the custom domain, review workflow and AI features sit behind a higher tier.

## 5. Pilot

Port the same 6 pages to both candidates:

1. The page with the most custom components or embedded widgets.
2. A generated OpenAPI reference page, from the real spec.
3. The quickstart.
4. The longest page.
5. A page support engineers fix most often.
6. A page with the heaviest code samples.

No versioned, translated or gated pages exist, so those slots are skipped.

Pass thresholds, written before the pilot:

| Task | Who | Pass |
| --- | --- | --- |
| Publish a one-line fix | The support engineer least used to docs tooling, unaided | Done, no developer or writer help |
| Approve from a preview | Tech writer | Preview link exists, nothing live before approval |
| Full-size import or build | Tech writer | Completes; minutes recorded |
| 10 real search queries | Anyone | Right page in the top 3 for at least 8 |
| Export | Tech writer | Page count, images and nav match the source |
| Old URLs | Anyone | Top-10 URLs resolve or 301 correctly |
| Proprietary component count | Tech writer | Recorded; this is the exit-cost evidence |

A failed knockout removes the candidate. Score differentiators with the weights above.

## 6. Cost

- **Standing:**
  - Owner time is about 2 hours per month (assumed), for editor roles, billing and platform changes. There are no upgrades, plugins or CI.
  - The subscription is priced as multipliers against 7 editors now and 10 in a year.
- **One-off:**
  - Convert custom components and map navigation.
  - Replace the OpenAPI plugin with the platform's renderer, from the spec rather than the old pages.
  - Build the redirect map from the top-traffic URLs.
  - Plan a short content freeze and the writer's review time.
- **Exit:** the count of proprietary components from the pilot, any export gaps, and the URL shape the next platform must reproduce.

Compare these against the ceiling of zero engineering hours and a one-quarter migration. If a candidate exceeds it, take the next class or narrow the scope, for example by moving guides and keeping the reference.

## 7. Plan, owners and revisit trigger

Schedule (baseline, from 2026-11-02):

| Weeks | Work |
| --- | --- |
| 1-2 | Confirm assumptions and register; verify vendor docs; pick 2 candidates |
| 3-5 | Pilot |
| 6 | Decision record signed |
| 7-10 | Migration, with the old site live in parallel |
| 11-12 | Cutover, redirects verified, rollback path kept |

Keep the old Docusaurus site live until the new one is verified, and keep its repository and build as the rollback path.

- **Standing owner:** the tech writer, to be confirmed with them.
- **Migration owner:** the tech writer, with outside help only if the VP funds it. Engineering contributes nothing.
- **Revisit triggers:** a price or plan change; editors past 15; the owner leaving; any knockout regression; engineering committing named monthly hours.

Handoffs at cutover:

- Redirects, canonicals and indexing: `docs-seo`.
- `llms.txt` and markdown endpoints: `coding-agent-docs-optimization`.
- Versions and locales don't apply today.

KPIs after cutover:

- Zero 404s from the old URL inventory within a week.
- Search traffic back to the pre-move baseline within two months (assumed).
- A rising number of edits from non-engineers.
- Owner hours within the Step 6 estimate.

## What I need from you

1. Confirm or correct the assumptions listed at the top.
2. Send the custom-component count, the top-10 URLs and any other capabilities the current site relies on.
3. Check whether the CTO will accept the "free is not zero-cost" argument, or whether the engineering-hours trigger needs a conversation with the VP first.