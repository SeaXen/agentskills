# Quillbase launch — sequencing plan

**Assumption:** "the 19th" = Monday, October 19, 2026 (nearest 19th after today, 3 days before your contract starts on the 22nd). If it's a different month, check the weekday — this plan leans on it being a normal US/EU business day. If it lands on a weekend, the whole HN/PH timing section below changes; flag that back to me.

## The one call that matters most

You listed "a Dev.to post" and "write up the architecture" as two separate items. **Merge them.** One long, genuinely technical Dev.to post about the storage layer *is* your Dev.to post. You don't have the hours to write two pieces of content — writing one well beats writing two adequately.

Second call: **the write-up is pre-launch work, not launch-day work.** Draft it now, this week, not on the 19th. If you're writing it from scratch during your 6 hours, cut something else — the write-up is your highest-leverage asset (it's what HN and Lobsters will actually engage with), so it can't be the thing you rush.

## Before the 19th (not counted in your 6 hours)

- **Write and get one outside pair of eyes on the architecture post.** A Rust-literate friend or a Discord acquaintance, not you re-reading your own draft.
- **Lobsters access — check this today.** It's invite-gated; if you don't have an account, you need an existing member to invite you, and approval isn't instant. Resolve it now or drop Lobsters from the list.
- **Confirm This Week in Rust's submission mechanism and cutoff** (PR against their GitHub repo; historically a weekly cutoff before their Tue/Wed issue). Verify the exact day so a Monday submission doesn't miss the window entirely.
- **Repo readiness gate:** a stranger should be able to `cargo add quillbase`, run the example, and get a working round-trip in under 5 minutes. This is what all the traffic converts on — fix this before fixing copy.
- **Pre-write everything:** HN title + Show HN text, r/rust text, r/programming text (different framing, not a copy-paste), LinkedIn post, one Twitter post. Writing under live-comment pressure on launch day wastes your scarce hours.
- **Schedule Product Hunt in advance** using their scheduling tool, so it goes live without consuming same-day attention.

## Launch day — 6 hours, run them 13:00–19:00 Paris time (07:00–13:00 ET)

This window is deliberate: it puts your HN post in the US morning while it's still your working afternoon.

| Time (Paris / ET) | Action |
|---|---|
| 13:00 / 07:00 | Final check: repo tagged, CI green, all text ready. No writing from scratch here. |
| 13:20 / 07:20 | Publish the architecture post on Dev.to. |
| 13:25 / 07:25 | Open the This Week in Rust PR, linking the post + repo. |
| 13:30 / 07:30 | Submit to Lobsters. |
| 13:50 / 07:50 | Submit **Show HN: Quillbase**. |
| 13:50–15:30 / 07:50–09:30 | Glued to HN only. Reply fast to every comment. This 100-minute block decides whether it survives to the front page — don't split it with anything else. |
| 15:30 / 09:30 | Post to r/rust (HN has had time to build its own momentum first). |
| 15:30–16:15 | Answer HN + start answering r/rust. |
| 16:15 | Post LinkedIn (2 minutes, opportunistic). |
| 16:30 | Post r/programming (staggered ~1h after r/rust to reduce "seen this already" overlap). |
| 16:30–18:30 | Keep answering all three threads. No new tasks. |
| 18:30 | Fire the one Twitter post, for the record. Zero expected return from 90 dormant followers — don't spend more than this on it. |
| 18:30–19:00 | Buffer: fix anything embarrassing raised in comments, thank people, write the maintenance-expectations note below. |

Product Hunt runs passively in the background on its scheduled slot — don't defend its rank live. With no audience to mobilize and no team for all-day PH engagement, it has the weakest expected return of everything on your list; scheduling it and walking away is the correct amount of effort.

## If time runs out, cut in this order

1. Twitter (already near-zero cost/return, nothing lost)
2. Product Hunt live engagement (keep the scheduled listing, drop the babysitting)
3. LinkedIn
4. r/programming
5. Lobsters
6. r/rust
7. This Week in Rust (cheap, durable, compounding — hard to justify cutting)
8. Hacker News (never cut — this is your best-fit channel for a novel Rust infra project with zero existing audience)
9. The architecture write-up itself (never cut — it's the thing everything else points to)

## The 22nd cliff

You go dark for contract work three days later. Before you stop, pin an issue or add a line to the README: launch traffic means bug reports and questions will keep arriving after you've gone quiet, and an unset expectation reads as an abandoned project one week in. One sentence — "actively maintained, slower responses week of Oct 19–26" — protects the credibility the launch just built.