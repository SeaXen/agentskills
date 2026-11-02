# Precedents, cost shape and lock-in

## Contents

- Named moves and what they teach
- Cost shape
- Lock-in surfaces
- Integration note: example products per class

## Named moves and what they teach

| Team                                                     | Move                                                                                        | What it teaches                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cloudflare developer docs                                | Hugo to an Astro-based docs theme (2024); Gatsby to Hugo (2021)                             | Carry current capabilities as "non-negotiable" knockouts. 8,060 files in six weeks: 10 days evaluation, 14 days component migration, 5 days staging, an 8-hour code freeze. Converted syntax with a Markdown syntax-tree walk, not regex. Picked a stack in its contributors' languages. Hit a build-time edge case past 4,000 pages. |
| MDN Web Docs                                             | Wiki on a database to content in a Git repository on a purpose-built static platform (2020) | A custom build with a funded owning team. Moved for maintainability and review-before-publish; the plan froze all translations read-only in a separate repository as a temporary stage.                                                                                                                                               |
| HubSpot developer docs                                   | In-house platform to a hosted platform                                                      | "An accidental docs platform team": every UI change needed engineering sprints. Chose build over buy three times before switching.                                                                                                                                                                                                    |
| Oso                                                      | Self-hosted generator to a hosted platform                                                  | Dependency updates and manual security patching were the standing cost it left.                                                                                                                                                                                                                                                       |
| A two-year GitBook user (dev.to post-mortem by mjkloski) | Hosted platform to another hosted platform                                                  | Left over per-user plus per-site pricing; no direct Markdown export, and Git Sync output kept proprietary blocks that needed cleanup. Rejected a self-hosted generator as too much infrastructure for a three-person team. The post endorses its destination vendor; its outcome claims are self-reported.                            |
| Tom Johnson's team at a large company                    | CMS with pasted HTML to a generator in internal Git                                         | Waited about a year for engineering bandwidth; repository layout flipped several times between build speed and shared theme updates.                                                                                                                                                                                                  |
| GitLab docs                                              | Nanoc to Hugo                                                                               | The new generator changed URL shapes and index-file names; a scripted bulk migration and a writer guide carried the change.                                                                                                                                                                                                           |

Moves run in several directions: self-run to hosted (HubSpot, Oso), generator to generator (Cloudflare, GitLab), CMS or wiki to Git (MDN, Tom Johnson's team), hosted to hosted (the GitBook user). The binding constraint (owner hours or subscription multipliers) decides, not the direction. Outcome claims in posts that endorse a vendor ("cut our support burden in half") are self-reported.

## Cost shape

- **Self-hosted generator:** no licence; standing cost is owner time for upgrades, plugins, search, security fixes and CI. Tom Johnson warns theme and tooling work can take "a quarter of your time" over months.
- **Hosted platform:** subscription that scales on multipliers: editors or seats, sites or projects, readers for gated audiences on some plans, and paid tiers that gate features (SSO, customer-only pages, multi-author review, custom domain, AI features). A second docs site (a help center, a second product) can cost as much as the first.
- Compare multipliers against the team's own counts now and in a year; never compare list prices.

## Lock-in surfaces

- **Proprietary components:** admonition, tab, callout and variable syntax specific to one platform must be converted on exit. Count them in the pilot.
- **Export gaps:** some hosted exports omit images or navigation, or need several files; test the export, do not read about it.
- **Content location:** a Git repository you own exits cheaply; a vendor database with export costs more; no export API costs most.
- **Editor hosting:** an open-source renderer does not mean a self-hostable editor; content can still live with the vendor, which fails residency and air-gapped requirements.
- **URL shape:** generators impose path rules (trailing paths, index-file names, organization-wide unique slugs); list the URLs the next platform must reproduce.
- **Generated reference:** keep the spec as the source; regenerate on the new platform instead of migrating rendered pages.

## Integration note: example products per class

Examples only, not a ranking. Products, plans and limits change; verify every knockout against the vendor's current docs during Step 4.

- Hosted docs platforms: Mintlify, GitBook, ReadMe, Fern, Document360.
- Managed hosting for an open-source generator (removes hosting, not upgrades or the owner): Read the Docs, general static hosts.
- Git-backed web editing on a generator: the code forge's web editor with pull-request previews, Git-backed CMS layers such as Decap CMS.
- Self-hosted docs generators: Docusaurus, MkDocs with Material, Sphinx, Astro Starlight, VitePress, Hugo with Docsy, Nextra, Antora.
- Spec-driven reference portals: Redocly, Scalar, Stoplight, Bump.sh, Swagger UI.
- Knowledge-base CMS: help-center products bundled with support desks, Confluence-style wikis.
- Custom build: a docs application on a general web framework, often with a content format such as Markdoc or MDX.
