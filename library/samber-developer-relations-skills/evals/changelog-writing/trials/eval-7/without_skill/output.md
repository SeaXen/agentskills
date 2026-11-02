No `CHANGELOG.md` has ever existed anywhere in this repository's git history — not at the root, not in any subdirectory, not even under `skill-wip/` (I checked, since that's excluded from this task anyway). The only changelog-*related* files in the whole repo are reference material about changelog writing as a topic (`skill-wip/developer-relations-skills/changelog-writing/...`, `skill-wip/memories/developer-relations-skills/changelog-*.md`), which are notes *about* the subject, not a project's actual release history — and they're off-limits for this task regardless.

So there's nothing here matching "43 releases since 2021, Keep a Changelog, now a library" — this repo (`example-repo`) is your affiliate/marketing skills tooling, not a versioned library with a release history.

That description fits one of your other repos much better — likely one of the Go libraries (`samber/lo`, `samber/do`, `samber/ro`, `samber/oops`, `samber/hot`, etc.) that actually ship SemVer releases. Could you point me at the right repo/path? I don't have access outside the current working directory, so if it's a different local checkout, either:

- tell me the absolute path and I'll open it there, or
- paste/attach the current `CHANGELOG.md` contents here.

Once I have the real file, I'll convert all 43 releases to [Common Changelog](https://common-changelog.org/) format in one consistent pass — collapsing `Deprecated`/`Security` into the appropriate `Changed`/`Fixed`-style entries per that spec, normalizing headings, and keeping the version/date history intact.