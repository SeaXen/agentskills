Using the `coding-agent-docs-optimization` skill to build this audit and fix plan. This skill's core rule directly overrides your ranking axis: **task impact decides what enters the queue, not how fast a fix is.** Your list was ranked by effort; I'm re-ranking by which findings actually caused one of your 4 cold-run failures, then by fixes-per-hour within that set.

# Agent-readiness audit — Thistlewood billing API

## Which do I do first

**#4 (billing-webhook fragment) first.** It's the cheapest fix of the four that map to a real failure, and it sits on your highest-stakes task — an agent inventing signature-verification code on a billing API is a security defect reaching production, not just a bad first attempt.

Then, in order: **#9 (pagination) → #6 (errors page exact strings) → #7 (enterprise SSO)**, with #7 last because it needs a scoping question answered before it's even a docs task. Full reasoning below.

## Task set and baseline

- 6 tasks run, 4 failed: billing webhook, pagination, enterprise SSO, rate-limit retry.
- ⚠️ Missing: model identifier and date. Cold-run-protocol.md run rule #6 — a score is only comparable within one agent generation. Record both before you re-run, or the "delta" you measure later won't mean anything.
- ⚠️ Missing: which 2 tasks passed. Worth naming them — if any of your "fast to fix" items (1, 2, 3, 5, 8, 10) sit on a *passing* task, that's actual evidence they don't need to move up the queue yet.

## Access check

Not run — no data given. This is step 1 of the workflow for a reason: "every surface below scores zero" if a CDN blocks AI crawlers, and that failure is silent — the audit looks fine, the agent hits a challenge page. Before trusting anything below, fetch a docs page with each agent user-agent you care about and confirm 200s. If Thistlewood's CDN blocks by default, that's the actual #1 fix, ahead of all 12.

## Findings

Only these four have cold-run evidence behind them. Ordered by fixes-per-hour (value is roughly equal — each one closes a full task failure — so effort breaks the tie).

### 1. Billing-webhook page ships an unrunnable fragment

- Task: billing webhook — **failed**.
- Your item: #4.
- Pattern: Snippet completeness + Self-containment (page-rules #4, #1).
- What's wrong: no imports, no client construction — an agent doesn't treat this as an excerpt, it pastes it verbatim and invents the missing setup.
- Fix: full snippet — imports with version pin, client construction, the call, the awaited result with a comment on what it returns, the error branch.
- Effort: low — mechanical rewrite of one page, no new facts needed from engineering.
- Why first: cheapest of the four, and it's the security-relevant one — invented webhook-verification code is a defect that ships.

### 2. Pagination page buries the call under four paragraphs

- Task: pagination — **failed**.
- Your item: #9.
- Pattern: Answer-first ordering (page-rules #10).
- What's wrong: cursor-design rationale before any code — forces extra reading, invites the agent to guess the call shape before it reaches the real one.
- Fix: reorder — working call, what it returns, parameters (as a table), rationale last. Content likely already exists; this is a restructure, not new writing.
- Effort: low — no new facts, pure reordering.

### 3. Errors page lists names, not the exact strings you emit

- Task: rate-limit retry — **failed**.
- Your item: #6.
- Pattern: Error mapping (page-rules #8).
- What's wrong: an agent building backoff logic matches against literal stderr/response text, not a human-readable error name. A name-only page means it guesses the field/string to check and gets it wrong.
- Fix: for every error, the exact string as emitted, plus conditions → cause → fix → a verification step (see cold-run-protocol.md's worked example — same shape).
- Effort: medium — needs someone to pull the literal strings from the API/SDK source, not just relabel prose.

### 4. Enterprise SSO page is dashboard-only

- Task: enterprise SSO — **failed**.
- Your item: #7.
- Pattern: UI paths (page-rules #3).
- What's wrong: an agent can't click. If the only setup path is "Settings → SSO → click Configure," the task is structurally unfinishable from docs alone.
- Fix — **but scope this before writing anything**: does an API or CLI path to configure SSO exist at all?
  - If yes: document it, keep the dashboard path as the human alternative. Cheap, same as the other three.
  - If no: this isn't a docs gap, it's a product gap. Per SKILL.md scope note — "pointing at [the API] as the real cause of a failure is a legitimate finding, not a deflection." Flag it to product/eng instead of trying to write your way out of it.
- Effort: unknown until scoped — could be small, could be blocked on another team. That uncertainty is exactly why it's last, not because SSO is unimportant.

## Fix plan

**Ships this week** (tier 1, in order): billing-webhook snippet → pagination reorder → errors-page exact strings.

**Needs a scoping answer before it's a docs task**: enterprise SSO — one question to eng ("is there a non-dashboard path?") decides whether this is a cheap fix or a product escalation.

**Backlog — no cold-run evidence yet, don't let them jump the queue:**

| # | Item | Why it waits |
|---|------|---------------|
| 1 | CLI code-fence languages | No cold-run task touches a CLI page. Cosmetic until one does. |
| 2 | `sdk` vs `client` naming | Naming-discipline pattern, but not the named root cause of any failure. If the Concepts page is a prerequisite the tier-1 pages link back to, fix it in that same editing pass — don't make it a separate trip. |
| 3 | Changelog 3 releases stale | Not tied to a failure. Feeds version/deprecation signalling but no evidence it broke a task. |
| 5 | Three pages say v2 | Version-labelling pattern — becomes urgent once cold runs shift from "invented call" failures to "version mismatch" failures, which the protocol calls the usual *second* failure. Recheck after tier 1 ships. |
| 8 | Two broken footer links | Footer nav is a human-UI artifact an agent reading markdown mostly never hits, unless it's the only path to an index/surface — check that specifically, otherwise pure site hygiene. |
| 10 | Glossary not alphabetized | Cosmetic; only matters if an agent linearly scans instead of searching. Lowest-value item on your list. |
| 11 | No Java quickstart | This is a missing *surface*, not a broken page — it can't have "failed" a cold run because no Java task exists in your frozen set. Add a Java task to the next round and let that decide priority, rather than building it speculatively. |
| 12 | Stale team photos | Not an agent-facing surface at all. Out of scope for this audit; runs on marketing's own clock. |

## Re-run

After tier 1 ships: re-run the identical 6-task set, same model generation, fresh context per task, no memory of this session. Hold against the exit criteria — first-attempt success up from baseline, zero invented surface on billing webhook specifically (it's your top-revenue task), corrective turns down. If rate-limit retry still fails after the exact-strings fix, that's a signal the root cause was something else (e.g., no runnable backoff sample) — don't declare it done on a page edit you haven't re-tested.