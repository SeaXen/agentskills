# Orbitkit on Medium: paid writers vs a sponsored post, and Priya's departure

I read `SKILL.md`, `references/limits-and-publications.md` and `references/templates.md` in full. I couldn't browse, so every rule below is as the skill states it. Re-read Medium's Distribution Guidelines, Rules and AI policy before you commit money. Labels: **[platform]** means Medium states it. **[practitioner]** means writer or publication reports. "Own reasoning" is mine.

**Assumptions** (they change the answer if wrong):
- Your four writers write in English.
- The sponsored post would run inside a Medium publication.
- Orbitkit has no canonical blog on Medium today.
- Your budget is the $1,200 you named.

## 1. $1,200 sponsored post vs four $300 community articles

**Verdict: the four articles, as a pilot with changes. Decline the sponsored post if it runs inside a Medium publication.**

I can't give you a numeric ROI. You gave me no traffic, signup or follower data, and Medium publishes no vendor benchmark. I can say which option is allowed and which has a measurable payoff.

Both options cost $1,200, so the comparison is about rules and reach, not price.

### Sponsored post: don't buy it on Medium

- A sponsored post promoting your product inside someone else's Medium publication is **third-party advertising, banned** [platform].
- Sponsored content also gets **Network distribution only** (the publication's followers) [platform].
- So you'd pay $1,200 for a ban risk and a reach cap.
- Medium sells no ads and no boosts, so no paid route exists on-platform [platform].

Ask the publication one question first: does the sponsored post live on Medium or on the network's own site?
- **Own site** (for example, In Plain English sells sponsored placements through a paid marketplace on plainenglish.io) [practitioner]: it sits outside Medium's rules, so the ban doesn't apply.
  - Get in writing that it won't be syndicated into their Medium publications.
  - The payoff is one-shot. Measure it with UTM links and compare it to the writer arm below.
- **Medium publication:** decline.

### Four writers at $300: allowed, with conditions

Paid writers on their own accounts are allowed if each piece stands on its own and the writer discloses what they received [platform]. These rules decide whether the money works:

| Rule | What to do |
| --- | --- |
| Disclosure | Each writer states in paragraph one that Orbitkit paid them. Template: "Orbitkit paid me for this post; the SDK limits section covers where it falls short." |
| Strip-the-product test | If nothing worth reading remains without "Orbitkit", the piece gets followers-only reach [platform]. Brief writers on a real project, a migration, or a benchmark they ran. |
| No templated near-duplicates | Templated near-duplicate posts are spam [platform]. Give each writer a different angle: for example migration from a homegrown flag system, React integration, testing with flags, and an incident story. |
| No AI-generated drafts | Majority-AI text gets no General distribution and no Boost, even when labelled [platform]. AI assistance needs a label in the first two paragraphs. |
| No engagement on cue | No asking friends or the team to clap, follow or respond. Bought reads and brigades are banned [platform]. |
| English | Curators review English stories only [platform]. |
| Rights | Writers keep all rights. Never require republishing rights as a condition of the fee [platform]. |
| Paywall | Off. Paywalled vendor stories are hidden from non-members, and the Partner Program pays on member activity only [platform]. |

Honest limit: a paid piece may be treated as content marketing and get Network distribution (own reasoning). Reach then equals the writer's follower count, so the first article from each writer is the test.

### How to decide on ROI

Define one metric before anyone writes: **cost per referral session and per signup**, from UTM-tagged links to your canonical page, read in your own analytics. Medium allows no tracking scripts [platform].

For each article, record:
- presentations compared with the writer's followers,
- reads, read ratio, and followers gained,
- referral sessions and signups,
- cost per signup = $300 ÷ signups.

Run the same arithmetic on the sponsored option if it's off-Medium ($1,200 ÷ signups). Set your pass threshold now, not after the numbers arrive. Pay the first fee for each writer as a pilot. Renew the writers whose stories show presentations well above their follower count.

### Free route to the same publication

Have your writers submit their finished stories to that JavaScript publication, following its guidelines. Open publications accept 3 active guest submissions per writer [platform]. A call to action to an open-source project at the end is typically acceptable. Ask the editor before linking a paid plan or trial. This costs nothing beyond the writers' time.

## 2. Priya's 12 imported posts

**Yes, act this month.** The skill says a company publication must be owned by a company-controlled account with a paid membership, never a departing engineer's [platform]. Nothing here is urgent if the posts are healthy. It becomes urgent if Priya owns the publication, or if her membership pays for it.

### Order of work (about 2-3 hours total)

1. **Find out who owns "Orbitkit Engineering"** (about 15 min). Check the publication's settings > Editors.
   - If Priya is the owner, add a company-controlled account as editor and move ownership to it. That account needs a paid membership, because owning a publication requires one [platform].
   - I couldn't verify Medium's exact ownership-transfer steps. Confirm the flow before her last day.
   - Also confirm whose paid membership currently covers the publication, and what happens to it when her card lapses. The skill doesn't say.
2. **Get the retention agreement in writing** (about 30 min, before her last day).
   - Terms: stories stay up, free (no paywall), and in the publication. Canonicals stay on the company domain. Imports are done only by named authors with company permission.
   - Put this in her employment or IP terms, not as a condition of the publication.
   - Each story stays under the author's control. Editors may not delete a story or remove it from the paywall without the writer [platform], so Priya's cooperation is the only lever you have.
   - Ask her not to delete, unlist or re-import any of the 12.
3. **Audit all 12 stories** (about 1 hour). For each, apply the "Canonical check before publishing" list from the templates:
   - Story settings > More settings > Advanced settings shows the original company URL.
   - The published page source contains `rel="canonical"` pointing at the company domain.
   - The paywall toggle is off.
   - Topics are chosen (max 5) and still fit.
   - The story is submitted to the publication.
4. **Check the publication's submission settings.** The recommended mode is Approved writers only, accepting published stories, with "paywalled" left off as a condition [platform]. Link a guidelines page. A draft is in the templates ("Write for Orbitkit Engineering").
5. **Do not re-post the 12 under another account.** Medium allows one copy; duplicates across accounts cause suspension until fixed, permanent on repeat [platform]. The stories stay under Priya's byline. Your canonical on the company domain is the copy you control.
6. **Name the next owners.** Assign two or more named engineers who import future posts under their own accounts and submit to the publication. Boost weighs first-hand experience, which a brand account cannot show [platform].
7. **Ask Priya to export her Medium data** (settings > download) as a backup. I haven't verified that the export covers everything.

### What this does not fix

Priya's followers are hers, not the publication's. Expect the followers-only reach on her 12 posts to stay as it is. The compounding asset is the publication's feed and your canonical URLs, not her profile.

## Suggested plan: next 8 weeks

| Weeks | Owner | Hours/week | Action |
| --- | --- | --- | --- |
| 1 | DevRel lead | 3 | Ownership transfer, retention agreement, 12-post audit (section 2) |
| 1 | DevRel lead | 1 | Ask the JS publication where the sponsored post lives; set the signup-metric threshold |
| 1-2 | Writers | 1 | Brief writers: unique angles, disclosure line, no AI drafts, paywall off |
| 2-4 | Writers | ~1 | Pilot: first article per writer, UTM links to canonical pages |
| 3-6 | Named engineers | 1-2 | Earn-first responses (no links), import 1-3 more posts under their own names, feature the best one weekly |
| By 6 | DevRel lead + writers | 1 | Submit one finished story to the JS publication |
| 8 | DevRel lead | 1 | Read the numbers; renew or cut writers; decide on a native deep-dive |

If you have under 2 hours a week, keep canonical imports and responses only.

## Metrics

Targets are self-set, because Medium publishes no vendor benchmark.
- **Per story:** presentations, feed click-through, reads, read ratio, followers gained.
- **Business:** UTM referral sessions and signups, then cost per signup for paid pieces.
- **Reach flag:** presentations at or below follower count suggests Network-only distribution. This is a signal, not proof.
- **Hygiene (must be zero):** AI-generated or unlabelled stories, teasers, duplicates, paid placements inside Medium publications.
- Leave each author's third-party AI setting on the default "Prioritize maximum reach" [platform].

## Questions that would change this answer

1. Does the sponsored post run inside a Medium publication or on the network's own site?
2. Who owns the publication, and whose membership pays for it?
3. Are your four writers' followings above 1,000? If not, expect followers-only reach and low yield.
4. Do the 12 posts pass the strip-the-product test? If most don't, the "backbone" has little reach regardless of ownership.