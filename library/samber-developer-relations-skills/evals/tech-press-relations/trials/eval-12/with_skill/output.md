Read the skill and its two most relevant reference chains — `tech-press-relations` (Steps 6–7, `announcement-playbooks.md`, `press-kit-checklist.md`) and the skill it explicitly routes channel-sequencing questions to, `oss-launch` (`launch-day-runbook.md`, `channel-playbook.md`) since your plan mixes press embargo mechanics with HN/Discord/subreddit mechanics, and the two skills disagree on nothing but need reconciling on timing.

Two parts of your plan aren't launch risk, they're existential risk for a secrets manager. Fixing those first, then the full runbook.

## 🔴 Two blockers — do not run the plan as written

**1. "Ask the team's 30 people to upvote it."** Delete this line entirely. HN's own rules: soliciting votes gets the submission, the account, and sometimes the whole domain penalized, and voting rings are detected. This isn't a soft norm — a domain-wide penalty on launch day silently kills every future post from your site, and you won't get told why. Compliant version: tell the team the thread exists and ask them to read and answer questions they're qualified on. Never "upvote," never "go vote."

**2. "If someone claims a KMS vulnerability, we'll argue it down with facts."** This is the one failure mode both skills call out by name, in identical terms: stop discussing it publicly, don't debate severity or exploit detail in the open — arguing looks defensive whether the claim is right or wrong, and it hands a live exploit discussion to a public thread on a secrets manager. The procedure (Google's OSS Vulnerability Guide / GitHub Security Lab coordinated-disclosure sequence, which both skills cite as the standard):

1. Reply once, in-thread: point at `SECURITY.md` and the private contact, say nothing else about the claim.
2. Add the reporter as a collaborator on a private security advisory (GitHub Security Advisories or equivalent).
3. Patch on a private branch.
4. Request a CVE if warranted.
5. Publish the advisory and ship the fix together, crediting the reporter.

This only works if a monitored `SECURITY.md` contact already exists and is checked continuously starting Tuesday morning — **confirm this exists before you post, it's a launch blocker, not a nice-to-have.** If it doesn't exist yet, that's this week's most important task, above anything else in this runbook.

## Three more fixes, lower severity but still load-bearing

- **"I'll check threads 'as needed'."** Both skills single this out by name as the wrong answer — "as needed" is not a cadence. You need a named person per channel and a stated check interval (below).
- **Press release pasted into Discord + two subreddits.** A pasted press release in a community reads as spam/bot and gets removed — Discord needs the showcase channel (ask a mod first), subreddits need the sidebar/showcase-thread rules read and the post rewritten in that community's own register, problem-first, link last. Never the same blurb twice.
- **HN, Discord, two subreddits, and embargo lift all firing at 9:00 simultaneously.** Four simultaneous "primary" posts produce four dead threads — everything ranks on early engagement density, so splitting attention at T+0 starves all of them. Fix: one anchor (HN) fires at T+0; Discord and the two subreddits fire staggered, T+2h to T+6h, each rewritten for that room.

---

# Greyhollow launch-day runbook — Tuesday, 2026-09-22

Times relative to the HN post (T+0). Set the actual clock hour to when your primary developer audience is at their desk — not a US-default assumption unless that's actually where your audience is.

## Monday (T-24h): pre-flight

- **Run the install command on a clean machine, start to finish, today.** Nothing else here matters if this fails Tuesday morning.
- **Verify every link that will appear anywhere Tuesday**: repo, docs, demo, README badges, press page.
- **Freeze the default branch** from tonight through end of Tuesday. No mid-launch refactors.
- **Confirm `SECURITY.md` is live, links to a real monitored contact, and someone is actually watching that inbox Tuesday** — this is the blocker from above, made concrete.
- **Leak check** — confirm none of these have already surfaced the story: pushed tag, public release draft, package already live on a registry, a merged PR or milestone that names the launch, a docs deploy, a changelog entry, a licence/pricing file, a status-page note. If the repo's been public and any of these already shipped, your embargo is already broken — find out tonight, not at 9:00.
- **Capture your baseline tonight, outside the traffic panel**: stars, unique visitors, cloners, docs sessions, any existing registry downloads, branded search, referring domains. Unrecoverable once the day starts.
- **Write and review, tonight, not Tuesday morning**: the HN title, the first comment, the two rewritten community posts, and honest answers to the three hardest questions — for Greyhollow, that's certainly "why trust your KMS integration over a manager with an existing security track record" and "what's your threat model."
- **Confirm nobody with a launch-day role has a meeting-heavy Tuesday.**
- **Decide your scope-cut rule now**: if pre-flight finds a real defect Monday night, what gets cut versus what gets fixed — don't debate this live at 8:45am.

## T+0 = 9:00 Tuesday: embargo lifts, HN posts

