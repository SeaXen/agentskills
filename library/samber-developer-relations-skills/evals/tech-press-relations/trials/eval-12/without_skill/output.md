# Greyhollow Launch-Day Runbook — Tuesday

## Three things in your plan will actively hurt you. Fix these first.

**🔴 Asking 30 people to upvote HN in the first hour will likely get the post killed, not boosted.**
HN's detection actively looks for coordinated voting from a known cluster (same company, same time window). Outcome is usually a "flame war detector" penalty or a flag-kill — worse than organic mediocrity, because now HN mods have seen your company name attached to vote manipulation on launch day. There is no upside version of this instruction.
- Fix: tell the team the post exists and invite them to read/comment if they have something real to say. Never mention upvoting, not even implicitly ("go check it out!" sent to 30 people at the same minute reads as coordination anyway — spread awareness over the whole week, not a synchronized ping).

**🔴 Pasting a press release into two subreddits is close to the worst format for Reddit, and will likely get removed.**
Corporate-announcement text, posted identically to two communities, from an account with no history in either — this is the exact pattern subreddit auto-mod and human mods filter for. "Copy-paste across subs" and "corporate announcements" are both named failure modes.
- Fix below in the Reddit section — different subreddits, different context per post, no press-release voice.

**🔴 "Argue it down with facts" is the wrong default response to a claimed KMS vulnerability, in both directions.**
If the claim is real: arguing in public before you've verified it is how a security launch becomes a security incident. If the claim is false: arguing publicly still reads as defensive, and HN/Reddit both penalize visible defensiveness regardless of who's right. Either way, "argue" is not a security response — "triage, then respond with verified facts" is.
- Full protocol below. This is the highest-stakes part of the whole launch — a secrets manager gets adversarial security scrutiny on day one as a matter of course, not as a tail risk.

**⚠️ 9:00 is very likely your local time (CEST) — check this before locking the schedule.** 9:00 CEST ≈ midnight Pacific. HN's own early-momentum window is 6–9 AM PT, which lands at ~15:00–18:00 CEST, not 9:00. Posting at midnight-Pacific-equivalent means the post gets zero organic US engagement while it's still fresh in the queue, and by the time the US wakes up it's already scrolled off `/new`.
- Fix: keep the **embargo lift / press / blog / Discord announcement at 9:00 CEST** — that's fine, those aren't algorithm-sensitive. Hold the **HN submission itself until ~15:00–16:00 CEST same day.** Nothing about the embargo requires the HN post to go up at the same minute; the repo and blog post are already public and citable all day.

---

## Pre-launch, before Tuesday

- [ ] **Publish a `SECURITY.md`** with a dedicated security contact (email, ideally with a PGP key) and a stated response SLA (e.g., "we acknowledge within 24h"). For a secrets manager, this needs to exist before launch day, not get improvised in a comment thread.
- [ ] If you've had any third-party security review, threat model doc, or audit — **link it from the README and have it ready to paste into the HN first comment.** For a secrets manager this preempts a large fraction of "how do I know this is safe" comments before they're asked.
- [ ] Check the HN account that will post: does it have real history/karma, or is it brand new? New accounts get extra scrutiny on submission ranking. If the CEO's account is fresh, consider having whoever on the team has the most genuine HN history post instead, with the CEO active in the comments.
- [ ] Confirm which two subreddits, then go read each one's sidebar/wiki self-promo rule **today** — don't assume they're similar. (See Reddit section.)
- [ ] Draft the HN first comment now (template below), don't write it live under pressure.
- [ ] Draft one short **holding statement** for "someone claims a vulnerability" so nobody has to compose it live (template below).
- [ ] Confirm who is staffed for each channel Tuesday (see Roles, below) — "I'll check as needed" is not a monitoring plan for a security-product launch with a press embargo and three simultaneous channels.

---

## Launch-day timeline

