# Pipeline diagnosis and bot roles

## Contents

- [The three pipelines](#the-three-pipelines)
- [Tests that separate them](#tests-that-separate-them)
- [Bot roles by vendor](#bot-roles-by-vendor)
- [What vendors say about citation choice](#what-vendors-say-about-citation-choice)

## The three pipelines

| Pipeline | What it reads | What the docs owner controls |
|---|---|---|
| Training recall | the text corpus at the model's training cutoff: docs of that era, tutorials, forum answers, public repos | nothing for the released model; the future corpus mix, and runtime signals that catch the old code |
| Search-grounded retrieval | the assistant vendor's search index at answer time | indexability, which version wins among duplicates, what the page says |
| User-triggered fetch | one page fetched live because a user or agent asked for it | access, page content, the markdown twin |

Retrieval answers carry citations; recall answers do not. Deprecated APIs surface most in recall answers. This split is practitioner inference, consistent with how every vendor documents its bots.

## Tests that separate them

Run these on each failing panel prompt:

1. **Search toggle.** Ask the same prompt with web search off and on, where the assistant offers the switch. Same wrong answer with search off = recall. Right answer only with search on = retrieval works and recall is stale. Where search is "auto", count a run as retrieval only when it shows sources or a search step.
2. **Source request.** Ask "which page is this from?" An invented or missing URL points to recall.
3. **Version probe.** Ask "which version of <product> does this code target?" A confident old version number confirms recall of an old corpus.
4. **Log check.** Look for a fetch from a user-triggered agent on the cited path within minutes of the run. A hit proves a live fetch, not whether search or the user triggered it. No hit and a citation = likely answered from the index copy. Many coding agents and IDE assistants send generic user agents, so for them a missing hit proves little.
5. **Index check.** Search the engine behind the assistant for the cited old-version URL. Still indexed = a retrieval problem with a docs-seo fix.

## Bot roles by vendor

Vendor-documented. These pages change several times a year: re-read each vendor's crawler page before acting, and treat this table as a starting map, not the source of truth.

| Vendor | Search index | User-triggered fetch | Training | robots.txt stance, vendor wording |
|---|---|---|---|---|
| OpenAI | `OAI-SearchBot` | `ChatGPT-User` | `GPTBot` | for `ChatGPT-User`, "robots.txt rules may not apply"; sites opted out of `OAI-SearchBot` "will not be shown in ChatGPT search answers, though can still appear as navigational links" |
| Anthropic | `Claude-SearchBot` | `Claude-User` | `ClaudeBot` | all three honor robots.txt; blocking the fetch or search agent "may reduce your site's visibility". `Claude-Web` and `anthropic-ai` are historic tokens the vendor no longer lists |
| Perplexity | `PerplexityBot` | `Perplexity-User` | neither used for foundation-model training | `Perplexity-User` "generally ignores robots.txt rules" |
| Google | `Googlebot` feeds Search, AI Overviews and AI Mode | `Google-Agent` and other user-triggered fetchers (the NotebookLM token has been renamed; check the list) | no separate crawler: the `Google-Extended` token gates Gemini training and "grounding… in Gemini Apps and Grounding with Google Search on Vertex AI"; it "does not impact a site's inclusion in Google Search" | user-triggered fetchers "generally ignore robots.txt rules" |
| Microsoft | `bingbot`; Copilot grounds on the Bing index, implied by its webmaster reporting of "grounding queries" | not documented per agent | not documented per agent | not documented per agent |

OpenAI also lists `OAI-AdsBot`, which checks ad landing pages and plays no part in answers. Perplexity runs no training agent.

Verify any bot claim against the vendor's published IP-range file: OpenAI, Perplexity and Google publish one JSON list per agent, Anthropic one file for all its agents. A user-agent string alone is trivially spoofed.

Because user-triggered fetchers may ignore robots.txt, a block meant to stop them belongs at the CDN or WAF, and so does any rate limit.

## What vendors say about citation choice

- No vendor publishes how a specific citation is chosen.
- Google: AI Overviews and AI Mode rest on core Search ranking; a page must be indexed and snippet-eligible; "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary"; "You don't need to create new machine readable files, AI text files, or markup". The two features "may use different models and techniques", and both may issue several related searches per question ("query fan-out").
- OpenAI ties ChatGPT search eligibility to `OAI-SearchBot` access. Anthropic and Perplexity tie visibility to their search agents.

Everything beyond eligibility - why page A beats page B - is practitioner reverse-engineering. Label it so in any report.
