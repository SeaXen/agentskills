# Docs structure audit — Stagpath Analytics, 2026-09-25

## Verdict

Three separate failures, not one messy docs site: a landing page that can't route a task-seeker, a page that makes three different readers wade through each other's content, and a whole SDK with no door in. The single biggest cost sits on the Node adoption path — 260 zero-result searches for "node getting started" in 90 days means Node developers are failing before they reach a single page. Three small, independent edits close the highest-confidence gaps; Reference needs no work at all.

This is a **partial, evidence-only pass** — five inputs supplied directly, no repository or site crawl run. Treat every "not evidenced" cell below as a real gap in what I could check, not a clean bill of health. Full gating questions (audience mix, generator, remediation capacity, redirect constraints, deadline) are listed at the bottom — answer those before this becomes the governed version of this audit.

## Section ratings (CNCF TechDocs scale, 1=not present → 5=exemplary)

Based on the one sampled page per section supplied — not a full section read. Treat as directional, not final.

| Section                  | Information architecture | New user content | Content maintainability | Content creation processes |
| ------------------------ | ------------------------- | ----------------- | ------------------------- | ---------------------------- |
| Guides (landing page)     | 2                          | n/e                | n/e                        | n/e                           |
| Access Control (concepts) | 2                          | n/e                | n/e                        | n/e                           |
| Node SDK                  | n/e                        | 1                  | n/e                        | n/e                           |
| Reference                 | 4                          | n/e                | n/e                        | n/e                           |

n/e = not evidenced from what was supplied. For calibration: CNCF's own 2024 published score for the TUF project's "New user content" was also a 1 — a 1 here is common for a project with no dedicated writer, not an alarm in itself.

## Scorecard

Most rows require a full inventory (file tree + nav config) that wasn't available this pass — left blank rather than guessed.

| Measure          | Now                                             | Target                   | Threshold source | Status |
| ----------------- | ------------------------------------------------ | ------------------------- | ----------------- | ------ |
| Entry points       | Node SDK has none                                 | 1 tutorial/quickstart per primary surface | Diátaxis        | fail   |
| Demand coverage    | 2/2 sampled queries unmet ("node getting started" 0 results; "how to" queries 71% exit on Guides) | ≥ 90%                      | agreed baseline    | fail   |
| Mode purity        | not computable sitewide; the one page inspected (access-control.md) holds 3 modes | ≥ 90%                      | agreed baseline    | fail (on sample) |
| Orphans / dead nav / broken links / nav depth | not assessed — no repo or nav config available | 0 / 0 / 0 / ≤3            | agreed baseline    | not assessed |
| ROT rate           | 1 confirmed Outdated flag (Go SDK samples, see "Not covered") | report, no target          | ROT heuristic       | partial |

## Coverage matrix

Rows are surfaces mentioned in evidence only — not the full product surface list (that needs question 5 answered).

| Surface         | Tutorial                          | How-to                          | Reference                    | Explanation                       |
| ---------------- | ---------------------------------- | --------------------------------- | ------------------------------ | ----------------------------------- |
| Node SDK          | **missing** — 260 zero-result queries/90d | 7 guides (present)                 | API reference (present)          | not evidenced                        |
| Access Control    | not evidenced                       | present, but bundled into concepts/access-control.md | present, but bundled into same page | present (diagram), but bundled into same page |
| Go SDK             | not evidenced                       | not evidenced                       | code samples present but non-compiling — **accuracy, not placement** | not evidenced                        |

Empty Tutorial on Node SDK is the most damaging cell here: it's a primary-surface entry point, not a minor feature, and the demand signal is unusually strong (260 in 90 days is above the volume that flagged the Python SDK gap in a comparable audit).

## Findings

**[must fix]** `concepts/access-control.md`

- Now: a permissions diagram (explanation), then 9 numbered steps to add a service account (how-to), then a 30-row permission table (reference). Three modes, one URL, and this is the #2 search landing page on the site.
- Reader impact: someone mid-incident adding a service account scrolls past a diagram and a 30-row table to find their 9 steps; someone evaluating the permission model for a security review hits procedural noise and leaves. Both are common needs, and both fail on the single highest-traffic page available to check.
- Next action: split into `concepts/access-control.md` (keep the diagram), `guides/add-a-service-account.md` (the 9 steps), `reference/permissions.md` (the 30-row table). Concept page keeps links to both. No SME arbitration needed — content already exists, it just needs relocating.

**[must fix]** No entry point for the Node SDK

