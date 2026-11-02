Here's the plan — and one thing I need from you to turn it into real data.

## What's blocking real numbers right now

I don't have the three rivals' names/domains (and didn't look in `skill-wip/`, as instructed, since that's likely where they live). Everything below is ready to run the second you give me:

1. **Your product** — one line, so "strength/weakness" reads as *relative to us*, not generic.
2. **The three rivals** — name + domain each.

Drop those in and I'll kick off the research myself in the background (GitHub API pulls, careers-page scrapes, blog-cadence analysis, sponsor-page checks) and hand you back the filled matrix — you won't spend your 4 hours doing lookups by hand. Until then, here's the exact plan, time-boxed so you can start solo immediately if you don't want to wait.

---

## The realistic scope for 4 hours, no engineer

Six dimensions × three rivals × real synthesis is a 2-day agency engagement. In 4 hours you get a **directional read, not a definitive one** — enough to make Q4 calls, not enough to publish as a report. Say that explicitly in the Friday meeting so nobody over-trusts a single-afternoon snapshot.

Cut scope by prioritizing **objective, fast-to-pull signals** over anything requiring judgment calls or paid tools (Ahrefs/DataForSEO-grade SEO analysis won't fit — skip it unless you already have Ahrefs open).

---

## Hour-by-hour

**Hour 1 — Repos & docs (fastest, most objective, do all 3 rivals side by side)**
- GitHub org page: stars/forks trend, release frequency (last 12 months of tags), open issue count vs. closed rate, top 5 contributors external vs. internal, README/CONTRIBUTING quality.
- No auth needed: `gh api repos/<org>/<repo> --jq '{stars:.stargazers_count, forks:.forks_count, issues:.open_issues_count, pushed:.pushed_at}'` — one line per rival.
- Docs: is there a changelog? How often does it move? Any recent restructure (signals a positioning shift)? Skim the last 3 "what's new" entries.

**Hour 2 — Hiring & conferences**
- Hiring: rival's own careers page + `site:linkedin.com/jobs "<Company>"` — count open roles, bucket by function (eng vs. DevRel vs. sales vs. support). A DevRel/community-manager req you didn't expect is a strong signal. Note seniority (are they building a team or hiring a lead?).
- Conferences: check the last 2-3 major events in your category — sponsor pages, speaker lists. If a sponsor page has since been updated, Wayback Machine it (`web.archive.org/web/2026*/eventsite.com/sponsors`) to catch what they sponsored earlier in the year, not just now.

**Hour 3 — Community activity & content trends**
- Community: Discord/Slack member count if public, GitHub Discussions activity, subreddit/HN mention frequency (`site:news.ycombinator.com "<Company>"`), Stack Overflow tag question volume if they have one.
- Content: pull their blog sitemap or RSS feed, bucket post dates by month for the last 12 — this alone tells you cadence and whether they ramped up or went quiet. Skim titles for 3 recurring themes (e.g., "moved from feature announcements to use-case content in Q2" is a real finding).

**Hour 4 — Synthesize**
- Fill the one-pager per rival (template below).
- Build the comparison matrix.
- Write the "so what for Q4" section — this is the only part anyone will actually read Friday.

---

## Deliverable template (fill one per rival)

```
# [Rival] — Snapshot, [date]

## Repos & docs
- Stars/forks: [n] ([trend last 90d])
- Release cadence: [x/month], last release [date]
- Docs: [changelog exists Y/N, last updated, notable restructure]

## Hiring (open roles right now)
- Eng: [n] | DevRel/Community: [n] | Sales/GTM: [n]
- Notable req: [anything unusual — new team, new region, seniority signal]

## Conferences (last 12mo)
- Sponsored: [event, tier, date]
- Spoke at: [event, topic, speaker]

## Community
- Discord/Slack: [size if public]
- Mention volume (HN/Reddit/SO): [rough trend — up/flat/down]

## Content (last 12mo)
- Cadence: [posts/month, trend]
- Themes: [3 recurring topics, and whether they shifted mid-year]

## So what
- [1-2 lines: what this rival is clearly building toward]
```

## Comparison matrix (fill after all 3 are done)

| Dimension | Rival A | Rival B | Rival C | Us |
|---|---|---|---|---|
| Release cadence | | | | |
| Star growth (90d) | | | | |
| Open DevRel/community roles | | | | |
| Conferences (12mo) | | | | |
| Community size | | | | |
| Content cadence | | | | |
| Content theme shift | | | | |

## Synthesis section (this is what Q4 planning actually uses)

3-5 bullets, each in this shape: **[observation] → [implication for us] → [Q4 action, if any]**. Example shape: "Rival B tripled DevRel hiring since Q2 and went quiet on conference sponsorship → they're betting on organic community over paid presence → worth checking if their Discord growth backs that up before we match the move."

---

Send me the product line + 3 rival domains and I'll run hours 1-3 for you — you'd only need to do hour 4 (the judgment calls a script can't make) yourself before Friday.