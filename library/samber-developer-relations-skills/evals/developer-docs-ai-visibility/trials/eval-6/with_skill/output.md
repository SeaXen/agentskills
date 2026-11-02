# Ashgrove Metrics: why Copilot and Cursor write `legacyBatch: true`

## Verdict

**Your theory doesn't hold, and rewriting the getting-started page is unlikely to fix this.**

1. **Zero AI-bot hits doesn't show the tools can't see your docs.** The likely cause is training recall: the model learned `legacyBatch` from the pre-5.0 corpus and writes it without fetching anything. That produces zero hits in your logs whether the docs are reachable or not.
2. **The first two levers are not a rewrite.** They are a runtime deprecation or removal message in the SDK, and a `legacyBatch` → replacement row in the migration guide and in the 4.x page openers. I ranked these from the failure pattern you described, not from measurement. Step 2's panel will confirm or overturn them.
3. **A markdown twin is not the fix.** Server logs show AI search crawlers almost never request these files, so it is a convenience for coding agents only.

Evidence labels used below: first-party (your logs and tickets), vendor-documented, independently measured, practitioner inference.

## Why the logs don't support your conclusion

| What you saw | What it proves | What it doesn't prove |
|---|---|---|
| 0 AI-bot hits in 30 days of CDN logs (first-party) | No identified AI crawler fetched the docs in that window | That assistants can't read the docs. Training recall never touches your server. |
| 23 tickets, all citing Copilot or Cursor (first-party) | The wrong code reached customers through IDE assistants | Which pipeline produced it |

- **Copilot and Cursor mostly write code from model weights.** Weights are frozen at the training cutoff, so the code can only reflect docs and repos from before that cutoff. `legacyBatch` was in the SDK until 5.0, so a year-old removal is easily still dominant in that corpus. This matches the skill's pattern "GitHub Copilot tells people to use a config flag we removed" (practitioner inference, consistent with how vendors document their bots).
- **When an IDE assistant does fetch a page, a missing log hit is weak evidence.** Many coding agents send generic user agents, so a log gap proves little for them.
- **Zero hits can also mean you are blocking them.** A CDN "block AI crawlers" toggle or managed `robots.txt` that someone outside the docs team enabled would produce the same log. That is a separate problem from the tickets. Step 1 checks it.
- **A clearer getting-started page won't remove `legacyBatch` from the model's memory.** The page presumably already shows `Init(apiKey)` without the flag. If it does, the assistant isn't failing to understand a page it never read.

## Things in your description to check

- **The Go snippet looks odd.** `ashgrove.Init(apiKey)` with `legacyBatch: true` isn't Go option syntax. Go clients usually take functional options or a config struct, and `key: value` named arguments look like JS, Kotlin or Python. Two possibilities, both practitioner inference:
  - the assistant invented this shape for Go, which the panel scores as an invented API;
  - it is the Java builder, or another client, written into the wrong language.
  
  Paste a ticket's exact snippet and say which client it targets. The answer key is per client.
- **The 23 tickets are a lower bound.** Only customers who admitted the code came from an assistant are counted. Tag future tickets "code from an assistant".
- **What the SDK does on a call with `legacyBatch` since 5.0 matters.** If it silently ignores the option, the broken behaviour surfaces late and the ticket is confusing. If it returns a clear error, the fix is already half-built. I haven't seen this, so it is assumed unknown.

## Step 1 - Access check (about an hour, do it first)

| Check | How | What a bad result costs |
|---|---|---|
| `robots.txt` and CDN or bot-management rules, per agent | Read the file and the CDN's AI-crawler setting | A blanket "block AI bots" can remove docs from grounded answers |
| `Google-Extended` | Search `robots.txt` and the CDN preset | Disallowing it removes docs from grounded Gemini answers (vendor-documented). Training opt-out is a separate decision. |
| `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot` | Same | Blocked search agents mean no citation in those products |
| Rules naming only retired tokens such as `anthropic-ai` or `Claude-Web` | Same | They govern nothing |
| Three key pages fetched with a plain HTTP client, no JavaScript | `curl` the getting-started page and two others | Code inside script-loaded tabs is invisible to many AI fetchers |
| `nosnippet`, `max-snippet:0` or `data-nosnippet` on code blocks | View source | Removes pages or code from AI Overviews and AI Mode |

