I can't reach your logs from here, so I have no version numbers. Below are the corrected claim, a script that produces the breakdown, and how to answer the robots.txt question.

## 1. Don't send the "ChatGPT reads our docs" message yet

**GPTBot hits do not show that ChatGPT search can read your docs.** OpenAI runs three separate crawlers, and each one obeys its own robots.txt rule:

| User-agent | Purpose | What GPTBot hits tell you about it |
|---|---|---|
| `GPTBot` | Collects content for model training | This is the one you counted. |
| `OAI-SearchBot` | Builds the index behind ChatGPT search results and citations | Nothing. |
| `ChatGPT-User` | Fetches a page when a user asks ChatGPT to open it | Nothing. |

- Your 4,200 hits show that GPTBot is allowed, or at least not blocked.
- A `User-agent: GPTBot` group can allow it while `OAI-SearchBot` falls under `User-agent: *` and gets blocked.
- Whether `ChatGPT-User` follows robots.txt is documented differently over time, so check OpenAI's current crawler page before you rely on it.
- A plain `grep GPTBot` can also match a referer or URL on the same line, and it counts spoofed user-agents.

## 2. Breakdown by version

Save this as `gptbot-by-version.sh`. It is read-only. Run it once per host, because the 1.x host is a different site. Put the logs in a folder you control and pass the paths as arguments.

```bash
#!/usr/bin/env bash
# usage: gptbot-by-version.sh <host> <agent-regex> <gz logs...>
# example: gptbot-by-version.sh docs.dunmoresignal.io GPTBot /logs/docs/*.gz
host=$1; agent=$2; shift 2
gzip -dcf "$@" | awk -F'"' -v host="$host" -v agent="$agent" '
  $6 ~ agent {                       # field 6 = user-agent in combined format
    split($2, r, " "); path = r[2]   # field 2 = "METHOD /path HTTP/x"
    split($3, s, " "); st = s[1]     # field 3 = " status bytes "
    if      (path ~ /^\/robots\.txt/)           v = "robots.txt"
    else if (host ~ /^v1\./)                    v = "1.x (v1 host)"
    else if (path ~ /^\/docs\/3\.x([\/?]|$)/)   v = "3.x"
    else if (path ~ /^\/docs\/2\.x([\/?]|$)/)   v = "2.x"
    else                                        v = "other (non-versioned)"
    print v "\t" substr(st,1,1) "xx"
  }' | sort | uniq -c | sort -rn
```

Run it for each agent so you can compare:

```bash
for a in GPTBot OAI-SearchBot ChatGPT-User; do
  echo "== $a =="
  ./gptbot-by-version.sh docs.dunmoresignal.io "$a" /logs/docs/*.gz
  ./gptbot-by-version.sh v1.docs.dunmoresignal.io "$a" /logs/v1/*.gz
done
```

Read the output like this:

- **Status column:** Hits that are mostly `3xx`, `4xx` or `5xx` mean GPTBot arrived but did not read the content. Only `2xx` counts as read.
- **Redirects:** If `/docs/` redirects to `/docs/3.x/`, the 301s inflate the count without adding content reads.
- **`other (non-versioned)`:** If this row is large, add its paths to the script. Examples are `/docs/latest/` or `/api/`.
- **Separate hosts:** Never merge the two hosts' numbers into one. If your logs record the host in a custom field, split on that instead.
- **Spoofing:** Take the distinct IPs of the GPTBot hits and check them against OpenAI's published ranges at `https://openai.com/gptbot.json`. The same check works for `searchbot.json` and `chatgpt-user.json`. IPs outside the ranges are spoofed and should not be in your count.

## 3. Does robots.txt allow ChatGPT search?

Fetch both files, because robots.txt applies per host:

```bash
curl -si https://docs.dunmoresignal.io/robots.txt
curl -si https://v1.docs.dunmoresignal.io/robots.txt
```

Then check these things:

1. **Look for an `OAI-SearchBot` group.** If one exists, it controls that crawler.
   - If it has `Disallow: /`, ChatGPT search can't crawl your docs.
   - The GPTBot hits don't contradict this.
2. **If there is no `OAI-SearchBot` group,** it follows `User-agent: *`.
   - A blanket `Disallow` there blocks it, even when `User-agent: GPTBot` allows it.
3. **Check paths, not just the agent.** `Disallow: /docs/2.x/` blocks that version for any agent that falls under the rule.
4. **Check the HTTP status of each file.**
   - A `404` means everything is allowed.
   - A `5xx` can make crawlers back off or treat the site as disallowed.
   - A redirect to a login page is a common failure.
5. **Expect a delay.** OpenAI says changes to robots.txt can take about 24 hours to be picked up.
6. **Look for blocks outside robots.txt.** WAF or CDN bot rules can return `403` to `OAI-SearchBot` even when robots.txt allows it.

As a final check, grep your logs for `OAI-SearchBot`. Zero hits over 30 days means one of two things: it is blocked, or your pages haven't been picked up yet. A few `2xx` hits on `/docs/3.x/` confirm it can reach you.

## 4. Wording for the team

Until the `OAI-SearchBot` check is done, use this:

> GPTBot (OpenAI's training crawler) fetched our docs N times in 30 days: X on 3.x, Y on 2.x, Z on 1.x. That shows training access only. We have not yet confirmed that ChatGPT search (`OAI-SearchBot`) or user-initiated fetches (`ChatGPT-User`) can reach us.

If you paste the script output and both robots.txt files here, I can fill in the real breakdown and give a firm verdict.