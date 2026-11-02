**1. Merge lands, epic closes? No.**

Two separate blockers, not one.

Blocker A — re-index. RAG bot only as good as its index. 20 new + 6 rewritten ≈ fifth of corpus by word count, roughly 20%. Practitioner threshold for re-embedding a docs-grounded assistant: ~10-15% content change. You're over it. "Rebuilt whenever we remember" is the exact failure this threshold exists to catch — corrected page keeps getting answered from stale index until someone re-embeds. Publishing ends at re-index, not at merge.
→ Name an owner who can trigger the re-embed, tied to this release, not to memory.

Blocker B — this isn't a project, it's a habit. KCS (Consortium for Service Innovation) frames capture as solve loop + evolve loop, run every cycle, never closed. Skill's own maintenance step:
- Stamp each page with last-verified date + owner.
- Re-run the clustering pass after publish. Same clusters reappearing = discoverability problem, not volume problem — don't read that as "write more pages."
- Book triggers now: release changes an error's text/cause → update entry same release. Fix ships → retire the known-issues entry same release. Escape-hatch channel moves → fix every entry pointing at it.
- Agree a coverage target before calling it done (skill's own baseline: 80% of top-20 clusters) and record the metrics baseline (cluster coverage, ticket volume per covered error, zero-result searches, entries touched since last release).

Close the epic once that baseline is written down. Not on merge.

**2. llms.txt / llms-full.txt — how much to care**

Push back on "W3C compliance" specifically — false framing, nothing to comply with. llms.txt is a proposal (Jeremy Howard, Answer.AI, Sept 2024), no ratified standard, no W3C or IETF working group behind it.

Care level: cheap and optional. Add it only if your docs generator emits it near-free. Never worth a dedicated project or sprint.

Better use of the same effort: serve clean per-page Markdown on request (GitHub's Markdown API pattern) — more durable, reuses pages you already have, helps any LLM reader, not just ones that fetch a root-level file.

Scope note: machine-facing entry points across a whole SDK/API is a separate, bigger job than troubleshooting docs. Don't let it ride in on this merge.

**3. Bot invents plausible fixes for undocumented errors**

This is a named failure mode for docs-grounded assistants, not a mystery: undocumented = doesn't exist in the bot's knowledge, so it's guessed, not answered. A bot inventing a fix costs more trust than one that says "no documented fix yet." It's a direct violation of Nielsen heuristic 9 (help users recover from errors) — wrong invented fix hurts recovery worse than no answer.

Two independent fixes, both needed:
1. Content — your 20+6 entries shrink the gap but never close it. Gartner: even best-in-class self-service resolves only ~36% of "very simple" issues, 14% overall. New and rare errors will always sit outside the corpus.
2. Bot config — the actual root cause. Add an explicit refusal guardrail: low retrieval confidence or no matching entry → state no documented fix exists, never fabricate. This is independent of the doc merge — fix it now, don't wait on corpus growth.

Bonus: the bot's own log of invented/no-match answers is your newest zero-result-search signal, in the reader's own words. Feed it into next cycle's cluster pass same as tickets. Also, for known-issues entries you can't reproduce, write the fix as "reported under these conditions, not reproduced here" explicitly instead of leaving silence — gives the bot a real documented "known, unresolved" answer to retrieve instead of a hole to fill with a guess.

Next: assign the re-embed owner for this merge before it ships.