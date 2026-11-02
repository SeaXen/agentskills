Job classification: this is job 3 (a code of conduct exists but is unenforceable) — but the Publish-gate audit below fails 9 of 11 items, so "fix only what fails" and "full rewrite" converge on the same output. Base document: Contributor Covenant 3.0 (recommended for new drafts — it drops 2.1's "a public apology may be requested" line and folds enforcement responsibilities into the moderator role).

Because this has to be a one-shot deliverable rather than the skill's normal one-question-at-a-time interview, I made the calls below where you didn't give me an answer, and flagged every one. Fix the bracketed placeholders before you commit this.

## Scope and jurisdiction

Surfaces: the Vantrel GitHub repository (issues, pull requests, discussions, code review) and any project chat you actually run. **Open question:** does Vantrel have a Discord/Matrix/forum? I've left it as a placeholder — don't ship the scope clause without naming it, or the first chat incident falls outside the document you just wrote.

People covered: contributors, maintainers, anyone participating in project spaces — explicitly including you, the maintainer. This is Publish-gate item 1, and it's the one Aurora & Gardiner call non-negotiable: a code the most powerful person is exempt from is worse than none.

Off-platform stance: in scope when it credibly bears on someone's safety inside the project, out of scope otherwise. This is the safer of the two standard stances and costs nothing to hold since you're not policing anyone's personal life.

Single body: since there's no foundation or fiscal host, one body handles everything — you, with the two other listed maintainers as the named alternate for cases where you're the subject or conflicted (see Response team below).

## Enforcement ladder

| Rung | Trigger | Consequence |
|---|---|---|
| 1. Warning | First occurrence of unprofessional or unwelcome behavior | Private written notice naming the behavior and the expected change. No public statement. |
| 2. Temporarily Limited Activities | A violation continues after a warning, or a moderate violation on first occurrence | Restricted from specific interactions (commenting, opening issues/PRs, chat posting) for a stated period, e.g. 2–4 weeks |
| 3. Temporary Suspension | Serious violation, or a pattern continuing after limited activities | Full removal from interaction across all named surfaces for a stated duration (Django's bands: 30–90 days short, 90+ extended) |
| 4. Permanent Ban | Pattern of violation, sustained harassment, threats, or doxxing | Permanent removal from all project surfaces |

All four rungs are executable by one person: GitHub admin rights cover block/restrict/ban on every surface named above, so this ladder doesn't need a second person to function day to day — only the two cases below do.

## Reporting

1. **Primary channel** — `[conduct email — e.g. conduct@<vantrel-domain>, or a free-tier alias like a ProtonMail address forwarding to your inbox]`, reaching you by name. Ten minutes of setup, and it means the address can be handed to someone else later without exposing your personal inbox.
2. **Alternate channel** — reports *about* you go to `[co-maintainer A]` and `[co-maintainer B]` instead, named by their GitHub handles in the document. **Open question, and the biggest gap in this rewrite:** confirm they're actually willing to occasionally read one email and render a judgment — inactive on commits doesn't necessarily mean unwilling. If either declines, the honest fallback is GitHub's own abuse-report / Trust & Safety channel for severe cases (threats, doxxing) — real, usable today, and independent of anyone's availability. Do not publish this section until you've asked them.
3. **Anonymous option** — a simple form (Google Forms with email collection off, or Formspree) linked from the reporting section. Free, low effort, worth doing.
4. **Acknowledgment target** — 3 business days. Chosen because it's CNCF's own published promise and realistic for a volunteer with a day job; tighten it once you have real data instead of a made-up ambitious number you can't hold.
5. **No-retaliation clause** — included in the document below.

## Response team

Just you, day to day, with `[co-maintainer A / B]` as the standing alternate for conflicted cases. This is thinner than the skill's usual recommendation (3–6 people surviving a third being unavailable) — correct for a project this size, not a compromise to fix later unless Vantrel's contributor base grows enough to recruit real moderators from observed helpers.

## Runbook summary (private — do not publish this section, only the CoC below)

- **Deadline clock**: acknowledge in 3 business days, decide in 15 business days (looser than Aurora & Gardiner's 10-day worked example, because you're one volunteer, not a staffed team — tighten once you see real volume).
- **Intake**: who, what, where, dates/links, does the reporter want anonymity, is anyone in immediate danger. Screenshot chat evidence before removing anything — deleted messages don't come back.
- **Recusal**: if a report names you, it routes to the alternate contacts automatically; you're excluded from the decision, not just the vote.
- **Decision rule**: for a body of one, there's no consensus-versus-majority question — the open question is only "am I conflicted." If yes, the alternates decide alone.
- **Case record**: a private note (even a local encrypted file or a locked GitHub Gist) with case code, dates, surface, neutral summary, decision, rung, effective/end dates. This is what lets you tell "second warning" from "first" — without it the ladder is decided from memory every time.
- **Notification**: use the four-part template — behavior, impact, expected change, consequence — never an apology request, never mediation as a substitute for a decision, never a stay-away condition instead of one.
- **Schedule the restoration** of any time-boxed sanction the day you apply it, or it becomes a permanent ban nobody decided on.

## Platform controls

Given the surfaces are GitHub-only for now and there's no flood/spam problem reported: GitHub's interaction limits (block non-collaborators from commenting for 24h/3d/1w) are pre-configurable in seconds and cost nothing to leave off until needed. No trust-level system or rate limiting is worth building for a project this size yet — revisit only if Vantrel starts seeing AI-slop issue floods or brigading.

## Publish gate

| # | Item | Old (dropped-in CC 2.1) | Rewrite below |
|---|---|---|---|
| 1 | Applies to the most powerful person | ❌ No real alternate channel — a report about the maintainer had nowhere else to go | ✅ Explicit, with a named alternate path |
| 2 | Scope names surfaces, people, off-platform stance | ❌ Generic boilerplate, no real surfaces named | ✅ Named (pending the chat-platform placeholder) |
| 3 | Every rung has trigger + consequence | ⚠️ Present but generic, never adapted to what one person can actually do | ✅ |
| 4 | Time-boxed sanctions state duration | ❌ "for a specified period of time" — no number | ✅ 30–90 day band |
| 5 | Private channel reaches a named group | ❌ "email the maintainers" names nobody | ✅ |
| 6 | Second channel for reports about the primary recipient | ❌ Did not exist | ⚠️ Depends on the two co-maintainers' consent — confirm before publishing |
| 7 | Acknowledgment target holdable at current volume | ❌ Not stated | ✅ 3 business days |
| 8 | No-retaliation statement | ❌ Not included | ✅ |
| 9 | Escalation body named | ❌ Not named | ⚠️ Same dependency as #6 |
| 10 | Case-record location/access/retention in writing | ❌ Not written anywhere | ✅ In the runbook above |
| 11 | At least two people can execute every promised action | ❌ One person, no backup, untested for two years | ⚠️ One person can execute every rung solo (GitHub admin); real redundancy still depends on #6/#9 |

Three items stay conditional until you talk to the other two maintainers. Everything else is fixed.

---

## `CODE_OF_CONDUCT.md`

```markdown
# Vantrel Code of Conduct

## Our Pledge

We as maintainers and contributors pledge to make participation in the Vantrel
project a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic
status, nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act in ways that contribute to an open, welcoming, diverse,
inclusive, and healthy community — including toward newcomers asking
low-level systems questions for the first time.

## Our Standards

Vantrel hasn't had a reported incident yet, so the examples below are drawn
from patterns common to systems-programming and runtime communities rather
than from our own case history. Update this list with specifics as real
cases occur.

**Encouraged behavior:**

- Answering a beginner's question about WASM internals without implying they
  shouldn't have needed to ask.
- Reviewing code and pull requests on the merits of the change, not the
  contributor's seniority or prior output.
- Disagreeing on technical design without questioning someone's competence
  or right to participate.
- Crediting others' work and ideas accurately.

**Unacceptable behavior:**

- Insults, put-downs, or gatekeeping language aimed at a contributor's
  experience level ("this is a beginner question," "read the spec before
  wasting our time").
- Sexualized language or imagery, and unwelcome sexual attention.
- Harassment, public or private — including sustained hostile technical
  arguments used to drive someone out of a discussion rather than resolve it.
- Publishing others' private information (address, real name if undisclosed,
  employer) without explicit permission.
- Sustained disruption of issues, pull requests, discussions, or chat.
- Any conduct that would reasonably be considered inappropriate in a
  professional setting.

## Enforcement Responsibilities

Vantrel's maintainer(s) are responsible for clarifying and enforcing these
standards and will take appropriate, fair corrective action in response to
any behavior they deem inappropriate, threatening, offensive, or harmful.

Maintainers have the right and responsibility to remove, edit, or reject
comments, commits, code, issues, and other contributions not aligned with
this Code of Conduct, and will communicate reasons for moderation decisions
when appropriate.

This Code of Conduct applies to every participant in Vantrel spaces without
exception, including maintainers. A report naming a maintainer follows the
alternate reporting path below, not the primary one.

## Scope

This Code of Conduct applies within all Vantrel project spaces, including
the GitHub repository (issues, pull requests, discussions, and code review),
[project chat platform — confirm and name it], and any official Vantrel
social media accounts. It also applies when an individual is officially
representing the project in public spaces.

Conduct outside these spaces is in scope when it credibly bears on a
member's safety inside them.

## Reporting

Report unacceptable behavior to **[conduct email]**, which reaches
[maintainer name]. We acknowledge every report within **3 business days**
and aim to reach a decision within 15 business days.

If your report concerns [maintainer name] directly, or you're not
comfortable using the primary address for any reason, contact
**[co-maintainer A]** or **[co-maintainer B]** instead, who have full
authority to investigate and decide the case independently.

An anonymous reporting option is available at **[form link]**.

All reports are handled with discretion. We will not disclose the identity
of a reporter without explicit consent, except where required by law.
Retaliation against anyone who reports in good faith is itself a violation
of this Code of Conduct.

## Enforcement Guidelines

Maintainers will follow these guidelines in determining the consequences for
any action they deem in violation of this Code of Conduct:

### 1. Warning

**Trigger:** Use of inappropriate language or other unprofessional or
unwelcome behavior, first occurrence.

**Consequence:** A private, written warning providing clarity around the
nature of the violation and an explanation of why the behavior was
inappropriate. No public statement is made.

### 2. Temporarily Limited Activities

**Trigger:** A violation through a single incident or series of actions,
or continuation of behavior after a warning.

**Consequence:** Restriction from specific types of interaction (commenting,
opening issues or pull requests, chat posting) for a stated period —
typically 2 to 4 weeks. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Suspension

**Trigger:** A serious violation of community standards, including sustained
inappropriate behavior after Temporarily Limited Activities.

**Consequence:** A temporary ban from any interaction or public
communication with the project for a specified period, stated at the time
the sanction is applied (typically 30–90 days). The restoration date is
scheduled the day the sanction begins.

### 4. Permanent Ban

**Trigger:** Demonstrating a pattern of violation of community standards,
including sustained inappropriate behavior, harassment of an individual, or
aggression toward or disparagement of classes of individuals.

**Consequence:** A permanent ban from any public interaction within the
project.

### Outcomes outside the ladder

Most reports don't end in a ban. Depending on the case, we may instead: fix
the underlying rule, template, or process that produced the incident; remove
the harmful content with or without a sanction; remove someone from a
maintainer role while keeping their membership; issue a public statement of
what the response would have been, if the account is gone or unidentifiable;
or offer mentoring to a well-meaning contributor with a skills gap rather
than a values gap. "No violation found" is a valid outcome, stated plainly
to both parties.

We do not compel apologies, mediate without both parties' informed consent
and as a substitute for a decision, or ask a harmed person to choose their
own remedy.

## Attribution

This Code of Conduct is adapted from the Contributor Covenant, version 3.0,
used under CC BY 4.0.
```

---

## Reporter-facing "what to expect" page (publish alongside the CoC — CONTRIBUTING.md or a docs page)

```markdown
## What happens when you report

1. You'll get an acknowledgment within 3 business days.
2. We'll ask for what happened, when, where, and who was involved — share
   only what you're comfortable sharing.
3. We keep your identity confidential from the person you're reporting,
   unless the law requires otherwise.
4. We'll show you our proposed response before we act on it, so you can flag
   anything we got wrong — we're not bound to change it, but we want to hear
   you first.
5. You'll be told the outcome that affects you. We don't share the full
   investigation with anyone outside the response contacts.
6. Retaliation against you for reporting in good faith is itself a
   violation.

Our internal process guide exists and may change — this page describes what
you can expect, not our exact internal steps.
```

## Announcement post draft

```markdown
We've rewritten Vantrel's Code of Conduct. The old one was the Contributor
Covenant dropped in two years ago and never adapted — it pointed reports at
"the maintainers" without saying who that meant or where to actually send
one, so we don't think anyone knew how to use it.

What changed: a named reporting address, a separate path for reports about
[maintainer name] specifically, an anonymous option, a response timeline we
can actually hold, and a clear four-step consequence ladder. It applies to
maintainers exactly the same as everyone else.

No incident prompted this — we'd rather have a working process before we
need one than after.
```

## Open questions for the user

1. Confirm the chat/forum platform(s) in scope, or say there are none beyond GitHub.
2. Ask `[co-maintainer A]` and `[co-maintainer B]` whether they'll take the alternate-contact role. If either declines, I'll rewrite that section to route to GitHub's abuse-report channel as the fallback instead.
3. Pick and fill in the actual conduct email/alias.
4. Set up the anonymous-report form (or confirm you don't want one — it's optional, not a Publish-gate item).
5. Confirm the 3-business-day / 15-business-day targets are ones you can actually hold given your day job — loosen them now rather than after the first report proves them wrong.