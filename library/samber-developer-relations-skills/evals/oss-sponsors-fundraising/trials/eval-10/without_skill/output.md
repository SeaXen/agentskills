Here's the situation stripped down: money and fairness are pulling in opposite directions, but the two threads (new issue, stalled PR) don't actually need the same answer.

**On "can it jump the queue":** Don't silently bump it — that's a precedent you can't take back once other contributors notice, and it trains sponsors that pressure works better than process. But you also don't need to hide behind "everyone's equal" if you don't mean it. Give them the honest version: sponsors get faster *acknowledgment and triage*, not a skipped review or a promised merge date.

**On the PR:** This one isn't a queue problem — it's blocked on their side. Don't let it sit vague; hand them the exact fix needed so the ball is visibly in their court, not yours.

Here's a message that does both without either overpromising or sounding transactional:

---

Hey [name] — thanks for flagging both of these, and for your patience.

On the new issue: I can't promise a specific timeline over anyone else in the queue, but I'll triage it this week and let you know where it lands. If it's related to the PR you've got open, fixing that might actually be the faster path to resolving both at once.

Speaking of which — the PR's been stuck because it doesn't handle the Windows path case (e.g. hardcoded `/` separators instead of `filepath.Join`/`filepath.Separator`). That's the only thing blocking merge on my end. If you can patch that, I'll review and merge quickly — happy to point at the exact failing case if useful.

Really appreciate the continued support — it's a big part of what keeps this project going.

---

Why this framing: it's true, it doesn't create a "sponsors skip the line" precedent, and it quietly moves the PR — the thing actually in their control — forward before renewal conversations start. If you *do* want sponsors to get real priority (not just triage speed), make that an explicit, published tier so it's a stated benefit rather than a favor granted under renewal pressure — that's the difference between a policy and a payoff.