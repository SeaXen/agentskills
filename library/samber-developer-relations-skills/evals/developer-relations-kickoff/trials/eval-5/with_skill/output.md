## Route

This task splits across two skill collections. Only one piece of it belongs to `developer-relations-skills` (the collection whose kickoff you asked me to follow); the rest is public-API surface design, which `developer-relations-kickoff` is explicitly built to hand off rather than stretch itself onto:

> "Public API surface design, webhooks, SDK portfolios, developer-portal design, OAuth for third-party apps, and connector-marketplace operations belong to `samber/developer-platform-skills`."

`samber/developer-platform-skills` is already present in your `skill-wip/samber/` tree, so here's the exact skill per item — not a generic "go install the other collection," since I read each skill's own declared scope to place your four work items precisely.

## Mapping — one skill per decision

**1. Rate-limit headers + what the 429 body looks like → two skills, not one**
- `samber/developer-platform-skills@api-rate-limit-policy` — metering model, tier/burst numbers, the header choice (legacy `X-RateLimit-*` vs IETF `RateLimit-*` fields), and the throttle *policy*. Its own scope note: "Do NOT use for the 429 error envelope."
- `samber/developer-platform-skills@api-error-design` — the 429 response *body* itself: RFC 9457 `problem+json` envelope, error-code taxonomy, `retryable` signaling, `documentation_url` per code. This is also where every other error body (idempotency conflicts, webhook signature failures) should draw its shape from, so it's the foundation, not an afterthought.

**2. Idempotency keys so retried writes don't double-charge**
- `samber/developer-platform-skills@api-idempotency-retry` — key derivation/scoping, storage TTL, atomic claim mechanism (DB unique constraint / SERIALIZABLE lock / conditional write), payload-mismatch rejection, in-flight duplicate handling, backoff+jitter, SDK retry defaults. Its framing is exactly your ask: ship key support and retry guidance together, or the guarantee is open wherever a dropped connection tests it.

**3. Webhook retry and replay behaviour**
- `samber/developer-platform-skills@webhook-platform-design` — event taxonomy, HMAC signing (Standard Webhooks), at-least-once delivery with retry/backoff, dead-letter policy, subscription lifecycle, and the developer-facing debugging surface (delivery logs, replay, test-event triggering). Provider side only; explicitly not the same skill as idempotency retry (that's the *consumer's* retry loop, this is *your* delivery loop).

**4. Document the whole thing, readable by unattended coding agents → two skills, split by reader**
- `samber/developer-platform-skills@api-reference-quality` — audits the published reference against the full contract surface (every endpoint, param, response code, error documented; snippet parity; CI gates that stop drift). This is what makes "the whole thing" actually complete once 1–3 are designed.
- `samber/developer-relations-skills@coding-agent-docs-optimization` — the one skill in *this* collection that's actually in scope: machine-readable entry points (`llms.txt`, OpenAPI/JSON Schema), self-contained copy-paste-safe pages, measured first-attempt agent success rate. `api-reference-quality` itself routes the agent-reader half here rather than duplicating it.

## Chain (dependency order — each link hands the next one an artifact)

1. `api-error-design` → defines the shared error envelope and `retryable` signal every other surface below reuses.
2. `api-rate-limit-policy` → fills in the 429 case against that envelope, plus the headers and tier numbers.
3. `api-idempotency-retry` → fills in the conflict/mismatch error case against that same envelope, designs the key mechanism.
4. `webhook-platform-design` → independent surface, own signing + retry/dead-letter contract.
5. `api-reference-quality` → documents and gates the finished surface for completeness.
6. `coding-agent-docs-optimization` → layers agent-specific readability on top of that finished reference.

## Not now

- `samber/developer-platform-skills@public-api-design-review` — a whole-surface consistency pass (naming, status codes, one error envelope end to end) across everything above. Unblocking condition: after 1–4 are drafted, before Q1 ships.
- `samber/developer-platform-skills@developer-portal-design` — only if "document the whole thing" turns into a self-serve portal, not just reference pages.
- `samber/developer-relations-skills@developer-quickstart-guide` / `docs-code-sample-standards` — if you also want a human zero-to-one path and a sample-code policy, distinct from the agent-readability and reference-completeness work above.

## Gap

None — every item on your list is covered by a named skill.

## Where to actually run this

Since five of the six skills live in `developer-platform-skills`, the right entry point for doing the work is that collection's own router, `samber/developer-platform-skills@developer-platform-kickoff`, not this one — `developer-relations-kickoff`'s own rule is to name the sibling and stop rather than execute its routing. Run `coding-agent-docs-optimization` from here once the contract (steps 1–4 above) is settled.

I didn't create or update `devrel-context.md` — this was a single routing question, not a cold-start project interview, so there's nothing durable to persist yet. Say the word if you want this tracked as an ongoing DevRel project and I'll run the full kickoff interview and bootstrap the artifact.