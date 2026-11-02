Script ready. Promise: for a developer deciding whether to adopt it, this video shows Fernwood's query builder replacing raw-SQL strings, running against real data, and catching type errors at compile time. Shape: feature walkthrough, 4 min. Narration only, chaptered — you handle the screen.

---

## Chapters

- `00:00` The problem with string-built queries
- `00:30` The old way: raw SQL strings
- `01:05` Building the same query with the builder
- `01:40` Running it against the sample database
- `02:15` The generated SQL
- `02:50` The type errors it catches
- `03:50` Wrap-up

## Narration

**[00:00 — Hook]**
Someone on our team once shipped a query with WHERE status equals 'paif' — a typo. It compiled. It ran. It just silently returned nothing, because to TypeScript, SQL is just a string. That's what the Fernwood query builder fixes. In four minutes: the old string-based way, the builder syntax that replaces it, a live run against the sample database, the SQL it actually generates, and the type errors it catches before you ship. You'll need Fernwood CLI 2.4 and the sample orders database — link's below.

**[00:30 — The old way]**
Here's how we wrote this query before: a template string, with values spliced straight in. It works — until a value has an apostrophe in it, or someone renames a column and nothing here warns you. To the compiler, this is just text. No autocomplete, no type checking, nothing catches the mistake before the query runs.
*[on screen, not spoken: `SELECT id, customer_id, total FROM orders WHERE status = '${status}' AND total > ${minTotal}`]*

**[01:05 — Builder syntax]**
Now the same query with the builder. Every piece is checked against the real schema — the table name, the column names, the operators, all of it — at compile time, not discovered later in production. You're not writing SQL text anymore. You're describing the query, and the builder writes the SQL for you.
*[on screen, not spoken: `db.table('orders').where('status', '=', status).andWhere('total', '>', minTotal).select('id', 'customer_id', 'total')`]*

**[01:40 — Run it]**
Let's run it against the sample orders database.
*[run the command, pause ~4s for the result — don't narrate over it]*
Three rows come back — the paid orders over a hundred dollars. Same result the string version gave us, but this time we never typed a single quote or concatenated a value by hand.

**[02:15 — Generated SQL]**
The builder still produces plain SQL underneath it. Call `.toSQL()` and here's exactly what ran: a select for id, customer ID, and total, from orders, where status equals one bound parameter and total is greater than a second — your values passed in as parameters, never concatenated into the string. That's also what closes the SQL injection gap the old version had.

**[02:50 — Type errors]**
Here's the part that matters most. I'll rename `total` to `total_amount` in the schema, without touching this query.
*[rebuild, pause ~4s on the error]*
Build fails immediately: property 'total' does not exist on type 'orders'. The old version would only have caught that in production, once it started returning undefined. Here's what happens next, when I pass a string where a number's expected.
*[pause ~4s on the error]*
Argument of type 'string' is not assignable to type 'number'. Both of those used to be runtime bugs someone found the hard way. Now they're compile errors, caught before the code ever merges.

**[03:50 — Wrap-up]**
That's the query builder: same SQL underneath, but now the compiler is reading it with you. It ships today as `@fernwood/query-builder` — migration guide's linked below.

## Runtime

~449 words ÷ 150 wpm (assumed rate — swap for your own measured pace) ≈ 3:00 speaking + ~12s scripted pauses ≈ **3:12 total**, against a 4:00 target. ~48s of buffer built in — don't pad it, just let the demo beats breathe.

## Cut list (if you run long anyway)

Drop the injection-gap line in the generated-SQL section and the "someone found the hard way" aside in the type-errors section — saves ~15s, promise still holds.