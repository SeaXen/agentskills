# Recommendation: don't re-add the tag, and don't email support to complain

Accept the removal, retag the post, and put the JavaScript-worthy content in a follow-up post. I couldn't check dev.to's current tag rules from here, so step 1 confirms them.

## Why not do what the CEO asked

- **Re-adding the tag is tag-warring.** Moderators see it, usually remove the tag again, and may flag the account or org. Harbor would lose standing with the people it wants to reach.
- **A complaint email won't work.** Support generally sends tag disputes back to the tag moderators. You'd spend goodwill and wait days for the same answer.
- **The moderator's reasoning is defensible.** A post that announces a release is product news. Readers of #javascript expect JavaScript craft: techniques, patterns, tooling. For a payments API, dev.to readers also tend to distrust anything that looks like an ad in a topic feed.
- **The cost of losing is small.** A tag is one distribution channel. The post is still live and still reachable through other tags, the org page, and your own sharing.

## What to do (about 30 minutes)

1. **Read the #javascript tag guidelines.** Open dev.to/t/javascript and read the "About" panel. Confirm what it says about announcements and promotion. If it explicitly allows release posts, that changes step 4. If it's silent or restrictive, the moderator is within their remit.
2. **Retag the post with tags that fit.** Check the guidelines for each one before you use it. Candidates are #node, #api, #webdev, #showdev, and #opensource if the SDK is open source. Don't put #javascript back.
3. **Write a second post that earns #javascript.** Examples:
   - "Idempotency keys and safe retries in Node.js, with examples"
   - "Typing a payments API client in TypeScript"
   - "Handling webhooks without double-processing"

   Use the SDK as the worked example, and make the post useful if the reader never uses Harbor. Link it to the release post. Tag mods rarely remove posts like this.
4. **Optional: ask the moderator one polite question.** For example: "Thanks for the note. Would a post on [topic] using our SDK as the example fit #javascript?" Don't argue the removal. If the guidelines allow release posts (step 1), you can instead ask which part of this post they felt fell outside the rules.
5. **Keep the release post where release posts belong.** Use your org page, the changelog, and a newsletter or social post. If the org account publishes on dev.to, make the Harbor affiliation obvious.

## Message for the CEO

> The mod removed one tag, and the post is still live. Re-adding it gets removed again and risks a flag on our org account. Support sends tag disputes back to the same mods, so a complaint won't change anything. I'm retagging the post with fitting tags and writing a Node.js technical post, using our SDK as the example, that qualifies for #javascript and reaches the same readers. If you want, I'll ask the moderator what they'd accept.

## When escalation is justified

Only if the written tag guidelines clearly permit release posts and the moderator ignored them. Even then, ask the moderator or the tag's listed contact first, politely and with the guideline quoted. Escalate to support only if that fails.