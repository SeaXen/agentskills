**Your premise has a gap.** Spec-wise, 0.x promises nothing. But you have four known production users and 60k downloads a month. The skill's failure-modes table flags this exact line, "We're 0.x, so we can break anything". "1.0 when it's stable" is the ZeroVer failure state.

- **PyPI gives no protection.** `~=0.9` accepts any 0.x from 0.9 up, so pip users get 0.10 unless you tell them how to pin.
- **Your two complaints show the public surface.** The default serializer (0.8) and an exception class (0.7) are defaults and error types. The skill counts both as breaking, and 0.10 changes the same kinds of things.
- **The ack-mode change is the risky one.** It has no signature change, and on a queue client it can cause redeliveries or stalled messages. Ship a deprecation warning in 0.9.3 and keep `Consumer = Subscriber` as an alias for one minor. If that is too much work for 3 hours a month, at least put it in the changelog as BREAKING.

Next to the paragraph, I'd write the full `RELEASES.md` (the skill's template) and add this paragraph to the README as a link to it.

## README paragraph

```markdown
## Versioning

loomreach is pre-1.0 and uses `0.MINOR.PATCH`. The MINOR number is the breaking
digit: `0.x.PATCH` releases only contain compatible fixes, while any `0.MINOR`
release may break the public API. Breaking changes are marked BREAKING in the
changelog and, where we can, deprecated with a warning one minor earlier.

The public API is the names exported from `loomreach`, their documented
behaviour, default values (serializer, ack mode), and the exception classes.
Underscore-prefixed names, undocumented behaviour and log text are not covered.

pip's `~=0.9` accepts every later `0.x`, so pin to the minor you tested:
`loomreach~=0.9.2` (or `==0.9.2`) and upgrade deliberately. Only the latest
`0.MINOR` receives fixes.

We will release 1.0 once the public API has gone two consecutive minors without a
breaking change. From 1.0, breaking changes ship only in a major version.
```

**Choices for you:**
- **The 1.0 rule.** "Two consecutive minors with no break" is my proposal. Swap in your own criterion, but keep it testable. 0.10 already bundles the two renames and defaults you wanted to fix, so it could plausibly be the last breaking minor.
- **Support window.** "Only the latest minor" is the safe promise at 3 hours a month. A security-only window on 0.9 would need the skill's capacity arithmetic first, and I don't have your fixes-per-year count.
- **Unanswered interview questions.** I haven't asked who the four companies are, who holds publish rights, or which Python versions you support. Those answers would feed a runtime-floor section in the full `RELEASES.md`.