- Embargoed press coverage goes live (their doing, not yours — nothing for you to execute here beyond having briefed them).
- Your own press page and the announcement post go live on your domain, at the same minute.
- **The founding engineer — whoever actually has HN account history and can speak to the architecture under questioning — posts the Show HN.** Reconsider "CEO posts it" if the CEO doesn't have that history: new/thin accounts get stricter moderation scrutiny, and karma buys no ranking advantage anyway, so there's no upside to routing this through title rather than credibility.
  - Title: `Show HN: Greyhollow – <plain description, no adjectives>`. No "revolutionary," "next-generation," "seamless" — moderators rewrite sensational titles, and technical readers discount them on sight.

**First comment, posted within one to two minutes of the submission, by the same person:**

```
I'm <name>, I built this because <the concrete problem, one or two sentences>.

Under the hood: <the architecture decisions worth explaining — for Greyhollow
this should include the KMS integration's actual design: key handling,
encryption at rest/in transit, what's audited and what isn't, and why you
chose this approach over the obvious alternative>.

What it does not do yet: <real limitations — an unaudited security claim
here is worse than silence; state the current audit status plainly>.

Happy to answer questions about <what you can go deep on>.
```

Do not thank people in advance, do not ask for anything, do not paste marketing copy. For a security product specifically: state your audit status honestly in this comment rather than waiting for someone to ask — an unprompted "we have not yet had an independent audit; here's our plan and timeline" reads as more credible than silence that gets interpreted as evasion.

## T+30–90min: your own accounts

Founders/engineers post from personal accounts, linking to the HN discussion (not duplicating the pitch). Personal accounts outperform the company account for this; if the company account posts too, let it amplify rather than lead.

## T+0 to T+4h: the window that decides everything

- **One named person owns the HN thread continuously** — answer every comment, ranked: technical questions and comparisons to alternatives first, then criticism, then praise.
- **A second person triages incoming GitHub issues** so the thread owner never context-switches.
- **A third person watches metrics and link/demo uptime.**
- Fix small real breakages the same hour and say so in the thread — visible repair converts skeptics faster than any argument.

Response patterns by comment type:

| Comment type | Response |
|---|---|
| "Why not just use Vault / 1Password / X" | Answer seriously — highest-value question in the thread. Name where they're genuinely better. |
| Security/architecture question | Answer with specifics: encryption scheme, key rotation, threat model. This audience will probe here hardest. |
| **Anything vulnerability-shaped** | **Stop. Follow the 5-step disclosure procedure above. Do not continue in-thread.** |
| Licensing/business-model suspicion | State the model and what will never be closed — vagueness here is fatal for a security product specifically. |
| Hostility/trolling | One factual reply at most, or none. Never the last word. |

Tone for all of it: "conveying without convincing" — you're writing for the silent majority reading the thread, not for the person arguing with you. Note also: HN comments lock for editing after two hours, so a wrong number posted in haste is close to permanent — slow down on anything with a number in it.

## T+2h to T+6h: staggered secondary communities

- **Discord**: post in the project's showcase channel (not general), after confirming with a mod if the norm is unclear. Rewrite the framing for that room — problem and technical decision first, link at the end. No press release text.
- **Subreddit 1 and Subreddit 2, staggered from each other, each independently rewritten**: check each sidebar and the last month of posts first; use the weekly self-promo/showcase thread if one exists — that's the sanctioned path. Post where a maintainer already has some history if at all possible. Same rule: lead with the problem, not the announcement, link last, never the same text twice.

## T+4h to end of day

- Keep checking hourly — late comments shape how the thread reads tomorrow.
- Log every question that comes up more than twice; that's next week's README/FAQ edit.
- Do not chase a quiet thread with a same-day repost anywhere.

## T+1 to T+7 days

- Ship the fixes the launch surfaced, cut a release, and say so.
- Answer every issue/PR, even with "looking at this this week" — and hold whatever SLA you state.
- Second wave: pitch outlets that passed on the embargo, using the coverage as proof; submit to newsletters/curated lists that missed the cycle.
- Thank the first external contributor by name in release notes.

## Roles (assign named people before Tuesday, not that morning)

| Role | Owns | Escalates to |
|---|---|---|
| Voice | HN thread, all replies, tone consistency | — |
| Security contact | `SECURITY.md` inbox, monitored continuously from 9:00 | Engineer who can patch |
| Triage | Incoming issues/PRs, same-hour fixes | Voice |
| Amplifier | Discord + both subreddits, staggered, rewritten each time | — |
| Watcher | Metrics snapshots, link/demo uptime | Triage |

If Greyhollow's team is smaller than five for launch day, merge in this priority order and drop the rest: `Voice + Security contact > Triage > Watcher > Amplifier`. The amplifier posts are the ones the efficiency ranking already expects you to cut first if hours run out — better a quiet Discord than a dead HN thread.

## What I'd confirm before Tuesday, since I can't verify it from here

- **`SECURITY.md` and a monitored private contact actually exist and someone owns watching it.** If not, this is the week's top priority, not a launch-day detail.
- Whether the embargoed press outreach (Steps 3–5 of `tech-press-relations` — media map, pitch, briefing pack) already happened; this runbook assumes it did and only covers day-of execution.
- Who on the team actually has an HN account with genuine history — that person should be posting, whether or not it's the CEO.
- Current independent-audit status for the KMS integration, so the first comment states it accurately rather than getting caught flat-footed by the first security question.