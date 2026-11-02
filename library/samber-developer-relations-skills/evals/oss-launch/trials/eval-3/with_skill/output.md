## Tilde — readiness-gate sanity check

**Verdict: not "go" yet.** Not because the README is bad — because two of the claims in your message don't hold up, and most of the readiness gate hasn't been checked at all.

### The two claims that don't hold up

**"Well under the five-minute industry standard."** There is no industry standard — that number doesn't exist anywhere except as a self-set default this skill uses when a project hasn't stated its own budget. The number that actually matters is whatever *Tilde's own README* promises, explicitly or implicitly. If it doesn't state one, that's the real gap: nothing to pass or fail a cold run against. Add a line like "install to first log line: under 2 minutes" and you've turned a vague vibe into a testable claim — and one your own data (Priya) already supports.

**"That's in the go.mod so it's not really a gap."** This is the one to push back on hardest. The cold-run protocol treats "a version guessed" and "a missing prerequisite" as defects by definition, and it explicitly forbids the reader from asking the maintainer — the maintainer is supposed to watch silently. Priya broke that rule by pinging you. That's not a workaround, that's the protocol's failure signal firing exactly as designed. "It's discoverable if you open go.mod" is true of almost anything a README leaves out; it's not a defense, because a first-five-minutes reader isn't going to open go.mod before running `go install`. Fix is trivial: one Requirements/Prerequisites line near the top stating the Go version. Ship that before you post — it's minutes of work and it removes the one hesitation you already have hard evidence for.

One more thing worth naming: a single colleague's run, unlogged, isn't the pass condition. Priya already knows you and roughly what the project does — she's a friendlier read than the protocol's target (a stranger, representative of the target adopter, notes taken on every hesitation). It's a fine signal, not proof the gate is cleared. Doesn't block you, just don't lean on it as more than one data point.

### What "anything else" actually covers, and what I can't check from here

I don't have access to the Tilde repo (not in this workspace, and I didn't go searching GitHub without you pointing me at it), so I can only flag what's still open per the checklist — not verify it:

| Blocker | Status |
|---|---|
| Name/trademark clearance, domain, org, handles secured | Not mentioned — confirm before this goes anywhere public. 8-week lead time if not started. |
| License file present, matches README, deps allow it | Unconfirmed |
| Hygiene — no keys/tokens/internal hostnames anywhere in git history, not just current tree | Unconfirmed |
| Distribution — tagged release, published wherever Go CLIs get discovered (if anywhere beyond `go install`) | Unconfirmed |
| `SECURITY.md` with a private reporting channel someone actually watches | Unconfirmed |
| Contribution channel — issue tracker open, basic guidance present | Unconfirmed |
| Claims — anything in your announcement draft (benchmarks, "used in production," etc.) defensible | Unconfirmed — only relevant if you're making any |

None of these are things "the README is good" tells you anything about, and your message only touched install speed.

### Smallest next step

1. Add the Go-version line to the README (Requirements section) — the one real defect you have evidence for.
2. State the time budget explicitly if it's not already there.
3. Send me the repo (URL or local path) and I'll run the rest of the blocker list — license, hygiene, security contact, distribution — for a real go/no-go instead of a partial one.