# Why Basalt's Medium posts stall at about 40 views, and what to do

**Caveat:** I used the playbook's rules as written and did not re-check Medium's pages. Medium rewrites these rules often, so re-read the Distribution Guidelines, AI content policy and Medium Rules before this goes to your VP. Labels: **[platform]** means Medium states it. **[practitioner]** means writer reports. Anything else is my own reasoning.

## One-paragraph version for the VP

Medium is not ignoring us by accident. Its rules give limited reach to what we publish. We publish product announcements and competitor comparisons from a brand account. The drafts are mostly AI-written, half are in Portuguese, we tag five loosely related topics, and we @mention about 25 people per post. Each of these on its own keeps a story at "Network" distribution [platform]. Network means our roughly 300 followers and nobody else. 40 views is about 13% of 300 followers, which is what Network-only looks like. Fixing one cause won't help, because the others still cap the story. The fix is a different kind of story from different authors.

## Diagnosis: five caps, each sufficient alone

| # | What we do | Medium rule | Effect |
|---|---|---|---|
| 1 | "Announcing Basalt 2.3", "Why Basalt beats RDS", each ending in a trial link | Content marketing, PR pieces and stories whose primary point is signups get Network only. Test: strip the product name; if nothing worth reading remains, it is content marketing [platform]. | Followers only. Both example titles fail the test. |
| 2 | ChatGPT draft, light edit | Majority-AI text with little editing is low-value: no General distribution, no Boost, labelled or not, and never paywalled [platform]. Unlabelled AI-assisted text also drops to Network only [platform]. | A label doesn't fix it. A rewrite does. |
| 3 | Half the posts in Portuguese | Curators review English stories only. Other languages get no Boost and no General distribution [platform]. | Those posts can only reach followers. |
| 4 | About 25 @mentions per post | The guideline's example of a mass mention is 20 users. Such stories lose General distribution [platform]. | We are over the example threshold. |
| 5 | Topics: Technology, AI, Startup, Productivity, Programming | Up to 5 topics, each one the story is actually about. Off-topic topics chosen for reach are penalised [platform]. | A managed-Postgres post is not about AI, Startup or Productivity. Topic matching only happens in General distribution anyway [platform]. |

Two aggravating factors:
- **Brand account.** Boost rewards a writer's first-hand experience, which a brand account cannot show [platform].
- **Possible new-account indexing delay.** New or untrusted accounts are held out of search "days to weeks" [platform]. I don't know how old the Basalt account is.

## How sure am I

- 🟠 **Strong inference, not proof.** Presentations at or near follower count suggest Network only. The playbook calls this a signal rather than proof.
- **Confirm before the meeting:**
  1. Open the traffic-source split on a few stories.
  2. Check that none predate 2025, because older stories show no presentations [platform].
  3. Compare an English post with a Portuguese one. If the Portuguese ones are lower still, cap 3 is confirmed.
- **Can't separate the causes from stats.** All five lead to the same observable result, so I can't say which matters most. Don't tell the VP a ranking.
- **Presentations high but views low** would mean a title, subtitle or cover problem instead. Your numbers say the opposite.

## Fit verdict

Today the playbook's verdict is **Skip**: only product announcements, AI-generated drafts and non-English stories get followers-only reach at best.

To change that to **Invest** or **Syndicate only**, three things must be true:
- Named engineers write.
- Original posts live on a Basalt blog with a canonical URL.
- Someone answers responses within two days.

If those can't be met, put the hours elsewhere and keep Medium for release notes.

## Account model

1. **Named engineers publish under their own accounts.** Boost weighs first-hand experience [platform].
2. **Two or more writers: create a Basalt Engineering publication.** A company-controlled account with a paid membership must own it, never a departing engineer's [platform].
3. **Sign a retention agreement before the first import.** Put it in employment or IP terms, not as a publication condition:
   - Engineers may import company posts.
   - Canonicals stay on the Basalt domain.
   - On departure, stories stay up, free and in the publication.
4. **Keep the brand account for release notes only.** Write them to be useful without the product link, and expect followers-only reach.
5. **Keep the canonical original on the Basalt domain.** It is the copy you control.

## What to change, ranked by value per hour

| Order | Surface | Hours | Note |
|---|---|---|---|
| 1 | Canonical import of an existing Basalt blog post under a named engineer, submitted to the publication | under 1 | Default rung. Only posts that pass the strip-the-product test qualify. |
| 2 | Substantive responses on others' Postgres stories, no links | under 1 per response | Earn-first. Use it to build the profile before publishing. |
| 3 | Basalt Engineering publication, one featured story a week | about 1 per story | Featured stories get reviewed for Boost first [platform]. |
| 4 | Submission to an established tech publication | high | Rates well only if the publication accepts published stories. |
| 5 | Native first-hand deep-dive | a day or more plus review | Highest value, highest effort. See the note below. |
| 6 | Brand-account release note | low | Followers-only reach. |

