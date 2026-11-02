# Cindermoor Pay: payout sample cleanup and sample rules

I followed `docs-code-sample-standards` and read its checklist and policy template. I did not run `scripts/sample-audit.py`, because writing the test files was denied. The findings and the check of the cleaned block below come from reading the skill's rules and the script's regexes, not from a run.

## ⚠️ P0: rotate the key first

`sk_live_9fKq2pRt7LwZ3xVn8MdE4cYb` is a live-format secret key in your most-copied block. Treat it as leaked. It is also now in this conversation.

1. Revoke it and issue a new one.
2. Check the audit logs for payouts you did not create. This endpoint moves money.
3. Then merge the cleanup below, since a cleaned page does not un-leak the key.

## Findings on the original block

| Severity | Finding | Fix |
|---|---|---|
| P0 | Live-format secret key in a copyable block | Replace it and rotate the real key |
| P2 | `$` prompt character is copied with the command | Remove it |
| P2 | `...` inside the block is copied and breaks the command | Remove it, or list the real parameters |
| P2 | Response glued into the command block | Move it to its own block |
| P2 | No language identifier on the fence | Use `bash` and `json` |
| P2 | No execution tier | Assign one (see below) |

## Cleaned block

Create a payout. First set `CINDERMOOR_API_KEY` to your own test-mode key from the dashboard. The key in this example is only a stand-in. It is rejected with a `401` until you replace it.

````markdown
```bash tier=run
export CINDERMOOR_API_KEY=acct_test_51H8xQ2eZvKY

curl -X POST https://api.cindermoor.com/v2/payouts \
  -H "Authorization: Bearer $CINDERMOOR_API_KEY" \
  -d amount=4500
```

Expected response:

```json
{ "id": "po_7731", "status": "pending" }
```
````

Three things to check before you publish:

- **The `...`:** I removed it and did not guess what it hid. If `/v2/payouts` requires more fields (currency, destination), list them. If none are required, leave it as is.
- **The `acct_test_` prefix:** it looks like an account ID, but the header expects a secret key. If your test-mode secret keys have another prefix, such as `sk_test_`, use that shape so the stand-in matches what readers will see.
- **The `tier=run` tag:** I assumed this is a quickstart-path sample, so I tagged it Run against test mode. If CI cannot run it, downgrade it to compile-only or illustrative and label it on the page.

## Where I departed from the skill's policy

You asked for `acct_test_51H8xQ2eZvKY` and no angle brackets. The skill's default is angle-bracket placeholders. It also lists a plausible fake value as a reader-paste failure mode. I followed your choice because the value is not a credential, so it is a P2 policy deviation, not a P0.

The risk is real, though. A reader who pastes it verbatim gets a `401`, which is the support ticket you are trying to stop. Three mitigations are built in:

- The key sits in an env var, so a reader changes one line and not the command.
- The prose says plainly that the value is a stand-in.
- The policy records an expiry for this exception (rule 3 below).

If support tickets don't drop within a quarter, switch to `<YOUR_API_KEY>`. Readers who find angle brackets confusing usually need the prose that explains them, not a different placeholder.

## Rules for the rest of the docs

**Anatomy**
1. Every fence has a language identifier (`bash`, `json`, `plaintext`).
2. A sample contains everything needed to run it in a fresh shell or file: setup, auth, and one code path.
3. Every sample has a tier tag in the fence info string: `tier=run`, `tier=compile-only` or `tier=illustrative`. Untagged samples count as Run, so they fail loudly. Illustrative samples carry a visible label on the page.
4. Blocks stay under 40 lines.

**Copy-paste safety**
1. No prompt characters (`$`, `#`, `PS>`) in command blocks.
2. Commands and their output go in separate blocks. Label the output "Expected response".
3. No `...` or `…` inside a block. Mark an omission with a comment in the language's own syntax, or list the real parameters.
4. Keep the placeholder format the same everywhere: one stand-in value, in a named env var, with the line "replace this with your test key" in the prose above the block. Record any exception to this rule in the policy with a reason and an expiry date.
5. Use only test-mode stand-ins and reserved-range hosts (`example.com`, `192.0.2.x`). Never use a value in a live-credential format (`sk_live_`, `AKIA…`, `ghp_…`, JWTs, private-key headers).

**Security**
1. No disabled TLS (`-k`, `--insecure`, `verify=False`).
2. Any money-moving or destructive call uses a test key and carries a warning above the block. Add an inline guard where the language allows one.
3. Auth setup lives on one page. Other samples link to it and do not repeat it with variations.
4. Show one failure path (for example the `401` and `402` responses) for any call that fails in normal use.

**Verification and ownership**
1. Quickstart, auth and first-call samples must be Run and green in CI against test mode. Everything else is Run or compile-only, or labelled illustrative.
2. Single-source samples from tested files and publish a marked region. Hide setup with markers and never delete it.
3. Failing samples fail the docs build. A red sample lands in the owning team's queue with a stated fix SLA.
4. Run `scripts/sample-audit.py docs/ --format summary` on every release. Read its flags as candidates to confirm, not verdicts.
5. Run the audit on the whole docs tree now, not only this page. A key that leaked here is likely to appear in other samples too.

## Fix queue

1. 🔴 Rotate the live key, check the logs, and publish the cleaned block. Do this first.
2. 🟠 Run the audit over the full docs tree and fix every `credential-shaped-literal` flag. The skill ranks leaked credentials above every other finding.
3. 🟢 Fix the remaining P2s (prompts, ellipses, glued output) in bulk, since the fixes are mechanical.
4. ℹ️ Add the audit to the release checklist and make CI fail on P0 and P1 findings.