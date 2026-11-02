**Recommendation: don't re-add the tag, and don't send a complaint email.** Fix the post against the tag's rules, reply politely to the moderator, and appeal only if the fixed post still gets removed. This follows the dev.to playbook I read.

## Why your CEO's plan fails

- **You can't re-add it.** The playbook says: "A tag moderator can remove a tag; the author cannot re-add it." Re-adding is also likely to be reverted.
- **A complaint costs you reputation and gains nothing.** Moderators are trusted community members. Harbor is a vendor on a site where "readers, trusted members and tag moderators punish marketing faster than the feed rewards it." A complaint about a tag call makes Harbor look like the problem. dev.to also holds the same line on repeats: re-posting or arguing makes things worse.
- **The moderator may be right.** A post that is only "we released SDK v2" is release notes. The #javascript sidebar asks for focused content, and release notes belong under a different tag.

## What to do

1. **Reply to the moderator first.** Use the playbook's template, adapted:
   > Thanks for the note - you're right, this is a release announcement, not JavaScript content. I've kept the remaining tags. Is there a tag you'd suggest for the release notes part?

   Don't argue. You are asking for guidance.
2. **Read the live #javascript sidebar rules.** I don't have the exact wording, so check it before deciding.
   - If the post is mostly a changelog, retag it. Keep `#node` or another focused language or framework tag.
   - Use `#news` for the release, with a brief summary and the source link. `#showdev` is the other launch tag: it fits your own project or company launch, in a tone that is "not overly corporate or salesy".
   - Don't keep chasing #javascript.
3. **Consider making the post earn #javascript.** If you want that tag, add real JavaScript content to the post:
   - one tutorial-style section, such as "Charge a card in Node in 10 lines";
   - a design decision and its trade-off, for example how the SDK handles idempotency keys or retries;
   - a runnable code sample.

   A post that teaches something is more likely to keep the tag. Don't add content just to justify the tag.
4. **Check the rest of the post while you're in there.**
   - **Full content on dev.to.** Don't post a teaser that links out to the real post. Canonical URL doesn't fix that.
   - **Org account.** Publish under the Harbor organization so the company links are allowed.
   - **AI disclosure.** Set the tier. If the post names Harbor's product, keep it human-written, because AI-assisted promotion of your own business is barred.
   - **Affiliation.** Put a disclosure in the first paragraph, for example "I work on Harbor; this post uses it, and the trade-offs section covers where it falls short."
5. **Appeal once, only if the post is still removed or flagged after the fix.** Use dev.to/appeal while signed in, or support@dev.to. Describe what you changed in two or three lines. Don't write a complaint.
6. **Don't re-post the article.** Repeats make it worse. Also don't use more than one account to push it.

## What to tell your CEO

> The moderator's call is final for tags, and a complaint to support won't change it. It would just cost us standing on a site that punishes vendor behavior. A one-line fix (retag to #news and add a tutorial section) gets the post indexed and in front of the right readers. One appeal stays available if the fix is removed anyway.

## Questions that would sharpen this

Answer any of these and I'll tailor the plan:

1. Is the post under a Harbor DEV organization or a personal account?
2. Is the post just the release notes, or does it have tutorial content?
3. Was it a cross-post from your blog, and is the canonical URL set?
4. Can someone answer comments within 24 hours? The first four days decide ranking, and unanswered vendor posts lose reputation.
5. Is there a launch date this post is tied to?