# HN thread on per-minute pricing: plan and reply shapes

**I can't give you postable replies.** HN bans generated and AI-edited text in comments **[HN]**, and moderators ask for "not even a tiny bit". Below is a plan, and for each complaint the points a reply has to hit. Your engineer writes the actual words, from scratch. No colleague or CEO should post a draft I wrote.

**I haven't seen the thread.** The five complaints below are assumptions about what usually comes up on a per-minute CI price change. Paste the real top-ranked comments, in page order, and I'll re-map them. Page order matters because comment scores are hidden on HN.

## 1. Moves I'm refusing

| CEO ask | Why it fails | Do this instead |
|---|---|---|
| Every engineer jumps in | Colleagues piling on or chatting among themselves is a booster pattern, and rings are detected **[HN]**. It reads as a brigade and costs you the silent readers. | One named person answers. Other engineers send technical facts to that person. |
| Say half the commenters are competitor astroturfers | Calling critics shills or brigaders is banned insinuation **[HN]**. It's also unproven: angry customers explain a pricing thread without any plot. | If you have real evidence, email hn@ycombinator.com and say nothing in the thread. |
| Staff upvote or praise the replies | Solicited votes and undisclosed praise can penalize the thread, your accounts and your domain **[HN]**. | Tell staff not to vote, comment or share the link. Use the internal note below. |
| Post from a company account | Moderators ask for a person's username, not a brand **[HN]**. | The poster uses a personal account. |
| Ask moderators to remove the angry comments | Criticism of company conduct gets answered, not removed. | Answer it. |

## 2. Account readiness

- **Poster:** one engineer or product owner who knows the pricing model and can defend its trade-offs. A founder or CEO usually reads as defensive.
- **Account age:** I don't know it. An account with no comment history that suddenly defends a vendor looks like a booster. If that's the only candidate, treat it as a warning, not a blocker.
- **Disclosure:** start every reply by saying they work at the company. No HN rule requires this, but undisclosed staff reads as a booster comment.
- **Time zone:** I'm assuming the poster can stay in the thread for the next 6 hours, since the thread is hot today. Tell me if not.

## 3. Reply shape for the five likely complaints

Every reply follows the skill's shape for replies to critics. It has three parts: what's right in the criticism, the fact or trade-off that answers it, and what changes or why it won't. Open with the disclosure line.

### 1. "My bill goes up, and I can't predict it"
- Agree that unpredictability is a real cost. Don't dispute the feeling.
- Bring one concrete worked example with real numbers: a typical team's before and after. If most teams pay more, say so.
- State what you're doing about it, such as spend caps, alerts or a calculator. Say only what exists or is committed.

### 2. "You bill for queue, setup or idle time, or round up per minute"
- Ask your billing engineers exactly what is metered, and describe it precisely. Don't generalize.
- Concede any rounding rule that works against customers. If you'll change it, say so.
- Link the docs page only if it answers the question and needs no signup.

### 3. "Bait-and-switch: short notice, no grandfathering"
- Agree that the notice period was a real issue, if it was.
- State the actual dates and what existing customers keep. Don't spin them.
- This is criticism of company conduct. Answer it in the thread and don't ask for removal.

### 4. "Cheaper alternatives exist (GitHub Actions, self-hosted runners)"
- Don't attack competitors or hint at astroturfing.
- Say honestly where the alternatives are cheaper. Say where your product costs more and why: what the extra price buys, such as startup speed, caching or support.
- In a competitor's thread, answer only a direct question, once, disclosed. This is your own thread, but keep the same restraint.

### 5. "Why change pricing at all?" (motive and trust)
- This is the hardest to answer without sounding corporate. Give the real reason in plain words, such as cost of compute or an unsustainable flat tier.
- Name what you'll do differently next time. A concrete commitment beats an apology.
- Don't cite "market research" or "value" language. HN readers read it as marketing **[HN]**.

**Rules for all five:**
- Answer the strongest reading of each criticism, never the weakest.
- Never address users by username **[HN]**.
- No marketing words, superlatives or feature lists **[HN]**.
- State any pricing numbers up front. HN readers complain when pricing is hidden **[HN]**.
- Keep replies calm. Overheated threads get demoted **[HN]**.
- Edits are possible for about 2 hours, and deletion only before replies **[practitioner]**. Reread before posting.

## 4. Example shape to rewrite

This is the skill's example for a fictional product. Study the shape, then write your own from scratch.

```
// ✓ Good - agrees first, answers with a fact, says what changes
You're right that the README oversells the throughput. The 2,000 jobs/s figure
is from a VPS with a local NVMe disk; on network storage I measured about 300.
I'll put both numbers in the README today.

// ✗ Bad - defends, addresses the user, insinuates
@foo123 you clearly didn't read the docs. Are you from <Competitor>?
```

Disclosure example, also fictional:

```
Disclosure: I work on Litequeue. For the dead-job problem you describe, we
lease jobs with a timeout and requeue them on expiry; the trade-off is a
duplicate run if a slow job outlives its lease, so jobs need to be idempotent.
```

## 5. Internal note to staff (finished text, never posted on HN)

> There's an HN thread about our new pricing. Please don't upvote it, don't post the link in team, community or social channels, and don't comment to defend us, even if you disagree with what's said. HN detects this and can penalize the thread, our accounts and our domain. <Author> answers the thread; send technical or billing facts to them instead of commenting. If someone is rude, don't reply; tell <Author>.

## 6. Limits that bind

| Limit | Kind |
|---|---|
| No generated or AI-edited text in comments | enforced **[HN]** |
| No vote or comment solicitation | enforced **[HN]** |
| Thread closes to comments after about two weeks | enforced **[HN]** |
| Flag and vouch need about 31 and 501 karma | enforced **[practitioner]** |
| Rate limits and reply delays after flamewars | enforced, numbers **[practitioner]** |

Don't comment about votes or flags in the thread **[HN]**. If the thread is flagged or sinking, email hn@ycombinator.com once.

## 7. Tell the CEO

- One calm, disclosed, specific answer per top complaint does more than 20 engineers posting.
- The thread is at 60 points and about 180 comments. A pile-on from staff tends to add heat, and it can get the whole thing demoted.
- Astroturfing may or may not be real. Even if it is, saying so in the thread loses you the silent readers.
- The real defence is the pricing itself. If a complaint is valid, conceding it publicly costs little and wins readers.

## 8. Metrics

- Points and comments at 1 h and 6 h, and whether the thread stays on the front page.
- Whether your replies are ranked high on the page, and the tone of the follow-ups.
- Signups, churn and support tickets citing HN over the next 7 days, against the baseline from before the pricing change.
- Whether any pricing commitment you made in the thread ships.

## 9. Next step

1. Paste the actual top complaints in page order, and I'll re-map section 3.
2. Confirm who the poster is, and the age and history of that account.
3. The poster writes the replies in their own words, using the shapes above. I can name problems in a draft, but I won't rewrite it.