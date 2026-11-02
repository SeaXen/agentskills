# Pinegrain community moderation setup

Two structural facts shape everything below, so state them before the documents:

**You don't own either primary venue.** r/pinegrain sits inside Reddit, but subreddit moderators get real, unilateral tools there — content removal, AutoModerator, Crowd Control, and a genuine permanent subreddit ban. The Slack channel is the opposite: #pinegrain is one channel inside a foundation-run workspace you don't administer. You almost certainly cannot unilaterally ban anyone from that Slack — only the foundation's workspace admins can. "Permanent ban" therefore means two different things depending on the surface, and the CoC and runbook below say so explicitly rather than promising a power you don't have.

**No escalation body exists yet.** The skill this is built from requires one named body above the moderation team for deadlocks and appeals. Pinegrain has no foundation of its own and the Slack's foundation isn't Pinegrain's governance. Until you name one, item 9 of the Publish gate (below) fails — this is the single biggest gap, not a formality.

I've drafted everything else on stated assumptions, flagged inline and collected at the end. Nothing here should ship before you correct the assumptions that are wrong.

---

## 1. `CODE_OF_CONDUCT.md` (repository root — public)

*Adapted from Contributor Covenant 3.0. Role title renamed to Pinegrain's actual roles.*

```markdown
# Pinegrain Code of Conduct

## Our Pledge

We as members, contributors, and moderators pledge to make participation in the
Pinegrain community a harassment-free experience for everyone, regardless of
age, body size, visible or invisible disability, ethnicity, sex characteristics,
gender identity and expression, level of experience, education, socio-economic
status, nationality, personal appearance, race, religion, or sexual identity
and orientation. This applies equally to first-time posters and to the people
who founded and maintain the project.

## Encouraged Behaviors

- Assuming good faith in technical disagreement, while still describing what
  actually happened rather than what you think someone meant.
- Giving and gracefully accepting constructive feedback on code, design, and
  RFCs.
- Taking responsibility for mistakes, apologizing to those affected, and
  learning from the experience — offered unprompted, never requested.
- Focusing on what is best for the Pinegrain project and its users as a whole.

## Restricted Behaviors

- Sexualized language or imagery, and sexual attention or advances of any kind.
- Trolling, insulting or derogatory comments, and personal or political
  attacks.
- Public or private harassment, including sustained unwanted contact after
  being asked to stop.
- Publishing others' private information — physical or email address — without
  explicit permission.
- **Organizing or participating in a coordinated pile-on**: recruiting or
  amplifying a wave of hostile replies, downvotes, or reports against one
  person or thread, whether coordinated on-platform or off-platform (e.g. on
  another subreddit, another Slack, or a social network) and directed at a
  Pinegrain space.
- Dogpiling a maintainer's design decision with repeated, escalating hostile
  restatements after the decision has been explained once.
- Submitting bulk low-effort or AI-generated issues, PRs, or bug reports
  without disclosing that assistance, when it consumes reviewer time in
  volume. (Handled primarily through the volume controls in §6 of the
  platform control sheet, not through this ladder — see there.)
- Other conduct which could reasonably be considered inappropriate in a
  professional setting.

## Enforcement Responsibilities

Pinegrain Moderators are responsible for clarifying and enforcing our
standards and will take appropriate and fair corrective action in response to
any behavior they deem inappropriate, threatening, offensive, or harmful,
across every surface listed in Scope. Moderators will remove, edit, or reject
comments, commits, code, issues, and other contributions not aligned with this
Code of Conduct, and will communicate reasons for moderation decisions when
appropriate. This applies to founders and maintainers exactly as it applies to
any other member; no one is exempt. [Confirm — see Open Questions.]

## Scope

This Code of Conduct applies within all Pinegrain community spaces:

- r/pinegrain (all posts, comments, and modmail)
- the #pinegrain channel in [Foundation]'s Slack
- the Pinegrain GitHub organization: issues, pull requests, discussions, and
  code review
- Pinegrain's project social accounts
- any event Pinegrain runs or is officially represented at

It also applies when an individual is officially representing the project in
public spaces outside those listed above. Conduct entirely outside these
spaces is out of scope unless it credibly bears on a member's safety inside
them — for example, off-platform coordination of a pile-on that then executes
inside r/pinegrain or #pinegrain is in scope for the coordination, not just
the execution.

## Reporting

Report abusive, harassing, or otherwise unacceptable behavior to
**conduct@pinegrain.dev** [confirm real address/domain], reaching the named
Pinegrain Conduct Team (§4). To report a member of that team, email
**escalate@pinegrain.dev** instead [needs a real, different recipient — see
Open Questions]. An anonymous reporting form is linked from this document at
[pinegrain.dev/report]. We acknowledge every report within **2 business days**
[baseline, recalibrate after one quarter] and never disclose a reporter's
identity to the reported person. Retaliation against anyone who reports in
good faith is itself a violation of this Code of Conduct.

## Enforcement Ladder

| Rung | Trigger | Consequence |
|---|---|---|
| 1. Correction | Unprofessional or unwelcome behavior, first occurrence | Private written notice from a named moderator, naming the behavior and the expected change |
| 2. Warning | A clear violation, or a pattern continuing after a correction | Formal written warning, a stated no-contact period, and notice that a further incident escalates |
| 3. Temporary suspension | A serious violation, or continued behavior after a warning | Time-boxed removal from interaction, 30–90 days for a first suspension, longer with return conditions for a repeat — see the platform-specific mechanism in the private runbook, since "removal" means different things on Reddit versus Slack |
| 4. Permanent ban | A pattern of violation, sustained harassment, doxxing, threats, or organizing/leading a pile-on | Permanent removal from public interaction in every Pinegrain-controlled space, and a formal request to [Foundation] for the same on Slack where we do not control that outcome directly |

Outcomes that don't require moving up the ladder — used when they close the
case on their own: removing the harmful content, removing someone from a
leadership or trusted-flagger role while keeping their membership, a public
statement of what the response would have been when an account is gone or
unidentifiable, a systemic fix (a rule, template, or channel change), or
mentoring for a well-meaning repeat offender who has a skills gap rather than
a values gap. "No violation found" is a finding, stated plainly to both sides,
not a consequence chosen to avoid one.

We do not compel apologies, use mediation as a substitute for a decision, let
a reported person stay on condition they avoid the person who reported them,
or ask a harmed person to choose their own remedy.

## Attribution

Adapted from the [Contributor Covenant, version 3.0](https://www.contributor-covenant.org/version/3/0/).
```

