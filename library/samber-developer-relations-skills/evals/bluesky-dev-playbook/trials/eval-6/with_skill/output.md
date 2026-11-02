# Verdict

**No, don't switch to text-only posts.** Bluesky states that links get the same visibility as other posts and aren't downranked **[Bluesky]**. The data you describe fits a different cause: a brand account with no named person, posting one-way announcements into a graph that hasn't opted into it.

I haven't looked at the account itself, so I can't rule out a moderation label or a block-list listing. Step 1 below checks for both in about 15 minutes.

## Why links aren't the problem

- **Bluesky's position on links.** @bsky.app and its CEO have said link posts get the same visibility as other posts **[Bluesky]**. A link-based shadowban would contradict that.
- **What a text-only switch would cost.** The posts would no longer point to docs or releases. It would also leave unfixed the actual reasons your posts get no reach.
- **Shadowban check.** Nothing in the platform facts I reviewed documents a "shadowban" mechanism. Bluesky does have per-reader down-ranking for toxic, off-topic or bad-faith replies, and for posts users mark "show less" **[Bluesky]**. Third-party labelers and block lists can also hide an account from the people who subscribe to them **[practitioner]**.

## What most likely explains 140 followers and 0-2 likes

1. **No chronological or algorithmic reach.** The Following feed is chronological and Discover is personalized per reader **[Bluesky]**. Posting more often doesn't create reach. Reach comes through people, opt-in feeds and starter packs. Three posts a day to 140 followers mostly reaches those 140.
2. **The account is a brand with no named person.** The playbook calls this the weakest setup. People post as themselves, and the brand account is a hub that reposts them **[practitioner]**.
3. **Every post is a broadcast.** Announcements and blog links with no question and no reply to anyone start no conversations. Ranking favours conversation, and replies from inside the reader's social neighbourhood rank higher **[Bluesky]**.
4. **Five hashtags per post.** Hashtag stuffing aimed at unrelated feeds gets accounts removed by feed operators and muted by readers **[practitioner]**. Hashtags also count toward the 300-character limit **[Bluesky]**.
5. **Possible mismatch with the feeds.**
   - The DevOps/SecOps/Cloud feed had about 130 likes at last count, which is a small audience.
   - #kubernetes, #startup and #ai point at feeds and readers of very different kinds.
   - `#ai` also attracts block-list readers, and AI branding draws mass blocks **[press]**.

I haven't verified that those feeds exist or what they match. Operators often don't document their rules **[practitioner]**.

## Step 1: rule out moderation and shadowban (15 minutes, do this first)

1. **Log out and open the profile.** In a private window, open `bsky.app/profile/gridmesh.bsky.social`. Check that the profile and recent posts load.
2. **Search for a recent post.** Search a distinctive phrase from it while logged out. A missing post is a red flag.
3. **Look for labels.** Check the profile for warnings or labels, and confirm the account isn't flagged as undeclared automation.
4. **Check block-list and labeler listings.** Look at the third-party block trackers, which are public **[practitioner]**. Any listing is a stop signal.
5. **Verify the posts show up in the feeds you tag for.** Check the operators' stated rules. If the posts are absent from a feed whose rule you meet, ask the operator.

If steps 1-3 all pass, you aren't shadowbanned. The cause is the account setup and content.

If you find a label, a block-list listing or missing posts, stop and tell me what you see. The fix then goes through Bluesky's appeal process or the list owner, and posting changes won't help.

## Step 2: go/skip

I don't know whether your audience is on Bluesky, so this is an assumption to confirm. **Go**, if at least one feed, starter pack or recognizable person in your stack (Kubernetes, DevOps, cloud) is active there. **Skip** if nothing active exists, or if nobody can post as a person for at least an hour a week. A skip verdict is a valid result. **Go small** (one person, replies only) applies if the product leans on AI or collects user data.

## Step 3: what to change

**Stop**
- Stop the 5-hashtag footer. Use zero or one, and only when a feed you've confirmed matches that tag.
- Stop posting 3 announcements a day. Drop to a few original posts a week per person.
- Don't add `#ai` unless the post is about AI.

**Start**
- **Put a named person behind the account.** Have an advocate or engineer post under their own name, with a bio naming the employer.
- **Switch to a domain handle.** Use `gridmesh.<your domain>` for the brand and `name.<your domain>` for staff, via a DNS TXT record **[Bluesky]**. Rename once, announce it, and keep the old name in the bio for a while. Repeated renames count as identity churning **[Bluesky]**.
- **Make the brand account a hub.** It reposts the team's teaching posts a few times a week, announces releases, and answers support.
- **Do two weeks of replies by named people.** They reply daily in existing Kubernetes and DevOps conversations, with no product links unless asked.
- **Ask for pack inclusion in week 3.** Ask one pack curator, in a public reply and for one named person, to consider adding them. Packs are the largest follow lever measured: members gained up to 85% more new followers **[research]**. That is an upper bound, and it favours accounts already popular. Never ask for the whole team.
- **Keep links, but use them well.** Keep posting links to docs, repos and posts, and put the point of the post in the text.

**Draft post, for the named person to rewrite in their own voice:**
> Rewrote our Helm upgrade checks after a rollout hung for 40 minutes. The failure mode and the fix are in the post. Anyone else seen this with CRD ordering? [link]

An example of a draft to retire:
> Announcing Gridmesh 2.4! 🚀 Read more: [link] #devops #cloud #kubernetes #ai #startup

**Disclosure.** When staff reply about the product, add "I work at Gridmesh". Undisclosed commercial content is banned **[Bluesky]**.

## Limits and refusals

- **Don't boost with likes.** Asking staff or a Discord to like and repost is artificial manipulation **[Bluesky]**.
- **Don't automate interactions.** Automated or bulk follows, likes and replies are spam **[Bluesky]**.
- **Don't promise growth.** Users can opt out of being shown to non-followers in Discover **[Bluesky]**. The most-liked dev feeds count likes in the hundreds **[Bluesky]**. Treat 0-2 likes at 140 followers as normal for a broadcast-only brand account. It isn't proof of suppression.
- **Starter packs:** 150 people and 3 feeds per pack, and the curator decides who is in **[Bluesky]**.

## Metrics

- Replies, reposts and quote posts per post and per person, not likes alone. Bluesky shows no impression counts **[practitioner]**.
- Follower change in the week after a pack inclusion or feed post. Pack attribution is an estimate only.
- Referral sessions with referrer `go.bsky.app` **[Bluesky]**, plus UTM-tagged links against a pre-launch baseline.
- Block-list and labeler listings. Any increase after a post is a stop signal.
- Don't headline raw follower totals.

## Evidence limits

Bluesky changes monthly, and I didn't re-check live pages in this session. Before you quote the feed like counts (about 130 for DevOps/SecOps/Cloud) or the link-visibility statement, confirm them on Bluesky's own pages and in the app.

## Questions that would sharpen this

1. Who will post under their own name, and how many hours a week can they give?
2. Do the Kubernetes and DevOps people you want to reach have active feeds or packs on Bluesky, and do any of them reply to your posts?
3. Does Gridmesh's messaging lean on AI, or collect user data? That decides Go versus Go small.
4. Do you control a domain for the handles, and is any account verified?