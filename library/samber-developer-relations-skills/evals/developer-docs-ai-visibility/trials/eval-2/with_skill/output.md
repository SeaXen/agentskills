**Verdict:** your four rules block OpenAI training, Gemini training and Gemini grounding. They block nothing else. The `Google-Extended` line explains the Gemini drop. The GPTBot line has no effect on ChatGPT citations. Two of the four lines do nothing.

## What each line does

Labels follow the skill: vendor-documented, practitioner inference, first-party.

| robots.txt line | What it controls | Effect |
|---|---|---|
| `GPTBot` | OpenAI training only (vendor-documented) | Keeps docs out of OpenAI training sets. Does not touch ChatGPT search or live fetch. |
| `Google-Extended` | Gemini training **and** grounding in the Gemini app (vendor-documented) | Removes docs from grounded Gemini answers. Google Search and AI Overviews are unaffected. |
| `Claude-Web` | Retired token (vendor-documented) | Does nothing. Anthropic no longer lists it. |
| `anthropic-ai` | Retired token (vendor-documented) | Does nothing. Anthropic no longer lists it. |

## Why ChatGPT still cites you

OpenAI runs three separate agents. `OAI-SearchBot` handles search. `ChatGPT-User` handles live fetch. `GPTBot` handles training. Your file blocks only `GPTBot`.

OpenAI says a site that opts out of `OAI-SearchBot` won't appear in ChatGPT search answers, and it says robots.txt rules may not apply to `ChatGPT-User`. Neither was blocked, so ChatGPT keeps citing you. Security's claim that GPTBot controls ChatGPT is wrong. GPTBot controls training only.

## Why Gemini stopped citing you

`Google-Extended` also gates grounding for Gemini Apps. Disallowing it removes your docs from grounded Gemini answers. This matches the devrel person's report.

- **Not confirmed:** nobody has measured this. The devrel claim is first-party anecdote, and the mechanism is vendor-documented. No before/after run exists.
- **Scope:** the loss covers Gemini app grounding only. AI Overviews and AI Mode run on Googlebot and Search. Check them separately, because "Gemini stopped" may not mean all Google AI surfaces.
- **Trade-off:** I found no way to opt out of Gemini training and keep Gemini grounding. It is one token. That makes this a real policy decision.

## Where the preset misses its goal

Security wanted docs out of training sets. For Anthropic, `ClaudeBot` is the training agent and your file doesn't list it. Anthropic training is therefore not opted out. The two Claude lines name tokens that no longer matter. `Claude-SearchBot` and `Claude-User` are also open, which is fine if you want Claude to cite you.

## What I couldn't check

- **CDN rules:** I saw only robots.txt. The preset may also run WAF or bot rules, and a block there overrides robots.txt. User-triggered fetchers such as `ChatGPT-User` and `Perplexity-User` may ignore robots.txt anyway, so only the CDN can stop them. Get the CDN's rule list.
- **Live file:** confirm the robots.txt you pulled is the one served now. A managed preset can append lines.
- **Vendor pages:** the bot table changes several times a year. Re-read each vendor's crawler page before changing anything.

## What to tell Security

1. `GPTBot` controls OpenAI training only. Keep it if training opt-out is the goal. It has no effect on ChatGPT citations.
2. `Claude-Web` and `anthropic-ai` are dead tokens. Real Anthropic training is open because `ClaudeBot` isn't blocked.
3. `Google-Extended` is why Gemini stopped citing the docs. Keeping it means accepting that loss. Removing it means accepting Gemini training on the docs.

## Decision for you and Security

- **Option A, keep the Gemini opt-out:** keep `GPTBot` and `Google-Extended`. Replace the two dead lines with `ClaudeBot`. Accept zero grounded Gemini citations and write that down as a deliberate trade.
- **Option B, restore Gemini:** drop `Google-Extended`. Keep `GPTBot` and add `ClaudeBot`. Accept Gemini training on the docs.

I lean to B only if Gemini answers matter to your developers. For API-first fraud scoring, I'd guess they do, but that is my inference. Security owns the training question. The docs team owns the visibility cost.

## Verify before you promise anything

1. **Next, about 15 minutes:** pull the CDN bot rules and the live robots.txt.
2. **Then, about half a day by hand:** run 10 real developer prompts, 5 runs each, on Gemini and ChatGPT with search on. Score cited sources and whether your docs are cited. This gives a June-onward baseline instead of an anecdote.
3. **After any change:** re-run the same panel in 4 to 8 weeks. Report citation recovery as pending until then, because re-crawl runs on Google's schedule.