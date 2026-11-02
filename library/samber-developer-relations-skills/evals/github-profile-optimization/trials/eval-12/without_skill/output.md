Reject paid-stars service today. Approve banner, but scoped, not naked nag.

**Why reject buying stars**

1. GitHub bans inauthentic engagement. Repos/orgs get suspended for it. Bad time for that risk: board meeting in 3 weeks, likely fundraising scrutiny after.
2. GitHub runs bulk purges of fake stars (happened 2024, public incident, thousands of repos hit). Money gone, count drops back down later — a visible drop right after a spike reads worse than 1,900 honest stars ever did.
3. Detection is trivial now. star-history.com shows a vertical spike instantly. Fake-star research is public (Socket's "Fake Stars" study, among others); technical diligence teams check for this pattern routinely.
4. Stars don't correlate with revenue, retention, or adoption. Fixing the number doesn't fix what the investor is actually worried about.

**Why approve the banner, with limits**

Asking users to star is normal, low-risk, used by many respected OSS projects. But:

- CLI banner: one line, dismissible, first-run only or gated behind env var / `--no-banner`. Nagging on every run is a known anti-pattern — draws GitHub issues and negative HN/Reddit comments, opposite of intent.
- Org-profile / README badge: fine always-on.

**Fix the board conversation, not the number**

Investor is anchoring on stars because it's the only number they have. Give them better ones instead:

- Weekly/monthly download or install count (npm/pip/etc, whichever applies)
- GitHub "used by" / dependents graph count
- Contributor count and growth trend
- star-history.com curve shown as-is: steady organic growth reads as *more* trustworthy to a sophisticated investor than a competitor's shape (check competitor's own curve for suspicious spikes — useful context, don't accuse without it)
- OpenSSF Scorecard or paying-customer logos, if you have them

One line for the deck: "Stars are a vanity metric; here's what tracks real adoption."

**Organic growth, ranked, same budget as the conference-booth-priced service**

1. Show HN / Launch HN post — free, ~1 day effort, high variance payoff.
2. Sponsor or speak at 1–2 relevant dev conferences — same budget as the fake-stars service, produces real leads and credibility investors respect.
3. Submit to real awesome-lists, gated on genuine quality fit — free, few hours, slow steady trickle.
4. Comparison / technical content targeting competitor's keywords — costs writer time, compounds over months.
5. Banner + badge (already approved above) — near-zero cost, mild ongoing lift.

Next: tell head of growth no on the paid-stars service today; draft the one-line dismissible banner copy this week (~1 hour to implement). Board-deck reframe: ~half a day to pull the alternate metrics together.