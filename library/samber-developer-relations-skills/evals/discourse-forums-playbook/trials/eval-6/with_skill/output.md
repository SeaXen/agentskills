# Why release announcements miss Hot and the summary email, and what to change

**Verdict:** Discourse ranks topics by how many different people react to them. A bump moves a topic up Latest and does almost nothing for Hot or Top. Four release posts a week, nudged by the same team, give the ranking almost nothing to count.

The mechanics below come from the discourse-forums-playbook skill, which labels them as taken from Discourse's source. I didn't re-check them against your live admin settings or the current source. Several numbers are admin-configurable, so check the values on your forum before you quote them.

## How Discourse decides

| Surface | What it scores | What it means for release posts |
|---|---|---|
| **Latest** | Time of last reply. | A bump works here and barely anywhere else. |
| **Hot** | Likes, plus distinct likers, plus distinct posters, in the last 7 days. The score decays with topic age (gravity 1.2). Closed topics count half. Only a top slice of recently active topics shows. | One team member replying three times counts as one poster. Replies from a handful of staff don't move it. A post that is three days old has already lost much of its score. |
| **Top** | log(views), first-post likes, likes per post (capped), log(post count), and a bonus once a topic reaches 10 posts. | A release post gets views and a few likes, then stops at 2–4 replies. Long, liked discussions win. |
| **Summary email** | Weekly by default, sent to absent members. It carries 5 popular topics and 5 posts and stops after 180 days of inactivity. | Your posts compete on the Top-style score above, so they lose to threads that draw discussion. |

## Why yours lose

1. **Few distinct people react.** A release post is read, liked once or twice, and left alone. Hot rewards many different people taking part.
2. **Bumping adds no distinct people.** It only changes who looks recent. Self-bumping is on the skill's "do less" list.
3. **Four posts a week split the audience.** Each post gets a quarter of the views and likes, so none builds the score that Top rewards.
4. **Announcements tend to be closed topics.** If you close them, Hot halves their score.
5. **Release posts crowd out member questions.** The skill ranks announcements near the bottom of its value-per-hour list. It warns that a forum full of release posts reads as a press room.

## What to do differently

1. **Stop bumping.** Don't ask people to reply to push a topic up either. Both are on the skill's "do less" list.
2. **Post fewer, hand-written release posts.**
   - Keep only the releases members care about, so about one or two a week at most.
   - Post them under the author's name, not a bot or team account.
   - End each with one real question, for example "which of these breaks your setup?" or "what should we fix next?".
   - Don't auto-post a feed or every blog article. The skill says these score low on Hot and push member questions off Latest.
3. **Keep replies open.** Don't close announcement topics. Closing halves their Hot score and stops questions.
4. **Answer in the thread, with different people.** Have the engineer who built the feature reply, plus a product manager or support. More distinct posters help Hot more than staff posting more. Real member replies are better still.
5. **Change what the summary email promotes.**
   - Treat the email as a tool for pulling lapsed members back. Popular discussion earns a place there, and announcements mostly won't.
   - Exclude Announcements, or noisy tags, with the digest suppress settings. Then the 5 slots go to topics that bring people back.
   - If you want releases in front of members, send them through your own newsletter. Don't depend on the digest.
6. **Put your effort where the ranking rewards it.**
   - The skill's default is a Support category with Solved enabled, plus a welcome topic.
   - Add a weekly ritual topic such as "what are you building?". It creates member-written content and many distinct posters.
   - Leave Solved off the Announcements category. It adds Q&A markup, and Google wants that only on one-question-with-answers pages.
7. **Judge the change on discussion, not rank.**
   - Track the number of distinct repliers on release posts.
   - Track the share of announcement topics with at least one non-staff reply.
   - Track median time to first reply.
   - Pull these from the admin reports. Set targets from your own baseline, since no default fits your forum.

## Questions for you

- Are the announcement topics closed after posting?
- Is the Announcements category excluded from the digest today?
- How many non-staff members actually reply to them now?

Those answers decide whether you need only fewer posts and open replies, or a bigger change to what the forum is for.