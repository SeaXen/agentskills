Refuse fixed biweekly cadence. Bad rule dressed as visibility hack.

**Why:**

- Skill catalog names this exact trap: "cadence theater — dependency bumps announced as features." Empty release becomes noise PR in every downstream repo, trains people to auto-merge or ignore your release feed — the one channel that reaches existing users direct.
- Adoption test for any channel: recurring cost, decay behavior, observable signal, kill date. Forced dep-bump release has no signal that moves — nobody adopts faster because you tagged a Tuesday. Channel with no signal is hobby, not channel.
- Capacity check: 3 hrs/month across 2 maintainers is already razor-thin. Self-set baseline caps total recurring channel cost at 60% of capacity. A mandatory biweekly release adds pure recurring tax for zero yield — exactly what "planning past capacity" warns against.
- Rule from this skill's release-cadence step: commit to a **max** interval ("fix lands within N weeks"), never a mandatory minimum. Second Friday no matter what is a minimum. Backwards.

**What to do instead:**

1. Put one line in README today: "Status: stable, maintained, low change rate." Costs 5 minutes. Fixes the actual fear — a registry reading silence as abandonment — without spending any of your 3 hours per month.
2. Batch dep bumps. Ship them together when they've piled up or a CVE forces it — not on a calendar.
3. Security fixes: out of band, fast, always. Never batched.
4. Save an actual cadence return for a real milestone — breaking change, 1.0, rewrite. That's the one thing worth spending awareness-channel hours on.

Next: add that README status line now, tell teammate the biweekly rule is refused and why.