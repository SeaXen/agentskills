# Mnemosyne dashboard graph empty-state and triples diagnosis

Use this when the standalone Mnemosyne dashboard shows a blank Knowledge Graph while other memory views still look populated.

## Verified diagnosis pattern

Live store shape observed in this session:

- `working_memory`: populated
- `episodic_memory`: populated
- `triples`: `0`
- `annotations`: populated
- `graph_edges`: populated
- `memoria_facts`: populated
- `memoria_kg`: populated

Result:
- Overview works
- History works
- Search works
- Visualiser works
- Knowledge Graph remains empty

This is **not** a renderer failure if the graph tab explicitly queries the SQL `triples` table.

## Key explanation to give the user

The dashboard's Knowledge Graph is backed by the `triples` table specifically.
Other stores like:
- `annotations`
- `graph_edges`
- `memoria_facts`
- `memoria_kg`

do **not automatically populate that graph view**.

So a blank graph with `triples = 0` means:
- memory exists
- some enrichment/annotation exists
- but **fact triples for the dashboard graph have not been written**

## Mnemosyne ingest semantics to explain plainly

Normal memory writes do not create graph facts by default.

Relevant behavior:
- `mnemosyne_remember(... extract=false)` is the default path
- without `extract=true`, fact triples are not added to `triples`
- manual triple writes via `mnemosyne_triple_add(...)` do populate the graph's backing table

## Recommended operator guidance

When the graph is empty but the store is otherwise healthy:

1. Say the graph is **data-empty, not broken**.
2. Confirm `triples` count with a real triple query.
3. Explain that normal remembers are storing memory but not fact triples.
4. Suggest one of two ways to populate it:
   - curated manual facts via `mnemosyne_triple_add`
   - selective enriched writes via `mnemosyne_remember(... extract=true)`
5. Avoid recommending blanket extraction everywhere unless the user explicitly wants a noisier graph.

## UX implication

If you patch the dashboard, prefer an empty-state message that tells the operator what to do next, for example:

- graph is empty because no triples exist
- add facts with `mnemosyne_triple_add`
- or store memories with `mnemosyne_remember(... extract=true)`

That turns an honest blank state into an actionable one.
