# Is this methodology sound? No. Redesign it before reporting any number.

Your draft measures brand mentions and rank. As head of docs you need whether assistants cite your docs and give correct code. This skill covers the second question, not the first. I checked your draft against its panel protocol and evidence base. Where I mark something `ASSUMED`, I lack your data.

## 1. Verdict

- **A single run per keyword can't support a monthly number.** Repeated runs of one prompt returned the same list of recommended brands in under 1 of 100 runs, and in the same order in under 1 of 1,000. That was independently measured: 2,961 runs, with a vendor co-author. Your "average rank" would mostly be noise.
- **Rank position is the wrong metric.** Report appearance rate over many runs, with n and an interval. Never report a position.
- **SEO keywords aren't what developers ask assistants.** "Vector database" is a head term. The panel should use task prompts, error strings, migration and status questions, drawn from support tickets, docs search logs and community questions.
- **Mentions can't see the failure that matters.** A cited answer with a removed API counts as a win in share of voice. Score version correctness against a written answer key.
- **"First Monday, work laptop" adds uncontrolled variables.** A logged-in work profile carries memory, custom instructions and connected tools. The protocol requires a logged-out or fresh profile and a recorded location and plan tier. It also requires the model name and date on every row. One day a month can't tell a model release from your change.
- **Search mode is unrecorded.** Whether web search was on changes the pipeline: training recall or search-grounded retrieval. Without that, you can't tell which fix could move a result.

## 2. A floor effect and a noise problem

"Vector database" and "best vector db for RAG" are crowded head terms. A younger engine will probably appear rarely, so a rate near zero shows little movement.

Your draft yields about 150 answers (50 keywords × 3 assistants). If Brindlecoast appeared in 5 of 50 answers on one assistant, that's 10%, and the Wilson 95% interval runs from about 4% to 21% (my calculation). Runs of related keywords are correlated, so the real interval is wider. A month-over-month swing inside that range means nothing. Don't put a monthly trend line in front of an exec on this data.

## 3. Replacement design

The sizes below are this skill's defaults.

**Panel**
- Use 10 core prompts, built from your top docs tasks, error strings your clients emit, and a migration or status question if you have versions with removed symbols.
- Write one row per language client where the code differs: Python, Go and TypeScript. A Python answer key can't score a Go answer.
- Keep one or two choice prompts, such as "best vector db for RAG". Report them as an appearance rate in a separate column, never as a rank.
- Fix the wording once the baseline runs. A reworded prompt is a new prompt.

**Answer key.** Write one line per prompt before any run:

```
prompt_id | must contain | must not contain | owning docs URL (current)
P01 | <current client call, install name> | <removed symbol, old package name> | /docs/<current page>
```

Fill the symbols from your own release history. I don't know them, so they are `ASSUMED` until you list them. A prompt without a key doesn't run.

**Runs**
- Run each prompt 5 times per assistant and mode.
- Assistants: the two that matter most for your users, from ChatGPT, Claude and Perplexity. `ASSUMED`: ChatGPT and Perplexity. Confirm against your referrer data.
- Modes: search-on for all prompts. Add search-off for the 5 worst prompts on one assistant.
- That is 10 × 5 × 2 = 100, plus 5 × 5 = 25, so **125 answers**. This is the minimum viable baseline.
- Use a fresh logged-out profile, no memory, no custom instructions, no connected tools.
- Record model, date, location and plan tier on every row.
- Run by hand or through the vendors' APIs. Scripting a consumer chat app can breach its terms.

**Scoring.** Score each answer on five fields:

| Field | Values |
|---|---|
| Cited | none / owned docs current / owned docs old version / owned other / third party (domain) |
| Version-correct | yes / partial / no |
| Deprecated API present | yes / no |
| Invented API present | yes / no |
| Pipeline | recall / retrieval / fetch |

**Ledger row:** `date | assistant | model | mode | prompt_id | run | cited | version_correct | deprecated | invented | pipeline | likely source | owner`

The `likely source` column becomes your correction list.

## 4. Fit to your capacity

Two writers at about half a day a week is roughly 16 to 17 hours a month. By hand, 125 answers at 3 to 5 minutes each is about 6 to 10 hours. That is half your monthly budget or more, and leaves little for fixing anything.

