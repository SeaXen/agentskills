# Ferrowave docs: AI-answer visibility plan review

**Short answer: no, the plan doesn't cover it.** Item 2 should be dropped because it would hurt your v3 customers. Items 1 and 3 won't fix the answer you saw, and the plan has nothing for the likely cause.

## 1. Verdict

- **Where answers go wrong:** ChatGPT gave removed v4 API (`ferrowave.connect(url, { group })`) with no sources and no version stated. I haven't run the panel, so the pipeline below is inferred from one answer, not measured.
- **Most likely pipeline:** training recall. No sources were shown, and the answer was confident and old. Recall reads the corpus at the model's cutoff, and canonicals, noindex and `llms.txt` don't touch it (practitioner inference, consistent with how vendors document their bots).
- **Two first levers:** version identity in page text, and cleaning your own stale copies (old blog tutorials, example repos, gists). Add the old-to-new symbol map right away, because users arrive with `connect()` in their prompts.

One more thing to check: `connect(url, { group })` was valid in v3, and v3 is still live and supported. The answer may be a correct v3 answer that never named its version. Your answer key must separate "wrong for v4" from "invented".

## 2. Your three items

| Item | Verdict | Why |
|---|---|---|
| (1) Canonical v3 → v4 on every page | ⚠️ Keep only where the pages are true equivalents | Canonicals are a search-index hint, owned by `docs-seo`. They don't reach recall answers. A v3 page whose code differs from v4 is not a duplicate, so a canonical there is a wrong signal. |
| (2) Noindex the whole v3 tree | ❌ Delete | A quarter of paying customers still run v3. Hiding the tree removes their pages from search, and a third-party copy then takes the citation. It also sends mixed signals with item 1: canonical says "consolidate to v4", noindex says "drop". |
| (3) Publish `llms.txt` listing v4 pages | ⚠️ Optional, coding agents only | Server-log studies find AI search crawlers almost never request it (independently measured). It won't earn ChatGPT citations. Keep it as a small surface for coding agents. It may state version facts and nothing else. |

Replace item 2 with: a server-rendered banner on every v3 page, the replacement link, and no noindex. This follows the skill's rule that old versions with real users keep their pages.

## 3. Access checks (do before any fix, about 1 hour)