- Now: 7 how-tos and an API reference exist; no tutorial or quickstart. Site search shows "node getting started" at 260 queries in 90 days with 0 results.
- Reader impact: a developer adopting the SDK from scratch — the group with the lowest tolerance for friction — has no supported first hour and is typing the exact words "getting started" into a search box that returns nothing.
- Next action: write a single-path quickstart to the first successful API call. Keep alternatives and configuration options out; link to the 7 how-tos for everything past "it works."

**[must fix]** `guides/index.md` (Guides landing page)

- Now: 41 ungrouped links, 14 conceptual and 27 procedural. Site search shows "how to" queries landing here at a 71% exit rate.
- Reader impact: someone arriving with a task scans 41 undifferentiated links and leaves for search instead of finding the procedure they came for.
- Next action: split the list into "Tasks" and "Concepts" groups on this page only. No files move, no redirects needed — this is a same-page edit.

**No finding** — Reference

- Credited as well-organized on the input given. Not independently re-verified page-by-page this pass; if a fuller audit runs later, sample it anyway rather than assuming it stays clean as the product grows.

## Not covered by this audit

- **Go SDK code samples not compiling.** This is an accuracy defect, not a structure or placement problem, and it's explicitly out of scope for this skill. Flagging it here so it doesn't get lost: route to whoever owns the Go SDK docs (engineering, most likely) for a compile-gate fix, and consider running `docs-code-sample-standards` once samples are green again to stop this recurring. Worth tracking as an Outdated (ROT) flag on the next full inventory pass.
- Prose quality, tone, translations.
- SEO/findability beyond the two search signals supplied (route to `docs-seo` if needed).
- Orphan pages, dead nav entries, broken links, nav depth — needs repo or nav-config access, which this pass didn't have.
- Any section not named in the four findings (unknown how many surfaces exist beyond Node SDK, Go SDK, Access Control, Guides).
- User validation (card sort / tree test) — not run. Every structural move above is **proposed**, not validated. If a tree test later shows >80% task success and >60% direct-path rate on these pages, stand down the splits and put the time into the Node quickstart and freshness instead.

## Remediation queue

Ordered by reader need fixed per hour of effort — not by severity, not by count of findings closed.

| # | Action | Page(s) | Mode outcome | Reader need fixed | Effort | Evidence |
|---|--------|---------|--------------|--------------------|--------|----------|
| 1 | Regroup Guides landing page into Tasks / Concepts | `guides/index.md` | how-to index, cleanly separated from concept links | reader stops scanning 41 flat links for one task | 1h, no files move | 71% exit rate on "how to" queries |
| 2 | Split access-control.md into concept + how-to + reference | `concepts/access-control.md` → +`guides/add-a-service-account.md`, +`reference/permissions.md` | explanation / how-to / reference | reader on the #2 highest-traffic page stops wading through two other readers' content | ~1 day, no redirect required (original URL keeps the concept content) | #2 site landing page, 3-mode mixing |
| 3 | Write Node.js quickstart | new: `tutorials/node-quickstart.md` | tutorial | Node adopters get a first-run path instead of a zero-result search | ~1 day + upkeep per release | 260 zero-result searches/90d — **promoted above its normal rank** (missing pages usually rank last on effort) because of the volume and because it's a whole-surface gap on the adoption path |

Nothing was deleted from this queue for redirect or capacity constraints — those constraints weren't answered (see below), so re-check row 2's redirect assumption once you know if URL stability is load-bearing here.

## Drift controls (recommend shipping with the queue, not after it)

- Declare content type in front matter (`concept` / `how-to` / `reference`) and validate it in CI, once the generator is confirmed.
- Ship a how-to and a tutorial template so the Node quickstart doesn't reinvent shape from scratch.
- Add a redirect for any future page move, even though none of the three actions above need one today.
- Put a CODEOWNERS entry on the SDK docs subtree — the Go sample rot suggests nobody currently owns "does this still compile."
- Re-run this inventory quarterly; a fix shipped once with no re-score is a document nobody trusts in six months.

## Inputs

- Supplied directly: page-level description of `concepts/access-control.md`; link count and grouping of the Guides landing page; SDK inventory count for Node (7 how-tos + reference, no tutorial); two site-search figures (71% exit on "how to," 260 zero-result "node getting started" queries/90d); a qualitative report that Reference is well-organized; a defect report on Go code samples.
- Not supplied, and gating a fuller pass per this skill: where the docs live (repo vs. site only), the generator, the full audience mix (self-serve vs. enterprise — inferred as likely both, given "service account" and "permission" language alongside an SDK-adopting audience), the full surface list beyond Node/Go/Access Control, whether user testing (card sort/tree test) is possible, remediation team size and hours/week, any URL-stability constraint, and a target date.
- No repository, nav config, or site crawl was read this pass — orphans, dead nav entries, broken links, and nav depth are unassessed, not clean.