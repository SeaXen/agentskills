# Docs platform decision: Halvane Robotics developer docs

**Status: unvalidated.** I wrote this in one pass without the interview or the section-by-section sign-off the skill asks for. Every `ASSUMED` item below should be confirmed before you act on the decision.

## Decision

**Don't build a custom Next.js docs app. Use a self-hosted docs generator, with a Next.js-based one first in the pilot.** The Doxygen output goes into the same site, and the whole site sits behind the customer portal login. Pilot a hosted platform alongside it as the fallback.

- This keeps what the CTO wants: Next.js, the marketing look, and portal login.
- It avoids the part that doesn't fit: owning a docs application with 3 part-time devs and a 10-week deadline.
- It only holds if the web team names an owner (see Blockers).

## Assumptions to confirm

1. **Build owner.** "The web team can help" does not count as an owner. I assumed one named dev with about 8 hours a month (baseline). If nobody commits, the class flips to hosted.
2. **Gating.** I assumed all or most docs sit behind portal login, and readers are external customers.
3. **Current docs.** I assumed 150 pages already exist in some source format. The platform, traffic and inbound links are unknown.
4. **Writers.** I assumed they can work in Markdown with pull-request previews. Their Git comfort is unknown.
5. **Content shape.** Versions per SDK release, locales, and PDF or offline output are all unknown. I assumed multiple SDK versions, no locales, and no PDF.
6. **Reference share.** I don't know how much of the 150 pages is the Doxygen reference. If it is most of them, the spec-driven reference class gets promoted.
7. **Vendor evidence.** I did not check any vendor docs or pricing. Every product capability below is `claimed` until the pilot.

## 1. Root cause

- **Trigger:** a wish list (CTO preference), not a pain on a current site.
- **Pain routing:** no findability, SEO, sample or agent-docs pains were reported, so nothing routes out. If pains appear later, route them to `developer-docs-structure-audit` or `docs-seo`.
- **Real platform constraints:** two, both capability tests.
  - The site must match the marketing look.
  - The site must sit behind the customer portal login.
- **Third constraint:** Doxygen C++ reference output.
- **Neither of the first two needs a custom build to be met.** Both are pilot tests.

## 2. Requirements register

Weights are fixed here, before any scoring.

| # | Requirement (outcome) | Source | Type | Test | Weight | Evidence |
|---|---|---|---|---|---|---|
| 1 | A logged-out reader cannot reach a gated page by URL, search or sitemap; a portal test account can | CTO, portal login | knockout | Gated-page test with SSO test account | - | claimed |
| 2 | C++ reference regenerates from source via Doxygen in CI with no hand edits | Content shape | knockout | Real Doxygen output renders; a header change appears after a rebuild | - | claimed |
| 3 | Header, footer, design tokens, analytics and consent banner match the marketing site | CTO, brand match | knockout | Pilot page shows all four | - | claimed |
| 4 | A writer publishes a one-line fix, and a reviewer approves from a preview first | 2 writers | knockout | Timed unaided edit and preview approval | - | claimed |
| 5 | Full 150-page build plus Doxygen output completes | Scale | knockout | Full-size build, minutes recorded | - | claimed |
| 6 | Live in 10 weeks with the pilot done by week 3 | Horizon | knockout | Schedule below holds at the week-3 gate | - | assumed |
| 7 | Export returns content, assets and navigation | Standing row: exit cost | knockout | Export diff against source | - | claimed |
| 8 | Top 10 old URLs resolve or 301 | Standing row: URL preservation | knockout | URL check | - | claimed |
| 9 | Owner named, within about 8 h/month | Standing row: owner | knockout | Named person, one dependency upgrade during the pilot | - | assumed |
| 10 | Search finds the right page for real queries, guides and C++ reference | Differentiator | differentiator | 10 real queries, right page in the top 3 for at least 8 | 3 | claimed |
| 11 | One-off effort headroom: pilot done and the cutover buffer kept | Differentiator | differentiator | Hours spent against plan | 3 | assumed |
| 12 | SDK version selector with banners | Content shape | differentiator | One page per live version | 2 | assumed |
| 13 | Build under 5 minutes at full size | Differentiator | differentiator | Build timing | 2 | claimed |
| 14 | Markdown and `llms.txt` surfaces | Differentiator | differentiator | Fetch both | 1 | claimed |

Pass thresholds are the ones in the pilot protocol: the fix is published with no developer help, and nothing goes live before approval.

## 3. Classes considered

| Class | Verdict | Why |
|---|---|---|
| Stay and fix | Not applicable | No current platform or pain was reported. |
| **Self-hosted docs generator** | **Recommended** | It fits a named owner, SSO-gated pages and brand sharing. Content stays in your Git, with no seat pricing. |
| Hosted docs platform | Fallback, piloted | It fits the 10-week date (it is inside a quarter) and has no build to maintain. The risks are Doxygen support, the gated-page tier, and per-reader pricing for external customers. |
| Spec-driven reference portal | Partial | Doxygen is the reference source. Treat it as a hybrid only if the reference is most of the site. |
| Knowledge-base CMS | Deleted | Weak for code-heavy SDK docs. |
| **Custom Next.js app** | **Deleted** | See below. |

**Why the custom build loses.** The skill allows a custom build only with a funded owning team and a written list of what no other class can do.

