**Not reasonable as planned. Reasonable in six weeks if staged.**

Don't transfer everything this week. Do hand over in stages before you leave.

## Why not this week

1. **Three weeks and five PRs is a short record.** The code was solid, but it tells you little about who they are. Nobody has yet seen how they handle a security report, a breaking change, or a hostile issue.
2. **The stakes are high.** About 2,100 dependents, some in logistics, means a malicious release spreads fast. EDI parsers sit on trusted business data.
3. **The pressure is a warning sign.** The 2024 xz-utils backdoor started the same way: a helpful new contributor, an exhausted solo maintainer, and accounts pushing to hand over control. I'm not saying quartz_hollow is hostile. Two "just give it to them" posts are not evidence of anything, though, so don't let them set your timeline.
4. **Some steps can't be undone.** Once a crate owner removes you, or the repo moves, your leverage is gone. As I understand crates.io, any owner can add or remove other owners, so check that before adding anyone.

## Plan: six weeks, about 1 to 2 hours a week

1. **Week 1: verify, then grant repo write access.**
   - Ask quartz_hollow for a public identity trail: other projects, a GitHub history older than three weeks, and a video call.
   - Give them merge rights, not keys. A revoked merge right costs you almost nothing.
   - Announce the handover plan in an issue. This answers the "project is dead" posts and sets the pace.
2. **Weeks 2 and 3: they run a release while you watch.**
   - They prepare the changelog and bump the version. You review and publish.
   - Turn on 2FA for everyone with access. Set up crates.io trusted publishing from CI if you can, so no long-lived tokens exist.
3. **Week 4: add them as a crates.io co-owner, with you still an owner.** Check how they handled the earlier release before doing this.
4. **Week 5: recruit a second maintainer.** Aim for two people who aren't both quartz_hollow. Ask a logistics company that depends on the crate, or someone already active in the issues. A single new owner just moves your single point of failure to them.
5. **Week 6: transfer the repo only if all of these hold.**
   - They shipped at least one release cleanly.
   - Two people can publish.
   - Credentials are documented.
   - Nothing in their behavior has bothered you.
6. **After you leave:** stay on as a dormant crates.io owner for about six months if you're willing. Use that role only as an emergency lever.

## If it doesn't go well

- Say so in the README and crate description, and mark it deprecated or seek co-maintainers elsewhere, rather than hand it to someone you don't trust. A clearly stated "unmaintained" is safer for dependents than a quiet takeover.
- You can also ask a trusted dependent or a community org to take it.

## Do this today

Post a short comment in the issue: "I'm stepping back in six weeks. Handover is staged. quartz_hollow gets merge rights now. Publishing rights follow after a shared release." Then message quartz_hollow to set up the video call.