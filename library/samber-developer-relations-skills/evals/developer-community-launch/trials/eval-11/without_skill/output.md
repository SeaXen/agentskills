## Recommendation: skip the community. Run a paid-zero advisory loop instead.

**The ask.** You want ~10 usable roadmap signals a month. That's a research output, not a community output. Don't build infrastructure to solve a research problem.

---

### Why a community fails your own test

Two standard readiness signals, both failing:

| Signal | Threshold | Tenvale |
|---|---|---|
| Repeat support volume (shared-FAQ potential) | Recurring questions at volume | 5 tickets/month, **zero repeats** |
| Organic peer-to-peer support | Users already answering users, unprompted | **Never observed, ever** |

Zero repeat tickets means there's no shared knowledge base trying to form. Zero peer-to-peer answers, ever, means there's no latent helping behavior waiting to be unlocked — a channel doesn't create that behavior, it just gives it an empty room to not happen in. 35 named users is also thin for a space that needs to look alive daily; most community benchmarks assume low hundreds of active participants before a channel self-sustains.

A dead server is worse than no server — it's a visible signal to prospects and press that adoption stalled. And the Rust ecosystem Discord already owns this problem space, with some of your own users already in it. Building a competing space fragments the one place your users already gather, for no gain.

Verdict: this isn't "not ready yet, revisit in 6 months." It's the wrong tool for the goal you actually stated.

---

### What to do instead: a rotating advisory conversation, run by Nils, inside his existing 4 hrs/week

No channel, no moderation, no CoC, no ongoing tax. Just structured outreach to the 35 named users, cycled monthly.

1. **Roster.** Keep the 35 names in a simple sheet: last contacted, role, product surface they touch most.
2. **Monthly cadence.** Nils reaches out to 8–10 of them (rotating, so everyone gets touched roughly every 4 months) for a 20–30 min conversation — call or async written thread, whichever they prefer.
3. **What he asks.** Not "any feedback?" — that's how you get nothing usable. Anchor on: *what's the last thing you hit that our static analysis should've caught and didn't* / *what are you doing manually that you wish the tool did* / *what almost made you stop using it*. That's a pain-point and trigger-event extraction, not a chat.
4. **Signal log.** Every conversation gets logged in a lightweight doc/GitHub Discussion: signal, user, date, what it implies for roadmap, rough priority. This is the artifact you bring back to exec, not "trust me, we talked to people."
5. **Passive listening, for free.** Nils already has an account in the Rust Discord. He participates there as himself — answering the odd static-analysis question when relevant, not as "Tenvale rep." That's goodwill plus a second signal source, at zero marginal cost, without owning or competing with the space.

### The math

- 8–10 structured conversations/month, each running ~1–2 usable signals (standard yield for anchored JTBD-style interviews) → **10–14 signals/month**. Target met.
- Time cost: 10 conversations × 30 min (~5 hrs) + prep/notes (~1.5 hrs) + monthly synthesis (~2 hrs) + Discord listening (~2 hrs) ≈ **10–11 hrs/month**, against a 16–17 hr/month budget. Slack left over for deep-dives on whatever surfaces.
- Dollar cost: **$0.** No platform, no swag, no bot, no bounty.

### Why this beats "a cheap Discord" specifically

A community's cost doesn't stop at setup — it's a standing tax: someone has to post to avoid the ghost-town look, someone has to handle the inevitable spam/troll, someone has to keep it from visibly dying in front of the 35 people you invited. That tax runs whether or not it produces signal. The advisory loop has no standing cost — it scales exactly with hours actually spent talking to users, and it stops with zero wind-down cost the moment it's not worth it.

### When to revisit

Not on a calendar — on evidence. Reopen the community question if either underlying signal flips:

- Support tickets start repeating (a real shared knowledge base is forming, worth capturing publicly).
- Someone is spotted answering another user's question about Tenvale unprompted, anywhere (Discord, GitHub, Reddit) — that's the actual fuel a community runs on, not a hope that inviting people will produce it.

Until then, this gets you the product-direction outcome you actually asked for, at zero budget, inside time you already have.