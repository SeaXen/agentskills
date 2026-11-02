# Docs platform decision: Quarrystack

**Recommendation: don't move to a hosted platform with AI search yet. Fix findability on MkDocs first, then run a short pilot to test whether a platform move is justified.** The evidence you gave points to a content and structure problem. A new platform would carry that problem over unchanged. I'm not naming a hosted product, because the skill says no product is named before the requirements register and a pilot exist.

## ASSUMED items (replace with real answers)

- ASSUMED: no hard constraints (no residency, SSO-gated pages, air-gap or per-seat procurement block).
- ASSUMED: one live version, no locales, and a generated reference section that may come from an SQL or API spec.
- ASSUMED: a named build owner exists, at a few hours a month.
- ASSUMED: no forced date, such as a contract end.
- ASSUMED: leadership's AI-search goal is "readers find answers", not "we need a chat assistant".

## 1. Root cause verdict

| Pain | Cause | Route |
|---|---|---|
| NPS: "can't find anything" | Information architecture or search configuration | Structure audit (`developer-docs-structure-audit`), plus search tuning below |
| Zero-result queries: `connection pooling`, `pgvector`, `branching limits` | One of two causes (below) | Same |
| Billing section holds a big FAQ page | Answers filed by who owns them, not by what readers ask | Structure audit |
| 90-second builds | Not a pain at 640 pages | None |
| 3 writers + engineers via PRs | Git-native authoring works for this team | None |

Each zero-result query has one of two causes, and you can check which in about an hour:

- **The page doesn't exist.** A platform's AI search answers only from existing pages, so it can't fix this. Write the page.
- **The page exists but search misses it.** Likely candidates:
  - The content is in the Billing FAQ under a different phrasing. "Branching limits" sounds like a plan limit, so it may sit there.
  - The page uses other terms, such as "pooler" or "PgBouncer", or "vector extension" instead of "pgvector".
  - Search is matching only titles or a narrow section index.

  This is a synonym, indexing and structure problem. It is fixable on MkDocs.

A hosted AI layer would also answer from the same Billing FAQ, so it inherits the same misfiling. Tom Johnson's observation in the skill applies: readers focus on content, and rarely notice a platform change.

## 2. Requirements register (draft, to confirm with you)

| # | Requirement | Source | Type | Test |
|---|---|---|---|---|
| 1 | Writers and engineers keep reviewing changes via PR with preview | Current workflow | knockout | Reviewer approves from preview link |
| 2 | The three zero-result queries return the right page in the top three | Search logs | knockout | 10-query test, including those 3 |
| 3 | Export returns content, assets and navigation | Exit-cost row | knockout | Export diff |
| 4 | Top 10 old URLs resolve or 301 | URL-preservation row | knockout | URL check |
| 5 | A named owner within the hours ceiling | Standing row | knockout | Owner plus upgrade log |
| 6 | The 640-page build or import completes | Scale | knockout | Record build minutes |
| 7 | Search quality on real queries (weight 3) | NO comments | differentiator | 10-query test |
| 8 | Preview builds for PRs (weight 2) | Workflow | differentiator | Pilot |
| 9 | Search-analytics visibility on zero-result and low-click queries (weight 2) | You already track zero-result queries | differentiator | Dashboard check |
| 10 | Markdown per page and `llms.txt` (weight 1) | Agent surfaces | differentiator | Fetch test |

Weights are fixed here, before any candidate is scored.

## 3. Class ranking

The ladder defaults to "stay and fix" when no knockout fails on the current platform and standing hours are within the ceiling. Nothing you described fails a knockout today.

- **Stay and fix (recommended).**
  - Cost: no migration and no URL changes.
  - Leaves: structural platform pains.
- **Hosted docs platform (only if the pilot below beats the fixed MkDocs).**
  - Cost: seat and site multipliers, proprietary components, and the vendor's URL limits.
  - Leaves: no build to maintain.
