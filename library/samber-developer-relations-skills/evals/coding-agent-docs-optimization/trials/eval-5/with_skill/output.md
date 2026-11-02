## Short answer

No. Spending the whole sprint on rich per-operation prose is the fourth-highest-leverage fix for this spec, not the first. With 90/140 operations missing `operationId` and most query params typed as unconstrained strings, the sprint is aimed at the wrong end of the failure mode. Reorder it.

## Why the "description is what the model reads" theory is incomplete

It's true, but it's not the *first* thing the model reads.

- **The tool name comes from `operationId`, not from the description.** Generators (`openapi-to-mcp`, FastMCP, etc.) turn `operationId` into the agent-facing function name. When it's absent, the fallback is a `{method}_{path}` slug like `get_api_v1_customers_id` — a name models handle badly, and some generators discard names that fail their pattern check entirely. No description, however well written, attaches to a tool the agent never selects because its name is garbage or its slot got dropped.
- **An unconstrained parameter is where invented values go**, independent of how good the description is. `type: string` with no `enum`, no `format`, no `pattern` means the agent is guessing at valid values from prose scattered elsewhere — or just inventing one that looks plausible. A gorgeous paragraph of prose sitting next to a free-form string field doesn't stop that; a one-line `enum:` does.
- Anthropic's own reported result — precise tool-description refinement improving SWE-bench — is real evidence that descriptions matter. But it doesn't say descriptions matter *before* the tool has a usable name and its arguments have a closed value space. Both fixes are cheaper than the one the sprint is currently pointed at.

## What actually ranks first, and why

Ranked by invented-calls-prevented per hour of work, not by what feels thorough:

1. **`operationId` on all 90 missing operations.** Mechanical, near-zero effort per operation, and it's the single highest-leverage field in the whole spec. Verb-noun camelCase (`listEmployees`, `getPayrollRun`), ≤30 characters, unique and stable across releases. This is generated from a Go handler on every build — it should come from the route/handler name in the generator, not be typed by hand into the output file. **This is not technical-writer work; it's a code-generation fix**, probably a few hours for one engineer, not a sprint task for two writers.
2. **Close the value space on the query parameters.** For every `type: string` that's actually a fixed set of values (status filters, pay period types, sort fields, department codes — the stuff an HR/payroll API is full of), add `enum`. Add `required`, `default`, and `format` (`date`, `date-time`, `uuid`) wherever they apply. This is a one-line edit per field, and each one removes a whole class of invented values. This *does* need domain knowledge — pair one writer with one backend engineer who knows what the Go validation layer actually accepts, since that validation logic almost certainly already encodes these constraints and just never made it into the spec.
3. **Decide on curation, given 140 operations.** Past roughly 20–30 operations exposed at once, tool selection degrades — that's OpenAI's own function-calling guidance, and FastMCP reports auto-converted OpenAPI servers underperforming curated ones specifically on APIs this size. If this spec is (or will be) converted into a callable tool surface, plan tag-based filtering now. If it's staying doc-only, this doesn't apply — but confirm that before writing 140 descriptions.
4. **`summary` / `description`, split by job — this is where your writers belong, once 1–3 are in shape.** `summary`: one imperative line, for disambiguation. `description`: preconditions, side effects, idempotency, required auth scope, rate limits, response shape, and a pointer to the sibling operation that might fit better. That's dense, structured, per-field information — not the "rich multi-paragraph narrative" your writers are picturing. Multi-paragraph prose is easy to skim past and expensive to keep in sync; a tight operational contract is what an agent actually uses to pick between two similar-looking payroll endpoints.
5. **Runnable per-operation samples — not this sprint.** These are the highest-value single fix for whichever 2–3 operations your own testing shows agents repeatedly getting wrong, but they're a standing maintenance cost across languages and don't belong in a first pass across all 140.

## The trap specific to your setup

The spec is generated from Go handlers on every build. If the writers add `operationId`, enums, or descriptions directly to the generated OpenAPI file, **the next build silently overwrites all of it.** Every annotation needs to land in the source the generator reads from — Go doc comments, struct tags, or whatever annotation mechanism your generator supports — or in a generator config the build step merges in. Confirm this mechanism exists (or build it) before either writer opens the spec file itself; otherwise the sprint's output has a shelf life of one build.

## What I'd actually book the sprint as

- **~0.5 day, one engineer:** wire `operationId` generation into the build from the handler/route name.
- **~1–2 days, writer + engineer pairing:** pull real constraints out of the Go validation code into `enum`/`required`/`format`/`default` for the query and body parameters. This is likely the single biggest reduction in invented calls you'll get all sprint.
- **Decision point, docs/eng lead:** is this spec becoming an MCP/tool surface? If yes, scope the tag-based curation now, separately from the writing work.
- **Remaining sprint time, both writers:** `summary` + `description` per operation, written as an operational contract (precondition / side effect / auth scope / rate limit / sibling pointer), prioritized by which operations your top integration tasks actually touch — not alphabetically through all 140.
- **Before calling it done:** run a handful of realistic integration tasks ("run payroll for a pay period and handle a validation error," "look up an employee's benefits enrollment," "paginate all terminated employees in the last quarter") against the docs alone, cold, and see what actually breaks. That tells you whether the remaining sprint hours are going to the right operations, instead of guessing from a theory about which field the model reads.

The instinct that descriptions matter is correct. The mistake is treating "multi-paragraph and rich" as the goal instead of "structurally complete and unambiguous" — and spending a whole sprint on paragraph five while fields one through three are still empty.