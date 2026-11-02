# Discourse forum reality check for the exec review

## Verdict

- ❌ Don't buy ads yet. At least 38% of new topics sit unanswered for a week (the 48-hour figure is higher), so new arrivals land in silence. Staffing and answer supply are the defect, not traffic.
- 🎯 This quarter: clear the backlog, merge 41 categories into 4-5, turn existing helpers into non-staff answerers, and link the forum from docs and the product. Revisit paid acquisition when the 48-hour no-reply rate is near the 10% starting threshold.

## Assumptions

I couldn't interview you, so I'm stating these. Tell me which are wrong.

- The forum is established but stalling, with a hosted or self-hosted plan I don't know. Check the admin settings for live values before quoting any number below.
- The primary job is peer community or support deflection. If it is support deflection, 80% staff answers is the design and not a defect. Then only the unanswered rate and the 41 categories need fixing.
- Two DevRel people have about 5-10 hours a week for the forum. Please confirm.
- Content is public. I haven't checked login-required or sitemap status, and the search check in week 1 will confirm it.

## What the numbers say

| Fact | Reading |
| --- | --- |
| 38% of new topics have no reply after 7 days | The 48-hour figure is higher. Above about 10% at 48 hours, staffing is the defect, not promotion [practitioner]. |
| Two staff write about 80% of answers | Either no TL2-TL3 helpers exist, or staff answer before helpers can. Check whether TL2-TL3 members post at all. |
| 41 categories for 3,100 members | Empty rooms announce a dead forum. Start with 3-5 and split only when one carries too many unrelated threads [practitioner]. |

The 38% is a proxy. The real 48-hour rate comes from the admin reports in week 1.

## Why not ads

- New members arrive as TL0, with limits on topics, links and attachments, into silence, and do not return. Ads multiply that failure.
- Ads make the staffing gap worse. More topics with the same two people means a higher unanswered rate.
- Forum search traffic also swings with core updates [practitioner], so promise answered questions first and search as upside.
- The cheaper audience is already on the 3,100-member list and in your docs and product. Those links come first.

## Plan, with dates

Today is Saturday 2026-10-31. Week 1 starts Monday 2026-11-02.

**Week 1 (Nov 2): baselines.**
- Pull from the admin reports: time to first response, topics with no response at 48 hours and 7 days, and TL2/TL3 counts.
- List categories with no new topic in 30 days.
- Compute the share of answers by non-staff, and who the top non-staff repliers are.
- Inspect one solved topic with `?print`. Confirm it is public, canonical and in `/sitemap.xml`.
- Check for login-only content, forced profile fields, or a queue on every first post.

**Week 2 (Nov 9): merge categories.**
- Merge dead categories into tags and keep URLs redirecting, so old links don't 404.
- Target 4-5 categories: Support (Q&A, Solved), Announcements, Show and tell, Feedback, plus the staff area.
- Write a one-sentence About post per category.
- Pre-create the tag set for product area, version and integration, and require one product tag in Support. Only TL3 and staff create tags by default.
- Post one pinned note explaining the new map.
- Enable Solved only on Support. It puts Q&A markup on every topic in the category, which suits only one-question pages.

**Week 3 (Nov 16): clear the backlog.**
- Reply to unanswered topics, merge duplicates, and close stale ones with a note. Never mass-bump.
- This is also the only large piece of work that moves the headline number inside the quarter.

**Weeks 4-6 (Nov 23 to Dec 11): build non-staff helpers.**
- Invite existing non-staff helpers (TL2-TL3, top repliers) by name into a helper group, using the invite below. Don't bulk-grant TL3 to new accounts. Grant at most TL1 through a verified-customer group, and let members earn the rest.
- Try a short delay before staff reply, so helpers get the first shot. Staff still answer anything left after the delay.
- Rewrite the default guidelines and the pinned welcome topic (below).
- Link the forum from docs, error messages and the product help menu.
- Start the weekly ritual topic.

