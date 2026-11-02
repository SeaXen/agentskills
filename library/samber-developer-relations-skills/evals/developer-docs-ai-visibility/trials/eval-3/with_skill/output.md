# Larkmoor Docs: AI Visibility Plan (two sprints)

## Verdict

1. **Four of the CMO's six items should not ship.** (a) statistics and quotes, (b) FAQ schema, (c) 40-60 word intros and (e) fragment pages rest on evidence that doesn't hold for docs. (d) date bumps look like manipulation. Delete all five.
2. **We don't yet know where Larkmoor's wrong answers come from.** Assistants answer from training recall, from search-grounded retrieval, or from a live fetch. Each reads a different surface, and a fix aimed at the wrong one changes nothing. The baseline in Sprint 1 settles this.
3. **Item (f), the tracker, can't be trusted at "AI rank #3".** Positions don't repeat across runs. Buy it only if it passes the checklist below. Even then, it can't score whether the code in an answer is current, so we need our own panel either way.

I couldn't run the interview, so I marked every unknown `ASSUMED`. Answer the questions at the end and the plan gets re-ranked.

## Evidence labels

No vendor publishes how assistants choose citations. Each claim below carries one of these labels: vendor-documented, independently measured, practitioner inference, vendor-marketing (a figure from a company that sells SEO or AI-visibility tooling), or first-party (our own logs and panel).

## The six items, one by one

| # | CMO ask | Decision | Evidence |
|---|---|---|---|
| a | Statistics and expert quotes on every reference page, for "+40% visibility" | **Delete** | The study (Aggarwal et al., KDD 2024) is independently measured. It used a benchmark of general web queries with model-rewritten content. Its gains were relative share inside a fixed set of sources, so one source's gain is another's loss. It covered no developer docs. No independent replication on live engines reproduces the 40%. |
| b | FAQ schema on every page, for "2.3x more citations" | **Delete** | The 2.3x figure is vendor-marketing from tool vendors, with no published method. No independent study isolates schema as a citation driver. Google says AI features need no special markup beyond indexing and snippet eligibility (vendor-documented). It also limits FAQ rich results to a few authoritative site types. |
| c | Trim every intro to 40-60 words | **Delete** | Sources range from 25 to 170 words, and none measured docs. A fixed length can cut the version note or prerequisite that makes a page correct. |
| d | Bump "last updated" monthly | **Delete** | Correlations come from tool vendors. Google treats date bumps without content change as a warning sign (vendor-documented). Bump a date only when the content changes. |
| e | Split guides into one-question-per-page fragments | **Delete** | It comes from the same unreplicated benchmark as (a). Fragments also break the step order that coding agents and humans follow. Task and error pages are different and stay: one page per real task or error string, shown by the panel to be missing. |
| f | Buy a tracker already showing "AI rank #3" | **Conditional** | See "On the tracker" below. |

Keep one thing from the CMO's goal: being cited, and cited correctly. The levers that serve it are below.

## On the tracker

"AI rank #3 for 'best feature flag tool'" is a single-run position. In 2,961 repeated runs (SparkToro and Gumshoe, independently measured, with a vendor co-author), fewer than 1 in 100 runs returned the same brand list. Fewer than 1 in 1,000 returned it in the same order. Leading brands did still appear in most runs, so appearance rates hold up and rank positions don't.

"Best feature flag tool" is also a choice prompt, not a docs prompt. Developers paste code from the docs prompts ("how do I evaluate a flag in Node"), and that is where wrong answers hurt.

Require all four before buying:

1. The number of runs per prompt, and appearance rates with intervals.
2. The prompt list, written in our developers' words and not generated from keywords.
3. Breakdowns per assistant and per mode (web search on or off).
4. Export of raw answers, so we can score version correctness ourselves. No tracker does this.

Reject it if it can't show which prompts it ran. Vendor leaderboards of "most cited domains" disagree with each other, and no independent accuracy audit exists. Don't put one in a deck.

