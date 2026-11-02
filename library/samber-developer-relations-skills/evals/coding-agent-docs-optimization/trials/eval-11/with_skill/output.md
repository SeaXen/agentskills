# Agent-readiness recommendation — Kestrel Streams TypeScript SDK

## Where the effort goes, in order

1. **Rewrite JSDoc/TSDoc on the SDK's public surface, starting with `subscribe()`.** Your own baseline already proves this is where the agent reads: 5 of 7 tasks never fetched a page, they read `.d.ts` straight from `node_modules`. That is the exact trigger condition this skill promotes SDK doc comments above every other surface for. Doc-site work you do this week will not touch those 5 tasks at all — the agent isn't in the doc site.
2. **Annotate the AsyncAPI 3.0 document, but only the mechanical fields first** (stable operation keys, enums, `required`, protocol bindings) **— not full prose descriptions yet.** You have no cold-run evidence that a task actually exercised payload construction/parsing, so the expensive prose pass doesn't qualify for the findings list yet. The cheap structural pass does, because it's near-zero cost and closes the same "structurally valid, semantically wrong" failure class that just bit `subscribe()`.
3. **Add 2 payload-handling tasks to the task set and re-run**, before deciding whether AsyncAPI's expensive `description` fields are worth the week they cost. You're an event-streaming vendor — "construct a payload for topic X and publish it" and "consume and deserialize a payload, handle a schema-version mismatch" are almost certainly in your top revenue-driving jobs, and they're conspicuously absent from a 7-task set that apparently only surfaced a `subscribe()` bug.
4. **Everything else — index file, markdown endpoints, full-corpus bundle, version labels — waits.** Not because they're worthless, but because 2 of your 7 tasks apparently did try to fetch docs and you haven't told me what happened there. That's the next thing to look at, not a new surface to build.

Below is the reasoning and the concrete edits, in the audit-report shape this skill uses.

---

## Interview answers used (stated or inferred — flag if wrong)

| # | Answer used | Status |
|---|---|---|
| 1 | Client SDK (TypeScript, `.d.ts`), plus an AsyncAPI 3.0 spec for event payloads | Given |
| 2 | AsyncAPI 3.0 exists, publicly referenced, annotation status: none. Whether it's generated from the implementation or hand-maintained | **Unknown — changes AsyncAPI effort estimate, ask** |
| 3 | Docs live somewhere you can fetch; where and whether you control build/headers/CDN bot policy | **Unknown — this is Workflow step 1, the gate, run it before trusting anything below** |
| 4 | 7 integration jobs already exist as the frozen cold-run set | Given (count is fine — skill wants 5-10) |
| 5 | Known failure: `subscribe()` consumer-group option invented, traced to a one-line JSDoc | Given |
| 6 | Vendor with a first-party SDK — commercial, not a volunteer-maintainer OSS project | Inferred from "managed event streaming" |
| 7 | TypeScript is the SDK in scope; other language parity unstated | Partial |
| 8-10 | No hard date, no stated ceiling stated | **Unknown — the ranking below assumes a standing mandate (SDK ships doc-comment fixes every release) rather than a one-shot fix. If this is a one-release push before a launch, re-rank: drop the AsyncAPI structural pass too and spend everything on the SDK doc comments plus the two highest-traffic pages.** |

## Step 0: verify the gate before trusting any of this

You haven't said whether an agent can fetch your docs at all. Two of seven tasks apparently *did* go to the docs (unstated outcome) — find out whether they succeeded, got a challenge page, or fetched something stale. If a WAF or bot-management default is silently blocking, that's a zero-effort dashboard fix that unblocks every future doc-site investment; skip verifying it and you can spend a quarter improving pages an agent never reaches.

## Findings (task-impact ordered)

### Finding 1 — `subscribe()` invents its consumer-group behavior

