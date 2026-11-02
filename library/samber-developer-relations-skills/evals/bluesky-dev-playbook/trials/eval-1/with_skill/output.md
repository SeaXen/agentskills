# Tessellate CI on Bluesky: plan check and posting-time answer

**Direct answer on posting times:** I can't give you best hours, and I won't invent a table. The Following feed is chronological, and Discover is personalized per reader. There is no shared ranking window to aim at **[Bluesky]**. Bluesky also shows no impression counts **[practitioner]**, so no one can measure "best hours" from outside. The substitute is below: post when a named person can answer replies, then read your own audience's pattern after a month.

I'm quoting the playbook's reference file from 2026-10-31. I didn't re-check live Bluesky pages, so verify the numbers before they reach a deck.

## Verdict: conditional go

I assumed these answers where you didn't give them. Tell me if any is wrong.

| Gap | Assumption | If wrong |
|---|---|---|
| Who posts | Brand account only, no named person | Weakest setup. Fix first (see Accounts). |
| Time budget | Unknown | Under 1 hour a week of a person posting means **skip**. |
| Audience present | Unknown | Run the 30-minute check below before anything else. |
| AI-forward messaging | No | If yes, go small: one person, replies only. |
| Domain | You control a company domain, e.g. `tessellateci.com` (placeholder, use the real one) | Without one, you can't do domain handles or the check. |
| Deadline | "End of month" | See the timing note. |

**Go/skip check (30 minutes, do it first):** search the app for CI, DevOps, GitHub Actions and your runner stack's terms. **Skip** if no feed, starter pack or recognizable person in your audience's stack is active. The DevOps/SecOps/Cloud feed had about 130 likes at last count and the Developers feed about 660, so the audience is thin but real **[Bluesky]**. Skip is a valid answer.

**Timing note:** today is 2026-10-31. If "end of month" means today, only Week 0 below can land. Realistic framing for leadership: account and identity are live by 2026-11-30, with growth measured in Q1.

## Your plan, point by point

| Your step | Verdict | Why and fix |
|---|---|---|
| Create `@tessellateci.bsky.social` | ❌ Change | Use a domain handle on a domain you control. This is Bluesky's own anti-impersonation advice **[Bluesky]**. Do it before applying for the blue check. Moving to a domain handle after the check drops the badge **[Bluesky]**. |
| Brand account as the main voice | ⚠️ Weak | People first. Advocates and engineers post under their own names. The brand account is a hub: reposts their teaching posts, release posts, support **[practitioner]**. |
| Buffer mirrors every X post and thread | ❌ Refuse | Unattended mirrors read as "nobody home". Replies make no sense off X, and dropped alt text and x.com links hurt **[practitioner]**. Details below. |
| Threads of 5-7 posts with a strong hook | ❌ Drop | Hook formulas and thread tuning are the X playbook, tuned for "the algorithm". Reach here comes from feeds, starter packs and replies. Write one 300-character post with the finding first. Put the long version in a blog post and link it. Links aren't downranked **[Bluesky]**. |
| Post at the best engagement hours | ❌ Drop | See the direct answer above. |
| One hashtag or none | ✅ Keep, with one tweak | Fine. Add the one tag a relevant dev feed actually matches, on posts that belong there. If the feed names no rule, watch it for a week or ask its operator first **[practitioner]**. Don't stuff tags to reach unrelated feeds. |
| 22k X followers as a base | ⚠️ Don't count on it | Followers don't transfer. Engagement is a different network, so don't promise leadership follower growth or virality **[Bluesky]**. |

## Accounts and identity

1. **Brand handle:** `tessellateci.com` (your real domain). Set it with a DNS TXT record at `_atproto.<domain>` with value `did=<account DID>`, or serve `/.well-known/atproto-did` **[Bluesky]**.
2. **People:** 2-3 named engineers or advocates on `name.tessellateci.com` subdomains. The well-known route needs a web server answering on each subdomain **[Bluesky]**.
3. **Bios:** name the person and employer. Draft for each person to rewrite: "Developer advocate at Tessellate CI (hosted CI runners). I write about slow pipelines and cache misses. Posts are mine."
4. **Blue check:** apply only after handle and display name are final. Never promise it to leadership. Bluesky verifies "notable and authentic" accounts at its discretion **[Bluesky]**.
5. **Team access:** each person and tool signs in with its own app password, 2FA on, so access stays revocable **[practitioner]**.
6. **Rebrand risk:** if the X handle differs from the final name, rename once, in one announced step. Identity churning is banned **[Bluesky]**.

## Cross-posting from X, done right

- Pick X as the home network. Cross-post **original posts only**, rewritten under 300 characters **[Bluesky]**, with alt text and without x.com links.
- Never cross-post replies or quote-tweets. A 5-7 post X thread becomes one Bluesky post plus a link to the write-up.
- Buffer is acceptable only as a scheduler for those rewritten posts, with a human approving each one. Don't turn on auto-mirroring.
- Buffer's own posting caps are a tool limit, not a Bluesky rule **[practitioner]**.
- A person must read Bluesky replies daily. If nobody does, stop the mirror.

## Surfaces, ranked for you

Replies in existing CI/DevOps conversations > inclusion in community starter packs > posting into existing dev feeds > your own pack > brand hub release posts > your own feed > trending topics.

