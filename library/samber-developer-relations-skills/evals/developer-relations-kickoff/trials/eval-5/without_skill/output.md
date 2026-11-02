## Which skills cover this

- **sdk-dx** — API/error design, error-message framework, versioning. Used for the 429 body shape and the error taxonomy.
- **docs-as-marketing** — information architecture (tutorial/how-to/reference/explanation split), quickstart structure, "copy-paste code must work" rule. Used for the docs plan.
- **ai-seo** (agent-readiness section) — machine-readable files (`llms.txt`, `/pricing.md`-style patterns), avoiding JS-only rendering, semantic structure for non-human readers. Used for the "readable by unattended coding agents" requirement.
- **technical-tutorials** — prerequisites, checkpoints, troubleshooting blocks. Used for the rate-limit/idempotency/webhook guides.

No skill in the catalog covers rate-limiting algorithms, idempotency-key semantics, or webhook delivery guarantees directly — those are backend-protocol design, not a documented skill. The design below follows established external-API conventions (Stripe/GitHub/Twilio-class APIs), which is what a coding agent integrating unattended will already have priors on — deviating from these conventions without reason is itself a DX cost.

---

## 1. Rate limiting

**Algorithm:** token bucket per API key (not per IP — this is B2B, keys are the identity), one bucket per rate-limit *policy* (reads vs. writes get separate policies since writes are more expensive).

**Headers (every response, not just 429s):**

| Header | Meaning |
|---|---|
| `RateLimit-Limit` | Bucket capacity for this request's policy |
| `RateLimit-Remaining` | Tokens left in the current window |
| `RateLimit-Reset` | Seconds until the bucket fully refills |
| `RateLimit-Policy` | Name of the policy applied, e.g. `writes;w=60` |

Only ship this one canonical set. Do **not** also ship legacy `X-RateLimit-*` aliases — there's no legacy consumer to support, and two names for the same value is exactly the kind of ambiguity that trips up a client (human or agent) that greps headers rather than reading a changelog.

On a 429, additionally send `Retry-After: <seconds>` — it's the one rate-limit-adjacent header with actual HTTP-spec standing (RFC 7231), so generic HTTP clients and agent frameworks that already special-case it will back off correctly even if they've never seen Ferrograph's docs.

**429 body** — same envelope as every other error (see §1a), so an integrator writes one parser, not one per status code:

```json
{
  "error": {
    "type": "rate_limit_exceeded",
    "code": "rate_limit_exceeded",
    "message": "Rate limit exceeded for policy 'writes'. Retry after 12 seconds.",
    "request_id": "req_01J8X9K3ZC",
    "retry_after": 12,
    "doc_url": "https://developers.ferrograph.com/errors/rate_limit_exceeded"
  }
}
```

**1a. Canonical error envelope** (used for 400/401/403/404/409/422/429/500 alike):

```json
{
  "error": {
    "type": "<machine_readable_slug>",
    "code": "<machine_readable_slug>",
    "message": "<human sentence, safe to log>",
    "request_id": "<for support correlation>",
    "doc_url": "<link to the specific error page>"
  }
}
```

`type`/`code` duplication is intentional: some client generators key off `error.code`, others off `error.type` (Stripe-style vs. GitHub-style) — supporting both costs nothing and removes a guess for whichever convention an agent's training leans toward. Every field beyond `message` is optional per-error-type (`retry_after` only on 429, `param`/`field` only on 400/422).

---

## 2. Idempotency keys

**Header:** `Idempotency-Key` — reuse the Stripe name deliberately; it's the pattern coding agents already default to when they see "idempotent write" in a prompt.

**Scope of enforcement:** required on every `POST` that creates or mutates a billable/side-effecting resource (charges, orders, anything "double-charging" applies to). Optional-but-honored on other mutating verbs (`PUT`/`PATCH`/`DELETE`), since those are naturally idempotent by resource ID already.

**Key shape:** opaque client-generated string (UUID v4 recommended), ASCII, ≤ 255 bytes.

**Server behavior**, keyed by `(account_id, Idempotency-Key)`:

| State | Response |
|---|---|
| New key | Process normally, store `{request_hash, status_code, response_body}`, return result |
| Same key, same request body hash, **completed** | Replay stored `status_code`/`body` verbatim, add `Idempotency-Replayed: true` |
| Same key, same request body hash, **still in flight** | `409 Conflict`, `error.type = "idempotency_key_in_progress"`, `Retry-After` set to a short backoff |
| Same key, **different** request body hash | `422 Unprocessable Entity`, `error.type = "idempotency_key_reused_with_different_params"` — reject before touching the resource layer, never partially apply |

`request_hash` is a hash of the normalized request body — this is what stops a client from reusing a key across two *different* payloads and silently getting the first payload's result back.

**Storage:** dedicated table, `(account_id, idempotency_key)` unique index, columns for `request_hash`, `status_code`, `response_body`, `locked_until`, `created_at`. The `locked_until` column implements the in-flight lock (short TTL, ~60s) so two near-simultaneous retries of the same request don't both hit the write path — the second one gets the 409 above instead of racing.

