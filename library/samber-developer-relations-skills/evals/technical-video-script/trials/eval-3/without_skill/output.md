Here's the narration script, timed to land at roughly 4 minutes when read at a normal pace (adjust the in-brackets pauses to match your actual typing/demo speed).

---

**[0:00–0:40] — The old way**

"Let's start with how most of us have been writing queries up to now."

*[pull up a raw SQL string built with concatenation or interpolation]*

"This works. It's also fragile. Nothing here checks that `user_status` is spelled right, nothing warns you if you forgot a parameter, and if you're building this string dynamically — adding a `WHERE` clause only when a filter is set — you end up with a pile of string-splicing logic that's easy to get wrong and annoying to test. And if you're not careful with how parameters get inserted, you've opened the door to injection."

**[0:40–1:35] — The builder syntax**

"Here's the same query with the new query builder."

*[type the fluent chain]*

"Same result, but now it's just method calls — `.select()`, `.where()`, `.orderBy()` — chained together. Every one of these is typed, so your editor knows what columns exist on this table, what types they are, and it'll autocomplete them for you. No more guessing whether it's `created_at` or `createdAt`. And because it's just Go — or TypeScript, whatever you're in — that conditional filter I mentioned earlier is now just an `if` statement around a `.where()` call, not string concatenation."

**[1:35–2:20] — Running it**

"Let's actually run this against the sample database."

*[execute, show results]*

"And there's our result set, same as the raw SQL version. The builder isn't some abstraction that only works in theory — it compiles down to a real query and hits the real database, same as if you'd typed it by hand."

**[2:20–3:00] — The generated SQL**

"Which brings up the obvious question: what is it actually sending?"

*[log or print the generated SQL]*

"You can always see the exact SQL it produces. Nothing's hidden. If you want to paste this into `psql` and run `EXPLAIN` on it, or hand it to a DBA to review, it's right here. This matters — the point isn't to hide SQL from you, it's to stop you from hand-assembling it wrong."

**[3:00–3:50] — Catching type errors**

"Now here's the part I actually like the most. Watch what happens if I get something wrong."

*[introduce a deliberate mistake — e.g. compare a string column against an int, or reference a column that doesn't exist]*

"That's a compile error, not a runtime surprise. With the raw string version, a typo like this doesn't show up until the query fails in production, or worse — it doesn't fail, it just silently returns the wrong rows. Here, it's caught before the code ever ships."

**[3:50–4:00] — Close**

"Same queries, same database, but now the mistakes show up on your screen instead of in your logs. That's the query builder."

---

A few notes since I don't have your actual API in front of me: swap in your real method names for `.select()` / `.where()` / `.orderBy()`, and pick a type-error example that's genuinely a compile-time catch in your language (a string-vs-int comparison or an unknown-column reference both read clearly on camera). If your builder does anything clever with the conditional-filter case, that's worth a beat of its own — it's usually the moment viewers who've felt this pain lean in.