**Weeks 7-9 (Dec 14 to Jan 1): holiday cover.**
- Two people out together stall every answer. Write the rota before Dec 14, and name one person on each day.

**Weeks 10-13 (Jan 4 to Jan 29): measure and promote.**
- Promote recurring solved answers into docs.
- Tune the summary email. Exclude Announcements and noisy tags with the digest suppress settings.
- Promote TL4 by hand from TL3 members who already moderate well.
- Run the first quarterly metric read.

**Every day:** one owner runs a pass on unanswered and unsolved topics and welcomes each new member's first post.

## Settings kept or changed

- **Trust levels:** keep the defaults. Links from everyone below TL3 carry nofollow, which matches Google's advice for untrusted users. TL4 stays manual.
- **Spam controls:**
  1. Check the AI spam settings first. Discourse enabled AI spam detection by default on lower hosted tiers. On self-hosted it is off until Discourse AI and an LLM are configured.
  2. Add watched words for the spam vocabulary, and block disposable email domains.
  3. Queue TL0 posts only during a spam wave: swap `trust_level_0` for `trust_level_1` in the two approval-exempt group settings. Removing TL0 alone queues every member.
- **Homepage:** Categories until the forum has daily traffic, then Latest.

## Surfaces, ranked for this forum

1. Support with Solved, answered fast. Compounding, and the unsolved filter is the triage queue.
2. Welcome topic, About posts and guidelines. Compounding.
3. Weekly ritual topic. Compounding.
4. Summary email. It pulls lapsed members back with popular topics.
5. Links from docs, errors and the product. Askers arrive where the answers live.
6. Show and tell, then announcements, then badges.

The order starves announcements. Don't auto-post blog articles or release feeds as topics: they score low on Hot and crowd out member questions.

## Limits that bind

- **TL0 accounts:** 3 topics and 10 replies on day one, 2 links, no attachments, 30 s between posts.
- **Registration:** 3 new accounts per IP.
- **Support:** one question per topic. When staff mark the solution, raise auto-close to 7-14 days so the asker can still say it failed.
- **Show and tell:** the only place for self-promotion. Support and Feedback allow none.

## Templates (fill the brackets with your product)

**Welcome topic**

```
Welcome to the [Product] forum

This is where [Product] users help each other [do the core job] in production.
The team reads every new topic on weekdays and answers within one working day.

- Stuck or seeing an error? Post in Support, one question per topic, with your version and the full error.
- Built something? Show it in Show and tell.
- Want something changed? Feedback. We reply with a decision, even when it is "not now".
- Billing or account access? Email support@[domain]; never post keys or invoices here.
```

**Helper invite** (send from a named person, not a bot)

```
Hi [name],

You answered [specific questions] on the forum last quarter. We'd like to ask you to
join a small helper group.

The ask: answer questions in your area when you see them, for the next three months.
In return: a Helper badge and a direct line to the [product] team.

No is a fine answer.
[your name], [role] at [Product]
```

**Solution nudge**

```
Did [username]'s reply fix it? If so, please mark it as the solution.
If not, post what you see now and we'll keep going.
```

**Duplicate note**

```
Closing this as a duplicate of [link], which has a solved answer.
If that fix doesn't match your case, open a new Support topic with your version and error, and link this one.
```

## Metrics

Targets come from the week-1 baseline. These starting values are [practitioner] defaults until a baseline exists.

- Median time to first reply under 24 hours.
- Topics with no reply after 48 hours near zero (the starting threshold is about 10%).
- Share of support topics solved.
- Share of solutions written by non-staff, rising quarter on quarter. Skip this one if the primary job is support deflection.
- Count of TL2 and TL3 members, and new members' first-week post rate.
- Search landings on solved topics, from the search console.

## Stop rule

If the primary-job metric is flat for two quarters, cut categories and scope before adding staff hours.

## For the CEO

If the 48-hour no-reply rate falls near the 10% starting threshold and non-staff solutions are rising, paid acquisition becomes worth testing next quarter. Until then it would add traffic to a forum that doesn't answer it.