---

## 2. Enforcement ladder — per-surface mechanics

The ladder above is one policy; the *mechanism* differs by surface because your authority differs by surface. This table is what a moderator actually clicks or sends.

| Rung | r/pinegrain (you control this) | #pinegrain Slack (you mostly don't) | GitHub (you fully control this) |
|---|---|---|---|
| 1. Correction | Modmail | DM from a named moderator | Comment/DM |
| 2. Warning | Modmail, logged | DM, logged | Comment + issue/PR interaction note, logged |
| 3. Temp. suspension | Native timed subreddit ban (30–90 days) | Remove from channel if a channel-manager role permits it; otherwise a formal, logged request to [Foundation]'s Slack admins for a timed removal | GitHub interaction limits (blocks comments/issues/PRs) for the stated period |
| 4. Permanent ban | Native permanent subreddit ban | Permanent removal from #pinegrain if permitted, **plus** an escalation request to [Foundation] for a workspace-level ban — this is a request, not a guarantee, and the CoC and reporter-facing page must say so | Org-level block |

**Honest note to put in front of the team, not just here:** rung 4 on Slack is the one promise in this document Pinegrain cannot unilaterally keep. Negotiate now — before the next incident — what [Foundation] will actually do on your escalation request, get it in writing, and name a real contact. If they won't commit to anything, say that in the reporter-facing summary rather than implying a ban you can't deliver.

---

## 3. Reporting channels

- **Primary**: `conduct@pinegrain.dev` — a domain you own, so it survives any Reddit or Slack policy change. Reaches the 3-person Pinegrain Conduct Team, named publicly.
- **Alternate** (for reports *about* a Conduct Team member): a separate address reaching a person or body not on that team — you need to name this person; right now nothing fills this role.
- **Anonymous option**: a linked form (e.g. a simple hosted form) forwarding into the same inbox without capturing identity unless the reporter chooses to provide it.
- **Acknowledgment target**: 2 business days, proposed as a starting gate between Django's 1 and CNCF's 3 — recalibrate once you have a quarter of real volume.
- **No-retaliation clause**: published in the CoC above.
- **Named recipients**: placeholder only above — a report with no real names attached to it gets reported less; fill this in before publishing.

---

## 4. Response team

