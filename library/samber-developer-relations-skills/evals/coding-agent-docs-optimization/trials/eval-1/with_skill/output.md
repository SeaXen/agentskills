# Agent-Readiness Audit — docs.halyard.io

**Date:** 2026-09-18 · **Requested by:** Halyard docs lead, for CEO review · **Auditor note:** this session had no outbound network access, so the access-layer check below is a diagnosis to confirm, not a live measurement. Commands to confirm it yourself are included — run them before the CEO meeting, they take minutes.

## Headline, for the CEO

**Don't lead with a page-quality score. Lead with this: the docs almost certainly aren't a content problem right now — they're an access problem.**

Fifteen independent reports of "my AI tool can't find your docs," pages that load fine for a human, and normal analytics, is the exact signature of a CDN bot-management ruleset challenging or blocking non-browser HTTP clients — turned on two months ago, at the same CDN migration. Two mechanisms explain why nobody but Discord users noticed:

1. **Humans pass, agents don't.** A managed bot-protection ruleset (Cloudflare's "Block AI Bots" / Bot Fight Mode, Akamai Bot Manager, etc.) typically gates on things a real browser does automatically — executing a JS challenge, matching a browser TLS/JA3 fingerprint — and a real person's browser clears it silently. A coding agent's fetch (an MCP fetch tool, a plain HTTP client inside Cursor/Copilot/Claude, a `WebFetch` call like the one this session tried against your domain) does none of that. It gets a 403 or a challenge page and reports back "couldn't access this page" — which is exactly the phrase your Discord users are relaying.
2. **The failures are invisible to your own dashboards.** Your analytics almost certainly fire from a JS beacon on the rendered page. A request that never gets past the bot challenge never executes that JS, so it never becomes a data point — not a dip, not an anomaly, just absence. "Traffic looks normal" is consistent with this theory, not evidence against it.

This matters for how you frame it to your CEO: this is not a "docs team wrote bad content" story, it's a "the CDN migration silently regressed a permissions/access control setting" story. In Netlify's AX framing (the term your CEO may have heard), this is a pillar-1 failure (access and permissions), not pillar-3 (doc quality) — and it's fixable in hours, not a content rewrite.

## Confirm it — run these today, before anything else

I could not reach `docs.halyard.io` from this session (no outbound network). Run these from a shell with real internet access and paste back the status codes:

```bash
# Baseline: how a human's browser sees it
curl -sI -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" https://docs.halyard.io/

# Named AI crawlers / fetchers your bot-protection vendor ships a category for
curl -sI -A "GPTBot/1.0 (+https://openai.com/gptbot)" https://docs.halyard.io/
curl -sI -A "ClaudeBot/1.0 (+https://www.anthropic.com/claude-bot)" https://docs.halyard.io/
curl -sI -A "PerplexityBot/1.0 (+https://perplexity.ai/bot)" https://docs.halyard.io/
curl -sI -A "Google-Extended" https://docs.halyard.io/

# The one that actually matters most for "coding agents": a generic, non-browser client
# with no recognizable bot UA at all - this is what most agent tool-calls look like on the wire.
curl -sI -A "python-requests/2.31" https://docs.halyard.io/
curl -sI https://docs.halyard.io/          # curl's own default UA

# Signalling layer - separate from enforcement, check both
curl -s https://docs.halyard.io/robots.txt
```

Read the results this way:

| Result pattern | What it means |
|---|---|
| Browser UA → 200, everything else → 403 / 429 / challenge HTML | Confirmed: bot-management ruleset is the whole story. Fix the ruleset, re-test, move to the task-set run below. |
| Browser UA → 200, named AI bots → 200, generic client (`python-requests`, bare `curl`) → 403 | Partial allowlist exists for known crawlers but not for tool-initiated fetches — the more damaging gap, since it's live coding-agent sessions doing the fetching, not just training crawlers. |
| Everything → 200 | The block isn't at this edge. Check whether it's origin-level, a WAF layer in front of the CDN, or intermittent (rules sometimes only trigger under rate/velocity heuristics — rerun from a few different IPs/times before ruling it out). |

In your CDN dashboard, look specifically for: a "Block AI Bots" / "AI Scrapers and Crawlers" managed rule, Bot Fight Mode or Super Bot Fight Mode, or a WAF rule added during the migration that challenges "automated" traffic. The fix is an allow-or-monitor rule for your target agent categories — not a full bot-protection disable. Scope it: verified AI-crawler UAs (GPTBot, ClaudeBot/anthropic-ai, PerplexityBot, Google-Extended) *and* the docs subdomain more permissively for generic clients if your CDN can scope bot rules per-host, since `docs.*` doesn't carry the fraud risk your app or checkout subdomains do.

## The score

**Today's honest number: the access gate fails, so first-attempt agent success is effectively 0% regardless of content quality — no page rewrite fixes a request that never lands.** That's the number for the CEO if the ruleset isn't fixed before the meeting: not "we don't have a score," but "we have a score, and it's zero, and here's the one-line reason and the one-line fix."