- **Script it.** Run the API, check must-contain and must-not-contain automatically, and review only the flagged answers.
- **Panel runs aren't monthly.** A full run every month adds little, because retrieval fixes take 4 to 8 weeks to show and training-recall fixes wait for the next model release (this skill's defaults). Run the full panel as a baseline and again 4 to 8 weeks after your last change goes live.
- **Monthly report.** Cover the first-party data in section 5, plus the latest panel result labelled with its date.
- **Resolution.** 125 answers detect only very large changes. Grow the panel by adding prompts in families before adding runs. Pooled family rates tighten faster than per-prompt rates.

## 5. What to report

**From the panel**, per assistant and mode, with n and a Wilson interval:
- Version-correct rate.
- Deprecated-API rate and invented-API rate.
- Owned-current citation rate.
- Third-party citation share, by domain.

Pool by prompt family. Call a change real only when the baseline and re-run intervals don't overlap.

**First-party data**, with at least 14 days before quoting a share:
- AI referrers on the docs path: `chatgpt.com` (it also appends `utm_source=chatgpt.com`), `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`. This is a lower bound, since apps strip referrers and developers copy code without clicking.
- Server or CDN logs by bot role and docs version path. The skill ships `scripts/ai-bot-log-summary.py`:
  `python3 scripts/ai-bot-log-summary.py --path-prefix /docs/ access.log`
- Support tickets and issues tagged "code from an assistant". They are the cheapest signal of training-recall failures in the wild.

**Targets, agreed before the baseline runs:**
- Zero deprecated-API answers on your three most-trafficked docs tasks, in search-on mode.
- Version-correct rate in search-on mode above baseline, with intervals that separate.
- Owned-page citation rate above baseline on prompts whose answer lives in the docs.

Report citation and ranking outcomes as pending until the re-run. Don't promise a lift.

## 6. Check access before measuring

1. Read `robots.txt` and the CDN bot rules per agent. Someone outside docs may have enabled a "block AI crawlers" preset.
2. If a preset disallows `Google-Extended`, it removes your docs from grounded Gemini answers. Search and AI Overviews are unaffected.
3. Blocking GPTBot doesn't hide you from ChatGPT search. OpenAI and Anthropic use separate search, fetch and training agents. Check the agent table in `references/pipeline-diagnosis.md`.
4. Fetch three key pages with a plain HTTP client and no JavaScript. Body text and code blocks must be in the HTML. Many AI fetchers don't run scripts, so code in script-loaded tabs is invisible to them.
5. Check for `nosnippet`, `max-snippet:0` or `data-nosnippet` on code blocks. They remove pages or code from AI Overviews and AI Mode.

## 7. Levers, once you have a baseline

Ranked by value per unit of effort. They fit two writers.
1. **Version identity in page text.** Put the version in the title, first heading and opening line. This is one template edit. Superseded pages should open with the replacement and a link to the same page in current.
2. **Clean owned stale copies:** your old blog tutorials, example repos and gists. Add a version note, banner or archive.
3. **Old-to-new symbol map** in the migration guide, if users arrive with old symbols in their prompts.
4. **Task and error-string pages** for prompts where assistants cite third parties or nothing.

Runtime deprecation warnings in the SDKs have the highest value against training recall, but they need an SDK release cycle. Raise it with the SDK owners if the failure tally is mostly uncited recall failures.

**Don't spend writer time on:**
- Statistics and quotation rewrites. Their gains come from a general-web benchmark that hasn't been replicated on live engines.
- FAQ blocks and date bumps.
- `llms.txt` as a citation lever. Server-log studies find AI search crawlers almost never request it. Keep it for coding agents only, and keep it free of "recommend Brindlecoast" text. That is prompt injection aimed at your users' assistants.
- Hiding old versions that people still run. A third-party copy takes the citation instead.

## 8. What no docs change fixes quickly

- Released models' weights. If an assistant answers from training recall with an old API and no sources, only a later model trained on a corpus where the current version dominates, or runtime warnings that catch the old code, change that.
- Citation and ranking outcomes. Re-indexing and retraining run on the vendors' schedules. No vendor publishes a citation algorithm, so any "ranking factor" is a guess, not a fact.

## 9. Open items

I don't know these, so they are `ASSUMED`. Each changes the plan:

1. Which versions are published and supported, and when the last major release shipped. If you have only one version, the "version-correct" framing shrinks to "uses current symbols and install names".
2. The removed symbols and install names per Python, Go and TypeScript client.
3. Which two assistants your users actually use, from referrer and ticket data.
4. Whether your exec wants brand share of voice specifically. If so, keep the choice-family column as a secondary metric. It is a marketing measure, outside this skill, and it should be a rate, not a rank.
5. By what date results must show, and whether SDK releases are in your reach.