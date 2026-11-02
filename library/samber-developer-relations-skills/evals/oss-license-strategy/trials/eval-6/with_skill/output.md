**Biggest problem first: the opening claims something false.** SSPL is not OSI-approved open source — OSI reviewed and never approved it, precisely because of clauses like the one you're adopting. "100% open source and always will be" next to an SSPL announcement is a checkable-in-seconds contradiction. It will get called out publicly (Hacker News, Reddit, your own users) within hours, and the correction does more damage than the license change itself. Fix the copy, don't polish the claim.

Here's the rewrite, plus the community section.

---

## Quillstone 5.0: an update to our license

Starting with version 5.0, Quillstone's source moves from [current license — fill in] to the Server Side Public License (SSPL). SSPL is source-available, not OSI-approved open source, and we're saying that plainly rather than blurring it.

For nearly everyone using Quillstone today, nothing changes. You can still read the source, self-host it, modify it, and build your product on it, exactly as before. The one thing SSPL adds: if a company offers Quillstone as a hosted service to third parties, it must open-source the entire stack that runs that service.

We're making this change because [name the specific competitor/hyperscaler] resells Quillstone as a managed service without contributing anything back. That's revenue leaving the project that should be funding it. SSPL closes that gap.

## Why this is good for the community

- **Your rights don't change.** Reading, self-hosting, modifying, and shipping Quillstone in your own product all work exactly as they did yesterday.
- **It targets one specific behavior, not the community.** Only a company reselling Quillstone as a hosted service without giving back is affected — not you, not most contributors, not most companies building on top of it.
- **It protects the thing that funds development.** [Company]'s ability to keep shipping [specific things the community values — name 2–3] depends on that revenue existing instead of being captured by a reseller who contributes nothing.
- **The source stays visible.** Nothing moves behind a paywall or closes to inspection — SSPL still requires the source to be published, just with one more obligation attached to a narrow use case.

Don't claim this is "even more open" or frame it as a pure win — it's a trade-off (see checklist below), and a defensive one. Say what it does and stop there; the honesty is what survives scrutiny.

---

**Before this goes out Tuesday, confirm these with engineering/legal — not mine to answer for you:**

1. Fill in `[current license]` — what Quillstone ships under today.
2. Confirm every outside contributor whose code is still present has either agreed via a CLA that permits relicensing, or has been asked directly. Relicensing without that consent is a real legal exposure, not a copy problem.
3. Decide the version boundary explicitly: does 5.0 alone move to SSPL, do all future releases, and what happens to 4.x under the old license.
4. Expect a fork or an ecosystem drop as the normal reaction, not a crisis — MongoDB (SSPL), Elastic, Redis, and HashiCorp all relicensed away from permissive terms and each got forked (OpenSearch, Valkey, OpenTofu) or dropped from Linux distros (MongoDB from Debian/Fedora). Have a one-line internal response ready before you publish, not after.
5. Never say "open source" anywhere in the release notes, docs, or package metadata for 5.0 — say "source-available." Procurement teams and package registries filter on OSI approval directly.

Next: get #1 and #2 answered — everything else in the draft depends on those two facts being right before it goes out.