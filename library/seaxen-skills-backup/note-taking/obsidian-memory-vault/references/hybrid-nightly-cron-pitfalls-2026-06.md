# Hybrid Nightly Cron — Pitfalls & Verification (2026-06 addendum)

Addendum to `references/hybrid-nightly-high-signal-cron.md`.
Captures the two real pitfalls hit when implementing the
`obsidian-nightly-high-signal-log` job, plus a verified working pattern.

## Pitfall 1: per-job `provider:` override is ignored in agent-mode cron

**Symptom:** cron job with `no_agent: false`, `model: openrouter/owl-alpha`,
`provider: openrouter` fails with:

```
RuntimeError: No LLM provider configured. Run `hermes model` to select a provider, or run `hermes setup` for first-time configuration.
```

**Root cause:** the cron runner does not apply the per-job `provider`/`model`
fields when it spawns the agent after the script runs. It falls back to the
default config's `provider:` (e.g. `nous`) and cannot initialize a working LLM
in the cron execution context.

**Fix:** use `no_agent: true` and do the LLM call from inside the script via
direct HTTP. Avoid relying on per-job provider overrides entirely for cron
jobs.

## Pitfall 2: `no_agent: true` scripts do NOT get env vars injected

**Symptom:** after switching to `no_agent: true`, the OpenRouter call returns:

```
ERROR: HTTP 401: {"error":{"message":"Missing Authentication header","code":401}}
```

**Root cause:** the cron runner does not inject `OPENROUTER_API_KEY` (or any
other secret) into the script's environment. The script must load the key
itself.

**Fix:** 3-tier key loading fallback. See the canonical pattern in
`openrouter_free_watch.py` (`~/.hermes/scripts/openrouter_free_watch.py`):

```python
ENV_PATHS = [Path('/root/.hermes/.env'), Path('/mnt/tb/hermes/.env')]
BWS_SECRET_ID_OPENROUTER = 'f6ee6e99-3f56-410a-8a19-b4590070c320'

def _get_bws_key(secret_id: str) -> str:
    try:
        result = subprocess.run(
            ['bws', 'secret', 'get', secret_id],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0:
            return json.loads(result.stdout).get('value', '').strip()
    except Exception:
        pass
    return ''

def load_openrouter_key() -> str:
    key = _get_bws_key(BWS_SECRET_ID_OPENROUTER)
    if key:
        return key
    key = os.environ.get('OPENROUTER_API_KEY', '').strip()
    if key:
        return key
    for path in ENV_PATHS:
        if path.exists():
            for line in path.read_text().splitlines():
                if line.startswith('OPENROUTER_API_KEY=***                    return line.split('=', 1)[1].strip()
    return ''
```

Resolution order: **bws CLI → env var → .env file**.

## Verified working shape

| Field | Value |
|---|---|
| `no_agent` | `true` |
| `script` | `obsidian_nightly_hybrid_full.py` |
| `enabled_toolsets` | `[]` |
| `model` / `provider` | not set (script handles it) |
| `deliver` | `discord:1510852262329585685` |

After the fix, scheduled 23:55 run shows `last_status: ok`,
`last_error: None`, `last_run_at: <today> 23:55:<n>`.

## Debug tip: how to confirm the key actually loaded

Add to the HTTP error branch:

```python
except urllib.error.HTTPError as e:
    body = e.read().decode()
    return f"ERROR: HTTP {e.code}: {body} | key_len={len(OPENROUTER_API_KEY)} | key_start={OPENROUTER_API_KEY[:10] if OPENROUTER_API_KEY else 'EMPTY'}"
```

If `key_len=0` → key loading failed (bws not on PATH, .env not readable,
or wrong secret ID).
If `key_len>0` and you still get 401 → the key itself is invalid, not
the header.

## Pitfall 3: single-model cron calls fail on quota, blackout, or 429

**Symptom:** the nightly cron fails with
`RuntimeError: HTTP 429: The usage limit has been reached` even though
the key is valid and the script is otherwise working.

