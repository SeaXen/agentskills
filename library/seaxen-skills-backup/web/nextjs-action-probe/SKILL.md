---
name: nextjs-action-probe
description: Call Next.js Server Actions via extracted action IDs.
category: web
---

# Next.js Server Action Probe

Use when a Next.js (App Router) site gates data behind a "Server Action" and you must call it directly - e.g. a search/availability checker that POSTs to its own URL, or the user hands you an action ID like `60e0f63a693b083fb961b661e6fd775e6ca25dc4ba`. Signs: page is static but has interactive forms/buttons; network tab shows a POST to the page URL with a 40-42 char hex in the body; or there's a "paste your action hash from F12" box.

## Workflow

### 1. Extract the action ID(s) from the production bundle
- Fetch the page HTML; collect `/_next/static/chunks/*.js` references.
- Download every chunk, then grep the binding:
  `grep -rhoE 'createServerReference\("([0-9a-f]{40,44})"' chunks/ | sed -E 's/.*"([0-9a-f]+)"/\1/' | sort -u`
- The ID is the first quoted arg; a trailing friendly name sometimes follows (`", "socialLogin"`).
- PITFALL: hex blobs may contain crypto constants (e.g. RFC 3526 DH prime `ffffffff.c90fdaa22168c234c4c6628b`). Real IDs sit inside `createServerReference("...")` calls.
- PITFALL: the ID may be 42 chars, not 40. Don't hard-code `{40}`.

### 2. Find how the page calls the action
- Grep HTML/JS for `fetch(`. App Router Server Actions are often called by POSTing to `window.location.href` (the current page) with `Content-Type: application/json` and a JSON body.
- Copy the body shape exactly: `JSON.stringify({ digits, brand, manual_action_id })` - field names vary per site.
- Read the value generator (e.g. `generateSlidingFuzzyVariations`, `activeSubdivisions`) to learn what candidate strings the UI sends. This reveals the expected INPUT FORMAT.

### 3. Replicate the POST - with browser headers (mandatory)
- A bare `urllib`/`curl` POST gets HTTP 403 from the WAF. Send browser-like headers or it reads as a bot:
  ```
  User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
  Accept: */*
  Accept-Language: en-US,en;q=0.9
  Origin: <site origin>
  Referer: <page URL>
  ```
- Parse the response. Typical:
  - `{"status":"EMPTY","message":"No available numbers match."}`
  - `{"status":"SUCCESSFUL","numbers":[{"msisdn":"88016.","vip_stars":0,"is_vip":false}]}`

### 4. DISCOVER THE CORRECT INPUT FORMAT (the #1 failure mode)
- The endpoint may NOT want a full phone number or a short fragment. Test all of these against one probe you expect to succeed:
  - full number with prefix: `01600502007`
  - 8-digit tail (part after the prefix): `00502007`  (often the right one)
  - short fragment with subdivisions: `31111`
- Match the site's own placeholder/example (e.g. its `20040888` is an 8-digit tail).
- PITFALL: sending the wrong format returns `EMPTY` for EVERY input. That looks like "nothing is available" but is YOUR bug. Always validate format with a probe expected to succeed before concluding "0 found".

### 5. Understand fuzzy matching
- A Server Action may return SEED/neighbor numbers, not literal matches. Airtel's checker returned 4 arbitrary allocated numbers per search tail - the tail is a search seed, not a substring requirement. Don't filter results by "must contain the tail"; keep all SUCCESSFUL results and rank them yourself by pattern.

### 6. Deliver the ACTUAL LIST, not a report
- The user wants the items, not a description of them. Write a .txt/.csv with one item per line, ranked (e.g. by VIP pattern score), and attach via `MEDIA:`.
- If 0 found, say so honestly BUT show what was scanned and why (wrong format vs genuinely empty). Never bury the list behind a "report" - when asked for a list, produce the list file.

## Rate-limit / safety
- Shared/public action IDs get throttled (403) after bulk scanning. Use >=1s gap, concurrency 1, checkpoint-resume. A private logged-in session ID avoids this but must come from the user.
- Read-only probing of a public endpoint; respect the site's ToS.

## References
- `references/extraction-recipe.md` - copy-paste commands to extract IDs and reverse the POST.
- `scripts/probe_server_action.py` - reusable safe scanner template (browser headers, checkpoint, ranking).