If the ruleset gets fixed today, don't replace that zero with a guessed number either. Run a same-day baseline (below) and report the *real* first-attempt success rate instead. Stripe publishes the only open benchmark of this shape — 73–92% across categories for frontier models, but that's best-of-3, not first-attempt, and measured on docs Stripe has spent real effort making agent-readable. Treat 80% first-attempt as a stretch goal to aim at over the coming quarter, not a number to promise by Friday.

## Minimal same-day cold run (if the fix lands today)

Five tasks, chosen for payments-API relevance and because they're the exact failure modes that show up most often industry-wide (webhooks, pagination, rate limits) plus two Halyard-specific ones. Pull the real ones from your Discord thread if you can — those fifteen people already told you which integrations they were attempting; that's a better task set than anything I can guess. Placeholder set if you need one now:

1. "Add webhook signature verification to an existing Express/Flask server for Halyard payment events."
2. "Create a charge/payment intent with an idempotency key, and handle the duplicate-key response."
3. "Paginate through all transactions in the last 30 days and write them to CSV."
4. "Handle a 429 rate-limit response with backoff on the transactions list endpoint."
5. "Issue a refund for an existing charge and verify the resulting status."

Run rules (non-negotiable for the number to mean anything): fresh context per task, no repo cache, sources restricted to what's actually published at docs.halyard.io, run to a verifiable end state, log every corrective turn. One task per agent in parallel if you can, otherwise separate sessions — never stack two tasks in one session, it inflates every score after the first.

## Surface inventory — fill this in, I can't see the site

| Surface | Status | How to check |
|---|---|---|
| `llms.txt` index | ? | `curl -sI https://docs.halyard.io/llms.txt` |
| Full-corpus bundle (`llms-full.txt`) | ? | `curl -sI https://docs.halyard.io/llms-full.txt` |
| Markdown endpoints per page | ? | Append/swap `.md` on a real doc URL, check it returns clean markdown not HTML |
| OpenAPI/spec file, publicly served | ? | Check your docs nav or `/openapi.json`, `/openapi.yaml` |
| Spec `operationId` + filled `description` fields | ? | Open the spec file, check whether `description` fields are empty or generic |
| SDK doc comments (if you ship typed SDKs) | ? | Check whether public methods have docstrings/JSDoc beyond the signature |
| Version pointer / deprecation labels | ? | Does a page state its own version machine-readably? |
| CLI `docs` command / package-local docs | ? | Does your CLI or SDK package ship offline reference docs? |

Every row above is worth nothing until the access gate is confirmed open — that's not a caveat, it's the actual finding. Building an `llms.txt` behind a 403 produces a tidy file no agent ever reaches.

## Findings

**Only one finding qualifies right now, because no cold run has executed yet — everything else would be a guess dressed as a finding, which this process explicitly refuses to do.**

### Access gate blocks non-browser fetches, silently, since the CDN migration
- Task: all of them — this is the gate, not a per-task failure.
- Outcome: unconfirmed pending the curl commands above, but consistent with all reported symptoms.
- Root cause: CDN bot-protection ruleset enabled during migration ~2 months ago, never scoped to allow AI-agent traffic.
- Fix: allow/monitor rule for target agent UA categories, scoped to the docs subdomain; re-test with the same curl matrix.
- Impact: blocks 100% of tasks. Nothing else on this list matters until it's closed.

Once access is confirmed open and a baseline cold run exists, re-run this audit — the findings section will fill in with real, task-linked page and spec issues at that point, ranked by fixes-per-hour like any other iteration.

## Fix plan

**Ships today (no build, no other team, this is the whole reason it's possible before Friday):**
- Scope the CDN bot-protection ruleset to allow the target agent categories on `docs.*`. **This is the one action that determines whether Friday's number is real.**
- Run the 5-task cold run above once the fix is live; that gives you an actual baseline percentage instead of a placeholder.

**Needs a build or engineering-cycle change — do not promise these for Friday:**
- `llms.txt` index generated from your nav source, advertised in the README/nav/response headers.
- Markdown endpoints for every page.
- OpenAPI spec annotation (`operationId`, filled `description`, constrained enums) if you have a spec — send it over and I'll do the annotation pass directly.
- SDK doc-comment pass, if you ship typed client libraries.

That split exists because of the deadline, not because those items don't matter — a hard date drops everything that needs a build cycle, full stop. They go on the roadmap as the standing work that gets you from "gate open, unmeasured content quality" to an actual 70-80%+ first-attempt number over the next one to two releases.

## What to actually tell the CEO Friday

> "Our AI-coding-tool complaints trace to one root cause: the CDN migration two months ago silently turned on bot protection that blocks non-browser traffic, including AI coding agents — human visitors and our analytics never showed it because blocked requests don't reach either. We [fixed / are fixing] the CDN rule today. [If run:] First real baseline: X% of test integration tasks succeed unattended on the first try. Roadmap to get that number to 75-80%+: llms.txt, markdown page endpoints, and OpenAPI annotation, landing over the next N weeks, re-measured after each."

That's an honest, specific, fixed-today story — stronger for a CEO than a fabricated score would have been, and it's the one this process is actually able to stand behind.