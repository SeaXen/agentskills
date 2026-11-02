No. CLA bot alone don't fix patent question.

**Why not:** CLA and license work in different directions.
- CLA = inbound. Contributor grants rights to project.
- License (MIT) = outbound. Project grants rights to user.

Insurer's legal ask about outbound: "can we use this code without patent risk." MIT text carry no patent clause at all — no grant, no defense clause. Adding CLA don't touch MIT text. Users still get bare MIT, same gap as today.

Kubernetes and friends use CLA/DCO **plus** Apache-2.0 license. Apache-2.0 has explicit patent grant (Section 3) and litigation-termination clause. CLA there just extends same grant to corporate contributions. CLA without Apache-2.0-style license = half the machine, missing the part that answers your contributor's question.

**Real fix, ranked:**

1. **Relicense to Apache-2.0** (recommend). Gives explicit patent grant to every user, going forward and retroactively once done. Direct answer to "has a patent grant."
2. **Dual-license MIT/Apache-2.0** (Rust-ecosystem style). Same patent grant, keeps MIT for users who prefer it. Slightly more doc overhead.
3. **Keep MIT, add CLA with patent language, skip license change.** Cheapest, but leaves outbound gap open. Legal depts that know what they're asking will not be satisfied — CLA text only binds contributor-to-project, not project-to-user.

Relicense needs consent from existing copyright holders. 11 contributors, 340 stars — light lift: email each, ask sign-off, or rewrite the rare holdout's lines.

Going forward, once license carries patent grant, a lightweight DCO (sign-off line, e.g. `probot-dco`) is enough. Full CLA bot is optics-heavy, not legally required for this problem.

Next: draft relicensing consent email, list your 11 contributors from `git shortlog -sne`, send it.