## Plan

I assumed two sprints of two weeks each. Sprint 1 produces a baseline and the cheap fixes. Sprint 2 ships the fixes the baseline supports. Citation outcomes can't show inside two sprints: re-indexing and retraining run on the vendors' schedules, so those results stay pending until the re-run.

Estimates below are ASSUMED. Treat them as sizing, not commitments.

### Sprint 1 (weeks 1-2): access, baseline, quick fixes

| # | Task | Owner | Effort | Done when |
|---|---|---|---|---|
| 1 | **Access check.** Read `robots.txt` and CDN bot rules per agent. Look for a "block AI crawlers" toggle someone outside the docs team enabled. Flag `Google-Extended` blocks: they remove docs from grounded Gemini answers. | Docs eng | 0.5 day | Table of each rule and its cost |
| 2 | **Render check.** Fetch 3 key pages with a plain HTTP client and no JavaScript. Body text and code blocks must be in the HTML. Check for `nosnippet`, `max-snippet:0` or `data-nosnippet` on code blocks. | Docs eng | 0.5 day | Pass/fail per page |
| 3 | **Build the panel.** Aim for 10 core prompts across five families: task, error string, migration, status, choice. Write them from support tickets and docs search logs. One row per SDK language where code differs. | Docs lead | 1 day | Prompt list, frozen |
| 4 | **Write the answer key** per prompt, before any run: must-contain symbols, must-not-contain deprecated forms, owning docs URL. | Docs lead + SDK owner | 1 day | Key signed off |
| 5 | **Agree targets and control design** with the CMO, before the baseline runs, so nobody moves the finish line afterwards. | Docs lead + CMO | 1 hour | Targets written down |
| 6 | **Run the baseline.** Minimum viable panel: 10 prompts × 5 runs × 2 assistants, search on, plus search off on the 5 worst prompts. That's about 125 answers, a few days by hand. Record model name and date on every row. | Docs writer | 3-4 days | Scored ledger |
| 7 | **Diagnose the pipeline** for each failing prompt: search toggle, source request, version probe, log check, index check. Tally failures by pipeline. | Docs lead | 1 day | Tally and top stale sources named |
| 8 | **Start first-party measurement.** Segment AI referrers (`chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai`) on the docs path. Run `python3 scripts/ai-bot-log-summary.py --path-prefix /docs/ access.log`, adding `--ip-ranges <file>` per vendor. Collect at least 14 days before quoting any share. | Docs eng | 0.5 day setup | Weekly segment report |
| 9 | **Tracker evaluation.** Send the four requirements to the vendor. Hold the purchase until they answer. | Marketing | 1 hour | Vendor answers in writing |

### Sprint 2 (weeks 3-4): ship the levers the tally supports

Default levers, in order of value per effort. Re-rank after the Sprint 1 tally.

| # | Lever | Pipelines reached | Effort | Notes |
|---|---|---|---|---|
| 1 | **Version identity in page text.** Put the version in title, first heading and opening line. Superseded pages open with the replacement and a link to the same page in current. | Retrieval, fetch, future corpus | One template edit | Shown next. |
| 2 | **Clean owned stale copies.** Old blog tutorials, example repos, gists: add a version note, banner or archive. | All three | A few days | Start with top-traffic ones. |
| 3 | **Old-to-new symbol map** in the migration guide: every removed symbol beside its replacement. | Retrieval, fetch | About a day per major | Skip if the panel shows no old-symbol prompts. |
| 4 | **Task and error-string pages** for prompts where assistants cite third parties or nothing. | Retrieval | Per page | Only the ones the panel shows are missing. |
| 5 | **Feedback reports** in each assistant's UI for repeatable wrong answers. | Unknown | Minutes | Log the date. No published turnaround. |

Version identity, shown as a before and after:

