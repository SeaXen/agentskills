I read the skill in full, plus its core rule up front: **"a community must not adopt a code of conduct if it will not apply to the most powerful people in it"** (Aurora & Gardiner, *How to Respond to Code of Conduct Reports*) — and Publish-gate item 1 makes that a hard blocker, not a style note: *"The code applies to the community's most powerful people, in practice and not only on paper."* The failure-mode table is explicit about what to do when that's not true: *"Stop. Fix the exemption or drop the conduct framing; a selectively enforced code is worse than none."*

Your request answers interview question 3 ("Would the policy be enforced against the founder, the top maintainer, or the biggest customer?") before I even asked it: no, and everyone on the team already treats that as settled. Per the skill, that's not a detail to route around — it's the finding. I'm not going to draft `CODE_OF_CONDUCT.md` with an enforcement ladder your team already agrees won't apply to Dario, because a document that promises accountability and doesn't deliver it is worse for your 2,800 members than having nothing: it tells everyone who gets a warning "this applies to you, not to power," which is a worse trust break than never having claimed enforcement at all.

Two things worth separating, because I think they're getting merged:

**"Your design is embarrassing" is a technical-argument problem, not automatically a conduct problem.** The skill treats "hostile technical arguments" as a frequent, non-malicious category with its own non-ladder responses (systemic fix, e.g. a `#architecture` norm requiring critique to target the design not the person; public statement of the standard; mentoring) — not an automatic trip to the ban ladder. Plenty of enforceable codes of conduct coexist with blunt engineering culture. That's not your blocker.

**The blocker is the blanket, in-advance exemption** — "obviously not something we'd use against him," independent of what he actually does. That's disqualifying regardless of whether his past comments would even cross a real line, because it means the rung a report lands on depends on who's named, not on what happened.

So, honestly, you have two shippable paths:

**Option A — fix the exemption, not necessarily Dario.** Write the standards section to explicitly draw the line the skill implies: critique the work, not the person; no targeting, demeaning, or contempt directed at an individual. If Dario's actual pattern is "harsh but aimed at the design," this is close to a non-issue in practice — he might not need to change much. What has to change is the team's private agreement that he's off the table if a report ever does land on him. That's a five-minute conversation with him now, before publishing, not a confrontation later. I can draft the full `CODE_OF_CONDUCT.md` + ladder + runbook once that's true — I still need answers to interview questions 2, 4, 6, 7, 9, 11 (is there a company entity/escalation body above the mod team, who moderates today, keep-working-after-founders-leave or close-this-case, roughly how many staff hours/week, other frequent problems besides this, any minors/contractual customers in the server).

**Option B — publish Community Guidelines instead, honestly scoped as non-enforcement.** This doesn't promise a ladder, so it can't be selectively broken. It's genuinely useful today and I can hand it to you right now:

---

```markdown
# Loomwright Community Guidelines

These are the norms for the Loomwright Discord — everyone here, employees included.
This is a guidelines document, not a code of conduct: it describes the standard we
expect, not a formal enforcement process with reporting channels and sanctions. If
that changes, this page will say so explicitly.

## What we're here for

Load testing, performance engineering, and building Loomwright together — bug
reports, architecture discussion, scripting help, war stories from production.

## Standards

- Attack the design, not the person. "This retry strategy will fall over past 10k
  RPS, here's why" is exactly what #architecture is for. "This is embarrassing" or
  any comment aimed at someone's competence rather than their proposal is not —
  say what's wrong with the plan instead.
- No harassment, hate speech, sexual content, or targeted insults, here or in DMs
  tied to this server.
- No spam, unsolicited self-promotion, or off-topic flooding.
- Disagree on technical grounds. Vendor and competitor employees are welcome to
  participate; sales pitches for competing products in our channels are not.
- Assume the person you're arguing with wants the same thing you do: a load
  testing tool that doesn't lie to you under pressure.

## What happens if this isn't followed

A moderator may remove content, mute, or in serious or repeated cases remove
someone from the server. This page doesn't commit to a published process, response
times, or appeal path for that — if you want that level of accountability, tell us;
we're weighing it.

## Reporting something

DM a member of the mod team, or use `#report` if you'd rather not DM. We read
everything.
```

---

That's real, shippable today, and it doesn't lie to your members about what they can expect.

One more thing worth saying plainly, since your team already treats the exemption as settled: the reason the skill's rule exists is a documented pattern, not a hypothetical — communities that ship a CoC with a known power exemption tend to find out about it publicly, from the person it failed to protect, at the worst possible time. Fixing this now costs one conversation with Dario. Fixing it after a reporter posts the DMs costs the community.

Tell me which path you want, and for A, give me answers to the outstanding interview questions above and I'll write the full document, ladder, and runbook.