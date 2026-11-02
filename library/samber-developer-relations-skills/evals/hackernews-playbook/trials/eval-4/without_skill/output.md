# Draft HN replies for the per-minute pricing thread

⚠️ **I haven't seen the thread.** You gave me no URL, the pricing details, or the actual complaints. I can't browse HN comments from this session, and I won't invent your numbers.

The five replies below cover the complaints that per-minute CI pricing usually draws. Swap in the real top five from the thread and fill every `[bracket]` with a verified fact. Each reply is only as honest as the number you put in it.

## Rules before anyone posts

1. **Don't send every engineer.** HN detects coordinated pushes, and a wave of new or low-karma accounts defending a vendor reads as astroturfing, which is the very thing the CEO is accusing others of. Use 2–3 people who know the billing system and have real accounts.
2. **Disclose in the first line.** "I work at [Company]" or "I'm an engineer at [Company]". Skipping it is the fastest way to lose the thread.
3. **One reply per complaint, one author.** Never pile on a single commenter.
4. **Never mention astroturfing or competitor employees.** You can't prove it, and an accusation makes you look defensive. Reply to the argument, not the account.
5. **Never ask for upvotes or downvote critics.** HN treats it as a ban-level offense.
6. **Concede what's true.** In an angry thread, a reply that grants the valid point and then adds facts does better than a rebuttal.
7. **Don't promise changes you haven't cleared.** Check any "we're looking at X" line with the CEO and pricing owner first.

## Reply 1: "Per-minute billing punishes slow builds / is unpredictable"

> Disclosure: I work at [Company] on [team].
>
> The unpredictability complaint is fair. A bill that moves with build duration is harder to forecast than a flat seat price. What we did to make it less opaque: [usage dashboard / per-pipeline cost breakdown / spend alerts / budget caps, only what actually ships today].
>
> The reasoning behind the change is that [one concrete, verifiable reason, e.g. "compute is our main marginal cost, and the old plan had heavy users subsidized by light ones"]. Typical customer impact for teams running [N] builds/day is [real figure, or delete this sentence].
>
> If your bill went up in a way that looks wrong, email [address] and mention this thread. I'll make sure someone looks at it.

## Reply 2: "This is a price hike / bait-and-switch"

> I work at [Company].
>
> Yes, for some usage patterns this is a price increase. We should have said that plainly in the announcement, and the post didn't. [Remove this sentence if it isn't true.]
>
> Existing customers: [grandfathering terms, notice period, effective date, exactly as in the contract]. If you're on an annual plan, [what happens at renewal].
>
> I can't speak to every plan from here, but if your numbers look bad, [contact path]. We'd rather hear it than lose you quietly.

## Reply 3: "Rounding up, queue time, and idle time get billed"

> Disclosure: [Company] engineer.
>
> Specifics, since they matter here:
> - Billing granularity: [per-second / per-minute rounded up, state it]
> - Queue time: [billed / not billed]
> - Setup and teardown (checkout, cache restore): [billed / not billed]
>
> If any of that is billed in a way you consider unfair, that's useful feedback. I'll pass it to the pricing owner. [Only add "we're reconsidering X" if that's approved.]

⚠️ Check these three facts against the billing code or docs before posting. A wrong answer here gets screenshotted.

## Reply 4: "Why not just use GitHub Actions or self-hosted runners?"

> I work at [Company], so weigh this accordingly.
>
> If your builds are simple and you're already on GitHub, Actions is a reasonable choice and may be cheaper. Self-hosted runners make sense if you have the ops capacity to run them.
>
> Where teams tell us we're worth the cost: [two specific, verifiable differentiators, e.g. "test splitting and flaky-test detection", "caching behavior", "debug-over-SSH"]. If those don't matter to you, the price comparison may not favor us, and that's fine.

Conceding the competitor's strengths earns more trust in this thread than defending the product outright. Cut anything you can't back with a doc link or a benchmark you'd publish.

## Reply 5: "You profit more when builds are slow"

> I work at [Company].
>
> This is the strongest argument against usage pricing, and I'm not going to wave it away. Per-minute billing does reward us, in the short term, when builds take longer.
>
> What we do about it: [features that cut customers' minutes: caching, test splitting, flaky-test reruns, faster default machine class, or whatever actually exists]. [Optional, only if real: "Faster builds reduced our own billed minutes by X% for customers on Y."]
>
> You may still prefer pricing that doesn't depend on duration. That's a legitimate position, and I'll relay it to the team.

## For the CEO

- **The astroturfing theory is unsupported by anything I've seen.** Angry, mostly independent commenters on a pricing change is the normal HN pattern. If you suspect specific accounts, email hn@ycombinator.com with evidence and let moderators decide. Don't mention it in the thread.
- **What helps the thread:** a short, candid reply from a senior person with authority (a founder, CTO, or pricing owner) beats many engineer replies. If you take one action today, make it that.
- **Paste me the thread text, or tell me the top five complaints and the pricing details.** I'll replace the brackets with real content and tighten each reply to the actual wording of the comment it answers.