**Root cause:** the cron script calls a single model (e.g.
`openrouter/owl-alpha`) with no fallback. A single transient
quota / 429 / 5xx from that model fails the whole job.

**Fix:** multi-model fallback list with 2 attempts per model and
exponential backoff. Each model in the list should be a different
provider family so a single provider's outage does not black out
the whole cron.

```python
# Primary first, then free-tier fallbacks in order.
OPENROUTER_MODELS = [
    os.environ.get("OPENROUTER_MODEL", "openrouter/owl-alpha").strip(),
    "qwen/qwen-2.5-72b-instruct:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "google/gemini-2.0-flash-exp:free",
]

def _call_openrouter_once(model, system, user, *, max_tokens=800, timeout=60):
    """Single call. Returns content on success, 'ERROR: ...' on failure."""

def call_openrouter(collector_context):
    # ...build prompts...
    attempts_per_model = 2
    backoffs = [2, 5, 10]  # seconds
    last_error = ""
    for model in OPENROUTER_MODELS:
        if not model:
            continue
        for attempt in range(1, attempts_per_model + 1):
            out = _call_openrouter_once(model, system_prompt, user_prompt)
            if not out.startswith("ERROR:"):
                return out
            last_error = out
            # 401/403/400 = same key rejected on every model — do not waste budget
            if "HTTP 401" in out or "HTTP 403" in out or "HTTP 400" in out:
                break
            if attempt < attempts_per_model:
                time.sleep(backoffs[min(attempt - 1, len(backoffs) - 1)])
    return f"ERROR: all models failed. last: {last_error}"
```

Why **skip on 401/403/400**: the script uses a single OpenRouter key
across all models. A 401/403/400 means the key is rejected or
malformed — trying the next model with the same key produces the
same error and burns the attempt budget. 429 and 5xx, by contrast,
are per-model and worth retrying against a different model.

Why **2 attempts per model**: one shot is not enough for transient
blips, 3+ wastes budget on a dead model. Two + backoff covers the
common case.

Why **2/5/10s backoff**: short first retry for a quick win, longer
for harder failures. Do not go above 10s in a cron — the scheduler
will kill the job if it overruns.

If you want this to be a 10/10 reliable cron, this is the layer that
gets you there. A single-model cron is at the mercy of one provider.

## Pitfall 4: `sessions.json` includes non-dict values (`_README`)

**Symptom:** `no_agent: true` script fails with `Script exited with code 1`
before any OpenRouter output:

```
AttributeError: 'str' object has no attribute 'get'
  File ".../obsidian_nightly_hybrid_full.py", line 213, in collect_sessions
    updated = parse_iso(meta.get("updated_at"))
```

This is **not** Pitfall 1 (no provider) and **not** Pitfall 3 (429). The
collector dies while building context; `Daily/YYYY-MM-DD.md` is never written.

**Root cause:** `~/.hermes/sessions/sessions.json` maps session keys to dicts
but also includes a string `_README` (gateway routing index text). Code that
assumes every value is a session object crashes on that key.

**Fix:**

```python
for meta in data.values():
    if not isinstance(meta, dict):
        continue
    updated = parse_iso(meta.get("updated_at"))
```

Use the same guard in backfill scripts that iterate `sessions.json`.

**Recovery when a night is lost:** (1) reconstruct or write
`Daily/YYYY-MM-DD.md` from the 24h window; (2) add `[[YYYY-MM-DD]]` to
`AGENT.md` Daily Note Index in the same pass; (3) re-run
`python3 ~/.hermes/scripts/obsidian_nightly_hybrid_full.py` to confirm exit 0.

**Triage cheat sheet** (read `last_error` before blaming AI quota):

| Error fragment | Layer | See |
|---|---|---|
| `No LLM provider configured` | agent-mode cron | Pitfall 1 |
| `Missing Authentication header` / HTTP 401 | key load in script | Pitfall 2 |
| `HTTP 429` / usage limit | OpenRouter quota | Pitfall 3 |
| `'str' object has no attribute 'get'` | sessions collector | Pitfall 4 |
| `HTTP 404 from <model>` / `No endpoints found` | OpenRouter model retired | Pitfall 5 |

