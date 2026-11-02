# Docs Plan: Northwind SDK Integration

## Timeline, stated plainly
- Today: Fri Sep 18
- Northwind starts integrating: ~Sep 27 (9 days — falls on a Sunday, so their real first day is likely Mon Sep 28)
- Partner goes live: Wed Oct 14 (26 days out)
- Real runway: **9 days to ship a working doc set, then ~17 days of live support before launch.**

## The one call that makes this doable solo

Northwind's engineers live in Cursor. Cursor reads two things without touching your web team's build at all: the repo itself (README, `/docs`, inline comments, OpenAPI spec) and any URL added to its custom "Docs" index. Neither needs engineering time or the web team's pipeline — a technical writer with repo write access can ship both directly.

Treat the polished docs site as a slow, parallel track that is **not** on the critical path. That's the load-bearing decision everything below hangs off. Stop treating "the docs site" as synonymous with "the docs" — for this launch, they're two different deliverables with two different owners and two different deadlines.

## Three tracks, running in parallel

### Track A — Repo-native docs (critical path, all you, done by Sep 26)

Ship these directly into the SDK repo as markdown/comments, via normal PRs:

1. **README quickstart** — install → auth → first successful call. Target under 5 minutes end-to-end. Every code block copy-pasteable, no placeholder values that require guessing.
2. **Auth guide** — the #1 first-hour blocker on any SDK integration. Key generation, env var convention, test-vs-live key distinction, the two or three most common 401/403 causes.
3. **Error reference** — every error type Northwind is likely to hit, each entry answering *what happened / why / how to fix it*. Don't rely on the error message alone to carry this; put it in docs too.
4. **Core workflow examples** — the 3–5 calls Northwind will actually make, in their language. Confirm their stack directly with them or your PM this weekend — don't guess. Test every sample against a live sandbox yourself before it ships; you have no engineer to catch a wrong one for you.
5. **Changelog / stability note** — flag what's stable vs. still moving before Oct 14, so Northwind doesn't build against something that shifts under them mid-integration.
6. **`.cursor/rules` (or `AGENTS.md`)** — a short file encoding your SDK's non-obvious conventions: correct auth pattern, the specific misuse Cursor's autocomplete tends to hallucinate, required headers, pagination shape. This pre-loads correctness into *every* Cursor session Northwind's engineers run — highest-leverage artifact on this whole list, and most SDKs never ship one.
7. **`llms.txt`** at the docs root — one page: what the product does, core concepts, links to everything above. Gives any AI tool indexing your docs (Cursor's custom docs source included) accurate orientation instead of guessing from scattered pages.

Write every section as a self-contained block — lead with the direct answer, a few sentences, no "as discussed above." That's not just an AI-extraction nicety; it's what makes a page skimmable at 11pm during someone's first integration attempt.

### Track B — Web team ticket (not on critical path, file today anyway)

File it now, flagged explicitly as partner-launch-related. Don't expect it before Oct 14 — a 6-week queue puts it in early November at best. Two cheap direct asks worth making, not assuming the answer to:
- Is there an **expedite lane** for launch-blocking work, separate from the standard queue? Many teams have one and don't advertise it.
- Can they give you **direct publish access** to an existing docs section for content-only changes, bypassing the build entirely? The 6-week queue may be for template/infra work, not prose edits.

If both come back no, stop pushing here. This ticket exists so the permanent site eventually catches up — it doesn't need to solve September.

### Track C — Standalone hosted docs (optional, only if Track A finishes early)

A lightweight tool you can stand up alone — Mintlify, ReadMe, GitBook, or a static site on Vercel/Netlify — no web team, no engineering ticket. Worth it because:
- It gives Northwind (and future partners) a clean URL to add as a Cursor custom docs source, instead of raw GitHub markdown.
- It's the actual long-term fix for "docs build owned by a team with a 6-week queue," worth planting now even at MVP state.

Only start this once Track A's seven items are done and merged. If you're not there with days to spare before Sep 27, skip it — Track A alone is sufficient for Northwind to integrate.

## Day-by-day

- **Sep 18–20**: Confirm Northwind's actual stack (language, framework, auth pattern) directly — don't guess. Draft quickstart + auth guide.
- **Sep 21–23**: Write error reference + workflow examples. Test every sample yourself against a real sandbox — your only QA pass.
- **Sep 24–25**: Write `.cursor/rules`/`AGENTS.md` + `llms.txt`. Get one lightweight sanity check — a 10–15 minute async Slack review from any engineer with SDK context, not allocated "engineering time," just a favor — on the auth guide and `.cursor/rules` specifically. Those two do the most damage if wrong.
- **Sep 26**: PR everything into the SDK repo, merge before Northwind's start date. File the Track B ticket.
- **Sep 27–Oct 13 (live support window)**: Set up (if it doesn't exist) a channel Northwind can ask questions in. Every real question is a docs gap — patch same-day. Keep a running "known issues" note at the top of the README so the same question doesn't land twice.
- **Oct 14**: Launch. Freeze doc changes the day before unless something's actively broken.

## Definition of done before Sep 27

- [ ] Quickstart gets a cold developer to one successful API call in under 5 minutes — timed by you, not estimated.
- [ ] Auth guide covers test vs. live keys and the top 401/403 causes.
- [ ] Every code sample has been run against a real sandbox by you, not pulled from memory or stale internal docs.
- [ ] Error reference covers every error type the API actually returns.
- [ ] `.cursor/rules`/`AGENTS.md` exists and encodes the auth pattern plus any call shape Cursor tends to get wrong.
- [ ] `llms.txt` exists and links everything above.
- [ ] A Northwind-facing question channel exists and you're watching it.
- [ ] Web team ticket filed; expedite lane asked about directly.

## What not to do

- Don't wait on the web team for anything gating Northwind's start — their queue outlasts your entire runway twice over.
- Don't write docs from memory of how the API "should" behave. Zero engineering time means zero safety net if a sample is wrong.
- Don't start Track C before Track A is finished. A polished standalone site with integration gaps helps no one on Sep 27.
- Don't skip the direct ask to Northwind about their stack — guessing wrong here burns a day you don't have.

## Biggest risk

Not the docs build — it's that you're the sole reviewer of technical accuracy on content gating a partner launch. Mitigate by testing every sample yourself and asking for the smallest possible async review (15 minutes, not "engineering time") on the two highest-risk documents: auth and `.cursor/rules`. If you get nothing else from engineering this quarter, get that.