What moved the order: you have an existing X audience but no named people on Bluesky, so replies and pack inclusion come first. Hub posts rank lower than leadership probably expects. Your own custom feed only makes sense if CI has no active feed and someone volunteers to own it.

Rough effect sizes, upper bounds that favour already-popular accounts **[research]**:
- Pack members gained up to 85% more new followers.
- Creators who listed themselves in their own pack gained up to 117% more.

## Dated cadence

Dates assume the account work starts Monday 2026-11-02.

1. **Week 0, 2026-11-02 to 11-06:** do the go/skip check. Set domain handles, bios and a pinned post. Each person saves searches for CI terms (search filters by keyword, people, date, language **[Bluesky]**). That is for listening only, never a firehose scrape.
2. **Weeks 1-2, 11-09 to 11-20:** each person replies daily to what those searches and relevant feeds surface. No product links unless asked. Use the disclosure line when relevant: "(Disclosure: I work on Tessellate CI, hosted CI runners.)"
3. **Week 3, 11-23 to 11-27:** ask each relevant pack's curator, in a **public reply first**, to consider **one named person**, with a reason the pack's readers gain. Never ask for the whole team.
4. **Week 4 onward, from 11-30:** a few original posts a week per person. The hub reposts staff and posts releases. Around 12-07, build your own pack of ~40 community people you now talk with, each asked first, mostly not staff. Announce it once, in a post.
5. **Launch day, any release:** the engineer who built it posts, the hub reposts, and the post uses the feed tag if one fits. Staff answer questions in replies and **don't mass-like**. If replies turn hostile, the poster can limit replies or detach quote posts **[Bluesky]**.
6. **Monthly:** check block-list inclusion and labels on your accounts, review referrals, drop surfaces that returned nothing.

## Posting times: what to do instead

- Post when the named person can reply within a few hours. Reply speed matters more than clock time on a chronological feed.
- For small feeds, watch when the feed itself is active and post then. That is observation, not a rule.
- After 4-6 weeks, look at when your replies and reposts cluster, per person. Treat that as your own data, one account's sample, not a platform finding.
- One unverified data point: a Bluesky staffer reported about 10x the engagement rate versus X on identical posts for one account **[practitioner]**. It was a single sample, so don't put it in a leadership deck as a benchmark.

## Refusals triggered by your plan

- Unattended X mirror: refused, replaced with the rewrite flow above.
- Don't follow/unfollow for follow-backs, and don't ask staff to like and repost launch posts. Both are artificial manipulation of social signals **[Bluesky]**.
- Don't DM people asking them to follow you or your pack. Bulk notifying interactions count as spam **[Bluesky]**, and by default only people a user follows can DM them **[Bluesky]**.
- Don't add people to your pack without asking, and don't pay a curator for placement unlabelled **[Bluesky]**.
- Publish AI-drafted posts only after the named person rewrites them. I did not run these drafts through a humanizer skill. They are starting points.

## Limits that bind

| Limit | Kind | Source |
|---|---|---|
| Post: 300 characters, hashtags count | enforced | [Bluesky] |
| Starter pack: 150 people, 3 feeds; curator decides who is in; blocking the creator removes you | enforced (size), policed (who) | [Bluesky] |
| Each custom feed sets its own entry rule; the operator can exclude you | policed | [practitioner] |
| Block lists and labelers: anyone can list your accounts, and subscribers stop seeing you | policed | [Bluesky] |
| Write budget 5,000 points/hour, 35,000/day, not a permission: bulk interactions are spam far below it | enforced | [Bluesky] |
| DMs: only accounts a user follows can DM them by default | enforced | [Bluesky] |

## Draft posts (for the named person to rewrite)

**First post:**
> New here. I spend most days staring at slow CI pipelines and the rest arguing that most of them are a cache problem. Who should I follow for people running CI at scale?

**Reply with disclosure:**
> (Disclosure: I work on Tessellate CI, hosted CI runners.) For flaky cold-start times, check whether your dependency cache key includes the lockfile hash before blaming the runner. Happy to look at the workflow if you post it.

**Pack ask, public reply to the curator:**
> Hi [curator], thanks for the DevOps pack. Would [name] (name.tessellateci.com) fit? They post weekly about pipeline performance and answer questions in the DevOps feed. No worries if the pack's scope is different.

**X thread to Bluesky:** one post, under 300 characters, key finding first, link to the write-up, alt text on any chart, no x.com link, no "1/6".

**Release post (hub):**
> Tessellate CI [version]: [one concrete change]. Changelog: [link]

## Metrics

Don't headline raw follower counts.
- Replies, reposts and quote posts per post and per person, not likes alone.
- Follower change in the week after a pack inclusion or feed post. Bluesky notifies a pack's creator only when a new user signs up through it **[Bluesky]**, so pack-driven follows are an estimate.
- Referral sessions and signups from `go.bsky.app` **[Bluesky]**, plus UTM-tagged links, since some clients strip referrers, against a pre-launch baseline.
- Count of block lists and labelers listing your accounts. Any increase after a post is a stop signal.

## Decisions I need from you

1. Who are the 2-3 named people, and how many hours a week can each give?
2. Which domain, and who controls its DNS?
3. Does your messaging lean on AI? If yes, the verdict drops to go small.