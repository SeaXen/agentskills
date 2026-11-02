**Verdict: not a good plan.** Three of its four moves are banned or backfire. The canonical import is the right first step. Keep it and change the rest.

## What breaks

1. **Same story to ITNEXT and Level Up Coding at once.** Medium allows one copy of a story. A story in two publications counts as a duplicate, and the penalty is suspension until you fix it [platform]. It is permanent on repeat. You get one shot per story, not two.
2. **Unlist, then republish with a punchier title.** Re-posting after unlisting is banned [platform]. The same one-copy rule applies. If views are low, fix the title, subtitle or cover on the existing story instead.
3. **8 people clapping 50 times in the first hour.** This is coordinated engagement, which Medium bans. Medium weighs each reader's claps against that reader's own habit, so eight sudden 50-clap bursts stand out [platform]. A clap ring can also bury the story. If you are in the Partner Program, it can cost you that too, "without notice or the option to appeal."
4. **"Kick the algorithm."** Reach comes from human curators, not early clap velocity [platform]. A curator who sees a clap ring will not boost the story.

## Plan to run instead

**Fit: Syndicate, moving to Invest.** You have a blog and 4k stars, so import first. Move to native Medium stories once imports draw followers. This assumes your posts are English and first-hand engineering stories, not release notes. If a post is a release note, it gets followers-only reach at best.

**Account:** Publish under your own profile, with no publication. You are an open-source maintainer, not a company. A publication only makes sense if two or more of the 8 write regularly, and it needs a paid membership.

**Steps:**

1. **Now, 20 min:** Read the current ITNEXT and Level Up Coding guidelines. Their self-promotion and submission rules change without notice. Level Up Coding's published guide is old (email a draft link). ITNEXT's rules need a fresh read. Either may demand an original instead of a published post. If so, write a native story for that publication and do not import.
2. **Pick one publication,** whichever fits your topic best. Do not run both in parallel. If the first declines, I would expect you can try the second. That is my own reasoning, not a platform rule. Confirm with Medium's help center before relying on it.
3. **Import, under 1 hour:** Use Stories > Import a story. The canonical link and original date set automatically. Your blog stays the canonical copy.
4. **Before publishing:**
   - Title says what happened, not "Introducing quill-rs X".
   - Up to 5 topics, each one the story is actually about.
   - Paywall off.
   - Add an AI label in the first two paragraphs if AI drafted the text.
   - Add an affiliation line only if one applies.
5. **Publish, then submit** to the one chosen publication. Feature the story. You get 4 featured credits to start, and featured stories get reviewed for Boost first.
6. **What the other 7 can do:**
   - Read it normally, and clap only as they genuinely would.
   - Leave real responses on other people's Rust and parser stories. Add a fact, use no link, and never use responses to point at your story.
   - Email your own opted-in subscribers on publish.

**Cadence if the post is soon:** An account that is new to Medium is held back from search indexing for "days to weeks" [platform]. Spend one week leaving a few substantive responses on Rust stories before importing. If the post cannot wait, import anyway and expect slow search pickup.

## Template: pitch to the editor

Use the publication's own form or email.

```text
Subject: Submission - "{title}"

Hi {editor name},

I maintain quill-rs, a Rust parser combinator library. This post covers
{one concrete problem, one number}. About {N} words, {N} diagrams.
It was first published on my blog, with the canonical link set to it.

It mentions quill-rs once, in the closing paragraph, linking the
open-source repo. Happy to drop that line if it breaks your guidelines.

Draft: {Medium link}
{name}
```

Delete the "first published on my blog" line if the publication requires an original.

## If it flops

Diagnose the story, not the platform:

1. Compare presentations with your follower count. Presentations at or below your followers suggest Network-only distribution. This is a signal, not proof.
2. Presentations high but views low: fix the title, subtitle or cover.
3. Views high but reads low: the opening does not deliver on the title.
4. Leave the story up. Never re-post it. Apply the lesson to the next one.

## Metrics

Targets are self-set, because Medium publishes no vendor benchmark.

- Presentations, feed click-through, reads, read ratio, followers gained.
- Referral sessions to the canonical page, read on your own analytics. Medium allows no tracking scripts, so tag links with UTM parameters.
- Hygiene, pass threshold zero: duplicates, clap-ring behaviour, unlabelled AI text, teaser posts, paid placements.

**Next (2 min):** Open the ITNEXT guidelines page and tell me whether it takes published stories or only originals.

**One open question:** When is the launch date? A fixed date moves the publication submission up. No date means build the standing channel first.