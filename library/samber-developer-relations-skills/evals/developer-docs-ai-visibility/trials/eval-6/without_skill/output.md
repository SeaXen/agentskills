Partly wrong. Don't rewrite the getting-started page yet.

**Next action:** ask Copilot and Cursor, in a fresh empty project, to "write code to initialize the Ashgrove Metrics Go SDK". Takes about 15 minutes. Details below.

## Why the theory is weak

1. **A zero in your CDN logs doesn't show the tools can't see your docs.**
   - Inline completion mostly comes from model weights plus the user's open files. It makes no live docs request.
   - Training crawls happened months ago, so a 30-day window can't show them.
   - Tools that fetch on demand (Cursor `@Docs`, web search) may not identify themselves as bots. Many fetch through proxies or generic user agents.
2. **Visibility is probably not the problem. Stale training data is the likelier cause.**
   - `legacyBatch` existed for years before 5.0 and was removed only a year ago.
   - Old blog posts, GitHub repos, Stack Overflow answers, and 4.x docs pages probably still carry it. The model repeats the majority pattern.
   - A clearer page won't outvote that, because the tool isn't reading the page when it writes the code.
3. **A markdown version helps only agents that fetch your docs at runtime.** It's cheap, but it won't stop these tickets alone.

I can't see your logs or the tools' internals. This is general knowledge about how they work, not a measurement of your case.

## Test it (15 to 30 minutes)

1. Ask Copilot and Cursor, in an empty project with no docs context, to initialize the SDK. Do this for Go and for Java.
   - If they emit `legacyBatch: true`, the cause is training data. The theory is wrong.
2. Repeat with your getting-started URL given to the tool (Cursor `@Docs` or `@Web`).
   - If they now emit correct code, docs do help once the tool reads them. The page content is fine, and the gap is retrieval.
   - If they still emit `legacyBatch`, the page itself is the problem. Only then does a rewrite make sense.
3. Search for `legacyBatch` in your own surfaces:
   - docs, including versioned 4.x pages
   - example repos and READMEs
   - blog posts and the Go/Java package pages
   - Any live hit is feeding the models.
4. Open 3 of the 23 tickets. Record the SDK version and what error the customer saw.
   - If they ran 5.x, the SDK failed in a way the tool and the customer couldn't understand. That's your biggest lever.

## What to do, ranked by leverage

1. **Make the SDK fix itself.** Coding agents read compile and runtime errors, then correct their code.
   - In a 5.x patch, make a removed option fail loudly with a pointed message, in both clients. Example: `legacyBatch was removed in 5.0; use <replacement>. See <migration URL>`.
   - Takes about half a day per client. This is the only fix that works whatever the tool read.
2. **Clean up the 4.x pages.** Add a "removed in 5.0" banner and point canonical links at the latest version. Consider `noindex` on old versions. About 1 to 2 hours.
3. **Add an explicit migration entry that names `legacyBatch`.** It will rank for the exact string customers paste. About 1 hour.
4. **Ship `.md` versions of the pages plus `llms.txt`.** Cheap, helps runtime-fetching agents. About 2 hours. Do it, but expect little effect on these 23 tickets.
5. **Rewrite getting-started only if step 2 of the test shows the page is the problem.** Skip it otherwise.

## Open question

What does the customer see today when `legacyBatch: true` hits SDK 5.x? A silent ignore, a cryptic compile error, or a clear message? That answer decides how much item 1 is worth.

**Next:** run the test above and tell me what Copilot and Cursor emit with and without the docs URL.