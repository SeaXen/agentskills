## Which do you do first

**Item 0, not on your list: find out why "rate-limit retry" failed.** Your cold run failed on 4 tasks — billing webhook, pagination, enterprise SSO, rate-limit retry — but rate-limit retry has no matching entry in your 12 problems. That means either the retry guidance doesn't exist at all, or it's buried somewhere you didn't flag during the read-through. You can't schedule a fix for a page you haven't located yet. Go find it (or confirm it's missing) before touching anything else — this is diagnosis, not a doc edit, so it costs you 10 minutes, not a slot in the queue.

Your ranking is sorted by fix speed. That's the wrong axis. Three of your four cold-run failures map directly onto items already in your list — that's real evidence of which docs actually break a working developer, independent of how fast they are to patch. Re-rank by that.

## Reprioritized

🔴 **Confirmed broken — a developer following these fails right now**

1. **(4) Billing-webhook fragment.** No imports, no client construction — textbook "copy-paste code that doesn't work," the single worst thing a code sample can do. Matches a cold-run failure. Fast fix: add the imports and client init, same as every other page already does.
2. **(9) Pagination buried under 4 paragraphs.** Matches a cold-run failure. Classic "wall of text" — lead with the working call, move the cursor-design explanation below it or into a separate concepts link. Fast fix, pure reorder.
3. **(7) Enterprise SSO is dashboard-only.** Matches a cold-run failure, but don't treat it as fast. First confirm SSO is even settable through the API — if it isn't, no doc can fix this, and you need a product conversation, not a docs edit, before promising a code path. Scope it before committing time.

🟠 **Not in the cold run, but load-bearing**

4. **(6) Errors page missing exact strings.** Names without strings means nobody can pattern-match on the actual error in code — this is exactly the kind of gap that produces silent failures your cold run didn't happen to hit this time. Fix alongside the webhook/retry work since you'll be touching error-handling context anyway.
5. **(11) No Java quickstart.** Possibly high-effort for uncertain payoff — check whether Java is actually a meaningful chunk of your integrators before committing. If yes, this is an acquisition gap, not cosmetic; ask, don't assume.
6. **(3) Changelog 3 releases behind.** Cheap, and it's a trust signal — a stale changelog reads as an unmaintained product to anyone doing due diligence.
7. **(5) Three pages still say v2.** Cheap, same trust-signal reasoning — this is often the first thing a skeptical evaluator notices.

🟢 **Cosmetic — no one fails a task over these**

8. **(2) `sdk` vs `client` naming on Concepts.** Consistency issue, not a functional one — nobody copy-runs the Concepts page.
9. **(1) Inconsistent code fence languages on CLI pages.** Breaks syntax highlighting, not execution.
10. **(8) Two broken footer links.** Quick fix — check first whether either link is something like a status page or support link; if so, bump it up, footer links to critical destinations matter more than decorative ones.
11. **(10) Glossary not alphabetized.** Zero functional impact.
12. **(12) Stale team photos.** Not really a docs problem — an about-page issue, lowest leverage of all twelve.

## Order to actually work in

1. Diagnose the rate-limit retry gap (unknown effort, do this first — it's the one thing you can't estimate yet)
2. Billing webhook fix (4)
3. Pagination reorder (9)
4. Errors page exact strings (6)
5. Scope enterprise SSO (7) — decide if it's even fixable via docs before scheduling it
6. Changelog (3), v2 titles (5) — batch these, both cheap trust-signal fixes
7. Everything in the cosmetic tier, in whatever order is convenient — none of it is blocking anyone