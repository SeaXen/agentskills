Three candidates, one per axis, per skill's Step 4 method. Test for each: could a competitor's account paste this unchanged?

**1. Mechanical** — what it does
> I maintain Tideglass — it diffs Postgres schemas and generates the migration to close the gap.

Clean, verb-first, names the exact mechanism. Fails competitor-paste test the least (any real schema-differ could say close to this). Safe default, no reliability claim.

**2. Problem removed** — what pain goes away
> I maintain Tideglass so Postgres migrations stop being hand-written guesses about what your schema changed.

More persuasive, sells the pain removed rather than the mechanism. Reads slightly more marketing-forward; a technical reviewer may want the "how" too.

**3. Recommended** — answers both audiences without splitting the line
> I maintain Tideglass, a Postgres schema differ that generates migrations you review and apply yourself — nothing auto-runs against your database.

Solo dev reads "generates migrations" = can build the thing I need. Bank platform team reads "nothing auto-runs against your database" = answers their real fear (loss of control), no institutional-trust claim needed. Passes competitor-paste test hardest: only true, and only pasteable, if the tool genuinely never auto-applies.

**Recommendation: #3.** It's the only one that does real work for both your named audiences in one sentence, per the skill's "first screen must be identical for both" rule — no need for two separate lines.

**Blocking check before you ship it:** is "nothing auto-runs against your database" literally true for Tideglass today? If there's an `apply` flag or CI auto-apply mode, this line is a false claim on day one and fails the skill's #1 fix priority. Confirm that, then paste #3 as your bio.