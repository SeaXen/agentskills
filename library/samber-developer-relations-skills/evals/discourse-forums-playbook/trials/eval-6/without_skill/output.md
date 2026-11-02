I couldn't fetch the Discourse source in this session. The network call needed an approval that wasn't granted, so I wrote what follows from memory. The mechanism is solid, but I haven't confirmed the weights and thresholds. The ones I'm unsure of are marked ⚠️, and the first step below shows how to check them.

## How Discourse decides

**Hot** is a per-topic score stored in `topic_hot_scores` and recomputed on a schedule. As far as I remember:
- ℹ️ The score is driven by engagement from other people: likes, and the number of distinct posters and likers. It is divided by an age-decay term, so it falls as the topic gets older.
- ℹ️ Age is measured from when the topic was created, not from `bumped_at`. A bump doesn't refresh the topic's age.
- ℹ️ Topics get a penalty if they are closed. ⚠️ I believe it's a halving.
- ⚠️ Only topics with enough recent activity are eligible. Plugin and site settings control the window and the gravity.
- ⚠️ A comment in `topic_hot_score.rb` describes the formula as roughly "(likes − 1) / (age + 2)^gravity". Past experience says the actual SQL differs from that comment, so don't trust the comment.

**Top** is a per-period score in `top_topics`, computed for daily, weekly, monthly, quarterly, yearly and all-time.
- ℹ️ It combines views on a log scale, likes (the first post's likes are weighted separately), and post/reply counts.
- ⚠️ The weights are site settings named `top_topics_formula_*`.
- ℹ️ The "Top" ranking and the summary email both rely on this score.

**Summary email** is a digest. It picks recent topics, skipping ones the user has already seen or has muted, and ranks them mostly by the top score.
- ℹ️ The number of topics per email is small. ⚠️ I believe the default is about 3 featured plus a handful of others.
- ℹ️ Only users who haven't been active recently get it.
- ⚠️ I'm unsure of the exact window and cap.

## Why your announcements lose

1. **Bumping doesn't help.** It moves a topic up Latest but adds no likes, no distinct posters and no views from new people. Several bumps from the same account add posts, which are low signal, and the topic's age keeps counting.
2. **Four announcements a week split the engagement.** Each one gets a few likes, and the best of them still ranks below one or two threads that get real discussion. A digest with 3 featured slots can fit at most a few of them.
3. **Closed or read-only topics take a penalty.** If the announcements category is replies-off or the topics are closed, they are penalised in Hot and can't collect replies.
4. **Release announcements attract few reactions.** People read them and move on, so they get views but few likes or replies. Views alone help Top a little, since it's log-scaled.
5. **The category may be excluded.** Check whether the announcements category is hidden from the Top and Hot lists or the digest. ⚠️ I'm not sure of the exact setting names.

## What to do

**1. Verify first (15 minutes).** Open `/hot.json` and `/top/weekly.json`, and look at where your posts rank and what scores they have. Query `topic_hot_scores` and `top_topics` with the Data Explorer plugin. Check Admin > Settings for `hot` and `top_topics_formula`, and check the category's settings for exclusion from lists. That settles the ⚠️ items.

**2. Stop bumping.** Remove the practice. If an announcement needs more attention, get a real reply or like on it instead.

**3. Consolidate.** Replace four posts a week with one weekly "What shipped" topic, and keep the detailed per-release posts linked from it or in the changelog. One topic can gather the likes and replies that four topics split.

**4. Ask for a reaction.** End each announcement with one specific question, such as "Which of these will you use first?", "Did the migration work for you?" or "What's missing?". Distinct posters and likers are the signal that drives Hot.

**5. Seed the first replies and likes.** Have the team and a few champions react within the first hours. Age decay punishes slow starts, and early engagement is what lifts a topic.

**6. Keep topics open.** Don't close announcements. Turn replies on, and use the staff-only or read-only setting only where it's really needed.

**7. Give the digest something to pick.** For the email, the weekly summary topic and any thread with real discussion will outrank standalone announcements. Link the release notes from them.

**8. Re-measure after 3–4 weeks.** Track Hot appearances, weekly digest inclusion, and likes and distinct posters per announcement. Judge by engagement per topic, not by how many you post.