# Launch plan — Quillbase (embedded vector store, Rust, MIT)

## Two things to confirm before this plan is valid at all

I have no visibility into repo state, so I can't score these — you have to, today, separately from the 6-hour launch-day budget:

1. **Name/license clearance (Step 1).** Has "Quillbase" had even a basic trademark/name-conflict check, and are the crates.io namespace, GitHub org, and any social handles already secured? This is normally an 8-week-lead-time item; you have ~3.5 weeks. That's tight but workable *if you do it now, this week* — a rename after the repo is visible is the one mistake on this whole list that can't be undone. Don't let launch-day planning distract from this.
2. **Readiness gate (Step 2 blockers).** Cold install on a clean machine, first working example inside whatever time budget your README promises, `SECURITY.md` with a monitored private contact, issues enabled. If any of these fail, the fix is "cut the claim" (e.g. drop an OS you haven't tested), not "push the date" — the date is locked. Do this check this week too, not on the 19th.

Neither of these eats into your 6 hours. They're pass/fail gates that happen before launch day exists.

## Verdict

**Go, with reduced scope.** Six hours cannot carry all nine items at real quality — HN alone (done properly) eats half the budget. Three items get cut from launch day itself, not because they're bad ideas, but because a parked "if there's time" item always becomes launch-morning scope. Cut cleanly now instead.

## Shape: single spike, not caravan

One story (a genuinely novel storage layer), one maintainer, one day. A caravan needs 3+ announceable items and a named owner per day — you have neither. Everything below fires once.

## Anchor: Hacker News, not Product Hunt

Product Hunt skews product/founder audiences; a dev tool with a novel technical decision gets better signal on an engineering aggregator, and PH's real value is a durable SEO page, not launch-day spike. HN gets full presence. PH still runs, but as cheap, low-touch secondary — see schedule.

If you don't already have an active Lobsters account (it's invite-only), drop it silently — a first post there from a fresh account reads as spam regardless of quality. If you do have one, it's a strong secondary given the systems/storage-engine story.

## The order, and why

Efficiency order for the channels you named, highest outcome per hour first:

**registry/repo hygiene → HN anchor → one staggered secondary (r/rust) → your own accounts → Dev.to (repurposed, not fresh) → This Week in Rust (already done, pre-launch) → [cut: Product Hunt gets a cheap slot, r/programming and the write-up are cut]**

Cuts, explicit, with reasons — not "later," actually deleted from this launch:

- **r/programming — cut.** Redundant reach: HN already covers general tech, r/rust already covers the exact target ecosystem. r/programming adds moderation/compliance risk (subreddit mods check post history; a first self-link there reads as spam) for marginal incremental reach. If you already post there regularly, swap it back in and drop something else instead — don't add it on top.
- **The architecture write-up — cut from launch day.** This is your best asset (durable, still gets readers a year out) and the one thing this ranking always starves — it costs a week you don't have, and you have zero hours after the 22nd. Don't write it "if there's time" on the 19th; that time won't appear. Two honest options: (a) if you find 2–3 hours *before* the 19th, outside this 6-hour count, write a short version purely to seed the HN comment and r/rust post with the real technical narrative — that's the highest-leverage use of any spare pre-launch hour you find; (b) if no such hours exist, skip it entirely for now and publish it properly whenever contract work frees real time again — a write-up doesn't need to ride the launch date, it just needs the launch to exist for it to link back to.
- **Product Hunt — kept, but demoted to near-zero effort.** Post it, drop a maker comment, don't staff it. It's not your audience for real feedback; its value is the page existing, not the launch-day thread.

## Hour-by-hour, Monday Oct 19, Europe/Paris time

Oct 19, 2026 is a Monday — workable, though PH's own Tue–Thu convention (folklore, not platform rule per the playbook) doesn't quite line up. Doesn't matter; your date is locked, and neither convention is a hard rule.

| Time (Paris) | Action |
|---|---|
| Morning, before 09:00 | Pre-flight, one last time: install command on a clean machine, every link in every draft resolves, main branch frozen, baseline metrics captured (stars, watchers, current downloads if any — you can't recover this after the fact). |
| 09:00 | **Row 1.** Tag the release, publish to crates.io, repo description/topics/social-preview image live. Minutes, but nothing else converts if this is broken. |
| 09:15 | Product Hunt goes live (≈9:01 Paris matches the 12:01 AM PT convention). Post the maker comment immediately. Then leave it — check back every hour or two, don't camp it. |
| 09:30–13:30 | Buffer. Glance at PH occasionally. This time is protected — don't let it bleed into launch prep. |
| 14:00 | **Anchor fires.** Show HN post goes live (~8am ET — solid US-morning overlap, still your working afternoon). Title: `Show HN: Quillbase – <plain description, no superlatives>`. |
| 14:01 | First comment, immediately, four moves: who you are and why you built it; the storage-layer decision and why you chose it over the obvious alternative (this is where the write-up's best material earns its keep even without the full article existing); what it doesn't do yet; invitation to ask about specifics. No marketing paragraph, no asking for anything. |
| 14:00–17:30 | **This is the day.** Stay in the thread continuously. Answer order: valid technical objections → misunderstandings → "why not X" (your highest-value question — name real alternatives honestly) → feature requests → hostility (one reply max, never the last word). Fix anything small that breaks and say so in the thread. |
| ~14:30 | One Twitter post, one LinkedIn post, back to back, both linking to the HN *discussion*, not restating it. Set expectations honestly: 90 unused followers won't move anything, but it's five minutes and free, so it stays in. |
| ~15:30 | Post to r/rust, context rewritten for that community specifically (lead with the technical decision, link at the end — not a pasted blurb). Read the sidebar and recent posts first if you haven't already. |
| ~16:30 | Dev.to post — reshape the HN first comment you already wrote into article format. This should cost 20–30 minutes, not a fresh write-up, because the words already exist. |
| 17:00–17:30 | Close out the HN thread backlog. Note every question asked twice — that's tomorrow's README edit. |

## This Week in Rust — do this now, not on the 19th

Submit a two-sentence blurb + link via PR to their repo *this week*. It's a weekly digest assembled days ahead; treat it as pre-launch prep that costs ten minutes, entirely outside the 6-hour launch-day budget, not a same-day task.

## What this buys and what it doesn't

Day 1 tells you if the story travelled (HN thread depth, r/rust reception). Day 7 tells you if anyone tried it (unique cloners, crates.io downloads — not stars). Day 30 tells you if it stuck (issues from people who read the code, not just starred it). If stars spike and downloads/cloners don't move, the announcement travelled and the project didn't — that's a positioning problem for next time, not a channel problem, so don't relaunch anywhere on the strength of day-1 numbers alone.

One more thing worth saying plainly: you're solo, with a hard wall on the 22nd. If the HN thread is still active when your contract starts, you will not be able to keep answering it. Say that nowhere in the thread itself, but do triage the biggest open questions before end of day on the 19th, and don't start anything on the 20th–21st you can't finish.