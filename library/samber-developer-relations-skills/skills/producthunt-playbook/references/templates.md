# Product Hunt templates

Listing fields and off-platform text may be drafted in full, then passed through your preferred humanizer skill. Comments on Product Hunt are skeletons: slots in `<angle brackets>`, filled by the maker in their own words, because the commenting guidelines ask for no LLM-written comments and a Likely AI badge labels them.

## Listing fields

```
URL:         <direct product link; for open source, the project's own docs domain when one exists, else the repo>
Name:        <product name only, no tagline, no emoji>
Tagline:     <what it does, plain words, 60 characters max>
Description: <who it is for, what it does, what is different; 260 characters max>
Topics:      <up to 3, most specific first>
Pricing:     <free | paid | paid with free trial or plan>
Thumbnail:   <square logo, 240x240; a GIF under 3 MB, no strobing>
Gallery:     <2+ images, 1270x760; first image shows the product working>
Status:      <released | not yet available (not featured; launch once access is open)>
Makers:      <every builder's Product Hunt username>
Promo:       <optional discount for Product Hunt visitors, never tied to votes>
```

```
// ✓ Good - names the thing and the job, no adjectives
Tagline: Run Postgres migrations with automatic rollback

// ✗ Bad - superlative, vague, emoji
Tagline: 🚀 The ultimate next-gen database tool for modern teams
```

For a library or CLI, the gallery shows a terminal session, a before/after diff or a benchmark chart, not a mock dashboard. Product Hunt staff note that images mostly display on a white background on the website.

## Maker comment (first comment at go-live)

1. `<who you are and who built it with you>`
2. `<the problem, where you hit it>`
3. `<what it does, said differently from the tagline>`
4. `<what is different from the tools readers already use, named honestly>`
5. `<what it does not do yet>`
6. `<how to try it now; any discount for Product Hunt visitors>`
7. `<one specific question you want answered>`

## Reply to a question or critic

1. `<the part that is right, or the need behind the question>`
2. `<the fact, trade-off or workaround that answers it>`
3. `<what you will change, or why not>`

```
// ✗ Bad - generic thanks, no answer, fishes for votes
Thanks so much!! 🙏 Would mean a lot if you upvoted!
```

## Announcement on your own channels (finished text allowed)

```
// ✓ Good - shares, invites feedback, asks for no vote
We launched <Product> on Product Hunt today. If you try it, we would love your feedback in the comments: <link>

// ✗ Bad - solicitation, banned
Please upvote us on Product Hunt, every vote counts! <link>
```

Post it in communities where the team is already active and to your own opt-in lists. No mass DMs, no cold email, nothing in upvote-swap groups.

## Internal team note (finished text, never posted)

> We launch <Product> on Product Hunt today at 12:01 AM Pacific. Please don't ask anyone to upvote, don't post in upvote groups, and don't mass-message the link. Product Hunt removes those votes and can drop or disqualify the launch. Sharing it on your own social accounts is fine. Only people tagged as makers comment on the launch, so the Maker badge shows who we are; everyone else sends technical points to <name>.

## Relaunch request (inside two months)

If unsure the change qualifies, email hello@producthunt.com before building the post.

```
Last launch: <date and link>
What changed: <the new app, redesign or new use case, with what a user can now do>
Who it serves that the last launch did not: <user or use case>
```

## Forum thread titles

Pick a topic per post: General for guides and questions, Self-Promotion for what you shipped. Lead with what readers learn; links come with context.

```
// ✓ Good - written the way people search
How we cut <Product> cold-start time from 4s to 400ms
What we shipped in <Product> in <Month>: <headline feature>
Launch recap: what <N> days on Product Hunt taught us about <topic>

// ✗ Bad - unsearchable
Some improvements we made
```

## Shoutout note

```
<Tool> - <what it does in your stack, one concrete line>
```
