**Verdict: not yet.** Two blockers stop safe ship. Two sizing bugs need fix regardless of date.

## Blocker 1 — access check, unverified, do first

Nothing below matters if crawler fetch blocked at edge. CDN can block AI crawlers by default on new properties; failure silent — you see finished files, agent sees a challenge page.

1. Fetch docs root + one deep page with each target agent user-agent (GPTBot, ClaudeBot, PerplexityBot, etc.), from outside your network.
2. Record status code per agent per surface.
3. Any 403/challenge → escalate to CDN/WAF owner today. Policy call, not docs fix.

Time: 30 min to check. Escalation time unknown, depends who owns bot policy.

## Blocker 2 — no cold-run baseline

Ship without this, and you can't tell if either file helped. Minimum version, still doable this week:

1. Write 5 tasks, one per product line plus one cross-cutting ("wire up Edge device onboarding," "pull last 30 days of Historian data via API").
2. Run each in fresh agent session, sources restricted to published docs, no memory carryover.
3. Log invented calls, corrective turns, docs fetched per task.
4. Re-run same 5 after shipping. Delta is what "did this work" means — a shipped file with no before/after number is a guess dressed as a plan.

Time: half day. Runs parallel to file fixes below.

## Sizing bug 1 — llms-full.txt at 6.2 MB

~1.5M tokens at 4 chars/token. No current agent context window holds that plus developer's own code — this bundle truncates mid-page on every real use. Agent believes it read everything it didn't. Worse than no bundle at all.

Fix, one of:
- Split per product line: 4 files, ~1.55 MB / ~390K tokens each. Still likely too big alongside real code — check against your top 2-3 target agents' context budgets before trusting even that.
- Or drop it. Markdown endpoints (clean `.md` per page) are the highest-value-per-hour surface in this skill and do the same job with zero truncation risk.

## Sizing bug 2 — llms.txt at 180,000 characters

Self-set split threshold: ~100K characters. You're 80% over.

Fix: root `llms.txt` (project name, one-line summary, links to 4 child indexes) + one child index per product line (`llms-edge.txt`, `llms-fleet.txt`, `llms-historian.txt`, `llms-studio.txt`). Order each child's sections by task frequency, not site nav order. Generate all 5 from docs nav source at build time — hand-maintained index rots within 2 releases.

## Footer link alone changes nothing measurable

Publishing without advertising is a no-op — agent fetches these because something points at them. Footer covers "docs navigation," one of three required spots. Add:

1. Root README of docs repo/site — name the index URL directly.
2. Response headers on every page: `Link: <https://docs.vantagegrid.com/llms.txt>; rel="describedby"`, plus `<link rel="alternate" type="text/markdown">` wherever a markdown twin exists.

## This week (content-only, no build change)

1. Access check.
2. Split llms.txt → root + 4 child indexes.
3. Split or drop llms-full.txt.
4. Footer link + README line.
5. Start the 5-task cold-run baseline, parallel to above.

## Needs more time / another team

- Response headers + `<link rel>` tags — needs docs-build/template change, not content-only.
- Per-page markdown endpoints for all ~1,400 pages — actual highest-value fix here, bigger than this week, schedule next.
- Bot-policy/WAF change — only if blocker 1 finds a block.
- If Vantage Grid ships an OpenAPI/protocol spec for Edge/Fleet — check. An annotated spec outranks index/bundle on value and isn't in the current plan at all.

Next: run the access check now — everything else depends on that result.