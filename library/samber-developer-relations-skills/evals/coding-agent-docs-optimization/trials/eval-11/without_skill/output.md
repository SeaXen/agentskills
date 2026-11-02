## Where the effort goes: type declarations first, AsyncAPI second, docs pages last

**The eval already told you the ranking.** 5 of 7 runs never opened a docs page — they resolved the SDK from `node_modules` and proceeded with confidence. That's not agent laziness, it's the normal cost model: reading the `.d.ts` + JSDoc that autocomplete/hover already surfaced is free (zero tool calls, zero latency, zero risk of a blocked fetch); opening a URL is a discrete, skippable action. Docs pages only get read by an agent that already suspects the types are insufficient — and your bug is exactly the case where the agent *didn't* suspect that, because a one-line JSDoc reads as complete, not as a stub. Confident-and-wrong is the worst outcome your eval could produce; it beats "slow but correct" for narrative but is worse for the customer.

So effort should go where the agent already looks, in this order:

### Tier 1 — JSDoc on the public API surface (do this first, it's the whole lever)

- Rewrite JSDoc for every exported method that takes an options object, has overloads, or exposes enum-like string values. `subscribe()` is priority one; audit the rest of the client with the same lens.
- For `subscribe()` specifically, document every field of the options parameter, its default, and its effect — not the method in one line. Add a runnable `@example` that includes a consumer group. Agents pattern-match off `@example` blocks almost verbatim; an example is worth more than a paragraph of prose.
- Go further than prose: fix this at the **type level**, not just the comment level. A loose `consumerGroup?: string` next to a one-liner gives the agent nothing to fail against — TypeScript will happily accept whatever the agent guesses. If subscribing without a consumer group and subscribing with one are semantically different operations (different delivery guarantees, different offset behavior), model that as a discriminated union or two distinct call shapes, so a wrong guess doesn't typecheck instead of merely being under-documented. This is the strongest fix available, because it doesn't depend on the agent reading anything — the compiler does the correcting.
- Treat this as a checklist pass across the whole SDK, not a one-off patch to `subscribe()`: any method where the current JSDoc restates the method name instead of explaining behavior, defaults, and side effects is the same bug.

### Tier 2 — AsyncAPI annotations (conditional, and probably not what caused this specific bug)

- Your `subscribe()` failure was about client-call semantics, not payload shape — annotating the AsyncAPI doc wouldn't have fixed it. Don't let it absorb the effort earmarked for Tier 1.
- It matters for a *different* failure mode: agents guessing field names/types/optionality on event payloads when producing or handling messages. That's plausible but unverified — you tested consumer groups, not payload correctness. Add 1–2 tasks to your eval that specifically exercise payload construction/consumption before spending effort here, so you're not annotating against a hypothetical gap.
- One thing worth checking before scoping this: does Kestrel generate the payload `.d.ts` types from the AsyncAPI document? If yes, annotating AsyncAPI `description` fields is the *same lever* as Tier 1 — it flows straight into the types agents already read for free, and should be promoted to Tier 1 priority. If the AsyncAPI doc is a detached artifact nobody's codegen touches, it's Tier 2: real, but lower-leverage, since almost nothing in your eval shows agents opening it today.

### Tier 3 — Docs pages (keep maintained, don't lead with it)

- Only 2 of 7 runs fetched docs at all, so this is the lowest-leverage channel for *this* failure mode — but it's not zero, and it's still what humans and the minority of docs-fetching agent runs depend on.
- When you do touch it, put the canonical, runnable example (including the consumer-group case) at the top of the `subscribe()` reference page, not buried in prose — the same "example over explanation" bias applies whether it's an agent or a developer skimming.
- If you also care about being cited by AI answer engines (a separate concern from coding-agent correctness), that's an `llms.txt`/AI-search-visibility question — lower priority than this and shouldn't compete for the same sprint.

### Process check

Re-run your existing 7-task eval after the Tier 1 JSDoc/type pass, before touching AsyncAPI or docs. You have a working regression harness — use it to confirm the consumer-group task now passes, rather than assuming better comments fixed it. If it doesn't pass, the type-level fix (making the wrong shape not compile) is the fallback that doesn't rely on the agent reading anything at all.