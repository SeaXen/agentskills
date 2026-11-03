---
name: nextjs-action-id-extraction
description: Find Next.js Server Action IDs for a given site URL.
---

# Extract Next.js Server Action IDs

Next.js App Router encodes Server Action IDs as **40–42 char hex strings** passed to `createServerReference(...)`. They are almost never in the static HTML and often not in the RSC flight of a static route. The reliable source is the downloaded JS chunks (`/_next/static/chunks/*.js`).

## When to use
- User gives a Next.js URL and asks for "the action ID" / "Live Next.js Action ID" / "server action id".
- User wants to know which Server Action a specific form or button triggers.

## Pitfalls (read first — these are where extractions go wrong)
1. **The target page may be STATIC.** If the route has no `<form>` and no `action=` attribute, there is no Server Action on that page — the CTAs are plain `<a>` links. Do NOT dump all site-wide action IDs and claim one belongs to that page. Verify the page actually wires a form/action first (grep `<form` and `action=` in the HTML). The user explicitly wants the ID *for that URL* — scanning the whole bundle and handing back unrelated global IDs is the wrong deliverable.
2. **IDs are 40–42 hex chars, not always 40.** Grep `[0-9a-f]{40,44}`. A strict `{40}` regex silently misses 42-char IDs (Next.js 14+ ships 42).
3. **The bundle call is `createServerReference)("<hex>"` with a `)` before the `(`.** It is invoked through a destructured export, e.g. `(0,s.createServerReference)("7f...",...)`. A naive regex without the `)` matches nothing.
4. **Action IDs are usually NOT in static HTML or RSC flight.** They live in `/_next/static/chunks/*.js`. Download the chunks.
5. **The action manifest (`/_next/static/app-build-manifest.js`) is normally 404 on prod.** Don't rely on it.
6. **Bare-hex grep lies.** A 40-hex grep on the bundle returns crypto constants (e.g. RFC 3526 DH prime `ffffffff...c90fdaa22168c234c4c6628b...`) and concatenated blobs. Always anchor on `createServerReference)("..."`, never bare hex.

## Workflow
1. Fetch the page HTML; record byte size.
   `curl -s -L <url> -o page.html`
2. Quick static checks (these often come back empty on App Router):
   `grep -oE '\$ACTION_ID_[0-9a-f]+' page.html`
   `grep -c '<form' page.html` and `grep -c 'action=' page.html`
   `grep -oE '[0-9a-f]{40,44}' page.html | sort -u`
3. Fetch the RSC payload (App Router):
   `curl -s -L <url> -H "RSC: 1" -o rsc.txt` then grep for hex/action.
4. Collect chunk URLs:
   `grep -oE '/_next/static/chunks/[A-Za-z0-9_/.-]+\.js' page.html | sort -u`
5. Download each chunk (loop over the list, strip the `/_next/static/chunks/` prefix for filenames).
6. Extract IDs from chunks:
   `grep -rhoE 'createServerReference\)\("[0-9a-f]{40,44}"' . | sed -E 's/.*"([0-9a-f]+)"/\1/' | sort -u`
7. (Optional) Label each ID by scanning ±400 chars of context for keywords: otp, login, order, balance, search, social, register, validate, msisdn, recharge, esim, prepaid, mnp.

## Verification
- **Cross-check with the user's example:** if they pasted a sample ID, confirm it appears in your extracted set — proves you hit the right bundle.
- **Confirm a specific page uses a given ID:** grep that page's RSC payload for the exact ID. If 0 matches, the page is static / doesn't call it.
- These IDs are public client-side values; extraction is read-only recon, not an exploit.

## Support files
- `scripts/extract_action_ids.sh` — one-shot bash: downloads all chunks for a URL and prints unique action IDs.
- `references/notes.md` — worked example (bd.airtel.com sim-services) and the 42-char / false-positive detail.
