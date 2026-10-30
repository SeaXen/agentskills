# Close-the-loop replies

Read this before Step 6: the status vocabulary, one reply per status, the public feedback policy, and the privacy rules.

## Contents

- Status vocabulary
- Reply templates
- Saying no publicly
- Public feedback policy page
- Privacy rules

## Status vocabulary

Publish these definitions where developers can read them. Each status triggers a reply.

| Status | Means | Who sets | Promise it makes |
|---|---|---|---|
| received | captured, linked to a record | DevRel | "we have it" - nothing more |
| under review | on a product review agenda; also a record revisited at most twice | DevRel | a decision by a stated review, not a ship date |
| needs discovery | product wants to talk to requesters | product | someone may contact you |
| planned | product committed to solving the problem | product | it will be addressed; a date only if product published one |
| not planned | product decided not to solve it now | product | the reason and the best workaround |
| shipped | released | product | a link to the release note |
| duplicate | merged into another record | DevRel | follow the canonical record instead |

Public roadmaps that hold up share two habits: a status meaning "no timeframe yet" exists, so "exploring" is never read as "coming soon", and a shipped item closes with a link to its changelog entry. Debate goes to a separate discussion space, not onto the roadmap item.

## Reply templates

Adapt the wording to the community's voice. Keep the structure.

**received**

```
Thanks - logged as <record link>, where <N> others hit the same problem. Add a reaction there
and describe your use case; product reviews these every <cycle>. I will post the decision there.
```

Use the same text as the chat or helpdesk macro that redirects a request to its record.

**under review**

```
<record link> is on the agenda for the product review on <date>. You will get a decision
there - a decision, not a delivery date.
```

**needs discovery**

```
Product wants to talk to a few people hitting <problem>. If that is you, reply on <record link>
with how to reach you. Talking to us commits neither side to anything.
```

**planned**

```
Product has committed to solving <problem> (<record link>). No date is published yet; I will
update the record when one is, and when it ships.
```

**not planned**

```
// ✓ Good - names the decision, the reason, the workaround, and what would change it
Product reviewed this on <date> and won't build configurable retries this year. The reason:
we're putting webhook work into a replay endpoint, which covers lost events for deploys of any
length. Until then, the workaround is <link>. If your case isn't covered by replay, say so on
<record link> - that's what would reopen it.

// ✗ Bad - a soft no that reads as a maybe, so the request returns every month
Great idea! We've passed this along to the team and it's on our radar for the future.
```

**shipped**

```
Shipped in <version> - <changelog link>. This came from <record link>; thank you to everyone
who added their use case. <One line on how it solves the problem stated in the record.>
```

**shipped, but not the fix requesters asked for**

```
Shipped in <version> - <changelog link>. You asked for <requested fix>; we built <what shipped>
instead, because <reason>. It solves <problem from the record> this way: <one line>. If it
doesn't cover your case, say so on <record link>.
```

**planned, now not planned**

```
In <month> we said product would solve <problem>. That changed at the <date> review: <what
changed and why>. Best workaround now: <link or "none exists">. I'm sorry for the reversal -
<record link> stays open for use cases that would change this again.
```

**duplicate**

```
This is the same problem as <record link> (<N> people). Closing this one so the votes and
use cases land in one place - please add yours there.
```

Post each reply where the requester asked, and on the record. Requesters subscribed to the record get notified by the tracker; requesters who asked in chat or through support only learn of it if someone tells them in that channel.

## Saying no publicly

- **Say no as no.** "Not planned" with a reason beats "on our radar", which reads as yes to the asker and as evasion to everyone else.
- **Give the reason at the level product approved.** Strategy ("we are deliberately the backend half"), cost ("it would freeze SDK releases for a quarter"), or fit ("it serves 0.3% of accounts and hurts the rest").
- **Always pair it with the best workaround**, or say plainly that none exists.
- **State what would change the decision** - a use case not yet represented, a segment shift - so the record stays useful.
- **In an open-source project, offer the build path** when maintainers would accept a contribution, and say so only if they would.
- **Never promise a date** that product has not published. A missed date costs more trust than an honest no.
- **Batch the no for themes.** When ten requests share one reason, publish the reason once and link it.

## Public feedback policy page

One short page, linked from every reply and from the community's channel topics.

```
How we handle feedback
- Where to post: <record of truth>. Chat is for conversation; requests posted there get linked here.
- What happens next: we merge duplicates, product reviews requests every <cycle>, and every
  reviewed request gets a status: <status list with one-line meanings>.
- What decides priority: <the factors product actually uses - problem severity, how many
  developers and teams it affects, fit with direction>. Votes are one input, not a ballot.
- What we can't take here: bugs -> <issue path>; security -> <private path>; support -> <path>.
- What we won't do: give dates before we are sure, or keep requests open we have decided against.
```

Publishing the capacity limit once ("we can't give every request the attention we'd like") is more honest than letting response times prove it.

## Privacy rules

- Never copy a private support message, an account name or a revenue figure into a public record. Link a private record instead.
- Quote chat messages publicly only when the channel is public and the quote is about the product, not the person; otherwise paraphrase.
- Ask before naming a company as a requester in public, even a happy one.
- Keep discovery-contact consent in the private record, per requester. Remove it, and the contact details with it, when the requester withdraws.
- Review private requester data on closed records on a fixed schedule, and delete what no open decision needs.
