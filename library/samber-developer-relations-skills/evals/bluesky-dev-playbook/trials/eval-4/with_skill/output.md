# Promptwright on Bluesky: launch-week plan

**Assumptions** (I'm running this in one pass, so these are gaps I filled):
- "Next Tuesday" is **Tue 3 Nov 2026**. Today is Sat 31 Oct, so you have 3 days of prep. If you meant 10 Nov, use the extra week for the replies in weeks 1-2.
- One named builder (engineer or founder) can post under their own name for at least 1 hour a week.
- I don't know whether your audience (GitHub-heavy teams, your language communities) is visibly on Bluesky. That's the first check below.

## 1. Verdict: Go small, with a Monday gate

- **Skip** if, on Monday, no feed, starter pack or recognizable person in your audience's stack is active on Bluesky. Put launch effort into other channels instead (see `hackernews-playbook` and `oss-launch`).
- **Go small** otherwise. Promptwright is AI-forward and the plan collects users' posts, so the playbook caps this at one person's own voice, replies first, and a hub that reposts.
- Don't promise follower growth or virality. Users can opt out of Discover exposure [Bluesky], and the most-liked dev feeds count likes in the hundreds [Bluesky].

## 2. Three parts of the plan I'm refusing, with replacements

| Your plan | Verdict | Why | Do this instead |
|---|---|---|---|
| Brand account posts a daily AI-generated tip | **Changed** | AI content and AI branding draw mass blocks and block-list inclusion. Bluesky's own AI assistant became the second most-blocked account [press]. A brand-only account with no named person is also the weakest setup [practitioner]. | 2-3 tips a week, written by named engineers from real review cases. An AI draft is a starting point the person rewrites. The hub reposts the best ones. |
| CEO asks all 40 employees to like and repost in the first hour | **Refused** | The Guidelines ban artificially manipulating social signals [Bluesky]. A coordinated staff push is that. Readers see the pile-on [practitioner]. | Staff answer questions in the replies, with a disclosure line. Nobody mass-likes. If someone is moved to repost something they like, that's their call, but no one asks for it. |
| Engineering pulls every "code review" post from the firehose for a prospect list and tone fine-tuning | **Refused** | Consent is the norm here, not the API's openness. A one-million-post dataset was pulled within a day over consent [press]. Putting this in an AI-forward launch is the worst pairing. Auto-interacting with keyword matches is spam, and bots may interact only when tagged [Bluesky]. | See section 3. |

## 3. Replacements for the firehose

- **Listening:** each person saves Bluesky searches for "code review", "PR review" and their stack's terms. Search filters by keyword, people, date and language [Bluesky]. A human reads the results. No scrape, no dataset.
- **Prospect list:** build it from people who raise a hand. These are replies to your posts, signups, GitHub App installs and inbound DMs. Nobody is added to a list or contacted because a post matched a keyword.
- **Tone fine-tuning:** train on material you own or have consent for, such as your docs, your own PR-review corpus and your support replies. If you want public Bluesky text as training data, that needs a separate decision with legal. I won't plan around it. I can only point to the consent backlash [press] and haven't checked the legal side.

## 4. Accounts and identity (before Tuesday)

- **Domain handles, set by Sunday:** `promptwright.com` (or your docs domain) for the hub, and `name.promptwright.com` for the builder. Use a DNS TXT record on `_atproto` with value `did=<the account's DID>`, or `/.well-known/atproto-did` [Bluesky]. Switching keeps followers because identity is the DID [Bluesky].
- **Decide the display name now.** Apply for the blue check only after the handle and display name are final, because changing either drops the badge [Bluesky]. Verification is at Bluesky's discretion, so don't promise it.
- **Hub operator:** name a human. Each person and tool signs in with its own app password and 2FA on.
- **Bios:** name the person and employer. Say what Promptwright does in plain words: "code review for GitHub PRs". Say once, plainly, that it uses AI. Don't lead with "AI-powered".
- **Pin one post:** the launch post, after Tuesday.

## 5. Surfaces for this launch (ranked by value per hour)

1. **Replies by named people in existing conversations.** This is the top lever, and it compounds [Bluesky].
2. **Existing dev custom feeds.** Add the feed's tag on posts that belong there. If the feed names no rule, watch it or ask the operator first [practitioner]. A hard launch date promotes this, so identify the 3-5 relevant feeds on Monday.
3. **Community starter packs.** This is the biggest follow lever measured, up to 85% more new followers for members [research]. It's an upper bound and favours accounts already popular. It can't land in 3 days, because the default rung is two weeks of replies first. Ask in week 3.
4. **Brand hub:** release posts and reposts of staff teaching posts.
5. **Your own pack or feed:** later, after about a month of replies.

## 6. Dated cadence

| When | Action |
|---|---|
| **Sat 31 Oct - Sun 1 Nov** | Set up domain handles, bios, disclosure line, saved searches. List the dev feeds, packs and people in your stack. |
| **Mon 2 Nov** | Run the go/skip gate. The builder does the first reply session: answer, don't pitch, no product links unless asked. Hub posts nothing yet. |
| **Tue 3 Nov, launch** | The builder posts from their own account with the feed tag. The hub reposts, then posts one release post with the changelog link. Staff reply to questions with the disclosure line and never mass-like. If replies turn hostile, the poster can limit replies or detach quote posts [Bluesky]. |
| **Wed 4 - Fri 6 Nov** | The builder replies daily. One human-written tip from an engineer per day at most (2-3 across the week is enough). The hub reposts the best one. Answer every real question within hours. |
| **Mon 9 Nov** | Review metrics (section 9). Check block-list and labeler inclusion. Drop surfaces that returned nothing. |
| **Weeks 2-3** | Keep replying. In week 3 ask each relevant pack's curator to consider one named person, with a reason the pack's readers gain, as a public reply first. Never ask for the whole team. |
| **Week 4 onwards** | A few original posts a week per person. About a month in, build your own pack from community people you now talk with. Ask each first and announce it once in a post. |

## 7. Limits that bind

| Limit | Kind | Source |
|---|---|---|
| Automated or bulk interactions that notify users are spam, with no published threshold | enforced | [Bluesky] |
| No artificial manipulation of likes or reposts, and no undisclosed sponsored content | enforced | [Bluesky] |
| 5,000 write points per hour and 35,000 per day. This is not permission: bulk interaction is spam far below it. | enforced | [Bluesky] |
| Starter packs hold 150 people and 3 feeds. The curator decides who is in. | enforced / policed | [Bluesky] |
| Custom feeds set their own entry rules, and the operator can exclude you. | policed | [practitioner] |
| Anyone can put your accounts on a block list, and subscribers stop seeing you. | policed | [Bluesky] |
| By default only people a user follows can DM them. | enforced | [Bluesky] |
| Posts are 300 characters, hashtags included. | enforced | [Bluesky] |

## 8. Draft posts

These are drafts for the named person to rewrite in their own voice. Don't post them as written, and run them through your humanizer first. Anything in brackets is a placeholder.

**Launch post (builder's account):**
```
I've spent [N months] on this: Promptwright reviews your GitHub PRs and comments on the lines that matter. It uses an LLM; here's what it flags and what it deliberately ignores: [link] What I'd love feedback on: false positives on your repo. #codereview
```
Attach alt text for any image.

**Hub post:**
```
Promptwright is out. [Name] built it and wrote up how it works: [changelog link]. Questions go here or in the docs: [help link].
```

**Staff reply, with disclosure:**
```
(I work on Promptwright.) It skips generated files and lockfiles by default; you can add paths in the config. Happy to look at your case if you share the repo layout.
```

**Tip (engineer, from a real case):**
```
A PR reviewer's most useful comment is "what breaks if this is called twice?" Here's the retry bug that question caught in our own code: [link]
```

**Pack ask (week 3, public reply, one person per ask):**
```
Hi [curator], thanks for the [topic] pack. Would [Name] ([handle]) fit? They post weekly about [topic] and answer questions in the [feed]. No worries if the scope is different.
```

## 9. Metrics

Bluesky shows no impression counts [practitioner], so measure what you can observe:
- **Replies, reposts and quote posts** per post and per person, not likes alone.
- **Follower change** in the week after a feed post or pack inclusion. Treat it as an estimate. Bluesky notifies a pack creator only when a new user signs up through it [Bluesky].
- **Referral sessions and signups** from `go.bsky.app` [Bluesky] plus UTM-tagged links, since some clients strip referrers. Compare against the pre-launch baseline (`devrel-analytics`).
- **Block lists and labelers** that list your accounts. Any increase after a post is a stop signal: pause the AI-adjacent posts and reread the replies.
- Never report raw follower totals as the headline.

## 10. Monday checklist

1. Run the go/skip gate.
2. Confirm the date is 3 Nov.
3. Name the builder and the hub operator.
4. Tell the CEO the like-and-repost ask is replaced by "answer questions in the replies".
5. Tell engineering the firehose job is off, and ask them to build the hand-raiser list from signups and installs.

## Related skills

- `oss-launch`
- `hackernews-playbook`
- `devrel-analytics`
- `developer-community-moderation` (if a pile-on starts)