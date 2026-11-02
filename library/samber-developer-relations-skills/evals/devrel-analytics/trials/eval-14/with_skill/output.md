## Verdict up front

Two of the five things in this plan are not a positioning problem — they're a design problem. No release-notes copy, blog post, or FAQ makes them safe to ship, because they break the floor this skill sets for CLI telemetry specifically because a "surprise" of this shape has, repeatedly, cost real tools their community's trust. Fix the design first; the comms below only work once the design is honest.

Checking your plan against `references/surface-register.md`'s CLI/SDK floor and the SKILL's privacy gate:

| Your plan | Rule it hits | Verdict |
|---|---|---|
| Full command line | "Never send code, paths, or arguments" | **Breaks the floor** |
| Working directory path | "Never send code, paths, or arguments" | **Breaks the floor** |
| On by default | "Make it opt-out **at minimum**, with a visible first-run notice" | OK *if* paired with a real first-run notice — release notes alone doesn't satisfy "visible" |
| Hashed machine ID | "Keep PII out of properties (hashing is not consent)" | OK as an identifier, but hashing doesn't substitute for disclosure |
| Slack alert per event | "Aggregate anything person-level" | **Breaks the floor** |

Why the two "breaks the floor" items aren't negotiable, not just unpopular:

**Full command line.** CLI arguments are one of the most common places secrets leak — `--api-key=sk-live-...`, `--token=`, DB connection strings, S3 URLs with embedded credentials. You'd be building a pipeline that, by design, exfiltrates whatever secret a user typed on the command line to your servers and then broadcasts it to a Slack channel, on every invocation, forever. This isn't a hypothetical edge case — it's the default way secrets end up in shell history and process lists, which is exactly why every serious CLI telemetry implementation excludes it. Next.js's own telemetry (the cited floor-setter here) explicitly excludes "anything that could carry secrets (env vars, paths, file contents, logs)."

**Working directory path.** `/Users/jane.doe/clients/acme-litigation-prep` or `/home/msmith/internal/project-codename-layoffs` tells you someone's real name, their employer, sometimes a client's name or a confidential project codename — none of which the user consented to reveal to you, let alone to a Slack channel. This is the direct GDPR-sensitive-data problem: a path is not anonymized by being sent alongside a hashed machine ID.

**The Slack alert makes both of these worse, not incidental.** Turning an event stream into a live chat feed converts "aggregate usage telemetry" into "real-time surveillance of one person's terminal, visible to everyone in the channel." Slack retains and is searchable indefinitely, is easy to screenshot, and integrates outward (Zapier, exports) in ways you don't control. At 30k installs generating routine CLI usage, this is also just operationally unworkable — it's a spam channel, not a signal. There is no framing of "we alert on every command you run" that reads as anything other than surveillance to a developer audience, and this audience already blocks tracking at high rates (58% block GA on tech-heavy sites) — they will find this, and once one person posts a screenshot of your Slack channel receiving their laptop's directory names, the story is "Brightmoor spies on your terminal in real time," not "Brightmoor improved its telemetry."

## What to build instead

Re-derive this from what leadership actually needs, per the skill's decision-first rule — an event with no decision behind it gets deleted, not defended:

**Decision:** "which kinds of projects use Brightmoor" — presumably to prioritize integrations, docs, or feature investment.

That doesn't require cwd or argv. It requires a **closed-vocabulary project-type signal**, computed locally, never raw text:

```
brightmoor_run_completed
  command:        enum, closed list of documented subcommands (e.g. "build", "deploy", "test")
  project_kind:   enum, detected from known manifest markers (e.g. "node", "python", "go", "unknown")
  cli_version:    semver string
  os:             enum (linux/macos/windows)
  install_method: enum (brew/npm/curl/binary)
  anonymous_id:   sha256(machine_id), salted, never reversible to a real identifier
```

No free text, no path, no argv, no PII in any property (matches the taxonomy rule: closed enums, never free text — a free-text field is what turned the bad example in the reference template unusable within a quarter).

- `command` gives you real usage shape ("70% of invocations are `build`") without ever touching what the user typed after it.
- `project_kind` gives you the "what kind of projects" signal leadership wants, detected from something like the presence of `package.json`/`go.mod`/`requirements.txt` — never the directory name or path.
- Drop the Slack alert. Replace it with what every cited comparable actually does: a daily/weekly aggregate rollup, plus threshold-based anomaly alerts on the *aggregate* (e.g., "error rate crossed 5%"), never a per-event stream of one person's activity.

## How to position this to the community

Once the design matches the floor above, this becomes an easy, even trust-building story — companies have made this exact move (opt-out CLI telemetry) work publicly by being concrete about the limits rather than vague about the intent.

**1. First-run notice, not release notes.** Release notes are read by a fraction of your install base; a first-run notice is read by all of them. Print it once, plainly:

> Brightmoor now collects anonymous usage data (command name, project type, OS, version) to help us prioritize development. No file paths, command arguments, or code are ever collected. Disable anytime with `BRIGHTMOOR_TELEMETRY=0` or `brightmoor telemetry disable`. Details: <docs link>

**2. A docs page that says exactly what is and isn't sent** — the property registry above, verbatim, as a table. "Exactly what is sent" is the specific bar this skill sets, and a table that a skeptical reader can audit in ten seconds is what discharges it. Explicitly list what you *don't* collect (paths, arguments, file contents, env vars) — the negative list is what actually earns trust, because it's checkable.

**3. A documented disable path**, one command and one env var, both mentioned in the same breath as the announcement — never "enabled by default, disable instructions buried three pages deep."

**4. Anchor the release notes to a credible external bar**, so the community isn't asked to trust you on vibes: "modeled on Next.js's CLI telemetry" is a real, checkable claim, and Next.js is a well-known example of opt-out telemetry that didn't blow up specifically because its scope is this narrow. If you want a stricter, higher-trust model later, Go's own toolchain telemetry (`golang.org/x/telemetry`) is opt-in with publicly reviewed counters — worth citing as the ceiling you could grow into, not the floor you're shipping now.

**5. Ship it as a minor version, but call the default-on change out as its own changelog entry**, not folded into a bullet list with unrelated features — a default-on data-collection change is the one line in a release most likely to be read as a breach of faith if it's found rather than announced.

The one-sentence version to hold onto while you write any of this: a telemetry surprise costs more community trust than the data is worth — and command lines, working directories, and a live Slack feed of both are exactly the shape of surprise that gets found and screenshotted.