**Retention:** 24 hours. Long enough to cover realistic retry storms (mobile connectivity gaps, overnight batch-job backoff), short enough to bound table growth without a full archival tier.

---

## 3. Webhook retry & replay

**Delivery:** at-least-once, `POST`, JSON body, 5s connect / 15s total timeout, success = any 2xx.

**Signing:** `Ferrograph-Signature: t=<unix_ts>,v1=<hex hmac-sha256>` over `"{t}.{raw_body}"`. Support two active secrets per endpoint (current + previous) so rotation never causes a delivery gap — verify against both, accept if either matches.

**Retry schedule** — exponential backoff with ±20% jitter (jitter prevents every failing endpoint's retries from synchronizing into a thundering herd), spread over 72 hours, 10 attempts:

```
T+0, +1m, +5m, +30m, +2h, +6h, +12h, +24h, +48h, +72h
```

72 hours matches the realistic window for "customer's on-call fixes their endpoint," without keeping a queue open indefinitely.

**Auto-disable:** after 100 consecutive failed deliveries to one endpoint within 24h, disable it automatically and notify the account (dashboard + email). Protects Ferrograph from spending retry budget on a permanently-dead endpoint, and protects the customer from silently missing 3 days of events without knowing.

**Ordering:** explicitly **not** guaranteed. Every event carries `id` (stable across redelivery/replay) and a per-resource monotonic `sequence` field. State this loudly in docs — it's the assumption most likely to break an unattended integration, since "webhooks arrive in order" is the default (wrong) mental model.

**Consumer-side idempotency:** since retries *and* replay can redeliver the same `event.id`, the docs must tell integrators to dedupe on `event.id`, not assume "received once."

**Replay API:**

```
POST /v1/webhook_endpoints/{endpoint_id}/events/{event_id}/replay
POST /v1/webhook_endpoints/{endpoint_id}/replay?since=...&until=...   # async bulk job, returns a job id
```

Replay creates a **new** delivery attempt record — it doesn't reuse or reset the original attempt counter, so replay history stays distinguishable from organic retries in the dashboard/logs. Bulk replay is itself rate-limited (same §1 mechanism) so a large backfill can't self-DoS the webhook fan-out path.

**Event log retention:** 30 days minimum — this is the outer bound on what `since`/`until` and single-event replay can reach.

---

## 4. Documentation plan

**Structure** (docs-as-marketing's four-type split):

```
Quickstart          — first authenticated call in <5 min
Guides/
  ├── rate-limiting.md      (technical-tutorials shape: prereqs → checkpoint → troubleshooting)
  ├── idempotent-writes.md
  └── webhooks-retry-replay.md
Reference/           — generated from OpenAPI, not hand-maintained
  ├── endpoints (per-resource)
  └── errors.md      — every error.type, its cause, its fix (sdk-dx error framework)
Explanation/
  ├── retry-and-backoff-rationale.md
  └── security-model.md
```

Each guide follows the same shape: prerequisites table → runnable curl example → expected response → checkpoint ("you should see X") → troubleshooting section for the 2–3 most likely mistakes (e.g., "reused an idempotency key with a different body," "webhook signature verification failing because you hashed the parsed body instead of the raw bytes").

**Source of truth:** one OpenAPI 3.1 spec, publicly fetchable at `/openapi.yaml`, no auth wall. Reference docs, SDKs, and Postman/Insomnia collections all generate from it — never hand-sync three copies of the same endpoint list.

**Agent-readability (the "unattended coding agent" requirement):**

- **`/llms.txt`** at the root: one-paragraph product summary + direct links to `/openapi.yaml`, the three guides above, and `errors.md`. This is the file an agent looks for first before it starts scraping HTML.
- **No JS-only rendering.** Docs must return real content on first response (SSR or static). An agent that doesn't execute a JS bundle sees an empty page otherwise — same failure mode as a search-engine crawler.
- **Markdown available at every doc URL**, either via `.md` suffix or `Accept: text/markdown` content negotiation. Agents parse clean Markdown far more reliably than they parse rendered HTML with nav chrome stripped out.
- **One canonical name per concept.** No `X-RateLimit-*` vs. `RateLimit-*` synonyms, no two different error-shape conventions on different endpoints. Every inconsistency here is a decision point a human skims past and an unattended agent gets wrong.
- **Every code sample must run unmodified when copied** — curl plus at least one SDK language per example — and should be tested in CI against a sandbox/mock server so a stale example never ships. An agent that copies a broken quickstart sample has no human in the loop to notice it failed for a *documentation* reason rather than an *integration* reason.
- **`errors.md` is exhaustive and structured** (table: `type`, cause, fix, retryable Y/N) rather than prose — this is the single highest-leverage page for unattended error recovery, since an agent's retry/backoff logic branches directly on `error.type`.