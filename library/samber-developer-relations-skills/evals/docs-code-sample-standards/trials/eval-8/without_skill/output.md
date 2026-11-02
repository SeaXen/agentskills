## ⚠️ Rotate the key first

`sk_live_9fKq2pRt7LwZ3xVn8MdE4cYb` is in your most-copied page, so treat it as leaked. Revoke it and issue a new one before you publish anything else. Check the logs for payouts you didn't create. A `po_7731` payout shown with a live key suggests someone may have run this command as written.

## Cleaned block

Command, with no `$` prompt, so a triple-click copies only runnable text:

```bash
curl -X POST https://api.cindermoor.com/v2/payouts \
  -H "Authorization: Bearer acct_test_51H8xQ2eZvKY" \
  -d amount=4500
```

Response, in its own block:

```json
{
  "id": "po_7731",
  "status": "pending"
}
```

Text to put around it:

> Replace `acct_test_51H8xQ2eZvKY` with your own test key from the dashboard. Test keys never move real money.

I changed four things:
- The live key is gone, so no secret remains.
- The `...` is gone. It made the command unrunnable.
- The command and its response are now in separate blocks. Copying the old block also copied the JSON.
- The JSON is pretty-printed.

**Open question:** if `/v2/payouts` requires more than `amount` (a currency or destination, say), add those as `-d` lines. I didn't invent fields. A command that fails on copy produces the same support tickets.

**Heads-up on the key:** `acct_` normally reads as an account ID, and your real keys use `sk_`. I used the key you gave me, but readers may wonder whether they need an account ID rather than a secret key. A line like "this is your test secret key" in the surrounding text would settle it.

## Rules for the rest of the docs

1. **Never publish a live credential.** Every key in the docs is a test key or a documented fake. A pre-commit secret scanner (gitleaks or similar) should block `sk_live_` and similar prefixes in docs.
2. **Use one canonical example key, sitewide.** It is `acct_test_51H8xQ2eZvKY`. Don't invent variants, so readers learn to recognize it and you can grep for it.
3. **No angle brackets or `YOUR_KEY` placeholders.** Use the concrete fake value and add one sentence after the block saying to replace it.
4. **State the substitution once, after the block, in prose.** Don't put "replace this" inside the code. Name the exact string to replace and where to find the real one.
5. **Every command runs as pasted.** No `...`, no `$` prompt, no elided flags. If a snippet is partial, say so in the text and link to the full call.
6. **Command and output never share a block.** Use a `bash` block for the command and a `json` block for the response.
7. **Use backslash continuations with two-space indents,** one flag per line, so the command reads cleanly and pastes intact.
8. **Pretty-print JSON responses,** and keep the response fields the same as the real API returns.
9. **Test keys only touch test mode.** Say that next to the first key a reader sees, so they know the command is safe to run.
10. **Audit what's already published.** Search the docs for `sk_live_`, `Bearer`, `...` inside code fences, and `$ ` prompts. Fix each hit under the same rules.
11. **Check support tickets monthly for repeated "I had to change X" complaints.** Each one is a snippet that breaks rule 5.