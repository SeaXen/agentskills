# `session_reset.mode: none` is bypassed by `resume_pending_expired` — misleading notification

## What the user sees

User's `~/.hermes/config.yaml` has:

```yaml
session_reset:
  at_hour: 4
  idle_minutes: 1440
  mode: none
```

Despite `mode: none`, the user periodically receives a Discord notification reading:

> ◐ Session automatically reset (inactive for 24h).
> Conversation history cleared.
> Use /resume to browse and restore a previous session.
> Adjust reset timing in config.yaml under session_reset.

The "inactive for 24h" message is **misleading** — the user was not inactive for 24 hours. Their session was reset because of an unrelated gateway event.

## Root cause: two code paths can reset a session

**Path A — policy-driven reset** (controlled by `session_reset.mode`):

- `gateway/session.py:1575` `_should_reset()` checks `policy.mode`
- If `mode == "none"`, returns `None` immediately — no reset
- This is what the user expects

**Path B — `resume_pending_expired`** (bypasses `mode`):

- `gateway/session.py:1791` after `_should_reset()` returns `None`:
  ```python
  elif entry.resume_pending:
      reset_reason = self._should_reset(entry, source)
      if not reset_reason:
          _fw = auto_continue_freshness_window()
          if _fw > 0 and (now - _ref_time).total_seconds() > _fw:
              reset_reason = "resume_pending_expired"
  ```
- This fires when a previous gateway restart marked the session as `resume_pending`, but `auto_continue_freshness_window` (default 3600s = 1h) elapsed without a successful recovery turn. The session is treated as a zombie and reset.

**Trigger sequence:**
1. User's session is active.
2. Gateway restarts (any reason: OOM, manual restart, hermes update, memory pressure).
3. On restart, Hermes marks the active session as `resume_pending` so its transcript reloads intact.
4. User doesn't send a new message within `auto_continue_freshness_window` (1h).
5. Next time anything touches that session, it falls through to `resume_pending_expired` → `was_auto_reset = True`.

## Why the message text is misleading

`gateway/run.py:10740` builds the user-facing notice:

```python
if reset_reason == "suspended":
    reason_text = "previous session was stopped or interrupted"
elif reset_reason == "daily":
    reason_text = f"daily schedule at {policy.at_hour}:00"
else:  # <-- resume_pending_expired falls here
    hours = policy.idle_minutes // 60  # 1440 / 60 = 24
    reason_text = f"inactive for {duration}"  # "inactive for 24h"
```

There is no `elif reset_reason == "resume_pending_expired":` branch. The code computes the duration from `policy.idle_minutes` (which is 1440 = 24h) and labels it as "inactive for 24h". But the actual trigger was a gateway restart, not 24h of inactivity.

## Diagnosis recipe (when the user complains)

1. Confirm `session_reset.mode: none` is in their `~/.hermes/config.yaml`.
2. Check `~/.hermes/sessions/sessions.json` for the affected session key. Look for:
   ```python
   python3 -c 'import json; d=json.load(open("/root/.hermes/sessions/sessions.json"));
   for k,v in d.items():
     if isinstance(v,dict) and v.get("was_auto_reset"):
       print(k, v.get("auto_reset_reason"), v.get("last_active_at"))'
   ```
3. Cross-reference `~/.hermes/logs/gateway.log` for recent restarts (look for `Gateway stopped`, `Launched systemd planned-restart`, `Shutdown`).
4. The session's `last_active_at` is typically minutes/hours before the reset, not 24h before — that proves it was `resume_pending_expired`, not real idle expiry.

## User-facing explanation (Bangla-English bilingual, since Dr. Sagar prefers)

> `mode: none` ঠিকই কাজ করছে। কিন্তু Hermes-এর একটা bug আছে: session gateway restart-এর পর `resume_pending` mark হয়, freshness window (default 1h) পেরিয়ে গেলে `resume_pending_expired` trigger হয় — `mode: none` ignore করে। Message text misleading কারণ code `policy.idle_minutes` (1440 = 24h) ধরে "inactive for 24h" বানায়, যদিও actual কারণ gateway restart, 24h inactivity না।

## Three options for the user

### Option A — keep `mode: none`, accept the occasional misleading message

This is what most users do. The reset itself is harmless — clearing stale context is often desirable. Only the **text** of the message is wrong.

### Option B — extend the freshness window so resume_pending doesn't expire

In `~/.hermes/config.yaml`:

```yaml
agent:
  gateway_auto_continue_freshness: 86400   # 24h instead of default 1h
```

This means a session stays resume-eligible for 24h after a gateway restart, so the next message within 24h will reload the transcript intact. Trade-off: a truly zombie session takes longer to be cleaned up.

### Option C — file an upstream issue

The cleanest fix is to add a `resume_pending_expired` branch to `gateway/run.py:10740` so the message text reflects the actual cause. Draft text lives in `references/upstream-issue-draft.md`.

## Verified on

- `hermes-agent` 0.18.1 (gateway/run.py lines 10699-10762, gateway/session.py lines 1575-1814)
- 2026-07-08: user noticed Discord message reading "inactive for 24h" while actively chatting hours ago. Investigation confirmed gateway restart had happened ~5h prior; session was resume_pending; freshness window was 1h default.
