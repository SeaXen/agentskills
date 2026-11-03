# Google AI Pro / Gemini Pro account safety through Hermes

Last updated: 2026-06-20

## TL;DR

- `google-gemini-cli` OAuth provider in Hermes = **ban risk** for Pro/Ultra accounts. Use `agy` (Antigravity CLI) instead, or the `gemini` API provider with a separate key.
- Pro subscription **does not** transfer to API quota. They are separate billing systems. The AI Studio free tier gives a small daily budget for free; heavy use needs paid AI Studio billing on top of the Pro sub.
- `agy` is Google's official replacement for `gemini-cli`. It is **already installed** at `~/.local/bin/agy` (verify with `command -v agy && agy --version`). Use it via the `agy-cli` skill.

## Google's official policy (verbatim)

From `google-gemini/gemini-cli` discussion #20632, posted by the Google team on 2026-02-28:

> "Using third-party software, tools, or services to harvest or piggyback on Gemini CLI's OAuth authentication to access our backend services is a **direct violation** of Gemini CLI's applicable terms and policies."
>
> "**Permanent ban**: If an account is flagged for a second violation of ToS, it will be permanently banned."

Enforcement is **client-fingerprint-based** (HTTP client user-agent, request shape, header set) rather than account-based. Even though the OAuth token is real and valid, if the request doesn't look like the official `gemini` / Antigravity CLI client, automated systems can flag the account. Bans have been **delayed and retroactive** — sometimes weeks after the offending traffic.

## What already happened (real, not theoretical)

| Date | Event | Source |
|---|---|---|
| 2026-02-11 | Mass 403 ToS bans on paid Pro/Ultra accounts using OpenClaw, CLIProxyAPI, Pi coder via Antigravity OAuth | github.com/openclaw/openclaw#14203, discuss.ai.google.dev #124508 |
| 2026-02-15 | Specific bug report: `Cloud Code Assist API 403 (ToS Violation) for Individual AI Premium Accounts using Antigravity Auth` | github.com/openclaw/openclaw#16847 |
| 2026-02-28 | Google posts official ToS clarification + reinstatement process | github.com/google-gemini/gemini-cli#20632 |
| 2026-03-01 | Google begins reversing some bans on case-by-case appeal | reddit.com/r/openclaw |
| 2026-04-06 | Anthropic follows suit, closes door on subscription use via third-party tools | theregister.com |
| 2026-06-18 | **Sunset:** Cloud Code Assist OAuth stops serving consumer Gemini tiers (free / Pro / Ultra) | github.com/google-gemini/gemini-cli#22970, agentpedia.codes migration guide |

Today (2026-06-20) we are 2 days past the sunset. The `google-gemini-cli` provider in Hermes is effectively deprecated for consumer tiers regardless of ban risk — it will start returning 404s on more models as Google rotates endpoints.

## Pro subscription vs API quota

These are **separate Google billing systems** and do not share quota or credits:

| Access path | Uses Pro sub? | Where billed | Cost model |
|---|---|---|---|
| Gemini app (web/mobile) | ✅ Yes | Google One | $20/mo (AI Premium) or $250/mo (Ultra) |
| `gemini` API via AI Studio | ❌ No | Google Cloud / AI Studio | Pay-per-token, free tier exists (≈15 RPM Flash, ≈2 RPM Pro, daily caps) |
| Vertex AI | ❌ No | Google Cloud | Pay-per-token, enterprise |
| `agy` (Antigravity CLI) | ✅ Yes | Google One | Same as Gemini app — uses Pro quota |
| `google-gemini-cli` OAuth via Hermes | ✅ Yes (while it works) | Google One | Same — but with ban risk |

**Common mistake to avoid:** suggesting an API key as a "free" path for Pro subscribers. It is not free — it bills separately on top of the Pro sub. For Hermes work, the right framing is:
- Heavy Pro usage in Hermes → use `agy` subprocess (no extra cost, no ban risk)
- Light Hermes work where `agy` is overkill → AI Studio free tier (no extra cost, no ban risk)
- Heavy non-Pro work in Hermes → paid AI Studio key (extra cost, but separate from Pro sub)

## Hermes provider cache fixes (for any provider, not just google)

When the per-user model picker cache is stale or wrong, edit:

```
~/.hermes/provider_models_cache.json
```

Structure:
```json
{
  "<provider-name>": {
    "fp": "<upstream-api-fingerprint>",
    "at": <unix-timestamp>,
    "models": ["model-a", "model-b", ...]
  }
}
```

