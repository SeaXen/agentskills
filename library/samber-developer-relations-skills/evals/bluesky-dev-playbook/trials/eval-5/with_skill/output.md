# Bluesky plan for Sorrel: order of the three moves

## Direct answer

Do the starter pack second, do not do the DMs, and do not build the feed.

1. **Replies and domain handles first (weeks 0-2).** This is the compounding lever, and it is the prerequisite for everything else.
2. **Ask existing community packs to add your people (week 3).**
3. **Build your own starter pack (week 4 or later).** Make it a Rust community pack that includes a few of you. Don't make it a team roster. Announce it once, in a public post.
4. **Replace the 200 DMs with that announcement post.** Bluesky's rules treat bulk notifying messages as spam [Bluesky]. By default only people a user follows can DM them [Bluesky]. Most of your 200 targets would never see the message.
5. **Don't build your own feed.** Post into the existing Rust feed instead. Revisit only if you find no active Rust feed and a maintainer volunteers to own it.

## Assumptions

I couldn't ask questions, so these are the gaps I filled. Correct any that are wrong.

- Goal is an ongoing presence, not a one-day launch.
- The 6 team members will post under their own names, about 1 hour a week each.
- Rust developers are visibly on Bluesky. I couldn't browse live, so check this first (see verdict).
- Sorrel's messaging doesn't lean on AI or on collecting users' posts.
- You control a `sorrel` domain, and no account is verified yet.

## Verdict: Go

Go if the check below passes. Skip if it fails. A skip verdict is a valid output.

- **Check:** search the app for Rust feeds, Rust packs and recognizable Rust people. The platform notes list a Rustlang feed at about 320 likes. Counts move, so verify this live.
- **Condition:** at least one named person can post for an hour a week.

## Why each of your three moves lands where it does

| Your move | Verdict | Reason |
|---|---|---|
| Starter pack of 6 team members plus the project account | Reshape, then do it | A pack of staff is a "staff directory dressed as a community pack", the playbook's own bad example. Readers follow packs for the community, not for your org chart. |
| DM about 200 Rust people | Refuse | Bulk messages that notify users count as spam [Bluesky]. Most recipients can't receive them anyway [Bluesky]. Spam flags and block-list inclusion cost far more than 200 follows are worth [practitioner]. |
| Own Rust custom feed | Defer, probably never | It is a standing job, and you become its moderator. A Rust feed already exists, so build only if you find no active one and someone volunteers to own the matching rule. |

## Surfaces ranked for Sorrel

Ranked by value per hour.

1. **Replies in existing Rust conversations.** Social-proximity ranking favours replies from people near the reader [Bluesky].
2. **Inclusion in community Rust packs.** Members gained up to 85% more new followers [research]. This is an upper bound and favours accounts that are already popular.
3. **Posts into the existing Rust feed.** Check its description for its keyword or tag rule. If it names none, watch it for a week or ask the operator [practitioner].
4. **Your own starter pack.** Creators who listed themselves gained up to 117% more new followers, and those who didn't about 22% [research].
5. **Project-account release posts.**
6. **Your own feed.** Last, and only if the starved-option condition above is met.

At about 3k stars you have some name recognition. That makes rungs 1-3 faster, but it doesn't change the order.

## Accounts and identity (week 0)

- **People first.** The 6 core members post under their own names. The `sorrel` account is a hub: release posts, reposts of their teaching posts, support answers [practitioner].
- **Domain handles.** Use `sorrel.dev` (or your domain) for the project and `name.sorrel.dev` for each person. Set them with a DNS TXT record on `_atproto` whose value is `did=<DID>`, or with `/.well-known/atproto-did` [Bluesky].
- **Blue check.** Apply only after handle and display name are final. Never promise it. Bluesky grants it at its discretion [Bluesky]. Renaming afterwards drops it [Bluesky].
- **Access.** Anyone with shared access to the project account uses their own app password, with 2FA on [practitioner].
- **Bios.** Name the person and "maintainer at Sorrel" in each bio.
- **Pinned post** on the project account.
- **Disclosure line** ready: "I work on Sorrel."

