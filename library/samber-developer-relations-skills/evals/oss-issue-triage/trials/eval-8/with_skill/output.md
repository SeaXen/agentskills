## Read on the request

"24-hour response on all GitHub issues" fails the capacity arithmetic before it fails anything else. This is the skill's own named failure mode, almost verbatim: **"Aspirational target — '24-hour response' from two [engineers] → publish the number the baseline supports."** I'm not drafting that line. Here's the math, what's missing to finalize a real number, and a version of the README section that says what you can actually stand behind — which is a stronger community signal than a promise that breaks the first time an SLA ticket fires.

## Why the number doesn't hold

- **Capacity given:** 2 engineers × 6 hours/week each = 12 person-hours/week on the OSS side, total. That's not 12 hours of triage — it's 12 hours for triage, review, maintenance, and releases combined.
- **Competing obligation:** those same 2 engineers carry 11 enterprise contracts at a contractual 4-hour response. That SLA is paid and binding; it wins every time it collides with the tracker. A public "24-hour on all issues" promise is a second commitment layered on the same scarce hours, with no contractual backstop — so it's the one that breaks under a support surge, not the paid one.
- **No queue baseline:** I don't have open-issue count, inflow rate, or issue type mix (bugs vs. questions vs. feature requests). The skill's own rule: don't set a response target from ambition, set it from measured capacity against measured inflow. Right now I have the capacity side only.
- **"Response" is doing a lot of work.** If leadership means "a human looks at it and says something," that's cheap and defensible. If reporters will read it as "your bug gets fixed," it's a promise you cannot make with 2 people and can't publish honestly.

Run this before locking a number in:

```bash
gh issue list --state all --limit 2000 \
  --json number,title,state,createdAt,updatedAt,closedAt,labels,author,comments > issues.json
python3 scripts/triage-baseline.py issues.json --triage-prefix "kind/,priority/"
```

If that's not available, hand-sample 50 open issues and estimate open count, age, and untriaged share. Either way, get the inflow number before the README number goes final — everything below marked `[placeholder]` depends on it.

## What I'd publish instead

Drop-in for the README, replacing "24-hour response on all GitHub issues":

```markdown
## Support and response times

PulseGrid is maintained by a small engineering team who also build the
product. We want to be honest about what that means for response times.

### Enterprise support

If you have an enterprise support contract, use your dedicated support
channel, not GitHub. Contractual response time (4 hours) and escalation
path are defined in your agreement.

### Community issues and pull requests

We triage the public tracker on a best-effort basis, on top of the
contractual support above. Our target:

- **New issues:** an initial human acknowledgment (label + short reply,
  not a fix) within [placeholder: N] business days.
- **Pull requests:** an initial direction check (does this belong in the
  project) within [placeholder: N] business days.

This is a target, not a guarantee — during a spike (support incidents,
a security report, high issue volume) it may slip. If we're behind for
more than two consecutive weeks, we'll post a note in this repo saying so
rather than let the target quietly stop meaning anything.

**Security reports:** do not open a public issue. Use
[GitHub's private vulnerability reporting](../../security/advisories/new)
so a fix can ship before details are public.

**Usage questions:** [placeholder: point at Discussions / a forum /
chat — not the issue tracker], so bug/feature triage capacity isn't spent
on "how do I configure X."
```

Fill in the two `[placeholder: N]` values from the baseline — with 12 person-hours/week split across triage, review, and maintenance for 2 people, a number in the 3–5 business day range for initial acknowledgment is a defensible starting point *if* inflow is in the tens of issues/week, not hundreds. I can't commit to a specific number without the queue data; publishing one now would be the same mistake as "24 hours," just less aggressive.

## Before this goes live

1. **Route usage questions off the tracker.** If any real share of inflow is "how do I…" rather than bugs, a chooser (GitHub Discussions, Discord, whatever you have) removes it before it ever competes with the target.
2. **Turn on private vulnerability reporting** if it isn't already — nothing above works if a security report lands in the public tracker instead.
3. **Run one real triage session, timed, on 15–20 issues** with both engineers before you commit the final day-count. That gives you the actual minutes-per-item instead of a guess.
4. **Decide the volume-gating trigger now, not during a spike.** PulseGrid is a scheduler with a year of public history — it's a plausible target for AI-generated "vulnerability" or bug reports. Decide in advance what inflow rate or bad-report share triggers capping submissions per author or requiring more structured forms, so it's policy when it happens, not improvisation.
5. **Tell leadership the tradeoff directly:** a published number they can defend in month three beats a number that reads well this week and gets publicly walked back in month two — which is worse for "serious about the community" than never promising a number at all.

Send me the `issues.json` baseline (or the 50-issue hand sample) and I'll turn the placeholders into real numbers, plus the label taxonomy and duty rotation to back the policy up.