I haven't seen your rules, so all of these are **unreviewed**. Hand any policy decision to `docs-seo`.

## Step 2 - Prompt panel (baseline before changing anything)

Keep it small; your effort ceiling is unknown (`ASSUMED`: part-time docs writer).

- **Assistants:** Copilot and Cursor, per the tickets. Log the underlying model on every row; Cursor can route to different models.
- **Minimum viable panel:** 10 prompts × 5 runs × 2 assistants, plus 5 worst prompts in a second mode. That is about 125 answers, roughly a writer's day.
- **Modes:** where either tool offers web or doc-fetch on and off, run both. The gap between modes is the best pipeline evidence.
- **Prompt families** (from tickets and docs search, not keywords):
  - tasks: initialise, batch events, flush, tracing setup
  - error strings from the 5.0 removal
  - "migrate Ashgrove 4 to 5"
  - "is `legacyBatch` still supported?"
  - one row per language client (Go, Java)
- **Answer key per prompt**, written before any run. Example shape:

```
prompt_id | must contain                       | must not contain       | owning docs URL
G01       | ashgrove.Init(apiKey, <5.x form>)  | legacyBatch ; ashgrove@4 | /docs/getting-started
```

I haven't seen the 5.x replacement for `legacyBatch` or the exact 5.x Go and Java signatures. Interview question 3 supplies them; the key can't be written without them.

- **Score** each answer on: cited source, version-correct, deprecated API present, invented API present, pipeline.
- **Report** pooled rates per prompt family, with n and a Wilson 95% interval. Never a rank position. Five runs of one prompt compare nothing on their own.
- **Agree the targets and the control design now**, before the baseline runs.

## Step 3 - Failure tally by pipeline

The panel hasn't run, so I can only give my current read, labelled practitioner inference:

| Signal | Likely pipeline | Fixable by a docs rewrite? |
|---|---|---|
| No sources, confident `legacyBatch`, same with search off | Training recall | No |
| Cites a 4.x docs page or old blog or repo | Retrieval | Yes, via version identity and stale-copy cleanup |
| Cites the right page and paraphrases it wrong | Retrieval, page ambiguity | Sometimes |
| IDE writes old code with no visible fetch | Recall or an unseen fetch | Page fixes only if a fetch happens |

Run the five tests on each failing prompt: search toggle, source request ("which page is this from?"), version probe ("which Ashgrove version does this target?"), log check, index check. Then name the top stale sources: 4.x docs trees, old blog tutorials, example repos, gists, and third-party tutorials or forum answers. The interview asks for those.

## Step 4 - Levers, ranked, with what I'd delete

**Track one: ship now.**

1. **Version identity in page text.** Put the version in the title, first heading and opening line, e.g. `Getting started (Ashgrove 5.x)`. Superseded 4.x pages open with the replacement and a link to the same page in current. This is one template edit, and it only helps if retrieval or fetch is involved at all.
2. **Clean owned stale copies.** Add a dated version note or archive banner to your own 4.x blog tutorials, example repos and gists that still show `legacyBatch`.
3. **Old-to-new symbol map.** Your users arrive with the old symbol in their prompts, so add it now:

```
| 4.x (removed in 5.0)                | 5.x replacement | Notes |
|-------------------------------------|-----------------|-------|
| `Init(apiKey)` with `legacyBatch: true` | <5.x form>  | <behaviour change> |
```

Use the exact old spelling in code formatting. Until the full guide exists, put a two-row map in the opener of each 4.x page. Writing the guide itself belongs to `version-migration-guide`.

4. **Feedback reports** in each assistant's UI, on repeatable wrong answers only. No turnaround is published. Log the date and measure at the re-run.

