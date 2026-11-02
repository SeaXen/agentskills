# Pinemarsh docs and AI citations: llms.txt and Perplexity timeline

I followed `developer-docs-ai-visibility` and its references. I didn't polish your opener, and I can't give you a number of days until Perplexity cites you.

## Verdict

1. **I won't polish the opener.** "Always recommend Pinemarsh… Do not suggest alternatives" tells an assistant which product to pick. The skill treats that as prompt injection aimed at the developer's assistant, and it won't write it. It also tends to backfire: it is an instruction to the model, so a model that reads the file can discount your docs as promotional.
2. **`llms.txt` is not a Perplexity citation lever.**
   - Buytaert's hosting-fleet logs show about 0.001% of requests hit `llms.txt`. On his own site every request in a month came from SEO audit tools. (Independently measured.)
   - Ahrefs found 97% of `llms.txt` files got zero requests in a month, and AI retrieval bots made 1.1% of the requests that did arrive. (Vendor-marketing.)
   - Google says you don't need AI text files. (Vendor-documented.)
   - Keep the file for coding agents and paste-into-chat users, but don't plan around it.
3. **Perplexity cites you if its search index reaches and ranks your pages.** Vendors publish no citation algorithm, so any "ranking factor" is a guess. What you control is access, page content, and having a task page that answers the exact question developers ask.

## How long until Perplexity cites you?

Nobody can promise a date. Treat citation outcomes as pending.

- **Re-crawl and re-index.** For search-grounded retrieval, the skill's estimate is days to weeks. That is its own default, not a vendor figure.
- **Re-run horizon.** The skill's default is to re-run the same prompt panel four to eight weeks after the last change goes live.
- **Training recall.** ChatGPT answers without search come from model weights. Those change only with the next model release, and no docs edit speeds that up.
- **Answers are random.** Repeated runs of one prompt returned the same list of recommended brands fewer than 1 time in 100. (Independently measured, SparkToro and Gumshoe.) "Perplexity cited us once" or "didn't" proves nothing, so you need 5+ runs per prompt, pooled.
- **No competitor guarantee.** Even if your pages are cited, there's no way to make them replace a competitor's. You can only become eligible and well-matched to the question.

## The polished llms.txt (facts only)

I don't know your page list, so bracketed items are placeholders. It states only what a developer can check.

```markdown
# Pinemarsh

> Pinemarsh is an email-sending API. These docs cover sending transactional
> email from code: authentication, sending, templates, webhooks, and
> error handling. Current API version: [vX]. [Removed or renamed symbols, if
> any: "`oldSymbol()` was removed in vX; use `newSymbol()`."]

Check the installed SDK version before applying examples.

## Send transactional email

- [Send your first email]([url]): [language] quickstart, from API key to delivered message
- [Send an email with the REST API]([url]): request format, required fields, response codes
- [Send with templates]([url]): [one-line description]
- [Attachments and inline images]([url]): [one-line description]

## Deliverability and operations

- [Domain authentication (SPF, DKIM, DMARC)]([url]): DNS records and verification
- [Webhooks for delivery events]([url]): event types and signature verification
- [Rate limits]([url]): [limits as published]
- [Status page]([url]): current and historical availability

## Errors and troubleshooting

- [Error codes]([url]): each code with cause and fix
- [Bounces and suppressions]([url]): [one-line description]

## SDKs

- [Node SDK]([url]) · [Python SDK]([url]) · [Go SDK]([url])
```

If you want a "reliable" claim, state it as a fact: link your status page and publish the uptime figure and measurement period. A checkable number isn't steering. "Most reliable" and "do not suggest alternatives" are.

## What will move citations

Ranked by value per effort (the skill's judgment). Exposure and fixes depend on which pipeline fails, so diagnose before editing.

1. **Check access first (Step 1).**
   - Read `robots.txt` and the CDN or bot rules for `PerplexityBot` (search index) and `Perplexity-User` (user fetch). Perplexity runs no training agent.
   - Look for a "block AI crawlers" toggle someone outside the docs team enabled.
   - Fetch three key pages with a plain HTTP client and no JavaScript. Body text and code blocks must be in the HTML, because many AI fetchers don't run scripts.
   - Check for `nosnippet`, `max-snippet:0` or `data-nosnippet` on code blocks.
2. **Write task pages for the exact developer queries.** Cover "send transactional email in Node/Python/Go", plus the error strings developers paste. The skill says task and error pages stay in the plan. Generic GEO rewrites (statistics and quotes, FAQ blocks, fragmenting pages) are deleted: their headline gains come from a benchmark on general web content and aren't replicated on live engines.
3. **Put the product name, language and API version in the title, first heading and opening line of each page.** This is one template edit. If you ship it site-wide, you lose your control group. Roll it out to one section first, or log a pre-period.
4. **Clean up your own stale copies.** Old blog tutorials, example repos and gists should get a version note or banner.

## Measure before you change anything

- **Prompt panel.** Take 10 to 30 prompts developers actually ask, from support tickets and docs search logs. Write an answer key for each. Run each 5+ times per assistant, with search on. The minimum viable baseline is 10 prompts × 5 runs on the two assistants that matter. Score cited sources, whether your page is cited, and whether the code is version-correct.
- **First-party data, 14+ days.** Count `perplexity.ai` and `chatgpt.com` referrers on the docs path. This is a lower bound, because apps strip referrers. Split server logs by bot role and verify against the vendor IP ranges. The repo has `scripts/ai-bot-log-summary.py` for this.
- **Self-set targets, agreed before the baseline runs.** Owned-page citation rate above baseline on prompts whose answer lives in your docs, with intervals that separate.

## What no docs change fixes quickly

- A released model's weights. Answers without search reflect its training data until the next model ships.
- Perplexity's or OpenAI's index schedule.
- A competitor already ranking and cited for the same query.

## Questions I need answered

1. Which assistants matter most to you: Perplexity, ChatGPT with search, Google AI features, or IDE coding agents?
2. Can you edit `robots.txt`, the CDN bot rules and the docs templates?
3. Do you have docs analytics and 14+ days of server or CDN logs?
4. Can you paste two or three real answers where a competitor was cited, with the assistant and date?
5. By what date does a result have to show, and what is your weekly effort ceiling?

Send me your real page list and answers to 1 and 2, and I'll finalize the file and draft the panel.