Splitting this into three independent decisions — one's fine, one's a real problem, one's a trust risk.

**Early access to v3 binaries + docs for $20+ sponsors — fine.** This is a well-worn, community-accepted OSS pattern (delayed open-source, sponsor-first releases). No issue with gating features/docs/binaries behind a sponsorship tier for a limited window.

**Holding back the two CVE patches to create urgency — don't.** This is qualitatively different from gating a feature, and it's the one part of this plan worth killing:

- A CVE means a known, exploitable vulnerability. Once a CVE ID exists, it can be visible in NVD/MITRE (even at "reserved" status) — meaning the *existence* of an unpatched hole in harborctl can become discoverable before you've shipped the fix to anyone who isn't paying.
- Every non-sponsor running harborctl in that window is a known-vulnerable install you *chose* to leave unpatched to drive signups. If one of them gets hit during that month, the story isn't "unfortunate incident" — it's "maintainer sat on a fix as a sales tactic," which is a different order of reputational and potentially legal exposure than a normal disclosure delay.
- If either CVE came in through a reporter or GitHub Security Advisory, there's usually an implicit or explicit expectation that you patch promptly once you have a fix — not that you sit on it for a monetization window. Coordinated-disclosure norms assume "fix ready → ship it," not "fix ready → queue it behind a paywall."
- It also undermines the actual pitch to sponsors: you want people paying because harborctl is good enough to fund, not because you engineered a security gap for everyone else.

Ship both CVE patches on your normal cadence, independent of the v3 embargo. Use non-security material (the new binaries, the docs site, maybe an early-access Discord/office-hours channel) as the entire sponsor incentive — that's plenty, and it's the version of this plan you can defend publicly without caveats.

**The 250 → "maybe 400 if it's going well" threshold — pick one number and hold it.** Moving the goalpost upward the moment it's working is the fastest way to teach your sponsor base that your public commitments are provisional. Sponsors at $20/mo who signed up believing "open to everyone at 250" watch that quietly become 400 will feel played, and it'll get posted about. Fix: commit to *either* a sponsor count *or* a hard date, not a squishy "whichever, we'll see" — e.g. "open to everyone at 250 sponsors, or 60 days after v3 ships, whichever comes first." Announce it once, publicly, and don't revise it after the fact even if momentum tempts you to.

**Net recommendation:** keep the sponsor-gated early access on v3 binaries/docs, drop the CVE-holdback entirely and ship those patches to everyone immediately, and lock the reopen trigger to a single fixed number or date before you announce anything.