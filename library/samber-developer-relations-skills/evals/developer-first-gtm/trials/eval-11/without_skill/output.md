# Ostrich Labs — PQL Rule (v1)

## The rule

**PQL = 30-day sustained usage AND production-scale usage intensity.**

```
PQL = SUSTAINED_30D AND USAGE_INTENSITY
```

Seats drop out entirely — Ostrich Labs has no org object, so there's nothing to count. Domain clustering becomes a **priority flag**, not a gate, so the gmail third of the base doesn't get excluded from qualifying.

## Why not port "5 seats" as-is

- Seats are a proxy for "multiple humans depend on this." The borrowed rule works for the source company because seats are a first-party object there — real headcount, real switching cost.
- For a hosted vector DB, headcount isn't the signal of durability — **query volume and stored data are.** A single engineer running production RAG traffic through one API key is a stronger buyer than five people who each spun up a demo index once.
- Copying the seat threshold *number* ("5") without copying the *mechanism* it measures is a category error. Replace the mechanism, not just relabel it.

## Criterion 1 — SUSTAINED_30D

Match the source rule's intent (durability, not a one-time burst), not just account age:

```
SUSTAINED_30D = active (≥1 write or query call) on at least 1 day
                in each of the last 4 calendar weeks
```

Dead trial accounts that are just 30+ days old don't qualify. Accounts with a real, ongoing workload do.

## Criterion 2 — USAGE_INTENSITY

This is the seat replacement. Pick thresholds a solo side-project would rarely cross:

```
USAGE_INTENSITY = (stored_vectors ≥ N1)
               OR (queries_per_day_p7 ≥ N2)
               OR (distinct_api_keys ≥ 2)
```

- `distinct_api_keys ≥ 2` is the closest available proxy to "seats" — it means someone gave this to a second integration, environment, or teammate, without needing an org object.
- Don't invent N1/N2 from nothing. Pull the current 5,600 free accounts, plot the distribution of stored-vector count and QPS, and set N1/N2 at roughly the p85–p90 mark. That's today's ship-able number — see calibration note below.

## The gmail problem — demote domain, don't branch on it

Don't build a two-branch rule (corporate domain vs. free domain). Domain clustering is unreliable in **both directions**, not just for the gmail third:

- **False positive:** 5 strangers on gmail.com look like a team.
- **False negative:** a real team that all signs up with personal gmail addresses (common, especially early-stage) looks like 5 unrelated solos.

So don't gate on it at all. Use it only as a **priority/routing signal** once PQL is already true from usage:

```
if PQL and same_domain_signup_count(domain) >= 3 and domain not in FREE_EMAIL_BLOCKLIST:
    priority = "high"   # likely multi-person account, route to AE first
else:
    priority = "standard"
```

`FREE_EMAIL_BLOCKLIST` starter set: `gmail.com, googlemail.com, outlook.com, hotmail.com, live.com, yahoo.com, icloud.com, me.com, aol.com, protonmail.com, proton.me, gmx.com, mail.com, yandex.com, qq.com, 163.com, 126.com, naver.com, zoho.com, fastmail.com`. Use a maintained free-email-domain list rather than hand-extending this — it goes stale.

## Ship today, recalibrate in 30–60 days

- The "5 seats / 30 days" number was battle-tested *for their product*, not yours. Treat N1/N2 as a hypothesis, not a fact, even though the 30-day duration window is safe to copy as-is (time is the one dimension that transfers across products cleanly).
- As soon as you have 30–60 days of PQL-flagged accounts, pull actual free→paid conversion against the flag and re-cut N1/N2 to whatever percentile actually predicts conversion, rather than the arbitrary p85–p90 starting point.
- Log the raw metrics (`stored_vectors`, `queries_per_day_p7`, `distinct_api_keys`, `active_weeks_trailing_30d`) on every account regardless of whether they cross the line — you'll need the full distribution, not just the qualifiers, to recalibrate.