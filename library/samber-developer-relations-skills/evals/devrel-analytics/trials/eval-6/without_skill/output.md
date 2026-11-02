**Short answer: risky as written. Fix it before Thursday.**

The problem isn't the number — it's the source. "Below the industry standard of 80%" states a hard fact with no attribution. Your head of data will ask "whose standard? Which report, which vendor, which cohort?" If you can't answer with a citation on the spot, the line reads as a number invented to create urgency — and once one figure in the deck looks manufactured, they'll start doubting the others, including the 74% and the 89%.

Two paths, pick one:

**If the 80% figure is real** (a published benchmark, a vendor SLA, an industry report), cite it inline: "below the industry benchmark of 80% (source: [X], 2026)." A specific, attributed source is credible. A bare assertion is not.

**If it's a number you picked to make the point land**, drop it. You don't need it. You already have a stronger, unimpeachable case: your own coverage fell from 89% to 74% since June — a 15-point drop, measured by your own system, undeniable. An external comparison is a crutch for a story that doesn't need one. Strunk's rule applies directly here: omit needless words, and don't put a claim in the room that you can't defend if challenged.

**What to put next to the number**, regardless of which path you take:

1. **The trend, not just the two endpoints.** A line or sparkline from June to now — monthly if you have it. A drop shown as a slope reads as "something broke" far more convincingly than two isolated percentages.
2. **What "coverage" costs in concrete terms.** Convert the 15-point gap into something the room feels: X thousand joins failing, Y downstream reports/dashboards affected, or Z% of records now unattributable. "74%" is abstract; "12,000 joins a day silently dropping" is not.
3. **Root cause, even preliminary.** What changed between June and now — a schema change, a tracking break, a migration, an upstream vendor change? If you don't know yet, say "root cause under investigation, findings by [date]" rather than leaving a gap. A head of data will ask "why" before "how do we fix it."
4. **Remediation plan with an owner and a date.** Since the whole point of the slide is to make the web team take it seriously, the actionable ask belongs right next to the number: who owns the fix, what the fix is, and when coverage should recover — ideally a target date and a target percentage (e.g., "back to 90%+ by [date]").

One line of prose to consider for the slide itself:

> "Join coverage has fallen from 89% (June) to 74% today. Root cause: [X]. Fix owned by [team], target: back above 90% by [date]."

That's concrete, sourced entirely from your own data, and gives the head of data everything they'll ask for in the same breath: what happened, why, and what's being done — without leaning on an external number you'd have to defend.