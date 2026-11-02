# Orbwright Slack community — launch plan

## ⚠️ Structural risk to fix before anything else

You said the big driver is people googling error strings and landing nowhere. **Slack doesn't fix that.** Slack workspaces aren't crawlable by Google — even a perfectly active community leaves zero footprint in search. Also check your plan tier: Slack's free tier drops message history after 90 days, which directly contradicts "answers stay correct for a year" — a great pinned answer becomes invisible three months later unless it's paid-tier or preserved outside plain chat history.

Two fixes, both cheap:
- **Preserve durable answers in Slack Canvas or pinned bookmarks**, not chat history. Canvas content survives regardless of plan/history limits and is the closest thing Slack has to a wiki page — a good match for answers with a 1-year+ shelf life.
- **Mirror resolved threads to something Google indexes.** You already have GitHub issues where 4 users answer each other — that's public and indexed today. Plan a recurring task (fits inside Dario's batched afternoons): once a config question gets a clean answer in Slack, copy it into a GitHub Discussion or a docs FAQ page. This is the actual fix for "lands nowhere" — Slack is the *triage and community* layer, GitHub/docs is the *SEO* layer. Don't let Slack alone carry a goal it structurally can't deliver.

## Channel structure — minimal, not the generic template

Your volume is small (20-30 questions/month) and Dario's real bandwidth is ~6h/week. Over-segmenting channels spreads that thin and makes empty channels look dead. Skip the generic 15-channel Discord-style layout entirely. Use:

- `#welcome` — rules + how support works here now
- `#announcements` — admin-only, config-surface changes
- one channel per real topic area (you said 4 — e.g. queues/routing, workers/concurrency, retries/backoff, storage backend; rename to your actual four)
- `#faq` — pinned/canvas'd canonical answers, not a discussion channel
- `#general` — optional, only if you want off-topic chat at all

That's 7 channels, not 20. Resist adding more until one of these is consistently active.

## Pre-launch: seed content before inviting anyone (SLC gate)

An empty Slack is not launch-ready — it's the "lovable" bar failing. Before any invite goes out:

1. Pull your best 15-20 answers from the last year of support email into `#faq`, one per topic. This is the single highest-leverage use of Dario's time this month — do it in one of his batched afternoons.
2. Write the norms doc pinned in `#welcome`: what this channel is for, and an honest response-time expectation (below).
3. Set up Canvas/bookmarks for the FAQ so it survives Slack's history limits.

## Founding cohort: recruit the 4 GitHub answerers first, not last

Those four are already doing unpaid support work in your issues. Reach out to them individually (DM or email) *before* the broader 60 — ask them to be founding members, not "moderators" with obligations. No formal tiered program needed at this size: just early access, a direct line to Dario, and public credit. Getting them active in week 1 means every topic channel has a real person in it before the other 56 show up — that's what prevents the "I posted and nobody answered" first impression that kills small communities.

## Invite plan: staggered, by name, spanning time zones

60 named invites across 3 continents, sent all at once, will bury the FAQ backlog and outstrip what Dario + 4 champions can cover in week one. Stagger it:

- **Week 1** — the 4 champions + ~10-15 more of your most engaged named users, deliberately mixed across topic areas *and* time zones, so every channel has someone awake for questions in most of the day.
- **Week 2-3** — remaining ~45, in 2 batches, personal email invite (not a blast) referencing what channel matches their use case.

Named, personal invites also do double duty as the exclusivity signal — treat this like a beta, not an open floodgate; 60-of-900 by name is already the right instinct.

## Operating rhythm that matches 6h/week, batched

Don't imply real-time support you can't deliver. State it plainly in `#welcome`:

> Core team reviews Slack on [2 fixed afternoons/week]. Community members often answer faster than that — feel free to jump in.

This does two things: sets honest expectations (nothing kills a support community faster than implied-but-unmet SLA), and explicitly invites the champions to fill the gap, which is the actual point of recruiting them first.

Dario's batched afternoon becomes a fixed routine:
1. Answer unresolved threads.
2. Update `#faq` with anything new and reusable.
3. Push the best 1-2 resolved threads of the week to GitHub Discussions/docs (the SEO fix above).

## What to skip

No bot stack (MEE6/Statbot-style automation) — that's Discord-community tooling for much larger, higher-noise servers. At 60-900 users with a single batched maintainer, it's overhead without payoff. One exception worth the setup cost: a join-triggered Slack workflow that auto-DMs new members straight to `#faq` — cheap, direct hit against the 1/3-duplicate-question problem.

## Metrics — lightweight, not a dashboard

Track only what tells you if this is working:
- Email questions/month, before vs. after (does volume actually drop)
- % of Slack questions answered by community vs. by Dario (are the champions actually carrying load)
- Threads mirrored to GitHub/docs per month (is the SEO fix actually happening, not just planned)
- New joiners who mention finding an old thread via Google (once the mirror has had a few months to get indexed)

## Timeline

| Phase | When | Action |
|---|---|---|
| Prep | Before invites | Seed `#faq`, set up Canvas, write norms doc, recruit 4 champions privately |
| Founding cohort | Week 1 | Champions + ~10-15 more, spread across topics/time zones |
| Full invite | Week 2-3 | Remaining ~45, 2 batches, personal invites |
| Steady state | Ongoing | Dario's 2 fixed afternoons/week; redirect new email questions to Slack; monthly best-of mirrored to GitHub/docs |