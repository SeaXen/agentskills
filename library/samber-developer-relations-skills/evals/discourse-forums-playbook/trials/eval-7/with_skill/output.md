**Verdict:** Don't switch to Discord because someone said so. Keep Discourse unless your main goal is real-time chat. The SSO and docs-embed work belongs to a sibling skill, so I only cover its forum-side constraints here.

## 1. Discord vs Discourse

Your forum is a searchable, async space you host and answer for. Its value is answered questions that stay findable. Discord is a real-time chat server, which is a different job. That choice is made by the forum's primary job, not by taste. I don't have your forum's numbers, so this is the decision rule, not a verdict on tallyhq.

| Primary job | Venue |
|---|---|
| Support deflection, search acquisition, searchable answers | **Discourse** |
| Live peer chat, fast back-and-forth | Discord, as an addition |
| Both | Discourse for Support, Discord for chat. They don't replace each other. |

Reasons not to switch:
- Discord answers are hard to find in search, and they don't deflect tickets the way indexed Solved topics do.
- Migrating without permalinks breaks old URLs and loses rankings.
- Moving the forum doesn't fix the usual cause of a quiet forum. That cause is unanswered topics, which is a staffing problem. Check it with the diagnose steps in step 3 below.
- If you really need a chat server, the sibling skill `samber/developer-relations-skills@discord-community-playbook` covers it. To choose a venue from scratch, use `samber/developer-relations-skills@developer-community-launch`.

## 2. SSO with the Tally app account, and related threads in docs

`samber/developer-platform-skills@developer-portal-design` owns SSO, embedding topics in docs, and the forum API and webhooks. Run it for the implementation. Constraints from the Discourse side:

1. **Check your plan first.** SSO depends on the hosted tier, so confirm yours before you design anything. [Discourse]
2. **Don't require login to read the forum.** Login-required content drops the whole site out of search. Opening it later breaches what members agreed to. SSO should make signup easy, not gate reading. [practitioner]
3. **Keep verified customers at TL1 at most.** If you map Tally accounts to a group, grant TL1 through a verified-customer group. Never bulk-grant TL3: those links lose nofollow, and TL3 can recategorize and rename. [Discourse]
4. **Keep any contract-covered topic in a restricted category** from the start, before you link accounts. [Discourse]
5. **Show only Support topics where Solved is on.** Solved switches every topic in a category to Q&A markup, and Google wants that only on pages with one question and its answers. Enable Solved only on categories where every topic is a question. [Discourse] [Google]
6. **Treat "links from docs" as the highest-value surface after Solved Support.** Askers then arrive where answers live. A plain link to the topic is a safe baseline. Whether embedded thread content helps docs rankings is unverified, so don't promise it. [practitioner]
7. **Be ready to turn the embed into error-reference pages.** `samber/developer-relations-skills@developer-troubleshooting-docs` covers this, and `samber/developer-relations-skills@docs-seo` covers docs SEO.

## 3. Before you commit, check these in the live forum

1. Count new topics with no reply after 48 hours. Above about 10%, staffing is the defect, not the venue. [practitioner]
2. Count categories with no new topic in 30 days, and merge them.
3. Check who answers. If staff write most answers, you may have no TL2-TL3 helpers.
4. Check signup friction: login-only content, forced profile fields, or a queue on every first post.

## Questions I need answered

Answer these and I'll turn this into a full plan:
1. Is the forum not opened, open under 90 days, established but stalling, or migrating?
2. What is its primary job: support deflection, search acquisition, peer community, product feedback, or extension ecosystem?
3. Who answers daily, for how many hours a week, in which time zones?
4. Is it hosted or self-hosted? Which plan?
5. Is any content private for legal or contractual reasons?

**Next (2 minutes):** Run the 48-hour no-reply count from step 3.1 in the admin reports, and send me the number plus your plan tier.