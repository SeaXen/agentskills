# Platform: Discord — not Slack, not a forum

**Discord, using Forum Channels (not plain text) for the two channels that matter most: `#help` and `#roadmap`.**

Why not the alternatives:

- **Slack** — free tier purges message history after 90 days. Two of your three goals (support deflection, roadmap capture) depend on old answers staying searchable forever. You'd need a paid tier just to not lose data, and it's more expensive per-seat than Discord at zero.
- **Discourse/forum software** — best long-term for SEO and searchability, but it's a second thing to host and maintain, and a forum with 45 members looks like a ghost town on day one. Wrong tool for cold-start.
- **GitHub Discussions** — tempting since your two power users already do this in Issues. But it's weak on the "vocal community that brings signups" goal — no presence, no real-time feel, nothing that turns into belonging. Keep GitHub for what it's good at (bug tracking) and don't try to make it your community hub.

Discord's Forum Channel type solves your actual problem structurally, not just culturally: each post is a thread, taggable (`unanswered` / `answered`, or `planned` / `shipped`), and searchable indefinitely for free. `#help` becomes a self-serve FAQ that grows on its own. `#roadmap` becomes a public feature-request board with zero extra tooling. That's support deflection and roadmap input built into the platform choice itself, not bolted on later.

# Structure — lean, not the standard template

Don't stand up 15 channels for 45 people — empty channels read as a dead community. Six is enough:

- `#welcome` — one pinned post: what this is, the three things it's for, link to docs
- `#introductions` — one post per person, light touch
- `#help` (Forum Channel) — tags: `unanswered`, `answered`, `bug`
- `#roadmap` (Forum Channel) — tags: `under review`, `planned`, `shipped`
- `#general` — open chat
- `#changelog` — you post only, release notes

Skip roles/bots/moderation stacks for now. At 45 people you are the moderator; adding tooling before you have a moderation problem is wasted setup time you don't have.

# Before you invite anyone (do this first — highest leverage of your 8 hours)

Write up the four questions you get by DM, as real answers, and post them as the first four threads in `#help`, pre-tagged `answered`. This is the single highest-leverage use of your time this week: it's instant support deflection, and it teaches the format you want people to use before anyone else posts.

# Week 1, day by day (~8 hours total)

**Day 1 — 2h.** Create the server, the six channels, a short code of conduct (one paragraph: be respectful, no spam, be patient with beginners). Write and pin the four FAQ threads in `#help`.

**Day 2 — 1.5h.** DM your two power users personally, before anyone else gets an invite. Tell them directly: you noticed them helping others in Issues, you're building a space for exactly that, and you want them in first as founding members. Give them something concrete, not just a badge — first look at the roadmap, a direct line to you. This is your entire "champion program" for week one; don't build more than this yet.

**Day 3 — 1.5h.** Soft-launch to ~10–12 of your 45 — the ones most likely to post, not a random slice. Personal invite message, one line on why you're inviting *them* specifically if you can. Be in `#help` and `#roadmap` yourself, answering fast, so the first thing anyone sees is a responsive space.

**Day 4 — 1h.** Post one open prompt in `#roadmap`: "What's the one thing slowing you down in production migrations right now?" This is your first real roadmap-input capture, deliberately started early so it's not an afterthought.

**Day 5 — 1h.** Invite the remaining ~33, now that the server has visible activity — real threads, real answers — instead of a blank room. Empty communities die on arrival; sequencing the invite this way avoids that.

**Weekend — 1h buffer.** Monitor, answer, and — important — when someone asks a fifth or sixth question that keeps recurring, add it to the FAQ immediately. Note who answers something before you get to it; that's your next champion candidate, not week one's problem to solve, just week two's to watch.

# What to deliberately not do yet

- No moderation bots, no auto-roles, no ticket system — 45 people don't need them, and setup time here is time not spent answering questions.
- No formal ambassador/champion program with tiers and swag — you have two candidates, not a cohort. Formalize once you can see who shows up consistently, not before.
- No referral/bounty program — premature until you know who your advocates actually are.
- Don't invite all 45 at once — a populated room with a few threads beats a big room with none.

# What "working" looks like by end of week 1

- Most of the 45 have joined (target 30+).
- At least a few `#help` threads answered by someone other than you — signal the peer-support pattern from Issues is transferring over.
- Your DM volume for the same four questions starts dropping, because you're linking people to `#help` instead of re-answering.
- At least one concrete, specific idea in `#roadmap` you wouldn't have gotten from a DM.

If those four hold, week two is: keep answering fast, start naming your two power users publicly when they help someone ("thanks for jumping in, @x"), and begin the invite-only champion conversation once — not before — you see a third or fourth person doing the same thing unprompted.