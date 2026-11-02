## Diagnosis

Reach isn't the only problem. The format and the metric are both weak.

1. **Docs summaries make poor feed content.** A 300-word recap of docs answers no question a reader came with. The "continue reading in the docs" link tells them the real content is elsewhere. Dev.to readers react to posts that solve a problem or tell a story on the page.
2. **Org accounts get less engagement than people.** Readers follow and react to individuals. A two-person team posting under a brand has no face to follow.
3. **No cover image.** Posts without covers tend to get fewer clicks in the feed. I haven't tested this on your account, but it is cheap to fix.
4. **Asking Discord for unicorns is the wrong lever.** Those reactions come from people who already know you, not from new readers. Reactions are also the lowest-effort signal. Comments, saves and follows say more about whether a post helps anyone. Begging for unicorns can also read as engagement farming.
5. **You check results once a month.** You get 4 data points per cycle and can't tell which change worked. You also haven't named views, reading time or docs clicks, so "3 reactions" has no denominator.

## What to do (in order)

1. **This week, pull real numbers.** Open dev.to analytics and record views, reading time, comments, follower count and clicks to docs for the last 8 posts. If views are ~100 and reactions are 3, that's normal-ish. If views are ~20, the problem is distribution. Send me those numbers if you want a sharper read.
2. **Stop the unicorn ask.** Replace it in Discord with one honest prompt: "New post on X. If it answered a question, tell us what's missing in the comments." That gives you comments and feedback instead of vanity reactions.
3. **Change the post type.** Every post starts from a problem a developer types into a search box, such as "How to retry failed webhooks without duplicates". Put the whole answer on dev.to, with working code. Link to the docs once at the end as "reference", not as the payoff. Lengths of 800–1,500 words are fine when the content earns them.
4. **Post every 2 weeks, not weekly,** if that buys quality. Two people can't make 52 good problem-first posts a year while also doing the rest of DevRel.
5. **Put a person on it.** Publish under a named individual with a bio that mentions the org. Keep the org account for cross-posting. If you must stay on the org account, sign posts with the author's name and photo inside the post.
6. **Polish the basics for each post:**
   - a cover image (a plain template with the title is enough)
   - a title that states the outcome
   - 4 tags, mixing one broad tag (e.g. `webdev`) with specific ones
   - the first two lines readable in the feed preview
   - a `canonical_url` set to the docs page only if SEO credit for the docs matters more than dev.to ranking. Decide this on purpose.
7. **Be present in the first hour.** Publish when one of you can reply to every comment within 60 minutes. Early replies are the cheapest engagement you can create.
8. **Engage before you publish.** Spend 15 minutes, 3 times a week, leaving substantive comments on posts in your tags. That's how a small account gets its first followers.
9. **Use docs as a source, not as the product.** Mine support questions, Discord threads and GitHub issues for post topics. They are already the questions real users have.

## Measurement

- Track weekly, not monthly: views, reading time, comments, new followers, and docs clicks via a UTM link (`?utm_source=devto&utm_medium=post&utm_campaign=<slug>`).
- Reactions are a secondary metric. Docs clicks per 100 views is your outcome metric.
- Run the new format for 6 posts, or 12 weeks at the biweekly pace, and compare it with the old baseline from step 1. One post proves nothing at this volume.
- Success looks like views and docs clicks up, plus at least one comment per post from someone outside your Discord.

## Caveats

- I haven't checked dev.to's current feed ranking, and it changes. Treat items 6–7 as good practice, not guarantees.
- If the audience you want isn't on dev.to, no format change will fix reach. Check which channels your docs traffic already comes from.

**Next action (10 min):** do step 1, pulling the numbers for the last 8 posts.