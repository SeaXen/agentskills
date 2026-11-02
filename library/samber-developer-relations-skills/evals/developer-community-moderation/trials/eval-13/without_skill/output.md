## Big picture

This isn't a "how do we discipline Casper" problem — it's a **single-point-of-failure problem**. One person's uncalibrated communication style is currently the gate every newcomer's first experience has to pass through, and that gate is failing silently (you only know about the 2 who vanished; you don't know how many never posted a PR after reading one of his comments on someone else's). The fact that he's the same way with you two is actually useful information: it tells you this is a **blunt communication style, not newcomer-targeted hostility** — which changes what fixes will land. Coaching alone treats it as a behavior to correct; you also need a structural fix, because a lifelong communication pattern doesn't reliably change on a timeline that matches your contributor pipeline.

## Ranked menu

**🥇 1. Written, concrete review norms — short, in CONTRIBUTING.md, co-authored with Casper**
Not a Code of Conduct with an enforcement ladder — that's disproportionate for 3 people. A half-page "how we review PRs here" with 2-3 example comments (bad phrasing → better phrasing). Depersonalizes the ask: it's "the project's standard," not "you personally are rude." Have Casper help write it — he clearly cares about code quality, so channel that into a doc he co-owns and is more likely to hold himself to.
🟢 low effort, 🟢 low risk, addresses root cause.

**🥇 2. The 1:1 conversation your co-maintainer already offered — do it, but frame it as calibration, not correction**
Proceed with this. But brief your co-maintainer to anchor on concrete evidence ("here are the two comments, here's what happened after") rather than "be nicer" — vague feedback is exactly what someone with a blunt-by-default style will fail to act on, because it doesn't tell him what "nicer" cashes out to in his own words. Pair it with #1: give him the doc to react to, not an abstract ask.
🟢 low effort, 🟠 medium risk (could land badly if it feels like an ambush — make sure it's collaborative in tone).

**🥈 3. Structural buffer for first-time contributors**
GitHub already flags first-time contributors. Route those PRs so a second maintainer reviews first, or reviews alongside Casper and posts before/after his comment. This is your insurance policy — it protects newcomers regardless of whether the coaching sticks, and it doesn't require Casper to change anything to take effect immediately.
🟠 medium effort (some process overhead), 🟢 low risk, immediate protection.

**🥈 4. Track retention as a real metric, not a vibe**
After you act, check in ~2 months: are first-time PRs converting to second PRs? This tells you if #1-3 worked before you consider anything heavier. Without this you're guessing.
🟢 low effort, 🟢 low risk, no downside.

**🟠 5. Escalation held in reserve, not deployed now**
If nothing changes after a real attempt (not one conversation — a couple of months with the norms doc live), the next step is narrower: Casper stops being the default/first reviewer on newcomer PRs, full stop, not "try to be nicer." This is a structural demotion of one specific privilege, not a confrontation — much easier to actually execute than "have another hard conversation."
🟠 medium risk to the relationship — only worth it if 1-4 demonstrably failed.

**🔴 6. Do nothing / let it self-resolve**
Rejected. You already have evidence of cost (2 contributors gone) and zero evidence it self-corrects — "he's like that in every technical thread" describes a stable trait, not a phase.

**🔴 7. Formal Code of Conduct with enforcement / third-party mediation**
Overkill for 3 maintainers and one blunt-but-not-malicious reviewer. This is the tool for when there's real harm, harassment, or a dispute between parties who won't otherwise engage — none of which is true here. Bureaucracy here will read as hostile to Casper and burn goodwill you don't need to spend.

**🔴 8. Remove Casper from reviews entirely / push him out**
Nuclear, unjustified by what you've described, and expensive: he's written 40% of the codebase. Losing him over an unaddressed-but-addressable communication issue would be a much bigger loss to the project than the 2 contributors you're trying to protect. Keep this off the table unless #5 fails too.

## What I'd pick

Run **#1 + #2 + #3 together, now**, not sequentially — the doc gives the conversation something concrete to work from, and the buffer protects newcomers immediately without waiting to see if the conversation "took." Set a calendar reminder for **#4** at ~2 months. Keep **#5** as the explicit next step if retention doesn't improve, and say so openly to your co-maintainers now so nobody's surprised later. Don't touch #7 or #8 unless the pattern repeats after a real, structural attempt to fix it — right now you have an oblivious-but-fixable communication gap, not a conduct violation.