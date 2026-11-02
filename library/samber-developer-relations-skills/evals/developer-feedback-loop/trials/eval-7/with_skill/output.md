# Answer: not yet. Fix three things first.

⚠️ None of the three drafts should go out as written. Each breaks a rule in the feedback-loop skill (Step 6). The board-only plan is a fourth problem.

## What's wrong with each draft

| # | Your draft | Problem |
|---|---|---|
| 1 | "Great idea, on our radar!" | It's a no, but it reads as a yes to the asker and as evasion to everyone else. The request comes back every month. |
| 2 | "Coming in Q2!" | "Probably Q2" is the PM's guess, not a date product committed to and published. A missed date costs more trust than an honest no. |
| 3 | Close the thread quietly | You promised this in January. A silent close is the most expensive option: it's a planned → not planned reversal, and the skill says that gets its own public reply. |
| All | Board only | Most asks came from Discord and support tickets. Board notifications reach only board subscribers, so those requesters would learn nothing. |

## Rewritten replies

Fill the `<…>` slots. Product must approve the reasons before you post.

**(1) Configurable webhook retries: not planned**

```
Product reviewed this on <review date> and won't build configurable retry counts.
The reason: webhook reliability work is going into a replay endpoint instead, which
covers lost events whatever the outage length. Nothing is committed or dated for
replay yet, so I won't promise it. Until then, the workaround is <link, or "none
exists">. If replay wouldn't cover your case, say so on <record link>. That is what
would reopen this.
```

- Don't write "replay is coming". "At some point" is not planned.
- If product wants replay to count as planned, product must set that status first.

**(2) SSO for self-hosted: planned, no date**

```
Product has committed to SSO for self-hosted (<record link>). No date is published
yet. I'll update the record when one is, and when it ships.
```

- Drop "Q2" unless product commits to it and approves publishing it. Only product may publish dates.
- If a requester asks "so Q2?", answer: "No date is published yet."

**(3) Bulk log export: planned, now not planned**

```
In January we said bulk log export was coming. That changed at the <date> review:
product is putting that capacity into <connector work>, and <reason product approves>.
Best workaround now: <link, or "none exists">. I'm sorry for the reversal. <record
link> stays open for use cases that would change this again.
```

- Name the reversal plainly and give the reason.
- Don't hide behind "priorities shifted".
- Keep customer names and revenue out of the reason. Say it at the level product approved.

## Where to post

1. Post each reply on its record on the board.
2. Post it again in the channel where the requester asked, because they can't see the board:
   - Discord: the original thread, or the requests channel if the thread is gone.
   - Support: a reply on each linked ticket. Ask support to send it, as the contract says support tells its own requesters.
3. Give #3 the most visibility, since the January promise was public. Put it first.
4. Post all three in one batch, in the week after the review.

## Before you send

1. **Product approval:** has the PM approved the reasons for #1 and #3, and the wording "no date yet" for #2?
2. **Who publishes:** who is allowed to say no in public at Greywater? That person approves publication.
3. **Replay workaround:** is there a workaround for #1 you can link? If not, say so.
4. **Stale bot:** if the board or GitHub issues auto-close stale items, exempt these three records until the replies land. A bot closing "bulk export" would be the quiet close by accident.
5. **Requester list:** can you pull requesters for #1 and #3 from Discord and tickets? If support needs to tell its own, brief them first.

Send me the answers to 1–3 and I'll finalize the three replies, plus a short Discord and ticket version.