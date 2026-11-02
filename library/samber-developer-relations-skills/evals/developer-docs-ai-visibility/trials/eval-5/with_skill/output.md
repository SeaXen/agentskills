**Do first (30 min, today):** collect 10+ Discord messages with `run_sync()`. For each, note the assistant, the date, and whether it showed sources. Without them the answer key and the pipeline diagnosis are guesses.

**Date check:** today is 2026-10-30, so 18 November is 19 days out (about 2.7 weeks), not 3.5. This plan uses 18 Nov. Confirm the date. If it is really later, the schedule below gets slack and nothing else changes.

## 1. Verdict

- **Where answers go wrong:** assistants likely hand out `Flow.run_sync()`, which v2 removed. The Discord pastes show it. I have no panel data yet, so this is ASSUMED.
- **Likely pipeline:** training recall, or retrieval of a v1 page that shares a title with its v2 twin. One search-on/search-off test per prompt on the 5 worst prompts separates the two.
- **First two levers:** (1) version identity in the title and a server-rendered opener on the v1 tree, a one-template edit you own; (2) clean owned stale copies. Add the symbol map at once, because users arrive with old symbols in their prompts.

## 2. Access (Step 1: all unreviewed, cost ~2 hours)

| Check | What to look for | Cost if wrong |
|---|---|---|
| `robots.txt` and CDN "block AI bots" preset | `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot` blocked | Out of those vendors' search answers (vendor-documented) |
| `Google-Extended` | Disallowed by a preset | Removes docs from grounded Gemini answers (vendor-documented). Search is unaffected. |
| 3 key pages fetched with `curl`, no JavaScript | Body text and code blocks present in the HTML | Code in script-loaded tabs is invisible to many fetchers |
| `nosnippet`, `max-snippet:0`, `data-nosnippet` on code | Any present | Pages or code drop out of AI Overviews and AI Mode |
| Logs | Run `ai-bot-log-summary.py --path-prefix /docs/` if you have 14+ days | Interim evidence only |

Hand any policy decision to `docs-seo`.

## 3. Panel (baseline pending)

- **Size:** minimum viable panel, 10 prompts × 5 runs × 2 assistants, search-on. Add search-off on the 5 worst prompts. That is 125 answers. Assistants are ASSUMED to be ChatGPT and Claude; confirm which ones your users paste from.
- **Cost:** by hand it is about 8 hours, a full writer-day. You own the build, so script it. Use the vendor API with must-contain / must-not-contain checks, and have the writer review only flagged answers. The API can answer differently from the consumer app, so state that caveat in the report.
- **Fallback if no API:** 75 answers on one assistant. That is below the skill's minimum and weaker evidence. Say so in the report.
- **Families:** task, error string, migration, status. Drop the "choice" family, since it measures brand, not version.

| ID | Prompt | Must contain | Must not contain |
|---|---|---|---|
| P01 | run a Tessaline flow from Python | `Flow.run(` | `run_sync(` |
| P02 | is `Flow.run_sync()` deprecated | removed in v2; `Flow.run()` | claims it works |
| P03 | migrate Tessaline v1 to v2 | replacement per symbol | removed symbols |
| P04 | `AttributeError … run_sync` (exact text ASSUMED; run it on v2 to get the real error) | `Flow.run()` | `run_sync(` |
| P05–P10 | top 3 docs tasks and their error strings, from Discord and tickets | fill from Q3 | fill from Q3 |

Everything marked "fill" needs the removed-symbol list. Get it by diffing the v1 and v2 public APIs. `griffe check` is one way (practitioner suggestion). Otherwise take the v2 changelog.

Freeze the prompt wording once the baseline runs. Score each answer on cited / version-correct / deprecated / invented / pipeline. Report pooled family rates with n and Wilson intervals. This panel only detects very large changes.

## 4. Failure tally

Pending the baseline. Likely stale sources to check in the `likely source` column:

- the v1 docs pages
- your own old blog tutorials and example repos
- third-party tutorials and forum answers

## 5. Lever plan

You have about 3 writer-days before 18 Nov. The SDK team has no slot, so anything needing an SDK release is out.

**Track one: ships before 18 Nov**