## Pitfall 5 — OpenRouter free models get retired; `openrouter/free` is the durable fix (v3, 2026-09-02)

**Symptom:** nightly cron `last_error: all models failed. last: ERROR:
HTTP 404 from <model>`. Hardcoded `:free` model list keeps rotting.

**Why hardcoded lists rot:** OpenRouter's free tier is a marketing funnel
for paid usage. Models are added and rotated weekly. Hardcoded names
from 2026-06 (`owl-alpha`, `qwen-2.5-72b:free`, `llama-3.3-70b:free`,
`gemini-2.0-flash-exp:free`) all gone by 2026-09; hardcoded names from
2026-07 (`openai/gpt-oss-120b:free`, `google/gemma-4-31b-it:free`,
`qwen/qwen3-next-80b-a3b-instruct:free`) also gone by 2026-09.

**Fix (2026-09-02):** Use **`openrouter/free`** as the single primary.
It is OpenRouter's catch-all alias that routes each request to a
currently-available free model. Probed 5 calls in a row → 4 distinct
backends (`nemotron-3.5-content-safety:free`, `poolside/laguna-s-2.1:free`,
`nemotron-3-nano-omni-30b-a3b-reasoning:free`, `inclusionai/ling-3.0-flash-fin:free`).
OpenRouter's own routing keeps the list fresh for us.

```python
# Single entry. No fallback list. openrouter/free self-rotates.
OPENROUTER_MODELS = [
    os.environ.get("OPENROUTER_MODEL", "openrouter/free").strip(),
]
```

**Two gotchas that come with `openrouter/free`:**

1. **Reasoning models return empty `content` + populated `reasoning`.**
   `_call_openrouter_once` must fall back to the `reasoning` field or
   the parser will see an empty response and the script will skip the
   night silently.

2. **The bullet parser was over-matching LLM thinking text.**
   `extract_writes()` was matching any line containing "decision" or
   "fix" anywhere — including inside the LLM's reasoning paragraph —
   and writing fake decisions to `Memory/decisions.md` for every
   successful run. Parser now only accepts bullets **under a
   `## Log` / `## Decisions` / `## Fixes` section header** that
   starts a section, and ignores everything before the first
   `## Header`.

3. **404 / 401 / 403 still skip-immediately** to avoid burning the
   2-attempt budget on dead endpoints. Same code as before.

**Tradeoff:** `openrouter/free` is non-deterministic (style, latency,
and instruction-following vary with the routed backend). For
reproducible runs, set `OPENROUTER_MODEL` env var to a specific model
you have paid access to, or accept the rotation.

**Refresh procedure when this fires again** (rare — only if
`openrouter/free` itself disappears):
1. `curl -s -H "Authorization: Bearer $(bws secret get <id>)" https://openrouter.ai/api/v1/models | jq -r '.data[].id' | grep ':free$'`
2. Pick 3-4 confirmed-OK models from the probe script
   (`probe_openrouter_free_models.py`).
3. If even `openrouter/free` returns 404, fall back to the explicit
   list as a temporary stop-gap.

## Companion: the recall feedback API

The `obsidian-auto-recall` plugin should also call
`submit_recall_feedback(vote, query, result)` after every turn
where vault notes were surfaced. The dashboard's
`get_recall_feedback_adjustments()` reads from the `recall_feedback`
table and nudges ranking on the next identical-shape query. Without
real agent feedback submissions, the table is empty and the ranking
adjustment is always zero. The plugin helper is:

```python
from hermes_plugins.obsidian_auto_recall import submit_recall_feedback
submit_recall_feedback("up",   user_query, result)   # result contributed to answer
submit_recall_feedback("down", user_query, result)   # off-topic, stale, contradicted
```

Submission is best-effort, never blocks the turn, silently no-ops on
network failure. See `references/dashboard-redesign-and-auto-recall.md`
for the bridge architecture and the `Mnemosyne ↔ Obsidian Vault
Cross-link` reference for the wiring example.
