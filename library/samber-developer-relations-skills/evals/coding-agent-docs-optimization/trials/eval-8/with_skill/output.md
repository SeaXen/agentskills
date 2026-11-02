**First move, today, 2 minutes:**
Open Cursor. Settings → Indexing & Docs → Add Doc → paste your main docs URL. Wait for index to finish.

Thin index, error, or zero pages = crawler gate blocking Northwind before you touch one page. That's Northwind's exact tool, so it beats any generic bot-UA test. Do this before anything below.

## Constraints — confirmed vs assumed

Confirmed, from you:
- Solo technical writer. Zero engineering hours this quarter.
- Docs build owned by web team. Queue: 6 weeks.
- Northwind engineers: Cursor, "basically everything."
- Northwind starts wiring SDK in 9 days.
- Partner integration live 14th next month.

Assumed, not stated — flag if wrong, changes the plan:
- Docs = client SDK docs, likely backed by hosted API (analytics product → event ingestion + query endpoints).
- You have direct edit access to page content (CMS or repo), even though you don't own the build.
- Unknown whether a machine-readable spec (OpenAPI/etc.) exists, is generated, or is hand-maintained. Check day 1.
- Unknown what's already failing for agents. Cold run finds this — don't guess it.
- Northwind's stack language(s) unknown. Confirm with their eng lead this week; determines which SDK language page gets priority.

## Cut from this quarter's plan, and why

Dates below explain the cuts (see Timeline). Two rules from the skill did the cutting:

- **Hard date drops anything needing a build change or another team's release.** Cut: markdown endpoints via build, response headers/link relations, build-generated index, robots.txt/bot-policy change. 6-week queue lands after go-live — file tickets now anyway, treat as next-quarter hardening, not this plan.
- **Hours-only ceiling deletes doc comments and terminal paths outright**, not just deprioritizes. Cut: SDK docstrings, CLI doc command. Both need engineering + a release. Zero available. Park for next quarter when eng time exists.
- Full-corpus bundle: not building. No evidence the corpus fits a context budget, and it needs a build step you don't have.

## Timeline

- Today: Fri Sep 18.
- Northwind starts: Sun Sep 27 (9 calendar days) — real first working day is **Mon Sep 28**.
- Your actual working days before that: **5** (Mon 21–Fri 25), not 9.
- Partner go-live: **Oct 14** (26 days out).
- Web team's 6-week queue resolves ~Oct 30 — after go-live. Anything filed there is not part of this plan's critical path.

## 9-day plan

**Phase 1 — today + Mon (findings, not fixes):**
1. Run the Cursor doc-index test above. Log result.
2. Fetch your top 3 docs pages + index/homepage with `curl -A "GPTBot"` and `curl -A "ClaudeBot"` from outside your office network (phone hotspot works). Log status codes.
3. Confirm with your Northwind counterpart: what are they actually building first? (Auth, first event send, first query — get the real 3 tasks, not guesses.)
4. Confirm whether a spec file (OpenAPI/etc.) exists and whether you can edit it directly.
5. Pick a cold-run task set: use the draft below, swap in Northwind's real 3 tasks for tasks 1–3.

**Phase 2 — Tue–Thu (baseline + fixes):**
1. Cold-run the task set once, unattended, sources restricted to your live docs — use Claude or GPT-5 in a fresh session, no repo access, no hints. Log every corrective turn.
2. Rewrite every page a failed task touched — checklist below, in order.
3. If spec is editable: annotate the fields the failed tasks exposed — checklist below.
4. Write one new content page: "Using \[Osprey] with a coding agent" — Cursor setup steps, spec URL, top task links. Content-only, no build ticket needed.

**Phase 3 — Fri + weekend buffer (verify):**
1. Re-run the same task set, fresh session.
2. Compare against baseline: fewer invented calls, fewer corrective turns.
3. Send Northwind's eng lead the new Cursor-setup page directly — don't wait for them to find it.
4. File web-team tickets for the cut items now, so the 6-week clock starts.

Through go-live (Oct 14): re-run the task set after every page edit. Score decays silently otherwise.

## Cold-run task set (draft — swap 1–3 for Northwind's real first tasks)

1. Install SDK and authenticate for the first time.
2. Send a first event / make a first API call and confirm it succeeded.
3. Query aggregated data and paginate through results.
4. Verify a webhook signature.
5. Handle a rate-limit response with backoff.
6. Rotate or refresh an expired credential.
7. Diagnose one real error string pulled from your support queue.

Freeze this list once set. A benchmark that changes between runs proves nothing.

## Rewrite priority (apply to every page a failed task touched)

Page checklist, in order:
1. Answer-first: working call, then what it returns, then params, then rationale.
2. Complete snippets: imports, client setup, call, awaited result, error branch. No excerpts.
3. Self-contained: restate the prerequisite, don't point back at an earlier page.
4. Error-string mapping: exact stderr text → cause → fix → how to verify the fix worked.
5. One name per concept, one placeholder style, across every page.

Spec checklist, if you can edit it directly, in order:
1. `operationId` on every operation — verb-noun, e.g. `sendEvent`, `listCustomers`.
2. Enums, `required`, `default`, `format` on every field — this is where invented values come from.
3. `description` field: preconditions, auth scope, rate limit, which sibling call fits better.

## Cursor-specific moves (this is your highest-leverage lever — no build change needed)

1. Cursor's doc-indexing crawls your existing rendered pages. Clean pages help immediately, before any markdown-endpoint work exists.
2. Ship the "using with a coding agent" page from Phase 2 — tell Northwind exactly how to add your docs URL in Cursor's Indexing settings.
3. If a spec exists, put its raw URL on that same page — Cursor agents can be pointed at it directly in chat.
4. Don't wait on markdown endpoints to help Cursor. HTML pages index fine if content is complete and self-contained.
5. SDK docstrings would help Cursor's in-editor completion too — this is the top item for next quarter once engineering time exists.

## Fix plan

**Ships in your 5 working days (no one else needed):**
- Page rewrites on failed-task pages.
- Spec field annotation, if editable directly.
- New Cursor-setup content page.
- Cold-run baseline + re-run.

**Filed now, lands after go-live — not part of this plan:**
- Markdown endpoints, response headers, build-generated index, bot-policy review.

**Cut entirely this quarter:**
- SDK doc comments, CLI doc command — need engineering, none available.

## Exit criteria for this cycle

Don't chase the published 80% first-attempt stretch target in 5 working days — that number comes from vendors with mature, build-level agent surfaces you don't have yet. Realistic target for go-live:

- Zero invented calls on the 3 tasks Northwind is actually shipping first.
- Every error string in your support queue mapped to cause + fix.
- Corrective turns down from baseline on the full 7-task set, even if success rate isn't perfect.

Report both numbers honestly to whoever's watching the partner deadline — the gap between this and 80% is the argument for the next-quarter engineering ask (doc comments, build changes), not a thing to hide.

**Next action:** run the Cursor doc-index test at the top. Takes 2 minutes, tells you if everything else is worth doing yet.