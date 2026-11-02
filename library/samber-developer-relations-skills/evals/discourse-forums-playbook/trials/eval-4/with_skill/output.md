# Verdict for Friday: decline all three agency proposals and run a 5-day diagnosis first

- **Verdict:** none of the three fixes addresses why a public forum gets zero Google traffic after 8 months. One of them (the 200 generated topics) risks a spam penalty.
- **Likely causes:** content that Google can't reach, or too few answered questions to rank. The checks below take about 2 hours and settle which.

I couldn't inspect community.pellucid.dev, so everything below comes from the playbook. Labels: **[Discourse]** means Discourse docs or source, **[Google]** means Search Central, **[practitioner]** means community-manager experience.

## The three proposals

| Agency proposal | Verdict | Why |
|---|---|---|
| Move to `pellucid.dev/community` because subfolders rank better | ❌ Decline | Google states no preference between subfolder and subdomain [Google]. Discourse recommends a subdomain [Discourse]. Migrating without permalinks makes old URLs 404 and lose rankings. It would cost weeks of engineering and fix nothing, because zero traffic isn't a domain-authority problem. |
| Add QAPage schema to every category, including Announcements and Feature Requests | ❌ Decline as written | Solved already puts Q&A markup on every topic in a category where it's enabled, solved or not [Discourse]. Google wants that markup only on pages with one question and its answers [Google]. Announcements are staff posts and Feature Requests are open-ended discussion, so neither fits. Marking them up invites a structured-data problem. |
| Auto-generate about 200 topics from docs pages | ❌ Refuse | Google's spam policies name generating many pages without adding value as scaled content abuse [Google]. These topics would have no real asker and no distinct posters, so they'd score low on Hot and crowd real member questions off Latest. A thin-content penalty could also hit the docs site, which presumably does rank. |

## What zero traffic after 8 months usually means

Run these in order. Each takes minutes.

1. **Login required?** Open a topic in a private window. If it asks for login, or the whole site is login-only, search engines see nothing. This is the most common cause of exactly zero traffic [practitioner]. Reopening login-only posts later breaches what members agreed to, so you may need new public categories instead.
2. **Indexable?** Inspect a solved topic with `?print`. Confirm it is public, canonical and listed in `/sitemap.xml` [Discourse]. Also check `robots.txt` and any `noindex` setting.
3. **Search Console:** Is the property verified? Is the sitemap submitted? How many pages are indexed? "Discovered, not indexed" would point to too little content or authority, not to the URL structure.
4. **Answered-content volume:** How many public topics have a marked solution? Ranking comes from answered questions in the asker's words. If there are only a few dozen, that's the cause, whatever the URL.
5. **Unanswered rate:** Count new topics with no reply after 48 hours. Above about 10% means staffing is the defect, not SEO [practitioner].
6. **Dead categories:** Count categories with no new topic in 30 days, and merge them.
7. **Links in:** Do the docs, error messages and product help menu link to the forum? If not, Google has little reason to crawl or trust it.

## Counter-proposal for the agency and Friday

**This week (about 2 hours):**
- Run the 7 checks above and send me the results, or ask the agency to.

**Weeks 1-2, whichever check fails:**
- **If checks 1 or 2 fail**, fix access and indexing first. Nothing else matters until this is done.
- **If answered content is thin**, seed 5-10 real questions from support tickets. Staff post them under their own names with the asker's consent, or the asker posts them. Each gets answered and marked solved [practitioner]. Seed from real questions only: no alt accounts and no AI-generated answers.
- **Enable Solved on Support only.** Leave Announcements and Feature Requests without Q&A markup.
- **Link to the forum** from the docs, error pages and the product help menu.

**Weeks 3-6:** keep a daily pass on unanswered and unsolved topics, and promote recurring solved answers into docs.

**Reporting:** track median time to first reply (under 24 hours), topics with no reply after 48 hours (near zero), the share of support topics solved, and search landings on solved topics from Search Console. Frame the forum's business case as answered questions first, with search traffic as upside. Forum search traffic swings with core updates [practitioner].

**Stop rule:** if the primary-job metric is flat for two quarters, cut categories and scope before adding staff hours.

## What I need from you

I can't tailor the plan beyond this without these answers. Assumptions are in brackets.

1. Is the forum public, or does it require login? [public]
2. Hosted or self-hosted? Solved and Discourse AI depend on the hosted tier [Discourse]. [hosted]
3. What is its primary job: support deflection, search acquisition, or peer community? [support deflection]
4. Who answers daily, and for how many hours a week? [one person, a few hours]
5. How many public topics have a marked solution today? [fewer than 30]

## Reply to send the agency

> We're not approving the three changes. Subfolder vs subdomain makes no difference to Google, QAPage markup only fits single-question topics, and generating 200 topics is scaled content abuse. Please send Search Console index coverage, a sitemap check and crawl results for the forum. We'll run a 2-week plan on real, answered content and review it with you.

I can draft the seed-from-ticket consent request and the Support About post from the playbook's templates once you confirm the product and the answers above.