- **Day-to-day moderators**: whoever already holds mod tools on r/pinegrain plus whoever has channel-management access on #pinegrain. Their power stops at content removal and time-outs.
- **Pinegrain Conduct Team** (the deciding body): recommend 3 named people minimum, with 1–2 alternates, so the team survives one person being unavailable. Only this team can apply rungs 3–4.
- **Escalation body**: **not yet named — this is the open item flagged at the top.** Options: a small "founding maintainers" group who are not on the day-to-day Conduct Team, or, if Pinegrain ever gets a fiscal host, that host's board.
- **Tiered powers**: remove a post → time out → temporary suspension → permanent ban, top rung reserved for the Conduct Team, mirrored across Reddit/Slack/GitHub as far as each platform allows.
- **Recusal**: hard conflict (accused, close relationship, personal stake) — excluded from discussion, vote, and materials. Soft conflict (same employer, appearance of conflict) — may discuss, may not vote.
- **Load cap**: propose 5 hours/week per moderator, rotating weekly triage duty, given the team is volunteer-run.
- **Employer cap**: unknown whether any moderators share an employer or sponsor relationship — flagged as an open question; if yes, cap seats per employer now, before it becomes a live recusal problem.
- **Moderator agreement**: each moderator signs off in writing on their powers, confidentiality duty, recusal duty, what they escalate rather than decide alone, and how to step down without drama.

---

## 5. Runbook summary (private — do not publish this section; publish only the reporter-facing "what to expect" page)

```
Team          3 named Conduct Team members + alternates. Escalation body: [NAME PENDING].
Intake        conduct@pinegrain.dev primary, escalate@pinegrain.dev for reports
              about the primary team, anonymous form as a third path.
              Acknowledge within 2 business days.
Handling      Recusal declared and graded before investigation starts. Read
              evidence first, then interview reporter → witnesses → reported
              person. Decision rule: 2 non-conflicted members must agree,
              consensus is the target, 2/3 majority the fallback, deadlock
              escalates to [escalation body]. Decide within 10 business days.
              Judge impact before intent.
Outcomes      The ladder in §2, plus non-ladder outcomes in the CoC.
Communication Show the proposed response to the harmed person before acting
              (to catch missed facts, not for approval). Notify the reported
              person: behavior, impact, expected change, consequence — never
              name the reporter, never request an apology.
Records       case_code, report_date, surface, person_codes, neutral_summary,
              scope_determination, safety_risk, conflicts_declared,
              investigation_notes, decision, rung_applied, effective_date,
              end_date, communications_sent, closure_date, follow_up.
              Team-only access. Leaking a case is grounds for removal from
              the team.
Review        Aggregate stats every 6 months. Annual anonymized trends report.
              Ladder review triggered by any case the team found hard to place.
```

**Evidence preservation, specific to your two rented surfaces**: screenshot and archive pile-on threads *immediately* on both Reddit and Slack — Reddit comments vanish on deletion, and Slack messages can be deleted by their author or, on some plans, purged by workspace retention policy that Pinegrain doesn't control. Don't rely on either platform's own history as your case record.

---

## 6. Platform control sheet

Ranked by inflow stopped per moderator-hour, per the skill this follows: rate limits and entry gates first, earned trust levels next (worth the week of setup precisely because you asked for them), automatic filters, individual bans last.

### Raid-night rate limits

| Surface | Control | Notes |
|---|---|---|
| r/pinegrain | **Crowd Control** (auto-collapses comments from low-karma/unvetted accounts) | Pre-enable now, not during a raid — it's a one-time setting. |
| r/pinegrain | Temporary switch to **Restricted posting** (approved submitters only), or an AutoModerator rule gating new comments by account age/karma | Write the AutoModerator rule now and keep it disabled-but-ready; flipping it live during a raid is the whole point. |
| r/pinegrain | Strict mod-queue for new-account comments during a declared raid window | Manual toggle, minutes of work. |
| #pinegrain Slack | **No native slow-mode exists at the channel level.** Your real options: pin a holding note redirecting to the owned surface below; if channel-manager tools permit, restrict posting; otherwise call the pre-arranged [Foundation] contact and ask for a temporary workspace-side restriction. | This is the gap you cannot close with settings — close it with a relationship instead. Get a named emergency contact at [Foundation] before the next raid, not during it. |
| Owned surface | Stand up a **Pinegrain-owned GitHub Discussions category** (or a status page) now, as the pressure valve you fully control | When a thread goes hostile on Reddit or Slack, you can lock/hide/ban there instantly regardless of what either rented platform allows. This is the single highest-leverage thing on this whole sheet, because it's the only surface where every future control actually works. |

### Trust levels — letting long-timers help police it

Neither Reddit nor Slack has a native trust-level system, so mirror it manually, per the skill's guidance: grant flagging power, never ban power, which stays reserved for the Conduct Team.

