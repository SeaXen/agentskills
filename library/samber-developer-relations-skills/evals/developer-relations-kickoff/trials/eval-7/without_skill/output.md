Here's the community health dashboard for Norbury Systems' Discord, built for a VP audience and structured so it survives contact with a board meeting.

## Bottom line

🟠 **Early and thin, not broken.** Five weeks old, 118 members, organic volume very low. That's normal for week 5 — most communities don't show real signal until week 12+. The number that actually matters for the board isn't message count, it's **how many distinct people are posting**, and that's the one figure Norbury doesn't have yet. Fix that gap before the deck, or the whole dashboard is a guess dressed as data.

## Baseline snapshot — Week 5 (as of 2026-09-19)

| Metric | Value | Status | Why it matters |
|---|---|---|---|
| Total members | 118 | — | Vanity number for the board slide, not a health signal on its own |
| Messages/day, best day observed | ~20 | 🟠 | Ceiling, not average — need the actual daily distribution |
| Staff share of best-day volume | 3/20 = 15% | 🟢 | Under the 30% warning line — staff isn't the one propping up the room |
| Organic messages/day (best day) | ~17 | 🟠 | 17 ÷ 118 members = 0.14 msg/member/day, on the *good* day |
| Unique weekly active posters | **unknown** | 🔴 | Not yet tracked — see "Fix this first" below |
| 7-day retention of new joiners | **unknown** | 🔴 | Not yet tracked |
| Monthly active ratio (target >20%) | **unknown** | 🔴 | Not yet tracked |
| Unanswered questions rate | **unknown** | 🔴 | Not yet tracked |

Everything marked 🔴 isn't "bad" — it's **not measured yet**. That's the actual gap between now and a credible board slide.

## Fix this first: unique active posters, not message count

20 messages from 3 people and 20 messages from 15 people look identical in a raw count, and mean completely different things. Message-per-member ratios collapse to noise unless you also track:

- **Weekly Unique Authors (WUA)** — distinct member IDs who sent ≥1 message this week, excluding staff role
- **Repeat-poster rate** — WUA who also posted the prior week ÷ WUA this week (this is your real retention signal at 5 weeks old, before "7-day join retention" has enough volume to mean anything)

Pull this from Discord's **Server Insights** (Server Settings → Community → Insights, if Community mode is enabled) or a free bot (Statbot, Carl-bot analytics) — do this today, not the week before the deck, so you have at least 2 real weekly data points by the 2026-10-03 deadline.

## Metric definitions (so this dashboard survives you handing it off)

| Metric | Formula | Source |
|---|---|---|
| Weekly Unique Authors (WUA) | COUNT(DISTINCT author_id) WHERE role != staff, in trailing 7 days | Statbot / audit log export |
| Staff share | staff messages ÷ total messages, trailing 7 days | Tag a "Staff" role, filter by it |
| Organic msg/member/day | (total msgs − staff msgs) ÷ member_count ÷ 7 | Derived |
| Monthly Active Ratio | WUA (30-day) ÷ total members | Derived |
| New-member 7-day retention | joined_28+_days_ago AND posted_in_first_7_days ÷ joined_28+_days_ago | Requires join-date + first-message timestamp join |
| Unanswered question rate | questions in #help with 0 non-staff replies ÷ total questions, trailing 7 days | Manual tag or Ticket Tool |
| Response time (support) | median(first_reply_time − question_posted_time) | Ticket Tool / manual sample |

## Weekly tracking table — reuse this every reporting cycle

| Week | Dates | Members (EOW) | Net new joins | Msgs/day (avg) | Staff share | WUA | MAR |
|---|---|---|---|---|---|---|---|
| W1 | Aug 15–21 | — | — | — | — | — | — |
| W2 | Aug 22–28 | — | — | — | — | — | — |
| W3 | Aug 29–Sep 4 | — | — | — | — | — | — |
| W4 | Sep 5–11 | — | — | — | — | — | — |
| W5 | Sep 12–18 | 118 | — | ~20 (best day) | ~15% | — | — |
| W6 | Sep 19–25 | *(fill live)* | | | | | |
| W7 | Sep 26–Oct 2 | *(fill live, this is the deck week)* | | | | | |

Backfill W1–W4 from Discord's audit log export if Community mode was on from day one; if not, say so on the slide rather than inventing numbers — a board that catches one fabricated cell distrusts the whole table.

## 2-week action plan (moves the metrics, not just reports them)

1. **Today**: enable Server Insights / install Statbot, tag a Staff role, start logging WUA daily.
2. **This week**: run 3 scheduled prompts (Mon goals, Wed hot-take, Fri show-and-tell) — cheap way to lift organic message count without staff carrying it.
3. **This week**: DM 10 quiet members individually with one specific question each — direct outreach converts lurkers to WUA faster than public prompts at this size.
4. **Week 2**: one 20-minute office-hours or AMA — gives a WUA spike and a genuine "engagement event" line for the deck.
5. **Before the deck**: pull real W6/W7 numbers — two consecutive weeks of *actual* WUA trend beats one static snapshot every time in front of a VP.

## How to present it on the slide

One headline number (WUA trend, 2 weeks minimum), one context line ("5 weeks old — communities typically inflect at 90 days"), and the RAG table above, collapsed to 5 rows max. Skip the raw member count as the hero metric — 118 members with 4 active posters reads worse to a sharp VP than 60 members with 20 active posters. Lead with the ratio, not the vanity total.