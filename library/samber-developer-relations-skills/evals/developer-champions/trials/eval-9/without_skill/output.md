Short answer: it's a reasonable *starting skeleton*, not something to adopt as-is. It's also a fairly generic template — those exact weights (content +25, top-decile usage +20, answering questions +20, general activity +15, mentions +10, feature requests +10) show up as a common example rubric in champion-program playbooks, so treat it as a skeleton to calibrate, not a validated model someone battle-tested for a program like yours.

**Problems with adopting it as written:**

- **It rewards volume, not quality or impact.** A rushed one-line answer and a deeply useful troubleshooting thread both bank +20. A mediocre blog post and a widely-shared technical deep-dive both bank +25. If any of these are per-instance (not one-time category flags), someone who's merely prolific will out-score someone who made one high-value contribution.

- **No recency decay.** All six signals read as lifetime totals. Someone who was active 18 months ago and silent since scores identically to someone active this week. A Guides program needs people who are engaged *now*.

- **Two categories double-count the same behavior.** "Answering other people's questions" (+20) and "general community activity" (+15) mostly measure the same underlying thing — being chatty/present in the community. That inflates active-but-shallow participants relative to people who contribute less often but more substantively.

- **It conflates "valuable user" with "wants a public mentoring role."** Top-decile product usage tells you someone is engaged, not that they want to be a public-facing Guide, or that they have the teaching/communication temperament for it. That gap matters most for exactly this kind of role.

- **The weighting doesn't match what a Guides program actually needs.** Content creation is the single highest-weighted signal, but the core job of a "Guide" is presumably helping other users directly, not blogging. If that's right, "answering questions" and mentoring aptitude should probably outweigh "content created," not the reverse. Re-derive weights from what Guides actually do, don't inherit a generic advocate-identification rubric wholesale.

- **No conduct/behavior gate.** Nothing here subtracts for hostile, self-promotional, or off-brand behavior. A top scorer could still be the wrong person to put in a public role representing you.

- **Some signals are easy to game.** Submitting many low-effort feature requests hoping a few land, or racking up "activity" via message volume, both pay off under this model as written.

- **No normalization or time window.** "Top-decile usage" relative to whom — all users, ever? Long-tenured users get a structural advantage over promising newer members, and you risk clustering champions in one company or use case if that segment dominates activity.

- **No threshold or decision rule.** The score gives you a rank order, not a cutoff for "this person becomes a Guide," and doesn't specify all-time cumulative vs. a trailing window (e.g., last 90 days) — which changes who shows up at the top substantially.

**What I'd change before shipping it:**

1. Add a trailing window (e.g., 90 days) or decay factor, so the score reflects current engagement, not historical peak.
2. Fold "answers questions" and "general activity" into one signal, or reweight so mentoring behavior (answering, helping) outweighs content creation — since that's the actual Guides job.
3. Cap or diminish returns per category (e.g., log-scale or capped count) so volume alone can't dominate.
4. Add a qualitative gate — a short human review pass for tone/conduct — before anyone with a high score gets invited, rather than auto-qualifying on score.
5. Use the score for **discovery/triage** (who do we look at) rather than as an automatic acceptance gate.