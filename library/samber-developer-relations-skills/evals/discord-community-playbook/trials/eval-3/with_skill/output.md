# Tidepool v3 launch: Discord playbook and DM template

**Next action, today (Sat 2026-10-31):** each devrel reads the rules channel of their assigned server and sends the moderator ask in section 4. Plan time is about 20 minutes each.

I assumed "next Tuesday" means 2026-11-03, so launch is 3 days out. If you meant 11-10, nothing here changes except the dates.

I did not run the humanizer pass on the templates, and I did not re-read the live rules pages. The server rules below come from the skill's reference file, so each devrel re-reads their server's rules before quoting them.

## 1. Four parts of your plan I refused

| Your plan | Verdict | Why | Replacement |
|---|---|---|---|
| Post the launch in Reactiflux `#general` and 5-6 other servers | ❌ | Reactiflux: "a community, not a free audience". Commercial posts belong only in dedicated channels, and nobody on your team has history there [server] | Ask the mods first and post only after a yes (section 4) |
| DM everyone who asked about state management last month | ❌ | Reactiflux allows no DMs without in-server permission [server]. Discord treats unsolicited bulk DMs as banned [Discord]. Four named staff doing this reads as a spam campaign | Reply in-thread, or use opt-in channels (section 6). The only DM template is the permission-granted one in section 7 |
| Claude-drafted answers pasted into Reactiflux and Python Discord | ❌ | Python Discord bans copy-pasted AI answers [server]. Elsewhere it reads as drive-by marketing [practitioner] | Humans write every answer in their own words. Claude can help you check facts and code, but it never supplies the pasted text |
| 50 answers a day each (200 a day in total) | ❌ | At that rate answers are not full, and the target counts volume, not usefulness [practitioner] | Quality target in section 5 |

Compressing the "earn first" weeks into launch week is also off the table. This skill's rule for a launch under two weeks away, with no staff history in the host servers, is:

- Send the moderator ask today.
- Post in a host server only after a yes.
- Carry the launch on your own channels.

## 2. Assumptions

I did not interview you, so these are my assumptions. Correct any that are wrong.

1. Tidepool is a funded vendor product. That means no showcase posts in Reactiflux `#i-built-this`, which is mainly for individuals and indie work, and a hosted Q&A pitch instead [server].
2. v3 has breaking changes, so a migration guide exists or will exist by Tuesday.
3. Tidepool has no Discord server of its own. If it does, tell me its size and age, because the answer changes the plan.
4. The 4 devrels work in at least 2 time zones.
5. The Python SDK is a secondary product, so Python Discord is for answering only.

## 3. Roles

| Devrel | Owns |
|---|---|
| A | Reactiflux: mod ask, hosted Q&A pitch, answers |
| B | 2 React or React Native servers: mod ask, answers |
| C | 2-3 other React or React Native servers: mod ask, answers |
| D | Python Discord answers, plus launch-day channels you own (announcement, docs, release notes, GitHub Discussions) |

Pick the 5-6 servers by one test: do your users already talk state management there? Name them before you start. I did not verify any server's rules beyond Reactiflux and Python Discord.

## 4. Launch week (dated)

| When | Action | Owner |
|---|---|---|
| Sat 10-31 | Read rules and the promotion page for each assigned server. Rules for many large servers live only inside Discord, so join and read `#rules-and-info` | all |
| Sat 10-31 | Reactiflux: email the mods a hosted Q&A pitch for `#q-and-a` (template A). Send it today because the pitch goes by email | A |
| Sat-Sun | Other servers: send the mod ask (template B) in the channel or modmail the server specifies. State intent and date, and offer to skip | B, C |
| Sun-Mon | Python Discord: read the rules and start answering. Answers only; no mention of Tidepool unless it is the answer | D |
| Mon 11-02 | Publish the migration guide. Have the announcement text ready (template C) | D |
| Tue 11-03 | Publish the announcement on your own channels: release notes, docs, GitHub release, X and LinkedIn. Post in a host server only where a mod said yes, one post per server, in the channel they named | all |
| Tue-Fri | Answer the "v3 upgrade" questions that appear. Disclose employer in every answer that touches Tidepool | all |
| Fri 11-06 | Count what happened (section 8). Re-check each server's rules | all |
| Following 2 weeks | Keep answering. No links to Tidepool unless the link is the answer | all |