## Dated cadence

Today is Sat 2026-10-31.

| When | Step |
|---|---|
| Nov 2-8 (week 0) | Handles, bios, pinned post. Each person saves searches for Rust terms (search filters by keyword, people, date and language [Bluesky]). Run the Rust-presence check from the verdict section. |
| Nov 9-22 (weeks 1-2) | Each person replies daily to what those searches and the Rust feed surface. No Sorrel links unless asked. |
| Nov 23-29 (week 3) | For each relevant community pack, ask the curator to consider one named person. Do it as a public reply first, with a reason the pack's readers gain. Never ask for the whole team. |
| From Nov 30 (week 4+) | A few original posts a week per person. Release posts on the hub. Post into the Rust feed using its tag. |
| Around Dec 7 | Build your own pack from Rust people you now actually talk with. Ask each one first. Announce it once in a normal post. |
| Monthly | Check block-list inclusion and labels on your accounts. Drop surfaces that returned nothing. |

## Your starter pack, done right

- **Scope:** "Rust people", with the web and backend crowd as the angle.
- **Size:** about 40 community people. The cap is 150 people and 3 feeds [Bluesky].
- **Your team:** the 6 members plus the project account are a small minority, not the pack's point. Add the Rust feed as one of the 3 feeds.
- **Consent:** ask everyone before adding them. Unconsented additions draw complaints [research].
- **Money:** never take or give payment for placement. Unlabelled paid placement is undisclosed commercial content [Bluesky].
- **Blocks:** blocking the pack's creator removes someone from it [Bluesky], so respect that.

## Limits that bind

| Limit | Kind | Source |
|---|---|---|
| Starter pack: 150 people, 3 feeds | enforced | [Bluesky] |
| Pack membership is the curator's call | policed | [Bluesky] |
| DMs: only accounts a user follows, by default | enforced | [Bluesky] |
| Bulk notifying interactions are spam, no published threshold | enforced | [Bluesky] |
| Write budget: 5,000 points/hour, 35,000/day | enforced | [Bluesky] |
| Feed entry rules and exclusion | policed by operator | [practitioner] |
| Block lists and labelers can list your accounts | policed | [Bluesky] |

The write budget is not permission. Bulk interactions count as spam far below it.

## Drafts

These are drafts for the named person to rewrite in their own voice. Don't post them as written.

**Reply to a pack curator (public, one person per ask):**
> Hi [curator], thanks for the Rust people pack, it's how I found half my timeline. Would [name] ([name].sorrel.dev) fit? They post weekly about [topic] and answer questions in the Rust feed. No worries if the pack's scope is different.

**Your pack:**
> Name: Rust in production
> Description: People who ship Rust for real and post about it: web, backend, library authors. Plus the Rust feed. Suggestions welcome in replies.
> Members: about 40 community people, a few from Sorrel.

**Announcing it, once, in a normal post:**
> Made a starter pack of people who ship Rust in production and post about it. About 40 people, mostly not us. Who's missing?
> [pack link]

**Reply with a disclosure:**
> (Disclosure: I work on Sorrel.) For your case [specific advice]. You only need a framework once [condition].

**Feed post:**
> Wrote up why [Sorrel design decision], with the code. #rustlang
> [link]

Check the Rust feed's description for its real tag before using `#rustlang`.

## Metrics

Bluesky shows no impression counts [practitioner]. Measure what is observable:

- Replies, reposts and quotes per post and per person, not likes alone.
- Follower change in the week after a pack inclusion or feed post. Pack creators are notified only when a new user signs up through the pack [Bluesky], so pack-driven follows are an estimate, never exact attribution.
- Referral sessions with referrer `go.bsky.app` [Bluesky], plus UTM-tagged links, against a pre-launch baseline.
- Count of block lists and labelers listing your accounts. Any increase after a post is a stop signal.
- Never report raw follower totals as the headline.

I could not browse live, so the Rust feed's like count and tag rule come from the playbook's notes. Re-check them before acting.