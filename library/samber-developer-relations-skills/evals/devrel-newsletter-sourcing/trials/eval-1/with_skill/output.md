# Candidate sheet: Ferrolink developer digest

**Thin-issue call:** not thin. 2 of the 3 required sections reach their minimum (Shipped and From the community). Recommend shipping shorter, with Learn dropped under the default empty-section rule. I applied that rule because you didn't state one.

**Action-required item:** Node SDK 6.0.0 removes v1 auth header support. It leads the issue under Heads-up. The skill forbids skipping the issue while an action-required item is open.

## Header

- **Window:** 2026-04-30 12:00 UTC to 2026-05-27 12:00 UTC.
  - I assumed the last cutoff was noon on the send day, since no cutoff was recorded.
  - I assumed UTC, and a send on Thursday 2026-05-28 (inferred from the item dates).
  - If the real send date is later, tell me. A longer gap changes the window.
- **Channels:**
  - Pasted by user: 10 items.
  - Not read by me: ecosystem and advisory feeds for the Node, Python and Go runtimes, the submissions inbox, the merged-PR and unlabelled-merge sweep, and the support and docs-search logs.
  - Events: no section, so no calendar.
- **Found 10, kept 4, held 2, cut 4.**
- **Link state:** every link is `user-supplied, not opened`. The pre-send check must open each one and swap in the page's own title.
- **Own vs external:** 3 own, 1 external, which is 25% against the one-third floor. That is a **shortfall** (see Open questions).

## Issue order (kept)

| # | Section | Item | Rung |
|---|---|---|---|
| 1 | Heads-up | Node SDK 6.0.0 removes v1 auth header support | 1, action required |
| 2 | Shipped | Payouts API GA docs page | 2 |
| 3 | Shipped | Python SDK 3.4.0 release notes (async client) | 2 |
| 4 | From the community | Idempotent refunds with Ferrolink in Go (dev.to) | 3, external |
| – | Learn | Dropped for now (0 of the minimum 1) | – |

Payouts goes before Python 3.4.0 because it fits every reader, not just Python users.

## Full sheet

| # | Item | Primary link | Origin | Date | Rung | Section | Verdict | Reason |
|---|---|---|---|---|---|---|---|---|
| 2 | Node SDK 6.0.0 changelog entry | ferrolink.dev/changelog#node-6-0-0 | own changelog | 2026-05-14 | 1 | Heads-up | **keep** | Breaking change, in window. Its scope is an open question (see Q1). |
| 1 | HN: "Ferrolink quietly killed API v1 auth headers" | news.ycombinator.com/item?id=4410921 | HN | date unknown | – | – | **cut** | Commentary on #2. The primary page is the changelog. 412 points never raises a rung. |
| 4 | Payouts API GA docs page | ferrolink.dev/docs/payouts | own docs | 2026-05-20 | 2 | Shipped | **keep** | GA release, public. |
| 3 | CEO tweet announcing Payouts GA | x.com/ferrolink_ceo/status/18822 | social | date unknown | – | – | **cut** | Social post. Collapsed into #4. |
| 9 | Python SDK 3.4.0 release notes | github.com/ferrolink/ferrolink-python/releases/tag/v3.4.0 | own releases | 2026-05-02 | 2 | Shipped | **keep** | New capability: async client. |
| 6 | Idempotent refunds with Ferrolink in Go | the dev.to post | dev.to | 2026-05-09 | 3 | From the community | **keep** | External, the author's own post, in window. Check at pre-send that it has no affiliate or sponsor stake. Check that its code still works on Go SDK 2.8.x. |
| 7 | DailyDevLinks repost of #6 | aggregator entry | aggregator | date unknown | – | – | **cut** | Duplicate of #6. The aggregator is not the primary source. |
| 5 | "9x faster than every payments API" (Medium) | the Medium post | Medium | date unknown | – | – | **hold** | Authenticity gate. It is a benchmark from a 3-week-old account and shows no method, no author history and no disclosed stake. A post that flatters Ferrolink reads as our endorsement. 2.1k claps is not a quality signal. |
| 8 | Forum: "Is anyone else seeing 429s on webhooks?" | forum thread | own forum | date unknown | – | – | **hold** | Its rung depends on a fact I lack: is this a limit change or an incident readers hit (rung 1), or a repeated question (Learn)? See Q2. Being the most upvoted thread this month does not matter. |
| 10 | Go SDK 2.8.1 | release page | own releases | 2026-05-22 | below 4 | – | **cut** | A typo fix in an error message has no reader consequence. |

**Duplicate gate:** every kept item is dated after the 2026-04-30 issue, so none can repeat that issue. The two issues before it are unknown, but they are older still. No kept verdict is provisional.

## Hold list

- **#5 Medium benchmark:** expires when the next window closes, about 2026-06-24 12:00 UTC (assumes a monthly Thursday send on 2026-06-25). To release it, it needs a stated method, the author's history, and any stake disclosed. I would not chase it.
- **#8 Forum 429 thread:** same expiry. It is released by the answer to Q2.

## Open questions

1. **Scope of the v1 auth removal (affects the lead item).** The HN title says "API v1 auth headers", but our changelog entry only says Node SDK 6.0.0. Did the API itself stop accepting v1 headers, and from what date? If so, Python and Go users are affected too. The Heads-up should then link the API changelog or a migration page, not just the Node entry. Send me that URL.
2. **The 429 thread.**
   - Is there a real webhook rate-limit change or incident behind it?
   - Is there an existing docs page on webhook retries or limits? That would be a good Learn item, because the thread is a dated trigger inside the window. Send me the URL.
   - Does a user-written thread on our own forum count as "external" under your charter?
3. **External share shortfall (25% against one third).**
   - The only passing external item is #6. Dropping an own item would break Shipped's minimum of 2 or the action-required item, so I did not swap.
   - Two ways to fix it before Thursday. Check the submissions inbox, and read the Node, Python and Go advisory feeds. Or ask the charter owner whether the forum thread counts as external.
   - Adding the 429 docs page to Learn and one more external item would give 2 of 6, which meets the floor.
   - If neither lands, ship with the shortfall stated and raise it with the programme owner as a charter question.
4. **Charter gaps assumed:**
   - Charter empty-section rule: assumed to be "drop the section".
   - Evergreen slot: assumed the charter names none, so I did not use one.
   - Primary reader: assumed to be developers integrating Ferrolink.
   - Off-limits list: none given, and Payouts is public, so I assumed none.
   - Last three issues: not given.

## Before Thursday

- Open every kept link, and swap in each page's own title and the exact GA date for Payouts.
- Re-open the three time-bound items (Node 6.0.0, Payouts GA, Python 3.4.0) on send day, in case any was yanked or revised.
- Record this cutoff (2026-05-27 12:00 UTC) so the next run starts from it.