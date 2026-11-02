Semver does allow it. The risk is the ack default, not the rename. Your two earlier complaints were loud failures: an exception name stopped matching, or the serializer output changed. Auto to manual ack is silent. Code that never calls `ack()` will stop acknowledging, so messages redeliver or pile up in production with no error. Four companies you know about run it, and there are likely more you don't.

Three cheap changes before 0.10 (about an hour total):
- **Keep the old name:** ship `Consumer` as an alias of `Subscriber` that raises `DeprecationWarning`, and remove it in 0.11.
- **Warn first:** in 0.9.3, warn when `ack_mode` isn't set explicitly ("default changes to manual in 0.10").
- **Fail loudly:** in 0.10, either raise if `ack_mode` is omitted, or keep the warning for one more release.

Here is the paragraph. It states what you can actually promise at 3 hours a month, and it gives 1.0 a checkable condition instead of "when it's stable".

```markdown
## Versioning

loomreach is pre-1.0, so the API is not frozen. Breaking changes can land in any
minor release (0.9 → 0.10), never in a patch release (0.9.2 → 0.9.3). Every
breaking change is listed under "Breaking" in the [CHANGELOG](CHANGELOG.md),
and where practical the old behavior warns for one minor release before it
changes. I maintain this project alone, so I can't promise long-term support
for old minor versions: pin to a minor range, for example
`loomreach>=0.9,<0.10`, and read the changelog before you raise it.

We'll release 1.0 when the public API (client, consumer/subscriber, ack
handling, serializers, exceptions) has gone two consecutive minor releases
without a breaking change. From 1.0, breaking changes only come with a major
version.
```

Adjust the 1.0 criterion if you prefer another one, such as a fixed API list or a date. Any concrete condition beats "stable".