---
name: nextjs-server-action-recon
description: Extract Next.js action IDs; replay proxied web trackers.
category: web-recon
---

# Next.js Server Action Recon

Use when a target site is a Next.js app (App Router) and the user wants its **Live Server Action ID** (the 40–42 hex-char string a Server Action form posts to, format like `60e0f63a693b083fb961b661e6fd775e6ca25dc4ba`), or wants to **reverse-engineer a client-side "tracker"** that POSTs to an operator/backend API to scan availability (phone numbers, SIM serials, etc.).

Covers: downloading the prod JS chunks, grepping the minified bundle for action-ID bindings, telling page-specific IDs apart from app-wide ones, and replicating the tracker's proxied POST with curl/python.

## Triggers
- "find the Live Next.js Action ID" / "scan action id" / "what server action does this form call"
- "this tracker checks number/serial availability — find the API it hits"
- any task needing the server-reference hash a Next.js form submits to

## Steps

1. **Confirm it's Next.js.** Look for `/_next/static/` references in the page HTML.

2. **Download all chunks.**
   ```bash
   curl -s -L "https://SITE/PATH" -o page.html
   grep -oE '/_next/static/chunks/[A-Za-z0-9_/.-]+\.js' page.html | sort -u > chunks.txt
   mkdir -p chunks && cd chunks
   while read c; do fn=$(echo "$c" | sed 's#/_next/static/chunks/##'); curl -s -L "https://SITE$c" -o "$fn"; done < chunks.txt
   ```

3. **Extract action IDs from the bundle** (see `references/nextjs_action_id_extraction.md` for the exact python one-liner). The minified pattern is:
   ```
   createServerReference)("(<hex>)"
   ```
   Note the `)(` — minified output is `createServerReference)(...`, NOT `createServerReference(...)`. Anchor your regex on that.

4. **Length reality: IDs are 42 hex chars here, not 40.** Do NOT hard-code `{40}`. The user's example format (`60e0f63a…`) is genuine but the captured IDs in this bundle were 42 chars. Match `[0-9a-f]+` and length-check afterward.

5. **Page-specific vs app-wide.** A *static* page (no `<form>`, no `action=` in HTML) has **no** Server Action ID in its HTML or RSC payload (`curl -H "RSC: 1"`). The shared chunks carry the site's **app-wide** auth/OTP/order IDs. If the specific page is static, its CTAs are plain `<a>` links and you'll find nothing page-specific — say so, and offer to trace the next route in the flow.

6. **Replay a proxied tracker.** Read its `fetch()` block. Many "trackers" POST a JSON body to `window.location.href` (their own URL), which the server proxies to the operator. Replicate with curl (see `references/web_tracker_post_replay.md`). Pass whatever fields the JS sends (`digits`, `brand`, `manual_action_id`, etc.).

7. **CRITICAL: send browser headers or you get a false 403.** A bare `urllib.request` POST (no UA/Origin/Referer) to the action endpoint returns **HTTP 403 from the WAF** — that is NOT a "no data" answer and will make you wrongly conclude "0 available". Send a full browser-like header set:
   ```python
   H = {
     "Content-Type": "application/json",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
     "Accept": "*/*", "Accept-Language": "en-US,en;q=0.9",
     "Origin": "https://SITE", "Referer": "https://SITE/PATH",
   }
   ```
   With these headers the SAME request returns a real `{"status":"EMPTY"}` or `{"status":"SUCCESSFUL",...}`. Always probe with one known-good value (the site's own example, e.g. `20040888`) to confirm SUCCESSFUL before trusting a sweep's EMPTYs.

8. **Detect/avoid throttling.** Operator APIs throttle shared/public action IDs. After bulk scanning you'll see HTTP **403 even with correct headers** (and the app's own default probes start 403-ing). Trustworthy results need low-rate retry: concurrency 1, ~0.8–1.2s gap, back off (re-probe every ~30s, cap ~10 min) on 403, then abort cleanly. Treat sustained EMPTY-after-initial-success as **throttle**, not "nothing available".

9. **Match the site's actual input format — the #1 cause of empty results.** Reverse-engineer exactly what the input box expects:
   - If the example is `20040888` (8 digits), the server wants the **8-digit tail**, NOT the full `016...` number and NOT a short fragment.
   - Some sites use `custom` scan mode and require `num.msisdn.includes(baseSearch)` — the returned value must **contain** your search string. Others do fuzzy neighbor matching (returning 4 arbitrary allocated numbers per seed that often DON'T match your pattern).
   - Search **short memorable fragments** (`7777`, `1212`, `1122`) and keep only numbers that contain the fragment — that's how a human finds memorable numbers; full 8-digit pattern seeds almost never match.

## Pitfalls
- Don't grep the static HTML or RSC payload for the hex ID — it lives in the `.js` chunks, not the page.
- The example ID the user gives may be one of many app-wide IDs; confirm it appears in a downloaded chunk to verify it's genuine.
- A public/shared action ID is not something you can mint. For sustained bulk scanning you'd need a private authenticated session — be honest about this limit.
- Browser automation on these SPA trackers is brittle: the page can crash to `about:blank` on search with no JS error. Prefer the curl/python replay over driving the UI.
- **Deliver a list, not a report.** When the user asks for "the number list" / "give me a txt file", write the actual itemized list (even if empty, print NONE + why) — not a summary report. A report with no list is the wrong deliverable.
- **Fuzzy matching returns noise.** A "VIP finder" returns 4 random allocated numbers per seed; most won't match your pattern. Filter strictly (require the fragment in the returned MSISDN) and rank by your own pattern score — but state the VIP-ness is *your* ranking, not the provider's certification (provider `vip_stars`/`is_vip` often come back 0/false on public relays).

## Verification
- After extraction: confirm the ID string appears in a downloaded chunk and matches the user-supplied example (if given).
- After replay: probe a known control fragment (e.g. the app's own default search value) to confirm the endpoint is live vs throttled before trusting a sweep's EMPTYs.

## References
- `references/nextjs_action_id_extraction.md` — exact terminal + python commands
- `references/web_tracker_post_replay.md` — concrete mueagle.com/Airtel VIP SIM tracker case study (request shape, response shape, rate-limit behavior)
