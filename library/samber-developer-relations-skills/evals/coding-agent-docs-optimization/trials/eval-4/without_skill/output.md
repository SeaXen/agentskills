**Verdict:** Structure ok, but 5 gaps break the test before it starts.

1. ⚠️ One long session contaminates results. Agent explains OAuth in task 2, then reuses that answer for later tasks instead of re-reading docs. Test measures "agent memory," not "docs work standalone." Fix: fresh session per task, unless multi-turn retention is its own separate metric.

2. ⚠️ Full web access defeats doc test. Agent solves webhook-signature task from generic HMAC pattern on GitHub/StackOverflow, not your docs. Pass tells nothing about doc quality. Fix: run each task twice — docs-only, then docs+web — diff results.

3. Binary pass/fail loses root cause. No record of missing info vs wrong info vs unclear wording vs agent guessed from general LLM knowledge. Fix: log full transcript + doc section cited, grade against written rubric, not eyeball.

4. n=1 per task, but you report a percentage. LLM output varies run to run. One shot per task across 8 tasks gives false precision. Fix: 3-5 runs per task, report range, pin model+version (results drift as model updates).

5. No rubric for security-sensitive task (webhook sig verify). Common bug: `==` instead of timing-safe compare, verify parsed body instead of raw body. "Code looks plausible" misses both. Fix: explicit pass checklist per task, not general impression.

Smaller notes:
- Task order should mirror real dev path (new user rarely reads OAuth docs before first API call). Order is itself a variable — control it, don't default to your write order.
- Task 1 needs sandbox creds. Define pass as "correct code" vs "actual successful call" — different bars.
- "Explain OAuth" task needs a grading rubric (must mention: expiry check, refresh endpoint, grant type, failure handling) or two people will score it differently.

Next: pick fresh-session-per-task vs shared, before running any of the 8.