- **r/pinegrain**: grant "Approved User" / contributor flair to long-timers with a clean record (no prior actioned report, a visible history of de-escalating rather than just posting a lot). Flair bypasses AutoModerator gating during a lockdown and marks them for a fast-tracked report route to the mod team.
- **#pinegrain Slack**: create a `@pinegrain-regulars` Slack user group for the same cohort. Give them a private `#pinegrain-mod-alerts` channel to fast-track a flag straight to the response team during a pile-on, instead of hoping a moderator happens to be online.
- **Nomination**: pulled from observed de-escalation behavior, approved by the Conduct Team — not from tenure or karma alone, and revocable (a "role removal" outcome) if the privilege is misused.
- **Hard boundary**: regulars flag and vouch; they never remove content or ban anyone. That stays with the Conduct Team on every surface, including Slack, where you don't have the removal authority to delegate even if you wanted to.

### Content actions (ordered by reversibility, not efficiency — pick the one the situation needs)

1. Hide/remove with a stated reason — native on Reddit; on Slack, pin an explanation since you likely can't edit someone else's message.
2. Redact — Reddit mods can remove but not edit another user's post, so this becomes "remove, then the person reposts redacted" or a moderator quote-and-redact in a new comment; note this platform limitation in the runbook so nobody expects a clean in-place edit.
3. Lock the thread — native on Reddit; no native equivalent on Slack, so the fallback is a pinned "closed" note plus a request to [Foundation] to archive if it's severe enough to need it.
4. Delete — last resort on either platform; capture the content in the case file first, since deleting is also deleting your own evidence.

### Volume floods (AI-slop issues/PRs — flagged as a guess, confirm it's actually a frequent problem)

If low-quality or AI-generated issue/PR floods turn out to be real (common for a graph-DB OSS project), this is not a conduct-ladder problem — there's usually no malice to escalate against. Gate on GitHub interaction limits and a contribution-history floor instead of trying to detect authorship; there's no reliable technical signal for that. Address only if confirmed — see Open Questions.

---

## 7. Announcement post (draft)

> **Pinegrain now has a published Code of Conduct and moderation process.**
>
> After two difficult incidents this quarter, we're publishing how Pinegrain
> actually handles harassment and pile-ons across r/pinegrain, #pinegrain, and
> GitHub — what the response team can do on each, how to report (including
> anonymously), and what happens after you do. Read it at
> [link to CODE_OF_CONDUCT.md]. Questions or concerns: conduct@pinegrain.dev.

---

## 8. Publish gate

| # | Item | Status |
|---|---|---|
| 1 | Applies to the most powerful people | **Fail until confirmed** — drafted as unconditional, but you must actually mean it |
| 2 | Scope names surfaces, people, off-platform stance | Pass, once adopted |
| 3 | Every rung has trigger + consequence | Pass |
| 4 | Time-boxed sanctions state duration | Pass (30–90 day bands) |
| 5 | Private channel reaching a named group | **Fail** — mechanism exists, names don't yet |
| 6 | Second channel for reports about the primary recipient | **Fail** — nobody named yet |
| 7 | Acknowledgment target the team can hold at current volume | **Unverified** — 2-day target is a guess against an unknown team size |
| 8 | No-retaliation statement published | Pass |
| 9 | Escalation body named | **Fail** — the central gap |
| 10 | Case-record location/access/retention in writing | Pass, once adopted |
| 11 | At least two people can execute every action the ladder promises | **Fail on Slack specifically** — you need at least two people with a live escalation relationship to [Foundation]'s admins, not just two Reddit mods |

Five of eleven fail right now — all fixable by naming real people and one real conversation with the foundation, not by rewriting the design.

---

## Open questions for the user

- ℹ️ Would this actually be enforced against a Pinegrain founder or top maintainer? If not, say so now — that changes item 1 from a draft note to a scoping decision.
- ℹ️ Who are the 3+ real names for the Conduct Team, the alternate report recipient, and the escalation body above them? Nothing publishes without these.
- ℹ️ Does Pinegrain have any relationship with [Foundation]'s Slack admins today? A named emergency contact there is the one piece of this whole setup you can't build with settings alone.
- ℹ️ How many people currently moderate, and how many hours a week can each realistically give? This resets the acknowledgment target and the load cap.
- ℹ️ Is a GitHub Discussions category (or equivalent owned surface) already live? If not, standing it up is the highest-leverage single action on this whole list.
- ℹ️ Is the AI-slop/low-quality-submission problem real and frequent, or was that an assumption on my part? Confirm before building the volume-gate controls.
- ℹ️ Any known minors, contractual customers, or shared-employer moderators in the room? Each changes a specific control (entry-gate data handling, recusal rule, employer cap).