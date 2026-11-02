## Launch HN vs. Show HN

Not actually your choice. **Launch HN is YC-only and editorially curated** — startups apply, staff select within two weeks, one per startup. Raising $6M and having a Series A doesn't unlock it; only YC batch membership does. Unless Sablefish went through YC, Launch HN isn't on the table, so there's nothing to weigh against Show HN.

⚠️ Also worth correcting before you rely on it: **830 karma buys no ranking advantage.** The "500+ karma = more initial trust" claim circulating in launch guides is wrong — 500 is the downvote threshold, unrelated to ranking. What your account *does* buy you is escaping the extra scrutiny HN applies to brand-new accounts, since a 2014 account with real history reads as a genuine person rather than a launch-day sock puppet. That's a real (if smaller) benefit — just not the mechanism you were counting on.

**Go with Show HN.**

## Timing: drop 9am ET Tuesday

"9am ET Tuesday" is the same category of folklore as the karma claim — HN publishes no first-party guidance on posting hour, and hardcoded US-morning windows in launch guides are invented. Tuesday itself is fine (mid-week, standard advice). The hour is wrong for you specifically.

Ranking divides points by a power of elapsed time, so the engagement your post gets in its first hour or two decides whether it survives, not total daily HN traffic. If your users are almost entirely in Germany and the Netherlands, the people who'll actually recognize the problem, comment intelligently, and upvote *because they mean it* are asleep or eating breakfast at 9am ET (3pm CEST) — you'd be posting into their late afternoon, after most of the workday's attention is already spent elsewhere.

**Post Tuesday, 08:00–09:00 CEST instead** (02:00–03:00 ET) — the start of the DACH/Benelux workday, when your real audience is fresh and scanning HN over coffee. Trade-off to accept explicitly: total HN traffic is thinner at that clock hour because the US is asleep, so raw pageviews in hour one will be lower than a US-prime-time post. That's the right trade for you — a smaller pool that's disproportionately your actual users beats a bigger pool that mostly isn't.

Staffing consequence: whoever posts the first comment and stays in the thread for the next several hours needs to be awake at 8am CEST. Assign that to an EU-based team member as DRI, not whoever happens to be senior.

If nobody can reliably staff that early, the fallback compromise is **~13:00 CEST / 07:00 ET** — still inside the European workday, and catches US East Coast waking up. Worse than the first option for your core audience, better than 9am ET.

## Your draft title has two violations

> "Show HN: Sablefish - the fastest open-source columnar cache, from the team that raised $6M"

| | |
|---|---|
| **Weak (yours)** | "Show HN: Sablefish - the fastest open-source columnar cache, from the team that raised $6M" |
| **Problem 1** | "Fastest" is a bare superlative — moderators rewrite these, and HN's own posting guidance to founders explicitly bans them. |
| **Problem 2** | "From the team that raised $6M" turns this into a funding announcement, not a Show. The reference case for this exact mistake: *"Show HN: Our startup raised $4M to fix logging"* is the canonical weak example — a funding announcement is not a Show HN and doesn't belong in the title at all. |

**Strong pattern:** `Show HN: <Name> – <plain description of what it does>`. Swap the superlative for a measurable, verifiable property with a link to the method — same fix as "fastest HTTP router" → "zero allocations on the hot path, benchmarks in `bench/`."

I don't have the actual mechanism you'd stand behind (what makes it fast — mmap layout, SIMD scans, a specific eviction policy, zero-copy reads?), so pick the real one and slot it in:

```
Show HN: Sablefish – an open-source columnar cache with <specific mechanism>
```

If you have nothing more specific than "columnar cache" to put there yet, the honest fallback is:

```
Show HN: Sablefish – an open-source columnar cache
```

Plain, undersells nothing, and won't get flagged. Whatever you pick, if the title implies a speed claim anywhere, the post body needs a reproducible benchmark command — a claim with no method attached is exactly what gets you discredited in the first ten comments on this audience.

**Where the $6M *does* belong:** not the title, in the announcement body, stated plainly and once — e.g. *"Sablefish is built and maintained by [company]. The core is [license] and stays that way; [commercial boundary if any]."* Readers accept a business model stated up front; they don't forgive finding it after they've adopted something they thought was purely community-run. If nothing is paid or planned to be paid, say that too — it's the disclosure that matters, not the funding number.