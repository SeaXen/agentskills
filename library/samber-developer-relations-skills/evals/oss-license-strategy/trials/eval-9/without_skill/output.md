## License recommendation for Bellrook

**Split license across the repo: Apache-2.0 for the Go client library, Business Source License 1.1 (BUSL) for the scheduler server.** Same repo, two `LICENSE` files, clearly scoped by directory. This is the standard shape for infra companies with a "library people embed + server people might host" structure (HashiCorp pre-2023, Sentry, CockroachDB all landed here).

### Why not one license for everything

- **Pure Apache-2.0/MIT everywhere** maximizes adoption and reads cleanest for the fundraise PR, but gives a cloud vendor (or anyone) a free path to offer "Bellrook Cloud" before you do. You're 12 months from your own hosted version — don't hand competitors a head start with your own code.
- **AGPL everywhere** is the wrong tool. It doesn't actually block a well-resourced cloud vendor (their legal team isolates the AGPL-covered piece and complies with source disclosure, nothing else), and it scares off the exact enterprise infra buyers you want embedding the client library — many companies have blanket AGPL-ban policies. Copyleft solves a different problem than the one you have.
- **SSPL everywhere** (MongoDB/Elastic's route) blocks hosting risk but is not OSI-approved, triggers "this isn't real open source" backlash on HN/Twitter, and several Linux distros and package indexes refuse to redistribute SSPL code. Bad optics for a fundraise announcement built on an open-source narrative.

### The split, specifically

- **`/client` (or wherever the Go library lives) → Apache-2.0.** Permissive, patent grant included (matters — infra buyers ask about patent trolls), embeddable in anyone's codebase with no friction. This is the piece that drives adoption and is what you want widely forked/starred/imported.
- **`/server` (the scheduler) → BUSL 1.1.** Source available, modifiable, free to self-host in production — just not offerable as a hosted/managed service to third parties without a commercial agreement with you. Set the **Additional Use Grant** to: "any use except providing a competing hosted/managed scheduler service." Set the **Change Date** 3–4 years out, converting automatically to Apache-2.0 — comfortably past your 12-month commercial launch plus runway to establish the hosted product before the code goes fully permissive.
- Use **FSL** instead of BUSL if you want simpler, shorter license text and a 2-year embargo instead of BUSL's typical 4 — functionally similar, newer, less legal precedent but easier to read. Ask the law firm which they're faster reviewing; either is defensible.

### Do this before the 3 friends' PRs turn into a bigger problem

Put a **CLA in place this week**, before merging anything else. Once external contributions accumulate without clean IP assignment, changing license terms later (tightening the Additional Use Grant, extending the change date, ever going fully proprietary on a component) requires tracking down every past contributor for consent — a mess you can avoid entirely by requiring sign-off now.

- Use a standard Apache-style Individual CLA (e.g., via CLA Assistant or the CNCF's EasyCLA template) — don't draft from scratch.
- Retroactively ask the 3 friends to sign it. Low friction since they're friends and it's 3 PRs, not 300.
- Have the **law firm on retainer review the CLA text and the BUSL Additional Use Grant language now** — this is exactly the kind of one-time document review outside counsel is for, and it doesn't need to wait for the January in-house hire.
- Brief the in-house counsel on this decision as onboarding material in January; the ongoing job from there is standard OSS governance (trademark policy, CLA enforcement at scale), not re-litigating the license.

### Repo mechanics for the 3-week deadline

- Root `LICENSE` file: short notice explaining the split, pointing to `client/LICENSE` (Apache-2.0) and `server/LICENSE` (BUSL-1.1).
- SPDX license headers per file (`// SPDX-License-Identifier: Apache-2.0` / `BUSL-1.1`) — cheap to script, removes any ambiguity about which license covers a given file if directories get reorganized later.
- Register the **Bellrook name/logo as a trademark separately from the code license** — standard in BUSL/FSL templates already (they don't grant trademark rights), but say so explicitly in your README so nobody assumes a fork can call itself "Bellrook."

### Framing for the announcement

Call the server **"source-available,"** not "open source" — BUSL isn't OSI-approved, and calling it open source invites the exact "is this really open source" pile-on that hit MongoDB and Elastic. Lead the PR narrative with the **Apache-2.0 client library** as the real open-source piece; frame the server's BUSL license as "source-available, converts to Apache-2.0 in N years, free to self-host, just not to resell as a hosted service" — that's a defensible, increasingly normal story in infra (HashiCorp told it for years before the IBM acquisition changed the calculus), and ex-infra-engineer audiences will recognize and generally accept it.