- **No funded team.** Three devs who "can help" is not one. HubSpot called this "an accidental docs platform team".
- **Only one real candidate for the list.** Page-level auth shared with the portal is the single argument. Requirement 1 tests whether the chosen generator, running on Next.js with middleware, can do it. If requirement 1 fails in the pilot for every candidate, reopen the custom build, with a funded team and a written list.
- **Brand match needs no custom app.** It needs a shared design-token or component package. Any candidate can consume one.
- **The deadline.** Search, versioning, previews, the Doxygen pipeline, auth and the 150-page migration are all work that a generator already provides. A 10-week build on top of the launch is the largest schedule risk.

**What flips the recommendation.**
- **No named owner:** hosted wins.
- **Reference is most of the 150 pages:** the hybrid is promoted.
- **Hosted fails requirement 1 or 2:** it is out.

## 4. Shortlist

Candidates come from the class lists in the skill's references. Verify each against the vendor's current docs and pricing page before spending pilot time.

- **A, self-hosted:** Nextra. It is the Next.js-based generator in the skill's list, so it shares the stack and components with the marketing site. Fallback inside the class: Docusaurus or Astro Starlight if Nextra fails a knockout.
- **B, hosted:** one of Mintlify, GitBook or ReadMe. Pick the one whose published docs claim a gated or SSO tier and a way to host custom reference HTML.

**Pricing multipliers for B** (no prices quoted):
- editors: 2 writers now, assumed 4 in a year
- sites: 1
- gated readers: external customers, potentially priced per reader
- plan tier required for SSO or customer-only pages
- custom domain
- AI features

Doxygen is the likely hosted-platform failure. Do not assume it works.

## 5. Pilot (weeks 1–3)

Run two candidates, not three, because the live date is inside a quarter.

**Page set (7 pages, ported to A and B):**
1. The page with the most custom components or embedded widgets.
2. One Doxygen-generated C++ class page, from the real source.
3. The quickstart.
4. One page that differs between SDK versions.
5. The longest page.
6. A gated page.
7. A page with the shared header and consent banner.

**Tasks:**
- the least technical writer publishes a fix
- a reviewer approves from a preview
- a full-size build or import runs
- 10 real search queries
- an export test
- 10 old URLs
- a gated page checked logged out, in search and in the sitemap
- a count of proprietary components needed

Any failed knockout removes the candidate. Score the differentiators with the weights above. Record the component count as exit-cost evidence.

## 6. Cost

| Cost | A: self-hosted generator | B: hosted platform |
|---|---|---|
| Standing | Owner about 8 h/month (baseline): upgrades, plugins, search, security, CI. No subscription. | Owner about 2 h/month (baseline) plus the multipliers above against 2 editors now and about 4 in a year. |
| One-off | Template and token package, MDX conversion, Doxygen CI step, auth middleware, redirect map, freeze window. | Import or port, Doxygen hosting workaround, redirect map, freeze window. |
| Exit | MDX in your repo. Nextra-specific components are the exit-cost count from the pilot. | Count of vendor blocks. Test the export. |

Both are measured against the Horizon ceiling. I don't have the user's ceiling, so I assumed 8 h/month standing and a 3-week pilot (both baseline). If either is exceeded, move to the next class.

## 7. Schedule (baseline, 10 weeks)

| Weeks | Work |
|---|---|
| 1–3 | Pilot A and B on the 7-page set. **Gate at end of week 3:** all knockouts tested, class and product decided. |
| 3–7 | Port the 150 pages, wire Doxygen into CI, add auth middleware, apply the design tokens. |
| 7–8 | Redirect map, search tuning, accessibility check, staging review. |
| 9 | Short content freeze (hours, not days), cutover. Old docs stay live in parallel until verified. |
| 10 | Launch, with a rollback path to the old docs. |

If the gate slips past week 3, drop B and take the least-risk path that passed.

## Decision record

- **Decision:** self-hosted docs generator (Nextra first), owner `<name, needed>`, live by launch week 10. Hosted platform is the fallback.
- **Trigger and root cause:** wish list. No content or structure pain was reported, so nothing is routed out.
- **Requirements:** register above. Results per candidate are filled in during the pilot.
- **Classes fell because:** see the table in section 3.
- **Pilot results:** pending.
- **Cost:** standing about 8 h/month, one-off per the table, exit per the pilot count.
- **Owners:** standing owner `<needed>`; migration owner `<needed>`.
- **Assumptions:** list at the top.
- **Revisit trigger:** owner leaves; editors past about 6; a requirement 1 or 2 regression; Nextra direction or maintenance changes; the reference grows to most of the site.
- **Handoffs:**
  - Redirects and indexing at cutover go to `docs-seo`.
  - Which SDK versions migrate goes to `docs-versioning-strategy`.
  - Locales go to `docs-localization-strategy`. Not needed if there are none.
  - `llms.txt` and markdown surfaces go to `coding-agent-docs-optimization`.

## Blockers to clear first

1. **Name the owner.** Which dev, how many hours a month?
2. **Confirm what is gated.** All docs, or only some? Are readers all external customers?
3. **Confirm writers' Git comfort.** Without it, requirement 4 pushes toward a Git-backed web editor or a hosted platform.
4. **Tell me the current platform and traffic.** This sets the redirect map and the migration effort.

## Sentence for the CTO

> You get Next.js, the same look as the marketing site, and portal login, by building on a docs framework instead of a docs product of our own. A custom app would need a funded team for the life of the docs, and the launch date has no room for one.