# Cinderpath — Launch Day Run of Show

**Launch:** Wednesday, September 30, 2026 (T+0) — Show HN as anchor
**Crew:** You (Voice) + Dan (Triage / Amplifier / Watcher)
**Fixed constraint:** you're offline all day Thursday, October 1 (T+1, team offsite). Dan covers that day solo.

*(If "next Wednesday" means something other than Sept 30, shift every date below by the same offset — the hour-by-hour structure doesn't change.)*

Two things to close before this plan is safe to run, not optional:

- **A working `SECURITY.md` with a private contact path.** The one branch of this runbook you can't improvise is a security report landing mid-thread — it only works if that contact path already exists on Tuesday.
- **The posting hour.** "Morning" needs a timezone. If that means your morning (Paris), you'd post around 3–4 AM US Eastern — the post decays for hours before the bulk of HN's readership wakes up, since HN ranks on points divided by elapsed time. Recommendation below assumes you shift to **early Paris afternoon** to catch US-morning readers while the post is still fresh. Overrule me if you have a reason not to.

---

## T-24h — Tuesday, September 29 (pre-flight)

- **Re-run the install command on a clean machine.** Nothing else here matters if it fails.
- **Click every link in the draft post** — repo, README anchors, docs, registry page, social preview image.
- **Freeze `main`.** No refactors between now and Thursday.
- **Capture the baseline tonight**, outside whatever traffic panel you use: stars, unique visitors, cloners, current issue/contributor count, referrers. It's not recoverable once the panel's rolling window moves.
- **Confirm both your calendars are clear Wednesday** — no back-to-back meetings for either of you.
- **Draft and review together:** Show HN title, first comment, your own social post, and three answers to the hardest question someone will ask (the obvious one for a job scheduler: "why not cron / Celery / Temporal / Airflow").
- **Agree the scope-cut rule now.** If a broken install path turns up at T-2h, decide in advance what gets cut rather than debating it live.
- **Agree what Dan can commit to publicly** — roadmap dates, licensing statements — before he's alone in the thread Thursday. Default: Dan answers technical questions and opens issues; anything about direction or licensing waits for you.

## T+0 — Wednesday, September 30 (post)

- **You post the Show HN**, from your own account with real history — not a fresh or throwaway one.
  - Title: `Show HN: Cinderpath – <plain description, no adjectives>`
  - Recommended window: **~14:00–15:00 CEST** (≈8–9 AM US Eastern), mid-week. Adjust only if you've checked where Cinderpath's likely early adopters actually are.
- **Post the first comment within 1–2 minutes of the submission going live.** A bare link invites drive-by dismissal; context invites real replies.

```
I'm <you>, I built Cinderpath because <the concrete problem — the gap in cron/Celery/
Temporal/whatever you were actually fighting>.

Under the hood: <one or two decisions a scheduler-literate reader would ask about first —
e.g. how you handle retries, distributed locking, or drift — and why you chose that over
the obvious alternative>.

What it does not do yet: <real gaps — HA story, UI, language support, scale ceiling,
whatever a critic would raise first>.

Happy to go deep on <the areas you can actually defend under questioning>.
```

Fill the brackets before Tuesday — don't write this live.

## T+0 to T+4h — the window that decides

This is where nearly the whole outcome gets set. Two of you, four roles — split them like this:

| Role | Owner | Job |
|---|---|---|
| Voice | You | Every reply in the HN thread. One voice, so tone stays consistent. |
| Triage | Dan | Incoming issues/PRs; ship and merge small fixes same-hour. |
| Amplifier | Dan | Your own-account post at T+30–90min, linking to the *discussion* not duplicating it. |
| Watcher | Dan (between the above) | Link/demo uptime, metrics snapshots. |

Reply priority when comments stack up: **technical questions → criticism → "why not X" comparisons → praise.**

| Comment type | Response |
|---|---|
| Valid technical objection | Agree, explain the trade-off, invite the better idea, open an issue and link it. |
| Misunderstanding | Clarify once, plainly — never "as stated in the README." |
| "Why not just use X" | Answer seriously. Highest-value question in the thread. Name where X genuinely wins. |
| Feature request | Yes / no / later — "later" always with a reason. |
| Hostility or trolling | One factual reply at most, or none. Never the last word. |
| Licensing/business-model suspicion | State the model plainly, what's closed, what never will be. Vagueness here is fatal. |

If something breaks — fix it the same hour and **say so in the thread.** Visible repair converts more skeptics than any argument does.

## T+4h to end of day (still Wednesday)

- Check back hourly even as it slows. Late comments shape how the thread reads tomorrow.
- Log every question that comes up **more than twice** — that's your next README/FAQ edit, not just a thread reply.
- Fire the secondary-community posts on schedule (T+2–6h window) even if the HN thread has gone quiet — some launches get carried by the secondary wave, not the anchor.
- **Don't repost or resubmit today**, whatever the thread does. A dead thread stays dead until the second-chance pool or a year passes — never a same-day retry.

## T+1 — Thursday, October 1 (you're at the offsite)

This is the gap that needs a real plan, not a hope:

- **Dan runs solo** — merges Voice + Triage + Watcher, drops Amplifier if it competes for time (`Voice > Triage > Watcher > Amplifier` when one person is covering).
- **Dan's authority, agreed Tuesday night, not improvised Thursday morning:** answers technical questions and "why not X" freely; on roadmap commitments, dates, or licensing, replies with "let me get you a precise answer" and flags it for you, rather than guessing.
- **You check in once, off-hours** — a five-minute phone glance at the thread over lunch or in the evening is enough; don't try to half-attend the offsite and the thread at once.
- Ship any small fixes Dan can safely land solo; hold anything structural for Friday when you're both back.

## T+2 to T+7 — Friday Oct 2 through Wednesday Oct 7

- Ship the fixes the launch surfaced and cut a release. Visible momentum matters to everyone who bookmarked it Wednesday and hasn't come back yet.
- Answer every issue and PR — even a one-line "looking at this later this week" beats silence.
- Fire the second wave: long-form write-up, any secondary community you deliberately staggered, newsletters that missed launch day.
- Thank the first external contributor by name in the release notes. Worth more than the star count.

## If a security report lands in the thread — separate procedure, run it exactly

1. **Stop discussing specifics publicly.** One brief reply pointing at `SECURITY.md` and the private contact.
2. Open a private advisory, add the reporter as a collaborator.
3. Patch on a private branch.
4. Publish the advisory, crediting them, once fixed.

Don't debate severity in the open thread — it reads as defensive either way and hands out exploit detail for free. This only works because the contact path exists *before* Wednesday.

## The one rule to say out loud to Dan before Wednesday

Never ask anyone to upvote, star, or comment — not in DMs, not "hey go check it out" framed as a nudge. HN penalizes the submission, the account, sometimes the whole domain, and the penalty is invisible from outside — you'd never learn why it died. "Go look" is fine. "Go upvote" is not. Make sure Dan draws that line the same place you do before either of you messages anyone Wednesday morning.