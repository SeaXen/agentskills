**~200,000 developers worldwide are currently writing embedded firmware in Rust** (plausible range: 150,000–350,000).

**How I got there** (Fermi estimate, not a directly published stat — nobody publishes this number):
- Total Rust developer population: ~2.8–3.7M worldwide (Rust Foundation / SlashData estimates)
- Share of Rust developers who report embedded/IoT as a use case: ~8–10% (Rust Foundation's annual "State of Rust" survey, where respondents can select multiple use-case categories)
- 2.8–3.7M × 8–10% ≈ 220,000–370,000, cross-checked against a bottom-up route (embedded.com/AspenCore's estimated ~2–3M global embedded/firmware engineers, of whom recent Embedded Markets Studies put Rust usage at roughly 6–8% → ~150,000–240,000). The two approaches converge in the 150K–350K band, so I'd anchor the headline at **~200,000**.

**Don't use your two anchor numbers directly — they don't answer this question:**
- RedMonk's #19 is an ordinal rank (derived from GitHub pull requests + Stack Overflow tags), not a percentage or headcount — you can't back out a developer count from a rank position.
- Octoverse's ~100M is *cumulative registered GitHub accounts* (students, bots, dormant accounts, duplicates all included), not active professional developers. Using it as the "developer population" base would overstate everything downstream by roughly 3–4x versus the ~28–47M active-developer estimates (SlashData/Evans Data) that survey-based percentages are actually calibrated against.

**One honest caveat for the deck:** this is a synthesized estimate from survey data (Rust Foundation, SlashData, embedded.com/AspenCore), built from training knowledge — I didn't have live web access this session to pull the latest editions and verify current figures. If a board member is likely to probe methodology, worth a 5-minute sanity check against the newest Rust Foundation survey and embedded.com Embedded Markets Study before Thursday. Say the word and I'll re-run it with live sources once search access is available.