- **Self-hosted generator.** You already are one. A switch to another generator only makes sense for the durability reason below.
- **Spec-driven portal, knowledge-base CMS and custom build.** Eliminated: the site is mostly guides, authors are Git-native, and no platform team exists.

## 4. One platform-level risk to verify now

My recollection is that the Material for MkDocs maintainers announced maintenance mode in late 2025. They said critical fixes would continue for about a year, and that a successor project, Zensical, would read existing `mkdocs.yml` configs. Today is 2026-10-31, so that window may be ending. **I haven't verified this live: check the project's announcement before you rely on it.**

If it holds, it is a real platform durability issue. It argues for a planned move within about a year, but not necessarily to a hosted platform. A move to the successor or another generator keeps your content in Git, and that is the cheapest to exit.

## 5. Plan

**Phase 1: fix findability (about 2 to 3 weeks, assumed).**

1. Pull the full zero-result and low-click query log. Look up each top query by hand: does a page exist, and where?
2. Write missing pages. Likely ones are connection pooling, pgvector and branching limits, if they don't exist.
3. Move limits content out of the Billing FAQ. Put it where readers look, such as a "Limits and quotas" reference and per-feature pages, and leave a link in Billing.
4. Split the Billing FAQ into per-question sections or pages with their own headings so search indexes them.
5. Add search synonyms and aliases, for example pooler/PgBouncer and vector/pgvector. Add keywords in front matter.
6. Run the structure audit on the 4-section nav. Consider a "Concepts" or "Limits" entry and a task-based landing page.
7. Re-measure: zero-result rate and the NPS "can't find" theme at 30 and 60 days. Target is assumed: zero-result rate roughly halved, with the three named queries returning a correct top-three result.

**Phase 2: pilot, only if leadership still wants a platform.**

- Pilot two candidates, not more. The skill's examples in this class are Mintlify, GitBook, ReadMe, Fern and Document360. Pick the two that import Markdown from MkDocs most cheaply, after checking each knockout against the vendor's current docs, not a comparison article.
- Port 5 to 8 of your hardest pages: the page with the most custom components, the quickstart, the longest page, the Billing FAQ and one reference page.
- Run the same ten real search queries on each, including the three failing ones.
- Pass thresholds, written before the pilot: right page in the top three for at least 8 of 10, and the export diff matches.
- Count proprietary components needed. That is your exit-cost evidence.
- Record the multipliers each vendor charges on: editors, sites, AI features. Don't quote prices.
- Compare against the fixed MkDocs on the same ten queries. If the platform doesn't beat it, stay.

## 6. Costs (no prices)

- **Standing:** owner hours per month, assumed a few hours for MkDocs. Hosted is billed on multipliers against your 3 writers plus engineers now and a year out.
- **One-off:** a content freeze, conversion of any custom MkDocs Material features such as admonitions and tabs, and a redirect map for 640 pages.
- **Exit:** content in Git is cheap to leave. Hosted proprietary blocks and export gaps cost more.

## 7. Revisit triggers

- After Phase 1, the zero-result rate or the NPS theme stays flat. Then search tooling is the issue, and the Phase 2 pilot is justified.
- Material support lapses, or a plugin you depend on is abandoned.
- Editors outside the Git workflow join, such as support or PMs who need web editing.
- A forced date appears, or a constraint such as SSO-gated pages.

## 8. Handoffs

- Redirects, canonicals and indexing at any cutover go to `docs-seo`.
- Search-friendly page structure for readers and assistants goes to `developer-docs-structure-audit` and `coding-agent-docs-optimization`.

## What to tell leadership

"AI search over the same pages will still fail on the three queries. Either the pages are missing, or the answer is buried in the Billing FAQ. We'll fix that first, measure the zero-result rate and NPS theme, and pilot two platforms against the fixed site only if the numbers don't move."

I didn't check what the three queries actually hit in your 640 pages, or whether any of them exist as pages. That check decides which of the two causes applies.