Using the coding-agent-docs-optimization skill for this: the skill explicitly names your manager's exact ask as the failure pattern to avoid ("Write an llms.txt for docs.example.com" → don't just emit the file). I tried to run the access check myself (`WebFetch` on `docs.brightloom.com` and `/openapi.json`) but this session has no outbound web access — that's now the first line item in the report below, not something I can silently skip.

Here is the audit report and the draft file.

---

# Agent-readiness audit — docs.brightloom.com — 2026-09-18

## 0. The honest headline

**Shipping `llms.txt` alone changes nothing measurable this week.** Two structural gaps sit underneath it:

- ⚠️ No markdown endpoints exist. Every link in the index will point at an HTML page, so an agent still pays for HTML-stripping and still risks scraping nav chrome as content.
- ⚠️ The OpenAPI file — the surface with the highest value-per-hour on the skill's own ranking — has empty `description` fields on roughly half its operations. An agent that follows the index straight to the spec still invents parameters once it's there.

Ship the file. Say this plainly to your manager in the same message: it's the cheapest surface, not the one that moves the score. The two fixes below it are what actually reduces invented calls.

## 1. Access check — I could not run this, you need to

I have no outbound HTTP access in this session (`WebFetch` failed on permission, not on a real block). Run this from outside your network before anything else — a CDN silently blocking AI crawlers makes every surface below score zero and no page rewrite fixes it:

```bash
curl -sI -A "GPTBot"        https://docs.brightloom.com/           # OpenAI
curl -sI -A "ClaudeBot"     https://docs.brightloom.com/           # Anthropic
curl -sI -A "PerplexityBot" https://docs.brightloom.com/
curl -sI -A "Google-Extended" https://docs.brightloom.com/
curl -s  https://docs.brightloom.com/robots.txt
curl -sI https://docs.brightloom.com/llms.txt                       # 404 today, expected
curl -sI https://docs.brightloom.com/openapi.json
```

Record status codes per agent. If any return a challenge page or 403, that's a bot-policy decision for whoever owns the CDN dashboard, not a docs fix, and it blocks everything else — flag it to that owner today, in parallel with the rest of this plan.

## 2. Surface inventory

| Surface | Status | Effort to fix | Unblocks |
|---|---|---|---|
| Crawler access | ❓ unverified — see §1 | — | everything |
| Index file (`llms.txt`) | ❌ missing | Low | routing, if the things it points at work |
| Markdown endpoints | ❌ missing — Next.js, HTML only | Medium–High (see §5) | halves fetch cost, removes HTML-stripping errors |
| OpenAPI spec | ⚠️ present, partial — ~50% of `description` fields empty, hand-written 2 years ago (drifted from implementation) | Medium | invented-parameter rate on every API task |
| `operationId` coverage | ❓ unknown — check while annotating | Low | tool-name quality if this ever feeds an MCP server |
| Version/deprecation labels | ❓ unknown | — | protects against SDK majors changing under agents |
| SDK doc comments | ❓ unknown — not mentioned | — | offline / in-editor agent, separate from web fetch |
| Full-corpus bundle | ❌ not recommended | — | 340 pages won't fit a working context budget — build per-product-line if ever needed, not now |

## 3. Cold-run task set (ready to run, not yet run)

I can't execute this myself — no live docs to test against and no fetch access. This is the frozen set for whoever runs it (docs owner, or a coding-agent harness pointed at the published surfaces only):

1. Install the Web SDK in a React app and send a first pageview event.
2. Identify a logged-in user and attach traits, without double-counting the pre-login anonymous stream.
3. Track a custom event server-side (Node) with retry-safe idempotency.
4. Verify inbound webhook signatures on an Express server.
5. Paginate the Events API and export the last 30 days of one event type to CSV.
6. Gate tracking behind consent so EU visitors aren't tracked pre-opt-in.
7. Handle a 429 from the ingestion API with backoff.
8. Migrate a v2-style tracking call to the current SDK major version.

Run rules: fresh context per task, sources restricted to the published surfaces, unattended to a verifiable outcome, full transcript kept, model + date logged. Full protocol in the skill's `cold-run-protocol.md`. Calibration reference (Stripe's open benchmark): treat 80% first-attempt as a stretch goal, not a floor — don't let this get heard as a minimum this week.

Baseline: **not measured.** Report it as unmeasured, not as a number, until someone actually runs the eight tasks.

## 4. Findings that don't need a cold run to be true

These are structural, visible from what you already told me — not task-specific findings, which require §3 to actually run:

- Every markdown-endpoint task in §3 will cost at least one extra HTML-stripping step per fetch, today, because no `.md` URL exists anywhere on the site.
- Any task touching the API surface (3, 4, 5, 7) has roughly even odds of hitting an operation with an empty `description` — that's where an agent fills a parameter with a plausible guess instead of the real contract.

