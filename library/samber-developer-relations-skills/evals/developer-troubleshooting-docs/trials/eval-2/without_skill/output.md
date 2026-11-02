## Writing order

**1. WAL exhaustion runbook (`could not extend file`, dedicated clusters) — 14 tickets**

Lowest volume on the list, but the only item priced in engineer-days, not support-minutes: 2–3 days per case × 14 = roughly 5–7 weeks of engineering time across two quarters. One of those cases already got a formal incident review for a contract customer — that's renewal/SLA risk, not just a slow ticket. The postmortem already exists, so this is mostly a reformat, not new research: pull the root-cause and remediation steps into (a) an internal runbook so the next engineer isn't re-deriving the fix from scratch, and (b) a short customer-facing "monitor WAL growth on dedicated clusters" guide aimed at prevention. Ships fast, saves the most.

**2. Connection & pool errors — 202 tickets combined**

- `FATAL: remaining connection slots are reserved` (84)
- `could not connect to server: Connection refused` (61)
- `connection to server failed: Connection refused` (57)

The last two are the same root cause (wrong port) in two client-version wordings — write one article, index both exact error strings so search/AI-answer hits either. Bundle all three into a single "connecting to your branch" troubleshooting doc rather than three separate pages; they're all first-contact connectivity issues a self-serve reader will hit in the same session. 202 tickets is 59% of the 340 you tallied — biggest single dent in ticket count, cheapest to write, ships in under a day. Do this right after #1 as the proof-of-value quick win.

**3. Branch creation hang at signup — 22 tickets**

Don't rank this by ticket count — rank it by the fact that half your affected signups never come back. That's an activation-funnel leak, not a support cost. Two deliverables, not one:
- A support-facing triage guide so the 35-minute investigation drops to minutes (recognize the symptom, apply the known workaround if one exists, escalate correctly).
- A flag to engineering that this is a P0 activation bug — a doc can shorten the pain, it can't stop something that "hangs forever." Say that explicitly when you hand this off; don't let a KB article read as "solved."

**4. Account suspended for non-payment — 9 tickets**

Cheap filler between bigger docs: a short FAQ plus a rewrite of the generic error message copy itself (that's a one-paragraph ask to whoever owns that string). Low volume, near-zero effort, do it opportunistically.

## Don't write

**`permission denied for schema public` — 11 tickets.** Grants change in 5.0 next month and the error disappears. Writing a full article now is dead weight in ~30 days. At most, a one-line dated notice ("fixed in 5.0") — don't spend real writer time here.

**`panic: send on closed channel` during failover — 7 tickets.** All clustered in the two weeks right after 4.6 shipped, nothing since — reads like a regression that's already been patched. Confirm with engineering before writing anything: if it's fixed, there's nothing customer-facing to document (it's an internal crash, not user-actionable); if it's not fixed, this is an engineering ticket, not a writing one.

## Why this order, not ticket count

Raw ticket volume (84 > 61 > 57 > 22 > 14 > 11 > 9 > 7) would put the WAL and signup-hang issues near the bottom. That's the wrong ranking: 14 WAL tickets cost more engineer-hours than the top three connection issues combined by roughly an order of magnitude, and the signup hang is bleeding customers, not just support time. Sequence by cost and risk avoided, use ticket count as the tiebreaker, and treat "will this problem still exist when the doc ships" (schema public, the 4.6 panic) as a hard filter before anything else.