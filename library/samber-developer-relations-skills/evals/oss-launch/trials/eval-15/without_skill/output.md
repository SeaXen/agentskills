# Cinderpath Launch — Run of Show

**Launch date:** Wed 2026-09-30 · **Team:** You (post + lead technical response) + Dan (full day Wed) · **Constraint:** You're at a team offsite all day Thu 2026-10-01 — Dan covers solo.

---

## ⚠️ Decision needed before anything else: posting time

You said "post in the morning" — check which morning. You're in Nantes (CEST, UTC+2). HN's own best-practice window is **6–9am PT**, which lands at **3–6pm Paris time**, not French morning. A literal French-morning post (~9am Paris) hits **~midnight PT** — the dead zone, US asleep, weakest possible first-hour momentum, and HN's ranking algorithm weighs early velocity heavily.

- **Recommended:** post **3:00–4:00pm Paris time** Wednesday. Catches US East Coast late morning + US West Coast early morning + tail of European afternoon — the actual "morning" the HN skill means.
- **If you post at true French morning anyway:** accept a slow first 90 minutes, don't panic, and put someone (Dan) on the post within the first 15 minutes regardless — the algorithm rewards early comments as much as early votes.

Pick one before Tuesday EOD so the rest of this schedule can anchor to it. Everything below assumes the **3–4pm Paris** slot; shift the block if you choose otherwise.

---

## T-minus checklist (Fri 9/25 → Tue 9/29)

**Repo readiness**
- [ ] README top: 1-line pitch, a GIF/demo showing it running in <30s scroll, quickstart ≤5 commands
- [ ] License file present, CONTRIBUTING.md exists, issue templates set up (bug / feature / question)
- [ ] CI green on default branch, a tagged release (v0.x or v1.0) cut
- [ ] GitHub Discussions enabled — HN traffic asking questions belongs there, not scattered across issues
- [ ] Live demo or one-command install works from a clean machine — test it yourself Tue night, not Wed morning

**Post prep**
- [ ] Draft title: `Show HN: Cinderpath – [one-line, concrete, no adjectives]`
- [ ] Draft first comment (backstory + technical meat) — template below
- [ ] Write a 1-page internal "differentiation cheat-sheet": how Cinderpath compares to cron/systemd-timers/Airflow/Temporal/Celery, license, HA story, production-readiness claim, why Dan and you built it. Both of you read it Tuesday so answers stay consistent under pressure.
- [ ] Check karma on the account that will post. If it's low/new, expect extra HN scrutiny — not disqualifying, just don't also look brand-new *and* thin.
- [ ] Confirm neither of you has posted anything else to HN in the last 24h (dupes get merged/killed)

**First-comment template (fill and save, don't write live)**
```
Hey HN, [you] here — built this with Dan.

Backstory: [1-2 sentences: what problem you hit that existing schedulers didn't solve]

Technical bits worth asking about: [scheduling model, HA/failover approach,
storage backend, language/runtime, what's still rough]

Happy to answer anything.
```

**Never do:** ask anyone — Dan, your team, community members — to upvote. Sharing the link internally for *awareness* is fine; coordinating votes gets both posts and accounts penalized.

---

## Wednesday — launch day

| Time (Paris) | Time (PT) | Action | Who |
|---|---|---|---|
| 2:30pm | 5:30am | Final smoke test of install/demo path. Confirm CI green. | Both |
| 2:45pm | 5:45am | Post goes live. Immediately add the first comment (from template, personalized). | You |
| 2:45–4:45pm | 5:45–7:45am | **Heaviest window.** Refresh every 5-10 min. Answer every comment, especially critical ones — acknowledge valid concerns, don't get defensive, don't argue with trolls. | You (primary), Dan (backup if you're mid-answer on something long) |
| 3:00pm | 6:00am | Dan starts GitHub triage: label incoming issues (bug/question/feature), don't promise timelines publicly, route "how does this compare to X" questions to the cheat-sheet answers so wording stays consistent with your HN comments. | Dan |
| 3:15pm | 6:15am | Once the post has visible traction (a handful of upvotes/comments), share the link once on your own social (X/LinkedIn) and any Slack/Discord communities where it's genuinely relevant. One post per channel, no repeats. | You or Dan |
| 4:00–6:00pm | 7:00–9:00am | Cross-post to Reddit (r/programming, r/devops, r/selfhosted, or a language-specific sub if relevant) and Lobsters if applicable. Space these out — don't fire everything in the same 5 minutes, it reads as coordinated. | Dan |
| Through EOD | — | Keep checking HN every 20-30 min even after the initial rush — late important comments (a maintainer of a competing tool, a "used this in prod" story) still show up hours in. | Both, alternating so neither of you is glued to it all evening |
| ~7pm | ~10am | End-of-day sync: what shipped as follow-up issues, what needs a fix before Thursday, what questions came up that the cheat-sheet didn't cover (add them to it tonight while fresh). | Both |

**If it's not gaining traction by ~4:15pm Paris (90 min in):** don't repost, don't ask for votes. Keep answering whatever comments exist, lean a bit harder on the Reddit/community cross-posts, and treat it as a data point — worth revisiting title/timing in 24h+ if it dies, per HN's own recovery guidance.

**Success signal to actually track:** not front-page rank — count meaningful technical comments, GitHub stars/clones, and issues opened. A post with 40 points and 15 sharp technical comments beats 200 points and no signal.

---

## Thursday — you're at the offsite, Dan solo

Hand this to Dan Wednesday night:

- **Your availability Thursday:** [fill in — fully dark, or checkable at breaks?]. State it explicitly to Dan so he's not guessing.
- **Dan owns:** ongoing HN thread replies, GitHub issue triage, Reddit/community thread replies.
- **Dan does NOT do solo:** commit to a roadmap item publicly, promise a release date, make a licensing statement, or handle anything that smells like a security disclosure.
- **Escalation rule:** text/call you only for (a) a security report, (b) something legally/publicly sensitive, (c) a decision that can't be walked back later. Everything else waits for Thursday evening or Friday.
- **End-of-day ping:** Dan sends you a short summary Thursday evening — thread status, open issues needing your input, anything he deferred.

---

## Friday — reconvene

- Read Thursday's summary, answer anything Dan flagged.
- Post a short follow-up (HN comment or a "thanks for the feedback" note in Discussions) if the thread is still active — closes the loop for anyone who came back.
- Skim new GitHub issues/PRs for anything worth turning into a "good first issue" — Show HN traffic often converts to first-time contributors in the following week, and unlabeled backlog is the main reason that doesn't happen.