# Recommendation: docs platform and findability

## Decision

**Don't pick a hosted platform yet. Fix findability on MkDocs first, then decide.** If leadership still wants to move after that, choose **Mintlify**.

Nothing in your data shows that the platform is the cause. The three zero-result queries point at content and search configuration:

| Zero-result query | Likely cause | A new platform fixes it? |
|---|---|---|
| `pgvector` | Page missing, or documented as "vector search" or "extensions" | No. Missing content stays missing. |
| `connection pooling` | Documented under another name ("pooler", "connection strings", "PgBouncer") | Only if its AI search handles synonyms. A search config change does the same. |
| `branching limits` | The limits sit inside the Billing FAQ or a quotas table, not on a page titled that way | No. This is an information architecture problem. |

I could not see your repo or search logs, so these causes are hypotheses. A quick grep for each term settles which one applies. Moving 640 pages without knowing risks paying for a migration and still seeing the same NPS comments.

## Step 1: Fix findability (2–3 weeks, about 1 writer plus 1 engineer)

1. **Triage the zero-result log.** Pull the top 100 zero-result queries and tag each as:
   - **missing content**
   - **vocabulary mismatch** (users say X, docs say Y)
   - **buried content** (the answer is inside a long page)
2. **Write the missing pages.** `pgvector` is almost certainly a standalone page, because users expect to search it by name. Add a "Limits and quotas" reference that covers branching, connections and storage in one place.
3. **Split the Billing FAQ** into one page per question. Search ranks whole pages, so a giant FAQ page matches everything weakly and nothing strongly. Redirect the old anchors.
4. **Add synonyms and keywords.** Put alternate terms in page titles, descriptions and the first paragraph. Material's built-in search has no synonym support, so this is the cheap fix.
5. **Replace or augment search if step 1 shows vocabulary gaps.** Pick one:
   - Algolia DocSearch (free for open-source docs only; paid otherwise)
   - Pagefind or Typesense (self-hosted)
   - An AI answer layer such as Kapa, Inkeep or Algolia AskAI

   All of these plug into MkDocs. Your 3 writers and the PR workflow stay as they are.
6. **Review zero-result queries weekly.** Assign an owner and make it a 20-minute ritual.

## Gate before any migration

Re-measure after 4 weeks.

| Metric | Target |
|---|---|
| Zero-result rate on site search | Down by more than half |
| Search-to-click rate | Up |
| NPS comments tagged "can't find" | Down in the next survey wave |

If these move, the platform was never the problem. If they don't, you have evidence for a move, plus a cleaned content set that migrates better.

## If you move anyway: Mintlify

I'm recommending Mintlify, with the caveat that **I did not verify current pricing or feature details**. Get live quotes before committing.

Why Mintlify fits you:
- **Git-based.** Engineers keep contributing via PRs and writers keep their review flow, so there is no CMS-only workflow to retrain on.
- **AI search and assistant are built in**, rather than bolted on. It also generates `llms.txt` and MCP access for coding agents.
- **Managed hosting and previews** replace your 90-second build.
- **Developer-docs focus**, including API reference from OpenAPI.

Alternatives I'd reject for you:
- **GitBook:** better for editor-led teams. Your engineers-via-PR model fits it less well.
- **ReadMe:** strongest for API-product docs. It is a worse fit for a database's guides-heavy content.
- **Docusaurus + Algolia:** this is not hosted and not a real gain over what you have.

## Migration costs leadership should hear

- **Syntax conversion.** MkDocs-specific features (admonitions, content tabs, snippets, macros) must be converted to MDX components. Budget a script plus manual review for roughly 640 pages.
- **URL redirects.** Every old URL needs a redirect, or you lose SEO and break links in support tickets.
- **A content freeze** of one to two weeks during cutover.
- **Vendor lock-in.** The AI search quality and pricing are the vendor's to change. Ask about per-query AI costs and about export.
- **Migrating first fixes nothing.** Convert the content, and the Billing FAQ is still one giant page.

## One timing risk to check

As of my knowledge, the Material for MkDocs maintainers announced the project is moving to maintenance mode as they build a successor, Zensical. Confirm the current support window on the project's site. If critical fixes end soon, you need a platform plan regardless. In that case compare three options:
- Zensical (a likely low-effort path, since it reads existing `mkdocs.yml` config)
- Mintlify
- Staying on Material and accepting the risk

That decision is about tooling longevity. Keep it separate from the findability problem so one doesn't hide the other.

## Next actions

1. This week: grep the docs for the three queries and tag the top 100 zero-result queries.
2. This week: confirm Material's support timeline.
3. Weeks 1–3: run steps 1–6 above.
4. Week 4: run the gate review. Move to Mintlify only if the gate fails or the Material timeline forces a move.