**Bump `at` to current time** when hand-editing. Leave `fp` alone unless you can compute the correct one — if Hermes detects a mismatch on next interactive refresh it will re-fetch from the provider.

**Do NOT edit `/usr/local/lib/hermes-agent/hermes_cli/models.py`** for tier-specific issues. The hardcoded fallback lists there often include **GA-channel-gated** models (e.g. `gemini-3.5-flash`) that 404 for free-tier OAuth but work for paid workspace accounts. Editing the shared file would break the picker for users on the other tier. The per-user cache is the right layer for tier-specific filtering.

To find which Python install `hermes` is using:
```bash
which hermes                    # path to wrapper
head -3 $(which hermes)         # shows the venv python it uses
$<venv-python> -c "import hermes_cli.models; print(hermes_cli.models.__file__)"
```

## Verification pattern for LLM response tests

**Weak test (don't rely on):** ask the model to echo a literal string. "Reply with exactly: PONG" — trivially satisfiable, can pass with a stub or a model that just parrots instructions. Session IDs prove the API was called but not that real reasoning happened.

**Strong test:** ask for a small computation or a fact with one right answer. Examples:
- Math: `"Compute 17 * 23 + 5 and answer with only the number."` → 396
- Capital: `"What is the capital of Bangladesh? One word."` → Dhaka
- Date reasoning: `"What day of the week was 2026-06-20?"` → Saturday

A correct answer proves the LLM ran end-to-end (auth, routing, tokenization, decoding all worked). An echo test only proves the request reached a model.

Also show **raw output** (not grep-filtered) so the user can see session IDs and any warnings — they want to verify, not just take your word.

## Antigravity CLI quick reference

```bash
# Verify installed
command -v agy && agy --version

# Auth (interactive — opens browser)
agy --prompt-interactive "test"

# One-shot prompt (most common in Hermes)
agy --print "Compute 17 * 23 + 5 and answer with only the number."

# Repo-aware
agy --add-dir /path/to/repo --print "Find auth bugs"

# Continue most recent
agy --continue

# Interactive session
agy -i "build a CLI for X"
```

In Hermes, drive these via the `terminal` tool (`pty=true` for interactive). The `agy-cli` skill is the operating manual.

For a native-feeling `/agy` slash command (no `terminal` tool calls, no subprocess noise in chat), use the **`agy-bridge` user plugin** at `~/.hermes/plugins/agy-bridge/`. The user plugin registers `/agy` as a first-class Hermes slash command. See `agy-cli` SKILL.md → "Slash command bridge" for the install recipe and the prefix-collision caveat with the `agy-cli` skill name.

## How to add a user plugin (do not use `hermes config set` or `hermes plugins enable`)

When creating a new user plugin, two pitfalls will silently break enablement:

1. **`hermes config set plugins.enabled '["a","b"]'` writes a JSON string, not a YAML list.** The loader checks `isinstance(enabled, list)` — a JSON string fails, so the plugin still shows "not enabled" in `hermes plugins list`. Edit `~/.hermes/config.yaml` directly and write a real YAML list:

   ```yaml
   plugins:
     enabled:
     - agy-bridge
     - other-plugin
   ```

2. **`hermes plugins enable <name>` replaces the entire enabled list** — it does not merge. Running it will wipe any other enabled plugins. Re-add them in the same edit (or use the YAML-list direct edit above).

Verify with `hermes plugins list` — the status column should read `enabled`, not `not enabled`. Test the plugin's handler in isolation by importing it as a Python module and calling the handler function directly (stub a `ctx` first); slash commands may not fire reliably in `hermes chat -Q -q` single-query mode.

## Sources

- github.com/google-gemini/gemini-cli/discussions/20632 — Google's official ToS statement
- github.com/NousResearch/hermes-agent/issues/29294 — Hermes-specific sunset announcement + Antigravity migration guidance
- github.com/google-gemini/gemini-cli/discussions/22970 — March 2026 service update + June 18 sunset
- discuss.ai.google.dev/t/urgent-mass-403-tos-bans-on-gemini-api-antigravity-for-open-source-cli-users-paid-tier/124508 — Feb 2026 mass ban report
- antigravity.google/docs/cli-install — official install instructions
- github.com/google-antigravity/antigravity-cli — official repo
- agentpedia.codes/blog/gemini-cli-to-antigravity-cli-migration — third-party migration walkthrough
