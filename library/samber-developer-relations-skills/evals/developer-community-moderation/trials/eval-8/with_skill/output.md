## Bottom line

This is a live incident, not a policy-drafting exercise — stabilize first, write the missing policy after. Ilya has three problems stacked on top of each other: he's the accused, he already read the report, and he holds delete power over two-thirds of the evidence. Handle in this order, today.

## Do these now, in this order

**1. 🔴 Archive the two chat threads before anything else.** Have someone who is *not* Ilya screenshot and export both linked threads in full — messages, timestamps, usernames, permalinks — and pull the platform's admin/audit log if it has one (that survives deletion even of the messages themselves). Do this before you send a single reply to anyone. Chat evidence disappears the moment it's deleted; a case record has to carry what the chat log won't.

**2. 🔴 Suspend Ilya's ability to delete in those spaces for the duration of the investigation**, or at minimum lock/archive the two threads so no one — including him — can alter them. Tell him plainly this is a standard evidence-preservation control, not a verdict and not a punishment. Frame it that way to him directly so it doesn't read as pre-judgment.

**3. Recuse Ilya — hard conflict, effective immediately.** He's the accused, so he's excluded from discussion, from the decision, and from any further confidential material. He already read the original report; that can't be undone, but nothing further routes through him: no drafting the team's response, no seeing the reporter's follow-ups, no vote on the outcome. Say this to him directly and put it in writing.

**4. Tell him no — he does not reply to her directly.** Not to explain, not to "clear up the misrepresentation." This isn't about whether his account is right. Reasons:
   - He's recused; recused people don't represent "the team's" response.
   - Unmediated contact from the accused to the reporter, before any decision, is the same failure pattern as "let's get on a call and clear the air" — it reframes a conduct complaint as a misunderstanding between two people, before the team has even read the evidence.
   - Regardless of intent, contact from someone she just reported carries retaliation risk. If he does it anyway, log it in the case record — it's relevant to the case, not a side issue.

**5. Acknowledge the reporter today, from one of the other three — not Ilya, and not a reply-all that keeps him visibly on the thread.** Confirm receipt, ask if there's any immediate safety concern, give her a timeline, and tell her explicitly that Ilya is not handling this and is not part of the decision. That last sentence is likely exactly what she's afraid of right now, since she knows the alias forwards to him.

**6. Open the case record immediately**: case code, code names for everyone involved, the report's actual arrival time (the clock started then, not when you started working it — set an acknowledgment target and a decision deadline now, e.g. 10 business days, and put both in a calendar), links to the archived evidence, `conflicts_declared: Ilya — accused, hard conflict`.

## Before you assume the other three can decide this

Check whether any of the remaining three maintainers also have a conflict — close personal relationship with Ilya, shared reporting line, anything that stops them being impartial. Small maintainer teams often are. If two of three are also conflicted, you don't have a quorum that can be trusted, and you need a body above this team. If Brackenline doesn't have one (a foundation, fiscal host, or a named senior body), that gap is real and needs naming now, not after the case — for a case this sensitive (lead maintainer, three linked incidents), an external investigator is a legitimate call if internal impartiality can't be established.

Investigation order once evidence is secured: read everything first, then interview the reporter, then any witnesses, then Ilya — last, not first. Fix the decision rule before you need it (e.g., at least two non-conflicted members must agree; escalate on a split), so the outcome isn't argued after the fact.

## Don't do these — they're the standard first-draft mistakes

- Don't ask her to accept an apology or let him volunteer one as the resolution.
- Don't let "misrepresentation" become an excuse to skip reading the evidence yourselves before deciding anything.
- Don't propose mediation, or a "just avoid each other" arrangement, as a substitute for a decision — either he's a risk or he isn't; a stay-away condition answers neither.
- Don't let him stay involved because he's lead maintainer and it's awkward. If the rules bend for the most powerful person in the room, you don't have a functioning process — you have a title-based exemption.
- Don't let the reporter choose the remedy. Show her the proposed response before it's announced, so she can flag a missed fact or retaliation risk — that's not the same as asking her to pick the sanction.

## The structural bug this exposed — fix it right after

`maintainers@` is a single alias that forwards to the person any report might name. That's the exact failure mode of "the only reporting address belongs to the person being reported," just with three safe recipients mixed in instead of zero. Stand up a second path today — even a plain stopgap (two named people, or one trusted outside contact, published on your README/SECURITY page) — for reports about anyone on the primary alias. Do this before the next report arrives, not after this case closes.