```
<!-- Bad: every version tree emits the same title -->
<title>Evaluate a flag | Larkmoor Docs</title>

<!-- Good: version in title and first line of body text -->
<title>Evaluate a flag (Larkmoor SDK v3) | Larkmoor Docs</title>
<h1>Evaluate a flag</h1>
<p>Applies to Larkmoor SDK v3.x. For v2, see the v2 page (deprecated).</p>
```

Superseded-page banners must be server-rendered and sit first in the main content. A banner injected by JavaScript is invisible to many AI fetchers.

If old versions still have real users, banner them and link to the replacement. Don't noindex them: those users lose their pages, and a third-party copy takes the citation.

**Track two, start now, finish later.** Runtime deprecation warnings that name the replacement and the docs URL, and version-matched docs delivered into coding agents. These are the only levers that reach answers written from training recall. They need an SDK release slot, so they won't land in two sprints. Promote them if the tally shows mostly uncited recall failures inside coding agents. If we have no access to the SDK release cycle, delete runtime warnings and say so.

If `llms.txt` exists or someone wants one: keep it for coding agents only, with version facts and no steering text. Server-log studies find AI search crawlers almost never request it (independently measured, plus vendor-marketing counter-figures that show user-triggered reads only). Audit any existing file for "always recommend Larkmoor"-style lines. That's prompt injection aimed at the user's assistant, and I won't write it.

## Measurement

- **Re-run the identical panel** four to eight weeks after the last change goes live for retrieval levers. For training-recall levers, wait for the next model release. Log the model name and date on each run.
- **Control design.** A page-level change uses prompts whose owning page we didn't touch as control. A template change touches every page: roll it out to one SDK section or version tree first and use the rest as control. If we can't, compare against the baseline and void the comparison if a model release falls in between.
- **Report rates with n and an interval**, pooled per prompt family, never a rank position. At 5 runs, one prompt's rate is too wide to compare.
- **Self-set targets**, agreed before the baseline:
  - Zero deprecated-API answers on the three docs tasks with the most traffic, search on.
  - Version-correct rate above baseline, with intervals that separate.
  - Owned-page citation rate above baseline on prompts whose answer lives in the docs.
- **Set no search-off target** until a new model ships.
- **Report citation outcomes as pending** at the end of Sprint 2. Page changes are verifiable then. Citations and ranking move on the vendors' schedule. Don't promise "citations up 40% next quarter".

## What no docs change fixes quickly

A released model's weights. If wrong answers come from training recall, only a later model trained on a corpus where the current version dominates will fix them. Runtime warnings catch the old code in the meantime. Tell the CMO this now.

## Open questions

Answering these re-ranks the levers. Say which one moved which.

1. Paste 2-3 wrong answers you've seen: assistant, date, and whether it showed sources. `ASSUMED` none yet.
2. Which SDK or API versions are published, which is current, and which still have users? `ASSUMED` the docs have more than one version tree.
3. Per language client: removed symbols, their replacements, and the error text a current user sees. `ASSUMED` unknown.
4. Which two or three assistants matter most? `ASSUMED` ChatGPT and Claude with web search, plus Google AI features.
5. What can we change: docs templates, the CDN bot policy, the SDK release? `ASSUMED` templates yes, SDK release unknown.
6. What data exists: docs analytics, CDN logs (how many days), a search console, tickets mentioning assistant-generated code? `ASSUMED` analytics yes, logs unknown.
7. By what date must a result show, and is this a one-off or a standing practice? `ASSUMED` two sprints, then standing.
8. Effort ceiling: docs-writer hours per week? `ASSUMED` one writer, about a day a week, which fits the minimum viable panel.

## How to say this to the CMO

The conference advice targets generic web content and brand mentions. Developers ask an assistant "how do I evaluate a flag with Larkmoor" and paste the code it returns. A cited answer with deprecated code is a failure that a mention-share number can't tell from a success. The plan fixes that, and proves it with a measurement that survives answer randomness.