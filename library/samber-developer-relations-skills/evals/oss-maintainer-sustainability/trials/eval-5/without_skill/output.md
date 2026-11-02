You don't have to delete anything tonight to make the issues tab stop reaching you. These steps take about 15 minutes. Account and module deletion can wait, and you can still do it later.

## Tonight: silence everything (reversible, about 15 min)

1. **Turn off notifications.** Go to GitHub, then Settings, then Notifications, and untick every email and web channel. On the repo, choose Watch, then Ignore.
2. **Mute your inbox.** Add a mail filter that sends `notifications@github.com` to a folder you never open.
3. **Limit who can interact.** Go to Settings, then Moderation options, then Interaction limits. Set a 6-month limit so only existing contributors can comment.
4. **Disable Issues and Discussions.** Go to the repo's Settings, then General, then Features, and untick both.
5. **Archive the repo.** Go to Settings, then Danger zone, then **Archive this repository**. It becomes read-only and the code stays downloadable.
6. **Close the laptop.** Everything else can wait for daylight.

## Why I'd hold off on deleting

- **Deleting the repo doesn't remove the module.** `proxy.golang.org` and pkg.go.dev keep serving it. The ~900 importers still resolve it through the proxy. Only direct or private-proxy fetches break.
- **Deleting the account releases your username.** Anyone can register it and publish a malicious `github.com/<you>/loomcastle` at a new tag. That puts a supply-chain risk on all ~900 dependents, and your name would be on it.
- **Account restoration isn't something to count on.** GitHub may allow recovery for a limited time. Don't plan around it.

An archived repo under a dormant account does what you want. Nobody can bother you, and nobody can hijack the path.

## If you still want out after a few days

Do these in order:

1. **Add a deprecation notice.** Put `// Deprecated: unmaintained, fork freely` directly above the `module` line in `go.mod`. Tag a new patch release, for example `v1.x.y+1`. Importers will see the notice in `go list -m -u`.
2. **Hand it over.** Post one short README note that says "looking for maintainers". Or transfer the repo to a volunteer or an org. This is the cleanest exit for a module with 900 dependents.
3. **Check the old tags.** Pre-release or broken tags get `retract` lines in `go.mod`.
4. **Keep the account.** Leave it empty, with notifications off. Don't delete it, so nobody can take the username.
5. **If you must remove the module from the Go index,** file a request through the form at go.dev/about under "Removing a module". It is slow and only granted in some cases.

## One more thing

Stress bad enough to wreck your sleep is a good reason to step back. Your doctor is right to flag it. A 900-dependent module is a real burden, and you're allowed to put it down. The archive-and-handover route lets you do that without leaving a mess behind you.

If tonight feels worse than stress, please call someone you trust or your local emergency or crisis line.

I can draft the README handover note, the deprecation comment, or a "maintainer wanted" post whenever you want. I'll keep each one to a few lines.