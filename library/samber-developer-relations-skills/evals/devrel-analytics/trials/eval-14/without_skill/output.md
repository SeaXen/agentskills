Before writing the copy: positioning can't rescue this plan, because the code is open source and anyone can read exactly what's captured. Four parts of the current design will get called out publicly, fast, no matter how the announcement is worded:

- **Full command line, verbatim.** CLI args routinely carry secrets — `--token=`, `--password=`, connection strings, API keys someone pasted for a one-off run. Shipping that to your servers (and then to Slack) turns a usage-analytics feature into a credential-exfiltration channel. This is the one that turns into a CVE writeup, not just an angry GitHub issue.
- **Raw working-directory path.** Absolute paths leak OS usernames, employer/client names, and internal project codenames (`/Users/jsmith/work/acme-corp-unreleased-merger-poc`). That's the kind of string a company will consider a leak of their own confidential info, not yours to collect.
- **"Hashed machine ID" ≠ anonymous.** A hash still gives you a stable per-machine identifier. Paired with free-text command lines and paths, you've built a pseudonymous profile, not an anonymous one — calling it "anonymous" in release notes is the line that gets screenshotted when someone reverse-engineers it, and now it's a credibility problem, not just a privacy one.
- **Default-on + "mention it in release notes."** Silently flipping a data-collection default and disclosing it in a paragraph nobody reads is the exact pattern behind the Audacity 2021 backlash (forked in a week), the 2016 Homebrew analytics blowup, and multiple similar incidents — all with tools far less popular than 30K installs. It reads as "opt-out and hope it's quiet," and technical communities specifically watch for that move.

The Slack-per-event pipe is a separate, internal problem worth flagging too: it puts raw (possibly sensitive) payloads in a chat tool with broad internal visibility and no query/retention discipline, and it doesn't scale past a few hundred events/day without becoming noise everyone mutes. Route to a real store; alert off aggregates on top of it.

## What I'd actually ship

- **Opt-in on upgrade, not opt-out.** First run after upgrading shows a one-time interactive notice; telemetry stays off until the user says yes. If leadership needs opt-out to hit adoption numbers, that's a legitimate call — but it has to be sold internally as "we're trading community trust for data volume," not smuggled through phrasing.
- **Respect `DO_NOT_TRACK=1`** (the cross-tool convention used by Next.js, Prisma, Netlify CLI, Gatsby) and auto-disable in CI (`CI=true`), same as those tools — CI runs would otherwise flood your data with non-representative noise anyway.
- **Never transmit raw argv or raw cwd.** Send an allow-listed subcommand name and flag names (no values), plus a coarse, locally-computed signal for "kind of project" (e.g., detected language/framework from a manifest file, not the path itself). If leadership wants "what kinds of projects," a category is the actual answer to that question — the raw path is not, it's a superset that happens to also contain the answer plus everyone's secrets.
- **Publish the exact schema** (a `TELEMETRY.md` with the literal JSON shape sent) and ship `brightmoor telemetry show-payload` so anyone can see exactly what would be sent before enabling it. This is the single highest-leverage trust move — it pre-empts the "someone greps the source and finds a mismatch" scenario entirely.
- **One-flag, one-env-var opt-out**, both documented in `--help`: `--no-telemetry` / `BRIGHTMOOR_TELEMETRY=0`.
- **Kill the per-event Slack webhook.** Batch to your own store; build a dashboard and alerting off aggregated data.

Everything below assumes this corrected design. I've written it so the language stays true even under scrutiny — that's the actual point of the exercise.

---

## Blog/community announcement

**Title: Brightmoor is adding optional, transparent usage analytics**

We're considering turning on anonymous usage analytics in Brightmoor to help us prioritize what to build next. Before we ship anything, here's exactly what that means, because we know "telemetry" is a loaded word in this community and we'd rather over-explain than have you find out from a packet capture.

**What we want to know:** which subcommands get used, roughly how often, and what kind of project Brightmoor typically runs against (language/framework), so we can prioritize features around real usage instead of guesses.

**What we will never collect:** the literal command line you typed, file paths, file contents, environment variables, or anything that could contain a secret or identify you personally.

**How it will work:**
- Off by default. You'll see a one-time prompt on first run after upgrading; nothing is sent until you opt in.
- `brightmoor telemetry show-payload` prints the exact JSON we'd send, any time, so you never have to take our word for it.
- `BRIGHTMOOR_TELEMETRY=0` or `--no-telemetry` disables it permanently, and we also respect the community `DO_NOT_TRACK` convention.
- Full schema is documented in [`TELEMETRY.md`](#) — every field, why we collect it, how long we keep it.
- The client-side code is in [`telemetry/`](#), same repo, same license, open to review and PRs.

**Why we're doing this at all:** 30,000+ installs and almost no signal on how the tool is actually used day to day. We'd rather ask than guess — and we'd rather ask properly than bury a default flip in a changelog line.

Feedback period: this is landing behind a flag in `vX.Y.0-beta` for two weeks before it's in a stable release. If something in the schema looks wrong to you, open an issue — this is the point where it's cheap to fix.

---

## CHANGELOG entry

```markdown
## [X.Y.0] - 2026-MM-DD
### Added
- Optional, opt-in anonymous usage analytics. Off by default; enable with
  `brightmoor telemetry enable`. Inspect the exact payload with
  `brightmoor telemetry show-payload` before turning it on.
  Full data schema: [TELEMETRY.md](./TELEMETRY.md). (#XXX)
```

---

## First-run CLI notice (shown once, on upgrade)

```
Brightmoor can send anonymous usage data (which commands you use, and
your project's detected language) to help us prioritize development.

It will NEVER send your command-line arguments, file paths, or file
contents. See exactly what's sent: brightmoor telemetry show-payload

Enable it?  [y/N]
You can change this later: brightmoor telemetry enable|disable
```

---

## FAQ (for docs / README)

**Is this on by default?** No. It stays off until you explicitly enable it.

**Can I see what's sent before I turn it on?** Yes — `brightmoor telemetry show-payload` prints the literal payload.

**Does it send my command-line arguments or file paths?** No. Never those.

**Is it really anonymous, or just pseudonymous?** We generate a random local ID (not tied to your machine hardware) and rotate it if you disable and re-enable. We're not calling it "anonymous" in the sense of unlinkable-across-sessions, because that would be inaccurate — see `TELEMETRY.md` for the precise guarantee.

**How do I turn it off?** `brightmoor telemetry disable`, `BRIGHTMOOR_TELEMETRY=0`, `--no-telemetry`, or set `DO_NOT_TRACK=1`.

**Does it run in CI?** No, disabled automatically when `CI` is set.

**Where's the code that sends this?** `telemetry/` in this repo — same license, open to review.

---

If leadership pushes back on opt-in specifically because it'll tank the adoption numbers they want — that's worth surfacing as an explicit tradeoff conversation (trust/goodwill vs. data volume), not something to resolve by writing better copy around an opt-out default.