| Check | What to look for | Cost if wrong |
|---|---|---|
| `robots.txt` and CDN "block AI crawlers" toggle | Rules per agent: `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `Claude-User`, `PerplexityBot`, `Googlebot` | Blocking a search or fetch agent drops you from that vendor's answers. Blocking only the training agent (`GPTBot`, `ClaudeBot`) leaves search untouched. |
| `Google-Extended` | Disallowed by a CDN preset? | Removes the docs from grounded Gemini answers. Search and AI Overviews are unaffected. |
| Rendering | Fetch three key pages with plain HTTP, no JavaScript. Are body text and code blocks in the HTML? | Many AI fetchers run no scripts. Code in script-loaded language tabs (Node/Python) is invisible to them. |
| Snippet controls | `nosnippet`, `max-snippet:0` or `data-nosnippet` on code blocks | Removes pages or code from AI Overviews and AI Mode. |

I haven't seen your rules or logs, so I treat them as **unreviewed**.

## 4. Panel and answer key

Nothing is measured yet. One answer proves nothing, because repeated runs of one prompt rarely return the same result (independently measured).

**Minimum viable baseline** is 125 answers, about a day of hand work. It is 10 core prompts × 5 runs × 2 assistants, search-on, plus search-off on the 5 worst prompts. Which assistants? I'll ask below.

- One row per client, Node and Python, because a Python key can't score a Node answer.
- Include migration ("v3 to v4 consumer group"), status ("is `ferrowave.connect` deprecated") and error-string prompts.
- Decide targets and control design **before** the run.

Example key, to confirm with you (symbols below are placeholders):

```
prompt_id | must contain          | must not contain          | owning URL
N01       | <v4 consumer-group API>| ferrowave.connect(        | /v4/...
N01-v3    | scored separately: a v3 answer that says "v3" is correct for v3 users
```

Score each answer on: cited, version-correct, deprecated API, invented API, pipeline. Report rates with n and a Wilson interval, pooled by family.

## 5. Lever plan

**Track 1: ships this sprint**

1. **Version identity in page text.** One template edit. Put the version in the title, first heading and opening line: `Consumer groups (Ferrowave Node v4)` and `Consumer groups (Ferrowave Node v3)`. Version twins sharing a title look identical to retrieval.
2. **v3 opener, server-rendered, above any code.** Not a JavaScript banner. Example: "Applies to Node client v3. Current: v4 (link to the same page). `ferrowave.connect()` was removed in v4; use `<v4 replacement>`."
3. **Clean your own stale copies.** Old blog tutorials, example repos, gists and registry READMEs. Add a dated version note, or archive the repo with the current one named first.
4. **Symbol map**, in the migration guide and in the v3 opener until it exists. Use the exact old spelling in code formatting, one row per symbol. This catches prompts containing `connect(`.
5. **Your canonicals (item 1)**, narrowed to true duplicates and coordinated with `docs-seo`.
6. **Feedback reports** in each assistant's UI. Cheap, unverified and with no published turnaround, so log the date.

**Track 2: start now on the client release cycle (needs SDK access)**

- **Runtime deprecation warning** in the last v3 release and a clear error in v4. Name the replacement and the docs URL, once per process. It is the only lever that reaches an answer already written from recall, because the developer or agent reads it on running the code.
- **Agent-delivered docs**, owned by `coding-agent-docs-optimization`. Promote this if the tally shows mostly uncited recall failures inside coding agents.
- If you have no SDK release access, delete both and say so.

**Deleted:** noindex on v3, `llms.txt` as a citation lever, FAQ/statistics rewrites, date bumps to fake freshness.

## 6. Measurement plan

- **First-party data, 14+ days minimum:** AI referrers on docs paths (`chatgpt.com` plus `utm_source=chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`). This is a lower bound, since many users copy code without clicking.
- **Logs by bot role and version path:** `python3 scripts/ai-bot-log-summary.py --path-prefix /v3/ access.log`, with vendor IP-range files for verification. User-fetch hits on v3 paths are the early warning.
- **Support tickets** tagged "code from an assistant". This is the cheapest recall signal.
- **Control design:** the template edit touches every page, so roll it out to one section first (e.g. Node v3 consumer-group pages) and use the rest as control. Otherwise compare to a logged baseline, voided if a model release lands between runs.
- **Re-run date:** 4–8 weeks after the last change goes live for retrieval levers. Training-recall levers wait for the next model release.
- **Self-set targets (agree before the baseline):** zero deprecated-API answers on your top 3 docs tasks in search-on mode; version-correct rate above baseline with intervals that separate; owned-page citation rate above baseline.

## 7. What no docs change fixes quickly

- **The released model's weights.** If the answer was recall, no page edit changes what that model says. Recall failures shrink only when a later model trains on a corpus where v4 dominates, and when runtime warnings catch the old code.
- **Citation and ranking outcomes are pending.** Page changes are verifiable today, but re-indexing and retraining run on the vendors' schedule. Promise no lift figure.
- **A quarter of customers on v3 will keep getting v3 answers.** That is partly correct, so the fix is version labelling, not suppression.

## Questions I need answered

1. Paste 2–3 wrong answers, with assistant, date and whether sources showed. Did search-off give the same `connect()` answer?
2. For Node and Python: removed symbols, replacements, install names, and the error text a v4 user sees on calling `connect()`.
3. Which 2–3 assistants matter: chat with search, IDE coding agents, search-engine AI features?
4. Can you change the SDK release (warnings), the docs template, and your CDN bot rules? What's the weekly docs-writer budget?
5. Any hard date (v3 end-of-support, a launch)? A date inside a month can show shipped changes, never citation outcomes.
6. Do you know third-party pages with `connect()` code that rank or get pasted: forum answers, tutorials, example repos?
7. Do you have 14+ days of CDN logs, and a webmaster console on the docs?