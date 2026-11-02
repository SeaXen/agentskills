Recognize the pattern first: patient contributor, 6-7 months, high volume of legitimate merged work, unusually responsive, then a push for irreversible elevated access (publish rights + your personal GPG key), timed against an external deadline that isn't yours. This is structurally identical to the xz-utils/Jia Tan backdoor (2024) — not proof ferrous_owl is malicious, but proof the *pattern itself* carries risk independent of their intent. Treat it as a process problem, not a character judgment about them.

🔴 **Do not send the GPG private key. Ever, to anyone, over any channel.** A private key isn't a permission you grant — it's a secret you can no longer fully revoke once it's left your machine. If you ever need to "undo" it, you're rotating keys and re-signing history, not flipping a switch back.

🔴 **Do not hand over direct PyPI account credentials or an unscoped token.** You don't need to, and doing so makes ferrous_owl a single point of failure exactly like you are now — you'd just be trading your bus-factor-1 for theirs.

## What actually solves their stated problem, without the risk

They say they need publish rights to ship 4.0. That's solvable without any key handoff:

- ✅ **Set up PyPI Trusted Publishing** (OIDC from GitHub Actions) this week. ~1 hour of work. Once configured, releases are cut by pushing a tag / running a workflow — no long-lived API token or GPG key needs to exist in anyone's hands at all. This is the single highest-leverage move here: it removes the reason they need your secrets.
- ✅ **Add ferrous_owl as a GitHub "Maintainer" with merge rights now.** That alone unblocks the 340-issue backlog and most of the day-to-day burden you're drowning in. It's revocable with one click, unlike a key.
- ✅ **Gate the actual attack surface, not normal PRs, with required 2-person review**: GitHub Actions workflows, `pyproject.toml`/`setup.py`, `MANIFEST.in`, build/packaging scripts, release tooling. (This is exactly where the xz backdoor was smuggled — in autotools/build-system changes and binary test blobs, not the readable C source.) Regular bugfix PRs from a trusted contributor don't need this scrutiny; anything touching how a release gets built and signed does.
- ⚠️ If you still want artifacts GPG-signed, keep signing on a key only you (or a small custodian group) hold — a release-scoped subkey you can revoke independently of your primary key, never your primary key itself.

## Don't go from bus-factor-1 to bus-factor-1

Handing everything to one person "so you can walk away" recreates the exact fragility you have now, just with someone unverified. Recruit 2-3 co-maintainers, not one savior. With 900 dependent projects, you likely have several long-time users or contributors from that install base who'd take a maintainer role if asked directly. Distribute trust; don't relocate it.

## Verify identity before any privilege escalation

Ask plainly, before granting anything beyond merge rights: real name, employer, why they're this invested. A genuine collaborator welcomes a video call. Evasiveness on basic questions is itself information — weigh it accordingly, but don't skip asking just because it feels awkward after 34 good PRs.

## Decouple from their deadline

"Ship 4.0 before SciPy" is their timeline pressure, not a constraint you owe anything to. Say it plainly to them: trusted publishing gets 4.0 shipped this week without you handing out secrets; governance changes (co-maintainers, key custody) happen on your timeline, not a conference's. Urgency toward a deadline is itself a lever worth being suspicious of, separate from whether they're acting in good faith.

## Get outside help — the stakes justify it

You're at 900 dependents and burned out; don't design maintainer succession alone under pressure.

- Python Packaging / PyPI security teams have direct experience with exactly this handoff scenario — ask them.
- OpenSSF and the PSF packaging group can advise on safe maintainer transitions for security-sensitive projects.
- Given this is scientific-instrument parsing (likely embedded in research pipelines), NumFOCUS or a similar scientific-Python fiscal sponsor may offer governance/maintainer support worth investigating regardless of this specific situation.

## This week, concretely

1. **Set up PyPI Trusted Publishing** — removes the actual reason they're asking for your key.
2. **Add ferrous_owl as GitHub Maintainer** (merge rights, not release/publish authority) — unblocks the backlog immediately.
3. **Message them directly**: "Trusted publishing means you won't need my key or PyPI creds to ship 4.0 — let's get that wired up this week. Separately, I want to talk about making you an official co-maintainer properly, with a couple other people too, not a single handoff." Reasonable collaborators respond well to this; it also naturally surfaces if someone's actual goal was the key/credentials specifically.
4. **Reach out to 2-3 other trusted users/contributors** about co-maintaining, so this isn't a single relationship either way.
5. **Require 2-reviewer sign-off** on anything touching CI, packaging, or release scripts going forward.

The exhaustion is real and the instinct to hand off is reasonable — the fix is distributing the load across a few verified people plus automation that removes the need for secret-sharing at all, not routing all of it through one seven-month-old relationship under deadline pressure.