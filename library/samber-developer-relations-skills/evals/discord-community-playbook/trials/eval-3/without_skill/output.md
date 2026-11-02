# Tidepool v3 launch playbook

**I changed two parts of your plan, and I didn't write the mass-DM template.** Here is why, followed by the playbook I'd run instead.

## What I changed and why

| Original plan | Problem | Replacement |
|---|---|---|
| Post the launch in #general and 5-6 other servers | Most large React servers restrict promotion to a showcase or self-promo channel. Cross-posting the same text the same day gets accounts muted or banned, and the ban attaches to your 4 named people. | Post once per server, in the sanctioned channel, with server-specific text. Ask mods first where there's no clear rule. |
| DM everyone who asked about state management last month | Unsolicited DMs from scraped lists break Discord's Terms of Service and most server rules. It also reads as stalking: "I saw you asked about state in March." Expect reports, bans and a "Tidepool spams DMs" thread. | Reply publicly in the original thread, where context exists. Offer opt-in follow-up (below). |
| Answer 50 questions a day using Claude drafts | Fifty a day is about one every 5 minutes over a 4-hour block. At that rate nobody is verifying code against v3's API, so drafts will go out with hallucinated APIs. In Python Discord, a React-lib vendor answering general Python questions looks like astroturfing. | Cap at 10-15 verified answers a day per person. Disclose affiliation. Restrict Python Discord to questions about your Python SDK. |

A launch that gets people banned or named in a "vendor spam" thread costs you more than the DMs would earn.

## Before launch (T-7 to T-1)

**Owner: one lead devrel, plus each of the 4 people for their servers.**

1. **Audit server rules.** For each target server, record where promotion is allowed, any cooldowns or minimum-activity rules, and whether mods want a heads-up. Reactiflux and Python Discord each get a line in this sheet.
2. **Assign servers.** One devrel per server, each already a visible, helpful member. A cold account that appears on launch day to post a link is the pattern mods remove.
3. **Message mods in advance** where rules are ambiguous: "We're releasing v3 of Tidepool, a state library. Is `<channel>` the right place to announce it, and any format you prefer?" Wait for a reply.
4. **Pick the launch story.** Lead with what changed for users, not "v3 is here." Include a migration guide link and a real before/after snippet. Test the migration guide on a cold project first.
5. **Prepare an FAQ document** (breaking changes, v2 support window, benchmarks with methodology, comparison to Zustand stated fairly). This is the source that answers get verified against.
6. **Set up attribution.** Use one UTM link per server (`?utm_source=<server>`). That tells you which servers worked without tracking individuals.

## Launch day (Tuesday)

1. **Post once per server** in the allowed channel, staggered across the day (no two within an hour), with server-specific text.
2. **Tell people who you are.** Open with "I work on Tidepool" or "I'm on the Tidepool team."
3. **Stay for replies.** Each poster answers questions in their own thread for the next 2-3 hours.
4. **Log feedback** in a shared doc: confusions, bugs, comparison questions.

### Post template (adapt per server)

> I'm on the Tidepool team (a small React state library, similar in spirit to Zustand). v3 shipped today.
>
> What's new: `<2-3 concrete changes, one line each>`
> What breaks: `<one line>`, migration guide: `<link>`
>
> Happy to answer questions here. Feedback on the migration path especially welcome.

## Handling people who asked about state management

Do not DM from a scraped list. Do this instead:

1. **Reply in the original thread only if** the thread is under about 30 days old, is still relevant, and Tidepool genuinely fits the question. Add value first: answer the actual question, then mention Tidepool if it applies. Say you work on it.
2. **Never reply to threads where the asker chose another tool and is happy.**
3. **Offer opt-in follow-up:** "If you'd like a heads-up on the migration guide or a worked example for your setup, say so and I'll DM you." Only DM people who reply yes.
4. **Keep a do-not-contact list.** Anyone who declines, or any mod who asks you to stop, goes on it for good.

### DM template (opt-in only, sent after the person said yes)

> Hi `<name>`, as promised in `<thread>`: here's the `<migration guide / example>` for `<their use case>`: `<link>`.
>
> I work on Tidepool, so I'm biased. If it doesn't fit your setup, tell me and I'll say so. No follow-ups unless you ask. 

## Ongoing help answers (Reactiflux and Python Discord)

### Rules

1. **Disclose** in your profile and when recommending Tidepool: "I work on Tidepool."
2. **Answer the question asked.** Recommend Tidepool only when it fits. Say when another tool fits better.
3. **Reactiflux:** answer general React and state questions. This is where goodwill gets built.
4. **Python Discord:** answer only questions about the Tidepool Python SDK, and only in channels where that's on-topic. If the server has no suitable channel, don't answer there. Send people to your own docs or issue tracker instead.
5. **Cap at 10-15 answers per person per day.** Quality is the goal, not volume.

### Claude-drafted answers: required workflow

1. **Draft with the FAQ and v3 docs as the only context**, so the draft cites your real API.
2. **Run every code snippet** before posting. A snippet that doesn't compile is worse than no answer.
3. **Rewrite in your own voice.** Remove generic filler and hedging.
4. **Never post a draft you haven't read in full.**
5. **Don't paste the same answer twice.** If a question recurs, add it to the FAQ and link it.
6. **Track errors:** keep a log of any wrong answer posted and correct it publicly within the day.

## Measurement (review at day 7 and day 30)

| Metric | Source |
|---|---|
| Clicks per server | UTM links |
| v3 installs vs. v2 | npm download deltas, with the caveat that CI inflates both |
| Migration guide completion | Docs analytics, plus "migrated successfully" replies |
| Questions answered, error rate | Answer log |
| Mod friction | Count of removals, warnings and bans, target zero |
| Sentiment | Tagged replies from the feedback doc |

**Stop rule:** if any server mod asks you to stop or remove a post, stop in that server immediately and apologize once, publicly or by DM to the mod.

## Day-after checklist

1. Fix any wrong answers from launch day.
2. Move the top 5 repeated questions into the FAQ and the migration guide.
3. Message the mods of each server with thanks, and ask what format worked best.
4. Write up the feedback doc for the engineers.

If you tell me which servers are on the list, I can draft the per-server posts and the rules-audit sheet.