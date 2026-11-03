---
name: web-endpoint-reverse-sweep
description: Extract a hidden web API and run a safe rate-limited sweep.
---

# Web Endpoint Reverse-Sweep (Safe)

Reverse-engineer how a web page talks to its backend, then run a polite sweep that
collects real results. The defining constraints: **do not break the host, do not
disconnect the agent's own chat (Discord/Telegram), and never fabricate results.**

## When to use
- User wants to extract a Next.js Server Action ID (looks like a 40–42 char hex string).
- User wants to "scan for available X" on a site that has no public API (VIP numbers,
  product availability, slot lookups, etc.).
- User pastes a URL and asks you to find or replicate the call a button makes.

## Step 1 — Get the static page + find the action ID
```bash
curl -s -L "URL" -o page.html
# 40-char hex candidates (App Router often 42 chars, verify length)
grep -oE '[0-9a-f]{40,44}' page.html | sort -u
```
If none in static HTML, the IDs live in JS chunks. Download every `_next/static/chunks/*.js`
referenced in the page, then extract the real Server Reference bindings:
```python
import re, glob
for f in glob.glob('chunks/*.js'):
    t = open(f, encoding='utf-8', errors='replace').read()
    for m in re.finditer(r'createServerReference\)\("([0-9a-f]+)",', t):
        print(m.group(1))   # the action ID
```
The ID is the **first quoted arg** to `createServerReference(...)`. Friendly names often
follow as a later string arg (e.g. `"socialLogin"`).

## Step 2 — Find the relayed endpoint + request shape
Search the page/app JS for `fetch(` to learn the method, URL, and body:
```bash
grep -aoE 'fetch\([^,]{0,120}' page.html
```
Common pattern for "tracker" style sites: it POSTs to its **own page URL** with a JSON
body that includes the action ID plus the user's search value. Read the exact body keys
from the source (e.g. `{"digits":..., "brand":..., "manual_action_id":...}`).

## Step 3 — Probe ONCE with browser-like headers (CRITICAL)
A bare `urllib`/`requests` call from the host often gets **HTTP 403** from the site's WAF
even though the user's real browser works fine. Always send browser headers:
```python
HEADERS = {
  "Content-Type": "application/json",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
  "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
  "Origin": "<site origin>", "Referer": "<page URL>",
}
```
Test a single value first. If you get a real JSON response (e.g. `{"status":"EMPTY"}` or
`{"status":"SUCCESSFUL","numbers":[...]}`), you're through. If 403, it's a header/WAF issue
— not proof the data is unavailable.

## Step 4 — Safe sweep
Replicate the site's own candidate-generation logic exactly (read it from the page JS —
e.g. for a 4-digit fragment it may build `sub+frag` and `sub+d+frag` for subdivision
prefixes `3,7,8,9,4` × d 0–9 = 55 candidates). Then:
- **Concurrency 1** (or ≤8 with a small gap), **~1.2s gap** between requests.
- **403 backoff**: on HTTP 403, wait and re-probe (e.g. every 30s) up to a cap (10 min);
  abort cleanly if it never clears. Do NOT hammer — that burns the shared ID.
- **Checkpoint + resume**: write found results to a JSON file every hit; write a
  `done.json` set so a re-run skips completed work and merges new hits.
- **Record only real `SUCCESSFUL` responses.** Never invent "available" entries.
- **Interpret responses precisely:** a valid JSON `EMPTY` is a genuine negative for that completed query, not evidence of IP blocking. Only claim throttling/blocking with direct evidence such as HTTP 403/429, CAPTCHA, transport failure, or an explicit server throttle response. Do not infer a block merely from repeated `EMPTY` responses.
- **Respect UI sampling semantics:** when a UI accepts a short fixed fragment (for example four digits inside an eight-digit serial), replicate the site's expansion and filtering exactly. Repeating the same fragment can be intentional when each run samples a bounded candidate batch; do not replace it with a one-shot full-number search.
- **User-controlled long runs:** if the user requests repeated searches until a hit or an explicit stop, keep the worker alive and report progress. Do not silently cap attempts, switch fragments, or kill/reconfigure an active worker without permission. If multiple fragments are requested as separate workers, stagger their starts and use the requested per-worker wait interval rather than conflating start staggering with request frequency.
- Outbound POSTs to the target site do NOT touch the host's network interface or VPN —
  this cannot make the agent's Discord appear offline. (The only thing that makes Discord
  drop is WARP/interface cycling — don't do that here.)

A ready runner lives at `scripts/safe_sweep.py` (adapt `URL`, `ACTION_ID`, header Origin/
Referer, and the candidate generator).

## Step 5 — Report + deliver
- Summarize: patterns covered, candidate serials checked, hits found, whether responses
  were genuine (EMPTY) or a block (403).
- Deliver found numbers as a **TXT file via MEDIA:** attachment**, not a path-only reply.
- Be honest about ceiling: shared/public action IDs can be throttled; a truly reliable
  sustained sweep needs a **private logged-in session ID** from the user's own browser
  (F12 → Network → find the POST with the 42-char hex). You cannot mint that.

## Gotchas
- Static HTML may have **no** action ID for a page that is fully static (CTAs are plain
  links, no `<form>`/Server Action). Then there's nothing to extract for that route — the
  ID belongs to a different (checkout/onboarding) route.
- Hex blobs in minified JS concatenate without separators; verify each candidate is passed
  as a quoted arg to `createServerReference`, not a substring of a longer constant
  (e.g. the RFC 3526 DH prime `ffff...c90fdaa...` is NOT an action ID).
- "EMPTY" from the API is a genuine negative, not a soft-block — distinguish it from 403.

## References
- `references/nextjs-action-id-notes.md` — how App Router encodes action IDs, where to
  look (chunks vs RSC payload), length variance (40 vs 42).