- **Task:** unstated, but reconstructable as something like "Subscribe to a topic as part of a consumer group and process messages."
- **Outcome:** failed/wrong — agent read the `.d.ts` signature, saw a `consumerGroup`-shaped option, and guessed its semantics from the name.
- **Where it looked:** `node_modules/kestrel-streams/**/*.d.ts` only. Never left the local filesystem.
- **Root cause:** the type signature constrains the *shape* of the parameter (TypeScript's job) but not its *contract* — the JSDoc is one line ("Subscribes to a topic.") and says nothing about what the option does, when it's required, what happens if two clients share a group ID, or default behavior when it's omitted.
- **Fix:** rewrite the TSDoc block (below). Don't touch the doc site for this — the agent that failed never got there.
- **Impact:** this is your proof case for "cold run shows the agent reading local code instead of fetching pages" — the exact condition that reorders this skill's whole priority list. Fix it first regardless of what else is on the list.

### Finding 2 — AsyncAPI payload contract is unexercised, not (yet) proven broken

- **Task:** none in your current 7 appears to test it.
- **Outcome:** unknown — you cannot fail a task you never ran.
- **Where it looked:** n/a.
- **Root cause:** the task set has a gap, not necessarily the spec.
- **Fix:** add the task, don't pre-annotate on faith. Do the cheap structural pass (below) in parallel since it costs almost nothing and the failure mechanism is identical to Finding 1.
- **Impact:** deferred pending evidence, per this skill's own rule — "a finding on a task no cold run failed does not make the list at all, however easy it would be to fix." Listed here so it isn't silently dropped.

## Which surface to build first — re-ranked for Kestrel

Skill default order (effort/value/efficiency general case) says lead with markdown endpoints and annotated spec files, and treat SDK doc comments as a standing cost that never wins on ratio. That default is explicitly overridden by one condition, and you're it:

> "Promote [SDK doc comments] above everything when the product ships typed SDKs and the cold runs show the agent reading local code instead of fetching pages."

Re-ranked:

1. **SDK doc comments (TSDoc/JSDoc)** — was ranked 5th/6th by default, now 1st. Reaches the agent that already proved it won't leave `node_modules`.
2. **AsyncAPI spec, structural fields only** (stable operation/message names, `enum`, `required`, protocol bindings) — cheap, mechanical, same failure class as #1.
3. **Access check** — free, do it this week regardless of rank; it's the gate everything else is scored against.
4. **AsyncAPI spec, `summary`/`description` prose** — held pending Finding 2 getting real evidence. This is the expensive one (a week on a real spec, per the spec-annotation reference); don't spend it on a hypothesis.
5. **Markdown endpoints, index file, version labels, full-corpus bundle** — parked. Nothing here helps a task that never fetches a page, and you don't yet know what your doc-fetching 2-of-7 tasks actually needed.

## The concrete edit for Finding 1

Before (what's shipping now):

```ts
/**
 * Subscribes to a topic.
 */
subscribe(topic: string, options?: SubscribeOptions): Subscription;
```

After — apply the page-rewrite patterns (self-containment, snippet completeness, answer-first) to the doc comment itself, since for this agent the doc comment *is* the page:

```ts
/**
 * Subscribes to a topic and starts delivering messages to the returned Subscription.
 *
 * Requires a connected {@link KestrelClient} (see `connect()`).
 *
 * `options.consumerGroup` controls delivery, not just naming:
 * - Omitted: exclusive subscription — this client receives every message on the topic,
 *   and offsets are not persisted across restarts.
 * - Set: joins (or creates, if new) a named consumer group. Kestrel load-balances
 *   partitions across every client sharing the same `consumerGroup` string, and commits
 *   offsets so a restart resumes rather than replays. Two clients in the same process
 *   with the same group id compete for partitions — they do not both receive every message.
 *
 * @example
 * ```ts
 * import { KestrelClient } from "kestrel-streams"; // kestrel-streams@^2.3
 *
 * const client = new KestrelClient({ apiKey: process.env.KESTREL_API_KEY });
 * const sub = client.subscribe("orders.created", { consumerGroup: "billing-service" });
 *
 * for await (const message of sub) {
 *   console.log(message.payload.orderId); // stops iterating on sub.close()
 * }
 * ```
 *
 * @param topic - Topic name, e.g. `"orders.created"`. Must already exist; see `createTopic`.
 * @param options.consumerGroup - See above. Omit for exclusive, non-durable delivery.
 * @returns A {@link Subscription} (async-iterable). Throws `TopicNotFoundError` if the topic doesn't exist.
 */
subscribe(topic: string, options?: SubscribeOptions): Subscription;
```

Apply the same pass to every other public method before widening scope — per the skill's page rules, this is one editing pass per already-open file, not a redesign.

## The AsyncAPI structural pass (do now, cheap)

Two caveats up front, stated because the source material is explicit about them: AsyncAPI guidance here is inferred from the OpenAPI annotation rules by analogy, not separately sourced — and if `consumerGroup` has a protocol binding entry in your AsyncAPI document (a Kafka-style binding object often carries a group-id field), **that binding is your actual source of truth** for Finding 1, not something separate. Check that first — if it exists, write the semantic contract there once and have the TSDoc point at or mirror it, rather than authoring the same fact twice and letting one copy drift.

Otherwise, work the cheap fields only, this pass:

- Give every AsyncAPI operation a stable, unique, verb-noun key (`publishOrderCreated`, not an auto-generated one) — same leverage as `operationId`, for the same reason: it's what any future tool-name generation derives from.
- Close every payload field's value space you already know the answer to: enums for status/type fields, `required` on mandatory fields, `format` for UUIDs/timestamps, instead of leaving them as bare `string`.
- Leave `description` empty for now on fields you're not confident about — an empty field is honest; a guessed one is worse.

## What "done" looks like

- Re-run the same 7 tasks, unattended, fresh context, after the `subscribe()` rewrite ships in a release — not before, since a doc comment fix that only lives in a PR doesn't reach an agent reading installed types.
- Add the 2 payload-handling tasks, run them once as a new baseline (not graded against the old 7 — it's evidence-gathering, not a re-run).
- Zero invented API surface on `subscribe()` and whatever your top 2 other tasks are is the bar — not a percentage. 80% first-attempt is a stretch goal from Stripe's published benchmark, not a floor to hold this one fix to.
- If the new payload tasks fail, that's what promotes AsyncAPI's `description` pass from "parked" to "next." If they pass on the structural fixes alone, the expensive prose pass stays parked — don't spend the week on faith either way.