# OmniRoute Combos: Strategy Selection + Account Pooling

## Goal: many equal-quota accounts should behave like one pooled source
Use:
- one provider/model target
- dynamic account selection
- `PRIORITY` strategy

This gives sticky usage on one account until quota/error, then automatic failover to the next account.

## What the user will see in analytics
- One account may show nearly all token usage for a while
- Other equal-quota accounts may look unused
- This does **not** mean failover is broken
- Rotation usually happens only after quota/rate/error pressure, not evenly per request

## Mid-session switching
OmniRoute can fail over to a different account in the middle of an ongoing client session if the active account hits quota/errors. The client still talks to the same combo/model name.

## When FUSION is the wrong choice
If the user says:
- "I want all 10 accounts to act like one"
- "I just want to use all quota across all accounts"
- "all accounts have same quota"

Then `FUSION` is usually the wrong fit. Prefer `PRIORITY`.

## Health warnings explained
### Quota nearly exhausted
The active provider/account is running low. Add fallbacks or wait for reset.

### Traffic distribution is highly skewed
Expected when:
- combo has only 1 model, or
- dynamic account selection is sticky and one account is carrying traffic

## Cost caveat
Subscription-backed providers can still show estimated per-token cost in OmniRoute analytics. That estimate may be wrong even when actual billing is flat-rate / effectively $0 per token.