**Silence from a mod team is a no** [practitioner]. If a server says no or does not answer, nothing goes there. Launch still lands through your own channels, and the answering earns the next ask.

## 5. Answering rules (Reactiflux, Python Discord, others)

1. Use your own named account, not a shared brand account. Set a server nickname or profile that names your employer. Never automate the account, since self-bots are banned [Discord].
2. Answer only what you can answer in full, in the thread. Add a link only when the link is the answer.
3. Write each answer yourself. Claude may help you verify a fix or reproduce a bug, and the text you post stays yours.
4. Disclose in any answer that mentions Tidepool, a competitor, or the state-management category. Example: "(I work on Tidepool, but you don't need it for this.)"
5. Never move a conversation to DMs unless the person invites it.
6. Python Discord: no unapproved advertising, no paid work. Answer Python questions on topic. Mention the Python SDK only when it solves the question, and disclose when you do.
7. Where Tidepool is not the right tool, say so. Recommending the right tool earns more than a forced mention.

**Realistic volume:** 5-10 full answers a day per devrel is a ceiling I chose [practitioner]. The count is not the goal.

## 6. Reaching last month's askers without DMs

Choose from these.

1. **Reply in their thread only if it is still open and your reply answers it.** Do not reopen a month-old thread with a launch link.
2. **Use the announcement channel route.** If a server allows it, ask whether it follows or hosts an announcement feed. Followers receive releases without @everyone [Discord].
3. **Put the migration guide where people search.** Last month's askers search "Zustand alternative" and "state management", so docs and GitHub Discussions reach them. Docs SEO belongs to the `docs-seo` skill.
4. **Add an opt-in.** In the launch announcement or docs, offer "Get v3 release news" through a newsletter or GitHub watch.

## 7. DM template: permission granted only

Use this only when the person asked for a DM or said yes to one in the server. Without that, send nothing.

```text
Hi {name}, thanks for saying yes to a DM. You asked in #{channel} about {their actual question, one line}.

Short answer: {one or two sentences that actually answer it, without Tidepool if Tidepool is not the answer}.

If it helps: Tidepool v3 shipped on {date}. I work on it, so weigh my view accordingly. The migration guide is here: {link}. Skip it if it doesn't fit what you're building.

I won't message again unless you ask.
```

Use these rules with the template:

- One DM per person.
- Never send it in bulk.
- If the person does not reply, stop.
- If a server forbids DMs even with consent, answer in the thread.

## 8. Moderator ask and hosted Q&A (templates A and B)

**A. Reactiflux hosted Q&A pitch (email)**

```text
Subject: Q&A offer for #q-and-a: moving off Zustand-style stores

Hi Reactiflux mods, I'm {name}, a maintainer at Tidepool, a React state library. Members ask about state management most weeks. I'd run a 45-minute text Q&A on state management trade-offs: no slides, no pitch, I answer what they bring. Any slot from {dates} works. If it doesn't fit, no problem.
```

**B. Ask before posting (other servers)**

```text
Hi {mod team}, I work on Tidepool (React state library) and I'm answering questions in #{help channel}. We ship v3 on {date}. Would one post in {channel} be welcome, or should we skip it? Happy to follow whatever you prefer.
```

**C. Announcement for your own channels**

```text
Tidepool v3 is out.
- {headline change 1}
- {headline change 2}
- Breaking: {key change}. Migration guide: {link}
Questions: {GitHub Discussions or help channel}. Full notes: {link}
```

No @everyone. Followed servers strip it, and members who mute it miss the next one.

## 9. Metrics

Count these on Friday 11-06 and compare against the following weeks:

- Mod asks sent, answered yes, answered no, and unanswered.
- Answers given per server, with the number accepted or thanked.
- Joins or visits from the link in your Discord profile (use one link per source).
- Questions about v3 migration answered the same day.

Do not count mentions or messages posted as the result.

## 10. Questions for you

Reply with the answers and I'll adjust the plan.

1. Does Tidepool have its own Discord server or GitHub Discussions?
2. Is Tidepool funded, or an indie or open-source side project?
3. Is launch 11-03 or 11-10?

**Next:** send me the 5-6 server names, or run the Saturday step from section 4.