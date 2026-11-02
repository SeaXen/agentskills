## Short answer: push back on four of the five, keep one

Your friend's instinct ("looks unserious") is about *perception*, but the fixes they suggested solve it by making the README describe a project that doesn't exist — a multi-maintainer, roadmapped, governed piece of infrastructure. For 200 lines maintained solo on weekends, that's not more serious, it's dishonest, and some of it actively creates the "ongoing" obligation you said you have zero appetite for.

Here's the reasoning per item, then the actual rewritten README.

- **Architecture section — skip, replace with a "Format" note.** A parse/re-emit crate for a fixed 128-bit spec has no architecture to speak of; a section with that title over one file reads as padding, which is *more* unserious than having none. What readers actually want to know is spec fidelity: does it validate Crockford Base32 strictly, does it reject overflow, is it byte-for-byte round-trip safe. That's three sentences, not a section with subheadings.

- **Roadmap — skip.** A roadmap is a promise. It invites "when's X shipping" issues on a crate you maintain when you feel like it. If you want to set expectations, one status line does it without committing to anything: "Feature-complete for its scope; not actively adding features."

- **Governance section — skip.** Governance describes how decisions get made among multiple people. You're one person. Writing a governance section for a solo project isn't more professional, it's inventing structure that will be visibly fake the moment someone reads CONTRIBUTORS and finds one name. The real question a contributor has — "will anyone look at my PR" — is one honest line under Contributing.

- **Security policy — skip the formal policy, add one honest line.** This is the one with actual downside. A `SECURITY.md` conventionally implies a disclosure process and a response-time SLA — exactly the standing obligation you're trying to avoid, and it can create a false sense of guarantee for anyone parsing untrusted ULID input in something sensitive. The real security surface here is narrow (malformed-input handling, panics, maybe timing of comparisons) and worth one sentence, not a policy document.

- **Demo GIF — this is the one worth doing, but not as a GIF.** A recorded terminal GIF is production overhead (recording, re-recording when the CLI output changes, hosting, file size in the repo) for a library whose entire value is visible in a four-line code snippet. A GIF is for tools where *behavior over time* is the point (a TUI, a build watcher). For "string in, struct out, string out," a copy-pasteable example already is the demo — make sure it's the very first thing under the one-liner, not buried after install instructions.

## The rewritten README

Placeholders where I don't have your actual API/type names (I don't have your current README or source — swap these for the real ones):

```markdown
# bitrune

A small Rust crate to parse and re-emit [ULID](https://github.com/ulid/spec) strings.

```rust
use bitrune::Ulid;

let id: Ulid = "01ARZ3NDEKTSV4RRFFQ69G5FAV".parse()?;
assert_eq!(id.to_string(), "01ARZ3NDEKTSV4RRFFQ69G5FAV");
```

## Install

```toml
[dependencies]
bitrune = "0.1"
```

## Format

Implements the [ULID spec](https://github.com/ulid/spec) as-is: 26-character
Crockford Base32, 48-bit timestamp + 80-bit randomness. Parsing rejects
malformed input (wrong length, invalid alphabet, timestamp overflow) instead
of silently truncating it.

## Status

Feature-complete for what it does — parse and re-emit ULID strings. Not
actively adding scope beyond that.

## Contributing

Solo-maintained, weekends-only. PRs and issues are welcome; there's no
guaranteed response time.

## Security

No known-unsafe code paths; parsing untrusted strings is the main attack
surface and is covered by the fuzz/property tests in `tests/`. Report
issues via GitHub issues — there's no formal disclosure SLA.

## License

<!-- your existing licence, unchanged -->
```

What changed from four sections to six: one line for spec fidelity (replaces "architecture"), one line for expectations (replaces "roadmap"), one line for contribution reality (replaces "governance"), one line for the actual security surface (replaces "security policy"). Nothing here promises anything you're not already doing on a random weekend.