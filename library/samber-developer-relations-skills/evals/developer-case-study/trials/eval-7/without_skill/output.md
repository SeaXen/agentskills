## Results

**Build queue wait time down 73%**

Orbit Cargo's median wait time in the Buildkite queue dropped from 22 minutes to 6 minutes after the cutover — a 73% reduction. The before figure reflects the six weeks prior to cutover; the after figure reflects the three weeks since. Engineers get a runner assigned in a fraction of the time it used to take, cutting the dead time between "push" and "build actually starts."

**CI spend down $8,500/month**

Monthly CI spend fell from $18,400 to $9,900 in the first full month after the move — a 46% cut. Annualized at that run rate, that's roughly $102,000/year in projected savings, assuming the first month holds as a representative baseline.

**Support burden reportedly lighter**

"Our support tickets are way down," said [VP name/title], Orbit Cargo. This is a directional, self-reported observation — no ticket volume was tracked before or after, so it's included as color, not as a measured result.

---

### Flagging before this goes to marketing

Two things worth fixing before you ship "$102,000 saved annually" and "over 70% faster builds" as standalone headlines:

1. **Confounded savings.** In the same month as the cutover, Orbit Cargo also moved its runner fleet to Graviton and deleted two flaky test suites. Either of those alone would lower CI spend and reduce queue pressure — cheaper compute per minute, and fewer retried/duplicate runs eating into the queue. Right now the $8,500/month figure is being credited entirely to the cutover, but it's really the combined effect of three simultaneous changes. If this case study is meant to sell the cutover specifically, claiming the full $102K for it isn't supportable from this data and would be an easy claim for a technical reader (or a competitor) to pick apart. Safer: attribute the savings to "the move" as a bundle, as I did above, or get a rough split from Orbit Cargo's team (e.g., "Graviton alone accounts for ~X%").

2. **"Faster builds" overclaims scope.** The 22→6 minute number is *queue wait* — time spent waiting for a runner — not build execution time. "Over 70% faster builds" implies the builds themselves got faster, which you have no data on. "Cut build queue wait time by 73%" is the accurate, still-strong claim; I'd use that instead of "faster builds" in the headline.

Both numbers are strong on their own without rounding up or stretching scope — you don't need the inflated framing to make this a good case study.