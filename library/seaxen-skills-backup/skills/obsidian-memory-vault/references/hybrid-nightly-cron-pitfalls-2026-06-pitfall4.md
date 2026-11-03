# Hybrid Nightly Cron — Pitfall 4 (2026-06-17 addendum)

Addendum to `references/hybrid-nightly-cron-pitfalls-2026-06.md`. Captures
the actual root cause of the 2026-06-17 `obsidian-nightly-high-signal-log`
failure despite the existing 4-model fallback.

## Pitfall 4: free-tier OpenRouter models share a quota pool

**Symptom:** the nightly cron failed with
`RuntimeError: HTTP 429: The usage limit has been reached` even though
the cron has the 4-model fallback from Pitfall 3 (1 paid model + 3
free models).

**Root cause:** `openrouter/qwen-2.5-72b-instruct:free`,
`openrouter/llama-3.3-70b-instruct:free`, and
`openrouter/gemini-2.0-flash-exp:free` are all on OpenRouter's
**shared free-tier quota pool**. When that pool is exhausted (peak
hours, or after a long paid-model session), **all three return 429
simultaneously**. Pitfall 3's per-model skip-on-401/403/400 fires
but cannot pivot **between free-tier models** because they share
the same bucket. The `owl-alpha` paid model is unaffected in theory,
but if it also 429s (daily rate cap, account quota), the cron fails.

## Real fix shape (use this for a true 10/10 cron)

1. **Add 429 to the skip-on-auth-error list only when the next model is
   in a different provider tier.** If `owl-alpha` 429s, DO retry the
   free-tier models — they have separate per-minute limits and may
   recover within seconds. If `qwen-...:free` 429s, skip the other
   free models in the same pool and fall through to the next paid
   model in the list (e.g. `anthropic/claude-3.5-haiku`).

2. **Treat "all models 429" as recoverable.** Sleep for the smallest
   remaining backoff (or 30s), then retry once. If it still 429s,
   emit a short `RATE_LIMITED` sentinel line to stdout. Let
   `no_agent: true` cron treat that as `last_status: ok` (silent) —
   the next cron in 24h usually clears.

3. **Best model list shape for Dr. Sagar's setup:** one paid model
   first + at most TWO free models in the same pool (more free
   models in one pool = no marginal coverage):

   ```python
   OPENROUTER_MODELS = [
       os.environ.get("OPENROUTER_MODEL", "openrouter/owl-alpha").strip(),
       "qwen/qwen-2.5-72b-instruct:free",          # free-tier quota
       "meta-llama/llama-3.3-70b-instruct:free",    # free-tier (same bucket)
       "anthropic/claude-3.5-haiku",               # paid, different provider, last-resort
   ]
   ```

4. **If the user only wants distillation when free quota is available,**
   accept 429 as a known failure mode and let the cron emit a compact
   "Rate-limited, will retry next cycle" line. Do NOT silently retry
   inside the cron — burn rate hits all subsequent crons too.

## Diagnostic probe after a 429 cron failure

```bash
# Check the cron job output for "all models failed" vs a specific model
grep -E 'HTTP 429|all models failed|attempt' /var/log/hermes-cron/<job_id>.log
# If you see "all models failed. last: ... HTTP 429" on every model,
# it's a tier-wide outage, not a single-model blip.
```

## The framing question to ask the user: "without AI, is this not doable or good?"

- **Distillation / summarization / signal ranking** → AI is required;
  cron is correct shape.
- **Raw change collection** (which notes changed, file diffs, activity
  log) → no AI needed; switch the cron to a `no_agent: true` script
  that scans `git log` / `mtime` deltas and posts directly. Faster,
  zero-quota, deterministic.

For Dr. Sagar's `obsidian-nightly-high-signal-log`, the AI path is
correct because the whole point of "high-signal log" is to **distill**,
not just collect. Keep AI, but accept that on peak days the cron may
emit a `RATE_LIMITED` sentinel and the next night will catch up.
