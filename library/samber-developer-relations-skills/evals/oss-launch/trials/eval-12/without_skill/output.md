Plan is right in spirit. Four gaps close before you post or push:

1. **Bind-address fix alone may not be enough.** Does the admin API have its own auth, or does it rely on "nobody can reach 0.0.0.0 anyway"? If auth is missing, localhost-only is a mitigation, not a fix — anyone with shell/container access on that host still walks in. Say so in the patch notes either way.
2. **Main isn't what users run.** Anyone who already deployed with the old default is still exposed after you merge, until they pull a new build. Tag a release right after merge, don't just land it on main and move on.
3. **Don't skip your own gates under pressure.** Run existing tests/linter before commit, no `--no-verify`. A rushed security patch that breaks something else is a worse HN thread than this one.
4. **Reply after the fix commit exists**, not before — link the actual commit/tag so the thread can verify, not just take your word.

Order for the next 20 minutes:

1. Patch default bind → `127.0.0.1`, keep override for people who *intentionally* want it exposed (env var, explicit, loud warning logged if set to `0.0.0.0`).
2. Run tests, commit, push, tag a patch release (e.g. `v0.x.y`).
3. Post the HN reply (below), linking the commit/tag.
4. Add the README note (below).
5. After the rush: file a GitHub Security Advisory for this — gets it a CVE, shows up in Dependabot-style scanners for anyone who forked/deployed it. Doesn't block steps 1–4.

Also worth 5 minutes if you have any telemetry on the hosted demo: check admin-route hits in logs before this thread existed. Someone finding it in a Show HN thread after 4 hours means it's easy to find — check it wasn't found earlier too.

---

**HN reply (draft):**

> You're right, and thanks for posting it straight instead of sitting on it. The default config bound the admin API to 0.0.0.0, so anyone running Prismvault with defaults on a host with a public interface had it reachable, not just on localhost.
>
> Fix: default admin bind is now 127.0.0.1. Exposing it beyond localhost now requires an explicit opt-in, and we log a warning if it's set that way. Pushed here: [commit/tag link], out in v0.x.y.
>
> If you already deployed with the old default: upgrading isn't enough on its own, restart the service on the new config, and firewall the admin port in the meantime if you can't upgrade right now.
>
> Filing a security advisory for this so it's tracked properly rather than just a changelog line. Appreciate the clear writeup — this is exactly how it should go.

**README note (draft):**

```
### Security notice — 2026-09-24
Versions before vX.Y.Z bound the admin API to 0.0.0.0 by default (reachable on
any network interface, not just localhost). Upgrade to vX.Y.Z+, or set
`admin.bind: 127.0.0.1` explicitly if you're on an older version. Details: GHSA-xxxx.
```

Next: change the default bind value and run your test suite — that's the step everything else depends on.