**Short answer: no — the "live, unnamed" part is the problem, not the writeup.**

The plan mixes two things that can't share a timeline: real-time narration of an active memory-safety bug, and calling it not-a-security-thing. Both together are worse than either alone.

**Why live-threading a heap overflow backfires, even unnamed:**
- Anyone can read a stack trace, crash input, or diff. You don't need the word "security" to recognize `EXIF` + heap corruption — that's one of the most fingerprinted bug classes there is (libexif, ImageMagick, exiftool all had public incidents from exactly this pattern).
- A public "hunt" thread posted before the fix ships is a play-by-play of an unpatched vuln to anyone scanning your repo/timeline — which security-motivated readers do.
- Intermediate commits during the week (repro cases, ASAN output, half-fixes) can leak more than the final writeup would.
- Meanwhile your 40k weekly-download users get *zero* signal to act on, because you're deliberately not naming it. You'd be maximizing attacker information and minimizing defender information — the opposite of what you want.

**The reporter matters too.** They privately disclosed to you, presumably expecting some form of coordinated handling. Turning their report into live public content without asking them first is a good way to make future reporters go elsewhere (or go public immediately instead of emailing you). Ask their disclosure preference and whether/how they want credit before you publish anything.

**What I'd do instead — same content, safer sequencing:**
1. Fix it privately this week. Don't narrate live.
2. Write real regression tests/fuzzing for this input class — heap overflows in parsers are easy to half-fix.
3. Ask the reporter how they want to be credited (or if they want anonymity).
4. Ship the patch with a proper advisory (GitHub Security Advisory, request a CVE) — plain description, affected versions, upgrade path. This is what actually protects your 40k downloads/week.
5. *Then* publish the "debugging diaries" writeup — full technical depth, exploit primitives, everything. Write it in the same day-by-day narrative voice as if it were live; nobody but you knows it wasn't.

You lose nothing narratively — a "here's the story of the gnarliest bug I've found in 8 months" post lands exactly the same whether it goes out live or the week after the patch. You just stop broadcasting an open vulnerability while it's still open.