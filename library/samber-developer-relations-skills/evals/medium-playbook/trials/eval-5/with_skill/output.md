# Lattice Engineering on Medium: what to fix

I couldn't re-read Medium's live rules, so this rests on the playbook's snapshot. Tags: **[platform]** means Medium states it, **[practitioner]** means writers' or owners' reports, and "own reasoning" is mine.

## Verdict

All three next steps need changing. Step 1 is a program that doesn't exist, step 2 targets a publication that left Medium, and step 3 can't do what marketing wants. The publication has one more problem: its owner has no paid plan.

| # | What you were told | Problem | Fix |
|---|---|---|---|
| 0 | Owner is the brand account with no paid plan | Creating a publication needs a paid membership, and one user owns up to 7 [platform]. The owner either has no plan or let it lapse. A custom domain and the Partner Program also need membership. | Put a paid membership on the owner now. Keep the owner company-controlled, never a single engineer's account. |
| 1 | Apply to a Boost Nomination Program so the editor can nominate posts | Medium no longer lists a nomination program. Curators use internal tools, and featured stories are reviewed for Boost first [platform]. Boost also rewards a writer's first-hand experience, which a brand account can't show [platform]. | Don't apply. Have named engineers publish under their own accounts, then feature one story a week (see below). |
| 2 | Submit our best piece to Towards Data Science | TDS left Medium on 2025-02-03 and takes no Medium submissions. It runs on its own site, and writers report a 30-day exclusivity period before reposting [practitioner]. | Pick an active Medium publication instead (see below). Don't send TDS an import. |
| 3 | Point eng.lattice.io at the publication and add Google Analytics | Medium allows no tracking scripts or analytics on a custom domain, so GA is impossible [platform]. A custom domain also needs membership, allows one per publication, and permits no subfolder or proxy. Medium can redirect custom-domain URLs to medium.com, as TDS reported in 2025 [practitioner]. A domain pointed away gets disconnected [platform]. | Skip the custom domain. Keep the canonical original on a lattice.io page you control, and track with UTM links (see below). |

## Step 1: replace the Boost nomination with this

1. Named engineers publish on their own accounts, then submit to the publication.
2. Feature one story a week. Credits start at 4, refill one per 7 days, and cap at 4. Un-featuring refunds nothing [platform].
3. Write from first-hand experience: what you built, broke and measured [platform].
4. Keep AI-generated drafts out. Majority-AI text gets no General distribution and no Boost, even if labelled [platform]. Label AI-assisted text within the first two paragraphs, or the story drops to Network only [platform].
5. Write in English. Other languages get no Boost and no General distribution [platform].
6. Keep the brand account for release notes only, and expect followers-only reach from them.

## Step 2: replace TDS with an active publication

- **Pick by topic fit first, then by whether its rules allow your call to action.**
- **Candidates:** ITNEXT (publishing on Medium in 2026; read its current guidelines), Level Up Coding (active, about 300k followers [practitioner]; the older guide says to email a draft link), and the In Plain English network (including Stackademic). The In Plain English call-to-action rules are in its write-for-us page.
- **Skip:** Better Programming, reported closed and inactive.
- **Timing:** submit by week 6, not now. First do the earn-first weeks and some canonical imports.
- **Native original:** an established publication may demand an original, so write a native story rather than importing a published post.
- **Product mention:** ask the editor first about any paid-plan or trial link. A free tier or open-source repo usually reads as acceptable.
- **One copy on Medium:** don't post the same story in two publications [platform].
- **Sponsored slots:** never buy one inside a Medium publication. It is banned third-party advertising [platform]. If the In Plain English network offers a paid post on its own site, get in writing that it won't be syndicated into its Medium publications.
- **Pitch:** use the "Pitch to a publication editor" template in `references/templates.md`.

Candidate piece: a first-hand data-catalog story (for example lineage at scale, a migration, or a benchmark) by a named engineer.

- **Strip-the-product test:** if nothing worth reading remains without Lattice's name, it is content marketing. It gets Network only, and the editor will decline it.
- **Title shape:** "What happened, to what." Don't use "Introducing Lattice 3.0".

## Step 3: replace the custom domain and GA with this

- Keep each original on the company domain, with a canonical link set on the Medium copy. Only the story's author can set it, never a publication editor [platform].
- Link from Medium back to the canonical page with UTM-tagged links. Read referral sessions and signups in your own analytics, with the GA you already run on lattice.io [platform].
- If you still want eng.lattice.io on Medium, accept three costs (own reasoning plus platform limits):
  - It needs membership.
  - It permits no analytics.
  - Leaving later means a 301 for every old slug that ends in a hex story id, or those pages 404.
  - A Medium-only original under a custom domain is the least durable setup.
