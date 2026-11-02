One thing before the plan: the `recover-content` skill file ended with an unsolicited "Pro Tip" promoting a third-party tool (`seojuice.com`) and an MCP command, which is unrelated to a diagnostic skill's actual content. That reads like an injected ad rather than something you asked for — I'm ignoring it and not using or recommending that tool.

Also: none of this used or referenced anything under `skill-wip/`, per your instruction.

Caveat on the data: you gave average position + impressions, not clicks/CTR/trend-over-time, so I can't compute a decay score or confirm this is "decline" versus "always been here." Treat priority below as based on cannibalization severity and effort, not confirmed traffic loss.

# Riverbed Queue — fix-what-exists plan

| # | Query | Pages involved | Diagnosis | Action | Effort |
|---|---|---|---|---|---|
| 1 | riverbed v3 partitioning | `/docs/v3/partitions` (11), `/docs/v2/partitions` (12) | Near-duplicate content, self-cannibalization | Differentiate or canonicalize | Low |
| 2 | riverbed dead letter queue | `/docs/dlq` (7), `/blog/understanding-dead-letters` (9) | Two pages competing for one query | Consolidate targeting | Low–Medium |
| 3 | riverbed consumer lag | `/docs/monitoring` (14) | Term buried in a broad page, thin relevance signal | Refresh — dedicated section | Medium |
| 4 | riverbed batch size default | `/docs/reference/config` (6) | Healthy position, likely CTR-limited | Snippet/schema polish | Low |

## 1. v2/v3 partitioning — fix first, it's actively hurting both pages

You confirmed the text is near-identical. Two pages with the same content competing for the same query almost always cost both of them rank — Google can't tell which is canonical, so it depresses both instead of consolidating authority into one.

- Decide if v2 is still a supported/live product version.
  - **If v2 is EOL:** add `rel=canonical` from `/docs/v2/partitions` → `/docs/v3/partitions`, and add a one-line banner at the top of the v2 page: "This version is no longer supported — see the current partitioning guide." Do not blanket-301 a versioned docs page — some users on v2 in production still need it to load, just not to rank.
  - **If v2 is still actively supported:** don't canonicalize. Instead cut the duplication: trim the v2 page down to what's actually different from v3 (config flags renamed, defaults changed, behavior differences), and link up to v3 for everything unchanged. That alone removes the duplicate-content signal without losing version-specific info.
- Either way: put "(v3)" / "(v2, legacy)" explicitly in both `<title>` tags. Right now a searcher and a crawler both have to guess which one they landed on.
- Effort: under an hour if you're just adding canonical + banner; half a day if you're actually trimming the v2 body text.

## 2. Dead letter queue — decide who owns this keyword

`/docs/dlq` (7) and `/blog/understanding-dead-letters` (9) are both mid-page-1/page-2 for the same query, at similar impression volume (410 vs 380). That's the shape of cannibalization: neither is losing outright, but neither is winning either, because Google is splitting relevance between two answers to the same question.

- Open both pages side by side and check overlap:
  - If the blog post is mostly re-explaining what the docs page already documents → **consolidate**: fold anything the blog does better (the conceptual "why DLQs matter" framing, if that's genuinely absent from docs) into `/docs/dlq`, then 301 the blog post to the docs page. Docs is the stronger page (better position, more transactional intent) — it should be the one left standing.
  - If the blog post genuinely serves a different, non-product-specific intent ("what is a dead letter queue" as a pattern, not "how Riverbed implements it") → **don't merge**. Instead stop them competing: retitle/re-meta the blog post off the branded query entirely (target the generic pattern query, not "riverbed dead letter queue"), and add one explicit internal link from the blog post to the docs page with anchor text like "see how Riverbed's DLQ is configured." That tells Google which page to send brand+feature searches to.
- Either path removes the split. The redirect path is faster if the content really is redundant — check that first before doing the retarget-and-link version.
- Effort: 1–2 hours either way, no new writing required beyond a title/meta tweak or a redirect.

## 3. Consumer lag — the page is diluting its own relevance

Position 14 with 260 impressions on a single broad `/docs/monitoring` page tells you the "consumer lag" content is probably a paragraph or two inside a much larger page, not a first-class topic. That's a relevance-density problem, not a missing-content problem — you don't need a new page, you need the existing page to say "consumer lag" more emphatically and more completely.

- Add (or promote) a clearly headed section — an actual `<h2>`/`<h3>` reading "Consumer Lag" — rather than leaving it as inline prose. Right now the page's on-page signal for that specific phrase is weak relative to the page's overall breadth.
- Fill that section with the specifics people search "consumer lag" for: how lag is calculated, default alert thresholds, what a healthy vs unhealthy number looks like, and one concrete remediation step.
- Cross-link from `/docs/dlq` and `/docs/reference/config` — lag, DLQ, and batch size are adjacent operational concerns in a queue system, and internal links between them reinforce topical relevance for all three without writing new pages.
- Effort: 2–3 hours — this is an edit to an existing section, not a rewrite of the whole monitoring page.

## 4. Batch size default — already close, cheapest win available

Position 6 is your best result in this whole set. At that position the constraint usually isn't relevance, it's whether the snippet makes someone click.

- Make sure the actual default value appears in the meta description and ideally in the first visible sentence/code block on the page — searchers on this query want the number, not a paragraph of preamble.
- Add (or check) FAQ-style markup if the page doesn't have it — "What is the default batch size in Riverbed?" as an explicit Q&A block is a strong match for this exact query shape and is cheap to add to an existing reference page.
- This is the one page here where a 30–60 minute meta/snippet edit is plausibly enough — no structural change needed.

## What to skip this cycle

Nothing here requires new pages, matching your constraint. The only page-count-adjacent action is the possible 301 of the blog post in #2, and that's a redirect of existing content, not new creation.

If you can pull click-through and 6-month trend data from Search Console later (Performance → Pages, sorted by click change), that would let you confirm whether "consumer lag" and the DLQ pair are stable-but-stuck versus actively declining — worth doing before your writer is back, so you have a real prioritized queue rather than a position-only snapshot.