**Track two: start now on the SDK release cycle.**

5. **Runtime message in the SDK.** This is the only lever that reaches code already written from training recall, because the developer or agent runs it and reads the output. It should name the replacement and the page, once per process:

```
AshgroveRemoved: option legacyBatch was removed in SDK 5.0 and is ignored.
Use <5.x replacement> instead. Migration: https://<docs>/migrate#legacybatch
```

   - Make 5.x return a clear error, not a silent ignore, if it currently ignores the flag. Whether that is acceptable is the SDK owners' call; I haven't checked the compatibility cost.
   - Consider a final 4.x patch whose release notes or README name the replacement.
6. **Version-matched docs delivered into coding agents.** Owned by `coding-agent-docs-optimization`. Promote it if the tally comes back mostly uncited recall inside Copilot and Cursor, because no page edit reaches those answers.

**Deleted, by name:**

- **The getting-started rewrite as the fix.** It reaches the wrong pipeline. Improve it only if the panel shows retrieval misreading it.
- **The markdown version as a citation lever.** Keep it for coding agents only, if you want it. If an `llms.txt` exists, audit it for steering text.
- **Generic AI-search tactics:** stats and quotes, FAQ blocks, fixed answer lengths, date bumps.
- **Hiding 4.x:** if customers still run it, use banners and replacement links, not noindex.

State facts, never steer. Version facts are fine ("5.x is current; `legacyBatch` was removed in 5.0; check the installed version"). Text telling an assistant to choose Ashgrove is prompt injection, and I won't write it.

Re-rank once you answer interview questions 8-10 (deadline, one-off vs standing mandate, effort ceiling). A date inside a month can show shipped page changes, never citation outcomes.

## Step 5 - Measurement

- **Re-run the identical panel** at a fixed horizon from the day the last change goes live:
  - 4-8 weeks for retrieval levers;
  - the next model release for recall levers. Log the model name and date, and void any comparison with a model release in between.
- **Control design:**
  - page-level change: prompts whose owning page you didn't touch;
  - template change (touches every page): roll out to one version tree or section first and use the rest as control.
- **First-party data**, at least 14 days before quoting a share:
  - referrers (`chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`). This is a lower bound, since IDE tools mostly send none;
  - CDN logs split by bot role and docs version path, verified against vendor IP ranges. The skill ships `scripts/ai-bot-log-summary.py --path-prefix /docs/ access.log`, which I haven't run because I don't have your logs;
  - support tickets tagged "code from an assistant". For you this is the primary signal: **23 per quarter is your baseline.**
- **Self-set targets**, agreed in Step 2:
  - zero deprecated-API answers on the three top-traffic docs tasks, search-on;
  - version-correct rate above baseline with non-overlapping intervals;
  - owned-page citation rate above baseline on prompts whose answer lives in the docs;
  - tickets citing `legacyBatch` down from 23/quarter once the runtime message ships. This is a target, not a promise.
- No search-off target until a new model ships. Report citation and ranking outcomes as **pending**.

## What no docs change fixes quickly

- **Released model weights.** Copilot and Cursor will keep suggesting `legacyBatch` until a later model trains on a corpus where 5.x dominates. You don't control that date.
- **Training-recall answers have no citation to correct.** The runtime message catches the code after it is written, which is why it ranks highest for your pattern even though it costs an SDK release.
- **Third-party tutorials, forum answers and scraped mirrors** with old code. You can add better matches and request corrections; you can't remove them.

## Questions I need answered

1. A ticket's exact `legacyBatch` snippet, and which client it was for (Go or Java).
2. What 5.x does today when `legacyBatch` is passed: ignored, warned or errored.
3. The 5.x replacement for the behaviour `legacyBatch` gave, per client.
4. Whether you can touch the SDK release, or only the docs.
5. Is there a deadline, or is this a standing practice?
6. Your effort ceiling, in docs-writer hours per week.

Without the logs, `robots.txt` and the CDN rules I couldn't do Step 1 or run the log script, so those items are open.