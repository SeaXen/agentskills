# Velarion Go SDK on Bluesky: paid posts and Mastodon mirror

**Short answers**
1. ❌ **Paid posts without disclosure: don't do it.** Bluesky bans undisclosed commercial content. Disclose, and keep the posts organic by letting each developer write their own honest take.
2. ⚠️ **Copy-every-toot script: I won't write the unattended version.** Use the opt-in Bridgy Fed bridge. I can sketch a constrained original-posts-only script if the bridge doesn't work for you.

## 1. Paid posts

**Verdict: disclose.**
- Undisclosed sponsored or affiliate content is banned on Bluesky **[Bluesky]**.
- The Community Guidelines also ban artificially manipulating social signals **[Bluesky]**. Three paid accounts posting in the same window, with staff liking and reposting, looks like exactly that.
- Reports and block lists spread on Bluesky. A hidden paid campaign that gets spotted costs more than a labelled one.
- My own reading, not a Bluesky rule **[practitioner]**: consumer-protection regulators in the US, UK and EU also expect paid endorsements to be labelled. Check with counsel for your jurisdictions.
- Free access or swag can also count as a material connection. Disclose that too, to be safe.

**How to keep it organic while disclosed**
- Pay for the work, not for a verdict. Say in writing that they may criticize the SDK and that you won't approve copy.
- Each developer writes their own post, in their own voice, with a real use case or a real gripe. No shared script, no matching hashtags, no same-hour posting.
- Use a short disclosure line, for example: "Sponsored by Velarion; they paid for this post." Make it part of the post, not buried in a reply.
- Don't ask staff or Discord members to like or repost. Staff may answer questions in replies, with the "I work at Velarion" line.
- Drop paid posts for any of the three who aren't active in Go conversations on Bluesky. Reach there comes from replies, packs and feeds, not from a big follower count.

**Draft posts.** These are drafts for each named person to rewrite in their own voice. Never post them as written.
```
Sponsored by Velarion; they paid for this post, and I told them I'd say what I actually think.
I tried their Go SDK on <real task>. What worked: <specific>. What bit me: <specific>. Code: <link> #golang
```

## 2. Mastodon to Bluesky

**Recommendation: use Bridgy Fed, not a copy script.**
- The playbook lists an unattended mirror as a refused move. Replies make no sense off-platform, and dropped alt text and broken links read as "nobody home" **[practitioner]**.
- Mastodon posts run up to 500 characters (typical default). Bluesky's limit is 300 graphemes, and links are shortened in the composer **[Bluesky]**. A naive copy truncates or fails.
- A script that posts on its own is an automated account. It must carry the bot label, and it may like, repost or reply only when someone tags it **[Bluesky]**.

**Bridgy Fed setup [practitioner: Bridgy Fed's own docs]**
1. From the fosstodon account, follow `@bsky.brid.gy@bsky.brid.gy`. That opts in.
2. Test that the bridge works from your instance. Some instances block it.
3. Bridged posts then appear on Bluesky under a bridged handle. Check the exact handle format in their docs, and note it is not a native domain-handle account.
4. Replies from Bluesky users who haven't bridged reach you only as an hourly DM digest. Someone must still read Bluesky directly.

**Limits of the bridge:** it gives you a presence, not a Bluesky-native brand. The bridged account can't have your `velarion.com` handle or the blue check. Native accounts are what feeds, starter packs and verification work with. So bridge as a stopgap if you want, but build the real presence below.

**If you still want a script (constrained spec)**
- Copy original toots only. Skip replies and boosts.
- Rewrite to under 300 characters, with a link to the full toot or post.
- Carry over alt text. Skip toots whose images lack it, or add it by hand.
- Own handle, "bot" in display name and bio, the human operator named, bot label on.
- Don't use it for engagement actions. A named person reads Bluesky replies daily, or the mirror gets switched off.

## Go or skip

**Go**, assuming the Go community is visible on Bluesky and someone can post as a person at least an hour a week. Check this first: search for Go people and the golang feed. The golang feed had about 140 likes when last checked, so reach is modest.

If the SDK is AI-forward or collects user data, go small instead: one person, replies only.

## Account and handle plan
- Brand: `velarion.com`, set with a DNS TXT record on `_atproto` with value `did=<DID>`, or the `/.well-known/atproto-did` route **[Bluesky]**.
- People: `name.velarion.com` for the staff who post.
- Apply for the blue check only once handle and display name are final. Don't promise it **[Bluesky]**.
- People first. The brand account reposts their teaching posts and announces releases.

## Surfaces, ranked for you
1. Replies in existing Go conversations. They compound.
2. Inclusion in Go community starter packs, by asking curators. Members gained up to 85% more followers, an upper bound that favours already-popular accounts **[research]**.
3. Posts to the golang feed, only if it states a tag rule, or after you ask its operator.
4. Your own pack, built from community people you have talked with, each asked first, announced once.
5. Brand release posts.

## Cadence (relative to the launch date, which I don't have)
1. **Week 0:** domain handles, bios naming person and employer, pinned post, disclosure line ready.
2. **Weeks 1-2:** the Velarion engineers reply daily in Go threads. No product links unless asked.
3. **Week 3:** ask each relevant pack's curator, in a public reply, to consider one named person.
4. **Launch day:** the engineer who built it posts. The hub reposts. The three sponsored posts go out as staggered, labelled, individually written posts. Staff answer questions and don't mass-like.
5. **Monthly:** check block-list inclusion and labels on your accounts. Drop surfaces that returned nothing.

## Limits that bind
- Starter pack: 150 people and 3 feeds; the curator decides; enforced for size, policed for who **[Bluesky]**.
- Bots: scheduled posts are fine, interactions only when tagged **[Bluesky]**.
- Write budget of 5,000 points per hour is not permission; bulk interactions count as spam far below it **[Bluesky]**.
- Sponsored disclosure is required; enforced **[Bluesky]**.

## Metrics
- Replies, reposts and quote posts per post, not likes alone.
- Follower change in the week after a pack inclusion or feed post.
- Referral sessions and signups from `go.bsky.app`, plus UTM links, against a pre-launch baseline.
- Count of block lists listing your accounts. An increase after a post is a stop signal, and a sponsored campaign is the likeliest cause.
- Don't report raw follower totals as the headline.

## Questions that would change this
- Is the SDK AI-forward or does it collect user data? That moves Go to Go small.
- Which three developers, and are they already active on Bluesky?
- What is the launch date?
- Does the bridge work from fosstodon? That decides whether you need the script at all.