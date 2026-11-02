**Short answer:** do the rebrand, but sequence it carefully. Skip the competitor and "alternative" handles.

## 1. Rebrand: you will probably lose the blue check

- Rename **and** change the display name in one step. Bluesky's Guidelines ban "identity churning", but one announced rebrand reads as legitimate and repeated renames don't. [Bluesky] for the ban, [practitioner] for my reading of the one-rebrand case.
- A verification only holds while the handle and display name match what they were at issue time. Moving to a domain handle counts as a change. I expect the badge to drop until you're re-verified. [Bluesky protocol spec; practitioner reports]
- I didn't re-check this against Bluesky's live pages. Read their verification page before the switch, and plan on re-applying.
- Don't promise anyone the badge will come back. Bluesky verifies "notable and authentic" accounts at its own discretion. [Bluesky]

**Order of steps:**

1. **Before the switch:** add the DNS TXT record `_atproto.nimbuscloud.com` with value `did=<your account's DID>`. Alternatively, serve `/.well-known/atproto-did` over HTTPS. [Bluesky] Confirm `nimbuscloud.com` is controlled by the company, and by someone who won't let it lapse. Handles revalidate periodically, so an expired domain or a moved file invalidates the handle.
2. **Pick the final display name** ("Nimbus Cloud") and the final bio before you change anything. Rename once, and don't tweak the display name afterwards, because each change is another identity change.
3. **Switch the handle and the display name together** to `nimbuscloud.com` / "Nimbus Cloud".
4. **Apply for verification through Bluesky's form** only after both are final.
5. **Pin a post** announcing the rebrand, and keep "formerly NimbusDB" in the bio for a while.
6. **Followers stay,** because identity is the DID. Old mentions keep resolving, and `nimbusdb.bsky.social` stays reserved after the switch. [Bluesky]
7. **Update every place that links to the old handle:** website, docs, staff bios and the X/Mastodon bios.
8. **Do staff subdomains in the same pass.** Use `name.nimbuscloud.com` handles for the people who post. Each one needs a TXT record, or a well-known route answering on that subdomain. Staff handles are the strongest anti-impersonation signal you have.

If you have trusted-verifier or labeler setups tied to the old name, check those too.

## 2. Registering extra handles: don't

- **Competitor-name handles are banned.** The Community Guidelines prohibit handle-squatting and impersonating brands. [Bluesky] "Register it so nobody squats it" is the same act when the name isn't yours. Your newly verified-looking account would carry the risk. I haven't verified whether a suspension of the spare accounts would affect the main one, but I wouldn't test it.
- **`planetscale-alternative.bsky.social` is the same problem.** It uses a competitor's trademark in the handle. That reads as brand impersonation or a squat even though it's a positioning phrase. It's also a second account someone must run. An empty account with no named person looks abandoned or like a squat, and brand accounts with no human behind them are the weakest setup.
- **If you want to own "PlanetScale alternative":** do it with posts, replies, feeds and your site, not a handle.
- **For defensive protection of your own name,** a domain handle is the protection. Only you control `nimbuscloud.com`, so nobody else can hold it as a handle. You can't stop someone taking `nimbuscloud.bsky.social`, and you don't need to. Report impersonators if one appears.
- **Optional:** claim an extra name you actually run, such as a bot account (`release-bot.nimbuscloud.com`). Turn on the bot label and name the human operator in the bio.

## 3. Other things to watch

- **Team access.** If several people run the brand account, give each person and tool its own app password with 2FA on, so access stays revocable.
- **Handle rate limits are not a concern here.** Handle changes allow 10 per 5 minutes and 50 per day. [Bluesky]
- **Don't announce the rebrand with a mass DM or an ask to like and repost.** Announce once in a normal post. Staff replying is fine; staff mass-liking is not. By default only people a user follows can DM them anyway.
- **Metrics:** note the follower count and referral baseline before the switch. If the badge drops, you can see whether it moved anything.

**Confidence labels:** the squatting and churning bans and the follow/DM rules are [Bluesky]. The badge-drop on rename is [Bluesky protocol spec; practitioner], not a verified current policy. My reading of "one announced rebrand is fine" is [practitioner].