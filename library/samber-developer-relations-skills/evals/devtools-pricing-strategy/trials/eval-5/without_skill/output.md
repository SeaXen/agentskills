A couple of things worth flagging before you ship this exact plan, then the draft itself.

⚠️ **The 2024 post said "always."** Reversing an explicit permanence promise is the highest-risk part of this — worse for trust than the storage cut itself. The draft below names it directly instead of hoping nobody notices; burying it would be worse if someone screenshots the original post.

⚠️ **Three weeks, same-day flip, for a limit cut is thin by the standard playbook** (typically months of notice + staged rollout for anything this visible). You may have reasons to move fast — but if there's room, even pushing the free-tier storage cut to a "your existing caches are safe until [date], new caches capped now" model would land softer than a hard cutover for users with >2GB already stored.

ℹ️ I've left bracketed placeholders where I don't have real specifics (eviction mechanics, exact plan/page names, contact address) — fill those from the actual product before publishing.

---

## Blog announcement (primary deliverable)

**Title:** Updates to the Tollgate Free plan, effective October 14, 2026

---

Starting **October 14, 2026**, we're making two changes to the Free plan:

1. **Free plan cache storage is going from 10 GB to 2 GB.**
2. **Build history is moving from Free to the $49/mo plan.**

If you're on a paid plan today, nothing changes for you until your next renewal on or after October 14 — see "What this means for existing customers" below.

### Why we're doing this

In 2024, [we wrote](link-to-2024-post) that the Free plan would always include 10 GB of cache storage. We're walking that back, and we're not going to pretend otherwise. "Always" was the wrong word to use in a pricing post, and we're sorry for the whiplash this causes anyone who built around it.

The short version: [cache storage cost scales directly with how much the Free plan gets used, and the free tier has grown to a size that isn't sustainable at 10 GB per account — insert your real reason here: infra cost, abuse, cross-subsidy from paid plans, etc.]. Rather than raise prices on paying customers to cover it, we're right-sizing the Free plan and moving build history — a feature that's genuinely more useful to teams running lots of builds — into the plan built for that use case.

We know a smaller free tier is a downgrade, not an improvement, and we're not going to dress it up as anything else.

### What's changing

**Cache storage:** Free plan accounts drop from 10 GB to 2 GB of cache storage.

- If you're currently storing more than 2 GB on the Free plan, [we'll evict your oldest/least-recently-used caches first until you're back under 2 GB — confirm actual eviction behavior before publishing].
- Paid plans are not affected by this change.

**Build history:** The build-history view moves from free-for-everyone to a $49/mo plan feature.

- Free plan accounts, and any paid plan below $49/mo, lose access to build history on October 14.
- The $49/mo plan and above keep full access, uninterrupted.

### What this means for existing customers

- **Free plan:** the new 2 GB limit and build-history change take effect October 14, 2026 — there's no renewal cycle to delay this on a free account.
- **Paid plans:** you keep your current build-history access and terms until your **next renewal date on or after October 14, 2026**. At that renewal, the new plan structure applies. If you're on a plan below $49/mo and want to keep build history without a gap, upgrade to the $49/mo plan any time before your renewal.

### What you need to do

- **On the Free plan, using less than 2 GB of cache and not using build history?** Nothing — you're not affected.
- **On the Free plan, using more than 2 GB?** [Back up or note anything you need before Oct 14 / nothing needed, caches are ephemeral by design — confirm which is true].
- **Relying on build history and not planning to upgrade?** Export or note what you need before your access changes.
- **Want to keep build history without interruption?** [Upgrade link].

Questions — reply to this post or reach us at [support email].

---

## Companion email to affected Free-plan users

**Subject: Changes to your Tollgate Free plan — effective October 14**

Hi [name],

Two changes are coming to the Tollgate Free plan on **October 14, 2026**:

- Cache storage drops from 10 GB to 2 GB.
- Build history moves to the $49/mo plan.

We said in 2024 that free storage would always stay at 10 GB. That's changing, and we wanted you to hear it from us directly rather than find out when a build fails. Full explanation here: [link to blog post].

Based on your current usage, [you're currently using X GB / you use build history regularly] — so this change [will / won't] affect you directly starting October 14.

If you want to keep your current storage headroom and build history, you can move to the $49/mo plan any time before then: [upgrade link].

Questions — just reply to this email.

— The Tollgate team