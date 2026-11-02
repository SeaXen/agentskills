## Diagnosis first — the two numbers you're citing are almost certainly measuring the bots, not the team

Before answering "what else can we automate," the two automations you already shipped need to be checked, because the metrics you quoted are exactly the failure this framework warns about: *"under machine-generated volume, closure ratios and time-to-close can improve while real maintainer burden rises"* (CHAOSS). Your two triagers reporting burnout while the board slide looks great is not a contradiction — it's the symptom.

**The 3-hour median time-to-first-response is very likely counting the welcome bot's comment as the response.** CHAOSS's own metric definitions (*Time to First Response*, *Issue Response Time*) exclude bot replies and author self-replies by definition — a bot posting "thanks for filing!" seconds after creation is not a response, it's a receipt. If whatever produces that 3-hour figure isn't filtering the welcome bot's author out, you're not measuring how fast a human looks at an issue. You're measuring how fast your bot runs. Pull the number again with the bot's account excluded — that's the number that belongs on the slide, and it's probably much worse than 3 hours.

**The 40% closure-ratio increase is doing the same thing on the other end.** An LLM auto-closing anything it scores as a duplicate inflates "closed" without any triager doing the closing. That's not a productivity gain, it's an accounting change — and this skill's own findings file is explicit that full automated duplicate-*closing* is not an established safe practice: manual search discipline is what dominates in production triage today, and even Mozilla's own ML triage tooling stops at component assignment, not duplicate detection, despite planning to go further. Step 8's rule is blunt: *"every documented ML triage deployment keeps a human as final decision-maker: treat model assistance as a scoring and suggestion layer, never an autonomous accept, reject, or close."* An auto-close on a duplicate score is a close decision, not a classification. It's the one thing this design explicitly says never to hand to a model.

That also explains the fried triagers better than "too many issues" does: every false-positive auto-close creates a reporter who comes back angry, reopens, or files a second issue — cleanup work that doesn't exist in a system where a human made the call once. You've likely traded a bounded amount of triage work for an unbounded amount of *damage control*, and damage control is worse for morale than triage.

## So: don't automate anything else yet. Fix what's already automated.

1. **Recompute time-to-first-response with the welcome bot's account excluded.** That's the real number. Put it on the next board slide next to the current one, labeled, so leadership sees the gap and understands why it's closing slower than 3 hours looks.
2. **Pull a sample of the LLM's auto-closed "duplicates" — 30 to 50 — and have a human re-check them.** You need the false-positive rate before you can trust this step at all. If it's meaningfully above zero, that's your fried-triager root cause, not queue volume.
3. **Downgrade auto-close to auto-suggest.** Keep the LLM doing the search and the scoring — that part is real, useful work — but have it apply a `possible-duplicate` label and link the candidate instead of closing. A triager confirms with one click. You keep almost all the time savings and stop manufacturing reopens. This is the difference between automating classification (fine) and automating the decision (not fine).
4. **Add the pairing metric this framework requires for every count metric: how many issues get a genuine human reply, and how many people could cover triage if one of your two left.** Right now that second number is 2, which is a bus-factor problem independent of everything else here — one triager burning out and quitting doesn't just slow you down, it potentially takes the whole rotation with it.

## What's actually safe to automate further, once the above is fixed

These reduce real triager minutes without touching a metric that can be gamed, because none of them make a decision a human should be making:

- Fill the **area label** automatically from changed file paths (for PRs) or from form fields (for issues).
- Auto-request review from the owning team/codeowner once area is set, so the wait sits on a named person instead of the general queue.
- Run a **staleness sweep restricted to the waiting-on-reporter state only** — never on anything a maintainer owns — with a dry run first.
- Sync the "who's on triage duty" field to a rotation calendar (Mozilla's pattern) so requests route to whoever's actually working this week, not one name that's now fried.

## The bigger lever, if two triagers really is the ceiling

If the honest (bot-excluded) numbers show capacity below inflow even after the fixes above, more automation on the response side won't close that gap — cutting intake will. A validated issue form with a required minimal-reproduction field, plus routing usage questions to a forum/discussions instead of the tracker, removes work before it ever reaches a human, which is the only lever here with compounding value instead of one-time cost. That's a separate design pass (issue forms + chooser routing), but it's the next conversation once the current numbers are trustworthy — not before.

## What I'd need to go further

I don't have birchkit's actual issue data, so everything above is diagnosis from what you described, not a measured baseline. To do the real capacity arithmetic (triagers × hours/week × real minutes-per-item vs. actual human-only inflow) and size a first-response target you can actually publish, I'd need:

- `gh issue list --state all --limit 2000 --json number,title,state,createdAt,updatedAt,closedAt,labels,author,comments` from the birchkit repo
- Confirmation of the welcome bot's and the LLM-closer's bot account names, so they can be excluded from the metrics script
- Each triager's realistic hours/week in a bad month (not a good one)

That's the step-1 baseline this framework runs before anything else, and it's the thing that turns "the board slide looks great" into a number you can defend when someone asks how it was measured.