| Time (CEST) | Action |
|---|---|
| 09:00 | Press embargo lifts. Blog post goes live. Announce in your own Discord — as a normal message from a person, not a pasted press release. |
| 09:00–15:00 | Team can read/comment on any early press coverage. No coordinated action anywhere. GitHub repo should already be in final state — no code changes during the launch window. |
| ~15:00–16:00 | **Show HN post goes live.** Title format: `Show HN: Greyhollow – an open-source secrets manager`. Post the first comment (template below) within minutes, as the founder/poster account. |
| 15:00–19:00 | Peak engagement window. Whoever posted stays on HN comments continuously. Security engineer on standby (see Roles) specifically watching for any security/vulnerability claims — do not let this be the same person juggling five things. |
| ~16:00–17:00 | First Reddit post (subreddit A). Space the second subreddit post by several hours, not simultaneously — identical near-simultaneous cross-posting reads as spam even when the content is tailored. |
| ~19:00–20:00 | Second Reddit post (subreddit B), retitled/recontextualized for that community, not copy-pasted. |
| All day | Rotating monitoring shifts (see below) — HN, both subreddits, Discord, GitHub issues, Twitter/X mentions. Continuous, not "as needed." |
| End of day | Internal debrief: what got asked repeatedly (→ FAQ/docs gap), any security reports (→ triage status), what worked. |

---

## Vulnerability-claim protocol (read this before Tuesday, not during)

If anyone claims a vulnerability in the KMS integration, in any thread:

1. **Acknowledge fast, in public, within ~15–30 minutes.** Not a denial, not a defense — an acknowledgment. Example:
   > "Thanks for flagging — pulling in the engineer who built this integration now, will follow up in this thread with specifics. If you want to share exploit details privately first, security@greyhollow.dev."
2. **Route technical detail to the security contact or a private channel**, not the public thread. Public back-and-forth about exact mechanics before verification is how real KMS issues turn into public 0-days, and how false claims turn into a credibility fight neither side wins.
3. **The person who wrote that integration handles the technical response, not the CEO.** The CEO stays visible and calm in the thread ("we're on it, update coming") but does not improvise security claims in real time.
4. **Only respond with specifics once verified.** If real: say so, give a timeline, patch, credit the reporter, publish a short post-mortem once fixed. If false: respond with the actual technical reasoning once you've checked, factually and without a defensive tone — "we checked, here's why X isn't exploitable: [specifics]" reads completely differently from "you're wrong."
5. **Never post internal infra details** (hostnames, internal architecture beyond what's already public in the docs/repo) into a public thread while investigating.

This person should not also be running Reddit or Discord that day. Give them one job.

---

## Hacker News specifics

- Format: `Show HN: Greyhollow – an open-source secrets manager` — factual, no adjectives.
- First comment, posted by you immediately after submitting:
  > Hey HN, [name] here, [role] at Greyhollow.
  > We built this because [1–2 sentence real reason — not marketing copy].
  > Technical details: [KMS integration approach, what's genuinely interesting under the hood, link to threat model/audit if you have one].
  > Happy to go deep on the security architecture, happy to be poked at — that's what today is for.
- Respond to every comment for the first 2–3 hours minimum, including critical ones. Acknowledge valid concerns, don't get defensive on subjective ones.
- Team awareness only, zero upvote coordination (see top of doc).

## Reddit specifics

- Pick subreddits by self-promo tolerance, not just relevance. Zero-tolerance subs (r/programming, r/sysadmin) will pull a Greyhollow post fast regardless of quality — skip those for a direct post. Better fits for an OSS secrets manager: **r/selfhosted**, **r/opensource** — both explicitly more tolerant of OSS project posts. **r/netsec** is a real option too if you want serious security-audience eyes, but expect the harshest technical scrutiny of any channel today — only post there if the security engineer is fully staffed and ready, not as an afterthought.
- Read each subreddit's rules today, not Tuesday morning — some restrict self-promo to a weekly thread.
- Write a real text post per subreddit — context, why you built it, what's technically interesting — not a link dump of the press release. Disclose you're the maker.
- Space the two posts by hours.

## Discord

- Your own server is an owned channel — no self-promo risk. Still, write it as a person talking to your community, not a pasted release. One paragraph: what shipped, why, link.

---

## Roles for Tuesday

Don't leave this to "check as needed." Assign explicitly:

- **HN post + comments**: founder/poster (whoever has the account with real history).
- **Security/vulnerability triage**: the engineer who owns the KMS integration, dedicated for the day, not double-booked.
- **Reddit + Discord + social monitoring**: one person, rotating check-ins every 30 min during 09:00–20:00 peak, not ad hoc.
- **Press/journalist replies**: whoever owns those relationships, separate from the above.

That's the runbook. The mechanics you already had (embargo, blog post, Discord announcement) are fine — the three items flagged red were the ones with real odds of turning launch day into a bad day, and the vulnerability protocol is the one to actually rehearse before Tuesday.