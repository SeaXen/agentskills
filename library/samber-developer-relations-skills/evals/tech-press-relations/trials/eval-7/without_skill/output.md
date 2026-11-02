Here's the sanity check on the Ashgrove 4.0 embargo plan. Four things need fixing before Thursday, ranked by how likely they are to blow the embargo early.

## 🔴 Critical — likely to leak before 14:00

**1. The changelog PR being open on the public repo right now.**
A public PR is visible to anyone browsing the repo — diff, branch name, commit messages, linked issues — regardless of draft status (draft only hides the merge button, not the content, on a public repo). If it mentions "Ashgrove 4.0," version numbers, or feature names, that's discoverable today by any bot or human scanning open PRs, weeks before Thursday. Bots that watch public repos for new PRs/tags (dependency bots, changelog scrapers, some journalists' own tooling) will find it.
- Fix: check right now whether the PR diff or title reveals anything embargo-sensitive. If it does, either close it and hold the branch unopened until go-time, or scrub the PR to a neutral title/description and keep the real content in a commit that gets force-pushed at 14:00.

**2. Docs site auto-deploying from `main`.**
Any merge to `main` — this docs PR or an unrelated one that happens to land first — ships instantly to the live docs site. There's no gate between "merged" and "public." If the Ashgrove 4.0 docs PR sits reviewed-and-approved waiting for Thursday, one accidental merge (wrong button, merge queue auto-merge, a teammate cleaning up PRs) is a full leak.
- Fix: don't merge the docs PR until 14:00. Don't leave it in a mergeable, approved state that someone could merge by habit. If your CI supports it, gate the deploy on a manual trigger instead of relying on nobody touching `main` for days.

**3. The pricing page flag in the marketing repo.**
"Merged behind a flag" means the code is already in production. Two leak paths: (a) if it's a client-side flag (LaunchDarkly-style SDKs commonly ship *all* flag payloads to the browser and just hide the UI), the page content or copy may be extractable from network requests even while "off." (b) if the route itself is reachable by direct URL regardless of flag state, it's not gated at all, just unlinked — and unlinked isn't the same as unpublished (crawlers, `sitemap.xml`, or someone guessing the URL will find it).
- Fix: confirm the flag actually blocks server-side rendering/response, not just nav visibility. Check the route returns 404 or is auth-gated while off, not 200 with hidden content.

## 🟠 Structural — no single "go" trigger

You have four independent release arms (git tag → npm CI publish, `main` merge → docs deploy, PR merge → changelog, flag flip → pricing) that all need to land at the same instant, each likely owned/executed by a different person. That's four chances for one to fire early or late relative to the others. There's no atomic switch.
- Fix: write an explicit sequence with one directly responsible person per step and a shared "go" signal (a timestamp in UTC, not "when you wake up"). Suggested order: flip pricing flag → merge docs → merge changelog → push tag (tag push is the most public, instantly-discoverable action via the npm registry, so it goes last). Do a dry run of the sequence on a private/test repo if you haven't already.

## ⚠️ "Thursday morning" vs. 14:00

This is the one most likely to bite you specifically because you already know about it and haven't fixed it. "Morning" told to a team spread across timezones means someone will reasonably read it as their own local morning — which could be hours before 14:00 in whichever timezone 14:00 is anchored to. If anyone on the technical side merges, tags, or flips a flag based on their own "morning," the whole embargo breaks regardless of what the reporters were told.

- Fix now: re-send the actual instant as an unambiguous absolute time — ISO 8601 with UTC offset (e.g., `2026-XX-XX 14:00 CEST / 12:00 UTC / 08:00 EDT`) to every internal person with a release action, not a relative description.
- Check what the *reporters* were told, separately. If they also got "Thursday morning," the same ambiguity applies to them, and an eager reporter in an earlier timezone publishing "in the morning" their time could break embargo for the other five before your 14:00. Standard embargo language is an exact instant with timezone, sent explicitly, not "morning." Re-confirm this with all six in writing if there's any doubt.

## ⚠️ The unvetted reporter

Six reporters "agreed to hold it" is good — that's the norm for embargoes. But one is someone you've never worked with, who reached out cold a week ago. Embargo trust is usually built on track record; a stranger's cold inbound a week before a major release is outside that norm and worth treating differently, not necessarily excluding.
- Check their byline history and outlet before trusting them with early access — a quick search confirms whether they're a real, known publication.
- Get explicit written confirmation of the exact embargo instant (see above) from them specifically, not just an "ok" to a vague ask.
- Have a fallback: if you can't verify them in time, give them the same materials at 14:00 alongside the public release instead of pre-embargo — no relationship is damaged, and it removes the highest-variance name from your pre-release list.

## One more thing to decide

What's the contingency if the embargo breaks anywhere (leak, or one reporter jumps early)? Standard practice: the moment it breaks publicly, you notify the other five immediately and lift the embargo for everyone — nobody waits to be scooped. Have that message pre-drafted, and let the six reporters know upfront that's the deal, so nobody's surprised.