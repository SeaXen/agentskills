**Do not tell the team "ChatGPT reads our docs and we're fine on access."** The 4,200 `GPTBot` hits don't support that sentence.

I have not seen your logs, so there are no per-version numbers below yet. Step 1 produces them in about 10 minutes.

## Verdict

1. `GPTBot` is OpenAI's **training** crawler (vendor-documented). Its hits say nothing about ChatGPT search or about live answers to a user.
2. ChatGPT search uses `OAI-SearchBot`. Live fetches for a user use `ChatGPT-User`. Your grep for `GPTBot` matches neither.
3. Hits do not prove robots.txt allows ChatGPT search. Nothing in an access log shows what robots.txt says. Read the file. ChatGPT search eligibility depends on `OAI-SearchBot` access (vendor-documented). A site that opted out of `OAI-SearchBot` "will not be shown in ChatGPT search answers, though can still appear as navigational links" (vendor wording).

A robots.txt like this gives you plenty of `GPTBot` hits and no ChatGPT search presence:

```
User-agent: OAI-SearchBot
Disallow: /
```

The reverse also happens. Blocking `GPTBot` leaves `OAI-SearchBot` untouched, so a "block AI training" preset can be safe for search.

## Step 1 - Per-version breakdown (run now)

The script's default version regex needs a `v` prefix (`/v3/`). Your paths are `/docs/3.x/`, so pass `--version-regex`. The combined log format has no host field, so run one pass per host.

```
# Host 1: docs.dunmoresignal.io
python3 scripts/ai-bot-log-summary.py \
  --path-prefix /docs/ \
  --version-regex '/docs/(\d+\.x)/' \
  --ip-ranges gptbot.json --ip-ranges searchbot.json --ip-ranges chatgpt-user.json \
  docs-access.log*.gz

# Host 2: v1.docs.dunmoresignal.io
python3 scripts/ai-bot-log-summary.py \
  --ip-ranges gptbot.json --ip-ranges searchbot.json --ip-ranges chatgpt-user.json \
  v1-access.log*.gz
```

- Treat every hit in the v1 output as 1.x. It will print `(unversioned)` because the version is in the hostname.
- Download the three OpenAI IP-range JSON files from OpenAI's bot documentation page. Pass every vendor file you want checked, or those agents read as unverified.
- Count only hits in published ranges. A user-agent string alone is trivially spoofed (vendor-documented practice), so some of the 4,200 may not be OpenAI.
- Read the status-class table. A `GPTBot` hit that got 301, 403 or 404 did not read a page.
- Fill in this table from the output:

| Version | `GPTBot` (training) | `OAI-SearchBot` (search index) | `ChatGPT-User` (live fetch) | Share of 200s | In OpenAI ranges |
|---|---|---|---|---|---|
| 3.x | from run 1 | from run 1 | from run 1 | from run 1 | from run 1 |
| 2.x | from run 1 | from run 1 | from run 1 | from run 1 | from run 1 |
| 1.x (separate host) | from run 2 | from run 2 | from run 2 | from run 2 | from run 2 |

What to look for:
- `OAI-SearchBot` at zero or near zero on 3.x while `GPTBot` is high means ChatGPT search likely can't see the current docs. Confirm in robots.txt and the CDN rules.
- High 2.x or 1.x share means training data favors old versions. That is first-party evidence for assistants answering with deprecated APIs.
- `ChatGPT-User` hits on old-version paths, and old paths with no current equivalent, are the early warning. A missing `ChatGPT-User` hit is weak evidence of anything.

## Step 2 - Check access (this answers the ChatGPT search question)

Read robots.txt on both hosts. Subdomains have separate robots.txt files, so `v1.docs.dunmoresignal.io/robots.txt` is a separate file to check.

1. Find rules for `OAI-SearchBot`, `ChatGPT-User` and `GPTBot`. A `User-agent: *` rule applies to any agent without its own group.
2. Check the CDN or bot-management layer for a "block AI crawlers" toggle or a managed robots.txt that someone outside the docs team enabled.
3. Remember `ChatGPT-User` may not obey robots.txt (vendor wording: "robots.txt rules may not apply"). Block or rate-limit it at the CDN or WAF, not in robots.txt.
4. Fetch three key pages with a plain HTTP client and no JavaScript. Body text and code blocks must be in the HTML. Many AI fetchers don't run scripts.
5. Check for `nosnippet`, `max-snippet:0` or `data-nosnippet` on code blocks. Those remove pages from Google's AI features. They don't affect ChatGPT.

Until you read the files, report robots.txt as **unreviewed**. Interim evidence of reachability is 200 responses to IP-verified `OAI-SearchBot` hits. That proves reach, not what robots.txt allows.

## What to tell the team

> We have 4,200 GPTBot hits (training crawler) across both docs hosts, split by version as shown above. That tells us OpenAI collected our docs for training, mostly from version X. It does not tell us ChatGPT search can cite our docs. We are checking OAI-SearchBot and ChatGPT-User traffic and robots.txt on both hosts, then we will confirm.

## Caveats

- OpenAI changes its agent list several times a year. Re-read its crawler page before acting.
- Hits show crawling, not citations. Whether ChatGPT cites you, and at the current version, needs a repeated prompt panel (5+ runs per prompt, scored against an answer key). No vendor publishes how it picks citations.

**Next, in 2 minutes:** run the two commands, then paste the "AI bot hits by role and agent" and "Bot hits by agent and docs version" sections here. I'll fill in the table and check robots.txt against it if you paste both files.