Notes on this table:
- **Deep-dive:** promote it only if you have a real incident, migration or benchmark story and a named engineer to own it.
- **No paid amplification:** Medium sells no ads, and bought traffic harms a publication's standing [platform].
- **Limited time:** under 2 hours a week means imports and responses only.
- **Launch date or compounding goal:** a launch promotes the established-publication submission, and a compounding mandate promotes the deep-dive.

## Hygiene rules, starting now

- ❌ Stop AI-generated drafts. A rewrite means a human telling a first-hand story. If AI assisted, label it in the first two paragraphs. Grammar, outline and fact-check tools need no label.
- ❌ Stop product-first and "X beats Y" posts on Medium. Competitor comparisons stay on the Basalt blog.
- ❌ Stop mass mentions. Mention someone only when the story cites their work.
- ❌ Stop the five-topic default. Use only topics the story is about, for example PostgreSQL, Databases, Cloud Computing.
- ❌ Stop Portuguese posts as a Medium strategy. Your own translation is not a duplicate [platform], but it reaches followers only. Serve the Brazil community on your own channels.
- ⚠️ Disclose the trial link right next to it, for example "this link leaves Medium" [platform].
- ⚠️ Don't re-post, delete or unlist old stories to retry them. One copy on Medium [platform]. Leave the old stories up.
- ⚠️ Keep stories free. The paywall hides them from non-members, and the Partner Program pays only on member reading [platform].

## Eight-week cadence

Hours and owners are my assumptions, because you haven't given me the real ones. Replace them.

| Weeks | Action | Owner | Hours/week |
|---|---|---|---|
| 1-2 | Complete profiles. Each writer follows target topics and leaves a few substantive responses a week, no links (a self-set pace, not a platform rule). Sign the retention agreement. Create the publication. | DevRel lead plus 2 named engineers | 2-3 |
| 2-3 | Import up to three existing Basalt blog posts that pass the strip-the-product test, one every few days, each under its named author. If none pass, start a native story instead. | Engineers | 1 each |
| 3-8 | One story every one or two weeks. Feature the strongest each week. Answer responses within two days. | Engineers, DevRel lead | 3-4 |
| By week 6 | Submit one story to an established publication whose rules allow your call to action. Ask the editor first about any trial link. An open publication takes 3 active submissions per guest writer [platform]. | DevRel lead | 1 |
| Monthly | Read story stats. Drop topics that drew no presentations. | DevRel lead | 0.5 |

## Metrics

Targets are self-set, because Medium publishes no vendor benchmark.

- **Per story:** presentations, feed click-through, reads, read ratio (reads of 30 seconds or more over views), followers gained.
- **Baseline for the VP:** presentations versus writer plus publication followers. Today it is roughly 1:1.
- **Business outcome:** referral sessions and signups from UTM-tagged links back to the canonical page, read in Basalt's own analytics. Medium allows no tracking scripts [platform].
- **Boost badges** per quarter.
- **Hygiene, pass threshold zero:** AI-generated or unlabelled stories, teasers, duplicates, paid placements.
- **Author setting:** keep each author's third-party AI setting on the default "Prioritize maximum reach" [platform].

## Templates, adapted to Basalt

The facts in brackets are placeholders. Don't publish figures you haven't measured.

**Disclosure, first paragraph:**
> I work on Basalt, the managed Postgres service this post uses; the limits section covers where it falls short.

**Title and subtitle shape:**
```text
✓ How we cut [query/replica/failover metric] from [X] to [Y] on managed Postgres
  [what we tried, and the change that made it worse]

✗ Announcing Basalt 2.3
✗ Why Basalt beats RDS
```

**Earn-first response:**
```text
✓ We hit [specific failure] once [condition]; the fix was [change],
  which cut [metric] from [X] to [Y]. Did you try [option]?
✗ Great article! Basalt solves this, try it free: [link]
```

**Story skeleton:**
1. The incident or decision, in the first paragraph, with one number.
2. What you tried first and why it failed.
3. What you changed, with code blocks and your own diagram.
4. Results, measured, and what still doesn't work.
5. One call to action: the repo, the docs page, or the free tier. Disclose the offsite link.

**Canonical check before publishing:**
1. Advanced settings shows the Basalt URL as original.
2. Page source has `rel="canonical"` pointing at the Basalt domain.
3. Paywall off, topics chosen, AI label present if needed.
4. Submitted to the publication, and featured if it is the week's best.

## Questions that would change this plan

- **Hours per week and who answers responses** decide whether this is Invest or just imports and responses.
- **Where the originals live** decides whether imports are possible. Without a Basalt blog canonical, you write native stories or skip Medium.
- **Goal and date** decide whether to pitch an established publication early. A launch pulls that forward.
- **One-off push versus compounding asset** decides whether to go to deep-dives.
- **Whether you control a paid Medium membership** decides whether you can create a publication at all.