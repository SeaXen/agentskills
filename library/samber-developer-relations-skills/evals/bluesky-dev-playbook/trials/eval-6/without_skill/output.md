**Short answer:** Almost certainly not a shadowban, and text-only posts won't fix it. I couldn't check live data (the network call needed approval), so what follows is reasoning from how Bluesky works, plus a test you can run yourselves.

## Why it's probably not a shadowban

- **Bluesky has no known penalty for links.** Its feeds are mostly chronological or follow-based, and the algorithmic ones are third-party and open. Links aren't demoted in the Following feed. Bluesky's official account has said so in its own posts, but I haven't re-checked that today, so confirm it before you cite it.
- **Link cards are normal on Bluesky.** Tech news accounts, blogs and newsletters post links all the time and get strong engagement.
- **Bluesky has no hidden-ranking shadowban like X's.** Moderation uses labels, and an account that's been actioned shows a label. Check the profile from a logged-out browser for any label or "suspended" notice.

## What the numbers point to

140 followers with 0-2 likes per post is about what this posting pattern earns. Likely causes, in order:

1. **Content is all broadcast.** Product announcements and blog links give people nothing to react to. Bluesky rewards people more than brands.
2. **Hashtags.** Five hashtags look like spam on Bluesky. Culture there is 0-2 tags, often none. `#cloud`, `#startup` and `#ai` are noise, and `#devops` and `#kubernetes` are crowded on other networks but barely used here.
3. **3 posts/day of the same type.** It trains followers to scroll past you. Frequency isn't penalized, but low-signal volume is.
4. **A small, wrong audience.** 140 followers is too few for likes to be a useful signal. Who the 140 are matters more than how many: bots and other brand accounts rarely engage.
5. **No replies.** There's no evidence the account answers or joins other people's threads, which is how small accounts get seen.

## Test it before you change anything

1. **Check visibility.** Search for one of your posts' exact text while logged out, or from a personal account that doesn't follow you. If it appears, you're not shadowbanned.
2. **Run a link-versus-text A/B for 2 weeks.** Alternate link posts and text posts, same topics, same hour, with fewer hashtags in both. Compare likes, replies and reposts per post. With so few likes, a sample under about 20 posts per arm tells you nothing, so don't stop early.
3. **Check who follows you.** Skim the 140. If most are bots or companies, the audience is the problem.

## What to do instead of going text-only

- **Don't go text-only.** Your goal is traffic and signups, and a link-free post can't deliver them. Put the insight in the post and the link at the end or in the first reply.
- **Cut hashtags to 0-2.** Use none on most posts. Drop `#startup`, `#cloud` and `#ai` altogether.
- **Post 1 a day, and make it a person's voice.** Write about a problem, a lesson, a chart, a code snippet, a question or a real opinion. Cap announcements at about one in four posts.
- **Reply to people.** Spend 15 minutes a day answering posts from engineers in your space. Small accounts grow this way.
- **Use Starter Packs and custom feeds.** Join or create a DevOps/Kubernetes starter pack, and get listed in relevant community feeds. Both are Bluesky's main discovery channels.
- **Put a human face on it.** Have a named engineer or advocate post from the account or alongside it. Bluesky developers follow people.
- **Set a realistic target.** Judge it by replies and follower growth from the right people, not likes. Revisit after 6 weeks.

## Decision

Keep links, but change the posts: fewer hashtags, fewer announcements, more voice, plus replies. Run the A/B test to settle the link question with your own data.