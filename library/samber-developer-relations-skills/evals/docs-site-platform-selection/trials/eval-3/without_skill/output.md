# Kelpline docs platform: recommendation and requirements

## Recommendation

**Migrate to a hosted docs platform with a web editor and native OpenAPI support. Start a 2-week pilot with Mintlify as the lead candidate and GitBook as the fallback. Name the tech writer as the platform owner.**

Docusaurus is fine software. Your problem is that nobody owns it, and a free license doesn't fix that. The platform choice won't fix it either, unless the owner is named.

## Why not "stay on Docusaurus"

The CTO is right that it costs nothing to license. It costs something to run:

- **Upgrades:** nobody has the hours. The OpenAPI plugin is two majors behind, and the build has broken twice. Each future Docusaurus or React major version repeats this work, and the community plugin may not keep up.
- **Editing:** the 6 support engineers can't edit without Git. Every fix they spot goes through Slack to the one writer, so the writer is a bottleneck and fixes get lost.
- **Engineering hours:** the VP set these at zero. Staying means either breaking that rule or letting the site rot further.

A Docusaurus rescue would need a one-off upgrade plus a CMS layer on top, such as Decap or TinaCMS, so non-Git people can edit. It would still need ongoing maintenance. That is the cost the CTO is assuming away.

**How to put it to the CTO:** compare the hosted subscription against the loaded cost of one engineer's days per quarter, plus the writer's time spent relaying Slack fixes. Pull current pricing from the vendors, because I haven't verified it. At 60 people and 300 pages, I expect the subscription to be small next to that.

## Requirements

**Must have**

1. **No engineering time to run.** Hosting, builds, search, TLS and upgrades are all handled by the vendor.
2. **A web editor for non-Git users.** A support engineer must be able to fix a typo or a paragraph in the browser. Changes go through review by the writer before publishing (suggestion or change-request flow).
3. **Native OpenAPI reference.** It must be generated from your spec file or URL, with a try-it playground. No community plugin may sit between you and the spec.
4. **Content stays portable.** Pages live in Markdown or MDX that you can export, ideally synced to a Git repo. The lock-in test is whether you can leave in a day.
5. **Migration of the ~300 pages.** Admonitions, tabs and custom React components are the usual breakage points. Old URLs must redirect (301), so you keep your search ranking and customer bookmarks.
6. **Search and basic analytics.** You need to see what users search for and which pages fail.
7. **Roles and review.** The writer approves publishes. Support engineers can propose edits but not publish.

**Should have**

- Custom domain, light branding, and a dark mode that matches the product.
- An `llms.txt` file or an AI-readable export. Customers increasingly read docs through assistants.
- SSO, if you need it for internal-only pages.

**Not needed:** versioning (you have one version), i18n (English only), self-hosting (no hosting restrictions).

## Candidates

| | Mintlify (lead) | GitBook (fallback) | Stay on Docusaurus |
|---|---|---|---|
| Non-Git editing | Web editor, Git-backed | Strongest editor, change requests | Needs an add-on CMS |
| OpenAPI | Native, strong playground | Supported, less customizable | Community plugin, two majors behind |
| Engineering hours | ~0 | ~0 | Ongoing |
| Portability | MDX in Git | Markdown, Git sync | Full |
| Migration effort | Moderate (MDX is close to Docusaurus MDX) | Moderate to higher (re-import) | None, but the upgrade backlog remains |

Vendor features and prices change fast. Verify every cell in the pilot, not from this table.

## Plan: 12 weeks

| Weeks | Step |
|---|---|
| 1–2 | **Pilot.** Import about 30 representative pages (tables, tabs, code blocks, images) and the OpenAPI spec into both candidates. Have 2 support engineers make real edits. |
| 3 | **Decide.** Use the pass/fail criteria below. Get CTO and VP sign-off with the cost comparison. |
| 4–8 | **Migrate.** Convert all 300 pages, build the redirect map, and fix broken components. Freeze non-urgent doc edits for the final week. |
| 9–10 | **Parallel run.** Keep the old site up. Test the support engineers' edit flow and check the redirects. |
| 11 | **Cutover.** Switch DNS, submit the new sitemap, and monitor 404s. |
| 12 | **Retire Docusaurus.** Archive the repo and write a one-page runbook. |

**Pilot pass/fail criteria**

- A support engineer fixes a page with no help from the writer, in under 10 minutes.
- The OpenAPI reference renders every endpoint in your spec with working examples.
- At least 95% of the 30 pilot pages need no manual rework after import.
- The export test works: you get all content out as Markdown.

## Risks and open items

- ⚠️ **The OpenAPI spec's source of truth.** Where does it live, and who updates it? If engineering publishes it from CI, great. If someone hand-edits it, the writer must own that file. Confirm this in week 1, because it decides whether the reference stays current.
- ⚠️ **Custom React or MDX components.** They won't port. Count them before you commit to a timeline.
- ⚠️ **Single owner.** One writer owning the platform is a bus-factor problem, which is how you ended up here. Name a backup, and write the runbook in week 12.
- ℹ️ **Support engineers' editing habit.** They route fixes through Slack today. After cutover, announce the new flow and have the writer review proposed edits weekly. Without that, the tool changes but the behavior doesn't.

## Decisions needed from you

1. Approve the 2-week pilot and a small tooling budget.
2. Confirm the tech writer as the platform owner.
3. Get the CTO's agreement that a subscription is acceptable, using the cost comparison above.