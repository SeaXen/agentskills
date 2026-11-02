**One-line answer for investor:** "Free tier not cost center — it's our CAC channel. Storage cap (50GB) do the gating. Devices and bandwidth cost us near-zero, so leaving them unlimited kill friction, not margin."

## Why each limit hold up

- **50GB storage cap = real gate.** Mobile apps (photos, video, user content) grow past 50GB as app succeed. That's natural upgrade trigger, tied to customer's own growth, not artificial timer.
- **Unlimited devices = near-zero marginal cost.** It's a policy flag, not infra spend. Capping it adds friction, kills exact hook driving signups. No investor should want you to cap a free feature that costs nothing.
- **Unlimited bandwidth = defend with mechanism, not just confidence.** Sync bandwidth track stored-data volume — deltas, not full re-transfers each sync. So bandwidth scale with same 50GB ceiling in practice, even though not enforced as hard cap. Say this explicitly; don't just call it "generous."

## Numbers to bring next time (pull before next conversation)

1. Cost per GB stored/month (infra bill ÷ GB stored).
2. Cost per GB transferred (bandwidth $ ÷ GB moved).
3. Free → paid conversion rate, and over what window.
4. Median free-user storage usage (likely far under 50GB — most free accounts cost pennies).
5. LTV of $99/mo customer vs. cost to carry one free signup.

One real number here (even rough) beats any amount of verbal defense. Investors push on "unlimited" because it sounds uncapped, not because they distrust the strategy.

## Objection script

- **"Doesn't unlimited bandwidth blow up costs?"** → Bandwidth scale with stored data via delta sync, not detached from it. [insert your $/GB number once pulled]
- **"What stops abuse?"** → If no answer today, that's the gap to close (see below).
- **"Why give away this much?"** → Free tier is our CAC channel. Conversion happens when free users' data outgrow 50GB — that's the paid trigger, not a discount.

## One real gap to close before next meeting

Unlimited bandwidth with no fair-use safeguard is genuine open exposure — a single abusive account could re-sync heavily across many devices with zero revenue. Add soft fair-use throttle (flag/rate-limit accounts syncing many multiples of their stored size per day). Cheap to build, and turns "unlimited" into "generous but protected" — the strongest possible answer to give.

**Next action:** pull cost-per-GB-stored and cost-per-GB-transferred from this month's infra bill. That single number kills most of the pushback before it starts.