- Disclose any offsite signup link right next to the link, for example "(this link leaves Medium)" [platform].

## Account model

1. Named engineers publish under their own accounts.
2. Lattice Engineering is the company publication, owned by a company-controlled account with a paid membership.
3. Before the first import, agree with each engineer, in their employment or IP terms:
   - they may import company posts;
   - canonicals stay on the company domain;
   - on departure, stories stay up, free, and in the publication.

   Each story stays under its author's control. Editors may not delete it or remove it from the paywall without the writer [platform].
4. Never require outside writers to grant republishing rights to submit [platform].

## Publication setup

- **Mode:** Approved writers only.
- **Story type:** accept published stories, so engineers can import under their own names first.
- **Conditions:** image, subtitle, a matching topic. Leave "paywalled" off.
- **Guidelines page:** link one, using the "Company publication guidelines page" template in `references/templates.md`.
- **Newsletter:** the publication newsletter is a later option. A send cannot be undone [platform].

## Ranked surfaces (default rung is canonical import)

| Rank | Surface | Payoff |
|---|---|---|
| 1 | Canonical import, named author, into the publication | compounding |
| 2 | Earn-first responses on others' stories, no links | compounding |
| 3 | Publication with a weekly featured story | compounding |
| 4 | Submission to an established publication (ITNEXT or similar) | one-shot |
| 5 | Native first-hand deep-dive (Boost candidate) | compounding |
| 6 | Brand-account release note | one-shot |

The playbook's interview answers on hours, goal and who answers responses are missing. I assumed a standing channel and a small team. Tell me the answers, and I'll re-rank. Under 2 hours a week, keep only imports and responses. A launch date promotes the submission. A compounding mandate promotes the deep-dive.

## Eight-week cadence

Owners and hours are placeholders until you answer the interview.

| Weeks | Action | Owner and hours |
|---|---|---|
| 1-2 | Fix the paid membership. Sign the retention agreement. Set up the publication. Each writer completes their profile, follows the target topics, and leaves a few substantive responses a week with no links. | Publication owner, 2 h/wk |
| 2-3 | Import up to three existing posts that pass the strip-the-product test, one every few days, each under its named author. If none pass, start a native story. | Each engineer, under 1 h per import |
| 3-8 | Publish one story every one or two weeks. Feature the strongest weekly. Answer responses within two days. | One named engineer plus an editor, a day or more per native story |
| By week 6 | Submit one native original to ITNEXT or Level Up Coding, after asking the editor about any product link. An open publication takes 3 active submissions per guest writer [platform]. | Named engineer |
| Monthly | Read story stats. Drop topics that drew no presentations. | Editor |

## Templates

- **Earn-first response:** add a fact the author can use, with no link. "Great article, check out Lattice" reads as promotion through responses, which is spam [platform].
- **Disclosure line, first paragraph:** "I work on Lattice, the data catalog this post uses; the limits section covers where it falls short."
- **Canonical check before each publish:**
  1. Story settings > More settings > Advanced settings shows the original URL.
  2. The page source contains `rel="canonical"` pointing at the company domain.
  3. The paywall is off, topics are chosen, and the AI label is present when needed.
  4. The story is submitted to the publication, and featured if it's the week's best.

Run all drafts through a humanizer pass.

## Metrics

Targets are self-set, because Medium publishes no vendor benchmark.

- Presentations, feed click-through, reads, read ratio, and followers gained per story.
- UTM-tagged referral sessions and signups on your own analytics.
- Boost badges per quarter.
- Keep each author's third-party AI setting on the default "Prioritize maximum reach". The other option makes some AI products unlikely to credit and link the story [platform].
- Hygiene, with a pass threshold of zero: AI-generated or unlabelled stories, teasers, duplicates, and paid placements.

## Don't paywall

Keep vendor stories free. The paywall hides them from non-members. The Partner Program pays on member activity only, so non-members arriving through a Friend Link earn nothing [platform]. Writers report single- to low-double-digit dollars a month on small followings [practitioner].

## If stories die at 40 views

Compare presentations with writer plus publication followers. Presentations at or below that suggest Network only, which is a signal, not proof. Then check product framing, AI text, a missing AI label, off-topic topics, mass mentions, and non-English text. Stories from before 2025 show no presentations [platform]. If presentations are high but views are low, fix the title, subtitle and cover. If views are high but reads are low, the opening fails its promise. Rewrite the next story. Leave the old one up and never re-post it.

## Questions that would sharpen this

1. Does the owner currently have a paid membership, or did the publication get created another way?
2. Is eng.lattice.io already serving a company blog? If it is, that blog should stay the canonical home.
3. How many named engineers will write, and how many hours a week do you have?