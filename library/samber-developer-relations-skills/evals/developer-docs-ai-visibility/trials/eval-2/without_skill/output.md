**Do first (about 20 min):** pull the live `https://docs.quillstone.com/robots.txt` and your CDN's bot or firewall events for June onward. The CDN preset blocks at the edge, separately from robots.txt, and it may block more than the four lines show. I did not check vendor docs or your CDN today. Confirm the bot names below against the vendors' current crawler pages before you quote them.

## What each line does

| Line | What it controls | Effect on citations |
|---|---|---|
| `GPTBot` | OpenAI **training** crawler | None. It does not control ChatGPT answers or citations. |
| `Claude-Web` | Legacy Anthropic token | Probably nothing. Anthropic now documents other names. |
| `anthropic-ai` | Legacy Anthropic token | Probably nothing, same reason. |
| `Google-Extended` | Google control token, not a crawler | Blocks use of your pages for Gemini training and Gemini grounding. |

## Why ChatGPT still cites you

- OpenAI uses separate bots:
  - `GPTBot` is for training.
  - `OAI-SearchBot` builds the ChatGPT search index that produces citations.
  - `ChatGPT-User` fetches pages when a user asks. OpenAI says robots.txt may not apply to it.
- Your file blocks none of the search bots, so Security's belief is wrong. `GPTBot` is a training opt-out and nothing more.
- Citations that continue are expected. Check that the CDN preset isn't also blocking `OAI-SearchBot` at the edge. If it is, citations will decay over time as the index refreshes.

## Why Gemini stopped

- Google says `Google-Extended` governs Gemini training and grounding for Gemini Apps and the Gemini API. It does not affect Search ranking or AI Overviews, which follow `Googlebot`.
- A June block and a June drop in Gemini citations match. This is the likely cause, not proof.
- Confirm it:
  - Ask the same 10 questions in the Gemini app and in AI Overviews or AI Mode. If only the Gemini app lost you, that points to `Google-Extended`.
  - Rule out a Google core update or ranking drop in Search Console for the same weeks.
- Google offers no way to opt out of training while allowing Gemini grounding. It is one token, so this is a business decision.

## What the Anthropic lines do

- Anthropic's current names are `ClaudeBot` (training), `Claude-SearchBot` (search) and `Claude-User` (user fetch).
- Your two lines use old names, so they probably don't block Claude's current crawlers and probably don't achieve Security's goal. The CDN preset may be doing the real blocking for Claude.
- Training crawlers not in your file at all: `CCBot`, `Applebot-Extended`, `Meta-ExternalAgent`, `Bytespider`, `PerplexityBot`. The CDN preset may cover some of them.
- Robots.txt is voluntary, and it does not remove anything already crawled.

## What to tell Security

1. **Keep the `GPTBot` line.** It does what they want, which is a training opt-out. It never controlled ChatGPT.
2. **Allow the search and user bots.** Add `OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot` and `Claude-User`. Put them in the CDN allowlist too, because robots.txt alone won't override an edge block.
3. **Replace the two dead Anthropic lines** with `ClaudeBot`.
4. **Decide on `Google-Extended` jointly.** Choose between "no Gemini training" and "Gemini cites our docs". My recommendation is to remove the line, because docs exist to be found and the block costs you Gemini visibility. Security can keep it if training exposure outweighs that, but that choice should be explicit.

Suggested robots.txt:

```
# Training opt-out
User-agent: GPTBot
Disallow: /

User-agent: ClaudeBot
Disallow: /

# Search and user-triggered fetch: keep citations
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Claude-SearchBot
Allow: /

User-agent: Claude-User
Allow: /
```

If Security keeps `Google-Extended`, add it as a `Disallow: /` block above the search bots. Otherwise omit it.

## Verify after the change

1. Test the edge with `curl -A "<bot UA>" -I https://docs.quillstone.com/` for each bot. Expect 200. A 403 means the CDN preset is blocking it.
2. Spoofed UAs may get different treatment from real verified bots, so also check the CDN bot logs for real hits.
3. Re-run your fixed question set after 1 to 4 weeks, because index refresh lags.

**Next:** run the `curl` check for `OAI-SearchBot` and paste the status code. It tells us whether the CDN preset is the second blocker.