## 5. Fix plan

**Ships this week** (your stated ceiling — no build change, no other team's release cycle):

- **Generate `llms.txt` from the Next.js nav source, not by hand.** A hand-maintained index rots within two releases. Write a small build-time script that walks whatever already drives your sidebar nav (route manifest, MDX frontmatter, or CMS query — tell me which and I'll write the exact script) and emits `public/llms.txt`. Draft below.
- **Annotate `description` on the OpenAPI operations behind the top 3 tasks in §3**, not all ~340 pages' worth of operations — task impact picks the order, not alphabetical sweep. Add `required`, `default`, and enums anywhere a value space is finite; that alone removes a whole class of invented parameters. Full field-by-field guidance is in the skill's spec-annotation reference.
- **Advertise the index in three places** (see §7) — none of these need a Next.js rebuild pipeline, just a README line, a nav entry, and a response header.

**Needs a build change or more time — name it, don't hide it:**

- Full markdown endpoints for all 340 pages. Two branches depending on an answer I don't have:
  - If pages render from MDX source → cheap: add a rewrite that serves the raw `.mdx` source at `.md`, stripping frontmatter.
  - If pages are CMS-driven or hand-built JSX → real work: an HTML→markdown conversion pipeline, or the CMS becomes the source of truth instead of rendered output. Tell me which and I'll scope it.
  - Stopgap if you want partial credit this week without waiting on that decision: a `getStaticProps`-driven `.md` route that strips tags from the rendered HTML. Lower quality (loses tables, can mangle code fences) — replace it, don't leave it as the permanent answer.
- Annotating the remaining ~half of OpenAPI operations. Standing job, never wins on ratio — schedule it, don't try to clear it in a sprint.
- Version/deprecation labels, SDK doc comments — both unscoped because I don't know if Brightloom's SDKs are versioned or typed for this. Answer that and I'll fold them into the next pass.
- The full cold-run in §3, and the re-run after this ships.

## 6. The `llms.txt` draft

Placeholder page slugs below — I don't have your actual nav, and hand-guessing 340 URLs would be worse than not shipping. Treat every bullet as a routing category to fill from the real source, not final copy:

```markdown
# Brightloom

> Product-analytics SDK: client and server libraries for tracking events, identifying
> users, and routing data to downstream destinations. Current major version: vX.

## Getting started

- [Install the Web SDK](https://docs.brightloom.com/sdk/web/install.md): package name, init snippet, first pageview event
- [Install a server SDK](https://docs.brightloom.com/sdk/server/install.md): Node, Python, Go, Java — auth key setup, first server-side event

## Core concepts

- [Identify users](https://docs.brightloom.com/concepts/identify.md): linking anonymous and identified traffic without double-counting
- [Track events](https://docs.brightloom.com/concepts/track.md): event schema, required fields, idempotency keys
- [Consent and privacy](https://docs.brightloom.com/concepts/consent.md): GDPR/CCPA gating before first track call

## Reference

- [API reference (OpenAPI)](https://docs.brightloom.com/openapi.json): full request/response schema
- [Error codes](https://docs.brightloom.com/errors.md): every error string, its cause, its fix
- [Webhooks](https://docs.brightloom.com/webhooks.md): inbound destination signature verification
- [Rate limits](https://docs.brightloom.com/limits.md): thresholds, backoff, retry-after header

## Optional

- [Migration guide: v2 → current](https://docs.brightloom.com/migrate.md)
- [Architecture rationale](https://docs.brightloom.com/design.md)
```

Interim reality: until §5's markdown work ships, every link above 404s or resolves only as HTML. Two honest options for this week — point the file at the current HTML URLs (functional, but an agent pays the stripping cost the skill's page rules exist to avoid) or hold publishing the index until the `.md` routes exist, even the stopgap ones. Your call — I'd hold it a few days rather than ship dead links, but it's a one-week deadline call, not mine.

## 7. Advertise it (publishing without this is a no-op)

- README: one line naming the index URL and the `.md` convention.
- Docs nav: a visible link, so a human can hand the URL to their agent.
- Response headers, via `next.config.js` `headers()` or middleware:
  ```
  Link: </llms.txt>; rel="describedby"
  ```
  on every docs page, plus `<link rel="alternate" type="text/markdown" href="...">` once `.md` routes exist.

## 8. Re-run

Same eight tasks, same model generation, after §5's "ships this week" items land. Compare against the (currently unmeasured) baseline from §3. Until that first run exists, nobody — including your manager — gets a score, only a shipped file and a named list of what it doesn't fix yet.