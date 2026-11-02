## Why the fumble happened

"Pretty generous" is the tell. The skill I used to build this (`devtools-business-model`) names this exact failure mode: **free tiers priced in adjectives**. "Generous" is not a number, and an investor hears it as "nobody has computed the marginal cost of a free user." That's what actually got fumbled — not the free tier itself.

The second problem sitting underneath it: 50 GB + unlimited devices + unlimited bandwidth is not obviously an *organization-only* boundary. A solo developer wants exactly that. If nothing about the free tier is something only a company needs, an investor is right to ask what forces anyone to ever pay $99.

## Run it through the paid-boundary test

Five gates, from the skill's scorecard. Answer these in writing before the next conversation — a "no" here is a blocking failure, not a weak point to talk around.

| Test | Verdict for Cindersync | Why |
|---|---|---|
| **Organization-only** | ❌ unclear / likely fails as described | Storage, devices, bandwidth are things a solo indie dev wants exactly as much as a company. Nothing here is inherently a company-only need. |
| **Defensible without hostility** | N/A (not open source) | Skip — this test is for OSS forks. Not your risk. |
| **Observable trigger** | ❌ unproven | You haven't stated what % of free accounts ever approach 50 GB. If almost nobody does, storage isn't the trigger — it's decoration. |
| **Cost-to-serve covered** | ❌ unquantified | "Unlimited bandwidth" with no cap is the dangerous phrase in the whole pitch. You don't have a number for what a free account can cost you in the worst case. |
| **Licence-compatible** | ✅ | Not applicable, hosted proprietary service. |

Two failing gates is the actual reason the room felt uneasy. Fix those two and the free tier becomes a strength again instead of a question mark.

## Fix #1: put a currency number on cost-to-serve

Before the next meeting, compute this — don't estimate it live in front of an investor again:

```
Marginal cost per free account/month =
    (avg GB stored × your storage cost per GB-month)
  + (avg GB egressed × your bandwidth cost per GB)
  + (support/infra overhead allocated per account)
```

Then compute the **worst case**, not the average — this is what "unlimited bandwidth" actually exposes you to:

```
Worst-case cost per free account/month =
    (50 GB cap × storage cost per GB-month)
  + (p99 bandwidth account, not average × bandwidth cost per GB)
```

If you don't know the p99 number, that's the gap — instrument it this week. The answer you want in the room isn't "it's generous," it's: *"our median free account costs us $X/month, our worst-case account under fair use costs $Y, and we recoup total free-tier COGS across Z months from the conversion funnel that same free tier feeds."* Three real numbers beats one adjective.

## Fix #2: "unlimited" needs a fair-use ceiling

The constraint table in this skill is blunt about this: heavy per-user infrastructure cost eliminates uncapped free tiers, full stop — it favors "hosted models with caps" instead. You almost certainly already throttle abuse informally; say so explicitly. Reframe internally (not necessarily in marketing copy) as "unlimited for normal mobile-app sync usage, with fair-use limits that stop a single account from costing more than a paying customer." That single sentence closes the scariest follow-up question ("what stops someone from running a free CDN on your dime?") before it's asked.

## Fix #3: name the real reason someone pays $99

Storage volume is the wrong trigger for a mobile sync backend — most app data is small, so most free accounts will never feel a 50 GB ceiling. That's not a bug in your framing, it's information: **the boundary needs to move off storage volume and onto something organizational.** Candidates that pass the organization-only test, none of which a solo developer building nights-and-weekends needs:

- Multiple developers/seats on one project
- An SLA / guaranteed response time
- Audit logs, data residency, or a signed DPA
- Staging + production environment separation
- Priority incident support

If $99 already buys some of this, say so plainly next time — that's your actual answer. If it doesn't yet, that's the roadmap item to point to: *"today the paid tier is priced on storage, we're moving the primary trigger to team/compliance needs because that's where the real willingness to pay lives — storage headroom stays generous because it's genuinely not the thing companies are buying."*

## The evidence to bring next time

One leading indicator, read monthly, that moves before revenue does: **% of free accounts that cross into needing a second seat, an SLA conversation, or a compliance ask, and their conversion rate to paid within 60 days of that signal.** That number — not signup count, not storage utilization — is what tells an investor the free tier is a funnel, not a subsidy.

## The 90-second answer, filled in with your numbers

> "Our free tier is generous on purpose because it's how a developer self-qualifies without ever talking to sales — that's most of our CAC advantage. It's not undisciplined: our median free account costs us $[X]/month to serve, our worst case under fair-use limits is capped at $[Y], and we recover total free-tier cost within [Z] months from the conversions that same channel produces. The free tier isn't designed to convert on storage — [N]% of free accounts never use a third of the 50 GB — it converts when a solo project becomes a team: that's when someone needs seats, an SLA, or compliance evidence, and that's exactly the boundary our $99 plan is built around."

Fill in X, Y, Z, N from your own telemetry before you say this to anyone. Quoting a number you haven't measured is the same failure mode as the adjective you're trying to replace.

## If this diagnosis is wrong

- If worst-case free-account cost is already trivial (sub-dollar), the cost-to-serve gate isn't actually a risk — say that with the number, and the whole conversation shortens to one sentence.
- If storage volume turns out to already be a real, frequently-hit trigger, don't move the boundary — instrument and quote the hit-rate instead.
- If $99 already buys team/compliance features today, this whole exercise is a communication fix, not a pricing fix — the founder just needs the script above, not a repricing.