| Order | Lever | Owner | Effort | When |
|---|---|---|---|---|
| 0 | Baseline panel and API script | you plus writer | ~1 writer-day | Week 1, **before any change ships** |
| 1 | Version identity on the v1 tree: title and server-rendered opener. Drive both from a versions manifest (current, deprecated, EOS date). | you | ~0.5 day | After baseline, week 1–2 |
| 2 | Symbol map: `Flow.run_sync()` → `Flow.run()`, plus the rest from the API diff. Put the two-row version in the opener until the full map exists. | writer | ~1 day | Week 2 |
| 3 | Owned stale copies: version note on the top 3 old blog posts and example repos, archive the rest | writer | ~0.5 day | Week 2–3 |
| 4 | Feedback reports in Google, OpenAI and Perplexity for repeatable wrong answers. Log dates. | writer | ~1 hour | Week 3 |
| 5 | One error page for the `run_sync` `AttributeError` | writer | ~0.5 day | Only if budget remains |

If you get only 2 writer-days, drop item 5 and cap item 3 at the top 3 items.

Opener and title for the v1 tree (shown with the pre-EOS wording; flip it from the manifest on the 18th):
```
<title>Run a flow (Tessaline Python SDK v1, deprecated) | Tessaline Docs</title>
<p><strong>Deprecated: Tessaline SDK v1 reaches end of support on 18 November 2026.</strong>
Kept for teams still on v1. Current page: <a href="/docs/v2/run">Run a flow (v2)</a>.
<code>Flow.run_sync()</code> was removed in v2; use <code>Flow.run()</code>.</p>
```
The banner must be server-rendered and the first text in the main content. Never inject it with JavaScript.

**Control design:** the template change touches every page, so ship it to the v1 tree only. Leave v2 titles untouched until after the re-run and use the v2 tree as control. It also disambiguates the v1/v2 title twins. A v2 label would help retrieval, but it destroys the control, so it waits.

**Track two: standing practice, start now**

- Make the versions manifest the per-release mechanism. A release then costs about 0.5 writer-day (estimate): flip the manifest, add removed-symbol rows from the changelog, re-run the mini panel.
- Make "removed-symbol rows in the migration guide" a docs-side release gate. It needs no SDK slot.
- Start the evidence pack for the SDK team: the panel's deprecated-API rate, plus weekly counts of `run_sync` pastes in Discord. Search the history for a baseline. Use it to ask for a runtime-warning slot next quarter.
- After 18 Nov, route version-matched docs for coding agents to `coding-agent-docs-optimization`. Page and markdown-twin work for agents fits your build.

**Deleted, by interview answer**

- **No SDK release access (Q10):** runtime deprecation warnings and the final-patch README for old packages. Both are out this quarter.
- **30% of workspaces still on v1:** no noindex on v1. Banner and replacement link only.
- **Generic AI-search rewrites:** statistics, quotations, FAQ blocks, answer-length rules. The headline gains are unreplicated on live engines.
- **`llms.txt` as a citation lever:** independent logs show AI search crawlers almost never request it. Keep it for coding agents only.
- **Date bumps to look fresh.**
- **Hiding v1.**
- **Third-party corrections:** do them only for the one or two worst sources the ledger names. Expected value is low.

## 6. Measurement

- **Referrers** on `/docs/`: `chatgpt.com` (including `utm_source=chatgpt.com`), `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai`. This is a lower bound; AI Overviews clicks show as ordinary Google organic.
- **Logs** by bot role and version path. Early warning: user-fetch hits on v1 paths.
- **Support and Discord:** weekly count of `run_sync` pastes. This is the cheapest first-party signal.
- **Re-run the identical panel** 4 weeks after the last change goes live. If that is 18 Nov, the earliest re-run is 16 Dec, and the window runs to 13 Jan. A model release in between voids the comparison. Log the model name and date.
- **Targets (self-set, agree now):**
  - Zero deprecated-API answers on the 3 top docs tasks, search-on.
  - Version-correct rate above baseline, with intervals that separate.
  - Owned-page citation rate above baseline.
- **Report on 18 Nov:** shipped page changes, checked by plain-HTTP fetch of the 3 key pages. Citation and ranking outcomes stay **pending**.

## 7. What no docs change fixes quickly

- Released model weights. Training-recall answers shrink only when a later model trains on a corpus where v2 dominates. Expect `run_sync` pastes in Discord to continue after 18 Nov.
- Runtime warnings are the only lever that reaches code already written from recall. They need the SDK team.
- Vendor re-indexing runs on the vendor's schedule. The lag is an estimate: days to weeks for retrieval, the next model release for recall.

## Open questions (marked ASSUMED above)

1. Is the EOS date 18 Nov or later?
2. Which assistants do your users paste from?
3. What are the exact removed symbols, and the real v2 error text for `run_sync`?
4. Can you script the vendor APIs?
5. Is the CDN or `robots.txt` policy yours to change?

**Next:** send me the Discord pastes and the removed-symbol list. I'll turn them into the full answer key and the ledger template.