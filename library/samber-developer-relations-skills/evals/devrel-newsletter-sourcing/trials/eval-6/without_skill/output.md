# Lattice Weekly: sourcing system for Dario

**Next action for you (about 30 min):** write down why you picked the last 8 issues' items, then fill the `[FILL]` fields below. Your instinct is the part Dario can't copy, so it needs to be on paper before the handoff.

## 1. Rules

- 3 hours per issue, hard cap.
- Items go into one log all week. Nothing is picked from memory.
- Social feeds (Twitter, HN) supply at most 40% of items. The rest come from sources that don't depend on what was trending that morning.
- An item gets in by score, not by feel.

## 2. Time budget (180 min)

| Min | Step |
|---|---|
| 60 | Pull from Tier 1 and Tier 2 sources |
| 30 | Scan Tier 3 (social, HN) |
| 20 | Process reader submissions and community channel |
| 40 | Score, dedupe, shortlist |
| 20 | Fill quota gaps with a targeted search |
| 10 | Update the log, note what worked |

Alerts and feeds collect passively, so Dario only reads what has already been gathered.

## 3. Source map

**Tier 1: first party (always check)**
- Lattice GitHub: releases, merged PRs, roadmap issues, discussions.
- Lattice docs changelog and blog.
- Maintainers' own posts and talks.

**Tier 2: ecosystem (set up once, then reads itself)**
- GitHub release feed for a watchlist of ecosystem repos: drivers, ORMs, clients, integrations, dashboards, deploy tooling. `[FILL: starting list of 15–25 repos]`
- GitHub code search for repos that import a Lattice client or depend on Lattice. Run it monthly to find new projects.
- Package registry pages for Lattice clients (new versions, new dependents).
- Alerts on "Lattice" plus graph-database terms. `[FILL: exact name variants to avoid collisions with other "Lattice" products]`
- 5–8 adjacent newsletters and blogs on graph databases, databases, and data infrastructure, via RSS.
- Conference and meetup talk lists that mention Lattice.

**Tier 3: social (capped at 30 min)**
- HN: Algolia saved searches for the name variants, plus Show HN.
- Twitter/X, Bluesky, Mastodon, Reddit: saved searches on the same variants. Don't scroll the timeline.
- Lists of Lattice users and maintainers. `[FILL]`

**Tier 4: reader-supplied**
- Submission form linked in every issue footer.
- Community channel (Discord/Slack) `#share` or equivalent.
- Replies to the newsletter. Log each one and credit the sender.

## 4. Weekly routine

1. Monday: check that the alert and feed inbox is working. Fix anything silent.
2. Tuesday, 60 min block: run Tiers 1 and 2. Log every candidate, even weak ones.
3. Tuesday, 30 min block: run Tier 3 with saved searches only.
4. Process submissions.
5. Score every logged item (section 5).
6. Check the mix against the quota (section 6). Run a targeted search for any empty slot.
7. Hand the shortlist to the writing step.

## 5. Scoring

Score each item 0–2 on five criteria:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Relevance | Tangential | Useful to some readers | Directly changes what a Lattice user does |
| Novelty | Seen in last 4 issues, or old news | Fresh angle on known topic | New this week |
| Substance | Announcement or opinion only | Some detail | Code, data, or real production lessons |
| Source quality | Unverifiable | Secondhand | Primary source or named author |
| Actionable | Nothing to do | Worth reading | Reader can try, adopt, or fix something |

- Include items scoring **7 or more**.
- Relevance of 0 is an automatic reject.
- Substance of 0 is rejected unless it's a first-party release.
- Ties go to the item from the less-represented source tier.

## 6. Issue mix (target 8–12 items)

- 1–2 first party (releases, roadmap, core news)
- 3–4 ecosystem (libraries, integrations, tools)
- 2 learning (tutorials, talks, deep dives)
- 1–2 community (user stories, submissions)
- 1 wildcard from an adjacent area

`[FILL: adjust to match the mix you actually run today.]`

If a slot is empty, ship without it. Don't pad with a weak item.

## 7. The log

One shared spreadsheet, one row per candidate:

`date found | title | URL | source tier | submitter | category | 5 scores | total | decision | issue # | reject reason`

- Check it for duplicates before scoring.
- Keep rejected rows. Rejections show whether the sources or the rubric need fixing.

## 8. Handoff checklist (before next month)

1. Write down your Tuesday habits: which accounts, which HN searches, which names you watch. Add them to Tier 2 and 3.
2. Take your last 8 issues, score every item with the rubric, and see where it disagrees with your picks. Adjust weights until it roughly matches.
3. Build the alerts, saved searches, and RSS folder. Give Dario ownership.
4. Share the full submitter history.
5. Do one issue together, with Dario running the process and you only reviewing.

## 9. Check the system (week 8)

- Click-through per item category, to see what readers value. `[FILL: do you have per-link click data?]`
- Share of items from each tier, and whether any tier produced nothing.
- Time spent against the 3-hour cap.
- Number of reader submissions used.
- Update the watchlist, quotas, and scoring weights from this data, not from instinct.

**Open question for you:** do you have click data from past issues? It would let you set the rubric weights from real reader behavior instead of guesses.